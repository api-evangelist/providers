---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - security
  trial: false
  try_now: false
agent_readiness:
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: false
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 0.0
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: On-demand electric shuttle service API
  name: Circuit API
  slug: circuit-api
artifact_total: 2
common:
- group: other
  href: https://artifacts.apis.io/circuittransit/hosts/circuittransit-hosts.yml
  title: ''
  type: Hosts
  url: hosts/circuittransit-hosts.yml
- group: other
  href: https://artifacts.apis.io/circuittransit/vendors/circuittransit-vendors.yml
  title: ''
  type: Vendors
  url: vendors/circuittransit-vendors.yml
- group: company
  title: ''
  type: Newsroom
  url: https://www.ridecircuit.com/press
- group: start
  title: ''
  type: DeveloperPortal
  url: https://portal.ridecircuit.com/
- group: auth
  href: https://artifacts.apis.io/circuittransit/security/circuittransit-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/circuittransit-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.ridecircuit.com
- group: company
  title: ''
  type: Blog
  url: https://www.ridecircuit.com/blog
- group: docs
  title: ''
  type: Documentation
  url: https://www.ridecircuit.com/faq
- group: operate
  title: ''
  type: Support
  url: https://www.ridecircuit.com/contact
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.ridecircuit.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.ridecircuit.com/privacy
coverage:
  checked: '2026-10-08'
  detail: The provider's documentation pages are HTML only and no OpenAPI, GraphQL, or other machine‑readable contract was found.
  evidence:
  - status: 200
    url: https://www.ridecircuit.com/faq
  - status: 0
    url: https://api.ridecircuit.com/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-08'
description: Circuittransit (RideCircuit) provides on-demand electric shuttle services for cities, agencies, and private properties. It designs, launches, and operates low‑cost, accessible, eco‑friendly transportation solutions, handling vehicles, drivers, technology, and reporting in a single platform. The company also offers turnkey electric mobility solutions for communities, aiming to reduce congestion and emissions while improving mobility for riders.
layout: provider
modified: '2026-10-08'
name: Circuittransit
nav: Providers
network: true
overview: 'Circuittransit is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Transportation, Electric Vehicles, On-demand Mobility, and Software-as-a-Service.


  Circuittransit''s developer surface includes engineering blog, documentation, support, and 8 more developer resources.'
random_paper: 16
score:
  band: minimal
  composite: 9.4
  coverage:
    artifact_dirs: 9
    catalog_earned: 30.0
    catalog_earned_first_party: 0.0
    catalog_gap: 85.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -5.4
  facets:
    access_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 13.1
    discoverability: 54.5
    operational_transparency: 0.0
  previous_composite: 14.8
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 9.8
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/circuittransit/circuittransit-2026-11-03T124211.png
security:
- kind: domain-security
  name: Circuittransit Domain Security
  slug: circuittransit-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: circuittransit
tags:
- Company
- Transportation
- Electric Vehicles
- On-demand Mobility
- Software-as-a-Service
website: https://www.ridecircuit.com
---
