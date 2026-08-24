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
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: verified
    event_surface_described: true
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    rate_limit_signal: false
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 47.1
  scored_at: '2026-08-24'
agentic_access:
- acting_count: 28
  human_in_the_loop: 0
  name: Neon Commerce Agentic Access
  operation_count: 48
  slug: neon-commerce-agentic-access
  summary_line: 48 operations · 28 acting
api_count: 13
apis:
- description: The Account API from Neon Commerce — 2 operation(s) for account.
  name: Neon Commerce Account API
  slug: neon-commerce-account-api
- description: The Assets API from Neon Commerce — 4 operation(s) for assets.
  name: Neon Commerce Assets API
  slug: neon-commerce-assets-api
- description: The Auth API from Neon Commerce — 1 operation(s) for auth.
  name: Neon Commerce Auth API
  slug: neon-commerce-auth-api
- description: The Checkout API from Neon Commerce — 3 operation(s) for checkout.
  name: Neon Commerce Checkout API
  slug: neon-commerce-checkout-api
- description: The Client API from Neon Commerce — 4 operation(s) for client.
  name: Neon Commerce Client API
  slug: neon-commerce-client-api
- description: The Payouts API from Neon Commerce — 1 operation(s) for payouts.
  name: Neon Commerce Payouts API
  slug: neon-commerce-payouts-api
- description: The Prices API from Neon Commerce — 1 operation(s) for prices.
  name: Neon Commerce Prices API
  slug: neon-commerce-prices-api
- description: The Pricing Sheet API from Neon Commerce — 1 operation(s) for pricing sheet.
  name: Neon Commerce Pricing Sheet API
  slug: neon-commerce-pricing-sheet-api
- description: The Purchases API from Neon Commerce — 6 operation(s) for purchases.
  name: Neon Commerce Purchases API
  slug: neon-commerce-purchases-api
- description: The Reports API from Neon Commerce — 1 operation(s) for reports.
  name: Neon Commerce Reports API
  slug: neon-commerce-reports-api
- description: The Status API from Neon Commerce — 1 operation(s) for status.
  name: Neon Commerce Status API
  slug: neon-commerce-status-api
- description: The Storefront API from Neon Commerce — 9 operation(s) for storefront.
  name: Neon Commerce Storefront API
  slug: neon-commerce-storefront-api
- description: The Subscriptions API from Neon Commerce — 4 operation(s) for subscriptions.
  name: Neon Commerce Subscriptions API
  slug: neon-commerce-subscriptions-api
artifact_total: 32
asyncapis:
- description: ''
  name: Neon Commerce Webhooks Asyncapi
  slug: neon-commerce-webhooks-asyncapi
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Account API
  slug: open-neon-commerce-account-api
- collection_type: open
  name: Account Assets API
  slug: open-neon-commerce-assets-api
- collection_type: open
  name: Account Auth API
  slug: open-neon-commerce-auth-api
- collection_type: open
  name: Account Checkout API
  slug: open-neon-commerce-checkout-api
- collection_type: open
  name: Account Client API
  slug: open-neon-commerce-client-api
- collection_type: open
  name: Account Payouts API
  slug: open-neon-commerce-payouts-api
- collection_type: open
  name: Account Prices API
  slug: open-neon-commerce-prices-api
- collection_type: open
  name: Account Pricing Sheet API
  slug: open-neon-commerce-pricing-sheet-api
- collection_type: open
  name: Account Purchases API
  slug: open-neon-commerce-purchases-api
- collection_type: open
  name: Account Reports API
  slug: open-neon-commerce-reports-api
- collection_type: open
  name: Account Status API
  slug: open-neon-commerce-status-api
- collection_type: open
  name: Account Storefront API
  slug: open-neon-commerce-storefront-api
- collection_type: open
  name: Account Subscriptions API
  slug: open-neon-commerce-subscriptions-api
common:
- group: other
  title: ''
  type: Overlay
  url: overlays/neon-commerce-account-overlay.yaml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/neon-commerce-domain-security.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/neon-commerce-agentic-access.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/neon-commerce-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://www.neonpay.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://console.neonpay.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.neonpay.com/docs/getting-started
