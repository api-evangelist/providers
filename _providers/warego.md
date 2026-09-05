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
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 2.5
  scored_at: '2026-09-04'
api_count: 1
apis:
- description: WareGo agent-native content surface. A live, well-formed llms.txt provides a curated sitemap of product, feature, industry and guide pages for LLM discovery, and is currently the only machine-readable
  name: WareGo
  slug: warego
artifact_total: 4
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/warego-domain-security.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/warego-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: conformance/warego-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/warego-lifecycle.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/warego-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/warego-rate-limits.yml
- group: commercial
  title: ''
  type: Pricing
  url: https://warego.co/pricing/
- group: start
  title: ''
  type: SignUp
  url: https://warego.co/signup/
- group: operate
  title: ''
  type: Support
  url: https://warego.co/customer-support/
- group: company
  title: ''
  type: Blog
  url: https://warego.co/blog/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://warego.co/terms-conditions/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://warego.co/privacy-policy/
coverage:
  checked: '2026-09-02'
  detail: WareGo's own integration guide says it "provides Open APIs" and tells integrators to access API documentation and set up API keys, but links to no reference and makes step 3 "Engage with Our Product Team" — the docs, endpoints and credentials are handed out through sales onboarding, and no developer portal, API reference or spec exists anywhere on the public web.
  evidence:
  - status: 200
    url: https://warego.co/customer-support/connections-and-integrations/
  - status: 200
    url: https://warego.co/llms.txt
  - status: 200
    url: https://api.warego.co/openapi.json
  - status: 404
    url: https://warego.co/openapi.json
  - status: 404
    url: https://warego.co/.well-known/agent-card.json
  - status: 403
    url: https://warego.co/pricing/
  reason: sales-gate
  state: gated
created: '2026-09-02'
description: Cloud-based Warehouse Management System (WMS) for wholesalers, distributors, 3PLs, and ecommerce businesses, covering inventory tracking, order fulfillment, serial-number tracking, kitting, replenishment, inventory forecasting and supply-chain visibility. Sold as a tiered SaaS platform with a sales-assisted onboarding funnel, and marketed as API-first with 200+ pre-built integrations across ecommerce storefronts, ERPs, accounting systems and carriers. WareGo states it supports the ANSI X12 EDI transaction sets that matter in 3PL (850, 856, 810, 940/944) alongside a REST API and webhooks, but publishes no developer portal, no API reference and no machine-readable contract.
image: https://warego.co/wp-content/uploads/2026/02/WareGo-Logo.jpg
layout: provider
modified: '2026-09-02'
name: WareGo
nav: Providers
network: true
overview: 'WareGo publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Warehouse Management, WMS, Inventory Management, Order Management, and Fulfillment.


  WareGo''s developer surface includes pricing, signup flow, support, engineering blog, and 8 more developer resources.'
plans:
- name: Warego Plans Pricing
  plan_count: 0
  slug: warego-plans-pricing
random_paper: 15
rate_limits:
- limit_count: 0
  name: Warego Rate Limits
  slug: warego-rate-limits
score:
  band: emerging
  composite: 23.6
  coverage:
    artifact_dirs: 8
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 52.6
    commercial_clarity: 52.6
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 16.7
    discoverability: 75.9
    governance: 18.2
    operational_transparency: 0.0
  previous_composite: 23.6
  provenance:
    conformance: first-party
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
security:
- kind: domain-security
  name: Warego Domain Security
  slug: warego-domain-security
  summary_line: TLSv1.3 · DMARC
slug: warego
tags:
- Warehouse Management
- WMS
- Inventory Management
- Order Management
- Fulfillment
- Supply Chain
- Logistics
- 3PL
- Ecommerce
- Retail
- Wholesale Distribution
- Manufacturing
- EDI
---
