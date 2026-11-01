---
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: unknown
    agentic_access: unknown
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    openapi_examples: verified
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 42.8
  scored_at: '2026-10-31'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Latlng Work Agentic Access
  operation_count: 4
  slug: latlng-work-agentic-access
  summary_line: 4 operations
api_count: 1
apis:
- baseURL: https://api.latlng.work
  baseurl_source: declared
  description: Convert addresses and place names to coordinates, and coordinates to addresses.
  name: latlng-work Geocoding API
  slug: latlng-work-geocoding-api
- baseURL: https://api.latlng.work
  baseurl_source: declared
  description: Search and discover OpenStreetMap points of interest.
  name: latlng-work Places API
  slug: latlng-work-places-api
artifact_total: 12
common:
- group: design
  href: https://artifacts.apis.io/latlng-work/data-model/latlng-work-data-model.yml
  title: ''
  type: DataModel
  url: data-model/latlng-work-data-model.yml
- group: agent
  href: https://artifacts.apis.io/latlng-work/agentic-access/latlng-work-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/latlng-work-agentic-access.yml
- group: design
  href: https://artifacts.apis.io/latlng-work/rules/latlng-work-rules.yml
  title: ''
  type: Spectral
  url: rules/latlng-work-rules.yml
- group: design
  href: https://artifacts.apis.io/latlng-work/vocabulary/latlng-work-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/latlng-work-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/latlng-work/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: auth
  href: https://artifacts.apis.io/latlng-work/authentication/latlng-work-authentication.yml
  title: ''
  type: Authentication
  url: authentication/latlng-work-authentication.yml
- group: design
  href: https://artifacts.apis.io/latlng-work/errors/latlng-work-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/latlng-work-problem-types.yml
- group: design
  href: https://artifacts.apis.io/latlng-work/conformance/latlng-work-conformance.yml
  title: ''
  type: Conformance
  url: conformance/latlng-work-conformance.yml
- group: build
  href: https://artifacts.apis.io/latlng-work/mcp/latlng-work-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/latlng-work-tool-crosswalk.yml
- group: agent
  href: https://artifacts.apis.io/latlng-work/mcp/latlng-work-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/latlng-work-mcp.yml
- group: auth
  href: https://artifacts.apis.io/latlng-work/well-known/latlng-work-mcp-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/latlng-work-mcp-security.txt
- group: agent
  href: https://artifacts.apis.io/latlng-work/well-known/latlng-work-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/latlng-work-well-known.yml
- group: other
  href: https://artifacts.apis.io/latlng-work/hosts/latlng-work-hosts.yml
  title: ''
  type: Hosts
  url: hosts/latlng-work-hosts.yml
- group: other
  href: https://artifacts.apis.io/latlng-work/vendors/latlng-work-vendors.yml
  title: ''
  type: Vendors
  url: vendors/latlng-work-vendors.yml
- group: build
  href: https://artifacts.apis.io/latlng-work/packages/latlng-work-packages.yml
  title: ''
  type: SDKs
  url: packages/latlng-work-packages.yml
- group: build
  href: https://artifacts.apis.io/latlng-work/packages/latlng-work-packages.yml
  title: ''
  type: Packages
  url: packages/latlng-work-packages.yml
- group: auth
  href: https://artifacts.apis.io/latlng-work/security/latlng-work-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/latlng-work-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://latlng.work/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://dash.latlng.work
- group: docs
  title: ''
  type: Documentation
  url: https://www.latlng.work/docs
- group: docs
  title: ''
  type: APIReference
  url: https://www.latlng.work/docs
- group: start
  title: ''
  type: GettingStarted
  url: https://www.latlng.work/docs
- group: operate
  title: ''
  type: Support
  url: https://www.latlng.work/contact
- group: commercial
  title: ''
  type: Pricing
  url: https://www.latlng.work/#pricing
- group: start
  title: ''
  type: SignUp
  url: https://dash.latlng.work
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.latlng.work/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.latlng.work/privacy
created: '2026-10-30'
description: LatLng provides a free, developer-friendly suite of geocoding, reverse geocoding, places search, and map tile APIs. It offers up to 3,000 free requests per day, with simple HTTP endpoints that return JSON data for converting addresses to latitude/longitude, discovering points of interest, and rendering vector or raster map tiles. The service is built on OpenStreetMap data and aims to be fast, reliable, and easy to integrate into any application, supporting both web and mobile platforms. Developers can obtain an API key via the dashboard and start using the APIs without cost, making it ideal for prototypes, small projects, and learning purposes.
image: https://dash.latlng.work/favicon-32x32.png
json_schemas:
- name: GeoJsonFeatureCollection
  property_count: 0
  slug: latlng-work-geo-json-feature-collection
- name: PlacesResponse
  property_count: 0
  slug: latlng-work-places-response
layout: provider
mcp_servers:
- description: Remote MCP server at mcp.latlng.work requiring an API key.
  name: latlng-work MCP Server
  slug: latlng-work-mcp-yml
modified: '2026-10-30'
name: latlng-work
nav: Providers
network: true
overview: 'latlng-work publishes 2 API contracts indexed on the [APIs.io](https://apis.io/) network: Geocoding API and Places API. Tagged areas include Company, Geocoding, Mapping, API, and Location.


  The latlng-work catalog on APIs.io includes 1 Spectral governance ruleset.


  latlng-work''s developer surface includes authentication, documentation, API reference, getting-started guide, support, pricing, signup flow, and 20 more developer resources.'
random_paper: 10
rate_limits:
- limit_count: 0
  name: Latlng Work Rate Limits
  slug: latlng-work-rate-limits
rules:
- authorship: generated
  effective_rule_count: 52
  extends:
  - spectral:oas
  name: latlng-work API Rules
  rule_count: 11
  severity_counts:
    error: 9
    hint: 0
    info: 1
    warn: 1
  slug: latlng-work-rules
scopes:
- name: Latlng Work Scopes
  scope_count: 0
  slug: latlng-work-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: strong
  composite: 55.6
  coverage:
    artifact_dirs: 24
    catalog_earned: 66.7
    catalog_earned_first_party: 0.0
    catalog_gap: 48.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 44.7
    contract_governance: 79.1
    contract_quality: 51.1
    developer_ergonomics: 68.3
    discoverability: 65.0
    operational_transparency: 10.5
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 34.3
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Latlng Work Authentication
  slug: latlng-work-authentication
  summary_line: 2 schemes
- kind: domain-security
  name: Latlng Work Domain Security
  slug: latlng-work-domain-security
  summary_line: TLSv1.3 · DMARC
skill_count: 1
skills:
- name: geocoding
  slug: latlng-work-geocoding
slug: latlng-work
tags:
- Company
- Geocoding
- Mapping
- API
- Location
website: https://latlng.work/
---
