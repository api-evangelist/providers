---
access_model:
  confidence: medium
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  - security
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
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: true
    idempotency: false
    mcp_server: documented
    openapi_examples: verified
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 52.8
  scored_at: '2026-10-03'
agentic_access:
- acting_count: 161
  human_in_the_loop: 2
  name: Bigpanda Agentic Access
  operation_count: 261
  slug: bigpanda-agentic-access
  summary_line: 261 operations · 161 acting · 2 human-in-the-loop
api_count: 29
apis:
- baseURL: https://api.bigpanda.io
  baseurl_source: declared
  description: AI analysis configurations and on-demand AI analysis generation.
  name: BigPanda AI Settings API
  phrasing_intents:
  - id: create-a-new-ai-analysis-configuration
    intent: Create an AI Analysis configuration
    question: How do I set up AI Analysis to run automatically on incidents in certain environments?
  - id: retrieve-all-ai-analysis-configurations
    intent: List AI Analysis configurations
    question: Which AI Analysis configurations are set up for our incidents?
  - id: delete-an-ai-analysis-configuration
    intent: Delete an AI Analysis configuration
    question: Can I delete an AI Analysis configuration we no longer want?
  - id: retrieve-an-ai-analysis-configuration-by-id
    intent: Get an AI Analysis configuration
    question: What environments and alert tags does a specific AI Analysis configuration use?
  - id: update-an-ai-analysis-configuration
    intent: Update an AI Analysis configuration
    question: Can I turn off auto-trigger on an existing AI Analysis configuration?
  - id: generate-an-ai-analysis
    intent: Generate an AI analysis for an incident
    question: Can I ask BigPanda to generate an AI analysis for a specific incident on demand?
  phrasing_ops: 6
  slug: bigpanda-ai-settings-api
- baseURL: https://api.bigpanda.io
  baseurl_source: declared
  description: Alert filters and filter schedules, in current and v1 routes, for suppressing alerts before correlation.
  name: BigPanda Alert Filters API
  phrasing_intents:
  - id: v1-create-an-alert-filter
    intent: Create an alert filter (v1, org token)
    question: How do I create an alert filter with my org token on the v1 API?
  - id: v1-retrieve-all-alert-filters
    intent: List alert filters (v1, org token)
    question: Can I list alert filters with an organization token on the older v1 endpoint?
  - id: create-an-alert-filter
    intent: Create an alert filter (v2, user API key)
    question: How do I suppress noisy alerts with a new filter in BigPanda?
  - id: retrieve-all-alert-filters
    intent: List alert filters (v2, user API key)
    question: Which alert filters exist in my organization under the current v2 API?
  - id: v1-create-an-alert-filter-schedule
    intent: Create an alert filter schedule (v1, org token)
    question: How do I create a filter schedule with a start and end date using the org token?
  - id: v1-retrieve-all-alert-filter-schedules
    intent: List alert filter schedules (v1, org token)
    question: Can I list maintenance-style filter schedules with the v1 org token API?
  - id: create-an-alert-filter-schedule
    intent: Create an alert filter schedule (v2, user API key)
    question: How do I schedule an alert filter to run only during a maintenance window?
  - id: retrieve-all-alert-filter-schedules
    intent: List alert filter schedules (v2, user API key)
    question: What schedules control when my alert filters are applied?
  phrasing_ops: 20
  slug: bigpanda-alert-filters-api
- baseURL: https://api.bigpanda.io
  baseurl_source: declared
  description: Open Integration Hub ingestion — send raw tool payloads for normalization and processing, with 23 documented tool reference payloads.
  name: BigPanda Alert Ingestion (OIM) API
  phrasing_intents:
  - id: ingestAlert
    intent: Send an alert to a named OIM integration
    question: How do I push an alert payload into BigPanda for a specific OIM integration by its name in the URL?
  - id: postOimAppdynamicsapiV3Alerts
    intent: Send an AppDynamics alert through OIM
    question: What does a well-formed AppDynamics health rule violation look like when sent to OIM?
  - id: postOimAzureMonitorV2Alerts
    intent: Send an Azure Monitor alert through OIM
    question: What payload shape does BigPanda expect from an Azure Monitor common alert schema?
  - id: postOimMerakiAlerts
    intent: Send a Cisco Meraki alert through OIM
    question: What fields does a Cisco Meraki network alert need when forwarded to BigPanda?
  - id: postOimCloudwatchAlerts
    intent: Send an Amazon CloudWatch alert through OIM
    question: What does an Amazon CloudWatch alert payload look like for BigPanda's CloudWatch integration?
  - id: postOimCriblAlerts
    intent: Send a Cribl alert through OIM
    question: Can Cribl forward alerts into BigPanda through an existing Cribl integration?
  - id: postOimDatadogV2Alerts
    intent: Send a Datadog monitor alert through OIM
    question: What does a Datadog monitor alert look like when it's sent to BigPanda?
  - id: postOimDynatraceV2Alerts
    intent: Send a Dynatrace problem alert through OIM
    question: How are Dynatrace problem notifications formatted for BigPanda ingestion?
  phrasing_ops: 26
  slug: bigpanda-alert-ingestion-oim-api
- baseURL: https://api.bigpanda.io
  baseurl_source: declared
  description: Inbound alert ingestion and batch alert resolution — the write path monitoring tools use to push events into BigPanda.
  name: BigPanda Alerts API
  phrasing_intents:
  - id: sendAlert
    intent: Send a monitoring alert into BigPanda
    question: How do I push an alert from my own monitoring script into BigPanda?
  - id: resolve-alerts
    intent: Resolve a batch of alerts
    question: Can I set a whole list of alerts back to OK in one call?
  - id: get-destination-tags
    intent: List destination tags by most recent
    question: Which destination tags has BigPanda received most recently?
  phrasing_ops: 3
  slug: bigpanda-alerts-api
