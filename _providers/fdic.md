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
    openapi_examples: verified
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 27.9
  scored_at: '2026-08-11'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Fdic Agentic Access
  operation_count: 8
  slug: fdic-agentic-access
  summary_line: 8 operations
api_count: 7
apis:
- description: Demographics Information
  name: FDIC Demographics API
  slug: fdic-demographics-api
- description: List of bank failures to date
  name: FDIC Failures API
  slug: fdic-failures-api
- description: Financial Information
  name: FDIC Financials API
  slug: fdic-financials-api
- description: Historical data from 1934 onward regarding financial institutions.
  name: FDIC Historical API
  slug: fdic-historical-api
- description: List of structure change events
  name: FDIC History API
  slug: fdic-history-api
- description: Financial institution demographic and location information
  name: FDIC Structure API
  slug: fdic-structure-api
- description: List of Summary of Deposits
  name: FDIC Summary of Deposits API
  slug: fdic-summary-of-deposits-api
artifact_total: 21
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
random_paper: 58
rate_limits:
- limit_count: 1
  name: Fdic Rate Limits
  slug: fdic-rate-limits
rules:
- name: FDIC API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: fdic-jsonschema-spectral-rules
score:
  band: thin
  composite: 39.1
  delta: -0.5
  facets:
    commercial_clarity: 39.5
    contract_quality: 62.7
    developer_ergonomics: 10.9
    discoverability: 74.1
    governance: 58.3
    operational_transparency: 26.3
  previous_composite: 39.6
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
  schema_version: 0.11.0
  scored_at: '2026-08-11'
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
