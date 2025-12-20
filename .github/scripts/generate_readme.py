import os
import re
from pathlib import Path

def extract_problem_info(problem_dir):
    """Extract problem number, title from folder name."""
    folder_name = os.path.basename(problem_dir)
    match = re.match(r'(\d+)-(.+)', folder_name)
    if not match:
        return None
    
    problem_num = match.group(1)
    problem_title = match.group(2).replace('-', ' ').title()
    
    return {
        'num': problem_num,
        'title': problem_title,
        'folder': folder_name
    }

def generate_readme():
    """Generate README.md with all solved problems."""
    repo_root = Path(__file__).parent.parent.parent
    problems = []
    
    for item in sorted(os.listdir(repo_root)):
        item_path = os.path.join(repo_root, item)
        if os.path.isdir(item_path) and not item.startswith('.') and item != '__pycache__':
            problem = extract_problem_info(item_path)
            if problem:
                problems.append(problem)
    
    problems.sort(key=lambda x: int(x['num']))
    
    with open(os.path.join(repo_root, 'README.md'), 'r', encoding='utf-8') as f:
        content = f.read()
    
    start_marker = '| Problem # | Title | Folder | Status |'
    end_marker = '---'
    
    start_idx = content.find(start_marker)
    if start_idx == -1:
        return
    
    start_idx = content.find('\n', start_idx) + 1
    start_idx = content.find('\n', start_idx) + 1
    
    end_idx = content.find(end_marker, start_idx)
    if end_idx == -1:
        end_idx = len(content)
    
    table_rows = ''
    for problem in problems:
        table_rows += f"| {problem['num']} | {problem['title']} | `{problem['folder']}` | ✅ |\n"
    
    new_content = content[:start_idx] + table_rows + content[end_idx:]
    
    with open(os.path.join(repo_root, 'README.md'), 'w', encoding='utf-8') as f:
        f.write(new_content)
    
    print(f"✅ README.md updated! Total problems: {len(problems)}")

if __name__ == '__main__':
    generate_readme()
