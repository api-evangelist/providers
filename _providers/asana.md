---
access_model:
  confidence: high
  label: Paid · Self-serve signup
  onboarding: self-serve
  pricing: paid
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: documented
    event_surface_described: derived
    idempotency: false
    mcp_server: verified
    openapi_examples: verified
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 53.6
  scored_at: '2026-10-03'
agentic_access:
- acting_count: 169
  human_in_the_loop: 0
  name: Asana Agentic Access
  operation_count: 316
  slug: asana-agentic-access
  summary_line: 316 operations · 169 acting
api_count: 3
apis:
- baseURL: https://app.asana.com/api/1.0
  baseurl_source: spec
  description: The Asana Allocations API is a tool that allows users to manage and allocate resources within their Asana project management system. With this API, users can easily assign tasks and track the progress
  name: Asana Allocations  API
  phrasing_intents:
  - id: getAllocation
    intent: Get a resource allocation
    question: What does a single allocation record show about someone's planned effort?
  - id: updateAllocation
    intent: Update a resource allocation
    question: Can I change the dates or effort on an existing allocation?
  - id: deleteAllocation
    intent: Delete a resource allocation
    question: Can I cancel someone's allocation to a project?
  - id: getAllocations
    intent: List allocations for a project or person
    question: How much of a person's time is allocated across projects?
  - id: createAllocation
    intent: Allocate a person to a project
    question: How do I plan a teammate's capacity on a project?
  phrasing_ops: 5
  slug: asana-allocations-api
- baseURL: https://app.asana.com/api/1.0
  baseurl_source: spec
  description: The Asana Attachments API allows developers to interact with and manage file attachments within the Asana project management platform. This API enables users to upload, download, and delete attachment
  name: Asana Attachments  API
  phrasing_intents:
  - id: getAttachment
    intent: Get an attachment's details
    question: How do I fetch the full record of a file attached in Asana?
  - id: deleteAttachment
    intent: Delete an attachment
    question: Can I remove a file attached to a task?
  - id: getAttachmentsForObject
    intent: List the files attached to a task or project
    question: Which files are attached to a task?
  - id: createAttachmentForObject
    intent: Upload a file or link to a task
    question: How do I upload a file to a task?
  phrasing_ops: 4
  slug: asana-attachments-api
- baseURL: https://app.asana.com/api/1.0
  baseurl_source: spec
  description: The Asana Custom Fields API allows developers to create and manage custom fields within Asana, a popular project management tool. With this API, users can define custom fields that are specific to the
  name: Asana Custom Fields  API
  phrasing_intents:
  - id: createCustomField
    intent: Create a custom field in a workspace
    question: How do I define a new custom field like a dropdown or number?
  - id: getCustomField
    intent: Get a custom field's definition
    question: What type and options does a custom field have?
  - id: updateCustomField
    intent: Update a custom field
    question: Can I rename a custom field or change its description?
  - id: deleteCustomField
    intent: Delete a custom field
    question: Can I delete a custom field from my workspace?
  - id: getCustomFieldsForWorkspace
    intent: List a workspace's custom fields
    question: What custom fields exist in my workspace?
  - id: createEnumOptionForCustomField
    intent: Add an option to a dropdown custom field
    question: How do I add a new choice to a dropdown field?
  - id: insertEnumOptionForCustomField
    intent: Reorder a dropdown field's options
    question: Can I move a dropdown option before or after another one?
  - id: updateEnumOption
    intent: Edit a dropdown option
    question: Can I rename, recolor or disable a single dropdown option?
  phrasing_ops: 8
  slug: asana-custom-fields-api
- baseURL: https://app.asana.com/api/1.0
  baseurl_source: spec
  description: The Asana Events API is a tool that allows users to track and interact with events happening within their Asana workspace. Through this API, users can receive real-time updates on changes to tasks, pr
  name: Asana Events  API
  phrasing_intents:
  - id: getEvents
    intent: Poll for changes on a resource
    question: What changed on a project since I last checked?
  phrasing_ops: 1
  slug: asana-events-api
- baseURL: https://app.asana.com/api/1.0
  baseurl_source: spec
  description: The Asana Goal Relationships API allows users to create and manage relationships between different goals within their Asana workspace. This API enables users to define dependencies between goals, trac
  name: Asana Goal Relationships  API
  phrasing_intents:
  - id: getGoalRelationship
    intent: Get a goal relationship
    question: What does a single goal relationship record include?
  - id: updateGoalRelationship
    intent: Update a goal relationship's contribution
    question: Can I change the contribution weight of a supporting goal?
  - id: getGoalRelationships
    intent: List what supports a goal
    question: Which projects, portfolios or subgoals support a given goal?
  - id: addSupportingRelationship
    intent: Link supporting work to a goal
    question: How do I connect a project or subgoal so it supports a goal?
  - id: removeSupportingRelationship
    intent: Unlink supporting work from a goal
    question: Can I stop a project from counting toward a goal?
  phrasing_ops: 5
  slug: asana-goal-relationships-api
- baseURL: https://app.asana.com/api/1.0
  baseurl_source: spec
  description: The Asana Goals API is a powerful tool that allows developers to programmatically interact with and manipulate goals within the Asana platform. By utilizing the API, users can create, update, and trac
  name: Asana Goals  API
  phrasing_intents:
  - id: getGoal
    intent: Get a goal's details
    question: What does the full record of a goal show?
  - id: updateGoal
    intent: Update a goal
    question: How do I change a goal's status, owner or due date?
  - id: deleteGoal
    intent: Delete a goal
    question: Can I delete a goal that's no longer relevant?
  - id: getGoals
    intent: List goals by team, project or time period
    question: Which goals does a team have this quarter?
  - id: createGoal
    intent: Create a goal
    question: How do I create a new goal for my team?
  - id: createGoalMetric
    intent: Set the metric that tracks a goal
    question: How do I attach a numeric target to a goal?
  - id: updateGoalMetric
    intent: Record a goal metric's current value
    question: How do I report progress on a goal's metric?
  - id: addFollowers
    intent: Add collaborators to a goal
    question: How do I add collaborators to a goal?
  phrasing_ops: 10
  slug: asana-goals-api
- baseURL: https://app.asana.com/api/1.0
  baseurl_source: spec
  description: Asana Jobs API is an application programming interface that allows developers to access and interact with job-related data and functionality within the Asana platform. This API enables users to progra
  name: Asana Jobs  API
  phrasing_intents:
  - id: getJob
    intent: Check an asynchronous job's status
    question: Has my project duplication job finished?
  phrasing_ops: 1
  slug: asana-jobs-api
- baseURL: https://app.asana.com/api/1.0
  baseurl_source: spec
  description: 'The Asana Memberships API is a tool that allows developers to integrate Asana''s membership features into their own applications. This API allows users to access and manage information related to team '
  name: Asana Memberships  API
  phrasing_intents:
  - id: getMemberships
    intent: List members of a goal, project or portfolio
    question: Who are the members of a given goal or project?
  - id: createMembership
    intent: Add a member to a goal, project or portfolio
    question: Can I add a team as a member of a project?
  - id: getMembership
    intent: Get a project membership by ID
    question: What access level does a particular project membership grant?
  - id: updateMembership
    intent: Change a member's access level
    question: How do I change someone's access level on a project or goal?
  - id: deleteMembership
    intent: Remove a membership
    question: Can I remove a user's membership in a goal, project or portfolio by membership ID?
  phrasing_ops: 5
  slug: asana-memberships-api
- baseURL: https://app.asana.com/api/1.0
  baseurl_source: spec
  description: The Asana Organization Exports API is a tool that allows users to extract and download data from their Asana organization for external use. This API enables business owners and project managers to exp
  name: Asana Organization Exports  API
  phrasing_intents:
  - id: createOrganizationExport
    intent: Request a full organization export
    question: How do I export all of my organization's data?
  - id: getOrganizationExport
    intent: Check an organization export request
    question: Is my organization export finished yet?
  phrasing_ops: 2
  slug: asana-organization-exports-api
- baseURL: https://app.asana.com/api/1.0
  baseurl_source: spec
  description: Asana Portfolios API allows developers to access and manage portfolios in the Asana platform programmatically. With this API, users can create, update, and delete portfolios, as well as add projects a
  name: Asana Portfolios  API
  phrasing_intents:
  - id: getPortfolios
    intent: List portfolios I own in a workspace
    question: Which portfolios do I own in a workspace?
  - id: createPortfolio
    intent: Create a portfolio
    question: How do I create a portfolio in Asana?
  - id: getPortfolio
    intent: Get a portfolio's details
    question: What's in the full record of a portfolio?
  - id: updatePortfolio
    intent: Update a portfolio
    question: Can I rename a portfolio or change its color?
  - id: deletePortfolio
    intent: Delete a portfolio
    question: Can I delete a portfolio I no longer use?
  - id: getItemsForPortfolio
    intent: List the projects in a portfolio
    question: Which projects are inside a portfolio?
  - id: addItemForPortfolio
    intent: Add a project to a portfolio
    question: How do I put a project into a portfolio?
  - id: removeItemForPortfolio
    intent: Remove a project from a portfolio
    question: Can I take a project out of a portfolio without deleting it?
  phrasing_ops: 12
  slug: asana-portfolios-api
