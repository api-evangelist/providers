---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source: []
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
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
  score: 7.9
  scored_at: '2026-09-03'
api_count: 0
artifact_total: 4
common:
- group: company
  title: ''
  type: Website
  url: https://cheerfy.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.cheerfy.com/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.cheerfy.com/es/cheerfy-loyalty/api-tarjeta-de-fidelizacion
- group: commercial
  title: ''
  type: Pricing
  url: https://www.en.cheerfy.com/pricing/loyalty
- group: company
  title: ''
  type: Blog
  url: https://www.en.cheerfy.com/academy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.en.cheerfy.com/legal/business-services
- group: operate
  title: ''
  type: Support
  url: https://www.en.cheerfy.com/contact
- group: start
  title: ''
  type: Login
  url: https://admin.cheerfy.com/login/
- group: auth
  title: ''
  type: DomainSecurity
  url: security/cheerfy-domain-security.yml
- group: docs
  title: ''
  type: APIReference
  url: https://docs.cheerfy.com/es/cheerfy-loyalty/api-cupones
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.en.cheerfy.com/legal/privacy-policy
- group: company
  title: ''
  type: BlogRSS
  url: https://www.en.cheerfy.com/academy?format=rss
- group: commercial
  title: ''
  type: Plans
  url: plans/cheerfy-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/cheerfy-rate-limits.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/cheerfy-authentication.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/cheerfy-problem-types.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/cheerfy-conventions.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/cheerfy-changelog.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/cheerfy-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/cheerfy-lifecycle.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/cheerfy-llms.txt
coverage:
  checked: '2026-08-10'
  detail: Both API reference pages (docs.cheerfy.com/es/cheerfy-loyalty/api-tarjeta-de-fidelizacion and /api-cupones) 307-redirect into the app.gitbook.com JavaScript shell, which serves the same 9,883-byte empty page for every path, so the documented Loyalty Card and Coupons endpoints, their base URL and their parameters are unreadable by any machine — and the published API hostname api.cheerfy.com returns 503 on every path.
  evidence:
  - status: 307
    url: https://docs.cheerfy.com/es/cheerfy-loyalty/api-tarjeta-de-fidelizacion
  - status: 200
    url: https://app.gitbook.com/o/FE20ERj3uqOoV8gciG2a/sites/site_WNSZl/es/cheerfy-loyalty/api-cupones
  - status: 503
    url: https://api.cheerfy.com/openapi.json
  - status: 401
    url: https://webhook.cheerfy.com/
  reason: js-rendered-docs
  state: unreadable
created: '2026-07-17'
description: Cheerfy is a customer-engagement and digital-experience platform for restaurants and hospitality brands, bringing CRM and loyalty, online ordering, pay-at-table, self-service kiosks, and a multi-brand marketplace together in a single platform. It centralizes customer data from POS, bookings, Wi-Fi and payment systems, then drives automated SMS, email and push marketing, branded loyalty cards and wallet-ready digital coupons, feedback surveys, and real-time analytics. Cheerfy serves 200+ restaurant brands and publishes developer documentation for its Loyalty Card and Coupons APIs. Backed by Techstars, it was added to the API Evangelist network from a Techstars portfolio lead and enriched from its public developer surface.
image: https://static1.squarespace.com/static/5a5091d4ace86412c1ba7bdb/t/5a807b280852294ef6f2697a/1518369577961/Screen+Shot+2018-02-11+at+18.15.29.png?format=1500w
layout: provider
modified: '2026-08-10'
name: Cheerfy
nav: Providers
network: true
overview: 'Cheerfy is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Restaurant, Hospitality, CRM, and Loyalty.


  Cheerfy''s developer surface includes documentation, API reference, pricing, engineering blog, support, authentication, changelog, and 14 more developer resources.'
plans:
- name: Cheerfy Plans Pricing
  plan_count: 3
  slug: cheerfy-plans-pricing
random_paper: 7
rate_limits:
- limit_count: 0
  name: Cheerfy Rate Limits
  slug: cheerfy-rate-limits
score:
  band: thin
  composite: 28.7
  coverage:
    artifact_dirs: 14
    catalog_gap: 76.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 69.7
    commercial_clarity: 69.7
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 19.0
    discoverability: 57.4
    governance: 18.2
    operational_transparency: 15.8
  previous_composite: 28.7
  provenance:
    conformance: first-party
  regulatory:
    applies: true
    jurisdictions:
    - jurisdiction: EU
      standard: gdpr
    jurisdictions_satisfied: 1
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 39.1
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/cheerfy/refs/heads/main/screenshots/cheerfy-2026-07-25T205137.png
security:
- kind: authentication
  name: Cheerfy Authentication
  slug: cheerfy-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Cheerfy Domain Security
  slug: cheerfy-domain-security
  summary_line: TLSv1.2 · HSTS · DMARC
slug: cheerfy
tags:
- Company
- Restaurant
- Hospitality
- CRM
- Loyalty
- Customer Engagement
- Marketing Automation
- Online Ordering
- Payments
website: https://cheerfy.com/
---
