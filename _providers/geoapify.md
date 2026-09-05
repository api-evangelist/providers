---
access_model:
  confidence: medium
  label: Freemium
  onboarding: unknown
  pricing: freemium
  public: false
  source:
  - plans
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: false
    consent_identity: false
    delegated_identity: false
    dry_run_mode: na
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: na
    mcp_server: documented
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 24.0
  scored_at: '2026-09-04'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Geoapify Agentic Access
  operation_count: 1
  slug: geoapify-agentic-access
  summary_line: 1 operation
api_count: 1
apis:
- description: Retrieve map tiles for various types and styles.
  name: Map Tiles API
  slug: map-tiles
- description: Generate static map images for embedding in applications.
  name: Static Maps API
  slug: static-maps
- description: Convert geographic coordinates into addresses.
  name: Reverse Geocoding API
  slug: reverse-geocoding
- description: Address autocomplete suggestions for search fields.
  name: Address Autocomplete API
  slug: address-autocomplete
- description: Identify the location of an IP address.
  name: IP Geolocation API
  slug: ip-geolocation
- description: Provides routing directions between multiple points.
  name: Routing API
  slug: routing
- description: Discover places based on various categories and parameters.
  name: Places API
  slug: places
- description: Retrieve boundary data for administrative regions.
  name: Boundaries API
  slug: boundaries
- description: Generate isolines to represent reachable areas.
  name: Isoline API
  slug: isoline
- baseURL: https://maps.geoapify.com/maptiles
  baseurl_source: declared
  description: The Geocode API from Geoapify — 1 operation(s) for geocode.
  name: Geoapify Geocode API
  slug: geoapify-geocode-api
artifact_total: 36
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Geoapify Forward Geocoding API
  slug: open-geoapify-forward-geocoding-api
- collection_type: open
  name: Geoapify Forward Geocoding Geocode API
  slug: open-geoapify-geocode-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/geoapify-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/geoapify-domain-security.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/geoapify
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/geoapify
- group: company
  title: ''
  type: Website
  url: https://www.geoapify.com/
- group: docs
  title: ''
  type: Documentation
  url: https://apidocs.geoapify.com/
- group: start
  title: ''
  type: Signup
  url: https://myprojects.geoapify.com/register
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.geoapify.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.geoapify.com/privacy
- group: agent
  title: ''
  type: LlmsText
  url: https://apidocs.geoapify.com/llms.txt
- group: company
  title: ''
  type: Blog
  url: https://www.geoapify.com/rss.xml
- group: agent
  title: ''
  type: MCPServer
  url: https://api.geoapify.com/v1/mcp
- group: docs
  title: ''
  type: MCPDocumentation
  url: https://www.geoapify.com/mcp/
created: '2024-01-01'
description: Geoapify Location Platform APIs for location-based services and mapping solutions.
features:
- 'Free: 3K credits/day, 5 RPS, limited commercial use'
- 'API 10: $59/mo, 10K credits/day, 12 RPS'
- 'API 25: $109/mo, 25K credits/day, 15 RPS'
- 'API 50: $179/mo, 50K credits/day, 20 RPS'
- 'API 100: $299/mo, 100K credits/day, 25 RPS'
- 'API 250: $609/mo, 250K credits/day, 30 RPS'
- 'Custom from $860/mo: unmetered, dedicated endpoint'
- Geocoding API (forward + reverse)
- Routing API (driving, walking, cycling, truck)
- Isochrones up to 15-120 min by tier
- Place Details API
- Map Tiles API
- Address Autocomplete
- Static Maps API
- Boundaries API
- OpenStreetMap-based data with global coverage
finops:
- name: Geoapify Finops
  service_category: Maps
  slug: geoapify-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/geoapify.png
json_structures:
- name: Geoapify Structure
  property_count: 0
  slug: geoapify-structure
layout: provider
mcp_servers:
- description: ''
  name: MCP Server
  slug: mcp-server
modified: '2026-07-12'
name: Geoapify
nav: Providers
network: true
overview: 'Geoapify publishes 1 API on the [APIs.io](https://apis.io/) network: Geocode API. Tagged areas include Geocoding, Geospatial, Location, and Maps.


  Geoapify''s developer surface includes documentation, signup flow, engineering blog, and 10 more developer resources.'
plans:
- name: Geoapify Plans Pricing
  plan_count: 7
  slug: geoapify-plans-pricing
random_paper: 12
rate_limits:
- limit_count: 6
  name: Geoapify Rate Limits
  slug: geoapify-rate-limits
score:
  band: emerging
  composite: 25.4
  coverage:
    artifact_dirs: 13
    catalog_earned: 36.0
    catalog_earned_first_party: 0.0
    catalog_gap: 79.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 28.9
    commercial_clarity: 28.9
    contract_governance: 0.0
    contract_quality: 48.3
    developer_ergonomics: 2.4
    discoverability: 57.4
    governance: 0.0
    operational_transparency: 10.5
  previous_composite: 25.4
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 1
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/geoapify/refs/heads/main/screenshots/geoapify-2026-06-20T181748.png
security:
- kind: domain-security
  name: Geoapify Domain Security
  slug: geoapify-domain-security
  summary_line: TLSv1.3 · DMARC
slug: geoapify
tags:
- Geocoding
- Geospatial
- Location
- Maps
website: https://www.geoapify.com/
---
