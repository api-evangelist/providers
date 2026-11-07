---
access_model:
  confidence: high
  label: Paid
  onboarding: unknown
  pricing: paid
  public: false
  source:
  - plans
  - authentication
  - scopes
  - rate-limits
  - security
  - sandbox
  trial: false
  try_now: false
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
    dynamic_client_registration: false
    error_semantics: derived
    event_surface_described: true
    idempotency: false
    mcp_server: templated
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: mostly
    pagination_ratio: false
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 41.5
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 74
  human_in_the_loop: 0
  name: Gainsight Agentic Access
  operation_count: 169
  slug: gainsight-agentic-access
  summary_line: 169 operations · 74 acting
api_count: 15
apis:
- baseURL: https://api.aptrinsic.com/v1
  baseurl_source: declared
  description: Manage account records and attributes
  name: Gainsight Accounts API
  phrasing_intents:
  - id: listAccounts
    intent: List product accounts
    question: How can I page through every account tracked in Gainsight PX?
  - id: createAccount
    intent: Create or update a product account
    question: How do I add a customer account to Gainsight PX, or overwrite it if it already exists?
  - id: getAccount
    intent: Get a product account
    question: What does Gainsight PX currently store for a single account?
  - id: updateAccount
    intent: Partially update a product account
    question: Can I change just an account's plan without resending all its attributes?
  - id: deleteAccount
    intent: Delete a product account
    question: Can I remove an account from Gainsight PX entirely?
  - id: getAccountsUsingGET
    intent: Filter accounts with the v1 API
    question: Which accounts match a filter such as industry equals software in the v1 accounts API?
  - id: createAccountUsingPOST
    intent: Create an account with product tag keys
    question: What do I need to create a v1 account, and why does it ask for a property key?
  - id: updateAccountUsingPUT
    intent: Update an account whose ID has special characters
    question: My account ID contains slashes, so how can I update it without putting it in the URL?
  phrasing_ops: 11
  slug: gainsight-accounts-api
- baseURL: https://{domain}.gainsightcloud.com/v1
  baseurl_source: declared
  description: Manage timeline activities
  name: Gainsight Activities API
  phrasing_intents:
  - id: createActivity
    intent: Log a timeline activity
    question: How do I log a meeting or call on a company's timeline?
  - id: bulkCreateActivities
    intent: Bulk create timeline activities
    question: Can I load many timeline activities in one request?
  - id: getActivity
    intent: Get a timeline activity
    question: Where can I read the notes and attendees of one logged activity?
  - id: updateActivity
    intent: Update a timeline activity
    question: Can I edit the subject or notes of an activity I already logged?
  - id: deleteActivity
    intent: Delete a timeline activity
    question: Can I remove an activity that was logged by mistake?
  - id: searchActivities
    intent: Search timeline activities
    question: Which activities were logged against a given company last quarter?
  phrasing_ops: 6
  slug: gainsight-activities-api
- baseURL: https://{domain}.gainsightcloud.com/v1
  baseurl_source: declared
  description: Retrieve activity type configurations
  name: Gainsight Activity Types API
  phrasing_intents:
  - id: getActivityTypes
    intent: List timeline activity types
    question: What activity types are configured for the timeline?
  phrasing_ops: 1
  slug: gainsight-activity-types-api
- baseURL: https://{domain}.gainsightcloud.com/v1
  baseurl_source: declared
  description: CRUD operations on company records
  name: Gainsight Companies API
  phrasing_intents:
  - id: insertCompanies
    intent: Insert company records in bulk
    question: Can I load a batch of new companies into the Company object?
  - id: updateCompanies
    intent: Bulk update company records by key
    question: How do I update up to 50 company records at once, matched on a key field?
  - id: searchCompanies
    intent: Search company records
    question: Which companies have ARR over a threshold and renew this quarter?
  - id: getCompany
    intent: Get a company from the Company object
    question: How do I read a company record from the data objects API by its Gainsight ID?
  - id: deleteCompany
    intent: Delete a company from the Company object
    question: Can I delete a company record through the data objects API?
  - id: listCompanies
    intent: List companies
    question: What companies are in Gainsight?
  - id: createCompany
    intent: Create a company
    question: How do I add a single new customer company with its ARR and lifecycle stage?
  - id: getV1CompaniesByCompanyId
    intent: Get a company
    question: What is a company's ARR, status and renewal date?
  phrasing_ops: 10
  slug: gainsight-companies-api
- baseURL: https://{domain}.gainsightcloud.com/v1
  baseurl_source: declared
  description: Manage company team records
  name: Gainsight Company Team API
  phrasing_intents:
  - id: upsertCompanyTeam
    intent: Assign users to company teams
    question: How do I assign a CSM or other team member to a customer company?
  - id: searchCompanyTeam
    intent: Search company team assignments
    question: Who is on the account team for a given company?
  phrasing_ops: 2
  slug: gainsight-company-team-api
- baseURL: https://{domain}.gainsightcloud.com/v1
  baseurl_source: declared
  description: Success plan configuration
  name: Gainsight Configuration API
  phrasing_intents:
  - id: getSuccessPlanTypes
    intent: List success plan types
    question: What success plan types are configured?
  phrasing_ops: 1
  slug: gainsight-configuration-api
- baseURL: https://{domain}.gainsightcloud.com/v1
  baseurl_source: declared
  description: Retrieve CTA type and reason configurations
  name: Gainsight CTA Configuration API
  phrasing_intents:
  - id: getCTATypes
    intent: List CTA types
    question: What CTA types are configured in Cockpit?
  - id: getCTAReasons
    intent: List CTA reasons
    question: What reasons can be given for a CTA?
  - id: getCTAPriorities
    intent: List CTA priorities
    question: What priority levels can a CTA have?
  - id: getCTAStatuses
    intent: List CTA statuses
    question: What statuses can a CTA move through?
  phrasing_ops: 4
  slug: gainsight-cta-configuration-api
- baseURL: https://{domain}.gainsightcloud.com/v1
  baseurl_source: declared
  description: Create and manage Calls to Action
  name: Gainsight CTAs API
  phrasing_intents:
  - id: createCTA
    intent: Create a call to action
    question: How do I open a new CTA in Cockpit for an at-risk customer?
  - id: getCTA
    intent: Get a call to action
    question: What is the status and owner of a specific CTA?
  - id: updateCTA
    intent: Update a call to action
    question: How do I close or reprioritize an existing CTA?
  - id: searchCTAs
    intent: Search calls to action
    question: Which open CTAs are overdue across my accounts?
  phrasing_ops: 4
  slug: gainsight-ctas-api
- baseURL: https://api.aptrinsic.com/v1
  baseurl_source: declared
  description: Send custom events for tracking
  name: Gainsight Custom Events API
  phrasing_intents:
  - id: sendCustomEvent
    intent: Track a custom event for a user
    question: How do I send a custom product event, like 'report exported', for one of my users?
  - id: getCustomEventsUsingGET
    intent: List custom events
    question: Which custom events has a given user fired in a date range?
  - id: createCustomEventUsingPOST
    intent: Record a custom event with the v1 API
    question: What does the v1 endpoint need to record a custom event with a product key and user type?
  phrasing_ops: 3
  slug: gainsight-custom-events-api
- baseURL: https://{domain}.gainsightcloud.com/v1
  baseurl_source: declared
  description: CRUD operations on custom object records
  name: Gainsight Custom Objects API
  phrasing_intents:
  - id: insertCustomObjectRecords
    intent: Insert custom object records
    question: Can I add new rows to one of my custom objects?
  - id: updateCustomObjectRecords
    intent: Bulk update custom object records
    question: How do I update existing rows in a custom object matched on key fields?
  - id: searchCustomObjectRecords
    intent: Search custom object records
    question: Which rows in a custom object match my filter?
  - id: getCustomObjectRecord
    intent: Get a custom object record
    question: How do I read one record from a custom object by ID?
  - id: deleteCustomObjectRecord
    intent: Delete a custom object record
    question: Can I delete one row from a custom object?
  phrasing_ops: 5
  slug: gainsight-custom-objects-api
