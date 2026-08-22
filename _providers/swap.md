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
    error_semantics: documented
    event_surface_described: true
    idempotency: documented
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 37.4
  scored_at: '2026-08-19'
api_count: 6
apis:
- description: 'Public Gateway API for the Agentic Storefront product: conversational discovery and chat, catalog/collection browsing, cart and checkout sessions, virtual try-on, orders and shipments, user profile an'
  name: Swap Agentic Storefront API
  slug: swap-agentic-storefront-api
- description: 'Public API for Swap Global: the cross-border checkout flow of classify (HS codes) then optional shipping rates, calculate (taxes and duties), and order completion reporting.'
  name: Swap Global API
  slug: swap-global-api
- description: 'Public API for the Swap Protect product: enroll protected orders and manage claim activity (create/update orders, retrieve claims, send claim messages, fetch delivery declarations).'
  name: Swap Protect API
  slug: swap-protect-api
- description: 'Public API for Swap Returns reverse logistics: list external returns (V1 and V2) and update quality-control status, with per-store JWT-signed webhooks for return lifecycle events.'
  name: Swap Returns API
  slug: swap-returns-api
- description: 'Public Shipping / Swap Values API: enrich a Shipment Intent into a customs-correct Compliance Pack (declared values, HS codes, commercial-invoice fields), create and cancel carrier shipping labels, an'
  name: Swap Shipping API
  slug: swap-shipping-api
- description: 'Public Total Landed Cost API: compute guaranteed landed cost (duties, taxes, import fees) for single or bulk cross-border shipments, request HS-code classification, and report shipped or voided transa'
  name: Swap TLC API
  slug: swap-tlc-api
artifact_total: 11
asyncapis:
- description: ''
  name: Swap Webhooks
  slug: swap-webhooks
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/swap-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.swap-commerce.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.api-swap-os.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.api-swap-os.com/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.api-swap-os.com/products/choosing-an-api/
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.api-swap-os.com/quickstart/make-first-request/
- group: start
  title: ''
  type: Quickstart
  url: https://docs.api-swap-os.com/quickstart/authentication/
- group: operate
  title: ''
  type: HelpCenter
  url: https://help.swap-commerce.com/
- group: operate
  title: ''
  type: Support
  url: mailto:contact@swap-commerce.com
- group: company
  title: ''
  type: Blog
  url: https://www.swap-commerce.com/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/swap-commerce
- group: start
  title: ''
  type: SignUp
  url: https://www.swap-commerce.com/book-a-demo
- group: start
  title: ''
  type: Login
  url: https://swap-os.com/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.swap-commerce.com/privacy-policy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.swap-commerce.com/terms-conditions
- group: auth
  title: ''
  type: Compliance
  url: https://www.swap-commerce.com/security-compliance
- group: auth
  title: ''
  type: TrustCenter
  url: https://www.swap-commerce.com/security-compliance
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/swap-llms.txt
- group: auth
  title: ''
  type: Authentication
  url: authentication/swap-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/swap-conventions.yml
- group: design
  title: ''
  type: Idempotency
  url: conventions/swap-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/swap-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/swap-lifecycle.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/swap-changelog.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/swap-webhooks.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/swap-conformance.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/swap-sandbox.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/swap-data-model.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/swap-mcp.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-07-17'
description: 'Swap (Swap Commerce, Inc.) is an agentic commerce platform that helps merchants sell, ship, and scale globally, powering 700+ brands across AI-led product discovery, cross-border checkout, fulfillment, and returns on a shared per-store data layer. Swap exposes six independent public API surfaces: the Agentic Storefront API (conversational discovery, chat, virtual try-on, and checkout), the Global API (cross-border classify, shipping rates, tax and duty calculation, and order reporting), the Protect API (package-protection order enrollment and claims), the Returns API (reverse logistics and quality control), the Shipping API / Swap Values API (customs-correct declared values and commercial-invoice enrichment for any carrier label stack), and the TLC API (guaranteed total landed cost and HS-code classification). Every surface authenticates with a per-API, per-environment API key plus a store identifier, and several ship JWT- or HMAC-signed webhooks.'
image: https://cdn.sanity.io/images/yqjhv3kv/production/8a30678bcf375982957978b1f5b4bd4c4eb1c3d1-1200x630.png
layout: provider
mcp_servers:
- description: ''
  name: swap-mcp.yml
  slug: swap-mcpyml
modified: '2026-07-21'
name: Swap
nav: Providers
network: true
overview: 'Swap publishes 6 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Ecommerce, Cross-Border, Customs, and Shipping.


  The Swap catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Swap''s developer surface includes documentation, API reference, getting-started guide, quickstart, support, engineering blog, signup flow, and 23 more developer resources.'
random_paper: 2
score:
  band: developing
  composite: 50.4
  delta: 1.9
  facets:
    access_clarity: 50.0
    commercial_clarity: 50.0
    contract_governance: 18.2
    contract_quality: 45.1
    developer_ergonomics: 66.1
    discoverability: 81.5
    governance: 18.2
    operational_transparency: 26.3
  previous_composite: 48.5
  provenance:
    conformance: first-party
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 46.9
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/swap/refs/heads/main/screenshots/swap-2026-08-17T082210.png
security:
- kind: authentication
  name: Swap Authentication
  slug: swap-authentication
  summary_line: apiKey/http · 8 schemes
- kind: domain-security
  name: Swap Domain Security
  slug: swap-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Swap Trust Center
  slug: swap-trust-center
  summary_line: ISO 27001:2022
slug: swap
tags:
- Company
- Ecommerce
- Cross-Border
- Customs
- Shipping
- Returns
- Tax
- Duties
- Agentic Commerce
- Checkout
- Package Protection
- Landed Cost
website: https://www.swap-commerce.com/
---
