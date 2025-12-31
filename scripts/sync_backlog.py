import json
import subprocess
import os

def get_issues():
    try:
        cmd = ["gh", "issue", "list", "--json", "number,title,state,body,labels,milestone,assignees", "--limit", "100"]
        result = subprocess.run(cmd, capture_output=True, text=True, check=True)
        return json.loads(result.stdout)
    except Exception as e:
        print(f"Error fetching issues: {e}")
        return []

def format_labels(labels):
    if not labels:
        return ""
    return ", ".join([f"`{l['name']}`" for l in labels])

def format_assignees(assignees):
    if not assignees:
        return "-"
    return ", ".join([f"@{a['login']}" for a in assignees])

def generate_markdown(issues):
    md = "# Project Backlog - libbase\n\n"
    md += "This document is automatically synchronized with GitHub Issues. Last updated: " 
    md += subprocess.run(["date", "+%Y-%m-%d %H:%M:%S"], capture_output=True, text=True).stdout.strip() + "\n\n"
    
    # --- 1. MASTER ISSUE LIST (OVERVIEW) ---
    md += "## 📋 Master Issue List\n"
    md += "| # | Status | Title | Executor | Sprint | Milestone |\n"
    md += "| :--- | :--- | :--- | :--- | :--- | :--- |\n"
    for i in issues:
        status_icon = "🟢" if i['state'] == 'OPEN' else "✅"
        sprints = [l['name'].replace('Sprint: ', '') for l in i.get('labels', []) if l['name'].startswith('Sprint:')]
        sprint_str = ", ".join(sprints) if sprints else "-"
        milestone = i.get('milestone', {}).get('title', '-') if i.get('milestone') else "-"
        executors = format_assignees(i.get('assignees', []))
        issue_link = f"[#{i['number']}](https://github.com/The-Band-Solution/libbase/issues/{i['number']})"
        md += f"| {issue_link} | {status_icon} | {i['title']} | {executors} | {sprint_str} | {milestone} |\n"
    md += "\n---\n\n"

    # --- 2. WORKFLOW STATES ---
    md += "## 📂 Workflow States\n\n"
    for state in ['OPEN', 'CLOSED']:
        title = "🟢 In Progress / Todo" if state == 'OPEN' else "✅ Done / Released"
        items = [i for i in issues if i['state'] == state]
        md += f"### {title}\n"
        for i in items:
            executors = format_assignees(i.get('assignees', []))
            issue_link = f"[#{i['number']}](https://github.com/The-Band-Solution/libbase/issues/{i['number']})"
            md += f"- {issue_link} **{i['title']}** (Executor: {executors})\n"
        md += "\n"
    
    return md

def main():
    issues = get_issues()
    if not issues: return
    content = generate_markdown(issues)
    os.makedirs("docs", exist_ok=True)
    with open("docs/backlog.md", "w") as f:
        f.write(content)

if __name__ == "__main__":
    main()
