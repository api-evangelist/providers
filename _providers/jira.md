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
    delegated_identity: documented
    dry_run_mode: true
    dynamic_client_registration: true
    error_semantics: verified
    event_surface_described: true
    idempotency: false
    mcp_server: verified
    mcp_tool_quality: na
    openapi_examples: verified
    operation_distinctiveness: distinct
    pagination_ratio: partial
    protected_resource_metadata: verified
    rate_limit_signal: verified
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 65.7
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 416
  human_in_the_loop: 4
  name: Jira Agentic Access
  operation_count: 814
  slug: jira-agentic-access
  summary_line: 814 operations · 416 acting · 4 human-in-the-loop
api_count: 4
apis:
- description: Version 2 of the Jira Cloud platform REST API, offering the same operations as v3 but without Atlassian Document Format support.
  name: Jira Cloud Platform REST API v2
  slug: jira-cloud-platform-rest-api-v2
- description: Operations APIs for Jira Service Management covering schedules, on-call rotations, alerts, escalations, and incident management.
  name: Jira Service Management Operations REST API
  slug: jira-service-management-operations-rest-api
- description: REST API for Jira Align enterprise agile planning platform, providing access to portfolios, epics, features, and program management data.
  name: Jira Align REST API
  slug: jira-align-rest-api
- description: REST API for Atlassian Customer Service Management providing access to customers, organizations, products, and entitlements data.
  name: Jira Customer Service Management REST API
  slug: jira-customer-service-management-rest-api
- baseURL: https://your-domain.atlassian.net/rest/api/3
  baseurl_source: declared
  description: Manage comments on issues.
  name: Jira Issue Comments API
  phrasing_intents:
  - id: getComments
    intent: List an issue's comments via the unversioned path
    question: Is there a legacy unversioned path for reading an issue's comments?
  - id: addComment
    intent: Comment on an issue via the unversioned path
    question: Can I post an ADF comment through the older unversioned issue comment path?
  - id: getCommentsByIds
    intent: Fetch several comments by their IDs
    question: Can I fetch a batch of comments across issues when I already know their IDs?
  - id: getRestApi3IssueByIssueIdOrKeyComment
    intent: List the comments on an issue
    question: How do I read all the comments on an issue?
  - id: postRestApi3IssueByIssueIdOrKeyComment
    intent: Add a comment to an issue
    question: How do I post a comment on an issue?
  - id: deleteComment
    intent: Delete a comment from an issue
    question: How do I delete a comment on an issue?
  - id: getComment
    intent: Get a single comment on an issue
    question: How do I retrieve one specific comment on an issue?
  - id: updateComment
    intent: Edit an existing comment
    question: Can I edit a comment I already posted on an issue?
  phrasing_ops: 8
  slug: jira-issue-comments-api
- baseURL: https://your-domain.atlassian.net/rest/api/3
  baseurl_source: declared
  description: Retrieve issue priority levels.
  name: Jira Issue Priorities API
  phrasing_intents:
  - id: getPriorities
    intent: List priorities via the root /priority path
    question: Is there a short root-level /priority endpoint that returns all issue priorities?
  - id: getRestApi3Priority
    intent: List all priorities (deprecated v3 endpoint)
    question: How did the older, now-deprecated REST v3 call return every issue priority?
  - id: createPriority
    intent: Create an issue priority
    question: How do I add a new priority level like Urgent to Jira?
  - id: setDefaultPriority
    intent: Set the default issue priority
    question: How do I change which priority new issues get by default?
  - id: movePriorities
    intent: Reorder issue priorities
    question: How do I change the order priorities appear in?
  - id: searchPriorities
    intent: Search priorities by name, project or ID
    question: Which priorities are available in a specific project?
  - id: deletePriority
    intent: Delete an issue priority
    question: How do I remove a priority we no longer use?
  - id: getPriority
    intent: Get one issue priority
    question: What are the name, color and description of a specific priority?
  phrasing_ops: 9
  slug: jira-issue-priorities-api
- baseURL: https://your-domain.atlassian.net/rest/api/3
  baseurl_source: declared
  description: Search for issues using JQL (Jira Query Language).
  name: Jira Issue Search API
  phrasing_intents:
  - id: searchForIssuesUsingJql
    intent: Search issues with JQL via /search GET
    question: Can I run a JQL search as a GET on the unversioned /search path?
  - id: searchForIssuesUsingJqlPost
    intent: Search issues with JQL via /search POST
    question: What if my JQL is too long for a query string on the unversioned /search path?
  - id: getIssuePickerResource
    intent: Suggest issues for autocomplete
    question: How can I build issue autocomplete as a user types a word?
  - id: matchIssues
    intent: Check which issues match JQL queries
    question: Can I test whether specific issues would be returned by a JQL query?
  - id: getRestApi3Search
    intent: Search issues with the retiring JQL GET
    question: Is the old /rest/api/3/search GET endpoint still usable while it's being removed?
  - id: postRestApi3Search
    intent: Search issues with the retiring JQL POST
    question: Does the legacy v3 search POST endpoint still take startAt offsets?
  - id: countIssues
    intent: Estimate how many issues match JQL
    question: Roughly how many issues match a bounded JQL query?
  - id: searchAndReconsileIssuesUsingJql
    intent: Search issues with enhanced JQL GET
    question: Which search endpoint uses nextPageToken paging and can include archived projects?
  phrasing_ops: 9
  slug: jira-issue-search-api
- baseURL: https://your-domain.atlassian.net/rest/api/3
  baseurl_source: declared
  description: Retrieve issue statuses.
  name: Jira Issue Statuses API
  phrasing_intents:
  - id: getAllStatuses
    intent: List a project's statuses by issue type
    question: Which statuses can issues in my project move through?
  phrasing_ops: 1
  slug: jira-issue-statuses-api
- baseURL: https://your-domain.atlassian.net/rest/api/3
  baseurl_source: declared
  description: Retrieve and perform workflow transitions on issues.
  name: Jira Issue Transitions API
  phrasing_intents:
  - id: getTransitions
    intent: List the transitions available on an issue
    question: What status changes can I make on an issue right now?
  - id: doTransition
    intent: Move an issue to a new status
    question: How do I move an issue to In Progress or Done through its workflow?
  phrasing_ops: 2
  slug: jira-issue-transitions-api
- baseURL: https://your-domain.atlassian.net/rest/api/3
  baseurl_source: declared
  description: Retrieve and manage issue types for projects.
  name: Jira Issue Types API
  phrasing_intents:
  - id: getIssueAllTypes
    intent: List issue types via the legacy unversioned path
    question: Is there an older unversioned endpoint that lists the issue types visible to me?
  - id: getRestApi3Issuetype
    intent: List all issue types via REST API v3
    question: Which issue types exist across the Jira site in the v3 API?
  - id: createIssueType
    intent: Create an issue type
    question: How do I add a new issue type to Jira?
  - id: getIssueTypesForProject
    intent: List issue types for a project
    question: Which issue types can be used in a particular project?
  - id: deleteIssueType
    intent: Delete an issue type
    question: How do I delete an issue type that's still used by issues?
  - id: getIssueType
    intent: Get one issue type
    question: What are the details of a specific issue type by ID?
  - id: updateIssueType
    intent: Update an issue type
    question: How do I rename an issue type or change its avatar?
  - id: getAlternativeIssueTypes
    intent: List replacement issue types for an issue type
    question: Which issue types could replace one I plan to delete?
  phrasing_ops: 9
  slug: jira-issue-types-api
- baseURL: https://your-domain.atlassian.net/rest/api/3
  baseurl_source: declared
  description: Create, read, update, delete, and transition Jira issues.
  name: Jira Issues API
  phrasing_intents:
  - id: createIssue
    intent: Create an issue via the legacy /issue endpoint
    question: Is there an older unversioned /issue endpoint for creating an issue or sub-task?
  - id: getIssue
    intent: Get an issue via the legacy /issue endpoint
    question: Can I still fetch an issue from the older unversioned /issue path by key?
  - id: editIssue
    intent: Edit an issue via the legacy /issue endpoint
    question: Can the older unversioned edit-issue call apply a transition during the edit?
  - id: deleteIssue
    intent: Delete an issue via the legacy /issue endpoint
    question: Can I delete an issue using the older unversioned /issue path?
  - id: getBulkChangelogs
    intent: Bulk fetch changelogs across many issues
    question: How do I pull the change history for a batch of issues in one request?
  - id: getEvents
    intent: List all issue events
    question: What issue event types exist in my Jira instance?
  - id: postRestApi3Issue
    intent: Create an issue or subtask
    question: How do I open a new issue in a project with a summary and issue type?
  - id: archiveIssuesAsync
    intent: Archive issues matching a JQL query
    question: How do I archive every issue that matches a JQL search?
  phrasing_ops: 28
  slug: jira-issues-api
- baseURL: https://your-domain.atlassian.net/rest/api/3
  baseurl_source: declared
  description: Manage Jira projects including metadata, roles, and components.
  name: Jira Projects API
  phrasing_intents:
  - id: getAllProjects
    intent: List all visible projects via the unversioned path
    question: Is there an older unversioned /project endpoint that returns every project at once?
  - id: searchProjects
    intent: Page through projects via the unversioned search path
    question: Does the unversioned /project/search path let me filter projects by type or category?
  - id: getProject
    intent: Get a project's details via the unversioned path
    question: Can I fetch a project's issue types and components from the legacy unversioned project path?
  - id: getAllStatuses
    intent: List a project's statuses via the unversioned path
    question: Does the legacy unversioned statuses path group a project's statuses by issue type?
  - id: getRestApi3Project
    intent: List every project I can see in one response
    question: How do I get every Jira project visible to me in a single unpaginated call?
  - id: createProject
    intent: Create a new project from a template
    question: How do I create a new Jira project with a key and a name?
  - id: getRecent
    intent: List projects I viewed recently
    question: Which projects have I looked at recently?
  - id: getRestApi3ProjectSearch
    intent: Search and page through projects
    question: How do I search for projects by name or key with pagination?
  phrasing_ops: 17
  slug: jira-projects-api
- description: Atlassian's official hosted Model Context Protocol server. An OAuth 2.1 protected endpoint that exposes Jira, Jira Service Management, Confluence, Bitbucket, Compass and Loom to MCP-capable AI clients
  name: Atlassian Remote MCP Server
  slug: atlassian-jira-remote-mcp-server
- baseURL: https://your-domain.atlassian.net/rest/api/3
  baseurl_source: declared
  description: Manage comments on issues.
  name: Atlassian Jira Issue Comments API
  phrasing_intents:
  - id: getComments
    intent: List an issue's comments via the unversioned path
    question: Is there a legacy unversioned path for reading an issue's comments?
  - id: addComment
    intent: Comment on an issue via the unversioned path
    question: Can I post an ADF comment through the older unversioned issue comment path?
  - id: getCommentsByIds
    intent: Fetch several comments by their IDs
    question: Can I fetch a batch of comments across issues when I already know their IDs?
  - id: getRestApi3IssueByIssueIdOrKeyComment
    intent: List the comments on an issue
    question: How do I read all the comments on an issue?
  - id: postRestApi3IssueByIssueIdOrKeyComment
    intent: Add a comment to an issue
    question: How do I post a comment on an issue?
  - id: deleteComment
    intent: Delete a comment from an issue
    question: How do I delete a comment on an issue?
  - id: getComment
    intent: Get a single comment on an issue
    question: How do I retrieve one specific comment on an issue?
  - id: updateComment
    intent: Edit an existing comment
    question: Can I edit a comment I already posted on an issue?
  phrasing_ops: 8
  slug: atlassian-jira-issue-comments-api
- baseURL: https://your-domain.atlassian.net/rest/api/3
  baseurl_source: declared
  description: Search issues using JQL.
  name: Atlassian Jira Issue Search API
  phrasing_intents:
  - id: searchForIssuesUsingJql
    intent: Search issues with JQL via /search GET
    question: Can I run a JQL search as a GET on the unversioned /search path?
  - id: searchForIssuesUsingJqlPost
    intent: Search issues with JQL via /search POST
    question: What if my JQL is too long for a query string on the unversioned /search path?
  - id: getIssuePickerResource
    intent: Suggest issues for autocomplete
    question: How can I build issue autocomplete as a user types a word?
  - id: matchIssues
    intent: Check which issues match JQL queries
    question: Can I test whether specific issues would be returned by a JQL query?
  - id: getRestApi3Search
    intent: Search issues with the retiring JQL GET
    question: Is the old /rest/api/3/search GET endpoint still usable while it's being removed?
  - id: postRestApi3Search
    intent: Search issues with the retiring JQL POST
    question: Does the legacy v3 search POST endpoint still take startAt offsets?
  - id: countIssues
    intent: Estimate how many issues match JQL
    question: Roughly how many issues match a bounded JQL query?
  - id: searchAndReconsileIssuesUsingJql
    intent: Search issues with enhanced JQL GET
    question: Which search endpoint uses nextPageToken paging and can include archived projects?
  phrasing_ops: 9
  slug: atlassian-jira-issue-search-api
- baseURL: https://your-domain.atlassian.net/rest/api/3
  baseurl_source: declared
  description: List and perform workflow transitions.
  name: Atlassian Jira Issue Transitions API
  phrasing_intents:
  - id: getTransitions
    intent: List the transitions available on an issue
    question: What status changes can I make on an issue right now?
  - id: doTransition
    intent: Move an issue to a new status
    question: How do I move an issue to In Progress or Done through its workflow?
  phrasing_ops: 2
  slug: atlassian-jira-issue-transitions-api
- baseURL: https://your-domain.atlassian.net/rest/api/3
  baseurl_source: declared
  description: Manage worklogs on issues.
  name: Atlassian Jira Issue Worklogs API
  phrasing_intents:
  - id: bulkDeleteWorklogs
    intent: Bulk delete worklogs from an issue
    question: Can I delete many worklogs from one issue at once?
  - id: getIssueWorklog
    intent: List worklogs on an issue
    question: How much time has been logged on an issue and by whom?
  - id: addWorklog
    intent: Log time on an issue
    question: How do I log hours worked against an issue?
  - id: bulkMoveWorklogs
    intent: Move worklogs from one issue to another
    question: Time got logged on the wrong issue; can I move those worklogs elsewhere?
  - id: deleteWorklog
    intent: Delete a worklog
    question: How do I remove a single time entry from an issue?
  - id: getWorklog
    intent: Get a single worklog
    question: Can I look up one specific worklog entry on an issue?
  - id: updateWorklog
    intent: Update a worklog
    question: How do I correct the time spent on a worklog I already logged?
  - id: getIdsOfWorklogsDeletedSince
    intent: List worklogs deleted since a time
    question: Which worklogs have been deleted since my last sync?
  phrasing_ops: 10
  slug: atlassian-jira-issue-worklogs-api
- baseURL: https://your-domain.atlassian.net/rest/api/3
  baseurl_source: declared
  description: Create, read, update and delete Jira issues.
  name: Atlassian Jira Issues API
  phrasing_intents:
  - id: createIssue
    intent: Create an issue via the legacy /issue endpoint
    question: Is there an older unversioned /issue endpoint for creating an issue or sub-task?
  - id: getIssue
    intent: Get an issue via the legacy /issue endpoint
    question: Can I still fetch an issue from the older unversioned /issue path by key?
  - id: editIssue
    intent: Edit an issue via the legacy /issue endpoint
    question: Can the older unversioned edit-issue call apply a transition during the edit?
  - id: deleteIssue
    intent: Delete an issue via the legacy /issue endpoint
    question: Can I delete an issue using the older unversioned /issue path?
  - id: getBulkChangelogs
    intent: Bulk fetch changelogs across many issues
    question: How do I pull the change history for a batch of issues in one request?
  - id: getEvents
    intent: List all issue events
    question: What issue event types exist in my Jira instance?
  - id: postRestApi3Issue
    intent: Create an issue or subtask
    question: How do I open a new issue in a project with a summary and issue type?
  - id: archiveIssuesAsync
    intent: Archive issues matching a JQL query
    question: How do I archive every issue that matches a JQL search?
  phrasing_ops: 28
  slug: atlassian-jira-issues-api
- baseURL: https://your-domain.atlassian.net/rest/api/3
  baseurl_source: declared
  description: Manage Jira projects.
  name: Atlassian Jira Projects API
  phrasing_intents:
  - id: getAllProjects
    intent: List all visible projects via the unversioned path
    question: Is there an older unversioned /project endpoint that returns every project at once?
  - id: searchProjects
    intent: Page through projects via the unversioned search path
    question: Does the unversioned /project/search path let me filter projects by type or category?
  - id: getProject
    intent: Get a project's details via the unversioned path
    question: Can I fetch a project's issue types and components from the legacy unversioned project path?
  - id: getAllStatuses
    intent: List a project's statuses via the unversioned path
    question: Does the legacy unversioned statuses path group a project's statuses by issue type?
  - id: getRestApi3Project
    intent: List every project I can see in one response
    question: How do I get every Jira project visible to me in a single unpaginated call?
  - id: createProject
    intent: Create a new project from a template
    question: How do I create a new Jira project with a key and a name?
  - id: getRecent
    intent: List projects I viewed recently
    question: Which projects have I looked at recently?
  - id: getRestApi3ProjectSearch
    intent: Search and page through projects
    question: How do I search for projects by name or key with pagination?
  phrasing_ops: 17
  slug: atlassian-jira-projects-api
- baseURL: https://your-domain.atlassian.net/rest/api/3
  baseurl_source: declared
  description: Read user information.
  name: Atlassian Jira Users API
  phrasing_intents:
  - id: removeUser
    intent: Delete a user from Jira
    question: Can I remove someone from Jira without deleting their Atlassian account?
  - id: getUser
    intent: Get a user's profile
    question: Can I look up a Jira user's details by account ID?
  - id: createUser
    intent: Create a user
    question: How do I add a new user and give them access to Jira products?
  - id: bulkGetUsers
    intent: Get several users by account ID
    question: Can I fetch details for a batch of users in one request?
  - id: bulkGetUsersMigration
    intent: Map usernames or keys to account IDs
    question: How do I convert old usernames or user keys into account IDs?
  - id: resetUserColumns
    intent: Reset a user's issue columns to default
    question: Can I put a user's issue table columns back to the system default?
  - id: getUserDefaultColumns
    intent: Get a user's default issue columns
    question: Which issue table columns does a user see by default?
  - id: setUserColumns
    intent: Set a user's default issue columns
    question: Can I change which columns a user sees in the issue table by default?
  phrasing_ops: 13
  slug: atlassian-jira-users-api
- baseURL: https://your-domain.atlassian.net/rest/api/2
  baseurl_source: declared
  description: This resource represents an announcement banner. Use it to retrieve and update banner configuration.
  name: Jira Announcement banner API
  phrasing_intents:
  - id: getBanner
    intent: Get the announcement banner settings
    question: What announcement banner is currently shown across Jira?
  - id: setBanner
    intent: Update the announcement banner
    question: Can I post a site-wide banner announcing planned maintenance?
  phrasing_ops: 2
  slug: jira-announcement-banner-api
- baseURL: https://your-domain.atlassian.net/rest/api/2
  baseurl_source: declared
  description: This resource represents app access rule data policies.
  name: Jira App data policies API
  phrasing_intents:
  - id: getPolicy
    intent: Get the workspace data policy
    question: Does my workspace have a data policy blocking app access?
  - id: getPolicies
    intent: Get data policies for projects
    question: Which projects restrict app access through a data policy?
  phrasing_ops: 2
  slug: jira-app-data-policies-api
