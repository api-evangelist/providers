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
- acting_count: 1
  human_in_the_loop: 0
  name: Readme Metrics Agentic Access
  operation_count: 5
  slug: readme-metrics-agentic-access
  summary_line: 5 operations · 1 acting
api_count: 5
apis:
- description: ReadMe Metrics captures and analyzes API request and response data to provide usage analytics, error tracking, and developer activity insights. It helps API providers understand how their APIs are bei
  name: ReadMe Metrics
  slug: readme-metrics
- description: The Api Registry API from ReadMe Metrics — 1 operation(s) for api registry.
  name: ReadMe Metrics Api Registry API
  slug: readme-metrics-api-registry-api
- description: The Api Specification API from ReadMe Metrics — 1 operation(s) for api specification.
  name: ReadMe Metrics Api Specification API
  slug: readme-metrics-api-specification-api
- description: The Changelogs API from ReadMe Metrics — 1 operation(s) for changelogs.
  name: ReadMe Metrics Changelogs API
  slug: readme-metrics-changelogs-api
- description: The Docs API from ReadMe Metrics — 1 operation(s) for docs.
  name: ReadMe Metrics Docs API
  slug: readme-metrics-docs-api
artifact_total: 17
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: ReadMe Api Registry API
  slug: open-readme-metrics-api-registry-api
- collection_type: open
  name: ReadMe Api Registry Api Specification API
  slug: open-readme-metrics-api-specification-api
- collection_type: open
  name: ReadMe Api Registry Changelogs API
  slug: open-readme-metrics-changelogs-api
- collection_type: open
  name: ReadMe Api Registry Docs API
  slug: open-readme-metrics-docs-api
- collection_type: open
  name: ReadMe API
  slug: open-readme-metrics
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/readme-metrics-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/readme-metrics-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/readme-metrics-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/readme
- group: company
  title: ''
  type: Website
  url: https://readme.com
- group: docs
  title: ''
  type: Documentation
  url: https://docs.readme.com
- group: company
  title: ''
  type: Blog
  url: https://readme.com/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://readme.com/pricing
- group: start
  title: ''
  type: Login
  url: https://dash.readme.com/login
- group: start
  title: ''
  type: Signup
  url: https://dash.readme.com/signup
- group: operate
  title: ''
  type: Support
  url: https://docs.readme.com/main/docs/support
- group: build
  title: ''
  type: GitHub
  url: https://github.com/readmeio
- group: company
  title: ''
  type: Twitter
  url: https://twitter.com/readme
- group: operate
  title: ''
  type: ChangeLog
  url: https://docs.readme.com/main/changelog
- group: build
  title: ''
  type: SDKs
  url: https://docs.readme.com/main/docs/metrics-sdks
- group: agent
  title: ''
  type: LlmsText
  url: https://docs.readme.com/llms.txt
created: '2026-03-26'
description: ReadMe is an API documentation and developer hub platform that helps companies build interactive API documentation, track API usage analytics, and improve developer experience. ReadMe Metrics captures and analyzes API request logs to provide insights into how developers are using your APIs.
finops:
- name: Readme Metrics Finops
  service_category: API
  slug: readme-metrics-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/readme-metrics.png
layout: provider
modified: '2026-04-28'
name: ReadMe Metrics
nav: Providers
network: true
overview: 'ReadMe Metrics publishes 4 APIs on the [APIs.io](https://apis.io/) network, including Api Registry API, Api Specification API, Changelogs API, and 1 more. Tagged areas include API Analytics, API Documentation, API Logs, API Metrics, and API Usage.


  ReadMe Metrics'' developer surface includes authentication, documentation, engineering blog, pricing, signup flow, support, GitHub presence, and 9 more developer resources.'
plans:
- name: Readme Metrics Plans Pricing
  plan_count: 3
  slug: readme-metrics-plans-pricing
random_paper: 85
rate_limits:
- limit_count: 5
  name: Readme Metrics Rate Limits
  slug: readme-metrics-rate-limits
score:
  band: thin
  composite: 39.8
  delta: 0.0
  facets:
    commercial_clarity: 39.5
    contract_quality: 57.5
    developer_ergonomics: 32.6
    discoverability: 72.2
    governance: 0.0
    operational_transparency: 28.9
  previous_composite: 39.8
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 4
  schema_version: 0.11.0
  scored_at: '2026-08-17'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/readme-metrics/refs/heads/main/screenshots/readme-metrics-2026-06-20T192740.png
security:
- kind: authentication
  name: Readme Metrics Authentication
  slug: readme-metrics-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Readme Metrics Domain Security
  slug: readme-metrics-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: readme-metrics
tags:
- API Analytics
- API Documentation
- API Logs
- API Metrics
- API Usage
- Developer Experience
- Developer Hubs
website: https://readme.com
---
