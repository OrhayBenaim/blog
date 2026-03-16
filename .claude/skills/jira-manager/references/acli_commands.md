# ACLI Command Reference

Full documentation: https://developer.atlassian.com/cloud/acli/reference/commands/

## Command Tree

```
acli jira
  auth
    login       - Authenticate (--site, --email, --token, --web)
    logout      - Log out
    status      - Show auth status
    switch      - Switch between accounts
  board
    list        - List boards (--json)
  dashboard
    list        - List dashboards (--json)
  field
    list        - List fields (--json)
  filter
    list        - List filters (--json)
  project
    list        - List projects (--json)
    view        - View project (--key, --json)
    update      - Update project
  sprint
    list        - List sprints (--board-id, --json)
    view        - View sprint (--sprint-id, --json)
  workitem
    archive             - Archive work items (--key, --jql, --filter)
    assign              - Assign work items (--key, --assignee)
    attachment-delete   - Delete attachment
    attachment-list     - List attachments (--key, --json)
    clone               - Clone work item (--key)
    comment-create      - Add comment (--key, --body)
    comment-delete      - Delete comment (--key, --comment-id)
    comment-list        - List comments (--key, --json)
    comment-update      - Update comment (--key, --comment-id, --body)
    comment-visibility  - Set comment visibility
    create              - Create work item (--project, --type, --summary)
    create-bulk         - Bulk create from JSON (--from-json, --project)
    delete              - Delete work item (--key)
    edit                - Edit work item(s) (--key, --jql, --filter)
    link                - Link work items (--key, --link-key, --link-type)
    search              - Search work items (--jql, --filter, --json)
    transition          - Change status (--key, --status)
    unarchive           - Unarchive work items (--key)
    view                - View work item details (--key, --json)
```

## workitem create - Full Flags

```
-a, --assignee string           Email, account ID, @me, or default
-d, --description string        Plain text or ADF
    --description-file string   Read description from file
-e, --editor                    Open text editor
-f, --from-file string          Read summary/description from file
    --from-json string          Read definition from JSON
    --generate-json             Generate template JSON
-h, --help                      Show help
    --json                      Output as JSON
-l, --label strings             Comma-separated labels
    --parent string             Parent work item key
-p, --project string            Project key (required)
-s, --summary string            Summary/title (required)
-t, --type string               Epic, Story, Task, Bug, Sub-task (required)
```

## workitem edit - Full Flags

```
-a, --assignee string           New assignee
-d, --description string        New description (plain text or ADF)
    --description-file string   Read description from file
    --filter string             Filter ID to select items
    --from-json string          Read updates from JSON
    --generate-json             Generate template JSON
-h, --help                      Show help
    --ignore-errors             Continue on errors
    --jql string                JQL query to select items
    --json                      Output as JSON
-k, --key string                Work item key(s), comma-separated
-l, --labels string             New labels
    --remove-assignee           Remove assignee
    --remove-labels string      Labels to remove
-s, --summary string            New summary
-t, --type string               New type
-y, --yes                       Skip confirmation
```

## workitem transition - Full Flags

```
    --filter string             Filter ID to select items
-h, --help                      Show help
    --jql string                JQL query to select items
-k, --key string                Work item key(s), comma-separated
-s, --status string             Target status (required)
-y, --yes                       Skip confirmation
```

## workitem search - Full Flags

```
    --filter string             Filter ID
-h, --help                      Show help
    --jql string                JQL query (required if no filter)
    --json                      Output as JSON
```

## Common JQL Patterns

```sql
-- My open items
project = PROJ AND assignee = currentUser() AND status != Done

-- All epics
project = PROJ AND type = Epic

-- Stories in an epic
parent = PROJ-100

-- Current sprint items
project = PROJ AND sprint in openSprints()

-- High priority bugs
project = PROJ AND type = Bug AND priority in (Highest, High)

-- Recently updated
project = PROJ AND updated >= -7d ORDER BY updated DESC

-- Unassigned items
project = PROJ AND assignee is EMPTY

-- Items with specific label
project = PROJ AND labels = "backend"

-- Cross-project search
project in (PROJ, OTHER) AND status = "In Progress"
```

## Link Types

Common values for `--link-type`:
- `blocks` / `is blocked by`
- `clones` / `is cloned by`
- `duplicates` / `is duplicated by`
- `relates to`

## Authentication

```bash
# API token (recommended)
echo <token> | acli jira auth login --site "site.atlassian.net" --email "user@email.com" --token

# Token from file
acli jira auth login --site "site.atlassian.net" --email "user@email.com" --token < token.txt

# OAuth (browser)
acli jira auth login --web

# Check status
acli jira auth status

# Switch accounts
acli jira auth switch

# Logout
acli jira auth logout
```
