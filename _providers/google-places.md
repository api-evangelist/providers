---
access_model:
  confidence: high
  label: Paid · Self-serve signup
  onboarding: self-serve
  pricing: paid
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: verified
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 44.1
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 3
  human_in_the_loop: 0
  name: Google Places Agentic Access
  operation_count: 5
  slug: google-places-agentic-access
  summary_line: 5 operations · 3 acting
api_count: 2
apis:
- description: Operations for retrieving place details and media.
  name: Google Places Places API
  slug: google-places-places-api
- description: Operations for searching and autocompleting places.
  name: Google Places Search API
  slug: google-places-search-api
artifact_total: 64
collections:
- collection_type: open
  name: Google Places API (New)
  slug: open-openapi
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/google-places-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/google-places-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/google-places-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/google-places-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/google-places-scopes.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/googlemaps
- group: build
  title: MCP Server
  type: Tools
  url: https://github.com/googlemaps/platform-ai
- group: build
  title: MCP Server (Grounding)
  type: Tools
  url: https://developers.google.com/maps/ai/grounding-lite/reference/mcp
- group: start
  title: ''
  type: GettingStarted
  url: https://developers.google.com/maps/documentation/places/web-service/overview
- group: auth
  title: ''
  type: Authentication
  url: https://developers.google.com/maps/documentation/places/web-service/get-api-key
- group: commercial
  title: ''
  type: Pricing
  url: https://developers.google.com/maps/billing-and-pricing/pricing
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/google-places-rate-limits.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/google-places-plans-pricing.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/google-places-finops.yml
- group: design
  title: ''
  type: JSONLD
  url: json-ld/context.jsonld
- group: design
  title: ''
  type: Spectral
  url: rules/google-places-spectral-rules.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/google-places-vocabulary.yml
- group: operate
  title: ''
  type: SupportTermsOfService
  url: https://cloud.google.com/maps-platform/terms
created: '2026-03-13'
description: The Google Places API is a service that accepts HTTP requests for location data through a variety of methods. It returns formatted location data and imagery about establishments, geographic locations, or prominent points of interest. Supports nearby search, text search, place details, place photos, and autocomplete.
examples:
- key_count: 3
  name: Author Attribution Example
  slug: author-attribution-example
- key_count: 6
  name: Autocomplete Request Example
  slug: autocomplete-request-example
- key_count: 1
  name: Autocomplete Response Example
  slug: autocomplete-response-example
- key_count: 2
  name: Circle Example
  slug: circle-example
- key_count: 2
  name: Lat Lng Example
  slug: lat-lng-example
- key_count: 2
  name: Localized Text Example
  slug: localized-text-example
- key_count: 7
  name: Nearby Search Request Example
  slug: nearby-search-request-example
- key_count: 3
  name: Opening Hours Example
  slug: opening-hours-example
- key_count: 4
  name: Photo Example
  slug: photo-example
- key_count: 2
  name: Photo Media Example
  slug: photo-media-example
- key_count: 19
  name: Place Example
  slug: place-example
- key_count: 7
  name: Review Example
  slug: review-example
- key_count: 1
  name: Search Response Example
  slug: search-response-example
- key_count: 2
  name: Suggestion Example
  slug: suggestion-example
- key_count: 9
  name: Text Search Request Example
  slug: text-search-request-example
- key_count: 3
  name: Time Point Example
  slug: time-point-example
finops:
- name: Google Places Finops
  service_category: Maps + Location
  slug: google-places-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/google-places.png
json_schemas:
- name: Google Place
  property_count: 12
  slug: Place
- name: AuthorAttribution
  property_count: 3
  slug: author-attribution
- name: AutocompleteRequest
  property_count: 6
  slug: autocomplete-request
- name: AutocompleteResponse
  property_count: 1
  slug: autocomplete-response
- name: Circle
  property_count: 2
  slug: circle
- name: LatLng
  property_count: 2
  slug: lat-lng
- name: LocalizedText
  property_count: 2
  slug: localized-text
- name: NearbySearchRequest
  property_count: 7
  slug: nearby-search-request