- baseURL: https://app.asana.com/api/1.0
  baseurl_source: spec
  description: The Asana Project Templates API is a tool that allows users to access and utilize pre-designed project templates within the Asana platform. With this API, users can easily create and customize project
  name: Asana Project Templates  API
  phrasing_intents:
  - id: getProjectTemplate
    intent: Get a project template
    question: What does a project template include, like its requested dates and roles?
  - id: deleteProjectTemplate
    intent: Delete a project template
    question: Can I delete a project template we no longer use?
  - id: getProjectTemplates
    intent: List project templates in a workspace or team
    question: What project templates are available in my workspace?
  - id: getProjectTemplatesForTeam
    intent: List a team's project templates
    question: Which project templates belong to a particular team?
  - id: instantiateProject
    intent: Create a project from a project template
    question: How do I spin up a new project from a template?
  phrasing_ops: 5
  slug: asana-project-templates-api
- baseURL: https://app.asana.com/api/1.0
  baseurl_source: spec
  description: The Asana Projects API is a tool that allows users to programmatically interact with Asana projects, enabling them to create, update, and manage tasks and projects within the Asana platform. By levera
  name: Asana Projects  API
  phrasing_intents:
  - id: getProjects
    intent: List projects filtered by workspace or team
    question: How do I list projects across a workspace or team?
  - id: createProject
    intent: Create a project
    question: How do I create a new project in Asana?
  - id: getProject
    intent: Get a project's details
    question: What does the full record for one project include?
  - id: updateProject
    intent: Update a project's settings
    question: How can I rename a project or change its owner?
  - id: deleteProject
    intent: Delete a project
    question: What happens when I delete a project?
  - id: duplicateProject
    intent: Duplicate a project
    question: Can I copy a whole project including its tasks and members?
  - id: getProjectsForTask
    intent: List the projects a task belongs to
    question: Which projects is a given task part of?
  - id: getProjectsForTeam
    intent: List a team's projects
    question: What projects does a particular team own?
  phrasing_ops: 19
  slug: asana-projects-api
- baseURL: https://app.asana.com/api/1.0
  baseurl_source: spec
  description: The Asana Sections API provides developers with the ability to programmatically interact with and manage sections within Asana projects. This API allows users to create, update, and delete sections as
  name: Asana Sections  API
  phrasing_intents:
  - id: getSection
    intent: Get a section's details
    question: What does a single section's record contain?
  - id: updateSection
    intent: Rename a section
    question: How do I rename a section or board column?
  - id: deleteSection
    intent: Delete an empty section
    question: Can I delete a section that still has tasks in it?
  - id: getSectionsForProject
    intent: List the sections in a project
    question: What sections or board columns does a project have?
  - id: createSectionForProject
    intent: Create a section in a project
    question: How do I add a new section or column to a project?
  - id: addTaskForSection
    intent: Move a task into a section
    question: How do I move a task into a different section?
  - id: insertSectionForProject
    intent: Reorder sections in a project
    question: Can I move one section above or below another?
  phrasing_ops: 7
  slug: asana-sections-api
- baseURL: https://app.asana.com/api/1.0
  baseurl_source: spec
  description: The Asana Status Updates API allows users to retrieve and update the status of tasks and projects within the Asana platform. This API enables developers to programmatically interact with the status up
  name: Asana Status Updates  API
  phrasing_intents:
  - id: getStatus
    intent: Get a status update
    question: What does a single status update say?
  - id: deleteStatus
    intent: Delete a status update
    question: Can I delete a status update I posted?
  - id: getStatusesForObject
    intent: List status updates on a project, portfolio or goal
    question: What status updates have been posted on a project or goal?
  - id: createStatusForObject
    intent: Post a status update
    question: How do I post a status update on a project, portfolio or goal?
  phrasing_ops: 4
  slug: asana-status-updates-api
- baseURL: https://app.asana.com/api/1.0
  baseurl_source: spec
  description: The Asana Tags API allows developers to programmatically create, read, update, and delete tags within the Asana project management tool. Tags are customizable labels that can be applied to tasks to he
  name: Asana Tags  API
  phrasing_intents:
  - id: getTags
    intent: List tags with optional workspace filter
    question: Which tags can I see across my workspaces?
  - id: createTag
    intent: Create a tag
    question: How do I create a new tag?
  - id: getTag
    intent: Get a tag's details
    question: What does a single tag's full record show?
  - id: updateTag
    intent: Update a tag
    question: Can I rename a tag or change its color?
  - id: deleteTag
    intent: Delete a tag
    question: Can I delete a tag I no longer use?
  phrasing_ops: 5
  slug: asana-tags-api
- baseURL: https://app.asana.com/api/1.0
  baseurl_source: spec
  description: The Asana Task Templates API allows users to create, manage, and customize task templates within the Asana platform. This API enables developers to programmatically interact with task templates, allow
  name: Asana Task Templates  API
  phrasing_intents:
  - id: getTaskTemplates
    intent: List a project's task templates
    question: What task templates does a project have?
  - id: getTaskTemplate
    intent: Get a task template
    question: What does a single task template contain?
  - id: deleteTaskTemplate
    intent: Delete a task template
    question: Can I delete a task template we no longer use?
  - id: instantiateTask
    intent: Create a task from a task template
    question: How do I create a task from a template?
  phrasing_ops: 4
  slug: asana-task-templates-api
- baseURL: https://app.asana.com/api/1.0
  baseurl_source: spec
  description: The Asana Tasks API is a powerful tool that allows developers to programmatically manage tasks and projects within the Asana platform. With this API, users can create, update, and delete tasks, as wel
  name: Asana Tasks  API
  phrasing_intents:
  - id: getTagsForTask
    intent: List the tags on a task
    question: Which tags have been applied to a particular Asana task?
  - id: getTasks
    intent: List tasks filtered by project, assignee or section
    question: How do I list tasks assigned to someone in a workspace?
  - id: createTask
    intent: Create a new task
    question: How do I create a new task in Asana?
  - id: getTask
    intent: Get the full details of a task
    question: What does the full record of one task include?
  - id: updateTask
    intent: Update a task's fields
    question: How can I change the due date or assignee on an existing task?
  - id: deleteTask
    intent: Delete a task
    question: What happens to a task after I delete it — can it be recovered from trash?
  - id: duplicateTask
    intent: Duplicate a task
    question: Can I copy an existing task, including its subtasks and attachments?
  - id: getTasksForProject
    intent: List the tasks in a project
    question: How do I list every task in a project in priority order?
  phrasing_ops: 28
  slug: asana-tasks-api
- baseURL: https://app.asana.com/api/1.0
  baseurl_source: spec
  description: Asana Teams API is a powerful tool that allows users to automate and streamline their team's workflow within the Asana platform. By utilizing this API, developers can create custom integrations and ap
  name: Asana Teams  API
  phrasing_intents:
  - id: createTeam
    intent: Create a team
    question: How do I create a new team in my organization?
  - id: getTeam
    intent: Get a team's details
    question: What does a team's full record include?
  - id: updateTeam
    intent: Update a team
    question: Can I rename a team or change its visibility?
  - id: getTeamsForWorkspace
    intent: List the teams in a workspace
    question: What teams exist in my organization?
  - id: getTeamsForUser
    intent: List the teams a user belongs to
    question: Which teams is a particular person on?
  - id: addUserForTeam
    intent: Add a user to a team
    question: How do I add someone to a team?
  - id: removeUserForTeam
    intent: Remove a user from a team
    question: Can I take someone off a team?
  phrasing_ops: 7
  slug: asana-teams-api
- baseURL: https://app.asana.com/api/1.0
  baseurl_source: spec
  description: The Asana Time Periods API is a tool that allows users to access and manage time periods within the Asana project management platform. This API enables developers to create, update, and delete time pe
  name: Asana Time Periods  API
  phrasing_intents:
  - id: getTimePeriod
    intent: Get a time period
    question: What dates does a given time period cover?
  - id: getTimePeriods
    intent: List time periods in a workspace
    question: What time periods like quarters are defined for goals in my workspace?
  phrasing_ops: 2
  slug: asana-time-periods-api
- baseURL: https://app.asana.com/api/1.0
  baseurl_source: spec
  description: The Asana Time Tracking Entries API is a tool that allows users to record and track time spent on tasks and projects within the Asana platform. This API enables developers to create custom time tracki
  name: Asana Time Tracking Entries  API
  phrasing_intents:
  - id: getTimeTrackingEntriesForTask
    intent: List time logged on a task
    question: How much time has been logged against a task?
  - id: createTimeTrackingEntry
    intent: Log time on a task
    question: How do I log time I spent on a task?
  - id: getTimeTrackingEntry
    intent: Get a time tracking entry
    question: What does a single time entry record show?
  - id: updateTimeTrackingEntry
    intent: Edit a time tracking entry
    question: Can I correct the duration on a time entry I logged?
  - id: deleteTimeTrackingEntry
    intent: Delete a time tracking entry
    question: Can I delete time I logged by mistake?
  phrasing_ops: 5
  slug: asana-time-tracking-entries-api