- baseURL: https://api.bigpanda.io
  baseurl_source: declared
  description: Create, read, update and revoke the User API Keys that authenticate every other call.
  name: BigPanda API Keys API
  phrasing_intents:
  - id: create-api-key
    intent: Create an API key
    question: How do I generate a new API key for an integration?
  - id: retrieve-all-api-keys
    intent: List API keys
    question: Which API keys exist in my BigPanda organization?
  - id: delete-an-api-key
    intent: Delete an API key
    question: How do I revoke an API key that may have leaked?
  - id: retrieve-an-api-key
    intent: Get an API key
    question: When was a particular API key last used?
  - id: update-an-api-key
    intent: Update an API key's name or expiry
    question: Can I set an expiration date on an existing API key?
  - id: retrieve-api-keys-for-a-service-account
    intent: List a service account's API keys
    question: Which API keys belong to a given service account?
  phrasing_ops: 6
  slug: bigpanda-api-keys-api
- baseURL: https://api.bigpanda.io
  baseurl_source: declared
  description: Search the organization audit log.
  name: BigPanda Audit API
  phrasing_intents:
  - id: getAuditLogs
    intent: Get API and user activity audit logs
    question: Can I see an audit trail of API calls and user actions in BigPanda?
  phrasing_ops: 1
  slug: bigpanda-audit-api
- baseURL: https://api.bigpanda.io
  baseurl_source: declared
  description: Send a natural-language question to Biggy and retrieve the response, synchronously or as an async job.
  name: BigPanda Biggy Query API
  phrasing_intents:
  - id: get-a-response
    intent: Fetch an async Biggy answer
    question: Where do I pick up Biggy's answer after sending an async query?
  - id: send-a-query
    intent: Ask Biggy a natural-language question
    question: Can I ask BigPanda's Biggy AI about my incidents in plain English?
  phrasing_ops: 2
  slug: bigpanda-biggy-query-api
- baseURL: https://api.bigpanda.io
  baseurl_source: declared
  description: Request and retrieve AI-powered risk ratings for ServiceNow change requests.
  name: BigPanda Change Risk API
  phrasing_intents:
  - id: request-a-risk-rating
    intent: Request a risk rating for a change
    question: How do I ask BigPanda to assess the risk of a change before we deploy it?
  - id: get-a-change
    intent: Get a change's risk rating
    question: What risk rating did BigPanda give a planned change?
  phrasing_ops: 2
  slug: bigpanda-change-risk-api
- baseURL: https://api.bigpanda.io
  baseurl_source: declared
  description: Ingest deployment and configuration changes and link them to incidents as Root Cause Changes.
  name: BigPanda Changes & Root Cause API
  phrasing_intents:
  - id: sendChange
    intent: Send a change event for correlation
    question: How do I tell BigPanda about a deployment so it can correlate alerts with it?
  phrasing_ops: 1
  slug: bigpanda-changes-api
- baseURL: https://api.bigpanda.io
  baseurl_source: declared
  description: The rules that turn alerts into incidents, including their evaluation order.
  name: BigPanda Correlation Patterns API
  phrasing_intents:
  - id: create-correlation-pattern
    intent: Create a correlation pattern
    question: How do I make BigPanda correlate alerts that share the same host within a time window?
  - id: retrieve-all-correlation-patterns
    intent: List correlation patterns
    question: Which correlation patterns group my alerts into incidents?
  - id: delete-correlation-pattern
    intent: Delete a correlation pattern
    question: How do I remove a correlation rule that's merging unrelated alerts?
  - id: retrieve-a-correlation-pattern-by-id
    intent: Get a correlation pattern
    question: What tags and time window does a specific correlation pattern use?
  - id: update-correlation-pattern
    intent: Update a correlation pattern
    question: Can I widen the time window on an existing correlation pattern?
  - id: reset-correlation-patterns-order
    intent: Reset correlation pattern order to time window
    question: Can I undo a custom rule order and go back to ordering by time window?
  - id: update-correlation-pattern-order
    intent: Set the run order of correlation patterns
    question: Can I control which correlation rule gets evaluated first?
  phrasing_ops: 7
  slug: bigpanda-correlation-patterns-api
- baseURL: https://api.bigpanda.io
  baseurl_source: declared
  description: Data connectors and their authentication.
  name: BigPanda Data Connectors API
  phrasing_intents:
  - id: add-data-connector-authentication
    intent: Get the auth setup link for a data connector
    question: Where do I finish authenticating a data connector I just created?
  - id: create-a-data-connector
    intent: Create a data connector
    question: How do I add a new data connector integration?
  - id: retrieve-all-data-connectors
    intent: List data connectors
    question: Which data connectors do I have access to in BigPanda?
  - id: delete-a-data-connector
    intent: Delete a data connector
    question: How do I remove a data connector integration I no longer use?
  - id: retrieve-a-data-connector
    intent: Get a data connector
    question: How is a specific data connector configured?
  phrasing_ops: 5
  slug: bigpanda-data-connectors-api
- baseURL: https://api.bigpanda.io
  baseurl_source: declared
  description: Versioned email-parser integration configuration, mirroring the OIM configuration lifecycle.
  name: BigPanda Email Parser Configuration API
  phrasing_intents:
  - id: diff-configuration-versions
    intent: Compare two integration configuration versions
    question: What changed between two saved versions of my parser configuration?
  - id: create-update-email-parser-configuration
    intent: Create or update an email parser configuration
    question: How do I tell BigPanda how to parse alert emails into tags?
  - id: retrieve-email-parser-configuration
    intent: Get an email parser configuration
    question: What parsing rules does my email integration currently use?
  - id: list-configuration-versions
    intent: List saved configuration versions
    question: What's the history of saved configurations for my integration?
  - id: restore-configuration-version
    intent: Restore a previous configuration version
    question: Can I roll my integration config back to an earlier saved version?
  - id: retrieve-configuration-version
    intent: Get one saved configuration version
    question: Can I view exactly what a past configuration version contained?
  phrasing_ops: 6
  slug: bigpanda-email-parser-configuration-api
