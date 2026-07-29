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
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    asyncapi_events: false
    auth_clarity: true
    consent_identity: true
    dry_run_mode: false
    error_semantics: documented
    idempotency: false
    mcp_server: true
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.2
  score: 51.4
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 90
  human_in_the_loop: 0
  name: Sentry System Agentic Access
  operation_count: 200
  slug: sentry-system-agentic-access
  summary_line: 200 operations · 90 acting
api_count: 44
apis:
- description: Manage alerts (beta)
  name: Sentry Alerts API
  slug: sentry-system-alerts-api
- description: View monitor check-in history
  name: Sentry Check-Ins API
  slug: sentry-system-check-ins-api
- description: Manage project client keys (DSNs)
  name: Sentry Client Keys API
  slug: sentry-system-client-keys-api
- description: Manage commits associated with releases
  name: Sentry Commits API
  slug: sentry-system-commits-api
- description: Manage custom integrations
  name: Sentry Custom Integrations API
  slug: sentry-system-custom-integrations-api
- description: Manage custom dashboards and their widgets
  name: Sentry Dashboards API
  slug: sentry-system-dashboards-api
- description: Manage data forwarding configurations
  name: Sentry Data Forwarders API
  slug: sentry-system-data-forwarders-api
- description: Manage debug information files
  name: Sentry Debug Files API
  slug: sentry-system-debug-files-api
- description: Manage deployments of releases
  name: Sentry Deploys API
  slug: sentry-system-deploys-api
- description: Manage saved Discover queries
  name: Sentry Discover API
  slug: sentry-system-discover-api
- description: Manage project and organization environments
  name: Sentry Environments API
  slug: sentry-system-environments-api
- description: Access and manage error and transaction events
  name: Sentry Events API
  slug: sentry-system-events-api
- description: Query and analyze event data
  name: Sentry Explore API
  slug: sentry-system-explore-api
- description: Manage external issue links
  name: Sentry External Issues API
  slug: sentry-system-external-issues-api
- description: Manage external team mappings
  name: Sentry External Teams API
  slug: sentry-system-external-teams-api
- description: Manage external user mappings
  name: Sentry External Users API
  slug: sentry-system-external-users-api
- description: Manage inbound data filters
  name: Sentry Filters API
  slug: sentry-system-filters-api
- description: Manage integration installations
  name: Sentry Installations API
  slug: sentry-system-installations-api
- description: Manage third-party integrations
  name: Sentry Integrations API
  slug: sentry-system-integrations-api
- description: View user interactions within replays
  name: Sentry Interactions API
  slug: sentry-system-interactions-api
- description: Manage issue alert rules at the project level
  name: Sentry Issue Alerts API
  slug: sentry-system-issue-alerts-api
- description: Manage error issues
  name: Sentry Issues API
  slug: sentry-system-issues-api
- description: Manage organization members and their roles
  name: Sentry Members API
  slug: sentry-system-members-api
- description: Manage metric alert rules at the organization level
  name: Sentry Metric Alerts API
  slug: sentry-system-metric-alerts-api
- description: Analyze mobile application build artifacts
  name: Sentry Mobile Builds API
  slug: sentry-system-mobile-builds-api
- description: Manage cron job monitors
  name: Sentry Monitors API
  slug: sentry-system-monitors-api
- description: Manage Sentry organizations
  name: Sentry Organizations API
  slug: sentry-system-organizations-api
- description: Manage projects within organizations
  name: Sentry Projects API
  slug: sentry-system-projects-api
- description: Access replay recording segments
  name: Sentry Recording Segments API
  slug: sentry-system-recording-segments-api
- description: Manage files associated with releases
  name: Sentry Release Files API
  slug: sentry-system-release-files-api
- description: Manage software releases
  name: Sentry Releases API
  slug: sentry-system-releases-api
- description: Manage session replays
  name: Sentry Replays API
  slug: sentry-system-replays-api
- description: Manage organization repositories
  name: Sentry Repositories API
  slug: sentry-system-repositories-api
- description: Provision and manage organization members via SCIM
  name: Sentry SCIM Members API
  slug: sentry-system-scim-members-api
- description: Provision and manage teams via SCIM
  name: Sentry SCIM Teams API
  slug: sentry-system-scim-teams-api
- description: AI-powered issue analysis and fix suggestions
  name: Sentry Seer API
  slug: sentry-system-seer-api