- baseURL: https://app.asana.com/api/1.0
  baseurl_source: spec
  description: Asana User Task Lists API is a tool that allows users to create, update, and manage task lists within the Asana platform. By using this API, users can access their task lists, view all the tasks withi
  name: Asana User Task Lists  API
  phrasing_intents:
  - id: getUserTaskList
    intent: Get a My Tasks list by its ID
    question: What does a user task list record contain?
  - id: getUserTaskListForUser
    intent: Find a user's My Tasks list
    question: How do I find someone's My Tasks list ID in a workspace?
  phrasing_ops: 2
  slug: asana-user-task-lists-api
- baseURL: https://app.asana.com/api/1.0
  baseurl_source: spec
  description: Asana Users API allows developers to interact with user data within the Asana project management platform. This API enables users to retrieve information about individual users, such as their names, e
  name: Asana Users  API
  phrasing_intents:
  - id: getUsers
    intent: List users I can see
    question: Which users can I see across my workspaces?
  - id: getUser
    intent: Get a user's profile
    question: How do I look up a user's name and email?
  - id: getFavoritesForUser
    intent: List a user's favorites
    question: What projects has a user starred as favorites?
  - id: getUsersForTeam
    intent: List the users in a team
    question: Who is on a particular team?
  - id: getUsersForWorkspace
    intent: List the users in a workspace
    question: Who are all the people in my organization?
  phrasing_ops: 5
  slug: asana-users-api
- baseURL: https://app.asana.com/api/1.0
  baseurl_source: spec
  description: Asana Webhooks API allows developers to receive real-time updates about changes and events happening within Asana. By setting up webhooks, users can subscribe to specific events such as task creation,
  name: Asana Webhooks  API
  phrasing_intents:
  - id: getWebhooks
    intent: List my webhooks in a workspace
    question: Which webhooks has my app registered in a workspace?
  - id: createWebhook
    intent: Subscribe to changes with a webhook
    question: How do I get notified when tasks in a project change?
  - id: getWebhook
    intent: Get a webhook's details
    question: What resource and target does a webhook point at?
  - id: updateWebhook
    intent: Change a webhook's filters
    question: Can I change which events a webhook receives?
  - id: deleteWebhook
    intent: Delete a webhook
    question: Can I still receive events right after deleting a webhook?
  phrasing_ops: 5
  slug: asana-webhooks-api
- baseURL: https://app.asana.com/api/1.0
  baseurl_source: spec
  description: 'The Asana Workspaces API allows users to access and manipulate data within their Asana workspaces programmatically. With this API, developers can create custom integrations, automate tasks, and build '
  name: Asana Workspaces  API
  phrasing_intents:
  - id: getTagsForWorkspace
    intent: List the tags in a workspace
    question: What tags already exist in a given workspace?
  - id: createTagForWorkspace
    intent: Create a tag in a specific workspace
    question: How do I create a tag scoped to a particular workspace by its ID?
  - id: getWorkspaces
    intent: List my workspaces
    question: Which workspaces and organizations can I access?
  - id: getWorkspace
    intent: Get a workspace's details
    question: Is a given workspace an organization?
  - id: updateWorkspace
    intent: Rename a workspace
    question: Can I change a workspace's name?
  - id: addUserForWorkspace
    intent: Add a user to a workspace
    question: How do I invite someone to my workspace by email?
  - id: removeUserForWorkspace
    intent: Remove a user from a workspace
    question: Do I need to be an admin to remove someone from a workspace?
  phrasing_ops: 7
  slug: asana-workspaces-api
- description: The Asana Access Requests API allows users to manage access requests for resources such as projects and portfolios. With this API, users can retrieve pending access requests, create new access request
  name: Asana Access Requests API
  slug: asana-access-requests-api
- description: The Asana Audit Log API provides an immutable log of important events within an organization's Asana instance. This API enables organizations to set up proactive alerting with SIEM tools, conduct reac
  name: Asana Audit Log API
  slug: asana-audit-log-api
- description: The Asana Budgets API allows developers to manage budget resources for projects. A budget object represents a budget for a specific parent resource such as a project and tracks values in either time o
  name: Asana Budgets API
  slug: asana-budgets-api
- description: The Asana Custom Types API allows developers to retrieve custom type resources associated with objects in Asana. A custom type includes properties such as name and status options, where each status op
  name: Asana Custom Types API
  slug: asana-custom-types-api
- description: The Asana Exports API provides graph export and resource export functionality for extracting data from Asana. Exports are generated in gzipped JSONL format with presigned S3 URLs that expire in one ho
  name: Asana Exports API
  slug: asana-exports-api
- description: The Asana Rates API allows developers to manage rate resources within projects. A rate represents a monetary value associated with a user for a specific project, tracking values in designated currency
  name: Asana Rates API
  slug: asana-rates-api
- description: The Asana Reactions API allows developers to retrieve emoji reactions on objects within Asana. Each reaction includes the emoji string used and information about the user who created it. This API enab
  name: Asana Reactions API
  slug: asana-reactions-api
- description: 'The Asana Roles API allows developers to programmatically manage Role-Based Access Control (RBAC) at the domain level. The API supports creating, retrieving, updating, and deleting roles. Read access '
  name: Asana Roles API
  slug: asana-roles-api
- baseURL: https://app.asana.com/api/1.0
  baseurl_source: spec
  description: Asana's audit log is an immutable log of [important events](/docs/audit-log-events#supported-audit-log-events) in your organization's Asana instance. The audit log API allows you to monitor and act up
  name: Asana Audit Log API
  phrasing_intents:
  - id: getAuditLogEvents
    intent: Pull audit log events for a domain
    question: How do I pull the audit log for my Asana domain?
  phrasing_ops: 1
  slug: asana-audit-log-api-api
- baseURL: https://app.asana.com/api/1.0
  baseurl_source: spec
  description: Perform multiple operations in a single HTTP request.
  name: Asana Batch API
  phrasing_intents:
  - id: createBatchRequest
    intent: Run several API requests in one batch
    question: Can I send multiple API calls in a single request?
  phrasing_ops: 1
  slug: asana-batch-api-api
- baseURL: https://app.asana.com/api/1.0
  baseurl_source: spec
  description: The Asana Custom Field Settings API manages the association between custom fields and projects, portfolios, teams, and goals. Custom fields are attached to a particular project with the custom field s
  name: Asana Custom Field Settings API
  phrasing_intents:
  - id: getCustomFieldSettingsForProject
    intent: List the custom fields on a project
    question: Which custom fields are set up on a project?
  - id: getCustomFieldSettingsForPortfolio
    intent: List the custom fields on a portfolio
    question: Which custom fields are configured on a portfolio?
  phrasing_ops: 2
  slug: asana-custom-field-settings-api
- baseURL: https://app.asana.com/api/1.0
  baseurl_source: spec
  description: The Asana Portfolio Memberships API allows developers to retrieve portfolio membership information. A portfolio membership represents the relationship between a user and a portfolio, including their a
  name: Asana Portfolio Memberships API
  phrasing_intents:
  - id: getPortfolioMemberships
    intent: List portfolio memberships by portfolio or user
    question: Which portfolios is a user a member of in a workspace?
  - id: getPortfolioMembership
    intent: Get a portfolio membership
    question: What does a single portfolio membership record include?
  - id: getPortfolioMembershipsForPortfolio
    intent: List a portfolio's memberships
    question: Who has membership in a specific portfolio?
  phrasing_ops: 3
  slug: asana-portfolio-memberships-api
- baseURL: https://app.asana.com/api/1.0
  baseurl_source: spec
  description: The Asana Project Briefs API allows developers to manage rich text documents that describe projects. A project brief includes a title, rich text content, and a permalink URL. The API supports creating
  name: Asana Project Briefs API
  phrasing_intents:
  - id: getProjectBrief
    intent: Get a project brief
    question: How do I read the overview brief written for a project?
  - id: updateProjectBrief
    intent: Edit a project brief
    question: Can I rewrite the text of a project brief?
  - id: deleteProjectBrief
    intent: Delete a project brief
    question: Can I remove the brief from a project?
  - id: createProjectBrief
    intent: Write a brief for a project
    question: How do I add an overview brief to a project?
  phrasing_ops: 4
  slug: asana-project-briefs-api
- baseURL: https://app.asana.com/api/1.0
  baseurl_source: spec
  description: The Asana Project Memberships API provides endpoints for retrieving project membership records. These endpoints enable developers to query membership information for projects, including setting member
  name: Asana Project Memberships API
  phrasing_intents:
  - id: getProjectMembership
    intent: Get a project membership
    question: What access does a single project membership record grant?
  - id: getProjectMembershipsForProject
    intent: List a project's memberships
    question: Who are the members of a particular project?
  phrasing_ops: 2
  slug: asana-project-memberships-api
