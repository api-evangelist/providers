---
access_model:
  confidence: medium
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    asyncapi_events: false
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: verified
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.2
  score: 30.2
  scored_at: '2026-07-28'
api_count: 6
apis:
- description: The order_attachments API from Channable — 2 operation(s) for order_attachments.
  name: Channable order_attachments API
  slug: channable-order-attachments-api
- description: The orders API from Channable — 10 operation(s) for orders.
  name: Channable orders API
  slug: channable-orders-api
- description: The returns API from Channable — 5 operation(s) for returns.
  name: Channable returns API
  slug: channable-returns-api
- description: The statistics API from Channable — 2 operation(s) for statistics.
  name: Channable statistics API
  slug: channable-statistics-api
- description: The stock_updates API from Channable — 2 operation(s) for stock_updates.
  name: Channable stock_updates API
  slug: channable-stock-updates-api
- description: The transporters API from Channable — 3 operation(s) for transporters.
  name: Channable transporters API
  slug: channable-transporters-api
artifact_total: 9
common:
- group: company
  title: ''
  type: Website
  url: https://www.channable.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.channable.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.channable.com/api/v1/
- group: docs
  title: ''
  type: APIReference
  url: https://api.channable.com/v1/docs
- group: start
  title: ''
  type: GettingStarted
  url: https://helpcenter.channable.com/hc/en-us/articles/360011209639-Using-the-Channable-API-for-an-order-connection
- group: operate
  title: ''
  type: HelpCenter
  url: https://helpcenter.channable.com/
- group: operate
  title: ''
  type: Support
  url: https://support.channable.com/
- group: company
  title: ''
  type: Blog
  url: https://www.channable.com/blog
- group: operate
  title: ''
  type: ChangeLog
  url: https://helpcenter.channable.com/changelog/
- group: operate
  title: ''
  type: StatusPage
  url: https://www.channablestatus.com/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.channable.com/pricing
- group: start
  title: ''
  type: SignUp
  url: https://app.channable.com/
- group: start
  title: ''
  type: Login
  url: https://app.channable.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.channable.com/terms-and-conditions
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.channable.com/privacy-policy
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/channable
- group: build
  title: ''
  type: Postman
  url: https://www.postman.com/docking-module-engineer-59598931/channable-integration-environement/collection/o2462ca/channable
- group: build
  title: ''
  type: Packages
  url: packages/channable-packages.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/channable-lifecycle.yml
- group: operate
  title: ''
  type: Deprecation
  url: lifecycle/channable-lifecycle.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/channable-rate-limits.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/channable-changelog.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/channable-conventions.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/channable-domain-security.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/channable-well-known.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/channable-llms.txt
created: '2026-07-17'
description: 'Channable is a feed management and marketplace integration platform that helps online retailers, brands, and agencies optimize, distribute, and advertise their product data across more than 2,500 marketing channels, price comparison sites, affiliate networks, and online marketplaces. Beyond feed optimization and PPC ad automation, Channable operates an order-connection layer that synchronizes orders, shipments, stock, and returns between marketplaces and a seller''s ERP, WMS, or e-commerce platform. The Channable order connection API (v1) exposes this layer programmatically: retailers and platform integrators can retrieve orders and returns, post shipment and cancellation updates, push stock/offer updates to every connected marketplace at once, upload order attachments, resolve standardized transporter codes, and pull order statistics. Authentication is a company-level bearer token, requests are rate limited per company with a leaky-bucket policy, and a Channable Sandbox connection
  lets integrators test order flows without touching live marketplaces.'
image: https://www.channable.com/favicon.ico
layout: provider
modified: '2026-07-18'
name: Channable
nav: Providers
network: true
overview: 'Channable publishes 6 APIs on the [APIs.io](https://apis.io/) network, including order_attachments API, orders API, returns API, and 3 more. Tagged areas include Company, Applicative Saas, Feed Management, Marketplaces, and E-commerce.


  Channable''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, changelog, pricing, and 19 more developer resources.'
random_paper: 33
rate_limits:
- limit_count: 0
  name: Channable Rate Limits
  slug: channable-rate-limits
score:
  band: developing
  composite: 46.0
  delta: -0.3
  facets:
    commercial_clarity: 44.7
    contract_quality: 45.8
    developer_ergonomics: 45.7
    discoverability: 92.6
    governance: 11.5
    operational_transparency: 44.7
  previous_composite: 46.3
  provenance:
    conformance: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 6
    mcp: derived
    skills: derived
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/channable/refs/heads/main/screenshots/channable-2026-07-25T205043.png
security:
- kind: authentication
  name: Channable Authentication
  slug: channable-authentication
  summary_line: http/apiKey · 2 schemes
- kind: domain-security
  name: Channable Domain Security
  slug: channable-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
slug: channable
tags:
- Company
- Applicative Saas
- Feed Management
- Marketplaces
- E-commerce
- Product Data
- Order Management
- Advertising
- PPC
- Retail
website: https://www.channable.com/
---
