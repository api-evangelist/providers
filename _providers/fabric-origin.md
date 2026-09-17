---
access_model:
  confidence: medium
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  - security
  trial: false
  try_now: true
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
    openapi_examples: false
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 52.7
  scored_at: '2026-09-16'
agentic_access:
- acting_count: 12
  human_in_the_loop: 0
  name: Fabric Origin Agentic Access
  operation_count: 121
  slug: fabric-origin-agentic-access
  summary_line: 121 operations · 12 acting
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
artifact_total: 34
asyncapis:
- description: ''
  name: Fabric Origin Events Webhooks
  slug: fabric-origin-events-webhooks
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
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
  href: https://raw.githubusercontent.com/api-evangelist/fabric-origin/refs/heads/main/capabilities/fabric-origin-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/fabric-origin-capability-edges.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/fabric-origin/refs/heads/main/agentic-access/fabric-origin-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/fabric-origin-agentic-access.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/fabric-origin/refs/heads/main/security/fabric-origin-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/fabric-origin-domain-security.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/fabric-origin/refs/heads/main/authentication/fabric-origin-authentication.yml
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
  href: https://raw.githubusercontent.com/api-evangelist/fabric-origin/refs/heads/main/changelog/fabric-origin-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/fabric-origin-changelog.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/fabric-origin/refs/heads/main/llms/fabric-origin-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/fabric-origin-llms.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/fabric-origin/refs/heads/main/mcp/fabric-origin-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/fabric-origin-mcp.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/fabric-origin/refs/heads/main/mcp/fabric-origin-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/fabric-origin-tool-crosswalk.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/fabric-origin/refs/heads/main/well-known/fabric-origin-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/fabric-origin-well-known.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/fabric-origin/refs/heads/main/packages/fabric-origin-packages.yml
  title: ''
  type: Packages
  url: packages/fabric-origin-packages.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/fabric-origin/refs/heads/main/conventions/fabric-origin-conventions.yml
  title: ''
  type: Conventions
  url: conventions/fabric-origin-conventions.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/fabric-origin/refs/heads/main/conformance/fabric-origin-conformance.yml
  title: ''
  type: Conformance
  url: conformance/fabric-origin-conformance.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/fabric-origin/refs/heads/main/conformance/fabric-origin-conformance.yml
  title: ''
  type: Compliance
  url: conformance/fabric-origin-conformance.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/fabric-origin/refs/heads/main/errors/fabric-origin-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/fabric-origin-problem-types.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/fabric-origin/refs/heads/main/lifecycle/fabric-origin-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/fabric-origin-lifecycle.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/fabric-origin/refs/heads/main/scopes/fabric-origin-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/fabric-origin-scopes.yml
