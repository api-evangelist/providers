---
access_model:
  confidence: high
  label: Free · Self-serve signup
  onboarding: self-serve
  pricing: free
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: true
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
  scored_at: '2026-08-24'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Ens Paris Agentic Access
  operation_count: 16
  slug: ens-paris-agentic-access
  summary_line: 16 operations
api_count: 4
apis:
- description: HAL-ENS is the open archive hosting the scientific production of ENS Paris researchers, teacher-researchers and doctoral students. It is part of the national HAL platform and is harvestable via the OA
  name: HAL-ENS Open Archive (OAI-PMH)
  slug: hal-oai-pmh
- description: 'The national HAL open-archive REST and Search API provides programmatic query access to publication metadata, including records deposited in the HAL-ENS portal. Results can be filtered by collection, '
  name: HAL Search / REST API
  slug: hal-api
- description: API to enumerate datasets
  name: École Normale Supérieure de Paris Catalog API
  slug: ens-paris-catalog-api
- description: API to work on records
  name: École Normale Supérieure de Paris Dataset API
  slug: ens-paris-dataset-api
artifact_total: 22
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Explore Catalog API
  slug: open-ens-paris-catalog-api
- collection_type: open
  name: Explore Catalog Dataset API
  slug: open-ens-paris-dataset-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/ens-paris-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/ens-paris-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/ens-paris-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://www.ens.psl.eu/en
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/school/ecole-normale-superieure/
- group: commercial
  title: ''
  type: Plans
  url: plans/ens-paris-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/ens-paris-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/ens-paris-finops.yml
- group: other
  title: ''
  type: Review
  url: review.yml
- group: design
  title: ''
  type: x-vocabulary
  url: vocabulary/ens-paris-vocabulary.yml
- group: design
  title: ''
  type: x-json-ld-context
  url: json-ld/ens-paris-context.jsonld
- group: company
  title: ''
  type: x-blogs
  url: blogs/blogs.json
created: '2026-06-03'
description: 'École Normale Supérieure de Paris (ENS, rue d''Ulm) is a leading French grande école and constituent member of Université PSL (Paris Sciences & Lettres), ranked #86 in the QS World University Rankings 2025. ENS operates 15 departments, 35 research laboratories and a network of libraries. ENS does not publish a first-party developer portal or documented institutional API; its programmatic surface is reached indirectly via national French research and higher-education open infrastructure. Researcher output is deposited in the HAL-ENS open archive, which is harvestable through the national HAL OAI-PMH endpoint and the HAL REST/Search API, and ENS establishment data is exposed through the Ministry of Higher Education (MESR) open-data platform''s Opendatasoft Explore API.'
examples:
- key_count: 4
  name: Ens Paris Query Dataset Records Example
  slug: ens-paris-query-dataset-records-example
- key_count: 4
  name: Ens Paris Query Datasets Example
  slug: ens-paris-query-datasets-example
finops:
- name: Ens Paris Finops
  service_category: Education
  slug: ens-paris-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/ens-paris.png
json_schemas:
- name: MESR Explore API Dataset
  property_count: 9
  slug: ens-paris-dataset
- name: MESR Explore API Records Response
  property_count: 3
  slug: ens-paris-records
json_structures:
- name: Ens Paris Dataset Structure
  property_count: 7
  slug: ens-paris-dataset-structure
- name: Ens Paris Records Structure
  property_count: 3
  slug: ens-paris-records-structure
jsonld:
- class_count: 20
  name: Ens Paris Context
  property_count: 2
  slug: ens-paris-context
layout: provider
modified: '2026-06-03'
name: École Normale Supérieure de Paris
nav: Providers
network: true
overview: 'École Normale Supérieure de Paris publishes 2 APIs on the [APIs.io](https://apis.io/) network: Catalog API and Dataset API. Tagged areas include Education, Higher Education, University, Research, and Open Data.


  The École Normale Supérieure de Paris catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  École Normale Supérieure de Paris'' developer surface includes authentication and 11 more developer resources.'
plans:
- name: Ens Paris Plans Pricing
  plan_count: 2
  slug: ens-paris-plans-pricing
random_paper: 11
rate_limits:
- limit_count: 1
  name: Ens Paris Rate Limits
  slug: ens-paris-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: École Normale Supérieure de Paris API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: ens-paris-jsonschema-spectral-rules
- effective_rule_count: 8
  extends: []
  name: École Normale Supérieure de Paris API Rules
  rule_count: 8
  severity_counts:
    error: 4
    hint: 0
    info: 1
    warn: 3
  slug: ens-paris-rules
score:
  band: thin
  composite: 37.9
  delta: 0.0
  facets:
    access_clarity: 28.9
    commercial_clarity: 28.9
    contract_governance: 9.8
    contract_quality: 71.4
    developer_ergonomics: 11.9
    discoverability: 74.1
    governance: 9.8
    operational_transparency: 21.1
  previous_composite: 37.9
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
    regime: Education & Research
    regime_id: education
    score: 31.5
  schema_version: 0.12.1
  scored_at: '2026-08-24'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/ens-paris/refs/heads/main/screenshots/ens-paris-2026-06-20T180723.png
security:
- kind: authentication
  name: Ens Paris Authentication
  slug: ens-paris-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Ens Paris Domain Security
  slug: ens-paris-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: ens-paris
tags:
- Education
- Higher Education
- University
- Research
- Open Data
- Open Access
- France
website: https://www.ens.psl.eu/en
---
