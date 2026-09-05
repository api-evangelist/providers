---
access_model:
  confidence: medium
  label: Freemium (free trial) · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  - security
  trial: true
  try_now: true
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: na
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: na
    mcp_server: false
    openapi_examples: documented
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 24.4
  scored_at: '2026-09-04'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Foursquare Agentic Access
  operation_count: 8
  slug: foursquare-agentic-access
  summary_line: 8 operations
api_count: 1
apis:
- description: Mobile SDK for iOS, Android, and React Native that translates passive device location signals into visit events using the Foursquare POI graph.
  name: Foursquare Movement SDK
  slug: movement-sdk
- description: Server-side API for managing geofences that trigger events when Movement SDK-equipped devices enter or exit defined places.
  name: Foursquare Movement Geofence API
  slug: movement-geofence-api
- description: API for managing datasets, maps, and visualizations within Foursquare Studio for geospatial analytics.
  name: Foursquare Studio Data API
  slug: studio-data-api
- description: API for attribution and audience measurement using Foursquare visit panels.
  name: Foursquare Measurement API (MAPI)
  slug: measurement-api
- baseURL: https://places-api.foursquare.com
  baseurl_source: declared
  description: Natural-language place search with justifications
  name: Foursquare Ask API
  slug: foursquare-ask-api
- baseURL: https://places-api.foursquare.com
  baseurl_source: declared
  description: Type-ahead search for places, addresses, and geographies
  name: Foursquare Autocomplete API
  slug: foursquare-autocomplete-api
- baseURL: https://places-api.foursquare.com
  baseurl_source: declared
  description: Retrieve attributes for a specific place
  name: Foursquare Details API
  slug: foursquare-details-api
- baseURL: https://places-api.foursquare.com
  baseurl_source: declared
  description: Resolve a coordinate to the most likely place (Place Snap)
  name: Foursquare Geotagging API
  slug: foursquare-geotagging-api
- baseURL: https://places-api.foursquare.com
  baseurl_source: declared
  description: Match an external POI record to a Foursquare place
  name: Foursquare Match API
  slug: foursquare-match-api
- baseURL: https://places-api.foursquare.com
  baseurl_source: declared
  description: Photos associated with a place
  name: Foursquare Photos API
  slug: foursquare-photos-api
- baseURL: https://places-api.foursquare.com
  baseurl_source: declared
  description: Find and explore places
  name: Foursquare Search API
  slug: foursquare-search-api
- baseURL: https://places-api.foursquare.com
  baseurl_source: declared
  description: User tips associated with a place
  name: Foursquare Tips API
  slug: foursquare-tips-api
artifact_total: 47
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Foursquare Places Ask API
  slug: open-foursquare-ask-api
- collection_type: open
  name: Foursquare Places Ask Autocomplete API
  slug: open-foursquare-autocomplete-api
- collection_type: open
  name: Foursquare Places Ask Details API
  slug: open-foursquare-details-api
- collection_type: open
  name: Foursquare Places Ask Geotagging API
  slug: open-foursquare-geotagging-api
- collection_type: open
  name: Foursquare Places Ask Match API
  slug: open-foursquare-match-api
- collection_type: open
  name: Foursquare Places Ask Photos API
  slug: open-foursquare-photos-api
- collection_type: open
  name: Foursquare Places API
  slug: open-foursquare-places
- collection_type: open
  name: Foursquare Places Ask Search API
  slug: open-foursquare-search-api
- collection_type: open
  name: Foursquare Places Ask Tips API
  slug: open-foursquare-tips-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/foursquare-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/foursquare-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/foursquare-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/foursquare
- group: build
  title: MCP Server
  type: Tools
  url: https://github.com/foursquare/foursquare-places-mcp
- group: build
  title: ''
  type: SDKs
  url: https://github.com/foursquare/movementsdk-ios-spm
- group: build
  title: ''
  type: SDKs
  url: https://github.com/foursquare/movement-sdk-react-native
- group: build
  title: ''
  type: SDKs
  url: https://github.com/foursquare/fsq-studio-sdk-examples
- group: build
  title: ''
  type: SampleCode
  url: https://github.com/foursquare/foursquare-places-api-samples
