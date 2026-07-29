---
access_model:
  confidence: medium
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: verified
    idempotency: false
    mcp_server: derived
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 36.3
  scored_at: '2026-07-28'
api_count: 19
apis:
- description: The Alert API from Prevedere — 1 operation(s) for alert.
  name: Prevedere Alert API
  slug: prevedere-alert-api
- description: The AlertDefinition API from Prevedere — 2 operation(s) for alertdefinition.
  name: Prevedere AlertDefinition API
  slug: prevedere-alertdefinition-api
- description: The AnalysisJob API from Prevedere — 2 operation(s) for analysisjob.
  name: Prevedere AnalysisJob API
  slug: prevedere-analysisjob-api
- description: The ComponentContributionOverrideValues API from Prevedere — 2 operation(s) for componentcontributionoverridevalues.
  name: Prevedere ComponentContributionOverrideValues API
  slug: prevedere-componentcontributionoverridevalues-api
- description: The Context API from Prevedere — 1 operation(s) for context.
  name: Prevedere Context API
  slug: prevedere-context-api
- description: The DataIntegration API from Prevedere — 3 operation(s) for dataintegration.
  name: Prevedere DataIntegration API
  slug: prevedere-dataintegration-api
- description: The DiscoverJob API from Prevedere — 2 operation(s) for discoverjob.
  name: Prevedere DiscoverJob API
  slug: prevedere-discoverjob-api
- description: The Enumeration API from Prevedere — 6 operation(s) for enumeration.
  name: Prevedere Enumeration API
  slug: prevedere-enumeration-api
- description: The Favorites API from Prevedere — 2 operation(s) for favorites.
  name: Prevedere Favorites API
  slug: prevedere-favorites-api
- description: The ForecastModel API from Prevedere — 16 operation(s) for forecastmodel.
  name: Prevedere ForecastModel API
  slug: prevedere-forecastmodel-api
- description: The ForecastModelHistory API from Prevedere — 1 operation(s) for forecastmodelhistory.
  name: Prevedere ForecastModelHistory API
  slug: prevedere-forecastmodelhistory-api
- description: The ForecastSummary API from Prevedere — 2 operation(s) for forecastsummary.
  name: Prevedere ForecastSummary API
  slug: prevedere-forecastsummary-api
- description: The Indicator API from Prevedere — 9 operation(s) for indicator.
  name: Prevedere Indicator API
  slug: prevedere-indicator-api
- description: The Provider API from Prevedere — 1 operation(s) for provider.
  name: Prevedere Provider API
  slug: prevedere-provider-api
- description: The Scenario API from Prevedere — 2 operation(s) for scenario.
  name: Prevedere Scenario API
  slug: prevedere-scenario-api
- description: The Tag API from Prevedere — 1 operation(s) for tag.
  name: Prevedere Tag API
  slug: prevedere-tag-api
- description: The Test API from Prevedere — 1 operation(s) for test.
  name: Prevedere Test API
  slug: prevedere-test-api
- description: The UserContext API from Prevedere — 2 operation(s) for usercontext.
  name: Prevedere UserContext API
  slug: prevedere-usercontext-api
- description: Workbenches are a powerful feature in the Board Foresight application that allow users to organize and analyze data through indicators. They enable the creation of models by selecting primary and addi
  name: Prevedere Workbench API
  slug: prevedere-workbench-api
artifact_total: 22
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/prevedere-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/prevedere-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://prevedere.com
- group: docs
  title: ''
  type: Documentation
  url: https://api.prevedere.com/docs/
- group: docs
  title: ''
  type: APIReference
  url: https://api.prevedere.com/docs/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.board.com/pricing
- group: operate
  title: ''
  type: Support
  url: https://community.board.com/categories/support
- group: operate
  title: ''
  type: StatusPage
  url: https://status.board.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.board.com/legal-notice
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.board.com/privacy-policy
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/prevedere-problem-types.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/prevedere-conventions.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/prevedere-conformance.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/prevedere-data-model.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/prevedere-lifecycle.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/prevedere-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/prevedere-llms.txt
- group: other
  title: ''
  type: Overlay
  url: overlays/prevedere-openapi-overlay.yaml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-07-17'
description: Prevedere is an economic forecasting and predictive analytics platform that ingests thousands of external macroeconomic, industry, weather, and market indicators to drive demand planning, financial forecasting, and risk analysis. Its models correlate a company's internal metrics against leading external signals to project revenue, demand, and other business outcomes. Prevedere was acquired by Board International and its capability is now delivered as Board Foresight; the live Board Foresight API (V1), hosted at api.prevedere.com, exposes forecast models, indicators, scenarios, alerts, correlation discovery, and client-data integration. This profile enriches the surviving API surface.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/prevedere.png
layout: provider
mcp_servers:
- description: ''
  name: prevedere-mcp.yml
  slug: prevedere-mcpyml
modified: '2026-07-20'
name: Prevedere
nav: Providers
network: true
overview: 'Prevedere publishes 19 APIs on the [APIs.io](https://apis.io/) network, including Alert API, AlertDefinition API, AnalysisJob API, and 16 more. Tagged areas include Company, Economic Forecasting, Predictive Analytics, Demand Planning, and Financial Planning.


  Prevedere''s developer surface includes authentication, documentation, API reference, pricing, support, and 14 more developer resources.'
random_paper: 14
score:
  band: thin
  composite: 35.9
  delta: -2.1
  facets:
    commercial_clarity: 31.6
    contract_quality: 40.0
    developer_ergonomics: 34.2
    discoverability: 92.6
    governance: 11.5
    operational_transparency: 15.8
  previous_composite: 38.0
  provenance:
    conformance: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 19
    mcp: derived
    skills: derived
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
security:
- kind: authentication
  name: Prevedere Authentication
  slug: prevedere-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Prevedere Domain Security
  slug: prevedere-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: prevedere
tags:
- Company
- Economic Forecasting
- Predictive Analytics
- Demand Planning
- Financial Planning
- Macroeconomic Data
- Indicators
- Time Series
- Data Integration
- Machine Learning
website: https://prevedere.com
---
