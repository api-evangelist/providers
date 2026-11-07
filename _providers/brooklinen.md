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
    error_semantics: derived
    event_surface_described: false
    idempotency: documented
    mcp_server: platform
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 25.0
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: Live Universal Commerce Protocol (UCP) endpoint exposed over MCP JSON-RPC at https://www.brooklinen.com/api/ucp/mcp, advertised by the store's own /agents.md, /robots.txt and /.well-known/ucp discover
  name: Brooklinen UCP / MCP Agentic Commerce API
  slug: brooklinen-ucp-mcp-agentic-commerce-api
artifact_total: 7
common:
- group: other
  href: https://artifacts.apis.io/brooklinen/capabilities/brooklinen-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/brooklinen-capability-edges.yml
- group: auth
  href: https://artifacts.apis.io/brooklinen/security/brooklinen-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/brooklinen-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.brooklinen.com/
- group: docs
  title: ''
  type: Documentation
  url: https://www.brooklinen.com/agents.md
- group: docs
  title: ''
  type: APIReference
  url: https://www.brooklinen.com/agents.md
- group: start
  title: ''
  type: GettingStarted
  url: https://www.brooklinen.com/agents.md
- group: operate
  title: ''
  type: Support
  url: https://www.brooklinen.com/pages/contact
- group: operate
  title: ''
  type: HelpCenter
  url: https://www.brooklinen.com/pages/faq
- group: company
  title: ''
  type: Blog
  url: https://www.brooklinen.com/blogs/brookliving
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Brooklinen
- group: start
  title: ''
  type: SignUp
  url: https://www.brooklinen.com/pages/sign-up
- group: start
  title: ''
  type: Login
  url: https://www.brooklinen.com/account/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.brooklinen.com/policies/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.brooklinen.com/policies/privacy-policy
- group: agent
  href: https://artifacts.apis.io/brooklinen/mcp/brooklinen-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/brooklinen-mcp.yml
- group: build
  href: https://artifacts.apis.io/brooklinen/mcp/brooklinen-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/brooklinen-tool-crosswalk.yml
- group: agent
  href: https://artifacts.apis.io/brooklinen/llms/brooklinen-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/brooklinen-llms.txt
- group: agent
  href: https://artifacts.apis.io/brooklinen/well-known/brooklinen-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/brooklinen-well-known.yml
- group: auth
  href: https://artifacts.apis.io/brooklinen/authentication/brooklinen-authentication.yml
  title: ''
  type: Authentication
  url: authentication/brooklinen-authentication.yml
- group: auth
  href: https://artifacts.apis.io/brooklinen/scopes/brooklinen-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/brooklinen-scopes.yml
- group: design
  href: https://artifacts.apis.io/brooklinen/conventions/brooklinen-conventions.yml
  title: ''
  type: Conventions
  url: conventions/brooklinen-conventions.yml
- group: design
  href: https://artifacts.apis.io/brooklinen/conventions/brooklinen-conventions.yml
  title: ''
  type: Idempotency
  url: conventions/brooklinen-conventions.yml
- group: design
  href: https://artifacts.apis.io/brooklinen/lifecycle/brooklinen-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/brooklinen-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/brooklinen/conformance/brooklinen-conformance.yml
  title: ''
  type: Conformance
  url: conformance/brooklinen-conformance.yml
- group: design
  href: https://artifacts.apis.io/brooklinen/errors/brooklinen-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/brooklinen-problem-types.yml
- group: design
  href: https://artifacts.apis.io/brooklinen/data-model/brooklinen-data-model.yml
  title: ''
  type: DataModel
  url: data-model/brooklinen-data-model.yml
- group: agent
  href: https://artifacts.apis.io/brooklinen/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: other
  href: https://artifacts.apis.io/brooklinen/overlays/brooklinen-storefront-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/brooklinen-storefront-overlay.yaml
- group: other
  title: ''
  type: SecondaryMarketListing
  url: https://forgeglobal.com/brooklinen_stock/
created: '2026-08-02'
description: 'Brooklinen is a direct-to-consumer home essentials brand founded in Brooklyn, New York in 2014 by Rich and Vicki Fulop, selling sheets, duvet covers, comforters, pillows, towels, robes and loungewear direct from the mill to the customer. Brooklinen publishes no traditional developer API program, but its storefront runs on Shopify and exposes a substantial machine-readable agent surface: an agent instruction document at /agents.md (mirrored at /llms.txt), a Universal Commerce Protocol (UCP) merchant profile at /.well-known/ucp declaring protocol versions 2026-04-08 and 2026-01-23, a live UCP/MCP JSON-RPC endpoint at /api/ucp/mcp for agent-driven catalog search, cart, checkout and order operations, OAuth 2.0 / OIDC customer-account authorization metadata at /.well-known/oauth-authorization-server and /.well-known/oauth-protected-resource, and the read-only Shopify storefront JSON endpoints for products, collections, search suggestions and cart. Checkout explicitly requires contemporaneous
  human buyer approval.'
image: https://cdn.shopify.com/s/files/1/0951/7126/files/0126_Shopify_Social_Image.jpg?v=1765839763
layout: provider
mcp_servers:
- description: Remote MCP server at www.brooklinen.com over HTTP; 13 tools listed.
  name: Brooklinen MCP Server
  slug: brooklinen-ucp-shopping
modified: '2026-08-02'
name: Brooklinen
nav: Providers
network: true
overview: 'Brooklinen is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include E-Commerce, Retail, Direct to Consumer, Home Goods, and Bedding.


  Brooklinen''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, signup flow, authentication, and 22 more developer resources.'
random_paper: 19
scopes:
- name: Brooklinen Scopes
  scope_count: 4
  slug: brooklinen-scopes
  summary_line: 4 scopes · authorizationCode
score:
  band: thin
  composite: 30.0
  coverage:
    artifact_dirs: 21
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 34.2
    contract_governance: 18.2
    contract_quality: 1.7
    developer_ergonomics: 54.8
    discoverability: 75.0
    operational_transparency: 2.6
  previous_composite: 30.0
  provenance:
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 1
      marker_coverage: 100.0
      total: 1
    mcp: platform-generated
    skills: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 31.3
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/brooklinen/brooklinen-2026-08-07T162830.png
security:
- kind: authentication
  name: Brooklinen Authentication
  slug: brooklinen-authentication
  summary_line: oauth2/openIdConnect/none · 4 schemes
- kind: domain-security
  name: Brooklinen Domain Security
  slug: brooklinen-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
skill_count: 2
skills:
- name: Buy from Brooklinen over UCP/MCP
  slug: brooklinen-agentic-purchase
- name: Browse the Brooklinen catalog
  slug: brooklinen-browse-catalog
slug: brooklinen
tags:
- E-Commerce
- Retail
- Direct to Consumer
- Home Goods
- Bedding
- Shopify
- Agentic Commerce
- Universal Commerce Protocol
- MCP
- Agent-Native
- Catalog
- Checkout
website: https://www.brooklinen.com/
---
