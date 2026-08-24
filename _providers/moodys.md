---
access_model:
  confidence: high
  label: Enterprise · Requires approval
  onboarding: approval
  pricing: enterprise
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: verified
    event_surface_described: true
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.2
  score: 45.5
  scored_at: '2026-08-24'
agentic_access:
- acting_count: 6
  human_in_the_loop: 0
  name: Moodys Agentic Access
  operation_count: 17
  slug: moodys-agentic-access
  summary_line: 17 operations · 6 acting
api_count: 14
apis:
- description: Moody's Analytics Data Buffet application program interface enables you to retrieve economic, demographic and financial time series directly from the Data Buffet repository, including international an
  name: Moody's Data Buffet API
  slug: data-buffet-api
- description: Retrieves expected consumer credit loss forecasts under baseline and stress scenarios. The ECCL API combines customer data, economic data from Moody's Analytics, and consumer credit data for credit ri
  name: Moody's Consumer Credit Loss Forecasts API
  slug: eccl-api
- description: The EDF-X API provides easy access to probability of default calculations for approximately 400 million companies globally via the Orbis database. It provides a PD term structure with annualized, cumu
  name: Moody's EDF-X API
  slug: edf-x-api
- description: Moody's Analytics QUIQspread is an intelligent, financial spreading software that will accelerate a company's spreading process. The API enables integration of automated financial statement processing
  name: Moody's QUIQSpread API
  slug: quiqspread-api
- description: Moody's Analytics Capital Risk Analyzer solution is a tool that projects key capital ratios and credit metrics based on various strategic and economic scenarios for capital planning and stress testing
  name: Moody's Capital Risk Analyzer API
  slug: capital-risk-analyzer-api
- description: The Climate On Demand API enables financial services organizations to build physical climate risk applications that leverage the power of the Intelligent Risk Platform.
  name: Moody's Climate on Demand API
  slug: climate-on-demand-api
- description: Location Intelligence API delivers more than 100 data layers across multiple kinds of data including hazard, location, risk score, model, and exposure data to help improve business decisions and bette
  name: Moody's Location Intelligence API
  slug: location-intelligence-api
- description: The Risk Modeler API enables you to manage end-to-end catastrophe modeling workflows using Moody's RMS models for portfolios, accounts, and locations on the Intelligent Risk Platform.
  name: Moody's Risk Modeler API
  slug: risk-modeler-api
- description: Moody's RMS Platform APIs are a collection of REST APIs that enable Intelligent Risk Platform tenants to work more efficiently. Risk Modeler, UnderwriteIQ, TreatyIQ, and ExposureIQ tenants can use the
  name: Moody's Intelligent Risk Platform API
  slug: intelligent-risk-platform-api
- description: API solutions to empower commercial real estate developers to build systems and platforms faster. Brings efficiency and automation into your organization, including the Commercial Location Score API a
  name: Moody's Commercial Real Estate API
  slug: commercial-real-estate-api
- description: Bring together real-time news sources, and the best of the business web and social media to empower decision makers. The NewsEdge API provides access to Moody's 24,000+ news sources for integration in
  name: Moody's NewsEdge API
  slug: newsedge-api
- description: Moody's Analytics AutoCycle API from Moody's — 3 path(s) described in OpenAPI.
  name: Moody's Analytics AutoCycle API
  slug: moodys-autocycle-api-swagger
- description: Moody's Analytics Muni Loss Forecast API from Moody's — 2 path(s) described in OpenAPI.
  name: Moody's Analytics Muni Loss Forecast API
  slug: moodys-municipal-api-swagger
- description: Moody's Scenario Studio Api from Moody's — 57 path(s) described in OpenAPI.
  name: Moody's Scenario Studio Api
  slug: moodys-scenario-studio-api-swagger
artifact_total: 102
collections:
- collection_type: postman
  name: Moody's Data Buffet Baskets API
  slug: postman-moodys-baskets-api
- collection_type: postman
  name: Moody's Data Buffet Baskets Health API
  slug: postman-moodys-health-api
- collection_type: postman
  name: Moody's Data Buffet Baskets Orders API
  slug: postman-moodys-orders-api
- collection_type: postman
  name: Moody's Data Buffet Baskets Reference API
  slug: postman-moodys-reference-api
- collection_type: postman
  name: Moody's Data Buffet Baskets Search API
  slug: postman-moodys-search-api
- collection_type: postman
  name: Moody's Data Buffet Baskets Series API
  slug: postman-moodys-series-api
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Moody's Analytics AutoCycle API
  slug: open-moodys-autocycle-api-swagger
- collection_type: open
  name: Moody's Data Buffet Baskets API
  slug: open-moodys-baskets-api
