---
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
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 0.0
  scored_at: '2026-10-17'
api_count: 1
apis:
- description: API for Citykart retail platform
  name: Citykart API
  slug: citykart-api
artifact_total: 2
common:
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/citykart/refs/heads/main/hosts/citykart-hosts.yml
  title: ''
  type: Hosts
  url: hosts/citykart-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/citykart/refs/heads/main/vendors/citykart-vendors.yml
  title: ''
  type: Vendors
  url: vendors/citykart-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://citykart.co.in/terms-of-use/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://citykart.co.in/privacy-statement/
- group: company
  title: ''
  type: Newsroom
  url: https://citykart.co.in/media/
- group: start
  title: ''
  type: Login
  url: https://citykart.co.in/login/
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/citykart/refs/heads/main/security/citykart-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/citykart-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://citykart.co.in
coverage:
  detail: the company publishes no developer documentation host and no machine-readable contract on its own domain
  evidence:
  - status: 200
    url: https://citykart.co.in
  - status: 403
    url: https://equityzen.com/company/citykart
  reason: no-developer-program
  state: none
created: '2026-10-08'
description: Citykart is an Indian value‑fashion retailer operating over 180 stores across more than 120 cities in 14 Indian states. It offers affordable apparel, footwear, accessories and home‑needs for men, women and children, targeting tier‑II and tier‑III markets. The company emphasizes quality, low prices and a wide‑reach physical presence, serving over 1.7 crore customers. Its online presence includes a corporate site citykart.co.in with brand information, store locator, career listings and corporate policies.
layout: provider
modified: '2026-10-08'
name: Citykart
nav: Providers
network: true
overview: Citykart is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Fashion Retail, Apparel, Footwear, Accessories, and Home Essentials.
random_paper: 17
score:
  band: emerging
  composite: 12.2
  coverage:
    artifact_dirs: 6
    catalog_earned: 30.0
    catalog_earned_first_party: 0.0
    catalog_gap: 85.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 34.2
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 55.4
    operational_transparency: 0.0
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 13.7
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Citykart Domain Security
  slug: citykart-domain-security
  summary_line: TLSv1.3 · DMARC
slug: citykart
tags:
- Fashion Retail
- Apparel
- Footwear
- Accessories
- Home Essentials
- Family Shopping
- Indian Market
website: https://citykart.co.in
---
