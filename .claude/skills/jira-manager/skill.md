---
name: jira-manager
description: Manage Jira tickets using the Atlassian CLI (ACLI). This skill should be used when the user asks to create, update, search, transition, or manage Jira work items including epics, stories, tasks, bugs, sprints, and boards. Triggers on phrases like "create a Jira ticket", "update PROJ-123", "move ticket to Done", "list my Jira issues", "create an epic", "add a story", "check sprint", "assign ticket", "Jira", "JIRA".
---

# Jira Manager

Manage Jira work items (epics, stories, tasks, bugs) via the Atlassian CLI (ACLI). All operations run through `acli jira` commands in the terminal.

## Prerequisites - Auto-Setup

On every invocation, verify ACLI is installed and authenticated before proceeding with any operation.

### Step 1: Check if ACLI is installed

Run `acli --version` silently. If the command fails (not found):

1. Detect the platform (`uname -s` or check `$OS`)
2. Attempt to install automatically:
   - **macOS**: `brew tap atlassian/acli && brew install acli`
   - **Windows**: `winget install Atlassian.ACLI` (if winget available), otherwise prompt the user to install manually from https://developer.atlassian.com/cloud/acli/guides/install-windows/
   - **Linux (Debian/Ubuntu)**: follow apt instructions from https://developer.atlassian.com/cloud/acli/guides/install-linux/
3. If automatic install fails or the platform is unclear, inform the user and provide the install link: https://developer.atlassian.com/cloud/acli/guides/install-acli/
4. Do not proceed with any Jira operations until ACLI is confirmed installed.

### Step 2: Check authentication

Run `acli jira auth status`. If not authenticated:

**Important:** The `acli jira auth login --web` command uses an interactive TUI that cannot run inside Claude Code's terminal. Do NOT attempt to run it yourself.

1. Tell the user to run the following command manually in their own terminal:
   ```
   acli jira auth login --web
   ```
2. Wait for the user to confirm they have authenticated.
3. Verify with `acli jira auth status` after they confirm.
4. Do not proceed with any Jira operations until authentication is confirmed.

## First Run - Project Configuration

