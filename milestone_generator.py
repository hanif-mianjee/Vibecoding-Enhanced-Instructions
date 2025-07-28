import os
from datetime import datetime

def prompt_questions(questions):
    answers = {}
    for q in questions:
        while True:
            # For status, show selectable options
            if q['key'] == 'status':
                options = ['todo', 'in-progress', 'blocked', 'done']
                print(f"{q['prompt']} Select one:")
                for idx, opt in enumerate(options, 1):
                    print(f"  {idx}. {opt}")
                choice = input('Enter number: ').strip()
                if choice.isdigit() and 1 <= int(choice) <= len(options):
                    answers[q['key']] = options[int(choice)-1]
                    break
                else:
                    print("Invalid selection. Please enter a valid number.")
            else:
                print(f"{q['prompt']}")
                answer = input('> ').strip()
                if q.get('mandatory', False) and not answer:
                    print("This field is mandatory and cannot be left empty. Please provide a value.")
                else:
                    answers[q['key']] = answer
                    break
    return answers

def generate_markdown(data):
    md = []
    # Milestone Title
    md.append(f"# Milestone Title: {data['milestone_title']}\n")

    # Milestone ID
    md.append(f"## Milestone ID\n\n{data['milestone_id']}\n")

    # Created On
    md.append(f"## Created On\n\n{data['created_on']}\n")

    # Description
    md.append(f"## Description\n\n{data['description']}\n")

    md.append("---\n")

    # Acceptance Criteria (only if any field is filled)
    ac_fields = ['should_happen', 'should_not_happen', 'edge_case_handling', 'considerations']
    ac_content = []
    for key, label in zip(ac_fields, ["What should happen", "What should not happen", "Edge case handling", "Performance, security, or UX consideration"]):
        if data.get(key):
            ac_content.append(f"- [ ] {data[key]}")
    if ac_content:
        md.append("## Acceptance Criteria\n")
        md.extend(ac_content)
        md.append("\n---\n")

    # Affected Areas (only if filled)
    if data.get('affected_areas'):
        md.append(f"## Affected Areas (expected)\n{data['affected_areas']}\n")
        md.append("---\n")

    # Status
    md.append(f"## Status\n\n`{data['status']}`\n")

    return '\n'.join(md)

def main():
    questions = []
    
    # Milestone Title
    questions.append({"key": "milestone_title", "prompt": "Milestone Title (Short Name):", "mandatory": True})

    # Milestone ID
    questions.append({"key": "milestone_id", "prompt": "Milestone ID (e.g., milestone-001):", "mandatory": True})

    # Description
    questions.append({"key": "description", "prompt": "Description (short explanation, goals):", "mandatory": True})

    # Acceptance Criteria (optional)
    questions.append({"key": "should_happen", "prompt": "Acceptance Criteria: What should happen?", "mandatory": False})
    questions.append({"key": "should_not_happen", "prompt": "Acceptance Criteria: What should not happen?", "mandatory": False})
    questions.append({"key": "edge_case_handling", "prompt": "Acceptance Criteria: Edge case handling:", "mandatory": False})
    questions.append({"key": "considerations", "prompt": "Acceptance Criteria: Performance, security, or UX consideration:", "mandatory": False})

    # Affected Areas (optional)
    questions.append({"key": "affected_areas", "prompt": "Affected Areas (expected):", "mandatory": False})

    # Status
    questions.append({"key": "status", "prompt": "Status (`todo`, `in-progress`, `blocked`, `done`):", "mandatory": True})
    
    answers = prompt_questions(questions)
    
    answers['created_on'] = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    
    md_content = generate_markdown(answers)
    
    safe_title = answers['milestone_title'].replace(' ', '_').replace('/', '_')
    filename = f"milestone_{answers['milestone_id']}_{safe_title}.md"
    folder = os.path.join(os.path.dirname(__file__), 'milestones')
    
    os.makedirs(folder, exist_ok=True)
    filepath = os.path.join(folder, filename)
    
    # Add color and formatting for terminal output
    YELLOW = '\033[93m'
    CYAN = '\033[96m'
    GREEN = '\033[92m'
    RESET = '\033[0m'
    BOLD = '\033[1m'
    print(f"\n{BOLD}{CYAN}========== Generated Milestone Markdown =========={RESET}\n")
    for line in md_content.split('\n'):
        if line.startswith('# '):
            print(f"{BOLD}{YELLOW}{line}{RESET}")
        elif line.startswith('##'):
            print(f"{BOLD}{CYAN}{line}{RESET}")
        elif line.startswith('###'):
            print(f"{BOLD}{GREEN}{line}{RESET}")
        elif line.strip() == '---':
            print(f"{CYAN}{'-'*40}{RESET}")
        else:
            print(line)
    print(f"\n{BOLD}{CYAN}========== End Markdown =========={RESET}\n")
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(md_content)
    print(f"New milestone generated: {os.path.join('milestones', filename)}")

if __name__ == "__main__":
    main()