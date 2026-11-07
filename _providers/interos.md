---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - authentication
  - rate-limits
  - security
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
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: false
    pagination_ratio: paginated
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 28.4
  scored_at: '2026-11-06'
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
  name: Interos Health API
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
- baseURL: https://api.interos.ai
  baseurl_source: declared
  description: My Data endpoints are available exclusively to customers with the My Data Attributes feature enabled. If you don't have access, talk to your CSM to enable first-party data.
  name: Interos My Data API
  slug: interos-my-data-api
artifact_total: 19
collections:
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
- group: company
  title: ''
  type: Blog
  url: https://www.interos.ai/press
- group: other
  href: https://artifacts.apis.io/interos/capabilities/interos-capability-edges.yml
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
  href: https://artifacts.apis.io/interos/openapi/_original/interos-openapi.json
  title: ''
  type: OpenAPI
  url: openapi/_original/interos-openapi.json
- group: other
  href: https://artifacts.apis.io/interos/overlays/interos-openapi-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/interos-openapi-overlay.yaml
- group: agent
  href: https://artifacts.apis.io/interos/mcp/interos-mcp.yml
  title: ''
  type: X-MCPServerCandidate
  url: mcp/interos-mcp.yml
- group: agent
  href: https://artifacts.apis.io/interos/llms/interos-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/interos-llms.txt
- group: agent
  href: https://artifacts.apis.io/interos/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: auth
  href: https://artifacts.apis.io/interos/authentication/interos-authentication.yml
  title: ''
  type: Authentication
  url: authentication/interos-authentication.yml
- group: agent
  href: https://artifacts.apis.io/interos/agentic-access/interos-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/interos-agentic-access.yml
- group: design
  href: https://artifacts.apis.io/interos/conventions/interos-conventions.yml
  title: ''
  type: Conventions
  url: conventions/interos-conventions.yml
- group: design
  href: https://artifacts.apis.io/interos/errors/interos-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/interos-problem-types.yml
- group: operate
  href: https://artifacts.apis.io/interos/rate-limits/interos-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/interos-rate-limits.yml
- group: design
  href: https://artifacts.apis.io/interos/lifecycle/interos-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/interos-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/interos/conformance/interos-conformance.yml
  title: ''
  type: Conformance
  url: conformance/interos-conformance.yml
- group: design
  href: https://artifacts.apis.io/interos/data-model/interos-data-model.yml
  title: ''
  type: DataModel
  url: data-model/interos-data-model.yml
- group: agent
  href: https://artifacts.apis.io/interos/well-known/interos-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/interos-well-known.yml
- group: auth
  href: https://artifacts.apis.io/interos/security/interos-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/interos-domain-security.yml
created: '2026-07-17'
description: Interos operates an automated supplier-resilience platform that maps and continuously monitors extended, multi-tier supply chains for Fortune 1000 companies and federal agencies. Its cloud-native, multi-tenant SaaS uses AI and a large B2B relationship graph to deliver real-time, multi-domain risk scores and alerts. The public Interos API (REST/JSON, OpenAPI 3.0.2) exposes organization search, organization and risk profiles, the supplier relationship graph, organization groups, custom fields, and scenario watchlists, authenticated with x-api-key and x-customer-id headers. Headquartered in Arlington, Virginia; backed by Kleiner Perkins.
image: https://logo.clearbit.com/interos.ai
layout: provider
modified: '2026-10-06'
name: Interos
nav: Providers
network: true
overview: 'Interos publishes 6 API contracts indexed on the [APIs.io](https://apis.io/) network, including Groups API, Health API, Organizations API, and 3 more. Tagged areas include Company, Enterprise, Supply Chain, Risk Management, and Supplier Risk.


  The Interos catalog on APIs.io includes 1 Spectral governance ruleset.


  Interos'' developer surface includes engineering blog, documentation, API reference, authentication, and 21 more developer resources.'
random_paper: 4
rate_limits:
- limit_count: 2
  name: Interos Rate Limits
  slug: interos-rate-limits
rules:
- authorship: generated
  effective_rule_count: 101
  extends:
  - spectral:oas
  name: Interos API Rules
  rule_count: 60
  severity_counts:
    error: 47
    hint: 0
    info: 3
    warn: 10
  slug: interos-rules
score:
  band: developing
  composite: 42.1
  coverage:
    artifact_dirs: 24
    catalog_earned: 49.5
    catalog_earned_first_party: 8.0
    catalog_gap: 65.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.8
  facets:
    access_clarity: 27.6
    contract_governance: 18.2
    contract_quality: 53.6
    developer_ergonomics: 42.3
    discoverability: 73.2
    operational_transparency: 36.8
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - united-states
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - north-america
  previous_composite: 41.3
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 54.5
      total: 11
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 22.7
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/interos/interos-2026-07-25T222710.png
security:
- kind: authentication
  name: Interos Authentication
  slug: interos-authentication
  summary_line: apiKey · 2 schemes
- kind: domain-security
  name: Interos Domain Security
  slug: interos-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
skill_count: 3
skills:
- name: Look up an organization and read its risk profile
  slug: interos-lookup-organization-risk
- name: Map an organization's supplier network
  slug: interos-map-supplier-network
- name: Monitor organizations on a scenario watchlist
  slug: interos-monitor-scenario-watchlist
slug: interos
tags:
- Company
- Enterprise
- Supply Chain
- Risk Management
- Supplier Risk
- Third-Party Risk Management
- Artificial Intelligence
website: https://www.interos.ai
---
