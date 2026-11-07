---
access_model:
  confidence: high
  gated: none
  gated_source:
  - onboarding
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  - scopes
  - rate-limits
  - security
  - sandbox
  trial: false
  try_now: true
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: verified
    event_surface_described: derived
    idempotency: false
    mcp_server: verified
    mcp_tool_quality: na
    openapi_examples: verified
    operation_distinctiveness: false
    pagination_ratio: false
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 57.0
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 146
  human_in_the_loop: 2
  name: Clickup Agentic Access
  operation_count: 248
  slug: clickup-agentic-access
  summary_line: 248 operations · 146 acting · 2 human-in-the-loop
api_count: 14
apis:
- baseURL: https://api.clickup.com
  baseurl_source: declared
  description: Operations for retrieving authenticated user information.
  name: clickup Authorization API
  phrasing_intents:
  - id: GetAccessToken
    intent: Exchange an OAuth code for an access token
    question: How do I turn an OAuth authorization code into a ClickUp access token?
  - id: GetAuthorizedUser
    intent: Get the authenticated user's account (v2)
    question: Which account is my token authenticated as, via the v2 endpoint?
  - id: getAuthorizedUser
    intent: Get the current user's profile (unversioned)
    question: Which non-v2 endpoint returns my user ID, username, email and profile picture?
  phrasing_ops: 3
  slug: clickup-authorization-api
- baseURL: https://api.clickup.com
  baseurl_source: declared
  description: Operations for managing comments on tasks, views, and lists.
  name: clickup Comments API
  phrasing_intents:
  - id: GetTaskComments
    intent: Read a task's comments, newest first (v2)
    question: How do I get the comments on a task through the v2 endpoint?
  - id: CreateTaskComment
    intent: Comment on a task (v2)
    question: What's the v2 endpoint for adding a comment to a task?
  - id: GetChatViewComments
    intent: Read comments in a Chat view (v2)
    question: How can I read the comments posted in a Chat view with the v2 API?
  - id: CreateChatViewComment
    intent: Post a comment in a Chat view (v2)
    question: How do I post a comment into a Chat view with the v2 endpoint?
  - id: GetListComments
    intent: Read the comments on a List (v2)
    question: What's the v2 way to see comments added to a List?
  - id: CreateListComment
    intent: Comment on a List (v2)
    question: How do I leave a comment on a List using v2?
  - id: UpdateComment
    intent: Edit, reassign or resolve a comment (v2)
    question: How do I replace the text of an existing comment via v2?
  - id: DeleteComment
    intent: Delete a comment (v2)
    question: What's the v2 endpoint for deleting a task comment?
  phrasing_ops: 19
  slug: clickup-comments-api
- baseURL: https://api.clickup.com
  baseurl_source: declared
  description: Operations for retrieving custom field definitions and setting custom field values on tasks.
  name: clickup Custom Fields API
  phrasing_intents:
  - id: GetAccessibleCustomFields
    intent: List a List's Custom Fields (v2)
    question: Which Custom Fields can I use on tasks in a particular List?
  - id: getFolderAvailableFields
    intent: List Folder-level Custom Fields
    question: What Custom Fields were created at the Folder level?
  - id: getSpaceAvailableFields
    intent: List Space-level Custom Fields
    question: Which Custom Fields are defined for a whole Space?
  - id: getTeamAvailableFields
    intent: List Workspace-level Custom Fields
    question: What Custom Fields exist at the Workspace level in ClickUp?
  - id: SetCustomFieldValue
    intent: Set a Custom Field on a task (v2)
    question: How do I fill in a Custom Field on a task through the v2 API?
  - id: RemoveCustomFieldValue
    intent: Clear a Custom Field on a task (v2)
    question: Can I clear a task's Custom Field without deleting the dropdown option itself?
  - id: getAccessibleCustomFields
    intent: List a List's Custom Fields (legacy path)
    question: On the older unversioned path, what field definitions and dropdown options does a List expose?
  - id: setCustomFieldValue
    intent: Set a Custom Field value (legacy path)
    question: On the older unversioned path, what format does a dropdown field value take?
  phrasing_ops: 9
  slug: clickup-custom-fields-api
- baseURL: https://api.clickup.com
  baseurl_source: declared
  description: Operations for managing Folders within ClickUp Spaces.
  name: clickup Folders API
  phrasing_intents:
  - id: GetFolders
    intent: List the Folders in a Space (v2)
    question: What Folders and subfolders are in a ClickUp Space?
  - id: CreateFolder
    intent: Create a Folder or subfolder (v2)
    question: Can I create a subfolder inside an existing Folder with the v2 API?
  - id: GetFolder
    intent: Retrieve a Folder and its Lists (v2)
    question: Can I see a Folder's Lists together with its nested subfolders via v2?
  - id: UpdateFolder
    intent: Rename a Folder (v2)
    question: Does renaming a subfolder in v2 keep it nested under its parent?
  - id: DeleteFolder
    intent: Delete a Folder (v2)
    question: How do I delete a Folder from my Workspace with v2?
  - id: MoveFolder
    intent: Move or nest a Folder
    question: Can I nest one Folder inside another as a subfolder?
  - id: CreateFolderFromTemplate
    intent: Create a Folder from a template
    question: Can I build a whole Folder with its Lists and tasks from a saved template?
  - id: getFolders
    intent: List a Space's Folders (legacy path)
    question: On the older unversioned path, how do I fetch every Folder in a Space?
  phrasing_ops: 12
  slug: clickup-folders-api
