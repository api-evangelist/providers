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
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: documented
    idempotency: false
    mcp_server: derived
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 32.7
  scored_at: '2026-07-28'
api_count: 3
apis:
- description: Create, retrieve, revise, and delete metric alarms.
  name: Pepperdata Alarms API
  slug: pepperdata-alarms-api
- description: Query application/job details, counters, and tuning recommendations.
  name: Pepperdata Job Details API
  slug: pepperdata-job-details-api
- description: Retrieve time-series metrics, series, and filters.
  name: Pepperdata Metrics API
  slug: pepperdata-metrics-api
artifact_total: 6
common:
- group: auth
  title: ''
  type: Authentication
  url: authentication/pepperdata-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/pepperdata-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/pepperdata-problem-types.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/pepperdata-conformance.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/pepperdata-data-model.yml
- group: build
  title: ''
  type: Packages
  url: packages/pepperdata-packages.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/pepperdata-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/pepperdata-llms.txt
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/pepperdata-domain-security.yml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.pepperdata.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.pepperdata.com/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.pepperdata.com/rest-api/
- group: company
  title: ''
  type: Blog
  url: https://www.pepperdata.com/blog/
- group: operate
  title: ''
  type: Support
  url: https://support.pepperdata.com/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.pepperdata.com/pricing/
- group: start
  title: ''
  type: SignUp
  url: https://www.pepperdata.com/request-a-demo/
- group: start
  title: ''
  type: Login
  url: https://dashboard.pepperdata.com/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.pepperdata.com/legal/privacy-policy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.pepperdata.com/legal/privacy-policy#terms
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/pepperdata
- group: company
  title: ''
  type: Website
  url: https://www.pepperdata.com/
created: '2026-07-17'
description: 'Pepperdata provides dynamic Kubernetes resource optimization and observability for data-intensive workloads, increasing cluster utilization, improving performance, and reducing cost in real time across Spark, MapReduce, Tez, and Kubernetes environments. Its REST API gives programmatic access to the same observability data available in the Pepperdata dashboard: time-series metrics with series breakdowns and filters (/m), application and job details including counters and cost/performance tuning recommendations (/jobdetails), and full CRUD over metric alarms (/alarms). Authentication uses a custom API-key header. Pepperdata is a portfolio company of Wing Venture Capital.'
image: https://www.pepperdata.com/wp-content/uploads/2025/03/normal-logo-1200px.png
layout: provider
mcp_servers:
- description: ''
  name: pepperdata-mcp.yml
  slug: pepperdata-mcpyml
modified: '2026-07-20'
name: Pepperdata
nav: Providers
network: true
overview: 'Pepperdata publishes 3 APIs on the [APIs.io](https://apis.io/) network: Alarms API, Job Details API, and Metrics API. Tagged areas include Company, Observability, Monitoring, Kubernetes, and Big Data.


  Pepperdata''s developer surface includes authentication, documentation, API reference, engineering blog, support, pricing, signup flow, and 15 more developer resources.'
random_paper: 35
score:
  band: developing
  composite: 43.2
  delta: -2.3
  facets:
    commercial_clarity: 44.7
    contract_quality: 60.2
    developer_ergonomics: 45.1
    discoverability: 81.5
    governance: 11.5
    operational_transparency: 5.3
  previous_composite: 45.5
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 3
    mcp: derived
    skills: derived
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
security:
- kind: authentication
  name: Pepperdata Authentication
  slug: pepperdata-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Pepperdata Domain Security
  slug: pepperdata-domain-security
  summary_line: TLSv1.2 · HSTS · DMARC
slug: pepperdata
tags:
- Company
- Observability
- Monitoring
- Kubernetes
- Big Data
- Cost Optimization
- Metrics
- APM
website: https://www.pepperdata.com/
---
