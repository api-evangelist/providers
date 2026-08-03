---
access_model:
  confidence: high
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: true
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 30.6
  scored_at: '2026-08-03'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Data Analysis Tools Bureau Of Justice Statistics Agentic Access
  operation_count: 4
  slug: data-analysis-tools-bureau-of-justice-statistics-agentic-access
  summary_line: 4 operations
api_count: 2
apis:
- description: National Crime Victimization Survey datasets.
  name: Bureau of Justice Statistics Data Analysis Tools NCVS API
  slug: data-analysis-tools-bureau-of-justice-statistics-ncvs-api
- description: NIBRS national-estimates datasets.
  name: Bureau of Justice Statistics Data Analysis Tools NIBRS API
  slug: data-analysis-tools-bureau-of-justice-statistics-nibrs-api
artifact_total: 14
collections:
- collection_type: open
  name: BJS NCVS API
  slug: open-bjs-ncvs-api
- collection_type: open
  name: BJS NIBRS National Estimates API
  slug: open-bjs-nibrs-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/data-analysis-tools-bureau-of-justice-statistics-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/data-analysis-tools-bureau-of-justice-statistics-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/data-analysis-tools-bureau-of-justice-statistics-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/bureau-of-justice-statistics
- group: company
  title: ''
  type: Website
  url: https://bjs.ojp.gov/
- group: build
  title: ''
  type: Data Analysis Tools
  url: https://bjs.ojp.gov/data/data-analysis-tools
- group: build
  title: ''
  type: Data Collections
  url: https://bjs.ojp.gov/data-collections
- group: other
  title: ''
  type: Publications
  url: https://bjs.ojp.gov/library
- group: other
  title: ''
  type: DOJ Developer
  url: https://www.justice.gov/developer
- group: design
  title: ''
  type: JSONLD
  url: json-ld/bjs-context.jsonld
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/bjs-vocabulary.yml
created: '2024-11-30'
description: The Bureau of Justice Statistics (BJS) is the agency within the U.S. Department of Justice responsible for collecting, analysing, and disseminating crime, criminal-justice, expenditure, and victimisation data. BJS exposes selected datasets through Socrata Open Data APIs and offers interactive data analysis tools such as the Justice Expenditure and Employment Tool (JEET) and the National Crime Victimization Survey (NCVS) Quick Tables.
finops:
- name: Data Analysis Tools Bureau Of Justice Statistics Finops
  service_category: API
  slug: data-analysis-tools-bureau-of-justice-statistics-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/data-analysis-tools-bureau-of-justice-statistics.png
json_schemas:
- name: BJSDatasetRow
  property_count: 4
  slug: bjs-dataset-row
jsonld:
- class_count: 3
  name: Bjs Context
  property_count: 5
  slug: bjs-context
layout: provider
modified: '2026-05-19'
name: Bureau of Justice Statistics Data Analysis Tools
nav: Providers
network: true
overview: 'Bureau of Justice Statistics Data Analysis Tools publishes 2 APIs on the [APIs.io](https://apis.io/) network: NCVS API and NIBRS API. Tagged areas include Crime Statistics, Federal Government, NCVS, NIBRS, and Open Data.


  The Bureau of Justice Statistics Data Analysis Tools catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Bureau of Justice Statistics Data Analysis Tools'' developer surface includes authentication and 10 more developer resources.'
plans:
- name: Data Analysis Tools Bureau Of Justice Statistics Plans Pricing
  plan_count: 3
  slug: data-analysis-tools-bureau-of-justice-statistics-plans-pricing
random_paper: 74
rate_limits:
- limit_count: 5
  name: Data Analysis Tools Bureau Of Justice Statistics Rate Limits
  slug: data-analysis-tools-bureau-of-justice-statistics-rate-limits
rules:
- name: Bureau of Justice Statistics Data Analysis Tools API Rules
  rule_count: 5
  severity_counts:
    error: 2
    hint: 0
    info: 0
    warn: 3
  slug: bjs-ncvs-api-rules
- name: Bureau of Justice Statistics Data Analysis Tools API Rules
  rule_count: 4
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 3
  slug: data-analysis-tools-bureau-of-justice-statistics-jsonschema-spectral-rules
score:
  band: thin
  composite: 39.8
  delta: 0.0
  facets:
    commercial_clarity: 39.5
    contract_quality: 65.9
    developer_ergonomics: 10.9
    discoverability: 68.5
    governance: 31.3
    operational_transparency: 31.6
  previous_composite: 39.8
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
    score: 31.5
  schema_version: 0.9
  scored_at: '2026-08-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/data-analysis-tools-bureau-of-justice-statistics/refs/heads/main/screenshots/data-analysis-tools-bureau-of-justice-statistics-2026-06-20T175505.png
security:
- kind: authentication
  name: Data Analysis Tools Bureau Of Justice Statistics Authentication
  slug: data-analysis-tools-bureau-of-justice-statistics-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Data Analysis Tools Bureau Of Justice Statistics Domain Security
  slug: data-analysis-tools-bureau-of-justice-statistics-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: data-analysis-tools-bureau-of-justice-statistics
tags:
- Crime Statistics
- Federal Government
- NCVS
- NIBRS
- Open Data
- SODA
- Statistics
- Victimization
website: https://bjs.ojp.gov/
---