- baseURL: https://api.clickup.com
  baseurl_source: declared
  description: Operations for managing Goals and Key Results within a ClickUp Workspace.
  name: clickup Goals API
  phrasing_intents:
  - id: GetGoals
    intent: List the Goals in a Workspace (v2)
    question: What Goals does my Workspace have, according to the v2 endpoint?
  - id: CreateGoal
    intent: Create a Goal (v2)
    question: How do I set up a new Goal with owners and a due date through v2?
  - id: GetGoal
    intent: Get a Goal and its Targets (v2)
    question: How can I see a single Goal's Targets through v2?
  - id: UpdateGoal
    intent: Update a Goal (v2)
    question: How do I rename a Goal or change its due date via v2?
  - id: DeleteGoal
    intent: Delete a Goal (v2)
    question: What's the v2 endpoint for removing a Goal from my Workspace?
  - id: CreateKeyResult
    intent: Add a Target to a Goal (v2)
    question: How do I add a measurable Target to a Goal through v2?
  - id: EditKeyResult
    intent: Update a Target's progress (v2)
    question: How do I record progress on a Goal Target through v2?
  - id: DeleteKeyResult
    intent: Delete a Target from a Goal (v2)
    question: What's the v2 way to remove a Target from a Goal?
  phrasing_ops: 16
  slug: clickup-goals-api
- baseURL: https://api.clickup.com
  baseurl_source: declared
  description: Operations for managing Lists within ClickUp Spaces and Folders.
  name: clickup Lists API
  phrasing_intents:
  - id: GetLists
    intent: List the Lists in a Folder (v2)
    question: What Lists are inside a given ClickUp Folder?
  - id: CreateList
    intent: Create a List in a Folder (v2)
    question: Can I create a List in a Folder with a markdown description and due date using v2?
  - id: GetFolderlessLists
    intent: List Lists not in a Folder (v2)
    question: Which Lists sit directly in a Space outside of any Folder?
  - id: CreateFolderlessList
    intent: Create a List directly in a Space (v2)
    question: Can I add a List to a Space without putting it in a Folder, using v2?
  - id: GetList
    intent: Retrieve a List's details (v2)
    question: What information does ClickUp's v2 API return about a single List?
  - id: UpdateList
    intent: Edit a List's settings (v2)
    question: Can I remove a List's color while renaming it through v2?
  - id: DeleteList
    intent: Delete a List (v2)
    question: How can I delete a List from my Workspace with v2?
  - id: AddTaskToList
    intent: Add a task to an additional List
    question: Can one task live in more than one List at the same time?
  phrasing_ops: 19
  slug: clickup-lists-api
- baseURL: https://api.clickup.com
  baseurl_source: declared
  description: Operations for managing Spaces within a ClickUp Workspace.
  name: clickup Spaces API
  phrasing_intents:
  - id: GetSpaces
    intent: List the Spaces in a Workspace (v2)
    question: What Spaces are in my Workspace, via the v2 endpoint?
  - id: CreateSpace
    intent: Create a Space (v2)
    question: How do I add a new Space to a Workspace through v2?
  - id: GetSpace
    intent: Get a Space's details (v2)
    question: How do I look up a single Space via v2?
  - id: UpdateSpace
    intent: Update a Space's settings (v2)
    question: How do I rename a Space or set its color via v2?
  - id: DeleteSpace
    intent: Delete a Space (v2)
    question: What's the v2 endpoint for removing a Space from my Workspace?
  - id: getSpaces
    intent: List Spaces (unversioned path)
    question: Which non-v2 endpoint lists all Spaces in a Workspace?
  - id: createSpace
    intent: Create a Space (unversioned path)
    question: Is there a non-v2 path to create a Space with just a name?
  - id: getSpace
    intent: Get a Space's features and statuses (unversioned)
    question: Which non-v2 endpoint returns a Space's features and statuses?
  phrasing_ops: 10
  slug: clickup-spaces-api
- baseURL: https://api.clickup.com
  baseurl_source: declared
  description: Operations for creating, retrieving, updating, and deleting tasks within ClickUp lists and workspaces.
  name: clickup Tasks API
  phrasing_intents:
  - id: GetTasks
    intent: List the tasks in a List (v2)
    question: How do I pull every task in one ClickUp List through the v2 API, 100 per page?
  - id: CreateTask
    intent: Create a task in a List (v2)
    question: What do I need to send to add a new task to a List using the v2 endpoint?
  - id: GetTask
    intent: Get a task's details (v2)
    question: How do I look up a single task's details and attachments with the v2 endpoint?
  - id: UpdateTask
    intent: Update a task's fields (v2)
    question: How can I change a task's status or priority through the v2 update endpoint?
  - id: DeleteTask
    intent: Delete a task (v2)
    question: How do I remove a task from my Workspace with the v2 endpoint?
  - id: GetFilteredTeamTasks
    intent: Filter tasks across a Workspace (v2)
    question: How do I find tasks across my whole Workspace that match certain filters using v2?
  - id: mergeTasks
    intent: Merge several tasks into one target task
    question: Can I merge duplicate tasks into a single task?
  - id: GetTask'sTimeinStatus
    intent: See how long a task spent in each status (v2)
    question: How long has one task been sitting in each status, using the v2 endpoint?
  phrasing_ops: 24
  slug: clickup-tasks-api
- baseURL: https://api.clickup.com
  baseurl_source: declared
  description: Operations for retrieving Workspace (team) information and membership.
  name: clickup Teams API
  phrasing_intents:
  - id: getTeams
    intent: List Workspaces I can access
    question: Which ClickUp Workspaces does my token have access to?
  - id: getTeamSeats
    intent: Check seat usage in a Workspace
    question: How many seats are filled versus empty in my Workspace?
  - id: getTeamMembers
    intent: List members of a Workspace
    question: Who are the members of my Workspace and what permissions do they have?
  phrasing_ops: 3
  slug: clickup-teams-api
