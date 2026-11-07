---
access_model:
  confidence: high
  label: Paid
  onboarding: unknown
  pricing: paid
  public: false
  source:
  - plans
  - authentication
  - scopes
  - rate-limits
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: derived
    event_surface_described: false
    idempotency: false
    mcp_server: platform
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 22.5
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Heuritech Agentic Access
  operation_count: 21
  slug: heuritech-agentic-access
  summary_line: 21 operations
api_count: 3
apis:
- description: The commercial Heuritech data API, sold as part of the Business and Enterprise plans. Heuritech's own product page describes it as "weekly data points on each of our product attributes (prints, colors
  name: Heuritech Trend Data API
  slug: heuritech-trend-data-api
- description: A live remote Model Context Protocol server on the heuritech.com host, advertised through RFC 8414 OAuth authorization-server metadata and RFC 9728 protected-resource metadata. It is the WordPress MCP
  name: Heuritech MCP Server
  slug: heuritech-mcp-server
- description: 'The public WordPress REST API (wp-json) of the Heuritech website at heuritech.com: the route index of the site''s content management system, catalogued as one site surface rather than as separate APIs.'
  name: Heuritech Website (WordPress REST)
  slug: heuritech-com-website-wordpress-rest
artifact_total: 13
common:
- group: agent
  href: https://artifacts.apis.io/heuritech/agentic-access/heuritech-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/heuritech-agentic-access.yml
- group: company
  title: ''
  type: Website
  url: https://heuritech.com/
- group: company
  title: ''
  type: About
  url: https://heuritech.com/company-about-us/
- group: other
  title: ''
  type: ParentCompany
  url: https://heuritech.com/luxurynsight-group/
- group: company
  title: ''
  type: Blog
  url: https://heuritech.com/blog/
- group: company
  title: ''
  type: BlogRSS
  url: https://heuritech.com/feed/
- group: company
  title: ''
  type: Press
  url: https://heuritech.com/press/
- group: operate
  title: ''
  type: FAQ
  url: https://heuritech.com/faq/
- group: commercial
  title: ''
  type: Pricing
  url: https://heuritech.com/pricing/
- group: start
  title: ''
  type: SignUp
  url: https://heuritech.com/get-a-demo/
- group: start
  title: ''
  type: Login
  url: https://market-trends.heuritech.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://heuritech.com/terms-conditions/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://heuritech.com/privacy-policy/
- group: operate
  title: ''
  type: Contact
  url: mailto:contact@heuritech.com
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/heuritech
- group: company
  title: ''
  type: Careers
  url: https://www.welcometothejungle.com/en/companies/luxurynsight
- group: commercial
  href: https://artifacts.apis.io/heuritech/plans/heuritech-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/heuritech-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/heuritech/rate-limits/heuritech-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/heuritech-rate-limits.yml
- group: agent
  href: https://artifacts.apis.io/heuritech/mcp/heuritech-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/heuritech-mcp.yml
- group: build
  href: https://artifacts.apis.io/heuritech/mcp/heuritech-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/heuritech-tool-crosswalk.yml
- group: agent
  href: https://artifacts.apis.io/heuritech/well-known/heuritech-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/heuritech-well-known.yml
- group: auth
  href: https://artifacts.apis.io/heuritech/authentication/heuritech-authentication.yml
  title: ''
  type: Authentication
  url: authentication/heuritech-authentication.yml
- group: auth
  href: https://artifacts.apis.io/heuritech/scopes/heuritech-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/heuritech-scopes.yml
- group: auth
  href: https://artifacts.apis.io/heuritech/security/heuritech-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/heuritech-domain-security.yml
- group: design
  href: https://artifacts.apis.io/heuritech/conventions/heuritech-conventions.yml
  title: ''
  type: Conventions
  url: conventions/heuritech-conventions.yml
- group: design
  href: https://artifacts.apis.io/heuritech/conformance/heuritech-conformance.yml
  title: ''
  type: Conformance
  url: conformance/heuritech-conformance.yml
- group: design
  href: https://artifacts.apis.io/heuritech/errors/heuritech-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/heuritech-problem-types.yml
- group: design
  href: https://artifacts.apis.io/heuritech/lifecycle/heuritech-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/heuritech-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/heuritech/data-model/heuritech-data-model.yml
  title: ''
  type: DataModel
  url: data-model/heuritech-data-model.yml
