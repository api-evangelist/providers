---
access_model:
  confidence: medium
  label: Free · Open access
  onboarding: open
  pricing: free
  public: true
  source:
  - plans
  trial: false
  try_now: true
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
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 20.0
  scored_at: '2026-08-30'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Fiscaldata Agentic Access
  operation_count: 9
  slug: fiscaldata-agentic-access
  summary_line: 9 operations
api_count: 1
apis:
- description: Daily federal cash and debt operations.
  name: U.S. Treasury Fiscal Data Daily Treasury Statement API
  slug: fiscaldata-daily-treasury-statement-api
- description: National debt outstanding and interest expense on the debt.
  name: U.S. Treasury Fiscal Data Debt API
  slug: fiscaldata-debt-api
- description: Treasury reporting rates of exchange for foreign currencies.
  name: U.S. Treasury Fiscal Data Exchange Rates API
  slug: fiscaldata-exchange-rates-api
- description: Average interest rates on U.S. Treasury securities.
  name: U.S. Treasury Fiscal Data Interest Rates API
  slug: fiscaldata-interest-rates-api
- description: Monthly federal receipts, outlays, and the budget deficit.
  name: U.S. Treasury Fiscal Data Monthly Treasury Statement API
  slug: fiscaldata-monthly-treasury-statement-api
- description: Treasury securities auction results.
  name: U.S. Treasury Fiscal Data Securities API
  slug: fiscaldata-securities-api
artifact_total: 18
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: U.S. Treasury Fiscal Data Daily Treasury Statement API
  slug: open-fiscaldata-daily-treasury-statement-api
- collection_type: open
  name: U.S. Treasury Fiscal Data Daily Treasury Statement Debt API
  slug: open-fiscaldata-debt-api
- collection_type: open
  name: U.S. Treasury Fiscal Data Daily Treasury Statement Exchange Rates API
  slug: open-fiscaldata-exchange-rates-api
- collection_type: open
  name: U.S. Treasury Fiscal Data Daily Treasury Statement Interest Rates API
  slug: open-fiscaldata-interest-rates-api
- collection_type: open
  name: U.S. Treasury Fiscal Data Daily Treasury Statement Monthly Treasury Statement API
  slug: open-fiscaldata-monthly-treasury-statement-api
- collection_type: open
  name: U.S. Treasury Fiscal Data Daily Treasury Statement Securities API
  slug: open-fiscaldata-securities-api
- collection_type: open
  name: U.S. Treasury Fiscal Data API
  slug: open-fiscaldata
common:
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/fiscaldata-capability-edges.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/fiscaldata-agentic-access.yml
- group: company
  title: ''
  type: Website
  url: https://fiscaldata.treasury.gov
- group: docs
  title: ''
  type: Documentation
  url: https://fiscaldata.treasury.gov/api-documentation/
- group: operate
  title: ''
  type: Support
  url: https://api-community.fiscal.treasury.gov/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/fedspendingtransparency/fiscal-data
- group: commercial
  title: ''
  type: Plans
  url: plans/fiscaldata-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/fiscaldata-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/fiscaldata-finops.yml
created: '2026-07-11'
description: U.S. Treasury Fiscal Data is a free, public source for federal government financial data published by the Bureau of the Fiscal Service. Its REST API serves machine-readable government reports and economic indicators - the national debt, average interest rates on Treasury securities, daily and monthly Treasury statements of federal revenue and spending, Treasury reporting rates of exchange, and Treasury securities auctions - as JSON, CSV, or XML. Every dataset endpoint responds from a single database table and supports field selection, filtering, sorting, and pagination. No registration, API key, or authentication is required, and the data is in the public domain.
finops:
- name: Fiscaldata Finops
  service_category: Government Open Data
  slug: fiscaldata-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/fiscaldata.png
layout: provider
modified: '2026-07-11'
name: U.S. Treasury Fiscal Data
nav: Providers
network: true
overview: 'U.S. Treasury Fiscal Data publishes 6 APIs on the [APIs.io](https://apis.io/) network, including Daily Treasury Statement API, Debt API, Exchange Rates API, and 3 more. Tagged areas include Government Data, Treasury, Economic Indicators, Interest Rates, and Open Data.


  U.S. Treasury Fiscal Data''s developer surface includes documentation, support, and 7 more developer resources.'
plans:
- name: Fiscaldata Plans Pricing
  plan_count: 1
  slug: fiscaldata-plans-pricing
random_paper: 7
rate_limits:
- limit_count: 2
  name: Fiscaldata Rate Limits
  slug: fiscaldata-rate-limits
score:
  band: thin
  composite: 29.8
  coverage:
    artifact_dirs: 8
    catalog_gap: 59.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: -0.5
  facets:
    access_clarity: 28.9
    commercial_clarity: 28.9
    contract_governance: 0.0
    contract_quality: 48.3
    developer_ergonomics: 26.2
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 23.7
  previous_composite: 30.3
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
    score: 0.0
  schema_version: 0.17.2
  scored_at: '2026-08-30'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/fiscaldata/refs/heads/main/screenshots/fiscaldata-2026-07-25T214629.png
slug: fiscaldata
tags:
- Government Data
- Treasury
- Economic Indicators
- Interest Rates
- Open Data
- National Debt
- Government Reports
- Public Domain
- Federal Finance
website: https://fiscaldata.treasury.gov
---
