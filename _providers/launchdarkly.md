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
    dry_run_mode: true
    dynamic_client_registration: true
    error_semantics: verified
    event_surface_described: derived
    idempotency: false
    mcp_server: verified
    mcp_tool_quality: na
    openapi_examples: partial
    operation_distinctiveness: false
    pagination_ratio: partial
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 60.6
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 25
  human_in_the_loop: 0
  name: Launchdarkly Agentic Access
  operation_count: 58
  slug: launchdarkly-agentic-access
  summary_line: 58 operations · 25 acting
api_count: 4
apis:
- baseURL: https://app.launchdarkly.com/api/v2
  baseurl_source: declared
  description: The LaunchDarkly Webhooks API allows developers to build custom integrations that subscribe to activity events within LaunchDarkly. When actions occur such as flag changes, project creation, or enviro
  name: LaunchDarkly Webhooks API
  slug: webhooks-api
- baseURL: https://app.launchdarkly.com/api/v2
  baseurl_source: declared
  description: Create and manage personal and service access tokens used to authenticate API requests.
  name: launchdarkly Access Tokens API
  phrasing_intents:
  - id: listAccessTokens
    intent: List personal and service access tokens
    question: Which API access tokens exist in my LaunchDarkly account?
  - id: createAccessToken
    intent: Create an API access token
    question: How do I generate a new API access token?
  phrasing_ops: 2
  slug: launchdarkly-access-tokens-api
- baseURL: https://app.launchdarkly.com/api/v2
  baseurl_source: declared
  description: Manage team members, invitations, and member roles within a LaunchDarkly account.
  name: launchdarkly Account Members API
  phrasing_intents:
  - id: listMembers
    intent: List account members
    question: Who are the members of our LaunchDarkly account?
  - id: inviteMember
    intent: Invite a new member to the account
    question: How do I invite a teammate to join our account?
  phrasing_ops: 2
  slug: launchdarkly-account-members-api
- baseURL: https://app.launchdarkly.com/api/v2
  baseurl_source: declared
  description: Manage approval requests and workflows for flag changes that require review before deployment.
  name: launchdarkly Approvals API
  phrasing_intents:
  - id: listApprovalRequests
    intent: List approval requests for a flag
    question: Which approval requests are open on this feature flag?
  - id: createApprovalRequest
    intent: Request approval for a flag change
    question: How do I ask for approval before changing a flag in production?
  phrasing_ops: 2
  slug: launchdarkly-approvals-api
- baseURL: https://app.launchdarkly.com/api/v2
  baseurl_source: declared
  description: Access the change history of all modifications made to resources in the LaunchDarkly account.
  name: launchdarkly Audit Log API
  phrasing_intents:
  - id: listAuditLogEntries
    intent: Search the account audit log
    question: Who changed what in our LaunchDarkly account last week?
  - id: getAuditlogByAuditLogId
    intent: Get one audit log entry
    question: How can I see the full details of a single audit log entry?
  phrasing_ops: 2
  slug: launchdarkly-audit-log-api
- baseURL: https://app.launchdarkly.com/api/v2
  baseurl_source: declared
  description: Flag evaluation endpoints for client-side and mobile SDKs using environment IDs or mobile keys for authentication.
  name: launchdarkly Client-Side Evaluation API
  phrasing_intents:
  - id: evaluateAllFlagsClientSide
    intent: Evaluate client-side flags for a context
    question: How do I get all client-side flag values for a user from the browser?
  phrasing_ops: 1
  slug: launchdarkly-client-side-evaluation-api
- baseURL: https://app.launchdarkly.com/api/v2
  baseurl_source: declared
  description: Server-Sent Events streaming endpoints for client-side and mobile SDKs to receive real-time flag updates.
  name: launchdarkly Client-Side Streaming API
  phrasing_intents:
  - id: streamClientSideEval
    intent: Stream evaluated flags to a client
    question: How do I open a live stream of flag values for a browser client?
  phrasing_ops: 1
  slug: launchdarkly-client-side-streaming-api
- baseURL: https://app.launchdarkly.com/api/v2
  baseurl_source: declared
  description: View code references that show where feature flags are used in your codebase.
  name: launchdarkly Code References API
  phrasing_intents:
  - id: listCodeReferenceRepositories
    intent: List repositories scanned for code references
    question: Which repositories are connected for flag code reference scanning?
  phrasing_ops: 1
  slug: launchdarkly-code-references-api
- baseURL: https://app.launchdarkly.com/api/v2
  baseurl_source: declared
  description: Define custom roles with fine-grained permissions using resource specifiers and actions.
  name: launchdarkly Custom Roles API
  phrasing_intents:
  - id: listCustomRoles
    intent: List custom roles
    question: What custom roles are defined in our account?
  - id: createCustomRole
    intent: Create a custom role with a policy
    question: How do I create a custom role with specific permissions?
  phrasing_ops: 2
  slug: launchdarkly-custom-roles-api
- baseURL: https://app.launchdarkly.com/api/v2
  baseurl_source: declared
  description: Manage environments within projects such as production, staging, and development.
  name: launchdarkly Environments API
  phrasing_intents:
  - id: listEnvironments
    intent: List a project's environments
    question: What environments exist in this project?
  - id: createEnvironment
    intent: Create an environment in a project
    question: How do I add a new staging environment to a project?
  - id: getProjectsByProjectKeyEnvironmentsByEnvironmentKey
    intent: Get one environment's details
    question: How do I look up the settings of a specific environment?
  - id: patchProjectsByProjectKeyEnvironmentsByEnvironmentKey
    intent: Update an environment's settings
    question: How do I rename an environment or change its color?
  - id: deleteProjectsByProjectKeyEnvironmentsByEnvironmentKey
    intent: Delete an environment
    question: How do I permanently remove an environment from a project?
  phrasing_ops: 5
  slug: launchdarkly-environments-api
- baseURL: https://app.launchdarkly.com/api/v2
  baseurl_source: declared
  description: Create and manage experiments to measure the impact of feature flag variations on metrics.
  name: launchdarkly Experiments API
  phrasing_intents:
  - id: listExperiments
    intent: List experiments in an environment
    question: What experiments are running in this project's production environment?
  - id: postProjectsByProjectKeyEnvironmentsByEnvironmentKeyExperiments
    intent: Create an experiment
    question: How do I set up a new experiment in LaunchDarkly?
  phrasing_ops: 2
  slug: launchdarkly-experiments-api