- baseURL: https://api.aptrinsic.com/v1
  baseurl_source: declared
  description: Manage in-app engagements
  name: Gainsight Engagements API
  phrasing_intents:
  - id: listEngagements
    intent: List in-app engagements
    question: What in-app engagements are set up in Gainsight PX?
  phrasing_ops: 1
  slug: gainsight-engagements-api
- baseURL: https://{domain}.gainsightcloud.com/v1
  baseurl_source: declared
  description: Publish and manage events
  name: Gainsight Events API
  phrasing_intents:
  - id: publishEvent
    intent: Publish an external event
    question: How do I push an event from another system into Gainsight to trigger rules?
  - id: publishEventsBulk
    intent: Publish events in bulk
    question: Can I publish many external events in a single request?
  - id: listEventTypes
    intent: List event types
    question: What event types are configured for publishing?
  phrasing_ops: 3
  slug: gainsight-events-api
- baseURL: https://api.aptrinsic.com/v1
  baseurl_source: declared
  description: Track feature usage and adoption
  name: Gainsight Feature Match API
  phrasing_intents:
  - id: listFeatures
    intent: List features with adoption metrics
    question: Which tracked features are users adopting most?
  phrasing_ops: 1
  slug: gainsight-feature-match-api
- baseURL: https://{domain}.gainsightcloud.com/v1
  baseurl_source: declared
  description: Retrieve field metadata
  name: Gainsight Fields API
  phrasing_intents:
  - id: listFields
    intent: List fields on an object
    question: What fields does the Company object have?
  - id: getField
    intent: Get a field's metadata
    question: What data type is a specific field on an object?
  phrasing_ops: 2
  slug: gainsight-fields-api
- baseURL: https://{domain}.gainsightcloud.com/v1
  baseurl_source: declared
  description: Manage customer goals
  name: Gainsight Goals API
  phrasing_intents:
  - id: createGoal
    intent: Create a customer goal
    question: How do I record a customer's business goal with a target date?
  - id: getGoal
    intent: Get a customer goal
    question: What is the status of a particular customer goal?
  - id: updateGoal
    intent: Update a customer goal
    question: Can I mark a customer goal as achieved?
  - id: searchGoals
    intent: Search customer goals
    question: Which customers have open goals due this quarter?
  phrasing_ops: 4
  slug: gainsight-goals-api
- baseURL: https://{domain}.gainsightcloud.com/v1
  baseurl_source: declared
  description: Manage bulk import jobs
  name: Gainsight Jobs API
  phrasing_intents:
  - id: createBulkJob
    intent: Start a CSV bulk import job
    question: How do I import a large CSV of records into a Gainsight object?
  - id: listBulkJobs
    intent: List bulk import jobs
    question: Which bulk imports are still running or failed?
  - id: getBulkJob
    intent: Check a bulk job's status
    question: Has my bulk import finished yet?
  - id: getBulkJobErrors
    intent: Get a bulk job's errors
    question: Which rows failed in my bulk import, and why?
  phrasing_ops: 4
  slug: gainsight-jobs-api
- baseURL: https://{domain}.gainsightcloud.com/v1
  baseurl_source: declared
  description: Manage goal metrics
  name: Gainsight Metrics API
  phrasing_intents:
  - id: listGoalMetrics
    intent: List a goal's metrics
    question: How is progress on a customer goal being measured?
  - id: addGoalMetric
    intent: Add a metric to a goal
    question: Can I add a measurable target, like adoption rate, to a customer goal?
  phrasing_ops: 2
  slug: gainsight-metrics-api
- baseURL: https://{domain}.gainsightcloud.com/v1
  baseurl_source: declared
  description: Manage success plan objectives
  name: Gainsight Objectives API
  phrasing_intents:
  - id: listObjectives
    intent: List a success plan's objectives
    question: What objectives are part of a customer's success plan?
  - id: createObjective
    intent: Add an objective to a success plan
    question: How do I add a new objective to a success plan?
  phrasing_ops: 2
  slug: gainsight-objectives-api
- baseURL: https://{domain}.gainsightcloud.com/v1
  baseurl_source: declared
  description: Retrieve object metadata
  name: Gainsight Objects API
  phrasing_intents:
  - id: listObjects
    intent: List data objects
    question: What standard and custom objects exist in my Gainsight org?
  - id: getObject
    intent: Get an object's metadata
    question: What is the definition of a particular object, such as Company?
  phrasing_ops: 2
  slug: gainsight-objects-api
- baseURL: https://{domain}.gainsightcloud.com/v1
  baseurl_source: declared
  description: Manage opportunity records
  name: Gainsight Opportunities API
  phrasing_intents:
  - id: createOpportunity
    intent: Create an opportunity
    question: How do I log a renewal, upsell or downsell opportunity?
  - id: updateOpportunity
    intent: Update opportunity records
    question: Can I update existing renewal opportunities matched on a key field?
  - id: searchOpportunities
    intent: Search opportunities
    question: Which renewals are closing this quarter?
  - id: getOpportunity
    intent: Get an opportunity
    question: What details come back when I look up one opportunity by ID?
  phrasing_ops: 4
  slug: gainsight-opportunities-api
- baseURL: https://{domain}.gainsightcloud.com/v1
  baseurl_source: declared
  description: Manage person records
  name: Gainsight People API
  phrasing_intents:
  - id: upsertPeople
    intent: Upsert person records
    question: How do I create or update contacts in Gainsight matched on email?
  - id: searchPeople
    intent: Search person records
    question: Which contacts work at a given company?
  - id: getPerson
    intent: Get a person record
    question: How do I read one contact's record by Gainsight ID?
  - id: deletePerson
    intent: Delete a person record
    question: Can I delete a contact from Gainsight?
  - id: listPeople
    intent: List person records
    question: What contacts are stored in Gainsight?
  phrasing_ops: 5
  slug: gainsight-people-api
- baseURL: https://{domain}.gainsightcloud.com/v1
  baseurl_source: declared
  description: Retrieve playbook configurations
  name: Gainsight Playbooks API
  phrasing_intents:
  - id: listPlaybooks
    intent: List playbooks
    question: What playbooks are configured for CTAs?
  - id: getPlaybook
    intent: Get a playbook and its tasks
    question: What task templates are in a particular playbook?
  phrasing_ops: 2
  slug: gainsight-playbooks-api
- baseURL: https://{domain}.gainsightcloud.com
  baseurl_source: declared
  description: Run reports and retrieve analytics data
  name: Gainsight Reports API
  phrasing_intents:
  - id: runReport
    intent: Run a report
    question: Can I run a saved Gainsight report through the API?
  phrasing_ops: 1
  slug: gainsight-reports-api
- baseURL: https://{domain}.gainsightcloud.com/v1
  baseurl_source: declared
  description: SCIM provisioning endpoints
  name: Gainsight SCIM API
  phrasing_intents:
  - id: scimListUsers
    intent: List users via SCIM
    question: How does my identity provider list Gainsight users over SCIM?
  - id: scimCreateUser
    intent: Provision a user via SCIM
    question: How do I provision a new Gainsight user from my identity provider?
  - id: scimGetUser
    intent: Get a user via SCIM
    question: Can I read one provisioned user through SCIM?
  - id: scimUpdateUser
    intent: Update a user via SCIM
    question: Can my identity provider update a user's email over SCIM?
  - id: scimDeleteUser
    intent: De-provision a user via SCIM
    question: How do I de-provision a departed employee over SCIM?
  phrasing_ops: 5
  slug: gainsight-scim-api
