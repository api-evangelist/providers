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
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    error_semantics: true
    idempotency: false
    mcp_server: true
    openapi_examples: false
    rate_limit_signal: true
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.1
  score: 72.1
  scored_at: '2026-07-23'
agentic_access:
- acting_count: 1
  human_in_the_loop: 0
  name: Skimbit Agentic Access
  operation_count: 19
  slug: skimbit-agentic-access
  summary_line: 19 operations · 1 acting
api_count: 8
apis:
- description: The Commissions API from SkimBit — 1 operation(s) for commissions.
  name: SkimBit Commissions API
  slug: skimbit-commissions-api
- description: The Domains API from SkimBit — 1 operation(s) for domains.
  name: SkimBit Domains API
  slug: skimbit-domains-api
- description: The Merchants API from SkimBit — 1 operation(s) for merchants.
  name: SkimBit Merchants API
  slug: skimbit-merchants-api
- description: The Offers API from SkimBit — 1 operation(s) for offers.
  name: SkimBit Offers API
  slug: skimbit-offers-api
- description: The Payments API from SkimBit — 1 operation(s) for payments.
  name: SkimBit Payments API
  slug: skimbit-payments-api
- description: The Products API from SkimBit — 4 operation(s) for products.
  name: SkimBit Products API
  slug: skimbit-products-api
- description: The Reports API from SkimBit — 8 operation(s) for reports.
  name: SkimBit Reports API
  slug: skimbit-reports-api
- description: The Verticals API from SkimBit — 2 operation(s) for verticals.
  name: SkimBit Verticals API
  slug: skimbit-verticals-api
artifact_total: 13
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/skimbit-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://skimlinks.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developers.skimlinks.com
- group: docs
  title: ''
  type: Documentation
  url: https://developers.skimlinks.com
- group: docs
  title: ''
  type: APIReference
  url: https://developers.skimlinks.com/merchant.html
- group: start
  title: ''
  type: SignUp
  url: https://signup.skimlinks.com/
- group: start
  title: ''
  type: Login
  url: https://hub.skimlinks.com/login
- group: operate
  title: ''
  type: Support
  url: https://support.skimlinks.com/hc/en-us
- group: company
  title: ''
  type: Blog
  url: https://www.skimlinks.com/insights/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.skimlinks.com/privacy-policy/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.skimlinks.com/terms-of-service/
- group: auth
  title: ''
  type: Authentication
  url: authentication/skimbit-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/skimbit-conventions.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/skimbit-rate-limits.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/skimbit-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/skimbit-lifecycle.yml
- group: operate
  title: ''
  type: Deprecation
  url: lifecycle/skimbit-lifecycle.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/skimbit-data-model.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/skimbit-conformance.yml
- group: design
  title: ''
  type: Components
  url: components/skimbit-components.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/skimbit-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/skimbit-llms.txt
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/skimbit-agentic-access.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/skimbit-merchant-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/skimbit-reporting-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/skimbit-product-key-overlay.yaml
created: '2026-07-17'
description: SkimBit Ltd, operating as Skimlinks, is a London-founded content-monetization and affiliate-marketing platform (now part of Taboola) that helps publishers and content creators earn commerce revenue from the products and merchants they mention in editorial content. Skimlinks automatically affiliates outbound merchant links, tracks the resulting clicks and commissions across thousands of affiliate networks and merchant programs, and pays publishers a share of the revenue. For developers, Skimlinks exposes a suite of publisher-facing REST APIs — the Merchant API (merchant programs, domains, verticals and offers), the Reporting API (raw commissions, aggregated performance, trending/purchased products, payment status and deactivated merchants) and the Product Key API (product details, pricing, availability and merchant alternatives across a billion+ product offers) — plus the Skimlinks JavaScript on-page monetization script and a batch Data Pipe delivering event-level clicks, impressions,
  commissions and product-purchase data to cloud storage.
image: https://www.skimlinks.com/wp-content/uploads/2025/06/Colour_icon.svg
layout: provider
mcp_servers:
- description: ''
  name: skimbit-mcp.yml
  slug: skimbit-mcpyml
modified: '2026-07-21'
name: SkimBit
nav: Providers
network: true
overview: 'SkimBit publishes 8 APIs on the [APIs.io](https://apis.io/) network, including Commissions API, Domains API, Merchants API, and 5 more. Tagged areas include Company, Affiliate Marketing, Content Monetization, Commerce, and Publishers.


  SkimBit''s developer surface includes documentation, API reference, signup flow, support, engineering blog, authentication, and 21 more developer resources.'
random_paper: 41
rate_limits:
- limit_count: 0
  name: Skimbit Rate Limits
  slug: skimbit-rate-limits
score:
  band: thin
  composite: 43.8
  delta: 0.0
  facets:
    commercial_clarity: 34.2
    contract_quality: 58.6
    developer_ergonomics: 56.5
    discoverability: 100.0
    governance: 0.0
    operational_transparency: 7.9
  previous_composite: 43.8
  schema_version: 0.5
  scored_at: '2026-07-23'
  trend: flat
security:
- kind: authentication
  name: Skimbit Authentication
  slug: skimbit-authentication
  summary_line: apiKey/oauth2-like-client-credentials · 1 scheme
- kind: domain-security
  name: Skimbit Domain Security
  slug: skimbit-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: skimbit
tags:
- Company
- Affiliate Marketing
- Content Monetization
- Commerce
- Publishers
- Advertising
- Retail
- Reporting
- Products
- eCommerce
website: https://skimlinks.com
---
