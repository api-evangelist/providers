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
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: verified
    idempotency: false
    mcp_server: derived
    openapi_examples: partial
    rate_limit_signal: verified
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 48.0
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 10
  human_in_the_loop: 0
  name: Zalando Agentic Access
  operation_count: 41
  slug: zalando-agentic-access
  summary_line: 41 operations · 10 acting
api_count: 20
apis:
- description: The AnnouncedReturns API from Zalando — 1 operation(s) for announcedreturns.
  name: Zalando AnnouncedReturns API
  slug: zalando-announcedreturns-api
- description: The attribute-types API from Zalando — 2 operation(s) for attribute-types.
  name: Zalando attribute-types API
  slug: zalando-attribute-types-api
- description: The attribute-values API from Zalando — 2 operation(s) for attribute-values.
  name: Zalando attribute-values API
  slug: zalando-attribute-values-api
- description: The Attributes API from Zalando — 2 operation(s) for attributes.
  name: Zalando Attributes API
  slug: zalando-attributes-api
- description: The Cross Border Movements API from Zalando — 1 operation(s) for cross border movements.
  name: Zalando Cross Border Movements API
  slug: zalando-cross-border-movements-api
- description: The Discovery API API from Zalando — 1 operation(s) for discovery api.
  name: Zalando Discovery API API
  slug: zalando-discovery-api-api
- description: The History of Price Update Attempts API from Zalando — 1 operation(s) for history of price update attempts.
  name: Zalando History of Price Update Attempts API
  slug: zalando-history-of-price-update-attempts-api
- description: The Liquidated Items API from Zalando — 1 operation(s) for liquidated items.
  name: Zalando Liquidated Items API
  slug: zalando-liquidated-items-api
- description: The Logistic Centers API from Zalando — 2 operation(s) for logistic centers.
  name: Zalando Logistic Centers API
  slug: zalando-logistic-centers-api
- description: The offer-blockers API from Zalando — 2 operation(s) for offer-blockers.
  name: Zalando offer-blockers API
  slug: zalando-offer-blockers-api
- description: The Orders API from Zalando — 11 operation(s) for orders.
  name: Zalando Orders API
  slug: zalando-orders-api
- description: The Outlines API from Zalando — 2 operation(s) for outlines.
  name: Zalando Outlines API
  slug: zalando-outlines-api
- description: The prices API from Zalando — 1 operation(s) for prices.
  name: Zalando prices API
  slug: zalando-prices-api
- description: The Product Association API from Zalando — 1 operation(s) for product association.
  name: Zalando Product Association API
  slug: zalando-product-association-api
- description: The Reports API from Zalando — 1 operation(s) for reports.
  name: Zalando Reports API
  slug: zalando-reports-api
- description: The Returned Items API from Zalando — 1 operation(s) for returned items.
  name: Zalando Returned Items API
  slug: zalando-returned-items-api
- description: The SalesChannels API from Zalando — 1 operation(s) for saleschannels.
  name: Zalando SalesChannels API
  slug: zalando-saleschannels-api
- description: The Shipments API from Zalando — 2 operation(s) for shipments.
  name: Zalando Shipments API
  slug: zalando-shipments-api
- description: The stocks API from Zalando — 1 operation(s) for stocks.
  name: Zalando stocks API
  slug: zalando-stocks-api
- description: The Types API from Zalando — 1 operation(s) for types.
  name: Zalando Types API
  slug: zalando-types-api
artifact_total: 25
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/zalando-domain-security.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/zalando-agentic-access.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/zalando-scopes.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/zalando-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://corporate.zalando.com/en
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developers.merchants.zalando.com/
- group: docs
  title: ''
  type: Documentation
  url: https://developers.merchants.zalando.com/docs/index.html
- group: docs
  title: ''
  type: APIReference
  url: https://developers.merchants.zalando.com/docs/api-overview.html
- group: start
  title: ''
  type: GettingStarted
  url: https://developers.merchants.zalando.com/docs/quick-start-guide.html