- baseURL: https://api.clickup.com
  baseurl_source: declared
  description: Operations for managing time entries and timers within a ClickUp Workspace.
  name: clickup Time Tracking API
  phrasing_intents:
  - id: Gettimeentrieswithinadaterange
    intent: List time entries in a date range (v2)
    question: How do I pull every time entry my team logged in ClickUp between two dates?
  - id: Createatimeentry
    intent: Log a manual time entry (v2)
    question: Can I log time after the fact with a start time and duration through the v2 API?
  - id: Getsingulartimeentry
    intent: Retrieve one time entry (v2)
    question: What details come back for a single time entry in the v2 API?
  - id: DeleteatimeEntry
    intent: Delete a time entry (v2)
    question: How can I remove a time entry that was logged by mistake with the v2 API?
  - id: UpdateatimeEntry
    intent: Edit a time entry (v2)
    question: Can I change the duration or description of a time entry already logged, using v2?
  - id: Gettimeentryhistory
    intent: View the change history of a time entry
    question: Who changed a time entry and what did they change?
  - id: Getrunningtimeentry
    intent: Check the currently running timer (v2)
    question: Is my ClickUp timer running right now, and on which task?
  - id: Removetagsfromtimeentries
    intent: Remove labels from time entries
    question: Can I strip a label off some time entries without deleting the label from the Workspace?
  phrasing_ops: 23
  slug: clickup-time-tracking-api
- baseURL: https://api.clickup.com
  baseurl_source: declared
  description: Operations for managing views at various levels of the ClickUp hierarchy.
  name: clickup Views API
  phrasing_intents:
  - id: GetTeamViews
    intent: List Everything-level views (v2)
    question: Which views live at the Everything level of my ClickUp Workspace?
  - id: CreateTeamView
    intent: Create an Everything-level view
    question: Can I add a Gantt or Workload view that spans the entire Workspace?
  - id: GetSpaceViews
    intent: List a Space's views (v2)
    question: What board, list and calendar views are set up on a given Space?
  - id: CreateSpaceView
    intent: Add a view to a Space
    question: Can I add a Calendar or Timeline view to a Space programmatically?
  - id: GetFolderViews
    intent: List a Folder's views (v2)
    question: What views does a particular Folder have?
  - id: CreateFolderView
    intent: Add a view to a Folder
    question: Can I add a Table view to a Folder with specific columns?
  - id: GetListViews
    intent: List a List's views (v2)
    question: Which views exist on a single List, including the required ones?
  - id: CreateListView
    intent: Add a view to a List
    question: Can I add a Board view to one List with my own grouping?
  phrasing_ops: 20
  slug: clickup-views-api
- baseURL: https://api.clickup.com
  baseurl_source: declared
  description: Operations for creating, retrieving, updating, and deleting webhook subscriptions.
  name: clickup Webhooks API
  phrasing_intents:
  - id: GetWebhooks
    intent: List my webhooks in a Workspace (v2)
    question: Which webhooks have I set up for my ClickUp Workspace?
  - id: CreateWebhook
    intent: Subscribe to Workspace events (v2)
    question: Can I get notified at my own URL when tasks change in one List?
  - id: UpdateWebhook
    intent: Change a webhook's events (v2)
    question: Can I change which events a webhook listens for in v2?
  - id: DeleteWebhook
    intent: Delete a webhook (v2)
    question: How do I stop a webhook from monitoring events via v2?
  - id: getWebhooks
    intent: List webhook subscriptions (legacy path)
    question: On the older unversioned path, can I see each webhook's health information?
  - id: createWebhook
    intent: Create a webhook subscription (legacy path)
    question: Does the older unversioned endpoint return a shared secret for signing webhook payloads?
  - id: updateWebhook
    intent: Edit a webhook subscription (legacy path)
    question: Can the older unversioned endpoint change only a subscription's URL?
  - id: deleteWebhook
    intent: Delete a webhook subscription (legacy path)
    question: Do events stop immediately when a subscription is erased on the older unversioned path?
  phrasing_ops: 8
  slug: clickup-webhooks-api
- baseURL: https://api.clickup.com
  baseurl_source: declared
  description: Operations for OAuth 2.0 authentication and token management.
  name: Clickup O Auth API
  phrasing_intents:
  - id: getAccessToken
    intent: Exchange an OAuth code for an access token
    question: How do I turn a ClickUp OAuth authorization code into an access token?
  phrasing_ops: 1
  slug: clickup-oauth-api
- baseURL: https://api.clickup.com
  baseurl_source: declared
  description: Acls API
  name: Clickup Acls API
  phrasing_intents:
  - id: publicPatchAcl
    intent: Change privacy and access on an item
    question: How do I make a Space, Folder or List private in ClickUp?
  phrasing_ops: 1
  slug: clickup-acls-api
- baseURL: https://api.clickup.com
  baseurl_source: declared
  description: The Attachments API from Clickup — 2 operation(s) for attachments.
  name: Clickup Attachments API
  phrasing_intents:
  - id: CreateTaskAttachment
    intent: Upload a file to a task (v2)
    question: How do I attach a local file to a ClickUp task?
  - id: getParentEntityAttachments
    intent: List attachments on a task or file field
    question: What files are attached to a task or a File Custom Field?
  - id: postEntityAttachment
    intent: Upload an attachment to a task or file field (v3)
    question: Can I upload a file into a File-type Custom Field with the v3 API?
  phrasing_ops: 3
  slug: clickup-attachments-api
- baseURL: https://api.clickup.com
  baseurl_source: declared
  description: The Audit Logs API from Clickup — 1 operation(s) for audit logs.
  name: Clickup Audit Logs API
  phrasing_intents:
  - id: queryAuditLog
    intent: Query Workspace audit logs
    question: How can a Workspace owner pull audit log events from ClickUp?
  phrasing_ops: 1
  slug: clickup-audit-logs-api
- baseURL: https://api.clickup.com
  baseurl_source: declared
  description: Auditlogs API
  name: Clickup Auditlogs API
  phrasing_intents:
  - id: queryAuditLog
    intent: Query Workspace-level audit logs
    question: How can a Workspace owner pull audit logs for their ClickUp Workspace?
  phrasing_ops: 1
  slug: clickup-auditlogs-api
