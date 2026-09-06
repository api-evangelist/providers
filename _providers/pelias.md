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
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 25.8
  scored_at: '2026-09-05'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Pelias Agentic Access
  operation_count: 5
  slug: pelias-agentic-access
  summary_line: 5 operations
api_count: 1
apis:
- baseURL: https://api.geocode.earth/v1
  baseurl_source: declared
  description: Real-time type-ahead geocoding for user input
  name: Pelias Autocomplete API
  slug: pelias-autocomplete-api
- baseURL: https://api.geocode.earth/v1
  baseurl_source: declared
  description: Convert text or addresses into geographic coordinates
  name: Pelias Forward Geocoding API
  slug: pelias-forward-geocoding-api
- baseURL: https://api.geocode.earth/v1
  baseurl_source: declared
  description: Retrieve details for a known place by ID
  name: Pelias Place Lookup API
  slug: pelias-place-lookup-api
- baseURL: https://api.geocode.earth/v1
  baseurl_source: declared
  description: Convert geographic coordinates into places and addresses
  name: Pelias Reverse Geocoding API
  slug: pelias-reverse-geocoding-api
artifact_total: 20
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Pelias Geocoding Autocomplete API
  slug: open-pelias-autocomplete-api
- collection_type: open
  name: Pelias Geocoding Autocomplete Forward Geocoding API
  slug: open-pelias-forward-geocoding-api
- collection_type: open
  name: Pelias Geocoding Autocomplete Place Lookup API
  slug: open-pelias-place-lookup-api
- collection_type: open
  name: Pelias Geocoding Autocomplete Reverse Geocoding API
  slug: open-pelias-reverse-geocoding-api
common:
- group: build
  title: ''
  type: CodeOfConduct
  url: https://github.com/pelias/pelias/blob/master/CODE_OF_CONDUCT.md
- group: docs
  title: ''
  type: ContributionGuide
  url: https://github.com/pelias/pelias/blob/master/CONTRIBUTING.md
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/pelias-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/pelias-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://pelias.io
- group: docs
  title: ''
  type: Documentation
  url: https://github.com/pelias/documentation
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/pelias
- group: commercial
  title: ''
  type: License
  url: https://github.com/pelias/pelias/blob/master/LICENSE
- group: other
  title: ''
  type: HostedService
  url: https://geocode.earth
- group: operate
  title: ''
  type: Status
  url: https://github.com/pelias/pelias/issues
- group: operate
  title: ''
  type: Support
  url: https://gitter.im/pelias/pelias
created: '2026-06-13'
description: Pelias is a modular, open-source geocoding search engine built on Elasticsearch that converts addresses and place names into geographic coordinates (forward geocoding) and geographic coordinates into places and addresses (reverse geocoding). Powered entirely by open data from OpenStreetMap, OpenAddresses, Who's on First, and Geonames, it is freely available under the MIT license and can be self-hosted or accessed via hosted services.
examples:
- key_count: 3
  name: Autocomplete
  slug: autocomplete
- key_count: 3
  name: Reverse
  slug: reverse
- key_count: 3
  name: Search
  slug: search
- key_count: 3
  name: Structured
  slug: structured
finops:
- name: Finops
  service_category: ''
  slug: finops
image: https://pelias.io/images/pelias-logo.png
json_schemas:
- name: Pelias Geocoding Response
  property_count: 4
  slug: geocoding-response
layout: provider
modified: '2026-06-13'
name: Pelias
nav: Providers
network: true
overview: 'Pelias publishes 4 APIs on the [APIs.io](https://apis.io/) network, including Autocomplete API, Forward Geocoding API, Place Lookup API, and 1 more. Tagged areas include Geocoding, Reverse Geocoding, Geospatial, Open-Source, and Elasticsearch.


  The Pelias catalog on APIs.io includes 1 Spectral governance ruleset.


  Pelias'' developer surface includes documentation, status page, support, and 8 more developer resources.'
plans:
- name: Plans
  plan_count: 5
  slug: plans
random_paper: 8
rate_limits:
- limit_count: 0
  name: Rate Limits
  slug: rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: Pelias API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: pelias-jsonschema-spectral-rules
score:
  band: thin
  composite: 31.4
  coverage:
    artifact_dirs: 13
    catalog_earned: 55.3
    catalog_earned_first_party: 0.0
    catalog_gap: 59.8
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 39.5
    commercial_clarity: 39.5
    contract_governance: 9.8
    contract_quality: 53.1
    developer_ergonomics: 9.5
    discoverability: 68.5
    governance: 9.8
    operational_transparency: 2.6
  previous_composite: 31.4
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 4
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/pelias/refs/heads/main/screenshots/pelias-2026-06-20T191527.png
security:
- kind: domain-security
  name: Pelias Domain Security
  slug: pelias-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: pelias
tags:
- Geocoding
- Reverse Geocoding
- Geospatial
- Open-Source
- Elasticsearch
- OpenStreetMap
- Addresses
- Places
- Autocomplete
website: https://pelias.io
---
