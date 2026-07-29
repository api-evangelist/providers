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
    agentic_access: derived
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: verified
    idempotency: false
    mcp_server: true
    openapi_examples: verified
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 52.9
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 6
  human_in_the_loop: 0
  name: Nixtla Agentic Access
  operation_count: 10
  slug: nixtla-agentic-access
  summary_line: 10 operations · 6 acting
api_count: 8
apis:
- description: The Anomaly Detection API from Nixtla — 1 operation(s) for anomaly detection.
  name: Nixtla Anomaly Detection API
  slug: nixtla-anomaly-detection-api
- description: The Cross Validation API from Nixtla — 1 operation(s) for cross validation.
  name: Nixtla Cross Validation API
  slug: nixtla-cross-validation-api
- description: The excluded API from Nixtla — 1 operation(s) for excluded.
  name: Nixtla excluded API
  slug: nixtla-excluded-api
- description: The Finetune API from Nixtla — 1 operation(s) for finetune.
  name: Nixtla Finetune API
  slug: nixtla-finetune-api
- description: The Finetuned Models API from Nixtla — 2 operation(s) for finetuned models.
  name: Nixtla Finetuned Models API
  slug: nixtla-finetuned-models-api
- description: The Forecast API from Nixtla — 1 operation(s) for forecast.
  name: Nixtla Forecast API
  slug: nixtla-forecast-api
- description: The Online Anomaly Detection API from Nixtla — 1 operation(s) for online anomaly detection.
  name: Nixtla Online Anomaly Detection API
  slug: nixtla-online-anomaly-detection-api
- description: The Validate Api Key API from Nixtla — 1 operation(s) for validate api key.
  name: Nixtla Validate Api Key API
  slug: nixtla-validate-api-key-api
artifact_total: 13
common:
- group: start
  title: ''
  type: DeveloperPortal
  url: https://www.nixtla.io/docs
- group: docs
  title: ''
  type: Documentation
  url: https://www.nixtla.io/docs
- group: docs
  title: ''
  type: APIReference
  url: https://www.nixtla.io/docs/api-reference/foundational-time-series-model-multi-series
- group: start
  title: ''
  type: GettingStarted
  url: https://www.nixtla.io/docs/forecasting/timegpt_quickstart
- group: build
  title: ''
  type: SDKs
  url: packages/nixtla-packages.yml
- group: build
  title: ''
  type: Packages
  url: packages/nixtla-packages.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/nixtla-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/nixtla-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/nixtla-problem-types.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/nixtla-data-model.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/nixtla-lifecycle.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://status.nixtla.io/
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/nixtla-changelog.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/nixtla-mcp.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/nixtla-agentic-access.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/nixtla-llms.txt
- group: design
  title: ''
  type: Conformance
  url: conformance/nixtla-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: https://trust.nixtla.io/
- group: auth
  title: ''
  type: TrustCenter
  url: security/nixtla-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/nixtla-domain-security.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Nixtla
- group: company
  title: ''
  type: Blog
  url: https://www.nixtla.io/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://www.nixtla.io/docs/introduction/timegpt_subscription_plans
- group: start
  title: ''
  type: SignUp
  url: https://nixtla.io/free-trial
- group: operate
  title: ''
  type: Support
  url: https://www.nixtla.io/docs
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.nixtla.io/docs/about/terms-and-conditions
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.nixtla.io/docs/about/privacy-notice
- group: company
  title: ''
  type: Website
  url: https://nixtla.io/
created: '2026-07-17'
description: Nixtla is an enterprise time-series intelligence platform built around TimeGPT, the first foundation model for time series. Through a simple REST API and Python/R SDKs it delivers zero-shot forecasting (no training data required), batch and real-time anomaly detection, cross-validation, and fine-tuning of the foundation model on customer data. The Nixtla Forecast API (OpenAPI 3.1) exposes /v2 endpoints for forecasting, anomaly detection, online anomaly detection, cross-validation, fine-tuning, and fine-tuned-model management, authenticated with a bearer API key. Nixtla also maintains a widely used open-source forecasting ecosystem (StatsForecast, NeuralForecast, MLForecast, HierarchicalForecast, CoreForecast) with tens of millions of downloads, offers cloud, self-hosted, and air-gapped deployments, ships MCP tools for agentic time-series workflows, and is SOC 2 Type II compliant. Nixtla is backed by Techstars and True Ventures.
image: https://www.nixtla.io/logo.png
layout: provider
mcp_servers:
- description: ''
  name: nixtla-mcp.yml
  slug: nixtla-mcpyml
modified: '2026-07-20'
name: Nixtla
nav: Providers
network: true
overview: 'Nixtla publishes 8 APIs on the [APIs.io](https://apis.io/) network, including Anomaly Detection API, Cross Validation API, excluded API, and 5 more. Tagged areas include Company, Time Series, Forecasting, Anomaly Detection, and Machine Learning.


  Nixtla''s developer surface includes documentation, API reference, getting-started guide, authentication, changelog, engineering blog, pricing, and 22 more developer resources.'
random_paper: 8
score:
  band: strong
  composite: 56.0
  delta: 0.1
  facets:
    commercial_clarity: 60.5
    contract_quality: 58.9
    developer_ergonomics: 69.0
    discoverability: 92.6
    governance: 11.5
    operational_transparency: 36.8
  previous_composite: 55.9
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 8
    mcp: first-party
    skills: derived
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
security:
- kind: authentication
  name: Nixtla Authentication
  slug: nixtla-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Nixtla Domain Security
  slug: nixtla-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: trust-center
  name: Nixtla Trust Center
  slug: nixtla-trust-center
  summary_line: SOC 2 Type II
slug: nixtla
tags:
- Company
- Time Series
- Forecasting
- Anomaly Detection
- Machine Learning
- Artificial Intelligence
- Foundation Model
- Predictive Analytics
- Data Science
website: https://nixtla.io/
---
