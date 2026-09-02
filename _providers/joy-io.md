---
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
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: true
  schema_version: 0.2
  score: 5.4
  scored_at: '2026-09-01'
api_count: 0
artifact_total: 3
common:
- group: company
  title: ''
  type: Website
  url: https://joy.io/
- group: operate
  title: ''
  type: Support
  url: https://faq.joy.io/
- group: company
  title: ''
  type: Blog
  url: https://joy.io/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://joy.io/nos-offres
- group: start
  title: ''
  type: Login
  url: https://app.joy.io/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.privateaser.com/cgu
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://joy.io/politique-de-confidentialite
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/joy-io-llms.txt
- group: commercial
  title: ''
  type: Plans
  url: plans/joy-io-plans-pricing.yml
- group: design
  title: ''
  type: Components
  url: components/joy-io-components.yml
- group: build
  title: ''
  type: Packages
  url: packages/joy-io-packages.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/joy-io-domain-security.yml
coverage:
  checked: '2026-08-17'
  detail: Joy ships software only as an end-user product — a manager web/mobile app plus a hosted booking widget — and publishes no developer portal, API reference, OpenAPI, webhook catalogue or SDK; the private backend its own app calls, manager-api.privateaser.com (read from https://app.joy.io/config.js), returns HTTP 404 on /openapi.json and every other spec path and is gated by an AWS Cognito user pool, and the 90-article help-center index at faq.joy.io/llms.txt never uses the word "api".
  evidence:
  - status: 404
    url: https://manager-api.privateaser.com/openapi.json
  - status: 200
    url: https://joy.io/sitemap.xml
  - status: 200
    url: https://faq.joy.io/llms.txt
  - status: 200
    url: https://api.github.com/orgs/Privateaser-Joy/repos?per_page=100
  reason: no-developer-program
  state: none
created: '2026-08-17'
description: 'Joy is a French SaaS platform for bars, restaurants and venues that turns group and event enquiries into confirmed bookings. Founded in 2014 as Privateaser, the company now runs a two-sided business: privateaser.com, the group-venue marketplace that captures demand, and Joy, the manager-facing application (web plus iOS/Android) where an establishment centralises requests from Google, Instagram, its own website, WhatsApp and Privateaser, then works them through a unified calendar and messaging inbox, an SEO/GEO-optimised event showcase page, a virtual phone assistant, quotes, French-compliant invoicing, and Stripe-backed deposits and prepayments. Joy reports more than 3,000 partner establishments and over EUR100M in bookings managed in 2025. It publishes no public API, SDK, webhook catalogue or developer portal; the only integration surfaces it documents for customers are an embeddable iframe booking form, Reserve-with-Google, and a one-click reservation copy into Zenchef.'
image: https://joy.io/og-image.png
layout: provider
modified: '2026-08-17'
name: Joy (ex-Privateaser)
nav: Providers
network: true
overview: 'Joy (ex-Privateaser) is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Marketplace, Reservations, Bookings, and Restaurant.


  Joy (ex-Privateaser)''s developer surface includes support, engineering blog, pricing, and 9 more developer resources.'
plans:
- name: Joy Io Plans Pricing
  plan_count: 3
  slug: joy-io-plans-pricing
random_paper: 11
rate_limits:
- limit_count: 0
  name: Joy Io Rate Limits
  slug: joy-io-rate-limits
score:
  band: emerging
  composite: 22.4
  coverage:
    artifact_dirs: 8
    catalog_gap: 76.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 76.3
    commercial_clarity: 76.3
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 7.1
    discoverability: 57.4
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 22.4
  schema_version: 0.18.0
  scored_at: '2026-09-01'
  trend: flat
security:
- kind: domain-security
  name: Joy Io Domain Security
  slug: joy-io-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: joy-io
tags:
- Company
- Marketplace
- Reservations
- Bookings
- Restaurant
- Hospitality
- Event
- Software-as-a-Service
- France
website: https://joy.io/
---
