---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
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
    error_semantics: documented
    event_surface_described: false
    idempotency: verified
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 27.5
  scored_at: '2026-09-01'
agentic_access:
- acting_count: 17
  human_in_the_loop: 0
  name: Rhythms Agentic Access
  operation_count: 31
  slug: rhythms-agentic-access
  summary_line: 31 operations · 17 acting
api_count: 1
apis:
- description: The access_requests API from Rhythms — 3 operation(s) for access_requests.
  name: Rhythms access_requests API
  slug: rhythms-access-requests-api
- description: The chat_refresh_threads API from Rhythms — 1 operation(s) for chat_refresh_threads.
  name: Rhythms chat_refresh_threads API
  slug: rhythms-chat-refresh-threads-api
- description: The connector_requests API from Rhythms — 1 operation(s) for connector_requests.
  name: Rhythms connector_requests API
  slug: rhythms-connector-requests-api
- description: The data_sources API from Rhythms — 1 operation(s) for data_sources.
  name: Rhythms data_sources API
  slug: rhythms-data-sources-api
- description: The documents API from Rhythms — 4 operation(s) for documents.
  name: Rhythms documents API
  slug: rhythms-documents-api
- description: The explorer_views API from Rhythms — 1 operation(s) for explorer_views.
  name: Rhythms explorer_views API
  slug: rhythms-explorer-views-api
- description: The labels API from Rhythms — 2 operation(s) for labels.
  name: Rhythms labels API
  slug: rhythms-labels-api
- description: The mention_access_checks API from Rhythms — 1 operation(s) for mention_access_checks.
  name: Rhythms mention_access_checks API
  slug: rhythms-mention-access-checks-api
- description: The notifications API from Rhythms — 1 operation(s) for notifications.
  name: Rhythms notifications API
  slug: rhythms-notifications-api
- description: The objectives API from Rhythms — 1 operation(s) for objectives.
  name: Rhythms objectives API
  slug: rhythms-objectives-api
- description: The teams API from Rhythms — 6 operation(s) for teams.
  name: Rhythms teams API
  slug: rhythms-teams-api
- description: The time_periods API from Rhythms — 2 operation(s) for time_periods.
  name: Rhythms time_periods API
  slug: rhythms-time-periods-api
- description: The users API from Rhythms — 1 operation(s) for users.
  name: Rhythms users API
  slug: rhythms-users-api
artifact_total: 32
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Rhythms (params in:body) access_requests API
  slug: open-rhythms-access-requests-api
- collection_type: open
  name: Rhythms (params in:body) access_requests chat_refresh_threads API
  slug: open-rhythms-chat-refresh-threads-api
- collection_type: open
  name: Rhythms (params in:body) access_requests connector_requests API
  slug: open-rhythms-connector-requests-api
- collection_type: open
  name: Rhythms (params in:body) access_requests data_sources API
  slug: open-rhythms-data-sources-api
- collection_type: open
  name: Rhythms (params in:body) access_requests documents API
  slug: open-rhythms-documents-api
- collection_type: open
  name: Rhythms (params in:body) access_requests explorer_views API
  slug: open-rhythms-explorer-views-api
- collection_type: open
  name: Rhythms (params in:body) access_requests labels API
  slug: open-rhythms-labels-api
- collection_type: open
  name: Rhythms (params in:body) access_requests mention_access_checks API
  slug: open-rhythms-mention-access-checks-api
- collection_type: open
  name: Rhythms (params in:body) access_requests notifications API
  slug: open-rhythms-notifications-api
- collection_type: open
  name: Rhythms (params in:body) access_requests objectives API
  slug: open-rhythms-objectives-api
- collection_type: open
  name: Rhythms (params in:body) access_requests teams API
  slug: open-rhythms-teams-api
- collection_type: open
  name: Rhythms (params in:body) access_requests time_periods API
  slug: open-rhythms-time-periods-api
- collection_type: open
  name: Rhythms (params in:body) access_requests users API
  slug: open-rhythms-users-api
common:
- group: other
  title: ''
  type: Overlay
  url: overlays/rhythms-openapi-overlay.yaml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/rhythms-domain-security.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/rhythms-agentic-access.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/rhythms-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/rhythms-conventions.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/rhythms-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/rhythms-lifecycle.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/rhythms-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/rhythms-llms.txt
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: company
  title: ''
  type: Website
  url: https://www.rhythms.ai/
- group: start
  title: ''
  type: SignUp
  url: https://app.rhythms.ai/auth/signup
- group: start
  title: ''
  type: Login
  url: https://app.rhythms.ai/auth/signin
- group: commercial
  title: ''
  type: Pricing
  url: https://app.rhythms.ai/pricing
- group: company
  title: ''
  type: Blog
  url: https://app.rhythms.ai/blog
- group: commercial
  title: ''
  type: TermsOfService
  url: https://app.rhythms.ai/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://app.rhythms.ai/privacy-policy
- group: operate
  title: ''
  type: Support
  url: https://app.rhythms.ai/faq
- group: operate
  title: ''
  type: StatusPage
  url: https://status.rhythms.ai/
- group: auth
  title: ''
  type: TrustCenter
  url: https://trust.rhythms.ai/
created: '2026-07-17'
description: Rhythms is an AI operating partner for teams, built by the team behind Ally.io and Microsoft Viva Goals. It automates business reviews, pre-briefs, reports, and OKR/goal tracking, surfaces execution risks early, and keeps organizational alignment visible across hundreds of connected business tools. Rhythms exposes a multi-tenant REST API (api.rhythms.ai) covering documents, teams, users, labels, OKR objectives and time periods, data sources, connector and access requests, and explorer views, with page-based pagination and a Ransack-based filtering DSL. It also supports custom Model Context Protocol (MCP) integrations so agents can connect to the platform. Backed by Accel.
image: https://www.rhythms.ai/favicon.ico
layout: provider
mcp_servers:
- description: ''
  name: Rhythms MCP Server
  slug: rhythms-mcp-server
modified: '2026-07-21'
name: Rhythms
nav: Providers
network: true
overview: 'Rhythms publishes 13 APIs on the [APIs.io](https://apis.io/) network, including access_requests API, chat_refresh_threads API, connector_requests API, and 10 more. Tagged areas include Company, Artificial Intelligence, Productivity, Goal Tracking, and OKR.


  Rhythms'' developer surface includes authentication, signup flow, pricing, engineering blog, support, and 15 more developer resources.'
random_paper: 6
score:
  band: thin
  composite: 27.6
  coverage:
    artifact_dirs: 15
    catalog_gap: 78.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 14.5
    commercial_clarity: 14.5
    contract_governance: 4.5
    contract_quality: 47.2
    developer_ergonomics: 13.7
    discoverability: 75.9
    governance: 4.5
    operational_transparency: 15.8
  previous_composite: 27.6
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 13
    mcp: derived
    skills: derived
  schema_version: 0.17.2
  scored_at: '2026-09-01'
  trend: flat
security:
- kind: authentication
  name: Rhythms Authentication
  slug: rhythms-authentication
  summary_line: undocumented · 0 schemes
- kind: domain-security
  name: Rhythms Domain Security
  slug: rhythms-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Rhythms Trust Center
  slug: rhythms-trust-center
  summary_line: trust center published
slug: rhythms
tags:
- Company
- Artificial Intelligence
- Productivity
- Goal Tracking
- OKR
- Workflow-Automation
- Team Collaboration
- Business Reviews
- MCP
website: https://www.rhythms.ai/
---