- collection_type: open
  name: Moody's Data Buffet API
  slug: open-moodys-data-buffet-api
- collection_type: open
  name: Moody's Data Buffet Baskets Health API
  slug: open-moodys-health-api
- collection_type: open
  name: Moody's Analytics Muni Loss Forecast API
  slug: open-moodys-municipal-api-swagger
- collection_type: open
  name: Moody's Data Buffet Baskets Orders API
  slug: open-moodys-orders-api
- collection_type: open
  name: Moody's Data Buffet Baskets Reference API
  slug: open-moodys-reference-api
- collection_type: open
  name: Scenario Studio Api
  slug: open-moodys-scenario-studio-api-swagger
- collection_type: open
  name: Moody's Data Buffet Baskets Search API
  slug: open-moodys-search-api
- collection_type: open
  name: Moody's Data Buffet Baskets Series API
  slug: open-moodys-series-api
common:
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/moodys/overview
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/moodys-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/moodys-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/moodys-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/moodys-scopes.yml
- group: build
  title: ''
  type: Packages
  url: packages/moodys-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/moodys-packages.yml
- group: build
  title: ''
  type: CLI
  url: cli/moodys-cli.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/moodys-well-known.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/moodys-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/moodys-llms.txt
- group: design
  title: ''
  type: Conformance
  url: conformance/moodys-conformance.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/moodys-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/moodys-lifecycle.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/moodys-conventions.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/moodys-data-model.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/moodys-sandbox.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  title: ''
  type: Webhooks
  url: https://www.kompany.com/kycapi/docs/guides/guides/working-with-endpoints/working-with-webhooks
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.moodys.com/termsofuseinfo.aspx
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.moodys.com/privatepolicy.aspx
- group: start
  title: ''
  type: Portal
  url: https://www.kompany.com/
- group: commercial
  title: ''
  type: Plans
  url: https://www.kompany.com/kycapi/dashboard/plans
- group: start
  title: ''
  type: GettingStarted
  url: https://www.kompany.com/kycapi/docs/quick-start
- group: start
  title: ''
  type: Console
  url: https://www.kompany.com/kycapi/console
- group: company
  title: ''
  type: Blog
  url: https://www.kompany.com/kycapi/community/developer-news
- group: start
  title: ''
  type: GettingStarted
  url: https://www.kompany.com/kycapi/docs/guides/guides/get-started
- group: start
  title: ''
  type: Sandbox
  url: https://www.kompany.com/kycapi/docs/guides/guides/get-started/sandbox-overview
- group: other
  title: ''
  type: Resources
  url: https://www.kompany.com/kycapi/docs/resources
- group: operate
  title: ''
  type: StatusPage
  url: https://kycapi-status.kompany.com/
- group: start
  title: ''
  type: Portal
  url: https://hub.moodysanalytics.com/
- group: docs
  title: ''
  type: Documentation
  url: https://hub.moodysanalytics.com/products
- group: start
  title: ''
  type: GettingStarted
  url: https://hub.moodysanalytics.com/gettingstarted
- group: operate
  title: ''
  type: Contact
  url: https://hub.moodysanalytics.com/contact
- group: start
  title: ''
  type: Portal
  url: https://developer.rms.com/
- group: docs
  title: ''
  type: Documentation
  url: https://www.economy.com/products/tools/api
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/moodysanalytics
- group: other
  title: ''
  type: Resources
  url: https://www.rms.com/developer-resources
created: '2024-09-25T00:00:00.000Z'
description: Moody's provides a comprehensive suite of APIs spanning KYC compliance, economic data and forecasting, credit risk analytics, insurance and catastrophe modeling, climate risk, commercial real estate, and news aggregation. With evolving regulatory pressures and increasingly complex risk landscapes, Moody's technology, data, and analytical capabilities power industry-leading solutions across financial services, insurance, and risk management.
examples:
- key_count: 3
  name: Moodys Data Buffet Access Token Example
  slug: moodys-data-buffet-access-token-example
- key_count: 3
  name: Moodys Data Buffet Basket Create Example
  slug: moodys-data-buffet-basket-create-example
- key_count: 6
  name: Moodys Data Buffet Basket Example
  slug: moodys-data-buffet-basket-example
- key_count: 3
  name: Moodys Data Buffet Error Example
  slug: moodys-data-buffet-error-example
- key_count: 4
  name: Moodys Data Buffet File Type Example
  slug: moodys-data-buffet-file-type-example
- key_count: 3
  name: Moodys Data Buffet Frequency Info Example
  slug: moodys-data-buffet-frequency-info-example
- key_count: 3
  name: Moodys Data Buffet Health Status Example
  slug: moodys-data-buffet-health-status-example
