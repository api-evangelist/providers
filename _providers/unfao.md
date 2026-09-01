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
  scored_at: '2026-09-01'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Unfao Agentic Access
  operation_count: 11
  slug: unfao-agentic-access
  summary_line: 11 operations
api_count: 2
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
artifact_total: 26
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: FAOSTAT Bulk Download Catalog API
  slug: open-unfao-catalog-api
- collection_type: open
  name: FAOSTAT Bulk Download Catalog Data API
  slug: open-unfao-data-api
- collection_type: open
  name: FAOSTAT Bulk Download Catalog Dimensions API
  slug: open-unfao-dimensions-api
- collection_type: open
  name: FAOSTAT Bulk Download Catalog Domains API
  slug: open-unfao-domains-api
- collection_type: open
  name: FAOSTAT Bulk Download Catalog Downloads API
  slug: open-unfao-downloads-api
- collection_type: open
  name: FAOSTAT Bulk Download Catalog Metadata API
  slug: open-unfao-metadata-api
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
overview: 'FAO FAOSTAT publishes 6 APIs on the [APIs.io](https://apis.io/) network, including Catalog API, Data API, Dimensions API, and 3 more. Tagged areas include Agriculture, Food Security, Statistics, Trade, and Land Use.


  The FAO FAOSTAT catalog on APIs.io includes 2 JSON-LD contexts and 1 Spectral governance ruleset.'
plans:
- name: Plans
  plan_count: 1
  slug: plans
random_paper: 12
rate_limits:
- limit_count: 0
  name: Rate Limits
  slug: rate-limits
rules:
- effective_rule_count: 4
  extends: []
  name: FAO FAOSTAT API Rules
  rule_count: 4
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 3
  slug: unfao-jsonschema-spectral-rules
score:
  band: thin
  composite: 31.2
  coverage:
    artifact_dirs: 13
    catalog_gap: 52.8
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 28.9
    commercial_clarity: 28.9
    contract_governance: 9.8
    contract_quality: 59.8
    developer_ergonomics: 9.5
    discoverability: 75.9
    governance: 9.8
    operational_transparency: 0.0
  previous_composite: 31.2
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 6
  regulatory:
    applies: true
    matched_via: tags
    regime: Government & Public Sector
    regime_id: government
    score: 20.4
  schema_version: 0.17.2
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/unfao/refs/heads/main/screenshots/unfao-2026-06-20T200026.png
security:
- kind: domain-security
  name: Unfao Domain Security
  slug: unfao-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: unfao
tags:
- Agriculture
- Food Security
- Statistics
- Trade
- Land Use
- Environment
- UN
- Open Data
website: https://www.fao.org/faostat/en/
---
