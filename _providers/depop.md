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
    idempotency: false
    mcp_server: true
    openapi_examples: false
    rate_limit_signal: true
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.1
  score: 81.7
  scored_at: '2026-07-23'
agentic_access:
- acting_count: 27
  human_in_the_loop: 0
  name: Depop Agentic Access
  operation_count: 43
  slug: depop-agentic-access
  summary_line: 43 operations · 27 acting
api_count: 12
apis:
- description: Service health and status endpoints
  name: depop API status API
  slug: depop-api-status-api
- description: OAuth 2.0 authentication endpoints for partner integration
  name: depop Authentication API
  slug: depop-authentication-api
- description: The Docs API from depop — 1 operation(s) for docs.
  name: depop Docs API
  slug: depop-docs-api
- description: Shop and product insights
  name: depop Insights API
  slug: depop-insights-api
- description: Order management and fulfillment operations
  name: depop Orders API
  slug: depop-orders-api
- description: ML-powered price recommendations and pricing guidance
  name: depop Pricing Inspiration API
  slug: depop-pricing-inspiration-api
- description: General product operations
  name: depop Products API
  slug: depop-products-api
- description: Product operations using internal product ID identifiers
  name: depop Products - By Product ID API
  slug: depop-products-by-product-id-api
- description: Product operations using SKU (Stock Keeping Unit) identifiers
  name: depop Products - By SKU API
  slug: depop-products-by-sku-api
- description: Product operations using URL-friendly slug identifiers
  name: depop Products - By Slug API
  slug: depop-products-by-slug-api
- description: Deprecated product endpoints - use By SKU or By Product ID alternatives instead
  name: depop Products - Legacy (Deprecated) API
  slug: depop-products-legacy-deprecated-api
- description: Shop and seller information endpoints
  name: depop Shop Management API
  slug: depop-shop-management-api
arazzos:
- description: ''
  name: _Index
  slug: _index
- description: Create/update a Depop listing by SKU, verify it, then mark it as sold.
  name: List a product and mark it sold
  slug: depop-list-and-sell.arazzo
- description: Read an order, mark a parcel shipped with tracking, optionally refund.
  name: Order fulfillment
  slug: depop-order-fulfillment.arazzo
artifact_total: 23
asyncapis:
- description: Event surface for the Depop Selling API, generated from the webhooks section of the OpenAPI 3.1 document. Depop delivers order and product engagement events to a partner-registered HTTPS endpoint. Eve
  name: Depop Selling API — Webhooks
  slug: depop-webhooks-asyncapi
common:
- group: start
  title: ''
  type: DeveloperPortal
  url: https://partnerapi.depop.com/api-docs/
- group: docs
  title: ''
  type: Documentation
  url: https://partnerapi.depop.com/api-docs/
- group: docs
  title: ''
  type: APIReference
  url: https://partnerapi.depop.com/api-docs/reference/
- group: start
  title: ''
  type: GettingStarted
  url: https://partnerapi.depop.com/api-docs/getting-started/your-first-listing/
- group: operate
  title: ''
  type: StatusPage
  url: https://depopstatus.com/
- group: operate
  title: ''
  type: Support
  url: https://depophelp.zendesk.com/
- group: company
  title: ''
  type: Blog
  url: https://engineering.depop.com/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/depop
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.depop.com/terms/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.depop.com/privacy/
- group: company
  title: ''
  type: Website
  url: https://www.depop.com/
- group: auth
  title: ''
  type: Authentication
  url: authentication/depop-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/depop-scopes.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/depop-problem-types.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/depop-conventions.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/depop-rate-limits.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/depop-lifecycle.yml
- group: operate
  title: ''
  type: Deprecation
  url: lifecycle/depop-lifecycle.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/depop-changelog.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/depop-sandbox.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/depop-conformance.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/depop-data-model.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/depop-webhooks-asyncapi.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/depop-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/depop-llms.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/depop-well-known.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/depop-agentic-access.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/depop-list-and-sell.arazzo.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/depop-order-fulfillment.arazzo.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/depop-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: https://www.depop.com/.well-known/security.txt
- group: auth
  title: ''
  type: DomainSecurity
  url: security/depop-domain-security.yml
created: '2026-07-17'
description: 'Depop is a peer-to-peer fashion marketplace where people buy, sell and discover secondhand and unique clothing. Its Selling API is an enterprise partner API that lets approved partners automate the seller experience on Depop: create and manage listings (by SKU, product id or slug), manage orders, mark parcels shipped, issue refunds, submit and automate offers, read seller and shipping details, and pull shop and product insights. The API is OpenAPI 3.1, secured with per-shop API keys and OAuth 2.0 (Authorization Code + PKCE) with granular scopes, documents rate limits, and emits webhooks for new orders, refunds and product likes. Access is by invitation via developers@depop.com. Depop is backed by Balderton Capital, Creandum, EQT Ventures and HV Capital and is owned by Etsy.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/depop.png
layout: provider
mcp_servers:
- description: ''
  name: depop-mcp.yml
  slug: depop-mcpyml
modified: '2026-07-18'
name: depop
nav: Providers
network: true
overview: 'depop publishes 12 APIs on the [APIs.io](https://apis.io/) network, including API status API, Authentication API, Docs API, and 9 more. Tagged areas include Company, Fashion, Marketplace, E-commerce, and Resale.


  The depop catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  depop''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, authentication, changelog, and 26 more developer resources.'
random_paper: 26
rate_limits:
- limit_count: 0
  name: Depop Rate Limits
  slug: depop-rate-limits
scopes:
- name: Depop Scopes
  scope_count: 7
  slug: depop-scopes
  summary_line: 7 scopes · authorizationCode
score:
  band: developing
  composite: 54.4
  delta: 0.0
  facets:
    commercial_clarity: 21.1
    contract_quality: 68.7
    developer_ergonomics: 73.9
    discoverability: 100.0
    governance: 0.0
    operational_transparency: 63.2
  previous_composite: 54.4
  schema_version: 0.5
  scored_at: '2026-07-23'
  trend: flat
security:
- kind: authentication
  name: Depop Authentication
  slug: depop-authentication
  summary_line: http/oauth2 · 2 schemes
- kind: domain-security
  name: Depop Domain Security
  slug: depop-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: vulnerability-disclosure
  name: Depop Vulnerability Disclosure
  slug: depop-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: depop
tags:
- Company
- Fashion
- Marketplace
- E-commerce
- Resale
- Retail
- Inventory Management
- Orders
- Sustainability
website: https://www.depop.com/
---
