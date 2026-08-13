---
access_model:
  confidence: medium
  label: Freemium · Open access
  onboarding: open
  pricing: freemium
  public: true
  source:
  - plans
  trial: false
  try_now: true
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 35.1
  scored_at: '2026-08-12'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: U S Treasury Fiscal Data Agentic Access
  operation_count: 9
  slug: u-s-treasury-fiscal-data-agentic-access
  summary_line: 9 operations
api_count: 4
apis:
- description: Treasury reporting rates of exchange for foreign currencies.
  name: U.S. Treasury Fiscal Data Exchange Rates API
  slug: u-s-treasury-fiscal-data-exchange-rates-api
- description: Federal debt, public debt outstanding, and interest rate data.
  name: U.S. Treasury Fiscal Data National Debt API
  slug: u-s-treasury-fiscal-data-national-debt-api
- description: Treasury securities, savings bonds, and investment data.
  name: U.S. Treasury Fiscal Data Securities API
  slug: u-s-treasury-fiscal-data-securities-api
- description: Daily and monthly Treasury financial statements.
  name: U.S. Treasury Fiscal Data Treasury Statements API
  slug: u-s-treasury-fiscal-data-treasury-statements-api
artifact_total: 69
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/u-s-treasury-fiscal-data-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/u-s-treasury-fiscal-data-domain-security.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/fedspendingtransparency
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/bureau-of-the-fiscal-service
- group: company
  title: ''
  type: Website
  url: https://fiscaldata.treasury.gov/
- group: docs
  title: ''
  type: Documentation
  url: https://fiscaldata.treasury.gov/api-documentation/
- group: design
  title: ''
  type: SpectralRules
  url: https://raw.githubusercontent.com/api-evangelist/u-s-treasury-fiscal-data/refs/heads/main/rules/treasury-fiscal-data-api-rules.yml
- group: design
  title: ''
  type: Vocabulary
  url: https://raw.githubusercontent.com/api-evangelist/u-s-treasury-fiscal-data/refs/heads/main/vocabulary/u-s-treasury-fiscal-data-vocabulary.yaml
created: '2024-12-25'
description: The U.S. Treasury Bureau of the Fiscal Service manages the government's finances including collecting revenue, paying federal bills, managing federal debt, and producing the nation's financial accounts. Their Fiscal Data API provides free, open access to federal financial data through a standardized RESTful API covering 80+ datasets. Key datasets include the Debt to the Penny (daily public debt outstanding), Treasury Reporting Rates of Exchange (quarterly foreign currency rates), Average Interest Rates on U.S. Treasury Securities, Daily Treasury Statements, Monthly Treasury Statements, and U.S. savings bond data. No authentication required.
examples:
- key_count: 6
  name: Treasury Daily Treasury Record Example
  slug: treasury-daily-treasury-record-example
- key_count: 3
  name: Treasury Daily Treasury Statement Response Example
  slug: treasury-daily-treasury-statement-response-example
- key_count: 11
  name: Treasury Debt Record Example
  slug: treasury-debt-record-example
- key_count: 3
  name: Treasury Debt To Penny Response Example
  slug: treasury-debt-to-penny-response-example
- key_count: 3
  name: Treasury Error Response Example
  slug: treasury-error-response-example
- key_count: 5
  name: Treasury Exchange Rate Record Example
  slug: treasury-exchange-rate-record-example
- key_count: 3
  name: Treasury Exchange Rate Response Example
  slug: treasury-exchange-rate-response-example
- key_count: 5
  name: Treasury Fiscal Links Example
  slug: treasury-fiscal-links-example
- key_count: 6
  name: Treasury Fiscal Meta Example
  slug: treasury-fiscal-meta-example
- key_count: 3
  name: Treasury Generic Fiscal Response Example
  slug: treasury-generic-fiscal-response-example
- key_count: 4
  name: Treasury Interest Rate Record Example
  slug: treasury-interest-rate-record-example
- key_count: 3
  name: Treasury Interest Rate Response Example
  slug: treasury-interest-rate-response-example
- key_count: 5
  name: Treasury Monthly Treasury Record Example
  slug: treasury-monthly-treasury-record-example
