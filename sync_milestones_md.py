import os
import re

MILESTONES_DIR = os.path.join(os.path.dirname(__file__), 'milestones')
MILESTONES_MD = os.path.join(os.path.dirname(__file__), 'milestones.md')

def status_icon(status):
    if status and status.strip().lower() == 'done':
        return '✅'
    return '⏳'

def extract_title_status_from_file(md_path):
    title = None
    status = None
    with open(md_path, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    for i, line in enumerate(lines):
        if line.startswith('# Milestone Title:'):
            title = line.replace('# Milestone Title:', '').strip()
        if line.strip().startswith('## Status'):
            # Status is on the next non-empty line
            for j in range(i+1, len(lines)):
                status_line = lines[j].strip()
                if status_line:
                    match = re.search(r'`([^`]+)`', status_line)
                    if match:
                        status = match.group(1).strip().lower()
                    else:
                        status = status_line.strip().lower()
                    break
    return title, status

def get_milestone_files():
    files = [f for f in os.listdir(MILESTONES_DIR) if f.endswith('.md')]
    # Sort by milestone number if present in filename
    def milestone_num(f):
        m = re.search(r'milestone_(\d+)', f)
        return int(m.group(1)) if m else 9999
    return sorted(files, key=milestone_num)

def get_milestones_from_folder():
    milestones = []
    for fname in get_milestone_files():
        fpath = os.path.join(MILESTONES_DIR, fname)
        title, status = extract_title_status_from_file(fpath)
        if title:
            milestones.append({'title': title, 'status': status or 'todo', 'file': fname})
    return milestones


def sync_milestones_md(milestones):
    # Overwrite milestones.md with header and new milestone list from files
    new_lines = ["## Milestones\n"]
    for m in milestones:
        icon = status_icon(m['status'])
        new_lines.append(f" - {icon} {m['title']}\n")
    with open(MILESTONES_MD, 'w', encoding='utf-8') as f:
        f.writelines(new_lines)
    print('milestones.md updated.')

def main():
    milestones = get_milestones_from_folder()
    sync_milestones_md(milestones)

if __name__ == '__main__':
    main()