- baseURL: https://app.launchdarkly.com/api/v2
  baseurl_source: declared
  description: Create, update, and manage feature flags and their targeting rules across projects and environments.
  name: launchdarkly Feature Flags API
  phrasing_intents:
  - id: listFeatureFlags
    intent: List a project's feature flags
    question: Which feature flags exist in this project?
  - id: createFeatureFlag
    intent: Create a feature flag
    question: How do I create a new feature flag with custom variations?
  - id: getFlagsByProjectKeyByFlagKey
    intent: Get a feature flag and its targeting
    question: How do I see a flag's targeting rules in each environment?
  - id: patchFlagsByProjectKeyByFlagKey
    intent: Update a flag's targeting or settings
    question: How do I turn a flag on or change its targeting rules?
  - id: deleteFlagsByProjectKeyByFlagKey
    intent: Delete a feature flag
    question: How do I permanently delete a flag we no longer use?
  phrasing_ops: 5
  slug: launchdarkly-feature-flags-api
- baseURL: https://app.launchdarkly.com/api/v2
  baseurl_source: declared
  description: Create triggers that allow external services to toggle feature flags via unique webhook URLs.
  name: launchdarkly Flag Triggers API
  phrasing_intents:
  - id: listFlagTriggers
    intent: List triggers on a flag
    question: What triggers are set up to toggle this flag?
  - id: createFlagTrigger
    intent: Create a trigger URL that toggles a flag
    question: How can a monitoring tool turn a flag off automatically?
  phrasing_ops: 2
  slug: launchdarkly-flag-triggers-api
- baseURL: https://app.launchdarkly.com/api/v2
  baseurl_source: declared
  description: Manage integrations that subscribe to audit log events and forward them to external tools.
  name: launchdarkly Integration Audit Log Subscriptions API
  phrasing_intents:
  - id: listIntegrationSubscriptions
    intent: List an integration's audit log subscriptions
    question: Which audit log subscriptions exist for a given integration?
  phrasing_ops: 1
  slug: launchdarkly-integration-audit-log-subscriptions-api
- baseURL: https://app.launchdarkly.com/api/v2
  baseurl_source: declared
  description: Define and manage metrics used to measure experiment outcomes and feature flag impact.
  name: launchdarkly Metrics API
  phrasing_intents:
  - id: listMetrics
    intent: List a project's metrics
    question: What metrics are defined in this project?
  - id: createMetric
    intent: Create a metric for experiments
    question: How do I create a click metric to measure an experiment?
  phrasing_ops: 2
  slug: launchdarkly-metrics-api
- baseURL: https://app.launchdarkly.com/api/v2
  baseurl_source: declared
  description: Polling endpoints for PHP server-side SDKs which do not support streaming mode.
  name: launchdarkly PHP Polling API
  phrasing_intents:
  - id: getLatestAllFlags
    intent: Poll the latest flag data for PHP SDKs
    question: How does a PHP server SDK fetch flag data without streaming?
  phrasing_ops: 1
  slug: launchdarkly-php-polling-api
- baseURL: https://app.launchdarkly.com/api/v2
  baseurl_source: declared
  description: Manage projects that organize feature flags and other resources.
  name: launchdarkly Projects API
  phrasing_intents:
  - id: getProjects
    intent: List projects on the dev server
    question: Which projects are configured on my local dev server?
  - id: createProject
    intent: Create a new project
    question: How do I create a new project with its own environments?
  - id: getProject
    intent: Get a dev server project's sync configuration
    question: How do I see how a project is configured to sync on the dev server?
  - id: patchProject
    intent: Update or resync a dev server project
    question: How do I force the dev server to resync a project?
  - id: deleteProject
    intent: Remove a project from the dev server
    question: How do I remove a project from the local dev server?
  - id: postAddProject
    intent: Add a project to the dev server
    question: How do I add a project to my local dev server?
  - id: postImportProject
    intent: Import a project from exported JSON
    question: How do I load a previously exported project into the dev server?
  - id: deleteOverrides
    intent: Clear all flag overrides for a project
    question: How do I reset every local flag override in a project?
  phrasing_ops: 11
  slug: launchdarkly-projects-api
- baseURL: https://app.launchdarkly.com/api/v2
  baseurl_source: declared
  description: Manage automatic configuration entries for LaunchDarkly Relay Proxy instances.
  name: launchdarkly Relay Proxy Configurations API
  phrasing_intents:
  - id: listRelayProxyConfigs
    intent: List Relay Proxy auto-configurations
    question: What Relay Proxy automatic configurations do we have?
  - id: createRelayProxyConfig
    intent: Create a Relay Proxy auto-configuration
    question: How do I generate a key for a new Relay Proxy instance?
  phrasing_ops: 2
  slug: launchdarkly-relay-proxy-configurations-api
- baseURL: https://app.launchdarkly.com/api/v2
  baseurl_source: declared
  description: Manage release pipelines for coordinating feature flag rollouts across environments.
  name: launchdarkly Releases API
  phrasing_intents:
  - id: listReleasePipelines
    intent: List a project's release pipelines
    question: What release pipelines are defined in this project?
  - id: createReleasePipeline
    intent: Create a release pipeline
    question: How do I set up a pipeline that promotes flags through environments?
  phrasing_ops: 2
  slug: launchdarkly-releases-api
- baseURL: https://app.launchdarkly.com/api/v2
  baseurl_source: declared
  description: Create and manage user segments for targeting groups of contexts with feature flags.
  name: launchdarkly Segments API
  phrasing_intents:
  - id: listSegments
    intent: List segments in an environment
    question: What user segments exist in this environment?
  - id: createSegment
    intent: Create a user segment
    question: How do I create a segment of beta users?
  - id: getSegmentsByProjectKeyByEnvironmentKeyBySegmentKey
    intent: Get one segment
    question: How do I see who is included in a specific segment?
  - id: patchSegmentsByProjectKeyByEnvironmentKeyBySegmentKey
    intent: Update a segment
    question: How do I add users to an existing segment?
  - id: deleteSegmentsByProjectKeyByEnvironmentKeyBySegmentKey
    intent: Delete a segment
    question: How do I permanently delete a segment?
  phrasing_ops: 5
  slug: launchdarkly-segments-api
- baseURL: https://app.launchdarkly.com/api/v2
  baseurl_source: declared
  description: Flag evaluation endpoints for server-side SDKs using SDK keys for authentication.
  name: launchdarkly Server-Side Evaluation API
  phrasing_intents:
  - id: evaluateAllFlagsForContext
    intent: Evaluate all flags for a context server-side
    question: How do I evaluate every flag for a context using my SDK key?
  phrasing_ops: 1
  slug: launchdarkly-server-side-evaluation-api
- baseURL: https://app.launchdarkly.com/api/v2
  baseurl_source: declared
  description: Server-Sent Events streaming endpoints for server-side SDKs to receive real-time flag updates.
  name: launchdarkly Server-Side Streaming API
  phrasing_intents:
  - id: streamAllFlags
    intent: Stream all flag and segment data to a server
    question: How does a server SDK get real-time updates for flags and segments together?
  - id: streamFlagsOnly
    intent: Stream only flag updates to a server
    question: Can I stream just flag changes without segment data?
  phrasing_ops: 2
  slug: launchdarkly-server-side-streaming-api