- baseURL: https://api.clickup.com
  baseurl_source: declared
  description: Chat API
  name: Clickup Chat API
  phrasing_intents:
  - id: getChatChannels
    intent: List the chat Channels in a Workspace
    question: What chat Channels exist in my ClickUp Workspace?
  - id: createChatChannel
    intent: Create a standalone chat Channel
    question: How do I start a new chat Channel that isn't attached to a Space, Folder or List?
  - id: createLocationChatChannel
    intent: Create a Channel on a Space, Folder or List
    question: Can I attach a chat Channel directly to a Space, Folder or List?
  - id: createDirectMessageChatChannel
    intent: Start a Direct Message with up to 15 users
    question: How many people can be in a Direct Message conversation?
  - id: getChatChannel
    intent: Get one chat Channel's details
    question: How do I look up a single chat Channel by its ID?
  - id: updateChatChannel
    intent: Update a chat Channel's settings
    question: How do I rename a chat Channel or change its topic?
  - id: deleteChatChannel
    intent: Delete a chat Channel
    question: Can I delete a Channel that's tied to a Space, Folder or List?
  - id: getChatChannelFollowers
    intent: List the followers of a chat Channel
    question: Who is following a particular chat Channel?
  phrasing_ops: 19
  slug: clickup-chat-api
- baseURL: https://api.clickup.com
  baseurl_source: declared
  description: The Chat (Experimental) API from Clickup — 1 operation(s) for chat (experimental).
  name: Clickup Chat (Experimental) API
  phrasing_intents:
  - id: getSubtypes
    intent: Look up post subtype IDs
    question: Where do I get the ID for an Announcement or Idea post before sending a chat message?
  phrasing_ops: 1
  slug: clickup-chat-experimental-api
- baseURL: https://api.clickup.com
  baseurl_source: declared
  description: The Custom Task Types API from Clickup — 1 operation(s) for custom task types.
  name: Clickup Custom Task Types API
  phrasing_intents:
  - id: GetCustomItems
    intent: List custom task types in a Workspace
    question: What custom task types are defined in my Workspace?
  phrasing_ops: 1
  slug: clickup-custom-task-types-api
- baseURL: https://api.clickup.com
  baseurl_source: declared
  description: Docs API
  name: Clickup Docs API
  phrasing_intents:
  - id: searchDocsPublic
    intent: Search the Docs in a Workspace
    question: How do I find the Docs in my ClickUp Workspace?
  - id: createDocPublic
    intent: Create a new Doc
    question: How do I create a new Doc in a Workspace?
  - id: getDocPublic
    intent: Get information about a Doc
    question: What details can I get about a single Doc?
  - id: getDocPageListingPublic
    intent: Get a Doc's page outline
    question: How can I see the structure of pages in a Doc without their content?
  - id: getDocPagesPublic
    intent: Fetch all pages of a Doc with content
    question: How do I pull every page of a Doc along with its content?
  - id: createPagePublic
    intent: Add a page to a Doc
    question: How do I add a new page to an existing Doc?
  - id: getPagePublic
    intent: Get a single page from a Doc
    question: How do I read one specific page of a Doc?
  - id: editPagePublic
    intent: Edit a page in a Doc
    question: Can I append to a Doc page instead of replacing its content?
  phrasing_ops: 8
  slug: clickup-docs-api
- baseURL: https://api.clickup.com
  baseurl_source: declared
  description: The Guests API from Clickup — 5 operation(s) for guests.
  name: Clickup Guests API
  phrasing_intents:
  - id: InviteGuestToWorkspace
    intent: Invite a guest to a Workspace
    question: How do I invite an outside contractor into my ClickUp Workspace as a guest?
  - id: GetGuest
    intent: Look up a guest
    question: What permissions does a particular guest have in my Workspace?
  - id: EditGuestOnWorkspace
    intent: Change a guest's permissions
    question: Can I let an existing guest see time estimates without making them a member?
  - id: RemoveGuestFromWorkspace
    intent: Revoke a guest's Workspace access
    question: How do I kick a guest out of my Workspace entirely?
  - id: AddGuestToTask
    intent: Share a task with a guest
    question: Can I share a single task with a guest and choose whether they can edit it?
  - id: RemoveGuestFromTask
    intent: Unshare a task from a guest
    question: How do I take away a guest's access to one task?
  - id: AddGuestToList
    intent: Share a List with a guest
    question: Can a guest be given access to a whole List at once?
  - id: RemoveGuestFromList
    intent: Unshare a List from a guest
    question: How do I remove a guest from a List they were shared on?
  phrasing_ops: 10
  slug: clickup-guests-api
- baseURL: https://api.clickup.com
  baseurl_source: declared
  description: The Members API from Clickup — 2 operation(s) for members.
  name: Clickup Members API
  phrasing_intents:
  - id: GetTaskMembers
    intent: List people with explicit access to a task
    question: Who has been given direct access to a specific task?
  - id: GetListMembers
    intent: List people with explicit access to a List
    question: Which Workspace members have explicit access to a List?
  phrasing_ops: 2
  slug: clickup-members-api
- baseURL: https://api.clickup.com
  baseurl_source: declared
  description: The Privacy and access API from Clickup — 1 operation(s) for privacy and access.
  name: Clickup Privacy and access API
  phrasing_intents:
  - id: publicPatchAcl
    intent: Change privacy and sharing on an object
    question: How do I make a Space, Folder, List or task private?
  phrasing_ops: 1
  slug: clickup-privacy-and-access-api
- baseURL: https://api.clickup.com
  baseurl_source: declared
  description: The Roles API from Clickup — 1 operation(s) for roles.
  name: Clickup Roles API
  phrasing_intents:
  - id: GetCustomRoles
    intent: List Custom Roles in a Workspace
    question: What Custom Roles are defined in my ClickUp Workspace?
  phrasing_ops: 1
  slug: clickup-roles-api
- baseURL: https://api.clickup.com
  baseurl_source: declared
  description: The Shared Hierarchy API from Clickup — 1 operation(s) for shared hierarchy.
  name: Clickup Shared Hierarchy API
  phrasing_intents:
  - id: SharedHierarchy
    intent: See tasks, Lists and Folders shared with me
    question: Which tasks, Lists and Folders have been shared with me in a Workspace?
  phrasing_ops: 1
  slug: clickup-shared-hierarchy-api