- name: OpeningHours
  property_count: 3
  slug: opening-hours
- name: PhotoMedia
  property_count: 2
  slug: photo-media
- name: Photo
  property_count: 4
  slug: photo
- name: Place
  property_count: 19
  slug: place
- name: Review
  property_count: 7
  slug: review
- name: SearchResponse
  property_count: 1
  slug: search-response
- name: Suggestion
  property_count: 2
  slug: suggestion
- name: TextSearchRequest
  property_count: 9
  slug: text-search-request
- name: TimePoint
  property_count: 3
  slug: time-point
json_structures:
- name: Author Attribution Structure
  property_count: 3
  slug: author-attribution-structure
- name: Autocomplete Request Structure
  property_count: 6
  slug: autocomplete-request-structure
- name: Autocomplete Response Structure
  property_count: 1
  slug: autocomplete-response-structure
- name: Circle Structure
  property_count: 2
  slug: circle-structure
- name: Lat Lng Structure
  property_count: 2
  slug: lat-lng-structure
- name: Localized Text Structure
  property_count: 2
  slug: localized-text-structure
- name: Nearby Search Request Structure
  property_count: 7
  slug: nearby-search-request-structure
- name: Opening Hours Structure
  property_count: 3
  slug: opening-hours-structure
- name: Photo Media Structure
  property_count: 2
  slug: photo-media-structure
- name: Photo Structure
  property_count: 4
  slug: photo-structure
- name: Place Structure
  property_count: 19
  slug: place-structure
- name: Review Structure
  property_count: 7
  slug: review-structure
- name: Search Response Structure
  property_count: 1
  slug: search-response-structure
- name: Suggestion Structure
  property_count: 2
  slug: suggestion-structure
- name: Text Search Request Structure
  property_count: 9
  slug: text-search-request-structure
- name: Time Point Structure
  property_count: 3
  slug: time-point-structure
jsonld:
- class_count: 16
  name: context Context
  property_count: 0
  slug: context
- class_count: 24
  name: Google Places Api Context
  property_count: 57
  slug: google-places-api-context
layout: provider
modified: '2026-06-02'
name: Google Places
nav: Providers
network: true
overview: 'Google Places publishes 2 APIs on the [APIs.io](https://apis.io/) network: Places API and Search API. Tagged areas include Restaurant, Geolocation, Google, Locations, and Maps.


  The Google Places catalog on APIs.io includes 2 JSON-LD contexts and 2 Spectral governance rulesets.


  Google Places'' developer surface includes authentication, tooling, getting-started guide, pricing, and 14 more developer resources.'
plans:
- name: Google Places Plans Pricing
  plan_count: 3
  slug: google-places-plans-pricing
random_paper: 18
rate_limits:
- limit_count: 2
  name: Google Places Rate Limits
  slug: google-places-rate-limits
rules:
- name: Google Places API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: google-places-jsonschema-spectral-rules
- name: Google Places API Rules
  rule_count: 44
  severity_counts:
    error: 6
    hint: 0
    info: 14
    warn: 24
  slug: google-places-spectral-rules
scopes:
- name: Google Places Scopes
  scope_count: 1
  slug: google-places-scopes
  summary_line: 1 scope · authorizationCode
score:
  band: developing
  composite: 52.8
  delta: -4.3
  facets:
    commercial_clarity: 50.0
    contract_quality: 79.7
    developer_ergonomics: 21.7
    discoverability: 68.5
    governance: 68.8
    operational_transparency: 26.3
  previous_composite: 57.1
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 2
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/google-places/refs/heads/main/screenshots/google-places-2026-06-20T182225.png
security:
- kind: authentication
  name: Google Places Authentication
  slug: google-places-authentication
  summary_line: apiKey/oauth2 · 3 schemes
- kind: domain-security
  name: Google Places Domain Security
  slug: google-places-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Google Places Vulnerability Disclosure
  slug: google-places-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: google-places
tags:
- Restaurant
- Geolocation
- Google
- Locations
- Maps
- Places
- Points of Interest
---