- baseURL: https://app.launchdarkly.com/api/v2
  baseurl_source: declared
  description: Health and status monitoring endpoints for the Relay Proxy. No authentication is required for these endpoints.
  name: launchdarkly Status API
  phrasing_intents:
  - id: getRelayProxyStatus
    intent: Check Relay Proxy health
    question: Is my Relay Proxy healthy or degraded?
  phrasing_ops: 1
  slug: launchdarkly-status-api
- baseURL: https://app.launchdarkly.com/api/v2
  baseurl_source: declared
  description: The Tags API from launchdarkly — 1 operation(s) for tags.
  name: launchdarkly Tags API
  phrasing_intents:
  - id: listTags
    intent: List tags used across the account
    question: What tags are in use across our LaunchDarkly resources?
  phrasing_ops: 1
  slug: launchdarkly-tags-api
- baseURL: https://app.launchdarkly.com/api/v2
  baseurl_source: declared
  description: Organize account members into teams for collaborative flag management and permissions.
  name: launchdarkly Teams API
  phrasing_intents:
  - id: listTeams
    intent: List teams
    question: What teams exist in our account?
  - id: createTeam
    intent: Create a team
    question: How do I create a team and add members to it?
  phrasing_ops: 2
  slug: launchdarkly-teams-api
- baseURL: https://app.launchdarkly.com/api/v2
  baseurl_source: declared
  description: Configure webhooks to receive HTTP POST notifications when changes occur in LaunchDarkly.
  name: launchdarkly Webhooks API
  phrasing_intents:
  - id: listWebhooks
    intent: List webhooks
    question: Which webhooks are configured in our account?
  - id: createWebhook
    intent: Create a webhook
    question: How do I get notified at my own URL when something changes?
  - id: getWebhooksByWebhookId
    intent: Get one webhook
    question: How do I look up the settings of a specific webhook?
  - id: patchWebhooksByWebhookId
    intent: Update a webhook
    question: How do I change a webhook's URL or turn it off?
  - id: deleteWebhooksByWebhookId
    intent: Delete a webhook
    question: How do I permanently remove a webhook subscription?
  phrasing_ops: 5
  slug: launchdarkly-webhooks-api
- baseURL: https://app.launchdarkly.com/api/v2
  baseurl_source: declared
  description: Create and manage automated workflows for scheduling and orchestrating flag changes.
  name: launchdarkly Workflows API
  phrasing_intents:
  - id: listWorkflows
    intent: List workflows on a flag
    question: What workflows are scheduled for this flag?
  phrasing_ops: 1
  slug: launchdarkly-workflows-api
- description: LaunchDarkly operates a first-party hosted Model Context Protocol server at https://mcp.launchdarkly.com/mcp/launchdarkly, reachable by any MCP client over streamable HTTP and authorized with OAuth 2.
  name: LaunchDarkly MCP Server
  slug: launchdarkly-mcp-server
- baseURL: https://app.launchdarkly.com/api/v2
  baseurl_source: declared
  description: The Backup API from LaunchDarkly — 1 operation(s) for backup.
  name: LaunchDarkly Backup API
  phrasing_intents:
  - id: getBackup
    intent: Download the backup
    question: How do I download the current backup?
  - id: restoreBackup
    intent: Restore from a backup
    question: How do I restore data from a backup?
  phrasing_ops: 2
  slug: launchdarkly-backup-api
- baseURL: https://app.launchdarkly.com/api/v2
  baseurl_source: declared
  description: The Debug Sessions API from LaunchDarkly — 3 operation(s) for debug sessions.
  name: LaunchDarkly Debug Sessions API
  phrasing_intents:
  - id: getDebugSessions
    intent: List debug sessions with event counts
    question: What debug sessions do I have and how many events does each hold?
  - id: deleteDebugSession
    intent: Delete a debug session and its events
    question: How do I delete a debug session I no longer need?
  - id: getDebugSessionEvents
    intent: Get events from a debug session
    question: How can I see the events captured in a specific debug session?
  phrasing_ops: 3
  slug: launchdarkly-debug-sessions-api
- baseURL: https://app.launchdarkly.com/api/v2
  baseurl_source: declared
  description: '> ### This feature is in beta > > To use this feature, pass in a header including the `LD-API-Version` key with value set to `beta`. Use this header with each call. To learn more, read [Beta resources'
  name: LaunchDarkly Account usage (beta) API
  slug: launchdarkly-account-usage-beta-api
- baseURL: https://app.launchdarkly.com/api/v2
  baseurl_source: declared
  description: Adaptive triggers automatically update the targeting of a feature flag or AgentControl config when a trigger source, such as an observability alert, fires. Each adaptive trigger pairs a trigger source
  name: LaunchDarkly Adaptive triggers API
  slug: launchdarkly-adaptive-triggers-api
- baseURL: https://app.launchdarkly.com/api/v2
  baseurl_source: declared
  description: The AgentControl API allows you to create, retrieve, and edit AgentControl configs, config variations, and AI model configurations. **This product name has changed, but the API has not.** AgentControl
  name: LaunchDarkly Agent Control API
  slug: launchdarkly-agentcontrol-api
- baseURL: https://app.launchdarkly.com/api/v2
  baseurl_source: declared
  description: The announcements API lets you create and update a custom announcement banner that appears in the LaunchDarkly user interface for everyone in your organization. You can use the banner to display organ
  name: LaunchDarkly Announcements API
  slug: launchdarkly-announcements-api
- baseURL: https://app.launchdarkly.com/api/v2
  baseurl_source: declared
  description: '> ### This feature is in beta > > To use this feature, pass in a header including the `LD-API-Version` key with value set to `beta`. Use this header with each call. To learn more, read [Beta resources'
  name: LaunchDarkly Applications (beta) API
  slug: launchdarkly-applications-beta-api
- baseURL: https://app.launchdarkly.com/api/v2
  baseurl_source: declared
  description: '> ### This feature is in beta > > To use this feature, pass in a header including the `LD-API-Version` key with value set to `beta`. Use this header with each call. To learn more, read [Beta resources'
  name: LaunchDarkly Approvals (beta) API
  slug: launchdarkly-approvals-beta-api
