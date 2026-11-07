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
  band: agent-native
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: true
    dynamic_client_registration: true
    error_semantics: documented
    event_surface_described: derived
    idempotency: documented
    mcp_server: verified
    mcp_tool_quality: na
    openapi_examples: partial
    operation_distinctiveness: false
    pagination_ratio: partial
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 57.4
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 112
  human_in_the_loop: 3
  name: Knock App Agentic Access
  operation_count: 181
  slug: knock-app-agentic-access
  summary_line: 181 operations · 112 acting · 3 human-in-the-loop
api_count: 2
apis:
- description: Outbound webhooks fire message lifecycle (sent, delivered, seen, read, interacted, archived, link_clicked, bounced, undelivered) and environment-change (workflow / email_layout / translation / partial
  name: Knock Outbound Webhooks
  slug: knock-webhooks
- baseURL: https://control.knock.app
  baseurl_source: spec
  description: Resources for managing your Knock account.
  name: Knock Accounts API
  phrasing_intents:
  - id: getWhoami
    intent: Check which scope my token belongs to
    question: Which account and scope is my Knock service token tied to?
  phrasing_ops: 1
  slug: knock-app-accounts-api
- baseURL: https://control.knock.app
  baseurl_source: spec
  description: The API keys API from Knock — 1 operation(s) for api keys.
  name: Knock API keys API
  phrasing_intents:
  - id: exchangeForApiKey
    intent: Exchange a service token for an API key
    question: How do I turn a Knock service token into a secret API key for one environment?
  phrasing_ops: 1
  slug: knock-app-api-keys-api
- baseURL: https://api.knock.app
  baseurl_source: spec
  description: The Audiences API from Knock — 4 operation(s) for audiences.
  name: Knock Audiences API
  phrasing_intents:
  - id: removeAudienceMembers
    intent: Remove members from an audience
    question: How do I take specific users out of an audience?
  - id: listAudienceMembers
    intent: List the members of an audience
    question: Who is currently in a given audience?
  - id: addAudienceMembers
    intent: Add members to an audience
    question: How do I add users to an existing audience?
  - id: archiveAudience
    intent: Archive an audience everywhere
    question: What happens to an audience when I archive it across all environments?
  - id: getAudience
    intent: Get an audience definition by key
    question: How do I look up a single audience's definition by its key?
  - id: upsertAudience
    intent: Create or update an audience
    question: How do I create a new audience or update one that already exists?
  - id: validateAudience
    intent: Validate an audience payload without saving
    question: Can I check an audience definition for errors before saving it?
  - id: listAudiences
    intent: List audiences in an environment
    question: Which audiences exist in my development environment?
  phrasing_ops: 8
  slug: knock-app-audiences-api
- baseURL: https://control.knock.app
  baseurl_source: spec
  description: Branches in Knock are a way to isolate changes to your Knock resources.
  name: Knock Branches API
  phrasing_intents:
  - id: listBranches
    intent: List branches
    question: Which branches exist, newest commit first?
  - id: deleteBranch
    intent: Delete a branch
    question: How do I delete a branch I'm finished with?
  - id: getBranch
    intent: Get a branch by slug
    question: How do I look up the details of one branch?
  - id: createBranch
    intent: Create a branch off development
    question: How do I create a new branch off the development environment?
  phrasing_ops: 4
  slug: knock-app-branches-api
- baseURL: https://control.knock.app
  baseurl_source: spec
  description: The Broadcasts API from Knock — 5 operation(s) for broadcasts.
  name: Knock Broadcasts API
  phrasing_intents:
  - id: sendBroadcast
    intent: Send or schedule a broadcast
    question: How do I send a broadcast right away?
  - id: validateBroadcast
    intent: Validate a broadcast without saving
    question: Can I check a broadcast payload for errors before saving it?
  - id: listBroadcasts
    intent: List broadcasts in an environment
    question: Which broadcasts have been created in this environment, newest first?
  - id: getBroadcast
    intent: Get a broadcast by key
    question: How do I see the details and status of one broadcast?
  - id: upsertBroadcast
    intent: Create or update a broadcast
    question: How do I create a broadcast or edit an existing draft?
  - id: cancelBroadcast
    intent: Cancel a scheduled broadcast
    question: How do I stop a broadcast that's scheduled but hasn't gone out yet?
  phrasing_ops: 6
  slug: knock-app-broadcasts-api
- baseURL: https://api.knock.app
  baseurl_source: spec
  description: The Bulk operations API from Knock — 12 operation(s) for bulk operations.
  name: Knock Bulk operations API
  phrasing_intents:
  - id: getBulkOperation
    intent: Check a bulk operation's progress
    question: How do I check whether a bulk job has finished?
  phrasing_ops: 1
  slug: knock-app-bulk-operations-api
- baseURL: https://api.knock.app
  baseurl_source: spec
  description: The Channel data API from Knock — 2 operation(s) for channel data.
  name: Knock Channel data API
  phrasing_intents:
  - id: unsetUserChannelData
    intent: Remove a user's channel data
    question: How do I delete a user's tokens for a channel when they log out?
  - id: getUserChannelData
    intent: Get a user's channel data
    question: How do I see a user's push tokens or chat connection for one channel?
  - id: setUserChannelData
    intent: Set a user's channel data
    question: How do I register a user's device push tokens on a channel?
  - id: unsetObjectChannelData
    intent: Remove an object's channel data
    question: How do I clear the channel data on an object?
  - id: getObjectChannelData
    intent: Get an object's channel data
    question: How do I see the channel data stored on an object, like a webhook URL for a project?
  - id: setObjectChannelData
    intent: Set an object's channel data
    question: How do I save a chat connection or webhook URL on an object?
  phrasing_ops: 6
  slug: knock-app-channel-data-api
- baseURL: https://control.knock.app
  baseurl_source: spec
  description: The Channel Groups API from Knock — 2 operation(s) for channel groups.
  name: Knock Channel Groups API
  phrasing_intents:
  - id: listChannelGroups
    intent: List channel groups
    question: Which channel groups exist across my account?
  - id: deleteChannelGroup
    intent: Archive a channel group
    question: How do I delete a channel group I no longer need?
  - id: getChannelGroup
    intent: Get a channel group by key
    question: How do I see which channels belong to a channel group?
  - id: upsertChannelGroup
    intent: Create or update a channel group
    question: How do I create a channel group that bundles several channels?
  phrasing_ops: 4
  slug: knock-app-channel-groups-api
- baseURL: https://control.knock.app
  baseurl_source: spec
  description: The Channels API from Knock — 2 operation(s) for channels.
  name: Knock Channels API
  phrasing_intents:
  - id: listChannels
    intent: List channels in my account
    question: Which delivery channels are configured in my Knock account?
  - id: getChannel
    intent: Get a channel and its settings
    question: How do I see a channel's per-environment provider settings?
  phrasing_ops: 2
  slug: knock-app-channels-api
- baseURL: https://control.knock.app
  baseurl_source: spec
  description: Commits are versioned changes to resources.
  name: Knock Commits API
  phrasing_intents:
  - id: getCommit
    intent: Get a commit by ID
    question: How do I inspect what a specific commit changed?
  - id: promoteOneCommit
    intent: Promote a single commit
    question: How do I promote just one change to the next environment?
  - id: promoteAllCommits
    intent: Promote all changes to an environment
    question: How do I promote every pending change into production?
  - id: listCommits
    intent: List commits in an environment
    question: Which commits haven't been promoted yet?
  - id: commitAllChanges
    intent: Commit all pending development changes
    question: How do I commit everything I've changed in development?
  phrasing_ops: 5
  slug: knock-app-commits-api
- baseURL: https://control.knock.app
  baseurl_source: spec
  description: Email layouts wrap your email templates and provide a consistent look and feel.
  name: Knock Email layouts API
  phrasing_intents:
  - id: listEmailLayouts
    intent: List email layouts
    question: Which email layouts are available in this environment?
  - id: getEmailLayout
    intent: Get an email layout by key
    question: How do I view the HTML and text of one email layout?
  - id: upsertEmailLayout
    intent: Create or update an email layout
    question: How do I create or edit an email layout in development?
  - id: validateEmailLayout
    intent: Validate an email layout without saving
    question: Can I check an email layout for errors before saving it?
  phrasing_ops: 4
  slug: knock-app-email-layouts-api
- baseURL: https://control.knock.app
  baseurl_source: spec
  description: Environments are isolated instances of your account that map to your infrastructure.
  name: Knock Environments API
  phrasing_intents:
  - id: getEnvironment
    intent: Get an environment by slug
    question: How do I look up the details of one environment?
  - id: listEnvironments
    intent: List environments
    question: Which environments does my Knock account have?
  phrasing_ops: 2
  slug: knock-app-environments-api
- baseURL: https://api.knock.app
  baseurl_source: spec
  description: The Feeds API from Knock — 2 operation(s) for feeds.
  name: Knock Feeds API
  phrasing_intents:
  - id: getUserInAppFeedSettings
    intent: Get a user's feed settings
    question: What feed settings apply to a user's in-app feed?
  - id: listUserInAppFeedItems
    intent: List a user's in-app feed items
    question: How do I load a user's in-app notification feed?
  phrasing_ops: 2
  slug: knock-app-feeds-api
- baseURL: https://api.knock.app
  baseurl_source: spec
  description: Guides let you define in-app guides that can be displayed to users based on priority and other conditions.
  name: Knock Guides API
  phrasing_intents:
  - id: markUserGuideAsInteracted(2)
    intent: Record a guide interaction (no message ID)
    question: How do I log a user clicking inside a guide when I lack a guide message ID?
  - id: markUserGuideAsUnarchived
    intent: Restore a dismissed guide
    question: How do I bring back a guide a user previously dismissed?
  - id: markUserGuideAsArchived(2)
    intent: Record a guide as dismissed (no message ID)
    question: How do I archive a guide for a user when I have no guide message ID?
  - id: listUserGuides
    intent: List guides a user is eligible for
    question: Which in-app guides should a particular user see right now?
  - id: resetUserGuideEngagement
    intent: Reset a user's engagement with a guide
    question: How do I reset a guide so a user's next interaction starts fresh?
  - id: markUserGuideAsArchived
    intent: Archive an existing guide message
    question: How do I archive a specific guide message a user dismissed?
  - id: markUserGuideAsSeen(2)
    intent: Record a guide as seen (no message ID)
    question: How do I record that a user saw a guide step when I don't have a guide message ID?
  - id: markUserGuideAsSeen
    intent: Record an existing guide message as seen
    question: How do I mark a specific guide message as seen for a user?
  phrasing_ops: 15
  slug: knock-app-guides-api
- baseURL: https://api.knock.app
  baseurl_source: spec
  description: The Integrations API from Knock — 2 operation(s) for integrations.
  name: Knock Integrations API
  phrasing_intents:
  - id: processCensusRpcRequest
    intent: Handle a Census custom destination request
    question: How do I sync data from Census into Knock through the custom destination?
  - id: processHightouchRpcRequest
    intent: Handle a Hightouch embedded destination request
    question: How do I push Hightouch syncs into Knock through the embedded destination?
  phrasing_ops: 2
  slug: knock-app-integrations-api
- baseURL: https://control.knock.app
  baseurl_source: spec
  description: The Members API from Knock — 2 operation(s) for members.
  name: Knock Members API
  phrasing_intents:
  - id: removeMember
    intent: Remove a member from the account
    question: How do I remove someone's access to our account?
  - id: getMember
    intent: Get an account member
    question: How do I look up one teammate on my Knock account?
  - id: listMembers
    intent: List account members
    question: Who has access to our account?
  phrasing_ops: 3
  slug: knock-app-members-api
- baseURL: https://control.knock.app
  baseurl_source: spec
  description: A message type allows you to specify an in-app schema that defines the fields available for your in-app notifications.
  name: Knock Message types API
  phrasing_intents:
  - id: validateMessageType
    intent: Validate a message type without saving
    question: Can I check a message type payload for errors before saving it?
  - id: getMessageType
    intent: Get a message type by key
    question: How do I see one message type's schema and variants?
  - id: upsertMessageType
    intent: Create or update a message type
    question: How do I create a custom in-app message type?
  - id: listMessageTypes
    intent: List message types
    question: Which message types are defined in this environment?
  phrasing_ops: 4
  slug: knock-app-message-types-api
- baseURL: https://api.knock.app
  baseurl_source: spec
  description: The Messages API from Knock — 24 operation(s) for messages.
  name: Knock Messages API
  phrasing_intents:
  - id: listMessages
    intent: List messages across the environment
    question: Which notifications were sent across the whole environment recently?
  - id: markMessageInteracted
    intent: Record an interaction on a message
    question: How do I record that a user clicked a button in a notification?
  - id: listMessageEvents
    intent: List a message's events
    question: What status events has a message gone through?
  - id: listMessagesForUser
    intent: List messages sent to a user
    question: What notifications has a particular user received?
  - id: getMessageContents
    intent: Get a message's rendered content
    question: What exactly did a sent message say, as rendered for its channel?
  - id: listMessageActivities
    intent: List a message's activities
    question: Which batched activities make up a message?
  - id: listMessagesForObject
    intent: List messages sent to an object
    question: Which notifications were sent to an object like a project or team?
  - id: batchMarkMessagesAsArchived
    intent: Archive several messages
    question: How do I archive a batch of notifications in one request?
  phrasing_ops: 27
  slug: knock-app-messages-api
- baseURL: https://api.knock.app
  baseurl_source: spec
  description: The Objects API from Knock — 19 operation(s) for objects.
  name: Knock Objects API
  phrasing_intents:
  - id: deleteObject
    intent: Delete an object permanently
    question: How do I permanently remove an object from a collection?
  - id: getObject
    intent: Get an object
    question: How do I look up an object and its properties?
  - id: setObject
    intent: Create or update an object
    question: How do I create an object, like a project or team, to notify?
  - id: updateObjectPreferenceCategories
    intent: Update all category settings in an object's preferences
    question: How do I replace every category preference on an object at once?
  - id: bulkDeleteObjects
    intent: Delete many objects in a collection
    question: How do I delete a list of objects from one collection at once?
  - id: updateObjectPreferenceCategory
    intent: Update one category in an object's preferences (deprecated)
    question: Can I still change a single category preference on an object with the deprecated endpoint?
  - id: listObjectPreferenceSets
    intent: List an object's preference sets
    question: Which preference sets does an object have?
  - id: updateObjectPreferenceWorkflows
    intent: Update all workflow settings in an object's preferences
    question: How do I replace the workflow opt-ins for an object's preference set?
  phrasing_ops: 19
  slug: knock-app-objects-api
- baseURL: https://control.knock.app
  baseurl_source: spec
  description: Partials allow you to reuse content across templates.
  name: Knock Partials API
  phrasing_intents:
  - id: listPartials
    intent: List template partials
    question: Which reusable partials are available in this environment?
  - id: getPartial
    intent: Get a template partial by key
    question: How do I see the content of one reusable partial?
  - id: upsertPartial
    intent: Create or update a template partial
    question: How do I create a reusable template block for my notifications?
  - id: validatePartial
    intent: Validate a partial without saving
    question: Can I check a partial for errors before saving it?
  phrasing_ops: 4
  slug: knock-app-partials-api
- baseURL: https://api.knock.app
  baseurl_source: spec
  description: The Providers API from Knock — 7 operation(s) for providers.
  name: Knock Providers API
  phrasing_intents:
  - id: listChannelsForMsTeamsProvider
    intent: List channels in a Microsoft Teams team
    question: How do I list the channels inside a customer's Microsoft Teams team?
  - id: slackProviderRevokeAccess
    intent: Revoke Slack access
    question: How do I disconnect a customer's Slack workspace?
  - id: msTeamsProviderAuthCheck
    intent: Check a Microsoft Teams connection
    question: How do I verify that a customer has authorized Microsoft Teams?
  - id: msTeamsProviderRevokeAccess
    intent: Revoke Microsoft Teams access
    question: How do I disconnect a customer's Microsoft Teams tenant?
  - id: listTeamsForMsTeamsProvider
    intent: List Microsoft Teams teams in a tenant
    question: How do I list the teams in a customer's Microsoft Entra tenant?
  - id: slackProviderAuthCheck
    intent: Check a Slack connection
    question: How do I confirm a Slack workspace connection is still authenticated?
  - id: listChannelsForSlackProvider
    intent: List Slack channels in a workspace
    question: How do I let a customer pick which Slack channel to send notifications to?
  phrasing_ops: 7
  slug: knock-app-providers-api
- baseURL: https://api.knock.app
  baseurl_source: spec
  description: The Schedules API from Knock — 3 operation(s) for schedules.
  name: Knock Schedules API
  phrasing_intents:
  - id: listUserSchedules
    intent: List a user's schedules
    question: What scheduled notifications does a particular user have?
  - id: deleteSchedules
    intent: Delete schedules
    question: How do I stop and remove schedules permanently?
  - id: listSchedules
    intent: List schedules for a workflow
    question: Which schedules exist for a given workflow?
  - id: createSchedules
    intent: Schedule a workflow for recipients
    question: How do I schedule a recurring digest for a set of users?
  - id: updateSchedules
    intent: Update existing schedules
    question: How do I change the timing of schedules I already created?
  - id: listObjectSchedules
    intent: List an object's schedules
    question: Which recurring notifications are scheduled for an object?
  phrasing_ops: 6
  slug: knock-app-schedules-api
- baseURL: https://api.knock.app
  baseurl_source: spec
  description: The Subscriptions API from Knock — 4 operation(s) for subscriptions.
  name: Knock Subscriptions API
  phrasing_intents:
  - id: listSubscriptionsForUser
    intent: List a user's subscriptions
    question: Which objects is a particular user subscribed to?
  - id: deleteSubscriptionsForObject
    intent: Unsubscribe recipients from an object
    question: How do I unsubscribe users from an object?
  - id: listSubscriptionsForObject
    intent: List an object's subscriptions
    question: Who is subscribed to a given object, like a project or channel?
  - id: addSubscriptionsForObject
    intent: Subscribe recipients to an object
    question: How do I subscribe users to an object so they get its notifications?
  phrasing_ops: 4
  slug: knock-app-subscriptions-api
- baseURL: https://control.knock.app
  baseurl_source: spec
  description: The Templates API from Knock — 1 operation(s) for templates.
  name: Knock Templates API
  phrasing_intents:
  - id: previewTemplate
    intent: Preview a template without saving it
    question: How do I render a notification template for a sample recipient without building a workflow?
  phrasing_ops: 1
  slug: knock-app-templates-api
- baseURL: https://api.knock.app
  baseurl_source: spec
  description: The Tenants API from Knock — 4 operation(s) for tenants.
  name: Knock Tenants API
  phrasing_intents:
  - id: listTenants
    intent: List tenants
    question: Which tenants exist in this environment?
  - id: bulkSetTenants
    intent: Create or update many tenants at once
    question: How do I sync a large batch of tenants in one call?
  - id: bulkDeleteTenants
    intent: Delete many tenants at once
    question: How do I delete up to 1,000 tenants in a single request?
  - id: deleteTenant
    intent: Delete a tenant and its data
    question: How do I delete a tenant and everything associated with it?
  - id: getTenant
    intent: Get a tenant
    question: How do I look up a tenant's name and settings?
  - id: setTenant
    intent: Create or update a tenant
    question: How do I create a tenant for one of my customer organizations?
  phrasing_ops: 6
  slug: knock-app-tenants-api
- baseURL: https://control.knock.app
  baseurl_source: spec
  description: Translations are per-locale string files that can be used in your templates.
  name: Knock Translations API
  phrasing_intents:
  - id: listTranslations
    intent: List translations
    question: Which locales have translations in this environment?
  - id: validateTranslation
    intent: Validate a translation without saving
    question: Can I check a translation file for errors before saving it?
  - id: getTranslation
    intent: Get a translation for a locale
    question: How do I fetch the strings for one locale?
  - id: upsertTranslation
    intent: Create or update a translation
    question: How do I add or update French strings for my notifications?
  phrasing_ops: 4
  slug: knock-app-translations-api
- baseURL: https://api.knock.app
  baseurl_source: spec
  description: The Users API from Knock — 28 operation(s) for users.
  name: Knock Users API
  phrasing_intents:
  - id: updateUserPreferenceChannelTypes
    intent: Update a user's channel type preferences (deprecated)
    question: How do I set every channel type preference for a user at once?
  - id: updateUserPreferenceChannelType
    intent: Update one channel type in a user's preferences (deprecated)
    question: How do I turn off only SMS for a user?
  - id: updateUserPreferenceWorkflows
    intent: Update a user's workflow preferences (deprecated)
    question: How do I replace every workflow opt-in in a user's preference set with the deprecated endpoint?
  - id: updateUserPreferenceCategory
    intent: Update one category in a user's preferences (deprecated)
    question: Can I still change a single category preference for a user through the deprecated endpoint?
  - id: mergeUser
    intent: Merge two users into one
    question: How do I combine a duplicate user record into the main one?
  - id: updateUserPreferenceCategories
    intent: Update a user's category preferences (deprecated)
    question: How do I replace a user's category preferences all at once?
  - id: listUsers
    intent: List users
    question: Which users exist in this environment?
  - id: bulkDeleteUsers
    intent: Delete many users at once
    question: How do I permanently delete a batch of users?
  phrasing_ops: 18
  slug: knock-app-users-api
- baseURL: https://control.knock.app
  baseurl_source: spec
  description: The Variables API from Knock — 2 operation(s) for variables.
  name: Knock Variables API
  phrasing_intents:
  - id: getVariable
    intent: Get a variable
    question: How do I see a variable's value in each environment?
  - id: listVariables
    intent: List variables
    question: Which variables are defined for my environment?
  phrasing_ops: 2
  slug: knock-app-variables-api
- baseURL: https://api.knock.app
  baseurl_source: spec
  description: The Workflow recipient runs API from Knock — 2 operation(s) for workflow recipient runs.
  name: Knock Workflow recipient runs API
  phrasing_intents:
  - id: getWorkflowRecipientRun
    intent: Get a workflow run for one recipient
    question: How do I debug what happened when a workflow ran for one recipient?
  - id: listWorkflowRecipientRuns
    intent: List workflow recipient runs
    question: Which workflow runs errored for recipients recently?
  phrasing_ops: 2
  slug: knock-app-workflow-recipient-runs-api
- baseURL: https://api.knock.app
  baseurl_source: spec
  description: The Workflow Triggers API from Knock — 2 operation(s) for workflow triggers.
  name: Knock Workflow Triggers API
  phrasing_intents:
  - id: triggerWorkflow(2)
    intent: Trigger a workflow via notify
    question: How do I send a notification through the notify endpoint?
  - id: cancelWorkflow
    intent: Cancel a triggered workflow via notify
    question: How do I cancel a notification I triggered through the notify endpoint?
  phrasing_ops: 2
  slug: knock-app-workflow-triggers-api
- baseURL: https://api.knock.app
  baseurl_source: spec
  description: Workflows let you express your cross-channel notification logic.
  name: Knock Workflows API
  phrasing_intents:
  - id: cancelWorkflow(2)
    intent: Cancel queued runs of a workflow
    question: How do I cancel a delayed notification before it sends?
  - id: triggerWorkflow
    intent: Trigger a workflow by key
    question: How do I send a notification by triggering a workflow for some users?
  - id: validateWorkflow
    intent: Validate a workflow without saving
    question: Can I check a workflow definition for errors before saving it?
  - id: runWorkflow
    intent: Run a committed workflow in an environment
    question: How do I run the latest committed version of a workflow in a chosen environment?
  - id: previewWorkflowTemplate
    intent: Preview a workflow step's template
    question: How do I see what a workflow step's message will look like for a recipient?
  - id: listWorkflows
    intent: List workflows
    question: Which workflows are defined in this environment?
  - id: activateWorkflow
    intent: Activate or deactivate a workflow
    question: How do I turn a workflow off in production?
  - id: getWorkflow
    intent: Get a workflow by key
    question: How do I see a workflow's steps and settings?
  phrasing_ops: 9
  slug: knock-app-workflows-api
arazzos:
- description: Bulk identify a batch of users, wait for the operation to complete, then notify them.
  name: Knock Bulk Identify Users and Notify
  slug: knock-app-bulk-identify-users-notify-workflow
- description: Bulk upsert objects in a collection, wait for completion, then notify one object.
  name: Knock Bulk Set Objects and Notify
  slug: knock-app-bulk-set-objects-notify-workflow
- description: Bulk upsert tenants, wait for the operation to complete, then list tenants to verify.
  name: Knock Bulk Set Tenants and Verify
  slug: knock-app-bulk-set-tenants-verify-workflow
- description: Identify a recipient, trigger a cancellable workflow, then cancel it by key.
  name: Knock Cancellable Workflow Trigger
  slug: knock-app-cancellable-workflow-trigger-workflow
- description: Identify a recipient, apply their notification preferences, then trigger a workflow for them.
  name: Knock Identify User, Set Preferences, and Trigger Workflow
  slug: knock-app-identify-user-set-preferences-trigger-workflow
- description: Identify a surviving user, merge a duplicate into it, then notify the merged user.
  name: Knock Merge Users and Re-notify
  slug: knock-app-merge-users-and-renotify-workflow
- description: Upsert an object, set its preference set, then audit messages sent to it.
  name: Knock Set Object Preferences and Audit Messages
  slug: knock-app-object-preferences-message-audit-workflow
- description: Create an object, subscribe recipients to it, then notify subscribers via a workflow.
  name: Knock Set Object, Add Subscriptions, and Notify
  slug: knock-app-object-subscriptions-notify-workflow
- description: Identify a user, register their channel data, then read their in-app feed.
  name: Knock Register Push Token and Read Feed
  slug: knock-app-register-push-token-and-read-feed-workflow
- description: Identify a recipient, create a recurring schedule, then verify it was registered.
  name: Knock Schedule a Recurring Workflow
  slug: knock-app-schedule-recurring-workflow-workflow
- description: Set a tenant, identify a member user, then notify them scoped to the tenant.
  name: Knock Tenant Onboarding and Notify
  slug: knock-app-tenant-onboarding-notify-workflow
- description: Trigger a workflow, find the resulting in-app message, then archive it.
  name: Knock Trigger Then Archive Feed Message
  slug: knock-app-trigger-then-archive-feed-message-workflow
- description: Trigger a workflow then locate the generated message and read its rendered content.
  name: Knock Trigger Workflow and Inspect Message Content
  slug: knock-app-trigger-workflow-inspect-message-content-workflow
- description: Trigger a workflow and poll its per-recipient run until it completes.
  name: Knock Trigger Workflow and Track Recipient Run
  slug: knock-app-trigger-workflow-track-recipient-run-workflow
artifact_total: 155
asyncapis:
- description: Knock fires outbound webhook events for message lifecycle (sent, delivered, seen, read, interacted, archived, link_clicked, bounced, undelivered) and for environment changes (workflow / email_layout /
  name: Knock Outbound Webhooks
  slug: knock-webhooks-asyncapi
collections:
- collection_type: postman
  name: Knock Audiences API
  slug: postman-knock-audiences-api
- collection_type: postman
  name: Knock Bulk Operations API
  slug: postman-knock-bulk-operations-api
- collection_type: postman
  name: Knock Channels API
  slug: postman-knock-channels-api
- collection_type: postman
  name: Knock Integrations API
  slug: postman-knock-integrations-api
- collection_type: postman
  name: Knock Management API (mAPI)
  slug: postman-knock-management-api
- collection_type: postman
  name: Knock Messages API
  slug: postman-knock-messages-api
- collection_type: postman
  name: Knock Notify API
  slug: postman-knock-notify-api
- collection_type: postman
  name: Knock Objects API
  slug: postman-knock-objects-api
- collection_type: postman
  name: Knock Providers API
  slug: postman-knock-providers-api
- collection_type: postman
  name: Knock Schedules API
  slug: postman-knock-schedules-api
- collection_type: postman
  name: Knock Tenants API
  slug: postman-knock-tenants-api
- collection_type: postman
  name: Knock Users API
  slug: postman-knock-users-api
- collection_type: postman
  name: Knock Workflows API
  slug: postman-knock-workflows-api
- collection_type: open
  name: Knock Audiences Accounts API
  slug: open-knock-app-accounts-api
- collection_type: open
  name: Knock Audiences Accounts API keys API
  slug: open-knock-app-api-keys-api
- collection_type: open
  name: Knock Accounts Audiences API
  slug: open-knock-app-audiences-api
- collection_type: open
  name: Knock Audiences Accounts Branches API
  slug: open-knock-app-branches-api
- collection_type: open
  name: Knock Audiences Accounts Broadcasts API
  slug: open-knock-app-broadcasts-api
- collection_type: open
  name: Knock Audiences Accounts Bulk operations API
  slug: open-knock-app-bulk-operations-api
- collection_type: open
  name: Knock Audiences Accounts Channel data API
  slug: open-knock-app-channel-data-api
- collection_type: open
  name: Knock Audiences Accounts Channel Groups API
  slug: open-knock-app-channel-groups-api
- collection_type: open
  name: Knock Audiences Accounts Channels API
  slug: open-knock-app-channels-api
- collection_type: open
  name: Knock Audiences Accounts Commits API
  slug: open-knock-app-commits-api
- collection_type: open
  name: Knock Audiences Accounts Email layouts API
  slug: open-knock-app-email-layouts-api
- collection_type: open
  name: Knock Audiences Accounts Environments API
  slug: open-knock-app-environments-api
- collection_type: open
  name: Knock Audiences Accounts Feeds API
  slug: open-knock-app-feeds-api
- collection_type: open
  name: Knock Audiences Accounts Guides API
  slug: open-knock-app-guides-api
- collection_type: open
  name: Knock Audiences Accounts Integrations API
  slug: open-knock-app-integrations-api
- collection_type: open
  name: Knock Audiences Accounts Members API
  slug: open-knock-app-members-api
- collection_type: open
  name: Knock Audiences Accounts Message types API
  slug: open-knock-app-message-types-api
- collection_type: open
  name: Knock Audiences Accounts Messages API
  slug: open-knock-app-messages-api
- collection_type: open
  name: Knock Audiences Accounts Microsoft Teams API
  slug: open-knock-app-microsoft-teams-api
- collection_type: open
  name: Knock Audiences Accounts Objects API
  slug: open-knock-app-objects-api
- collection_type: open
  name: Knock Audiences Accounts Partials API
  slug: open-knock-app-partials-api
- collection_type: open
  name: Knock Audiences Accounts Preferences API
  slug: open-knock-app-preferences-api
- collection_type: open
  name: Knock Audiences Accounts Providers API
  slug: open-knock-app-providers-api
- collection_type: open
  name: Knock Audiences Accounts Schedules API
  slug: open-knock-app-schedules-api
- collection_type: open
  name: Knock Audiences Accounts Slack API
  slug: open-knock-app-slack-api
- collection_type: open
  name: Knock Audiences Accounts Subscriptions API
  slug: open-knock-app-subscriptions-api
- collection_type: open
  name: Knock Audiences Accounts Templates API
  slug: open-knock-app-templates-api
- collection_type: open
  name: Knock Audiences Accounts Tenants API
  slug: open-knock-app-tenants-api
- collection_type: open
  name: Knock Audiences Accounts Translations API
  slug: open-knock-app-translations-api
- collection_type: open
  name: Knock Audiences Accounts Users API
  slug: open-knock-app-users-api
- collection_type: open
  name: Knock Audiences Accounts Variables API
  slug: open-knock-app-variables-api
- collection_type: open
  name: Knock Audiences Accounts Workflow recipient runs API
  slug: open-knock-app-workflow-recipient-runs-api
- collection_type: open
  name: Knock Audiences Accounts Workflow Triggers API
  slug: open-knock-app-workflow-triggers-api
- collection_type: open
  name: Knock Audiences Accounts Workflows API
  slug: open-knock-app-workflows-api
- collection_type: open
  name: Knock Audiences API
  slug: open-knock-audiences-api
- collection_type: open
  name: Knock Bulk Operations API
  slug: open-knock-bulk-operations-api
- collection_type: open
  name: Knock Channels API
  slug: open-knock-channels-api
- collection_type: open
  name: Knock Integrations API
  slug: open-knock-integrations-api
- collection_type: open
  name: Knock Management API (mAPI)
  slug: open-knock-management-api
- collection_type: open
  name: Knock Messages API
  slug: open-knock-messages-api
- collection_type: open
  name: Knock Notify API
  slug: open-knock-notify-api
- collection_type: open
  name: Knock Objects API
  slug: open-knock-objects-api
- collection_type: open
  name: Knock Providers API
  slug: open-knock-providers-api
- collection_type: open
  name: Knock Schedules API
  slug: open-knock-schedules-api
- collection_type: open
  name: Knock Tenants API
  slug: open-knock-tenants-api
- collection_type: open
  name: Knock Users API
  slug: open-knock-users-api
- collection_type: open
  name: Knock Workflows API
  slug: open-knock-workflows-api
common:
- group: other
  href: https://artifacts.apis.io/knock-app/capabilities/knock-app-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/knock-app-capability-edges.yml
- group: company
  title: ''
  type: Website
  url: https://www.knock.app/
- group: agent
  href: https://artifacts.apis.io/knock-app/agentic-access/knock-app-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/knock-app-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/knock-app/security/knock-app-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/knock-app-domain-security.yml
- group: auth
  href: https://artifacts.apis.io/knock-app/authentication/knock-app-authentication.yml
  title: ''
  type: Authentication
  url: authentication/knock-app-authentication.yml
- group: build
  href: https://artifacts.apis.io/knock-app/packages/knock-app-packages.yml
  title: ''
  type: Packages
  url: packages/knock-app-packages.yml
- group: agent
  href: https://artifacts.apis.io/knock-app/well-known/knock-app-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/knock-app-well-known.yml
- group: agent
  href: https://artifacts.apis.io/knock-app/mcp/knock-app-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/knock-app-mcp.yml
- group: agent
  href: https://artifacts.apis.io/knock-app/llms/knock-app-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/knock-app-llms.txt
- group: design
  href: https://artifacts.apis.io/knock-app/conformance/knock-app-conformance.yml
  title: ''
  type: Conformance
  url: conformance/knock-app-conformance.yml
- group: design
  href: https://artifacts.apis.io/knock-app/errors/knock-app-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/knock-app-problem-types.yml
- group: design
  href: https://artifacts.apis.io/knock-app/lifecycle/knock-app-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/knock-app-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/knock-app/conventions/knock-app-conventions.yml
  title: ''
  type: Conventions
  url: conventions/knock-app-conventions.yml
- group: start
  href: https://artifacts.apis.io/knock-app/sandbox/knock-app-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/knock-app-sandbox.yml
- group: build
  href: https://artifacts.apis.io/knock-app/cli/knock-app-cli.yml
  title: ''
  type: CLI
  url: cli/knock-app-cli.yml
- group: design
  href: https://artifacts.apis.io/knock-app/components/knock-app-components.yml
  title: ''
  type: Components
  url: components/knock-app-components.yml
- group: design
  href: https://artifacts.apis.io/knock-app/data-model/knock-app-data-model.yml
  title: ''
  type: DataModel
  url: data-model/knock-app-data-model.yml
- group: other
  href: https://artifacts.apis.io/knock-app/overlays/knock-app-audiences-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/knock-app-audiences-overlay.yaml
- group: other
  href: https://artifacts.apis.io/knock-app/overlays/knock-app-bulk-operations-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/knock-app-bulk-operations-overlay.yaml
- group: other
  href: https://artifacts.apis.io/knock-app/overlays/knock-app-channels-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/knock-app-channels-overlay.yaml
- group: other
  href: https://artifacts.apis.io/knock-app/overlays/knock-app-integrations-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/knock-app-integrations-overlay.yaml
- group: other
  href: https://artifacts.apis.io/knock-app/overlays/knock-app-management-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/knock-app-management-overlay.yaml
- group: other
  href: https://artifacts.apis.io/knock-app/overlays/knock-app-messages-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/knock-app-messages-overlay.yaml
- group: other
  href: https://artifacts.apis.io/knock-app/overlays/knock-app-notify-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/knock-app-notify-overlay.yaml
- group: other
  href: https://artifacts.apis.io/knock-app/overlays/knock-app-objects-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/knock-app-objects-overlay.yaml
- group: other
  href: https://artifacts.apis.io/knock-app/overlays/knock-app-providers-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/knock-app-providers-overlay.yaml
- group: other
  href: https://artifacts.apis.io/knock-app/overlays/knock-app-schedules-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/knock-app-schedules-overlay.yaml
- group: other
  href: https://artifacts.apis.io/knock-app/overlays/knock-app-tenants-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/knock-app-tenants-overlay.yaml
- group: other
  href: https://artifacts.apis.io/knock-app/overlays/knock-app-users-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/knock-app-users-overlay.yaml
- group: other
  href: https://artifacts.apis.io/knock-app/overlays/knock-app-workflows-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/knock-app-workflows-overlay.yaml
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/knock/overview
- group: design
  href: https://artifacts.apis.io/knock-app/arazzo/knock-app-bulk-identify-users-notify-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/knock-app-bulk-identify-users-notify-workflow.yml
- group: design
  href: https://artifacts.apis.io/knock-app/arazzo/knock-app-bulk-set-objects-notify-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/knock-app-bulk-set-objects-notify-workflow.yml
- group: design
  href: https://artifacts.apis.io/knock-app/arazzo/knock-app-bulk-set-tenants-verify-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/knock-app-bulk-set-tenants-verify-workflow.yml
- group: design
  href: https://artifacts.apis.io/knock-app/arazzo/knock-app-cancellable-workflow-trigger-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/knock-app-cancellable-workflow-trigger-workflow.yml
- group: design
  href: https://artifacts.apis.io/knock-app/arazzo/knock-app-identify-user-set-preferences-trigger-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/knock-app-identify-user-set-preferences-trigger-workflow.yml
- group: design
  href: https://artifacts.apis.io/knock-app/arazzo/knock-app-merge-users-and-renotify-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/knock-app-merge-users-and-renotify-workflow.yml
- group: design
  href: https://artifacts.apis.io/knock-app/arazzo/knock-app-object-preferences-message-audit-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/knock-app-object-preferences-message-audit-workflow.yml
- group: design
  href: https://artifacts.apis.io/knock-app/arazzo/knock-app-object-subscriptions-notify-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/knock-app-object-subscriptions-notify-workflow.yml
- group: design
  href: https://artifacts.apis.io/knock-app/arazzo/knock-app-register-push-token-and-read-feed-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/knock-app-register-push-token-and-read-feed-workflow.yml
- group: design
  href: https://artifacts.apis.io/knock-app/arazzo/knock-app-schedule-recurring-workflow-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/knock-app-schedule-recurring-workflow-workflow.yml
- group: design
  href: https://artifacts.apis.io/knock-app/arazzo/knock-app-tenant-onboarding-notify-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/knock-app-tenant-onboarding-notify-workflow.yml
- group: design
  href: https://artifacts.apis.io/knock-app/arazzo/knock-app-trigger-then-archive-feed-message-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/knock-app-trigger-then-archive-feed-message-workflow.yml
- group: design
  href: https://artifacts.apis.io/knock-app/arazzo/knock-app-trigger-workflow-inspect-message-content-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/knock-app-trigger-workflow-inspect-message-content-workflow.yml
- group: design
  href: https://artifacts.apis.io/knock-app/arazzo/knock-app-trigger-workflow-track-recipient-run-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/knock-app-trigger-workflow-track-recipient-run-workflow.yml
- group: start
  title: ''
  type: Portal
  url: https://knock.app
- group: docs
  title: ''
  type: Documentation
  url: https://docs.knock.app/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.knock.app/api-reference/overview
- group: docs
  title: ''
  type: Documentation
  url: https://docs.knock.app/mapi
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.knock.app/getting-started/what-is-knock
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.knock.app/getting-started/quick-start/general
- group: start
  title: ''
  type: Signup
  url: https://dashboard.knock.app/signup
- group: auth
  title: ''
  type: Authentication
  url: https://docs.knock.app/api-reference/overview/authentication
- group: operate
  title: ''
  type: RateLimits
  url: https://docs.knock.app/api-reference/overview/rate-limits
- group: operate
  title: ''
  type: RateLimits
  url: https://docs.knock.app/api-reference/overview/batch-rate-limits
- group: design
  title: ''
  type: Idempotency
  url: https://docs.knock.app/api-reference/overview/idempotent-requests
- group: design
  title: ''
  type: Pagination
  url: https://docs.knock.app/api-reference/overview/pagination
- group: design
  title: ''
  type: ErrorCodes
  url: https://docs.knock.app/api-reference/overview/errors
- group: design
  title: ''
  type: ErrorCodes
  url: https://docs.knock.app/api-reference/overview/error-codes
- group: operate
  title: ''
  type: StatusPage
  url: https://status.knock.app
- group: operate
  title: ''
  type: ChangeLog
  url: https://knock.app/changelog
- group: operate
  href: https://artifacts.apis.io/knock-app/changelog/knock-app-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/knock-app-changelog.yml
- group: commercial
  title: ''
  type: Pricing
  url: https://knock.app/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://knock.app/legal/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://knock.app/legal/privacy
- group: auth
  title: ''
  type: TrustCenter
  url: https://trust.knock.app
- group: company
  title: ''
  type: Blog
  url: https://knock.app/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/knocklabs
- group: build
  title: ''
  type: SDKs
  url: https://github.com/knocklabs/knock-node
- group: build
  title: ''
  type: SDKs
  url: https://github.com/knocklabs/knock-python
- group: build
  title: ''
  type: SDKs
  url: https://github.com/knocklabs/knock-ruby
- group: build
  title: ''
  type: SDKs
  url: https://github.com/knocklabs/knock-go
- group: build
  title: ''
  type: SDKs
  url: https://github.com/knocklabs/knock-elixir
- group: build
  title: ''
  type: SDKs
  url: https://github.com/knocklabs/knock-java
- group: build
  title: ''
  type: SDKs
  url: https://github.com/knocklabs/knock-dotnet
- group: build
  title: ''
  type: SDKs
  url: https://github.com/knocklabs/knock-php
- group: build
  title: ''
  type: SDKs
  url: https://github.com/knocklabs/knock-swift
- group: build
  title: ''
  type: SDKs
  url: https://github.com/knocklabs/knock-android
- group: build
  title: ''
  type: SDKs
  url: https://github.com/knocklabs/knock-flutter
- group: build
  title: ''
  type: SDKs
  url: https://github.com/knocklabs/javascript
- group: build
  title: ''
  type: SDKs
  url: https://github.com/knocklabs/knock-mgmt-node
- group: build
  title: ''
  type: SDKs
  url: https://github.com/knocklabs/knock-mgmt-python
- group: build
  title: ''
  type: SDKs
  url: https://github.com/knocklabs/knock-mgmt-go
- group: build
  title: ''
  type: Tools
  url: https://github.com/knocklabs/knock-cli
- group: build
  title: ''
  type: Tools
  url: https://mcp.knock.app/mcp
- group: build
  title: ''
  type: Tools
  url: https://github.com/knocklabs/knock-mcp
- group: build
  title: ''
  type: Tools
  url: https://github.com/knocklabs/agent-toolkit
- group: build
  title: ''
  type: Tools
  url: https://github.com/knocklabs/telegraph
- group: build
  title: ''
  type: CodeExamples
  url: https://github.com/knocklabs/in-app-notifications-example-nextjs
- group: build
  title: ''
  type: CodeExamples
  url: https://github.com/knocklabs/slack-kit-example
- group: build
  title: ''
  type: CodeExamples
  url: https://github.com/knocklabs/ios-example-app
- group: build
  title: ''
  type: CodeExamples
  url: https://github.com/knocklabs/ai-agent-examples
- group: build
  title: ''
  type: CodeExamples
  url: https://github.com/knocklabs/workflow-templates
- group: build
  title: ''
  type: CodeExamples
  url: https://github.com/knocklabs/notion-feed-example
- group: build
  title: ''
  type: CodeExamples
  url: https://github.com/knocklabs/marketplace-example
- group: build
  title: ''
  type: Plugins
  url: https://github.com/knocklabs/react-notification-feed
- group: design
  title: ''
  type: Webhooks
  url: https://docs.knock.app/developer-tools/outbound-webhooks/overview
- group: design
  title: ''
  type: Webhooks
  url: https://docs.knock.app/developer-tools/outbound-webhooks/event-types
- group: docs
  href: https://artifacts.apis.io/knock-app/asyncapi/knock-webhooks-asyncapi.yml
  title: ''
  type: AsyncAPI
  url: asyncapi/knock-webhooks-asyncapi.yml
- group: commercial
  href: https://artifacts.apis.io/knock-app/plans/knock-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/knock-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/knock-app/rate-limits/knock-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/knock-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/knock-app/finops/knock-finops.yml
  title: ''
  type: FinOps
  url: finops/knock-finops.yml
- group: design
  href: https://artifacts.apis.io/knock-app/json-ld/knock-app-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/knock-app-context.jsonld
- group: design
  href: https://artifacts.apis.io/knock-app/vocabulary/knock-app-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/knock-app-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/knock-app/rules/knock-app-rules.yml
  title: ''
  type: SpectralRules
  url: rules/knock-app-rules.yml
- group: docs
  title: ''
  type: Documentation
  url: https://docs.knock.app/ai/mcp-server
- group: docs
  title: ''
  type: Documentation
  url: https://docs.knock.app/ai/agent
- group: docs
  title: ''
  type: Documentation
  url: https://docs.knock.app/ai/skills
- group: docs
  title: ''
  type: Documentation
  url: https://docs.knock.app/ai/agent-function
- group: docs
  title: ''
  type: Documentation
  url: https://docs.knock.app/developer-tools/service-tokens
- group: docs
  title: ''
  type: Documentation
  url: https://docs.knock.app/concepts/environments
- group: docs
  title: ''
  type: Documentation
  url: https://docs.knock.app/concepts/commits
- group: docs
  title: ''
  type: Documentation
  url: https://docs.knock.app/template-editor/reference-liquid-helpers
- group: operate
  title: ''
  type: Forums
  url: https://knock.app/community
created: '2026-05-25'
description: Knock is notifications infrastructure as a service — a product and customer messaging platform you use to power transactional, lifecycle, broadcast, and in-product messaging across email, SMS, push, in-app, in-app guides, chat (Slack / Discord / Teams / WhatsApp), and outbound webhooks. Knock exposes two REST surfaces — a runtime API (api.knock.app) for triggering workflows and managing recipients/messages, and a Management API (control.knock.app) for resource CRUD — together with official SDKs in Node, Python, Ruby, Go, Elixir, Java, .NET, PHP and mobile (Swift, Kotlin, Flutter, React Native, Expo); a CLI; a remote MCP server; an agent toolkit for OpenAI / AI SDK / Langchain / Mastra; outbound webhooks; AI agent workflow steps; SlackKit and TeamsKit; and a git-style environment / branch / commit model for safe promotion of notification resources.
examples:
- key_count: 2
  name: Knock Create Schedule Example
  slug: knock-create-schedule-example
- key_count: 2
  name: Knock Identify User Example
  slug: knock-identify-user-example
- key_count: 2
  name: Knock Trigger Workflow Example
  slug: knock-trigger-workflow-example
features:
- Cross-channel notification workflows — email, SMS, push, in-app, in-app guides, chat (Slack/Discord/Teams/WhatsApp), and outbound webhooks from one trigger
- Workflow function steps — batch, delay, branch, experiment, throttle, fetch (HTTP), AI agent, trigger-workflow, update-user / update-tenant / update-object / update-data / update-audience
- Drag-and-drop workflow builder used collaboratively by engineering, product, and growth
- Broadcasts — one-time messages to audience-targeted groups from the Knock dashboard
- Guides — in-app lifecycle messaging using your own components and design system
- Recipients model — Users, non-user Objects, and Tenants with channel data and properties
- Preferences — per-channel, per-workflow, per-category preference sets enforced automatically on every run and broadcast
- Audiences — static and dynamic user segments that automatically drive lifecycle workflow triggers
- Schedules — one-off and recurring (timezone-aware) workflow firing
- Subscriptions — many-to-many fan-out from Objects to recipient lists
- Conditions — dynamic control flow on trigger data, recipient properties, and prior step status
- Templates — drag-and-drop editor + Liquid; partials, branding, translations (i18n), email layouts
- Real-time in-app feed API plus pre-built React, JavaScript, iOS, Android, Flutter, React Native, Expo, and Vue/Nuxt SDKs
- Outbound webhook events for full message lifecycle and environment change tracking
- Customer-facing webhook channel (let your customers configure their own webhook destinations)
- Idempotent requests via Idempotency-Key
- Cursor-based pagination
- Tiered per-endpoint rate limits (1, 5, 60, 200, 1000 req/sec) scoped per environment or per signed user
- Enhanced security mode with signed user tokens (JWT)
- Environments + Branches + Commits — git-style resource workflow with promotion across dev/staging/prod
- Knock CLI for local-first resource management against the Management API
- Knock MCP server (remote) at mcp.knock.app/mcp — OAuth 2.1 + PKCE; tool groups for resources, commits, debug, data, and docs
- Knock Agent Toolkit — AI SDK, OpenAI function-calling, Langchain, Mastra, and local MCP server bindings
- AI agent function step inside workflows for prompt-driven enrichment and personalization
- Knock skills — procedural knowledge packages for AI agents working with Knock
- SlackKit and TeamsKit — drop-in OAuth + channel-data UX for connecting customer Slack/Teams workspaces
- Data warehouse / Segment / Datadog observability streams
- Source events — trigger workflows from CDPs (Segment, Rudderstack) or reverse-ETL (Hightouch, Census)
- Multi-tenancy with per-tenant branding and locked preferences (Enterprise)
- SAML 2.0 SSO, SCIM directory sync, HIPAA / BAA on Enterprise
- Official SDKs in Node, Python, Ruby, Go, Elixir, Java, .NET, PHP, plus mobile (Swift, Kotlin, Flutter, React Native, Expo) and Management-API SDKs (Node, Python, Go)
finops:
- has_sources: true
  method: derived
  name: Knock Finops
  primary_unit: subscription
  service_category: ''
  slug: knock-finops
  template: false
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/knock-app.png
json_schemas:
- name: Knock Message
  property_count: 19
  slug: knock-message
- name: Knock Workflow Trigger Request
  property_count: 5
  slug: knock-workflow-trigger
jsonld:
- class_count: 0
  name: Knock App Context
  property_count: 11
  slug: knock-app-context
layout: provider
mcp_servers:
- description: Knock ships an official remote (hosted) MCP server plus a local MCP server bundled with the Agent Toolkit. The remote server exposes tools to interact with all Knock resources through the Management A
  name: Knock MCP Server
  slug: knock
modified: '2026-06-20'
name: Knock
nav: Providers
network: true
overview: 'Knock publishes 32 API contracts indexed on the [APIs.io](https://apis.io/) network, including Outbound Webhooks, Accounts API, API keys API, and 29 more. Tagged areas include Notification, Messaging, Infrastructure, Workflows, and Cross-Channel.


  The Knock catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 3 Spectral governance rulesets.


  Knock''s developer surface includes authentication, sandbox, CLI, developer portal, documentation, getting-started guide, signup flow, and 107 more developer resources.'
plans:
- name: Knock App Price Estimates
  plan_count: 0
  slug: knock-app-price-estimates
- name: Knock Plans Pricing
  plan_count: 3
  slug: knock-plans-pricing
random_paper: 12
rate_limits:
- limit_count: 5
  name: Knock Rate Limits
  slug: knock-rate-limits
rules:
- authorship: generated
  effective_rule_count: 33
  extends:
  - spectral:asyncapi
  name: Knock — asyncapi rules
  rule_count: 6
  severity_counts:
    error: 1
    hint: 0
    info: 0
    warn: 5
  slug: knock-app-asyncapi-spectral-rules
- authorship: generated
  effective_rule_count: 5
  extends: []
  name: Knock — jsonschema rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: knock-app-jsonschema-spectral-rules
- authorship: unmarked
  effective_rule_count: 49
  extends:
  - spectral:oas
  name: Knock API Rules
  rule_count: 8
  severity_counts:
    error: 3
    hint: 0
    info: 2
    warn: 3
  slug: knock-app-rules
score:
  band: strong
  composite: 59.9
  coverage:
    artifact_dirs: 37
    catalog_earned: 64.0
    catalog_earned_first_party: 0.0
    catalog_gap: 51.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.2
  facets:
    access_clarity: 35.5
    contract_governance: 31.8
    contract_quality: 69.7
    developer_ergonomics: 82.1
    discoverability: 66.7
    operational_transparency: 50.0
  previous_composite: 59.7
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 23.2
      total: 56
    mcp: first-party
  regulatory:
    applies: true
    jurisdictions:
    - jurisdiction: US
      standard: hipaa
    jurisdictions_satisfied: 1
    matched_via: tags
    regime: Telecommunications
    regime_id: telecommunications
    score: 16.3
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 33.3
screenshot: https://apis.io/screenshots/knock-app/knock-app-2026-06-20T184113.png
security:
- kind: authentication
  name: Knock App Authentication
  slug: knock-app-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Knock App Domain Security
  slug: knock-app-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: knock-app
tags:
- Notification
- Messaging
- Infrastructure
- Workflows
- Cross-Channel
- Email
- SMS
- Push
- In-App
- Chat
- Slack
- Webhook
- MCP
- AI Agents
- Developer Platform
website: https://www.knock.app/
---
