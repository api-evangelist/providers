---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - plans
  - authentication
  - scopes
  - rate-limits
  - security
  - sandbox
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: documented
    event_surface_described: true
    idempotency: false
    mcp_server: verified
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: false
    pagination_ratio: false
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 49.8
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 4
  human_in_the_loop: 0
  name: Fabric Origin Agentic Access
  operation_count: 121
  slug: fabric-origin-agentic-access
  summary_line: 121 operations · 4 acting
api_count: 14
apis:
- baseURL: https://api.origin.fabricdata.com
  baseurl_source: declared
  description: The Entertainment API ingests and serves metadata for movies, television shows, and games, including identifiers used to retrieve associated videos and images from sibling APIs. Responses are availabl
  name: Fabric Origin Entertainment API
  slug: entertainment-api
- baseURL: https://api.origin.fabricdata.com
  baseurl_source: declared
  description: The Celebrity API serves metadata about celebrities, including actors, directors, and other entertainment industry figures, with cross references to titles served by the Entertainment API.
  name: Fabric Origin Celebrity API
  slug: celebrity-api
- baseURL: https://api.origin.fabricdata.com
  baseurl_source: declared
  description: The Video API generates playable links for trailers and other video assets using video identifiers returned from the Entertainment API, allowing customers to embed Fabric Origin video content into the
  name: Fabric Origin Video API
  slug: video-api
- baseURL: https://api.origin.fabricdata.com
  baseurl_source: declared
  description: The Image API provides access to images hosted on Fabric Origin's servers, including posters, stills, and promotional artwork referenced from the Entertainment and Celebrity APIs. Customers are encour
  name: Fabric Origin Image API
  slug: image-api
- baseURL: https://api.origin.fabricdata.com
  baseurl_source: declared
  description: The Entertainment API from Fabric Origin — 14 operation(s) for entertainment.
  name: Fabric Origin Entertainment API
  slug: fabric-origin-entertainment-api
- baseURL: https://api.origin.fabricdata.com
  baseurl_source: declared
  description: The Images API from Fabric Origin — 4 operation(s) for images.
  name: Fabric Origin Images API
  slug: fabric-origin-images-api
- baseURL: https://api.origin.fabricdata.com
  baseurl_source: declared
  description: The Videos API from Fabric Origin — 2 operation(s) for videos.
  name: Fabric Origin Videos API
  slug: fabric-origin-videos-api
- baseURL: https://api.origin.fabricdata.com
  baseurl_source: declared
  description: Theatrical showtimes and ticketing — geolocation lookup, nearby theaters, movies playing, and showtime groupings by date, theater, format and amenities, linked back to Origin title identifiers.
  name: Fabric Origin Fandango API
  slug: fandango-api
- baseURL: https://api.origin.fabricdata.com
  baseurl_source: declared
  description: Metascores and Metacritic reviews for movies and TV, keyed on Origin identifiers.
  name: Fabric Origin Metacritic API
  slug: metacritic-api
- description: The Origin Studio metadata management API — records, record lifecycles, fields, datasets, media, credits, contributors, data deliveries, data ingress, background jobs, audit, tenants and users. Follow
  name: Origin Studio Production API
  slug: origin-studio-api
- description: A hosted Model Context Protocol server over Origin Studio — metadata records, catalog operations and availability. Streamable HTTP on the root path, OAuth 2.0 with mandatory PKCE, acting as its own au
  name: Origin Studio MCP Server
  slug: origin-studio-mcp
- description: A hosted Model Context Protocol server over Origin Insights streaming market intelligence — availability, demand, TVOD pricing, subscription plans, platforms, supply, coming-soon and pre-built reports
  name: Origin Insights MCP Server
  slug: origin-insights-mcp
- baseURL: https://api.origin.fabricdata.com
  baseurl_source: declared
  description: The analytics API from Fabric Origin — 1 operation(s) for analytics.
  name: Fabric Origin Analytics API
  slug: fabric-origin-analytics-api
- baseURL: https://api.origin.fabricdata.com
  baseurl_source: declared
  description: The common API from Fabric Origin — 39 operation(s) for common.
  name: Fabric Origin Common API
  slug: fabric-origin-common-api
- baseURL: https://api.origin.fabricdata.com
  baseurl_source: declared
  description: The commonsense API from Fabric Origin — 2 operation(s) for commonsense.
  name: Fabric Origin Commonsense API
  slug: fabric-origin-commonsense-api
