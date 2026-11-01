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
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 0.0
  scored_at: '2026-10-31'
api_count: 1
apis:
- description: LetMeShip's multi-carrier shipping interface – simply connect and send parcels, pallets and documents for your company.
  name: Shipping API
  slug: shipping-api
artifact_total: 3
common:
- group: commercial
  href: https://artifacts.apis.io/letmeship/plans/letmeship-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/letmeship-plans-pricing.yml
- group: agent
  href: https://artifacts.apis.io/letmeship/llms/letmeship-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/letmeship-llms.txt
- group: other
  href: https://artifacts.apis.io/letmeship/hosts/letmeship-hosts.yml
  title: ''
  type: Hosts
  url: hosts/letmeship-hosts.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.letmeship.com/legal-notice/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.letmeship.com/privacy-policy/
- group: company
  title: ''
  type: Newsroom
  url: https://www.letmeship.com/press/
- group: start
  title: ''
  type: Login
  url: https://www.letmeship.com/de/login/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/letmeship
- group: auth
  href: https://artifacts.apis.io/letmeship/security/letmeship-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/letmeship-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://letmeship.com/
- group: docs
  title: ''
  type: Documentation
  url: https://www.letmeship.com/shipping-software/shipping-api/
- group: docs
  title: ''
  type: APIReference
  url: https://www.letmeship.com/shipping-software/shipping-api/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.letmeship.com/pricing/
- group: company
  title: ''
  type: Blog
  url: https://www.letmeship.com/blog/
- group: operate
  title: ''
  type: Support
  url: https://www.letmeship.com/contact/
coverage:
  checked: '2026-10-28'
  detail: Documentation page renders HTML without a machine‑readable OpenAPI or other contract.
  evidence:
  - status: 200
    url: https://www.letmeship.com/shipping-software/shipping-api/
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-27'
description: LetMeShip provides a B2B shipping platform that simplifies multi‑carrier shipping, customs, and logistics for European businesses. Their Shipping API enables developers to integrate rate calculation, label generation, and shipment tracking across numerous carriers, supporting parcel, document, and pallet shipments both domestically and internationally.
image: https://www.letmeship.com/wp-content/uploads/2025/11/lms-shareimage-placeholder-1024x576.png
layout: provider
modified: '2026-10-27'
name: LetMeShip
nav: Providers
network: true
overview: 'LetMeShip is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Shipping, Logistics, B2B, API, and Europe.


  LetMeShip''s developer surface includes documentation, API reference, pricing, engineering blog, support, and 10 more developer resources.'
plans:
- name: Letmeship Plans Pricing
  plan_count: 1
  slug: letmeship-plans-pricing
random_paper: 11
score:
  band: emerging
  composite: 24.3
  coverage:
    artifact_dirs: 7
    catalog_earned: 40.0
    catalog_earned_first_party: 8.0
    catalog_gap: 75.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 65.8
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 23.8
    discoverability: 58.9
    operational_transparency: 5.3
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 13.7
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Letmeship Domain Security
  slug: letmeship-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: letmeship
tags:
- Shipping
- Logistics
- B2B
- API
- Europe
website: https://letmeship.com/
---