- description: Manage project service hooks
  name: Sentry Service Hooks API
  slug: sentry-system-service-hooks-api
- description: Retrieve release health session statistics
  name: Sentry Sessions API
  slug: sentry-system-sessions-api
- description: Manage spike protection notification actions
  name: Sentry Spike Protection API
  slug: sentry-system-spike-protection-api
- description: Manage teams within organizations
  name: Sentry Teams API
  slug: sentry-system-teams-api
- description: Retrieve test result metrics and test suites
  name: Sentry Test Results API
  slug: sentry-system-test-results-api
- description: Manage repository upload tokens
  name: Sentry Tokens API
  slug: sentry-system-tokens-api
- description: Manage user feedback submissions
  name: Sentry User Feedback API
  slug: sentry-system-user-feedback-api
- description: Retrieve user-related information
  name: Sentry Users API
  slug: sentry-system-users-api
arazzos:
- description: Find a recent project event, attach user feedback to it, and confirm the feedback was recorded.
  name: Sentry Capture User Feedback for an Event
  slug: sentry-system-capture-user-feedback-workflow
- description: Create a cron-job monitor for an organization, confirm it, and list its check-ins.
  name: Sentry Create a Cron Monitor and Verify Check-ins
  slug: sentry-system-create-cron-monitor-workflow
- description: Create a metric alert rule for an organization, retrieve it, and confirm it appears in the rule list.
  name: Sentry Create a Metric Alert Rule
  slug: sentry-system-create-metric-alert-workflow
- description: Create a team, confirm it, add an existing organization member, and verify the team roster.
  name: Sentry Create a Team and Add a Member
  slug: sentry-system-create-team-add-member-workflow
- description: Create an organization release, confirm it, record a deploy to an environment, and list its deploys.
  name: Sentry Cut a Release and Record a Deploy
  slug: sentry-system-cut-release-deploy-workflow
- description: Confirm a project, grant a team access to it, and verify the team appears on the project.
  name: Sentry Grant a Team Access to a Project
  slug: sentry-system-grant-team-project-access-workflow
- description: Find an issue, inspect a tag's distribution and values, then bookmark and assign it for follow-up.
  name: Sentry Investigate an Issue's Tags
  slug: sentry-system-investigate-issue-tags-workflow
- description: Invite a new member to an organization, confirm the invite, add them to a team, and verify the roster.
  name: Sentry Invite a Member and Onboard to a Team
  slug: sentry-system-invite-member-onboard-team-workflow
- description: Create a new project under a team, confirm it, and mint a client key (DSN) for the SDK.
  name: Sentry Provision a Project and Client Key
  slug: sentry-system-provision-project-key-workflow
- description: List available Seer models, start an AI autofix for an issue, then poll until the fix completes.
  name: Sentry Run a Seer AI Autofix on an Issue
  slug: sentry-system-seer-autofix-issue-workflow
- description: Trigger a Prevent repository sync from GitHub, poll until it finishes, then list the synced repositories.
  name: Sentry Sync Prevent Repositories
  slug: sentry-system-sync-prevent-repos-workflow
- description: Find a high-priority unresolved issue in an organization, inspect it, then assign and resolve it.
  name: Sentry Triage and Resolve an Issue
  slug: sentry-system-triage-resolve-issue-workflow
artifact_total: 165
collections:
- collection_type: postman
  name: Sentry Alerts API
  slug: postman-sentry-alerts
- collection_type: postman
  name: Sentry API
  slug: postman-sentry-api
- collection_type: postman
  name: Sentry Crons API
  slug: postman-sentry-crons
- collection_type: postman
  name: Sentry Dashboards API
  slug: postman-sentry-dashboards
- collection_type: postman
  name: Sentry Discover API
  slug: postman-sentry-discover
- collection_type: postman
  name: Sentry Environments API
  slug: postman-sentry-environments
- collection_type: postman
  name: Sentry Events and Issues API
  slug: postman-sentry-events-issues
- collection_type: postman
  name: Sentry Explore API
  slug: postman-sentry-explore
- collection_type: postman
  name: Sentry Integration Platform API
  slug: postman-sentry-integration-platform
- collection_type: postman
  name: Sentry Integrations API
  slug: postman-sentry-integrations
- collection_type: postman
  name: Sentry Mobile Builds API
  slug: postman-sentry-mobile-builds
