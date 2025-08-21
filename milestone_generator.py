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

            # For checklist, show yes/no options
            elif q['key'] == 'milestone_checklist':
                options = ['yes', 'no']
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
    ac_content = ["- [ ] Review and complete all items in `dev_checklist.md` before marking a milestone as done."]
    if ac_content:
        md.append("## Acceptance Criteria\n")
        md.extend(ac_content)
        md.append("\n---\n")

    # Affected Areas (only if filled)
    if data.get('affected_areas'):
        md.append(f"## Affected Areas (expected)\n{data['affected_areas']}\n")
        md.append("---\n")

    # Status
    md.append(f"## Status ('todo', 'in-progress', 'blocked', 'done')\n\n`{data['status']}`\n")

    # Milestone Completion Checklist
    if data['milestone_checklist'] == 'yes':
        md.append("---\n")
        md.append(f"## Milestone Completion Checklist\n")
        md.append(f"- check `dev_checklist.md` in the root for Milestone Completion Checklist\n")

    return '\n'.join(md)

def main():
    while True:
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
        # Milestone Checklist
        questions.append({"key": "milestone_checklist", "prompt": "Enable milestone checklist? (yes/no):", "mandatory": True})

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

        # Ask if user wants to create another milestone
        while True:
            more = input("\nDo you want to create another milestone? (yes/no): ").strip().lower()
            if more in ("yes", "y"):
                break  # break out of this inner loop and start another milestone
            elif more in ("no", "n"):
                # After user is done, ask about regenerating milestones.md
                while True:
                    regen = input("\nDo you want to regenerate milestones.md from all milestone files now? (yes/no): ").strip().lower()
                    if regen in ("yes", "y"):
                        script_path = os.path.join(os.path.dirname(__file__), 'sync_milestones_md.py')
                        if not os.path.exists(script_path):
                            print("sync_milestones_md.py not found!")
                        else:
                            import subprocess
                            subprocess.run([os.sys.executable, script_path])
                        return
                    elif regen in ("no", "n"):
                        return
                    else:
                        print("Please enter yes or no.")
                return
            else:
                print("Please enter yes or no.")

if __name__ == "__main__":
    import subprocess
    def print_menu():
        print("\nWhat would you like to do?")
        print("  1. Create a new milestone")
        print("  2. Sync milestones.md with milestone files")
        print("  3. Exit")

    while True:
        print_menu()
        choice = input('Enter number: ').strip()
        if choice == '1':
            main()
            break
        elif choice == '2':
            script_path = os.path.join(os.path.dirname(__file__), 'sync_milestones_md.py')
            if not os.path.exists(script_path):
                print("sync_milestones_md.py not found!")
            else:
                subprocess.run([os.sys.executable, script_path])
            break
        elif choice == '3':
            print("Goodbye!")
            break
        else:
            print("Invalid selection. Please enter 1, 2, or 3.")