- baseURL: https://api.clickup.com
  baseurl_source: declared
  description: The Tags API from Clickup — 3 operation(s) for tags.
  name: Clickup Tags API
  phrasing_intents:
  - id: GetSpaceTags
    intent: List the task Tags in a Space
    question: What task Tags are available in a Space?
  - id: CreateSpaceTag
    intent: Create a task Tag in a Space
    question: How do I add a new tag to a Space so tasks can use it?
  - id: EditSpaceTag
    intent: Rename or recolor a Space tag
    question: How do I rename an existing tag in a Space?
  - id: DeleteSpaceTag
    intent: Delete a tag from a Space
    question: How do I delete a tag entirely from a Space?
  - id: AddTagToTask
    intent: Add a tag to a task (v2)
    question: What's the v2 endpoint for tagging a task?
  - id: RemoveTagFromTask
    intent: Remove a tag from a task (v2)
    question: Does removing a tag from a task through v2 delete the tag from the Space?
  phrasing_ops: 6
  slug: clickup-tags-api
- baseURL: https://api.clickup.com
  baseurl_source: declared
  description: The Task Checklists API from Clickup — 4 operation(s) for task checklists.
  name: Clickup Task Checklists API
  phrasing_intents:
  - id: CreateChecklist
    intent: Add a checklist to a task
    question: How do I add a to-do checklist to a ClickUp task?
  - id: EditChecklist
    intent: Rename or reorder a checklist
    question: Can I move a checklist above the others on a task?
  - id: DeleteChecklist
    intent: Delete a checklist from a task
    question: What's the way to remove an entire checklist from a task?
  - id: CreateChecklistItem
    intent: Add an item to a checklist
    question: Can I add a line item to a task checklist and assign it to someone?
  - id: EditChecklistItem
    intent: Update or resolve a checklist item
    question: How do I tick off a checklist item as done?
  - id: DeleteChecklistItem
    intent: Delete a checklist item
    question: Can I remove a single line from a checklist without deleting the checklist?
  phrasing_ops: 6
  slug: clickup-task-checklists-api
- baseURL: https://api.clickup.com
  baseurl_source: declared
  description: The Task Relationships API from Clickup — 2 operation(s) for task relationships.
  name: Clickup Task Relationships API
  phrasing_intents:
  - id: AddDependency
    intent: Make a task wait on or block another
    question: How do I mark one task as blocked by another?
  - id: DeleteDependency
    intent: Remove a dependency between tasks
    question: How do I remove a waiting-on or blocking relationship between tasks?
  - id: AddTaskLink
    intent: Link two tasks together
    question: Can I link two related tasks without making one depend on the other?
  - id: DeleteTaskLink
    intent: Unlink two tasks
    question: How do I remove a Task Link between two tasks?
  phrasing_ops: 4
  slug: clickup-task-relationships-api
- baseURL: https://api.clickup.com
  baseurl_source: declared
  description: The Templates API from Clickup — 3 operation(s) for templates.
  name: Clickup Templates API
  phrasing_intents:
  - id: GetTaskTemplates
    intent: List task templates in a Workspace
    question: Which task templates are available in my Workspace?
  - id: GetListTemplates
    intent: List the List templates in a Workspace
    question: Where do I find List template IDs for creating a List from a template?
  - id: GetFolderTemplates
    intent: List the Folder templates in a Workspace
    question: Which Folder templates can I use in my Workspace?
  phrasing_ops: 3
  slug: clickup-templates-api
- baseURL: https://api.clickup.com
  baseurl_source: declared
  description: The Time Tracking (Legacy) API from Clickup — 2 operation(s) for time tracking (legacy).
  name: Clickup Time Tracking (Legacy) API
  phrasing_intents:
  - id: Gettrackedtime
    intent: Get time tracked on a task (legacy)
    question: How much time has been tracked on a task, using the legacy time endpoint?
  - id: Tracktime
    intent: Log a time interval on a task (legacy)
    question: How do I log time against a task with the legacy time tracking endpoint?
  - id: Edittimetracked
    intent: Edit a tracked time interval (legacy)
    question: Can I fix the start or end of a time interval logged with the legacy endpoint?
  - id: Deletetimetracked
    intent: Delete a tracked time interval (legacy)
    question: How do I remove a time interval I logged with the legacy endpoint?
  phrasing_ops: 4
  slug: clickup-time-tracking-legacy-api
- baseURL: https://api.clickup.com
  baseurl_source: declared
  description: The User Groups API from Clickup — 3 operation(s) for user groups.
  name: Clickup User Groups API
  phrasing_intents:
  - id: CreateUserGroup
    intent: Create a user group
    question: How do I create a ClickUp user group so I can @mention a whole team at once?
  - id: UpdateTeam
    intent: Rename a user group or change members
    question: Can I add or remove people from an existing user group?
  - id: DeleteTeam
    intent: Delete a user group
    question: What's involved in removing a user group from my Workspace?
  - id: GetTeams1
    intent: List user groups in a Workspace
    question: Which user groups exist in my Workspace and who is in them?
  phrasing_ops: 4
  slug: clickup-user-groups-api
- baseURL: https://api.clickup.com
  baseurl_source: declared
  description: The Users API from Clickup — 2 operation(s) for users.
  name: Clickup Users API
  phrasing_intents:
  - id: InviteUserToWorkspace
    intent: Invite someone to a Workspace as a member
    question: How do I invite a new member to my ClickUp Workspace by email?
  - id: GetUser
    intent: Get a user's details in a Workspace
    question: What information can I see about a user in my Workspace?
  - id: EditUserOnWorkspace
    intent: Change a Workspace user's name and role
    question: How do I change a user's name or role in my Workspace?
  - id: RemoveUserFromWorkspace
    intent: Deactivate a user from a Workspace
    question: How do I remove someone from my Workspace?
  phrasing_ops: 4
  slug: clickup-users-api