- baseURL: https://api.aptrinsic.com/v1
  baseurl_source: declared
  description: Manage event subscriptions
  name: Gainsight Subscription API
  phrasing_intents:
  - id: listSubscriptions
    intent: List event webhook subscriptions
    question: What webhook subscriptions are set up for events?
  - id: createSubscription
    intent: Subscribe a webhook to events
    question: How do I get Gainsight events pushed to my own URL?
  phrasing_ops: 2
  slug: gainsight-subscription-api
- baseURL: https://{domain}.gainsightcloud.com/v1
  baseurl_source: declared
  description: Manage success plans
  name: Gainsight Success Plans API
  phrasing_intents:
  - id: createSuccessPlan
    intent: Create a success plan
    question: How do I create a success plan for a customer?
  - id: getSuccessPlan
    intent: Get a success plan
    question: What is the status of a customer's success plan?
  - id: updateSuccessPlan
    intent: Update a success plan
    question: Can I change a success plan's owner or end date?
  - id: searchSuccessPlans
    intent: Search success plans
    question: Which customers have active success plans?
  phrasing_ops: 4
  slug: gainsight-success-plans-api
- baseURL: https://{domain}.gainsightcloud.com/v1
  baseurl_source: declared
  description: Manage tasks
  name: Gainsight Tasks API
  phrasing_intents:
  - id: createTask
    intent: Create a CTA task
    question: How do I add a follow-up task to a CTA?
  - id: getTask
    intent: Get a task
    question: What is the status of a particular task?
  - id: updateTask
    intent: Update a task
    question: Can I mark a CTA task as complete?
  - id: searchTasks
    intent: Search tasks
    question: Which tasks are overdue across my CTAs?
  phrasing_ops: 4
  slug: gainsight-tasks-api
- baseURL: https://{domain}.gainsightcloud.com/v1
  baseurl_source: declared
  description: Manage goal templates
  name: Gainsight Templates API
  phrasing_intents:
  - id: listGoalTemplates
    intent: List goal templates
    question: What goal templates are configured?
  phrasing_ops: 1
  slug: gainsight-templates-api
- baseURL: https://{domain}.gainsightcloud.com/v1
  baseurl_source: declared
  description: Manage Gainsight users
  name: Gainsight Users API
  phrasing_intents:
  - id: listUsers
    intent: List Gainsight users
    question: Who are the users in my Gainsight instance?
  - id: createUser
    intent: Create or update a product user
    question: How do I add an end user to Gainsight PX, or overwrite them if they exist?
  - id: getUser
    intent: Get a Gainsight user
    question: Where can I look up a Gainsight user by user ID?
  - id: updateUser
    intent: Change a user's license or role
    question: Can I change a Gainsight user's license type or user type?
  - id: patchUsersByUserId
    intent: Partially update a product user
    question: Can I patch just a PX user's title or phone?
  - id: deleteUser
    intent: Delete a product user
    question: Can I delete a user from Gainsight PX by user ID?
  - id: deactivateUser
    intent: Deactivate a user
    question: Is there a way to deactivate a user without deleting them?
  - id: getUsersUsingGET
    intent: Filter users with the v1 API
    question: Which users match a filter such as role or last seen date?
  phrasing_ops: 16
  slug: gainsight-users-api
- description: 'The Gainsight Customer Communities REST API — 348 documented operations across five groups: Community (articles, conversations, questions, ideas, product updates, tags, moderation, webhooks), Events, '
  name: Gainsight CC (Customer Communities) REST API
  slug: gainsight-cc-api
- description: Gainsight's first-party remote Model Context Protocol server for Gainsight CS, exposed per tenant at /v1/ds-mcp/mcp on the customer's own gainsightcloud.com host. Reads companies, relationships, CTAs,
  name: Gainsight CS MCP Server
  slug: gainsight-cs-mcp
- baseURL: https://api.aptrinsic.com/v1
  baseurl_source: declared
  description: Admin Model
  name: Gainsight Admin API
  phrasing_intents:
  - id: getModelAttributesUsingGET
    intent: List attributes of a data model
    question: What attributes does the user or account model have in PX?
  - id: getEngagementCollisionsUsingGET
    intent: Report engagement collisions
    question: Which engagements collided with each other in the last month?
  - id: getEngagementErrorDetailsUsingGET
    intent: Get error details for an engagement
    question: Why is one particular engagement failing, broken down by browser?
  - id: getEngagementErrorSummariesUsingGET
    intent: Summarize engagements with errors
    question: Which engagements had errors this week?
  - id: getIntegrationStatusesUsingGET
    intent: Check integration statuses
    question: Are my PX integrations healthy right now?
  - id: getDetailUsingGET
    intent: Get subscription details
    question: What are the details of my current PX subscription?
  - id: getSubscriptionUsersNotSeenAfterUsingGET
    intent: Find users not seen since a date
    question: Which users haven't been seen in the product since a given date?
  phrasing_ops: 7
  slug: gainsight-admin-api
- baseURL: https://api.aptrinsic.com/v1
  baseurl_source: declared
  description: Article related endpoints
  name: Gainsight Article API
  phrasing_intents:
  - id: getArticlesUsingGET
    intent: List knowledge center articles
    question: What articles exist in my PX subscription?
  - id: getArticleUsingGET
    intent: Get a knowledge center article
    question: How do I pull the content of one article by its ID?
  phrasing_ops: 2
  slug: gainsight-article-api
- baseURL: https://api.aptrinsic.com/v1
  baseurl_source: declared
  description: Email Event Operations
  name: Gainsight Email Event API
  phrasing_intents:
  - id: getEmailEventsUsingGET
    intent: List email events
    question: Which email opens and clicks were tracked for my users?
  phrasing_ops: 1
  slug: gainsight-emailevent-api
- baseURL: https://api.aptrinsic.com/v1
  baseurl_source: declared
  description: Engagement Operations
  name: Gainsight Engagement API
  phrasing_intents:
  - id: getEngagementsUsingGET
    intent: List in-app engagements
    question: What in-app guides and dialogs have we built?
  - id: changeEngagementEnvUsingPUT
    intent: Move an engagement to one environment
    question: How do I move an engagement from QA to Production?
  - id: changeEngagementEnvsUsingPUT
    intent: Assign an engagement to several environments
    question: Can one engagement run in both Stage and Production at once?
  - id: getEngagementsExtendedUsingGET
    intent: List engagements with rule custom events
    question: Which custom events does each engagement's audience rule depend on?
  - id: getEngagementViewEventsUsingGET
    intent: Get survey metadata for an engagement
    question: What survey metadata is recorded for a given engagement?
  - id: changeEngagementStateUsingPUT
    intent: Start or pause an engagement
    question: How do I pause a guide that's showing to users?
  - id: getEngagementUsingGET
    intent: Get an in-app engagement
    question: How do I look up one engagement's configuration?
  - id: deleteEngagementUsingDELETE
    intent: Delete an in-app engagement
    question: Can I delete an engagement I no longer need?
  phrasing_ops: 8
  slug: gainsight-engagement-api
- baseURL: https://api.aptrinsic.com/v1
  baseurl_source: declared
  description: Engagement View Event Operations
  name: Gainsight Engagement View Event API
  phrasing_intents:
  - id: getEngagementViewEventsUsingGET_1
    intent: List engagement view events
    question: Which users viewed a particular in-app engagement?
  phrasing_ops: 1
  slug: gainsight-engagementviewevent-api
