---
access_model:
  confidence: medium
  label: Anonymous read-only content API; no registration, no plans, no price
  onboarding: unknown
  pricing: free
  public: true
  source:
  - probe
  trial: false
  try_now: true
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
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
  score: 22.8
  scored_at: '2026-11-06'
api_count: 2
apis:
- description: 'The public WordPress REST API (wp-json) of the Cornerstone Building Brands website at www.cornerstonebuildingbrands.com: the route index of the site''s content management system, catalogued as one site'
  name: Cornerstone Building Brands Website (WordPress REST)
  slug: cornerstonebuildingbrands-com-website-wordpress-rest
- description: A live remote Model Context Protocol server served from the corporate WordPress estate under the `mcp` REST namespace. Two MCP routes are advertised in the route index — mcp-oauth-server and mcp-adapt
  name: Cornerstone Building Brands MCP Server (WordPress MCP Adapter)
  slug: cornerstone-building-brands-mcp
artifact_total: 11
common:
- group: commercial
  href: https://artifacts.apis.io/cornerstone-building-brands/finops/cornerstone-building-brands-finops.yml
  title: ''
  type: FinOps
  url: finops/cornerstone-building-brands-finops.yml
- group: company
  title: ''
  type: Website
  url: https://www.cornerstonebuildingbrands.com
- group: company
  title: ''
  type: Newsroom
  url: https://www.cornerstonebuildingbrands.com/news-and-updates
- group: company
  title: ''
  type: BlogRSS
  url: https://www.cornerstonebuildingbrands.com/feed
- group: other
  title: ''
  type: Leadership
  url: https://www.cornerstonebuildingbrands.com/leadership-team
- group: operate
  title: ''
  type: Support
  url: https://www.cornerstonebuildingbrands.com/contact-us
- group: company
  title: ''
  type: Careers
  url: https://www.cornerstonebuildingbrands.com/careers
- group: start
  title: ''
  type: Login
  url: https://portal.cornerstonebuildingbrands.com/
- group: start
  title: ''
  type: SignUp
  url: https://www.cornerstonebuildingbrands.com/portalaccess
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.cornerstonebuildingbrands.com/legal
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.cornerstonebuildingbrands.com/privacy-policy
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/cornerstone-building-brands
- group: agent
  href: https://artifacts.apis.io/cornerstone-building-brands/well-known/cornerstone-building-brands-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/cornerstone-building-brands-well-known.yml
- group: agent
  href: https://artifacts.apis.io/cornerstone-building-brands/mcp/cornerstone-building-brands-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/cornerstone-building-brands-mcp.yml
- group: build
  href: https://artifacts.apis.io/cornerstone-building-brands/mcp/cornerstone-building-brands-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/cornerstone-building-brands-tool-crosswalk.yml
- group: auth
  href: https://artifacts.apis.io/cornerstone-building-brands/authentication/cornerstone-building-brands-authentication.yml
  title: ''
  type: Authentication
  url: authentication/cornerstone-building-brands-authentication.yml
- group: auth
  href: https://artifacts.apis.io/cornerstone-building-brands/scopes/cornerstone-building-brands-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/cornerstone-building-brands-scopes.yml
- group: design
  href: https://artifacts.apis.io/cornerstone-building-brands/conformance/cornerstone-building-brands-conformance.yml
  title: ''
  type: Conformance
  url: conformance/cornerstone-building-brands-conformance.yml
- group: design
  href: https://artifacts.apis.io/cornerstone-building-brands/errors/cornerstone-building-brands-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/cornerstone-building-brands-problem-types.yml
- group: design
  href: https://artifacts.apis.io/cornerstone-building-brands/conventions/cornerstone-building-brands-conventions.yml
  title: ''
  type: Conventions
  url: conventions/cornerstone-building-brands-conventions.yml
- group: design
  href: https://artifacts.apis.io/cornerstone-building-brands/data-model/cornerstone-building-brands-data-model.yml
  title: ''
  type: DataModel
  url: data-model/cornerstone-building-brands-data-model.yml
- group: design
  href: https://artifacts.apis.io/cornerstone-building-brands/lifecycle/cornerstone-building-brands-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/cornerstone-building-brands-lifecycle.yml
- group: agent
  href: https://artifacts.apis.io/cornerstone-building-brands/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  href: https://artifacts.apis.io/cornerstone-building-brands/llms/cornerstone-building-brands-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/cornerstone-building-brands-llms.txt
- group: build
  href: https://artifacts.apis.io/cornerstone-building-brands/packages/cornerstone-building-brands-packages.yml
  title: ''
  type: Packages
  url: packages/cornerstone-building-brands-packages.yml