- baseURL: https://app.asana.com/api/1.0
  baseurl_source: spec
  description: The Asana Project Statuses API allows developers to manage progress updates on projects. A project status includes descriptive text and color codes indicating the project state such as green for on tr
  name: Asana Project Statuses API
  phrasing_intents:
  - id: getProjectStatus
    intent: Get a legacy project status
    question: Can I still fetch an old-style project status update by ID?
  - id: deleteProjectStatus
    intent: Delete a legacy project status
    question: Can I delete an old-style project status?
  - id: getProjectStatusesForProject
    intent: List a project's legacy status updates
    question: How do I list a project's status updates on the older project status route?
  - id: createProjectStatusForProject
    intent: Post a legacy project status
    question: Can I still post a project status with the older project status endpoint?
  phrasing_ops: 4
  slug: asana-project-statuses-api
- baseURL: https://app.asana.com/api/1.0
  baseurl_source: spec
  description: The Asana Rules API allows developers to automate common patterns and workflows by combining triggers with automatic actions. The API supports triggering rules via incoming web requests, enabling exte
  name: Asana Rules API
  phrasing_intents:
  - id: triggerRule
    intent: Trigger a rule via incoming web request
    question: Can I trigger an automation rule from an external system?
  phrasing_ops: 1
  slug: asana-rules-api
- baseURL: https://app.asana.com/api/1.0
  baseurl_source: spec
  description: The Asana Stories API allows developers to manage stories, which are records of activity associated with objects in the Asana system. Stories are generated by the system when users take actions such a
  name: Asana Stories API
  phrasing_intents:
  - id: getStory
    intent: Get a story or comment
    question: What does a single story or comment record contain?
  - id: updateStory
    intent: Edit a comment
    question: Can I edit the text of a comment I posted?
  - id: deleteStory
    intent: Delete a comment
    question: Can I delete a comment someone else wrote?
  - id: getStoriesForTask
    intent: List a task's comments and activity
    question: How do I read the comments and activity history on a task?
  - id: createStoryForTask
    intent: Comment on a task
    question: How do I post a comment on a task?
  phrasing_ops: 5
  slug: asana-stories-api
- baseURL: https://app.asana.com/api/1.0
  baseurl_source: spec
  description: The Asana Team Memberships API allows developers to retrieve team membership records. A team membership represents the relationship between a user and a team, including flags for guest status, limited
  name: Asana Team Memberships API
  phrasing_intents:
  - id: getTeamMembership
    intent: Get a team membership
    question: What does a single team membership record include?
  - id: getTeamMemberships
    intent: List team memberships by team, user or workspace
    question: Which teams is a user a member of in a workspace?
  - id: getTeamMembershipsForTeam
    intent: List a team's memberships
    question: Who holds membership in a particular team?
  - id: getTeamMembershipsForUser
    intent: List a user's team memberships
    question: What team memberships does a user hold in a workspace?
  phrasing_ops: 4
  slug: asana-team-memberships-api
- baseURL: https://app.asana.com/api/1.0
  baseurl_source: spec
  description: The Asana Typeahead API provides search functionality for objects within a single workspace. This API enables developers to build autocomplete and search-as-you-type features by retrieving Asana objec
  name: Asana Typeahead API
  phrasing_intents:
  - id: typeaheadForWorkspace
    intent: Quickly find objects by name as you type
    question: What's the fastest way to power an autocomplete picker for projects or users?
  phrasing_ops: 1
  slug: asana-typeahead-api
- baseURL: https://app.asana.com/api/1.0
  baseurl_source: spec
  description: The Asana Workspace Memberships API allows developers to determine if a user is a member of a workspace and retrieve membership details. The API provides endpoints to get a specific workspace membersh
  name: Asana Workspace Memberships API
  phrasing_intents:
  - id: getWorkspaceMembership
    intent: Get a workspace membership
    question: What does a single workspace membership record include?
  - id: getWorkspaceMembershipsForUser
    intent: List a user's workspace memberships
    question: Which workspaces does a particular user belong to?
  - id: getWorkspaceMembershipsForWorkspace
    intent: List a workspace's memberships
    question: Who are all the members of a workspace?
  phrasing_ops: 3
  slug: asana-workspace-memberships-api
arazzos:
- description: Create a workspace custom field and attach it to a project as a custom field setting.
  name: Asana Add a Custom Field to a Project
  slug: asana-add-custom-field-to-project-workflow
- description: Confirm a task exists, add it to a project section, and note the move with a comment.
  name: Asana Add an Existing Task to a Project Section
  slug: asana-add-existing-task-to-project-workflow
- description: Create a task, assign it to an owner, and add followers who should be notified.
  name: Asana Assign and Add Followers to a Task
  slug: asana-assign-and-follow-task-workflow
- description: Create a task and attach an external file URL to it as a reference.
  name: Asana Attach a File to a New Task
  slug: asana-attach-file-to-task-workflow
- description: Create a project in a team, add a section to it, drop a first task into the project, and open the discussion with a comment.
  name: Asana Bootstrap a Project Board
  slug: asana-bootstrap-project-board-workflow
- description: Create an enum custom field in a workspace and add two enum options to it.
  name: Asana Build an Enum Custom Field With Options
  slug: asana-build-enum-custom-field-workflow
- description: Read a task, post a closing comment, and mark it complete in a single closeout pass.
  name: Asana Find, Comment On, and Complete a Task
  slug: asana-complete-task-with-comment-workflow
- description: Create a parent task, then add two subtasks under it to break the work down.
  name: Asana Create a Task With Subtasks
  slug: asana-create-task-with-subtasks-workflow
- description: Create a team in an organization and stand up its first project.
  name: Asana Create a Team With a First Project
  slug: asana-create-team-with-project-workflow
- description: Kick off a project duplication job and poll the async job until it succeeds.
  name: Asana Duplicate a Project and Poll the Job
  slug: asana-duplicate-project-and-poll-workflow
- description: List a project's sections, then insert a new section at the top of the board.
  name: Asana Insert a Section Into a Project
  slug: asana-insert-section-into-project-workflow
- description: Create a blocking task and a dependent task, then wire the dependency between them.
  name: Asana Create Dependent Tasks
  slug: asana-link-task-dependencies-workflow
- description: Remove a user from a team and then remove them from the workspace.
  name: Asana Offboard a User
  slug: asana-offboard-user-workflow
- description: Add a user to a workspace and then add them to a team within that workspace.
  name: Asana Onboard a User to a Workspace and Team
  slug: asana-onboard-user-to-workspace-and-team-workflow
- description: Read a project's task counts, then post a status update summarizing progress.
  name: Asana Post a Project Status Update
  slug: asana-post-project-status-update-workflow
- description: Create a standalone task and then set its parent so it becomes a subtask.
  name: Asana Create a Task and Nest It Under a Parent
  slug: asana-promote-task-to-subtask-workflow
- description: Create a tag in a workspace and immediately apply it to an existing task.
  name: Asana Provision a Tag and Label a Task
  slug: asana-provision-tag-and-label-task-workflow
- description: Create a project directly in a workspace and seed it with a first task.
  name: Asana Provision a Workspace Project With a First Task
  slug: asana-provision-workspace-project-workflow
- description: Read the most recent status update on a project, then post a fresh one.
  name: Asana Refresh a Project's Status Update
  slug: asana-refresh-project-status-update-workflow
- description: Read the existing comments on a task, then post a reply comment to the thread.
  name: Asana Review and Reply on a Task Comment Thread
  slug: asana-review-and-reply-comment-thread-workflow
- description: Search a workspace for a task by text, then reassign the first match to a new owner.
  name: Asana Search and Reassign a Task
  slug: asana-search-and-reassign-task-workflow
- description: Create a task, place it in a section, and label it with a tag in one triage pass.
  name: Asana Triage and Tag a Task
  slug: asana-triage-and-tag-task-workflow
artifact_total: 367
asyncapis:
- description: 'The Asana Webhooks Events API delivers real-time event notifications to your application when changes occur on Asana resources. Webhooks use HTTP POST to deliver events to a target URL you configure. '
  name: Asana Webhooks Events API
  slug: asana-webhooks-asyncapi
collections:
- collection_type: postman
  name: Asana Allocations API
  slug: postman-asana-allocations-api
- collection_type: postman
  name: Asana Attachments API
  slug: postman-asana-attachments-api
- collection_type: postman
  name: Asana Batch API
  slug: postman-asana-batch-api
- collection_type: postman
  name: Asana Custom Fields API
  slug: postman-asana-custom-fields-api
- collection_type: postman
  name: Asana Enum Options API
  slug: postman-asana-enum-options-api
- collection_type: postman
  name: Asana Events API
  slug: postman-asana-events-api
- collection_type: postman
  name: Asana Goal Relationships API
  slug: postman-asana-goal-relationships-api
- collection_type: postman
  name: Asana Goals API
  slug: postman-asana-goals-api
- collection_type: postman
  name: Asana Jobs API
  slug: postman-asana-jobs-api
- collection_type: postman
  name: Asana Memberships API
  slug: postman-asana-memberships-api
- collection_type: postman
  name: Asana Organization Exports API
  slug: postman-asana-organization-exports-api
- collection_type: postman
  name: Asana Portfolios API
  slug: postman-asana-portfolios-api
- collection_type: postman
  name: Asana Project Templates API
  slug: postman-asana-project-templates-api