- baseURL: https://api.aptrinsic.com/v1
  baseurl_source: declared
  description: External Segment Operations
  name: Gainsight External Segments API
  phrasing_intents:
  - id: createExternalSegmentUsingPOST
    intent: Create an external segment
    question: How do I register a segment defined in another system?
  - id: updateExternalSegmentUsingPUT
    intent: Update an external segment
    question: Can I rename an external segment or change its description?
  - id: updateMembershipUsingPOST
    intent: Change external segment membership
    question: What's the way to add users to, or drop them from, an external segment?
  phrasing_ops: 3
  slug: gainsight-externalsegments-api
- baseURL: https://api.aptrinsic.com/v1
  baseurl_source: declared
  description: Feature Operations
  name: Gainsight Feature API
  phrasing_intents:
  - id: getFeaturesUsingGET
    intent: List tracked features
    question: What features are defined in my product's feature tree?
  - id: getFeatureAdoptionUsingGET
    intent: Get feature adoption statistics
    question: How many users adopted a feature last week?
  - id: backfillFeatureUsingPOST
    intent: Backfill a feature's historical data
    question: Can PX recompute a feature's usage for data captured before it was defined?
  - id: getFeatureUsingGET
    intent: Get a feature
    question: How do I see one feature's name, type and parent?
  - id: updateFeatureUsingPUT
    intent: Rename or move a feature
    question: Can I move a feature to the root of the feature tree?
  - id: getFeaturesExtendedUsingGET
    intent: List features with extended details
    question: Is there a v2 feature listing with more detail than the basic one?
  phrasing_ops: 6
  slug: gainsight-feature-api
- baseURL: https://api.aptrinsic.com/v1
  baseurl_source: declared
  description: Feature Match Event Operations
  name: Gainsight Feature Match Event API
  phrasing_intents:
  - id: getFeatureMatchEventsUsingGET
    intent: List feature match events
    question: When did users trigger a given feature?
  phrasing_ops: 1
  slug: gainsight-featurematchevent-api
- baseURL: https://api.aptrinsic.com/v1
  baseurl_source: declared
  description: Form Submit Event Operations
  name: Gainsight Form Submit Event API
  phrasing_intents:
  - id: getFormSubmitEventsUsingGET
    intent: List form submit events
    question: Which forms did my users submit in the product?
  phrasing_ops: 1
  slug: gainsight-formsubmitevent-api
- baseURL: https://api.aptrinsic.com/v1
  baseurl_source: declared
  description: Identify Event Operations
  name: Gainsight Identify Event API
  phrasing_intents:
  - id: getIdentifyEventsUsingGET
    intent: List identify events
    question: When were my users identified in the product?
  phrasing_ops: 1
  slug: gainsight-identifyevent-api
- baseURL: https://api.aptrinsic.com/v1
  baseurl_source: declared
  description: KC Bot related endpoints
  name: Gainsight K Cbot API
  phrasing_intents:
  - id: getKcBotsUsingGET
    intent: List Knowledge Center bots
    question: What Knowledge Center bots are set up in my subscription?
  - id: changeEngagementStateUsingPUT_1
    intent: Start or pause a Knowledge Center bot
    question: How do I pause a Knowledge Center bot?
  - id: getKcBotWithIdUsingGET
    intent: Get a Knowledge Center bot
    question: How do I look up one KC bot's configuration?
  phrasing_ops: 3
  slug: gainsight-kcbot-api
- baseURL: https://api.aptrinsic.com/v1
  baseurl_source: declared
  description: Lead Event Operations
  name: Gainsight Lead Event API
  phrasing_intents:
  - id: getLeadEventsUsingGET
    intent: List lead events
    question: Which lead capture events were recorded?
  phrasing_ops: 1
  slug: gainsight-leadevent-api
- baseURL: https://api.aptrinsic.com/v1
  baseurl_source: declared
  description: localization
  name: Gainsight Localization API
  phrasing_intents:
  - id: exportXLIFFForArticlesUsingGET
    intent: Export article translations as XLIFF
    question: Can I export an article's text for translation?
  - id: exportContentXLIFFUsingGET
    intent: Export a Content Library entry as XLIFF
    question: What's the way to send a Content Library entry out for translation?
  - id: exportXLIFFForEngagementUsingGET
    intent: Export an engagement as XLIFF
    question: Where do I get an in-app engagement's text out for translators?
  - id: exportKCXLIFFUsingGET
    intent: Export a Knowledge Center bot as XLIFF
    question: How do I export a KC bot's strings for localization?
  - id: importXLIFFForArticlesUsingPOST
    intent: Import article translations
    question: What endpoint loads translated articles back into PX?
  - id: importXLIFFForContentEntryUsingPOST
    intent: Import Content Library translations
    question: Where would I upload a translated Content Library entry?
  - id: importXLIFFForEngagementUsingPOST
    intent: Import engagement translations
    question: Can translated engagement text be brought back into PX?
  - id: importXLIFFForKCUsingPOST
    intent: Import Knowledge Center bot translations
    question: How do I upload translated strings for a KC bot?
  phrasing_ops: 8
  slug: gainsight-localization-api
- baseURL: https://api.aptrinsic.com/v1
  baseurl_source: declared
  description: Page View Event Operations
  name: Gainsight Page View Event API
  phrasing_intents:
  - id: getPageViewEventsUsingGET
    intent: List page view events
    question: Which pages did my users view in the product?
  phrasing_ops: 1
  slug: gainsight-pageviewevent-api
- baseURL: https://api.aptrinsic.com/v1
  baseurl_source: declared
  description: Segment Operations
  name: Gainsight Segment API
  phrasing_intents:
  - id: getSegmentsUsingGET
    intent: List segments
    question: What user segments are defined in PX?
  - id: getSegmentUsingGET
    intent: Get a segment
    question: How do I see one segment's definition?
  phrasing_ops: 2
  slug: gainsight-segment-api
- baseURL: https://api.aptrinsic.com/v1
  baseurl_source: declared
  description: Segment Match Event Operations
  name: Gainsight Segment Match Event API
  phrasing_intents:
  - id: getSegmentMatchEventsUsingGET
    intent: List segment match events
    question: When did users enter a given segment?
  phrasing_ops: 1
  slug: gainsight-segmentmatchevent-api
- baseURL: https://api.aptrinsic.com/v1
  baseurl_source: declared
  description: Session Event Operations
  name: Gainsight Session Event API
  phrasing_intents:
  - id: getSessionInitializedEventsUsingGET
    intent: List session start events
    question: When did my users start product sessions?
  phrasing_ops: 1
  slug: gainsight-sessionevent-api
- baseURL: https://api.aptrinsic.com/v1
  baseurl_source: declared
  description: Survey Response Events
  name: Gainsight Survey Response API
  phrasing_intents:
  - id: getEngagementViewEventsUsingGET_2
    intent: List survey responses
    question: What did users answer in my in-app surveys?
  phrasing_ops: 1
  slug: gainsight-surveyresponse-api
- baseURL: https://api.aptrinsic.com/v1
  baseurl_source: declared
  description: User Preferences Version 2 API. Version 2 has support for new setting called 'trackEmailAnalytics' which is to specify whether to track email analytics or not for the given user.
  name: Gainsight UserPreferences V2 API
  phrasing_intents:
  - id: getUserPreferencesUsingPOST_1
    intent: Read v2 preferences with the user ID in the body
    question: Is there a v2 POST lookup that includes email analytics preferences?
  - id: updateUserPreferencesUsingPUT_3
    intent: Update v2 preferences with the user ID in the body
    question: How do I set email analytics tracking for a user whose ID can't go in the URL?
  - id: getUserPreferencesUsingGET_1
    intent: Get a user's v2 preferences
    question: Has a user allowed email analytics tracking?
  - id: updateUserPreferencesUsingPUT_2
    intent: Update a user's v2 preferences
    question: Can I turn off email analytics for one user?
  phrasing_ops: 4
  slug: gainsight-userpreferences-v2-api
