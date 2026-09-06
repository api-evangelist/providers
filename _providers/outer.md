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
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: true
    agentic_access: false
    agentic_commerce: platform
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: verified
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 23.9
  scored_at: '2026-09-05'
api_count: 1
apis:
- description: The Universal Commerce Protocol shopping service Outer's storefront exposes over MCP, advertised in the merchant profile at https://liveouter.com/.well-known/ucp. It carries the dev.ucp.shopping servi
  name: Outer UCP Shopping (MCP)
  slug: ucp-shopping
artifact_total: 5
common:
- group: company
  title: ''
  type: Website
  url: https://liveouter.com/
- group: other
  title: ''
  type: SecondaryMarket
  url: https://forgeglobal.com/outer_stock/
- group: company
  title: ''
  type: Blog
  url: https://liveouter.com/blogs/outdoor-furniture
- group: operate
  title: ''
  type: Support
  url: https://liveouter.com/pages/helpful-faqs
- group: start
  title: ''
  type: SignUp
  url: https://liveouter.com/account/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://liveouter.com/policies/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://liveouter.com/policies/privacy-policy
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/outer-llms.txt
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/outer-mcp.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/outer-well-known.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/outer-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/outer-scopes.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/outer-conventions.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/outer-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/outer-lifecycle.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/outer-domain-security.yml
created: '2026-08-04'
description: 'Outer is a direct-to-consumer outdoor furniture brand founded in 2017 by Jiake Liu and Terry Lin and headquartered in Santa Monica, California, known for its OuterShell built-in cushion cover, OuterWeave wicker and OuterCloud cushions, and for the Neighborhood Showroom program that turns customer backyards into showrooms. Outer publishes no traditional developer program and no OpenAPI, but its Shopify-hosted storefront at liveouter.com serves a real machine-readable agent surface: an /llms.txt and /agents.md agent instruction document, a Universal Commerce Protocol (UCP) merchant profile at /.well-known/ucp advertising catalog search, cart, checkout, fulfillment, discount and order capabilities, a UCP MCP endpoint at /api/ucp/mcp, and OAuth 2.0 / OpenID Connect discovery documents for the Shopify Customer Account API.'
image: https://liveouter.com/cdn/shop/files/outer-hero-banner-aluminum_513ea457-357e-47e1-9e01-8e84b8b4fd29.png?v=1769763708&width=2048
layout: provider
mcp_servers:
- description: ''
  name: Outer MCP Server
  slug: outer-mcp-server
modified: '2026-08-04'
name: Outer
nav: Providers
network: true
overview: 'Outer publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Retail, E-Commerce, Consumer Goods, and Furniture.


  Outer''s developer surface includes engineering blog, support, signup flow, authentication, and 13 more developer resources.'
random_paper: 13
scopes:
- name: Outer Scopes
  scope_count: 4
  slug: outer-scopes
  summary_line: 4 scopes · authorizationCode
score:
  band: emerging
  composite: 21.9
  coverage:
    artifact_dirs: 12
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 34.2
    commercial_clarity: 34.2
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 26.2
    discoverability: 75.9
    governance: 18.2
    operational_transparency: 0.0
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - north-america
  previous_composite: 21.9
  provenance:
    conformance: first-party
    mcp: first-party
    skills: first-party
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/outer/refs/heads/main/screenshots/outer-2026-08-07T191054.png
security:
- kind: authentication
  name: Outer Authentication
  slug: outer-authentication
  summary_line: oauth2/openIdConnect · 1 scheme
- kind: domain-security
  name: Outer Domain Security
  slug: outer-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: outer
tags:
- Company
- Retail
- E-Commerce
- Consumer Goods
- Furniture
- Homes
- Direct to Consumer
- Agentic Commerce
- Shopify
- Universal Commerce Protocol
website: https://liveouter.com/
---
