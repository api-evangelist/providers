---
access_model:
  confidence: high
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
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
    error_semantics: documented
    event_surface_described: derived
    idempotency: false
    mcp_server: documented
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.2
  score: 43.6
  scored_at: '2026-09-03'
agentic_access:
- acting_count: 25
  human_in_the_loop: 0
  name: Launchdarkly Agentic Access
  operation_count: 58
  slug: launchdarkly-agentic-access
  summary_line: 58 operations · 25 acting
api_count: 3
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
  slug: launchdarkly-access-tokens-api
- baseURL: https://app.launchdarkly.com/api/v2
  baseurl_source: declared
  description: Manage team members, invitations, and member roles within a LaunchDarkly account.
  name: launchdarkly Account Members API
  slug: launchdarkly-account-members-api
- baseURL: https://app.launchdarkly.com/api/v2
  baseurl_source: declared
  description: Manage approval requests and workflows for flag changes that require review before deployment.
  name: launchdarkly Approvals API
  slug: launchdarkly-approvals-api
- baseURL: https://app.launchdarkly.com/api/v2
  baseurl_source: declared
  description: Access the change history of all modifications made to resources in the LaunchDarkly account.
  name: launchdarkly Audit Log API
  slug: launchdarkly-audit-log-api
- baseURL: https://app.launchdarkly.com/api/v2
  baseurl_source: declared
  description: Flag evaluation endpoints for client-side and mobile SDKs using environment IDs or mobile keys for authentication.
  name: launchdarkly Client-Side Evaluation API
  slug: launchdarkly-client-side-evaluation-api
- baseURL: https://app.launchdarkly.com/api/v2
  baseurl_source: declared
  description: Server-Sent Events streaming endpoints for client-side and mobile SDKs to receive real-time flag updates.
  name: launchdarkly Client-Side Streaming API
  slug: launchdarkly-client-side-streaming-api
- baseURL: https://app.launchdarkly.com/api/v2
  baseurl_source: declared
  description: View code references that show where feature flags are used in your codebase.
  name: launchdarkly Code References API
  slug: launchdarkly-code-references-api
- baseURL: https://app.launchdarkly.com/api/v2
  baseurl_source: declared
  description: Define custom roles with fine-grained permissions using resource specifiers and actions.
  name: launchdarkly Custom Roles API
  slug: launchdarkly-custom-roles-api
- baseURL: https://app.launchdarkly.com/api/v2
  baseurl_source: declared
  description: Manage environments within projects such as production, staging, and development.
  name: launchdarkly Environments API
  slug: launchdarkly-environments-api
- baseURL: https://app.launchdarkly.com/api/v2
  baseurl_source: declared
  description: Create and manage experiments to measure the impact of feature flag variations on metrics.
  name: launchdarkly Experiments API
  slug: launchdarkly-experiments-api
- baseURL: https://app.launchdarkly.com/api/v2
  baseurl_source: declared
  description: Create, update, and manage feature flags and their targeting rules across projects and environments.
  name: launchdarkly Feature Flags API
  slug: launchdarkly-feature-flags-api
- baseURL: https://app.launchdarkly.com/api/v2
  baseurl_source: declared
  description: Create triggers that allow external services to toggle feature flags via unique webhook URLs.
  name: launchdarkly Flag Triggers API
  slug: launchdarkly-flag-triggers-api
- baseURL: https://app.launchdarkly.com/api/v2
  baseurl_source: declared
  description: Manage integrations that subscribe to audit log events and forward them to external tools.
  name: launchdarkly Integration Audit Log Subscriptions API
  slug: launchdarkly-integration-audit-log-subscriptions-api
- baseURL: https://app.launchdarkly.com/api/v2
  baseurl_source: declared
  description: Define and manage metrics used to measure experiment outcomes and feature flag impact.
  name: launchdarkly Metrics API
  slug: launchdarkly-metrics-api
- baseURL: https://app.launchdarkly.com/api/v2
  baseurl_source: declared
  description: Polling endpoints for PHP server-side SDKs which do not support streaming mode.
  name: launchdarkly PHP Polling API
  slug: launchdarkly-php-polling-api