- baseURL: https://your-domain.atlassian.net/rest/api/2
  baseurl_source: declared
  description: 'This resource supports [app migrations](https://developer.atlassian.com/platform/app-migration/). Use it to: - [to request migrated workflow rules details](https://developer.atlassian.com/platform/app'
  name: Jira App migration API
  phrasing_intents:
  - id: AppIssueFieldValueUpdateResource.updateIssueFields_put
    intent: Bulk update app custom field values in migration
    question: During app migration, how do I set values of my Connect app's custom fields on issues?
  - id: MigrationResource.updateEntityPropertiesValue_put
    intent: Bulk update entity properties in migration
    question: Can a Connect app bulk set entity properties while migrating from server to cloud?
  - id: MigrationResource.workflowRuleSearch_post
    intent: Get migrated workflow transition rule configs
    question: Which workflow transition rules owned by my app were migrated to cloud?
  phrasing_ops: 3
  slug: jira-app-migration-api
- baseURL: https://your-domain.atlassian.net/rest/api/2
  baseurl_source: declared
  description: This resource represents app properties. Use it to store arbitrary data for your [Connect app](https://developer.atlassian.com/cloud/jira/platform/index/#connect-apps).
  name: Jira App properties API
  phrasing_intents:
  - id: AddonPropertiesResource.getAddonProperties_get
    intent: List a Connect app's properties
    question: What properties has my Connect app stored in Jira?
  - id: AddonPropertiesResource.deleteAddonProperty_delete
    intent: Delete a Connect app property
    question: How do I remove a stored property from my Connect app?
  - id: AddonPropertiesResource.getAddonProperty_get
    intent: Get one Connect app property
    question: What value is stored under a specific key for my Connect app?
  - id: AddonPropertiesResource.putAddonProperty_put
    intent: Set a Connect app property
    question: How does a Connect app store its own custom data in Jira?
  - id: getForgeAppPropertyKeys
    intent: List a Forge app's property keys
    question: Which property keys has my Forge app saved in Jira?
  - id: deleteForgeAppProperty
    intent: Delete a Forge app property
    question: How does a Forge app remove one of its stored properties?
  - id: getForgeAppProperty
    intent: Get a Forge app property value
    question: What value does my Forge app have under a given property key?
  - id: putForgeAppProperty
    intent: Set a Forge app property
    question: How does a Forge app save a value it can later use in Jira expressions?
  phrasing_ops: 8
  slug: jira-app-properties-api
- baseURL: https://your-domain.atlassian.net/rest/api/2
  baseurl_source: declared
  description: This resource represents application roles. Use it to get details of an application role or all application roles.
  name: Jira Application roles API
  phrasing_intents:
  - id: getAllApplicationRoles
    intent: List application roles
    question: Which application roles, like Jira Software or Service Management, exist on this site?
  - id: getApplicationRole
    intent: Get an application role
    question: What groups and seat counts belong to one application role?
  phrasing_ops: 2
  slug: jira-application-roles-api
- baseURL: https://your-domain.atlassian.net/rest/api/2
  baseurl_source: declared
  description: The Assets API from Jira — 2 operation(s) for assets.
  name: Jira Assets API
  phrasing_intents:
  - id: getAssetsWorkspaces
    intent: List Assets workspace IDs
    question: What Assets workspace ID do I need to call the Assets REST APIs?
  - id: getInsightWorkspaces
    intent: List Insight workspace IDs (deprecated)
    question: Is there an older Insight endpoint that lists workspace IDs?
  phrasing_ops: 2
  slug: jira-assets-api
- baseURL: https://your-domain.atlassian.net/rest/api/2
  baseurl_source: declared
  description: This resource represents audits that record activities undertaken in Jira. Use it to get a list of audit records.
  name: Jira Audit records API
  phrasing_intents:
  - id: getAuditRecords
    intent: List audit records
    question: What administrative changes were made in Jira recently?
  phrasing_ops: 1
  slug: jira-audit-records-api
- baseURL: https://your-domain.atlassian.net/rest/api/2
  baseurl_source: declared
  description: This resource represents system and custom avatars. Use it to obtain the details of system or custom avatars, add and remove avatars from a project, issue type or priority and obtain avatar images.
  name: Jira Avatars API
  phrasing_intents:
  - id: getAllSystemAvatars
    intent: List built-in system avatars by type
    question: Which built-in avatars does Jira ship for projects, users or priorities?
  - id: getAvatars
    intent: List system and custom avatars for an item
    question: What avatars, including custom uploads, are available for a specific project?
  - id: storeAvatar
    intent: Upload a custom avatar for a project, issue type or priority
    question: How do I upload a custom avatar image for a project or priority?
  - id: deleteAvatar
    intent: Delete a custom avatar
    question: How do I remove a custom avatar from a project or issue type?
  - id: getAvatarImageByType
    intent: Get the default avatar image for a type
    question: Where can I download the default image used for new projects or priorities?
  - id: getAvatarImageByID
    intent: Download an avatar image by its ID
    question: How do I fetch the actual image file for a known avatar ID?
  - id: getAvatarImageByOwner
    intent: Download the current avatar image of an item
    question: What image is a particular project currently using as its avatar?
  phrasing_ops: 7
  slug: jira-avatars-api
- baseURL: https://your-domain.atlassian.net/rest/api/2
  baseurl_source: declared
  description: Apis related to the backlog
  name: Jira Backlog API
  phrasing_intents:
  - id: moveIssuesToBacklog
    intent: Move issues out of sprints to the backlog
    question: How do I pull issues out of their active or future sprints back into the backlog?
  - id: moveIssuesToBacklogForBoard
    intent: Move issues to a specific board's backlog
    question: Can I move issues to the backlog of one particular board and control their rank?
  phrasing_ops: 2
  slug: jira-backlog-api
- baseURL: https://your-domain.atlassian.net/rest/api/2
  baseurl_source: declared
  description: Apis related to boards
  name: Jira Board API
  phrasing_intents:
  - id: getAllBoards
    intent: List the boards I can see
    question: Which Jira boards do I have permission to view?
  - id: createBoard
    intent: Create a scrum or kanban board
    question: How do I create a new scrum board from a saved filter?
  - id: getBoardByFilterId
    intent: Find boards that use a filter
    question: Which boards are built on a particular saved filter?
  - id: deleteBoard
    intent: Delete a board
    question: Can I permanently remove a board I no longer use?
  - id: getBoard
    intent: Get a board's details
    question: What are the name, type and location of a specific board?
  - id: getIssuesForBacklog
    intent: List backlog issues on a board
    question: What issues are sitting in a board's backlog, not in any sprint?
  - id: getIssuesForBacklogJSIS
    intent: List backlog issues with token paging
    question: Is there a backlog endpoint that pages with a nextPageToken instead of startAt?
  - id: getApproximateIssueCountForBacklog
    intent: Count backlog issues on a board
    question: Roughly how many issues are in a board's backlog?
  phrasing_ops: 33
  slug: jira-board-api
- baseURL: https://your-domain.atlassian.net/rest/api/2
  baseurl_source: declared
  description: 'APIs related to integrating build data with Jira Software. These APIs are available to Atlassian Connect apps. To use these APIs you must have the `jiraBuildInfoProvider` module in your Connect app''s '
  name: Jira Builds API
  phrasing_intents:
  - id: submitBuilds
    intent: Send CI build results to Jira
    question: How do I show my CI pipeline's build results on the related Jira issues?
  - id: deleteBuildsByProperty
    intent: Delete builds matching tagged properties
    question: Can I delete every build I submitted that carries a certain property?
  - id: getBuildByKey
    intent: Get a build by pipeline and build number
    question: What build data does Jira currently store for a given pipeline run?
  - id: deleteBuildByKey
    intent: Delete one build by pipeline and build number
    question: How do I remove a single build run from Jira?
  phrasing_ops: 4
  slug: jira-builds-api
- baseURL: https://your-domain.atlassian.net/rest/api/2
  baseurl_source: declared
  description: This resource represents classification levels.
  name: Jira Classification levels API
  phrasing_intents:
  - id: getAllUserDataClassificationLevels
    intent: List data classification levels
    question: What data classification levels are defined in Jira?
  phrasing_ops: 1
  slug: jira-classification-levels-api
- baseURL: https://your-domain.atlassian.net/rest/api/2
  baseurl_source: declared
  description: The Customer API from Jira — 2 operation(s) for customer.
  name: Jira Customer API
  phrasing_intents:
  - id: createCustomer
    intent: Create a service desk customer
    question: How do I add a new customer to Jira Service Management by email?
  - id: revokePortalOnlyAccessForUser
    intent: Revoke a user's portal-only access
    question: How do I stop a portal-only customer from logging into the help center?
  phrasing_ops: 2
  slug: jira-customer-api
- baseURL: https://your-domain.atlassian.net/rest/api/2
  baseurl_source: declared
  description: This resource represents dashboards. Use it to obtain the details of dashboards as well as get, create, update, or remove item properties and gadgets from dashboards.
  name: Jira Dashboards API
  phrasing_intents:
  - id: getAllDashboards
    intent: List dashboards I own or that are shared with me
    question: Which Jira dashboards do I own or have shared with me?
  - id: createDashboard
    intent: Create a new dashboard
    question: How do I create a new dashboard with its own share and edit permissions?
  - id: bulkEditDashboards
    intent: Change owner or permissions on many dashboards
    question: Can I change the owner of up to 100 dashboards in one request?
  - id: getAllAvailableDashboardGadgets
    intent: List gadgets that can be added to dashboards
    question: What gadgets are available to add to a dashboard?
  - id: getDashboardsPaginated
    intent: Search dashboards by name, owner, group or project
    question: How do I find a dashboard by its name?
  - id: getAllGadgets
    intent: List the gadgets on a dashboard
    question: Which gadgets are currently on my dashboard?
  - id: addGadget
    intent: Add a gadget to a dashboard
    question: How do I put a new gadget on a dashboard?
  - id: removeGadget
    intent: Remove a gadget from a dashboard
    question: How do I take a gadget off a dashboard?
  phrasing_ops: 17
  slug: jira-dashboards-api
- baseURL: https://your-domain.atlassian.net/rest/api/2
  baseurl_source: declared
  description: APIs related to integrating deployment data with Jira Software. These APIs are available to Atlassian Connect apps. To use these APIs you must have the `jiraDeploymentInfoProvider` module in your Conn
  name: Jira Deployments API
  phrasing_intents:
  - id: submitDeployments
    intent: Send deployment data to Jira
    question: How do I report deployments from my CI/CD pipeline so they show on Jira issues?
  - id: deleteDeploymentsByProperty
    intent: Delete all deployments matching given properties
    question: Can I wipe every deployment tagged with a certain property?
  - id: getDeploymentByKey
    intent: Get a stored deployment by its key
    question: What deployment data does Jira currently hold for a pipeline run?
  - id: deleteDeploymentByKey
    intent: Delete one deployment by its key
    question: How do I delete a single deployment record from Jira?
  - id: getDeploymentGatingStatusByKey
    intent: Check a deployment's gating status
    question: Is my deployment currently gated or allowed to proceed?
  phrasing_ops: 5
  slug: jira-deployments-api
- baseURL: https://your-domain.atlassian.net/rest/api/2
  baseurl_source: declared
  description: APIs related to integrating development information (commits, branches and pull requests) with Jira. These APIs are available to Atlassian Connect apps and on-premise integrations using OAuth. Connect
  name: Jira Development Information API
  phrasing_intents:
  - id: storeDevelopmentInformation
    intent: Send commits, branches and pull requests to Jira
    question: How do I push repository commits, branches and pull requests into Jira so they show on issues?
  - id: getRepository
    intent: Get a repository's stored development data
    question: What development data does Jira currently hold for one of my repositories?
  - id: deleteRepository
    intent: Delete a repository's development data
    question: How do I remove a repository and all of its dev data from Jira?
  - id: deleteByProperties
    intent: Delete dev data matching tagged properties
    question: Can I wipe all repositories tagged with a certain account or project property?
  - id: existsByProperties
    intent: Check whether dev data exists for properties
    question: Is there any repository data in Jira tagged with a given set of properties?
  - id: deleteEntity
    intent: Delete one commit, branch or pull request
    question: How do I remove a single pull request or branch from Jira's dev panel?
  phrasing_ops: 6
  slug: jira-development-information-api
- baseURL: https://your-domain.atlassian.net/rest/api/2
  baseurl_source: declared
  description: APIs related to integrating Dev Ops Components affected by Incident data with Jira Software. These APIs are available to Atlassian Connect apps. To use these APIs you must have the `jiraDevOpsComponen
  name: Jira DevOps Components API
  phrasing_intents:
  - id: submitComponents
    intent: Send DevOps component data to Jira
    question: How does my app push DevOps components like services into Jira?
  - id: deleteComponentsByProperty
    intent: Bulk delete DevOps components by property
    question: How do I delete every DevOps component I tagged with a given property?
  - id: getComponentById
    intent: Get a stored DevOps component by ID
    question: What DevOps component data does Jira currently hold for an ID?
  - id: deleteComponentById
    intent: Delete one DevOps component by ID
    question: How do I remove a single DevOps component from Jira?
  phrasing_ops: 4
  slug: jira-devops-components-api
- baseURL: https://your-domain.atlassian.net/rest/api/2
  baseurl_source: declared
  description: This resource represents [modules registered dynamically](https://developer.atlassian.com/cloud/jira/platform/dynamic-modules/) by [Connect apps](https://developer.atlassian.com/cloud/jira/platform/in
  name: Jira Dynamic modules API
  phrasing_intents:
  - id: DynamicModulesResource.removeModules_delete
    intent: Remove a Connect app's dynamic modules
    question: How do I unregister modules my Connect app added dynamically?
  - id: DynamicModulesResource.getModules_get
    intent: List a Connect app's dynamic modules
    question: Which modules has my Connect app registered dynamically at runtime?
  - id: DynamicModulesResource.registerModules_post
    intent: Register dynamic modules for a Connect app
    question: How do I add modules to my Connect app without changing its descriptor?
  phrasing_ops: 3
  slug: jira-dynamic-modules-api
- baseURL: https://your-domain.atlassian.net/rest/api/2
  baseurl_source: declared
  description: Apis related to epics
  name: Jira Epic API
  phrasing_intents:
  - id: getIssuesWithoutEpic
    intent: List issues not in any epic
    question: Which issues don't belong to any epic yet?
  - id: removeIssuesFromEpic
    intent: Remove issues from their epics
    question: How do I take issues out of whatever epic they're in?
  - id: getIssuesWithoutEpicJSIS
    intent: List issues without an epic, token paged
    question: Is there a token-paged way to list issues that have no epic?
  - id: getEpic
    intent: Get an epic
    question: How do I look up an epic's name, summary and done status?
  - id: partiallyUpdateEpic
    intent: Update an epic's name, summary, color or status
    question: How do I rename an epic or change its color?
  - id: getIssuesForEpic
    intent: List issues in an epic
    question: Which issues belong to a given epic?
  - id: moveIssuesToEpic
    intent: Move issues into an epic
    question: How do I add existing issues to an epic?
  - id: getIssuesForEpicJSIS
    intent: List an epic's issues with token paging
    question: Is there an enhanced epic issues listing that pages with nextPageToken?
  phrasing_ops: 9
  slug: jira-epic-api
- baseURL: https://your-domain.atlassian.net/rest/api/2
  baseurl_source: declared
  description: APIs related to integrating feature flags with Jira Software. These APIs are available to Atlassian Connect apps. To use these APIs you must have the `jiraFeatureFlagInfoProvider` module in your Conne
  name: Jira Feature Flags API
  phrasing_intents:
  - id: submitFeatureFlags
    intent: Send feature flag data to Jira
    question: How does my feature flag tool push flag status into Jira issues?
  - id: deleteFeatureFlagsByProperty
    intent: Delete feature flags by property
    question: Can I bulk delete feature flags that share certain properties?
  - id: getFeatureFlagById
    intent: Get a stored feature flag
    question: How do I read back a feature flag my app sent to Jira?
  - id: deleteFeatureFlagById
    intent: Delete a stored feature flag
    question: How do I delete one feature flag's data from Jira?
  phrasing_ops: 4
  slug: jira-feature-flags-api
- baseURL: https://your-domain.atlassian.net/rest/api/2
  baseurl_source: declared
  description: This resource represents field schemes which are replacing field configuration schemes to control field associations. They are currently in beta and only available to customers who have opted-in to th
  name: Jira Field schemes API
  phrasing_intents:
  - id: getFieldAssociationSchemes
    intent: List field schemes
    question: What field schemes are set up on my Jira site?
  - id: createFieldAssociationScheme
    intent: Create a new field scheme
    question: How do I create a brand new field scheme from scratch?
  - id: removeFieldsAssociatedWithSchemes
    intent: Remove fields from field schemes
    question: How can I take fields out of one or more field schemes?
  - id: updateFieldsAssociatedWithSchemes
    intent: Update which fields belong to field schemes
    question: Can I add fields to several field schemes in one go?
  - id: removeFieldAssociationSchemeItemParameters
    intent: Remove field parameter overrides
    question: How do I clear work type overrides on field parameters in a field scheme?
  - id: updateFieldAssociationSchemeItemParameters
    intent: Update field parameters in field schemes
    question: Can I override a field's parameters, like required or description, per work type in a field scheme?
  - id: getProjectsWithFieldSchemes
    intent: Get field schemes assigned to projects
    question: Which field scheme is each of my projects using?
  - id: associateProjectsToFieldAssociationSchemes
    intent: Assign projects to field schemes
    question: How do I switch a project to a different field scheme?
  phrasing_ops: 15
  slug: jira-field-schemes-api
- baseURL: https://your-domain.atlassian.net/rest/api/2
  baseurl_source: declared
  description: This resource represents options for sharing [filters](#api-group-Filters). Use it to get share scopes as well as add and remove share scopes from filters.
  name: Jira Filter sharing API
  phrasing_intents:
  - id: getDefaultShareScope
    intent: Get my default sharing for new filters
    question: Who are my new filters and dashboards shared with by default?
  - id: setDefaultShareScope
    intent: Set default sharing for new filters
    question: How do I make my new filters and dashboards private by default?
  - id: getSharePermissions
    intent: List a filter's share permissions
    question: Who is a saved filter shared with?
  - id: addSharePermission
    intent: Share a filter with a user, group or project
    question: How do I share a saved filter with a group or project?
  - id: deleteSharePermission
    intent: Stop sharing a filter with someone
    question: How do I unshare a filter from a group or project?
  - id: getSharePermission
    intent: Get one share permission on a filter
    question: What does one particular share permission on a filter grant?
  phrasing_ops: 6
  slug: jira-filter-sharing-api
- baseURL: https://your-domain.atlassian.net/rest/api/2
  baseurl_source: declared
  description: This resource represents [filters](https://confluence.atlassian.com/x/eQiiLQ). Use it to get, create, update, or delete filters. Also use it to configure the columns for a filter and set favorite filt
  name: Jira Filters API
  phrasing_intents:
  - id: createFilter
    intent: Save a JQL search as a filter
    question: How do I save a JQL query as a reusable filter?
  - id: getFavouriteFilters
    intent: List my favorite filters
    question: Which filters have I starred as favorites?
  - id: getMyFilters
    intent: List filters I own
    question: What filters have I created myself?
  - id: getFiltersPaginated
    intent: Search filters by name, owner or project
    question: How can I find a filter by part of its name?
  - id: deleteFilter
    intent: Delete a filter
    question: Who is allowed to delete a saved filter?
  - id: getFilter
    intent: Get a filter
    question: What JQL is behind a particular saved filter?
  - id: updateFilter
    intent: Update a filter's name, JQL or sharing
    question: How do I change the JQL of a filter I own?
  - id: resetColumns
    intent: Reset a filter's columns to default
    question: Can I undo my custom columns on a filter and go back to the default?
  phrasing_ops: 13
  slug: jira-filters-api
- baseURL: https://your-domain.atlassian.net/rest/api/2
  baseurl_source: declared
  description: This resource represents a list of users and a list of groups. Use it to obtain the details to populate user and group picker suggestions list.
  name: Jira Group and user picker API
  phrasing_intents:
  - id: findUsersAndGroups
    intent: Search users and groups together
    question: How do I find both people and groups matching a name in one search?
  phrasing_ops: 1
  slug: jira-group-and-user-picker-api
- baseURL: https://your-domain.atlassian.net/rest/api/2
  baseurl_source: declared
  description: 'This resource represents groups of users. Use it to get, create, find, and delete groups as well as add and remove users from groups. (\[WARNING\] The standard Atlassian group names are default names '
  name: Jira Groups API
  phrasing_intents:
  - id: removeGroup
    intent: Delete a group
    question: How do I delete a group and move its permissions to another group?
  - id: getGroup
    intent: Get a group and its users (deprecated)
    question: Is there an older endpoint that returns a group together with its users?
  - id: createGroup
    intent: Create a user group
    question: How do I create a new group of users in Jira?
  - id: bulkGetGroups
    intent: List groups in bulk
    question: Can I get a paginated list of all groups on my site?
  - id: getUsersFromGroup
    intent: List members of a group
    question: Who are the members of a given group?
  - id: removeUserFromGroup
    intent: Remove a user from a group
    question: How do I take a user out of a group?
  - id: addUserToGroup
    intent: Add a user to a group
    question: How do I add someone to a group?
  - id: findGroups
    intent: Search groups by name for a picker
    question: Which groups have names containing a given word?
  phrasing_ops: 8
  slug: jira-groups-api
- baseURL: https://your-domain.atlassian.net/rest/api/2
  baseurl_source: declared
  description: The Info API from Jira — 1 operation(s) for info.
  name: Jira Info API
  phrasing_intents:
  - id: getInfo
    intent: Get Jira Service Management instance info
    question: Which version and build of Jira Service Management is running?
  phrasing_ops: 1
  slug: jira-info-api
- baseURL: https://your-domain.atlassian.net/rest/api/2
  baseurl_source: declared
  description: Apis related to issues
  name: Jira Issue API
  phrasing_intents:
  - id: rankIssues
    intent: Rank issues before or after another issue
    question: How do I reorder issues on a board's backlog?
  - id: getIssue
    intent: Get an issue with agile fields
    question: Which sprint and epic is an issue in, and is it flagged?
  - id: getIssueEstimationForBoard
    intent: Get an issue's estimate on a board
    question: What is the story point estimate of an issue on a particular board?
  - id: estimateIssueForBoard
    intent: Set an issue's estimate for a board
    question: How do I set story points on an issue for a specific board?
  phrasing_ops: 4
  slug: jira-issue-api
- baseURL: https://your-domain.atlassian.net/rest/api/2
  baseurl_source: declared
  description: This resource represents issue attachments and the attachment settings for Jira. Use it to get the metadata for an attachment, delete an attachment, and view the metadata for the contents of an attach
  name: Jira Issue attachments API
  phrasing_intents:
  - id: getAttachmentContent
    intent: Download an attachment's content
    question: How do I download the file attached to an issue?
  - id: getAttachmentMeta
    intent: Get attachment settings
    question: Are attachments enabled on my Jira site?
  - id: getAttachmentThumbnail
    intent: Get an attachment thumbnail
    question: Can I get a small preview image of an attachment?
  - id: removeAttachment
    intent: Delete an attachment
    question: How do I remove a file attached to an issue?
  - id: getAttachment
    intent: Get attachment metadata
    question: What's the filename, size and author of an attachment?
  - id: expandAttachmentForHumans
    intent: List files inside an archive attachment
    question: What files are inside a ZIP attached to an issue?
  - id: expandAttachmentForMachines
    intent: Get raw contents metadata for an archive attachment
    question: Can I get machine-friendly metadata for the entries in a ZIP attachment?
  - id: addAttachment
    intent: Attach files to an issue
    question: How do I upload a file to an issue?
  phrasing_ops: 8
  slug: jira-issue-attachments-api
- baseURL: https://your-domain.atlassian.net/rest/api/2
  baseurl_source: declared
  description: This resource represents the issue bulk operations. Use it to move multiple issues from one project to another project or edit fields of multiple issues in one go. For additional clarity, we have crea
  name: Jira Issue bulk operations API
  phrasing_intents:
  - id: submitBulkDelete
    intent: Delete many issues in one request
    question: How do I delete hundreds of issues at once?
  - id: getBulkEditableFields
    intent: List fields that can be bulk edited on issues
    question: Which fields can I bulk edit across a set of issues?
  - id: submitBulkEdit
    intent: Edit fields on many issues at once
    question: Can I change the same field on a batch of issues in one go?
  - id: submitBulkMove
    intent: Move many issues to another project or type
    question: How do I move issues from several projects into one target project?
  - id: getAvailableTransitions
    intent: List transitions available for bulk transitioning
    question: What status transitions can I apply to a group of issues together?
  - id: submitBulkTransition
    intent: Transition the status of many issues
    question: Can I move up to 1,000 issues to a new status in one request?
  - id: submitBulkUnwatch
    intent: Stop watching many issues at once
    question: How do I unwatch a large batch of issues?
  - id: submitBulkWatch
    intent: Start watching many issues at once
    question: Can I watch up to 1,000 issues with one request?
  phrasing_ops: 9
  slug: jira-issue-bulk-operations-api
- baseURL: https://your-domain.atlassian.net/rest/api/2
  baseurl_source: declared
  description: This resource represents [issue comment](#api-group-Issue-comments) properties, which provides for storing custom data against an issue comment. Use is to get, set, and delete issue comment properties
  name: Jira Issue comment properties API
  phrasing_intents:
  - id: getCommentPropertyKeys
    intent: List property keys on a comment
    question: What custom property keys are stored on an issue comment?
  - id: deleteCommentProperty
    intent: Delete a property from a comment
    question: How do I remove a custom property from an issue comment?
  - id: getCommentProperty
    intent: Read a comment property value
    question: What value is stored under a given key on an issue comment?
  - id: setCommentProperty
    intent: Set a property on a comment
    question: How do I store custom JSON data against an issue comment?
  phrasing_ops: 4
  slug: jira-issue-comment-properties-api
- baseURL: https://your-domain.atlassian.net/rest/api/2
  baseurl_source: declared
  description: 'This resource represents the fields associated to project and issue type contexts. Use it to: * assign custom field to projects and issue types.'
  name: Jira Issue custom field associations API
  phrasing_intents:
  - id: removeAssociations
    intent: Unassociate fields from projects and issue types
    question: How do I remove fields from a project and issue type combination?
  - id: createAssociations
    intent: Associate fields with projects and issue types
    question: How do I make a set of fields available in certain projects?
  phrasing_ops: 2
  slug: jira-issue-custom-field-associations-api
- baseURL: https://your-domain.atlassian.net/rest/api/2
  baseurl_source: declared
  description: This resource represents configurations stored against a custom field context by a [Forge app](https://developer.atlassian.com/platform/forge/). Configurations are information used by the Forge app at
  name: Jira Issue custom field configuration (apps) API
  phrasing_intents:
  - id: getCustomFieldsConfigurations
    intent: Bulk get configurations for Forge custom fields
    question: How do I get the configurations of several Forge app custom fields in one request?
  - id: getCustomFieldConfiguration
    intent: Get configurations for one Forge custom field
    question: What configuration does my Forge custom field have in each context?
  - id: updateCustomFieldConfiguration
    intent: Update a Forge custom field's context configs
    question: How do I change the configuration of my Forge custom field for its contexts?
  phrasing_ops: 3
  slug: jira-issue-custom-field-configuration-apps-api
- baseURL: https://your-domain.atlassian.net/rest/api/2
  baseurl_source: declared
  description: 'This resource represents issue custom field contexts. Use it to: * get, create, update, and delete custom field contexts. * get context to issue types and projects mappings. * get custom field context'
  name: Jira Issue custom field contexts API
  phrasing_intents:
  - id: getContextsForField
    intent: List the contexts of a custom field
    question: What contexts are defined for a custom field?
  - id: createCustomFieldContext
    intent: Create a context for a custom field
    question: How do I create a new context for a custom field limited to certain projects?
  - id: getDefaultValues
    intent: Get default values for a custom field's contexts
    question: What default value does each context of my custom field use?
  - id: setDefaultValues
    intent: Set default values for a custom field's contexts
    question: How do I set a default value for a custom field in a context?
  - id: getContextDefaultValues
    intent: Get a field's defaults grouped by context and issue type
    question: Can I see a custom field's default values broken down per issue type?
  - id: getIssueTypeMappingsForContexts
    intent: List which issue types each field context covers
    question: Which issue types are mapped to each context of a custom field?
  - id: getCustomFieldContextsForProjectsAndIssueTypes
    intent: Find which field context applies to project/issue type pairs
    question: Which context of a custom field applies to a given project and issue type combination?
  - id: getProjectContextMapping
    intent: List which projects each field context covers
    question: Which projects is each context of a custom field assigned to?
  phrasing_ops: 14
  slug: jira-issue-custom-field-contexts-api
- baseURL: https://your-domain.atlassian.net/rest/api/2
  baseurl_source: declared
  description: 'This resource represents custom issue field select list options created in Jira or using the REST API. This resource supports the following field types: * Checkboxes. * Radio Buttons. * Select List (s'
  name: Jira Issue custom field options API
  phrasing_intents:
  - id: getCustomFieldOption
    intent: Get a custom field option by ID
    question: How do I look up a single select list option by its option ID?
  - id: getOptionsForContext
    intent: List options of a custom field context
    question: What options are available in a select field for a given context?
  - id: createCustomFieldOption
    intent: Add options to a select field context
    question: How do I add new choices to a dropdown custom field?
  - id: updateCustomFieldOption
    intent: Update select options in a field context
    question: How do I rename or disable existing options in a select field?
  - id: reorderCustomFieldOptions
    intent: Reorder options in a field context
    question: How do I change the order options appear in a select field?
  - id: deleteCustomFieldOption
    intent: Delete a select option from a field context
    question: How do I remove a choice from a dropdown custom field?
  - id: replaceCustomFieldOption
    intent: Replace an option's value on issues
    question: How do I swap one select option for another on all issues that use it?
  phrasing_ops: 7
  slug: jira-issue-custom-field-options-api
- baseURL: https://your-domain.atlassian.net/rest/api/2
  baseurl_source: declared
  description: 'This resource represents custom issue field select list options created by a Connect app. See [Issue custom field options](#api-group-Issue-custom-field-options) to manipulate options created in Jira '
  name: Jira Issue custom field options (apps) API
  phrasing_intents:
  - id: getAllIssueFieldOptions
    intent: List all options of an app's select field
    question: How do I list every option my Connect app added to its select list issue field?
  - id: createIssueFieldOption
    intent: Add an option to an app's select field
    question: How can my Connect app add a new choice to its select list issue field?
  - id: getSelectableIssueFieldOptions
    intent: List field options the user can select
    question: Which options of an app select field can the current user pick when editing an issue?
  - id: getVisibleIssueFieldOptions
    intent: List field options the user can view
    question: Which options of an app select field is the current user allowed to see, even ones they cannot select?
  - id: deleteIssueFieldOption
    intent: Delete an option from an app's select field
    question: How do I remove a choice from my app's select list field?
  - id: getIssueFieldOption
    intent: Get one option of an app's select field
    question: How do I read a single option's name and properties from my app's select field?
  - id: updateIssueFieldOption
    intent: Update or create a field option by ID
    question: How do I rename an existing option in my app's select field?
  - id: replaceIssueFieldOption
    intent: Deselect an option on issues, optionally replacing it
    question: How do I swap one select option for another on every issue that uses it?
  phrasing_ops: 8
  slug: jira-issue-custom-field-options-apps-api
- baseURL: https://your-domain.atlassian.net/rest/api/2
  baseurl_source: declared
  description: This resource represents the values of custom fields added by [Forge apps](https://developer.atlassian.com/platform/forge/). Use it to update the value of a custom field on issues.
  name: Jira Issue custom field values (apps) API
  phrasing_intents:
  - id: updateMultipleCustomFieldValues
    intent: Update several app custom fields on issues
    question: Can my app update values of multiple custom fields across many issues at once?
  - id: updateCustomFieldValue
    intent: Update one app custom field on issues
    question: How does an app set the value of its own custom field on several issues?
  phrasing_ops: 2
  slug: jira-issue-custom-field-values-apps-api
- baseURL: https://your-domain.atlassian.net/rest/api/2
  baseurl_source: declared
  description: This resource represents issue field configurations. Use it to get, set, and delete field configurations and field configuration schemes.
  name: Jira Issue field configurations API
  phrasing_intents:
  - id: getAllFieldConfigurations
    intent: List field configurations
    question: Which field configurations exist in my Jira site?
  - id: createFieldConfiguration
    intent: Create a field configuration
    question: How do I create a new field configuration in company-managed Jira?
  - id: deleteFieldConfiguration
    intent: Delete a field configuration
    question: Can I delete a field configuration that is no longer used?
  - id: updateFieldConfiguration
    intent: Rename or redescribe a field configuration
    question: How do I rename an existing field configuration?
  - id: getFieldConfigurationItems
    intent: List the fields in a field configuration
    question: Which fields are hidden or required in a given field configuration?
  - id: updateFieldConfigurationItems
    intent: Change field settings in a field configuration
    question: How do I make a field required or hidden within a field configuration?
  - id: getAllFieldConfigurationSchemes
    intent: List field configuration schemes
    question: What field configuration schemes are defined in my Jira instance?
  - id: createFieldConfigurationScheme
    intent: Create a field configuration scheme
    question: How do I create a new field configuration scheme?
  phrasing_ops: 15
  slug: jira-issue-field-configurations-api
- baseURL: https://your-domain.atlassian.net/rest/api/2
  baseurl_source: declared
  description: This resource represents issue fields, both system and custom fields. Use it to get fields, field configurations, and create custom fields.
  name: Jira Issue fields API
  phrasing_intents:
  - id: getFields
    intent: List all system and custom issue fields
    question: What system and custom fields exist on my Jira site?
  - id: createCustomField
    intent: Create a custom field
    question: How do I add a new custom field to issues?
  - id: getFieldsPaginated
    intent: Search fields page by page
    question: How do I search for fields whose name contains a word?
  - id: getTrashedFieldsPaginated
    intent: List custom fields in the trash
    question: Which custom fields are currently in the trash?
  - id: updateCustomField
    intent: Update a custom field's name, description or searcher
    question: How do I rename a custom field?
  - id: getFieldProjectAssociations
    intent: List projects a custom field is associated with
    question: Which projects is a custom field associated with?
  - id: getContextsForFieldDeprecated
    intent: List a field's contexts via the deprecated endpoint
    question: Is there an older deprecated endpoint that lists the contexts a field is used in?
  - id: deleteCustomField
    intent: Permanently delete a custom field
    question: How do I permanently delete a custom field, even if it's in the trash?
  phrasing_ops: 11
  slug: jira-issue-fields-api
- baseURL: https://your-domain.atlassian.net/rest/api/2
  baseurl_source: declared
  description: This resource represents [issue link](#api-group-Issue-links) types. Use it to get, create, update, and delete link issue types as well as get lists of all link issue types. To use it, the site must h
  name: Jira Issue link types API
  phrasing_intents:
  - id: getIssueLinkTypes
    intent: List issue link types
    question: What kinds of issue links, like blocks or duplicates, are available?
  - id: createIssueLinkType
    intent: Create an issue link type
    question: How do I add a custom link type such as depends on?
  - id: deleteIssueLinkType
    intent: Delete an issue link type
    question: Can I delete a link type nobody uses anymore?
  - id: getIssueLinkType
    intent: Get an issue link type
    question: What are the inward and outward descriptions of a specific link type?
  - id: updateIssueLinkType
    intent: Update an issue link type
    question: Can I rename a link type or change its inward and outward text?
  phrasing_ops: 5
  slug: jira-issue-link-types-api
- baseURL: https://your-domain.atlassian.net/rest/api/2
  baseurl_source: declared
  description: This resource represents links between issues. Use it to get, create, and delete links between issues. To use it, the site must have [issue linking](https://confluence.atlassian.com/x/yoXKM) enabled.
  name: Jira Issue links API
  phrasing_intents:
  - id: linkIssues
    intent: Link two issues together
    question: How do I mark one issue as blocking another?
  - id: deleteIssueLink
    intent: Delete an issue link
    question: How do I unlink two issues?
  - id: getIssueLink
    intent: Get an issue link
    question: What issues and link type does a specific issue link connect?
  phrasing_ops: 3
  slug: jira-issue-links-api
- baseURL: https://your-domain.atlassian.net/rest/api/2
  baseurl_source: declared
  description: This resource represents issue navigator settings. Use it to get and set issue navigator default columns.
  name: Jira Issue navigator settings API
  phrasing_intents:
  - id: getIssueNavigatorDefaultColumns
    intent: Get site-wide issue navigator columns
    question: Which columns does the issue navigator show by default for everyone?
  - id: setIssueNavigatorDefaultColumns
    intent: Set site-wide issue navigator columns
    question: Can I change the default issue navigator columns for the whole site?
  phrasing_ops: 2
  slug: jira-issue-navigator-settings-api
- baseURL: https://your-domain.atlassian.net/rest/api/2
  baseurl_source: declared
  description: This resource represents notification schemes, lists of events and the recipients who will receive notifications for those events. Use it to get details of a notification scheme and a list of notifica
  name: Jira Issue notification schemes API
  phrasing_intents:
  - id: getNotificationSchemes
    intent: List notification schemes
    question: What notification schemes are set up in Jira?
  - id: createNotificationScheme
    intent: Create a notification scheme
    question: How do I create a new notification scheme with its events and recipients?
  - id: getNotificationSchemeToProjectMappings
    intent: See which projects use which notification scheme
    question: Which projects are assigned to a particular notification scheme?
  - id: getNotificationScheme
    intent: Get a notification scheme's events
    question: Who gets notified for each event in a notification scheme?
  - id: updateNotificationScheme
    intent: Rename or describe a notification scheme
    question: Can I rename a notification scheme or change its description?
  - id: addNotifications
    intent: Add notifications to a scheme
    question: Can I add new event recipients to an existing notification scheme?
  - id: deleteNotificationScheme
    intent: Delete a notification scheme
    question: Can I delete a notification scheme I no longer need?
  - id: removeNotificationFromNotificationScheme
    intent: Remove one notification from a scheme
    question: Can I stop one recipient from being notified without deleting the whole scheme?
  phrasing_ops: 8
  slug: jira-issue-notification-schemes-api
- baseURL: https://your-domain.atlassian.net/rest/api/2
  baseurl_source: declared
  description: This resource supports bulk pinning and unpinning of [issue panels](https://developer.atlassian.com/platform/forge/) that are added by a Forge app. Only Jira administrators can use it.
  name: Jira Issue panels API
  phrasing_intents:
  - id: bulkPinUnpinProjectsAsync
    intent: Pin or unpin a Forge issue panel across projects
    question: How do I pin a Forge app's issue panel to many projects at once?
  phrasing_ops: 1
  slug: jira-issue-panels-api
- baseURL: https://your-domain.atlassian.net/rest/api/2
  baseurl_source: declared
  description: This resource represents [issue](#api-group-Issues) properties, which provides for storing custom data against an issue. Use it to get, set, and delete issue properties as well as obtain details of al
  name: Jira Issue properties API
  phrasing_intents:
  - id: bulkSetIssuesPropertiesList
    intent: Set the same properties on many issues
    question: Can I apply one list of entity properties to thousands of issues in one request?
  - id: bulkSetIssuePropertiesByIssue
    intent: Set different properties per issue in bulk
    question: How do I give each issue its own property values in a single async request?
  - id: bulkDeleteIssueProperty
    intent: Delete one property from many issues
    question: How do I strip a property off lots of issues at once?
  - id: bulkSetIssueProperty
    intent: Set one property across many issues
    question: Can I set a single property key on every issue that matches a filter?
  - id: getIssuePropertyKeys
    intent: List property keys on an issue
    question: What custom property keys are stored on an issue?
  - id: deleteIssueProperty
    intent: Delete a property from a single issue
    question: How do I remove one custom property from a single issue?
  - id: getIssueProperty
    intent: Read one property of an issue
    question: What value is stored under a given property key on one issue?
  - id: setIssueProperty
    intent: Set a property on a single issue
    question: How do I store custom JSON data against one issue?
  phrasing_ops: 8
  slug: jira-issue-properties-api
- baseURL: https://your-domain.atlassian.net/rest/api/2
  baseurl_source: declared
  description: This resource represents Issue Redaction. Provides APIs to redact issue data.
  name: Jira Issue redaction API
  phrasing_intents:
  - id: redact
    intent: Redact sensitive data in issue fields
    question: How do I permanently redact sensitive text from issue fields?
  - id: getRedactionStatus
    intent: Check a redaction job's status
    question: Has my redaction job finished yet?
  phrasing_ops: 2
  slug: jira-issue-redaction-api
- baseURL: https://your-domain.atlassian.net/rest/api/2
  baseurl_source: declared
  description: This resource represents remote issue links, a way of linking Jira to information in other systems. Use it to get, create, update, and delete remote issue links either by ID or global ID. The global I
  name: Jira Issue remote links API
  phrasing_intents:
  - id: deleteRemoteIssueLinkByGlobalId
    intent: Delete a remote link by global ID
    question: Can I remove a remote link using its global ID rather than its link ID?
  - id: getRemoteIssueLinks
    intent: List an issue's remote links
    question: What external web links are attached to an issue?
  - id: createOrUpdateRemoteIssueLink
    intent: Create or upsert a remote issue link
    question: How do I attach an external link, like a support ticket, to an issue?
  - id: deleteRemoteIssueLinkById
    intent: Delete a remote issue link by ID
    question: Can I delete a remote link from an issue using its link ID?
  - id: getRemoteIssueLinkById
    intent: Get a remote issue link by ID
    question: Can I fetch a single remote link on an issue by its numeric link ID?
  - id: updateRemoteIssueLink
    intent: Update a remote issue link by ID
    question: Can I change the target of an existing remote link by its link ID?
  phrasing_ops: 6
  slug: jira-issue-remote-links-api
- baseURL: https://your-domain.atlassian.net/rest/api/2
  baseurl_source: declared
  description: This resource represents issue resolution values. Use it to obtain a list of all issue resolution values and the details of individual resolution values.
  name: Jira Issue resolutions API
  phrasing_intents:
  - id: getResolutions
    intent: List all issue resolutions
    question: What resolution values are available for issues in my Jira?
  - id: createResolution
    intent: Create an issue resolution
    question: How do I add a new resolution like 'Won't Do'?
  - id: setDefaultResolution
    intent: Set the default resolution
    question: How do I change which resolution is the default?
  - id: moveResolutions
    intent: Reorder issue resolutions
    question: How do I change the order resolutions appear in?
  - id: searchResolutions
    intent: Search resolutions with paging
    question: Can I page through resolutions or filter to specific IDs?
  - id: deleteResolution
    intent: Delete a resolution and reassign issues
    question: How do I delete a resolution that issues already use?
  - id: getResolution
    intent: Get one issue resolution
    question: How do I look up a single resolution by ID?
  - id: updateResolution
    intent: Rename or redescribe a resolution
    question: How do I rename an existing resolution?
  phrasing_ops: 8
  slug: jira-issue-resolutions-api
- baseURL: https://your-domain.atlassian.net/rest/api/2
  baseurl_source: declared
  description: This resource represents issue security levels. Use it to obtain the details of any issue security level. For more information about issue security levels, see [Configuring issue-level security](https
  name: Jira Issue security level API
  phrasing_intents:
  - id: getIssueSecurityLevelMembers
    intent: List members of security levels in a scheme
    question: Who can see issues at each security level in an issue security scheme?
  - id: getIssueSecurityLevel
    intent: Get details of an issue security level
    question: What is the name and description of a given issue security level?
  phrasing_ops: 2
  slug: jira-issue-security-level-api
- baseURL: https://your-domain.atlassian.net/rest/api/2
  baseurl_source: declared
  description: This resource represents issue security schemes. Use it to get an issue security scheme or a list of issue security schemes. Issue security schemes control which users or groups of users can view an i
  name: Jira Issue security schemes API
  phrasing_intents:
  - id: getIssueSecuritySchemes
    intent: List all issue security schemes
    question: What issue security schemes exist on my Jira site?
  - id: createIssueSecurityScheme
    intent: Create an issue security scheme
    question: How do I create a new issue security scheme to restrict who sees issues?
  - id: getSecurityLevels
    intent: List issue security levels across schemes
    question: Which security levels are defined in my issue security schemes?
  - id: setDefaultLevels
    intent: Set default security levels for schemes
    question: How do I change which security level new issues get by default in a scheme?
  - id: getSecurityLevelMembers
    intent: List members of issue security levels
    question: Who is allowed to see issues at a given security level?
  - id: searchProjectsUsingSecuritySchemes
    intent: Find projects associated with security schemes
    question: Which projects use a given issue security scheme?
  - id: associateSchemesToProjects
    intent: Assign a security scheme to a project
    question: How do I apply an issue security scheme to a project?
  - id: searchSecuritySchemes
    intent: Search issue security schemes with paging
    question: Can I search issue security schemes by ID or by the projects that use them?
  phrasing_ops: 16
  slug: jira-issue-security-schemes-api
- baseURL: https://your-domain.atlassian.net/rest/api/2
  baseurl_source: declared
  description: 'This resource represents [issue type](#api-group-Issue-types) properties, which provides for storing custom data against an issue type. Use it to get, create, and delete issue type properties as well '
  name: Jira Issue type properties API
  phrasing_intents:
  - id: getIssueTypePropertyKeys
    intent: List property keys stored on an issue type
    question: What custom properties has my app stored on an issue type?
  - id: deleteIssueTypeProperty
    intent: Delete an issue type property
    question: How do I remove custom data stored on an issue type?
  - id: getIssueTypeProperty
    intent: Read an issue type property value
    question: How do I read the value stored under a property key on an issue type?
  - id: setIssueTypeProperty
    intent: Store custom data on an issue type
    question: How can my app store its own data against an issue type?
  phrasing_ops: 4
  slug: jira-issue-type-properties-api
- baseURL: https://your-domain.atlassian.net/rest/api/2
  baseurl_source: declared
  description: 'This resource represents issue type schemes in classic projects. Use it to: * get issue type schemes and a list of the projects that use them. * associate issue type schemes with projects. * add issue'
  name: Jira Issue type schemes API
  phrasing_intents:
  - id: getAllIssueTypeSchemes
    intent: List issue type schemes
    question: What issue type schemes exist for our classic projects?
  - id: createIssueTypeScheme
    intent: Create an issue type scheme
    question: How do I create a new issue type scheme with a chosen set of issue types?
  - id: getIssueTypeSchemesMapping
    intent: List the issue types inside issue type schemes
    question: Which issue types belong to each issue type scheme?
  - id: getIssueTypeSchemeForProjects
    intent: Find the issue type scheme used by projects
    question: Which issue type scheme is a given project using?
  - id: assignIssueTypeSchemeToProject
    intent: Assign an issue type scheme to a project
    question: How do I switch a classic project to a different issue type scheme?
  - id: deleteIssueTypeScheme
    intent: Delete an issue type scheme
    question: How do I delete an issue type scheme we no longer need?
  - id: updateIssueTypeScheme
    intent: Update an issue type scheme's details
    question: How do I rename an issue type scheme or change its default issue type?
  - id: addIssueTypesToIssueTypeScheme
    intent: Add issue types to an issue type scheme
    question: How do I add more issue types to an existing issue type scheme?
  phrasing_ops: 10
  slug: jira-issue-type-schemes-api
- baseURL: https://your-domain.atlassian.net/rest/api/2
  baseurl_source: declared
  description: 'This resource represents issue type screen schemes. Use it to: * get issue type screen schemes and a list of the projects that use them. * create issue type screen schemes. * update issue type screen '
  name: Jira Issue type screen schemes API
  phrasing_intents:
  - id: getIssueTypeScreenSchemes
    intent: List issue type screen schemes
    question: What issue type screen schemes are set up on my site?
  - id: createIssueTypeScreenScheme
    intent: Create an issue type screen scheme
    question: How do I create a scheme that assigns different screen schemes to different issue types?
  - id: getIssueTypeScreenSchemeMappings
    intent: List issue type to screen scheme mappings
    question: Which screen scheme does each issue type use across my issue type screen schemes?
  - id: getIssueTypeScreenSchemeProjectAssociations
    intent: Find the issue type screen scheme for projects
    question: Which issue type screen scheme does my project use?
  - id: assignIssueTypeScreenSchemeToProject
    intent: Assign an issue type screen scheme to a project
    question: How do I apply an issue type screen scheme to a project?
  - id: deleteIssueTypeScreenScheme
    intent: Delete an issue type screen scheme
    question: How do I delete an issue type screen scheme I no longer need?
  - id: updateIssueTypeScreenScheme
    intent: Rename or redescribe an issue type screen scheme
    question: How do I rename an issue type screen scheme?
  - id: appendMappingsForIssueTypeScreenScheme
    intent: Add issue type mappings to a screen scheme
    question: How do I add another issue type to an existing issue type screen scheme?
  phrasing_ops: 11
  slug: jira-issue-type-screen-schemes-api
- baseURL: https://your-domain.atlassian.net/rest/api/2
  baseurl_source: declared
  description: This resource represents votes cast by users on an issue. Use it to get details of votes on an issue as well as cast and withdrawal votes.
  name: Jira Issue votes API
  phrasing_intents:
  - id: removeVote
    intent: Remove my vote from an issue
    question: Can I take back a vote I cast on an issue?
  - id: getVotes
    intent: See votes on an issue
    question: How many votes does an issue have, and who voted?
  - id: addVote
    intent: Vote for an issue
    question: Can I vote for an issue on my own behalf through the API?
  phrasing_ops: 3
  slug: jira-issue-votes-api
- baseURL: https://your-domain.atlassian.net/rest/api/2
  baseurl_source: declared
  description: This resource represents users watching an issue. Use it to get details of users watching an issue as well as start and stop a user watching an issue.
  name: Jira Issue watchers API
  phrasing_intents:
  - id: getIsWatchingIssueBulk
    intent: Check which of several issues I'm watching
    question: Am I watching any of these issues?
  - id: removeWatcher
    intent: Remove a watcher from an issue
    question: How do I stop a user from watching an issue?
  - id: getIssueWatchers
    intent: List who is watching an issue
    question: Who is watching this issue?
  - id: addWatcher
    intent: Add a watcher to an issue
    question: How do I add someone as a watcher on an issue?
  phrasing_ops: 4
  slug: jira-issue-watchers-api
- baseURL: https://your-domain.atlassian.net/rest/api/2
  baseurl_source: declared
  description: This resource represents [issue worklog](#api-group-Issue-worklogs) properties, which provides for storing custom data against an issue worklog. Use it to get, create, and delete issue worklog propert
  name: Jira Issue worklog properties API
  phrasing_intents:
  - id: getWorklogPropertyKeys
    intent: List a worklog's property keys
    question: What custom property keys are stored on a worklog?
  - id: deleteWorklogProperty
    intent: Delete a worklog property
    question: Can I remove custom data I stored on a worklog?
  - id: getWorklogProperty
    intent: Read a worklog property
    question: What value is stored under a property key on a worklog?
  - id: setWorklogProperty
    intent: Store a property on a worklog
    question: Can I store my own JSON data on a worklog entry?
  phrasing_ops: 4
  slug: jira-issue-worklog-properties-api
- baseURL: https://your-domain.atlassian.net/rest/api/2
  baseurl_source: declared
  description: This resource is a collection of operations for [Jira expressions](https://developer.atlassian.com/cloud/jira/platform/jira-expressions/).
  name: Jira Jira expressions API
  phrasing_intents:
  - id: analyseExpression
    intent: Analyse and validate Jira expressions
    question: Is my Jira expression syntactically valid before I use it?
  - id: evaluateJiraExpression
    intent: Evaluate an expression (legacy eval, being removed)
    question: Does the old strongly consistent eval endpoint still evaluate expressions?
  - id: evaluateJSISJiraExpression
    intent: Evaluate an expression with enhanced search
    question: How do I evaluate an expression that runs JQL using the enhanced search API?
  phrasing_ops: 3
  slug: jira-jira-expressions-api
- baseURL: https://your-domain.atlassian.net/rest/api/2
  baseurl_source: declared
  description: This resource represents various settings in Jira. Use it to get and update Jira settings and properties.
  name: Jira Jira settings API
  phrasing_intents:
  - id: getApplicationProperty
    intent: Get application properties
    question: What editable application properties does my Jira have?
  - id: getAdvancedSettings
    intent: Get advanced settings
    question: Which properties appear on Jira's Advanced Settings page?
  - id: setApplicationProperty
    intent: Change an application property
    question: How do I change the clone prefix or another editable application property?
  - id: getConfiguration
    intent: Get global Jira settings
    question: Are subtasks and time tracking enabled on my Jira site?
  phrasing_ops: 4
  slug: jira-jira-settings-api
- baseURL: https://your-domain.atlassian.net/rest/api/2
  baseurl_source: declared
  description: This resource represents JQL search auto-complete details. Use it to obtain JQL search auto-complete data and suggestions for use in programmatic construction of queries or custom query builders. It a
  name: Jira JQL API
  phrasing_intents:
  - id: getAutoComplete
    intent: Get JQL field and function reference data
    question: What fields and functions can I use when writing JQL searches?
  - id: getAutoCompletePost
    intent: Get JQL reference data for specific projects
    question: Can I get JQL field reference data limited to certain projects?
  - id: getFieldAutoCompleteForQueryString
    intent: Suggest JQL values for a field
    question: What values can I type for a field in a JQL query?
  - id: parseJqlQueries
    intent: Parse and validate JQL queries
    question: How can I check whether a JQL query is valid before running it?
  - id: migrateQueries
    intent: Convert usernames in JQL to account IDs
    question: How do I make stored JQL queries GDPR compliant by replacing usernames?
  - id: sanitiseJqlQueries
    intent: Hide details a user can't see in JQL
    question: How do I strip project names a user isn't allowed to see out of a JQL query?
  phrasing_ops: 6
  slug: jira-jql-api
- baseURL: https://your-domain.atlassian.net/rest/api/2
  baseurl_source: declared
  description: This resource represents JQL function's precomputations. Precomputation is a mapping between custom function call and JQL fragment returned by this function. Use it to get and update precomputations.
  name: Jira JQL functions (apps) API
  phrasing_intents:
  - id: getPrecomputations
    intent: List an app's JQL function precomputations
    question: What precomputed values exist for my app's custom JQL function?
  - id: updatePrecomputations
    intent: Update JQL function precomputation values
    question: How does my app update the precomputed JQL fragment for a custom function?
  - id: getPrecomputationsByID
    intent: Look up JQL precomputations by ID
    question: Can I fetch specific JQL function precomputations by their IDs?
  phrasing_ops: 3
  slug: jira-jql-functions-apps-api
- baseURL: https://your-domain.atlassian.net/rest/api/2
  baseurl_source: declared
  description: This resource represents available labels. Use it to get available labels for the global label field.
  name: Jira Labels API
  phrasing_intents:
  - id: getAllLabels
    intent: List all labels
    question: What labels are in use across Jira?
  phrasing_ops: 1
  slug: jira-labels-api
- baseURL: https://your-domain.atlassian.net/rest/api/2
  baseurl_source: declared
  description: This resource represents license metrics. Use it to get available metrics for Jira licences.
  name: Jira License metrics API
  phrasing_intents:
  - id: getLicense
    intent: Get the Jira instance's license details
    question: What licenses does our Jira instance have?
  - id: getApproximateLicenseCount
    intent: Get approximate user count across all licenses
    question: Roughly how many user accounts are counted across all our Jira licenses?
  - id: getApproximateApplicationLicenseCount
    intent: Get approximate user count for one Jira product
    question: How many users are counted against a single Jira product license?
  phrasing_ops: 3
  slug: jira-license-metrics-api
- baseURL: https://your-domain.atlassian.net/rest/api/2
  baseurl_source: declared
  description: This resource supports the migration of some Connect modules to their equivalent Forge modules.
  name: Jira Migration of Connect modules to Forge API
  phrasing_intents:
  - id: ConnectToForgeMigrationFetchTaskResource.fetchMigrationTask_get
    intent: Check a Connect issue field's Forge migration
    question: How far along is the migration of my Connect issue field to Forge?
  - id: ConnectToForgeMigrationTaskSubmissionResource.submitTask_post
    intent: Start migrating a Connect issue field to Forge
    question: How do I trigger migration of a Connect issue field to its Forge custom field?
  phrasing_ops: 2
  slug: jira-migration-of-connect-modules-to-forge-api
- baseURL: https://your-domain.atlassian.net/rest/api/2
  baseurl_source: declared
  description: This resource represents information about the current user, such as basic details, group membership, application roles, preferences, and locale. Use it to get, create, update, and delete (restore def
  name: Jira Myself API
  phrasing_intents:
  - id: removePreference
    intent: Delete one of my user preferences
    question: How do I restore a system preference to its default value?
  - id: getPreference
    intent: Get one of my user preferences
    question: What value is set for one of my Jira user preferences?
  - id: setPreference
    intent: Set one of my user preferences
    question: How do I change a user preference like email notification format?
  - id: getLocale
    intent: Get my locale
    question: What locale is my account using?
  - id: setLocale
    intent: Set my locale (deprecated)
    question: Can I still change my language locale through the deprecated my-preferences endpoint?
  - id: getCurrentUser
    intent: Get the current user
    question: Who am I logged in as, and what is my account ID?
  phrasing_ops: 6
  slug: jira-myself-api
- baseURL: https://your-domain.atlassian.net/rest/api/2
  baseurl_source: declared
  description: APIs related to integrating Incident and Post-Incident Review (PIR) data with Jira Software. These APIs are available to Atlassian Connect apps. To use these APIs you must have the `jiraOperationsInfo
  name: Jira Operations API
  phrasing_intents:
  - id: submitOperationsWorkspaces
    intent: Link Operations workspaces to the Jira site
    question: How does my app link its Operations workspace IDs to a Jira site?
  - id: deleteWorkspaces
    intent: Unlink Operations workspaces in bulk
    question: How do I unlink Operations workspaces from a Jira site in bulk?
  - id: getWorkspaces
    intent: List linked Operations workspaces
    question: Which Operations workspace IDs are linked to my Jira site?
  - id: submitEntity
    intent: Send incident or post-incident review data
    question: How does my ops tool push incident and review data into Jira?
  - id: deleteEntityByProperty
    intent: Delete incidents and reviews by property
    question: Can I bulk delete incident data that matches certain properties?
  - id: getIncidentById
    intent: Get a stored incident
    question: How do I read back an incident my app sent to Jira?
  - id: deleteIncidentById
    intent: Delete a stored incident
    question: How do I delete a single incident my app submitted?
  - id: getReviewById
    intent: Get a post-incident review
    question: How do I fetch a post-incident review my app stored in Jira?
  phrasing_ops: 9
  slug: jira-operations-api
- baseURL: https://your-domain.atlassian.net/rest/api/2
  baseurl_source: declared
  description: The Organization API from Jira — 6 operation(s) for organization.
  name: Jira Organization API
  phrasing_intents:
  - id: getOrganizations
    intent: List all organizations in Service Management
    question: What customer organizations exist across my whole Jira Service Management instance?
  - id: createOrganization
    intent: Create a customer organization
    question: How do I create a new customer organization in the service desk?
  - id: deleteOrganization
    intent: Delete a customer organization
    question: How do I delete a customer organization entirely?
  - id: getOrganization
    intent: Get an organization's details
    question: What are the details of a specific customer organization?
  - id: getPropertiesKeys
    intent: List an organization's property keys
    question: What custom properties has my app stored against an organization?
  - id: deleteProperty
    intent: Remove an organization property
    question: How do I delete custom data stored on an organization?
  - id: getProperty
    intent: Read an organization property value
    question: How do I read the JSON stored in one organization property?
  - id: setProperty
    intent: Store custom data on an organization
    question: How can my app store custom data against a customer organization?
  phrasing_ops: 14
  slug: jira-organization-api
- baseURL: https://your-domain.atlassian.net/rest/api/2
  baseurl_source: declared
  description: This resource represents permission schemes. Use it to get, create, update, and delete permission schemes as well as get, create, update, and delete details of the permissions granted in those schemes
  name: Jira Permission schemes API
  phrasing_intents:
  - id: getAllPermissionSchemes
    intent: List all permission schemes
    question: What permission schemes exist on my Jira site?
  - id: createPermissionScheme
    intent: Create a permission scheme
    question: How do I create a new permission scheme for a set of projects?
  - id: deletePermissionScheme
    intent: Delete a permission scheme
    question: How do I delete a permission scheme that's no longer needed?
  - id: getPermissionScheme
    intent: Get a permission scheme
    question: What does a particular permission scheme contain?
  - id: updatePermissionScheme
    intent: Update a permission scheme
    question: Will sending a permissions list when updating a scheme overwrite all existing grants?
  - id: getPermissionSchemeGrants
    intent: List grants in a permission scheme
    question: Who is granted which permissions in a given scheme?
  - id: createPermissionGrant
    intent: Add a permission grant to a scheme
    question: How do I give a group Browse Projects permission in a scheme?
  - id: deletePermissionSchemeEntity
    intent: Remove a grant from a permission scheme
    question: How do I revoke one permission grant from a scheme?
  phrasing_ops: 9
  slug: jira-permission-schemes-api
- baseURL: https://your-domain.atlassian.net/rest/api/2
  baseurl_source: declared
  description: This resource represents permissions. Use it to obtain details of all permissions and determine whether the user has certain permissions.
  name: Jira Permissions API
  phrasing_intents:
  - id: getMyPermissions
    intent: Check my permissions
    question: Do I have permission to edit issues in a certain project?
  - id: getAllPermissions
    intent: List all permissions defined in Jira
    question: What global and project permissions exist on the instance?
  - id: getBulkPermissions
    intent: Check a user's permissions in bulk
    question: Which of a set of projects and issues can a given user browse or edit?
  - id: getPermittedProjects
    intent: List projects where I hold given permissions
    question: In which projects am I allowed to create issues?
  phrasing_ops: 4
  slug: jira-permissions-api
- baseURL: https://your-domain.atlassian.net/rest/api/2
  baseurl_source: declared
  description: This resource represents plans. Use it to get, create, duplicate, update, trash and archive plans.
  name: Jira Plans API
  phrasing_intents:
  - id: getPlans
    intent: List plans
    question: What plans exist in Jira?
  - id: createPlan
    intent: Create a plan
    question: How do I create a new plan from boards, projects or filters?
  - id: getPlan
    intent: Get a plan
    question: What are the issue sources and scheduling settings of a plan?
  - id: updatePlan
    intent: Update a plan's details
    question: Can I change a plan's name, lead or estimation unit?
  - id: archivePlan
    intent: Archive a plan
    question: How do I archive a plan that's finished?
  - id: duplicatePlan
    intent: Duplicate a plan
    question: Can I make a copy of an existing plan?
  - id: trashPlan
    intent: Move a plan to trash
    question: How do I send a plan to the trash?
  phrasing_ops: 7
  slug: jira-plans-api
- baseURL: https://your-domain.atlassian.net/rest/api/2
  baseurl_source: declared
  description: This resource represents issue priority schemes. Use it to get priority schemes and related information, and to create, update and delete priority schemes.
  name: Jira Priority schemes API
  phrasing_intents:
  - id: getPrioritySchemes
    intent: List priority schemes
    question: What priority schemes are configured in Jira?
  - id: createPriorityScheme
    intent: Create a priority scheme
    question: How do I create a priority scheme with its own set of priorities?
  - id: suggestedPrioritiesForMappings
    intent: Preview priorities that need remapping
    question: If I change a priority scheme, which priorities will need mapping to new ones?
  - id: getAvailablePrioritiesByPriorityScheme
    intent: List priorities available to add to a scheme
    question: Which priorities can I still add to a priority scheme?
  - id: deletePriorityScheme
    intent: Delete a priority scheme
    question: Can I delete a priority scheme that still has projects attached?
  - id: updatePriorityScheme
    intent: Update a priority scheme
    question: How can I change the default priority of an existing priority scheme?
  - id: getPrioritiesByPriorityScheme
    intent: List priorities in a priority scheme
    question: Which priorities are included in a given priority scheme?
  - id: getProjectsByPriorityScheme
    intent: List projects using a priority scheme
    question: Which projects use a particular priority scheme?
  phrasing_ops: 8
  slug: jira-priority-schemes-api
- baseURL: https://your-domain.atlassian.net/rest/api/2
  baseurl_source: declared
  description: This resource represents avatars associated with a project. Use it to get, load, set, and remove project avatars.
  name: Jira Project avatars API
  phrasing_intents:
  - id: updateProjectAvatar
    intent: Choose the avatar a project displays
    question: How do I switch which avatar a project shows?
  - id: deleteProjectAvatar
    intent: Delete a custom project avatar
    question: How do I remove a custom avatar I uploaded to a project?
  - id: createProjectAvatar
    intent: Upload a custom avatar to a project
    question: How do I upload our logo as a project avatar?
  - id: getAllProjectAvatars
    intent: List a project's system and custom avatars
    question: Which avatars can a project choose from, including ones we uploaded?
  phrasing_ops: 4
  slug: jira-project-avatars-api
- baseURL: https://your-domain.atlassian.net/rest/api/2
  baseurl_source: declared
  description: This resource represents project categories. Use it to create, update, and delete project categories as well as obtain a list of all project categories and details of individual categories. For more i
  name: Jira Project categories API
  phrasing_intents:
  - id: getAllProjectCategories
    intent: List project categories
    question: What project categories exist in my Jira?
  - id: createProjectCategory
    intent: Create a project category
    question: How do I create a category for grouping projects?
  - id: removeProjectCategory
    intent: Delete a project category
    question: How do I delete a project category I no longer need?
  - id: getProjectCategoryById
    intent: Get a project category
    question: How do I look up one project category by ID?
  - id: updateProjectCategory
    intent: Update a project category
    question: How do I rename a project category?
  phrasing_ops: 5
  slug: jira-project-categories-api
- baseURL: https://your-domain.atlassian.net/rest/api/2
  baseurl_source: declared
  description: This resource represents classification levels used in a project. Use it to view and manage classification levels in your projects.
  name: Jira Project classification levels API
  phrasing_intents:
  - id: getProjectClassificationConfig
    intent: Get a project's full classification settings
    question: Which data classification levels are permitted in my project, and is there an override?
  - id: removeDefaultProjectClassification
    intent: Remove a project's default classification level
    question: How do I clear the default data classification from a project?
  - id: getDefaultProjectClassification
    intent: Get a project's default classification level
    question: What data classification level do new issues in a project get by default?
  - id: updateDefaultProjectClassification
    intent: Set a project's default classification level
    question: How do I set a default data classification level on a project?
  phrasing_ops: 4
  slug: jira-project-classification-levels-api
- baseURL: https://your-domain.atlassian.net/rest/api/2
  baseurl_source: declared
  description: This resource represents project components. Use it to get, create, update, and delete project components. Also get components for project and get a count of issues by component.
  name: Jira Project components API
  phrasing_intents:
  - id: findComponentsForProjects
    intent: Find components across several projects
    question: Which components exist across a set of projects, including Compass components?
  - id: createComponent
    intent: Create a component in a project
    question: How do I add a new component to a project?
  - id: deleteComponent
    intent: Delete a component
    question: How do I delete a component from a project?
  - id: getComponent
    intent: Get a component's details
    question: Who is the lead of a particular component?
  - id: updateComponent
    intent: Update a component
    question: Can I rename a component or change its lead?
  - id: getComponentRelatedIssues
    intent: Count issues assigned to a component
    question: How many issues are assigned to a component?
  - id: getProjectComponentsPaginated
    intent: Page through a project's components
    question: Can I page through a project's components and filter them by name?
  - id: getProjectComponents
    intent: List all components in a project at once
    question: How do I get every component of a project in one unpaginated list?
  phrasing_ops: 8
  slug: jira-project-components-api
- baseURL: https://your-domain.atlassian.net/rest/api/2
  baseurl_source: declared
  description: This resource represents the email address used to send a project's notifications. Use it to get and set the [project's sender email address](https://confluence.atlassian.com/x/dolKLg).
  name: Jira Project email API
  phrasing_intents:
  - id: getProjectEmail
    intent: Get a project's sender email
    question: Which email address do notifications from a project come from?
  - id: updateProjectEmail
    intent: Set a project's sender email
    question: How do I change the address a project sends notifications from?
  phrasing_ops: 2
  slug: jira-project-email-api
- baseURL: https://your-domain.atlassian.net/rest/api/2
  baseurl_source: declared
  description: This resource represents project features. Use it to get the list of features for a project and modify the state of a feature. The project feature endpoint is available only for Jira Software, both fo
  name: Jira Project features API
  phrasing_intents:
  - id: getFeaturesForProject
    intent: List a project's features
    question: Which features are turned on for a project?
  - id: toggleFeatureForProject
    intent: Turn a project feature on or off
    question: Can I enable or disable a feature for a single project?
  phrasing_ops: 2
  slug: jira-project-features-api
- baseURL: https://your-domain.atlassian.net/rest/api/2
  baseurl_source: declared
  description: This resource provides validation for project keys and names.
  name: Jira Project key and name validation API
  phrasing_intents:
  - id: validateProjectKey
    intent: Check whether a project key is valid and free
    question: Is a project key I want already taken or invalid?
  - id: getValidProjectKey
    intent: Get a usable project key, generated if needed
    question: Can Jira suggest a free project key if mine is already taken?
  - id: getValidProjectName
    intent: Get an unused project name
    question: Is a project name already in use on my site?
  phrasing_ops: 3
  slug: jira-project-key-and-name-validation-api
- baseURL: https://your-domain.atlassian.net/rest/api/2
  baseurl_source: declared
  description: 'This resource represents permission schemes for a project. Use this resource to: * get details of a project''s issue security levels available to the calling user. * get the permission scheme associate'
  name: Jira Project permission schemes API
  phrasing_intents:
  - id: getProjectIssueSecurityScheme
    intent: Get a project's issue security scheme
    question: Which issue security scheme is attached to my project?
  - id: getAssignedPermissionScheme
    intent: Get the permission scheme a project uses
    question: What permission scheme is my project using?
  - id: assignPermissionScheme
    intent: Assign a permission scheme to a project
    question: How do I switch a project to a different permission scheme?
  - id: getSecurityLevelsForProject
    intent: List a project's issue security levels
    question: What security levels can I set on issues in this project?
  phrasing_ops: 4
  slug: jira-project-permission-schemes-api
- baseURL: https://your-domain.atlassian.net/rest/api/2
  baseurl_source: declared
  description: This resource represents [project](#api-group-Projects) properties, which provides for storing custom data against a project. Use it to get, create, and delete project properties as well as get a list
  name: Jira Project properties API
  phrasing_intents:
  - id: getProjectPropertyKeys
    intent: List a project's property keys
    question: What custom property keys are stored on a project?
  - id: deleteProjectProperty
    intent: Delete a project property
    question: Can I remove a custom property from a project?
  - id: getProjectProperty
    intent: Read a project property
    question: What value is saved under a given property key on a project?
  - id: setProjectProperty
    intent: Store a property on a project
    question: Can I store custom JSON data against a project without a database?
  phrasing_ops: 4
  slug: jira-project-properties-api
- baseURL: https://your-domain.atlassian.net/rest/api/2
  baseurl_source: declared
  description: This resource represents the users assigned to [project roles](#api-group-Issue-comments). Use it to get, add, and remove default users from project roles. Also use it to add and remove users from a p
  name: Jira Project role actors API
  phrasing_intents:
  - id: deleteActor
    intent: Remove a user or group from a project role
    question: How do I take a person out of a role in one specific project?
  - id: addActorUsers
    intent: Add users or groups to a project role
    question: How do I add someone to a project role without removing current members?
  - id: setActors
    intent: Replace all actors in a project role
    question: How do I overwrite everyone in a project role with a new set of users and groups?
  - id: deleteProjectRoleActorsFromRole
    intent: Remove default actors from a project role
    question: How do I stop a user being added to a role by default in new projects?
  - id: getProjectRoleActorsForRole
    intent: List a project role's default actors
    question: Who are the default members of a project role for new projects?
  - id: addProjectRoleActorsToRole
    intent: Add default actors to a project role
    question: How do I make a group a default member of a role for all future projects?
  phrasing_ops: 6
  slug: jira-project-role-actors-api
- baseURL: https://your-domain.atlassian.net/rest/api/2
  baseurl_source: declared
  description: This resource represents the roles that users can play in projects. Use this resource to get, create, update, and delete project roles.
  name: Jira Project roles API
  phrasing_intents:
  - id: getProjectRoles
    intent: List the roles in a project
    question: What project roles exist in a given project?
  - id: getProjectRole
    intent: See who holds a role in a project
    question: Who are the users and groups in the Developers role of my project?
  - id: getProjectRoleDetails
    intent: Get details of every role for a project
    question: Which project roles am I a member of in this project?
  - id: getAllProjectRoles
    intent: List all project roles site-wide
    question: What project roles are defined across the whole Jira site?
  - id: createProjectRole
    intent: Create a new project role
    question: How do I define a new project role like QA Lead?
  - id: deleteProjectRole
    intent: Delete a project role
    question: How do I delete a project role that's still in use?
  - id: getProjectRoleById
    intent: Get a project role and its default actors
    question: Which default actors are attached to a specific project role?
  - id: partialUpdateProjectRole
    intent: Change only a project role's name or description
    question: How do I rename a project role without touching its description?
  phrasing_ops: 9
  slug: jira-project-roles-api
- baseURL: https://your-domain.atlassian.net/rest/api/2
  baseurl_source: declared
  description: This resource represents project templates. Use it to create a new project from a custom template.
  name: Jira Project templates API
  phrasing_intents:
  - id: createProjectWithCustomTemplate
    intent: Create a project from a custom template
    question: How do I create a project whose configuration comes from a custom template?
  - id: editTemplate
    intent: Edit a custom project template
    question: Can I rename or re-describe a saved custom project template?
  - id: liveTemplate
    intent: Get a custom project template
    question: What does a live custom project template contain?
  - id: removeTemplate
    intent: Delete a custom project template
    question: How do I delete a custom project template I no longer want?
  - id: saveTemplate
    intent: Save a project as a custom template
    question: Can I turn an existing project's setup into a reusable template?
  phrasing_ops: 5
  slug: jira-project-templates-api
- baseURL: https://your-domain.atlassian.net/rest/api/2
  baseurl_source: declared
  description: This resource represents project types. Use it to obtain a list of all project types, a list of project types accessible to the calling user, and details of a project type.
  name: Jira Project types API
  phrasing_intents:
  - id: getAllProjectTypes
    intent: List all project types
    question: What project types exist, licensed or not?
  - id: getAllAccessibleProjectTypes
    intent: List licensed project types
    question: Which project types does my site have a valid license for?
  - id: getProjectTypeByKey
    intent: Get a project type by key
    question: How do I look up a project type like software or business by key?
  - id: getAccessibleProjectTypeByKey
    intent: Check a project type is accessible to me
    question: Is a particular project type accessible to my user?
  phrasing_ops: 4
  slug: jira-project-types-api
- baseURL: https://your-domain.atlassian.net/rest/api/2
  baseurl_source: declared
  description: This resource represents project versions. Use it to get, get lists of, create, update, move, merge, and delete project versions. This resource also provides counts of issues by version.
  name: Jira Project versions API
  phrasing_intents:
  - id: getProjectVersionsPaginated
    intent: Page through a project's versions
    question: Can I search a project's versions by name and filter to released or archived ones?
  - id: getProjectVersions
    intent: Get all versions of a project unpaginated
    question: Can I get every version of a project in one unpaginated response?
  - id: createVersion
    intent: Create a project version
    question: How do I add a new release version to a project?
  - id: deleteVersion
    intent: Delete a version (legacy)
    question: Can I delete a version and move its fix-version issues somewhere else using the older delete endpoint?
  - id: getVersion
    intent: Get a project version
    question: What are the dates and release status of a particular version?
  - id: updateVersion
    intent: Update or release a project version
    question: Can I mark an existing version as released?
  - id: mergeVersions
    intent: Merge one version into another
    question: Can I merge two versions so all fix-version references point at one?
  - id: moveVersion
    intent: Reorder a version in a project
    question: Can I change the display order of versions in a project?
  phrasing_ops: 15
  slug: jira-project-versions-api
- baseURL: https://your-domain.atlassian.net/rest/api/2
  baseurl_source: declared
  description: APIs related to integrating remote link data with Jira Software. These APIs are available to Atlassian Connect apps. To use these APIs you must have the `jiraRemoteLinkInfoProvider` module in your Con
  name: Jira Remote Links API
  phrasing_intents:
  - id: submitRemoteLinks
    intent: Submit remote link data
    question: How does my app push remote links into Jira?
  - id: deleteRemoteLinksByProperty
    intent: Delete remote links matching properties
    question: Can I bulk delete every remote link tagged with a given property?
  - id: getRemoteLinkById
    intent: Get a remote link by ID
    question: What data is currently stored for a particular remote link?
  - id: deleteRemoteLinkById
    intent: Delete a remote link by ID
    question: How do I remove a single remote link my app submitted?
  phrasing_ops: 4
  slug: jira-remote-links-api
- baseURL: https://your-domain.atlassian.net/rest/api/2
  baseurl_source: declared
  description: The Request API from Jira — 18 operation(s) for request.
  name: Jira Request API
  phrasing_intents:
  - id: getCustomerRequests
    intent: List my service desk customer requests
    question: Which customer requests have I raised or participate in across all service desks?
  - id: createCustomerRequest
    intent: Raise a customer request in a service desk
    question: How do I raise a new customer request in a Jira Service Management desk?
  - id: validateCustomerRequest
    intent: Check a customer request payload without creating it
    question: Can I test whether a customer request payload is valid before actually submitting it?
  - id: getCustomerRequestByIdOrKey
    intent: Get one customer request
    question: How can I look up a single service desk request by its key?
  - id: getApprovals
    intent: List approvals on a customer request
    question: Which approvals are attached to this service desk request?
  - id: getApprovalById
    intent: Check the status and approvers of one approval
    question: Who are the approvers on a specific approval, and has it been decided yet?
  - id: answerApproval
    intent: Approve or decline an approval
    question: How do I approve or decline a pending approval assigned to me on a request?
  - id: getAttachmentsForRequest
    intent: List attachments on a customer request
    question: Which files have been attached to a customer request?
  phrasing_ops: 29
  slug: jira-request-api
- baseURL: https://your-domain.atlassian.net/rest/api/2
  baseurl_source: declared
  description: The Rest API from Jira — 4 operation(s) for rest.
  name: Jira Rest API
  phrasing_intents:
  - id: getWorklogsByIssueIdAndWorklogId
    intent: Bulk fetch worklogs by issue and worklog ID
    question: Can an internal service fetch many worklogs at once from issue and worklog ID pairs?
  - id: createCustomer
    intent: Create a service desk customer account (internal)
    question: Is there an internal endpoint that creates a customer account without a user context token?
  - id: viewArticle
    intent: View a knowledge base article
    question: How do I open a single knowledge base article by its page ID?
  - id: addCustomers
    intent: Add customers to a service desk (internal)
    question: Is there an internal route to add customers to a service desk without a user context?
  phrasing_ops: 4
  slug: jira-rest-api
- baseURL: https://your-domain.atlassian.net/rest/api/2
  baseurl_source: declared
  description: This resource represents screen schemes in classic projects. Use it to get, create, update, and delete screen schemes.
  name: Jira Screen schemes API
  phrasing_intents:
  - id: getScreenSchemes
    intent: List screen schemes
    question: What screen schemes are defined for my classic projects?
  - id: createScreenScheme
    intent: Create a screen scheme
    question: How do I create a screen scheme that sets different screens for create, edit and view?
  - id: deleteScreenScheme
    intent: Delete a screen scheme
    question: How do I delete a screen scheme?
  - id: updateScreenScheme
    intent: Update a screen scheme
    question: How do I rename a screen scheme?
  phrasing_ops: 4
  slug: jira-screen-schemes-api
- baseURL: https://your-domain.atlassian.net/rest/api/2
  baseurl_source: declared
  description: This resource represents the screen tab fields used to record issue details. Use it to get, add, move, and remove fields from screen tabs.
  name: Jira Screen tab fields API
  phrasing_intents:
  - id: getAllScreenTabFields
    intent: List the fields on a screen tab
    question: Which fields are on a particular tab of a screen?
  - id: addScreenTabField
    intent: Add a field to a screen tab
    question: How do I add a field to a specific tab on a screen?
  - id: removeScreenTabField
    intent: Remove a field from a screen tab
    question: How do I take a field off a screen tab?
  - id: moveScreenTabField
    intent: Reorder a field on a screen tab
    question: How do I change the order of fields on a screen tab?
  phrasing_ops: 4
  slug: jira-screen-tab-fields-api
- baseURL: https://your-domain.atlassian.net/rest/api/2
  baseurl_source: declared
  description: This resource represents the screen tabs used to record issue details. Use it to get, create, update, move, and delete screen tabs.
  name: Jira Screen tabs API
  phrasing_intents:
  - id: getBulkScreenTabs
    intent: List tabs across many screens
    question: How do I get the tabs for several screens in one request?
  - id: getAllScreenTabs
    intent: List the tabs on one screen
    question: What tabs does a particular screen have?
  - id: addScreenTab
    intent: Add a tab to a screen
    question: How do I add a new tab to a Jira screen?
  - id: deleteScreenTab
    intent: Delete a screen tab
    question: How do I remove a tab from a screen?
  - id: renameScreenTab
    intent: Rename a screen tab
    question: How do I rename a tab on a screen?
  - id: moveScreenTab
    intent: Reorder a tab on a screen
    question: How do I change the order of tabs on a screen?
  phrasing_ops: 6
  slug: jira-screen-tabs-api
- baseURL: https://your-domain.atlassian.net/rest/api/2
  baseurl_source: declared
  description: 'This resource represents the screens used to record issue details. Use it to: * get details of all screens. * get details of all the fields available for use on screens. * create screens. * delete scr'
  name: Jira Screens API
  phrasing_intents:
  - id: getScreensForField
    intent: List the screens a field appears on
    question: Which screens is a particular field used on?
  - id: getScreens
    intent: List or search screens
    question: What screens are configured on my Jira site?
  - id: createScreen
    intent: Create a screen
    question: How do I create a new screen?
  - id: addFieldToDefaultScreen
    intent: Add a field to the default screen
    question: How do I put a field on the default screen's default tab?
  - id: deleteScreen
    intent: Delete a screen
    question: How do I delete a screen I no longer use?
  - id: updateScreen
    intent: Rename or redescribe a screen
    question: Can I rename a screen used in a classic project?
  - id: getAvailableScreenFields
    intent: List fields that can be added to a screen
    question: Which fields could I still add to a screen?
  phrasing_ops: 7
  slug: jira-screens-api
- baseURL: https://your-domain.atlassian.net/rest/api/2
  baseurl_source: declared
  description: Send security information to Jira Software and enable your teams to turn unplanned vulnerabilities into planned and tracked work. Security is everyone's responsibility, and the security feature in Jir
  name: Jira Security Information API
  phrasing_intents:
  - id: submitWorkspaces
    intent: Link security workspaces to the Jira site
    question: How does my security app link its workspaces to a Jira site?
  - id: deleteLinkedWorkspaces
    intent: Unlink security workspaces from Jira
    question: How do I disconnect security workspaces from a Jira site in bulk?
  - id: getLinkedWorkspaces
    intent: List linked security workspaces
    question: Which security workspaces are currently linked to my Jira site?
  - id: getLinkedWorkspaceById
    intent: Get one linked security workspace
    question: Is a specific security workspace linked to my Jira site?
  - id: submitVulnerabilities
    intent: Send vulnerability data to Jira
    question: How does my security tool push vulnerabilities into Jira?
  - id: deleteVulnerabilitiesByProperty
    intent: Bulk delete vulnerabilities by property
    question: How do I delete all vulnerabilities I tagged with a certain property?
  - id: getVulnerabilityById
    intent: Get a stored vulnerability by ID
    question: How do I check what vulnerability data Jira has stored for an ID?
  - id: deleteVulnerabilityById
    intent: Delete a vulnerability by ID
    question: How do I remove one vulnerability from Jira?
  phrasing_ops: 8
  slug: jira-security-information-api
- baseURL: https://your-domain.atlassian.net/rest/api/2
  baseurl_source: declared
  description: This resource provides information about the Jira instance.
  name: Jira Server info API
  phrasing_intents:
  - id: getServerInfo
    intent: Get Jira instance info
    question: What version and deployment type is my Jira instance?
  phrasing_ops: 1
  slug: jira-server-info-api
- baseURL: https://your-domain.atlassian.net/rest/api/2
  baseurl_source: declared
  description: This resource represents a service registry. Use it to retrieve attributes related to a [service registry](https://support.atlassian.com/jira-service-management-cloud/docs/what-is-services/) in JSM.
  name: Jira Service Registry API
  phrasing_intents:
  - id: ServiceRegistryResource.services_get
    intent: Get attributes of service registry entries
    question: What attributes are recorded for specific services in the service registry?
  phrasing_ops: 1
  slug: jira-service-registry-api
- baseURL: https://your-domain.atlassian.net/rest/api/2
  baseurl_source: declared
  description: The Servicedesk API from Jira — 16 operation(s) for servicedesk.
  name: Jira Servicedesk API
  phrasing_intents:
  - id: getServiceDesks
    intent: List all accessible service desks
    question: Which service desks can I access in our Jira Service Management instance?
  - id: getServiceDeskById
    intent: Get details of one service desk
    question: What are the details of a specific service desk if I only have its ID?
  - id: attachTemporaryFile
    intent: Upload a temporary attachment to a service desk
    question: How do I upload a file to a service desk before attaching it to a customer request?
  - id: removeCustomers
    intent: Remove customers from a service desk
    question: How do I take customers off a closed-access service desk?
  - id: getCustomers
    intent: List customers on a service desk
    question: Who are the customers registered on a given service desk?
  - id: addCustomers
    intent: Add existing users as service desk customers
    question: How do I give existing users customer access to a service desk?
  - id: inviteCustomer
    intent: Invite a new customer by email
    question: How do I email an invitation to someone so they can use our help center?
  - id: getArticles
    intent: Search a service desk's knowledge base articles
    question: Which knowledge base articles linked to a service desk mention a given topic?
  phrasing_ops: 22
  slug: jira-servicedesk-api
- baseURL: https://your-domain.atlassian.net/rest/api/2
  baseurl_source: declared
  description: Apis related to sprints
  name: Jira Sprint API
  phrasing_intents:
  - id: createSprint
    intent: Create a future sprint on a board
    question: How do I create a new sprint on my Jira board?
  - id: deleteSprint
    intent: Delete a sprint
    question: What happens to open issues when I delete a sprint?
  - id: getSprint
    intent: Get a sprint's details
    question: What are the dates, state and goal of a particular sprint?
  - id: partiallyUpdateSprint
    intent: Change selected fields of a sprint
    question: Can I change just a sprint's goal without touching its other fields?
  - id: updateSprint
    intent: Replace all fields of a sprint
    question: How do I do a full update of a sprint where missing fields get cleared?
  - id: getIssuesForSprint
    intent: List issues in a sprint
    question: Which issues are in the current sprint, ordered by rank?
  - id: moveIssuesToSprintAndRank
    intent: Move issues into a sprint
    question: How do I pull issues from the backlog into an active sprint?
  - id: getIssuesForSprintJSIS
    intent: List sprint issues with token paging
    question: Is there a sprint issue listing that pages with a nextPageToken instead of startAt?
  phrasing_ops: 13
  slug: jira-sprint-api
- baseURL: https://your-domain.atlassian.net/rest/api/2
  baseurl_source: declared
  description: This resource represents statuses. Use it to search, get, create, delete, and change statuses.
  name: Jira Status API
  phrasing_intents:
  - id: deleteStatusesById
    intent: Bulk delete statuses
    question: How do I delete workflow statuses I no longer need?
  - id: getStatusesById
    intent: Get statuses by ID
    question: How do I look up several workflow statuses by their IDs?
  - id: createStatuses
    intent: Create statuses globally or for a project
    question: How do I add new workflow statuses for one project only?
  - id: updateStatuses
    intent: Bulk update statuses
    question: How do I rename several workflow statuses at once?
  - id: getStatusesByName
    intent: Get statuses by name
    question: How do I find a status's ID when I only know its name?
  - id: search
    intent: Search statuses by name, project or category
    question: Which statuses are in the Done category?
  - id: getProjectIssueTypeUsagesForStatus
    intent: List issue types using a status in a project
    question: Which issue types in a project use a given status?
  - id: getProjectUsagesForStatus
    intent: List projects using a status
    question: Which projects use a particular status?
  phrasing_ops: 9
  slug: jira-status-api
- baseURL: https://your-domain.atlassian.net/rest/api/2
  baseurl_source: declared
  description: This resource represents a [long-running asynchronous tasks](#async-operations). Use it to obtain details about the progress of a long-running task or cancel a long-running task.
  name: Jira Tasks API
  phrasing_intents:
  - id: getTask
    intent: Check a long-running task's status
    question: How do I check progress on an asynchronous Jira task?
  - id: cancelTask
    intent: Cancel a long-running task
    question: Can I cancel an asynchronous task that's still running?
  phrasing_ops: 2
  slug: jira-tasks-api
- baseURL: https://your-domain.atlassian.net/rest/api/2
  baseurl_source: declared
  description: This resource represents planning settings for plan-only and Atlassian teams in a plan. Use it to get, create, update and delete planning settings.
  name: Jira Teams in plan API
  phrasing_intents:
  - id: getTeams
    intent: List teams in a plan
    question: Which teams are part of a Jira plan?
  - id: addAtlassianTeam
    intent: Add an Atlassian team to a plan
    question: Can I bring an existing Atlassian team into a plan with a scrum or kanban planning style?
  - id: removeAtlassianTeam
    intent: Remove an Atlassian team from a plan
    question: Can I take an Atlassian team out of a plan?
  - id: getAtlassianTeam
    intent: Get an Atlassian team's plan settings
    question: What capacity and sprint length is an Atlassian team configured with in a plan?
  - id: updateAtlassianTeam
    intent: Update an Atlassian team's plan settings
    question: Can I change an Atlassian team's capacity or sprint length in a plan?
  - id: createPlanOnlyTeam
    intent: Create a plan-only team
    question: How do I create a team that exists only inside one plan?
  - id: deletePlanOnlyTeam
    intent: Delete a plan-only team
    question: Can I delete a team that only exists in one plan?
  - id: getPlanOnlyTeam
    intent: Get a plan-only team's settings
    question: What are the members and capacity of a plan-only team?
  phrasing_ops: 9
  slug: jira-teams-in-plan-api
- baseURL: https://your-domain.atlassian.net/rest/api/2
  baseurl_source: declared
  description: This resource represents time tracking and time tracking providers. Use it to get and set the time tracking provider, get and set the time tracking options, and disable time tracking.
  name: Jira Time tracking API
  phrasing_intents:
  - id: getSelectedTimeTrackingImplementation
    intent: See which time tracking provider is active
    question: Which time tracking provider is currently selected on my site?
  - id: selectTimeTrackingImplementation
    intent: Choose the time tracking provider
    question: How do I switch to a different time tracking provider?
  - id: getAvailableTimeTrackingImplementations
    intent: List available time tracking providers
    question: What time tracking providers can I choose from?
  - id: getSharedTimeTrackingConfiguration
    intent: Get time tracking settings
    question: What time format and default unit does time tracking use?
  - id: setSharedTimeTrackingConfiguration
    intent: Change time tracking settings
    question: How do I change the working hours per day used for time tracking?
  phrasing_ops: 5
  slug: jira-time-tracking-api
- baseURL: https://your-domain.atlassian.net/rest/api/2
  baseurl_source: declared
  description: 'UI modifications is a feature available for **Forge apps only**. It enables Forge apps to control how selected Jira and Jira Service Management fields behave on the following views: * Jira global issu'
  name: Jira UI modifications (apps) API
  phrasing_intents:
  - id: getUiModifications
    intent: List my Forge app's UI modifications
    question: Which UI modifications has my Forge app defined?
  - id: createUiModification
    intent: Create a UI modification
    question: How do I create a UI modification for my Forge app?
  - id: deleteUiModification
    intent: Delete a UI modification
    question: Can I delete a UI modification my Forge app no longer needs?
  - id: updateUiModification
    intent: Update a UI modification
    question: Can I change the contexts or data of an existing UI modification?
  phrasing_ops: 4
  slug: jira-ui-modifications-apps-api
- baseURL: https://your-domain.atlassian.net/rest/api/2
  baseurl_source: declared
  description: This resource represents [user](#api-group-Users) properties and provides for storing custom data against a user. Use it to get, create, and delete user properties as well as get a list of property ke
  name: Jira User properties API
  phrasing_intents:
  - id: getUserPropertyKeys
    intent: List property keys stored on a user
    question: What custom properties are stored against a user?
  - id: deleteUserProperty
    intent: Remove a property from a user
    question: How do I delete a custom property from a user?
  - id: getUserProperty
    intent: Read a user property value
    question: How do I read a custom property saved on a user?
  - id: setUserProperty
    intent: Store a custom property on a user
    question: Can I store custom data against a Jira user?
  phrasing_ops: 4
  slug: jira-user-properties-api
- baseURL: https://your-domain.atlassian.net/rest/api/2
  baseurl_source: declared
  description: This resource represents various ways to search for and find users. Use it to obtain list of users including users assignable to projects and issues, users with permissions, user lists for pickup fiel
  name: Jira User search API
  phrasing_intents:
  - id: findBulkAssignableUsers
    intent: Find users assignable across projects
    question: Who can be assigned issues in all of several projects?
  - id: findAssignableUsers
    intent: Find users assignable to an issue
    question: Who can be set as the assignee on a particular issue?
  - id: findUsersWithAllPermissions
    intent: Find users holding given permissions
    question: Which users have both browse and edit permission in a project?
  - id: findUsersForPicker
    intent: Suggest users for a user picker
    question: Can I get user suggestions with the matching text highlighted for a picker field?
  - id: findUsers
    intent: Search active users by name or property
    question: Can I search active users by name or email?
  - id: findUsersByQuery
    intent: Find users with a structured query
    question: Can I find users with a structured query like is assignee of a project?
  - id: findUserKeysByQuery
    intent: Find user keys with a structured query
    question: Can I get only user keys, not full profiles, from a structured user query?
  - id: findUsersWithBrowsePermission
    intent: Find users who can view an issue
    question: Which users are able to browse a specific issue?
  phrasing_ops: 8
  slug: jira-user-search-api
- baseURL: https://your-domain.atlassian.net/rest/api/2
  baseurl_source: declared
  description: 'This resource represents webhooks. Webhooks are calls sent to a URL when an event occurs in Jira for issues specified by a JQL query. Only Connect and OAuth 2.0 apps can register and manage webhooks. '
  name: Jira Webhooks API
  phrasing_intents:
  - id: deleteWebhookById
    intent: Delete my app's webhooks
    question: Can I unregister webhooks my app created?
  - id: getDynamicWebhooksForApp
    intent: List my app's registered webhooks
    question: Which webhooks has my app registered in Jira?
  - id: registerDynamicWebhooks
    intent: Register webhooks for my app
    question: How do I subscribe my app to Jira issue events with a webhook?
  - id: getFailedWebhooks
    intent: List failed webhook deliveries
    question: Which webhook deliveries to my app failed after all retries?
  - id: refreshWebhooks
    intent: Extend the life of webhooks
    question: Do API-registered webhooks expire, and can I keep them alive?
  phrasing_ops: 5
  slug: jira-webhooks-api
- baseURL: https://your-domain.atlassian.net/rest/api/2
  baseurl_source: declared
  description: This resource represents draft workflow schemes. Use it to manage drafts of workflow schemes. A workflow scheme maps issue types to workflows. A workflow scheme can be associated with one or more proj
  name: Jira Workflow scheme drafts API
  phrasing_intents:
  - id: createWorkflowSchemeDraftFromParent
    intent: Create a draft copy of an active workflow scheme
    question: How do I start a draft of an active workflow scheme so I can edit it safely?
  - id: deleteWorkflowSchemeDraft
    intent: Discard a draft workflow scheme
    question: How do I throw away unpublished changes to a workflow scheme?
  - id: getWorkflowSchemeDraft
    intent: Get the draft of a workflow scheme
    question: What pending changes are in the draft of an active workflow scheme?
  - id: updateWorkflowSchemeDraft
    intent: Update a draft workflow scheme
    question: How do I rename or re-describe the draft of a workflow scheme?
  - id: deleteDraftDefaultWorkflow
    intent: Reset a draft's default workflow to the system one
    question: How do I reset a draft scheme's default workflow back to Jira's system workflow?
  - id: getDraftDefaultWorkflow
    intent: Get the default workflow in a scheme's draft
    question: Which workflow handles unmapped issue types in a draft workflow scheme?
  - id: updateDraftDefaultWorkflow
    intent: Set the default workflow in a scheme's draft
    question: How do I change the default workflow in a draft workflow scheme?
  - id: deleteWorkflowSchemeDraftIssueType
    intent: Remove an issue type's mapping from a draft
    question: How do I unmap one issue type from its workflow in a draft scheme?
  phrasing_ops: 14
  slug: jira-workflow-scheme-drafts-api
- baseURL: https://your-domain.atlassian.net/rest/api/2
  baseurl_source: declared
  description: This resource represents the associations between workflow schemes and projects. For more information, see [Managing your workflows](https://confluence.atlassian.com/x/q4hKLg).
  name: Jira Workflow scheme project associations API
  phrasing_intents:
  - id: getWorkflowSchemeProjectAssociations
    intent: Find the workflow scheme used by projects
    question: Which workflow scheme does a given classic project use?
  - id: assignSchemeToProject
    intent: Assign a workflow scheme to a project
    question: How do I attach a workflow scheme to a classic project?
  phrasing_ops: 2
  slug: jira-workflow-scheme-project-associations-api
- baseURL: https://your-domain.atlassian.net/rest/api/2
  baseurl_source: declared
  description: This resource represents workflow schemes. Use it to manage workflow schemes and the workflow scheme's workflows and issue types. A workflow scheme maps issue types to workflows. A workflow scheme can
  name: Jira Workflow schemes API
  phrasing_intents:
  - id: getAllWorkflowSchemes
    intent: List all published workflow schemes
    question: How do I list every workflow scheme on my Jira site?
  - id: createWorkflowScheme
    intent: Create a new workflow scheme
    question: How can I set up a brand-new workflow scheme for a group of projects?
  - id: switchWorkflowSchemeForProject
    intent: Switch a project to a different workflow scheme
    question: How do I move a classic project onto another workflow scheme?
  - id: readWorkflowSchemes
    intent: Bulk fetch workflow schemes by scheme or project
    question: Which workflow schemes are my projects using?
  - id: updateSchemes
    intent: Update a workflow scheme immediately, without drafts
    question: How can I change a team-managed project's workflow scheme with the changes applying right away?
  - id: getRequiredWorkflowSchemeMappings
    intent: Preview status mappings needed for a scheme change
    question: Which status mappings will I need before changing the workflows in a workflow scheme?
  - id: deleteWorkflowScheme
    intent: Delete a workflow scheme
    question: How do I get rid of a workflow scheme I no longer use?
  - id: getWorkflowScheme
    intent: Get one workflow scheme's details
    question: What does a specific workflow scheme contain?
  phrasing_ops: 19
  slug: jira-workflow-schemes-api
- baseURL: https://your-domain.atlassian.net/rest/api/2
  baseurl_source: declared
  description: This resource represents status categories. Use it to obtain a list of all status categories and the details of a category. Status categories provided a mechanism for categorizing [statuses](#api-grou
  name: Jira Workflow status categories API
  phrasing_intents:
  - id: getStatusCategories
    intent: List all status categories
    question: What status categories does Jira use to group statuses?
  - id: getStatusCategory
    intent: Get one status category
    question: What are the details of a single status category?
  phrasing_ops: 2
  slug: jira-workflow-status-categories-api
- baseURL: https://your-domain.atlassian.net/rest/api/2
  baseurl_source: declared
  description: This resource represents issue workflow statuses. Use it to obtain a list of all statuses associated with workflows and the details of a status.
  name: Jira Workflow statuses API
  phrasing_intents:
  - id: getStatuses
    intent: List all statuses in active workflows
    question: What statuses are used across all active workflows?
  - id: getStatus
    intent: Look up one status by ID or name
    question: How do I look up a status like In Review by its name?
  phrasing_ops: 2
  slug: jira-workflow-statuses-api
- baseURL: https://your-domain.atlassian.net/rest/api/2
  baseurl_source: declared
  description: This resource represents workflow transition rules. Workflow transition rules define a Connect or a Forge app routine, such as a [workflow post functions](https://developer.atlassian.com/cloud/jira/pl
  name: Jira Workflow transition rules API
  phrasing_intents:
  - id: getWorkflowTransitionRuleConfigurations
    intent: List workflows with my app's transition rules
    question: Which workflows use my app's post functions, conditions or validators?
  - id: updateWorkflowTransitionRuleConfigurations
    intent: Update configuration of workflow transition rules
    question: How do I change the configuration of my app's post function in a workflow?
  - id: deleteWorkflowTransitionRuleConfigurations
    intent: Remove transition rules from workflows
    question: How do I delete my app's transition rules from workflows?
  phrasing_ops: 3
  slug: jira-workflow-transition-rules-api
- baseURL: https://your-domain.atlassian.net/rest/api/2
  baseurl_source: declared
  description: 'This resource represents workflows. Use it to: * Get workflows * Create workflows * Update workflows * Delete inactive workflows * Get workflow capabilities'
  name: Jira Workflows API
  phrasing_intents:
  - id: readWorkflowFromHistory
    intent: Read a past version of a workflow
    question: What did a workflow look like at an earlier version number?
  - id: listWorkflowHistory
    intent: List the change history of a workflow
    question: Which saved versions exist in a workflow's history?
  - id: getWorkflowsPaginated
    intent: Page through published classic workflows
    question: Where can I get a paged list of published classic workflows before that endpoint is retired?
  - id: deleteInactiveWorkflow
    intent: Delete an inactive workflow
    question: How do I delete a workflow nobody uses anymore?
  - id: getWorkflowProjectIssueTypeUsages
    intent: List issue types in a project using a workflow
    question: Which issue types in a given project are governed by a particular workflow?
  - id: getProjectUsagesForWorkflow
    intent: List projects using a workflow
    question: Which projects are using a given workflow?
  - id: getWorkflowSchemeUsagesForWorkflow
    intent: List workflow schemes using a workflow
    question: Which workflow schemes include a particular workflow?
  - id: readWorkflows
    intent: Bulk fetch workflows by name, ID or project
    question: Can I fetch the full definitions of several workflows at once by their IDs?
  phrasing_ops: 16
  slug: jira-workflows-api
- baseURL: https://your-domain.atlassian.net/rest/api/2
  baseurl_source: declared
  description: The Knowledge Base API from Jira — 1 operation(s) for knowledge base.
  name: Jira Knowledge Base API
  phrasing_intents:
  - id: getArticles
    intent: Search knowledge base articles across service desks
    question: How do I search help articles across all my service desks?
  phrasing_ops: 1
  slug: jira-knowledge-base-api
- baseURL: https://your-domain.atlassian.net/rest/api/2
  baseurl_source: declared
  description: The Request Type API from Jira — 1 operation(s) for request type.
  name: Jira Request Type API
  phrasing_intents:
  - id: getAllRequestTypes
    intent: List customer request types
    question: What kinds of requests can customers raise across my service desks?
  phrasing_ops: 1
  slug: jira-request-type-api
arazzos:
- description: Read an issue, page through its comment thread oldest-first, then add a reply.
  name: Jira Read an Issue Comment Thread and Reply
  slug: jira-comment-thread-reply-workflow
- description: Resolve project metadata, create an issue, then read back the stored issue.
  name: Jira Create an Issue and Read It Back
  slug: jira-create-issue-read-back-workflow
- description: Search for an existing issue by JQL and either comment on the duplicate or create a new issue.
  name: Jira Deduplicate Issue Intake
  slug: jira-deduplicate-issue-intake-workflow
- description: Read an issue, apply a field edit and label operations, then re-read to verify.
  name: Jira Edit an Issue and Verify the Change
  slug: jira-edit-issue-verify-workflow
- description: Cache the projects, issue types, and priorities an issue-creation surface needs.
  name: Jira Bootstrap Issue Creation Metadata
  slug: jira-issue-metadata-bootstrap-workflow
- description: Run a JQL search via GET, then drill into the first matching issue and its comments.
  name: Jira Run a JQL Report and Drill Into a Result
  slug: jira-jql-issue-report-workflow
- description: Search projects by name, read the matched project, and map its per-issue-type statuses.
  name: Jira Discover a Project and Its Workflow Statuses
  slug: jira-project-discovery-workflow
- description: Read an issue and its sub-tasks first, then delete it with an explicit sub-task decision.
  name: Jira Safely Delete an Issue
  slug: jira-safe-issue-delete-workflow
- description: Find stale issues with JQL, annotate the first match, discover its transitions, and close it.
  name: Jira Sweep a Stale Issue Through a Transition
  slug: jira-stale-issue-sweep-workflow
- description: Read an issue, discover its legal transitions, apply one, and verify the new status.
  name: Jira Transition an Issue to a New Status
  slug: jira-transition-issue-workflow
artifact_total: 338
asyncapis:
- description: Jira Cloud webhooks deliver HTTP POST payloads to a configured URL whenever specified events occur in your Jira instance. Webhooks can be registered via the Jira REST API or through the Jira administr
  name: Jira Cloud Webhooks
  slug: jira-webhooks-asyncapi
- description: ''
  name: Jira Webhooks
  slug: jira-webhooks
collections:
- collection_type: postman
  name: Jira Cloud Platform REST Issue Comments API
  slug: postman-jira-issue-comments-api
- collection_type: postman
  name: Jira Cloud Platform REST Issue Comments Issue Priorities API
  slug: postman-jira-issue-priorities-api
- collection_type: postman
  name: Jira Cloud Platform REST Issue Comments Issue Search API
  slug: postman-jira-issue-search-api
- collection_type: postman
  name: Jira Cloud Platform REST Issue Comments Issue Statuses API
  slug: postman-jira-issue-statuses-api
- collection_type: postman
  name: Jira Cloud Platform REST Issue Comments Issue Transitions API
  slug: postman-jira-issue-transitions-api
- collection_type: postman
  name: Jira Cloud Platform REST Issue Comments Issue Types API
  slug: postman-jira-issue-types-api
- collection_type: postman
  name: Jira Cloud Platform REST Issue Comments Issues API
  slug: postman-jira-issues-api
- collection_type: postman
  name: Jira Cloud Platform REST Issue Comments Projects API
  slug: postman-jira-projects-api
- collection_type: open
  name: Jira Cloud Platform REST API
  slug: open-jira-cloud-platform-rest-api
- collection_type: open
  name: Jira Cloud Platform REST Issue Comments API
  slug: open-jira-issue-comments-api
- collection_type: open
  name: Jira Cloud Platform REST Issue Comments Issue Priorities API
  slug: open-jira-issue-priorities-api
- collection_type: open
  name: Jira Cloud Platform REST Issue Comments Issue Search API
  slug: open-jira-issue-search-api
- collection_type: open
  name: Jira Cloud Platform REST Issue Comments Issue Statuses API
  slug: open-jira-issue-statuses-api
- collection_type: open
  name: Jira Cloud Platform REST Issue Comments Issue Transitions API
  slug: open-jira-issue-transitions-api
- collection_type: open
  name: Jira Cloud Platform REST Issue Comments Issue Types API
  slug: open-jira-issue-types-api
- collection_type: open
  name: Jira Cloud Platform REST Issue Comments Issues API
  slug: open-jira-issues-api
- collection_type: open
  name: Jira Cloud Platform REST Issue Comments Projects API
  slug: open-jira-projects-api
- collection_type: open
  name: Atlassian Jira Cloud Platform REST API v3
  slug: open-jira
common:
- group: other
  href: https://artifacts.apis.io/jira/capabilities/jira-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/jira-capability-edges.yml
- group: other
  href: https://artifacts.apis.io/jira/overlays/jira-platform-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/jira-platform-overlay.yaml
- group: other
  href: https://artifacts.apis.io/jira/overlays/jira-software-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/jira-software-overlay.yaml
- group: other
  href: https://artifacts.apis.io/jira/overlays/jira-service-management-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/jira-service-management-overlay.yaml
- group: commercial
  href: https://artifacts.apis.io/jira/plans/jira-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/jira-plans-pricing.yml
- group: commercial
  href: https://artifacts.apis.io/jira/finops/jira-finops.yml
  title: ''
  type: FinOps
  url: finops/jira-finops.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/atlassian
- group: docs
  title: ''
  type: Documentation
  url: https://developer.atlassian.com/cloud/jira/platform/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.atlassian.com/software/jira/pricing
- group: operate
  title: ''
  type: Community
  url: https://community.developer.atlassian.com/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/atlassian
- group: build
  href: https://artifacts.apis.io/jira/mcp/jira-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/jira-tool-crosswalk.yml
- group: auth
  title: ''
  type: Compliance
  url: https://www.atlassian.com/trust/compliance
- group: operate
  title: ''
  type: Deprecation
  url: https://developer.atlassian.com/platform/marketplace/atlassian-rest-api-policy/
- group: start
  href: https://artifacts.apis.io/jira/sandbox/jira-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/jira-sandbox.yml
- group: design
  href: https://artifacts.apis.io/jira/asyncapi/jira-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/jira-webhooks.yml
- group: agent
  href: https://artifacts.apis.io/jira/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.atlassian.com/
- group: docs
  title: ''
  type: APIReference
  url: https://developer.atlassian.com/cloud/jira/platform/rest/v3/api-group-issues/
- group: operate
  title: ''
  type: Roadmap
  url: https://www.atlassian.com/roadmap/cloud
- group: start
  title: ''
  type: SignUp
  url: https://www.atlassian.com/try/cloud/signup?bundle=jira-software
- group: operate
  title: ''
  type: HelpCenter
  url: https://community.atlassian.com/
- group: auth
  title: ''
  type: Trust
  url: https://www.atlassian.com/trust
- group: auth
  title: ''
  type: BugBounty
  url: https://bugcrowd.com/atlassian
- group: build
  href: https://artifacts.apis.io/jira/collections/jira.postman_collection.json
  title: ''
  type: PostmanCollection
  url: collections/jira.postman_collection.json
- group: build
  href: https://artifacts.apis.io/jira/collections/jira.opencollection.json
  title: ''
  type: OpenCollection
  url: collections/jira.opencollection.json
- group: company
  title: ''
  type: Website
  url: https://www.atlassian.com/software/jira
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/jira/overview
- group: build
  href: https://artifacts.apis.io/jira/packages/jira-packages.yml
  title: ''
  type: Packages
  url: packages/jira-packages.yml
- group: agent
  href: https://artifacts.apis.io/jira/well-known/jira-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/jira-well-known.yml
- group: auth
  href: https://artifacts.apis.io/jira/well-known/jira-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/jira-security.txt
- group: agent
  href: https://artifacts.apis.io/jira/mcp/jira-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/jira-mcp.yml
- group: agent
  href: https://artifacts.apis.io/jira/llms/jira-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/jira-llms.txt
- group: other
  href: https://artifacts.apis.io/jira/overlays/jira-cloud-platform-rest-api-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/jira-cloud-platform-rest-api-overlay.yaml
- group: design
  href: https://artifacts.apis.io/jira/conformance/jira-conformance.yml
  title: ''
  type: Conformance
  url: conformance/jira-conformance.yml
- group: design
  href: https://artifacts.apis.io/jira/errors/jira-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/jira-problem-types.yml
- group: design
  href: https://artifacts.apis.io/jira/lifecycle/jira-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/jira-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/jira/conventions/jira-conventions.yml
  title: ''
  type: Conventions
  url: conventions/jira-conventions.yml
- group: operate
  href: https://artifacts.apis.io/jira/changelog/jira-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/jira-changelog.yml
- group: build
  href: https://artifacts.apis.io/jira/cli/jira-cli.yml
  title: ''
  type: CLI
  url: cli/jira-cli.yml
- group: design
  href: https://artifacts.apis.io/jira/components/jira-components.yml
  title: ''
  type: Components
  url: components/jira-components.yml
- group: design
  href: https://artifacts.apis.io/jira/data-model/jira-data-model.yml
  title: ''
  type: DataModel
  url: data-model/jira-data-model.yml
- group: agent
  href: https://artifacts.apis.io/jira/agentic-access/jira-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/jira-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/jira/security/jira-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/jira-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/jira/security/jira-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/jira-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/jira/security/jira-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/jira-domain-security.yml
- group: auth
  href: https://artifacts.apis.io/jira/authentication/jira-authentication.yml
  title: ''
  type: Authentication
  url: authentication/jira-authentication.yml
- group: auth
  href: https://artifacts.apis.io/jira/scopes/jira-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/jira-scopes.yml
- group: design
  href: https://artifacts.apis.io/jira/arazzo/jira-comment-thread-reply-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/jira-comment-thread-reply-workflow.yml
- group: design
  href: https://artifacts.apis.io/jira/arazzo/jira-create-issue-read-back-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/jira-create-issue-read-back-workflow.yml
- group: design
  href: https://artifacts.apis.io/jira/arazzo/jira-deduplicate-issue-intake-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/jira-deduplicate-issue-intake-workflow.yml
- group: design
  href: https://artifacts.apis.io/jira/arazzo/jira-edit-issue-verify-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/jira-edit-issue-verify-workflow.yml
- group: design
  href: https://artifacts.apis.io/jira/arazzo/jira-issue-metadata-bootstrap-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/jira-issue-metadata-bootstrap-workflow.yml
- group: design
  href: https://artifacts.apis.io/jira/arazzo/jira-jql-issue-report-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/jira-jql-issue-report-workflow.yml
- group: design
  href: https://artifacts.apis.io/jira/arazzo/jira-project-discovery-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/jira-project-discovery-workflow.yml
- group: design
  href: https://artifacts.apis.io/jira/arazzo/jira-safe-issue-delete-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/jira-safe-issue-delete-workflow.yml
- group: design
  href: https://artifacts.apis.io/jira/arazzo/jira-stale-issue-sweep-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/jira-stale-issue-sweep-workflow.yml
- group: design
  href: https://artifacts.apis.io/jira/arazzo/jira-transition-issue-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/jira-transition-issue-workflow.yml
- group: start
  title: ''
  type: Portal
  url: https://developer.atlassian.com/cloud/jira/platform/
- group: start
  title: ''
  type: GettingStarted
  url: https://developer.atlassian.com/cloud/jira/platform/getting-started/
- group: build
  title: ''
  type: SDKs
  url: https://developer.atlassian.com/cloud/jira/platform/libraries/
- group: auth
  title: OAuth 2.0
  type: Authentication
  url: https://developer.atlassian.com/cloud/jira/platform/oauth-2-3lo-apps/
- group: operate
  title: ''
  type: Support
  url: https://support.atlassian.com/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.atlassian.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.atlassian.com/legal/cloud-terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.atlassian.com/legal/privacy-policy
- group: operate
  title: ''
  type: ChangeLog
  url: https://developer.atlassian.com/changelog/
- group: company
  title: ''
  type: Blog
  url: https://www.atlassian.com/blog/developer
- group: other
  title: ''
  type: Marketplace
  url: https://developer.atlassian.com/platform/marketplace/getting-started/
- group: operate
  title: ''
  type: RateLimits
  url: https://developer.atlassian.com/cloud/jira/platform/rate-limiting/
- group: auth
  title: ''
  type: Security
  url: https://developer.atlassian.com/cloud/jira/platform/security-overview/
- group: docs
  href: https://artifacts.apis.io/jira/json-schema/jira-issue-schema.json
  title: ''
  type: JSONSchema
  url: json-schema/jira-issue-schema.json
- group: docs
  href: https://artifacts.apis.io/jira/json-schema/jira-project-schema.json
  title: ''
  type: JSONSchema
  url: json-schema/jira-project-schema.json
- group: design
  href: https://artifacts.apis.io/jira/json-ld/jira-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/jira-context.jsonld
created: '2024'
description: APIs for Atlassian Jira project management and issue tracking platform.
examples:
- key_count: 3
  name: Jira Cloud Platform Rest Atlassian Document Format Example
  slug: jira-cloud-platform-rest-atlassian-document-format-example
- key_count: 8
  name: Jira Cloud Platform Rest Attachment Example
  slug: jira-cloud-platform-rest-attachment-example
- key_count: 4
  name: Jira Cloud Platform Rest Avatar Urls Example
  slug: jira-cloud-platform-rest-avatar-urls-example
- key_count: 3
  name: Jira Cloud Platform Rest Change History Example
  slug: jira-cloud-platform-rest-change-history-example
- key_count: 7
  name: Jira Cloud Platform Rest Change Item Example
  slug: jira-cloud-platform-rest-change-item-example
- key_count: 4
  name: Jira Cloud Platform Rest Changelog Example
  slug: jira-cloud-platform-rest-changelog-example
- key_count: 6
  name: Jira Cloud Platform Rest Comment Example
  slug: jira-cloud-platform-rest-comment-example
- key_count: 7
  name: Jira Cloud Platform Rest Component Example
  slug: jira-cloud-platform-rest-component-example
- key_count: 4
  name: Jira Cloud Platform Rest Created Issue Example
  slug: jira-cloud-platform-rest-created-issue-example
- key_count: 2
  name: Jira Cloud Platform Rest Entity Property Example
  slug: jira-cloud-platform-rest-entity-property-example
- key_count: 3
  name: Jira Cloud Platform Rest Error Collection Example
  slug: jira-cloud-platform-rest-error-collection-example
- key_count: 5
  name: Jira Cloud Platform Rest Field Update Operation Example
  slug: jira-cloud-platform-rest-field-update-operation-example
- key_count: 8
  name: Jira Cloud Platform Rest Issue Bean Example
  slug: jira-cloud-platform-rest-issue-bean-example
- key_count: 4
  name: Jira Cloud Platform Rest Issue Create Request Example
  slug: jira-cloud-platform-rest-issue-create-request-example
- key_count: 17
  name: Jira Cloud Platform Rest Issue Fields Example
  slug: jira-cloud-platform-rest-issue-fields-example
- key_count: 2
  name: Jira Cloud Platform Rest Issue Link Example
  slug: jira-cloud-platform-rest-issue-link-example
- key_count: 5
  name: Jira Cloud Platform Rest Issue Link Type Example
  slug: jira-cloud-platform-rest-issue-link-type-example
- key_count: 4
  name: Jira Cloud Platform Rest Issue Ref Example
  slug: jira-cloud-platform-rest-issue-ref-example
- key_count: 3
  name: Jira Cloud Platform Rest Issue Transition Request Example
  slug: jira-cloud-platform-rest-issue-transition-request-example
- key_count: 8
  name: Jira Cloud Platform Rest Issue Type Details Example
  slug: jira-cloud-platform-rest-issue-type-details-example
- key_count: 5
  name: Jira Cloud Platform Rest Issue Type With Status Example
  slug: jira-cloud-platform-rest-issue-type-with-status-example
- key_count: 4
  name: Jira Cloud Platform Rest Issue Update Request Example
  slug: jira-cloud-platform-rest-issue-update-request-example
- key_count: 7
  name: Jira Cloud Platform Rest Page Bean Project Example
  slug: jira-cloud-platform-rest-page-bean-project-example
- key_count: 4
  name: Jira Cloud Platform Rest Page Of Comments Example
  slug: jira-cloud-platform-rest-page-of-comments-example
- key_count: 4
  name: Jira Cloud Platform Rest Page Of Worklogs Example
  slug: jira-cloud-platform-rest-page-of-worklogs-example
- key_count: 6
  name: Jira Cloud Platform Rest Priority Example
  slug: jira-cloud-platform-rest-priority-example
- key_count: 4
  name: Jira Cloud Platform Rest Project Category Example
  slug: jira-cloud-platform-rest-project-category-example
- key_count: 17
  name: Jira Cloud Platform Rest Project Example
  slug: jira-cloud-platform-rest-project-example
- key_count: 5
  name: Jira Cloud Platform Rest Project Ref Example
  slug: jira-cloud-platform-rest-project-ref-example
- key_count: 4
  name: Jira Cloud Platform Rest Resolution Example
  slug: jira-cloud-platform-rest-resolution-example
- key_count: 1
  name: Jira Cloud Platform Rest Scope Example
  slug: jira-cloud-platform-rest-scope-example
- key_count: 8
  name: Jira Cloud Platform Rest Search Request Example
  slug: jira-cloud-platform-rest-search-request-example
- key_count: 8
  name: Jira Cloud Platform Rest Search Results Example
  slug: jira-cloud-platform-rest-search-results-example
- key_count: 5
  name: Jira Cloud Platform Rest Status Category Example
  slug: jira-cloud-platform-rest-status-category-example
- key_count: 5
  name: Jira Cloud Platform Rest Status Details Example
  slug: jira-cloud-platform-rest-status-details-example
- key_count: 7
  name: Jira Cloud Platform Rest Transition Example
  slug: jira-cloud-platform-rest-transition-example
- key_count: 1
  name: Jira Cloud Platform Rest Transition Ref Example
  slug: jira-cloud-platform-rest-transition-ref-example
- key_count: 2
  name: Jira Cloud Platform Rest Transitions Example
  slug: jira-cloud-platform-rest-transitions-example
- key_count: 7
  name: Jira Cloud Platform Rest User Details Example
  slug: jira-cloud-platform-rest-user-details-example
- key_count: 10
  name: Jira Cloud Platform Rest Version Example
  slug: jira-cloud-platform-rest-version-example
- key_count: 3
  name: Jira Cloud Platform Rest Visibility Example
  slug: jira-cloud-platform-rest-visibility-example
- key_count: 3
  name: Jira Cloud Platform Rest Votes Example
  slug: jira-cloud-platform-rest-votes-example
- key_count: 3
  name: Jira Cloud Platform Rest Watches Example
  slug: jira-cloud-platform-rest-watches-example
- key_count: 7
  name: Jira Cloud Platform Rest Worklog Example
  slug: jira-cloud-platform-rest-worklog-example
features:
- 'Free: up to 10 users'
- 'Standard: $7.91-$9.05/user/mo (volume tiered)'
- 'Premium: $14.54-$18.30/user/mo with Advanced Roadmaps'
- 'Enterprise custom: Atlassian Intelligence, 99.95% uptime, data residency'
- 'Volume discount: rates drop above 100 users (max 50K)'
- REST API v3 at api.atlassian.com
- GraphQL API for some products
- Token-bucket rate limit ~10 req/sec/app/user
- Bulk operations max 100 items/request
- Webhooks v3 for issue/project events
- OAuth 2.0 (3LO) and API tokens
- Atlassian Connect framework for marketplace apps
- Forge for serverless app development
- JQL (Jira Query Language) for advanced search
- Atlassian Intelligence AI assistant (Enterprise)
- Cross-product Analytics + Atlas integrations
finops:
- has_sources: true
  method: derived
  name: Jira Finops
  primary_unit: user
  service_category: ''
  slug: jira-finops
  template: false
image: https://www.atlassian.com/dam/jcr:e33efd9e-e0b8-4d61-a24d-68a48ef9bbe4/jira-icon-blue.svg
integrations:
- description: Link Jira issues to Confluence pages for seamless knowledge management and documentation alongside project tracking.
  name: Confluence
- description: Connect code repositories to Jira issues for automated status updates, smart commits, and development tracking.
  name: Bitbucket
- description: Link GitHub pull requests, branches, and commits to Jira issues for end-to-end development visibility.
  name: GitHub
- description: Create and manage Jira issues from Slack channels with bi-directional notifications and status updates.
  name: Slack
- description: Receive Jira notifications and manage issues directly from Microsoft Teams conversations.
  name: Microsoft Teams
json_schemas:
- name: AtlassianDocumentFormat
  property_count: 3
  slug: jira-cloud-platform-rest-atlassian-document-format
- name: Attachment
  property_count: 8
  slug: jira-cloud-platform-rest-attachment
- name: AvatarUrls
  property_count: 4
  slug: jira-cloud-platform-rest-avatar-urls
- name: ChangeHistory
  property_count: 3
  slug: jira-cloud-platform-rest-change-history
- name: ChangeItem
  property_count: 7
  slug: jira-cloud-platform-rest-change-item
- name: Changelog
  property_count: 4
  slug: jira-cloud-platform-rest-changelog
- name: Comment
  property_count: 6
  slug: jira-cloud-platform-rest-comment
- name: Component
  property_count: 7
  slug: jira-cloud-platform-rest-component
- name: CreatedIssue
  property_count: 4
  slug: jira-cloud-platform-rest-created-issue
- name: EntityProperty
  property_count: 2
  slug: jira-cloud-platform-rest-entity-property
- name: ErrorCollection
  property_count: 3
  slug: jira-cloud-platform-rest-error-collection
- name: FieldUpdateOperation
  property_count: 5
  slug: jira-cloud-platform-rest-field-update-operation
- name: IssueBean
  property_count: 8
  slug: jira-cloud-platform-rest-issue-bean
- name: IssueCreateRequest
  property_count: 4
  slug: jira-cloud-platform-rest-issue-create-request
- name: IssueFields
  property_count: 17
  slug: jira-cloud-platform-rest-issue-fields
- name: IssueLink
  property_count: 2
  slug: jira-cloud-platform-rest-issue-link
- name: IssueLinkType
  property_count: 5
  slug: jira-cloud-platform-rest-issue-link-type
- name: IssueRef
  property_count: 4
  slug: jira-cloud-platform-rest-issue-ref
- name: IssueTransitionRequest
  property_count: 3
  slug: jira-cloud-platform-rest-issue-transition-request
- name: IssueTypeDetails
  property_count: 8
  slug: jira-cloud-platform-rest-issue-type-details
- name: IssueTypeWithStatus
  property_count: 5
  slug: jira-cloud-platform-rest-issue-type-with-status
- name: IssueUpdateRequest
  property_count: 4
  slug: jira-cloud-platform-rest-issue-update-request
- name: PageBeanProject
  property_count: 7
  slug: jira-cloud-platform-rest-page-bean-project
- name: PageOfComments
  property_count: 4
  slug: jira-cloud-platform-rest-page-of-comments
- name: PageOfWorklogs
  property_count: 4
  slug: jira-cloud-platform-rest-page-of-worklogs
- name: Priority
  property_count: 6
  slug: jira-cloud-platform-rest-priority
- name: ProjectCategory
  property_count: 4
  slug: jira-cloud-platform-rest-project-category
- name: ProjectRef
  property_count: 5
  slug: jira-cloud-platform-rest-project-ref
- name: Project
  property_count: 17
  slug: jira-cloud-platform-rest-project
- name: Resolution
  property_count: 4
  slug: jira-cloud-platform-rest-resolution
- name: Scope
  property_count: 1
  slug: jira-cloud-platform-rest-scope
- name: SearchRequest
  property_count: 8
  slug: jira-cloud-platform-rest-search-request
- name: SearchResults
  property_count: 8
  slug: jira-cloud-platform-rest-search-results
- name: StatusCategory
  property_count: 5
  slug: jira-cloud-platform-rest-status-category
- name: StatusDetails
  property_count: 5
  slug: jira-cloud-platform-rest-status-details
- name: TransitionRef
  property_count: 1
  slug: jira-cloud-platform-rest-transition-ref
- name: Transition
  property_count: 7
  slug: jira-cloud-platform-rest-transition
- name: Transitions
  property_count: 2
  slug: jira-cloud-platform-rest-transitions
- name: UserDetails
  property_count: 7
  slug: jira-cloud-platform-rest-user-details
- name: Version
  property_count: 10
  slug: jira-cloud-platform-rest-version
- name: Visibility
  property_count: 3
  slug: jira-cloud-platform-rest-visibility
- name: Votes
  property_count: 3
  slug: jira-cloud-platform-rest-votes
- name: Watches
  property_count: 3
  slug: jira-cloud-platform-rest-watches
- name: Worklog
  property_count: 7
  slug: jira-cloud-platform-rest-worklog
- name: Jira Issue
  property_count: 10
  slug: jira-issue
- name: Jira Project
  property_count: 22
  slug: jira-project
json_structures:
- name: Jira Cloud Platform Rest Atlassian Document Format Structure
  property_count: 3
  slug: jira-cloud-platform-rest-atlassian-document-format-structure
- name: Jira Cloud Platform Rest Attachment Structure
  property_count: 8
  slug: jira-cloud-platform-rest-attachment-structure
- name: Jira Cloud Platform Rest Avatar Urls Structure
  property_count: 4
  slug: jira-cloud-platform-rest-avatar-urls-structure
- name: Jira Cloud Platform Rest Change History Structure
  property_count: 3
  slug: jira-cloud-platform-rest-change-history-structure
- name: Jira Cloud Platform Rest Change Item Structure
  property_count: 7
  slug: jira-cloud-platform-rest-change-item-structure
- name: Jira Cloud Platform Rest Changelog Structure
  property_count: 4
  slug: jira-cloud-platform-rest-changelog-structure
- name: Jira Cloud Platform Rest Comment Structure
  property_count: 6
  slug: jira-cloud-platform-rest-comment-structure
- name: Jira Cloud Platform Rest Component Structure
  property_count: 7
  slug: jira-cloud-platform-rest-component-structure
- name: Jira Cloud Platform Rest Created Issue Structure
  property_count: 4
  slug: jira-cloud-platform-rest-created-issue-structure
- name: Jira Cloud Platform Rest Entity Property Structure
  property_count: 2
  slug: jira-cloud-platform-rest-entity-property-structure
- name: Jira Cloud Platform Rest Error Collection Structure
  property_count: 3
  slug: jira-cloud-platform-rest-error-collection-structure
- name: Jira Cloud Platform Rest Field Update Operation Structure
  property_count: 5
  slug: jira-cloud-platform-rest-field-update-operation-structure
- name: Jira Cloud Platform Rest Issue Bean Structure
  property_count: 8
  slug: jira-cloud-platform-rest-issue-bean-structure
- name: Jira Cloud Platform Rest Issue Create Request Structure
  property_count: 4
  slug: jira-cloud-platform-rest-issue-create-request-structure
- name: Jira Cloud Platform Rest Issue Fields Structure
  property_count: 17
  slug: jira-cloud-platform-rest-issue-fields-structure
- name: Jira Cloud Platform Rest Issue Link Structure
  property_count: 2
  slug: jira-cloud-platform-rest-issue-link-structure
- name: Jira Cloud Platform Rest Issue Link Type Structure
  property_count: 5
  slug: jira-cloud-platform-rest-issue-link-type-structure
- name: Jira Cloud Platform Rest Issue Ref Structure
  property_count: 4
  slug: jira-cloud-platform-rest-issue-ref-structure
- name: Jira Cloud Platform Rest Issue Transition Request Structure
  property_count: 3
  slug: jira-cloud-platform-rest-issue-transition-request-structure
- name: Jira Cloud Platform Rest Issue Type Details Structure
  property_count: 8
  slug: jira-cloud-platform-rest-issue-type-details-structure
- name: Jira Cloud Platform Rest Issue Type With Status Structure
  property_count: 5
  slug: jira-cloud-platform-rest-issue-type-with-status-structure
- name: Jira Cloud Platform Rest Issue Update Request Structure
  property_count: 4
  slug: jira-cloud-platform-rest-issue-update-request-structure
- name: Jira Cloud Platform Rest Page Bean Project Structure
  property_count: 7
  slug: jira-cloud-platform-rest-page-bean-project-structure
- name: Jira Cloud Platform Rest Page Of Comments Structure
  property_count: 4
  slug: jira-cloud-platform-rest-page-of-comments-structure
- name: Jira Cloud Platform Rest Page Of Worklogs Structure
  property_count: 4
  slug: jira-cloud-platform-rest-page-of-worklogs-structure
- name: Jira Cloud Platform Rest Priority Structure
  property_count: 6
  slug: jira-cloud-platform-rest-priority-structure
- name: Jira Cloud Platform Rest Project Category Structure
  property_count: 4
  slug: jira-cloud-platform-rest-project-category-structure
- name: Jira Cloud Platform Rest Project Ref Structure
  property_count: 5
  slug: jira-cloud-platform-rest-project-ref-structure
- name: Jira Cloud Platform Rest Project Structure
  property_count: 17
  slug: jira-cloud-platform-rest-project-structure
- name: Jira Cloud Platform Rest Resolution Structure
  property_count: 4
  slug: jira-cloud-platform-rest-resolution-structure
- name: Jira Cloud Platform Rest Scope Structure
  property_count: 1
  slug: jira-cloud-platform-rest-scope-structure
- name: Jira Cloud Platform Rest Search Request Structure
  property_count: 8
  slug: jira-cloud-platform-rest-search-request-structure
- name: Jira Cloud Platform Rest Search Results Structure
  property_count: 8
  slug: jira-cloud-platform-rest-search-results-structure
- name: Jira Cloud Platform Rest Status Category Structure
  property_count: 5
  slug: jira-cloud-platform-rest-status-category-structure
- name: Jira Cloud Platform Rest Status Details Structure
  property_count: 5
  slug: jira-cloud-platform-rest-status-details-structure
- name: Jira Cloud Platform Rest Transition Ref Structure
  property_count: 1
  slug: jira-cloud-platform-rest-transition-ref-structure
- name: Jira Cloud Platform Rest Transition Structure
  property_count: 7
  slug: jira-cloud-platform-rest-transition-structure
- name: Jira Cloud Platform Rest Transitions Structure
  property_count: 2
  slug: jira-cloud-platform-rest-transitions-structure
- name: Jira Cloud Platform Rest User Details Structure
  property_count: 7
  slug: jira-cloud-platform-rest-user-details-structure
- name: Jira Cloud Platform Rest Version Structure
  property_count: 10
  slug: jira-cloud-platform-rest-version-structure
- name: Jira Cloud Platform Rest Visibility Structure
  property_count: 3
  slug: jira-cloud-platform-rest-visibility-structure
- name: Jira Cloud Platform Rest Votes Structure
  property_count: 3
  slug: jira-cloud-platform-rest-votes-structure
- name: Jira Cloud Platform Rest Watches Structure
  property_count: 3
  slug: jira-cloud-platform-rest-watches-structure
- name: Jira Cloud Platform Rest Worklog Structure
  property_count: 7
  slug: jira-cloud-platform-rest-worklog-structure
jsonld:
- class_count: 0
  name: Jira Cloud Platform Rest Context
  property_count: 0
  slug: jira-cloud-platform-rest-context
- class_count: 0
  name: Jira Context
  property_count: 15
  slug: jira-context
layout: provider
mcp_servers:
- description: Remote MCP server at mcp.atlassian.com over HTTP.
  name: Atlassian Rovo MCP Server
  slug: atlassian-rovo-mcp-server
modified: '2026-06-20'
name: Jira
nav: Providers
network: true
overview: 'Jira publishes 132 API contracts indexed on the [APIs.io](https://apis.io/) network, including Issue Comments API, Issue Priorities API, Issue Search API, and 129 more. Tagged areas include Agile, Issue Tracking, ITSM, Project Management, and Service Management.


  The Jira catalog on APIs.io includes 2 event-driven AsyncAPI specifications, 2 JSON-LD contexts, and 3 Spectral governance rulesets.


  Jira''s developer surface includes documentation, pricing, sandbox, API reference, signup flow, changelog, CLI, and 67 more developer resources.'
plans:
- name: Jira Plans Pricing
  plan_count: 4
  slug: jira-plans-pricing
- name: Jira Price Estimates
  plan_count: 0
  slug: jira-price-estimates
random_paper: 14
rate_limits:
- limit_count: 4
  name: Jira Rate Limits
  slug: jira-rate-limits
rules:
- authorship: generated
  effective_rule_count: 33
  extends:
  - spectral:asyncapi
  name: Jira — asyncapi rules
  rule_count: 6
  severity_counts:
    error: 1
    hint: 0
    info: 1
    warn: 4
  slug: jira-asyncapi-spectral-rules
- authorship: generated
  effective_rule_count: 6
  extends: []
  name: Jira — jsonschema rules
  rule_count: 6
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 4
  slug: jira-jsonschema-spectral-rules
- authorship: generated
  effective_rule_count: 58
  extends:
  - spectral:oas
  name: Jira API Rules
  rule_count: 17
  severity_counts:
    error: 8
    hint: 0
    info: 2
    warn: 7
  slug: jira-spectral-rules
scopes:
- name: Jira Scopes
  scope_count: 5
  slug: jira-scopes
  summary_line: 5 scopes · authorizationCode
score:
  band: exemplar
  composite: 82.6
  coverage:
    artifact_dirs: 39
    catalog_earned: 65.5
    catalog_earned_first_party: 12.0
    catalog_gap: 49.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 1.0
  facets:
    access_clarity: 94.7
    contract_governance: 18.2
    contract_quality: 72.6
    developer_ergonomics: 81.5
    discoverability: 78.3
    operational_transparency: 73.7
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - australia
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
  previous_composite: 81.6
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 6.6
      derived: 0
      marker_coverage: 75.4
      total: 122
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 43.1
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 61.1
screenshot: https://apis.io/screenshots/jira/jira-2026-06-20T183734.png
security:
- kind: authentication
  name: Jira Authentication
  slug: jira-authentication
  summary_line: http/oauth2 · 3 schemes
- kind: domain-security
  name: Jira Domain Security
  slug: jira-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Jira Vulnerability Disclosure
  slug: jira-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Jira Trust Center
  slug: jira-trust-center
  summary_line: FedRAMP
slug: jira
tags:
- Agile
- Issue Tracking
- ITSM
- Project Management
- Service Management
- Jira
use_cases:
- description: Automate issue creation, assignment, and transitions based on external events from CI/CD pipelines, monitoring tools, or customer feedback systems.
  name: Issue Tracking Automation
- description: Programmatically manage sprints, backlogs, and board configurations for automated agile workflow orchestration.
  name: Sprint Management
- description: Integrate customer support channels with Jira Service Management for automated ticket creation and SLA tracking.
  name: Service Desk Integration
- description: Automate incident response workflows with on-call scheduling, alert routing, and escalation management.
  name: Incident Management
- description: Connect portfolio planning tools with Jira Align for cross-team dependency tracking and program-level reporting.
  name: Enterprise Agile Planning
website: https://www.atlassian.com/software/jira
---
