---
access_model:
  confidence: high
  label: Paid · Self-serve signup
  onboarding: self-serve
  pricing: paid
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 30.6
  scored_at: '2026-08-11'
agentic_access:
- acting_count: 10
  human_in_the_loop: 0
  name: Scalablepress Agentic Access
  operation_count: 24
  slug: scalablepress-agentic-access
  summary_line: 24 operations · 10 acting
api_count: 8
apis:
- description: Invoices and payments.
  name: Scalable Press Billing API
  slug: scalablepress-billing-api
- description: Available customization options.
  name: Scalable Press Customization API
  slug: scalablepress-customization-api
- description: Reusable design objects describing artwork and placement.
  name: Scalable Press Design API
  slug: scalablepress-design-api
- description: Order and item lifecycle events (v3).
  name: Scalable Press Event API
  slug: scalablepress-event-api
- description: Product mockup rendering (v3).
  name: Scalable Press Mockup API
  slug: scalablepress-mockup-api
- description: Place and manage print-and-ship orders.
  name: Scalable Press Order API
  slug: scalablepress-order-api
- description: Product catalog, categories, availability, and item details.
  name: Scalable Press Product API
  slug: scalablepress-product-api
- description: Standard and bulk price quotes including shipping.
  name: Scalable Press Quote API
  slug: scalablepress-quote-api
artifact_total: 15
collections:
- collection_type: open
  name: Scalable Press API
  slug: open-scalablepress
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/scalablepress-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/scalablepress-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/scalablepress-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/scalablepress
- group: company
  title: ''
  type: Website
  url: https://scalablepress.com
- group: docs
  title: ''
  type: Documentation
  url: https://scalablepress.com/docs/
- group: start
  title: ''
  type: SignUp
  url: https://scalablepress.com/api
- group: commercial
  title: ''
  type: Plans
  url: plans/scalablepress-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/scalablepress-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/scalablepress-finops.yml
created: '2026-07-11'
description: Scalable Press is a technology-driven print-on-demand and fulfillment platform for custom apparel, accessories, and promotional products, offering DTG (direct-to-garment) and screen printing, embroidery, laser engraving, posters, and phone cases with worldwide shipping. Its public REST API lets developers browse a wholesale blank-and-printed product catalog, generate price quotes (including item, print, and shipping costs), place and manage print-and-ship orders, track fulfillment status through order events, create designs and product mockups, and retrieve billing invoices. The API uses HTTP Basic authentication with a private API key supplied as the password, spans v2 (product, quote, order, design, customization, billing) and v3 (event, mockup) surfaces, and operates on a pay-per-order model with no monthly subscription fee.
finops:
- name: Scalablepress Finops
  service_category: Print on Demand and Fulfillment
  slug: scalablepress-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/scalablepress.png
layout: provider
modified: '2026-07-11'
name: Scalable Press
nav: Providers
network: true
overview: 'Scalable Press publishes 8 APIs on the [APIs.io](https://apis.io/) network, including Billing API, Customization API, Design API, and 5 more. Tagged areas include Print on Demand, Fulfillment, Apparel, Custom Printing, and E-Commerce.


  Scalable Press'' developer surface includes authentication, documentation, signup flow, and 7 more developer resources.'
plans:
- name: Scalablepress Plans Pricing
  plan_count: 2
  slug: scalablepress-plans-pricing
random_paper: 104
rate_limits:
- limit_count: 3
  name: Scalablepress Rate Limits
  slug: scalablepress-rate-limits
score:
  band: thin
  composite: 39.2
  delta: -0.6
  facets:
    commercial_clarity: 42.1
    contract_quality: 61.2
    developer_ergonomics: 19.6
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 31.6
  previous_composite: 39.8
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 8
  schema_version: 0.11.0
  scored_at: '2026-08-11'
  trend: flat
security:
- kind: authentication
  name: Scalablepress Authentication
  slug: scalablepress-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Scalablepress Domain Security
  slug: scalablepress-domain-security
  summary_line: TLSv1.2 · DMARC
slug: scalablepress
tags:
- Print on Demand
- Fulfillment
- Apparel
- Custom Printing
- E-Commerce
- Wholesale
website: https://scalablepress.com
---
