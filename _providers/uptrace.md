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
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 23.2
  scored_at: '2026-09-01'
agentic_access:
- acting_count: 11
  human_in_the_loop: 0
  name: Uptrace Agentic Access
  operation_count: 19
  slug: uptrace-agentic-access
  summary_line: 19 operations · 11 acting
api_count: 1
apis:
- description: Alert rule management and notifications
  name: Uptrace Alerts API
  slug: uptrace-alerts-api
- description: Chart annotation management
  name: Uptrace Annotations API
  slug: uptrace-annotations-api
- description: Dashboard management
  name: Uptrace Dashboards API
  slug: uptrace-dashboards-api
- description: Prometheus metrics ingestion and querying
  name: Uptrace Metrics API
  slug: uptrace-metrics-api
- description: Project and DSN management
  name: Uptrace Projects API
  slug: uptrace-projects-api
artifact_total: 27
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Uptrace Alerts API
  slug: open-uptrace-alerts-api
- collection_type: open
  name: Uptrace Alerts Annotations API
  slug: open-uptrace-annotations-api
- collection_type: open
  name: Uptrace Alerts Dashboards API
  slug: open-uptrace-dashboards-api
- collection_type: open
  name: Uptrace Alerts Metrics API
  slug: open-uptrace-metrics-api
- collection_type: open
  name: Uptrace Alerts Projects API
  slug: open-uptrace-projects-api
- collection_type: open
  name: Uptrace API
  slug: open-uptrace
common:
- group: operate
  title: ''
  type: IssueTracker
  url: https://github.com/uptrace/uptrace/issues
- group: operate
  title: ''
  type: Releases
  url: https://github.com/uptrace/uptrace/releases
- group: docs
  title: ''
  type: ContributionGuide
  url: https://github.com/uptrace/uptrace/blob/master/CONTRIBUTING.md
- group: commercial
  title: ''
  type: License
  url: https://github.com/uptrace/uptrace/blob/master/LICENSE
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/uptrace-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/uptrace-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/uptrace-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/uptracedev
- group: company
  title: ''
  type: Website
  url: https://uptrace.dev
- group: docs
  title: ''
  type: Documentation
  url: https://uptrace.dev/get/get-started.html
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/uptrace/uptrace
- group: other
  title: ''
  type: Docker Hub
  url: https://hub.docker.com/r/uptrace/uptrace
- group: agent
  title: ''
  type: MCPServer
  url: https://github.com/uptrace/mcp
- group: agent
  title: ''
  type: LlmsText
  url: https://uptrace.dev/llms.txt
created: '2026-03-25'
description: Uptrace is an open source APM and distributed tracing platform powered by OpenTelemetry for monitoring application traces, metrics, and logs. The Uptrace API provides programmatic access to annotations, Prometheus metrics ingestion, PromQL querying, alert rules, project management, and dashboards.
examples:
- key_count: 2
  name: Uptrace Create Alert Example
  slug: uptrace-create-alert-example
- key_count: 2
  name: Uptrace Create Annotation Example
  slug: uptrace-create-annotation-example
finops:
- name: Uptrace Finops
  service_category: API
  slug: uptrace-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/uptrace.png
json_schemas:
- name: Uptrace Alert
  property_count: 11
  slug: uptrace-alert
- name: Uptrace Annotation
  property_count: 9
  slug: uptrace-annotation
json_structures:
- name: Uptrace Annotation Structure
  property_count: 0
  slug: uptrace-annotation-structure
jsonld:
- class_count: 5
  name: Uptrace Context
  property_count: 19
  slug: uptrace-context
layout: provider
mcp_servers:
- description: ''
  name: MCP Server
  slug: mcp-server
modified: '2026-05-19'
name: Uptrace
nav: Providers
network: true
overview: 'Uptrace publishes 5 APIs on the [APIs.io](https://apis.io/) network, including Alerts API, Annotations API, Dashboards API, and 2 more. Tagged areas include APM, Observability, OpenTelemetry, Distributed Tracing, and Monitoring.


  The Uptrace catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Uptrace''s developer surface includes authentication, documentation, and 12 more developer resources.'
plans:
- name: Uptrace Plans Pricing
  plan_count: 3
  slug: uptrace-plans-pricing
random_paper: 0
rate_limits:
- limit_count: 5
  name: Uptrace Rate Limits
  slug: uptrace-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: Uptrace API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: uptrace-jsonschema-spectral-rules
- effective_rule_count: 48
  extends:
  - spectral:oas
  name: Uptrace API Rules
  rule_count: 7
  severity_counts:
    error: 0
    hint: 0
    info: 3
    warn: 4
  slug: uptrace-rules
score:
  band: thin
  composite: 37.6
  coverage:
    artifact_dirs: 16
    catalog_gap: 53.5
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 15.8
    commercial_clarity: 15.8
    contract_governance: 13.6
    contract_quality: 64.6
    developer_ergonomics: 21.4
    discoverability: 75.9
    governance: 13.6
    operational_transparency: 26.3
  open_source:
    applies: true
    score: 50.0
  previous_composite: 37.6
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 5
  schema_version: 0.18.0
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/uptrace/refs/heads/main/screenshots/uptrace-2026-06-20T200501.png
security:
- kind: authentication
  name: Uptrace Authentication
  slug: uptrace-authentication
  summary_line: apiKey/http · 2 schemes
- kind: domain-security
  name: Uptrace Domain Security
  slug: uptrace-domain-security
  summary_line: TLSv1.3 · DMARC
slug: uptrace
tags:
- APM
- Observability
- OpenTelemetry
- Distributed Tracing
- Monitoring
website: https://uptrace.dev
---
