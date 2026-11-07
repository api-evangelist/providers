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
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 21.8
  scored_at: '2026-11-06'
api_count: 0
artifact_total: 1
common:
- group: agent
  href: https://artifacts.apis.io/cartrevolt-com/well-known/cartrevolt-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/cartrevolt-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/cartrevolt-com/hosts/cartrevolt-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/cartrevolt-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/cartrevolt-com/vendors/cartrevolt-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/cartrevolt-com-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://cartrevolt.com/terms
- group: operate
  title: ''
  type: Support
  url: https://cartrevolt.com/help
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://cartrevolt.com/privacy
- group: start
  title: ''
  type: Login
  url: https://cartrevolt.com/sign-in
- group: auth
  href: https://artifacts.apis.io/cartrevolt-com/security/cartrevolt-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/cartrevolt-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://cartrevolt.com/
coverage:
  checked: '2026-11-03'
  detail: No public API contract discovered; attempts to fetch OpenAPI at https://api.cartrevolt.com/openapi.json returned error 525.
  evidence:
  - status: 525
    url: https://api.cartrevolt.com/openapi.json
  reason: not-a-software-company
  state: none
created: '2026-11-03'
description: CartRevolt is a community-driven platform that aggregates real‑time deals, discounts, and hacks to help shoppers save money as prices rise. It offers curated deals, user‑submitted hacks, gift‑card promotions, and a draw system, aiming to empower consumers with verified savings and smarter shopping choices.
image: https://cartrevolt.com/og/default.png
layout: provider
modified: '2026-11-03'
name: CartRevolt
nav: Providers
network: true
overview: 'CartRevolt is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Coupons, Discounts, Gift Cards, Shopping Hacks, and Community Deals.


  CartRevolt''s developer surface includes support and 8 more developer resources.'
random_paper: 18
score:
  band: minimal
  composite: 8.7
  coverage:
    artifact_dirs: 6
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 17.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 2.4
    discoverability: 55.4
    operational_transparency: 0.0
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 14.3
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Cartrevolt Com Domain Security
  slug: cartrevolt-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: cartrevolt-com
tags:
- Coupons
- Discounts
- Gift Cards
- Shopping Hacks
- Community Deals
website: https://cartrevolt.com/
---
