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
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: partial
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 33.8
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 134
  human_in_the_loop: 7
  name: Openobserve Agentic Access
  operation_count: 219
  slug: openobserve-agentic-access
  summary_line: 219 operations · 134 acting · 7 human-in-the-loop
api_count: 33
apis:
- description: The Actions API from OpenObserve — 5 operation(s) for actions.
  name: OpenObserve Actions API
  slug: openobserve-actions-api
- description: Alerts retrieval & management operations
  name: OpenObserve Alerts API
  slug: openobserve-alerts-api
- description: Super cluster operations
  name: OpenObserve Clusters API
  slug: openobserve-clusters-api
- description: Dashboard operations
  name: OpenObserve Dashboards API
  slug: openobserve-dashboards-api
- description: The Folders API from OpenObserve — 6 operation(s) for folders.
  name: OpenObserve Folders API
  slug: openobserve-folders-api
- description: Functions retrieval & management operations
  name: OpenObserve Functions API
  slug: openobserve-functions-api
- description: The Groups API from OpenObserve — 2 operation(s) for groups.
  name: OpenObserve Groups API
  slug: openobserve-groups-api
- description: Alert incident correlation & management operations
  name: OpenObserve Incidents API
  slug: openobserve-incidents-api
- description: The Key API from OpenObserve — 2 operation(s) for key.
  name: OpenObserve Key API
  slug: openobserve-key-api
- description: The Keys API from OpenObserve — 1 operation(s) for keys.
  name: OpenObserve Keys API
  slug: openobserve-keys-api
- description: Key Value retrieval & management operations
  name: OpenObserve KV API
  slug: openobserve-kv-api
- description: Logs data ingestion operations
  name: OpenObserve Logs API
  slug: openobserve-logs-api
- description: The MCP API from OpenObserve — 2 operation(s) for mcp.
  name: OpenObserve MCP API
  slug: openobserve-mcp-api
- description: Meta details about the OpenObserve state itself. e.g. healthz
  name: OpenObserve Meta API
  slug: openobserve-meta-api
- description: Metrics data ingestion operations
  name: OpenObserve Metrics API
  slug: openobserve-metrics-api
- description: Organizations retrieval & management operations
  name: OpenObserve Organizations API
  slug: openobserve-organizations-api
- description: Log pattern extraction operations (enterprise)
  name: OpenObserve Patterns API
  slug: openobserve-patterns-api
- description: The Pipelines API from OpenObserve — 10 operation(s) for pipelines.
  name: OpenObserve Pipelines API
  slug: openobserve-pipelines-api
- description: Ratelimit operations
  name: OpenObserve Ratelimit API
  slug: openobserve-ratelimit-api
- description: The Report API from OpenObserve — 1 operation(s) for report.
  name: OpenObserve Report API
  slug: openobserve-report-api
- description: The Reports API from OpenObserve — 9 operation(s) for reports.
  name: OpenObserve Reports API
  slug: openobserve-reports-api
- description: The Roles API from OpenObserve — 4 operation(s) for roles.
  name: OpenObserve Roles API
  slug: openobserve-roles-api
- description: The Rum API from OpenObserve — 3 operation(s) for rum.
  name: OpenObserve Rum API
  slug: openobserve-rum-api
- description: Collection of saved search views for easy retrieval
  name: OpenObserve Saved Views API
  slug: openobserve-saved-views-api
- description: Search/Query operations
  name: OpenObserve Search API
  slug: openobserve-search-api
- description: The Search Jobs API from OpenObserve — 5 operation(s) for search jobs.
  name: OpenObserve Search Jobs API
  slug: openobserve-search-jobs-api
- description: Multi-signal correlation across logs, traces, and metrics (enterprise)
  name: OpenObserve Service Streams API
  slug: openobserve-service-streams-api
- description: The ServiceAccounts API from OpenObserve — 2 operation(s) for serviceaccounts.
  name: OpenObserve ServiceAccounts API
  slug: openobserve-serviceaccounts-api
- description: Short Url Service
  name: OpenObserve Short Url API
  slug: openobserve-short-url-api
- description: Stream retrieval & management operations
  name: OpenObserve Streams API
  slug: openobserve-streams-api
- description: The Templates API from OpenObserve — 3 operation(s) for templates.
  name: OpenObserve Templates API
  slug: openobserve-templates-api
- description: Traces data ingestion operations
  name: OpenObserve Traces API
  slug: openobserve-traces-api
- description: Users retrieval & management operations
  name: OpenObserve Users API
  slug: openobserve-users-api
artifact_total: 41
collections:
- collection_type: open
  name: openobserve
  slug: open-openobserve
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/openobserve-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/openobserve-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/openobserve-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/openobserve-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/openobserve
- group: company
  title: ''
  type: Website
  url: https://openobserve.ai
- group: docs
  title: ''
  type: Documentation
  url: https://openobserve.ai/docs/
- group: build
  title: ''
  type: GitHubOrg
  url: https://github.com/openobserve
- group: agent
  title: ''
  type: LlmsText
  url: https://openobserve.ai/llms.txt
- group: company
  title: ''
  type: Blog
  url: https://openobserve.ai/blog/
created: '2026-03-25'
description: OpenObserve is an open source petabyte-scale observability platform with unified logs, metrics, traces, and front-end telemetry in a single UI with SQL and PromQL querying. The HTTP API exposes ingestion, search, alerting, dashboards, pipelines, RUM, and administration endpoints.
finops:
- name: Openobserve Finops
  service_category: API
  slug: openobserve-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/openobserve.png
layout: provider
modified: '2026-05-19'
name: OpenObserve
nav: Providers
network: true
overview: 'OpenObserve publishes 33 APIs on the [APIs.io](https://apis.io/) network, including Actions API, Alerts API, Clusters API, and 30 more. Tagged areas include Observability, Logs, Metrics, Traces, and RUM.


  OpenObserve''s developer surface includes authentication, documentation, engineering blog, and 7 more developer resources.'
plans:
- name: Openobserve Plans Pricing
  plan_count: 3
  slug: openobserve-plans-pricing
random_paper: 7
rate_limits:
- limit_count: 5
  name: Openobserve Rate Limits
  slug: openobserve-rate-limits
score:
  band: thin
  composite: 39.4
  delta: -3.3
  facets:
    commercial_clarity: 47.4
    contract_quality: 53.6
    developer_ergonomics: 21.7
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 36.8
  previous_composite: 42.7
  provenance:
    agentic_access: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 33
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/openobserve/refs/heads/main/screenshots/openobserve-2026-06-20T191019.png
security:
- kind: authentication
  name: Openobserve Authentication
  slug: openobserve-authentication
  summary_line: apiKey/http · 2 schemes
- kind: domain-security
  name: Openobserve Domain Security
  slug: openobserve-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: trust-center
  name: Openobserve Trust Center
  slug: openobserve-trust-center
  summary_line: SOC 2, ISO 27001
slug: openobserve
tags:
- Observability
- Logs
- Metrics
- Traces
- RUM
- Open Source
website: https://openobserve.ai
---