- baseURL: https://api.aptrinsic.com/v1
  baseurl_source: declared
  description: User Preferences
  name: Gainsight User Preferences API
  phrasing_intents:
  - id: getUserPreferencesUsingPOST
    intent: Read preferences for a user ID in the body
    question: How do I read a user's preferences when their ID can't go in the URL?
  - id: updateUserPreferencesUsingPUT_1
    intent: Update preferences for a user ID in the body
    question: My user's identify ID has special characters, so how can I update their preferences?
  - id: getUserPreferencesUsingGET
    intent: Get a user's preferences
    question: Has a user opted out of usage tracking or product updates?
  - id: updateUserPreferencesUsingPUT
    intent: Update a user's preferences
    question: How do I stop tracking usage for a user who opted out?
  phrasing_ops: 4
  slug: gainsight-user-preferences-api
artifact_total: 238
asyncapis:
- description: ''
  name: Gainsight Cc Webhooks
  slug: gainsight-cc-webhooks
collections:
- collection_type: open
  name: Gainsight CS Bulk Accounts API
  slug: open-gainsight-accounts-api
- collection_type: open
  name: Gainsight CS Bulk Accounts Activities API
  slug: open-gainsight-activities-api
- collection_type: open
  name: Gainsight CS Bulk Accounts Activity Types API
  slug: open-gainsight-activity-types-api
- collection_type: open
  name: Gainsight CS Bulk Accounts Companies API
  slug: open-gainsight-companies-api
- collection_type: open
  name: Gainsight CS Bulk Accounts Company Team API
  slug: open-gainsight-company-team-api
- collection_type: open
  name: Gainsight CS Bulk Accounts Configuration API
  slug: open-gainsight-configuration-api
- collection_type: open
  name: Gainsight CS Bulk API
  slug: open-gainsight-cs-bulk-api
- collection_type: open
  name: Gainsight CS Company API
  slug: open-gainsight-cs-company-api
- collection_type: open
  name: Gainsight CS CTA API
  slug: open-gainsight-cs-cta-api
- collection_type: open
  name: Gainsight CS Custom Object API
  slug: open-gainsight-cs-custom-object-api
- collection_type: open
  name: Gainsight CS Customer Goals API
  slug: open-gainsight-cs-customer-goals-api
- collection_type: open
  name: Gainsight CS Data Management API
  slug: open-gainsight-cs-data-management-api
- collection_type: open
  name: Gainsight CS Events API
  slug: open-gainsight-cs-events-api
- collection_type: open
  name: Gainsight CS Person API
  slug: open-gainsight-cs-person-api
- collection_type: open
  name: Gainsight CS Renewal Center API
  slug: open-gainsight-cs-renewal-center-api
- collection_type: open
  name: Gainsight CS Success Plan API
  slug: open-gainsight-cs-success-plan-api
- collection_type: open
  name: Gainsight CS Task and Playbook API
  slug: open-gainsight-cs-task-and-playbook-api
- collection_type: open
  name: Gainsight CS Timeline API
  slug: open-gainsight-cs-timeline-api
- collection_type: open
  name: Gainsight CS User Management API
  slug: open-gainsight-cs-user-management-api
- collection_type: open
  name: Gainsight CS Bulk Accounts CTA Configuration API
  slug: open-gainsight-cta-configuration-api
- collection_type: open
  name: Gainsight CS Bulk Accounts CTAs API
  slug: open-gainsight-ctas-api
- collection_type: open
  name: Gainsight CS Bulk Accounts Custom Events API
  slug: open-gainsight-custom-events-api
- collection_type: open
  name: Gainsight CS Bulk Accounts Custom Objects API
  slug: open-gainsight-custom-objects-api
- collection_type: open
  name: Gainsight CS Bulk Accounts Engagements API
  slug: open-gainsight-engagements-api
- collection_type: open
  name: Gainsight CS Bulk Accounts Events API
  slug: open-gainsight-events-api
- collection_type: open
  name: Gainsight CS Bulk Accounts Feature Match API
  slug: open-gainsight-feature-match-api
- collection_type: open
  name: Gainsight CS Bulk Accounts Fields API
  slug: open-gainsight-fields-api
- collection_type: open
  name: Gainsight CS Bulk Accounts Goals API
  slug: open-gainsight-goals-api
- collection_type: open
  name: Gainsight CS Bulk Accounts Jobs API
  slug: open-gainsight-jobs-api
- collection_type: open
  name: Gainsight CS Bulk Accounts Metrics API
  slug: open-gainsight-metrics-api
- collection_type: open
  name: Gainsight CS Bulk Accounts Objectives API
  slug: open-gainsight-objectives-api
- collection_type: open
  name: Gainsight CS Bulk Accounts Objects API
  slug: open-gainsight-objects-api
- collection_type: open
  name: Gainsight CS Bulk Accounts Opportunities API
  slug: open-gainsight-opportunities-api
- collection_type: open
  name: Gainsight CS Bulk Accounts People API
  slug: open-gainsight-people-api
- collection_type: open
  name: Gainsight CS Bulk Accounts Playbooks API
  slug: open-gainsight-playbooks-api
- collection_type: open
  name: Gainsight PX API
  slug: open-gainsight-px-api
- collection_type: open
  name: Gainsight CS Bulk Accounts Reports API
  slug: open-gainsight-reports-api
- collection_type: open
  name: Gainsight REST API
  slug: open-gainsight-rest-api
- collection_type: open
  name: Gainsight CS Bulk Accounts SCIM API
  slug: open-gainsight-scim-api
- collection_type: open
  name: Gainsight CS Bulk Accounts Subscription API
  slug: open-gainsight-subscription-api
- collection_type: open
  name: Gainsight CS Bulk Accounts Success Plans API
  slug: open-gainsight-success-plans-api
- collection_type: open
  name: Gainsight CS Bulk Accounts Tasks API
  slug: open-gainsight-tasks-api
- collection_type: open
  name: Gainsight CS Bulk Accounts Templates API
  slug: open-gainsight-templates-api
- collection_type: open
  name: Gainsight CS Bulk Accounts Users API
  slug: open-gainsight-users-api
common:
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/gainsight/overview
- group: operate
  href: https://artifacts.apis.io/gainsight/lifecycle/gainsight-lifecycle.yml
  title: ''
  type: Deprecation
  url: lifecycle/gainsight-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/gainsight/rules/gainsight-rules.yml
  title: ''
  type: Spectral
  url: rules/gainsight-rules.yml
- group: design
  href: https://artifacts.apis.io/gainsight/rules/gainsight-jsonschema-spectral-rules.yml
  title: ''
  type: Spectral
  url: rules/gainsight-jsonschema-spectral-rules.yml
- group: agent
  href: https://artifacts.apis.io/gainsight/llms/gainsight-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/gainsight-llms.txt
- group: auth
  href: https://artifacts.apis.io/gainsight/well-known/gainsight-support-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/gainsight-support-security.txt
- group: other
  href: https://artifacts.apis.io/gainsight/hosts/gainsight-hosts.yml
  title: ''
  type: Hosts
  url: hosts/gainsight-hosts.yml
- group: build
  href: https://artifacts.apis.io/gainsight/integrations/gainsight-integration-edges.yml
  title: ''
  type: IntegrationEdges
  url: integrations/gainsight-integration-edges.yml
