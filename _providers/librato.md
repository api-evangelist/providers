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
    agent_skills: false
    agentic_access: false
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    error_semantics: true
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.1
  score: 17.3
  scored_at: '2026-07-27'
api_count: 1
apis:
- description: RETIRED. JSON REST API for submitting and retrieving time-series measurements and for managing metrics, metric attributes, spaces, charts, dashboards, instruments, annotations, alerts, notification se
  name: Librato Metrics API
  slug: metrics-api
artifact_total: 3
common:
- group: company
  title: ''
  type: Website
  url: https://www.librato.com
- group: docs
  title: ''
  type: APIReference
  url: https://github.com/librato/api-docs
- group: docs
  title: ''
  type: Documentation
  url: https://github.com/librato/api-docs
- group: start
  title: ''
  type: GettingStarted
  url: https://github.com/librato/api-docs/blob/master/source/includes/_introduction.md
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/librato
- group: auth
  title: ''
  type: Authentication
  url: authentication/librato-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/librato-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/librato-problem-types.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/librato-data-model.yml
- group: build
  title: ''
  type: Packages
  url: packages/librato-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/librato-packages.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/librato-lifecycle.yml
- group: operate
  title: ''
  type: Deprecation
  url: https://documentation.solarwinds.com/en/success_center/observability/content/migrate-ao/ao-eol.htm
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/librato-llms.txt
- group: auth
  title: ''
  type: DomainSecurity
  url: security/librato-domain-security.yml
- group: other
  title: ''
  type: Parent Company
  url: https://www.solarwinds.com/
created: '2026-07-17'
description: 'Librato was a hosted metrics, monitoring and analytics service for operational data — time-series measurements, tagged metrics, dashboards ("spaces"), charts, annotations, alerts and notification services — delivered as a developer-first SaaS with a JSON REST API at metrics-api.librato.com/v1. Backed by Cowboy Ventures among others, the San Francisco company was acquired by SolarWinds in 2015 for a reported $40 million, and its metrics platform was folded into SolarWinds AppOptics — released in November 2017 — which has itself since reached end of life. The librato.com domain and every product subdomain (metrics., status., www.) now 301-redirect to the SolarWinds AppOptics end-of-life notice, the metrics-api.librato.com API host no longer resolves in DNS, and the github.com/librato organization was archived on 2024-01-02. This profile is retained as a historical record of a well-regarded developer API: the API reference source, the first-party Ruby, Python, Java and Node client
  libraries and the collection agents remain publicly archived and are catalogued here. The successor product is SolarWinds Observability SaaS.'
image: https://avatars.githubusercontent.com/u/146042?v=4
layout: provider
modified: '2026-07-19'
name: Librato
nav: Providers
network: true
overview: 'Librato publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Developer Tools, Monitoring, Metrics, and Observability.


  Librato''s developer surface includes API reference, documentation, getting-started guide, authentication, and 12 more developer resources.'
random_paper: 1
score:
  band: emerging
  composite: 19.7
  delta: 0.0
  facets:
    commercial_clarity: 0.0
    contract_quality: 0.0
    developer_ergonomics: 43.5
    discoverability: 92.5
    governance: 0.0
    operational_transparency: 13.2
  previous_composite: 19.7
  schema_version: 0.5
  scored_at: '2026-07-27'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/librato/refs/heads/main/screenshots/librato-2026-07-25T225027.png
security:
- kind: authentication
  name: Librato Authentication
  slug: librato-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Librato Domain Security
  slug: librato-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: librato
tags:
- Company
- Developer Tools
- Monitoring
- Metrics
- Observability
- Time Series
- Alerting
- Dashboards
- Analytics
- Retired
website: https://www.librato.com
---
