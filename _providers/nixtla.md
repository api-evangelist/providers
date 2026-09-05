---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - authentication
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 32.4
  scored_at: '2026-09-04'
agentic_access:
- acting_count: 6
  human_in_the_loop: 0
  name: Nixtla Agentic Access
  operation_count: 10
  slug: nixtla-agentic-access
  summary_line: 10 operations · 6 acting
api_count: 1
apis:
- baseURL: https://api.nixtla.io
  baseurl_source: declared
  description: The Anomaly Detection API from Nixtla — 1 operation(s) for anomaly detection.
  name: Nixtla Anomaly Detection API
  slug: nixtla-anomaly-detection-api
- baseURL: https://api.nixtla.io
  baseurl_source: declared
  description: The Cross Validation API from Nixtla — 1 operation(s) for cross validation.
  name: Nixtla Cross Validation API
  slug: nixtla-cross-validation-api
- baseURL: https://api.nixtla.io
  baseurl_source: declared
  description: The excluded API from Nixtla — 1 operation(s) for excluded.
  name: Nixtla excluded API
  slug: nixtla-excluded-api
- baseURL: https://api.nixtla.io
  baseurl_source: declared
  description: The Finetune API from Nixtla — 1 operation(s) for finetune.
  name: Nixtla Finetune API
  slug: nixtla-finetune-api
- baseURL: https://api.nixtla.io
  baseurl_source: declared
  description: The Finetuned Models API from Nixtla — 2 operation(s) for finetuned models.
  name: Nixtla Finetuned Models API
  slug: nixtla-finetuned-models-api
- baseURL: https://api.nixtla.io
  baseurl_source: declared
  description: The Forecast API from Nixtla — 1 operation(s) for forecast.
  name: Nixtla Forecast API
  slug: nixtla-forecast-api
- baseURL: https://api.nixtla.io
  baseurl_source: declared
  description: The Online Anomaly Detection API from Nixtla — 1 operation(s) for online anomaly detection.
  name: Nixtla Online Anomaly Detection API
  slug: nixtla-online-anomaly-detection-api
- baseURL: https://api.nixtla.io
  baseurl_source: declared
  description: The Validate Api Key API from Nixtla — 1 operation(s) for validate api key.
  name: Nixtla Validate Api Key API
  slug: nixtla-validate-api-key-api
artifact_total: 22
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Nixtla Forecast Anomaly Detection API
  slug: open-nixtla-anomaly-detection-api
- collection_type: open
  name: Nixtla Forecast Anomaly Detection Cross Validation API
  slug: open-nixtla-cross-validation-api
- collection_type: open
  name: Nixtla Forecast Anomaly Detection excluded API
  slug: open-nixtla-excluded-api
- collection_type: open
  name: Nixtla Forecast Anomaly Detection Finetune API
  slug: open-nixtla-finetune-api
- collection_type: open
  name: Nixtla Forecast Anomaly Detection Finetuned Models API
  slug: open-nixtla-finetuned-models-api
- collection_type: open
  name: Nixtla Anomaly Detection Forecast API
  slug: open-nixtla-forecast-api
- collection_type: open
  name: Nixtla Forecast Anomaly Detection Online Anomaly Detection API
  slug: open-nixtla-online-anomaly-detection-api
- collection_type: open
  name: Nixtla Forecast Anomaly Detection Validate Api Key API
  slug: open-nixtla-validate-api-key-api
common:
- group: other
  title: ''
  type: Overlay
  url: overlays/nixtla-forecast-overlay.yaml
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
- description: Nixtla ships MCP tools that expose TimeGPT time-series forecasting and anomaly detection to AI agents. Announced 2025-12-18 as part of Nixtla Enterprise's foundation-models + MCP + agentic release. Di
  name: Nixtla MCP Server
  slug: nixtla-mcp-server
modified: '2026-07-20'
name: Nixtla
nav: Providers
network: true
overview: 'Nixtla publishes 8 APIs on the [APIs.io](https://apis.io/) network, including Anomaly Detection API, Cross Validation API, excluded API, and 5 more. Tagged areas include Company, Time Series, Forecasting, Anomaly Detection, and Machine-Learning.


  Nixtla''s developer surface includes documentation, API reference, getting-started guide, authentication, changelog, engineering blog, pricing, and 23 more developer resources.'
random_paper: 5
score:
  band: developing
  composite: 50.3
  coverage:
    artifact_dirs: 19
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 52.6
    commercial_clarity: 52.6
    contract_governance: 4.5
    contract_quality: 56.0
    developer_ergonomics: 66.1
    discoverability: 75.9
    governance: 4.5
    operational_transparency: 34.2
  previous_composite: 50.3
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
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/nixtla/refs/heads/main/screenshots/nixtla-2026-08-07T185350.png
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
- Machine-Learning
- Artificial Intelligence
- Foundation Model
- Predictive Analytics
- Data Science
website: https://nixtla.io/
---
