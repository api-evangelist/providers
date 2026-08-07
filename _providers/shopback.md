---
agent_readiness:
  band: agent-native
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: verified
    event_surface_described: true
    idempotency: verified
    mcp_server: false
    openapi_examples: partial
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.2
  score: 53.8
  scored_at: '2026-08-06'
api_count: 2
apis:
- description: The ShopBack Online Payments API (v2.0), also documented as the Online Bespoke API, lets merchants add ShopBack Pay and ShopBack PayLater to any web or app checkout. It covers merchant JWT login, orde
  name: ShopBack Online Payments API
  slug: shopback-online-payments-api
- description: 'The ShopBack In-Store Payments API (v1.4) accepts ShopBack Pay at the point of sale and in customer-facing apps and websites. It supports merchant-presented dynamic QR, customer-presented QR scanning '
  name: ShopBack In-Store Payments API
  slug: shopback-in-store-payments-api
artifact_total: 5
asyncapis:
- description: ''
  name: Shopback Payment Notification Webhooks
  slug: shopback-payment-notification-webhooks
common:
- group: company
  title: ''
  type: Website
  url: https://www.shopback.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.shopback.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.shopback.com/docs/getting-started
- group: docs
  title: ''
  type: APIReference
  url: https://docs.shopback.com/reference/initiateorder
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.shopback.com/docs/quickstart-api
- group: operate
  title: ''
  type: Support
  url: https://shopback.my.site.com/merchanthelpcenter/s/
- group: operate
  title: ''
  type: HelpCenter
  url: https://support.shopback.sg/hc/en-gb
- group: company
  title: ''
  type: Blog
  url: https://www.shopback.com/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/shopback
- group: commercial
  title: ''
  type: Pricing
  url: https://business.shopback.com/sg/payments
- group: start
  title: ''
  type: SignUp
  url: https://business.shopback.sg/signin
- group: commercial
  title: ''
  type: TermsOfService
  url: https://support.shopback.com/hc/en-us/articles/33321351340307-Terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://support.shopback.com/hc/en-us/articles/33321399347475-ShopBack-Privacy-Policy
- group: operate
  title: ''
  type: StatusPage
  url: https://status.shopback.com/
- group: build
  title: ''
  type: Postman
  url: https://docs.shopback.com/docs/postman-payload-sample
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/shopback-changelog.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/shopback-lifecycle.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/shopback-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/shopback-conventions.yml
- group: design
  title: ''
  type: Idempotency
  url: conventions/shopback-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/shopback-problem-types.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/shopback-conformance.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/shopback-sandbox.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/shopback-data-model.yml
- group: design
  title: ''
  type: Components
  url: components/shopback-components.yml
- group: build
  title: ''
  type: Packages
  url: packages/shopback-packages.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/shopback-payment-notification-webhooks.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/shopback-llms.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/shopback-well-known.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/shopback-domain-security.yml
created: '2026-08-02'
description: ShopBack is a Singapore-headquartered shopping, rewards and payments platform founded in 2014, operating across 13 markets in Asia-Pacific, Europe and the United States with more than 20 million members and 20,000 merchant partners. Alongside its consumer cashback and discovery app, ShopBack runs a merchant-facing payments business — ShopBack Pay and ShopBack PayLater — and publishes a public developer hub at docs.shopback.com covering two REST APIs. The Online Payments API (v2.0, also called the Online Bespoke API) handles merchant login, order initiation, order status, refunds, and a tokenized-payments surface for account linking, pre-authorization hold/capture/void, immediate charge and cashback-balance lookup. The In-Store Payments API (v1.4) covers merchant-presented and customer-presented QR ordering, order status, refunds, cancellations, and a payment-notification webhook for point-of-sale and customer-facing app checkout. Both are HMAC- or JWT-authenticated over HTTPS/TLS
  1.2+, support an X-ShopBack-Idempotent-Id idempotency header, and ship e-commerce plugins for Shopify, WooCommerce, Magento, PrestaShop, EasyStore and Salesforce Commerce Cloud.
image: https://corporate.shopback.com/opengraph.jpg
layout: provider
modified: '2026-08-02'
name: ShopBack
nav: Providers
network: true
overview: 'ShopBack publishes 2 APIs on the [APIs.io](https://apis.io/) network: Online Payments API and In-Store Payments API. Tagged areas include Company, Payments, Cashback, Rewards, and Loyalty.


  The ShopBack catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  ShopBack''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, pricing, signup flow, and 24 more developer resources.'
random_paper: 52
score:
  band: developing
  composite: 54.6
  delta: 0.0
  facets:
    commercial_clarity: 44.7
    contract_quality: 67.4
    developer_ergonomics: 64.7
    discoverability: 87.0
    governance: 11.5
    operational_transparency: 44.7
  previous_composite: 54.6
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 2
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 54.7
  schema_version: 0.9.1
  scored_at: '2026-08-06'
  trend: flat
security:
- kind: authentication
  name: Shopback Authentication
  slug: shopback-authentication
  summary_line: http/hmac/apiKey · 3 schemes
- kind: domain-security
  name: Shopback Domain Security
  slug: shopback-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: shopback
tags:
- Company
- Payments
- Cashback
- Rewards
- Loyalty
- E-Commerce
- Buy Now Pay Later
- Point Of Sale
- Checkout
- Singapore
website: https://www.shopback.com/
---