- baseURL: https://app.launchdarkly.com/api/v2
  baseurl_source: declared
  description: Manage projects that organize feature flags and other resources.
  name: launchdarkly Projects API
  slug: launchdarkly-projects-api
- baseURL: https://app.launchdarkly.com/api/v2
  baseurl_source: declared
  description: Manage automatic configuration entries for LaunchDarkly Relay Proxy instances.
  name: launchdarkly Relay Proxy Configurations API
  slug: launchdarkly-relay-proxy-configurations-api
- baseURL: https://app.launchdarkly.com/api/v2
  baseurl_source: declared
  description: Manage release pipelines for coordinating feature flag rollouts across environments.
  name: launchdarkly Releases API
  slug: launchdarkly-releases-api
- baseURL: https://app.launchdarkly.com/api/v2
  baseurl_source: declared
  description: Create and manage user segments for targeting groups of contexts with feature flags.
  name: launchdarkly Segments API
  slug: launchdarkly-segments-api
- baseURL: https://app.launchdarkly.com/api/v2
  baseurl_source: declared
  description: Flag evaluation endpoints for server-side SDKs using SDK keys for authentication.
  name: launchdarkly Server-Side Evaluation API
  slug: launchdarkly-server-side-evaluation-api
- baseURL: https://app.launchdarkly.com/api/v2
  baseurl_source: declared
  description: Server-Sent Events streaming endpoints for server-side SDKs to receive real-time flag updates.
  name: launchdarkly Server-Side Streaming API
  slug: launchdarkly-server-side-streaming-api
- baseURL: https://app.launchdarkly.com/api/v2
  baseurl_source: declared
  description: Health and status monitoring endpoints for the Relay Proxy. No authentication is required for these endpoints.
  name: launchdarkly Status API
  slug: launchdarkly-status-api
- baseURL: https://app.launchdarkly.com/api/v2
  baseurl_source: declared
  description: The Tags API from launchdarkly — 1 operation(s) for tags.
  name: launchdarkly Tags API
  slug: launchdarkly-tags-api
- baseURL: https://app.launchdarkly.com/api/v2
  baseurl_source: declared
  description: Organize account members into teams for collaborative flag management and permissions.
  name: launchdarkly Teams API
  slug: launchdarkly-teams-api
- baseURL: https://app.launchdarkly.com/api/v2
  baseurl_source: declared
  description: Configure webhooks to receive HTTP POST notifications when changes occur in LaunchDarkly.
  name: launchdarkly Webhooks API
  slug: launchdarkly-webhooks-api
- baseURL: https://app.launchdarkly.com/api/v2
  baseurl_source: declared
  description: Create and manage automated workflows for scheduling and orchestrating flag changes.
  name: launchdarkly Workflows API
  slug: launchdarkly-workflows-api
- description: LaunchDarkly operates a first-party hosted Model Context Protocol server at https://mcp.launchdarkly.com/mcp/launchdarkly, reachable by any MCP client over streamable HTTP and authorized with OAuth 2.
  name: LaunchDarkly MCP Server
  slug: launchdarkly-mcp-server
- baseURL: https://app.launchdarkly.com/api/v2
  baseurl_source: declared
  description: The Backup API from LaunchDarkly — 1 operation(s) for backup.
  name: LaunchDarkly Backup API
  slug: launchdarkly-backup-api
- baseURL: https://app.launchdarkly.com/api/v2
  baseurl_source: declared
  description: The Debug Sessions API from LaunchDarkly — 3 operation(s) for debug sessions.
  name: LaunchDarkly Debug Sessions API
  slug: launchdarkly-debug-sessions-api
artifact_total: 161
asyncapis:
- description: LaunchDarkly sends webhook notifications as HTTP POST requests when changes occur within the platform. The webhook payload format is identical to audit log entries and includes details about what chan
  name: LaunchDarkly Webhooks Events
  slug: launchdarkly-webhooks-asyncapi
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
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
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/launchdarkly-capability-edges.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/launchdarkly-trust-center.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/launchdarkly-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/launchdarkly-domain-security.yml
- group: auth
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
  title: ''
  type: JSONSchema
  url: json-schema/launchdarkly-feature-flag-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/launchdarkly-webhook-event-schema.json