- group: build
  href: https://artifacts.apis.io/heuritech/packages/heuritech-packages.yml
  title: ''
  type: Packages
  url: packages/heuritech-packages.yml
- group: agent
  href: https://artifacts.apis.io/heuritech/llms/heuritech-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/heuritech-llms.txt
- group: agent
  href: https://artifacts.apis.io/heuritech/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-08-17'
description: 'Heuritech is a Paris-based artificial-intelligence company (Heuritech SAS, RCS Paris B 794 196 055) founded in 2013 by two machine-learning PhDs, and since December 2024 part of the Luxurynsight group. It applies computer vision and deep-learning demand forecasting to roughly one million social-media posts a day from Instagram, Weibo and TikTok, recognising more than 2,000 fashion attributes — prints, colours, fabrics, shapes and product details — to quantify and predict consumer demand for apparel, footwear and luxury brands up to a year ahead. The product is sold as a SaaS platform and, on the Business and Enterprise plans, as a data API delivering weekly data points per product attribute with up to six years of history and two years of forecast for injection into a customer''s own planning models. That commercial API is entirely sales-gated: Heuritech publishes no developer portal, no API reference, no base URL and no machine-readable specification for it, and access begins
  with a demo request. The only machine-readable surface a member of the public can reach on heuritech.com is the WordPress REST API (wp/v2) that serves the company blog, marketing pages, media library, comments, editorial taxonomy and site search as JSON, alongside a live but OAuth-gated WordPress MCP server advertised through RFC 8414 and RFC 9728 discovery metadata.'
image: https://heuritech.com/wp-content/uploads/2020/06/20200526_image_partage.jpg
layout: provider
mcp_servers:
- description: Heuritech serves a live remote Model Context Protocol server on its primary marketing host. It is advertised nowhere in Heuritech's documentation and appears in no MCP registry — it was found by probi
  name: Heuritech MCP Server
  slug: mcp-oauth-server
modified: '2026-08-17'
name: Heuritech
nav: Providers
network: true
overview: 'Heuritech is listed with 3 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Artificial Intelligence, Computer Vision, Machine Learning, and Fashion.


  Heuritech''s developer surface includes engineering blog, FAQ, pricing, signup flow, authentication, and 27 more developer resources.'
plans:
- name: Heuritech Plans Pricing
  plan_count: 3
  slug: heuritech-plans-pricing
random_paper: 1
rate_limits:
- limit_count: 0
  name: Heuritech Rate Limits
  slug: heuritech-rate-limits
scopes:
- name: Heuritech Scopes
  scope_count: 1
  slug: heuritech-scopes
  summary_line: 1 scope · authorizationCode
score:
  band: thin
  composite: 27.2
  coverage:
    artifact_dirs: 21
    catalog_earned: 42.0
    catalog_earned_first_party: 12.0
    catalog_gap: 73.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -1.0
  facets:
    access_clarity: 71.1
    contract_governance: 4.5
    contract_quality: 0.0
    developer_ergonomics: 20.8
    discoverability: 57.5
    operational_transparency: 2.6
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - france
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - europe
    - france-iberia
  previous_composite: 28.2
  provenance:
    agentic_access: derived
    conformance: derived
    mcp: site-plugin
    skills: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 30.0
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/heuritech/heuritech-2026-09-02T145723.png
security:
- kind: authentication
  name: Heuritech Authentication
  slug: heuritech-authentication
  summary_line: none/http/oauth2 · 3 schemes
- kind: domain-security
  name: Heuritech Domain Security
  slug: heuritech-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
skill_count: 3
skills:
- name: Harvest the Heuritech product and pricing pages
  slug: heuritech-harvest-product-and-pricing-pages
- name: Read the Heuritech trend editorial
  slug: heuritech-read-trend-editorial
- name: Search the Heuritech estate
  slug: heuritech-search-the-estate
slug: heuritech
tags:
- Company
- Artificial Intelligence
- Computer Vision
- Machine Learning
- Fashion
- Trend Forecasting
- Demand Forecasting
- Retail
- Luxury
- Market Intelligence
- Consumer Insights
- Social Media Analytics
website: https://heuritech.com/
---
