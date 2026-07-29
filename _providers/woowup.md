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
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: documented
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: false
    well_known_catalog: true
  schema_version: 0.2
  score: 19.4
  scored_at: '2026-07-28'
api_count: 1
apis:
- description: REST API for syncing customers (multi-ID), purchases, products, categories, branches, coupons, benefits, points, user events, custom attributes, abandoned carts, blacklists, segment exports, and integ
  name: WoowUp API v3
  slug: woowup-api-v3
artifact_total: 4
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/woowup-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.woowup.com
- group: company
  title: ''
  type: Blog
  url: https://www.woowup.com/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://www.woowup.com/planes-y-precios
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.woowup.com/legal/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.woowup.com/legal/privacypolicy
- group: operate
  title: ''
  type: Support
  url: https://help.woowup.com/es/
- group: start
  title: ''
  type: Login
  url: https://app.woowup.com/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/woowup
- group: docs
  title: ''
  type: Documentation
  url: https://docs.woowup.com
- group: start
  title: ''
  type: GettingStarted
  url: https://woowup-docs.gitbook.io/woowup-developer-docs/master
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/woowup-llms.txt
- group: build
  title: ''
  type: Packages
  url: packages/woowup-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/woowup-packages.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/woowup-well-known.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/woowup-conformance.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/woowup-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/woowup-lifecycle.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/woowup-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/woowup-conventions.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/woowup-rate-limits.yml
- group: design
  title: ''
  type: Components
  url: components/woowup-components.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/woowup-data-model.yml
created: '2026-07-17'
description: WoowUp is a customer marketing and loyalty CRM platform built for retail and ecommerce brands across Latin America. Founded in Buenos Aires and backed by 500 Global, WoowUp centralizes customer, purchase, and product data from POS and ecommerce platforms (VTEX, Magento, Shopify, WooCommerce, PrestaShop, Tienda Nube) and activates it through segmentation, campaigns, loyalty programs, web push notifications, and abandoned-cart recovery. Its REST API v3 lets developers sync users (multi-ID), purchases, products, coupons, benefits, points, and custom events, with client libraries published in PHP.
image: https://www.woowup.com/hubfs/Logo/favicon_.png
layout: provider
modified: '2026-07-21'
name: WoowUp
nav: Providers
network: true
overview: 'WoowUp publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, CRM, Loyalty, Customer Data, and Marketing Automation.


  WoowUp''s developer surface includes engineering blog, pricing, support, documentation, getting-started guide, authentication, and 17 more developer resources.'
random_paper: 57
rate_limits:
- limit_count: 1
  name: Woowup Rate Limits
  slug: woowup-rate-limits
score:
  band: thin
  composite: 31.3
  delta: 1.0
  facets:
    commercial_clarity: 44.7
    contract_quality: 0.0
    developer_ergonomics: 43.5
    discoverability: 87.0
    governance: 12.5
    operational_transparency: 26.3
  previous_composite: 30.3
  provenance:
    conformance: first-party
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
security:
- kind: authentication
  name: Woowup Authentication
  slug: woowup-authentication
  summary_line: apiKey · 2 schemes
- kind: domain-security
  name: Woowup Domain Security
  slug: woowup-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: woowup
tags:
- Company
- CRM
- Loyalty
- Customer Data
- Marketing Automation
- Retail
- eCommerce
- Push Notifications
website: https://www.woowup.com
---
