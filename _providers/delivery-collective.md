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
- group: agent
  href: https://artifacts.apis.io/delivery-collective/llms/delivery-collective-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/delivery-collective-llms.txt
- group: other
  href: https://artifacts.apis.io/delivery-collective/hosts/delivery-collective-hosts.yml
  title: ''
  type: Hosts
  url: hosts/delivery-collective-hosts.yml
- group: other
  href: https://artifacts.apis.io/delivery-collective/vendors/delivery-collective-vendors.yml
  title: ''
  type: Vendors
  url: vendors/delivery-collective-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://withbites.com/terms-of-service
- group: auth
  title: ''
  type: Security
  url: https://withbites.com/locations/security
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://withbites.com/privacy-policy
- group: company
  title: ''
  type: Newsroom
  url: https://withbites.com/newsroom
- group: auth
  href: https://artifacts.apis.io/delivery-collective/security/delivery-collective-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/delivery-collective-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://withbites.com/
coverage:
  checked: '2026-10-22'
  detail: The API spec endpoint redirects to a JavaScript‑rendered HTML page, providing no machine‑readable OpenAPI definition.
  evidence:
  - status: 308
    url: https://api.withbites.com/openapi.json
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-22'
description: Bites, operating as Delivery Collective, is an AI‑native food ordering network that eliminates menu markups, hidden fees, and commissions. It connects diners directly with restaurants, offering transparent pricing and a fair revenue model for partners. The platform provides mobile apps for consumers and tools for restaurants and POS partners, aiming to reshape food delivery with a focus on fairness and technology.
image: https://withbites.com/Food.png
layout: provider
modified: '2026-10-22'
name: Delivery Collective
nav: Providers
network: true
overview: Delivery Collective is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Food Delivery, Artificial Intelligence, Marketplace, Fair Pricing, and Restaurant.
random_paper: 11
score:
  band: minimal
  composite: 10.2
  coverage:
    artifact_dirs: 8
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 50.0
    operational_transparency: 10.5
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 12.7
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Delivery Collective Domain Security
  slug: delivery-collective-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: delivery-collective
tags:
- Food Delivery
- Artificial Intelligence
- Marketplace
- Fair Pricing
- Restaurant
website: https://withbites.com/
---
