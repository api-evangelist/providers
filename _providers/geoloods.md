---
access_model:
  confidence: high
  gated: none
  gated_source:
  - onboarding
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  - rate-limits
  - security
  trial: false
  try_now: true
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: partial
    operation_distinctiveness: na
    pagination_ratio: false
    protected_resource_metadata: false
    rate_limit_signal: verified
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 30.3
  scored_at: '2026-11-06'
api_count: 1
apis:
- baseURL: https://api.geoloods.io/v2/
  baseurl_source: declared
  description: Machine signup
  name: Geoloods Agent API
  slug: geoloods-agent-api
- baseURL: https://api.geoloods.io/v2/
  baseurl_source: declared
  description: Bounding box search
  name: Geoloods Bbox API
  slug: geoloods-bbox-api
- baseURL: https://api.geoloods.io/v2/
  baseurl_source: declared
  description: Country list
  name: Geoloods Countries API
  slug: geoloods-countries-api
- baseURL: https://api.geoloods.io/v2/
  baseurl_source: declared
  description: Reverse geocoding. Default filter=smart prefers settlements and excludes HTL/RSRT/MALL. filter=simple is opt-in nearest feature. Hotels via /nearby.
  name: Geoloods Geocode API
  slug: geoloods-geocode-api
- baseURL: https://api.geoloods.io/v2/
  baseurl_source: declared
  description: Named places within a radius, including hotels/venues when you want them
  name: Geoloods Nearby API
  slug: geoloods-nearby-api
- baseURL: https://api.geoloods.io/v2/
  baseurl_source: declared
  description: Named-place search (gazetteer only; not streets, addresses, or venues)
  name: Geoloods Search API
  slug: geoloods-search-api
artifact_total: 17
common:
- group: company
  title: ''
  type: Blog
  url: https://geoloods.io/blog
- group: other
  href: https://artifacts.apis.io/geoloods/capabilities/geoloods-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/geoloods-capability-edges.yml
- group: other
  href: https://artifacts.apis.io/geoloods/overlays/geoloods-openapi-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/geoloods-openapi-overlay.yaml
- group: agent
  href: https://artifacts.apis.io/geoloods/mcp/geoloods-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/geoloods-mcp.yml
- group: company
  title: ''
  type: Website
  url: https://geoloods.io
- group: start
  title: ''
  type: DeveloperPortal
  url: https://geoloods.io/docs
- group: docs
  title: ''
  type: Documentation
  url: https://geoloods.io/docs
- group: docs
  title: ''
  type: APIReference
  url: https://geoloods.io/docs
- group: commercial
  title: ''
  type: Pricing
  url: https://geoloods.io/pricing
- group: start
  title: ''
  type: SignUp
  url: https://geoloods.io/auth
- group: commercial
  title: ''
  type: TermsOfService
  url: https://geoloods.io/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://geoloods.io/privacy
- group: operate
  title: ''
  type: StatusPage
  url: https://status.softwareloods.nl/798067685
- group: operate
  title: ''
  type: Support
  url: mailto:support@geoloods.io
- group: auth
  href: https://artifacts.apis.io/geoloods/security/geoloods-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/geoloods-domain-security.yml
- group: auth
  href: https://artifacts.apis.io/geoloods/authentication/geoloods-authentication.yml
  title: ''
  type: Authentication
  url: authentication/geoloods-authentication.yml
- group: design
  href: https://artifacts.apis.io/geoloods/conformance/geoloods-conformance.yml
  title: ''
  type: Conformance
  url: conformance/geoloods-conformance.yml
- group: design
  href: https://artifacts.apis.io/geoloods/lifecycle/geoloods-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/geoloods-lifecycle.yml
- group: operate
  href: https://artifacts.apis.io/geoloods/rate-limits/geoloods-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/geoloods-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/geoloods/plans/geoloods-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/geoloods-plans-pricing.yml
- group: agent
  href: https://artifacts.apis.io/geoloods/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-09-20'
description: A place-search and geocoding API that resolves named places (cities, towns, villages, parks, landmarks) to coordinates and rich location metadata over JSON/HTTPS. Covers 6.5M+ named places across 195 countries with coordinates, timezone, population, and country metadata. Agent-aware with machine signup and llms.txt index.
finops:
- has_sources: true
  method: derived
  name: Geoloods Finops
  primary_unit: requests
  service_category: ''
  slug: geoloods-finops
  template: false
layout: provider
mcp_servers:
- description: MCP server; 5 tools listed. A candidate, not confirmed as published by the provider.
  name: Geoloods MCP Server
  slug: geoloods-mcp-yml
modified: '2026-10-06'
name: Geoloods
nav: Providers
network: true
overview: 'Geoloods publishes 6 API contracts indexed on the [APIs.io](https://apis.io/) network, including Agent API, Bbox API, Countries API, and 3 more. Tagged areas include Geocoding, Place Search, Location, Coordinates, and Mapping.


  The Geoloods catalog on APIs.io includes 1 Spectral governance ruleset.


  Geoloods'' developer surface includes engineering blog, documentation, API reference, pricing, signup flow, support, authentication, and 14 more developer resources.'
plans:
- name: Geoloods Plans Pricing
  plan_count: 4
  slug: geoloods-plans-pricing
- name: Geoloods Price Estimates
  plan_count: 0
  slug: geoloods-price-estimates
random_paper: 20
rate_limits:
- limit_count: 0
  name: Geoloods Rate Limits
  slug: geoloods-rate-limits
rules:
- authorship: generated
  effective_rule_count: 108
  extends:
  - spectral:oas
  name: Geoloods API Rules
  rule_count: 67
  severity_counts:
    error: 65
    hint: 0
    info: 1
    warn: 1
  slug: geoloods-rules
score:
  band: developing
  composite: 43.1
  coverage:
    artifact_dirs: 24
    catalog_earned: 54.5
    catalog_earned_first_party: 12.0
    catalog_gap: 60.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -7.3
  facets:
    access_clarity: 61.8
    contract_governance: 18.2
    contract_quality: 54.6
    developer_ergonomics: 33.9
    discoverability: 69.6
    operational_transparency: 7.9
  previous_composite: 50.4
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 100.0
      total: 6
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 20.6
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/geoloods/geoloods-2026-10-11T104814.png
security:
- kind: authentication
  name: Geoloods Authentication
  slug: geoloods-authentication
  summary_line: apiKey · 2 schemes
- kind: domain-security
  name: Geoloods Domain Security
  slug: geoloods-domain-security
  summary_line: TLSv1.3 · DNSSEC
skill_count: 3
skills:
- name: Sign up as an agent and search for a place
  slug: geoloods-agent-signup-and-search
- name: List places in an area
  slug: geoloods-places-in-an-area
- name: Reverse geocode a coordinate
  slug: geoloods-reverse-geocode-a-coordinate
slug: geoloods
tags:
- Geocoding
- Place Search
- Location
- Coordinates
- Mapping
- Geospatial
- Agents
- OpenAPI
- Llms.txt
website: https://geoloods.io
---
