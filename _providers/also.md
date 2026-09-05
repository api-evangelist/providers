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
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 50.8
  scored_at: '2026-09-04'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Also Agentic Access
  operation_count: 6
  slug: also-agentic-access
  summary_line: 6 operations
api_count: 1
apis:
- description: 'The Shopify Storefront GraphQL API served on ALSO''s own domain. Open, unauthenticated introspection was confirmed; 35 root queries (products, collections, cart, search, blogs, shop, localization) and '
  name: ALSO Storefront GraphQL API
  slug: also-storefront-graphql-api
- description: ALSO's Universal Commerce Protocol (UCP) endpoint, advertised in its own /.well-known/ucp discovery profile and /agents.md. Exposes the dev.ucp.shopping service over MCP transport for agent-driven cat
  name: ALSO UCP Commerce MCP API
  slug: also-ucp-commerce-mcp-api
- baseURL: https://ridealso.com/api/2026-07/graphql.json
  baseurl_source: declared
  description: The current session cart.
  name: Also Cart API
  slug: also-cart-api
- baseURL: https://ridealso.com/api/2026-07/graphql.json
  baseurl_source: declared
  description: Collection listings and the products within a collection.
  name: Also Collections API
  slug: also-collections-api
- baseURL: https://ridealso.com/api/2026-07/graphql.json
  baseurl_source: declared
  description: Product catalog listings and per-product detail.
  name: Also Products API
  slug: also-products-api
- baseURL: https://ridealso.com/api/2026-07/graphql.json
  baseurl_source: declared
  description: Storefront search.
  name: Also Search API
  slug: also-search-api
artifact_total: 17
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: ALSO Storefront JSON Cart API
  slug: open-also-cart-api
- collection_type: open
  name: ALSO Storefront JSON Collections API
  slug: open-also-collections-api
- collection_type: open
  name: ALSO Storefront JSON Products API
  slug: open-also-products-api
- collection_type: open
  name: ALSO Storefront JSON Search API
  slug: open-also-search-api
common:
- group: other
  title: ''
  type: Overlay
  url: overlays/also-storefront-json-overlay.yaml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/also-agentic-access.yml
- group: company
  title: ''
  type: Website
  url: https://ridealso.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://ridealso.com/agents.md
- group: docs
  title: ''
  type: Documentation
  url: https://ridealso.com/agents.md
- group: docs
  title: ''
  type: APIReference
  url: https://shopify.dev/docs/api/storefront
- group: start
  title: ''
  type: GettingStarted
  url: https://ridealso.com/agents.md
- group: operate
  title: ''
  type: Support
  url: https://ridealso.com/pages/support
- group: operate
  title: ''
  type: HelpCenter
  url: https://ridealso.com/pages/help-center
- group: company
  title: ''
  type: Blog
  url: https://ridealso.com/blogs/all
- group: company
  title: ''
  type: About
  url: https://ridealso.com/pages/company
- group: company
  title: ''
  type: Careers
  url: https://jobs.ashbyhq.com/Ridealso
- group: commercial
  title: ''
  type: Pricing
  url: https://ridealso.com/products/tm-b
- group: start
  title: ''
  type: SignUp
  url: https://ridealso.com/account/login
- group: start
  title: ''
  type: Login
  url: https://ridealso.com/account/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://ridealso.com/pages/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://ridealso.com/pages/privacy
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/also-llms.txt
- group: other
  title: ''
  type: AgentsMD
  url: llms/also-agents.md
- group: agent
  title: ''
  type: WellKnown
  url: well-known/also-well-known.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/also-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/also-scopes.yml
- group: other
  title: ''
  type: OpenIDConnect
  url: well-known/also-openid-configuration.json
- group: design
  title: ''
  type: Conventions
  url: conventions/also-conventions.yml
- group: design
  title: ''
  type: Idempotency
  url: conventions/also-conventions.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/also-rate-limits.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/also-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/also-lifecycle.yml
- group: design
  title: ''
  type: Components
  url: components/also-components.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/also-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/ridealso
- group: learn
  title: ''
  type: YouTube
  url: https://www.youtube.com/@ride_also
- group: company
  title: ''
  type: Instagram
  url: https://www.instagram.com/ridealso
- group: other
  title: ''
  type: TikTok
  url: https://www.tiktok.com/@ridealso
- group: other
  title: ''
  type: SecondaryMarket
  url: https://forgeglobal.com/also_stock/
created: '2026-08-02'
description: ALSO (Also, Inc.) is a Palo Alto, California electric micromobility company spun out of Rivian in March 2025, building small electric vehicles for moving people and goods, both driven and autonomous. Its flagship product is the TM-B, a modular Class 3 electric bike with a swappable top frame and the in-house DreamRide software-defined drive system, alongside a delivery quad for logistics fleets and the Alpha Wave helmet. ALSO reached a $1B valuation in 2026 on a $200M round led by Greenoaks and announced an autonomous-delivery partnership with DoorDash. Its public digital surface is a Shopify-hosted commerce platform at ridealso.com that exposes an open Storefront GraphQL API (35 queries / 41 mutations), the Shopify JSON storefront endpoints, and a Universal Commerce Protocol (UCP) MCP endpoint for agent-driven shopping and checkout, all advertised in the company's own published agents.md / llms.txt.
image: https://cdn.shopify.com/s/files/1/0747/5878/3200/files/Social_Share.jpg?v=1760978876
layout: provider
mcp_servers:
- description: ''
  name: Also MCP Server
  slug: also-mcp-server
modified: '2026-08-02'
name: Also
nav: Providers
network: true
overview: 'Also publishes 4 APIs on the [APIs.io](https://apis.io/) network, including Cart API, Collections API, Products API, and 1 more. Tagged areas include Company, Micromobility, Electric Vehicles, Transportation, and E-Commerce.


  Also''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, pricing, signup flow, and 29 more developer resources.'
random_paper: 11
rate_limits:
- limit_count: 0
  name: Also Rate Limits
  slug: also-rate-limits
scopes:
- name: Also Scopes
  scope_count: 5
  slug: also-scopes
  summary_line: 5 scopes · authorizationCode/refreshToken/urn:ietf:params:oauth:grant-type:jwt-bearer
score:
  band: developing
  composite: 42.1
  coverage:
    artifact_dirs: 21
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 44.7
    commercial_clarity: 44.7
    contract_governance: 4.5
    contract_quality: 52.9
    developer_ergonomics: 58.9
    discoverability: 75.9
    governance: 4.5
    operational_transparency: 0.0
  previous_composite: 42.1
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 4
    mcp: first-party
    skills: derived
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/also/refs/heads/main/screenshots/also-2026-08-07T161241.png
security:
- kind: authentication
  name: Also Authentication
  slug: also-authentication
  summary_line: none/oauth2/openIdConnect/apiKey · 4 schemes
- kind: domain-security
  name: Also Domain Security
  slug: also-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: also
tags:
- Company
- Micromobility
- Electric Vehicles
- Transportation
- E-Commerce
- Consumer Hardware
- Agentic Commerce
- Logistics
- Delivery
website: https://ridealso.com/
---