- group: other
  href: https://artifacts.apis.io/gainsight/vendors/gainsight-vendors.yml
  title: ''
  type: Vendors
  url: vendors/gainsight-vendors.yml
- group: company
  title: ''
  type: Newsroom
  url: https://www.gainsight.com/newsroom/
- group: other
  title: ''
  type: Leadership
  url: https://www.gainsight.com/company/leadership/
- group: other
  href: https://artifacts.apis.io/gainsight/capabilities/gainsight-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/gainsight-capability-edges.yml
- group: company
  title: ''
  type: Website
  url: https://www.gainsight.com/
- group: agent
  href: https://artifacts.apis.io/gainsight/agentic-access/gainsight-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/gainsight-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/gainsight/security/gainsight-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/gainsight-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/gainsight/security/gainsight-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/gainsight-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/gainsight/security/gainsight-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/gainsight-domain-security.yml
- group: auth
  href: https://artifacts.apis.io/gainsight/authentication/gainsight-authentication.yml
  title: ''
  type: Authentication
  url: authentication/gainsight-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/gainsight
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/gainsight
- group: start
  title: ''
  type: Portal
  url: https://support.gainsight.com
- group: start
  title: ''
  type: Login
  url: https://app.gainsight.com
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.gainsight.com/terms-of-service/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.gainsight.com/privacy-policy/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.gainsight.com/
- group: docs
  title: ''
  type: developer-docs
  url: https://support.gainsight.com/gainsight_nxt/API_and_Developer_Docs
- group: auth
  title: ''
  type: Authentication
  url: https://support.gainsight.com/gainsight_nxt/API_and_Developer_Docs/Generate_REST_API/Generate_REST_API_Key
- group: auth
  title: ''
  type: oauth
  url: https://support.gainsight.com/gainsight_nxt/01Onboarding_and_Implementation/Onboarding_for_Gainsight_NXT/Login_and_Permissions/OAuth_for_Gainsight_APIs
- group: operate
  title: ''
  type: ReleaseNotes
  url: https://support.gainsight.com/gainsight_nxt/Release_Notes
- group: operate
  title: ''
  type: Community
  url: https://communities.gainsight.com
- group: company
  title: ''
  type: Blog
  url: https://www.gainsight.com/blog/
- group: other
  title: ''
  type: education
  url: https://education.gainsight.com
- group: design
  href: https://artifacts.apis.io/gainsight/json-ld/gainsight-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/gainsight-context.jsonld
- group: docs
  href: https://artifacts.apis.io/gainsight/json-schema/gainsight-company-schema.json
  title: ''
  type: JSONSchema
  url: json-schema/gainsight-company-schema.json
- group: docs
  href: https://artifacts.apis.io/gainsight/json-schema/gainsight-person-schema.json
  title: ''
  type: JSONSchema
  url: json-schema/gainsight-person-schema.json
- group: docs
  href: https://artifacts.apis.io/gainsight/json-schema/gainsight-cta-schema.json
  title: ''
  type: JSONSchema
  url: json-schema/gainsight-cta-schema.json
- group: docs
  href: https://artifacts.apis.io/gainsight/json-schema/gainsight-opportunity-schema.json
  title: ''
  type: JSONSchema
  url: json-schema/gainsight-opportunity-schema.json
- group: docs
  href: https://artifacts.apis.io/gainsight/json-schema/gainsight-timeline-activity-schema.json
  title: ''
  type: JSONSchema
  url: json-schema/gainsight-timeline-activity-schema.json
- group: agent
  href: https://artifacts.apis.io/gainsight/llms/gainsight-px-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/gainsight-px-llms.txt
- group: agent
  href: https://artifacts.apis.io/gainsight/llms/gainsight-cc-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/gainsight-cc-llms.txt
- group: agent
  href: https://artifacts.apis.io/gainsight/well-known/gainsight-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/gainsight-well-known.yml
- group: agent
  href: https://artifacts.apis.io/gainsight/mcp/gainsight-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/gainsight-mcp.yml
- group: build
  href: https://artifacts.apis.io/gainsight/mcp/gainsight-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/gainsight-tool-crosswalk.yml
- group: build
  href: https://artifacts.apis.io/gainsight/packages/gainsight-packages.yml
  title: ''
  type: Packages
  url: packages/gainsight-packages.yml
- group: build
  href: https://artifacts.apis.io/gainsight/packages/gainsight-packages.yml
  title: ''
  type: SDKs
  url: packages/gainsight-packages.yml
- group: build
  href: https://artifacts.apis.io/gainsight/cli/gainsight-cli.yml
  title: ''
  type: CLI
  url: cli/gainsight-cli.yml
- group: design
  href: https://artifacts.apis.io/gainsight/components/gainsight-components.yml
  title: ''
  type: Components
  url: components/gainsight-components.yml
- group: design
  href: https://artifacts.apis.io/gainsight/conformance/gainsight-conformance.yml
  title: ''
  type: Conformance
  url: conformance/gainsight-conformance.yml
- group: auth
  href: https://artifacts.apis.io/gainsight/security/gainsight-trust-center.yml
  title: ''
  type: Compliance
  url: security/gainsight-trust-center.yml
- group: design
  href: https://artifacts.apis.io/gainsight/errors/gainsight-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/gainsight-problem-types.yml
- group: design
  href: https://artifacts.apis.io/gainsight/lifecycle/gainsight-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/gainsight-lifecycle.yml
- group: auth
  href: https://artifacts.apis.io/gainsight/scopes/gainsight-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/gainsight-scopes.yml
- group: design
  href: https://artifacts.apis.io/gainsight/conventions/gainsight-conventions.yml
  title: ''
  type: Conventions
  url: conventions/gainsight-conventions.yml
- group: operate
  href: https://artifacts.apis.io/gainsight/changelog/gainsight-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/gainsight-changelog.yml
- group: design
  href: https://artifacts.apis.io/gainsight/data-model/gainsight-data-model.yml
  title: ''
  type: DataModel
  url: data-model/gainsight-data-model.yml
- group: design
  href: https://artifacts.apis.io/gainsight/asyncapi/gainsight-cc-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/gainsight-cc-webhooks.yml
- group: agent
  href: https://artifacts.apis.io/gainsight/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: start
  href: https://artifacts.apis.io/gainsight/sandbox/gainsight-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/gainsight-sandbox.yml
- group: other
  href: https://artifacts.apis.io/gainsight/overlays/gainsight-px-rest-api-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/gainsight-px-rest-api-overlay.yaml
- group: auth
  title: ''
  type: Security
  url: https://www.gainsight.com/security/vulnerability-disclosure-program/
- group: operate
  href: https://artifacts.apis.io/gainsight/rate-limits/gainsight-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/gainsight-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/gainsight/plans/gainsight-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/gainsight-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/gainsight/vocabulary/gainsight-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/gainsight-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/gainsight/rules/gainsight-jsonschema-spectral-rules.yml
  title: ''
  type: Rules
  url: rules/gainsight-jsonschema-spectral-rules.yml
- group: commercial
  href: https://artifacts.apis.io/gainsight/finops/gainsight-finops.yml
  title: ''
  type: FinOps
  url: finops/gainsight-finops.yml
- group: design
  href: https://artifacts.apis.io/gainsight/json-structure/gainsight-structure.json
  title: ''
  type: JSONStructure
  url: json-structure/gainsight-structure.json
- group: commercial
  title: ''
  type: Pricing
  url: https://www.gainsight.com/pricing/
- group: docs
  title: ''
  type: Documentation
  url: https://support.gainsight.com/gainsight_nxt/API_and_Developer_Docs
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer-portal.gainsight.com/
- group: docs
  title: ''
  type: APIReference
  url: https://developer-portal.gainsight.com/docs/api
