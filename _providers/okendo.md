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
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: true
    idempotency: false
    mcp_server: derived
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 34.5
  scored_at: '2026-08-10'
api_count: 2
apis:
- description: Server-side Enterprise REST API for managing reviews (list/get/update/reply), review groups, customers and profiles, loyalty (rules, transactions, VIP tiers, coupons), survey and quiz responses, trans
  name: Okendo Merchant REST API
  slug: okendo-merchant-rest-api
- description: Public, unauthenticated read API (scoped by okendo_user_id in the path) for displaying published reviews, review aggregates, review media, AI review summaries/keywords and product questions across pro
  name: Okendo Storefront REST API
  slug: okendo-storefront-rest-api
artifact_total: 8
asyncapis:
- description: ''
  name: Okendo Webhooks
  slug: okendo-webhooks
common:
- group: company
  title: ''
  type: Website
  url: https://www.okendo.io/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.okendo.io/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.okendo.io/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.okendo.io/merchant-rest-api/endpoints
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.okendo.io/merchant-rest-api/quick-start
- group: operate
  title: ''
  type: Support
  url: https://support.okendo.io
- group: company
  title: ''
  type: Blog
  url: https://okendo.io/resources/blog/
- group: commercial
  title: ''
  type: Pricing
  url: https://okendo.io/pricing/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://okendo.io/legal-merchants/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://okendo.io/legal-end-users/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.okendo.io/
- group: auth
  title: ''
  type: Security
  url: https://okendo.io/security/
- group: auth
  title: ''
  type: TrustCenter
  url: security/okendo-trust-center.yml
- group: auth
  title: ''
  type: Compliance
  url: https://trust.okendo.io/
- group: auth
  title: ''
  type: Authentication
  url: authentication/okendo-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/okendo-conventions.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/okendo-webhooks.yml
- group: build
  title: ''
  type: Packages
  url: packages/okendo-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/okendo-packages.yml
- group: design
  title: ''
  type: Components
  url: components/okendo-components.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/okendo-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/okendo-llms.txt
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/okendo-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/okendo-conformance.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/okendo-data-model.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/okendo-domain-security.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/okendo-vulnerability-disclosure.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-07-17'
description: 'Okendo is a customer-marketing platform for ecommerce brands, centered on the Shopify ecosystem, that unifies product reviews and ratings, loyalty programs, referrals, quizzes and surveys to drive conversion and repeat purchases. For developers Okendo exposes two REST surfaces: a server-side Merchant (Enterprise) REST API (https://api.okendo.io/enterprise, HTTP Basic auth plus a dated okendo-api-version header) for reviews moderation, loyalty, customers, surveys, quizzes, settings and webhook management; and a public Storefront REST API for reading published reviews, aggregates, media and Q&A. It also ships embeddable on-site widgets, a Storefront Javascript API, and first-party Vue and Shopify Hydrogen component packages, plus a webhook event stream across reviews, loyalty, surveys, quizzes and referrals.'
image: https://www.okendo.io/favicon.ico
layout: provider
mcp_servers:
- description: ''
  name: okendo-mcp.yml
  slug: okendo-mcpyml
modified: '2026-07-20'
name: Okendo
nav: Providers
network: true
overview: 'Okendo publishes 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Business Applications, Reviews, Ratings, and Ecommerce.


  The Okendo catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Okendo''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, pricing, authentication, and 21 more developer resources.'
random_paper: 60
score:
  band: developing
  composite: 48.4
  delta: 0.0
  facets:
    commercial_clarity: 47.4
    contract_quality: 51.6
    developer_ergonomics: 62.5
    discoverability: 87.0
    governance: 3.1
    operational_transparency: 34.2
  previous_composite: 48.4
  provenance:
    conformance: derived
    mcp: derived
    skills: derived
  schema_version: 0.9.1
  scored_at: '2026-08-10'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/okendo/refs/heads/main/screenshots/okendo-2026-08-07T190049.png
security:
- kind: authentication
  name: Okendo Authentication
  slug: okendo-authentication
  summary_line: http · 2 schemes
- kind: domain-security
  name: Okendo Domain Security
  slug: okendo-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Okendo Vulnerability Disclosure
  slug: okendo-vulnerability-disclosure
  summary_line: disclosure policy published
- kind: trust-center
  name: Okendo Trust Center
  slug: okendo-trust-center
  summary_line: SOC 2, GDPR
slug: okendo
tags:
- Company
- Business Applications
- Reviews
- Ratings
- Ecommerce
- Loyalty
- Customer Marketing
- Shopify
- Webhooks
website: https://www.okendo.io/
---
