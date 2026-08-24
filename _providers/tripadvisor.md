---
access_model:
  confidence: high
  label: Enterprise · Self-serve signup
  onboarding: self-serve
  pricing: enterprise
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
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 35.9
  scored_at: '2026-08-24'
agentic_access:
- acting_count: 1
  human_in_the_loop: 0
  name: Tripadvisor Agentic Access
  operation_count: 8
  slug: tripadvisor-agentic-access
  summary_line: 8 operations · 1 acting
api_count: 7
apis:
- description: Availability endpoint called in real-time when users view hotel pages on Tripadvisor to retrieve pricing and room availability.
  name: Tripadvisor Availability API
  slug: tripadvisor-availability-api
- description: Configuration endpoint that Tripadvisor queries to discover the partner's supported features and API version.
  name: Tripadvisor Configuration API
  slug: tripadvisor-configuration-api
- description: Hotel inventory endpoint queried daily by Tripadvisor to import the partner's full list of connected hotels.
  name: Tripadvisor Hotel Inventory API
  slug: tripadvisor-hotel-inventory-api
- description: Retrieve comprehensive information about a specific location including name, address, rating, and Tripadvisor listing URLs.
  name: Tripadvisor Location Details API
  slug: tripadvisor-location-details-api
- description: Access high-quality recent photos for a specific location in multiple size formats.
  name: Tripadvisor Location Photos API
  slug: tripadvisor-location-photos-api
- description: Retrieve the most recent reviews for a specific location, up to 5 reviews per request.
  name: Tripadvisor Location Reviews API
  slug: tripadvisor-location-reviews-api
- description: Search for locations by keyword query or geographic proximity. Returns up to 10 matching locations per request.
  name: Tripadvisor Location Search API
  slug: tripadvisor-location-search-api
artifact_total: 57
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Tripadvisor Content Availability API
  slug: open-tripadvisor-availability-api
- collection_type: open
  name: Tripadvisor Content Availability Configuration API
  slug: open-tripadvisor-configuration-api
- collection_type: open
  name: Tripadvisor Content API
  slug: open-tripadvisor-content-api
- collection_type: open
  name: Tripadvisor Hotel Availability Check API
  slug: open-tripadvisor-hotel-availability-check-api
- collection_type: open
  name: Tripadvisor Content Availability Hotel Inventory API
  slug: open-tripadvisor-hotel-inventory-api
- collection_type: open
  name: Tripadvisor Content Availability Location Details API
  slug: open-tripadvisor-location-details-api
- collection_type: open
  name: Tripadvisor Content Availability Location Photos API
  slug: open-tripadvisor-location-photos-api
- collection_type: open
  name: Tripadvisor Content Availability Location Search API
  slug: open-tripadvisor-location-search-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/tripadvisor-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/tripadvisor-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/tripadvisor-authentication.yml
- group: company
  title: ''
  type: Blog
  url: https://www.tripadvisor.com/blog/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/tripadvisor
- group: company
  title: ''
  type: Website
  url: https://www.tripadvisor.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer-tripadvisor.com
- group: docs
  title: ''
  type: Documentation
  url: https://tripadvisor-content-api.readme.io/reference/overview
- group: start
  title: ''
  type: Signup
  url: https://developer-tripadvisor.com/content-api/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://developer-tripadvisor.com/content-api/terms-of-use/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/tripadvisor
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/tripadvisor-dev
- group: design
  title: ''
  type: JSONLD
  url: json-ld/tripadvisor-context.jsonld
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/tripadvisor-location-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/tripadvisor-review-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/tripadvisor-hotel-availability-schema.json
- group: design
  title: ''
  type: SpectralRules
  url: rules/tripadvisor-rules.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/tripadvisor-vocabulary.yml
- group: agent
  title: ''
  type: LlmsText
  url: https://tripadvisor-content-api.readme.io/llms.txt
created: '2026-05-03'
description: Tripadvisor is the world's largest travel guidance platform, helping hundreds of millions of travelers each month find places to stay, things to do, and restaurants through reviews, photos, and tools. The platform maintains over 7.5 million locations and 1 billion reviews across 43 markets and 29 languages. Tripadvisor provides APIs for content integration, hotel connectivity, and restaurant reservations.
examples:
- key_count: 2
  name: Tripadvisor Check Hotel Availability Example
  slug: tripadvisor-check-hotel-availability-example
