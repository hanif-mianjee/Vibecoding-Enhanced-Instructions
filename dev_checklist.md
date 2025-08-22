## IMPORTANT INSTRUCTION FOR AGENTS

You must address and verify every item in this checklist before marking a milestone as complete. For each item, provide clear evidence in the relevant project files (logs, summaries, documentation, code, or commit messages). Do not skip or assume any step is optional, regardless of its order in the list. If an item does not apply, explicitly state why in the milestone summary.

### Dev Checklist

- [ ] Read `memory_bank.md` before starting the milestone to recall context and unresolved issues.
- [ ] Update milestone status in the `milestones/` file after completion as well.
- [ ] Before marking a milestone complete, verify all documentation, and logs are updated.
- [ ] Update current-development-state.md with milestone details and next steps
- [ ] Update dev-log.txt with milestone summary
- [ ] Update chat-summary.md with milestone summary and next steps
- [ ] Mark milestone as complete in milestones.md
- [ ] Append a summary of actions, key decisions, and unresolved issues to `memory_bank.md` after completing the milestone.
- [ ] Commit the code with meaningfull commit
- [ ] Before starting, review the code map and previous milestone’s ‘Where to Start’ notes.
- [ ] Have you checked for existing modules to extend before creating new files?
- [ ] Is your feature linked/integrated with the main code flow (not isolated)?
- [ ] After completing the milestone, update `current-development-state.md` and/or `memory_bank.md` with a “Where to Start” section for the next agent. List relevant files, entry points, and suggested integration locations.
- [ ] Scan the folder and delete any non-essential files and empty folders. Make sure all the references are update
- [ ] Reference the milestone ID in all commit messages to link code changes to milestones.

**Commit Message Template:**
`<type>: [M###] <main summary>, <details if needed>`
Examples:
- `feat: [M003] Add export to CSV feature, update tests and documentation`
- `fix: [M004] Resolve popup UI bug, update logs and milestone status`