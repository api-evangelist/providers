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
    well_known_catalog: true
  schema_version: '0.2'
  score: 2.9
  scored_at: '2026-11-06'
api_count: 0
artifact_total: 1
common:
- group: other
  href: https://artifacts.apis.io/davinci-micro-fulfillment/hosts/davinci-micro-fulfillment-hosts.yml
  title: ''
  type: Hosts
  url: hosts/davinci-micro-fulfillment-hosts.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://davincimicrofulfillment.com/terms/
- group: operate
  title: ''
  type: StatusPage
  url: https://davincimicrofulfillment.com/status/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://davincimicrofulfillment.com/privacy-policy/
- group: start
  title: ''
  type: Login
  url: https://davincimicrofulfillment.com/login/
- group: auth
  href: https://artifacts.apis.io/davinci-micro-fulfillment/security/davinci-micro-fulfillment-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/davinci-micro-fulfillment-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://davincimicrofulfillment.com
coverage:
  checked: '2026-10-22'
  detail: API documentation is served as a JavaScript‑rendered SPA with no machine‑readable OpenAPI spec.
  evidence:
  - status: 200
    url: https://portal.davincimicrofulfillment.com/openapi.json
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-22'
description: DaVinci Micro Fulfillment provides end‑to‑end eCommerce fulfillment solutions for direct‑to‑consumer brands. Leveraging a network of micro‑fulfillment centers across the United States, it enables same‑day, 1‑day, and 2‑day delivery, optimizing inventory placement, reducing costs, and improving customer experience. The company offers services including network planning, inventory management, order processing, and integration with major marketplaces such as Walmart.
layout: provider
modified: '2026-10-22'
name: DaVinci Micro Fulfillment
nav: Providers
network: true
overview: DaVinci Micro Fulfillment is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Fulfillment, E-Commerce, Logistics, and Micro-Fulfillment.
random_paper: 4
score:
  band: minimal
  composite: 8.1
  coverage:
    artifact_dirs: 7
    catalog_earned: 25.0
    catalog_earned_first_party: 0.0
    catalog_gap: 90.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -5.0
  facets:
    access_clarity: 17.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 44.6
    operational_transparency: 7.9
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - united-states
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - north-america
  previous_composite: 13.1
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
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/davinci-micro-fulfillment/davinci-micro-fulfillment-2026-11-03T130319.png
security:
- kind: domain-security
  name: Davinci Micro Fulfillment Domain Security
  slug: davinci-micro-fulfillment-domain-security
  summary_line: TLSv1.3
slug: davinci-micro-fulfillment
tags:
- Company
- Fulfillment
- E-Commerce
- Logistics
- Micro-Fulfillment
- United States
website: https://davincimicrofulfillment.com
---
