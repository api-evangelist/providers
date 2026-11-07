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
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 20.0
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 124
  human_in_the_loop: 0
  name: Starfish Space Agentic Access
  operation_count: 225
  slug: starfish-space-agentic-access
  summary_line: 225 operations · 124 acting
api_count: 2
apis:
- description: A live Model Context Protocol (MCP) server exposed by Starfish Space at https://www.starfishspace.com/wp-json/mcp/mcp-oauth-server, served through the WordPress MCP adapter. Access is OAuth 2.1 protec
  name: Starfish Space MCP Server
  slug: starfish-space-mcp-server
- description: 'The public WordPress REST API (wp-json) of the Starfish Space website at www.starfishspace.com: the route index of the site''s content management system, catalogued as one site surface rather than as s'
  name: Starfish Space Website (WordPress REST)
  slug: starfishspace-com-website-wordpress-rest
artifact_total: 22
collections:
- collection_type: open
  name: API Collection
  slug: open-starfish-space-wordpress-routes
common:
- group: agent
  href: https://artifacts.apis.io/starfish-space/agentic-access/starfish-space-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/starfish-space-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/starfish-space/security/starfish-space-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/starfish-space-domain-security.yml
- group: auth
  href: https://artifacts.apis.io/starfish-space/authentication/starfish-space-authentication.yml
  title: ''
  type: Authentication
  url: authentication/starfish-space-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://www.starfishspace.com/
- group: company
  title: ''
  type: Blog
  url: https://www.starfishspace.com/news/
- group: company
  title: ''
  type: BlogRSS
  url: https://www.starfishspace.com/feed/
- group: operate
  title: ''
  type: Support
  url: https://www.starfishspace.com/contact/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.starfishspace.com/privacy-policy/
- group: company
  title: ''
  type: About
  url: https://www.starfishspace.com/company/
- group: company
  title: ''
  type: Careers
  url: https://www.starfishspace.com/careers/
- group: other
  title: ''
  type: Products
  url: https://www.starfishspace.com/the-otter/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/starfish-space/
- group: company
  title: ''
  type: Twitter
  url: https://twitter.com/StarfishSpace/
- group: agent
  href: https://artifacts.apis.io/starfish-space/mcp/starfish-space-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/starfish-space-mcp.yml
- group: agent
  href: https://artifacts.apis.io/starfish-space/well-known/starfish-space-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/starfish-space-well-known.yml
- group: auth
  href: https://artifacts.apis.io/starfish-space/scopes/starfish-space-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/starfish-space-scopes.yml
- group: design
  href: https://artifacts.apis.io/starfish-space/conventions/starfish-space-conventions.yml
  title: ''
  type: Conventions
  url: conventions/starfish-space-conventions.yml
- group: design
  href: https://artifacts.apis.io/starfish-space/errors/starfish-space-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/starfish-space-problem-types.yml
- group: design
  href: https://artifacts.apis.io/starfish-space/lifecycle/starfish-space-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/starfish-space-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/starfish-space/conformance/starfish-space-conformance.yml
  title: ''
  type: Conformance
  url: conformance/starfish-space-conformance.yml
- group: design
  href: https://artifacts.apis.io/starfish-space/data-model/starfish-space-data-model.yml
  title: ''
  type: DataModel
  url: data-model/starfish-space-data-model.yml
- group: agent
  href: https://artifacts.apis.io/starfish-space/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  href: https://artifacts.apis.io/starfish-space/llms/starfish-space-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/starfish-space-llms.txt
- group: other
  href: https://artifacts.apis.io/starfish-space/overlays/starfish-space-wordpress-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/starfish-space-wordpress-overlay.yaml
