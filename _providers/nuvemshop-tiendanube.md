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
  band: human-only
  dimensions:
    agent_skills: false
    agentic_access: false
    asyncapi_events: true
    auth_clarity: false
    consent_identity: true
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: false
    well_known_catalog: true
  schema_version: 0.1
  score: 12.5
  scored_at: '2026-07-27'
api_count: 1
apis:
- description: 'REST API for building public apps and integrations on the Nuvemshop / Tiendanube e-commerce platform: products, orders, customers, categories, coupons, discounts, transactions, shipping, locations, me'
  name: Nuvemshop Tiendanube API
  slug: nuvemshop-tiendanube-api
artifact_total: 8
asyncapis:
- description: Webhook event surface for the Nuvemshop/Tiendanube platform. Apps register a Webhook resource (event + url) and receive HTTP POST callbacks signed with HMAC-SHA256 in the x-linkedstore-hmac-sha256 hea
  name: Nuvemshop Tiendanube Webhook Events
  slug: nuvemshop-tiendanube-events-asyncapi
- description: ''
  name: Nuvemshop Tiendanube Webhooks
  slug: nuvemshop-tiendanube-webhooks
common:
- group: company
  title: ''
  type: Website
  url: https://www.nuvemshop.com.br/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://dev.tiendanube.com/
- group: docs
  title: ''
  type: Documentation
  url: https://tiendanube.github.io/api-documentation/
- group: docs
  title: ''
  type: APIReference
  url: https://tiendanube.github.io/api-documentation/intro
- group: start
  title: ''
  type: GettingStarted
  url: https://dev.tiendanube.com/docs/getting-started
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/TiendaNube
- group: operate
  title: ''
  type: Support
  url: https://atendimento.nuvemshop.com.br/
- group: company
  title: ''
  type: Blog
  url: https://www.nuvemshop.com.br/blog
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.nuvemshop.com.br/termos-de-uso
- group: operate
  title: ''
  type: StatusPage
  url: https://status.nuvemshop.com.br/
- group: build
  title: ''
  type: SDKs
  url: packages/nuvemshop-tiendanube-packages.yml
- group: build
  title: ''
  type: Packages
  url: packages/nuvemshop-tiendanube-packages.yml
- group: build
  title: ''
  type: CLI
  url: cli/nuvemshop-tiendanube-cli.yml
- group: design
  title: ''
  type: Components
  url: components/nuvemshop-tiendanube-components.yml
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/nuvemshop-tiendanube-security.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/nuvemshop-tiendanube-well-known.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/nuvemshop-tiendanube-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: security/nuvemshop-tiendanube-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/nuvemshop-tiendanube-domain-security.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/nuvemshop-tiendanube-llms.txt
created: '2026-07-17'
description: Nuvemshop (Tiendanube in Spanish-speaking markets) is the leading e-commerce platform in Latin America, powering online stores for merchants across Brazil, Argentina, Mexico, Chile, Colombia and beyond. Its REST API lets partners and developers build public apps and integrations that manage products, variants, images, categories, orders, draft orders, abandoned checkouts, customers, coupons, discounts, transactions, payment providers, shipping carriers, locations, metafields, scripts and store data. Apps authenticate with a restricted OAuth 2 authorization-code flow (non-expiring bearer tokens), respect a leaky-bucket rate limit, and subscribe to a rich catalog of webhooks (order, product, customer, category, fulfillment, subscription and data-protection events) verified with HMAC-SHA256. The platform also ships an official CLI, the nube-sdk JavaScript packages, and the Nimbus design system.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/nuvemshop-tiendanube.png
layout: provider
mcp_servers:
- description: ''
  name: nuvemshop-tiendanube-mcp.yml
  slug: nuvemshop-tiendanube-mcpyml
modified: '2026-07-20'
name: Nuvemshop Tiendanube
nav: Providers
network: true
overview: 'Nuvemshop Tiendanube publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, E-Commerce, Retail, Online Stores, and Payments.


  The Nuvemshop Tiendanube catalog on APIs.io includes 2 event-driven AsyncAPI specifications.


  Nuvemshop Tiendanube''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, CLI, and 14 more developer resources.'
random_paper: 57
scopes:
- name: Nuvemshop Tiendanube Scopes
  scope_count: 12
  slug: nuvemshop-tiendanube-scopes
  summary_line: 12 scopes · authorizationCode
score:
  band: thin
  composite: 37.1
  delta: 0.0
  facets:
    commercial_clarity: 10.5
    contract_quality: 29.2
    developer_ergonomics: 54.3
    discoverability: 92.5
    governance: 0.0
    operational_transparency: 31.6
  previous_composite: 37.1
  regulatory:
    applies: true
    regime: Payments
    regime_id: payments
    score: 56.5
  schema_version: 0.5
  scored_at: '2026-07-27'
  trend: flat
security:
- kind: authentication
  name: Nuvemshop Tiendanube Authentication
  slug: nuvemshop-tiendanube-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Nuvemshop Tiendanube Domain Security
  slug: nuvemshop-tiendanube-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: vulnerability-disclosure
  name: Nuvemshop Tiendanube Vulnerability Disclosure
  slug: nuvemshop-tiendanube-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: nuvemshop-tiendanube
tags:
- Company
- E-Commerce
- Retail
- Online Stores
- Payments
- Shipping
- Webhooks
- OAuth
- Latin America
- Storefront
- Apps Platform
website: https://www.nuvemshop.com.br/
---
