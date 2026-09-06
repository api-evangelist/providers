---
access_model:
  confidence: medium
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - authentication
  - scopes
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: true
    agentic_commerce: platform
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: verified
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 44.2
  scored_at: '2026-09-05'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Black Buffalo Agentic Access
  operation_count: 0
  slug: black-buffalo-agentic-access
  summary_line: 0 operations
api_count: 3
apis:
- description: The Shopify Storefront GraphQL API as served from Black Buffalo's own domain. Introspection is anonymous — the full schema (424 types, 35 query fields, 41 mutations, 28 Relay connections) was retrieve
  name: Black Buffalo Storefront GraphQL API
  slug: storefront-graphql
- description: A live Model Context Protocol server on Black Buffalo's storefront host. An anonymous JSON-RPC tools/list returned five tools with full JSON Schema input contracts — search_catalog, get_product_detail
  name: Black Buffalo Storefront MCP Server
  slug: storefront-mcp
- description: Black Buffalo implements the Universal Commerce Protocol for agent-driven commerce. The merchant profile at /.well-known/ucp declares UCP 2026-04-08 and 2026-01-23, the dev.ucp.shopping MCP service en
  name: Black Buffalo UCP Agentic Commerce API
  slug: ucp-commerce
artifact_total: 8
common:
- group: company
  title: ''
  type: Website
  url: https://blackbuffalo.com/
- group: docs
  title: ''
  type: Documentation
  url: https://blackbuffalo.com/agents.md
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/black-buffalo-llms.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/black-buffalo-well-known.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/black-buffalo-mcp.yml
- group: build
  title: ''
  type: ToolCrosswalk
  url: mcp/black-buffalo-tool-crosswalk.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/black-buffalo-agentic-access.yml
- group: docs
  title: ''
  type: GraphQL
  url: graphql/black-buffalo-storefront.graphql
- group: design
  title: ''
  type: DataModel
  url: data-model/black-buffalo-data-model.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/black-buffalo-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/black-buffalo-scopes.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/black-buffalo-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/black-buffalo-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/black-buffalo-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/black-buffalo-conformance.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/black-buffalo-domain-security.yml
- group: operate
  title: ''
  type: FAQ
  url: https://blackbuffalo.com/pages/faq
- group: company
  title: ''
  type: Blog
  url: https://blackbuffalo.com/blogs/stories
- group: company
  title: ''
  type: About
  url: https://blackbuffalo.com/pages/our-story
- group: operate
  title: ''
  type: ContactUs
  url: https://blackbuffalo.com/pages/contact
- group: operate
  title: ''
  type: Support
  url: https://blackbuffalo.com/pages/contact
- group: other
  title: ''
  type: StoreLocator
  url: https://blackbuffalo.com/a/locator/
- group: start
  title: ''
  type: SignUp
  url: https://blackbuffalo.com/account/register
- group: start
  title: ''
  type: Login
  url: https://blackbuffalo.com/account/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://blackbuffalo.com/policies/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://blackbuffalo.com/policies/privacy-policy
- group: other
  title: ''
  type: RefundPolicy
  url: https://blackbuffalo.com/policies/refund-policy
- group: other
  title: ''
  type: ShippingPolicy
  url: https://blackbuffalo.com/policies/shipping-policy
- group: other
  title: ''
  type: LoyaltyProgram
  url: https://blackbuffalo.com/pages/rewards
- group: other
  title: ''
  type: SecondaryMarket
  url: https://equityzen.com/company/blackbuffalo/
created: '2026-08-07'
description: 'Black Buffalo Inc. is an American smokeless tobacco alternative company founded in 2015 and headquartered in Chicago, Illinois, selling nicotine pouches, long cut dip and its nicotine-free ZERO line direct to adult consumers at blackbuffalo.com and through convenience and fuel retailers. Imperial Brands'' U.S. subsidiary ITG Brands acquired the company in May 2026. Black Buffalo runs no developer program and publishes no OpenAPI, but its Shopify-hosted storefront exposes a substantial machine-readable surface from its own domain: an anonymously introspectable Storefront GraphQL API, TWO live Model Context Protocol servers whose tools/list both answer anonymously, a Universal Commerce Protocol merchant profile at /.well-known/ucp, OpenID Connect and RFC 8414 discovery for customer accounts, and a provider-authored /agents.md and /llms.txt that tell AI agents which surface to use, what claims they may not make about a regulated nicotine product, and that no agent may finalize
  payment without contemporaneous human approval.'
image: https://cdn.shopify.com/s/files/1/2258/8521/files/Black-Buffalo-Social-Sharing-Image.jpg?v=1738521407
layout: provider
mcp_servers:
- description: 'Black Buffalo serves TWO live MCP endpoints from its own storefront host, and — unlike most Shopify merchants profiled in this catalog — BOTH answer an anonymous JSON-RPC tools/list with HTTP 200 and '
  name: Black Buffalo MCP Server
  slug: black-buffalo-mcp-server
modified: '2026-08-07'
name: Black Buffalo
nav: Providers
network: true
overview: 'Black Buffalo publishes 3 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Consumer Packaged Goods, Nicotine Pouches, Smokeless Tobacco Alternative, and E-Commerce.


  Black Buffalo''s developer surface includes documentation, authentication, FAQ, engineering blog, support, signup flow, and 25 more developer resources.'
random_paper: 8
scopes:
- name: Black Buffalo Scopes
  scope_count: 4
  slug: black-buffalo-scopes
  summary_line: 4 scopes · authorizationCode
score:
  band: thin
  composite: 32.6
  coverage:
    artifact_dirs: 16
    catalog_earned: 40.0
    catalog_earned_first_party: 0.0
    catalog_gap: 75.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 34.2
    commercial_clarity: 34.2
    contract_governance: 18.2
    contract_quality: 37.2
    developer_ergonomics: 30.4
    discoverability: 81.5
    governance: 18.2
    operational_transparency: 0.0
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - north-america
  previous_composite: 32.6
  provenance:
    agentic_access: first-party
    conformance: first-party
    mcp: first-party
    skills: derived
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/black-buffalo/refs/heads/main/screenshots/black-buffalo-2026-08-07T162610.png
security:
- kind: authentication
  name: Black Buffalo Authentication
  slug: black-buffalo-authentication
  summary_line: none/openIdConnect/oauth2/agentProfile · 7 schemes
- kind: domain-security
  name: Black Buffalo Domain Security
  slug: black-buffalo-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: black-buffalo
tags:
- Company
- Consumer Packaged Goods
- Nicotine Pouches
- Smokeless Tobacco Alternative
- E-Commerce
- Direct to Consumer
- Retail
- Agentic Commerce
- Shopify
- GraphQL
- MCP
- Universal Commerce Protocol
website: https://blackbuffalo.com/
---
