---
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: documented
    event_surface_described: true
    idempotency: false
    mcp_server: false
    openapi_examples: documented
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 40.1
  scored_at: '2026-08-06'
api_count: 8
apis:
- description: 'The Hotmart authorization server. Exchanges a developer credential (client_id/client_secret, presented with HTTP Basic) for a short-lived OAuth 2.0 client_credentials access token, which is then sent '
  name: Hotmart Authentication (OAuth 2.0)
  slug: hotmart-authentication-oauth-20
- description: 'Read and manage recurring subscriptions on a Hotmart product — list subscribers with status, plan and date filters, pull a subscriber''s purchase history, list subscription transactions and summaries, '
  name: Hotmart Subscriptions API
  slug: hotmart-subscriptions-api
- description: Sales reporting and post-sale actions for a Hotmart producer — sales history, sales summary, per-transaction price breakdown, commission split across producer, co-producer and affiliate, buyer records
  name: Hotmart Sales API
  slug: hotmart-sales-api
- description: Create and list Hotmart payment links, attach additional offers and plans to a link, and charge a saved payment token by offer or by arbitrary value — the programmatic equivalent of Hotmart's hosted c
  name: Hotmart Payment Link API
  slug: hotmart-payment-link-api
- description: The product catalog surface — list products, read a product's offers and plans by ucode, update product configuration, and create, read and delete discount coupons for a product.
  name: Hotmart Products API
  slug: hotmart-products-api
- description: The members-area / LMS surface. Lists Club modules and pages for a subdomain, lists enrolled users, and reads a user's lesson-by-lesson progress — the content-consumption side of a Hotmart product, di
  name: Hotmart Club (Members Area) API
  slug: hotmart-club-members-area-api
- description: The logistics/fulfillment partner surface for physical products sold through Hotmart. Manages partner credentials, creates and updates products and variants, posts shipment status and tracking updates
  name: Hotmart Physical Products API
  slug: hotmart-physical-products-api
- description: The smaller documented surfaces — event ticket information and participant lists (/events/api/v1), account information (/accounts/api/v1/info), the authenticated user profile (/user/api/v1/me), and in
  name: Hotmart Events, Account and User API
  slug: hotmart-events-account-and-user-api
artifact_total: 13
asyncapis:
- description: ''
  name: Hotmart Webhooks
  slug: hotmart-webhooks
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/hotmart-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://hotmart.com/en
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developers.hotmart.com/
- group: docs
  title: ''
  type: Documentation
  url: https://developers.hotmart.com/docs/en/
- group: docs
  title: ''
  type: APIReference
  url: https://developers.hotmart.com/docs/en/
- group: start
  title: ''
  type: GettingStarted
  url: https://developers.hotmart.com/docs/en/start/
- group: operate
  title: ''
  type: Support
  url: https://help.hotmart.com/en
- group: company
  title: ''
  type: Blog
  url: https://hotmart.com/en/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Hotmart-Org
- group: commercial
  title: ''
  type: Pricing
  url: https://hotmart.com/en/pricing
- group: start
  title: ''
  type: SignUp
  url: https://hotmart.com/en/signup
- group: start
  title: ''
  type: Login
  url: https://app-vlc.hotmart.com/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://hotmart.com/en/legal/terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://hotmart.com/en/legal/privacy-policy
- group: operate
  title: ''
  type: StatusPage
  url: https://status.hotmart.com/
- group: operate
  title: ''
  type: ChangeLog
  url: https://developers.hotmart.com/docs/en/changelog
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/hotmart-changelog.yml
- group: operate
  title: ''
  type: FAQ
  url: https://developers.hotmart.com/docs/en/faq
- group: auth
  title: ''
  type: Authentication
  url: authentication/hotmart-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/hotmart-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/hotmart-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/hotmart-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/hotmart-conformance.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/hotmart-rate-limits.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/hotmart-sandbox.yml
- group: build
  title: ''
  type: Examples
  url: examples/hotmart-code-samples.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/hotmart-data-model.yml
- group: design
  title: ''
  type: Components
  url: components/hotmart-components.yml
- group: build
  title: ''
  type: Packages
  url: packages/hotmart-packages.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/hotmart-webhooks.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/hotmart-llms.txt
- group: auth
  title: ''
  type: Security
  url: https://hotmart.com/en/legal/cybersecurity-policy
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/hotmart-vulnerability-disclosure.yml
created: '2026-08-04'
description: 'Hotmart is a Brazilian creator-economy platform for producing, selling and delivering digital products — online courses, ebooks, mentorships, paid communities, events and, more recently, physical products. It bundles a hosted checkout, a marketplace, an affiliate network, a members-area LMS (Hotmart Club) and payment processing as merchant of record (HotPay), and sells into more than 180 countries. Hotmart Developers is the public REST API over that platform: OAuth 2.0 client-credentials authentication, product-area path prefixes (/payments, /club, /products, /physicalproducts, /events, /accounts, /user), cursor pagination, a sparse-fieldset `select` parameter, a 500-request-per-minute rate limit, a full-parity sandbox host, and a per-product webhook (postback) event surface carrying purchase, subscription, members-area and logistics events on two independently versioned payload schemas. Hotmart publishes no OpenAPI, no SDK and no CLI — the contract an integrator works from
  is prose documentation plus per-endpoint cURL, Node and Java request samples.'
image: https://hotmart.com/static/app-hotmart-next/images/share--general.jpg
layout: provider
modified: '2026-08-04'
name: Hotmart
nav: Providers
network: true
overview: 'Hotmart publishes 8 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Creator Economy, Digital Products, Online Courses, and E-Commerce.


  The Hotmart catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Hotmart''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, pricing, signup flow, and 27 more developer resources.'
random_paper: 89
rate_limits:
- limit_count: 1
  name: Hotmart Rate Limits
  slug: hotmart-rate-limits
score:
  band: developing
  composite: 52.7
  delta: 0.0
  facets:
    commercial_clarity: 44.7
    contract_quality: 51.6
    developer_ergonomics: 60.3
    discoverability: 92.6
    governance: 3.1
    operational_transparency: 76.3
  previous_composite: 52.7
  provenance:
    conformance: derived
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 48.4
  schema_version: 0.9.1
  scored_at: '2026-08-06'
  trend: flat
security:
- kind: authentication
  name: Hotmart Authentication
  slug: hotmart-authentication
  summary_line: oauth2/http · 2 schemes
- kind: domain-security
  name: Hotmart Domain Security
  slug: hotmart-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Hotmart Vulnerability Disclosure
  slug: hotmart-vulnerability-disclosure
  summary_line: Hackerone
slug: hotmart
tags:
- Company
- Creator Economy
- Digital Products
- Online Courses
- E-Commerce
- Payments
- Subscriptions
- Affiliate Marketing
- Webhooks
- Learning Management
- Brazil
website: https://hotmart.com/en
---
