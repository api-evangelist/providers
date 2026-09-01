---
agent_readiness:
  band: agent-native
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: na
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: false
    idempotency: na
    mcp_server: verified
    openapi_examples: false
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 54.4
  scored_at: '2026-09-01'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Heuritech Agentic Access
  operation_count: 21
  slug: heuritech-agentic-access
  summary_line: 21 operations
api_count: 10
apis:
- description: The commercial Heuritech data API, sold as part of the Business and Enterprise plans. Heuritech's own product page describes it as "weekly data points on each of our product attributes (prints, colors
  name: Heuritech Trend Data API
  slug: heuritech-trend-data-api
- description: A live remote Model Context Protocol server on the heuritech.com host, advertised through RFC 8414 OAuth authorization-server metadata and RFC 9728 protected-resource metadata. It is the WordPress MCP
  name: Heuritech MCP Server
  slug: heuritech-mcp-server
- description: The Heuritech editorial blog over the WordPress REST API — 169 published posts on fashion trend forecasting, AI, market insight and retail data, anonymously readable as JSON. Derived by API Evangelist
  name: Heuritech Posts API
  slug: heuritech-posts-api
- description: The 63 published marketing, product, pricing, FAQ and legal pages that make up heuritech.com, served as JSON by the WordPress REST API. Derived by API Evangelist from the live route-discovery document
  name: Heuritech Pages API
  slug: heuritech-pages-api
- description: The 3,800-item Heuritech media library — trend imagery, report covers, charts and downloadable assets — with rendition URLs and metadata, served as JSON by the WordPress REST API.
  name: Heuritech Media API
  slug: heuritech-media-api
- description: The 1,284 reader comments attached to Heuritech blog posts, anonymously readable as JSON by post, author or date range.
  name: Heuritech Comments API
  slug: heuritech-comments-api
- description: The five editorial categories Heuritech uses to classify its blog content, plus the (currently empty) tag taxonomy, served as JSON by the WordPress REST API.
  name: Heuritech Taxonomy API
  slug: heuritech-taxonomy-api
- description: The 25 authoring profiles behind Heuritech blog content — analysts, fashion experts and data scientists — with names, biographies and avatars, served as JSON by the WordPress REST API.
  name: Heuritech Users API
  slug: heuritech-users-api
- description: Site-wide search across the 232 indexed posts and pages on heuritech.com, returning id, title, url, type and subtype for each hit.
  name: Heuritech Search API
  slug: heuritech-search-api
- description: The WordPress metadata routes describing which post types, taxonomies and post statuses heuritech.com exposes — the self-description layer an agent reads before querying the content collections.
  name: Heuritech Discovery API
  slug: heuritech-discovery-api
artifact_total: 17
common:
- group: agent
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
  title: ''
  type: Plans
  url: plans/heuritech-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/heuritech-rate-limits.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/heuritech-mcp.yml
- group: build
  title: ''
  type: ToolCrosswalk
  url: mcp/heuritech-tool-crosswalk.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/heuritech-well-known.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/heuritech-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/heuritech-scopes.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/heuritech-domain-security.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/heuritech-conventions.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/heuritech-conformance.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/heuritech-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/heuritech-lifecycle.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/heuritech-data-model.yml
- group: build
  title: ''
  type: Packages
  url: packages/heuritech-packages.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/heuritech-llms.txt
- group: other
  title: ''
  type: Overlay
  url: overlays/heuritech-content-overlay.yaml
- group: agent
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
  slug: heuritech-mcp-server
modified: '2026-08-17'
name: Heuritech
nav: Providers
network: true
overview: 'Heuritech publishes 8 APIs on the [APIs.io](https://apis.io/) network, including Posts API, Pages API, Media API, and 5 more. Tagged areas include Company, Artificial Intelligence, Computer-Vision, Machine-Learning, and Fashion.


  Heuritech''s developer surface includes engineering blog, FAQ, pricing, signup flow, authentication, and 28 more developer resources.'
plans:
- name: Heuritech Plans Pricing
  plan_count: 3
  slug: heuritech-plans-pricing
random_paper: 16
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
  composite: 28.1
  coverage:
    artifact_dirs: 19
    catalog_gap: 68.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 71.1
    commercial_clarity: 71.1
    contract_governance: 4.5
    contract_quality: 13.1
    developer_ergonomics: 16.1
    discoverability: 64.8
    governance: 4.5
    operational_transparency: 2.6
  previous_composite: 28.1
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 8
      marker_coverage: 100.0
      total: 8
    mcp: first-party
    skills: derived
  schema_version: 0.17.2
  scored_at: '2026-09-01'
  trend: flat
security:
- kind: authentication
  name: Heuritech Authentication
  slug: heuritech-authentication
  summary_line: none/http/oauth2 · 3 schemes
- kind: domain-security
  name: Heuritech Domain Security
  slug: heuritech-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: heuritech
tags:
- Company
- Artificial Intelligence
- Computer-Vision
- Machine-Learning
- Fashion
- Trend Forecasting
- Demand Forecasting
- Retail
- Luxury
- Market Intelligence
- Consumer Insights
- Social Media Analytics
- Content
website: https://heuritech.com/
---
