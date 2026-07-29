---
access_model:
  confidence: high
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: true
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
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 36.9
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Positionstack Agentic Access
  operation_count: 2
  slug: positionstack-agentic-access
  summary_line: 2 operations
api_count: 3
apis:
- description: Run multiple forward or reverse geocoding lookups in a single request (Professional plan and above).
  name: positionstack Batch Geocoding API
  slug: positionstack-batch-geocoding-api
- description: Convert addresses, place names, or partial location strings into geographic coordinates.
  name: positionstack Forward Geocoding API
  slug: positionstack-forward-geocoding-api
- description: Convert latitude/longitude coordinates into a full address with locality, region, and country.
  name: positionstack Reverse Geocoding API
  slug: positionstack-reverse-geocoding-api
arazzos:
- description: Forward geocode an address and branch on the match confidence to either enrich or re-verify the result.
  name: positionstack Geocode with Confidence Branch
  slug: positionstack-geocode-confidence-branch-workflow
- description: Forward geocode an address, then reverse geocode the resulting coordinates to verify the match.
  name: positionstack Geocode Roundtrip
  slug: positionstack-geocode-roundtrip-workflow
- description: Reverse geocode a coordinate pair with country, timezone, and sun modules to build a full place profile.
  name: positionstack Reverse Geocode Enriched Place Profile
  slug: positionstack-reverse-enrich-place-workflow
artifact_total: 54
collections:
- collection_type: postman
  name: positionstack
  slug: postman-positionstack
- collection_type: open
  name: positionstack
  slug: open-positionstack
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/positionstack-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/positionstack-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/positionstack-authentication.yml
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/positionstack/overview
- group: design
  title: ''
  type: Arazzo
  url: arazzo/positionstack-geocode-confidence-branch-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/positionstack-geocode-roundtrip-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/positionstack-reverse-enrich-place-workflow.yml
- group: company
  title: ''
  type: Website
  url: https://positionstack.com/
- group: start
  title: ''
  type: Portal
  url: https://positionstack.com/dashboard
- group: start
  title: ''
  type: Signup
  url: https://positionstack.com/signup/free
- group: commercial
  title: ''
  type: Pricing
  url: https://positionstack.com/product
- group: docs
  title: ''
  type: Documentation
  url: https://docs.apilayer.com/positionstack/docs/api-documentation
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.apilayer.com/positionstack/docs/getting-started
- group: company
  title: ''
  type: Blog
  url: https://blog.apilayer.com/
- group: operate
  title: ''
  type: StatusPage
  url: https://positionstack.com/api-status
- group: operate
  title: ''
  type: Support
  url: mailto:support@positionstack.com
- group: operate
  title: ''
  type: FAQ
  url: https://positionstack.com/faq
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.ideracorp.com/legal/APILayer
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.ideracorp.com/Legal/PrivacyPolicy
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/apilayer
- group: build
  title: ''
  type: GitHubRepository
  url: https://github.com/apilayer/positionstack
- group: other
  title: ''
  type: PublicAPIsListing
  url: https://github.com/public-apis/public-apis
- group: commercial
  title: ''
  type: Plans
  url: plans/positionstack-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/positionstack-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/positionstack-finops.yml
- group: design
  title: ''
  type: SpectralRules
  url: rules/positionstack-rules.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/positionstack-vocabulary.yml
created: '2026-05-28'
description: Forward and Reverse Batch Geocoding REST API by positionstack (an apilayer product, owned by Idera, Inc.). Convert addresses to coordinates and coordinates to addresses across 2+ billion global places, with optional data modules for country, timezone, sun, and bounding-box enrichment.
examples:
- key_count: 2
  name: Positionstack Batch Forward Example
  slug: positionstack-batch-forward-example
- key_count: 2
  name: Positionstack Error Example
  slug: positionstack-error-example
- key_count: 2
  name: Positionstack Forward Geocode Example
  slug: positionstack-forward-geocode-example
- key_count: 2
  name: Positionstack Reverse Geocode Example
  slug: positionstack-reverse-geocode-example
features:
- description: Convert addresses, place names, and postal codes into geographic coordinates.
  name: Forward Geocoding
- description: Convert latitude/longitude coordinates into structured address data.
  name: Reverse Geocoding
- description: Run up to 80 forward or reverse lookups per request (Professional plan and above).
  name: Batch Geocoding
- description: Responses available in JSON, XML, and GeoJSON.
  name: Multiple Output Formats
- description: Each result includes a `map_url` that can be embedded via iFrame.
  name: Embeddable Maps
- description: Localize results in multiple languages via the `language` parameter.
  name: Multi-Language Results
- description: Optional enrichment adding ISO codes, currency, languages, flag, dial code, and area.
  name: Country Module