- key_count: 3
  name: Treasury Monthly Treasury Statement Response Example
  slug: treasury-monthly-treasury-statement-response-example
features:
- description: All Treasury Fiscal Data API endpoints are publicly accessible without API keys or registration, enabling immediate programmatic access.
  name: No Authentication Required
- description: Use the fields parameter to request only the specific data fields needed, reducing response payload size and improving performance.
  name: Flexible Field Selection
- description: Filter datasets using field:operator:value syntax supporting equality, range, and set membership operators across any field in the dataset.
  name: Advanced Filtering
- description: All endpoints support page[number] and page[size] pagination with metadata indicating total record count and total pages available.
  name: Pagination Support
- description: API responses available in JSON, XML, and CSV formats suitable for programmatic consumption, data warehousing, and spreadsheet analysis.
  name: Multiple Output Formats
- description: 80+ datasets covering all major Bureau of the Fiscal Service financial reports from the Debt to the Penny to Monthly Treasury Statements.
  name: Comprehensive Coverage
finops:
- name: U S Treasury Fiscal Data Finops
  service_category: API
  slug: u-s-treasury-fiscal-data-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/u-s-treasury-fiscal-data.png
integrations:
- description: Federal Reserve Economic Database (FRED) integrates Treasury Fiscal Data series for economic research and modeling applications.
  name: FRED Economic Database
- description: Federal spending transparency portal uses Bureau of the Fiscal Service data alongside Treasury Fiscal Data for comprehensive spending analysis.
  name: USASpending.gov
- description: Treasury exchange rates and fiscal data support OMB/FASAB-compliant financial reporting across federal agencies and programs.
  name: Federal Accounting Standards
- description: The official Treasury Fiscal Data portal provides data visualization, dataset explorer, and download tools built on the same API.
  name: fiscaldata.treasury.gov
json_schemas:
- name: DailyTreasuryRecord
  property_count: 6
  slug: treasury-daily-treasury-record
- name: DailyTreasuryStatementResponse
  property_count: 3
  slug: treasury-daily-treasury-statement-response
- name: DebtRecord
  property_count: 11
  slug: treasury-debt-record
- name: DebtToPennyResponse
  property_count: 3
  slug: treasury-debt-to-penny-response
- name: ErrorResponse
  property_count: 3
  slug: treasury-error-response
- name: ExchangeRateRecord
  property_count: 5
  slug: treasury-exchange-rate-record
- name: ExchangeRateResponse
  property_count: 3
  slug: treasury-exchange-rate-response
- name: FiscalLinks
  property_count: 5
  slug: treasury-fiscal-links
- name: FiscalMeta
  property_count: 6
  slug: treasury-fiscal-meta
- name: GenericFiscalResponse
  property_count: 3
  slug: treasury-generic-fiscal-response
- name: InterestRateRecord
  property_count: 4
  slug: treasury-interest-rate-record
- name: InterestRateResponse
  property_count: 3
  slug: treasury-interest-rate-response
- name: MonthlyTreasuryRecord
  property_count: 5
  slug: treasury-monthly-treasury-record
- name: MonthlyTreasuryStatementResponse
  property_count: 3
  slug: treasury-monthly-treasury-statement-response
json_structures:
- name: Treasury Daily Treasury Record Structure
  property_count: 6
  slug: treasury-daily-treasury-record-structure
- name: Treasury Daily Treasury Statement Response Structure
  property_count: 3
  slug: treasury-daily-treasury-statement-response-structure
- name: Treasury Debt Record Structure
  property_count: 11
  slug: treasury-debt-record-structure
- name: Treasury Debt To Penny Response Structure
  property_count: 3
  slug: treasury-debt-to-penny-response-structure
- name: Treasury Error Response Structure
  property_count: 3
  slug: treasury-error-response-structure
- name: Treasury Exchange Rate Record Structure
  property_count: 5
  slug: treasury-exchange-rate-record-structure
- name: Treasury Exchange Rate Response Structure
  property_count: 3
  slug: treasury-exchange-rate-response-structure
