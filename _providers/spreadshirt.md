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
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: true
    idempotency: false
    mcp_server: false
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 33.2
  scored_at: '2026-09-01'
api_count: 1
apis:
- description: Spreadshirt Public Shop API — REST API for building custom e-commerce storefronts against the Spreadshirt EU (spreadshirt.net) and North American (spreadshirt.com) marketplaces, using SprdAuth API-key
  name: Spreadshirt Public Shop API
  slug: spreadshirt-public-shop-api
- description: The Articles API from Spreadshirt — 2 operation(s) for articles.
  name: Spreadshirt Articles API
  slug: spreadshirt-articles-api
- description: The Spreadconnect API allows you to connect to the Spreadconnect system and lets you manage your products, submit orders and get them fulfilled via requests. To make sure that the requests send to the
  name: Spreadshirt Authentication API
  slug: spreadshirt-authentication-api
- description: The Designs API from Spreadshirt — 1 operation(s) for designs.
  name: Spreadshirt Designs API
  slug: spreadshirt-designs-api
- description: There are different ways to place an order in Spreadconnect REST API. You can choose a simple way, where you have to send just one request or you can use a more complex way, with more control over the
  name: Spreadshirt Orders API
  slug: spreadshirt-orders-api
- description: Product types represent our available base products that can be used for customisation. This information can also be found in the User Interface of the Spreadconnect application when creating a produc
  name: Spreadshirt Product Types API
  slug: spreadshirt-product-types-api
- description: Get the available stock on the variants of the created articles.
  name: Spreadshirt Stocks API
  slug: spreadshirt-stocks-api
- description: 'This api offers you webhook subscriptions that will notify you about changes with your order via a POST request. ### Acknowledge notifications Notifications are following the at *least once principal*'
  name: Spreadshirt Subscriptions API
  slug: spreadshirt-subscriptions-api
artifact_total: 22
asyncapis:
- description: ''
  name: Spreadshirt Webhooks
  slug: spreadshirt-webhooks
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Spreadconnect fulfillment service REST Articles API
  slug: open-spreadshirt-articles-api
- collection_type: open
  name: Spreadconnect fulfillment service REST Articles Authentication API
  slug: open-spreadshirt-authentication-api
- collection_type: open
  name: Spreadconnect fulfillment service REST Articles Designs API
  slug: open-spreadshirt-designs-api
- collection_type: open
  name: Spreadconnect fulfillment service REST Articles Orders API
  slug: open-spreadshirt-orders-api
- collection_type: open
  name: Spreadconnect fulfillment service REST Articles Product Types API
  slug: open-spreadshirt-product-types-api
- collection_type: open
  name: Spreadconnect fulfillment service REST Articles Stocks API
  slug: open-spreadshirt-stocks-api
- collection_type: open
  name: Spreadconnect fulfillment service REST Articles Subscriptions API
  slug: open-spreadshirt-subscriptions-api
common:
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/spreadshirt-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/spreadshirt-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/spreadshirt-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://www.spreadshirt.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://www.spreadshop.com/spreadconnect
- group: docs
  title: ''
  type: Documentation
  url: https://api.spreadconnect.app/docs/
- group: docs
  title: ''
  type: APIReference
  url: https://api.spreadconnect.app/docs/
- group: start
  title: ''
  type: GettingStarted
  url: https://faq.spod.com/hc/en-us/articles/360020927339-How-do-I-get-started-with-the-API
- group: operate
  title: ''
  type: Support
  url: https://faq.spod.com/hc/en-us
- group: start
  title: ''
  type: SignUp
  url: https://login.spreadconnect.app
- group: start
  title: ''
  type: Login
  url: https://login.spreadconnect.app
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/spreadshirt
- group: auth
  title: ''
  type: Security
  url: well-known/spreadshirt-security.txt
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/spreadshirt-security.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/spreadshirt-well-known.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/spreadshirt-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/spreadshirt-lifecycle.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/spreadshirt-conventions.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/spreadshirt-rate-limits.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/spreadshirt-webhooks.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/spreadshirt-sandbox.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/spreadshirt-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/spreadshirt-llms.txt
- group: other
  title: ''
  type: Overlay
  url: overlays/spreadshirt-spreadconnect-overlay.yaml
- group: design
  title: ''
  type: Conformance
  url: conformance/spreadshirt-conformance.yml
- group: build
  title: ''
  type: Packages
  url: packages/spreadshirt-packages.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/spreadshirt-data-model.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-07-17'
description: 'Spreadshirt (Spread Group) is a European print-on-demand and custom apparel platform that lets individuals and businesses design, sell, and order personalized T-shirts, hoodies, accessories, and merchandise. It exposes two developer surfaces: the SpreadConnect (SPOD) fulfillment REST API, which connects any shop system to on-demand production and drop-shipping (articles, orders, product types, stock, designs, and webhook subscriptions), and the older Spreadshirt Public Shop API for building custom storefronts against the EU and North American marketplaces. Added to the API Evangelist network as a consumer / print-on-demand provider and enriched by the pipeline.'
image: https://www.spreadshirt.com/apple-touch-icon.png
layout: provider
mcp_servers:
- description: ''
  name: Spreadshirt MCP Server
  slug: spreadshirt-mcp-server
modified: '2026-07-21'
name: Spreadshirt
nav: Providers
network: true
overview: 'Spreadshirt publishes 7 APIs on the [APIs.io](https://apis.io/) network, including Articles API, Authentication API, Designs API, and 4 more. Tagged areas include Company, Consumer, Print on Demand, E-Commerce, and Apparel.


  The Spreadshirt catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Spreadshirt''s developer surface includes authentication, documentation, API reference, getting-started guide, support, signup flow, sandbox, and 21 more developer resources.'
random_paper: 17
rate_limits:
- limit_count: 1
  name: Spreadshirt Rate Limits
  slug: spreadshirt-rate-limits
score:
  band: developing
  composite: 42.0
  coverage:
    artifact_dirs: 22
    catalog_gap: 70.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 4.5
    contract_quality: 62.7
    developer_ergonomics: 63.7
    discoverability: 75.9
    governance: 4.5
    operational_transparency: 42.1
  previous_composite: 42.0
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 7
    mcp: derived
    skills: derived
  schema_version: 0.17.2
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/spreadshirt/refs/heads/main/screenshots/spreadshirt-2026-08-17T082038.png
security:
- kind: authentication
  name: Spreadshirt Authentication
  slug: spreadshirt-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Spreadshirt Domain Security
  slug: spreadshirt-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC
- kind: vulnerability-disclosure
  name: Spreadshirt Vulnerability Disclosure
  slug: spreadshirt-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: spreadshirt
tags:
- Company
- Consumer
- Print on Demand
- E-Commerce
- Apparel
- Custom Merchandise
- Fulfillment
- Dropshipping
- Webhook
website: https://www.spreadshirt.com/
---
