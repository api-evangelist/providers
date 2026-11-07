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
    mcp_server: documented
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
  score: 3.1
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: Server-to-server car shipping quotes API for US routes only.
  name: CarHauler247 Quotes API
  slug: carhauler247-quotes-api
artifact_total: 2
common:
- group: agent
  href: https://artifacts.apis.io/carhauler247-com/llms/carhauler247-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/carhauler247-com-llms.txt
- group: other
  href: https://artifacts.apis.io/carhauler247-com/hosts/carhauler247-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/carhauler247-com-hosts.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://carhauler247.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://carhauler247.com/privacy
- group: start
  title: ''
  type: Login
  url: https://carhauler247.com/login
- group: auth
  href: https://artifacts.apis.io/carhauler247-com/security/carhauler247-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/carhauler247-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://carhauler247.com/
created: '2026-11-03'
description: CarHauler247 provides nationwide auto transport services, offering instant online quotes for shipping vehicles across the United States. Founded in 2020, the company emphasizes fast, affordable, and reliable door-to-door car shipping with full insurance coverage. Customers can obtain quotes within minutes, track shipments, and access carrier licensing information. The platform supports both open and enclosed transport options, catering to a wide range of vehicle types and customer needs.
image: https://carhauler247.com/img/logo-social-share-1200x630.png
layout: provider
modified: '2026-11-03'
name: CarHauler247
nav: Providers
network: true
overview: CarHauler247 is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, AutoTransport, Shipping, Logistics, and USA.
random_paper: 8
score:
  band: minimal
  composite: 9.2
  coverage:
    artifact_dirs: 8
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 17.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 66.1
    operational_transparency: 0.0
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - united-states
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - north-america
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 9.8
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Carhauler247 Com Domain Security
  slug: carhauler247-com-domain-security
  summary_line: TLSv1.2 · HSTS · DMARC
slug: carhauler247-com
tags:
- Company
- AutoTransport
- Shipping
- Logistics
- USA
website: https://carhauler247.com/
---
