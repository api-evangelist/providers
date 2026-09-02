---
access_model:
  confidence: high
  label: Enterprise · Self-serve signup
  onboarding: self-serve
  pricing: enterprise
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: negotiable
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 27.7
  scored_at: '2026-09-01'
agentic_access:
- acting_count: 2
  human_in_the_loop: 0
  name: Aladdin Studio Agentic Access
  operation_count: 13
  slug: aladdin-studio-agentic-access
  summary_line: 13 operations · 2 acting
api_count: 10
apis:
- description: Portfolio performance and attribution analytics
  name: Aladdin Studio Analytics API
  slug: aladdin-studio-analytics-api
- description: Aladdin Data Cloud Snowflake connection management
  name: Aladdin Studio Connections API
  slug: aladdin-studio-connections-api
- description: Available dataset and table discovery
  name: Aladdin Studio Datasets API
  slug: aladdin-studio-datasets-api
- description: Trading order management and execution
  name: Aladdin Studio Orders API
  slug: aladdin-studio-orders-api
- description: Portfolio metadata and management operations
  name: Aladdin Studio Portfolios API
  slug: aladdin-studio-portfolios-api
- description: Portfolio position and holdings data
  name: Aladdin Studio Positions API
  slug: aladdin-studio-positions-api
- description: SQL query execution against Data Cloud datasets
  name: Aladdin Studio Queries API
  slug: aladdin-studio-queries-api
- description: Investment research data and analyst ratings
  name: Aladdin Studio Research API
  slug: aladdin-studio-research-api
- description: Risk analytics and factor exposure calculations
  name: Aladdin Studio Risk API
  slug: aladdin-studio-risk-api
- description: Security reference data and classification
  name: Aladdin Studio Securities API
  slug: aladdin-studio-securities-api
artifact_total: 108
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Aladdin Data Cloud Analytics API
  slug: open-aladdin-studio-analytics-api
- collection_type: open
  name: Aladdin Data Cloud Analytics Connections API
  slug: open-aladdin-studio-connections-api
- collection_type: open
  name: Aladdin Data Cloud Analytics Datasets API
  slug: open-aladdin-studio-datasets-api
- collection_type: open
  name: Aladdin Data Cloud Analytics Orders API
  slug: open-aladdin-studio-orders-api
- collection_type: open
  name: Aladdin Data Cloud Analytics Portfolios API
  slug: open-aladdin-studio-portfolios-api
- collection_type: open
  name: Aladdin Data Cloud Analytics Positions API
  slug: open-aladdin-studio-positions-api
- collection_type: open
  name: Aladdin Data Cloud Analytics Queries API
  slug: open-aladdin-studio-queries-api
- collection_type: open
  name: Aladdin Data Cloud Analytics Research API
  slug: open-aladdin-studio-research-api
- collection_type: open
  name: Aladdin Data Cloud Analytics Risk API
  slug: open-aladdin-studio-risk-api
- collection_type: open
  name: Aladdin Data Cloud Analytics Securities API
  slug: open-aladdin-studio-securities-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/aladdin-studio-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/aladdin-studio-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/aladdin-studio-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/aladdin-studio-scopes.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/showcase/aladdinbyblackrock
- group: start
  title: ''
  type: Portal
  url: https://www.blackrock.com/aladdin/products/apis
- group: docs
  title: ''
  type: Documentation
  url: https://www.blackrock.com/aladdin/products/aladdin-studio
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/blackrock
- group: build
  title: Python SDK (AladdinSDK)
  type: SDKs
  url: https://github.com/blackrock/aladdinsdk
- group: build
  title: Python SDK (PyPI)
  type: SDKs
  url: https://pypi.org/project/aladdinsdk/
- group: build
  title: Plugin Builder
  type: SDKs
  url: https://github.com/blackrock/aladdinsdk-plugin-builder
- group: design
  title: ''
  type: SpectralRules
  url: rules/aladdin-studio-spectral-rules.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/aladdin-studio-vocabulary.yaml
- group: design
  title: ''
  type: JSONLD
  url: json-ld/aladdin-studio-context.jsonld