- baseURL: https://api.origin.fabricdata.com
  baseurl_source: declared
  description: The katchmedia API from Fabric Origin — 1 operation(s) for katchmedia.
  name: Fabric Origin Katchmedia API
  slug: fabric-origin-katchmedia-api
- baseURL: https://api.origin.fabricdata.com
  baseurl_source: declared
  description: The rabbitrecommendations API from Fabric Origin — 1 operation(s) for rabbitrecommendations.
  name: Fabric Origin Rabbitrecommendations API
  slug: fabric-origin-rabbitrecommendations-api
- baseURL: https://api.origin.fabricdata.com
  baseurl_source: declared
  description: The rev API from Fabric Origin — 3 operation(s) for rev.
  name: Fabric Origin Rev API
  slug: fabric-origin-rev-api
- baseURL: https://api.origin.fabricdata.com
  baseurl_source: declared
  description: The rottentomatoes API from Fabric Origin — 4 operation(s) for rottentomatoes.
  name: Fabric Origin Rottentomatoes API
  slug: fabric-origin-rottentomatoes-api
- baseURL: https://api.origin.fabricdata.com
  baseurl_source: declared
  description: The tvgrid API from Fabric Origin — 21 operation(s) for tvgrid.
  name: Fabric Origin Tvgrid API
  slug: fabric-origin-tvgrid-api
artifact_total: 38
asyncapis:
- description: ''
  name: Fabric Origin Events Webhooks
  slug: fabric-origin-events-webhooks
collections:
- collection_type: open
  name: Fabric Origin Data APIs Entertainment API
  slug: open-fabric-origin-entertainment-api
- collection_type: open
  name: Fabric Origin Data APIs Entertainment Images API
  slug: open-fabric-origin-images-api
- collection_type: open
  name: Fabric Origin Data APIs Entertainment Videos API
  slug: open-fabric-origin-videos-api
- collection_type: open
  name: Fabric Origin Entertainment Data APIs
  slug: open-fabric-origin
common:
- group: other
  href: https://artifacts.apis.io/fabric-origin/capabilities/fabric-origin-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/fabric-origin-capability-edges.yml
- group: agent
  href: https://artifacts.apis.io/fabric-origin/agentic-access/fabric-origin-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/fabric-origin-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/fabric-origin/security/fabric-origin-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/fabric-origin-domain-security.yml
- group: auth
  href: https://artifacts.apis.io/fabric-origin/authentication/fabric-origin-authentication.yml
  title: ''
  type: Authentication
  url: authentication/fabric-origin-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://www.fabricdata.com/
- group: other
  title: ''
  type: Knowledge Base
  url: https://knowledgebase.fabricdata.com/origin
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.origin.fabricdata.com/portal/login
- group: docs
  title: ''
  type: Documentation
  url: https://knowledgebase.fabricdata.com/origin/apis-all/
- group: docs
  title: ''
  type: Documentation
  url: https://knowledgebase.fabricdata.com/origin
- group: docs
  title: ''
  type: APIReference
  url: https://knowledgebase.fabricdata.com/origin/apis-all
- group: start
  title: ''
  type: GettingStarted
  url: https://knowledgebase.fabricdata.com/origin/getting-started
- group: start
  title: ''
  type: SignUp
  url: https://www.fabricdata.com/contact-us
- group: start
  title: ''
  type: Login
  url: https://developer.origin.fabricdata.com/portal/login
- group: operate
  title: ''
  type: Support
  url: https://metahive.atlassian.net/servicedesk/customer/portal/2
- group: operate
  title: ''
  type: HelpCenter
  url: https://helpcenter.fabricdata.com/
- group: company
  title: ''
  type: Blog
  url: https://www.fabricdata.com/trends
- group: commercial
  title: ''
  type: Pricing
  url: https://www.fabricdata.com/pricing-models
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.fabricdata.com/privacy-policy
- group: operate
  title: ''
  type: StatusPage
  url: https://status.fabricdata.com/
- group: operate
  title: ''
  type: FAQ
  url: https://knowledgebase.fabricdata.com/origin/faq
- group: operate
  href: https://artifacts.apis.io/fabric-origin/changelog/fabric-origin-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/fabric-origin-changelog.yml
- group: agent
  href: https://artifacts.apis.io/fabric-origin/llms/fabric-origin-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/fabric-origin-llms.txt
- group: agent
  href: https://artifacts.apis.io/fabric-origin/mcp/fabric-origin-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/fabric-origin-mcp.yml