- group: build
  title: ''
  type: Postman
  url: https://github.com/foursquare/Place-API-Postman-Collection
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/location-foursquare
- group: company
  title: ''
  type: Website
  url: https://foursquare.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.foursquare.com/developer/
- group: start
  title: ''
  type: Signup
  url: https://foursquare.com/developers/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.foursquare.com/developer/reference/places-api-overview
- group: operate
  title: ''
  type: Discord
  url: https://discord.gg/foursquare
- group: company
  title: ''
  type: Blog
  url: https://location.foursquare.com/resources/blog/
- group: agent
  title: ''
  type: LlmsText
  url: https://docs.foursquare.com/llms.txt
created: '2025-03-01'
description: Foursquare is a location intelligence platform that maintains a global graph of more than 100 million points of interest (POI) and provides developer APIs and SDKs for place search, geotagging, autocomplete, audience measurement, and visit detection across web and mobile.
examples:
- key_count: 1
  name: Foursquare Ask Example
  slug: foursquare-ask-example
- key_count: 1
  name: Foursquare Geotagging Example
  slug: foursquare-geotagging-example
- key_count: 1
  name: Foursquare Match Example
  slug: foursquare-match-example
- key_count: 16
  name: Foursquare Place Example
  slug: foursquare-place-example
- key_count: 2
  name: Foursquare Search Example
  slug: foursquare-search-example
finops:
- name: Foursquare Finops
  service_category: Geospatial & Location Data
  slug: foursquare-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/foursquare.png
json_schemas:
- name: AskResponse
  property_count: 1
  slug: foursquare-ask-response
- name: AutocompleteResponse
  property_count: 1
  slug: foursquare-autocomplete-response
- name: GeotaggingResponse
  property_count: 1
  slug: foursquare-geotagging-response
- name: Photo
  property_count: 6
  slug: foursquare-photo
- name: PlaceMatchResponse
  property_count: 1
  slug: foursquare-place-match-response
- name: Place
  property_count: 23
  slug: foursquare-place
- name: PlaceSearchResponse
  property_count: 2
  slug: foursquare-place-search-response
- name: FoursquarePlace
  property_count: 17
  slug: foursquare-place
- name: Tip
  property_count: 3
  slug: foursquare-tip
- name: FoursquareTip
  property_count: 3
  slug: foursquare-tip
json_structures:
- name: Foursquare Structure
  property_count: 0
  slug: foursquare-structure
jsonld:
- class_count: 19
  name: Foursquare Context
  property_count: 0
  slug: foursquare-context
layout: provider
modified: '2026-06-02'
name: Foursquare
nav: Providers
network: true
overview: 'Foursquare publishes 8 APIs on the [APIs.io](https://apis.io/) network, including Ask API, Autocomplete API, Details API, and 5 more. Tagged areas include Restaurant, Locations, Places, Geocoding, and Recommendations.


  The Foursquare catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Foursquare''s developer surface includes authentication, tooling, signup flow, documentation, engineering blog, and 13 more developer resources.'
plans:
- name: Foursquare Plans Pricing
  plan_count: 10
  slug: foursquare-plans-pricing
random_paper: 9
rate_limits:
- limit_count: 2
  name: Foursquare Rate Limits
  slug: foursquare-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: Foursquare API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: foursquare-jsonschema-spectral-rules
- effective_rule_count: 0
  extends: []
  name: Foursquare API Rules
  rule_count: 0
  severity_counts:
    error: 0
    hint: 0
    info: 0
    warn: 0
  slug: foursquare-places-rules
score:
  band: developing
  composite: 43.7
  coverage:
    artifact_dirs: 17
    catalog_earned: 66.3
    catalog_earned_first_party: 0.0
    catalog_gap: 48.8
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 28.9
    commercial_clarity: 28.9
    contract_governance: 25.0
    contract_quality: 69.0
    developer_ergonomics: 50.0
    discoverability: 66.7
    governance: 25.0
    operational_transparency: 7.9
  previous_composite: 43.7
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 8
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/foursquare/refs/heads/main/screenshots/foursquare-2026-06-20T181457.png
security:
- kind: authentication
  name: Foursquare Authentication
  slug: foursquare-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Foursquare Domain Security
  slug: foursquare-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: foursquare
tags:
- Restaurant
- Locations
- Places
- Geocoding
- Recommendations
- Reviews
- Movement
website: https://foursquare.com/
---