created: '2024-03-05'
description: Aladdin Studio is BlackRock's developer platform enabling institutional investors, asset managers, and wealth managers to build custom solutions on top of the Aladdin investment operating system. APIs provide access to portfolio data, risk analytics, trading, investment research, and the Aladdin Data Cloud, supporting approximately $25 trillion in assets managed on the platform.
examples:
- key_count: 5
  name: Aladdin Studio Data Cloud Connection Example
  slug: aladdin-studio-data-cloud-connection-example
- key_count: 1
  name: Aladdin Studio Data Cloud Connection List Example
  slug: aladdin-studio-data-cloud-connection-list-example
- key_count: 5
  name: Aladdin Studio Data Cloud Dataset Example
  slug: aladdin-studio-data-cloud-dataset-example
- key_count: 1
  name: Aladdin Studio Data Cloud Dataset List Example
  slug: aladdin-studio-data-cloud-dataset-list-example
- key_count: 4
  name: Aladdin Studio Data Cloud Query Request Example
  slug: aladdin-studio-data-cloud-query-request-example
- key_count: 5
  name: Aladdin Studio Data Cloud Query Result Example
  slug: aladdin-studio-data-cloud-query-result-example
- key_count: 3
  name: Aladdin Studio Graph Factor Exposure Example
  slug: aladdin-studio-graph-factor-exposure-example
- key_count: 8
  name: Aladdin Studio Graph Portfolio Example
  slug: aladdin-studio-graph-portfolio-example
- key_count: 4
  name: Aladdin Studio Graph Portfolio List Example
  slug: aladdin-studio-graph-portfolio-list-example
- key_count: 8
  name: Aladdin Studio Graph Portfolio Risk Example
  slug: aladdin-studio-graph-portfolio-risk-example
- key_count: 8
  name: Aladdin Studio Graph Position Example
  slug: aladdin-studio-graph-position-example
- key_count: 4
  name: Aladdin Studio Graph Position List Example
  slug: aladdin-studio-graph-position-list-example
- key_count: 10
  name: Aladdin Studio Graph Security Example
  slug: aladdin-studio-graph-security-example
- key_count: 7
  name: Aladdin Studio Investment Research Portfolio Analytics Example
  slug: aladdin-studio-investment-research-portfolio-analytics-example
- key_count: 6
  name: Aladdin Studio Investment Research Security Research Example
  slug: aladdin-studio-investment-research-security-research-example
- key_count: 11
  name: Aladdin Studio Trading Order Example
  slug: aladdin-studio-trading-order-example
- key_count: 2
  name: Aladdin Studio Trading Order List Example
  slug: aladdin-studio-trading-order-list-example
- key_count: 6
  name: Aladdin Studio Trading Order Request Example
  slug: aladdin-studio-trading-order-request-example
features:
- description: Retrieve comprehensive portfolio data including positions, holdings, securities, and performance metrics across asset classes.
  name: Portfolio Data Access
- description: Access Aladdin's institutional-grade risk analytics including factor exposures, VaR, scenario analysis, and stress testing across public and private markets.
  name: Risk Analytics
- description: Snowflake-based data warehousing providing access to large-scale portfolio analytics with OAuth and JWT authentication supporting both Snowflake connectors and Snowpark.
  name: Aladdin Data Cloud
- description: Order management and trading workflow APIs enabling integration with Aladdin's trading platform for order creation, tracking, and execution.
  name: Trading Integration
- description: APIs for accessing investment research data, analyst insights, and quantitative analytics built on Aladdin's data infrastructure.
  name: Investment Research Access
- description: Support for long-running operation (LRO) patterns with configurable polling, enabling asynchronous processing of computationally intensive analytics requests.
  name: Long-Running Operations
- description: Batch API support with sequential and parallel execution capabilities for processing large volumes of portfolio data operations efficiently.
  name: Batch Processing
- description: Flexible authentication supporting Basic Auth with API tokens, OAuth client credentials flow, OAuth refresh token flow, and Snowflake JWT for Data Cloud access.
  name: Multi-Auth Support
- description: Extensible SDK plugin architecture enabling domain-specific packages (trading, investment research) built on top of the core AladdinSDK.
  name: Plugin Architecture
- description: Downloadable Python Jupyter Notebooks and code samples in multiple languages for rapid solution development and prototyping.
  name: Jupyter Notebook Integration
finops:
- name: Aladdin Studio Finops
  service_category: Investment Management Platform
  slug: aladdin-studio-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/aladdin-studio.png
