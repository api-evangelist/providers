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
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: verified
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 24.8
  scored_at: '2026-08-10'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Imf Agentic Access
  operation_count: 5
  slug: imf-agentic-access
  summary_line: 5 operations
api_count: 2
apis:
- description: Retrieve actual statistical data observations from IMF datasets
  name: IMF Data Data API
  slug: imf-data-api
- description: Retrieve dataset metadata including dataflows, data structures, codelists, and concept schemes
  name: IMF Data Structure API
  slug: imf-structure-api
artifact_total: 17
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/imf-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/imf-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.imf.org/en/Data
- group: docs
  title: ''
  type: Documentation
  url: https://datahelp.imf.org/knowledgebase/articles/667294-using-json-restful-web-service
- group: build
  title: ''
  type: GitHubOrg
  url: https://github.com/IMFStatistics
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/international-monetary-fund
- group: company
  title: ''
  type: Blog
  url: https://www.imf.org/en/Blogs
- group: commercial
  title: ''
  type: Pricing
  url: https://www.imf.org/en/Data
- group: operate
  title: ''
  type: StatusPage
  url: https://data.imf.org/
- group: other
  title: ''
  type: X
  url: https://x.com/IMFData
- group: commercial
  title: ''
  type: Plans
  url: plans/imf-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/imf-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/imf-finops.yml
created: '2026-06-13'
description: International Monetary Fund data REST API for accessing financial statistics, economic indicators, balance of payments, exchange rates, and international financial data. The API follows the SDMX 3.0 standard and provides access to hundreds of datasets covering macroeconomic indicators, fiscal monitor data, monetary and financial statistics, government finance statistics, and balance of payments across IMF member countries.
examples:
- key_count: 2
  name: Get Codelist Response
  slug: get-codelist-response
- key_count: 2
  name: Get Data Response
  slug: get-data-response
- key_count: 2
  name: List Dataflows Response
  slug: list-dataflows-response
finops:
- name: Imf Finops
  service_category: ''
  slug: imf-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/imf.png
json_schemas:
- name: Codelist
  property_count: 5
  slug: codelist
- name: DataMessage
  property_count: 2
  slug: data-message
- name: DataStructure
  property_count: 3
  slug: data-structure
- name: Dataflow
  property_count: 6
  slug: dataflow
jsonld:
- class_count: 39
  name: context Context
  property_count: 10
  slug: context
- class_count: 0
  name: Imf Api Context
  property_count: 0
  slug: imf-api
layout: provider
modified: '2026-06-13'
name: IMF Data
nav: Providers
network: true
overview: 'IMF Data publishes 2 APIs on the [APIs.io](https://apis.io/) network: Data API and Structure API. Tagged areas include Financial Data, Economic Indicators, Balance of Payments, Exchange Rates, and International Finance.


  The IMF Data catalog on APIs.io includes 2 JSON-LD contexts and 1 Spectral governance ruleset.


  IMF Data''s developer surface includes documentation, engineering blog, pricing, and 10 more developer resources.'
plans:
- name: Imf Plans Pricing
  plan_count: 1
  slug: imf-plans-pricing
random_paper: 84
rate_limits:
- limit_count: 1
  name: Imf Rate Limits
  slug: imf-rate-limits
rules:
- name: IMF Data API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: imf-jsonschema-spectral-rules
score:
  band: developing
  composite: 46.1
  delta: 0.0
  facets:
    commercial_clarity: 39.5
    contract_quality: 66.7
    developer_ergonomics: 10.9
    discoverability: 68.5
    governance: 58.3
    operational_transparency: 42.1
  previous_composite: 46.1
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 2
  schema_version: 0.9.1
  scored_at: '2026-08-10'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/imf/refs/heads/main/screenshots/imf-2026-06-20T183250.png
security:
- kind: domain-security
  name: Imf Domain Security
  slug: imf-domain-security
  summary_line: TLSv1.3 · DMARC
slug: imf
tags:
- Financial Data
- Economic Indicators
- Balance of Payments
- Exchange Rates
- International Finance
- SDMX
- Macroeconomics
- Fiscal Policy
- Monetary Statistics
- Government Finance
website: https://www.imf.org/en/Data
---