- group: build
  href: https://artifacts.apis.io/fabric-origin/mcp/fabric-origin-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/fabric-origin-tool-crosswalk.yml
- group: agent
  href: https://artifacts.apis.io/fabric-origin/well-known/fabric-origin-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/fabric-origin-well-known.yml
- group: build
  href: https://artifacts.apis.io/fabric-origin/packages/fabric-origin-packages.yml
  title: ''
  type: Packages
  url: packages/fabric-origin-packages.yml
- group: design
  href: https://artifacts.apis.io/fabric-origin/conventions/fabric-origin-conventions.yml
  title: ''
  type: Conventions
  url: conventions/fabric-origin-conventions.yml
- group: design
  href: https://artifacts.apis.io/fabric-origin/conformance/fabric-origin-conformance.yml
  title: ''
  type: Conformance
  url: conformance/fabric-origin-conformance.yml
- group: auth
  href: https://artifacts.apis.io/fabric-origin/conformance/fabric-origin-conformance.yml
  title: ''
  type: Compliance
  url: conformance/fabric-origin-conformance.yml
- group: design
  href: https://artifacts.apis.io/fabric-origin/errors/fabric-origin-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/fabric-origin-problem-types.yml
- group: design
  href: https://artifacts.apis.io/fabric-origin/lifecycle/fabric-origin-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/fabric-origin-lifecycle.yml
- group: auth
  href: https://artifacts.apis.io/fabric-origin/scopes/fabric-origin-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/fabric-origin-scopes.yml
- group: start
  href: https://artifacts.apis.io/fabric-origin/sandbox/fabric-origin-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/fabric-origin-sandbox.yml
- group: design
  href: https://artifacts.apis.io/fabric-origin/data-model/fabric-origin-data-model.yml
  title: ''
  type: DataModel
  url: data-model/fabric-origin-data-model.yml
- group: design
  href: https://artifacts.apis.io/fabric-origin/asyncapi/fabric-origin-events-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/fabric-origin-events-webhooks.yml
- group: agent
  href: https://artifacts.apis.io/fabric-origin/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: commercial
  href: https://artifacts.apis.io/fabric-origin/plans/fabric-origin-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/fabric-origin-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/fabric-origin/rate-limits/fabric-origin-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/fabric-origin-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/fabric-origin/finops/fabric-origin-finops.yml
  title: ''
  type: FinOps
  url: finops/fabric-origin-finops.yml
- group: other
  href: https://artifacts.apis.io/fabric-origin/overlays/fabric-origin-captions-translations-api-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/fabric-origin-captions-translations-api-overlay.yaml
- group: other
  href: https://artifacts.apis.io/fabric-origin/overlays/fabric-origin-celebrity-api-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/fabric-origin-celebrity-api-overlay.yaml
- group: other
  href: https://artifacts.apis.io/fabric-origin/overlays/fabric-origin-common-metadata-api-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/fabric-origin-common-metadata-api-overlay.yaml
- group: other
  href: https://artifacts.apis.io/fabric-origin/overlays/fabric-origin-common-sense-media-api-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/fabric-origin-common-sense-media-api-overlay.yaml
- group: other
  href: https://artifacts.apis.io/fabric-origin/overlays/fabric-origin-entertainment-api-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/fabric-origin-entertainment-api-overlay.yaml
- group: other
  href: https://artifacts.apis.io/fabric-origin/overlays/fabric-origin-fandango-api-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/fabric-origin-fandango-api-overlay.yaml
- group: other
  href: https://artifacts.apis.io/fabric-origin/overlays/fabric-origin-images-api-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/fabric-origin-images-api-overlay.yaml
- group: other
  href: https://artifacts.apis.io/fabric-origin/overlays/fabric-origin-katch-media-api-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/fabric-origin-katch-media-api-overlay.yaml
- group: other
  href: https://artifacts.apis.io/fabric-origin/overlays/fabric-origin-metacritic-api-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/fabric-origin-metacritic-api-overlay.yaml
- group: other
  href: https://artifacts.apis.io/fabric-origin/overlays/fabric-origin-rabbit-recommendations-api-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/fabric-origin-rabbit-recommendations-api-overlay.yaml
- group: other
  href: https://artifacts.apis.io/fabric-origin/overlays/fabric-origin-rotten-tomatoes-api-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/fabric-origin-rotten-tomatoes-api-overlay.yaml
- group: other
  href: https://artifacts.apis.io/fabric-origin/overlays/fabric-origin-tv-grid-online-api-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/fabric-origin-tv-grid-online-api-overlay.yaml