- collection_type: postman
  name: Sentry Monitors API
  slug: postman-sentry-monitors
- collection_type: postman
  name: Sentry Organizations API
  slug: postman-sentry-organizations
- collection_type: postman
  name: Sentry Prevent API
  slug: postman-sentry-prevent
- collection_type: postman
  name: Sentry Projects API
  slug: postman-sentry-projects
- collection_type: postman
  name: Sentry Releases API
  slug: postman-sentry-releases
- collection_type: postman
  name: Sentry Replays API
  slug: postman-sentry-replays
- collection_type: postman
  name: Sentry SCIM API
  slug: postman-sentry-scim
- collection_type: postman
  name: Sentry Seer API
  slug: postman-sentry-seer
- collection_type: postman
  name: Sentry Teams API
  slug: postman-sentry-teams
- collection_type: postman
  name: Sentry Users API
  slug: postman-sentry-users
- collection_type: open
  name: Sentry Alerts API
  slug: open-sentry-alerts
- collection_type: open
  name: Sentry API
  slug: open-sentry-api
- collection_type: open
  name: Sentry Crons API
  slug: open-sentry-crons
- collection_type: open
  name: Sentry Dashboards API
  slug: open-sentry-dashboards
- collection_type: open
  name: Sentry Discover API
  slug: open-sentry-discover
- collection_type: open
  name: Sentry Environments API
  slug: open-sentry-environments
- collection_type: open
  name: Sentry Events and Issues API
  slug: open-sentry-events-issues
- collection_type: open
  name: Sentry Explore API
  slug: open-sentry-explore
- collection_type: open
  name: Sentry Integration Platform API
  slug: open-sentry-integration-platform
- collection_type: open
  name: Sentry Integrations API
  slug: open-sentry-integrations
- collection_type: open
  name: Sentry Mobile Builds API
  slug: open-sentry-mobile-builds
- collection_type: open
  name: Sentry Monitors API
  slug: open-sentry-monitors
- collection_type: open
  name: Sentry Organizations API
  slug: open-sentry-organizations
- collection_type: open
  name: Sentry Prevent API
  slug: open-sentry-prevent
- collection_type: open
  name: Sentry Projects API
  slug: open-sentry-projects
- collection_type: open
  name: Sentry Releases API
  slug: open-sentry-releases
- collection_type: open
  name: Sentry Replays API
  slug: open-sentry-replays
- collection_type: open
  name: Sentry SCIM API
  slug: open-sentry-scim
- collection_type: open
  name: Sentry Seer API
  slug: open-sentry-seer
- collection_type: open
  name: Sentry Teams API
  slug: open-sentry-teams
- collection_type: open
  name: Sentry Users API
  slug: open-sentry-users
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/sentry-system-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/sentry-system-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/sentry-system-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/sentry-system-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/sentry-system-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/sentry-system-scopes.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/sentry-system-well-known.yml
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/sentry-system-security.txt
- group: build
  title: ''
  type: Packages
  url: packages/sentry-system-packages.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/sentry-system-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/sentry-system-llms.txt
- group: build
  title: ''
  type: CLI
  url: cli/sentry-system-cli.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/sentry-system-changelog.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/sentry-system-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/sentry-system-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/sentry-system-conformance.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/sentry-system-conventions.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/sentry-system-data-model.yml
- group: design
  title: ''
  type: Components
  url: components/sentry-system-components.yml
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/sentry/overview
- group: design
  title: ''
  type: Arazzo
  url: arazzo/sentry-system-capture-user-feedback-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/sentry-system-create-cron-monitor-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/sentry-system-create-metric-alert-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/sentry-system-create-team-add-member-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/sentry-system-cut-release-deploy-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/sentry-system-grant-team-project-access-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/sentry-system-investigate-issue-tags-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/sentry-system-invite-member-onboard-team-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/sentry-system-provision-project-key-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/sentry-system-seer-autofix-issue-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/sentry-system-sync-prevent-repos-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/sentry-system-triage-resolve-issue-workflow.yml
- group: start
  title: ''
  type: Portal
  url: https://sentry.io/
- group: company
  title: ''
  type: Website
  url: https://sentry.io/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.sentry.io/
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.sentry.io/product/sentry-basics/
- group: auth
  title: ''
  type: Authentication
  url: https://docs.sentry.io/api/auth/
