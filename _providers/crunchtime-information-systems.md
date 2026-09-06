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
  - sandbox
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 5.9
  scored_at: '2026-09-05'
api_count: 1
apis:
- description: REST data-integration API for Crunchtime's Inventory Management, Labor & Scheduling, and Cruise products. GET and POST operations move employees, locations, budgets, categories, products, recipes, sal
  name: Crunchtime Inventory & Labor APIs
  slug: crunchtime-inventory-labor-apis
artifact_total: 5
common:
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.crunchtime.com/
- group: docs
  title: ''
  type: Documentation
  url: https://developer.crunchtime.com/docs/introduction
- group: docs
  title: ''
  type: APIReference
  url: https://developer.crunchtime.com/reference
- group: start
  title: ''
  type: GettingStarted
  url: https://developer.crunchtime.com/docs/getting-started-with-apis
- group: operate
  title: ''
  type: Support
  url: https://crunchtime.zendesk.com/hc/en-us
- group: company
  title: ''
  type: Blog
  url: https://www.crunchtime.com/blog
- group: start
  title: ''
  type: SignUp
  url: https://www.crunchtime.com/request-demo
- group: auth
  title: ''
  type: TrustCenter
  url: https://trust.crunchtime.com/
- group: auth
  title: ''
  type: Compliance
  url: https://trust.crunchtime.com/
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/crunchtime-information-systems-llms.txt
- group: auth
  title: ''
  type: Authentication
  url: authentication/crunchtime-information-systems-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/crunchtime-information-systems-conventions.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/crunchtime-information-systems-rate-limits.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/crunchtime-information-systems-changelog.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/crunchtime-information-systems-sandbox.yml
- group: agent
  title: ''
  type: X-MCPServerCandidate
  url: mcp/crunchtime-information-systems-mcp.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/crunchtime-information-systems-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/crunchtime-information-systems-domain-security.yml
created: '2026-07-17'
description: Crunchtime (Crunchtime Information Systems) is a Boston-based provider of AI-powered operations-management software for multi-unit restaurants, founded in 1995 and serving 850+ restaurant brands across 150,000+ locations. Its platform unifies inventory management, labor scheduling, kitchen/operations execution, and analytics. Crunchtime publishes a public developer hub for its Inventory & Labor and Cruise data-integration REST APIs, letting partners and customers push and pull employees, locations, budgets, products, recipes, sales/menu mix, purchase orders, inventory counts, time clock, and forecasting data. Backed by Battery Ventures.
image: https://logo.clearbit.com/crunchtime.com
layout: provider
modified: '2026-07-18'
name: Crunchtime Information Systems
nav: Providers
network: true
overview: 'Crunchtime Information Systems publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Restaurant, Food Service, Hospitality, and Inventory Management.


  Crunchtime Information Systems'' developer surface includes documentation, API reference, getting-started guide, support, engineering blog, signup flow, authentication, and 12 more developer resources.'
random_paper: 17
rate_limits:
- limit_count: 1
  name: Crunchtime Information Systems Rate Limits
  slug: crunchtime-information-systems-rate-limits
score:
  band: thin
  composite: 28.8
  coverage:
    artifact_dirs: 12
    catalog_earned: 45.0
    catalog_earned_first_party: 8.0
    catalog_gap: 70.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 28.9
    commercial_clarity: 28.9
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 53.0
    discoverability: 75.9
    governance: 0.0
    operational_transparency: 36.8
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - north-america
  previous_composite: 28.8
  provenance:
    mcp: derived
    skills: derived
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/crunchtime-information-systems/refs/heads/main/screenshots/crunchtime-information-systems-2026-07-25T210822.png
security:
- kind: authentication
  name: Crunchtime Information Systems Authentication
  slug: crunchtime-information-systems-authentication
  summary_line: apiKey · 4 schemes
- kind: domain-security
  name: Crunchtime Information Systems Domain Security
  slug: crunchtime-information-systems-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Crunchtime Information Systems Trust Center
  slug: crunchtime-information-systems-trust-center
  summary_line: SOC 2, ISO 27001
slug: crunchtime-information-systems
tags:
- Company
- Restaurant
- Food Service
- Hospitality
- Inventory Management
- Labor Scheduling
- Operations Management
- Back Office
- Supply Chain
website: https://developer.crunchtime.com/
---
