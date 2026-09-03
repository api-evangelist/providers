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
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 25.8
  scored_at: '2026-09-03'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Fdic Agentic Access
  operation_count: 8
  slug: fdic-agentic-access
  summary_line: 8 operations
api_count: 1
apis:
- baseURL: https://api.fdic.gov/banks
  baseurl_source: declared
  description: Demographics Information
  name: FDIC Demographics API
  slug: fdic-demographics-api
- baseURL: https://api.fdic.gov/banks
  baseurl_source: declared
  description: List of bank failures to date
  name: FDIC Failures API
  slug: fdic-failures-api
- baseURL: https://api.fdic.gov/banks
  baseurl_source: declared
  description: Financial Information
  name: FDIC Financials API
  slug: fdic-financials-api
- baseURL: https://api.fdic.gov/banks
  baseurl_source: declared
  description: Historical data from 1934 onward regarding financial institutions.
  name: FDIC Historical API
  slug: fdic-historical-api
- baseURL: https://api.fdic.gov/banks
  baseurl_source: declared
  description: List of structure change events
  name: FDIC History API
  slug: fdic-history-api
- baseURL: https://api.fdic.gov/banks
  baseurl_source: declared
  description: Financial institution demographic and location information
  name: FDIC Structure API
  slug: fdic-structure-api
- baseURL: https://api.fdic.gov/banks
  baseurl_source: declared
  description: List of Summary of Deposits
  name: FDIC Summary of Deposits API
  slug: fdic-summary-of-deposits-api
artifact_total: 29
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: FDIC Bank Data API (Beta) Demographics API
  slug: open-fdic-demographics-api
- collection_type: open
  name: FDIC Bank Data API (Beta) Demographics Failures API
  slug: open-fdic-failures-api
- collection_type: open
  name: FDIC Bank Data API (Beta) Demographics Financials API
  slug: open-fdic-financials-api
- collection_type: open
  name: FDIC Bank Data API (Beta) Demographics Historical API
  slug: open-fdic-historical-api
- collection_type: open
  name: FDIC Bank Data API (Beta) Demographics History API
  slug: open-fdic-history-api
- collection_type: open
  name: FDIC Bank Data API (Beta) Demographics Structure API
  slug: open-fdic-structure-api
- collection_type: open
  name: FDIC Bank Data API (Beta) Demographics Summary of Deposits API
  slug: open-fdic-summary-of-deposits-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/fdic-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/fdic-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.fdic.gov/
- group: docs
  title: ''
  type: Documentation
  url: https://api.fdic.gov/banks/docs
- group: build
  title: ''
  type: GitHubOrg
  url: https://github.com/fdic-gov
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/fdic/
- group: company
  title: ''
  type: Blog
  url: https://www.fdic.gov/news
- group: commercial
  title: ''
  type: Pricing
  url: https://api.fdic.gov/banks/docs
- group: other
  title: ''
  type: X
  url: https://x.com/FDICgov
- group: commercial
  title: ''
  type: Plans
  url: plans/fdic-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/fdic-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/fdic-finops.yml
created: '2026-06-13'
description: The Federal Deposit Insurance Corporation (FDIC) provides the BankFind Suite REST API, offering developers programmatic access to publicly available data on FDIC-insured financial institutions. The API enables searching, filtering, and downloading information about bank institutions, branch locations, financial reports, structure change history, failed banks, and summary deposit data. All data is provided free of charge under the U.S. public domain license.
examples:
- key_count: 3
  name: Fdic Failure Example
  slug: fdic-failure-example
- key_count: 2
  name: Fdic Financials Example
  slug: fdic-financials-example
- key_count: 2
  name: Fdic Institution Example
  slug: fdic-institution-example
finops:
- name: Fdic Finops
  service_category: ''
  slug: fdic-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/fdic.png
json_schemas:
- name: FDIC Bank Failure
  property_count: 12
  slug: fdic-failure
- name: FDIC Financial Report
  property_count: 12
  slug: fdic-financial
- name: FDIC Institution
  property_count: 18
  slug: fdic-institution
- name: FDIC Institution Location
  property_count: 11
  slug: fdic-location
jsonld:
- class_count: 6
  name: Fdic Context
  property_count: 46
  slug: fdic-context
layout: provider
modified: '2026-06-13'
name: FDIC
nav: Providers
network: true
overview: 'FDIC publishes 7 APIs on the [APIs.io](https://apis.io/) network, including Demographics API, Failures API, Financials API, and 4 more. Tagged areas include Banking, Finance, Government, FDIC, and Financial Data.


  The FDIC catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  FDIC''s developer surface includes documentation, engineering blog, pricing, and 9 more developer resources.'
plans:
- name: Fdic Plans Pricing
  plan_count: 1
  slug: fdic-plans-pricing
random_paper: 7
rate_limits:
- limit_count: 1
  name: Fdic Rate Limits
  slug: fdic-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: FDIC API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: fdic-jsonschema-spectral-rules
score:
  band: thin
  composite: 33.4
  coverage:
    artifact_dirs: 14
    catalog_gap: 44.8
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 39.5
    commercial_clarity: 39.5
    contract_governance: 9.8
    contract_quality: 57.1
    developer_ergonomics: 11.9
    discoverability: 68.5
    governance: 9.8
    operational_transparency: 26.3
  previous_composite: 33.4
  provenance:
    agentic_access: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 7
  regulatory:
    applies: true
    matched_via: tags
    regime: Banking & Open Finance
    regime_id: banking_open_finance
    score: 13.9
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/fdic/refs/heads/main/screenshots/fdic-2026-06-20T181105.png
security:
- kind: domain-security
  name: Fdic Domain Security
  slug: fdic-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: fdic
tags:
- Banking
- Finance
- Government
- FDIC
- Financial Data
- Bank Data
- Regulatory
website: https://www.fdic.gov/
---