- collection_type: postman
  name: Asana Projects API
  slug: postman-asana-projects-api
- collection_type: postman
  name: Asana Rule Triggers API
  slug: postman-asana-rule-triggers-api
- collection_type: postman
  name: Asana Sections API
  slug: postman-asana-sections-api
- collection_type: postman
  name: Asana Status Updates API
  slug: postman-asana-status-updates-api
- collection_type: postman
  name: Asana Tags API
  slug: postman-asana-tags-api
- collection_type: postman
  name: Asana Task Templates API
  slug: postman-asana-task-templates-api
- collection_type: postman
  name: Asana Tasks API
  slug: postman-asana-tasks-api
- collection_type: postman
  name: Asana Teams API
  slug: postman-asana-teams-api
- collection_type: postman
  name: Asana Time Periods API
  slug: postman-asana-time-periods-api
- collection_type: postman
  name: Asana Time Tracking Entries API
  slug: postman-asana-time-tracking-entries-api
- collection_type: postman
  name: Asana User Task Lists API
  slug: postman-asana-user-task-lists-api
- collection_type: postman
  name: Asana Users API
  slug: postman-asana-users-api
- collection_type: postman
  name: Asana Webhooks API
  slug: postman-asana-webhooks-api
- collection_type: postman
  name: Asana Workspaces API
  slug: postman-asana-workspaces-api
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Asana Allocations API
  slug: open-asana-allocations-api
- collection_type: open
  name: Asana Allocations Attachments API
  slug: open-asana-attachments-api
- collection_type: open
  name: Asana Allocations Audit Log API API
  slug: open-asana-audit-log-api-api
- collection_type: open
  name: Asana Allocations Batch API API
  slug: open-asana-batch-api-api
- collection_type: open
  name: Asana Batch API
  slug: open-asana-batch-api
- collection_type: open
  name: Asana Allocations Custom Field Settings API
  slug: open-asana-custom-field-settings-api
- collection_type: open
  name: Asana Allocations Custom Fields API
  slug: open-asana-custom-fields-api
- collection_type: open
  name: Asana Allocations Enum Options API
  slug: open-asana-enum-options-api
- collection_type: open
  name: Asana Allocations Events API
  slug: open-asana-events-api
- collection_type: open
  name: Asana Allocations Goal Relationships API
  slug: open-asana-goal-relationships-api
- collection_type: open
  name: Asana Allocations Goals API
  slug: open-asana-goals-api
- collection_type: open
  name: Asana Allocations Jobs API
  slug: open-asana-jobs-api
- collection_type: open
  name: Asana Allocations Memberships API
  slug: open-asana-memberships-api
- collection_type: open
  name: Asana Allocations Organization Exports API
  slug: open-asana-organization-exports-api
- collection_type: open
  name: Asana Allocations Portfolio Memberships API
  slug: open-asana-portfolio-memberships-api
- collection_type: open
  name: Asana Allocations Portfolios API
  slug: open-asana-portfolios-api
- collection_type: open
  name: Asana Allocations Project Briefs API
  slug: open-asana-project-briefs-api
- collection_type: open
  name: Asana Allocations Project Memberships API
  slug: open-asana-project-memberships-api
- collection_type: open
  name: Asana Allocations Project Statuses API
  slug: open-asana-project-statuses-api
- collection_type: open
  name: Asana Allocations Project Templates API
  slug: open-asana-project-templates-api
- collection_type: open
  name: Asana Allocations Projects API
  slug: open-asana-projects-api
- collection_type: open
  name: Asana Rule Triggers API
  slug: open-asana-rule-triggers-api
- collection_type: open
  name: Asana Allocations Rules API
  slug: open-asana-rules-api
- collection_type: open
  name: Asana Allocations Sections API
  slug: open-asana-sections-api
- collection_type: open
  name: Asana Allocations Status Updates API
  slug: open-asana-status-updates-api
- collection_type: open
  name: Asana Allocations Stories API
  slug: open-asana-stories-api
- collection_type: open
  name: Asana Allocations Tags API
  slug: open-asana-tags-api
- collection_type: open
  name: Asana Allocations Task Templates API
  slug: open-asana-task-templates-api
- collection_type: open
  name: Asana Allocations Tasks API
  slug: open-asana-tasks-api
- collection_type: open
  name: Asana Allocations Team Memberships API
  slug: open-asana-team-memberships-api
- collection_type: open
  name: Asana Allocations Teams API
  slug: open-asana-teams-api
- collection_type: open
  name: Asana Allocations Time Periods API
  slug: open-asana-time-periods-api
- collection_type: open
  name: Asana Allocations Time Tracking Entries API
  slug: open-asana-time-tracking-entries-api
- collection_type: open
  name: Asana Allocations Typeahead API
  slug: open-asana-typeahead-api
- collection_type: open
  name: Asana Allocations User Task Lists API
  slug: open-asana-user-task-lists-api
- collection_type: open
  name: Asana Allocations Users API
  slug: open-asana-users-api
- collection_type: open
  name: Asana Allocations Webhooks API
  slug: open-asana-webhooks-api
- collection_type: open
  name: Asana Allocations Workspace Memberships API
  slug: open-asana-workspace-memberships-api
- collection_type: open
  name: Asana Allocations Workspaces API
  slug: open-asana-workspaces-api
- collection_type: open
  name: Asana
  slug: open-asana
common:
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/asana/refs/heads/main/capabilities/asana-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/asana-capability-edges.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/asana/refs/heads/main/agentic-access/asana-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/asana-agentic-access.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/asana/refs/heads/main/security/asana-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/asana-trust-center.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/asana/refs/heads/main/security/asana-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/asana-vulnerability-disclosure.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/asana/refs/heads/main/security/asana-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/asana-domain-security.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/asana/refs/heads/main/authentication/asana-authentication.yml
  title: ''
  type: Authentication
  url: authentication/asana-authentication.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/asana/refs/heads/main/scopes/asana-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/asana-scopes.yml
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/asana/overview
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/asana/refs/heads/main/arazzo/asana-add-custom-field-to-project-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/asana-add-custom-field-to-project-workflow.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/asana/refs/heads/main/arazzo/asana-add-existing-task-to-project-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/asana-add-existing-task-to-project-workflow.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/asana/refs/heads/main/arazzo/asana-assign-and-follow-task-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/asana-assign-and-follow-task-workflow.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/asana/refs/heads/main/arazzo/asana-attach-file-to-task-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/asana-attach-file-to-task-workflow.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/asana/refs/heads/main/arazzo/asana-bootstrap-project-board-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/asana-bootstrap-project-board-workflow.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/asana/refs/heads/main/arazzo/asana-build-enum-custom-field-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/asana-build-enum-custom-field-workflow.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/asana/refs/heads/main/arazzo/asana-complete-task-with-comment-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/asana-complete-task-with-comment-workflow.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/asana/refs/heads/main/arazzo/asana-create-task-with-subtasks-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/asana-create-task-with-subtasks-workflow.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/asana/refs/heads/main/arazzo/asana-create-team-with-project-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/asana-create-team-with-project-workflow.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/asana/refs/heads/main/arazzo/asana-duplicate-project-and-poll-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/asana-duplicate-project-and-poll-workflow.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/asana/refs/heads/main/arazzo/asana-insert-section-into-project-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/asana-insert-section-into-project-workflow.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/asana/refs/heads/main/arazzo/asana-link-task-dependencies-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/asana-link-task-dependencies-workflow.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/asana/refs/heads/main/arazzo/asana-offboard-user-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/asana-offboard-user-workflow.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/asana/refs/heads/main/arazzo/asana-onboard-user-to-workspace-and-team-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/asana-onboard-user-to-workspace-and-team-workflow.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/asana/refs/heads/main/arazzo/asana-post-project-status-update-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/asana-post-project-status-update-workflow.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/asana/refs/heads/main/arazzo/asana-promote-task-to-subtask-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/asana-promote-task-to-subtask-workflow.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/asana/refs/heads/main/arazzo/asana-provision-tag-and-label-task-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/asana-provision-tag-and-label-task-workflow.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/asana/refs/heads/main/arazzo/asana-provision-workspace-project-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/asana-provision-workspace-project-workflow.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/asana/refs/heads/main/arazzo/asana-refresh-project-status-update-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/asana-refresh-project-status-update-workflow.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/asana/refs/heads/main/arazzo/asana-review-and-reply-comment-thread-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/asana-review-and-reply-comment-thread-workflow.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/asana/refs/heads/main/arazzo/asana-search-and-reassign-task-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/asana-search-and-reassign-task-workflow.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/asana/refs/heads/main/arazzo/asana-triage-and-tag-task-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/asana-triage-and-tag-task-workflow.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/asana
- group: docs
  title: ''
  type: Specification
  url: https://github.com/Asana/openapi
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/asana/refs/heads/main/json-ld/asana-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/asana-context.jsonld
- group: docs
  href: https://raw.githubusercontent.com/api-evangelist/asana/refs/heads/main/openapi/_original/asana-openapi.yml
  title: ''
  type: OpenAPI
  url: openapi/_original/asana-openapi.yml