- baseURL: https://api.bigpanda.io
  baseurl_source: declared
  description: BPQL-defined environments and environment groups that scope every incident operation.
  name: BigPanda Environments API
  phrasing_intents:
  - id: listEnvironments
    intent: List incident environments
    question: Which environments are set up in my BigPanda organization?
  - id: createEnvironment
    intent: Create an incident grouping environment
    question: How do I create an environment that groups incidents by a condition?
  - id: getEnvironment
    intent: Get an environment by ID (basic)
    question: Can I fetch a single environment's basic definition by its ID?
  - id: deleteEnvironment
    intent: Delete an environment by ID (basic)
    question: Is there a simple way to delete an environment by ID?
  - id: create-environment-groups
    intent: Create an environment group
    question: Can I bundle several environments into one group?
  - id: retrieve-all-environment-groups
    intent: List environment groups
    question: How are my environments organized into groups?
  - id: delete-environment
    intent: Delete an environment (user API key)
    question: How do I delete an environment with my user API key?
  - id: get-an-environment
    intent: Get an environment with roles and filter
    question: Which roles can see a particular environment and what filter does it use?
  phrasing_ops: 11
  slug: bigpanda-environments-api
- baseURL: https://api.bigpanda.io
  baseurl_source: declared
  description: Search, read, assign, comment, tag, snooze, merge, split and resolve correlated incidents.
  name: BigPanda Incidents API
  phrasing_intents:
  - id: listIncidents
    intent: List incidents in an environment
    question: Which incidents are currently open in my BigPanda environment?
  - id: getIncident
    intent: Get an incident's details
    question: What are the details of a specific incident?
  - id: create-multiple-incident-tags
    intent: Set several tags on an incident at once
    question: Can I add or update several incident tags in one request?
  - id: delete-all-incident-tags
    intent: Remove all tags from an incident
    question: Can I clear every tag off an incident in one go?
  - id: retrieve-multiple-incident-tags-from-a-single-incident
    intent: List all tags on an incident
    question: Which incident tags have been set on this incident?
  - id: create-an-incident-tag
    intent: Set a single tag value on an incident
    question: Can I set one incident tag, like priority, on a specific incident?
  - id: delete-an-incident-tag
    intent: Remove one tag from an incident
    question: Can I remove a single tag value from an incident but keep the others?
  - id: retrieve-an-incident-tag-from-a-single-incident
    intent: Get one tag's value on an incident
    question: What value does a particular tag have on this incident?
  phrasing_ops: 21
  slug: bigpanda-incidents-api
- baseURL: https://api.bigpanda.io
  baseurl_source: declared
  description: Schedule maintenance windows to suppress alerts during planned work, and stop a running window early.
  name: BigPanda Maintenance Plans API
  phrasing_intents:
  - id: listMaintenancePlans
    intent: List all maintenance plans
    question: Which maintenance plans do we have set up in BigPanda?
  - id: createMaintenancePlan
    intent: Schedule a maintenance window to suppress alerts
    question: How do I suppress alerts from certain hosts during a planned maintenance window?
  - id: maintenance-plan-v2-delete-plan
    intent: Delete a maintenance plan
    question: Can I delete a maintenance plan that was scheduled by mistake?
  - id: maintenance-plan-v2-retrieve-plan
    intent: Get a maintenance plan
    question: What condition and window does a particular maintenance plan cover?
  - id: maintenance-plan-v2-update-plan
    intent: Update a maintenance plan
    question: Can I extend the end time of a maintenance plan that's already running?
  - id: retrieve-all-plans-v2
    intent: Search and filter maintenance plans
    question: Can I search maintenance plans by text and filter them by status?
  - id: maintenance-plan-v2-stop-plan
    intent: Stop an active maintenance plan
    question: Can I end a maintenance window early once the work is done?
  phrasing_ops: 7
  slug: bigpanda-maintenance-plans-api
- baseURL: https://api.bigpanda.io
  baseurl_source: declared
  description: Add the Biggy transcription bot to a call, then list transcripts, read raw text and generate AI summaries.
  name: BigPanda Meetings & Transcripts API
  phrasing_intents:
  - id: generate-summary
    intent: Summarize a meeting transcript
    question: Can Biggy summarize a bridge call we just finished?
  - id: join-a-meeting
    intent: Invite Biggy to join and transcribe a meeting
    question: How do I get Biggy to join our incident bridge and take notes?
  - id: retrieve-transcripts
    intent: List transcribed meetings
    question: Which meetings and calls has Biggy transcribed for us?
  - id: retrieve-raw-transcript
    intent: Get the raw transcript of a call
    question: Can I read the full word-for-word transcript of a call, chat included?
  phrasing_ops: 4
  slug: bigpanda-meetings-transcripts-api
- baseURL: https://api.bigpanda.io
  baseurl_source: declared
  description: Configure Notifications Webhook v2 destinations and discover the dynamic variables a webhook template can interpolate.
  name: BigPanda Notifications & Webhooks API
  phrasing_intents:
  - id: create-a-new-webhook-v2-workflow-integration
    intent: Create a webhook v2 notification integration
    question: How do I send incident notifications to our ticketing system with a custom webhook payload?
  - id: retrieve-all-existing-webhook-v2-configurations
    intent: List webhook v2 notification integrations
    question: Which outbound webhook v2 integrations are sending BigPanda incidents to other tools?
  - id: deleteResourcesV21IntegrationsByAppKey
    intent: Delete a webhook v2 integration
    question: Do I need the app key rather than the integration ID to delete a webhook v2 integration?
  - id: retrieve-an-existing-webhook-v2-configuration
    intent: Get a webhook v2 integration's configuration
    question: What triggers and payload does a specific webhook v2 integration use?
  - id: update-an-existing-webhook-v2-workflow-integration
    intent: Update a webhook v2 integration's workflow
    question: Can I change the payload or headers of an existing webhook v2 integration?
  - id: retrieve-available-dynamic-variables
    intent: List dynamic variables for webhook templates
    question: Which incident and alert fields can I use as variables in a webhook payload?
  phrasing_ops: 6
  slug: bigpanda-notifications-api
