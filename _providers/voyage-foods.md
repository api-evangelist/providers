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
  band: agent-native
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: true
    agentic_commerce: platform
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: false
    idempotency: documented
    mcp_server: verified
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 39.2
  scored_at: '2026-09-04'
agentic_access:
- acting_count: 8
  human_in_the_loop: 1
  name: Voyage Foods Agentic Access
  operation_count: 13
  slug: voyage-foods-agentic-access
  summary_line: 13 operations · 8 acting · 1 human-in-the-loop
api_count: 3
apis:
- description: The Voyage Foods storefront implements the Universal Commerce Protocol (UCP) for agent-driven commerce over MCP. A JSON-RPC 2.0 endpoint at /api/ucp/mcp answers tools/list anonymously with thirteen to
  name: Voyage Foods UCP Commerce MCP API
  slug: voyage-foods-ucp-commerce-mcp
- description: The Shopify Storefront GraphQL API as deployed on the voyagefoods.com host at /api/2026-04/graphql.json. Anonymous introspection is open and returns a 416-type schema with 35 QueryRoot fields (product
  name: Voyage Foods Storefront GraphQL API
  slug: voyage-foods-storefront-graphql
- description: The read-only, unauthenticated product and collection JSON endpoints the store documents for agents in agents.md — /products.json, /products/{handle}.json, /collections/{handle}/products.json and /sea
  name: Voyage Foods Storefront Product JSON API
  slug: voyage-foods-storefront-json
artifact_total: 8
common:
- group: company
  title: ''
  type: Website
  url: https://voyagefoods.com/
- group: other
  title: ''
  type: SecondaryMarket
  url: https://forgeglobal.com/voyage-foods_stock/
- group: docs
  title: ''
  type: Documentation
  url: https://voyagefoods.com/agents.md
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/voyage-foods-llms.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/voyage-foods-well-known.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/voyage-foods-mcp.yml
- group: build
  title: ''
  type: ToolCrosswalk
  url: mcp/voyage-foods-tool-crosswalk.yml
- group: docs
  title: ''
  type: GraphQL
  url: graphql/voyage-foods-storefront.graphql
- group: auth
  title: ''
  type: Authentication
  url: authentication/voyage-foods-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/voyage-foods-scopes.yml
- group: other
  title: ''
  type: OpenIDConnect
  url: well-known/voyage-foods-openid-configuration.json
- group: design
  title: ''
  type: Conventions
  url: conventions/voyage-foods-conventions.yml
- group: design
  title: ''
  type: Idempotency
  url: conventions/voyage-foods-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/voyage-foods-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/voyage-foods-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/voyage-foods-conformance.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/voyage-foods-domain-security.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/voyage-foods-agentic-access.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/voyage-foods-data-model.yml
- group: company
  title: ''
  type: Blog
  url: https://voyagefoods.com/blogs/partnerwithus
- group: operate
  title: ''
  type: Support
  url: https://voyagefoods.com/pages/contact
- group: commercial
  title: ''
  type: Pricing
  url: https://voyagefoods.com/collections/samples
- group: start
  title: ''
  type: SignUp
  url: https://voyagefoods.com/account/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://voyagefoods.com/pages/terms-and-conditions
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://voyagefoods.com/pages/privacy-policy
created: '2026-08-05'
description: 'Voyage Foods is an Oakland, California food-technology company that reengineers supply-chain-constrained foods from widely available inputs — cocoa-free chocolate, bean-free coffee, and peanut-free and hazelnut-free spreads built from seeds, grape seed and grains — sold direct to consumers and to CPG manufacturers as bulk ingredient. Its public API surface is its commerce surface: the voyagefoods.com storefront publishes a Universal Commerce Protocol (UCP) merchant profile at /.well-known/ucp, a live agent-facing MCP endpoint at /api/ucp/mcp exposing thirteen catalog, cart, checkout and order tools, an anonymously introspectable Shopify Storefront GraphQL API, read-only product and collection JSON endpoints, and an agents.md / llms.txt pair stating the store''s agent access policy.'
image: https://voyagefoods.com/cdn/shop/files/ComboTabletop_0035_1_5.jpg?v=1697240864
layout: provider
mcp_servers:
- description: ''
  name: Voyage Foods MCP Server
  slug: voyage-foods-mcp-server
modified: '2026-08-05'
name: Voyage Foods
nav: Providers
network: true
overview: 'Voyage Foods publishes 3 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Food and Beverage, Consumer Packaged Goods, E-Commerce, and Agentic Commerce.


  Voyage Foods'' developer surface includes documentation, authentication, engineering blog, support, pricing, signup flow, and 20 more developer resources.'
random_paper: 17
scopes:
- name: Voyage Foods Scopes
  scope_count: 4
  slug: voyage-foods-scopes
  summary_line: 4 scopes · authorizationCode/refreshToken/urn:ietf:params:oauth:grant-type:jwt-bearer
score:
  band: thin
  composite: 34.1
  coverage:
    artifact_dirs: 15
    catalog_earned: 40.0
    catalog_earned_first_party: 0.0
    catalog_gap: 75.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 44.7
    commercial_clarity: 44.7
    contract_governance: 4.5
    contract_quality: 41.5
    developer_ergonomics: 30.4
    discoverability: 81.5
    governance: 4.5
    operational_transparency: 0.0
  previous_composite: 34.1
  provenance:
    agentic_access: first-party
    conformance: derived
    mcp: first-party
    skills: derived
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/voyage-foods/refs/heads/main/screenshots/voyage-foods-2026-09-02T170301.png
security:
- kind: authentication
  name: Voyage Foods Authentication
  slug: voyage-foods-authentication
  summary_line: openIdConnect/oauth2/http/none/agent-profile · 6 schemes
- kind: domain-security
  name: Voyage Foods Domain Security
  slug: voyage-foods-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: voyage-foods
tags:
- Company
- Food and Beverage
- Consumer Packaged Goods
- E-Commerce
- Agentic Commerce
- Universal Commerce Protocol
- MCP
- GraphQL
- Shopify
- Food Technology
website: https://voyagefoods.com/
---
