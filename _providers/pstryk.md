---
access_model:
  confidence: low
  label: Open access
  onboarding: open
  pricing: unknown
  public: true
  source:
  - authentication
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
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 2.5
  scored_at: '2026-11-06'
api_count: 0
artifact_total: 5
common:
- group: agent
  href: https://artifacts.apis.io/pstryk/llms/pstryk-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/pstryk-llms.txt
- group: other
  href: https://artifacts.apis.io/pstryk/hosts/pstryk-hosts.yml
  title: ''
  type: Hosts
  url: hosts/pstryk-hosts.yml
- group: other
  href: https://artifacts.apis.io/pstryk/vendors/pstryk-vendors.yml
  title: ''
  type: Vendors
  url: vendors/pstryk-vendors.yml
- group: build
  href: https://artifacts.apis.io/pstryk/packages/pstryk-packages.yml
  title: ''
  type: SDKs
  url: packages/pstryk-packages.yml
- group: build
  href: https://artifacts.apis.io/pstryk/packages/pstryk-packages.yml
  title: ''
  type: Packages
  url: packages/pstryk-packages.yml
- group: auth
  href: https://artifacts.apis.io/pstryk/security/pstryk-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/pstryk-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://pstryk.pl/
- group: company
  title: ''
  type: Blog
  url: https://pstryk.pl/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://pstryk.pl/cennik
- group: commercial
  title: ''
  type: TermsOfService
  url: https://pstryk.pl/regulamin-pstryk-polecaj
coverage:
  checked: '2026-10-28'
  detail: Pstryk provides energy pricing services and does not expose a public API.
  evidence:
  - status: 200
    url: https://pstryk.pl/
  reason: not-a-software-company
  state: none
created: '2026-10-28'
description: Pstryk is a Polish energy technology company offering dynamic electricity pricing plans through its mobile application. It guarantees a maximum price, provides real‑time monitoring of consumption and costs, and enables users to switch electricity suppliers in three simple online steps. The service combines dynamic tariffs with optional solar storage and electric vehicle integration, aiming to reduce household energy bills.
image: https://images.prismic.io/pstryk/aO4mM55xUNkB17hp_offer-header-meta-img.webp?auto=format,compress&rect=0,0,1200,630&w=2400&h=1260
layout: provider
modified: '2026-10-28'
name: Pstryk
nav: Providers
network: true
overview: 'Pstryk is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Energy, Utilities, Fintech, and Poland.


  Pstryk''s developer surface includes engineering blog, pricing, and 8 more developer resources.'
plans:
- name: Pstryk Plans Pricing
  plan_count: 0
  slug: pstryk-plans-pricing
random_paper: 13
rate_limits:
- limit_count: 0
  name: Pstryk Rate Limits
  slug: pstryk-rate-limits
scopes:
- name: Pstryk Scopes
  scope_count: 0
  slug: pstryk-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: minimal
  composite: 10.4
  coverage:
    artifact_dirs: 22
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -2.6
  facets:
    access_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 8.3
    discoverability: 55.4
    operational_transparency: 0.0
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - poland
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - cee
    - europe
  previous_composite: 13.0
  provenance:
    conformance: unknown
    mcp: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Energy & Utilities
    regime_id: energy_utilities
    score: 20.5
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/pstryk/pstryk-2026-11-03T141701.png
security:
- kind: authentication
  name: Pstryk Authentication
  slug: pstryk-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Pstryk Domain Security
  slug: pstryk-domain-security
  summary_line: TLSv1.3 · DMARC
slug: pstryk
tags:
- Company
- Energy
- Utilities
- Fintech
- Poland
- Dynamic Pricing
website: https://pstryk.pl/
---
