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
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: verified
    idempotency: false
    mcp_server: derived
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.2
  score: 45.3
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 1
  human_in_the_loop: 0
  name: Interos Agentic Access
  operation_count: 10
  slug: interos-agentic-access
  summary_line: 10 operations · 1 acting
api_count: 5
apis:
- description: The Groups API from Interos — 2 operation(s) for groups.
  name: Interos Groups API
  slug: interos-groups-api
- description: The health API from Interos — 1 operation(s) for health.
  name: Interos health API
  slug: interos-health-api
- description: The Organizations API from Interos — 2 operation(s) for organizations.
  name: Interos Organizations API
  slug: interos-organizations-api
- description: The Relationships API from Interos — 2 operation(s) for relationships.
  name: Interos Relationships API
  slug: interos-relationships-api
- description: The Watchtower API from Interos — 3 operation(s) for watchtower.
  name: Interos Watchtower API
  slug: interos-watchtower-api
artifact_total: 10
common:
- group: company
  title: ''
  type: Website
  url: https://www.interos.ai
- group: start
  title: ''
  type: DeveloperPortal
  url: https://api.interos.ai/docs
- group: docs
  title: ''
  type: Documentation
  url: https://api.interos.ai/docs
- group: docs
  title: ''
  type: APIReference
  url: https://api.interos.ai/docs
- group: start
  title: ''
  type: Login
  url: https://platform.interos.ai/login
- group: operate
  title: ''
  type: StatusPage
  url: https://status.interos.ai/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.interos.ai/termsofservice
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.interos.ai/privacy-policy/
- group: docs
  title: ''
  type: OpenAPI
  url: openapi/interos-openapi.json
- group: other
  title: ''
  type: Overlay
  url: overlays/interos-openapi-overlay.yaml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/interos-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/interos-llms.txt
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/interos-authentication.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/interos-agentic-access.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/interos-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/interos-problem-types.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/interos-rate-limits.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/interos-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/interos-conformance.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/interos-data-model.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/interos-well-known.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/interos-domain-security.yml
created: '2026-07-17'
description: Interos operates an automated supplier-resilience platform that maps and continuously monitors extended, multi-tier supply chains for Fortune 1000 companies and federal agencies. Its cloud-native, multi-tenant SaaS uses AI and a large B2B relationship graph to deliver real-time, multi-domain risk scores and alerts. The public Interos API (REST/JSON, OpenAPI 3.0.2) exposes organization search, organization and risk profiles, the supplier relationship graph, organization groups, custom fields, and scenario watchlists, authenticated with x-api-key and x-customer-id headers. Headquartered in Arlington, Virginia; backed by Kleiner Perkins.
image: https://logo.clearbit.com/interos.ai
layout: provider
mcp_servers:
- description: ''
  name: interos-mcp.yml
  slug: interos-mcpyml
modified: '2026-07-19'
name: Interos
nav: Providers
network: true
overview: 'Interos publishes 5 APIs on the [APIs.io](https://apis.io/) network, including Groups API, health API, Organizations API, and 2 more. Tagged areas include Company, Enterprise, Supply Chain, Risk Management, and Supplier Risk.


  Interos'' developer surface includes documentation, API reference, authentication, and 20 more developer resources.'
random_paper: 43
rate_limits:
- limit_count: 0
  name: Interos Rate Limits
  slug: interos-rate-limits
score:
  band: thin
  composite: 41.3
  delta: -1.1
  facets:
    commercial_clarity: 34.2
    contract_quality: 56.1
    developer_ergonomics: 38.6
    discoverability: 92.6
    governance: 11.5
    operational_transparency: 15.8
  previous_composite: 42.4
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 5
    mcp: derived
    skills: derived
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/interos/refs/heads/main/screenshots/interos-2026-07-25T222710.png
security:
- kind: authentication
  name: Interos Authentication
  slug: interos-authentication
  summary_line: apiKey · 2 schemes
- kind: domain-security
  name: Interos Domain Security
  slug: interos-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: interos
tags:
- Company
- Enterprise
- Supply Chain
- Risk Management
- Supplier Risk
- Third-Party Risk
- Artificial Intelligence
- API
website: https://www.interos.ai
---
