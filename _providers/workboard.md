---
access_model:
  confidence: medium
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - authentication
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
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: true
    idempotency: false
    mcp_server: verified
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 41.9
  scored_at: '2026-08-26'
agentic_access:
- acting_count: 32
  human_in_the_loop: 12
  name: Workboard Agentic Access
  operation_count: 63
  slug: workboard-agentic-access
  summary_line: 63 operations · 32 acting · 12 human-in-the-loop
api_count: 12
apis:
- description: SCIM 2.0 provisioning API for organization users — create, read, update (title and manager), and disable. Groups, bulk operations, and filtering are not supported. Authenticated with an admin-requeste
  name: WorkBoard SCIM API
  slug: workboard-scim-api
- description: The Activity (Action Items) API from WorkBoard — 2 operation(s) for activity (action items).
  name: WorkBoard Activity (Action Items) API
  slug: workboard-activity-action-items-api
- description: Read and write custom field values on Objectives, Key Results, Work Items, and Users
  name: WorkBoard custom-attributes API
  slug: workboard-custom-attributes-api
- description: '[WorkBoard''s help center documentation on Datastreams.](https://support.workboard.com/hc/en-us/articles/360006666652-Pushing-Business-Data-into-Workboard-with-Data-Streams#pushing-business-data-into-w'
  name: WorkBoard Datastream API
  slug: workboard-datastream-api
- description: The Goal (Objective) API from WorkBoard — 5 operation(s) for goal (objective).
  name: WorkBoard Goal (Objective) API
  slug: workboard-goal-objective-api
- description: The Metric (Key Result) API from WorkBoard — 6 operation(s) for metric (key result).
  name: WorkBoard Metric (Key Result) API
  slug: workboard-metric-key-result-api
- description: The Tags API from WorkBoard — 4 operation(s) for tags.
  name: WorkBoard Tags API
  slug: workboard-tags-api
- description: The Team API from WorkBoard — 4 operation(s) for team.
  name: WorkBoard Team API
  slug: workboard-team-api
- description: The User API from WorkBoard — 2 operation(s) for user.
  name: WorkBoard User API
  slug: workboard-user-api
- description: The User Goals (User Objectives) API from WorkBoard — 2 operation(s) for user goals (user objectives).
  name: WorkBoard User Goals (User Objectives) API
  slug: workboard-user-goals-user-objectives-api
- description: The Webhook API from WorkBoard — 1 operation(s) for webhook.
  name: WorkBoard Webhook API
  slug: workboard-webhook-api
- description: '[WorkBoard''s help center documentation on Workstreams.](https://support.workboard.com/hc/en-us/articles/115005163567-Workstreams#workstreams-0-0)'
  name: WorkBoard Workstream API
  slug: workboard-workstream-api
artifact_total: 32
asyncapis:
- description: ''
  name: Workboard Webhooks
  slug: workboard-webhooks
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: WorkBoard External Public Activity (Action Items) Activity (Action Items) Activity (Action Items) API
  slug: open-workboard-activity-action-items-api
- collection_type: open
  name: WorkBoard External Public Activity (Action Items) Activity (Action Items) custom-attributes API
  slug: open-workboard-custom-attributes-api
- collection_type: open
  name: WorkBoard External Public Activity (Action Items) Activity (Action Items) Datastream API
  slug: open-workboard-datastream-api
- collection_type: open
  name: WorkBoard External Public Activity (Action Items) Activity (Action Items) Goal (Objective) API
  slug: open-workboard-goal-objective-api
- collection_type: open
  name: WorkBoard External Public Activity (Action Items) Activity (Action Items) Metric (Key Result) API
  slug: open-workboard-metric-key-result-api
- collection_type: open
  name: WorkBoard External Public Activity (Action Items) Activity (Action Items) Tags API
  slug: open-workboard-tags-api
- collection_type: open
  name: WorkBoard External Public Activity (Action Items) Activity (Action Items) Team API
  slug: open-workboard-team-api
- collection_type: open
  name: WorkBoard External Public Activity (Action Items) Activity (Action Items) User API
  slug: open-workboard-user-api
- collection_type: open
  name: WorkBoard External Public Activity (Action Items) Activity (Action Items) User Goals (User Objectives) API
  slug: open-workboard-user-goals-user-objectives-api
- collection_type: open
  name: WorkBoard External Public Activity (Action Items) Activity (Action Items) Webhook API
  slug: open-workboard-webhook-api