integrations:
- description: Native Aladdin Data Cloud integration with Snowflake for large-scale analytics, supporting both standard connectors and Snowpark for Python-based data science workflows.
  name: Snowflake
- description: Aladdin available on AWS infrastructure (general availability expected second half of 2026) complementing existing Azure deployment.
  name: Amazon Web Services
- description: Primary cloud infrastructure for Aladdin platform, supporting enterprise deployments across institutional clients.
  name: Microsoft Azure
- description: Private markets data integrated into Aladdin ecosystem following BlackRock's acquisition for alternatives and private market analytics.
  name: Preqin
- description: First-class Python support via AladdinSDK on PyPI, with Jupyter Notebook examples and plugin architecture for domain extensions.
  name: Python Ecosystem
- description: ESG risk data integrated into Aladdin portfolio management for reputational and environmental risk analysis.
  name: RepRisk
json_schemas:
- name: ConnectionList
  property_count: 1
  slug: aladdin-studio-data-cloud-connection-list
- name: Connection
  property_count: 5
  slug: aladdin-studio-data-cloud-connection
- name: DatasetList
  property_count: 1
  slug: aladdin-studio-data-cloud-dataset-list
- name: Dataset
  property_count: 5
  slug: aladdin-studio-data-cloud-dataset
- name: QueryRequest
  property_count: 4
  slug: aladdin-studio-data-cloud-query-request
- name: QueryResult
  property_count: 5
  slug: aladdin-studio-data-cloud-query-result
- name: FactorExposure
  property_count: 3
  slug: aladdin-studio-graph-factor-exposure
- name: PortfolioList
  property_count: 4
  slug: aladdin-studio-graph-portfolio-list
- name: PortfolioRisk
  property_count: 8
  slug: aladdin-studio-graph-portfolio-risk
- name: Portfolio
  property_count: 8
  slug: aladdin-studio-graph-portfolio
- name: PositionList
  property_count: 4
  slug: aladdin-studio-graph-position-list
- name: Position
  property_count: 8
  slug: aladdin-studio-graph-position
- name: Security
  property_count: 10
  slug: aladdin-studio-graph-security
- name: PortfolioAnalytics
  property_count: 7
  slug: aladdin-studio-investment-research-portfolio-analytics
- name: SecurityResearch
  property_count: 6
  slug: aladdin-studio-investment-research-security-research
- name: OrderList
  property_count: 2
  slug: aladdin-studio-trading-order-list
- name: OrderRequest
  property_count: 6
  slug: aladdin-studio-trading-order-request
- name: Order
  property_count: 11
  slug: aladdin-studio-trading-order
json_structures:
- name: Aladdin Studio Data Cloud Connection List Structure
  property_count: 1
  slug: aladdin-studio-data-cloud-connection-list-structure
- name: Aladdin Studio Data Cloud Connection Structure
  property_count: 5
  slug: aladdin-studio-data-cloud-connection-structure
- name: Aladdin Studio Data Cloud Dataset List Structure
  property_count: 1
  slug: aladdin-studio-data-cloud-dataset-list-structure
- name: Aladdin Studio Data Cloud Dataset Structure
  property_count: 5
  slug: aladdin-studio-data-cloud-dataset-structure
- name: Aladdin Studio Data Cloud Query Request Structure
  property_count: 4
  slug: aladdin-studio-data-cloud-query-request-structure
- name: Aladdin Studio Data Cloud Query Result Structure
  property_count: 5
  slug: aladdin-studio-data-cloud-query-result-structure
- name: Aladdin Studio Graph Factor Exposure Structure
  property_count: 3
  slug: aladdin-studio-graph-factor-exposure-structure
- name: Aladdin Studio Graph Portfolio List Structure
  property_count: 4
  slug: aladdin-studio-graph-portfolio-list-structure
- name: Aladdin Studio Graph Portfolio Risk Structure
  property_count: 8
  slug: aladdin-studio-graph-portfolio-risk-structure
- name: Aladdin Studio Graph Portfolio Structure
  property_count: 8
  slug: aladdin-studio-graph-portfolio-structure
- name: Aladdin Studio Graph Position List Structure
  property_count: 4
  slug: aladdin-studio-graph-position-list-structure
- name: Aladdin Studio Graph Position Structure
  property_count: 8
  slug: aladdin-studio-graph-position-structure