- name: Treasury Fiscal Links Structure
  property_count: 5
  slug: treasury-fiscal-links-structure
- name: Treasury Fiscal Meta Structure
  property_count: 6
  slug: treasury-fiscal-meta-structure
- name: Treasury Generic Fiscal Response Structure
  property_count: 3
  slug: treasury-generic-fiscal-response-structure
- name: Treasury Interest Rate Record Structure
  property_count: 4
  slug: treasury-interest-rate-record-structure
- name: Treasury Interest Rate Response Structure
  property_count: 3
  slug: treasury-interest-rate-response-structure
- name: Treasury Monthly Treasury Record Structure
  property_count: 5
  slug: treasury-monthly-treasury-record-structure
- name: Treasury Monthly Treasury Statement Response Structure
  property_count: 3
  slug: treasury-monthly-treasury-statement-response-structure
jsonld:
- class_count: 0
  name: Treasury Fiscal Data Api Context
  property_count: 62
  slug: treasury-fiscal-data-api-context
layout: provider
modified: '2026-05-19'
name: U.S. Treasury Fiscal Data
nav: Providers
network: true
overview: 'U.S. Treasury Fiscal Data publishes 4 APIs on the [APIs.io](https://apis.io/) network, including Exchange Rates API, National Debt API, Securities API, and 1 more. Tagged areas include Federal Government, Finance, Treasury, National Debt, and Exchange Rates.


  The U.S. Treasury Fiscal Data catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  U.S. Treasury Fiscal Data''s developer surface includes documentation and 7 more developer resources.'
plans:
- name: U S Treasury Fiscal Data Plans Pricing
  plan_count: 3
  slug: u-s-treasury-fiscal-data-plans-pricing
random_paper: 63
rate_limits:
- limit_count: 5
  name: U S Treasury Fiscal Data Rate Limits
  slug: u-s-treasury-fiscal-data-rate-limits
rules:
- name: U.S. Treasury Fiscal Data API Rules
  rule_count: 31
  severity_counts:
    error: 6
    hint: 0
    info: 12
    warn: 13
  slug: treasury-fiscal-data-api-rules
- name: U.S. Treasury Fiscal Data API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: u-s-treasury-fiscal-data-jsonschema-spectral-rules
score:
  band: thin
  composite: 28.0
  delta: 0.0
  facets:
    commercial_clarity: 15.8
    contract_quality: 28.2
    developer_ergonomics: 8.7
    discoverability: 74.1
    governance: 68.8
    operational_transparency: 13.2
  previous_composite: 28.0
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 4
      marker_coverage: 100.0
      total: 4
  regulatory:
    applies: true
    matched_via: tags
    regime: Government & Public Sector
    regime_id: government
    score: 20.4
  schema_version: 0.11.0
  scored_at: '2026-08-12'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/u-s-treasury-fiscal-data/refs/heads/main/screenshots/u-s-treasury-fiscal-data-2026-06-20T195919.png
security:
- kind: domain-security
  name: U S Treasury Fiscal Data Domain Security
  slug: u-s-treasury-fiscal-data-domain-security
  summary_line: TLSv1.2 · HSTS · DNSSEC · DMARC
slug: u-s-treasury-fiscal-data
tags:
- Federal Government
- Finance
- Treasury
- National Debt
- Exchange Rates
- Economics
use_cases:
- description: Journalists, economists, and citizens monitor daily changes in U.S. public debt outstanding including amounts held by the public and intragovernmental holdings.
  name: National Debt Tracking
- description: Federal agencies, researchers, and businesses use Treasury exchange rates for reporting foreign currency transactions in accordance with federal accounting standards.
  name: Exchange Rate Research
- description: Policy analysts and budget offices track federal government receipts and outlays from Monthly Treasury Statements to assess deficit trends.
  name: Budget Analysis
- description: Economists and investors track average interest rates on Treasury securities to analyze government borrowing costs and monetary policy.
  name: Interest Rate Monitoring
- description: Financial researchers analyze Daily Treasury Statement data to understand federal government cash flows and liquidity management.
  name: Treasury Cash Management
website: https://fiscaldata.treasury.gov/
---