- description: Optional enrichment with IANA timezone, GMT offset, abbreviation, and DST status.
  name: Timezone Module
- description: Optional enrichment with sunrise, sunset, and solar transit times.
  name: Sun Module
- description: Optional enrichment with bounding box coordinates per result.
  name: BBox Module
- description: Global coverage across 2+ billion addresses and places.
  name: 2+ Billion Places
- description: Average reported availability across forward, reverse, and batch endpoints.
  name: 99.9% Uptime
- description: Email and dashboard alerts at 75%, 90%, and 100% of monthly quota.
  name: Overage Notifications
finops:
- name: Positionstack Finops
  service_category: ''
  slug: positionstack-finops
image: https://positionstack.com/site_images/positionstack_square.png
integrations:
- description: Sibling apilayer API providing weather data for resolved coordinates.
  name: weatherstack
- description: Sibling apilayer API offering IP geolocation that pairs with positionstack lookups.
  name: ipstack
- description: Sibling apilayer API for address verification and autocomplete.
  name: streetlayer
- description: Display positionstack results on third-party map libraries via the embeddable `map_url`.
  name: Mapbox / Leaflet / OpenStreetMap
- description: Bulk-enrich spreadsheet data with coordinates via the batch endpoint.
  name: Power BI / Tableau / Excel
json_schemas:
- name: ErrorResponse
  property_count: 2
  slug: positionstack-error
- name: Location
  property_count: 20
  slug: positionstack-location
json_structures:
- name: Positionstack Location Structure
  property_count: 0
  slug: positionstack-location-structure
jsonld:
- class_count: 21
  name: Positionstack Context
  property_count: 6
  slug: positionstack-context
layout: provider
modified: '2026-05-29'
name: positionstack
nav: Providers
network: true
overview: 'positionstack publishes 3 APIs on the [APIs.io](https://apis.io/) network: Batch Geocoding API, Forward Geocoding API, and Reverse Geocoding API. Tagged areas include Geocoding, Reverse Geocoding, Maps, Location, and Address Validation.


  The positionstack catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  positionstack''s developer surface includes authentication, developer portal, signup flow, pricing, documentation, getting-started guide, engineering blog, and 20 more developer resources.'
plans:
- name: Positionstack Plans Pricing
  plan_count: 5
  slug: positionstack-plans-pricing
random_paper: 76
rate_limits:
- limit_count: 0
  name: Positionstack Rate Limits
  slug: positionstack-rate-limits
rules:
- name: positionstack API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: positionstack-jsonschema-spectral-rules
- name: positionstack API Rules
  rule_count: 8
  severity_counts:
    error: 3
    hint: 0
    info: 1
    warn: 4
  slug: positionstack-rules
score:
  band: strong
  composite: 63.1
  delta: -3.8
  facets:
    commercial_clarity: 71.1
    contract_quality: 78.8
    developer_ergonomics: 50.0
    discoverability: 81.5
    governance: 68.8
    operational_transparency: 21.1
  previous_composite: 66.9
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 3
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/positionstack/refs/heads/main/screenshots/positionstack-2026-06-20T191943.png
security:
- kind: authentication
  name: Positionstack Authentication
  slug: positionstack-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Positionstack Domain Security
  slug: positionstack-domain-security
  summary_line: TLSv1.3 · DMARC
slug: positionstack
solutions:
- description: 100 requests/month, personal use, JSON output, no HTTPS.
  name: Free / Hobbyist
- description: 100k req/mo, $9.99/mo, HTTPS, multi-format, commercial license.
  name: Basic
- description: 1M req/mo, $49.99/mo, batch endpoint enabled.
  name: Professional
- description: 3M req/mo, $99.99/mo.
  name: Business
- description: Custom volume + SLA + dedicated account team.
  name: Enterprise / Platinum
tags:
- Geocoding
- Reverse Geocoding
- Maps
- Location
- Address Validation
- apilayer
- Public APIs
use_cases:
- description: Power address autocomplete and validation in signup or checkout flows.
  name: Address Autocomplete
- description: Resolve GPS coordinates from vehicles, IoT devices, or pet trackers into addresses.
  name: Fleet & Asset Tracking
- description: Geocode user-entered addresses to find nearest stores or service centers.
  name: Store Locator
- description: Cleanse and standardize delivery addresses across bulk shipment manifests.
  name: Logistics & Delivery
- description: Map property listings by geocoding street addresses.
  name: Real Estate Listings
- description: Enrich CRM records with geographic, country, and timezone data.
  name: Market Analysis
- description: Pair coordinates with weather APIs (e.g. weatherstack) for hyper-local services.
  name: Weather & Local Services
website: https://positionstack.com/
---