- group: start
  href: https://raw.githubusercontent.com/api-evangelist/fabric-origin/refs/heads/main/sandbox/fabric-origin-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/fabric-origin-sandbox.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/fabric-origin/refs/heads/main/data-model/fabric-origin-data-model.yml
  title: ''
  type: DataModel
  url: data-model/fabric-origin-data-model.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/fabric-origin/refs/heads/main/asyncapi/fabric-origin-events-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/fabric-origin-events-webhooks.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/fabric-origin/refs/heads/main/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/fabric-origin/refs/heads/main/plans/fabric-origin-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/fabric-origin-plans-pricing.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/fabric-origin/refs/heads/main/rate-limits/fabric-origin-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/fabric-origin-rate-limits.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/fabric-origin/refs/heads/main/finops/fabric-origin-finops.yml
  title: ''
  type: FinOps
  url: finops/fabric-origin-finops.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/fabric-origin/refs/heads/main/overlays/fabric-origin-captions-translations-api-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/fabric-origin-captions-translations-api-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/fabric-origin/refs/heads/main/overlays/fabric-origin-celebrity-api-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/fabric-origin-celebrity-api-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/fabric-origin/refs/heads/main/overlays/fabric-origin-common-metadata-api-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/fabric-origin-common-metadata-api-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/fabric-origin/refs/heads/main/overlays/fabric-origin-common-sense-media-api-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/fabric-origin-common-sense-media-api-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/fabric-origin/refs/heads/main/overlays/fabric-origin-entertainment-api-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/fabric-origin-entertainment-api-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/fabric-origin/refs/heads/main/overlays/fabric-origin-fandango-api-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/fabric-origin-fandango-api-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/fabric-origin/refs/heads/main/overlays/fabric-origin-images-api-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/fabric-origin-images-api-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/fabric-origin/refs/heads/main/overlays/fabric-origin-katch-media-api-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/fabric-origin-katch-media-api-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/fabric-origin/refs/heads/main/overlays/fabric-origin-metacritic-api-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/fabric-origin-metacritic-api-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/fabric-origin/refs/heads/main/overlays/fabric-origin-rabbit-recommendations-api-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/fabric-origin-rabbit-recommendations-api-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/fabric-origin/refs/heads/main/overlays/fabric-origin-rotten-tomatoes-api-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/fabric-origin-rotten-tomatoes-api-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/fabric-origin/refs/heads/main/overlays/fabric-origin-tv-grid-online-api-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/fabric-origin-tv-grid-online-api-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/fabric-origin/refs/heads/main/overlays/fabric-origin-video-analytics-api-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/fabric-origin-video-analytics-api-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/fabric-origin/refs/heads/main/overlays/fabric-origin-videos-api-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/fabric-origin-videos-api-overlay.yaml
created: '2025-03-01'
description: 'Fabric Origin is the entertainment metadata and market-intelligence arm of Fabric, the media software company formed from Xytech and IVA. Origin spans three products: Nexus, a family of 14 REST APIs serving movie, television, game and celebrity metadata plus images, trailers, TV listings, showtimes and licensed third-party ratings from Metacritic, Rotten Tomatoes, Common Sense Media and Katch; Studio, a JSON:API 1.1 metadata management platform with an SNS event surface; and Insights, streaming market intelligence across 1,000+ platforms and 249 countries. Fabric publishes machine-readable OpenAPI 3.1.1 for the whole Nexus surface, an llms.txt index at the company root, and two OAuth-governed hosted MCP servers — Origin Studio and Origin Insights — making it one of the more deliberately agent-ready entertainment-data providers in the catalog.'
finops:
- name: Fabric Origin Finops
  service_category: API
  slug: fabric-origin-finops
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
overview: 'Fabric Origin publishes 17 APIs on the [APIs.io](https://apis.io/) network, including Entertainment API, Celebrity API, Video API, and 14 more. Tagged areas include Entertainment, Metadata, Movies, Television, and Games.


  The Fabric Origin catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Fabric Origin''s developer surface includes authentication, documentation, API reference, getting-started guide, signup flow, support, engineering blog, and 46 more developer resources.'
plans:
- name: Fabric Origin Plans Pricing
  plan_count: 0
  slug: fabric-origin-plans-pricing
random_paper: 10
rate_limits:
- limit_count: 5
  name: Fabric Origin Rate Limits
  slug: fabric-origin-rate-limits
scopes:
- name: Fabric Origin Scopes
  scope_count: 0
  slug: fabric-origin-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: strong
  composite: 55.1
  coverage:
    artifact_dirs: 25
    catalog_earned: 52.0
    catalog_earned_first_party: 12.0
    catalog_gap: 63.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -0.7
  facets:
    access_clarity: 50.0
    contract_governance: 18.2
    contract_quality: 54.4
    developer_ergonomics: 66.1
    discoverability: 75.9
    operational_transparency: 71.1
  previous_composite: 55.8
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
  schema_version: 0.22.0
  scored_at: '2026-09-16'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://raw.githubusercontent.com/api-evangelist/fabric-origin/refs/heads/main/screenshots/fabric-origin-2026-06-20T181001.png
security:
- kind: authentication
  name: Fabric Origin Authentication
  slug: fabric-origin-authentication
  summary_line: apiKey/http/oauth2 · 0 schemes
- kind: domain-security
  name: Fabric Origin Domain Security
  slug: fabric-origin-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
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
