---
agent_readiness:
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: platform
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
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 4.5
  scored_at: '2026-10-04'
api_count: 1
apis:
- description: GraphQL API for Bluetokaicoffeeroasters e‑commerce platform
  name: Bluetokaicoffeeroasters API
  slug: bluetokaicoffeeroasters-api
artifact_total: 2
common:
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/bluetokaicoffeeroasters/refs/heads/main/llms/bluetokaicoffeeroasters-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/bluetokaicoffeeroasters-llms.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/bluetokaicoffeeroasters/refs/heads/main/well-known/bluetokaicoffeeroasters-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/bluetokaicoffeeroasters-well-known.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/bluetokaicoffeeroasters/refs/heads/main/hosts/bluetokaicoffeeroasters-hosts.yml
  title: ''
  type: Hosts
  url: hosts/bluetokaicoffeeroasters-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/bluetokaicoffeeroasters/refs/heads/main/vendors/bluetokaicoffeeroasters-vendors.yml
  title: ''
  type: Vendors
  url: vendors/bluetokaicoffeeroasters-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://bluetokaicoffee.com/pages/terms-and-conditions
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://bluetokaicoffee.com/pages/privacy-policy
- group: company
  title: ''
  type: Newsroom
  url: https://bluetokaicoffee.com/blogs/press
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/bluetokaicoffeeroasters/refs/heads/main/security/bluetokaicoffeeroasters-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/bluetokaicoffeeroasters-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://bluetokaicoffee.com
created: '2026-09-29'
description: Blue Tokai Coffee Roasters is an Indian specialty coffee company founded in 2013, roasting and selling fresh coffee beans, capsules, and ready‑to‑drink beverages. The company operates an e‑commerce site offering subscriptions, wholesale, and retail sales, and maintains a blog, brewing guides, and community recipes. It provides a developer portal for its e‑commerce APIs, enabling partners to integrate product catalogs, orders, and customer data.
image: http://bluetokaicoffee.com/cdn/shop/files/og-image_fb86e907-95f5-4bce-a80f-c940e284474d.jpg?v=1692794605
layout: provider
modified: '2026-09-29'
name: Bluetokaicoffeeroasters
nav: Providers
network: true
overview: Bluetokaicoffeeroasters publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Coffee, E-Commerce, Specialty Coffee, India, and Roasting.
random_paper: 17
score:
  band: emerging
  composite: 11.4
  coverage:
    artifact_dirs: 6
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 75.0
    operational_transparency: 0.0
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - india
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - india-south-asia
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 13.7
  schema_version: 0.23.0
  scored_at: '2026-10-04'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Bluetokaicoffeeroasters Domain Security
  slug: bluetokaicoffeeroasters-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: bluetokaicoffeeroasters
tags:
- Coffee
- E-Commerce
- Specialty Coffee
- India
- Roasting
website: https://bluetokaicoffee.com
---