- name: Aladdin Studio Graph Security Structure
  property_count: 10
  slug: aladdin-studio-graph-security-structure
- name: Aladdin Studio Investment Research Portfolio Analytics Structure
  property_count: 7
  slug: aladdin-studio-investment-research-portfolio-analytics-structure
- name: Aladdin Studio Investment Research Security Research Structure
  property_count: 6
  slug: aladdin-studio-investment-research-security-research-structure
- name: Aladdin Studio Trading Order List Structure
  property_count: 2
  slug: aladdin-studio-trading-order-list-structure
- name: Aladdin Studio Trading Order Request Structure
  property_count: 6
  slug: aladdin-studio-trading-order-request-structure
- name: Aladdin Studio Trading Order Structure
  property_count: 11
  slug: aladdin-studio-trading-order-structure
jsonld:
- class_count: 18
  name: Aladdin Studio Context
  property_count: 72
  slug: aladdin-studio-context
layout: provider
modified: '2026-05-19'
name: Aladdin Studio
nav: Providers
network: true
overview: 'Aladdin Studio publishes 10 APIs on the [APIs.io](https://apis.io/) network, including Analytics API, Connections API, Datasets API, and 7 more. Tagged areas include Financial, Investment Management, Portfolio Analytics, Risk Management, and Asset Management.


  The Aladdin Studio catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Aladdin Studio''s developer surface includes authentication, developer portal, documentation, and 11 more developer resources.'
plans:
- name: Aladdin Studio Plans Pricing
  plan_count: 1
  slug: aladdin-studio-plans-pricing
random_paper: 19
rate_limits:
- limit_count: 1
  name: Aladdin Studio Rate Limits
  slug: aladdin-studio-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: Aladdin Studio API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: aladdin-studio-jsonschema-spectral-rules
- effective_rule_count: 81
  extends:
  - spectral:oas
  name: Aladdin Studio API Rules
  rule_count: 40
  severity_counts:
    error: 16
    hint: 0
    info: 4
    warn: 20
  slug: aladdin-studio-spectral-rules
scopes:
- name: Aladdin Studio Scopes
  scope_count: 7
  slug: aladdin-studio-scopes
  summary_line: 7 scopes · clientCredentials/authorizationCode
score:
  band: thin
  composite: 31.4
  coverage:
    artifact_dirs: 17
    catalog_gap: 50.5
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 13.2
    commercial_clarity: 13.2
    contract_governance: 28.8
    contract_quality: 32.0
    developer_ergonomics: 54.8
    discoverability: 50.0
    governance: 28.8
    operational_transparency: 10.5
  previous_composite: 31.4
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 14
      marker_coverage: 100.0
      total: 14
  schema_version: 0.18.0
  scored_at: '2026-09-01'
  trend: flat
security:
- kind: authentication
  name: Aladdin Studio Authentication
  slug: aladdin-studio-authentication
  summary_line: http/oauth2 · 4 schemes
- kind: domain-security
  name: Aladdin Studio Domain Security
  slug: aladdin-studio-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: aladdin-studio
tags:
- Financial
- Investment Management
- Portfolio Analytics
- Risk Management
- Asset Management
- BlackRock
- Data Cloud
use_cases:
- description: Build bespoke portfolio analysis tools using Aladdin's risk and performance data to generate custom insights for investment teams.
  name: Custom Portfolio Analytics
- description: Automate generation of risk reports, factor exposure summaries, and stress test results using Aladdin's risk analytics APIs.
  name: Automated Risk Reporting
- description: Integrate Aladdin trading data into proprietary order management systems and automate trading workflow processes.
  name: Trading Workflow Automation
- description: Connect internal research platforms to Aladdin's investment research data for unified analyst workflow tooling.
  name: Investment Research Integration
- description: Access Aladdin Data Cloud from Snowflake-based data science environments for quantitative model development and backtesting.
  name: Data Science and Quantitative Research
- description: Build automated client reporting solutions pulling portfolio performance, risk, and holdings data from Aladdin APIs.
  name: Client Reporting Automation
- description: Analyze portfolios across public equities, fixed income, alternatives, and private markets using Aladdin's unified data platform.
  name: Multi-Asset Class Analytics
website: https://www.blackrock.com/aladdin/products/apis
---
