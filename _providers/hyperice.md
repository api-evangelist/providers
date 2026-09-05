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
  - rate-limits
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-native
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: platform
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: na
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: false
    idempotency: na
    mcp_server: verified
    openapi_examples: partial
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 55.0
  scored_at: '2026-09-04'
agentic_access:
- acting_count: 13
  human_in_the_loop: 0
  name: Hyperice Agentic Access
  operation_count: 21
  slug: hyperice-agentic-access
  summary_line: 21 operations · 13 acting
api_count: 1
apis:
- description: The Shopify Storefront GraphQL API served on Hyperice's own domain. Full introspection succeeded unauthenticated on 2026-07-31 — 424 types, 35 QueryRoot fields, 41 Mutation fields — making this the ri
  name: Hyperice Storefront GraphQL API
  slug: hyperice-storefront-graphql-api
- description: A live MCP (JSON-RPC 2.0 over HTTP) server implementing the Universal Commerce Protocol shopping service, declared by Hyperice's own /.well-known/ucp merchant profile and advertised to agents in /llms
  name: Hyperice UCP Shopping MCP Server
  slug: hyperice-ucp-shopping-mcp-server
- baseURL: https://hyperice.com/api/2026-04/graphql.json
  baseurl_source: declared
  description: Collection (category) read operations.
  name: Hyperice Collections API
  slug: hyperice-collections-api
- baseURL: https://hyperice.com/api/2026-04/graphql.json
  baseurl_source: declared
  description: Agent- and crawler-facing discovery documents.
  name: Hyperice Discovery API
  slug: hyperice-discovery-api
- baseURL: https://hyperice.com/api/2026-04/graphql.json
  baseurl_source: declared
  description: Product catalog read operations.
  name: Hyperice Products API
  slug: hyperice-products-api
artifact_total: 12
collections:
- collection_type: open
  name: Hyperice Storefront API
  slug: open-hyperice-storefront
common:
- group: company
  title: ''
  type: Website
  url: https://hyperice.com/
- group: other
  title: ''
  type: SecondaryMarket
  url: https://forgeglobal.com/hyperice_stock/
- group: docs
  title: ''
  type: Documentation
  url: https://hyperice.com/agents.md
- group: docs
  title: ''
  type: APIReference
  url: https://ucp.dev/2026-04-08/specification/overview/
- group: start
  title: ''
  type: GettingStarted
  url: https://hyperice.com/llms.txt
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/hyperice-llms.txt
- group: other
  title: ''
  type: AgentInstructions
  url: llms/hyperice-agents.md
- group: agent
  title: ''
  type: MCPServer
  url: mcp/hyperice-mcp.yml
- group: build
  title: ''
  type: ToolCrosswalk
  url: mcp/hyperice-tool-crosswalk.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/hyperice-agentic-access.yml
- group: docs
  title: ''
  type: GraphQL
  url: graphql/hyperice-storefront.graphql
- group: docs
  title: ''
  type: OpenAPI
  url: openapi/hyperice-storefront-openapi.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/hyperice-storefront-overlay.yaml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/hyperice-well-known.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/hyperice-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/hyperice-scopes.yml
- group: other
  title: ''
  type: OpenIDConnect
  url: well-known/hyperice-openid-configuration.json
- group: design
  title: ''
  type: Conventions
  url: conventions/hyperice-conventions.yml
- group: design
  title: ''
  type: Idempotency
  url: conventions/hyperice-conventions.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/hyperice-rate-limits.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/hyperice-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/hyperice-lifecycle.yml
- group: build
  title: ''
  type: DeclineCodes
  url: errors/hyperice-decline-codes.yml
- group: build
  title: ''
  type: Packages
  url: packages/hyperice-packages.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/hyperice-conformance.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/hyperice-data-model.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/hyperice-domain-security.yml
- group: operate
  title: ''
  type: Support
  url: https://hyperice.com/pages/contact
- group: operate
  title: ''
  type: HelpCenter
  url: https://hyperice.zendesk.com/hc/en-us
- group: company
  title: ''
  type: Blog
  url: https://hyperice.com/blogs/hyperhub
- group: start
  title: ''
  type: SignUp
  url: https://accounts.hyperice.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://hyperice.com/policies/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://hyperice.com/policies/privacy-policy
- group: other
  title: ''
  type: RefundPolicy
  url: https://hyperice.com/policies/refund-policy
- group: other
  title: ''
  type: ShippingPolicy
  url: https://hyperice.com/policies/shipping-policy
- group: other
  title: ''
  type: Accessibility
  url: https://hyperice.com/pages/accessibility
- group: other
  title: ''
  type: Patents
  url: https://hyperice.com/pages/patents
- group: company
  title: ''
  type: About
  url: https://hyperice.com/pages/about-us
created: '2026-07-31'
description: 'Hyperice is a recovery and movement-enhancement technology company founded in 2010 and headquartered in Irvine, California, known for the Hypervolt percussion massage line, the Normatec dynamic air-compression systems it acquired in 2020, and the Venom thermal/vibration wearables. Its API surface is not a developer platform but an agentic-commerce storefront: hyperice.com runs on Shopify and publishes a machine-readable agent contract at /llms.txt and /agents.md, a Universal Commerce Protocol (UCP) merchant profile at /.well-known/ucp, a live MCP shopping server at /api/ucp/mcp, a fully introspectable Shopify Storefront GraphQL API, OIDC/OAuth2 customer accounts at accounts.hyperice.com, and an unauthenticated read-only product and collection JSON surface.'
image: https://hyperice.com/cdn/shop/files/hyperice-social-share.jpg?v=1775020762&width=1200
layout: provider
mcp_servers:
- description: Hyperice runs a live, publicly addressable MCP server as the transport for the Universal Commerce Protocol (UCP) shopping service on its Shopify storefront. The server is declared by Hyperice's own UC
  name: Hyperice MCP Server
  slug: hyperice-mcp-server
modified: '2026-07-31'
name: Hyperice
nav: Providers
network: true
overview: 'Hyperice publishes 3 APIs on the [APIs.io](https://apis.io/) network: Collections API, Discovery API, and Products API. Tagged areas include Company, Commerce, Retail, Health and Wellness, and Consumer Hardware.


  Hyperice''s developer surface includes documentation, API reference, getting-started guide, authentication, support, engineering blog, signup flow, and 32 more developer resources.'
random_paper: 17
rate_limits:
- limit_count: 0
  name: Hyperice Rate Limits
  slug: hyperice-rate-limits
scopes:
- name: Hyperice Scopes
  scope_count: 4
  slug: hyperice-scopes
  summary_line: 4 scopes · authorizationCode
score:
  band: developing
  composite: 43.8
  coverage:
    artifact_dirs: 21
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 21.1
    commercial_clarity: 21.1
    contract_governance: 18.2
    contract_quality: 55.6
    developer_ergonomics: 49.4
    discoverability: 75.9
    governance: 18.2
    operational_transparency: 0.0
  previous_composite: 43.8
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 3
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 58.8
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/hyperice/refs/heads/main/screenshots/hyperice-2026-08-07T170541.png
security:
- kind: authentication
  name: Hyperice Authentication
  slug: hyperice-authentication
  summary_line: none/openIdConnect/oauth2/http · 4 schemes
- kind: domain-security
  name: Hyperice Domain Security
  slug: hyperice-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: hyperice
tags:
- Company
- Commerce
- Retail
- Health and Wellness
- Consumer Hardware
- Sports And Fitness
- Agentic Commerce
- GraphQL
- MCP
- Shopify
website: https://hyperice.com/
---
