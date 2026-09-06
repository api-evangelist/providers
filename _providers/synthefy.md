---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - authentication
  - rate-limits
  - security
  trial: false
  try_now: false
agent_readiness:
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 5.0
  scored_at: '2026-09-05'
api_count: 2
apis:
- description: Direct REST access to Synthefy's foundation models for multivariate time-series forecasting (Migas-1.0), with automatic timestamp/value/metadata handling and exogenous covariate context. Called via th
  name: Synthefy Forecasting API
  slug: synthefy-forecasting-api
- description: Hosted in-context tabular regression and classification via the Nori foundation model. Predicts on any table in a single forward pass with no training; served over an OpenAI-style Bearer-authenticated
  name: Synthefy Nori API
  slug: synthefy-nori-api
artifact_total: 5
common:
- group: company
  title: ''
  type: Website
  url: https://www.synthefy.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.synthefy.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.synthefy.com/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.synthefy.com/forecasting-api/overview
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.synthefy.com/forecasting-api/cloud-quickstart
- group: company
  title: ''
  type: Blog
  url: https://www.synthefy.com/blog
- group: operate
  title: ''
  type: Support
  url: https://www.synthefy.com/contact
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Synthefy
- group: start
  title: ''
  type: SignUp
  url: https://console.synthefy.com/
- group: start
  title: ''
  type: Login
  url: https://console.synthefy.com/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.synthefy.com/privacy
- group: auth
  title: ''
  type: Compliance
  url: https://www.synthefy.com/
- group: auth
  title: ''
  type: Authentication
  url: authentication/synthefy-authentication.yml
- group: build
  title: ''
  type: Packages
  url: packages/synthefy-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/synthefy-packages.yml
- group: agent
  title: ''
  type: X-MCPServerCandidate
  url: mcp/synthefy-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/synthefy-llms.txt
- group: design
  title: ''
  type: Conformance
  url: conformance/synthefy-conformance.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/synthefy-conventions.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/synthefy-rate-limits.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/synthefy-lifecycle.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/synthefy-changelog.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/synthefy-domain-security.yml
created: '2026-07-17'
description: Synthefy builds foundation models for structured data, replacing task-specific machine learning (XGBoost, LightGBM, ARIMA, Prophet) with a single API call. Its Nori tabular model performs in-context regression and classification on any table with no training, and its time-series Forecasting API (Migas-1.0) delivers multivariate probabilistic forecasts with exogenous context. The platform is delivered as a hosted REST API, Python SDKs, Docker containers, AWS SageMaker, and Snowflake, serving banking, retail, insurance, healthcare, infrastructure, and marketing use cases with SOC 2 Type II, HIPAA, GDPR, and zero-data-retention compliance.
image: https://synthefy.com/opengraph-image
layout: provider
modified: '2026-07-21'
name: Synthefy
nav: Providers
network: true
overview: 'Synthefy publishes 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Foundation Models, Machine-Learning, Forecasting, and Time Series.


  Synthefy''s developer surface includes documentation, API reference, getting-started guide, engineering blog, support, signup flow, authentication, and 16 more developer resources.'
random_paper: 8
rate_limits:
- limit_count: 2
  name: Synthefy Rate Limits
  slug: synthefy-rate-limits
score:
  band: thin
  composite: 31.2
  coverage:
    artifact_dirs: 13
    catalog_earned: 45.0
    catalog_earned_first_party: 8.0
    catalog_gap: 70.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 18.4
    commercial_clarity: 18.4
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 63.1
    discoverability: 75.9
    governance: 18.2
    operational_transparency: 39.5
  previous_composite: 31.2
  provenance:
    conformance: first-party
    mcp: derived
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/synthefy/refs/heads/main/screenshots/synthefy-2026-09-02T161632.png
security:
- kind: authentication
  name: Synthefy Authentication
  slug: synthefy-authentication
  summary_line: apiKey/http · 2 schemes
- kind: domain-security
  name: Synthefy Domain Security
  slug: synthefy-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: synthefy
tags:
- Company
- Foundation Models
- Machine-Learning
- Forecasting
- Time Series
- Tabular Data
- Synthetic Data
- Artificial Intelligence
- Predictive Analytics
website: https://www.synthefy.com/
---
