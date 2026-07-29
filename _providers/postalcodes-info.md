---
access_model:
  confidence: medium
  label: Free
  onboarding: unknown
  pricing: free
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
    asyncapi_events: false
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: partial
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 24.8
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Postalcodes Info Agentic Access
  operation_count: 5
  slug: postalcodes-info-agentic-access
  summary_line: 5 operations
api_count: 3
apis:
- description: Country-level CSV, XLSX and JSON exports.
  name: PostalCodes.info Downloads API
  slug: postalcodes-info-downloads-api
- description: Canonical HTML pages for manual review and citation.
  name: PostalCodes.info Lookup Pages API
  slug: postalcodes-info-lookup-pages-api
- description: Interactive postal-code and locality lookup.
  name: PostalCodes.info Search API
  slug: postalcodes-info-search-api
artifact_total: 23
collections:
- collection_type: open
  name: PostalCodes.info Postal Code Reference API
  slug: open-postalcodes-info
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/postalcodes-info-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/postalcodes-info-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://postalcodes.info/
- group: docs
  title: ''
  type: Documentation
  url: https://postalcodes.info/api
- group: docs
  title: ''
  type: Dataset Documentation
  url: https://postalcodes.info/datasets
- group: docs
  title: ''
  type: OpenAPI
  url: https://postalcodes.info/openapi.json
- group: commercial
  title: ''
  type: License
  url: https://postalcodes.info/licensing
- group: commercial
  title: ''
  type: License
  url: https://opendatacommons.org/licenses/odbl/1-0/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://postalcodes.info/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://postalcodes.info/privacy
- group: operate
  title: ''
  type: Contact
  url: https://postalcodes.info/contact
- group: other
  title: ''
  type: DataSources
  url: https://postalcodes.info/data-sources
- group: other
  title: ''
  type: UpdatePolicy
  url: https://postalcodes.info/update-policy
- group: other
  title: ''
  type: APIsJSON
  url: https://raw.githubusercontent.com/PabloCirre/postalcodes-info-open-data/main/apis.json
- group: build
  title: ''
  type: GitHub
  url: https://github.com/PabloCirre/postalcodes-info-open-data
- group: other
  title: ''
  type: Citation
  url: https://zenodo.org/records/19493709
- group: other
  title: ''
  type: MethodologyNote
  url: https://zenodo.org/records/19930578
- group: other
  title: ''
  type: CoverageBenchmark
  url: https://zenodo.org/records/19930688
created: '2026-05-16'
description: Postal-code lookup, search, country exports, and address validation worldwide. PostalCodes.info publishes a same-origin reference API and bulk CSV / JSON / XLSX downloads for 123+ countries, anchored on GeoNames and national open-data feeds, released under the Open Database License (ODbL) 1.0.
examples:
- key_count: 6
  name: Postalcodes Info Create Download Token Example
  slug: postalcodes-info-create-download-token-example
- key_count: 7
  name: Postalcodes Info Download Country Dataset Example
  slug: postalcodes-info-download-country-dataset-example
- key_count: 6
  name: Postalcodes Info Get Country Lookup Page Example
  slug: postalcodes-info-get-country-lookup-page-example
- key_count: 2
  name: Postalcodes Info Postal Record Example
  slug: postalcodes-info-postal-record-example
- key_count: 5
  name: Postalcodes Info Preview Country Records Example
  slug: postalcodes-info-preview-country-records-example
- key_count: 5
  name: Postalcodes Info Search Postal Codes Example
  slug: postalcodes-info-search-postal-codes-example
- key_count: 2
  name: Postalcodes Info Search Suggestion Example
  slug: postalcodes-info-search-suggestion-example
finops:
- name: Postalcodes Info Finops
  service_category: ''
  slug: postalcodes-info-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/postalcodes-info.png
json_schemas:
- name: Error
  property_count: 1
  slug: postalcodes-info-error
- name: PostalRecord
  property_count: 8
  slug: postalcodes-info-postal-record
- name: SearchSuggestion
  property_count: 4
  slug: postalcodes-info-search-suggestion
json_structures:
- name: Postalcodes Info Postal Record Structure
  property_count: 0
  slug: postalcodes-info-postal-record-structure
jsonld:
- class_count: 11
  name: Postalcodes Info Context
  property_count: 8
  slug: postalcodes-info-context
layout: provider
modified: '2026-05-19'
name: PostalCodes.info
nav: Providers
network: true
overview: 'PostalCodes.info publishes 3 APIs on the [APIs.io](https://apis.io/) network: Downloads API, Lookup Pages API, and Search API. Tagged areas include Postal Codes, Geocoding, Open Data, Address Validation, and Logistics.


  The PostalCodes.info catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  PostalCodes.info''s developer surface includes documentation, GitHub presence, and 16 more developer resources.'
plans:
- name: Postalcodes Info Plans Pricing
  plan_count: 1
  slug: postalcodes-info-plans-pricing
random_paper: 41
rate_limits:
- limit_count: 0
  name: Postalcodes Info Rate Limits
  slug: postalcodes-info-rate-limits
rules:
- name: PostalCodes.info API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: postalcodes-info-jsonschema-spectral-rules
- name: PostalCodes.info API Rules
  rule_count: 11
  severity_counts:
    error: 4
    hint: 0
    info: 1
    warn: 6
  slug: postalcodes-info-rules
score:
  band: developing
  composite: 42.5
  delta: -5.0
  facets:
    commercial_clarity: 50.0
    contract_quality: 67.8
    developer_ergonomics: 8.7
    discoverability: 74.1
    governance: 58.3
    operational_transparency: 5.3
  previous_composite: 47.5
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 3
  regulatory:
    applies: true
    matched_via: tags
    regime: Government & Public Sector
    regime_id: government
    score: 35.2
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: falling
screenshot: https://raw.githubusercontent.com/api-evangelist/postalcodes-info/refs/heads/main/screenshots/postalcodes-info-2026-06-20T191947.png
security:
- kind: domain-security
  name: Postalcodes Info Domain Security
  slug: postalcodes-info-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: postalcodes-info
tags:
- Postal Codes
- Geocoding
- Open Data
- Address Validation
- Logistics
website: https://postalcodes.info/
---
