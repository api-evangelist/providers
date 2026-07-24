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
    agent_skills: false
    agentic_access: true
    asyncapi_events: false
    auth_clarity: false
    consent_identity: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: true
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.1
  score: 38.5
  scored_at: '2026-07-23'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Unfao Agentic Access
  operation_count: 11
  slug: unfao-agentic-access
  summary_line: 11 operations
api_count: 7
apis:
- description: API for bulk downloading complete datasets for any FAOSTAT domain as zipped CSV files. The catalog endpoint lists all available datasets with download URLs and last-updated dates.
  name: FAOSTAT Bulk Download API
  slug: faostat-bulk-download-api
- description: Browse available bulk datasets
  name: FAO FAOSTAT Catalog API
  slug: unfao-catalog-api
- description: Operations for retrieving FAOSTAT statistical data
  name: FAO FAOSTAT Data API
  slug: unfao-data-api
- description: Operations for querying dimension members (areas, items, elements, years, flags)
  name: FAO FAOSTAT Dimensions API
  slug: unfao-dimensions-api
- description: Operations for browsing available FAOSTAT domains and groups
  name: FAO FAOSTAT Domains API
  slug: unfao-domains-api
- description: Download complete domain datasets as ZIP archives
  name: FAO FAOSTAT Downloads API
  slug: unfao-downloads-api
- description: Operations for retrieving dataset and indicator metadata
  name: FAO FAOSTAT Metadata API
  slug: unfao-metadata-api
artifact_total: 19
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/unfao-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/unfao-domain-security.yml
created: '2026-06-13'
description: The Food and Agriculture Organization (FAO) of the United Nations operates FAOSTAT, the world's largest freely accessible database for food and agriculture statistics. FAOSTAT provides REST APIs for programmatic access to agricultural production data, food security indicators, trade flows, land use, environmental indicators, food balances, and prices covering 180+ countries from 1961 to present across 70+ thematic domains.
examples:
- key_count: 3
  name: Data Query Crops
  slug: data-query-crops
- key_count: 3
  name: Domains List
  slug: domains-list
finops:
- name: Finops
  service_category: ''
  slug: finops
image: https://www.fao.org/favicon.ico
json_schemas:
- name: FAOSTAT Data Record
  property_count: 17
  slug: data-record
- name: FAOSTAT Domain
  property_count: 5
  slug: domain
jsonld:
- class_count: 7
  name: Faostat Context
  property_count: 30
  slug: faostat-context
- class_count: 0
  name: Faostat Dataset Context
  property_count: 0
  slug: faostat-dataset
layout: provider
modified: '2026-06-13'
name: FAO FAOSTAT
nav: Providers
network: true
overview: 'FAO FAOSTAT publishes 6 APIs on the [APIs.io](https://apis.io/) network, including Catalog API, Data API, Dimensions API, and 3 more. Tagged areas include agriculture, food security, statistics, trade, and land use.


  The FAO FAOSTAT catalog on APIs.io includes 2 JSON-LD contexts and 1 Spectral governance ruleset.'
plans:
- name: Plans
  plan_count: 1
  slug: plans
random_paper: 27
rate_limits:
- limit_count: 0
  name: Rate Limits
  slug: rate-limits
rules:
- name: FAO FAOSTAT API Rules
  rule_count: 4
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 3
  slug: unfao-jsonschema-spectral-rules
score:
  band: thin
  composite: 38.3
  delta: -2.5
  facets:
    commercial_clarity: 28.9
    contract_quality: 64.9
    developer_ergonomics: 0.0
    discoverability: 100.0
    governance: 73.7
    operational_transparency: 0.0
  previous_composite: 40.8
  regulatory:
    applies: true
    regime: Government & Public Sector
    regime_id: government
    score: 23.9
  schema_version: 0.5
  scored_at: '2026-07-23'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/unfao/refs/heads/main/screenshots/unfao-2026-06-20T200026.png
security:
- kind: domain-security
  name: Unfao Domain Security
  slug: unfao-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: unfao
tags:
- agriculture
- food security
- statistics
- trade
- land use
- environment
- UN
- open data
website: https://www.fao.org/faostat/en/
---
