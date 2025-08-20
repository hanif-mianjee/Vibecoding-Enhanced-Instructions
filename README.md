# 🧠 Copilot Agent Development Setup Guide

This guide walks you through how to use GitHub Copilot (Agent Mode) with the included `instructions.md` file to begin and manage your project effectively.

![Version](https://img.shields.io/badge/version-0.1.0-blue.svg)

**Current Version:** `0.1.0`

---

## 📦 Versioning

This project uses [Semantic Versioning](https://semver.org/). The current version is tracked in the `VERSION` file and displayed above.

### How to update the version

1. Edit the `VERSION` file and update the version number following SemVer (e.g., `MAJOR.MINOR.PATCH`).
2. Update the version badge and version section in this `README.md` if needed.
3. Commit your changes:

   ```sh
   git add VERSION README.md
   git commit -m "Bump version to x.y.z"
   ```

4. Tag the release:

   ```sh
   git tag vX.Y.Z
   git push origin vX.Y.Z
   ```

---

## ✅ Step-by-Step Usage

### 1. 📂 Prepare Your Project Folder

- Create or open a new project folder in VS Code.
- Place the `instructions.md` file in the root of your project.
- Create a `milestones/` folder to store milestone markdown tickets (with descriptions, acceptance criteria, etc.).
- Use the provided `milestone_generator.py` script to interactively generate milestone files in the `milestones/` folder.
  - You can create multiple milestones in one session.
  - At the end, you will be prompted to regenerate the `milestones.md` summary file from all milestone files.
  - The script `sync_milestones_md.py` is used internally to keep `milestones.md` in sync with the milestone files.


### 2. 📌 Generate Milestone Files & Sync

- Run the `milestone_generator.py` script:

  ```sh
  python milestone_generator.py
  ```

- You will be prompted to:
  1. Create one or more milestone files interactively (repeat as needed)
  2. Optionally regenerate the `milestones.md` summary file from all milestone files at the end

- The script will display the generated markdown in your terminal and save it to the `milestones/` folder.
- The `milestones.md` file will always reflect the current state of all milestone files, in order.

#### Manual Sync (Advanced)

If you ever need to manually regenerate the summary file, you can run:

```sh
python sync_milestones_md.py
```

### 3. 🚀 Enable Copilot Agent in VS Code

- Open the **GitHub Copilot Chat** sidebar or panel.
- Make sure you are signed in and Agent Mode is enabled.
- Ensure you are using GPT-4o model for best context handling.

### 4. 💬 First Prompt to Copilot Agent

In the Copilot Chat window, enter the following:

```text
You are a software developer agent. A full set of instructions is provided in the file `instructions.md` in this workspace. Start by reading that file thoroughly. The project has not been started yet, so begin by generating the recommended folder structure, a README, and initializing the project with appropriate files based on the plan. Follow the instructions carefully. Use TDD. At each step, update the instructions.md file under "Current State of Development" and "What’s Next".
```

This will prompt the agent to:

- Read the `instructions.md`
- Understand project goals and current status
- Begin setup using TDD
- Document and plan next steps

---

## 🔍 Observing What Works Best

After each milestone or work session, assess the agent’s performance using these criteria:

### ✅ What Worked Well?

- Did it follow the plan and pick the right milestore?
- Was the folder structure meaningful?
- Were the test plans created before implementation?
- Was the `instructions.md` updated correctly?

### ⚠️ What Needs Improvement?

- Did it skip steps or tests?
- Was anything misunderstood or over-engineered?
- Were errors handled poorly or not documented?

### 🧾 How to Improve

- Update `instructions.md` with clearer instructions or missing rules.
- Add clarifications to test expectations, code structure, or naming conventions.

---

## 🧠 Pro Tip

Create a `dev-log.txt` to keep track of what was done in each session.

---

## 📂 Folder Structure Suggestion

```
your-project/
│
├── instructions.md
├── feedback-checklist.md
├── README.md
├── dev-log.txt
├── chat-summary.md
├── milestone_generator.py
├── milestones/
│   ├── milestone_001_Milestone_Title.md
│   └── milestone_002_Another_Milestone.md
└── src/
    └── ...
```

You are now ready to begin! 🎯