- key_count: 1
  name: Moodys Data Buffet Multi Series Request Example
  slug: moodys-data-buffet-multi-series-request-example
- key_count: 1
  name: Moodys Data Buffet Multi Series Response Example
  slug: moodys-data-buffet-multi-series-response-example
- key_count: 3
  name: Moodys Data Buffet Observation Example
  slug: moodys-data-buffet-observation-example
- key_count: 2
  name: Moodys Data Buffet Order Create Example
  slug: moodys-data-buffet-order-create-example
- key_count: 8
  name: Moodys Data Buffet Order Example
  slug: moodys-data-buffet-order-example
- key_count: 4
  name: Moodys Data Buffet Search Results Example
  slug: moodys-data-buffet-search-results-example
- key_count: 6
  name: Moodys Data Buffet Series Request Example
  slug: moodys-data-buffet-series-request-example
- key_count: 13
  name: Moodys Data Buffet Series Response Example
  slug: moodys-data-buffet-series-response-example
- key_count: 9
  name: Moodys Data Buffet Series Summary Example
  slug: moodys-data-buffet-series-summary-example
- key_count: 2
  name: Moodys Data Buffet Vintage Example
  slug: moodys-data-buffet-vintage-example
features:
- 'Moody''s: API access via partner / B2B contracts only'
- No public API pricing published — contact enterprise sales
- Moody's Analytics APIs (Ratings, Risk, Economics) are enterprise data subscriptions priced per data product.
finops:
- name: Moodys Finops
  service_category: Financial Data / Ratings
  slug: moodys-finops
image: /assets/icons/moodys.png
json_schemas:
- name: AccessToken
  property_count: 3
  slug: moodys-data-buffet-access-token
- name: BasketCreate
  property_count: 3
  slug: moodys-data-buffet-basket-create
- name: Basket
  property_count: 6
  slug: moodys-data-buffet-basket
- name: Error
  property_count: 3
  slug: moodys-data-buffet-error
- name: FileType
  property_count: 4
  slug: moodys-data-buffet-file-type
- name: FrequencyInfo
  property_count: 3
  slug: moodys-data-buffet-frequency-info
- name: HealthStatus
  property_count: 3
  slug: moodys-data-buffet-health-status
- name: MultiSeriesRequest
  property_count: 1
  slug: moodys-data-buffet-multi-series-request
- name: MultiSeriesResponse
  property_count: 1
  slug: moodys-data-buffet-multi-series-response
- name: Observation
  property_count: 3
  slug: moodys-data-buffet-observation
- name: OrderCreate
  property_count: 2
  slug: moodys-data-buffet-order-create
- name: Order
  property_count: 8
  slug: moodys-data-buffet-order
- name: SearchResults
  property_count: 4
  slug: moodys-data-buffet-search-results
- name: SeriesRequest
  property_count: 6
  slug: moodys-data-buffet-series-request
- name: SeriesResponse
  property_count: 13
  slug: moodys-data-buffet-series-response
- name: SeriesSummary
  property_count: 9
  slug: moodys-data-buffet-series-summary
- name: Vintage
  property_count: 2
  slug: moodys-data-buffet-vintage
- name: Moody's Analytics Time Series
  property_count: 17
  slug: moodys-time-series
json_structures:
- name: Moodys Data Buffet Access Token Structure
  property_count: 3
  slug: moodys-data-buffet-access-token-structure
- name: Moodys Data Buffet Basket Create Structure
  property_count: 3
  slug: moodys-data-buffet-basket-create-structure
- name: Moodys Data Buffet Basket Structure
  property_count: 6
  slug: moodys-data-buffet-basket-structure
- name: Moodys Data Buffet Error Structure
  property_count: 3
  slug: moodys-data-buffet-error-structure
- name: Moodys Data Buffet File Type Structure
  property_count: 4
  slug: moodys-data-buffet-file-type-structure
- name: Moodys Data Buffet Frequency Info Structure
  property_count: 3
  slug: moodys-data-buffet-frequency-info-structure
- name: Moodys Data Buffet Health Status Structure
  property_count: 3
  slug: moodys-data-buffet-health-status-structure
- name: Moodys Data Buffet Multi Series Request Structure
  property_count: 1
  slug: moodys-data-buffet-multi-series-request-structure
- name: Moodys Data Buffet Multi Series Response Structure
  property_count: 1
  slug: moodys-data-buffet-multi-series-response-structure
- name: Moodys Data Buffet Observation Structure
  property_count: 3
  slug: moodys-data-buffet-observation-structure
- name: Moodys Data Buffet Order Create Structure
  property_count: 2
  slug: moodys-data-buffet-order-create-structure
- name: Moodys Data Buffet Order Structure
  property_count: 8
  slug: moodys-data-buffet-order-structure