- group: commercial
  title: ''
  type: Pricing
  url: https://sentry.io/pricing/
- group: company
  title: ''
  type: Blog
  url: https://blog.sentry.io/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/getsentry
- group: operate
  title: ''
  type: Discord
  url: https://discord.gg/sentry
- group: start
  title: ''
  type: Signup
  url: https://sentry.io/signup/
- group: start
  title: ''
  type: Login
  url: https://sentry.io/auth/login/
- group: operate
  title: ''
  type: Support
  url: https://sentry.zendesk.com/hc/en-us/
- group: operate
  title: ''
  type: Forums
  url: https://forum.sentry.io/
- group: operate
  title: ''
  type: ChangeLog
  url: https://sentry.io/changelog/
- group: auth
  title: ''
  type: Security
  url: https://sentry.io/security/
- group: operate
  title: ''
  type: Community
  url: https://sentry.io/community/
- group: other
  title: ''
  type: Self-Hosted
  url: https://docs.sentry.io/server/
- group: docs
  title: ''
  type: Documentation
  url: https://develop.sentry.dev/
- group: build
  title: ''
  type: CLI
  url: https://docs.sentry.io/cli/
- group: build
  title: ''
  type: SDKs
  url: https://docs.sentry.io/platforms/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.sentry.io/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://sentry.io/terms/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://sentry.io/privacy/
- group: agent
  title: ''
  type: LlmsText
  url: https://docs.sentry.io/llms.txt
created: '2024-01-15'
description: Sentry is an open-source error tracking and performance monitoring platform that helps developers identify, triage, and resolve issues in their applications in real-time.
finops:
- name: Sentry System Finops
  service_category: Observability / APM
  slug: sentry-system-finops
image: https://sentry-brand.storage.googleapis.com/sentry-logo-black.png
json_schemas:
- name: Sentry Alert Rule
  property_count: 12
  slug: sentry-alert-rule
- name: Sentry Event
  property_count: 14
  slug: sentry-event
- name: Sentry Issue
  property_count: 19
  slug: sentry-issue
- name: Sentry Monitor
  property_count: 9
  slug: sentry-monitor
- name: Sentry Organization
  property_count: 9
  slug: sentry-organization
- name: Sentry Project
  property_count: 14
  slug: sentry-project
- name: Sentry Release
  property_count: 14
  slug: sentry-release
- name: Sentry Replay
  property_count: 17
  slug: sentry-replay
- name: CheckIn
  property_count: 5
  slug: sentry-system-checkin
- name: ClientKey
  property_count: 9
  slug: sentry-system-clientkey
- name: Commit
  property_count: 5
  slug: sentry-system-commit
- name: Dashboard
  property_count: 5
  slug: sentry-system-dashboard
- name: DashboardSummary
  property_count: 5
  slug: sentry-system-dashboardsummary
- name: DataForwarder
  property_count: 3
  slug: sentry-system-dataforwarder
- name: DebugFile
  property_count: 8
  slug: sentry-system-debugfile
- name: Deploy
  property_count: 6
  slug: sentry-system-deploy
- name: Environment
  property_count: 4
  slug: sentry-system-environment
- name: Event
  property_count: 11
  slug: sentry-system-event
- name: ExternalIssue
  property_count: 5
  slug: sentry-system-externalissue
- name: Installation
  property_count: 5
  slug: sentry-system-installation
- name: Integration
  property_count: 8
  slug: sentry-system-integration
- name: Issue
  property_count: 15
  slug: sentry-system-issue
- name: IssueAlertRule
  property_count: 11
  slug: sentry-system-issuealertrule
- name: MetricAlertRule
  property_count: 12
  slug: sentry-system-metricalertrule
- name: Monitor
  property_count: 9
  slug: sentry-system-monitor
- name: MonitorAlert
  property_count: 4
  slug: sentry-system-monitoralert
- name: Organization
  property_count: 7
  slug: sentry-system-organization
- name: OrganizationDetail
  property_count: 9
  slug: sentry-system-organizationdetail
- name: OrganizationMember
  property_count: 10
  slug: sentry-system-organizationmember
- name: PreventRepository
  property_count: 5
  slug: sentry-system-preventrepository
- name: Project
  property_count: 12
  slug: sentry-system-project
- name: ProjectDetail
  property_count: 14
  slug: sentry-system-projectdetail