- key_count: 2
  name: Tripadvisor Get Location Details Example
  slug: tripadvisor-get-location-details-example
- key_count: 2
  name: Tripadvisor Get Location Reviews Example
  slug: tripadvisor-get-location-reviews-example
- key_count: 2
  name: Tripadvisor Search For Locations Example
  slug: tripadvisor-search-for-locations-example
features:
- name: Location Search
- name: Nearby Search
- name: Location Details
- name: Location Photos
- name: Location Reviews
- name: Hotel Availability Check
- name: Hotel Inventory Management
- name: 7.5 Million Locations
- name: 1 Billion Reviews
- name: 29 Languages
- name: 43 Markets
finops:
- name: Tripadvisor Finops
  service_category: Travel Content / Reviews API
  slug: tripadvisor-finops
graphqls:
- description: This conceptual GraphQL schema models the TripAdvisor travel reviews and search platform. While TripAdvisor exposes a REST-based Content API, this schema captures the full domain model including locat
  name: TripAdvisor GraphQL Schema
  slug: tripadvisor-graphql
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/tripadvisor.png
integrations:
- name: Booking.com
- name: Expedia
- name: Hotels.com
- name: Viator
- name: TheFork
json_schemas:
- name: Tripadvisor Hotel Availability Response
  property_count: 3
  slug: tripadvisor-hotel-availability
- name: Tripadvisor Location
  property_count: 25
  slug: tripadvisor-location
- name: Tripadvisor Review
  property_count: 14
  slug: tripadvisor-review
json_structures:
- name: Tripadvisor Location Structure
  property_count: 0
  slug: tripadvisor-location-structure
jsonld:
- class_count: 0
  name: Tripadvisor Context
  property_count: 7
  slug: tripadvisor-context
layout: provider
modified: '2026-06-03'
name: Tripadvisor
nav: Providers
network: true
overview: 'Tripadvisor publishes 7 APIs on the [APIs.io](https://apis.io/) network, including Availability API, Configuration API, Hotel Inventory API, and 4 more. Tagged areas include Attractions, Hotels, Hospitality, Restaurant, and Reviews.


  The Tripadvisor catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Tripadvisor''s developer surface includes authentication, engineering blog, documentation, signup flow, and 15 more developer resources.'
plans:
- name: Tripadvisor Plans Pricing
  plan_count: 2
  slug: tripadvisor-plans-pricing
random_paper: 10
rate_limits:
- limit_count: 3
  name: Tripadvisor Rate Limits
  slug: tripadvisor-rate-limits
rules:
- effective_rule_count: 6
  extends: []
  name: Tripadvisor API Rules
  rule_count: 6
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 5
  slug: tripadvisor-jsonschema-spectral-rules
- effective_rule_count: 50
  extends:
  - spectral:oas
  name: Tripadvisor API Rules
  rule_count: 9
  severity_counts:
    error: 2
    hint: 0
    info: 0
    warn: 7
  slug: tripadvisor-rules
score:
  band: developing
  composite: 43.2
  delta: 0.0
  facets:
    access_clarity: 36.8
    commercial_clarity: 36.8
    contract_governance: 28.8
    contract_quality: 64.8
    developer_ergonomics: 33.3
    discoverability: 81.5
    governance: 28.8
    operational_transparency: 10.5
  previous_composite: 43.2
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 7
  schema_version: 0.12.1
  scored_at: '2026-08-24'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/tripadvisor/refs/heads/main/screenshots/tripadvisor-2026-06-20T195729.png
security:
- kind: authentication
  name: Tripadvisor Authentication
  slug: tripadvisor-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Tripadvisor Domain Security
  slug: tripadvisor-domain-security
  summary_line: TLSv1.3 · DMARC
slug: tripadvisor
tags:
- Attractions
- Hotels
- Hospitality
- Restaurant
- Reviews
- Travel
use_cases:
- name: Travel Content Integration
- name: Hotel Booking Widget
- name: Restaurant Discovery
- name: Attraction Finder
- name: Hotel Connectivity Partner
- name: Travel App Development
- name: Review Aggregation
website: https://www.tripadvisor.com
---