- name: Moodys Data Buffet Search Results Structure
  property_count: 4
  slug: moodys-data-buffet-search-results-structure
- name: Moodys Data Buffet Series Request Structure
  property_count: 6
  slug: moodys-data-buffet-series-request-structure
- name: Moodys Data Buffet Series Response Structure
  property_count: 13
  slug: moodys-data-buffet-series-response-structure
- name: Moodys Data Buffet Series Summary Structure
  property_count: 9
  slug: moodys-data-buffet-series-summary-structure
- name: Moodys Data Buffet Vintage Structure
  property_count: 2
  slug: moodys-data-buffet-vintage-structure
jsonld:
- class_count: 0
  name: Moodys Context
  property_count: 6
  slug: moodys-context
- class_count: 0
  name: Moodys Data Buffet Context
  property_count: 0
  slug: moodys-data-buffet-context
layout: provider
mcp_servers:
- description: ''
  name: Moody's MCP Server
  slug: moodys-mcp-server
modified: '2026-07-25'
name: Moody's
nav: Providers
network: true
overview: 'Moody''s publishes 4 APIs on the [APIs.io](https://apis.io/) network, including Data Buffet API, Analytics AutoCycle API, Analytics Muni Loss Forecast API, and 1 more. Tagged areas include Climate Risk, Compliance, Credit Risk, Economic Data, and Entity Verification.


  The Moody''s catalog on APIs.io includes 2 JSON-LD contexts and 2 Spectral governance rulesets.


  Moody''s'' developer surface includes authentication, CLI, sandbox, developer portal, getting-started guide, developer console, engineering blog, and 31 more developer resources.'
plans:
- name: Moodys Plans Pricing
  plan_count: 1
  slug: moodys-plans-pricing
press:
- date: '2026-05-25'
  title: Responsible AI Principles at Moody's
  url: https://www.moodys.com/web/en/us/innovation/ai-principles.html
- date: '2026-05-25'
  title: Artificial intelligence insights
  url: https://www.moodys.com/web/en/us/insights/ai.html
- date: '2026-05-25'
  title: Moody's AI Principles
  url: https://www.moodys.com/web/en/us/about-us/trust-center/ai-principles.html
- date: '2026-05-25'
  title: Artificial intelligence on trial
  url: https://www.moodys.com/web/en/us/insights/insurance/artificial-intelligence-on-trial.html
- date: '2026-05-25'
  title: Moody's Advances Decision-Grade Credit Intelligence ...
  url: https://www.businesswire.com/news/home/20260421137955/en/Moodys-Advances-Decision-Grade-Credit-Intelligence-Across-Enterprise-AI-Workflows-Powered-by-Microsoft-365-Copilot
random_paper: 16
rate_limits:
- limit_count: 1
  name: Moodys Rate Limits
  slug: moodys-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: Moody's API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: moodys-jsonschema-spectral-rules
- effective_rule_count: 58
  extends:
  - spectral:oas
  name: Moody's API Rules
  rule_count: 17
  severity_counts:
    error: 8
    hint: 0
    info: 1
    warn: 8
  slug: moodys-spectral-rules
scopes:
- name: Moodys Scopes
  scope_count: 0
  slug: moodys-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: strong
  composite: 58.8
  delta: 0.0
  facets:
    access_clarity: 34.2
    commercial_clarity: 34.2
    contract_governance: 30.3
    contract_quality: 53.7
    developer_ergonomics: 73.2
    discoverability: 92.6
    governance: 30.3
    operational_transparency: 34.2
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: no_resolvable_host
  previous_composite: 58.8
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 6
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Insurance
    regime_id: insurance
    score: 71.2
  schema_version: 0.12.1
  scored_at: '2026-08-24'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/moodys/refs/heads/main/screenshots/moodys-2026-06-20T185751.png
security:
- kind: authentication
  name: Moodys Authentication
  slug: moodys-authentication
  summary_line: oauth2 · 4 schemes
- kind: domain-security
  name: Moodys Domain Security
  slug: moodys-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: moodys
tags:
- Climate Risk
- Compliance
- Credit Risk
- Economic Data
- Entity Verification
- Financial Analytics
- Insurance
- KYC
- Risk
- Screening
use_cases:
- description: Evaluate counterparty credit risk using EDF-X probability of default and loss given default models.
  name: Credit Risk Assessment
- description: Generate stress scenarios for DFAST, CCAR, and EBA regulatory compliance testing.
  name: Regulatory Stress Testing
- description: Automate financial spreading and credit analysis workflows for commercial loan underwriting.
  name: Commercial Lending
- description: Model insurance portfolio risk exposure using catastrophe models and location intelligence.
  name: Catastrophe Modeling
website: https://www.kompany.com/
---