- baseURL: https://api.bigpanda.io
  baseurl_source: declared
  description: Versioned Open Integration Hub configuration with list, retrieve, diff and restore — the only versioned object in the BigPanda surface.
  name: BigPanda OIM Configuration API
  phrasing_intents:
  - id: create-update-oim-configuration-v2
    intent: Create or update an OIM integration configuration
    question: How do I define how a custom inbound alert payload maps to BigPanda tags?
  - id: retrieve-oim-configuration-v2
    intent: Get an OIM integration configuration
    question: What parsing rules does my custom Open Integration Manager integration use?
  - id: postConfigurationsAlertsOimByAppKeyPreprocessor
    intent: Add preprocessor functions to an OIM config
    question: Can I run URL shortening on incoming payloads before OIM parsing rules apply?
  phrasing_ops: 3
  slug: bigpanda-oim-configuration-api
- baseURL: https://api.bigpanda.io
  baseurl_source: declared
  description: Troubleshooting logs and multi-context report generation.
  name: BigPanda Reporting API
  phrasing_intents:
  - id: create-a-multi-context-report
    intent: Generate a report from transcripts and tickets
    question: Can I generate a post-incident report from meeting transcripts and ServiceNow records together?
  - id: get-integration-alerts
    intent: See raw alerts an integration recently sent
    question: What exactly did BigPanda receive from an integration before enrichment?
  - id: retrieve-all-troubleshooting-logs
    intent: Search troubleshooting logs
    question: Are there error logs explaining why an enrichment or integration misbehaved?
  phrasing_ops: 3
  slug: bigpanda-reporting-api
- baseURL: https://api.bigpanda.io
  baseurl_source: declared
  description: Roles, role membership and the permission catalog that decides what a User API Key can do.
  name: BigPanda Roles & Permissions API
  phrasing_intents:
  - id: postRoleUsers
    intent: Add users to a role in bulk
    question: Can I add a whole team of users to a role in one call when onboarding?
  - id: deleteRoleUsers
    intent: Remove users from a role
    question: Can I take several users out of a role at once?
  - id: create-a-role
    intent: Create a role
    question: How do I create a new role with a specific set of permissions?
  - id: retrieve-all-roles
    intent: List roles with sorting and paging (v2.1)
    question: Can I page through my roles sorted by a field using the v2.1 Roles API?
  - id: delete-a-role
    intent: Delete a role
    question: How do I delete a role we no longer use?
  - id: retrieve-role-by-id
    intent: Get a role by ID (v2.1)
    question: Can I fetch one role's users and permissions from the v2.1 Roles API?
  - id: updateRoleById
    intent: Partially update a role in place
    question: Can I tweak just one property of a role without resending the whole definition?
  - id: update-a-role
    intent: Replace a role's name, users and permissions
    question: Do I have to send the full list of users and permissions every time I replace a role?
  phrasing_ops: 12
  slug: bigpanda-roles-permissions-api
- baseURL: https://api.bigpanda.io
  baseurl_source: declared
  description: Machine identities and the API keys attached to them.
  name: BigPanda Service Accounts API
  phrasing_intents:
  - id: createServiceAccount
    intent: Create a service account
    question: How do I create a service account for an automation to use?
  - id: getAllServiceAccounts
    intent: List service accounts
    question: Which service accounts exist in our BigPanda organization?
  - id: deleteServiceAccount
    intent: Delete a service account
    question: Can I permanently delete a service account we no longer need?
  - id: getServiceAccountById
    intent: Get a service account
    question: What are the details of a particular service account?
  - id: updateServiceAccount
    intent: Update a service account
    question: Can I change the details of an existing service account?
  phrasing_ops: 5
  slug: bigpanda-service-accounts-api
- baseURL: https://api.bigpanda.io
  baseurl_source: declared
  description: Service and infrastructure topology used to relate alerts across systems.
  name: BigPanda Topology API
  phrasing_intents:
  - id: create-topology
    intent: Create the organization's topology model
    question: How do I describe how my services and hosts connect to each other?
  - id: retrieve-all-topologies
    intent: List topology models
    question: Does my organization already have a topology model defined?
  - id: delete-topology
    intent: Delete the topology model
    question: How do I remove my organization's topology model entirely?
  - id: retrieve-topology
    intent: Get a topology model
    question: What links are in my current topology model?
  - id: update-topology
    intent: Update the topology model's links
    question: Can I replace the service dependency links in my topology?
  phrasing_ops: 5
  slug: bigpanda-topology-api
- baseURL: https://api.bigpanda.io
  baseurl_source: declared
  description: User management plus a standards-based SCIM 2.0 provisioning surface for Users and Groups.
  name: BigPanda Users & SCIM API
  phrasing_intents:
  - id: postUserActivate
    intent: Activate an invited user account
    question: How does an invited user finish the invitation flow and become active?
  - id: changeUserPassword
    intent: Change a user's password
    question: Can an admin reset someone's password in BigPanda through the API?
  - id: createGroupSCIM
    intent: Create a group via SCIM
    question: Can my identity provider create a new group through SCIM provisioning?
  - id: getGroupsBySCIMQueryParams
    intent: List groups via SCIM
    question: Which groups has my identity provider provisioned over SCIM?
  - id: createUserSCIM
    intent: Provision a user via SCIM
    question: Can I provision a new user from my identity provider with SCIM?
  - id: getUsersBySCIMQueryParams
    intent: List users via SCIM
    question: Which users are provisioned through SCIM right now?
  - id: deleteGroupByIdSCIM
    intent: Delete a SCIM group
    question: How do I deprovision a group that was created through SCIM?
  - id: getGroupByIdSCIM
    intent: Get a SCIM group by ID
    question: How can I see the details and members of one SCIM group?
  phrasing_ops: 26
  slug: bigpanda-users-api
