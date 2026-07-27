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
  band: agent-native
  dimensions:
    agent_skills: true
    agentic_access: true
    asyncapi_events: true
    auth_clarity: true
    consent_identity: false
    error_semantics: true
    idempotency: true
    mcp_server: true
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.1
  score: 83.7
  scored_at: '2026-07-27'
agentic_access:
- acting_count: 7
  human_in_the_loop: 0
  name: Goody Agentic Access
  operation_count: 23
  slug: goody-agentic-access
  summary_line: 23 operations · 7 acting
api_count: 12
apis:
- description: The Brands API from Goody — 1 operation(s) for brands.
  name: Goody Brands API
  slug: goody-brands-api
- description: The Cards API from Goody — 1 operation(s) for cards.
  name: Goody Cards API
  slug: goody-cards-api
- description: The Collections API from Goody — 2 operation(s) for collections.
  name: Goody Collections API
  slug: goody-collections-api
- description: The Commerce User Payment Methods API from Goody — 1 operation(s) for commerce user payment methods.
  name: Goody Commerce User Payment Methods API
  slug: goody-commerce-user-payment-methods-api
- description: The Me API from Goody — 1 operation(s) for me.
  name: Goody Me API
  slug: goody-me-api
- description: The Order Activities API from Goody — 1 operation(s) for order activities.
  name: Goody Order Activities API
  slug: goody-order-activities-api
- description: The Order Batches API from Goody — 5 operation(s) for order batches.
  name: Goody Order Batches API
  slug: goody-order-batches-api
- description: The Orders API from Goody — 4 operation(s) for orders.
  name: Goody Orders API
  slug: goody-orders-api
- description: The Payment Methods API from Goody — 1 operation(s) for payment methods.
  name: Goody Payment Methods API
  slug: goody-payment-methods-api
- description: The Products API from Goody — 2 operation(s) for products.
  name: Goody Products API
  slug: goody-products-api
- description: The Webhooks API from Goody — 2 operation(s) for webhooks.
  name: Goody Webhooks API
  slug: goody-webhooks-api
- description: The Workspaces API from Goody — 1 operation(s) for workspaces.
  name: Goody Workspaces API
  slug: goody-workspaces-api
artifact_total: 19
asyncapis:
- description: ''
  name: Goody Webhooks
  slug: goody-webhooks
common:
- group: company
  title: ''
  type: Website
  url: https://www.ongoody.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.ongoody.com/
- group: docs
  title: ''
  type: Documentation
  url: https://developer.ongoody.com/introduction/overview
- group: docs
  title: ''
  type: APIReference
  url: https://developer.ongoody.com/api-reference/order-batches/create-an-order-batch
- group: start
  title: ''
  type: GettingStarted
  url: https://developer.ongoody.com/commerce-api/authentication
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/ongoody
- group: company
  title: ''
  type: Blog
  url: https://www.ongoody.com/blog
- group: operate
  title: ''
  type: Support
  url: https://goody.kustomer.help/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.ongoody.com/business/pricing
- group: start
  title: ''
  type: SignUp
  url: https://www.ongoody.com/business/gift-api
- group: start
  title: ''
  type: Login
  url: https://www.ongoody.com/business/signin
- group: commercial
  title: ''
  type: TermsOfService
  url: https://assets.ongoody.com/static/terms/PlusTermsAndConditions.pdf
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.ongoody.com/privacy
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/goody-changelog.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/goody-lifecycle.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/goody-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/goody-scopes.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/goody-mcp.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/goody-webhooks.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/goody-conventions.yml
- group: design
  title: ''
  type: Idempotency
  url: conventions/goody-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/goody-problem-types.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/goody-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: https://trust.ongoody.com/
- group: auth
  title: ''
  type: TrustCenter
  url: security/goody-trust-center.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/goody-data-model.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/goody-sandbox.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/goody-well-known.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/goody-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/goody-domain-security.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/goody-llms.txt
created: '2026-07-17'
description: Goody (ongoody.com) is a business and personal gifting platform that lets senders deliver physical products and gift cards without needing a recipient's address — the recipient accepts via a shareable gift link and can swap the gift. For developers, Goody exposes a REST Commerce/Automation API (base https://api.ongoody.com, with a separate sandbox at api.sandbox.ongoody.com) to browse a curated product catalog, price and send gift order-batches to one or many recipients, manage contacts and autogift rules, and track order lifecycle. Bearer API-key auth for the REST API, plus an official hosted MCP server (OAuth2 + PKCE) exposing 28 tools so agents can discover, draft, price, and send gifts in natural language. Webhooks (via Svix) cover the full order lifecycle. SOC 2 certified. Backed by Index Ventures.
image: https://www.ongoody.com/assets/frontend/assets/goody-logo-jy0bt7ba.digested.svg
layout: provider
mcp_servers:
- description: ''
  name: goody-mcp.yml
  slug: goody-mcpyml
modified: '2026-07-19'
name: Goody
nav: Providers
network: true
overview: 'Goody publishes 12 APIs on the [APIs.io](https://apis.io/) network, including Brands API, Cards API, Collections API, and 9 more. Tagged areas include Company, Retail, Gifting, Gift Cards, and E-Commerce.


  The Goody catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Goody''s developer surface includes documentation, API reference, getting-started guide, engineering blog, support, pricing, signup flow, and 25 more developer resources.'
random_paper: 2
scopes:
- name: Goody Scopes
  scope_count: 4
  slug: goody-scopes
  summary_line: 4 scopes · authorizationCode
score:
  band: strong
  composite: 60.0
  delta: 0.0
  facets:
    commercial_clarity: 60.5
    contract_quality: 58.4
    developer_ergonomics: 73.9
    discoverability: 100.0
    governance: 0.0
    operational_transparency: 28.9
  previous_composite: 60.0
  regulatory:
    applies: true
    regime: Payments
    regime_id: payments
    score: 87.0
  schema_version: 0.5
  scored_at: '2026-07-27'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/goody/refs/heads/main/screenshots/goody-2026-07-25T220106.png
security:
- kind: authentication
  name: Goody Authentication
  slug: goody-authentication
  summary_line: http/oauth2 · 2 schemes
- kind: domain-security
  name: Goody Domain Security
  slug: goody-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Goody Trust Center
  slug: goody-trust-center
  summary_line: SOC 2
slug: goody
tags:
- Company
- Retail
- Gifting
- Gift Cards
- E-Commerce
- Commerce
- Payments
- MCP
- Webhooks
- Rewards
website: https://www.ongoody.com/
---
