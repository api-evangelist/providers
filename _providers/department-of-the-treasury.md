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
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 21.6
  scored_at: '2026-08-10'
agentic_access:
- acting_count: 1
  human_in_the_loop: 0
  name: Department Of The Treasury Agentic Access
  operation_count: 10
  slug: department-of-the-treasury-agentic-access
  summary_line: 10 operations · 1 acting
api_count: 11
apis:
- description: Public reference data on marketable Treasury securities (auctions, results, security details) published via TreasuryDirect.
  name: TreasuryDirect Securities API
  slug: treasury-direct-api
- description: Federal Service for Award Management (SAM) entity registration, exclusions, and assistance-listings data published via api.data.gov.
  name: SAM.gov Entity Management API
  slug: sam-entity-management-api
- description: The Internal Revenue Service exposes select public datasets and tools through download endpoints, including Tax-Exempt Organization Search.
  name: IRS Public APIs
  slug: irs-public-apis
- description: Treasury securities auctions data
  name: Department of the Treasury Auctions API
  slug: department-of-the-treasury-auctions-api
- description: Federal debt-related datasets
  name: Department of the Treasury Debt API
  slug: department-of-the-treasury-debt-api
- description: Foreign currency exchange rates
  name: Department of the Treasury Exchange Rates API
  slug: department-of-the-treasury-exchange-rates-api
- description: Average interest rates and yield curves
  name: Department of the Treasury Interest Rates API
  slug: department-of-the-treasury-interest-rates-api
- description: SDN and Consolidated Sanctions list downloads
  name: Department of the Treasury Sanctions Lists API
  slug: department-of-the-treasury-sanctions-lists-api
- description: Structured search across the SDN and Consolidated lists
  name: Department of the Treasury Search API
  slug: department-of-the-treasury-search-api
- description: Federal spending datasets
  name: Department of the Treasury Spending API
  slug: department-of-the-treasury-spending-api
- description: Daily and monthly Treasury statements
  name: Department of the Treasury Treasury Operations API
  slug: department-of-the-treasury-treasury-operations-api
artifact_total: 25
collections:
- collection_type: open
  name: Treasury Fiscal Data API
  slug: open-fiscal-data-api
- collection_type: open
  name: OFAC Sanctions List Service API
  slug: open-ofac-sdn-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/department-of-the-treasury-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/department-of-the-treasury-domain-security.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/US-Department-of-the-Treasury
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/us-treasury
- group: start
  title: ''
  type: Portal
  url: https://home.treasury.gov/
- group: docs
  title: ''
  type: Documentation
  url: https://fiscaldata.treasury.gov/api-documentation/
- group: docs
  title: ''
  type: Reference
  url: https://ofac.treasury.gov/
- group: company
  title: ''
  type: Blog
  url: https://home.treasury.gov/rss.xml
created: '2024-12-03'
description: The U.S. Department of the Treasury manages federal finances, public debt, Treasury securities, U.S. currency production, tax administration, financial sanctions, and economic-statistical reporting. Treasury bureaus publish several public APIs, anchored by the Bureau of the Fiscal Service's Fiscal Data API and the Office of Foreign Assets Control's Sanctions List Service.
examples:
- key_count: 3
  name: Debt To Penny Example
  slug: debt-to-penny-example
- key_count: 9
  name: Sanctioned Entity Example
  slug: sanctioned-entity-example
finops:
- name: Department Of The Treasury Finops
  service_category: Federal Government / Public Open Data
  slug: department-of-the-treasury-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/department-of-the-treasury.png
json_schemas:
- name: Sanctioned Entity
  property_count: 9
  slug: sanctioned-entity
- name: Debt to the Penny Record
  property_count: 11
  slug: treasury-debt-record
jsonld:
- class_count: 0
  name: Treasury Context
  property_count: 5
  slug: treasury-context
layout: provider
modified: '2026-05-19'
name: Department of the Treasury
nav: Providers
network: true
overview: 'Department of the Treasury publishes 8 APIs on the [APIs.io](https://apis.io/) network, including Auctions API, Debt API, Exchange Rates API, and 5 more. Tagged areas include Federal Government, Finance, Debt, and Sanctions.


  The Department of the Treasury catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Department of the Treasury''s developer surface includes developer portal, documentation, engineering blog, and 5 more developer resources.'
plans:
- name: Department Of The Treasury Plans Pricing
  plan_count: 1
  slug: department-of-the-treasury-plans-pricing
random_paper: 88
rate_limits:
- limit_count: 3
  name: Department Of The Treasury Rate Limits
  slug: department-of-the-treasury-rate-limits
rules:
- name: Department of the Treasury API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: department-of-the-treasury-jsonschema-spectral-rules
- name: Department of the Treasury API Rules
  rule_count: 0
  severity_counts:
    error: 0
    hint: 0
    info: 0
    warn: 0
  slug: treasury-rules
score:
  band: developing
  composite: 44.4
  delta: 0.0
  facets:
    commercial_clarity: 28.9
    contract_quality: 64.1
    developer_ergonomics: 26.1
    discoverability: 55.6
    governance: 58.3
    operational_transparency: 36.8
  previous_composite: 44.4
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 8
  schema_version: 0.9.1
  scored_at: '2026-08-10'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/department-of-the-treasury/refs/heads/main/screenshots/department-of-the-treasury-2026-06-20T175925.png
security:
- kind: domain-security
  name: Department Of The Treasury Domain Security
  slug: department-of-the-treasury-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: department-of-the-treasury
tags:
- Federal Government
- Finance
- Debt
- Sanctions
website: https://home.treasury.gov/
---