- baseURL: https://api.clickup.com
  baseurl_source: declared
  description: The Workspaces API from Clickup — 3 operation(s) for workspaces.
  name: Clickup Workspaces API
  phrasing_intents:
  - id: GetAuthorizedTeams
    intent: List my authorized Workspaces
    question: Which ClickUp Workspaces can the authenticated user see?
  - id: GetWorkspaceseats
    intent: View member and guest seats
    question: How many member and guest seats are used and available in my Workspace?
  - id: GetWorkspaceplan
    intent: View a Workspace's plan
    question: What plan is my Workspace currently on?
  phrasing_ops: 3
  slug: clickup-workspaces-api
artifact_total: 135
asyncapis:
- description: The ClickUp Webhooks event system delivers real-time notifications when changes occur within a ClickUp Workspace. When subscribed events happen, ClickUp sends HTTP POST requests to a registered endpoi
  name: ClickUp Webhooks Events
  slug: clickup-webhooks-asyncapi
collections:
- collection_type: open
  name: ClickUp Comments Authorization API
  slug: open-clickup-authorization-api
- collection_type: open
  name: ClickUp Authorization Comments API
  slug: open-clickup-comments-api
- collection_type: open
  name: ClickUp Comments API
  slug: open-clickup-comments
- collection_type: open
  name: ClickUp Comments Authorization Custom Fields API
  slug: open-clickup-custom-fields-api
- collection_type: open
  name: ClickUp Custom Fields API
  slug: open-clickup-custom-fields
- collection_type: open
  name: ClickUp Comments Authorization Folders API
  slug: open-clickup-folders-api
- collection_type: open
  name: ClickUp Folders API
  slug: open-clickup-folders
- collection_type: open
  name: ClickUp Comments Authorization Goals API
  slug: open-clickup-goals-api
- collection_type: open
  name: ClickUp Goals API
  slug: open-clickup-goals
- collection_type: open
  name: ClickUp Comments Authorization Lists API
  slug: open-clickup-lists-api
- collection_type: open
  name: ClickUp Lists API
  slug: open-clickup-lists
- collection_type: open
  name: ClickUp Comments Authorization OAuth API
  slug: open-clickup-oauth-api
- collection_type: open
  name: ClickUp OAuth API
  slug: open-clickup-oauth
- collection_type: open
  name: ClickUp Comments Authorization Spaces API
  slug: open-clickup-spaces-api
- collection_type: open
  name: ClickUp Spaces API
  slug: open-clickup-spaces
- collection_type: open
  name: ClickUp Comments Authorization Tasks API
  slug: open-clickup-tasks-api
- collection_type: open
  name: ClickUp Tasks API
  slug: open-clickup-tasks
- collection_type: open
  name: ClickUp Comments Authorization Teams API
  slug: open-clickup-teams-api
- collection_type: open
  name: ClickUp Teams (Workspaces) API
  slug: open-clickup-teams
- collection_type: open
  name: ClickUp Comments Authorization Time Tracking API
  slug: open-clickup-time-tracking-api
- collection_type: open
  name: ClickUp Time Tracking API
  slug: open-clickup-time-tracking
- collection_type: open
  name: ClickUp Comments Authorization Views API
  slug: open-clickup-views-api
- collection_type: open
  name: ClickUp Views API
  slug: open-clickup-views
- collection_type: open
  name: ClickUp Comments Authorization Webhooks API
  slug: open-clickup-webhooks-api
- collection_type: open
  name: ClickUp Webhooks API
  slug: open-clickup-webhooks
common:
- group: commercial
  href: https://artifacts.apis.io/clickup/finops/clickup-finops.yml
  title: ''
  type: FinOps
  url: finops/clickup-finops.yml
- group: other
  href: https://artifacts.apis.io/clickup/capabilities/clickup-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/clickup-capability-edges.yml
- group: other
  href: https://artifacts.apis.io/clickup/overlays/clickup-api-v2-reference-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/clickup-api-v2-reference-overlay.yaml
- group: other
  href: https://artifacts.apis.io/clickup/overlays/clickup-public-api-v3-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/clickup-public-api-v3-overlay.yaml
- group: auth
  href: https://artifacts.apis.io/clickup/security/clickup-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/clickup-vulnerability-disclosure.yml
- group: company
  title: ''
  type: Website
  url: https://www.clickup.com/
- group: agent
  href: https://artifacts.apis.io/clickup/agentic-access/clickup-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/clickup-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/clickup/security/clickup-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/clickup-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/clickup/security/clickup-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/clickup-domain-security.yml
- group: auth
  href: https://artifacts.apis.io/clickup/authentication/clickup-authentication.yml
  title: ''
  type: Authentication
  url: authentication/clickup-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/clickup
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/clickup-app
- group: design
  href: https://artifacts.apis.io/clickup/json-ld/clickup-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/clickup-context.jsonld
- group: docs
  href: https://artifacts.apis.io/clickup/json-schema/clickup-task-schema.json
  title: ''
  type: JSONSchema
  url: json-schema/clickup-task-schema.json
- group: docs
  href: https://artifacts.apis.io/clickup/json-schema/clickup-webhook-payload-schema.json
  title: ''
  type: JSONSchema
  url: json-schema/clickup-webhook-payload-schema.json
- group: agent
  title: ''
  type: LlmsText
  url: https://developer.clickup.com/llms.txt
- group: company
  title: ''
  type: Blog
  url: https://clickup.com/blog
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.clickup.com/
- group: docs
  title: ''
  type: Documentation
  url: https://developer.clickup.com/docs
- group: docs
  title: ''
  type: APIReference
  url: https://developer.clickup.com/reference
- group: start
  title: ''
  type: GettingStarted
  url: https://developer.clickup.com/docs/authentication
- group: operate
  title: ''
  type: Support
  url: https://help.clickup.com/hc/en-us
- group: commercial
  title: ''
  type: Pricing
  url: https://clickup.com/pricing
- group: start
  title: ''
  type: SignUp
  url: https://app.clickup.com/signup
- group: commercial
  title: ''
  type: TermsOfService
  url: https://clickup.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://clickup.com/terms/privacy