- group: other
  title: ''
  type: Explorer
  url: https://developers.asana.com/docs/api-explorer
- group: start
  title: ''
  type: Sandbox
  url: https://developers.asana.com/docs/developer-sandbox
- group: start
  title: ''
  type: GettingStarted
  url: https://developers.asana.com/docs/quick-start
- group: operate
  title: ''
  type: FAQ
  url: https://developers.asana.com/docs/faq
- group: auth
  title: ''
  type: Authentication
  url: https://developers.asana.com/docs/authentication
- group: other
  title: ''
  type: OpenIDConnect
  url: https://developers.asana.com/docs/openid-connect
- group: docs
  title: ''
  type: Documentation
  url: https://developers.asana.com/docs/ac-api-reference
- group: build
  title: ''
  type: SDKs
  url: https://developers.asana.com/docs/client-libraries
- group: build
  title: ''
  type: Examples
  url: https://developers.asana.com/docs/examples
- group: build
  title: ''
  type: PostmanCollection
  url: https://developers.asana.com/docs/postman-collection
- group: operate
  title: ''
  type: ChangeLog
  url: https://developers.asana.com/docs/change-log
- group: design
  title: ''
  type: Components
  url: https://developers.asana.com/docs/app-components
- group: other
  title: ''
  type: Applications
  url: https://developers.asana.com/docs/manage-and-share-your-app
- group: other
  title: ''
  type: ApplicationDirectory
  url: https://developers.asana.com/docs/apps?category=all-apps
- group: docs
  title: ''
  type: Guide
  url: https://developers.asana.com/docs/overview
- group: company
  title: ''
  type: Partners
  url: https://developers.asana.com/docs/partners
- group: company
  title: ''
  type: Blog
  url: https://developers.asana.com/docs/inside-asana
- group: other
  title: ''
  type: Feedback
  url: https://developers.asana.com/docs/?k=C4sELCq6hAUsoWEY0kJwAA&d=15793206719
- group: commercial
  title: ''
  type: TermsOfService
  url: https://developers.asana.com/docs/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://developers.asana.com/docs/privacy-statement
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developers.asana.com
- group: operate
  title: ''
  type: Support
  url: https://asana.com/support
- group: operate
  title: ''
  type: Forums
  url: https://forum.asana.com
- group: operate
  title: ''
  type: Contact
  url: https://asana.com/support/contact
- group: start
  title: ''
  type: Signup
  url: https://asana.com/create-account
- group: start
  title: ''
  type: Login
  url: https://app.asana.com
- group: auth
  title: ''
  type: OAuth
  url: https://developers.asana.com/docs/oauth
- group: auth
  title: ''
  type: OAuthScopes
  url: https://developers.asana.com/docs/oauth-scopes
- group: operate
  title: ''
  type: RateLimits
  url: https://developers.asana.com/docs/rate-limits
- group: design
  title: ''
  type: Pagination
  url: https://developers.asana.com/docs/pagination
- group: design
  title: ''
  type: ErrorCodes
  url: https://developers.asana.com/docs/errors
- group: other
  title: ''
  type: InputOutputOptions
  url: https://developers.asana.com/docs/input-output-options
- group: other
  title: ''
  type: RichText
  url: https://developers.asana.com/docs/rich-text
- group: other
  title: ''
  type: SCIM
  url: https://developers.asana.com/docs/scim
- group: other
  title: ''
  type: AuditLogEvents
  url: https://developers.asana.com/docs/audit-log-events
- group: operate
  title: ''
  type: Deprecations
  url: https://developers.asana.com/docs/deprecations
- group: docs
  title: ''
  type: Documentation
  url: https://developers.asana.com/docs/object-hierarchy
- group: design
  title: ''
  type: Webhooks
  url: https://developers.asana.com/docs/webhooks
- group: docs
  title: ''
  type: Documentation
  url: https://developers.asana.com/docs/api-features
- group: docs
  title: ''
  type: Guide
  url: https://developers.asana.com/docs/building-app-components
- group: docs
  title: ''
  type: Guide
  url: https://developers.asana.com/docs/app-listing-guidelines
- group: company
  title: ''
  type: Website
  url: https://asana.com
- group: commercial
  title: ''
  type: Pricing
  url: https://asana.com/pricing
- group: operate
  title: ''
  type: StatusPage
  url: https://trust.asana.com
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Asana
- group: operate
  title: ''
  type: StackOverflow
  url: https://stackoverflow.com/questions/tagged/asana
- group: auth
  title: ''
  type: Security
  url: https://asana.com/trust
- group: learn
  title: ''
  type: YouTube
  url: https://www.youtube.com/@asana
- group: agent
  title: ''
  type: LlmsText
  url: https://asana.com/llms.txt
created: '2023-11-01'
description: Asana is a web and mobile application designed to help teams organize, track, and manage their work. The Asana API allows developers to programmatically access and integrate Asana's project management capabilities into their applications.
features:
- 'Personal plan: free forever, 2 users'
- Starter at $10.99/user/mo annual with timelines, dashboards, AI Studio (50K credits)
- Advanced at $24.99/user/mo with portfolios, goals, AI Studio (75K credits)
- 'Enterprise: SAML/SCIM, capacity planning, AI Studio (200K credits)'
- 'REST API: 1,500 req/min Paid, 150 req/min Free'
- 'Search API: 60 req/min'
- 50 concurrent request cap
- Webhooks for tasks, projects, comments
- OAuth 2.0 and personal access tokens
- Asana Connect for service accounts
- Custom Fields API
- Goals API for OKR tracking
- Time Tracking and Workload management
- AI Teammates and AI Studio
- Approvals and proofing workflows
- Salesforce, Tableau, Power BI integrations
finops:
- name: Asana Finops
  service_category: Project Management
  slug: asana-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/asana.png
json_schemas:
- name: AddCustomFieldSettingRequest
  property_count: 4
  slug: asana-addcustomfieldsettingrequest
- name: AddFollowersRequest
  property_count: 1
  slug: asana-addfollowersrequest
- name: AddMembersRequest
  property_count: 1
  slug: asana-addmembersrequest
- name: AllocationBase
  property_count: 5
  slug: asana-allocationbase
- name: AllocationRequest
  property_count: 5
  slug: asana-allocationrequest
- name: AllocationResponse
  property_count: 8
  slug: asana-allocationresponse
- name: AsanaNamedResource
  property_count: 3
  slug: asana-asananamedresource
- name: AsanaResource
  property_count: 2
  slug: asana-asanaresource
- name: AttachmentBase
  property_count: 0
  slug: asana-attachmentbase
- name: AttachmentCompact
  property_count: 4
  slug: asana-attachmentcompact
- name: AttachmentRequest
  property_count: 6
  slug: asana-attachmentrequest
- name: AttachmentResponse
  property_count: 12
  slug: asana-attachmentresponse
- name: AuditLogEvent
  property_count: 8
  slug: asana-auditlogevent
- name: AuditLogEventActor
  property_count: 4
  slug: asana-auditlogeventactor
- name: AuditLogEventContext
  property_count: 6
  slug: asana-auditlogeventcontext
- name: AuditLogEventDetails
  property_count: 3
  slug: asana-auditlogeventdetails
- name: AuditLogEventResource
  property_count: 5
  slug: asana-auditlogeventresource
- name: BatchRequest
  property_count: 1
  slug: asana-batchrequest
- name: BatchRequestAction
  property_count: 4
  slug: asana-batchrequestaction
- name: BatchResponse
  property_count: 3
  slug: asana-batchresponse
- name: CreateMembershipRequest
  property_count: 4
  slug: asana-createmembershiprequest
- name: CreateTimeTrackingEntryRequest
  property_count: 2
  slug: asana-createtimetrackingentryrequest
- name: CustomFieldBase
  property_count: 0
  slug: asana-customfieldbase
- name: CustomFieldCompact
  property_count: 5
  slug: asana-customfieldcompact
- name: CustomFieldRequest
  property_count: 6
  slug: asana-customfieldrequest
- name: CustomFieldResponse
  property_count: 10
  slug: asana-customfieldresponse
- name: CustomFieldSettingBase
  property_count: 0
  slug: asana-customfieldsettingbase
- name: CustomFieldSettingCompact
  property_count: 2
  slug: asana-customfieldsettingcompact
- name: CustomFieldSettingResponse
  property_count: 0
  slug: asana-customfieldsettingresponse
- name: DateVariableCompact
  property_count: 3
  slug: asana-datevariablecompact
- name: DateVariableRequest
  property_count: 2
  slug: asana-datevariablerequest
- name: DeprecatedPortfolioMembershipBase
  property_count: 0
  slug: asana-deprecatedportfoliomembershipbase
- name: DeprecatedPortfolioMembershipCompact
  property_count: 5
  slug: asana-deprecatedportfoliomembershipcompact
- name: DeprecatedPortfolioMembershipResponse
  property_count: 0
  slug: asana-deprecatedportfoliomembershipresponse
- name: EmptyResponse
  property_count: 0
  slug: asana-emptyresponse
- name: EnumOption
  property_count: 5
  slug: asana-enumoption
- name: EnumOptionBase
  property_count: 0
  slug: asana-enumoptionbase