- group: commercial
  href: https://artifacts.apis.io/cornerstone-building-brands/plans/cornerstone-building-brands-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/cornerstone-building-brands-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/cornerstone-building-brands/rate-limits/cornerstone-building-brands-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/cornerstone-building-brands-rate-limits.yml
- group: auth
  href: https://artifacts.apis.io/cornerstone-building-brands/security/cornerstone-building-brands-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/cornerstone-building-brands-domain-security.yml
- group: other
  href: https://artifacts.apis.io/cornerstone-building-brands/regulatory/cornerstone-building-brands-regulatory-posture.yml
  title: ''
  type: RegulatoryPosture
  url: regulatory/cornerstone-building-brands-regulatory-posture.yml
- group: commercial
  title: ''
  type: GlobalPrivacyControl
  url: https://www.cornerstonebuildingbrands.com/privacy-policy
- group: other
  title: ''
  type: DataSubjectRequest
  url: https://www.cornerstonebuildingbrands.com/privacy-request-form
created: '2026-04-19'
description: 'Cornerstone Building Brands, Inc. is a Fortune 1000 manufacturer of exterior building products in North America — vinyl siding and accessories, metal and rainware, fence and railing, windows and entry doors, and metal roofs, walls and buildings — sold under brands including Ply Gem, Simonton and Mastic through dealers, distributors and builders rather than as software. It operates no developer program and publishes no API documentation, SDK or developer portal: the hosts its earlier catalog record named, developer.cornerstonebuildingbrands.com and api.cornerstonebuildingbrands.com, do not resolve. Its machine-readable surface is what the corporate WordPress estate on www.cornerstonebuildingbrands.com exposes — an anonymously readable WordPress REST content API (press releases, industry pages, leadership profiles, pages, media, taxonomies and search) and, notably for a manufacturer, a live remote Model Context Protocol server published through the WordPress MCP Adapter, advertised
  by real RFC 8414 authorization-server metadata and RFC 9728 protected-resource metadata, with tools/list OAuth-gated. The company''s partner-facing integration surface — orders, ASNs, warranty claims — sits behind the Windows & Doors Customer Portal, which signs in with Microsoft Entra ID over an Azure API Management gateway whose developer portal is unpublished.'
finops:
- has_sources: true
  method: generated
  name: Cornerstone Building Brands Finops
  primary_unit: ''
  service_category: Building Products Manufacturer
  slug: cornerstone-building-brands-finops
  template: false
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/cornerstone-building-brands.png
layout: provider
mcp_servers:
- description: Cornerstone Building Brands serves a live remote Model Context Protocol server from its corporate WordPress site. It appears in no MCP registry and in no company documentation — the company has no dev
  name: Cornerstone Building Brands MCP Server
  slug: cornerstone-building-brands
modified: '2026-09-19'
name: Cornerstone Building Brands
nav: Providers
network: true
overview: 'Cornerstone Building Brands is listed with 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Building Products, Construction, Manufacturing, Building Materials, and MCP.


  Cornerstone Building Brands'' developer surface includes support, signup flow, authentication, and 28 more developer resources.'
plans:
- name: Cornerstone Building Brands Plans Pricing
  plan_count: 0
  slug: cornerstone-building-brands-plans-pricing
random_paper: 12
rate_limits:
- limit_count: 0
  name: Cornerstone Building Brands Rate Limits
  slug: cornerstone-building-brands-rate-limits
scopes:
- name: Cornerstone Building Brands Scopes
  scope_count: 1
  slug: cornerstone-building-brands-scopes
  summary_line: 1 scope · authorizationCode
score:
  band: emerging
  composite: 24.6
  coverage:
    artifact_dirs: 21
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -0.9
  facets:
    access_clarity: 34.2
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 23.2
    discoverability: 68.3
    operational_transparency: 0.0
  previous_composite: 25.5
  provenance:
    conformance: first-party
    mcp: site-plugin
    skills: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 42.2
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/cornerstone-building-brands/cornerstone-building-brands-2026-06-20T175036.png
security:
- kind: authentication
  name: Cornerstone Building Brands Authentication
  slug: cornerstone-building-brands-authentication
  summary_line: none/oauth2 · 2 schemes
- kind: domain-security
  name: Cornerstone Building Brands Domain Security
  slug: cornerstone-building-brands-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
skill_count: 2
skills:
- name: Look up Cornerstone Building Brands leadership, industries and corporate pages
  slug: cornerstone-building-brands-company-profile-lookup
- name: Read the Cornerstone Building Brands news feed
  slug: cornerstone-building-brands-read-news
slug: cornerstone-building-brands
tags:
- Building Products
- Construction
- Manufacturing
- Building Materials
- MCP
- WordPress
- News
website: https://www.cornerstonebuildingbrands.com
---