- collection_type: open
  name: WorkBoard External Public Activity (Action Items) Activity (Action Items) Workstream API
  slug: open-workboard-workstream-api
common:
- group: other
  title: ''
  type: Overlay
  url: overlays/workboard-external-v1-overlay.yaml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/workboard-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/workboard-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/workboard-authentication.yml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://www.workboard.com/developer
- group: docs
  title: ''
  type: Documentation
  url: https://apidocs.myworkboard.com/
- group: docs
  title: ''
  type: APIReference
  url: https://apidocs.myworkboard.com/
- group: start
  title: ''
  type: GettingStarted
  url: https://www.workboard.com/developer
- group: operate
  title: ''
  type: Support
  url: https://support.myworkboard.com/en/
- group: company
  title: ''
  type: Blog
  url: https://www.workboard.com/resources/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/workboard
- group: start
  title: ''
  type: Login
  url: https://www.myworkboard.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.workboard.com/legal/terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.workboard.com/legal/privacy-policy
- group: operate
  title: ''
  type: StatusPage
  url: https://workboard.statuspage.io/
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/workboard-lifecycle.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/workboard-changelog.yml
- group: agent
  title: ''
  type: MCPServer
  url: https://www.myworkboard.com/wb/mcp
- group: agent
  title: ''
  type: MCPServer
  url: mcp/workboard-mcp.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/workboard-llms.txt
- group: build
  title: ''
  type: Packages
  url: packages/workboard-packages.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/workboard-well-known.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/workboard-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: https://www.workboard.com/security
- group: auth
  title: ''
  type: TrustCenter
  url: security/workboard-trust-center.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/workboard-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: https://www.workboard.com/security
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/workboard-problem-types.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/workboard-conventions.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/workboard-data-model.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/workboard-webhooks.yml
created: '2026-07-17'
description: WorkBoard (WorkBoardAI) is an AI-native strategy, OKR, and strategic portfolio management platform used by enterprises like Cisco, AstraZeneca, and Mercedes-Benz to connect strategy pillars, outcomes, investments, and OKRs. Its External REST API (v1) exposes users, teams, goals (objectives), metrics (key results), action items, workstreams, and datastreams; the Public API v2 manages custom attributes; a SCIM 2.0 API handles user provisioning; and a published MCP server gives AI agents scoped access to OKRs, KPIs, scorecards, business reviews, and meetings.
image: https://img.cdn.myworkboard.com/wb/images/icons/login_logo.png
layout: provider
mcp_servers:
- description: ''
  name: WorkBoard MCP Server
  slug: workboard-mcp-server
- description: ''
  name: WorkBoard MCP Server manifest
  slug: workboard-mcp-server-manifest
modified: '2026-07-21'
name: WorkBoard
nav: Providers
network: true
overview: 'WorkBoard publishes 11 APIs on the [APIs.io](https://apis.io/) network, including Activity (Action Items) API, custom-attributes API, Datastream API, and 8 more. Tagged areas include OKRs, Strategy Execution, Goals, Key Results, and Enterprise.


  The WorkBoard catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  WorkBoard''s developer surface includes authentication, documentation, API reference, getting-started guide, support, engineering blog, changelog, and 25 more developer resources.'
random_paper: 5
score:
  band: developing
  composite: 50.0
  delta: 0.0
  facets:
    access_clarity: 43.4
    commercial_clarity: 43.4
    contract_governance: 30.3
    contract_quality: 60.1
    developer_ergonomics: 42.3
    discoverability: 74.1
    governance: 30.3
    operational_transparency: 52.6
  previous_composite: 50.0
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 11
    mcp: first-party
    skills: derived
  schema_version: 0.15.0
  scored_at: '2026-08-26'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/workboard/refs/heads/main/screenshots/workboard-2026-08-17T082939.png
security:
- kind: authentication
  name: Workboard Authentication
  slug: workboard-authentication
  summary_line: http/oauth2 · 2 schemes
- kind: domain-security
  name: Workboard Domain Security
  slug: workboard-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Workboard Vulnerability Disclosure
  slug: workboard-vulnerability-disclosure
  summary_line: Hackerone · contact published
- kind: trust-center
  name: Workboard Trust Center
  slug: workboard-trust-center
  summary_line: SOC 2 Type 2, ISO/IEC 27001, GDPR
slug: workboard
tags:
- OKRs
- Strategy Execution
- Goals
- Key Results
- Enterprise
- AI Agents
- Performance Management
- Strategic Portfolio Management
website: https://www.workboard.com/developer
---