- baseURL: https://api.bigpanda.io
  baseurl_source: declared
  description: The Agents (MCP & A2A) API from BigPanda — 3 operation(s) for agents (mcp & a2a).
  name: BigPanda Agents (MCP & A2A) API
  phrasing_intents:
  - id: retrieve-agent-card
    intent: Get Biggy's A2A agent card
    question: What skills and input/output modes does the Biggy agent advertise?
  - id: use-action-plans-as-mcp
    intent: Call Biggy action plans over remote MCP
    question: Can I use BigPanda's Biggy action plans as tools from my own MCP client?
  - id: use-the-a2a-protocol
    intent: Message Biggy's agent via A2A
    question: How can my own AI agent send messages to Biggy using A2A?
  phrasing_ops: 3
  slug: bigpanda-agents-mcp-a2a-api
- baseURL: https://api.bigpanda.io
  baseurl_source: declared
  description: The Alert Tags & Enrichment API from BigPanda — 22 operation(s) for alert tags & enrichment.
  name: BigPanda Alert Tags & Enrichment API
  phrasing_intents:
  - id: check-status-of-upload-job
    intent: Check an Enrichment V2 mapping table upload job
    question: Has my Enrichment V2 mapping table upload finished processing?
  - id: postResourcesAlertEnricherSchemas
    intent: Create an advanced mapping schema
    question: How do I create an advanced mapping schema in the Alert Enricher?
  - id: getResourcesAlertEnricherSchemas
    intent: List advanced mapping schemas
    question: Which advanced mapping enrichment schemas does the Alert Enricher have set up?
  - id: create-enrichment-1
    intent: Create an Enrichment V2 enrichment item
    question: Can I add a new enrichment item with the older Enrichment V2 API?
  - id: create-tag
    intent: Create an alert tag
    question: How do I create a new alert tag with its own enrichments?
  - id: retrieve-all-tags
    intent: List alert tags (v2.1)
    question: What alert tags exist in the v2.1 enrichments config?
  - id: create-tag-rule
    intent: Add enrichment items to an existing alert tag
    question: Can I add a composition enrichment to an alert tag I already created?
  - id: delete-tag-rule
    intent: Delete enrichment items from an alert tag
    question: How do I remove a composition or extraction enrichment from an alert tag?
  phrasing_ops: 45
  slug: bigpanda-alert-tags-enrichment-api
- baseURL: https://api.bigpanda.io
  baseurl_source: declared
  description: The Audit Log API from BigPanda — 2 operation(s) for audit log.
  name: BigPanda Audit Log API
  phrasing_intents:
  - id: get-an-audit-log
    intent: Search audit log entries
    question: Who deleted configuration objects in my BigPanda org last week?
  - id: get-audit-log-metadata
    intent: Get valid audit log filter values
    question: Which entity types and change types can I filter the audit log by?
  phrasing_ops: 2
  slug: bigpanda-audit-log-api
- baseURL: https://api.bigpanda.io
  baseurl_source: declared
  description: The Changes & Root Cause API from BigPanda — 4 operation(s) for changes & root cause.
  name: BigPanda Changes & Root Cause API
  phrasing_intents:
  - id: create-related-change-rcc
    intent: Link a change to an incident as a root cause
    question: How do I mark a change as the likely cause of an incident?
  - id: retrieve-rcc-relations
    intent: List root cause change relations
    question: Which changes have been linked as possible root causes of an incident?
  - id: retrieve-all-changes
    intent: Search change records in a time frame
    question: What changes went out in the hour before an incident started?
  - id: retrieve-a-change
    intent: Get a change record
    question: What are the details of a specific change record?
  - id: retrieve-an-rcc-change
    intent: Get a root cause change relation
    question: What certainty and comment are on a specific RCC relation?
  - id: update-related-change-rcc
    intent: Update a root cause change relation
    question: Can I raise or lower the match certainty on a linked root cause change?
  phrasing_ops: 6
  slug: bigpanda-changes-root-cause-api
- baseURL: https://api.bigpanda.io
  baseurl_source: declared
  description: The Major Incident Management API from BigPanda — 7 operation(s) for major incident management.
  name: BigPanda Major Incident Management API
  phrasing_intents:
  - id: postMimExecutionsByExecutionIdCancel
    intent: Cancel a major incident execution
    question: How do I call off a major incident workflow that was started by mistake?
  - id: postMimExecute
    intent: Start a major incident workflow from a template
    question: How do I kick off a major incident with channels and automated actions from a template?
  - id: getMimTemplates
    intent: List major incident templates
    question: Which major incident templates are configured for my organization?
  - id: postMimExecutionsByExecutionIdResolve
    intent: Resolve a major incident execution
    question: How do I close out a major incident so final reports run and channels get archived?
  - id: getMimExecutionsByExecutionId
    intent: Get a major incident execution's details
    question: Which automated actions have finished for a running major incident?
  - id: getMimExecutions
    intent: List major incident executions
    question: Which major incidents are active right now?
  - id: getMimTemplatesByTemplateId
    intent: Get a major incident template's actions
    question: Which actions in a MIM template require approval before they run?
  phrasing_ops: 7
  slug: bigpanda-major-incident-management-api
