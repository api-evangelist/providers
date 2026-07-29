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
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: verified
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 44.1
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 1
  human_in_the_loop: 0
  name: U S Bureau Of Labor Statistics Agentic Access
  operation_count: 5
  slug: u-s-bureau-of-labor-statistics-agentic-access
  summary_line: 5 operations · 1 acting
api_count: 2
apis:
- description: Time series data operations for retrieving labor statistics across BLS surveys including employment, CPI, wages, and more.
  name: U.S. Bureau of Labor Statistics Series API
  slug: u-s-bureau-of-labor-statistics-series-api
- description: Survey metadata and catalog operations for discovering available BLS surveys and their series identifiers.
  name: U.S. Bureau of Labor Statistics Surveys API
  slug: u-s-bureau-of-labor-statistics-surveys-api
artifact_total: 65
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/u-s-bureau-of-labor-statistics-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/u-s-bureau-of-labor-statistics-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/u-s-bureau-of-labor-statistics-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/bureau-of-labor-statistics
- group: company
  title: ''
  type: Website
  url: https://www.bls.gov/
- group: docs
  title: ''
  type: Documentation
  url: https://www.bls.gov/developers/
- group: start
  title: ''
  type: GettingStarted
  url: https://www.bls.gov/developers/home.htm
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.bls.gov/bls/bls-privacy.htm
- group: operate
  title: ''
  type: FAQ
  url: https://www.bls.gov/developers/api_faqs.htm
- group: design
  title: ''
  type: SpectralRules
  url: https://raw.githubusercontent.com/api-evangelist/u-s-bureau-of-labor-statistics/refs/heads/main/rules/bls-public-data-api-rules.yml
- group: design
  title: ''
  type: Vocabulary
  url: https://raw.githubusercontent.com/api-evangelist/u-s-bureau-of-labor-statistics/refs/heads/main/vocabulary/u-s-bureau-of-labor-statistics-vocabulary.yaml
created: '2024-12-25'
description: The U.S. Bureau of Labor Statistics (BLS) is the principal federal statistical agency responsible for measuring labor market activity, working conditions, and price changes in the U.S. economy. BLS collects, processes, analyzes, and disseminates statistical data on employment, unemployment, inflation, wages, productivity, and occupational safety through a public API that provides programmatic access to published historical time series data.
examples:
- key_count: 2
  name: Bls Calculations Example
  slug: bls-calculations-example
- key_count: 7
  name: Bls Data Point Example
  slug: bls-data-point-example
- key_count: 2
  name: Bls Footnote Example
  slug: bls-footnote-example
- key_count: 8
  name: Bls Multiple Series Request Example
  slug: bls-multiple-series-request-example
- key_count: 2
  name: Bls Period Calculations Example
  slug: bls-period-calculations-example
- key_count: 4
  name: Bls Popular Series Response Example
  slug: bls-popular-series-response-example
- key_count: 8
  name: Bls Series Catalog Example
  slug: bls-series-catalog-example
- key_count: 4
  name: Bls Series Data Example
  slug: bls-series-data-example
- key_count: 4
  name: Bls Series Response Example
  slug: bls-series-response-example
- key_count: 1
  name: Bls Series Results Example
  slug: bls-series-results-example
- key_count: 4
  name: Bls Survey Example
  slug: bls-survey-example
- key_count: 4
  name: Bls Survey Metadata Response Example
  slug: bls-survey-metadata-response-example
- key_count: 4
  name: Bls Surveys Response Example
  slug: bls-surveys-response-example
features:
- description: Retrieve historical labor statistics data using BLS series IDs covering employment, unemployment, CPI, wages, and productivity.
  name: Time Series Data Access
- description: Version 2 API allows requesting up to 50 series in a single POST request, returning 20 years of data per series.
  name: Multiple Series in One Request
- description: Optional calculations including net change and percent change from prior periods are available in Version 2 responses.
  name: Net and Percent Change Calculations
- description: Retrieve metadata for all available BLS surveys and discover popular series IDs through the catalog endpoint.
  name: Survey Catalog Discovery
- description: Request annual average values (M13 period) alongside monthly data for trend analysis.
  name: Annual Averages
- description: The BLS API is free to use. Version 1 requires no registration; Version 2 requires a free API key for higher query limits.
  name: Public API with Free Registration
finops:
- name: U S Bureau Of Labor Statistics Finops
  service_category: API
  slug: u-s-bureau-of-labor-statistics-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/u-s-bureau-of-labor-statistics.png
integrations:
- description: Open-source Python package for querying the BLS API with support for v1 and v2 endpoints.
  name: Python blsapi
- description: CRAN R package providing a simple interface to the BLS Public Data API for statistical computing.
  name: R blsAPI
- description: BLS connector available in Power Automate, Power Apps, and Copilot Studio for low-code BLS data access.
  name: Microsoft Power Platform
- description: BLS datasets are cataloged on data.gov as part of the federal open data initiative.
  name: data.gov
json_schemas:
- name: Calculations
  property_count: 2
  slug: bls-calculations
- name: DataPoint
  property_count: 7
  slug: bls-data-point
- name: Footnote
  property_count: 2
  slug: bls-footnote
