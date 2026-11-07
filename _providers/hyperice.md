---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
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
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: platform
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: derived
    event_surface_described: false
    idempotency: documented
    mcp_server: platform
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 39.6
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Hyperice Agentic Access
  operation_count: 8
  slug: hyperice-agentic-access
  summary_line: 8 operations
api_count: 1
apis:
- description: The Shopify Storefront GraphQL API served on Hyperice's own domain. Full introspection succeeded unauthenticated on 2026-07-31 — 424 types, 35 QueryRoot fields, 41 Mutation fields — making this the ri
  name: Hyperice Storefront GraphQL API
  slug: hyperice-storefront-graphql-api
- description: A live MCP (JSON-RPC 2.0 over HTTP) server implementing the Universal Commerce Protocol shopping service, declared by Hyperice's own /.well-known/ucp merchant profile and advertised to agents in /llms
  name: Hyperice UCP Shopping MCP Server
  slug: hyperice-ucp-shopping-mcp-server
artifact_total: 12
collections:
- collection_type: open
  name: Hyperice Storefront API
  slug: open-hyperice-storefront
common:
- group: company
  title: ''
  type: BlogRSS
  url: https://hyperice.com/blogs/hyperhub.atom
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
  href: https://artifacts.apis.io/hyperice/llms/hyperice-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/hyperice-llms.txt
- group: other
  href: https://artifacts.apis.io/hyperice/llms/hyperice-agents.md
  title: ''
  type: AgentInstructions
  url: llms/hyperice-agents.md
- group: agent
  href: https://artifacts.apis.io/hyperice/mcp/hyperice-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/hyperice-mcp.yml
- group: build
  href: https://artifacts.apis.io/hyperice/mcp/hyperice-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/hyperice-tool-crosswalk.yml
- group: agent
  href: https://artifacts.apis.io/hyperice/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  href: https://artifacts.apis.io/hyperice/agentic-access/hyperice-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/hyperice-agentic-access.yml
- group: docs
  href: https://artifacts.apis.io/hyperice/graphql/hyperice-storefront.graphql
  title: ''
  type: GraphQL
  url: graphql/hyperice-storefront.graphql
- group: docs
  href: https://artifacts.apis.io/hyperice/openapi/_original/hyperice-storefront-openapi.yml
  title: ''
  type: OpenAPI
  url: openapi/_original/hyperice-storefront-openapi.yml
- group: other
  href: https://artifacts.apis.io/hyperice/overlays/hyperice-storefront-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/hyperice-storefront-overlay.yaml
- group: agent
  href: https://artifacts.apis.io/hyperice/well-known/hyperice-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/hyperice-well-known.yml
- group: auth
  href: https://artifacts.apis.io/hyperice/authentication/hyperice-authentication.yml
  title: ''
  type: Authentication
  url: authentication/hyperice-authentication.yml
- group: auth
  href: https://artifacts.apis.io/hyperice/scopes/hyperice-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/hyperice-scopes.yml
- group: other
  href: https://artifacts.apis.io/hyperice/well-known/hyperice-openid-configuration.json
  title: ''
  type: OpenIDConnect
  url: well-known/hyperice-openid-configuration.json
- group: design
  href: https://artifacts.apis.io/hyperice/conventions/hyperice-conventions.yml
  title: ''
  type: Conventions
  url: conventions/hyperice-conventions.yml
- group: design
  href: https://artifacts.apis.io/hyperice/conventions/hyperice-conventions.yml
  title: ''
  type: Idempotency
  url: conventions/hyperice-conventions.yml
- group: operate
  href: https://artifacts.apis.io/hyperice/rate-limits/hyperice-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/hyperice-rate-limits.yml
- group: design
  href: https://artifacts.apis.io/hyperice/errors/hyperice-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/hyperice-problem-types.yml
- group: design
  href: https://artifacts.apis.io/hyperice/lifecycle/hyperice-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/hyperice-lifecycle.yml
- group: build
  href: https://artifacts.apis.io/hyperice/errors/hyperice-decline-codes.yml
  title: ''
  type: DeclineCodes
  url: errors/hyperice-decline-codes.yml
- group: build
  href: https://artifacts.apis.io/hyperice/packages/hyperice-packages.yml
  title: ''
  type: Packages
  url: packages/hyperice-packages.yml
- group: design
  href: https://artifacts.apis.io/hyperice/conformance/hyperice-conformance.yml
  title: ''
  type: Conformance
  url: conformance/hyperice-conformance.yml
- group: design
  href: https://artifacts.apis.io/hyperice/data-model/hyperice-data-model.yml
  title: ''
  type: DataModel
  url: data-model/hyperice-data-model.yml
- group: auth
  href: https://artifacts.apis.io/hyperice/security/hyperice-domain-security.yml
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
  slug: hyperice-ucp-shopping
modified: '2026-10-06'
name: Hyperice
nav: Providers
network: true
overview: 'Hyperice publishes 2 API contracts indexed on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Commerce, Retail, Health and Wellness, and Consumer Hardware.


  Hyperice''s developer surface includes documentation, API reference, getting-started guide, authentication, support, engineering blog, signup flow, and 33 more developer resources.'
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
  band: thin
  composite: 29.5
  coverage:
    artifact_dirs: 23
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 21.1
    contract_governance: 18.2
    contract_quality: 10.4
    developer_ergonomics: 49.4
    discoverability: 75.0
    operational_transparency: 0.0
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - united-states
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - north-america
  previous_composite: 29.5
  provenance:
    agentic_access: derived
    conformance: first-party
    mcp: platform-generated
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 32.8
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: this provider''s published contracts declare no write operations, and a read-only API cannot create-or-update. Excluded from the denominator, not zeroed.'
    reason: read_only
screenshot: https://apis.io/screenshots/hyperice/hyperice-2026-08-07T170541.png
security:
- kind: authentication
  name: Hyperice Authentication
  slug: hyperice-authentication
  summary_line: none/openIdConnect/oauth2/http · 4 schemes
- kind: domain-security
  name: Hyperice Domain Security
  slug: hyperice-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
skill_count: 3
skills:
- name: Buy a Hyperice product as an agent
  slug: hyperice-agent-commerce-checkout
- name: Browse the Hyperice product catalog
  slug: hyperice-browse-catalog
- name: Build and submit a cart on the Storefront GraphQL API
  slug: hyperice-graphql-cart
slug: hyperice
tags:
- Company
- Commerce
- Retail
- Health and Wellness
- Consumer Hardware
- Agentic Commerce
- GraphQL
- MCP
- Shopify
- Fitness
website: https://hyperice.com/
---
