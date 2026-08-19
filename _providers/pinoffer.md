---
access_model:
  confidence: medium
  label: Freemium · Self-serve signup
  onboarding: unknown
  pricing: freemium
  public: true
  source:
  - https://www.converted.in/pricing
  - https://app.converted.in/register
  - https://developer.converted.in/api-1/getting-started
  trial: true
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: documented
    event_surface_described: true
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.2
  score: 38.9
  scored_at: '2026-08-19'
api_count: 3
apis:
- description: 'The one API surface Convertedin hosts itself. A merchant''s storefront (Magento, Salla, or a custom platform) POSTs commerce events into Convertedin — orders, customers, products, collections, and app '
  name: Convertedin Webhook Ingest API
  slug: convertedin-webhook-ingest-api
- description: The contract a merchant on a custom e-commerce platform IMPLEMENTS so that Convertedin can pull its catalogue and customer data. Convertedin is the client here, not the server, which is why the base U
  name: Convertedin Store Connector API
  slug: convertedin-store-connector-api
- description: A second merchant-implemented contract, aimed at loyalty and point-of-sale vendors. GET endpoints for /api/store-info, /api/products, /api/orders and /api/customers on the vendor's own host, authentic
  name: Convertedin Loyalty & POS Integration API
  slug: convertedin-loyalty-pos-integration-api
artifact_total: 8
asyncapis:
- description: ''
  name: Pinoffer Webhooks
  slug: pinoffer-webhooks
common:
- group: company
  title: ''
  type: Website
  url: https://convertedin.com
- group: company
  title: ''
  type: About
  url: https://convertedin.com/about
- group: commercial
  title: ''
  type: TermsOfService
  url: https://convertedin.com/archive/Terms-of-Use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://convertedin.com/archive/Privacy-Policy
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/convertedin
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.converted.in
- group: docs
  title: ''
  type: Documentation
  url: https://developer.converted.in
- group: docs
  title: ''
  type: APIReference
  url: https://developer.converted.in/api-1/getting-started
- group: start
  title: ''
  type: GettingStarted
  url: https://developer.converted.in/api-1/getting-started
- group: commercial
  title: ''
  type: Pricing
  url: https://www.converted.in/pricing
- group: start
  title: ''
  type: SignUp
  url: https://app.converted.in/register
- group: start
  title: ''
  type: Login
  url: https://app.converted.in/login
- group: operate
  title: ''
  type: StatusPage
  url: https://status.converted.in/
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/pinoffer-lifecycle.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/pinoffer-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/pinoffer-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/pinoffer-problem-types.yml
- group: build
  title: ''
  type: Packages
  url: packages/pinoffer-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/pinoffer-packages.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/pinoffer-webhooks.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/pinoffer-llms.txt
- group: design
  title: ''
  type: Conformance
  url: conformance/pinoffer-conformance.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/pinoffer-data-model.yml
- group: design
  title: ''
  type: Components
  url: components/pinoffer-components.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/pinoffer-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/pinoffer-rate-limits.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/pinoffer-domain-security.yml
created: '2026-07-17'
description: 'Pinoffer is the API Evangelist network profile for Convertedin (converted.in / convertedin.com), the MENA-focused marketing operating system for e-commerce founded in Cairo in 2019 by Mohamed Fergany, Mohamed Atef and Mustafa Raslan. "PinOffer" is the company''s former name and is still the identifier used by 500 Global, Crunchbase, MAGNiTT and LinkedIn, which is why the network entry carries it. Backed by Merak Capital, 500 Global and MSAS, Convertedin operates across Egypt, Saudi Arabia, the UAE and Brazil, and sells a unified growth platform covering store analytics, a commerce pixel, segmentation, SMS and email automation, and multi-channel ad buying on Meta, TikTok, Snapchat and Google — plus the Converted Pay, Flyerz, Leads and Orders products. Convertedin DOES run a public developer program at developer.converted.in, contrary to the earlier enrichment pass on this repo: it publishes an llms.txt-indexed documentation set covering a live webhook ingest API at app.converted.in,
  two merchant-implemented data-sync contracts (Store Connector and Loyalty/POS), a browser pixel SDK, first-party Android and iOS SDKs, and a Flyerz DSP iframe embed. What it does not publish is any machine-readable contract — no OpenAPI, AsyncAPI, GraphQL schema, MCP server or agent card exists on any Convertedin host.'
image: https://framerusercontent.com/images/mru1tCz0BzvuFna3W9s3gStqS5A.png
layout: provider
modified: '2026-08-12'
name: Pinoffer
nav: Providers
network: true
overview: 'Pinoffer publishes 3 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Advertising Technology, Marketing Technology, E-commerce, and Marketing Automation.


  The Pinoffer catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Pinoffer''s developer surface includes documentation, API reference, getting-started guide, pricing, signup flow, authentication, and 21 more developer resources.'
plans:
- name: Pinoffer Plans Pricing
  plan_count: 3
  slug: pinoffer-plans-pricing
random_paper: 112
rate_limits:
- limit_count: 0
  name: Pinoffer Rate Limits
  slug: pinoffer-rate-limits
score:
  band: developing
  composite: 51.8
  delta: 0.8
  facets:
    access_clarity: 76.3
    commercial_clarity: 76.3
    contract_governance: 18.2
    contract_quality: 45.1
    developer_ergonomics: 57.1
    discoverability: 92.6
    governance: 18.2
    operational_transparency: 10.5
  previous_composite: 51.0
  provenance:
    conformance: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 39.1
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/pinoffer/refs/heads/main/screenshots/pinoffer-2026-08-17T081239.png
security:
- kind: authentication
  name: Pinoffer Authentication
  slug: pinoffer-authentication
  summary_line: 5 schemes
- kind: domain-security
  name: Pinoffer Domain Security
  slug: pinoffer-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: pinoffer
tags:
- Company
- Advertising Technology
- Marketing Technology
- E-commerce
- Marketing Automation
- Customer Data
- Lead Generation
- Payments
- Emerging Markets
- MENA
- Advertising
- Webhooks
website: https://convertedin.com
---