- name: MultipleSeriesRequest
  property_count: 8
  slug: bls-multiple-series-request
- name: PeriodCalculations
  property_count: 2
  slug: bls-period-calculations
- name: PopularSeriesResponse
  property_count: 4
  slug: bls-popular-series-response
- name: SeriesCatalog
  property_count: 8
  slug: bls-series-catalog
- name: SeriesData
  property_count: 4
  slug: bls-series-data
- name: SeriesResponse
  property_count: 4
  slug: bls-series-response
- name: SeriesResults
  property_count: 1
  slug: bls-series-results
- name: SurveyMetadataResponse
  property_count: 4
  slug: bls-survey-metadata-response
- name: Survey
  property_count: 4
  slug: bls-survey
- name: SurveysResponse
  property_count: 4
  slug: bls-surveys-response
json_structures:
- name: Bls Calculations Structure
  property_count: 2
  slug: bls-calculations-structure
- name: Bls Data Point Structure
  property_count: 7
  slug: bls-data-point-structure
- name: Bls Footnote Structure
  property_count: 2
  slug: bls-footnote-structure
- name: Bls Multiple Series Request Structure
  property_count: 8
  slug: bls-multiple-series-request-structure
- name: Bls Period Calculations Structure
  property_count: 2
  slug: bls-period-calculations-structure
- name: Bls Popular Series Response Structure
  property_count: 4
  slug: bls-popular-series-response-structure
- name: Bls Series Catalog Structure
  property_count: 8
  slug: bls-series-catalog-structure
- name: Bls Series Data Structure
  property_count: 4
  slug: bls-series-data-structure
- name: Bls Series Response Structure
  property_count: 4
  slug: bls-series-response-structure
- name: Bls Series Results Structure
  property_count: 1
  slug: bls-series-results-structure
- name: Bls Survey Metadata Response Structure
  property_count: 4
  slug: bls-survey-metadata-response-structure
- name: Bls Survey Structure
  property_count: 4
  slug: bls-survey-structure
- name: Bls Surveys Response Structure
  property_count: 4
  slug: bls-surveys-response-structure
jsonld:
- class_count: 13
  name: Bls Public Data Api Context
  property_count: 36
  slug: bls-public-data-api-context
layout: provider
modified: '2026-05-19'
name: U.S. Bureau of Labor Statistics
nav: Providers
network: true
overview: 'U.S. Bureau of Labor Statistics publishes 2 APIs on the [APIs.io](https://apis.io/) network: Series API and Surveys API. Tagged areas include Federal Government, Labor, Statistics, Employment, and Economic Data.


  The U.S. Bureau of Labor Statistics catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  U.S. Bureau of Labor Statistics'' developer surface includes authentication, documentation, getting-started guide, FAQ, and 7 more developer resources.'
plans:
- name: U S Bureau Of Labor Statistics Plans Pricing
  plan_count: 3
  slug: u-s-bureau-of-labor-statistics-plans-pricing
random_paper: 18
rate_limits:
- limit_count: 5
  name: U S Bureau Of Labor Statistics Rate Limits
  slug: u-s-bureau-of-labor-statistics-rate-limits
rules:
- name: U.S. Bureau of Labor Statistics API Rules
  rule_count: 33
  severity_counts:
    error: 9
    hint: 0
    info: 7
    warn: 17
  slug: bls-public-data-api-rules
- name: U.S. Bureau of Labor Statistics API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: u-s-bureau-of-labor-statistics-jsonschema-spectral-rules
score:
  band: developing
  composite: 49.9
  delta: -6.9
  facets:
    commercial_clarity: 50.0
    contract_quality: 68.6
    developer_ergonomics: 30.4
    discoverability: 68.5
    governance: 47.9
    operational_transparency: 31.6
  previous_composite: 56.8
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 2
      marker_coverage: 100.0
      total: 2
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: falling
screenshot: https://raw.githubusercontent.com/api-evangelist/u-s-bureau-of-labor-statistics/refs/heads/main/screenshots/u-s-bureau-of-labor-statistics-2026-06-20T195913.png
security:
- kind: authentication
  name: U S Bureau Of Labor Statistics Authentication
  slug: u-s-bureau-of-labor-statistics-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: U S Bureau Of Labor Statistics Domain Security
  slug: u-s-bureau-of-labor-statistics-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
slug: u-s-bureau-of-labor-statistics
tags:
- Federal Government
- Labor
- Statistics
- Employment
- Economic Data
use_cases:
- description: Economists and researchers use BLS time series data to analyze labor market trends, wage growth, and employment cycles.
  name: Economic Research
- description: Track CPI and PPI data for measuring inflation trends across consumer goods, food, energy, and other categories.
  name: Inflation Monitoring
- description: Policy analysts use unemployment and employment statistics to evaluate labor market conditions and inform policy decisions.
  name: Employment Policy Analysis
- description: Developers integrate BLS data into economic dashboards, journalism applications, and data visualization tools.
  name: Dashboard and Application Development
- description: Universities and think tanks use BLS historical data for econometric modeling, academic papers, and policy reports.
  name: Academic Research
website: https://www.bls.gov/
---