- group: docs
  title: ''
  type: APIReference
  url: https://docs.neonpay.com/reference
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.neonpay.com/docs/getting-started
- group: operate
  title: ''
  type: Support
  url: https://support.neonpay.com
- group: company
  title: ''
  type: Blog
  url: https://www.neonpay.com/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://docs.neonpay.com/docs/pricing
- group: start
  title: ''
  type: SignUp
  url: https://console.neonpay.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.neonpay.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.neonpay.com/privacy
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/neon-xyz
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/neonpay
- group: operate
  title: ''
  type: ChangeLog
  url: https://docs.neonpay.com/changelog
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/neon-commerce-llms.txt
- group: design
  title: ''
  type: Conventions
  url: conventions/neon-commerce-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/neon-commerce-problem-types.yml
- group: build
  title: ''
  type: DeclineCodes
  url: errors/neon-commerce-decline-codes.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/neon-commerce-sandbox.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/neon-commerce-changelog.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/neon-commerce-lifecycle.yml
- group: operate
  title: ''
  type: Deprecation
  url: lifecycle/neon-commerce-lifecycle.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/neon-commerce-webhooks-asyncapi.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/neon-commerce-data-model.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/neon-commerce-mcp.yml
- group: build
  title: ''
  type: Packages
  url: packages/neon-commerce-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/neon-commerce-packages.yml
- group: design
  title: ''
  type: Components
  url: components/neon-commerce-components.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/neon-commerce-conformance.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-07-17'
description: Neon Commerce (Neon) is the direct-to-consumer commerce and payments platform for mobile and PC game developers, backed by a16z Games, Thrive Capital, Griffin Gaming Partners and Ribbit Capital. Neon lets studios launch a branded web storefront (Neon Shop), embed or host checkout (Neon Checkout), and accept global payments across 50+ markets and 30+ payment methods as merchant of record — shifting revenue away from app-store fees to owned direct-to-consumer channels. The Neon API (base https://api.neonpay.com) exposes storefront/offer/item management, checkout and subscription creation, purchase and refund lookups, payouts, reports, player authentication, brand/inventory image assets, and a full webhook/callback event surface, with sandbox and production environments scoped by API key.
image: https://www.neonpay.com/api/media/file/meta-image-1200x630.jpg
layout: provider
mcp_servers:
- description: ''
  name: Neon Commerce MCP Server
  slug: neon-commerce-mcp-server
modified: '2026-07-20'
name: Neon Commerce
nav: Providers
network: true
overview: 'Neon Commerce publishes 13 APIs on the [APIs.io](https://apis.io/) network, including Account API, Assets API, Auth API, and 10 more. Tagged areas include Commerce, Payments, Gaming, Checkout, and Storefront.


  The Neon Commerce catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Neon Commerce''s developer surface includes authentication, documentation, API reference, getting-started guide, support, engineering blog, pricing, and 27 more developer resources.'
random_paper: 18
score:
  band: strong
  composite: 55.8
  delta: 0.0
  facets:
    access_clarity: 44.7
    commercial_clarity: 44.7
    contract_governance: 16.7
    contract_quality: 64.5
    developer_ergonomics: 64.9
    discoverability: 81.5
    governance: 16.7
    operational_transparency: 36.8
  previous_composite: 55.8
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 13
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 51.6
  schema_version: 0.12.1
  scored_at: '2026-08-24'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/neon-commerce/refs/heads/main/screenshots/neon-commerce-2026-08-17T082605.png
security:
- kind: authentication
  name: Neon Commerce Authentication
  slug: neon-commerce-authentication
  summary_line: apiKey · 3 schemes
- kind: domain-security
  name: Neon Commerce Domain Security
  slug: neon-commerce-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: neon-commerce
tags:
- Commerce
- Payments
- Gaming
- Checkout
- Storefront
- Direct to Consumer
- Subscription
- Merchant of Record
- Game Monetization
- Company
website: https://www.neonpay.com/
---