On first invocation, check if a memory file exists at the auto-memory directory (the project's `.claude` memory path) named `jira_config.md`. If it does, read it to get the default project key and use it for all commands.

If the memory file does not exist:

1. Ask the user: "What is your Jira project key (prefix)? For example: PROJ, TEAM, ENG"
2. Ask: "What is your Atlassian site? (e.g., mycompany.atlassian.net)"
3. Ask: "What is your Atlassian email?"
4. Optionally ask: "Do you have additional project keys you work with?"
5. Save the response to a memory file with this format:

```markdown
---
name: jira_config
description: Jira project configuration - default project key, site, email, and known projects
type: project
---

Default project key: <KEY>
Atlassian site: <SITE> (e.g., mycompany.atlassian.net, without https://)
Email: <EMAIL>
Additional projects: <KEY2>, <KEY3> (if provided)

**Why:** Avoids asking for project key, site, and email on every Jira operation.
**How to apply:** Use the default project key for all `--project` flags unless the user specifies a different one. Use the Atlassian site and email for `--site` and `--email` flags in auth commands.
```

Once configured, use the saved default project key automatically in all commands where `--project` is required, unless the user explicitly provides a different one or the ticket key implies a different project.

## Command Structure

```
acli jira <subcommand> [<action>] {MANDATORY FLAGS} [OPTIONAL FLAGS]
```

Append `--json` to commands when parsing output programmatically.

## Core Operations

### Creating Work Items

Create any work item type (Epic, Story, Task, Bug, Sub-task):

```
acli jira workitem create \
  --project "PROJ" \
  --type "Story" \
  --summary "Implement user login" \
  --description "As a user, I want to log in with email and password" \
  --assignee "user@email.com" \
  --label "backend,auth"
```

Key flags:
- `-p, --project` (required): Project key
- `-t, --type` (required): Epic, Story, Task, Bug, Sub-task
- `-s, --summary` (required): Title
- `-d, --description`: Plain text or ADF format
- `--description-file`: Read description from file
- `-a, --assignee`: Email, account ID, `@me`, or `default`
- `-l, --label`: Comma-separated labels
- `--parent`: Parent work item key (for stories under epics, sub-tasks under stories)
- `-e, --editor`: Open text editor for summary/description
- `--from-json`: Read definition from JSON file
- `--generate-json`: Generate a template JSON for creation

#### Creating Hierarchies

To create an epic with child stories:

```bash
# 1. Create the epic
acli jira workitem create --project "PROJ" --type "Epic" --summary "User Authentication" --json

# 2. Create stories under the epic (use the epic key as --parent)
acli jira workitem create --project "PROJ" --type "Story" --summary "Login page" --parent "PROJ-100"
acli jira workitem create --project "PROJ" --type "Story" --summary "Password reset" --parent "PROJ-100"

# 3. Create tasks/sub-tasks under a story
acli jira workitem create --project "PROJ" --type "Sub-task" --summary "Add form validation" --parent "PROJ-101"
```

#### Bulk Creation

```
acli jira workitem create-bulk --from-json "items.json" --project "PROJ"
```

### Viewing Work Items

```
acli jira workitem view --key "PROJ-123" --json
```

### Searching Work Items

Search using JQL queries or filter IDs:

```bash
# By JQL
acli jira workitem search --jql "project = PROJ AND status = 'In Progress' AND assignee = currentUser()" --json

# By filter ID
acli jira workitem search --filter 10001 --json

# All open items in a project
acli jira workitem search --jql "project = PROJ AND status != Done ORDER BY priority DESC" --json

# Epics in a project
acli jira workitem search --jql "project = PROJ AND type = Epic" --json

# Stories under an epic
acli jira workitem search --jql "parent = PROJ-100" --json
```

### Editing Work Items

Edit by key, JQL, or filter:

```bash
# Single item
acli jira workitem edit --key "PROJ-123" --summary "Updated title" --description "New description"

# Multiple items by key
acli jira workitem edit --key "PROJ-123,PROJ-124" --assignee "user@email.com" --yes

# By JQL (batch update)
acli jira workitem edit --jql "project = PROJ AND status = 'To Do'" --labels "sprint-5" --yes

# Change type
acli jira workitem edit --key "PROJ-123" --type "Bug"

# Remove assignee
acli jira workitem edit --key "PROJ-123" --remove-assignee

# From JSON template
acli jira workitem edit --from-json "updates.json"
```

Key flags:
- `-k, --key`: Work item key(s), comma-separated
- `--jql`: JQL query to select items
- `--filter`: Filter ID
- `-s, --summary`: New summary
- `-d, --description`: New description
- `-a, --assignee`: New assignee
- `-l, --labels`: New labels
- `--remove-assignee`: Remove current assignee
- `--remove-labels`: Remove specific labels
- `-t, --type`: Change work item type
- `-y, --yes`: Skip confirmation prompt (use for batch operations)
- `--ignore-errors`: Continue on errors during batch edits

### Transitioning Status

```bash
# Single item
acli jira workitem transition --key "PROJ-123" --status "In Progress"

# Multiple items
acli jira workitem transition --key "PROJ-123,PROJ-124" --status "Done"

# By JQL
acli jira workitem transition --jql "project = PROJ AND sprint in openSprints()" --status "In Progress" --yes

# By filter
acli jira workitem transition --filter 10001 --status "To Do" --yes
```

Common statuses: `To Do`, `In Progress`, `In Review`, `Done` (vary by project workflow).

### Assigning Work Items

```bash
acli jira workitem assign --key "PROJ-123" --assignee "user@email.com"

# Self-assign
acli jira workitem assign --key "PROJ-123" --assignee "@me"
```

### Comments

```bash
# Add comment
acli jira workitem comment-create --key "PROJ-123" --body "Implementation complete, ready for review"

# List comments
acli jira workitem comment-list --key "PROJ-123" --json

# Update comment
acli jira workitem comment-update --key "PROJ-123" --comment-id "12345" --body "Updated comment"

# Delete comment
acli jira workitem comment-delete --key "PROJ-123" --comment-id "12345"
```

### Linking Work Items

```
acli jira workitem link --key "PROJ-123" --link-key "PROJ-456" --link-type "blocks"
```

### Cloning Work Items

```
acli jira workitem clone --key "PROJ-123"
```

### Archiving

```bash
acli jira workitem archive --key "PROJ-123"
acli jira workitem unarchive --key "PROJ-123"
```

### Deleting Work Items

```
acli jira workitem delete --key "PROJ-123"
```

**Always confirm with the user before running delete commands.**

## Project, Board, and Sprint Commands

For detailed flags on project, board, sprint, field, filter, and dashboard commands, consult `references/acli_commands.md`.

```bash
# List projects
acli jira project list --json

# View project details
acli jira project view --key "PROJ" --json

# List boards
acli jira board list --json

# List sprints for a board
acli jira sprint list --board-id 1 --json

# View sprint details
acli jira sprint view --sprint-id 1 --json
```

## Workflow Guidelines

### Before Creating Items

1. Confirm the project key with the user if not obvious from context
2. Ask about work item type if ambiguous (e.g., is it a Story or Task?)
3. For epics with children, create the epic first to get its key, then create child stories with `--parent`

### Before Batch Operations

1. Preview affected items first using `workitem search`
2. Show the user what will be affected before running edit/transition with `--yes`

### Output Handling

- Use `--json` flag for programmatic parsing of results
- When displaying results to users, format them in a readable table or summary
- After creating items, report back the work item key(s) created

### Safety Rules

- Never delete work items without explicit user confirmation
- Never bulk-edit without showing the user the affected items first
- Only use `--yes` after confirming scope with the user
- Treat transition failures as indicators to check available statuses for that project's workflow
