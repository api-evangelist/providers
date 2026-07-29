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
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 30.6
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 12
  human_in_the_loop: 0
  name: Spod Agentic Access
  operation_count: 23
  slug: spod-agentic-access
  summary_line: 23 operations · 12 acting
api_count: 7
apis:
- description: The Articles API from SPOD — 2 operation(s) for articles.
  name: SPOD Articles API
  slug: spod-articles-api
- description: The Common API from SPOD — 1 operation(s) for common.
  name: SPOD Common API
  slug: spod-common-api
- description: The Orders API from SPOD — 4 operation(s) for orders.
  name: SPOD Orders API
  slug: spod-orders-api
- description: The Product Types API from SPOD — 2 operation(s) for product types.
  name: SPOD Product Types API
  slug: spod-product-types-api
- description: The Shipping API from SPOD — 3 operation(s) for shipping.
  name: SPOD Shipping API
  slug: spod-shipping-api
- description: The Stock API from SPOD — 2 operation(s) for stock.
  name: SPOD Stock API
  slug: spod-stock-api
- description: The Subscriptions API from SPOD — 5 operation(s) for subscriptions.
  name: SPOD Subscriptions API
  slug: spod-subscriptions-api
artifact_total: 15
collections:
- collection_type: open
  name: SPOD (Spreadconnect) Fulfillment REST API
  slug: open-spod
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/spod-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/spod-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/spod-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/spod-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/SP0D
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/spod-spreadshirt-print-on-demand
- group: company
  title: ''
  type: Website
  url: https://www.spod.com
- group: docs
  title: ''
  type: Documentation
  url: https://rest.spod.com/docs/
- group: commercial
  title: ''
  type: Plans
  url: plans/spod-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/spod-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/spod-finops.yml
created: '2026-07-11'
description: SPOD (Spreadshirt Print-On-Demand), now branded Spreadconnect, is the print-on-demand and dropshipping fulfillment service from Spreadshirt. Its REST API (base https://rest.spod.com) lets any shop system create customizable articles from designs, place and manage orders, choose shipping types and track shipments, browse the catalog of 250+ product types, check stock, and subscribe to webhook notifications for article, order, and shipment events. Authentication is a per-account API access token sent in the X-SPOD-ACCESS-TOKEN header. There are no setup or monthly fees; sellers are invoiced per fulfilled order (base product price plus print and shipping costs).
finops:
- name: Spod Finops
  service_category: Print on Demand and Fulfillment
  slug: spod-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/spod.png
layout: provider
modified: '2026-07-11'
name: SPOD
nav: Providers
network: true
overview: 'SPOD publishes 7 APIs on the [APIs.io](https://apis.io/) network, including Articles API, Common API, Orders API, and 4 more. Tagged areas include Print on Demand, POD, Dropshipping, Fulfillment, and E-commerce.


  SPOD''s developer surface includes authentication, documentation, and 9 more developer resources.'
plans:
- name: Spod Plans Pricing
  plan_count: 1
  slug: spod-plans-pricing
random_paper: 53
rate_limits:
- limit_count: 2
  name: Spod Rate Limits
  slug: spod-rate-limits
score:
  band: thin
  composite: 34.4
  delta: -2.1
  facets:
    commercial_clarity: 28.9
    contract_quality: 55.3
    developer_ergonomics: 19.6
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 26.3
  previous_composite: 36.5
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 7
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
security:
- kind: authentication
  name: Spod Authentication
  slug: spod-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Spod Domain Security
  slug: spod-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Spod Vulnerability Disclosure
  slug: spod-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: spod
tags:
- Print on Demand
- POD
- Dropshipping
- Fulfillment
- E-commerce
- Merchandise
- Spreadshirt
- Spreadconnect
website: https://www.spod.com
---