- baseURL: https://api.bigpanda.io
  baseurl_source: declared
  description: The SSO & JIT Provisioning API from BigPanda — 7 operation(s) for sso & jit provisioning.
  name: BigPanda SSO & JIT Provisioning API
  phrasing_intents:
  - id: postSsoConfig
    intent: Configure SSO for an identity provider
    question: How do I set up single sign-on to BigPanda with our identity provider?
  - id: deleteJitDomain
    intent: Delete a just-in-time domain rule
    question: Can I stop an email domain from auto-provisioning accounts on first SSO login?
  - id: deleteJitRole
    intent: Delete a just-in-time role rule
    question: Can I remove a rule that hands out a role automatically on first SSO login?
  - id: getSamlDebug
    intent: Get SAML debug information
    question: Why are our SAML assertions failing during SSO setup?
  - id: getSsoConfig
    intent: Get the organization's SSO configuration
    question: Is SSO turned on for our BigPanda organization, and with which provider?
  - id: putSsoConfig
    intent: Enable, disable or switch SSO
    question: Can I disable SSO for the organization temporarily?
  - id: createJitDomain
    intent: Allow a domain to auto-provision accounts
    question: How do I let everyone on our email domain get an account automatically at first SSO login?
  - id: getJitDomains
    intent: List just-in-time domain rules
    question: Which email domains are allowed to auto-provision accounts on first SSO login?
  phrasing_ops: 10
  slug: bigpanda-sso-jit-provisioning-api
artifact_total: 111
asyncapis:
- description: ''
  name: Bigpanda Webhooks
  slug: bigpanda-webhooks
collections:
- collection_type: postman
  name: BigPanda Alerts API
  slug: postman-bigpanda-alerts-api
- collection_type: postman
  name: BigPanda Alerts Audit API
  slug: postman-bigpanda-audit-api
- collection_type: postman
  name: BigPanda Alerts Changes API
  slug: postman-bigpanda-changes-api
- collection_type: postman
  name: BigPanda Alerts Environments API
  slug: postman-bigpanda-environments-api
- collection_type: postman
  name: BigPanda Alerts Incidents API
  slug: postman-bigpanda-incidents-api
- collection_type: postman
  name: BigPanda Alerts Maintenance Plans API
  slug: postman-bigpanda-maintenance-plans-api
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: BigPanda Alerts API
  slug: open-bigpanda-alerts-api
- collection_type: open
  name: BigPanda Alerts Audit API
  slug: open-bigpanda-audit-api
- collection_type: open
  name: BigPanda Alerts Changes API
  slug: open-bigpanda-changes-api
- collection_type: open
  name: BigPanda Alerts Environments API
  slug: open-bigpanda-environments-api
- collection_type: open
  name: BigPanda Alerts Incidents API
  slug: open-bigpanda-incidents-api
- collection_type: open
  name: BigPanda Alerts Maintenance Plans API
  slug: open-bigpanda-maintenance-plans-api
- collection_type: open
  name: BigPanda API
  slug: open-bigpanda
common:
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/bigpanda/refs/heads/main/overlays/bigpanda-agents-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/bigpanda-agents-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/bigpanda/refs/heads/main/overlays/bigpanda-alert-enrichment-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/bigpanda-alert-enrichment-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/bigpanda/refs/heads/main/overlays/bigpanda-mim-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/bigpanda-mim-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/bigpanda/refs/heads/main/overlays/bigpanda-sso-provisioning-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/bigpanda-sso-provisioning-overlay.yaml
- group: company
  title: ''
  type: Website
  url: https://www.bigpanda.io/
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/bigpanda/refs/heads/main/agentic-access/bigpanda-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/bigpanda-agentic-access.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/bigpanda/refs/heads/main/security/bigpanda-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/bigpanda-trust-center.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/bigpanda/refs/heads/main/security/bigpanda-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/bigpanda-domain-security.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/bigpanda/refs/heads/main/authentication/bigpanda-authentication.yml
  title: ''
  type: Authentication
  url: authentication/bigpanda-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/bigpandaio
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/bigpanda
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/bigpanda/overview
- group: operate
  title: ''
  type: StatusPage
  url: https://status.bigpanda.io/
- group: design
  title: ''
  type: SpectralRules
  url: https://raw.githubusercontent.com/api-evangelist/bigpanda/refs/heads/main/rules/bigpanda-spectral-rules.yml
- group: design
  title: ''
  type: Vocabulary
  url: https://raw.githubusercontent.com/api-evangelist/bigpanda/refs/heads/main/vocabulary/bigpanda-vocabulary.yaml
- group: start
  title: ''
  type: Portal
  url: https://api-docs.bigpanda.io/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://api-docs.bigpanda.io/
- group: docs
  title: ''
  type: APIReference
  url: https://api-docs.bigpanda.io/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.bigpanda.io/docs/get-started
- group: start
  title: ''
  type: GettingStarted
  url: https://api-docs.bigpanda.io/get-started
