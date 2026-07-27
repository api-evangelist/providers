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
  band: agent-native
  dimensions:
    agent_skills: true
    agentic_access: false
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    error_semantics: true
    idempotency: false
    mcp_server: true
    openapi_examples: false
    rate_limit_signal: true
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.1
  score: 61.5
  scored_at: '2026-07-27'
api_count: 18
apis:
- description: custom-columns operations
  name: ComboCurve v1 custom-columns API
  slug: combocurve-v1-custom-columns-api
- description: daily-productions operations
  name: ComboCurve v1 daily-productions API
  slug: combocurve-v1-daily-productions-api
- description: directional-surveys operations
  name: ComboCurve v1 directional-surveys API
  slug: combocurve-v1-directional-surveys-api
- description: econ-models operations
  name: ComboCurve v1 econ-models API
  slug: combocurve-v1-econ-models-api
- description: econ-runs operations
  name: ComboCurve v1 econ-runs API
  slug: combocurve-v1-econ-runs-api
- description: exports operations
  name: ComboCurve v1 exports API
  slug: combocurve-v1-exports-api
- description: forecast-configurations operations
  name: ComboCurve v1 forecast-configurations API
  slug: combocurve-v1-forecast-configurations-api
- description: forecast-daily-volumes operations
  name: ComboCurve v1 forecast-daily-volumes API
  slug: combocurve-v1-forecast-daily-volumes-api
- description: forecast-monthly-volumes operations
  name: ComboCurve v1 forecast-monthly-volumes API
  slug: combocurve-v1-forecast-monthly-volumes-api
- description: monthly-productions operations
  name: ComboCurve v1 monthly-productions API
  slug: combocurve-v1-monthly-productions-api
- description: ownership-qualifiers operations
  name: ComboCurve v1 ownership-qualifiers API
  slug: combocurve-v1-ownership-qualifiers-api
- description: projects operations
  name: ComboCurve v1 projects API
  slug: combocurve-v1-projects-api
- description: tags operations
  name: ComboCurve v1 tags API
  slug: combocurve-v1-tags-api
- description: users operations
  name: ComboCurve v1 users API
  slug: combocurve-v1-users-api
- description: well-comments operations
  name: ComboCurve v1 well-comments API
  slug: combocurve-v1-well-comments-api
- description: wells operations
  name: ComboCurve v1 wells API
  slug: combocurve-v1-wells-api
- description: wells-identifiers operations
  name: ComboCurve v1 wells-identifiers API
  slug: combocurve-v1-wells-identifiers-api
- description: exports operations
  name: ComboCurve v2 exports API
  slug: combocurve-v2-exports-api
artifact_total: 21
common:
- group: company
  title: ''
  type: Website
  url: https://combocurve.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.api.combocurve.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.api.combocurve.com/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.api.combocurve.com/api/getting-started
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.api.combocurve.com/api/getting-started
- group: operate
  title: ''
  type: RateLimits
  url: https://docs.api.combocurve.com/api/getting-started
- group: operate
  title: ''
  type: Support
  url: https://forum.api.combocurve.com/
- group: company
  title: ''
  type: Blog
  url: https://combocurve.com/blog/
- group: start
  title: ''
  type: Login
  url: https://app.combocurve.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://combocurve.com/terms-of-service/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://combocurve.com/privacy-policy/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.combocurve.com/
- group: build
  title: ''
  type: Postman
  url: https://docs.api.combocurve.com/downloads/combocurve-api.postman_collection.json
- group: auth
  title: ''
  type: Authentication
  url: authentication/combocurve-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/combocurve-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/combocurve-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/combocurve-lifecycle.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/combocurve-data-model.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/combocurve-conformance.yml
- group: build
  title: ''
  type: Packages
  url: packages/combocurve-packages.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/combocurve-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/combocurve-llms.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/combocurve-well-known.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/combocurve-domain-security.yml
created: '2026-07-17'
description: ComboCurve is an oil & gas well forecasting, type-curve, reserves and economics platform used by petroleum engineers, operators, private equity firms, investment banks, and mineral/royalty companies for acquisition-and-divestiture (A&D), upstream asset management, and reserves analysis. Its public REST API at https://api.combocurve.com exposes well headers, daily and monthly production data, directional surveys, forecasts, forecast configurations, econ-models (capex, expenses, differentials, escalations, depreciation, ownership reversions), economics runs, and asynchronous export jobs. Backed by Bessemer Venture Partners.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/combocurve.png
layout: provider
mcp_servers:
- description: ''
  name: combocurve-mcp.yml
  slug: combocurve-mcpyml
modified: '2026-07-18'
name: ComboCurve
nav: Providers
network: true
overview: 'ComboCurve publishes 18 APIs on the [APIs.io](https://apis.io/) network, including v1 custom-columns API, v1 daily-productions API, v1 directional-surveys API, and 15 more. Tagged areas include Company, Vertical Software, Oil and Gas, Energy, and Forecasting.


  ComboCurve''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, authentication, and 19 more developer resources.'
random_paper: 57
score:
  band: developing
  composite: 47.8
  delta: 0.0
  facets:
    commercial_clarity: 34.2
    contract_quality: 58.3
    developer_ergonomics: 71.7
    discoverability: 100.0
    governance: 0.0
    operational_transparency: 15.8
  previous_composite: 47.8
  schema_version: 0.5
  scored_at: '2026-07-27'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/combocurve/refs/heads/main/screenshots/combocurve-2026-07-25T210107.png
security:
- kind: authentication
  name: Combocurve Authentication
  slug: combocurve-authentication
  summary_line: apiKey/http · 2 schemes
- kind: domain-security
  name: Combocurve Domain Security
  slug: combocurve-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: combocurve
tags:
- Company
- Vertical Software
- Oil and Gas
- Energy
- Forecasting
- Reserves
- Economics
- Upstream
- Petroleum Engineering
website: https://combocurve.com/
---