- name: EnumOptionInsertRequest
  property_count: 3
  slug: asana-enumoptioninsertrequest
- name: EnumOptionRequest
  property_count: 5
  slug: asana-enumoptionrequest
- name: Error
  property_count: 3
  slug: asana-error
- name: ErrorResponse
  property_count: 1
  slug: asana-errorresponse
- name: EventResponse
  property_count: 7
  slug: asana-eventresponse
- name: GoalAddSubgoalRequest
  property_count: 3
  slug: asana-goaladdsubgoalrequest
- name: GoalAddSupportingRelationshipRequest
  property_count: 4
  slug: asana-goaladdsupportingrelationshiprequest
- name: GoalAddSupportingWorkRequest
  property_count: 1
  slug: asana-goaladdsupportingworkrequest
- name: GoalBase
  property_count: 9
  slug: asana-goalbase
- name: GoalCompact
  property_count: 4
  slug: asana-goalcompact
- name: GoalMembershipBase
  property_count: 8
  slug: asana-goalmembershipbase
- name: GoalMembershipCompact
  property_count: 0
  slug: asana-goalmembershipcompact
- name: GoalMembershipResponse
  property_count: 0
  slug: asana-goalmembershipresponse
- name: GoalMetricBase
  property_count: 12
  slug: asana-goalmetricbase
- name: GoalMetricCurrentValueRequest
  property_count: 3
  slug: asana-goalmetriccurrentvaluerequest
- name: GoalMetricRequest
  property_count: 0
  slug: asana-goalmetricrequest
- name: GoalRelationshipBase
  property_count: 0
  slug: asana-goalrelationshipbase
- name: GoalRelationshipCompact
  property_count: 5
  slug: asana-goalrelationshipcompact
- name: GoalRelationshipRequest
  property_count: 2
  slug: asana-goalrelationshiprequest
- name: GoalRelationshipResponse
  property_count: 6
  slug: asana-goalrelationshipresponse
- name: GoalRemoveSubgoalRequest
  property_count: 1
  slug: asana-goalremovesubgoalrequest
- name: GoalRemoveSupportingRelationshipRequest
  property_count: 1
  slug: asana-goalremovesupportingrelationshiprequest
- name: GoalRequest
  property_count: 11
  slug: asana-goalrequest
- name: GoalRequestBase
  property_count: 0
  slug: asana-goalrequestbase
- name: GoalResponse
  property_count: 16
  slug: asana-goalresponse
- name: GoalUpdateRequest
  property_count: 0
  slug: asana-goalupdaterequest
- name: JobBase
  property_count: 0
  slug: asana-jobbase
- name: JobCompact
  property_count: 7
  slug: asana-jobcompact
- name: JobResponse
  property_count: 7
  slug: asana-jobresponse
- name: Like
  property_count: 2
  slug: asana-like
- name: MemberCompact
  property_count: 3
  slug: asana-membercompact
- name: MembershipCompact
  property_count: 2
  slug: asana-membershipcompact
- name: MembershipRequest
  property_count: 1
  slug: asana-membershiprequest
- name: MembershipResponse
  property_count: 9
  slug: asana-membershipresponse
- name: MembershipUpdateRequest
  property_count: 2
  slug: asana-membershipupdaterequest
- name: ModifyDependenciesRequest
  property_count: 1
  slug: asana-modifydependenciesrequest
- name: ModifyDependentsRequest
  property_count: 1
  slug: asana-modifydependentsrequest
- name: NextPage
  property_count: 3
  slug: asana-nextpage
- name: OrganizationExportBase
  property_count: 0
  slug: asana-organizationexportbase
- name: OrganizationExportCompact
  property_count: 6
  slug: asana-organizationexportcompact
- name: OrganizationExportRequest
  property_count: 1
  slug: asana-organizationexportrequest
- name: OrganizationExportResponse
  property_count: 0
  slug: asana-organizationexportresponse
- name: PortfolioAddItemRequest
  property_count: 3
  slug: asana-portfolioadditemrequest
- name: PortfolioBase
  property_count: 0
  slug: asana-portfoliobase
- name: PortfolioCompact
  property_count: 3
  slug: asana-portfoliocompact
- name: PortfolioMembershipBase
  property_count: 0
  slug: asana-portfoliomembershipbase
- name: PortfolioMembershipCompact
  property_count: 5
  slug: asana-portfoliomembershipcompact
- name: PortfolioMembershipCompactResponse
  property_count: 0
  slug: asana-portfoliomembershipcompactresponse
- name: PortfolioMembershipResponse
  property_count: 0
  slug: asana-portfoliomembershipresponse
- name: PortfolioRemoveItemRequest
  property_count: 1
  slug: asana-portfolioremoveitemrequest
- name: PortfolioRequest
  property_count: 0
  slug: asana-portfoliorequest
- name: PortfolioResponse
  property_count: 0
  slug: asana-portfolioresponse
- name: Preview
  property_count: 8
  slug: asana-preview
- name: Asana Project
  property_count: 23
  slug: asana-project-json
- name: ProjectBase
  property_count: 0
  slug: asana-projectbase
- name: ProjectBriefBase
  property_count: 0
  slug: asana-projectbriefbase
- name: ProjectBriefCompact
  property_count: 2
  slug: asana-projectbriefcompact
- name: ProjectBriefRequest
  property_count: 0
  slug: asana-projectbriefrequest
- name: ProjectBriefResponse
  property_count: 0
  slug: asana-projectbriefresponse
- name: ProjectCompact
  property_count: 3
  slug: asana-projectcompact
- name: ProjectDuplicateRequest
  property_count: 4
  slug: asana-projectduplicaterequest
- name: ProjectMembershipBase
  property_count: 0
  slug: asana-projectmembershipbase
- name: ProjectMembershipCompact
  property_count: 5
  slug: asana-projectmembershipcompact
- name: ProjectMembershipCompactResponse
  property_count: 0
  slug: asana-projectmembershipcompactresponse
- name: ProjectMembershipNormalResponse
  property_count: 0
  slug: asana-projectmembershipnormalresponse
- name: ProjectRequest
  property_count: 0
  slug: asana-projectrequest
- name: ProjectResponse
  property_count: 0
  slug: asana-projectresponse
- name: ProjectSaveAsTemplateRequest
  property_count: 4
  slug: asana-projectsaveastemplaterequest
- name: ProjectSectionInsertRequest
  property_count: 3
  slug: asana-projectsectioninsertrequest
- name: ProjectStatusBase
  property_count: 0
  slug: asana-projectstatusbase
- name: ProjectStatusCompact
  property_count: 3
  slug: asana-projectstatuscompact
- name: ProjectStatusRequest
  property_count: 0
  slug: asana-projectstatusrequest
- name: ProjectStatusResponse
  property_count: 0
  slug: asana-projectstatusresponse
- name: ProjectTemplateBase
  property_count: 0
  slug: asana-projecttemplatebase
- name: ProjectTemplateCompact
  property_count: 3
  slug: asana-projecttemplatecompact
- name: ProjectTemplateInstantiateProjectRequest
  property_count: 7
  slug: asana-projecttemplateinstantiateprojectrequest
- name: ProjectTemplateResponse
  property_count: 0
  slug: asana-projecttemplateresponse
- name: ProjectUpdateRequest
  property_count: 0
  slug: asana-projectupdaterequest
- name: RemoveCustomFieldSettingRequest
  property_count: 1
  slug: asana-removecustomfieldsettingrequest
- name: RemoveFollowersRequest
  property_count: 1
  slug: asana-removefollowersrequest
- name: RemoveMembersRequest
  property_count: 1
  slug: asana-removemembersrequest
- name: RequestedRoleRequest
  property_count: 2
  slug: asana-requestedrolerequest
- name: RuleTriggerRequest
  property_count: 2
  slug: asana-ruletriggerrequest
- name: RuleTriggerResponse
  property_count: 1
  slug: asana-ruletriggerresponse
- name: SectionBase
  property_count: 0
  slug: asana-sectionbase
- name: SectionCompact
  property_count: 3
  slug: asana-sectioncompact
- name: SectionRequest
  property_count: 3
  slug: asana-sectionrequest
- name: SectionResponse
  property_count: 0
  slug: asana-sectionresponse
- name: SectionTaskInsertRequest
  property_count: 3
  slug: asana-sectiontaskinsertrequest
- name: StatusUpdateBase
  property_count: 0
  slug: asana-statusupdatebase
- name: StatusUpdateCompact
  property_count: 4
  slug: asana-statusupdatecompact
- name: StatusUpdateRequest
  property_count: 0
  slug: asana-statusupdaterequest
- name: StatusUpdateResponse
  property_count: 0
  slug: asana-statusupdateresponse
- name: StoryBase
  property_count: 8
  slug: asana-storybase
- name: StoryCompact
  property_count: 6
  slug: asana-storycompact
- name: StoryRequest
  property_count: 0
  slug: asana-storyrequest
- name: StoryResponse
  property_count: 0
  slug: asana-storyresponse
- name: StoryResponseDates
  property_count: 3
  slug: asana-storyresponsedates