created: '2026-08-02'
description: Starfish Space is a satellite-servicing company founded in 2019 by Trevor Bennett and Austin Link and headquartered in the Seattle, Washington area (Tukwila). It builds Otter, a small, low-cost, electrically propelled servicing vehicle that performs autonomous rendezvous, proximity operations and docking (RPOD) with satellites that were never designed to be serviced — extending their life, relocating them, or disposing of them at end of mission. Its Otter Pup demonstration missions target the first-ever commercial satellite docking in low Earth orbit, and the company has been awarded a $54.5M U.S. Space Force contract for a dedicated Otter servicing vehicle. Starfish Space publishes no developer product API; the machine-readable surface catalogued here is the public WordPress REST API and the OAuth-protected Model Context Protocol (MCP) server served from starfishspace.com.
image: https://www.starfishspace.com/wp-content/uploads/2023/06/starfishspace-logo-fullcolor.png
json_schemas:
- name: category
  property_count: 10
  slug: starfish-space-categories.schema
- name: comment
  property_count: 17
  slug: starfish-space-comments.schema
- name: attachment
  property_count: 33
  slug: starfish-space-media.schema
- name: page
  property_count: 26
  slug: starfish-space-pages.schema
- name: search-result
  property_count: 5
  slug: starfish-space-search.schema
- name: status
  property_count: 8
  slug: starfish-space-statuses.schema
- name: tag
  property_count: 8
  slug: starfish-space-tags.schema
- name: taxonomy
  property_count: 11
  slug: starfish-space-taxonomies.schema
- name: type
  property_count: 16
  slug: starfish-space-types.schema
- name: user
  property_count: 19
  slug: starfish-space-users.schema
layout: provider
mcp_servers:
- description: Starfish Space serves a live Model Context Protocol server from its own host, via the WordPress MCP adapter. The MCP namespace, the OAuth 2.1 authorization-server metadata and the protected-resource m
  name: Starfish Space MCP Server
  slug: starfish-space-mcp-yml
modified: '2026-08-02'
name: Starfish Space
nav: Providers
network: true
overview: 'Starfish Space is listed with 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Aerospace, Space, Satellite, and Satellite Servicing.


  The Starfish Space catalog on APIs.io includes 1 Spectral governance ruleset.


  Starfish Space''s developer surface includes authentication, engineering blog, support, and 21 more developer resources.'
random_paper: 21
rules:
- authorship: generated
  effective_rule_count: 106
  extends:
  - spectral:oas
  name: Starfish Space API Rules
  rule_count: 65
  severity_counts:
    error: 57
    hint: 0
    info: 1
    warn: 7
  slug: starfish-space-rules
scopes:
- name: Starfish Space Scopes
  scope_count: 1
  slug: starfish-space-scopes
  summary_line: 1 scope · authorizationCode
score:
  band: emerging
  composite: 18.8
  coverage:
    artifact_dirs: 25
    catalog_earned: 36.5
    catalog_earned_first_party: 0.0
    catalog_gap: 78.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -1.0
  facets:
    access_clarity: 10.5
    contract_governance: 18.2
    contract_quality: 1.7
    developer_ergonomics: 25.6
    discoverability: 66.7
    operational_transparency: 0.0
  previous_composite: 19.8
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 1
      marker_coverage: 100.0
      total: 1
    mcp: site-plugin
    skills: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 30.4
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/starfish-space/starfish-space-2026-09-02T160802.png
security:
- kind: authentication
  name: Starfish Space Authentication
  slug: starfish-space-authentication
  summary_line: apiKey/http · 2 schemes
- kind: domain-security
  name: Starfish Space Domain Security
  slug: starfish-space-domain-security
  summary_line: TLSv1.3
skill_count: 3
skills:
- name: Connect to the Starfish Space MCP server
  slug: starfish-space-connect-mcp
- name: Inventory Starfish Space site content and media
  slug: starfish-space-inventory-site-content
- name: Read Starfish Space news and press releases
  slug: starfish-space-read-news
slug: starfish-space
tags:
- Company
- Aerospace
- Space
- Satellite
- Satellite Servicing
- Spacecraft
- Space Robotics
- Defense
- Content Management
- MCP
website: https://www.starfishspace.com/
---