- group: design
  title: ''
  type: JSONLD
  url: json-ld/launchdarkly-context.jsonld
- group: company
  title: ''
  type: Blog
  url: https://launchdarkly.com/blog/feed/
- group: docs
  title: ''
  type: OpenAPI
  url: openapi/launchdarkly-rest-api-openapi.json
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/launchdarkly-llms.txt
- group: build
  title: ''
  type: Packages
  url: packages/launchdarkly-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/launchdarkly-packages.yml
- group: build
  title: ''
  type: CLI
  url: cli/launchdarkly-cli.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/launchdarkly-well-known.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/launchdarkly-mcp.yml
- group: build
  title: ''
  type: ToolCrosswalk
  url: mcp/launchdarkly-tool-crosswalk.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/launchdarkly-conventions.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/launchdarkly-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: conformance/launchdarkly-conformance.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/launchdarkly-problem-types.yml
- group: design
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
  title: ''
  type: OAuthScopes
  url: scopes/launchdarkly-scopes.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/launchdarkly-data-model.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/launchdarkly-changelog.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/launchdarkly-sandbox.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/launchdarkly-rest-api-overlay.yaml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/launchdarkly-webhooks-asyncapi.yml
- group: docs
  title: ''
  type: AsyncAPI
  url: asyncapi/launchdarkly-webhooks-asyncapi.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/launchdarkly-plans-pricing.yml
- group: operate
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
  title: ''
  type: VulnerabilityDisclosure
  url: security/launchdarkly-vulnerability-disclosure.yml
- group: auth
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
- name: Launchdarkly Finops
  service_category: Feature Management
  slug: launchdarkly-finops
graphqls:
- description: LaunchDarkly does not publish a native GraphQL API. This is a conceptual GraphQL schema derived from the LaunchDarkly REST API (version 20240415) data model documented at https://apidocs.launchdarkly.
  name: LaunchDarkly GraphQL Schema
  slug: launchdarkly-graphql
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
overview: 'LaunchDarkly publishes 29 APIs on the [APIs.io](https://apis.io/) network, including Webhooks API, Access Tokens API, Account Members API, and 26 more. Tagged areas include Feature Flags, Feature Management, Experimentation, Observability, and Continuous Delivery.


  The LaunchDarkly catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 2 Spectral governance rulesets.


  LaunchDarkly''s developer surface includes authentication, engineering blog, CLI, changelog, sandbox, documentation, API reference, and 42 more developer resources.'
plans:
- name: Launchdarkly Plans Pricing
  plan_count: 4
  slug: launchdarkly-plans-pricing
random_paper: 1
rate_limits:
- limit_count: 4
  name: Launchdarkly Rate Limits
  slug: launchdarkly-rate-limits
rules:
- effective_rule_count: 35
  extends:
  - spectral:asyncapi
  name: LaunchDarkly API Rules
  rule_count: 8
  severity_counts:
    error: 1
    hint: 0
    info: 1
    warn: 6
  slug: launchdarkly-asyncapi-spectral-rules
- effective_rule_count: 6
  extends: []
  name: LaunchDarkly API Rules
  rule_count: 6
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 4
  slug: launchdarkly-jsonschema-spectral-rules
scopes:
- name: Launchdarkly Scopes
  scope_count: 0
  slug: launchdarkly-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: exemplar
  composite: 77.9
  coverage:
    artifact_dirs: 34
    catalog_gap: 35.5
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 100.0
    commercial_clarity: 100.0
    contract_governance: 31.8
    contract_quality: 71.7
    developer_ergonomics: 80.4
    discoverability: 81.5
    governance: 31.8
    operational_transparency: 92.1
  previous_composite: 77.9
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 72.4
      derived: 0
      marker_coverage: 0.0
      total: 29
    mcp: first-party
    skills: derived
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/launchdarkly/refs/heads/main/screenshots/launchdarkly-2026-06-20T184335.png
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
website: https://launchdarkly.com/docs/home
---