- name: RecordingSegment
  property_count: 4
  slug: sentry-system-recordingsegment
- name: Release
  property_count: 9
  slug: sentry-system-release
- name: ReleaseFile
  property_count: 7
  slug: sentry-system-releasefile
- name: Replay
  property_count: 17
  slug: sentry-system-replay
- name: Repository
  property_count: 7
  slug: sentry-system-repository
- name: SavedQuery
  property_count: 12
  slug: sentry-system-savedquery
- name: ScimGroup
  property_count: 5
  slug: sentry-system-scimgroup
- name: ScimListResponse
  property_count: 5
  slug: sentry-system-scimlistresponse
- name: ScimUser
  property_count: 7
  slug: sentry-system-scimuser
- name: SeerAutofixState
  property_count: 5
  slug: sentry-system-seerautofixstate
- name: SeerModel
  property_count: 4
  slug: sentry-system-seermodel
- name: SentryApp
  property_count: 11
  slug: sentry-system-sentryapp
- name: ServiceHook
  property_count: 6
  slug: sentry-system-servicehook
- name: SpikeProtectionAction
  property_count: 3
  slug: sentry-system-spikeprotectionaction
- name: Team
  property_count: 7
  slug: sentry-system-team
- name: TeamDetail
  property_count: 9
  slug: sentry-system-teamdetail
- name: TeamMember
  property_count: 8
  slug: sentry-system-teammember
- name: TestResult
  property_count: 6
  slug: sentry-system-testresult
- name: UptimeMonitor
  property_count: 7
  slug: sentry-system-uptimemonitor
- name: UserFeedback
  property_count: 6
  slug: sentry-system-userfeedback
- name: Widget
  property_count: 6
  slug: sentry-system-widget
- name: Sentry Team
  property_count: 9
  slug: sentry-team
json_structures:
- name: Sentry System Structure
  property_count: 0
  slug: sentry-system-structure
jsonld:
- class_count: 0
  name: Sentry Context
  property_count: 15
  slug: sentry-context
layout: provider
mcp_servers:
- description: ''
  name: sentry-system-mcp.yml
  slug: sentry-system-mcpyml
modified: '2026-06-20'
name: Sentry
nav: Providers
network: true
overview: 'Sentry publishes 44 APIs on the [APIs.io](https://apis.io/) network, including Alerts API, Check-Ins API, Client Keys API, and 41 more. Tagged areas include APM, Application Monitoring, Bug Tracking, Developer Tools, and Error Tracking.


  The Sentry catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Sentry''s developer surface includes authentication, CLI, changelog, developer portal, documentation, getting-started guide, pricing, and 49 more developer resources.'
plans:
- name: Sentry System Plans Pricing
  plan_count: 4
  slug: sentry-system-plans-pricing
random_paper: 13
rate_limits:
- limit_count: 2
  name: Sentry System Rate Limits
  slug: sentry-system-rate-limits
rules:
- name: Sentry API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: sentry-system-jsonschema-spectral-rules
scopes:
- name: Sentry System Scopes
  scope_count: 26
  slug: sentry-system-scopes
  summary_line: 26 scopes · authorizationCode
score:
  band: exemplar
  composite: 77.8
  delta: 0.3
  facets:
    commercial_clarity: 92.1
    contract_quality: 77.0
    developer_ergonomics: 71.7
    discoverability: 85.2
    governance: 69.8
    operational_transparency: 68.4
  previous_composite: 77.5
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 44
    mcp: first-party
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/sentry-system/refs/heads/main/screenshots/sentry-system-2026-06-20T193714.png
security:
- kind: authentication
  name: Sentry System Authentication
  slug: sentry-system-authentication
  summary_line: apiKey/http · 2 schemes
- kind: domain-security
  name: Sentry System Domain Security
  slug: sentry-system-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Sentry System Vulnerability Disclosure
  slug: sentry-system-vulnerability-disclosure
  summary_line: Hackerone · security.txt · contact published
- kind: trust-center
  name: Sentry System Trust Center
  slug: sentry-system-trust-center
  summary_line: SOC 2 Type I, SOC 2 Type II, ISO 27001, HIPAA
slug: sentry-system
tags:
- APM
- Application Monitoring
- Bug Tracking
- Developer Tools
- Error Tracking
- Observability
- Performance Monitoring
- Real-Time Monitoring
website: https://sentry.io/
---