- baseURL: https://app.launchdarkly.com/api/v2
  baseurl_source: declared
  description: You can use the context settings API to assign a context to a specific variation for any feature flag. To learn more, read [View and manage contexts](https://launchdarkly.com/docs/home/observability/c
  name: LaunchDarkly Context settings API
  slug: launchdarkly-context-settings-api
- baseURL: https://app.launchdarkly.com/api/v2
  baseurl_source: declared
  description: Contexts are people, services, machines, or other resources that encounter feature flags in your product. Contexts are identified by their `kind`, which describes the type of resources encountering fl
  name: LaunchDarkly Contexts API
  slug: launchdarkly-contexts-api
- baseURL: https://app.launchdarkly.com/api/v2
  baseurl_source: declared
  description: '> ### Data Export is an add-on feature > > Data Export is available as an add-on for customers on a Foundation or Enterprise plan. To learn more, [read about our pricing](https://launchdarkly.com/pric'
  name: LaunchDarkly Data Export destinations API
  slug: launchdarkly-data-export-destinations-api
- baseURL: https://app.launchdarkly.com/api/v2
  baseurl_source: declared
  description: '> ### This feature is in beta > > To use this feature, pass in a header including the `LD-API-Version` key with value set to `beta`. Use this header with each call. To learn more, read [Beta resources'
  name: LaunchDarkly Feature flags (beta) API
  slug: launchdarkly-feature-flags-beta-api
- baseURL: https://app.launchdarkly.com/api/v2
  baseurl_source: declared
  description: '> ### This feature is in beta > > To use this feature, pass in a header including the `LD-API-Version` key with value set to `beta`. Use this header with each call. To learn more, read [Beta resources'
  name: LaunchDarkly Flag import configurations (beta) API
  slug: launchdarkly-flag-import-configurations-beta-api
- baseURL: https://app.launchdarkly.com/api/v2
  baseurl_source: declared
  description: '> ### This feature is in beta > > To use this feature, pass in a header including the `LD-API-Version` key with value set to `beta`. Use this header with each call. To learn more, read [Beta resources'
  name: LaunchDarkly Flag links (beta) API
  slug: launchdarkly-flag-links-beta-api
- baseURL: https://app.launchdarkly.com/api/v2
  baseurl_source: declared
  description: Follow flags to receive email updates about targeting changes to a flag in a project and environment. Several of the endpoints in the follow flags API require a member ID. The member ID is returned as
  name: LaunchDarkly Follow flags API
  slug: launchdarkly-follow-flags-api
- baseURL: https://app.launchdarkly.com/api/v2
  baseurl_source: declared
  description: '> ### Available for customers using Experimentation > > Holdouts are available to customers using [Experimentation](https://launchdarkly.com/docs/api/experiments). Holdouts let you exclude a percentag'
  name: LaunchDarkly Holdouts API
  slug: launchdarkly-holdouts-api
- baseURL: https://app.launchdarkly.com/api/v2
  baseurl_source: declared
  description: '> ### This feature is in beta > > To use this feature, pass in a header including the `LD-API-Version` key with value set to `beta`. Use this header with each call. To learn more, read [Beta resources'
  name: LaunchDarkly Insights charts (beta) API
  slug: launchdarkly-insights-charts-beta-api
- baseURL: https://app.launchdarkly.com/api/v2
  baseurl_source: declared
  description: '> ### This feature is in beta > > To use this feature, pass in a header including the `LD-API-Version` key with value set to `beta`. Use this header with each call. To learn more, read [Beta resources'
  name: LaunchDarkly Insights deployments (beta) API
  slug: launchdarkly-insights-deployments-beta-api
- baseURL: https://app.launchdarkly.com/api/v2
  baseurl_source: declared
  description: '> ### This feature is in beta > > To use this feature, pass in a header including the `LD-API-Version` key with value set to `beta`. Use this header with each call. To learn more, read [Beta resources'
  name: LaunchDarkly Insights flag events (beta) API
  slug: launchdarkly-insights-flag-events-beta-api
- baseURL: https://app.launchdarkly.com/api/v2
  baseurl_source: declared
  description: '> ### This feature is in beta > > To use this feature, pass in a header including the `LD-API-Version` key with value set to `beta`. Use this header with each call. To learn more, read [Beta resources'
  name: LaunchDarkly Insights pull requests (beta) API
  slug: launchdarkly-insights-pull-requests-beta-api
- baseURL: https://app.launchdarkly.com/api/v2
  baseurl_source: declared
  description: '> ### This feature is in beta > > To use this feature, pass in a header including the `LD-API-Version` key with value set to `beta`. Use this header with each call. To learn more, read [Beta resources'
  name: LaunchDarkly Insights repositories (beta) API
  slug: launchdarkly-insights-repositories-beta-api
- baseURL: https://app.launchdarkly.com/api/v2
  baseurl_source: declared
  description: '> ### This feature is in beta > > To use this feature, pass in a header including the `LD-API-Version` key with value set to `beta`. Use this header with each call. To learn more, read [Beta resources'
  name: LaunchDarkly Insights scores (beta) API
  slug: launchdarkly-insights-scores-beta-api
- baseURL: https://app.launchdarkly.com/api/v2
  baseurl_source: declared
  description: '> ### This feature is in beta > > To use this feature, pass in a header including the `LD-API-Version` key with value set to `beta`. Use this header with each call. To learn more, read [Beta resources'
  name: LaunchDarkly Integration delivery configurations (beta) API
  slug: launchdarkly-integration-delivery-configurations-beta-api
- baseURL: https://app.launchdarkly.com/api/v2
  baseurl_source: declared
  description: '> ### This feature is in beta > > To use this feature, pass in a header including the `LD-API-Version` key with value set to `beta`. Use this header with each call. To learn more, read [Beta resources'
  name: LaunchDarkly Integrations (beta) API
  slug: launchdarkly-integrations-beta-api
- baseURL: https://app.launchdarkly.com/api/v2
  baseurl_source: declared
  description: '> ### This feature is in beta > > To use this feature, pass in a header including the `LD-API-Version` key with value set to `beta`. Use this header with each call. To learn more, read [Beta resources'
  name: LaunchDarkly IP Allowlist (beta) API
  slug: launchdarkly-ip-allowlist-beta-api
- baseURL: https://app.launchdarkly.com/api/v2
  baseurl_source: declared
  description: '> ### Available for customers using Experimentation > > Layers are available to customers using [Experimentation](https://launchdarkly.com/docs/api/experiments). There are some cases in which you may '
  name: LaunchDarkly Layers API
  slug: launchdarkly-layers-api
- baseURL: https://app.launchdarkly.com/api/v2
  baseurl_source: declared
  description: '> ### This feature is in beta > > To use this feature, pass in a header including the `LD-API-Version` key with value set to `beta`. Use this header with each call. To learn more, read [Beta resources'
  name: LaunchDarkly Metrics (beta) API
  slug: launchdarkly-metrics-beta-api
- baseURL: https://app.launchdarkly.com/api/v2
  baseurl_source: declared
  description: 'The OAuth2 client API allows you to register a LaunchDarkly OAuth client for use in your own custom integrations. Registering a LaunchDarkly OAuth client allows you to use LaunchDarkly as an identity '
  name: LaunchDarkly OAuth2 Clients API
  slug: launchdarkly-oauth2-clients-api
- baseURL: https://app.launchdarkly.com/api/v2
  baseurl_source: declared
  description: Other requests available in the LaunchDarkly API.
  name: LaunchDarkly Other API
  slug: launchdarkly-other-api
- baseURL: https://app.launchdarkly.com/api/v2
  baseurl_source: declared
  description: '> ### This feature is in beta > > To use this feature, pass in a header including the `LD-API-Version` key with value set to `beta`. Use this header with each call. To learn more, read [Beta resources'
  name: LaunchDarkly Persistent store integrations (beta) API
  slug: launchdarkly-persistent-store-integrations-beta-api
- baseURL: https://app.launchdarkly.com/api/v2
  baseurl_source: declared
  description: '> ### This feature is in beta > > To use this feature, pass in a header including the `LD-API-Version` key with value set to `beta`. Use this header with each call. To learn more, read [Beta resources'
  name: LaunchDarkly Release pipelines (beta) API
  slug: launchdarkly-release-pipelines-beta-api
- baseURL: https://app.launchdarkly.com/api/v2
  baseurl_source: declared
  description: '> ### This feature is in beta > > To use this feature, pass in a header including the `LD-API-Version` key with value set to `beta`. Use this header with each call. To learn more, read [Beta resources'
  name: LaunchDarkly Release policies (beta) API
  slug: launchdarkly-release-policies-beta-api
- baseURL: https://app.launchdarkly.com/api/v2
  baseurl_source: declared
  description: '> ### This feature is in beta > > To use this feature, pass in a header including the `LD-API-Version` key with value set to `beta`. Use this header with each call. To learn more, read [Beta resources'
  name: LaunchDarkly Releases (beta) API
  slug: launchdarkly-releases-beta-api
- baseURL: https://app.launchdarkly.com/api/v2
  baseurl_source: declared
  description: '> ### Scheduled flag changes is an Enterprise feature > > Scheduled flag changes is available to customers on an Enterprise plan. To learn more, [read about our pricing](https://launchdarkly.com/prici'
  name: LaunchDarkly Scheduled changes API
  slug: launchdarkly-scheduled-changes-api
- baseURL: https://app.launchdarkly.com/api/v2
  baseurl_source: declared
  description: '> ### This feature is in beta > > To use this feature, pass in a header including the `LD-API-Version` key with value set to `beta`. Use this header with each call. To learn more, read [Beta resources'
  name: LaunchDarkly SDK Keys (beta) API
  slug: launchdarkly-sdk-keys-beta-api
- baseURL: https://app.launchdarkly.com/api/v2
  baseurl_source: declared
  description: '> ### This feature is in beta > > To use this feature, pass in a header including the `LD-API-Version` key with value set to `beta`. Use this header with each call. To learn more, read [Beta resources'
  name: LaunchDarkly Teams (beta) API
  slug: launchdarkly-teams-beta-api
- baseURL: https://app.launchdarkly.com/api/v2
  baseurl_source: declared
  description: '> ### Contexts are now available > > After you have upgraded your LaunchDarkly SDK to use contexts instead of users, you should use [Contexts](https://launchdarkly.com/docs/api/contexts) instead of th'
  name: LaunchDarkly User settings API
  slug: launchdarkly-user-settings-api
- baseURL: https://app.launchdarkly.com/api/v2
  baseurl_source: declared
  description: '> ### Contexts are now available > > After you have upgraded your LaunchDarkly SDK to use contexts instead of users, you should use [Contexts](https://launchdarkly.com/docs/api/contexts) instead of th'
  name: LaunchDarkly Users API
  slug: launchdarkly-users-api
- baseURL: https://app.launchdarkly.com/api/v2
  baseurl_source: declared
  description: The views API allows you to create, retrieve, and edit views, and link other resources to views. A view is a resource in LaunchDarkly that you can use to logically group other resources within a proje
  name: LaunchDarkly Views API
  slug: launchdarkly-views-api
- baseURL: https://app.launchdarkly.com/api/v2
  baseurl_source: declared
  description: '> ### Workflows are in maintenance mode > > The workflows feature is in maintenance mode, and is planned for future deprecation at a date not yet specified. We will work with existing customers using '
  name: LaunchDarkly Workflow templates API
  slug: launchdarkly-workflow-templates-api
artifact_total: 200
asyncapis:
- description: LaunchDarkly sends webhook notifications as HTTP POST requests when changes occur within the platform. The webhook payload format is identical to audit log entries and includes details about what chan
  name: LaunchDarkly Webhooks Events
  slug: launchdarkly-webhooks-asyncapi
collections:
- collection_type: open
  name: LaunchDarkly Relay Proxy Access Tokens API
  slug: open-launchdarkly-access-tokens-api
- collection_type: open
  name: LaunchDarkly Relay Proxy Access Tokens Account Members API
  slug: open-launchdarkly-account-members-api
- collection_type: open
  name: LaunchDarkly Relay Proxy Access Tokens Approvals API
  slug: open-launchdarkly-approvals-api
- collection_type: open
  name: LaunchDarkly Relay Proxy Access Tokens Audit Log API
  slug: open-launchdarkly-audit-log-api
- collection_type: open
  name: LaunchDarkly Relay Proxy Access Tokens Client-Side Evaluation API
  slug: open-launchdarkly-client-side-evaluation-api
- collection_type: open
  name: LaunchDarkly Relay Proxy Access Tokens Client-Side Streaming API
  slug: open-launchdarkly-client-side-streaming-api
- collection_type: open
  name: LaunchDarkly Relay Proxy Access Tokens Code References API
  slug: open-launchdarkly-code-references-api
- collection_type: open
  name: LaunchDarkly Relay Proxy Access Tokens Custom Roles API
  slug: open-launchdarkly-custom-roles-api
- collection_type: open
  name: LaunchDarkly Relay Proxy Access Tokens Environments API
  slug: open-launchdarkly-environments-api
- collection_type: open
  name: LaunchDarkly Relay Proxy Access Tokens Experiments API
  slug: open-launchdarkly-experiments-api
- collection_type: open
  name: LaunchDarkly Relay Proxy Access Tokens Feature Flags API
  slug: open-launchdarkly-feature-flags-api
- collection_type: open
  name: LaunchDarkly Relay Proxy Access Tokens Flag Triggers API
  slug: open-launchdarkly-flag-triggers-api
- collection_type: open
  name: LaunchDarkly Relay Proxy Access Tokens Integration Audit Log Subscriptions API
  slug: open-launchdarkly-integration-audit-log-subscriptions-api
- collection_type: open
  name: LaunchDarkly Relay Proxy Access Tokens Metrics API
  slug: open-launchdarkly-metrics-api
- collection_type: open
  name: LaunchDarkly Relay Proxy Access Tokens PHP Polling API
  slug: open-launchdarkly-php-polling-api
- collection_type: open
  name: LaunchDarkly Relay Proxy Access Tokens Projects API
  slug: open-launchdarkly-projects-api
- collection_type: open
  name: LaunchDarkly Relay Proxy Access Tokens Relay Proxy Configurations API
  slug: open-launchdarkly-relay-proxy-configurations-api
- collection_type: open
  name: LaunchDarkly Relay Proxy
  slug: open-launchdarkly-relay-proxy
- collection_type: open
  name: LaunchDarkly Relay Proxy Access Tokens Releases API
  slug: open-launchdarkly-releases-api
- collection_type: open
  name: LaunchDarkly REST API
  slug: open-launchdarkly-rest-api
- collection_type: open
  name: LaunchDarkly Relay Proxy Access Tokens Segments API
  slug: open-launchdarkly-segments-api
- collection_type: open
  name: LaunchDarkly Relay Proxy Access Tokens Server-Side Evaluation API
  slug: open-launchdarkly-server-side-evaluation-api
- collection_type: open
  name: LaunchDarkly Relay Proxy Access Tokens Server-Side Streaming API
  slug: open-launchdarkly-server-side-streaming-api
- collection_type: open
  name: LaunchDarkly Relay Proxy Access Tokens Status API
  slug: open-launchdarkly-status-api
- collection_type: open
  name: LaunchDarkly Relay Proxy Access Tokens Tags API
  slug: open-launchdarkly-tags-api
- collection_type: open
  name: LaunchDarkly Relay Proxy Access Tokens Teams API
  slug: open-launchdarkly-teams-api
- collection_type: open
  name: LaunchDarkly Relay Proxy Access Tokens Webhooks API
  slug: open-launchdarkly-webhooks-api
- collection_type: open
  name: LaunchDarkly Relay Proxy Access Tokens Workflows API
  slug: open-launchdarkly-workflows-api
common:
- group: commercial
  href: https://artifacts.apis.io/launchdarkly/finops/launchdarkly-finops.yml
  title: ''
  type: FinOps
  url: finops/launchdarkly-finops.yml
- group: company
  title: ''
  type: Website
  url: https://www.launchdarkly.com/
- group: other
  href: https://artifacts.apis.io/launchdarkly/capabilities/launchdarkly-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/launchdarkly-capability-edges.yml
- group: auth
  href: https://artifacts.apis.io/launchdarkly/security/launchdarkly-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/launchdarkly-trust-center.yml
- group: agent
  href: https://artifacts.apis.io/launchdarkly/agentic-access/launchdarkly-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/launchdarkly-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/launchdarkly/security/launchdarkly-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/launchdarkly-domain-security.yml
- group: auth
  href: https://artifacts.apis.io/launchdarkly/authentication/launchdarkly-authentication.yml
  title: ''
  type: Authentication
  url: authentication/launchdarkly-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/launchdarkly
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/launchdarkly
- group: docs
  href: https://artifacts.apis.io/launchdarkly/json-schema/launchdarkly-feature-flag-schema.json
  title: ''
  type: JSONSchema
  url: json-schema/launchdarkly-feature-flag-schema.json
- group: docs
  href: https://artifacts.apis.io/launchdarkly/json-schema/launchdarkly-webhook-event-schema.json
  title: ''
  type: JSONSchema
  url: json-schema/launchdarkly-webhook-event-schema.json
- group: design
  href: https://artifacts.apis.io/launchdarkly/json-ld/launchdarkly-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/launchdarkly-context.jsonld
- group: company
  title: ''
  type: Blog
  url: https://launchdarkly.com/blog/feed/
- group: docs
  href: https://artifacts.apis.io/launchdarkly/openapi/launchdarkly-rest-api-openapi.json
  title: ''
  type: OpenAPI
  url: openapi/launchdarkly-rest-api-openapi.json
- group: agent
  href: https://artifacts.apis.io/launchdarkly/llms/launchdarkly-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/launchdarkly-llms.txt
- group: build
  href: https://artifacts.apis.io/launchdarkly/packages/launchdarkly-packages.yml
  title: ''
  type: Packages
  url: packages/launchdarkly-packages.yml
- group: build
  href: https://artifacts.apis.io/launchdarkly/packages/launchdarkly-packages.yml
  title: ''
  type: SDKs
  url: packages/launchdarkly-packages.yml
- group: build
  href: https://artifacts.apis.io/launchdarkly/cli/launchdarkly-cli.yml
  title: ''
  type: CLI
  url: cli/launchdarkly-cli.yml
- group: agent
  href: https://artifacts.apis.io/launchdarkly/well-known/launchdarkly-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/launchdarkly-well-known.yml
- group: agent
  href: https://artifacts.apis.io/launchdarkly/mcp/launchdarkly-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/launchdarkly-mcp.yml
- group: build
  href: https://artifacts.apis.io/launchdarkly/mcp/launchdarkly-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/launchdarkly-tool-crosswalk.yml
- group: design
  href: https://artifacts.apis.io/launchdarkly/conventions/launchdarkly-conventions.yml
  title: ''
  type: Conventions
  url: conventions/launchdarkly-conventions.yml
- group: design
  href: https://artifacts.apis.io/launchdarkly/conformance/launchdarkly-conformance.yml
  title: ''
  type: Conformance
  url: conformance/launchdarkly-conformance.yml
- group: auth
  href: https://artifacts.apis.io/launchdarkly/conformance/launchdarkly-conformance.yml
  title: ''
  type: Compliance
  url: conformance/launchdarkly-conformance.yml
- group: design
  href: https://artifacts.apis.io/launchdarkly/errors/launchdarkly-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/launchdarkly-problem-types.yml
- group: design
  href: https://artifacts.apis.io/launchdarkly/lifecycle/launchdarkly-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/launchdarkly-lifecycle.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://status.launchdarkly.com/
- group: operate
  title: ''
  type: Deprecation
  url: https://launchdarkly.com/policies/end-of-life-policy/
- group: auth
  href: https://artifacts.apis.io/launchdarkly/scopes/launchdarkly-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/launchdarkly-scopes.yml
- group: design
  href: https://artifacts.apis.io/launchdarkly/data-model/launchdarkly-data-model.yml
  title: ''
  type: DataModel
  url: data-model/launchdarkly-data-model.yml
- group: operate
  href: https://artifacts.apis.io/launchdarkly/changelog/launchdarkly-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/launchdarkly-changelog.yml
- group: start
  href: https://artifacts.apis.io/launchdarkly/sandbox/launchdarkly-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/launchdarkly-sandbox.yml
- group: agent
  href: https://artifacts.apis.io/launchdarkly/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: other
  href: https://artifacts.apis.io/launchdarkly/overlays/launchdarkly-rest-api-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/launchdarkly-rest-api-overlay.yaml
- group: design
  href: https://artifacts.apis.io/launchdarkly/asyncapi/launchdarkly-webhooks-asyncapi.yml
  title: ''
  type: Webhooks
  url: asyncapi/launchdarkly-webhooks-asyncapi.yml
- group: docs
  href: https://artifacts.apis.io/launchdarkly/asyncapi/launchdarkly-webhooks-asyncapi.yml
  title: ''
  type: AsyncAPI
  url: asyncapi/launchdarkly-webhooks-asyncapi.yml
- group: commercial
  href: https://artifacts.apis.io/launchdarkly/plans/launchdarkly-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/launchdarkly-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/launchdarkly/rate-limits/launchdarkly-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/launchdarkly-rate-limits.yml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://launchdarkly.com/docs/home
- group: docs
  title: ''
  type: Documentation
  url: https://launchdarkly.com/docs/home
- group: docs
  title: ''
  type: APIReference
  url: https://launchdarkly.com/docs/api
- group: start
  title: ''
  type: GettingStarted
  url: https://launchdarkly.com/docs/home/getting-started
- group: operate
  title: ''
  type: Support
  url: https://support.launchdarkly.com/
- group: commercial
  title: ''
  type: Pricing
  url: https://launchdarkly.com/pricing/
- group: start
  title: ''
  type: SignUp
  url: https://app.launchdarkly.com/signup
- group: commercial
  title: ''
  type: TermsOfService
  url: https://launchdarkly.com/policies/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://launchdarkly.com/privacy/
- group: company
  title: ''
  type: Blog
  url: https://launchdarkly.com/blog/
- group: build
  title: ''
  type: SourceCode
  url: https://github.com/launchdarkly/ldcli
- group: auth
  href: https://artifacts.apis.io/launchdarkly/security/launchdarkly-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/launchdarkly-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/launchdarkly/security/launchdarkly-vulnerability-disclosure.yml
  title: ''
  type: Security
  url: security/launchdarkly-vulnerability-disclosure.yml
created: 2024/04/14
description: LaunchDarkly is a feature management and runtime control platform. Development teams use it to wrap releases in feature flags, target variations at specific users, contexts, segments and environments, run experiments and guarded rollouts, and turn a change back off without shipping new code. The platform now extends the same targeting, approval and audit machinery to AI through AgentControl, where prompts, models, tools and agent graphs are versioned and rolled out as configs, and to observability through session replay, errors, logs and traces. LaunchDarkly publishes a 401-operation REST API, more than thirty SDKs across thirteen client-side, thirteen server-side and four edge runtimes, a self-hosted Relay Proxy, a CLI, and a hosted MCP server exposing 125 tools to AI clients. LaunchDarkly is operated by Catamorphic Co.
features:
- 'Developer free: unlimited flags, seats, 30 SDKs, 5K replays, 10M logs'
- 'Foundation: $12/mo per Service Connection + $10 per 1k client MAU'
- 'Enterprise custom: SAML/SCIM, custom roles, release automation'
- 'Guardian custom: release monitoring, auto rollback, guardrails'
- REST API for projects, environments, flags, segments
- Per-route rate limits + global 200 req/10s
- Server-side, client-side, mobile SDKs (30+ languages)
- Streaming SDK for real-time flag updates
- Webhooks for flag and audit events
- OAuth 2.0 + Personal API tokens + service accounts
- Experimentation with statistical analysis
- Code references (find flag usage in code)
- Workflows with scheduling and approvals (Enterprise)
- Release pipelines and progressive rollouts
- Observability (Errors + Logs + Traces + Replays)
- Galaxy AI features for flag governance
finops:
- has_sources: true
  method: derived
  name: Launchdarkly Finops
  primary_unit: account
  service_category: ''
  slug: launchdarkly-finops
  template: false
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/launchdarkly.png
json_schemas:
- name: AccessToken
  property_count: 10
  slug: launchdarkly-accesstoken
- name: AccessTokenBody
  property_count: 5
  slug: launchdarkly-accesstokenbody
- name: AccessTokens
  property_count: 2
  slug: launchdarkly-accesstokens
- name: ApprovalRequest
  property_count: 6
  slug: launchdarkly-approvalrequest
- name: ApprovalRequestBody
  property_count: 4
  slug: launchdarkly-approvalrequestbody
- name: ApprovalRequests
  property_count: 2
  slug: launchdarkly-approvalrequests
- name: AuditLogEntries
  property_count: 2
  slug: launchdarkly-auditlogentries
- name: AuditLogEntry
  property_count: 9
  slug: launchdarkly-auditlogentry
- name: Clause
  property_count: 5
  slug: launchdarkly-clause
- name: CodeReferenceRepositories
  property_count: 1
  slug: launchdarkly-codereferencerepositories
- name: CustomRole
  property_count: 6
  slug: launchdarkly-customrole
- name: CustomRoleBody
  property_count: 4
  slug: launchdarkly-customrolebody
- name: CustomRoles
  property_count: 2
  slug: launchdarkly-customroles
- name: Environment
  property_count: 10
  slug: launchdarkly-environment
- name: EnvironmentBody
  property_count: 6
  slug: launchdarkly-environmentbody
- name: Environments
  property_count: 3
  slug: launchdarkly-environments
- name: EnvironmentStatus
  property_count: 8
  slug: launchdarkly-environmentstatus
- name: EvaluationContext
  property_count: 4
  slug: launchdarkly-evaluationcontext
- name: Experiment
  property_count: 7
  slug: launchdarkly-experiment
- name: ExperimentBody
  property_count: 4
  slug: launchdarkly-experimentbody
- name: Experiments
  property_count: 3
  slug: launchdarkly-experiments
- name: LaunchDarkly Feature Flag
  property_count: 14
  slug: launchdarkly-feature-flag
- name: FeatureFlag
  property_count: 12
  slug: launchdarkly-featureflag
- name: FeatureFlagBody
  property_count: 8
  slug: launchdarkly-featureflagbody
- name: FeatureFlags
  property_count: 3
  slug: launchdarkly-featureflags
- name: FlagData
  property_count: 2
  slug: launchdarkly-flagdata
- name: FlagEnvironment
  property_count: 10
  slug: launchdarkly-flagenvironment
- name: FlagEvaluation
  property_count: 6
  slug: launchdarkly-flagevaluation
- name: FlagEvaluations
  property_count: 0
  slug: launchdarkly-flagevaluations
- name: FlagTrigger
  property_count: 6
  slug: launchdarkly-flagtrigger
- name: FlagTriggerBody
  property_count: 2
  slug: launchdarkly-flagtriggerbody
- name: FlagTriggers
  property_count: 2
  slug: launchdarkly-flagtriggers
- name: IntegrationSubscriptions
  property_count: 1
  slug: launchdarkly-integrationsubscriptions
- name: Links
  property_count: 1
  slug: launchdarkly-links
- name: Member
  property_count: 8
  slug: launchdarkly-member
- name: MemberInviteBody
  property_count: 3
  slug: launchdarkly-memberinvitebody
- name: Members
  property_count: 3
  slug: launchdarkly-members
- name: MemberSummary
  property_count: 5
  slug: launchdarkly-membersummary
- name: Metric
  property_count: 8
  slug: launchdarkly-metric
- name: MetricBody
  property_count: 7
  slug: launchdarkly-metricbody
- name: Metrics
  property_count: 2
  slug: launchdarkly-metrics
- name: PatchOperation
  property_count: 2
  slug: launchdarkly-patchoperation
- name: Project
  property_count: 6
  slug: launchdarkly-project
- name: ProjectBody
  property_count: 4
  slug: launchdarkly-projectbody
- name: Projects
  property_count: 3
  slug: launchdarkly-projects
- name: RelayProxyConfig
  property_count: 8
  slug: launchdarkly-relayproxyconfig
- name: RelayProxyConfigBody
  property_count: 2
  slug: launchdarkly-relayproxyconfigbody
- name: RelayProxyConfigs
  property_count: 1
  slug: launchdarkly-relayproxyconfigs
- name: RelayProxyStatus
  property_count: 3
  slug: launchdarkly-relayproxystatus
- name: ReleasePipeline
  property_count: 5
  slug: launchdarkly-releasepipeline
- name: ReleasePipelineBody
  property_count: 4
  slug: launchdarkly-releasepipelinebody
- name: ReleasePipelines
  property_count: 1
  slug: launchdarkly-releasepipelines
- name: Rollout
  property_count: 3
  slug: launchdarkly-rollout
- name: Rule
  property_count: 5
  slug: launchdarkly-rule
- name: Segment
  property_count: 10
  slug: launchdarkly-segment
- name: SegmentBody
  property_count: 4
  slug: launchdarkly-segmentbody
- name: SegmentRule
  property_count: 4
  slug: launchdarkly-segmentrule
- name: Segments
  property_count: 3
  slug: launchdarkly-segments
- name: Statement
  property_count: 5
  slug: launchdarkly-statement
- name: TagCollection
  property_count: 2
  slug: launchdarkly-tagcollection
- name: Target
  property_count: 3
  slug: launchdarkly-target
- name: Team
  property_count: 7
  slug: launchdarkly-team
- name: TeamBody
  property_count: 5
  slug: launchdarkly-teambody
- name: Teams
  property_count: 3
  slug: launchdarkly-teams
- name: Variation
  property_count: 4
  slug: launchdarkly-variation
- name: LaunchDarkly Webhook Event
  property_count: 13
  slug: launchdarkly-webhook-event
- name: Webhook
  property_count: 8
  slug: launchdarkly-webhook
- name: WebhookBody
  property_count: 6
  slug: launchdarkly-webhookbody
- name: Webhooks
  property_count: 2
  slug: launchdarkly-webhooks
- name: Workflows
  property_count: 1
  slug: launchdarkly-workflows
json_structures:
- name: Launchdarkly Structure
  property_count: 0
  slug: launchdarkly-structure
jsonld:
- class_count: 0
  name: Launchdarkly Context
  property_count: 15
  slug: launchdarkly-context
layout: provider
mcp_servers:
- description: LaunchDarkly operates a first-party hosted MCP server covering feature management, AgentControl and observability, and also publishes a local stdio server for the federal and EU instances where the ho
  name: LaunchDarkly MCP Server
  slug: launchdarkly-mcp-server
modified: '2026-08-27'
name: LaunchDarkly
nav: Providers
network: true
overview: 'LaunchDarkly publishes 68 API contracts indexed on the [APIs.io](https://apis.io/) network, including Webhooks API, Access Tokens API, Account Members API, and 65 more. Tagged areas include Feature Flags, Feature Management, Experimentation, Observability, and Continuous Delivery.


  The LaunchDarkly catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 2 Spectral governance rulesets.


  LaunchDarkly''s developer surface includes authentication, engineering blog, CLI, changelog, sandbox, documentation, API reference, and 44 more developer resources.'
plans:
- name: Launchdarkly Plans Pricing
  plan_count: 4
  slug: launchdarkly-plans-pricing
random_paper: 10
rate_limits:
- limit_count: 4
  name: Launchdarkly Rate Limits
  slug: launchdarkly-rate-limits
rules:
- authorship: generated
  effective_rule_count: 35
  extends:
  - spectral:asyncapi
  name: LaunchDarkly — asyncapi rules
  rule_count: 8
  severity_counts:
    error: 1
    hint: 0
    info: 1
    warn: 6
  slug: launchdarkly-asyncapi-spectral-rules
- authorship: generated
  effective_rule_count: 6
  extends: []
  name: LaunchDarkly — jsonschema rules
  rule_count: 6
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 4
  slug: launchdarkly-jsonschema-spectral-rules
scopes:
- name: Launchdarkly Scopes
  scope_count: 4
  slug: launchdarkly-scopes
  summary_line: 4 scopes
score:
  band: exemplar
  composite: 85.5
  coverage:
    artifact_dirs: 37
    catalog_earned: 79.5
    catalog_earned_first_party: 24.0
    catalog_gap: 35.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.7
  facets:
    access_clarity: 100.0
    contract_governance: 31.8
    contract_quality: 74.2
    developer_ergonomics: 80.4
    discoverability: 80.0
    operational_transparency: 92.1
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - united-states
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
  previous_composite: 84.8
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 56.7
      total: 67
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
    score: 33.3
screenshot: https://apis.io/screenshots/launchdarkly/launchdarkly-2026-06-20T184335.png
security:
- kind: authentication
  name: Launchdarkly Authentication
  slug: launchdarkly-authentication
  summary_line: apiKey/oauth2 · 3 schemes
- kind: domain-security
  name: Launchdarkly Domain Security
  slug: launchdarkly-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Launchdarkly Vulnerability Disclosure
  slug: launchdarkly-vulnerability-disclosure
  summary_line: Hackerone
- kind: trust-center
  name: Launchdarkly Trust Center
  slug: launchdarkly-trust-center
  summary_line: SOC 2, ISO 27001, HIPAA, FedRAMP, GDPR
skill_count: 3
skills:
- name: launchdarkly-audit-and-clean-up-flags
  slug: launchdarkly-audit-and-clean-up-flags
- name: launchdarkly-governed-flag-change
  slug: launchdarkly-governed-flag-change
- name: launchdarkly-ship-a-feature-flag
  slug: launchdarkly-ship-a-feature-flag
slug: launchdarkly
tags:
- Feature Flags
- Feature Management
- Experimentation
- Observability
- Continuous Delivery
- DevOps
- AI Agents
- Release Management
- Developer Tools
- T1
website: https://www.launchdarkly.com/
---
