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
  scored_at: '2026-08-26'
api_count: 1
apis:
- description: 'Janio''s production REST API for cross-border logistics: order creation and batch order management, unified multi-carrier tracking, rate and transit-time quotes, shipping label and customs document gen'
  name: Janio Logistics API
  slug: janio-logistics-api
artifact_total: 4
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/janio-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.janio.asia/
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/janio-llms.txt
- group: operate
  title: ''
  type: Support
  url: https://support.janio.asia/en/support/home
- group: company
  title: ''
  type: Blog
  url: https://www.janio.asia/resources/articles
- group: commercial
  title: ''
  type: Pricing
  url: https://www.janio.asia/pricing
- group: start
  title: ''
  type: Login
  url: https://app.janio.asia/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.janio.asia/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.janio.asia/privacy
- group: operate
  title: ''
  type: Contact
  url: https://www.janio.asia/contact
- group: operate
  title: ''
  type: FAQ
  url: https://www.janio.asia/faq
- group: company
  title: ''
  type: About
  url: https://www.janio.asia/about
- group: other
  title: ''
  type: CaseStudies
  url: https://www.janio.asia/case-studies
- group: company
  title: ''
  type: Careers
  url: https://www.janio.asia/careers
- group: commercial
  title: ''
  type: Plans
  url: plans/janio-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/janio-rate-limits.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/janio-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: conformance/janio-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/janio-lifecycle.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/janio-conventions.yml
- group: build
  title: ''
  type: Packages
  url: packages/janio-packages.yml
coverage:
  checked: '2026-08-23'
  detail: Janio runs a live production REST API — https://api.janio.asia/api/order/orders/ answers 403 {"detail":"Permission denied."} — but ships no machine-readable contract at any probed location, and the Integrations page's only route to the reference is a "Request API Documentation" button that leads to the /contact sales form, above Janio's own line "API documentation is available upon request".
  evidence:
  - status: 403
    url: https://api.janio.asia/api/order/orders/
  - status: 404
    url: https://api.janio.asia/openapi.json
  - status: 200
    url: https://www.janio.asia/integrations
  - status: 200
    url: https://www.janio.asia/llms.txt
  reason: sales-gate
  state: gated
created: '2026-08-23'
description: Janio is a Singapore-headquartered fourth-party logistics (4PL) provider serving Southeast Asia and Greater China. Rather than owning trucks or warehouses, Janio orchestrates a network of 500+ vetted carriers and 3PLs on a customer's behalf under one contract, one invoice and one SLA, across land, air and ocean freight plus warehousing. Its platform covers multi-carrier allocation, logistics-as-a-service, strategic procurement, a supply-chain control tower and automated freight invoice audit. Janio publishes a production REST API at api.janio.asia for order creation, tracking, rating, label generation, inventory sync and webhook events, together with pre-built Shopify, WooCommerce and Magento connectors — but the API reference itself is released only on request through the sales contact form, so no machine-readable contract is publicly available.
image: https://www.janio.asia/brand/janio-icon.png
layout: provider
modified: '2026-08-23'
name: Janio
nav: Providers
network: true
overview: 'Janio publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Logistics, Supply Chain, Shipping, Fourth-Party Logistics, and Cross-Border Ecommerce.


  Janio''s developer surface includes support, engineering blog, pricing, FAQ, and 17 more developer resources.'
plans:
- name: Janio Plans Pricing
  plan_count: 4
  slug: janio-plans-pricing
random_paper: 4
rate_limits:
- limit_count: 0
  name: Janio Rate Limits
  slug: janio-rate-limits
score:
  band: thin
  composite: 26.7
  delta: -1.3
  facets:
    access_clarity: 77.6
    commercial_clarity: 77.6
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 7.1
    discoverability: 75.9
    governance: 18.2
    operational_transparency: 0.0
  previous_composite: 28.0
  provenance:
    conformance: first-party
  schema_version: 0.15.0
  scored_at: '2026-08-26'
  trend: flat
security:
- kind: domain-security
  name: Janio Domain Security
  slug: janio-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: janio
tags:
- Logistics
- Supply Chain
- Shipping
- Fourth-Party Logistics
- Cross-Border Ecommerce
- Freight
- Tracking
- Southeast Asia
- Singapore
- Company
website: https://www.janio.asia/
---
