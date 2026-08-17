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
  scored_at: '2026-08-17'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Archrock Agentic Access
  operation_count: 5
  slug: archrock-agentic-access
  summary_line: 5 operations
api_count: 4
apis:
- description: The Financials API from Archrock — 1 operation(s) for financials.
  name: Archrock Financials API
  slug: archrock-financials-api
- description: The Fleet API from Archrock — 2 operation(s) for fleet.
  name: Archrock Fleet API
  slug: archrock-fleet-api
- description: The Operations API from Archrock — 1 operation(s) for operations.
  name: Archrock Operations API
  slug: archrock-operations-api
- description: The SEC Filings API from Archrock — 1 operation(s) for sec filings.
  name: Archrock SEC Filings API
  slug: archrock-sec-filings-api
artifact_total: 51
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Archrock Investor Relations Financials API
  slug: open-archrock-financials-api
- collection_type: open
  name: Archrock Investor Relations Financials Fleet API
  slug: open-archrock-fleet-api
- collection_type: open
  name: Archrock Investor Relations Financials Operations API
  slug: open-archrock-operations-api
- collection_type: open
  name: Archrock Investor Relations Financials SEC Filings API
  slug: open-archrock-sec-filings-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/archrock-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/archrock-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/archrock-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/archrock
- group: start
  title: ''
  type: Portal
  url: https://www.archrock.com/
- group: docs
  title: ''
  type: Documentation
  url: https://www.archrock.com/investor-relations
- group: company
  title: ''
  type: Blog
  url: https://www.archrock.com/news
- group: design
  title: ''
  type: SpectralRules
  url: https://raw.githubusercontent.com/api-evangelist/archrock/refs/heads/main/rules/archrock-spectral-rules.yml
- group: design
  title: ''
  type: Vocabulary
  url: https://raw.githubusercontent.com/api-evangelist/archrock/refs/heads/main/vocabulary/archrock-vocabulary.yaml
- group: design
  title: ''
  type: JSONLD
  url: https://raw.githubusercontent.com/api-evangelist/archrock/refs/heads/main/json-ld/archrock-investor-relations-api-context.jsonld
created: '2026-03-23'
description: 'Archrock (NYSE: AROC) is the premier provider of natural gas compression services and equipment to customers in the oil and natural gas industry throughout the United States. The company operates a large fleet of compression equipment and provides contract operations and aftermarket services.'
examples:
- key_count: 2
  name: Archrock Investor Relations Api Equipment Example
  slug: archrock-investor-relations-api-equipment-example
- key_count: 2
  name: Archrock Investor Relations Api Equipment List Example
  slug: archrock-investor-relations-api-equipment-list-example
- key_count: 2
  name: Archrock Investor Relations Api Fleet Statistics Example
  slug: archrock-investor-relations-api-fleet-statistics-example
- key_count: 2
  name: Archrock Investor Relations Api Operational Metrics Example
  slug: archrock-investor-relations-api-operational-metrics-example
- key_count: 2
  name: Archrock Investor Relations Api Quarterly Financials Example
  slug: archrock-investor-relations-api-quarterly-financials-example
- key_count: 2
  name: Archrock Investor Relations Api Sec Filing Example
  slug: archrock-investor-relations-api-sec-filing-example
- key_count: 2
  name: Archrock Investor Relations Api Sec Filing List Example
  slug: archrock-investor-relations-api-sec-filing-list-example
features:
- description: Contract operations and maintenance of natural gas compression equipment across the US.
  name: Natural Gas Compression
- description: Management of one of the largest compression fleets in North America with diverse horsepower ratings.
  name: Fleet Management
- description: Parts, service, and maintenance for third-party compression equipment.
  name: Aftermarket Services
- description: Financial performance, fleet statistics, and operational metrics for investors and analysts.
  name: Investor Relations Data
- description: Annual reports, 10-K, 10-Q, and 8-K filings available through SEC EDGAR.
  name: SEC Filings
finops:
- name: Archrock Finops
  service_category: API
  slug: archrock-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/archrock.png
integrations:
- description: All SEC filings available through the EDGAR electronic filing system.
  name: SEC EDGAR
- description: Financial and operational data integrated with Bloomberg terminal.
  name: Bloomberg
- description: Production and financial data available through Refinitiv data services.
  name: Refinitiv
json_schemas:
- name: EquipmentList
  property_count: 4
  slug: archrock-investor-relations-api-equipment-list
- name: Equipment
  property_count: 9
  slug: archrock-investor-relations-api-equipment
- name: FleetStatistics
  property_count: 9
  slug: archrock-investor-relations-api-fleet-statistics
- name: OperationalMetrics
  property_count: 10
  slug: archrock-investor-relations-api-operational-metrics
- name: QuarterlyFinancials
  property_count: 11
  slug: archrock-investor-relations-api-quarterly-financials
