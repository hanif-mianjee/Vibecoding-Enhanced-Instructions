# 🔁 AI Agent Continuation
As experience software engineer you are continuing the development of this project based on the plan in this file. Your tasks are:
1. Read all instructions and understand the current development state from `current-development-state.md` file.
2. Pick the next required milestore from the `milestones.md` file.
   - All starts '- ⏳ <milestone title>' are pending milestones. Just pick one.
   - Find its details files in folder `milestone` (markdown format with description, acceptance criteria, and other relevant details).
3. Generate a test-plan for that milestone and wait for user review.
4. Once test plan is approved, implement the feature using TDD.
5. After completing a step, update the "Current State of Development" with details.
6. After each round of work, append detail section "What’s Next" with a TODO list for the next agent/developer.
7. Always document new files, code functions, and design decisions.
8. Suggest clean and meaningful commit messages.

# 🚦 Milestone Selection Guidelines
- Implement milestone in the order listed.
- Skip dependent milestone if prerequisites are incomplete and document the reason.
- Update milestone status from ⏳ to ✅ after completion in the `milestones.md`.
- Update milestone status in the file after completion as well.
- Before marking a milestone complete, verify all documentation, logs, and commit messages are updated.

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
- Unit and integration tests must be written for each feature before implementation.
- Validate all input, secure all endpoints.
- Document setup, run, and test instructions in `README.md`.
- Summarize all progress in `dev-log.txt` and `chat-summary.md`.
- Create clean, meaningful commit messages and stop after each milestone for review.

# 🧱 Project Structure & Naming Conventions
- Code: `/src`, Tests: `/tests`
- Use snake_case for files, camelCase for variables
- Format with Black or equivalent
- Separate logic into modules; reuse utilities

# ✅ TDD Enforcement Rules
- Write tests before code.
- Get test-plan.txt approved before implementation.
- Tests must cover valid, invalid, and edge cases.
- Keep tests isolated and repeatable.

# 📘 Documentation & Logging Rules
- Update `README.md` if setup, commands, or milestone change.
- Update `dev-log.txt` after each milestone.
- Summarize AI chat decisions in `chat-summary.md`.

# 📦 Deployment Readiness
- Ensure all milestone are ✅
- Pass all tests and linters
- README should be complete
- Package the code for release

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
