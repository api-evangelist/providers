---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - plans
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
    auth_clarity: false
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: true
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 17.3
  scored_at: '2026-11-06'
api_count: 0
artifact_total: 3
asyncapis:
- description: ''
  name: Gift Up Webhooks
  slug: gift-up-webhooks
common:
- group: commercial
  href: https://artifacts.apis.io/gift-up/plans/gift-up-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/gift-up-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/gift-up/asyncapi/gift-up-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/gift-up-webhooks.yml
- group: design
  href: https://artifacts.apis.io/gift-up/conformance/gift-up-conformance.yml
  title: ''
  type: Conformance
  url: conformance/gift-up-conformance.yml
- group: other
  href: https://artifacts.apis.io/gift-up/hosts/gift-up-hosts.yml
  title: ''
  type: Hosts
  url: hosts/gift-up-hosts.yml
- group: other
  href: https://artifacts.apis.io/gift-up/vendors/gift-up-vendors.yml
  title: ''
  type: Vendors
  url: vendors/gift-up-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.giftup.com/terms-conditions
- group: operate
  title: ''
  type: Support
  url: https://help.giftup.com/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.giftup.com/pricing
- group: docs
  title: ''
  type: Documentation
  url: https://developer.giftup.com/
- group: auth
  href: https://artifacts.apis.io/gift-up/security/gift-up-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/gift-up-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://giftup.com/
coverage:
  checked: '2026-10-27'
  detail: Developer portal at https://developer.giftup.com/ provides HTML docs but no OpenAPI, GraphQL, AsyncAPI, gRPC or WSDL specifications were found.
  evidence:
  - status: 200
    url: https://developer.giftup.com/
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-27'
description: Gift Up! provides a simple platform for businesses to sell digital and physical gift cards online. It offers a fully automated checkout, integrates with any website or e‑commerce platform, supports multiple currencies, and handles payment processing, delivery, and redemption without monthly fees. Users can customize card designs, set custom values, and manage sales through a web dashboard or mobile app.
image: http://static1.squarespace.com/static/58ecc0993a0411e543bfb8de/t/5e80919a554fd6780ab575ab/1585484187109/Logo%2BBlack%2BYellow%2BWhite.png?format=1500w
layout: provider
modified: '2026-10-27'
name: Gift Up!
nav: Providers
network: true
overview: 'Gift Up! is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Payments, E-Commerce, Gift Cards, and Software-as-a-Service.


  The Gift Up! catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Gift Up!''s developer surface includes support, pricing, documentation, and 8 more developer resources.'
plans:
- name: Gift Up Plans Pricing
  plan_count: 1
  slug: gift-up-plans-pricing
random_paper: 4
score:
  band: emerging
  composite: 25.4
  coverage:
    artifact_dirs: 12
    catalog_earned: 35.0
    catalog_earned_first_party: 8.0
    catalog_gap: 80.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -3.8
  facets:
    access_clarity: 31.6
    contract_governance: 18.2
    contract_quality: 39.0
    developer_ergonomics: 7.1
    discoverability: 48.2
    operational_transparency: 7.9
  previous_composite: 29.2
  provenance:
    conformance: first-party
    mcp: unknown
  regulatory:
    applies: true
    jurisdictions:
    - jurisdiction: EU
      standard: gdpr
    jurisdictions_satisfied: 1
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 18.8
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/gift-up/gift-up-2026-11-03T132822.png
security:
- kind: domain-security
  name: Gift Up Domain Security
  slug: gift-up-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: gift-up
tags:
- Company
- Payments
- E-Commerce
- Gift Cards
- Software-as-a-Service
website: https://giftup.com/
---
