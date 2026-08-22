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
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: documented
    event_surface_described: derived
    idempotency: false
    mcp_server: false
    openapi_examples: partial
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.2
  score: 41.2
  scored_at: '2026-08-19'
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
artifact_total: 24
asyncapis:
- description: 'The Skimlinks Data Pipe is the event-level data surface behind the Skimlinks affiliate platform: impressions, clicks, commissions and products purchased, cleaned and exported daily to a customer-owned'
  name: Skimlinks Data Pipe
  slug: skimbit-data-pipe-asyncapi
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Skimlinks Merchant Commissions API
  slug: open-skimbit-commissions-api
- collection_type: open
  name: Skimlinks Merchant Commissions Domains API
  slug: open-skimbit-domains-api
- collection_type: open
  name: Skimlinks Merchant Commissions Merchants API
  slug: open-skimbit-merchants-api
- collection_type: open
  name: Skimlinks Merchant Commissions Offers API
  slug: open-skimbit-offers-api
- collection_type: open
  name: Skimlinks Merchant Commissions Payments API
  slug: open-skimbit-payments-api
- collection_type: open
  name: Skimlinks Merchant Commissions Products API
  slug: open-skimbit-products-api
- collection_type: open
  name: Skimlinks Merchant Commissions Reports API
  slug: open-skimbit-reports-api
- collection_type: open
  name: Skimlinks Merchant Commissions Verticals API
  slug: open-skimbit-verticals-api
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
- group: build
  title: ''
  type: Packages
  url: packages/skimbit-packages.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/skimbit-plans-pricing.yml
- group: docs
  title: ''
  type: AsyncAPI
  url: asyncapi/skimbit-data-pipe-asyncapi.yml
- group: build
  title: ''
  type: ToolCrosswalk
  url: mcp/skimbit-tool-crosswalk.yml
- group: docs
  title: ''
  type: Documentation
  url: https://developers.skimlinks.com/data-pipe.html
created: '2026-07-17'
description: SkimBit Ltd, operating as Skimlinks, is a London-founded content-monetization and affiliate-marketing platform (now part of Taboola) that helps publishers and content creators earn commerce revenue from the products and merchants they mention in editorial content. Skimlinks automatically affiliates outbound merchant links, tracks the resulting clicks and commissions across thousands of affiliate networks and merchant programs, and pays publishers a share of the revenue. For developers, Skimlinks exposes a suite of publisher-facing REST APIs — the Merchant API (merchant programs, domains, verticals and offers), the Reporting API (raw commissions, aggregated performance, trending/purchased products, payment status and deactivated merchants) and the Product Key API (product details, pricing, availability and merchant alternatives across a billion+ product offers) — plus the Skimlinks JavaScript on-page monetization script and a batch Data Pipe delivering event-level clicks, impressions,
  commissions and product-purchase data to cloud storage.
image: https://www.skimlinks.com/wp-content/uploads/2025/06/Colour_icon.svg
layout: provider
mcp_servers:
- description: ''
  name: skimbit-mcp.yml
  slug: skimbit-mcpyml
modified: '2026-08-13'
name: SkimBit
nav: Providers
network: true
overview: 'SkimBit publishes 8 APIs on the [APIs.io](https://apis.io/) network, including Commissions API, Domains API, Merchants API, and 5 more. Tagged areas include Company, Affiliate Marketing, Content Monetization, Commerce, and Publishers.


  The SkimBit catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  SkimBit''s developer surface includes documentation, API reference, signup flow, support, engineering blog, authentication, and 26 more developer resources.'
plans:
- name: Skimbit Plans Pricing
  plan_count: 0
  slug: skimbit-plans-pricing
random_paper: 20
rate_limits:
- limit_count: 6
  name: Skimbit Rate Limits
  slug: skimbit-rate-limits
score:
  band: developing
  composite: 48.5
  delta: 0.0
  facets:
    access_clarity: 34.2
    commercial_clarity: 34.2
    contract_governance: 16.7
    contract_quality: 63.3
    developer_ergonomics: 47.0
    discoverability: 92.6
    governance: 16.7
    operational_transparency: 39.5
  previous_composite: 48.5
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 100.0
      total: 8
    mcp: derived
    skills: derived
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/skimbit/refs/heads/main/screenshots/skimbit-2026-08-17T081913.png
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
