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
    mcp_server: documented
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
  scored_at: '2026-10-31'
api_count: 0
artifact_total: 1
common:
- group: other
  href: https://artifacts.apis.io/backpackbang-com/hosts/backpackbang-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/backpackbang-com-hosts.yml
- group: auth
  href: https://artifacts.apis.io/backpackbang-com/security/backpackbang-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/backpackbang-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://backpackbang.com
- group: company
  title: ''
  type: Blog
  url: https://backpackbang.com/blog
- group: start
  title: ''
  type: Login
  url: https://backpackbang.com/connect
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://backpackbang.com/privacy
- group: start
  title: ''
  type: SignUp
  url: https://backpackbang.com/signup
- group: commercial
  title: ''
  type: TermsOfService
  url: https://backpackbang.com/terms
- group: auth
  title: ''
  type: TrustCenter
  url: https://backpackbang.com/trust
coverage:
  checked: '2026-10-29'
  detail: Home page returns a JavaScript shell with no machine‑readable API documentation.
  evidence:
  - status: 200
    url: https://backpackbang.com
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-29'
description: Backpack is an e‑commerce fulfillment service that enables shoppers in Bangladesh to purchase products from Amazon, eBay and other US/UK stores, delivering them within 16 days with a world‑class shopper guarantee and policy support.
image: https://storage.googleapis.com/backpack-images/bp-default-og.jpg
layout: provider
modified: '2026-10-29'
name: Backpack
nav: Providers
network: true
overview: 'Backpack is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include e-commerce, fulfillment, Bangladesh, marketplace, and startup.


  Backpack''s developer surface includes engineering blog, signup flow, and 7 more developer resources.'
random_paper: 4
score:
  band: emerging
  composite: 14.2
  coverage:
    artifact_dirs: 6
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 42.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 2.4
    discoverability: 48.2
    operational_transparency: 0.0
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 18.6
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Backpackbang Com Domain Security
  slug: backpackbang-com-domain-security
  summary_line: TLSv1.3 · HSTS
slug: backpackbang-com
tags:
- e-commerce
- fulfillment
- Bangladesh
- marketplace
- startup
website: https://backpackbang.com
---
