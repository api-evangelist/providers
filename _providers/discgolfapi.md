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
    mcp_server: false
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 22.9
  scored_at: '2026-08-30'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Discgolfapi Agentic Access
  operation_count: 6
  slug: discgolfapi-agentic-access
  summary_line: 6 operations
api_count: 1
apis:
- description: Country coverage index.
  name: DiscGolfAPI Countries API
  slug: discgolfapi-countries-api
- description: Course list and course detail endpoints.
  name: DiscGolfAPI Courses API
  slug: discgolfapi-courses-api
- description: Dataset manifest and publication metadata.
  name: DiscGolfAPI Metadata API
  slug: discgolfapi-metadata-api
- description: Region, state and subdivision coverage index.
  name: DiscGolfAPI Regions API
  slug: discgolfapi-regions-api
- description: Recent public data updates.
  name: DiscGolfAPI Updates API
  slug: discgolfapi-updates-api
artifact_total: 27
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: DiscGolf Countries API
  slug: open-discgolfapi-countries-api
- collection_type: open
  name: DiscGolf Countries Courses API
  slug: open-discgolfapi-courses-api
- collection_type: open
  name: DiscGolf Countries Metadata API
  slug: open-discgolfapi-metadata-api
- collection_type: open
  name: DiscGolf Countries Regions API
  slug: open-discgolfapi-regions-api
- collection_type: open
  name: DiscGolf Countries Updates API
  slug: open-discgolfapi-updates-api
- collection_type: open
  name: DiscGolfAPI
  slug: open-discgolfapi
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/discgolfapi-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/discgolfapi-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/discgolfapi-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://discgolfapi.com/
- group: docs
  title: ''
  type: Documentation
  url: https://discgolfapi.com/docs/
- group: other
  title: ''
  type: APIsJSON
  url: https://discgolfapi.com/apis.json
- group: docs
  title: ''
  type: OpenAPI
  url: https://discgolfapi.com/openapi.json
- group: commercial
  title: ''
  type: TermsOfService
  url: https://discgolfapi.com/terms/
- group: commercial
  title: ''
  type: License
  url: https://discgolfapi.com/licence/
- group: operate
  title: ''
  type: Contact
  url: https://discgolfapi.com/contact/
- group: agent
  title: ''
  type: LlmsText
  url: https://discgolfapi.com/llms.txt
- group: other
  title: ''
  type: RobotsTxt
  url: https://discgolfapi.com/robots.txt
- group: docs
  title: ''
  type: Schema
  url: https://discgolfapi.com/schema/
- group: other
  title: ''
  type: Coverage
  url: https://discgolfapi.com/coverage/
- group: operate
  title: ''
  type: ChangeLog
  url: https://discgolfapi.com/changelog/
- group: other
  title: ''
  type: Use Our Data
  url: https://discgolfapi.com/use-our-data/
created: '2026-05-03'
description: DiscGolfAPI is a free, read-only public API that publishes structured JSON data about disc golf courses for developers, clubs, publishers, apps, and AI systems. It provides machine-readable course records with names, locations, countries, regions, hole counts where known, coordinates where available, operational and access fields, confidence and verification signals, update timestamps, and attribution/licence metadata. DiscGolfAPI is infrastructure and reference data — not a review site, rating platform, or social network.
examples:
- key_count: 4
  name: Discgolfapi Get Course Example
  slug: discgolfapi-get-course-example
- key_count: 4
  name: Discgolfapi List Courses Example
  slug: discgolfapi-list-courses-example
- key_count: 4
  name: Discgolfapi Manifest Example
  slug: discgolfapi-manifest-example
finops:
- name: Discgolfapi Finops
  service_category: Open Data API
  slug: discgolfapi-finops
image: https://discgolfapi.com/wp-content/themes/blocksy-child/assets/blue.png
json_schemas:
- name: DiscGolfAPI Course
  property_count: 22
  slug: discgolfapi-course
- name: DiscGolfAPI Manifest
  property_count: 7
  slug: discgolfapi-manifest
json_structures:
- name: Discgolfapi Course Structure
  property_count: 0
  slug: discgolfapi-course-structure
jsonld:
- class_count: 0
  name: Discgolfapi Context
  property_count: 56
  slug: discgolfapi-context
layout: provider
modified: '2026-05-19'
name: DiscGolfAPI
nav: Providers
network: true
overview: 'DiscGolfAPI publishes 5 APIs on the [APIs.io](https://apis.io/) network, including Countries API, Courses API, Metadata API, and 2 more. Tagged areas include Disc Golf, Sports, Courses, Open Data, and Recreation.


  The DiscGolfAPI catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  DiscGolfAPI''s developer surface includes documentation, changelog, and 14 more developer resources.'
plans:
- name: Discgolfapi Plans Pricing
  plan_count: 2
  slug: discgolfapi-plans-pricing
random_paper: 2
rate_limits:
- limit_count: 2
  name: Discgolfapi Rate Limits
  slug: discgolfapi-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: DiscGolfAPI API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: discgolfapi-jsonschema-spectral-rules
- effective_rule_count: 56
  extends:
  - spectral:oas
  name: DiscGolfAPI API Rules
  rule_count: 15
  severity_counts:
    error: 4
    hint: 0
    info: 3
    warn: 8
  slug: discgolfapi-rules
score:
  band: developing
  composite: 44.3
  coverage:
    artifact_dirs: 16
    catalog_gap: 34.5
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: -0.5
  facets:
    access_clarity: 39.5
    commercial_clarity: 39.5
    contract_governance: 28.8
    contract_quality: 66.5
    developer_ergonomics: 9.5
    discoverability: 70.4
    governance: 28.8
    operational_transparency: 36.8
  previous_composite: 44.8
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 5
  regulatory:
    applies: true
    matched_via: tags
    regime: Government & Public Sector
    regime_id: government
    score: 38.9
  schema_version: 0.17.2
  scored_at: '2026-08-30'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/discgolfapi/refs/heads/main/screenshots/discgolfapi-2026-06-20T180032.png
security:
- kind: domain-security
  name: Discgolfapi Domain Security
  slug: discgolfapi-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Discgolfapi Vulnerability Disclosure
  slug: discgolfapi-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: discgolfapi
tags:
- Disc Golf
- Sports
- Courses
- Open Data
- Recreation
website: https://discgolfapi.com/
---