- name: SecFilingList
  property_count: 4
  slug: archrock-investor-relations-api-sec-filing-list
- name: SecFiling
  property_count: 7
  slug: archrock-investor-relations-api-sec-filing
json_structures:
- name: Archrock Investor Relations Api Equipment List Structure
  property_count: 4
  slug: archrock-investor-relations-api-equipment-list-structure
- name: Archrock Investor Relations Api Equipment Structure
  property_count: 9
  slug: archrock-investor-relations-api-equipment-structure
- name: Archrock Investor Relations Api Fleet Statistics Structure
  property_count: 9
  slug: archrock-investor-relations-api-fleet-statistics-structure
- name: Archrock Investor Relations Api Operational Metrics Structure
  property_count: 10
  slug: archrock-investor-relations-api-operational-metrics-structure
- name: Archrock Investor Relations Api Quarterly Financials Structure
  property_count: 11
  slug: archrock-investor-relations-api-quarterly-financials-structure
- name: Archrock Investor Relations Api Sec Filing List Structure
  property_count: 4
  slug: archrock-investor-relations-api-sec-filing-list-structure
- name: Archrock Investor Relations Api Sec Filing Structure
  property_count: 7
  slug: archrock-investor-relations-api-sec-filing-structure
jsonld:
- class_count: 7
  name: Archrock Investor Relations Api Context
  property_count: 0
  slug: archrock-investor-relations-api-context
layout: provider
modified: '2026-04-19'
name: Archrock
nav: Providers
network: true
overview: 'Archrock publishes 4 APIs on the [APIs.io](https://apis.io/) network, including Financials API, Fleet API, Operations API, and 1 more. Tagged areas include Natural Gas, Compression Services, Oil And Gas, Energy, and Industrial.


  The Archrock catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Archrock''s developer surface includes authentication, developer portal, documentation, engineering blog, and 6 more developer resources.'
plans:
- name: Archrock Plans Pricing
  plan_count: 3
  slug: archrock-plans-pricing
press:
- date: '2026-05-25'
  title: Archrock, Inc.
  url: https://www.facebook.com/Archrock/posts/yesterday-archrock-inc-reported-its-q2-2025-earnings-and-the-results-were-outsta/1359602162836702/
- date: '2026-05-25'
  title: Rising LNG Exports & AI-Driven Power Demand Drive ...
  url: https://finance.yahoo.com/news/rising-lng-exports-ai-driven-191500994.html
- date: '2026-05-25'
  title: Archrock Surges on Record Earnings, Eyes LNG and AI Growth ...
  url: https://briefglance.com/articles/archrock-surges-on-record-earnings-eyes-lng-and-ai-growth-boom
- date: '2026-05-25'
  title: Archrock Stock Fuels Breakout On Demand From AI Data ...
  url: https://www.investors.com/research/breakout-stocks-technical-analysis/archrock-stock-aroc-cng-ai-data-centers/
- date: '2026-05-25'
  title: AI Power, LNG Growth Sparking Natural Gas Compression ...
  url: https://naturalgasintel.com/news/ai-power-lng-growth-sparking-natural-gas-compression-boom-for-archrock/
random_paper: 100
rate_limits:
- limit_count: 5
  name: Archrock Rate Limits
  slug: archrock-rate-limits
rules:
- name: Archrock API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: archrock-jsonschema-spectral-rules
- name: Archrock API Rules
  rule_count: 19
  severity_counts:
    error: 8
    hint: 0
    info: 1
    warn: 10
  slug: archrock-spectral-rules
score:
  band: thin
  composite: 37.5
  delta: 0.0
  facets:
    commercial_clarity: 15.8
    contract_quality: 60.4
    developer_ergonomics: 30.4
    discoverability: 64.8
    governance: 68.8
    operational_transparency: 7.9
  previous_composite: 37.5
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 4
  regulatory:
    applies: true
    matched_via: tags
    regime: Energy & Utilities
    regime_id: energy_utilities
    score: 23.0
  schema_version: 0.11.0
  scored_at: '2026-08-17'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/archrock/refs/heads/main/screenshots/archrock-2026-06-20T172409.png
security:
- kind: authentication
  name: Archrock Authentication
  slug: archrock-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Archrock Domain Security
  slug: archrock-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: archrock
tags:
- Natural Gas
- Compression Services
- Oil And Gas
- Energy
- Industrial
- 'NYSE: AROC'
use_cases:
- description: Analyze Archrock financial performance and fleet utilization for investment decisions.
  name: Investment Research
- description: Track natural gas compression services market trends and operational data.
  name: Energy Sector Analysis
- description: Access environmental and safety performance data for ESG analysis.
  name: ESG Reporting
- description: Operators use Archrock fleet data for compression capacity planning.
  name: Supply Chain Planning
website: https://www.archrock.com/
---
