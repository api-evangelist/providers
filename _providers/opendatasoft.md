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
    dry_run_mode: na
    error_semantics: false
    event_surface_described: false
    idempotency: na
    mcp_server: false
    openapi_examples: verified
    rate_limit_signal: documented
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 41.8
  scored_at: '2026-08-19'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Opendatasoft Agentic Access
  operation_count: 16
  slug: opendatasoft-agentic-access
  summary_line: 16 operations
api_count: 4
apis:
- description: 'OData 3.0 and 4.0 compliant REST API for querying Opendatasoft datasets using standard OData query parameters including filtering, sorting, pagination, field selection, and full-text search. Supports '
  name: Opendatasoft OData API
  slug: opendatasoft-odata-api
- description: 'Legacy REST API (v1) for searching datasets and records on Opendatasoft portals. Supports dataset search, dataset lookup, records search, records lookup, analysis, download, geo clustering, real-time '
  name: Opendatasoft Explore API v1 (Deprecated)
  slug: opendatasoft-explore-api-v1-deprecated
- description: API to enumerate datasets
  name: Opendatasoft Catalog API
  slug: opendatasoft-catalog-api
- description: API to work on records
  name: Opendatasoft Dataset API
  slug: opendatasoft-dataset-api
artifact_total: 30
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Explore Catalog API
  slug: open-opendatasoft-catalog-api
- collection_type: open
  name: Explore Catalog Dataset API
  slug: open-opendatasoft-dataset-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/opendatasoft-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/opendatasoft-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/opendatasoft-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/opendatasoft-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://www.huwise.com/en/
- group: company
  title: ''
  type: LegacyWebsite
  url: https://www.opendatasoft.com/
- group: other
  title: ''
  type: Developer
  url: https://help.opendatasoft.com/
- group: operate
  title: ''
  type: Community
  url: https://community.huwise.com/p/help
- group: build
  title: ''
  type: GitHub
  url: https://github.com/opendatasoft
- group: company
  title: ''
  type: Blog
  url: https://www.huwise.com/en/blog/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.huwise.com/en/privacy-policy/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.huwise.com/en/terms-of-use/
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/api-evangelist/workspace/opendatasoft
- group: auth
  title: ''
  type: Authentication
  url: https://help.opendatasoft.com/apis/ods-explore-v2/#section/Authentication
- group: commercial
  title: ''
  type: Plans
  url: https://raw.githubusercontent.com/api-evangelist/opendatasoft/refs/heads/main/plans/opendatasoft-explore-api.yml
- group: operate
  title: ''
  type: RateLimits
  url: https://raw.githubusercontent.com/api-evangelist/opendatasoft/refs/heads/main/rate-limits/opendatasoft-explore-api.yml
- group: commercial
  title: ''
  type: FinOps
  url: https://raw.githubusercontent.com/api-evangelist/opendatasoft/refs/heads/main/finops/opendatasoft.yml
created: '2026-06-13'
description: Open data platform with REST APIs for accessing public datasets from 1,000+ cities and organizations, providing standard OData and JSON query interfaces. Now operating as Huwise, the platform powers 3,000+ data marketplaces and provides catalog, records, analysis, and export APIs across public portals worldwide.
examples:
- key_count: 2
  name: Catalog Datasets Search
  slug: catalog-datasets-search
- key_count: 3
  name: Dataset Export Csv
  slug: dataset-export-csv
- key_count: 2
  name: Dataset Facets
  slug: dataset-facets
- key_count: 2
  name: Dataset Records Query
  slug: dataset-records-query
finops:
- name: Opendatasoft
  service_category: ''
  slug: opendatasoft
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/opendatasoft.png
json_schemas:
- name: Attachment
  property_count: 2
  slug: attachment
- name: Dataset
  property_count: 9
  slug: dataset
- name: Datasets
  property_count: 3
  slug: datasets
- name: Enum Format Datasets
  property_count: 0
  slug: enum-format-datasets
- name: Facet Enumeration
  property_count: 2
  slug: facet_enumeration
- name: Facet Value Enumeration
  property_count: 4
  slug: facet_value_enumeration
- name: Links
  property_count: 2
  slug: links
- name: Record
  property_count: 4
  slug: record
- name: Records
  property_count: 3
  slug: records
jsonld:
- class_count: 4
  name: Opendatasoft Context
  property_count: 46
  slug: opendatasoft-context
layout: provider
modified: '2026-06-13'
name: Opendatasoft
nav: Providers
network: true
overview: 'Opendatasoft publishes 2 APIs on the [APIs.io](https://apis.io/) network: Catalog API and Dataset API. Tagged areas include Open Data, Datasets, Public Data, OData, and REST.


  The Opendatasoft catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Opendatasoft''s developer surface includes authentication, GitHub presence, engineering blog, and 14 more developer resources.'
plans:
- name: Opendatasoft Explore Api
  plan_count: 3
  slug: opendatasoft-explore-api
random_paper: 7
rate_limits:
- limit_count: 4
  name: Opendatasoft Explore Api
  slug: opendatasoft-explore-api
- limit_count: 3
  name: Opendatasoft Odata Api
  slug: opendatasoft-odata-api
rules:
- effective_rule_count: 5
  extends: []
  name: Opendatasoft API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: opendatasoft-jsonschema-spectral-rules
score:
  band: developing
  composite: 47.5
  delta: -5.5
  facets:
    access_clarity: 50.0
    commercial_clarity: 50.0
    contract_governance: 9.8
    contract_quality: 64.4
    developer_ergonomics: 19.0
    discoverability: 74.1
    governance: 9.8
    operational_transparency: 36.8
  previous_composite: 53.0
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 2
  regulatory:
    applies: true
    matched_via: tags
    regime: Government & Public Sector
    regime_id: government
    score: 50.0
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: falling
screenshot: https://raw.githubusercontent.com/api-evangelist/opendatasoft/refs/heads/main/screenshots/opendatasoft-2026-06-20T190954.png
security:
- kind: authentication
  name: Opendatasoft Authentication
  slug: opendatasoft-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Opendatasoft Domain Security
  slug: opendatasoft-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Opendatasoft Vulnerability Disclosure
  slug: opendatasoft-vulnerability-disclosure
  summary_line: disclosure policy published
slug: opendatasoft
tags:
- Open Data
- Datasets
- Public Data
- OData
- REST
- Government
- Cities
website: https://www.huwise.com/en/
---