- group: operate
  title: ''
  type: Roadmap
  url: https://feedback.clickup.com/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.clickup.com/
- group: operate
  title: ''
  type: ChangeLog
  url: https://clickup.canny.io/changelog
- group: operate
  href: https://artifacts.apis.io/clickup/changelog/clickup-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/clickup-changelog.yml
- group: auth
  title: ''
  type: Security
  url: https://clickup.com/security
- group: auth
  title: ''
  type: Compliance
  url: https://security.clickup.com/
- group: design
  href: https://artifacts.apis.io/clickup/conformance/clickup-conformance.yml
  title: ''
  type: Conformance
  url: conformance/clickup-conformance.yml
- group: agent
  href: https://artifacts.apis.io/clickup/well-known/clickup-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/clickup-well-known.yml
- group: other
  href: https://artifacts.apis.io/clickup/well-known/clickup-api-catalog.json
  title: ''
  type: APICatalog
  url: well-known/clickup-api-catalog.json
- group: auth
  href: https://artifacts.apis.io/clickup/well-known/clickup-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/clickup-security.txt
- group: build
  href: https://artifacts.apis.io/clickup/packages/clickup-packages.yml
  title: ''
  type: Packages
  url: packages/clickup-packages.yml
- group: agent
  href: https://artifacts.apis.io/clickup/mcp/clickup-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/clickup-mcp.yml
- group: build
  href: https://artifacts.apis.io/clickup/mcp/clickup-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/clickup-tool-crosswalk.yml
- group: agent
  href: https://artifacts.apis.io/clickup/llms/clickup-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/clickup-llms.txt
- group: design
  href: https://artifacts.apis.io/clickup/errors/clickup-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/clickup-problem-types.yml
- group: design
  href: https://artifacts.apis.io/clickup/errors/clickup-error-codes.yml
  title: ''
  type: ErrorCatalog
  url: errors/clickup-error-codes.yml
- group: design
  href: https://artifacts.apis.io/clickup/lifecycle/clickup-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/clickup-lifecycle.yml
- group: auth
  href: https://artifacts.apis.io/clickup/scopes/clickup-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/clickup-scopes.yml
- group: design
  href: https://artifacts.apis.io/clickup/conventions/clickup-conventions.yml
  title: ''
  type: Conventions
  url: conventions/clickup-conventions.yml
- group: design
  href: https://artifacts.apis.io/clickup/data-model/clickup-data-model.yml
  title: ''
  type: DataModel
  url: data-model/clickup-data-model.yml
- group: start
  title: ''
  type: Console
  url: https://developer.clickup.com/docs/trytheapi
- group: start
  href: https://artifacts.apis.io/clickup/sandbox/clickup-sandbox.yml
  title: ''
  type: Console
  url: sandbox/clickup-sandbox.yml
- group: operate
  href: https://artifacts.apis.io/clickup/rate-limits/clickup-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/clickup-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/clickup/plans/clickup-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/clickup-plans-pricing.yml
- group: agent
  href: https://artifacts.apis.io/clickup/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  title: ''
  type: Webhooks
  url: https://developer.clickup.com/docs/webhooks
- group: build
  title: ''
  type: Postman
  url: https://www.postman.com/clickup-api/clickup-public-api/collection/rekuqnj/clickup-api-v2-reference
created: '2026-05-03'
description: 'ClickUp is a work management platform — tasks, Lists, Folders, Spaces, Docs, Chat, Goals, time tracking, dashboards and automations in one Workspace. It ships a public REST API in two concurrent versions: v2 (138 operations, the broad surface) and v3 (35 operations, Chat, Docs, attachments, audit logs and ACLs), both published as first-party OpenAPI documents and advertised through an RFC 9727 api-catalog at developer.clickup.com. Authentication is a single Authorization header carrying either a personal token or an OAuth 2.0 access token authorized per Workspace; there are no OAuth scopes. Webhooks are HMAC-SHA256 signed. ClickUp also runs a remote MCP server at mcp.clickup.com with its own OAuth authorization server, PKCE and dynamic client registration, exposing 48 documented tools. Rate limits are per token and set by the Workspace plan. There is no sandbox, no idempotency mechanism and no published deprecation policy.'
features:
- 'Free plan: 60MB storage, unlimited tasks/members'
- Unlimited at $7/user/mo annual with unlimited everything
- Business at $12/user/mo with dashboards, automations (5K/mo), Google SSO
- 'Enterprise: SAML/SCIM, MSA/HIPAA, 250K automations/mo, data residency'
- 'REST API v2: 100/min Free, 1000/min Unlimited/Business, 10K/min Enterprise'
- Webhooks for task, list, space, doc events
- OAuth 2.0 and personal API tokens
- Custom Fields API
- Goals, Portfolios, Time Tracking APIs
- Docs, Whiteboards, Forms
- ClickUp Chat (Business+)
- ClickUp AI for content and automation (per-user add-on)
- Sprint management with story points
- Mind maps and Gantt charts
- 1,000+ integrations
- Custom branding and audit log on Enterprise
finops:
- has_sources: true
  method: derived
  name: Clickup Finops
  primary_unit: user / mo · billed yearly
  service_category: ''
  slug: clickup-finops
  template: false
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/clickup.png
json_schemas:
- name: AuthorizedUser
  property_count: 9
  slug: clickup-authorizeduser
- name: Comment
  property_count: 9
  slug: clickup-comment
- name: CreateCommentRequest
  property_count: 3
  slug: clickup-createcommentrequest
- name: CreateFolderRequest
  property_count: 1
  slug: clickup-createfolderrequest
- name: CreateGoalRequest
  property_count: 6
  slug: clickup-creategoalrequest
- name: CreateKeyResultRequest
  property_count: 8
  slug: clickup-createkeyresultrequest
- name: CreateListRequest
  property_count: 7
  slug: clickup-createlistrequest
- name: CreateSpaceRequest
  property_count: 3
  slug: clickup-createspacerequest
