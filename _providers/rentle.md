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
    agentic_access: derived
    asyncapi_events: true
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: verified
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 31.1
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 7
  human_in_the_loop: 0
  name: Rentle Agentic Access
  operation_count: 28
  slug: rentle-agentic-access
  summary_line: 28 operations · 7 acting
api_count: 11
apis:
- description: API Key-related queries
  name: Rentle API Keys API
  slug: rentle-api-keys-api
- description: Category-related queries
  name: Rentle Categories API
  slug: rentle-categories-api
- description: Customer-related queries
  name: Rentle Customers API
  slug: rentle-customers-api
- description: Discount code-related queries
  name: Rentle Discount Codes API
  slug: rentle-discount-codes-api
- description: Inventory-related queries
  name: Rentle Inventory Articles API
  slug: rentle-inventory-articles-api
- description: The Inventory SKUs API from Rentle — 2 operation(s) for inventory skus.
  name: Rentle Inventory SKUs API
  slug: rentle-inventory-skus-api
- description: Merchant-related queries
  name: Rentle Merchant API
  slug: rentle-merchant-api
- description: Order-related queries
  name: Rentle Orders API
  slug: rentle-orders-api
- description: Product-related queries
  name: Rentle Products API
  slug: rentle-products-api
- description: Store-related queries
  name: Rentle Stores API
  slug: rentle-stores-api
- description: 'This section describes API endpoints you can use to configure webhooks. Check the [webhook events section](#tag/WebhooksOverview) for more inforation regarding the webhooks events that Twice delivers '
  name: Rentle Webhooks API
  slug: rentle-webhooks-api
artifact_total: 15
asyncapis:
- description: ''
  name: Rentle Webhooks
  slug: rentle-webhooks
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/rentle-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/rentle-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.twicecommerce.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://www.twicecommerce.com/docs/overview
- group: docs
  title: ''
  type: Documentation
  url: https://www.twicecommerce.com/docs/overview
- group: docs
  title: ''
  type: APIReference
  url: https://api.rentle.io/admin/
- group: operate
  title: ''
  type: Support
  url: https://support.twicecommerce.com
- group: company
  title: ''
  type: Blog
  url: https://www.twicecommerce.com/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/rentle
- group: commercial
  title: ''
  type: Pricing
  url: https://www.twicecommerce.com/pricing
- group: start
  title: ''
  type: SignUp
  url: https://admin.twicecommerce.com/signup
- group: start
  title: ''
  type: Login
  url: https://admin.twicecommerce.com/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://firebasestorage.googleapis.com/v0/b/rentle-prod.appspot.com/o/rentle-tos-pricing%2Ftos%2FTwice%20Commerce%20Terms%20and%20Conditions%20v.6.4.pdf?alt=media&token=eb7ee536-cb6c-4476-84fd-277e45e4a304
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.twicecommerce.com/privacy
- group: operate
  title: ''
  type: StatusPage
  url: https://status.twicecommerce.com
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/rentle-changelog.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/rentle-lifecycle.yml
- group: design
  title: ''
  type: Components
  url: components/rentle-components.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/rentle-llms.txt
created: '2026-07-17'
description: Rentle, now operating as Twice Commerce, is a Helsinki-founded (2018) circular-commerce platform that lets merchants run rentals, resale, and subscriptions from one system. Its Twice Admin API (OpenAPI 3.0.0, date-based version 2023-02-01) exposes categories, customers, inventory articles, SKUs, products, orders, stores, merchant details, discount codes, API keys, and webhooks over a REST interface authenticated with HTTP Basic API keys. Outbound webhooks cover nine order and product lifecycle events. This profile was enriched by the API Evangelist pipeline from Rentle/Twice Commerce public developer surfaces.
image: https://www.twicecommerce.com/favicon.ico
layout: provider
modified: '2026-07-20'
name: Rentle
nav: Providers
network: true
overview: 'Rentle publishes 11 APIs on the [APIs.io](https://apis.io/) network, including API Keys API, Categories API, Customers API, and 8 more. Tagged areas include Company, Rental, Commerce, E-commerce, and Circular Economy.


  The Rentle catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Rentle''s developer surface includes documentation, API reference, support, engineering blog, pricing, signup flow, changelog, and 12 more developer resources.'
random_paper: 2
score:
  band: developing
  composite: 45.4
  delta: 0.1
  facets:
    commercial_clarity: 44.7
    contract_quality: 60.0
    developer_ergonomics: 30.4
    discoverability: 92.6
    governance: 11.5
    operational_transparency: 36.8
  previous_composite: 45.3
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 11
    mcp: derived
    skills: derived
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
security:
- kind: authentication
  name: Rentle Authentication
  slug: rentle-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Rentle Domain Security
  slug: rentle-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: rentle
tags:
- Company
- Rental
- Commerce
- E-commerce
- Circular Economy
- Resale
- Subscriptions
- Bookings
- Webhooks
- SaaS
website: https://www.twicecommerce.com/
---
