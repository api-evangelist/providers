---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
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
  scored_at: '2026-08-30'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Noaa Erddap Agentic Access
  operation_count: 9
  slug: noaa-erddap-agentic-access
  summary_line: 9 operations
api_count: 1
apis:
- description: Download subsets of tabular or gridded data.
  name: NOAA ERDDAP Data Access API
  slug: noaa-erddap-data-access-api
- description: Search and browse available datasets.
  name: NOAA ERDDAP Discovery API
  slug: noaa-erddap-discovery-api
- description: Browse and download raw files associated with a dataset.
  name: NOAA ERDDAP Files API
  slug: noaa-erddap-files-api
- description: Inspect variable and attribute metadata for a specific dataset.
  name: NOAA ERDDAP Metadata API
  slug: noaa-erddap-metadata-api
artifact_total: 20
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: ERDDAP REST Data Access API
  slug: open-noaa-erddap-data-access-api
- collection_type: open
  name: ERDDAP REST Data Access Discovery API
  slug: open-noaa-erddap-discovery-api
- collection_type: open
  name: ERDDAP REST Data Access Files API
  slug: open-noaa-erddap-files-api
- collection_type: open
  name: ERDDAP REST Data Access Metadata API
  slug: open-noaa-erddap-metadata-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/noaa-erddap-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/noaa-erddap-domain-security.yml
created: '2026-06-13'
description: NOAA Environmental Research Division Data Access Program (ERDDAP) is a free, publicly accessible REST API and data server that provides a simple, consistent way to search, subset, and download gridded and tabular oceanographic, meteorological, and climate science datasets in a wide variety of common file formats.
examples:
- key_count: 5
  name: Advanced Search
  slug: advanced-search
- key_count: 4
  name: Get Dataset Metadata
  slug: get-dataset-metadata
- key_count: 5
  name: Griddap Query
  slug: griddap-query
- key_count: 4
  name: Search Datasets
  slug: search-datasets
- key_count: 5
  name: Tabledap Query
  slug: tabledap-query
finops:
- name: Finops
  service_category: ''
  slug: finops
image: https://www.noaa.gov/sites/default/files/styles/crop_394x394/public/2022-03/NOAA_2022_logo.png
jsonld:
- class_count: 0
  name: Api Context
  property_count: 0
  slug: api
layout: provider
modified: '2026-06-13'
name: NOAA ERDDAP
nav: Providers
network: true
overview: 'NOAA ERDDAP publishes 4 APIs on the [APIs.io](https://apis.io/) network, including Data Access API, Discovery API, Files API, and 1 more. Tagged areas include oceanography, meteorology, climate, environmental data, and gridded data.


  The NOAA ERDDAP catalog on APIs.io includes 1 JSON-LD context.'
plans:
- name: Plans
  plan_count: 2
  slug: plans
random_paper: 13
rate_limits:
- limit_count: 0
  name: Rate Limits
  slug: rate-limits
score:
  band: thin
  composite: 31.6
  coverage:
    artifact_dirs: 10
    catalog_gap: 62.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: -0.6
  facets:
    access_clarity: 39.5
    commercial_clarity: 39.5
    contract_governance: 0.0
    contract_quality: 56.2
    developer_ergonomics: 9.5
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 32.2
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 4
  regulatory:
    applies: true
    matched_via: tags
    regime: Government & Public Sector
    regime_id: government
    score: 27.8
  schema_version: 0.17.2
  scored_at: '2026-08-30'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/noaa-erddap/refs/heads/main/screenshots/noaa-erddap-2026-06-20T190341.png
security:
- kind: domain-security
  name: Noaa Erddap Domain Security
  slug: noaa-erddap-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: noaa-erddap
tags:
- oceanography
- meteorology
- climate
- environmental data
- gridded data
- tabular data
- scientific data
- government
- NOAA
- open data
---
