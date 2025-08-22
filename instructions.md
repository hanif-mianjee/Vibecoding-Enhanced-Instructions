# ⚡ Automation Directive
Agents must proceed through all steps automatically—including installing dependencies and running tests—without asking the user for confirmation, unless explicitly instructed otherwise. Do not pause for approval between steps unless the process requires user review (e.g., test plan approval). Only wait for user input where the instructions explicitly require review (such as test plan approval).

# 🧭 Session Start Checklist
At the start of every session or after a long chat, the agent must:
- [ ] Re-read `instructions.md`, `current-development-state.md`, `memory_bank.md`, and all relevant milestone files.
- [ ] Summarize current state, memory, and pending milestones.
- [ ] Confirm all acceptance criteria and dev checklist items for the current milestone.
- [ ] List any unresolved issues or open questions.
- [ ] Output this summary before taking any further action.

# 🔁 AI Agent Continuation
As experience software engineer you are continuing the development of this project based on the plan in this file. Your tasks are:
1. Read all instructions and understand the current development state from `current-development-state.md` file.
2. Read the `memory_bank.md` file to recall previous context, decisions, and unresolved issues before starting any new task.
2. Pick the next required milestore from the `milestones.md` file.
   - All starts '- ⏳ <milestone title>' are pending milestones. Just pick one.
   - Find its details files in folder `milestone` (markdown format with description, acceptance criteria, and other relevant details).
3. Generate a test-plan for that milestone and wait for user review.
4. Once test plan is approved, implement the feature using TDD. Test files must include full test logic and assertions for all scenarios before feature implementation. Do not create empty or placeholder tests. Then implement the feature code to make these tests pass
5. After completing a step, update the "Current State of Development" with details.
6. Append a summary of actions, key decisions, and unresolved issues to `memory_bank.md` for continuity.
7. Review and complete all items in `dev_checklist.md` before marking a milestone as done.
8. Always document new files, code functions, and design decisions.
9. Suggest clean and meaningful commit messages.

# 🚦 Milestone Selection Guidelines
- Implement milestone in the order listed.
- Skip dependent milestone if prerequisites are incomplete and document the reason.

# 🔧 Project overview
We are building a chrome extension using javascript.

## Key Development Goals:
1. Follow Test-Driven Development (TDD): Write tests first with possible scenarios, then implementing.
2. Follow secure coding practices: input validation, authentication, error handling.
3. Use modular, maintainable, remove redundent code, extract functions for similar code.
4. Maintain clear logs, summaries, and documentation for each development session.
5. Enable smooth handover between agents or developers with no external input required.

# 📋 Requirements
- Use clean and secure code practices.
- Use proper folder structure (`/src`, `/tests`, etc.) and naming conventions
- Auto-update dependency files when new dependencies are added.
- Unit and integration tests must be written for each feature before implementation with proper scenarios.
- Validate all input, secure all endpoints.
- Document setup, run, and test instructions in `README.md`.
- Summarize all progress in `dev-log.txt` and `chat-summary.md` for the next agent/developer.
- Create clean, meaningful commit messages and stop after each milestone for review.

# 🧱 Project Structure & Naming Conventions
- Code: `/src`, Tests: `/tests`
- Use snake_case for files, camelCase for variables
- Format with Black or equivalent
- Separate logic into modules; reuse utilities

# ✅ TDD Enforcement Rules
- All tests must import and call the actual feature code from the source files (e.g., from `/src`). Do not simulate or mock the feature logic inside the test itself.
- Write tests before implementing any feature code (test-first).
- Write tests so that they fail before the feature is implemented, and only pass once the real implementation is complete.
- Get test-plan.md approved before implementation.
- Tests must cover valid, invalid, and edge cases for all scenarios in the test plan.
- Ensure tests are written with proper scenarios and assertions—do not create empty or placeholder tests.
- Keep tests isolated, repeatable, and independent of each other.
- Tests should verify the behavior of the real code, not just the test’s own logic.

# 📝 Test Plan Review Process
After generating `test-plan.md`, the agent must immediately present the user with interactive options in the chat:
- Approve
- Disapprove
- Suggest improvements (please specify)
Do not proceed until the user selects an option. Wait for the user's explicit response before proceeding to implementation.

# 📘 Documentation & Logging Rules
- Update `README.md` if setup or commands change.
- Update `dev-log.txt` after each milestone for the next agent/developer.
- Summarize AI chat decisions in `chat-summary.md`.

# 🛠️ Troubleshooting Guidance
- Log errors clearly with context.
- Suggest resolution paths if stuck.
- Don’t patch bugs silently—log them and ask for confirmation.

# 🧪 How to Generate test-plan.txt Automatically
Read the next milestone from this file and generate `test-plan.md` with the following format:

Feature: [Feature Name]

Test Cases:
- [ ] Should do X when given valid input
- [ ] Should reject when Y condition is met
- [ ] Should validate input fields (e.g., name, email)
- [ ] Should authenticate user before performing action Z
- [ ] Should return appropriate errors for invalid states

Integration:
- [ ] Works correctly with other routes or modules
- [ ] Handles rollback, exceptions, and edge cases