- group: operate
  title: ''
  type: ChangeLog
  url: https://docs.bigpanda.io/docs/release-notes
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/bigpanda/refs/heads/main/changelog/bigpanda-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/bigpanda-changelog.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/bigpanda/refs/heads/main/lifecycle/bigpanda-lifecycle.yml
  title: ''
  type: Deprecation
  url: lifecycle/bigpanda-lifecycle.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/bigpanda/refs/heads/main/lifecycle/bigpanda-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/bigpanda-lifecycle.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/bigpanda/refs/heads/main/conventions/bigpanda-conventions.yml
  title: ''
  type: Conventions
  url: conventions/bigpanda-conventions.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/bigpanda/refs/heads/main/conformance/bigpanda-conformance.yml
  title: ''
  type: Conformance
  url: conformance/bigpanda-conformance.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/bigpanda/refs/heads/main/security/bigpanda-trust-center.yml
  title: ''
  type: Compliance
  url: security/bigpanda-trust-center.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/bigpanda/refs/heads/main/errors/bigpanda-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/bigpanda-problem-types.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/bigpanda/refs/heads/main/scopes/bigpanda-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/bigpanda-scopes.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/bigpanda/refs/heads/main/packages/bigpanda-packages.yml
  title: ''
  type: Packages
  url: packages/bigpanda-packages.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/bigpanda/refs/heads/main/well-known/bigpanda-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/bigpanda-well-known.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/bigpanda/refs/heads/main/mcp/bigpanda-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/bigpanda-mcp.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/bigpanda/refs/heads/main/mcp/bigpanda-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/bigpanda-tool-crosswalk.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/bigpanda/refs/heads/main/asyncapi/bigpanda-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/bigpanda-webhooks.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/bigpanda/refs/heads/main/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/bigpanda/refs/heads/main/data-model/bigpanda-data-model.yml
  title: ''
  type: DataModel
  url: data-model/bigpanda-data-model.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/bigpanda/refs/heads/main/plans/bigpanda-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/bigpanda-plans-pricing.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/bigpanda/refs/heads/main/rate-limits/bigpanda-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/bigpanda-rate-limits.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/bigpanda/refs/heads/main/finops/bigpanda-finops.yml
  title: ''
  type: FinOps
  url: finops/bigpanda-finops.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/bigpanda/refs/heads/main/llms/bigpanda-api-reference-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/bigpanda-api-reference-llms.txt
- group: agent
  title: ''
  type: LlmsText
  url: https://api-docs.bigpanda.io/llms.txt
- group: commercial
  title: ''
  type: Pricing
  url: https://www.bigpanda.io/pricing/
- group: start
  title: ''
  type: SignUp
  url: https://www.bigpanda.io/demo/
- group: start
  title: ''
  type: Login
  url: https://login.bigpanda.io/
- group: operate
  title: ''
  type: Support
  url: https://support.bigpanda.io/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.bigpanda.io/terms-of-service/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.bigpanda.io/privacy-notice/
- group: company
  title: ''
  type: Blog
  url: https://www.bigpanda.io/blog/
- group: company
  title: ''
  type: BlogRSS
  url: https://www.bigpanda.io/feed/
created: '2025-01-08'
description: 'BigPanda is an agentic IT operations (AIOps) platform that ingests alerts from monitoring and observability tools, correlates them into a small number of actionable incidents, links those incidents to the deployment and configuration changes that caused them, and increasingly acts on them through AI agents. Its public API is large and current: 263 operations across 165 paths, published as OpenAPI 3.0.1 on BigPanda''s own API reference, covering alert ingestion and enrichment, correlation patterns, incidents, environments, changes and root cause, maintenance plans, topology, outbound webhooks, SCIM 2.0 user provisioning, SSO, roles and API keys, plus a Biggy assistant surface with a remote Model Context Protocol server and an A2A agent endpoint.'
examples:
- key_count: 6
  name: Bigpanda Alert Request Example
  slug: bigpanda-alert-request-example
- key_count: 2
  name: Bigpanda Alert Response Example
  slug: bigpanda-alert-response-example
- key_count: 4
  name: Bigpanda Audit Log Entry Example
  slug: bigpanda-audit-log-entry-example
- key_count: 1
  name: Bigpanda Audit Logs Response Example
  slug: bigpanda-audit-logs-response-example
- key_count: 5
  name: Bigpanda Change Request Example
  slug: bigpanda-change-request-example
- key_count: 2
  name: Bigpanda Change Response Example
  slug: bigpanda-change-response-example
- key_count: 4
  name: Bigpanda Environment Example
  slug: bigpanda-environment-example
- key_count: 3
  name: Bigpanda Environment Request Example
  slug: bigpanda-environment-request-example
- key_count: 1
  name: Bigpanda Environments Response Example
  slug: bigpanda-environments-response-example
- key_count: 6
  name: Bigpanda Incident Example
  slug: bigpanda-incident-example
- key_count: 1
  name: Bigpanda Incidents Response Example
  slug: bigpanda-incidents-response-example
- key_count: 5
  name: Bigpanda Maintenance Plan Example
  slug: bigpanda-maintenance-plan-example
- key_count: 4
  name: Bigpanda Maintenance Plan Request Example
  slug: bigpanda-maintenance-plan-request-example
- key_count: 1
  name: Bigpanda Maintenance Plans Response Example
  slug: bigpanda-maintenance-plans-response-example
features:
- description: ML-powered correlation of alerts from 200+ monitoring tools into actionable incidents.
  name: AI Alert Correlation
- description: Triage, acknowledge, and resolve correlated incidents with full audit trail.
  name: Incident Management
- description: Automatically identify root causes by correlating alerts with change events.
  name: Root Cause Analysis
- description: Schedule maintenance windows to suppress expected alerts during planned work.
  name: Maintenance Plans
- description: Ingest deployment and config changes to correlate with alert spikes.
  name: Change Correlation
- description: Define DSL-based environments to group incidents by source, severity, or host.
  name: Environments
- description: Enrich alerts with contextual tags from CMDB and other data sources.
  name: Enrichments
- description: Automate incident response workflows with AI-driven insights and routing.
  name: AIOps Automation
finops:
- name: Bigpanda Finops
  service_category: API
  slug: bigpanda-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/bigpanda.png
json_schemas:
- name: AlertRequest
  property_count: 6
  slug: bigpanda-alert-request
- name: AlertResponse
  property_count: 2
  slug: bigpanda-alert-response
- name: AuditLogEntry
  property_count: 4
  slug: bigpanda-audit-log-entry
- name: AuditLogsResponse
  property_count: 1
  slug: bigpanda-audit-logs-response
- name: ChangeRequest
  property_count: 5
  slug: bigpanda-change-request
- name: ChangeResponse
  property_count: 2
  slug: bigpanda-change-response