- group: start
  title: ''
  type: GettingStarted
  url: https://developer-portal.gainsight.com/docs/getting-started
- group: operate
  title: ''
  type: Support
  url: https://support.gainsight.com
created: '2024-01-01'
description: 'Gainsight is a customer success platform that helps companies retain and grow their customer base through data-driven insights, automation and engagement. Four product lines ship developer surfaces: Gainsight CS (the customer success platform, with REST, Bulk, SCIM and a first-party remote MCP server), Gainsight PX (product experience and analytics, the one surface with a published Swagger contract), Gainsight CC / Customer Communities (348 documented REST operations plus a widget, connector and SDK extension platform), and Skilljar (customer education). Authentication is OAuth 2.1 with PKCE on Gainsight CS, OAuth 2.0 client credentials on CC, and an API-key header on PX.'
finops:
- has_sources: true
  method: derived
  name: Gainsight Finops
  primary_unit: ''
  service_category: ''
  slug: gainsight-finops
  template: true
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/gainsight.png
json_schemas:
- name: Account
  property_count: 24
  slug: gainsight-account-2
- name: AccountInput
  property_count: 6
  slug: gainsight-account-input
- name: Account
  property_count: 10
  slug: gainsight-account
- name: AccountInput
  property_count: 6
  slug: gainsight-accountinput
- name: AccountsPage
  property_count: 3
  slug: gainsight-accounts-page
- name: ActivityInput
  property_count: 9
  slug: gainsight-activity-input
- name: Activity
  property_count: 15
  slug: gainsight-activity
- name: ActivityType
  property_count: 4
  slug: gainsight-activity-type
- name: ActivityInput
  property_count: 9
  slug: gainsight-activityinput
- name: ActivityType
  property_count: 4
  slug: gainsight-activitytype
- name: ApiResponse_2
  property_count: 4
  slug: gainsight-api-response-2
- name: ApiResponse
  property_count: 4
  slug: gainsight-api-response
- name: ApiResponse
  property_count: 4
  slug: gainsight-apiresponse
- name: ArticleExternalViewPage
  property_count: 3
  slug: gainsight-article-external-view-page
- name: ArticleExternalView
  property_count: 14
  slug: gainsight-article-external-view
- name: AttributeMetadata
  property_count: 11
  slug: gainsight-attribute-metadata
- name: BulkJobError
  property_count: 3
  slug: gainsight-bulk-job-error
- name: BulkJob
  property_count: 11
  slug: gainsight-bulk-job
- name: BulkJob
  property_count: 11
  slug: gainsight-bulkjob
- name: BulkJobError
  property_count: 3
  slug: gainsight-bulkjoberror
- name: CompanyInput
  property_count: 7
  slug: gainsight-company-input
- name: CompanyRecord
  property_count: 18
  slug: gainsight-company-record
- name: Gainsight Company
  property_count: 18
  slug: gainsight-company
- name: CompanyTeamRecord
  property_count: 5
  slug: gainsight-company-team-record
- name: CompanyInput
  property_count: 7
  slug: gainsight-companyinput
- name: CompanyRecord
  property_count: 18
  slug: gainsight-companyrecord
- name: CompanyTeamRecord
  property_count: 5
  slug: gainsight-companyteamrecord
- name: Gainsight Call to Action (CTA)
  property_count: 20
  slug: gainsight-cta
- name: CTAInput
  property_count: 10
  slug: gainsight-ctainput
- name: CTAPriority
  property_count: 3
  slug: gainsight-ctapriority
- name: CTAReason
  property_count: 3
  slug: gainsight-ctareason
- name: CTAStatus
  property_count: 3
  slug: gainsight-ctastatus
- name: CTAType
  property_count: 3
  slug: gainsight-ctatype
- name: CustomEvent
  property_count: 14
  slug: gainsight-custom-event-2
- name: CustomEvent
  property_count: 7
  slug: gainsight-custom-event
- name: CustomEventsPage
  property_count: 3
  slug: gainsight-custom-events-page
- name: CustomEvent
  property_count: 7
  slug: gainsight-customevent
- name: EmailEventsPage
  property_count: 3
  slug: gainsight-email-events-page
- name: EngagementAllTypesViewEventsPage
  property_count: 3
  slug: gainsight-engagement-all-types-view-events-page
- name: EngagementEnvironmentsChangeRequest
  property_count: 2
  slug: gainsight-engagement-environments-change-request
- name: EngagementErrorSummaryPage
  property_count: 3
  slug: gainsight-engagement-error-summary-page
- name: Engagement
  property_count: 5
  slug: gainsight-engagement
- name: EngagementStateChangeRequest
  property_count: 3
  slug: gainsight-engagement-state-change-request
- name: EngagementsPage
  property_count: 3
  slug: gainsight-engagements-page
- name: EngagementsWithCustomEventsPage
  property_count: 3
  slug: gainsight-engagements-with-custom-events-page
- name: EventInput
  property_count: 7
  slug: gainsight-event-input
- name: EventType
  property_count: 4
  slug: gainsight-event-type
- name: EventInput
  property_count: 7
  slug: gainsight-eventinput
- name: EventType
  property_count: 4
  slug: gainsight-eventtype
- name: ExternalSegmentDto
  property_count: 4
  slug: gainsight-external-segment-dto
- name: FeatureMatchEventsPage
  property_count: 3
  slug: gainsight-feature-match-events-page
- name: Feature
  property_count: 6
  slug: gainsight-feature
- name: FeatureWithDetailsPage
  property_count: 3
  slug: gainsight-feature-with-details-page
- name: FeaturesPage
  property_count: 3
  slug: gainsight-features-page
- name: FieldMetadata
  property_count: 10
  slug: gainsight-field-metadata
- name: FieldMetadata
  property_count: 10
  slug: gainsight-fieldmetadata
- name: FormSubmitEventsPage
  property_count: 3
  slug: gainsight-form-submit-events-page
- name: GainsightUser
  property_count: 11
  slug: gainsight-gainsight-user
- name: GainsightUser
  property_count: 11
  slug: gainsight-gainsightuser
- name: GainsightUserInput
  property_count: 6
  slug: gainsight-gainsightuserinput
- name: GoalInput
  property_count: 7
  slug: gainsight-goal-input
- name: GoalMetricInput
  property_count: 4
  slug: gainsight-goal-metric-input
- name: GoalMetric
  property_count: 7
  slug: gainsight-goal-metric
- name: Goal
  property_count: 13
  slug: gainsight-goal
- name: GoalTemplate
  property_count: 5
  slug: gainsight-goal-template
- name: GoalInput
  property_count: 7
  slug: gainsight-goalinput
- name: GoalMetric
  property_count: 7
  slug: gainsight-goalmetric
- name: GoalMetricInput
  property_count: 4
  slug: gainsight-goalmetricinput
- name: GoalTemplate
  property_count: 5
  slug: gainsight-goaltemplate
- name: IdentifyEventsPage
  property_count: 3
  slug: gainsight-identify-events-page
- name: KCExternalStateChangeRequest
  property_count: 3
  slug: gainsight-kcexternal-state-change-request
- name: KnowledgeCenterExternalViewPage
  property_count: 3
  slug: gainsight-knowledge-center-external-view-page
- name: KnowledgeCenterExternalView
  property_count: 14
  slug: gainsight-knowledge-center-external-view
- name: LeadEventsPage
  property_count: 3
  slug: gainsight-lead-events-page
- name: ObjectMetadata
  property_count: 9
  slug: gainsight-object-metadata
- name: ObjectiveInput
  property_count: 5
  slug: gainsight-objective-input