- group: other
  href: https://artifacts.apis.io/fabric-origin/overlays/fabric-origin-video-analytics-api-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/fabric-origin-video-analytics-api-overlay.yaml
- group: other
  href: https://artifacts.apis.io/fabric-origin/overlays/fabric-origin-videos-api-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/fabric-origin-videos-api-overlay.yaml
created: '2025-03-01'
description: 'Fabric Origin is the entertainment metadata and market-intelligence arm of Fabric, the media software company formed from Xytech and IVA. Origin spans three products: Nexus, a family of 14 REST APIs serving movie, television, game and celebrity metadata plus images, trailers, TV listings, showtimes and licensed third-party ratings from Metacritic, Rotten Tomatoes, Common Sense Media and Katch; Studio, a JSON:API 1.1 metadata management platform with an SNS event surface; and Insights, streaming market intelligence across 1,000+ platforms and 249 countries. Fabric publishes machine-readable OpenAPI 3.1.1 for the whole Nexus surface, an llms.txt index at the company root, and two OAuth-governed hosted MCP servers — Origin Studio and Origin Insights — making it one of the more deliberately agent-ready entertainment-data providers in the catalog.'
finops:
- has_sources: true
  method: derived
  name: Fabric Origin Finops
  primary_unit: ''
  service_category: ''
  slug: fabric-origin-finops
  template: true
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/fabric-origin.png
layout: provider
mcp_servers:
- description: 'Fabric publishes two hosted Model Context Protocol servers inside the Origin product family: Origin Studio MCP (metadata records, catalog operations, availability) and Origin Insights MCP (streaming a'
  name: Fabric Origin MCP Servers
  slug: fabric-origin-mcp-servers
modified: '2026-09-07'
name: Fabric Origin
nav: Providers
network: true
overview: 'Fabric Origin publishes 20 API contracts indexed on the [APIs.io](https://apis.io/) network, including Entertainment API, Celebrity API, Video API, and 17 more. Tagged areas include Entertainment, Metadata, Movies, Television, and Games.


  The Fabric Origin catalog on APIs.io includes 1 event-driven AsyncAPI specification and 1 Spectral governance ruleset.


  Fabric Origin''s developer surface includes authentication, documentation, API reference, getting-started guide, signup flow, support, engineering blog, and 46 more developer resources.'
plans:
- name: Fabric Origin Plans Pricing
  plan_count: 1
  slug: fabric-origin-plans-pricing
random_paper: 12
rate_limits:
- limit_count: 5
  name: Fabric Origin Rate Limits
  slug: fabric-origin-rate-limits
rules:
- authorship: generated
  effective_rule_count: 84
  extends:
  - spectral:oas
  name: Fabric Origin API Rules
  rule_count: 43
  severity_counts:
    error: 34
    hint: 0
    info: 1
    warn: 8
  slug: fabric-origin-rules
scopes:
- name: Fabric Origin Scopes
  scope_count: 0
  slug: fabric-origin-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: strong
  composite: 61.7
  coverage:
    artifact_dirs: 32
    catalog_earned: 64.5
    catalog_earned_first_party: 20.0
    catalog_gap: 50.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 63.2
    contract_governance: 31.8
    contract_quality: 49.7
    developer_ergonomics: 66.1
    discoverability: 80.0
    operational_transparency: 71.1
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - united-states
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
  previous_composite: 61.7
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 14
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 35.3
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/fabric-origin/fabric-origin-2026-06-20T181001.png
security:
- kind: authentication
  name: Fabric Origin Authentication
  slug: fabric-origin-authentication
  summary_line: apiKey/http/oauth2 · 0 schemes
- kind: domain-security
  name: Fabric Origin Domain Security
  slug: fabric-origin-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
skill_count: 4
skills:
- name: fabric-origin-catalog-change-tracking
  slug: fabric-origin-catalog-change-tracking
- name: fabric-origin-mcp-agent-access
  slug: fabric-origin-mcp-agent-access
- name: fabric-origin-showtimes-and-ticketing
  slug: fabric-origin-showtimes-and-ticketing
- name: fabric-origin-title-lookup-and-enrichment
  slug: fabric-origin-title-lookup-and-enrichment
slug: fabric-origin
tags:
- Entertainment
- Metadata
- Movies
- Television
- Games
- Celebrities
- Trailers
- Image
- TV Listings
- Market Intelligence
- Media
- MCP
website: https://www.fabricdata.com/
---
