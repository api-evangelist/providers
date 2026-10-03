---
agent_readiness:
  band: agent-ready
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
    error_semantics: verified
    event_surface_described: false
    idempotency: na
    mcp_server: false
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 29.6
  scored_at: '2026-10-03'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Postfinder Io Agentic Access
  operation_count: 12
  slug: postfinder-io-agentic-access
  summary_line: 12 operations
api_count: 1
apis:
- baseURL: https://api.postfinder.io
  baseurl_source: declared
  description: 'What is nearest a coordinate: the question most callers are asking.'
  name: Postfinder Nearby API
  slug: postfinder-io-nearby-api
- baseURL: https://api.postfinder.io
  baseurl_source: declared
  description: 'The directory as the site''s pages have it: countries, regions, suburbs and places.'
  name: Postfinder Places API
  slug: postfinder-io-places-api
- baseURL: https://api.postfinder.io
  baseurl_source: declared
  description: Postcode lookup, in both directions.
  name: Postfinder Postcodes API
  slug: postfinder-io-postcodes-api
- baseURL: https://api.postfinder.io
  baseurl_source: declared
  description: This document.
  name: Postfinder Reference API
  slug: postfinder-io-reference-api
- baseURL: https://api.postfinder.io
  baseurl_source: declared
  description: Turn what somebody typed into a suburb or a place.
  name: Postfinder Search API
  slug: postfinder-io-search-api
artifact_total: 15
common:
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/postfinder-io/refs/heads/main/agentic-access/postfinder-io-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/postfinder-io-agentic-access.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/postfinder-io/refs/heads/main/rules/postfinder-io-rules.yml
  title: ''
  type: Spectral
  url: rules/postfinder-io-rules.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/postfinder-io/refs/heads/main/json-ld/postfinder-io-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/postfinder-io-context.jsonld
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/postfinder-io/refs/heads/main/vocabulary/postfinder-io-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/postfinder-io-vocabulary.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/postfinder-io/refs/heads/main/data-model/postfinder-io-data-model.yml
  title: ''
  type: DataModel
  url: data-model/postfinder-io-data-model.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/postfinder-io/refs/heads/main/errors/postfinder-io-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/postfinder-io-problem-types.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/postfinder-io/refs/heads/main/conformance/postfinder-io-conformance.yml
  title: ''
  type: Conformance
  url: conformance/postfinder-io-conformance.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/postfinder-io/refs/heads/main/llms/postfinder-io-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/postfinder-io-llms.txt
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/postfinder-io/refs/heads/main/hosts/postfinder-io-hosts.yml
  title: ''
  type: Hosts
  url: hosts/postfinder-io-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/postfinder-io/refs/heads/main/vendors/postfinder-io-vendors.yml
  title: ''
  type: Vendors
  url: vendors/postfinder-io-vendors.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/postfinder-io/refs/heads/main/packages/postfinder-io-packages.yml
  title: ''
  type: SDKs
  url: packages/postfinder-io-packages.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/postfinder-io/refs/heads/main/packages/postfinder-io-packages.yml
  title: ''
  type: Packages
  url: packages/postfinder-io-packages.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://postfinder.io/en/terms/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://postfinder.io/en/privacy/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://api.postfinder.io<!--
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/postfinder
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/postfinder-io/refs/heads/main/security/postfinder-io-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/postfinder-io-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://postfinder.io/
- group: docs
  title: ''
  type: Documentation
  url: https://postfinder.io/api/
created: '2026-10-02'
description: Postfinder provides an API for Australian address autocomplete and location lookup of post offices, parcel lockers, carrier drop‑off points and street post boxes. The service aggregates data from Australia Post, OpenStreetMap and carrier feeds, offering opening hours, addresses, maps and postcode lookup. Users can search by suburb, street address or postcode, and also browse locations by state or country, covering Australia, Canada, New Zealand, the United Kingdom and the United States. The API returns structured JSON suitable for integration into e‑commerce, logistics and mapping applications.
image: https://postfinder.io/og.png
json_schemas:
- name: CategoryResponse
  property_count: 2
  slug: postfinder-io-category-response
- name: CountriesResponse
  property_count: 2
  slug: postfinder-io-countries-response
- name: NearbyResponse
  property_count: 2
  slug: postfinder-io-nearby-response
- name: PlacesResponse
  property_count: 3
  slug: postfinder-io-places-response
- name: PostcodesResponse
  property_count: 2
  slug: postfinder-io-postcodes-response
- name: SearchResponse
  property_count: 2
  slug: postfinder-io-search-response
jsonld:
- class_count: 37
  name: Postfinder Io Context
  property_count: 59
  slug: postfinder-io-context
layout: provider
modified: '2026-10-02'
name: Postfinder
nav: Providers
network: true
overview: 'Postfinder publishes 5 APIs on the [APIs.io](https://apis.io/) network, including Nearby API, Places API, Postcodes API, and 2 more. Tagged areas include Company, Address, Autocomplete, Logistics, and Australia.


  The Postfinder catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Postfinder''s developer surface includes documentation and 18 more developer resources.'
random_paper: 5
rules:
- effective_rule_count: 55
  extends:
  - spectral:oas
  name: Postfinder API Rules
  rule_count: 14
  severity_counts:
    error: 13
    hint: 0
    info: 1
    warn: 0
  slug: postfinder-io-rules
score:
  band: developing
  composite: 43.1
  coverage:
    artifact_dirs: 17
    catalog_earned: 62.0
    catalog_earned_first_party: 0.0
    catalog_gap: 38.0
    catalog_max: 100.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 57.1
    contract_governance: 19.7
    contract_quality: 62.3
    developer_ergonomics: 26.2
    discoverability: 73.2
    operational_transparency: 5.3
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 5
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 18.6
  schema_version: 0.23.0
  scored_at: '2026-10-03'
  upsert:
    applies: false
    note: 'Not scored: this provider''s published contracts declare no write operations, and a read-only API cannot create-or-update. Excluded from the denominator, not zeroed.'
    reason: read_only
security:
- kind: domain-security
  name: Postfinder Io Domain Security
  slug: postfinder-io-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: postfinder-io
tags:
- Company
- Address
- Autocomplete
- Logistics
- Australia
website: https://postfinder.io/
---