- name: Objective
  property_count: 10
  slug: gainsight-objective
- name: ObjectiveInput
  property_count: 5
  slug: gainsight-objectiveinput
- name: ObjectMetadata
  property_count: 9
  slug: gainsight-objectmetadata
- name: OpportunityRecord
  property_count: 20
  slug: gainsight-opportunity-record
- name: Gainsight Opportunity
  property_count: 20
  slug: gainsight-opportunity
- name: OpportunityRecord
  property_count: 20
  slug: gainsight-opportunityrecord
- name: PageViewEventsPage
  property_count: 3
  slug: gainsight-page-view-events-page
- name: PersonRecord
  property_count: 19
  slug: gainsight-person-record
- name: Gainsight Person
  property_count: 18
  slug: gainsight-person
- name: PersonRecord
  property_count: 19
  slug: gainsight-personrecord
- name: Playbook
  property_count: 8
  slug: gainsight-playbook
- name: ResponseEntity
  property_count: 3
  slug: gainsight-response-entity
- name: ScimUserInput
  property_count: 5
  slug: gainsight-scim-user-input
- name: ScimUser
  property_count: 7
  slug: gainsight-scim-user
- name: ScimUser
  property_count: 7
  slug: gainsight-scimuser
- name: ScimUserInput
  property_count: 5
  slug: gainsight-scimuserinput
- name: SearchRequest
  property_count: 4
  slug: gainsight-search-request
- name: SearchResponse
  property_count: 2
  slug: gainsight-search-response
- name: SearchRequest
  property_count: 5
  slug: gainsight-searchrequest
- name: SearchResponse
  property_count: 2
  slug: gainsight-searchresponse
- name: SegmentMatchEventsPage
  property_count: 3
  slug: gainsight-segment-match-events-page
- name: SegmentPayload
  property_count: 3
  slug: gainsight-segment-payload
- name: Segment
  property_count: 2
  slug: gainsight-segment
- name: SegmentsPage
  property_count: 3
  slug: gainsight-segments-page
- name: SessionInitializedEventsPage
  property_count: 3
  slug: gainsight-session-initialized-events-page
- name: SubscriptionInput
  property_count: 3
  slug: gainsight-subscription-input
- name: Subscription
  property_count: 5
  slug: gainsight-subscription
- name: SubscriptionInput
  property_count: 3
  slug: gainsight-subscriptioninput
- name: SuccessPlanInput
  property_count: 8
  slug: gainsight-success-plan-input
- name: SuccessPlan
  property_count: 14
  slug: gainsight-success-plan
- name: SuccessPlan
  property_count: 14
  slug: gainsight-successplan
- name: SuccessPlanInput
  property_count: 8
  slug: gainsight-successplaninput
- name: TaskInput
  property_count: 7
  slug: gainsight-task-input
- name: Task
  property_count: 16
  slug: gainsight-task
- name: TaskInput
  property_count: 7
  slug: gainsight-taskinput
- name: Gainsight Timeline Activity
  property_count: 15
  slug: gainsight-timeline-activity
- name: UpdateUserPreferences
  property_count: 6
  slug: gainsight-update-user-preferences
- name: UpdateUserPreferencesV2
  property_count: 7
  slug: gainsight-update-user-preferences-v2
- name: User
  property_count: 29
  slug: gainsight-user-2
- name: UserIdentifyId
  property_count: 1
  slug: gainsight-user-identify-id
- name: UserInput
  property_count: 10
  slug: gainsight-user-input
- name: UserPreferences
  property_count: 5
  slug: gainsight-user-preferences
- name: UserPreferencesV2
  property_count: 6
  slug: gainsight-user-preferences-v2
- name: User
  property_count: 17
  slug: gainsight-user
- name: UserInput
  property_count: 10
  slug: gainsight-userinput
- name: UsersPage
  property_count: 3
  slug: gainsight-users-page
- name: WriteResponse
  property_count: 2
  slug: gainsight-write-response
- name: WriteResponse
  property_count: 2
  slug: gainsight-writeresponse
json_structures:
- name: Gainsight Structure
  property_count: 0
  slug: gainsight-structure
jsonld:
- class_count: 0
  name: Gainsight Context
  property_count: 11
  slug: gainsight-context
layout: provider
mcp_servers:
- description: Gainsight ships a first-party remote MCP server for Gainsight CS, exposed per tenant at /v1/ds-mcp/mcp on the customer's own gainsightcloud.com host, and a separate local stdio MCP server bundled insi
  name: Gainsight CS MCP Server
  slug: gainsight-cs-mcp-server
modified: '2026-09-17'
name: Gainsight
nav: Providers
network: true
overview: 'Gainsight publishes 51 API contracts indexed on the [APIs.io](https://apis.io/) network, including Accounts API, Activities API, Activity Types API, and 48 more. Tagged areas include Customer Success, Customer Experience, Product Analytics, Customer Communities, and Customer Health.


  The Gainsight catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 2 Spectral governance rulesets.


  Gainsight''s developer surface includes authentication, developer portal, release notes, engineering blog, CLI, changelog, sandbox, and 65 more developer resources.'
plans:
- name: Gainsight Plans Pricing
  plan_count: 9
  slug: gainsight-plans-pricing
random_paper: 22
rate_limits:
- limit_count: 4
  name: Gainsight Rate Limits
  slug: gainsight-rate-limits
rules:
- authorship: generated
  effective_rule_count: 5
  extends: []
  name: Gainsight — jsonschema rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: gainsight-jsonschema-spectral-rules
- authorship: generated
  effective_rule_count: 55
  extends:
  - spectral:oas
  name: Gainsight API Rules
  rule_count: 14
  severity_counts:
    error: 8
    hint: 0
    info: 1
    warn: 5
  slug: gainsight-rules
scopes:
- name: Gainsight Scopes
  scope_count: 5
  slug: gainsight-scopes
  summary_line: 5 scopes
score:
  band: exemplar
  composite: 82.2
  coverage:
    artifact_dirs: 40
    catalog_earned: 86.8
    catalog_earned_first_party: 24.0
    catalog_gap: 28.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -0.2
  facets:
    access_clarity: 85.5
    contract_governance: 35.6
    contract_quality: 71.4
    developer_ergonomics: 70.8
    discoverability: 81.7
    operational_transparency: 92.1
  previous_composite: 82.4
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 98.0
      derived: 0
      marker_coverage: 0.0
      total: 49
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 41.4
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 50.0
screenshot: https://apis.io/screenshots/gainsight/gainsight-2026-07-25T215357.png
security:
- kind: authentication
  name: Gainsight Authentication
  slug: gainsight-authentication
  summary_line: oauth2/apiKey/http · 5 schemes
- kind: domain-security
  name: Gainsight Domain Security
  slug: gainsight-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Gainsight Vulnerability Disclosure
  slug: gainsight-vulnerability-disclosure
  summary_line: Bugcrowd · contact published
- kind: trust-center
  name: Gainsight Trust Center
  slug: gainsight-trust-center
  summary_line: SOC 2, ISO 27001, HIPAA, GDPR
skill_count: 4
skills:
- name: gainsight-cs-mcp-connect
  slug: gainsight-cs-mcp-connect
- name: gainsight-px-manage-engagement
  slug: gainsight-px-manage-engagement
- name: gainsight-px-sync-account
  slug: gainsight-px-sync-account
- name: gainsight-px-track-custom-event
  slug: gainsight-px-track-custom-event
slug: gainsight
tags:
- Customer Success
- Customer Experience
- Product Analytics
- Customer Communities
- Customer Health
- Customer Education
- Software-as-a-Service
- MCP
- Retention
- Community
website: https://www.gainsight.com/
---
