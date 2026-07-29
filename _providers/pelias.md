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
    asyncapi_events: false
    auth_clarity: false
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
  score: 27.9
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Pelias Agentic Access
  operation_count: 5
  slug: pelias-agentic-access
  summary_line: 5 operations
api_count: 4
apis:
- description: Real-time type-ahead geocoding for user input
  name: Pelias Autocomplete API
  slug: pelias-autocomplete-api
- description: Convert text or addresses into geographic coordinates
  name: Pelias Forward Geocoding API
  slug: pelias-forward-geocoding-api
- description: Retrieve details for a known place by ID
  name: Pelias Place Lookup API
  slug: pelias-place-lookup-api
- description: Convert geographic coordinates into places and addresses
  name: Pelias Reverse Geocoding API
  slug: pelias-reverse-geocoding-api
artifact_total: 15
common:
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
overview: 'Pelias publishes 4 APIs on the [APIs.io](https://apis.io/) network, including Autocomplete API, Forward Geocoding API, Place Lookup API, and 1 more. Tagged areas include geocoding, reverse geocoding, geospatial, open source, and elasticsearch.


  The Pelias catalog on APIs.io includes 1 Spectral governance ruleset.


  Pelias'' developer surface includes documentation, status page, support, and 6 more developer resources.'
plans:
- name: Plans
  plan_count: 5
  slug: plans
random_paper: 6
rate_limits:
- limit_count: 0
  name: Rate Limits
  slug: rate-limits
rules:
- name: Pelias API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: pelias-jsonschema-spectral-rules
score:
  band: thin
  composite: 39.1
  delta: -4.2
  facets:
    commercial_clarity: 39.5
    contract_quality: 54.2
    developer_ergonomics: 13.0
    discoverability: 74.1
    governance: 58.3
    operational_transparency: 5.3
  previous_composite: 43.3
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 4
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/pelias/refs/heads/main/screenshots/pelias-2026-06-20T191527.png
security:
- kind: domain-security
  name: Pelias Domain Security
  slug: pelias-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: pelias
tags:
- geocoding
- reverse geocoding
- geospatial
- open source
- elasticsearch
- openstreetmap
- addresses
- places
- autocomplete
website: https://pelias.io
---
