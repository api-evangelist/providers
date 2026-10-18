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
- description: Public API referenced in developer resources (none found).
  name: RideCake API
  slug: ridecake-api
artifact_total: 2
common:
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/cakebikes/refs/heads/main/hosts/cakebikes-hosts.yml
  title: ''
  type: Hosts
  url: hosts/cakebikes-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/cakebikes/refs/heads/main/vendors/cakebikes-vendors.yml
  title: ''
  type: Vendors
  url: vendors/cakebikes-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://ridecake.com/en-US/terms-for-purchasing-of-cake-products
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://ridecake.com/en-SE/privacy-policy
- group: commercial
  title: ''
  type: Pricing
  url: https://ridecake.com/en-SE/pricing-folksam-insurance
- group: company
  title: ''
  type: Newsroom
  url: https://ridecake.com/en-US/news
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/cakebikes/refs/heads/main/security/cakebikes-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/cakebikes-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://ridecake.com
coverage:
  checked: '2026-10-06'
  detail: Attempted to fetch OpenAPI spec at https://ridecake.com/openapi.json but received HTTP 500
  evidence:
  - status: 500
    url: https://ridecake.com/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-06'
description: Cake (brand CAKE) is a Scandinavian electric motorbike manufacturer offering high‑performance electric mopeds and motorcycles for commuters, off‑road riders and professionals. The company focuses on lightweight, quiet, zero‑emission vehicles and provides a range of models such as Makka, Kalk, Ösa, Bukk and others. Their website offers product details, specifications, pricing, support, and a story about the brand’s mission to accelerate e‑mobility.
image: https://cdn.sanity.io/images/n0u8owzc/production2/1819f416c0f84aa4130b6c62272835825c1a0379-1200x627.jpg?rect=3,0,1194,627&w=1200&h=630
layout: provider
modified: '2026-10-06'
name: Cakebikes
nav: Providers
network: true
overview: 'Cakebikes is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Electric Vehicles, Motorcycles, Scandinavia, Sustainable Transport, and CAKE.


  Cakebikes'' developer surface includes pricing and 7 more developer resources.'
random_paper: 6
score:
  band: emerging
  composite: 12.0
  coverage:
    artifact_dirs: 5
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 31.6
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 58.9
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
  name: Cakebikes Domain Security
  slug: cakebikes-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: cakebikes
tags:
- Electric Vehicles
- Motorcycles
- Scandinavia
- Sustainable Transport
- CAKE
website: https://ridecake.com
---