- name: EnvironmentRequest
  property_count: 3
  slug: bigpanda-environment-request
- name: Environment
  property_count: 4
  slug: bigpanda-environment
- name: EnvironmentsResponse
  property_count: 1
  slug: bigpanda-environments-response
- name: Incident
  property_count: 6
  slug: bigpanda-incident
- name: IncidentsResponse
  property_count: 1
  slug: bigpanda-incidents-response
- name: MaintenancePlanRequest
  property_count: 4
  slug: bigpanda-maintenance-plan-request
- name: MaintenancePlan
  property_count: 5
  slug: bigpanda-maintenance-plan
- name: MaintenancePlansResponse
  property_count: 1
  slug: bigpanda-maintenance-plans-response
json_structures:
- name: Bigpanda Alert Request Structure
  property_count: 6
  slug: bigpanda-alert-request-structure
- name: Bigpanda Alert Response Structure
  property_count: 2
  slug: bigpanda-alert-response-structure
- name: Bigpanda Audit Log Entry Structure
  property_count: 4
  slug: bigpanda-audit-log-entry-structure
- name: Bigpanda Audit Logs Response Structure
  property_count: 1
  slug: bigpanda-audit-logs-response-structure
- name: Bigpanda Change Request Structure
  property_count: 5
  slug: bigpanda-change-request-structure
- name: Bigpanda Change Response Structure
  property_count: 2
  slug: bigpanda-change-response-structure
- name: Bigpanda Environment Request Structure
  property_count: 3
  slug: bigpanda-environment-request-structure
- name: Bigpanda Environment Structure
  property_count: 4
  slug: bigpanda-environment-structure
- name: Bigpanda Environments Response Structure
  property_count: 1
  slug: bigpanda-environments-response-structure
- name: Bigpanda Incident Structure
  property_count: 6
  slug: bigpanda-incident-structure
- name: Bigpanda Incidents Response Structure
  property_count: 1
  slug: bigpanda-incidents-response-structure
- name: Bigpanda Maintenance Plan Request Structure
  property_count: 4
  slug: bigpanda-maintenance-plan-request-structure
- name: Bigpanda Maintenance Plan Structure
  property_count: 5
  slug: bigpanda-maintenance-plan-structure
- name: Bigpanda Maintenance Plans Response Structure
  property_count: 1
  slug: bigpanda-maintenance-plans-response-structure
jsonld:
- class_count: 6
  name: Bigpanda Context
  property_count: 19
  slug: bigpanda-context
layout: provider
mcp_servers:
- description: 'BigPanda ships two distinct remote Model Context Protocol surfaces. The product one is the Biggy action-plan server at https://api.biggy.io/mcp, documented in BigPanda''s own API reference: a single st'
  name: BigPanda MCP Server
  slug: bigpanda-mcp-server
modified: '2026-09-04'
name: BigPanda
nav: Providers
network: true
overview: 'BigPanda publishes 29 APIs on the [APIs.io](https://apis.io/) network, including AI Settings API, Alert Filters API, Alert Ingestion (OIM) API, and 26 more. Tagged areas include Incidents, Monitoring, Platform, AIOps, and IT Operations.


  The BigPanda catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 2 Spectral governance rulesets.


  BigPanda''s developer surface includes authentication, developer portal, API reference, documentation, getting-started guide, changelog, pricing, and 42 more developer resources.'
plans:
- name: Bigpanda Plans Pricing
  plan_count: 0
  slug: bigpanda-plans-pricing
random_paper: 8
rate_limits:
- limit_count: 5
  name: Bigpanda Rate Limits
  slug: bigpanda-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: BigPanda API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: bigpanda-jsonschema-spectral-rules
- effective_rule_count: 70
  extends:
  - spectral:oas
  name: BigPanda API Rules
  rule_count: 29
  severity_counts:
    error: 8
    hint: 0
    info: 0
    warn: 21
  slug: bigpanda-spectral-rules
scopes:
- name: Bigpanda Scopes
  scope_count: 0
  slug: bigpanda-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: exemplar
  composite: 71.8
  coverage:
    artifact_dirs: 32
    catalog_earned: 75.0
    catalog_earned_first_party: 12.0
    catalog_gap: 40.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 68.4
    contract_governance: 45.5
    contract_quality: 67.1
    developer_ergonomics: 55.4
    discoverability: 80.0
    operational_transparency: 81.6
  previous_composite: 71.8
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 3
      marker_coverage: 86.7
      total: 30
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 39.2
  schema_version: 0.23.0
  scored_at: '2026-10-03'
  trend: flat
  upsert:
    applies: true
    score: 33.3
screenshot: https://raw.githubusercontent.com/api-evangelist/bigpanda/refs/heads/main/screenshots/bigpanda-2026-06-20T173234.png
security:
- kind: authentication
  name: Bigpanda Authentication
  slug: bigpanda-authentication
  summary_line: apiKey/http · 2 schemes
- kind: domain-security
  name: Bigpanda Domain Security
  slug: bigpanda-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Bigpanda Trust Center
  slug: bigpanda-trust-center
  summary_line: SOC 2, ISO 27001
slug: bigpanda
tags:
- Incidents
- Monitoring
- Platform
- AIOps
- IT Operations
- Alerts
- Incident Management
- Observability
- Agents
- MCP
use_cases:
- description: Reduce alert fatigue by correlating thousands of alerts into a handful of incidents.
  name: Alert Noise Reduction
- description: Automatically link deployment changes to alert spikes for faster root cause identification.
  name: Change Impact Analysis
- description: Route correlated incidents to the right on-call team with full context.
  name: On-Call Automation
- description: Suppress alerts during planned maintenance to prevent false incident creation.
  name: Maintenance Scheduling
- description: Automatically create and update tickets in ServiceNow or Jira from correlated incidents.
  name: ITSM Integration
website: https://www.bigpanda.io/
---
