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
api_count: 0
artifact_total: 1
common:
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/cakejp/refs/heads/main/vendors/cakejp-vendors.yml
  title: ''
  type: Vendors
  url: vendors/cakejp-vendors.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/cakejp/refs/heads/main/hosts/cakejp-hosts.yml
  title: ''
  type: Hosts
  url: hosts/cakejp-hosts.yml
- group: operate
  title: ''
  type: Support
  url: https://support.cake.jp/hc/ja
- group: auth
  title: ''
  type: Security
  url: https://cake.jp/security/login_link
- group: start
  title: ''
  type: Login
  url: https://cake.jp/carts/login/
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/cakejp/refs/heads/main/security/cakejp-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/cakejp-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://cake.jp
coverage:
  checked: '2026-10-06'
  detail: The homepage returns a JavaScript shell with no machine‑readable API documentation.
  evidence:
  - status: 200
    url: https://cake.jp
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-06'
description: Cake.jp is a Japanese e‑commerce platform specializing in the online sale and delivery of cakes, sweets, and assorted confectionery. The site offers a wide range of products for occasions such as birthdays, holidays, and themed events, with options for custom designs, character cakes, and seasonal specialties. Customers can browse categories, place orders, and arrange delivery across Japan, while the platform provides membership, loyalty points, and promotional campaigns.
image: https://assets.cake.jp/bp/img/brand/og_image/new_sns_logo.jpg
layout: provider
modified: '2026-10-06'
name: Cakejp
nav: Providers
network: true
overview: 'Cakejp is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, E-Commerce, Japan, Confectionery, and Online Retail.


  Cakejp''s developer surface includes support and 6 more developer resources.'
random_paper: 6
score:
  band: minimal
  composite: 8.4
  coverage:
    artifact_dirs: 5
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 13.2
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 4.8
    discoverability: 48.2
    operational_transparency: 10.5
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 5.9
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Cakejp Domain Security
  slug: cakejp-domain-security
  summary_line: TLSv1.2 · HSTS · DMARC
slug: cakejp
tags:
- Company
- E-Commerce
- Japan
- Confectionery
- Online Retail
website: https://cake.jp
---