- name: CreateTaskRequest
  property_count: 17
  slug: clickup-createtaskrequest
- name: CreateTimeEntryRequest
  property_count: 8
  slug: clickup-createtimeentryrequest
- name: CreateWebhookRequest
  property_count: 6
  slug: clickup-createwebhookrequest
- name: CustomField
  property_count: 8
  slug: clickup-customfield
- name: CustomFieldDefinition
  property_count: 7
  slug: clickup-customfielddefinition
- name: Folder
  property_count: 11
  slug: clickup-folder
- name: Goal
  property_count: 20
  slug: clickup-goal
- name: GoalFolder
  property_count: 8
  slug: clickup-goalfolder
- name: KeyResult
  property_count: 17
  slug: clickup-keyresult
- name: List
  property_count: 16
  slug: clickup-list
- name: Member
  property_count: 6
  slug: clickup-member
- name: Priority
  property_count: 4
  slug: clickup-priority
- name: Space
  property_count: 11
  slug: clickup-space
- name: Status
  property_count: 5
  slug: clickup-status
- name: Tag
  property_count: 4
  slug: clickup-tag
- name: ClickUp Task
  property_count: 34
  slug: clickup-task
- name: Team
  property_count: 5
  slug: clickup-team
- name: TeamMember
  property_count: 2
  slug: clickup-teammember
- name: TimeEntry
  property_count: 14
  slug: clickup-timeentry
- name: UpdateCommentRequest
  property_count: 3
  slug: clickup-updatecommentrequest
- name: UpdateFolderRequest
  property_count: 1
  slug: clickup-updatefolderrequest
- name: UpdateGoalRequest
  property_count: 6
  slug: clickup-updategoalrequest
- name: UpdateKeyResultRequest
  property_count: 2
  slug: clickup-updatekeyresultrequest
- name: UpdateListRequest
  property_count: 7
  slug: clickup-updatelistrequest
- name: UpdateSpaceRequest
  property_count: 6
  slug: clickup-updatespacerequest
- name: UpdateTaskRequest
  property_count: 13
  slug: clickup-updatetaskrequest
- name: UpdateTimeEntryRequest
  property_count: 8
  slug: clickup-updatetimeentryrequest
- name: UpdateViewRequest
  property_count: 9
  slug: clickup-updateviewrequest
- name: UpdateWebhookRequest
  property_count: 3
  slug: clickup-updatewebhookrequest
- name: User
  property_count: 6
  slug: clickup-user
- name: View
  property_count: 16
  slug: clickup-view
- name: ClickUp Webhook Payload
  property_count: 8
  slug: clickup-webhook-payload
- name: Webhook
  property_count: 12
  slug: clickup-webhook
json_structures:
- name: Clickup Structure
  property_count: 0
  slug: clickup-structure
jsonld:
- class_count: 0
  name: Clickup Context
  property_count: 11
  slug: clickup-context
layout: provider
mcp_servers:
- description: Remote MCP server at mcp.clickup.com over HTTP requiring OAuth; 48 tools listed.
  name: Clickup MCP Server
  slug: clickup
modified: '2026-09-17'
name: Clickup
nav: Providers
network: true
overview: 'Clickup publishes 34 API contracts indexed on the [APIs.io](https://apis.io/) network, including Authorization API, Comments API, Custom Fields API, and 31 more. Tagged areas include Project Management, Work Management, Productivity, Collaboration, and Task.


  The Clickup catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 2 Spectral governance rulesets.


  Clickup''s developer surface includes authentication, engineering blog, documentation, API reference, getting-started guide, support, pricing, and 46 more developer resources.'
plans:
- name: Clickup Plans Pricing
  plan_count: 6
  slug: clickup-plans-pricing
- name: Clickup Price Estimates
  plan_count: 0
  slug: clickup-price-estimates
random_paper: 3
rate_limits:
- limit_count: 5
  name: Clickup Rate Limits
  slug: clickup-rate-limits
rules:
- authorship: generated
  effective_rule_count: 34
  extends:
  - spectral:asyncapi
  name: Clickup — asyncapi rules
  rule_count: 7
  severity_counts:
    error: 1
    hint: 0
    info: 0
    warn: 6
  slug: clickup-asyncapi-spectral-rules
- authorship: generated
  effective_rule_count: 6
  extends: []
  name: Clickup — jsonschema rules
  rule_count: 6
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 5
  slug: clickup-jsonschema-spectral-rules
scopes:
- name: Clickup Scopes
  scope_count: 2
  slug: clickup-scopes
  summary_line: 2 scopes
score:
  band: exemplar
  composite: 73.7
  coverage:
    artifact_dirs: 36
    catalog_earned: 79.5
    catalog_earned_first_party: 24.0
    catalog_gap: 35.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 1.2
  facets:
    access_clarity: 86.8
    contract_governance: 31.8
    contract_quality: 63.7
    developer_ergonomics: 68.5
    discoverability: 80.0
    operational_transparency: 85.5
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - united-states
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
  previous_composite: 72.5
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 34
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 45.1
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/clickup/clickup-2026-06-20T174517.png
security:
- kind: authentication
  name: Clickup Authentication
  slug: clickup-authentication
  summary_line: apiKey/oauth2 · 4 schemes
- kind: domain-security
  name: Clickup Domain Security
  slug: clickup-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Clickup Vulnerability Disclosure
  slug: clickup-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Clickup Trust Center
  slug: clickup-trust-center
  summary_line: SOC 2, ISO 27001, ISO 27017, ISO 27018, PCI DSS, GDPR
skill_count: 3
skills:
- name: Create and track a ClickUp task
  slug: clickup-create-and-track-task
- name: Subscribe to ClickUp webhooks
  slug: clickup-subscribe-to-webhooks
- name: Work with ClickUp Docs and Chat (API v3)
  slug: clickup-work-with-docs-and-chat
slug: clickup
tags:
- Project Management
- Work Management
- Productivity
- Collaboration
- Task
- Documents
- Chat
- Time Tracking
- MCP
website: https://www.clickup.com/
---
