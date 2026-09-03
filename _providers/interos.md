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
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 26.4
  scored_at: '2026-09-03'
agentic_access:
- acting_count: 1
  human_in_the_loop: 0
  name: Interos Agentic Access
  operation_count: 10
  slug: interos-agentic-access
  summary_line: 10 operations · 1 acting
api_count: 1
apis:
- baseURL: https://api.interos.ai
  baseurl_source: declared
  description: The Groups API from Interos — 2 operation(s) for groups.
  name: Interos Groups API
  slug: interos-groups-api
- baseURL: https://api.interos.ai
  baseurl_source: declared
  description: The health API from Interos — 1 operation(s) for health.
  name: Interos health API
  slug: interos-health-api
- baseURL: https://api.interos.ai
  baseurl_source: declared
  description: The Organizations API from Interos — 2 operation(s) for organizations.
  name: Interos Organizations API
  slug: interos-organizations-api
- baseURL: https://api.interos.ai
  baseurl_source: declared
  description: The Relationships API from Interos — 2 operation(s) for relationships.
  name: Interos Relationships API
  slug: interos-relationships-api
- baseURL: https://api.interos.ai
  baseurl_source: declared
  description: The Watchtower API from Interos — 3 operation(s) for watchtower.
  name: Interos Watchtower API
  slug: interos-watchtower-api
artifact_total: 15
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Interos Groups API
  slug: open-interos-groups-api
- collection_type: open
  name: Interos Groups health API
  slug: open-interos-health-api
- collection_type: open
  name: Interos Groups Organizations API
  slug: open-interos-organizations-api
- collection_type: open
  name: Interos Groups Relationships API
  slug: open-interos-relationships-api
- collection_type: open
  name: Interos Groups Watchtower API
  slug: open-interos-watchtower-api
common:
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/interos-capability-edges.yml
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
  url: openapi/_original/interos-openapi.json
- group: other
  title: ''
  type: Overlay
  url: overlays/interos-openapi-overlay.yaml
- group: agent
  title: ''
  type: X-MCPServerCandidate
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
modified: '2026-07-19'
name: Interos
nav: Providers
network: true
overview: 'Interos publishes 5 APIs on the [APIs.io](https://apis.io/) network, including Groups API, health API, Organizations API, and 2 more. Tagged areas include Company, Enterprise, Supply Chain, Risk Management, and Supplier Risk.


  Interos'' developer surface includes documentation, API reference, authentication, and 21 more developer resources.'
random_paper: 16
rate_limits:
- limit_count: 2
  name: Interos Rate Limits
  slug: interos-rate-limits
score:
  band: developing
  composite: 40.3
  coverage:
    artifact_dirs: 18
    catalog_gap: 70.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 27.6
    commercial_clarity: 27.6
    contract_governance: 4.5
    contract_quality: 55.5
    developer_ergonomics: 39.9
    discoverability: 75.9
    governance: 4.5
    operational_transparency: 36.8
  previous_composite: 40.3
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
  schema_version: 0.18.2
  scored_at: '2026-09-03'
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
website: https://www.interos.ai
---