- group: auth
  title: ''
  type: Authentication
  url: https://developers.merchants.zalando.com/docs/auth.html
- group: operate
  title: ''
  type: ChangeLog
  url: https://developers.merchants.zalando.com/docs/release-notes.html
- group: operate
  title: ''
  type: RateLimits
  url: https://developers.merchants.zalando.com/docs/rate-limiting.html
- group: start
  title: ''
  type: SignUp
  url: https://partnerportal.zalando.com/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/zalando
- group: company
  title: ''
  type: Blog
  url: https://engineering.zalando.com/
- group: docs
  title: ''
  type: Guidelines
  url: https://opensource.zalando.com/restful-api-guidelines/
- group: agent
  title: ''
  type: MCPServer
  url: mcp/zalando-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/zalando-llms.txt
- group: design
  title: ''
  type: Conventions
  url: conventions/zalando-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/zalando-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/zalando-lifecycle.yml
- group: operate
  title: ''
  type: Deprecation
  url: https://developers.merchants.zalando.com/docs/versioning-and-deprecation-policy.html
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/zalando-changelog.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/zalando-sandbox.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/zalando-data-model.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/zalando-conformance.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/zalando-onboard-and-price-article.md
- group: agent
  title: ''
  type: AgentSkill
  url: skills/zalando-retrieve-and-fulfill-orders.md
created: '2026-07-17'
description: 'Zalando is Europe''s leading online platform for fashion and lifestyle, connecting customers, brands and partners across more than 20 markets. Its zDirect Platform (formerly the Zalando Partner / Merchant Platform) exposes a suite of REST APIs that let merchants and integration partners manage the full article lifecycle: onboarding and enriching products, submitting attributes, controlling prices and stock, blocking or unblocking offers, managing sales channels and logistic centers, retrieving orders, and operating Zalando Fulfillment Solutions (ZFS) stock movements and cross-border reporting. All APIs are OAuth 2.0 client-credentials protected, follow the widely referenced Zalando RESTful API and Event Guidelines, use JSON (with JSON:API media types on several services), and offer a full sandbox environment. Zalando was surfaced as an HV Capital portfolio company and enriched into the API Evangelist network from its public developer surface.'
image: https://avatars.githubusercontent.com/u/1564818?s=200&v=4
layout: provider
mcp_servers:
- description: Candidate MCP tool list derived from zDirect OpenAPI operations; no official server published.
  name: zDirect candidate MCP (derived)
  slug: zdirect-candidate-mcp-derived
modified: '2026-07-21'
name: Zalando
nav: Providers
network: true
overview: 'Zalando publishes 20 APIs on the [APIs.io](https://apis.io/) network, including AnnouncedReturns API, attribute-types API, attribute-values API, and 17 more. Tagged areas include Company, Consumer; Marketplace, Fashion, E-Commerce, and Retail.


  Zalando''s developer surface includes authentication, documentation, API reference, getting-started guide, changelog, signup flow, engineering blog, and 21 more developer resources.'
random_paper: 34
scopes:
- name: Zalando Scopes
  scope_count: 16
  slug: zalando-scopes
  summary_line: 16 scopes · clientCredentials
score:
  band: thin
  composite: 37.9
  delta: -2.6
  facets:
    commercial_clarity: 13.2
    contract_quality: 39.2
    developer_ergonomics: 58.2
    discoverability: 87.0
    governance: 11.5
    operational_transparency: 28.9
  previous_composite: 40.5
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 20
    mcp: derived
    skills: derived
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
security:
- kind: authentication
  name: Zalando Authentication
  slug: zalando-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Zalando Domain Security
  slug: zalando-domain-security
  summary_line: TLSv1.3 · DMARC
slug: zalando
tags:
- Company
- Consumer; Marketplace
- Fashion
- E-Commerce
- Retail
- Marketplace
- Fulfillment
- Merchant Platform
- Orders
- Products
website: https://corporate.zalando.com/en
---
