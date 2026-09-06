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
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    agentic_commerce: platform
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    openapi_examples: false
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 38.0
  scored_at: '2026-09-05'
api_count: 2
apis:
- description: Anonymous, fully introspectable GraphQL endpoint served from Johnnie-O's own Hydrogen storefront host. This is the Shopify Storefront API for merchant tenant 22750137; the Hydrogen app proxies the req
  name: Johnnie-O Storefront GraphQL API
  slug: storefront-graphql
- description: Live remote MCP server implementing the Universal Commerce Protocol shopping service (version 2026-04-08) on Johnnie-O's Shopify-served primary domain. An anonymous JSON-RPC tools/list returns thirtee
  name: Johnnie-O UCP Commerce MCP Endpoint
  slug: ucp-mcp
artifact_total: 8
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/johnnie-o-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.johnnie-o.com/
- group: docs
  title: ''
  type: GraphQL
  url: graphql/johnnie-o-storefront.graphql
- group: agent
  title: ''
  type: MCPServer
  url: mcp/johnnie-o-mcp.yml
- group: build
  title: ''
  type: ToolCrosswalk
  url: mcp/johnnie-o-tool-crosswalk.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/johnnie-o-llms.txt
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/johnnie-o-well-known.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/johnnie-o-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/johnnie-o-scopes.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/johnnie-o-conformance.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/johnnie-o-conventions.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/johnnie-o-lifecycle.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/johnnie-o-problem-types.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/johnnie-o-data-model.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/johnnie-o-rate-limits.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/johnnie-o-plans-pricing.yml
- group: build
  title: ''
  type: Packages
  url: packages/johnnie-o-packages.yml
- group: docs
  title: ''
  type: Documentation
  url: https://checkout.johnnie-o.com/llms.txt
- group: operate
  title: ''
  type: Support
  url: https://www.johnnie-o.com/contact-us
- group: operate
  title: ''
  type: HelpCenter
  url: https://www.johnnie-o.com/pages/faqs-new-icon
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.johnnie-o.com/pages/terms-conditions
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.johnnie-o.com/pages/privacy
- group: start
  title: ''
  type: SignUp
  url: https://www.johnnie-o.com/account/login
created: '2026-08-23'
description: 'Johnnie-O is a Los Angeles based men''s, women''s and boys'' apparel brand founded in 2005 by John O''Donnell, blending East Coast prep with West Coast casual across polos, performance golf shirts, outerwear, shorts and collegiate Game Day licensed product, sold direct through johnnie-o.com, its own retail stores, wholesale and green-grass golf accounts. It is an apparel company, not a software vendor, and it operates no developer program, publishes no API documentation, ships no SDK and has no GitHub organization. It does, however, expose two real anonymous machine-readable surfaces through the Shopify Hydrogen storefront it runs: an introspectable Storefront GraphQL endpoint on its own domain, and a live Universal Commerce Protocol (UCP) MCP endpoint on its Shopify-served primary domain that publishes thirteen agent tools for catalog search, cart, checkout and order lookup. The store also serves its own llms.txt and agents.md agent instructions. Those surfaces are Shopify
  platform infrastructure running under Johnnie-O''s tenant and on hosts Johnnie-O controls; they are profiled here as Johnnie-O''s agent surface, not as Johnnie-O-authored API design.'
image: https://johnnie-o-prod.s3.us-west-2.amazonaws.com/media/_190x190_crop_center-center_none/logo-200x200.png
layout: provider
mcp_servers:
- description: ''
  name: Johnnie-O MCP Server
  slug: johnnie-o-mcp-server
modified: '2026-08-23'
name: Johnnie-O
nav: Providers
network: true
overview: 'Johnnie-O publishes 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Apparel, Retail, E-Commerce, and Direct to Consumer.


  Johnnie-O''s developer surface includes authentication, documentation, support, signup flow, and 20 more developer resources.'
plans:
- name: Johnnie O Plans Pricing
  plan_count: 0
  slug: johnnie-o-plans-pricing
random_paper: 0
rate_limits:
- limit_count: 0
  name: Johnnie O Rate Limits
  slug: johnnie-o-rate-limits
scopes:
- name: Johnnie O Scopes
  scope_count: 0
  slug: johnnie-o-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: thin
  composite: 31.5
  coverage:
    artifact_dirs: 17
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
    contract_quality: 37.2
    developer_ergonomics: 28.0
    discoverability: 75.9
    governance: 18.2
    operational_transparency: 0.0
  previous_composite: 31.5
  provenance:
    conformance: first-party
    mcp: first-party
    skills: derived
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/johnnie-o/refs/heads/main/screenshots/johnnie-o-2026-09-02T145957.png
security:
- kind: authentication
  name: Johnnie O Authentication
  slug: johnnie-o-authentication
  summary_line: 4 schemes
- kind: domain-security
  name: Johnnie O Domain Security
  slug: johnnie-o-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: johnnie-o
tags:
- Company
- Apparel
- Retail
- E-Commerce
- Direct to Consumer
- Golf
- Fashion
- Consumer Goods
- Shopify
- Agentic Commerce
website: https://www.johnnie-o.com/
---
