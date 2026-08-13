---
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: true
    agentic_access: true
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: documented
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 47.1
  scored_at: '2026-08-12'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Fabric8Labs Agentic Access
  operation_count: 19
  slug: fabric8labs-agentic-access
  summary_line: 19 operations
api_count: 8
apis:
- description: A Model Context Protocol server endpoint registered on www.fabric8labs.com under the WordPress REST "mcp" namespace and served at /wp-json/mcp/mcp-oauth-server (with a sibling /wp-json/mcp/mcp-adapter
  name: Fabric8Labs MCP Server (WordPress MCP Adapter)
  slug: mcp
- description: The Posts API from Fabric8Labs — 2 anonymous read operations over the 13 published newsroom and technical-showcase posts on www.fabric8labs.com.
  name: Fabric8Labs Posts API
  slug: fabric8labs-posts-api
- description: The Pages API from Fabric8Labs — 2 anonymous read operations over the 27 published marketing, market and technology pages on www.fabric8labs.com.
  name: Fabric8Labs Pages API
  slug: fabric8labs-pages-api
- description: The Media API from Fabric8Labs — 2 anonymous read operations over the 276 media library attachments (product imagery, press assets, diagrams) on www.fabric8labs.com.
  name: Fabric8Labs Media API
  slug: fabric8labs-media-api
- description: The Team API from Fabric8Labs — 2 anonymous read operations over the "team" custom post type, a 3-record leadership directory registered by the fabric8labs WordPress theme.
  name: Fabric8Labs Team API
  slug: fabric8labs-team-api
- description: The Taxonomy API from Fabric8Labs — 4 anonymous read operations over the 6 content categories (News, Insights, Case Study, Guide, White Paper, Uncategorized) and the post_tag vocabulary, which is regi
  name: Fabric8Labs Taxonomy API
  slug: fabric8labs-taxonomy-api
- description: The Search API from Fabric8Labs — 1 anonymous read operation returning a unified search index across every public post type on www.fabric8labs.com.
  name: Fabric8Labs Search API
  slug: fabric8labs-search-api
- description: The Discovery API from Fabric8Labs — 6 anonymous read operations describing the registered post types, taxonomies and post statuses that define the rest of the surface.
  name: Fabric8Labs Discovery API
  slug: fabric8labs-discovery-api
artifact_total: 15
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/fabric8labs-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/fabric8labs-domain-security.yml
- group: docs
  title: ''
  type: OpenAPI
  url: openapi/
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/fabric8labs-llms.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/fabric8labs-well-known.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/fabric8labs-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/fabric8labs-scopes.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/fabric8labs-conventions.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/fabric8labs-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/fabric8labs-lifecycle.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/fabric8labs-data-model.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/fabric8labs-problem-types.yml
- group: build
  title: ''
  type: Examples
  url: examples/fabric8labs-examples.yml
- group: build
  title: ''
  type: Packages
  url: packages/fabric8labs-packages.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/fabric8labs-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/fabric8labs-rate-limits.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/fabric8labs-posts-api-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/fabric8labs-pages-api-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/fabric8labs-media-api-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/fabric8labs-team-api-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/fabric8labs-taxonomy-api-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/fabric8labs-search-api-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/fabric8labs-discovery-api-overlay.yaml
- group: company
  title: ''
  type: Website
  url: https://www.fabric8labs.com/
- group: company
  title: ''
  type: About
  url: https://www.fabric8labs.com/about/
- group: other
  title: ''
  type: Technology
  url: https://www.fabric8labs.com/technology/
- group: other
  title: ''
  type: Manufacturing
  url: https://www.fabric8labs.com/manufacturing/
- group: other
  title: ''
  type: Markets
  url: https://www.fabric8labs.com/markets/
- group: other
  title: ''
  type: Industries
  url: https://www.fabric8labs.com/industries/
- group: company
  title: ''
  type: Blog
  url: https://www.fabric8labs.com/press/
- group: company
  title: ''
  type: BlogRSS
  url: https://www.fabric8labs.com/feed/
- group: company
  title: ''
  type: Press
  url: https://www.fabric8labs.com/press/
- group: other
  title: ''
  type: Events
  url: https://www.fabric8labs.com/events/
- group: operate
  title: ''
  type: Support
  url: https://www.fabric8labs.com/contact-us/
- group: operate
  title: ''
  type: Contact
  url: https://www.fabric8labs.com/contact-us/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.fabric8labs.com/privacy-policy/
- group: other
  title: ''
  type: Accessibility
  url: https://www.fabric8labs.com/web-accessibility/
- group: other
  title: ''
  type: SiteMap
  url: https://www.fabric8labs.com/site-map/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Fabric8Labs
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/fabric8labs
- group: other
  title: ''
  type: SecondaryMarket
  url: https://forgeglobal.com/fabric8labs_stock/
created: '2026-08-12'
description: Fabric8Labs is a San Diego, California based advanced-manufacturing company founded in 2015 that invented and commercialized Electrochemical Additive Manufacturing (ECAM), a room-temperature metal 3D printing process that uses a patented microelectrode array printhead to electroplate copper ions out of a water-based metal-salt solution pixel by pixel. Unlike powder-bed and laser metal additive methods, ECAM needs no high-temperature step, no expensive metal powder feedstock and effectively no post-processing, prints at micron-scale resolution directly onto temperature-sensitive substrates, and the company reports more than a 90% reduction in greenhouse gas emissions against alternative additive and traditional manufacturing routes. Fabric8Labs operates as both a technology developer and a production foundry, manufacturing high-precision components for data-center liquid cooling and AI/HPC thermal management (cold plates, single-phase, two-phase and immersion cooling), RF and
  wireless communications, satellite and aerospace systems, power electronics, photonics cooling, semiconductors, medical devices and luxury goods. It has raised funding from Intel Capital, TDK Ventures and others, including a $50M round announced in November 2025 to expand United States manufacturing capacity toward tens of millions of components annually, and on 10 June 2026 announced it will be acquired by TDK Corporation — the company continues under existing leadership, with ECAM folded into TDK's global manufacturing network. Fabric8Labs publishes no product, customer or developer API and runs no developer program; the only machine-readable surface on fabric8labs.com is the public WordPress REST API (namespace wp/v2) that serves the company newsroom, site pages, leadership team directory, taxonomy and media library as JSON, alongside a WordPress MCP Adapter endpoint and RFC 8414/RFC 9728 OAuth discovery documents that are served but authentication-gated.
image: https://www.fabric8labs.com/wp-content/uploads/2024/06/logo-background.png
layout: provider
mcp_servers:
- description: ''
  name: fabric8labs-mcp.yml
  slug: fabric8labs-mcpyml
modified: '2026-08-12'
name: Fabric8Labs
nav: Providers
network: true
overview: 'Fabric8Labs publishes 7 APIs on the [APIs.io](https://apis.io/) network, including Posts API, Pages API, Media API, and 4 more. Tagged areas include Company, Advanced Manufacturing, Additive Manufacturing, 3D Printing, and Metal 3D Printing.


  Fabric8Labs'' developer surface includes authentication, code examples, engineering blog, support, and 38 more developer resources.'
plans:
- name: Fabric8Labs Plans Pricing
  plan_count: 0
  slug: fabric8labs-plans-pricing
random_paper: 9
rate_limits:
- limit_count: 0
  name: Fabric8Labs Rate Limits
  slug: fabric8labs-rate-limits
scopes:
- name: Fabric8Labs Scopes
  scope_count: 1
  slug: fabric8labs-scopes
  summary_line: 1 scope · authorizationCode
score:
  band: thin
  composite: 34.6
  facets:
    commercial_clarity: 10.5
    contract_quality: 53.7
    developer_ergonomics: 23.9
    discoverability: 81.5
    governance: 20.8
    operational_transparency: 5.3
  regulatory:
    applies: true
    matched_via: tags
    regime: Energy & Utilities
    regime_id: energy_utilities
    score: 51.4
  schema_version: 0.11.0
  scored_at: '2026-08-12'
security:
- kind: authentication
  name: Fabric8Labs Authentication
  slug: fabric8labs-authentication
  summary_line: none/oauth2 · 3 schemes
- kind: domain-security
  name: Fabric8Labs Domain Security
  slug: fabric8labs-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: fabric8labs
tags:
- Company
- Advanced Manufacturing
- Additive Manufacturing
- 3D Printing
- Metal 3D Printing
- Electrochemical Additive Manufacturing
- Thermal Management
- Liquid Cooling
- Data Centers
- Semiconductors
- Electronics
- Aerospace
- Photonics
- Power Electronics
- Hardware
- Content
website: https://www.fabric8labs.com/
---