- name: TagBase
  property_count: 0
  slug: asana-tagbase
- name: TagCompact
  property_count: 3
  slug: asana-tagcompact
- name: TagCreateTagForWorkspaceRequest
  property_count: 0
  slug: asana-tagcreatetagforworkspacerequest
- name: TagRequest
  property_count: 0
  slug: asana-tagrequest
- name: TagResponse
  property_count: 0
  slug: asana-tagresponse
- name: Asana Task
  property_count: 30
  slug: asana-task-json
- name: TaskAddFollowersRequest
  property_count: 1
  slug: asana-taskaddfollowersrequest
- name: TaskAddProjectRequest
  property_count: 4
  slug: asana-taskaddprojectrequest
- name: TaskAddTagRequest
  property_count: 1
  slug: asana-taskaddtagrequest
- name: TaskBase
  property_count: 0
  slug: asana-taskbase
- name: TaskCompact
  property_count: 5
  slug: asana-taskcompact
- name: TaskCountResponse
  property_count: 6
  slug: asana-taskcountresponse
- name: TaskDuplicateRequest
  property_count: 2
  slug: asana-taskduplicaterequest
- name: TaskRemoveFollowersRequest
  property_count: 1
  slug: asana-taskremovefollowersrequest
- name: TaskRemoveProjectRequest
  property_count: 1
  slug: asana-taskremoveprojectrequest
- name: TaskRemoveTagRequest
  property_count: 1
  slug: asana-taskremovetagrequest
- name: TaskRequest
  property_count: 0
  slug: asana-taskrequest
- name: TaskResponse
  property_count: 0
  slug: asana-taskresponse
- name: TaskSetParentRequest
  property_count: 3
  slug: asana-tasksetparentrequest
- name: TaskTemplateBase
  property_count: 0
  slug: asana-tasktemplatebase
- name: TaskTemplateCompact
  property_count: 3
  slug: asana-tasktemplatecompact
- name: TaskTemplateInstantiateTaskRequest
  property_count: 1
  slug: asana-tasktemplateinstantiatetaskrequest
- name: TaskTemplateRecipe
  property_count: 0
  slug: asana-tasktemplaterecipe
- name: TaskTemplateRecipeCompact
  property_count: 2
  slug: asana-tasktemplaterecipecompact
- name: TaskTemplateResponse
  property_count: 0
  slug: asana-tasktemplateresponse
- name: TeamAddUserRequest
  property_count: 1
  slug: asana-teamadduserrequest
- name: TeamBase
  property_count: 0
  slug: asana-teambase
- name: TeamCompact
  property_count: 3
  slug: asana-teamcompact
- name: TeamMembershipBase
  property_count: 0
  slug: asana-teammembershipbase
- name: TeamMembershipCompact
  property_count: 7
  slug: asana-teammembershipcompact
- name: TeamMembershipResponse
  property_count: 0
  slug: asana-teammembershipresponse
- name: TeamRemoveUserRequest
  property_count: 1
  slug: asana-teamremoveuserrequest
- name: TeamRequest
  property_count: 0
  slug: asana-teamrequest
- name: TeamResponse
  property_count: 0
  slug: asana-teamresponse
- name: TemplateRole
  property_count: 3
  slug: asana-templaterole
- name: TimePeriodBase
  property_count: 0
  slug: asana-timeperiodbase
- name: TimePeriodCompact
  property_count: 6
  slug: asana-timeperiodcompact
- name: TimePeriodResponse
  property_count: 0
  slug: asana-timeperiodresponse
- name: TimeTrackingEntryBase
  property_count: 0
  slug: asana-timetrackingentrybase
- name: TimeTrackingEntryCompact
  property_count: 5
  slug: asana-timetrackingentrycompact
- name: UpdateTimeTrackingEntryRequest
  property_count: 2
  slug: asana-updatetimetrackingentryrequest
- name: Asana User
  property_count: 6
  slug: asana-user-json
- name: UserBase
  property_count: 0
  slug: asana-userbase
- name: UserBaseResponse
  property_count: 0
  slug: asana-userbaseresponse
- name: UserCompact
  property_count: 3
  slug: asana-usercompact
- name: UserRequest
  property_count: 0
  slug: asana-userrequest
- name: UserResponse
  property_count: 0
  slug: asana-userresponse
- name: UserTaskListBase
  property_count: 0
  slug: asana-usertasklistbase
- name: UserTaskListCompact
  property_count: 5
  slug: asana-usertasklistcompact
- name: UserTaskListRequest
  property_count: 0
  slug: asana-usertasklistrequest
- name: UserTaskListResponse
  property_count: 0
  slug: asana-usertasklistresponse
- name: Asana Webhook Event
  property_count: 7
  slug: asana-webhook-event-json
- name: WebhookCompact
  property_count: 5
  slug: asana-webhookcompact
- name: WebhookFilter
  property_count: 4
  slug: asana-webhookfilter
- name: WebhookRequest
  property_count: 3
  slug: asana-webhookrequest
- name: WebhookResponse
  property_count: 0
  slug: asana-webhookresponse
- name: WebhookUpdateRequest
  property_count: 1
  slug: asana-webhookupdaterequest
- name: Asana Workspace
  property_count: 5
  slug: asana-workspace-json
- name: WorkspaceAddUserRequest
  property_count: 1
  slug: asana-workspaceadduserrequest
- name: WorkspaceBase
  property_count: 0
  slug: asana-workspacebase
- name: WorkspaceCompact
  property_count: 3
  slug: asana-workspacecompact
- name: WorkspaceMembershipBase
  property_count: 0
  slug: asana-workspacemembershipbase
- name: WorkspaceMembershipCompact
  property_count: 4
  slug: asana-workspacemembershipcompact
- name: WorkspaceMembershipRequest
  property_count: 0
  slug: asana-workspacemembershiprequest
- name: WorkspaceMembershipResponse
  property_count: 0
  slug: asana-workspacemembershipresponse
- name: WorkspaceRemoveUserRequest
  property_count: 1
  slug: asana-workspaceremoveuserrequest
- name: WorkspaceRequest
  property_count: 0
  slug: asana-workspacerequest
- name: WorkspaceResponse
  property_count: 0
  slug: asana-workspaceresponse
json_structures:
- name: Asana Structure
  property_count: 0
  slug: asana-structure
jsonld:
- class_count: 0
  name: Asana Context
  property_count: 16
  slug: asana-context
layout: provider
modified: '2026-09-16'
name: Asana
nav: Providers
network: true
overview: 'Asana publishes 44 APIs on the [APIs.io](https://apis.io/) network, including Allocations  API, Attachments  API, Custom Fields  API, and 41 more. Tagged areas include Collaboration, Productivity, Project Management, Project, and Task Management.


  The Asana catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 2 Spectral governance rulesets.


  Asana''s developer surface includes authentication, sandbox, getting-started guide, FAQ, documentation, code examples, changelog, and 76 more developer resources.'
plans:
- name: Asana Plans Pricing
  plan_count: 4
  slug: asana-plans-pricing
random_paper: 10
rate_limits:
- limit_count: 4
  name: Asana Rate Limits
  slug: asana-rate-limits
rules:
- effective_rule_count: 29
  extends:
  - spectral:asyncapi
  name: Asana API Rules
  rule_count: 2
  severity_counts:
    error: 0
    hint: 0
    info: 0
    warn: 2
  slug: asana-asyncapi-spectral-rules
- effective_rule_count: 6
  extends: []
  name: Asana API Rules
  rule_count: 6
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 5
  slug: asana-jsonschema-spectral-rules
scopes:
- name: Asana Scopes
  scope_count: 18
  slug: asana-scopes
  summary_line: 18 scopes · authorizationCode
score:
  band: exemplar
  composite: 70.2
  coverage:
    artifact_dirs: 25
    catalog_earned: 61.9
    catalog_earned_first_party: 0.0
    catalog_gap: 53.1
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.5
  facets:
    access_clarity: 68.4
    contract_governance: 13.6
    contract_quality: 79.3
    developer_ergonomics: 69.0
    discoverability: 71.7
    operational_transparency: 71.1
  previous_composite: 69.7
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 36
    mcp: first-party
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 45.1
  schema_version: 0.23.0
  scored_at: '2026-10-03'
  trend: flat
  upsert:
    applies: true
    score: 11.1
screenshot: https://raw.githubusercontent.com/api-evangelist/asana/refs/heads/main/screenshots/asana-2026-06-20T172555.png
security:
- kind: authentication
  name: Asana Authentication
  slug: asana-authentication
  summary_line: http/oauth2 · 2 schemes
- kind: domain-security
  name: Asana Domain Security
  slug: asana-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Asana Vulnerability Disclosure
  slug: asana-vulnerability-disclosure
  summary_line: Bugcrowd · security.txt · contact published
- kind: trust-center
  name: Asana Trust Center
  slug: asana-trust-center
  summary_line: SOC 2, ISO 27001, ISO 27017, ISO 27018, HIPAA, GDPR, CSA STAR
slug: asana
tags:
- Collaboration
- Productivity
- Project Management
- Project
- Task Management
- Task
- Workflows
website: https://asana.com
---
