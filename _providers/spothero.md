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
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
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
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 25.5
  scored_at: '2026-09-01'
agentic_access:
- acting_count: 2
  human_in_the_loop: 0
  name: Spothero Agentic Access
  operation_count: 8
  slug: spothero-agentic-access
  summary_line: 8 operations · 2 acting
api_count: 1
apis:
- description: SpotNow is SpotHero's server and API built in Kotlin for real-time parking availability and instant booking functionality, exposed via the HeroLab platform.
  name: SpotHero SpotNow API
  slug: spotnow-api
- description: Check real-time parking availability
  name: SpotHero Availability API
  slug: spothero-availability-api
- description: Retrieve facility details, amenities, pricing, and directions
  name: SpotHero Facilities API
  slug: spothero-facilities-api
- description: Retrieve pricing and rate information
  name: SpotHero Rates API
  slug: spothero-rates-api
- description: Create, manage, and cancel parking reservations
  name: SpotHero Reservations API
  slug: spothero-reservations-api
- description: Search for available parking locations and facilities
  name: SpotHero Search API
  slug: spothero-search-api
artifact_total: 33
collections:
- collection_type: postman
  name: SpotHero Parking Availability API
  slug: postman-spothero-availability-api
- collection_type: postman
  name: SpotHero Parking Availability Facilities API
  slug: postman-spothero-facilities-api
- collection_type: postman
  name: SpotHero Parking Availability Rates API
  slug: postman-spothero-rates-api
- collection_type: postman
  name: SpotHero Parking Availability Reservations API
  slug: postman-spothero-reservations-api
- collection_type: postman
  name: SpotHero Parking Availability Search API
  slug: postman-spothero-search-api
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: SpotHero Parking Availability API
  slug: open-spothero-availability-api
- collection_type: open
  name: SpotHero Parking Availability Facilities API
  slug: open-spothero-facilities-api
- collection_type: open
  name: SpotHero Parking API
  slug: open-spothero-parking
- collection_type: open
  name: SpotHero Parking Availability Rates API
  slug: open-spothero-rates-api
- collection_type: open
  name: SpotHero Parking Availability Reservations API
  slug: open-spothero-reservations-api
- collection_type: open
  name: SpotHero Parking Availability Search API
  slug: open-spothero-search-api
common:
- group: other
  title: ''
  type: ParentCompany
  url: https://apis.io/providers/uber/
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/spothero-capability-edges.yml
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/spothero/overview
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/spothero-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/spothero-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/spothero-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/spothero
- group: docs
  title: ''
  type: Documentation
  url: https://spothero.com/developers
- group: start
  title: ''
  type: DeveloperPortal
  url: https://api.spothero.com/v2/docs
- group: commercial
  title: ''
  type: TermsOfService
  url: https://spothero.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://spothero.com/privacy
- group: company
  title: ''
  type: Website
  url: https://spothero.com
- group: operate
  title: ''
  type: Contact
  url: mailto:partner.support@spothero.com
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/spothero-reservation-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/spothero-facility-schema.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/spothero-reservation-structure.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/spothero-facility-structure.json
- group: design
  title: ''
  type: JSONLD
  url: json-ld/spothero-context.jsonld
- group: design
  title: ''
  type: SpectralRules
  url: rules/spothero-rules.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/spothero-vocabulary.yml
- group: company
  title: ''
  type: Blog
  url: https://blog.spothero.com/feed/
created: '2025-02-06'
description: SpotHero is the leading digital parking marketplace in North America, offering a flexible parking API and developer toolkit that connects vehicles, drivers, and mobility apps with the largest network of off-street parking facilities. The platform enables navigation apps, rideshare services, connected cars, and enterprise fleets to seamlessly book and manage parking reservations. SpotHero was acquired by Uber in 2026 to power parking reservation experiences within the Uber app.
examples:
- key_count: 3
  name: Spothero Create Reservation Example
  slug: spothero-create-reservation-example
- key_count: 3
  name: Spothero Search Parking Example
  slug: spothero-search-parking-example
finops:
- name: Spothero Finops
  service_category: API
  slug: spothero-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/spothero.png
json_schemas:
- name: SpotHero Facility
  property_count: 15
  slug: spothero-facility
- name: SpotHero Reservation
  property_count: 15
  slug: spothero-reservation
json_structures:
- name: Spothero Facility Structure
  property_count: 0
  slug: spothero-facility-structure
- name: Spothero Reservation Structure
  property_count: 0
  slug: spothero-reservation-structure
jsonld:
- class_count: 38
  name: Spothero Context
  property_count: 0
  slug: spothero-context
layout: provider
modified: '2026-05-19'
name: SpotHero
nav: Providers
network: true
overview: 'SpotHero publishes 5 APIs on the [APIs.io](https://apis.io/) network, including Availability API, Facilities API, Rates API, and 2 more. Tagged areas include Parking, Mobility, Transportation, Navigation, and Reservations.


  The SpotHero catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  SpotHero''s developer surface includes authentication, documentation, engineering blog, and 18 more developer resources.'
plans:
- name: Spothero Plans Pricing
  plan_count: 3
  slug: spothero-plans-pricing
random_paper: 2
rate_limits:
- limit_count: 5
  name: Spothero Rate Limits
  slug: spothero-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: SpotHero API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: spothero-jsonschema-spectral-rules
- effective_rule_count: 55
  extends:
  - spectral:oas
  name: SpotHero API Rules
  rule_count: 14
  severity_counts:
    error: 6
    hint: 0
    info: 1
    warn: 7
  slug: spothero-rules
score:
  band: thin
  composite: 36.5
  coverage:
    artifact_dirs: 18
    catalog_gap: 51.5
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 15.8
    commercial_clarity: 15.8
    contract_governance: 28.8
    contract_quality: 62.4
    developer_ergonomics: 28.6
    discoverability: 68.5
    governance: 28.8
    operational_transparency: 13.2
  previous_composite: 36.5
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 5
  schema_version: 0.18.0
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/spothero/refs/heads/main/screenshots/spothero-2026-06-20T194352.png
security:
- kind: authentication
  name: Spothero Authentication
  slug: spothero-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Spothero Domain Security
  slug: spothero-domain-security
  summary_line: TLSv1.3 · DMARC
slug: spothero
tags:
- Parking
- Mobility
- Transportation
- Navigation
- Reservations
website: https://spothero.com
---
