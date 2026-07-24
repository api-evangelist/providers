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
  band: agent-ready
  dimensions:
    agent_skills: false
    agentic_access: true
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: true
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.1
  score: 48.1
  scored_at: '2026-07-23'
agentic_access:
- acting_count: 1
  human_in_the_loop: 0
  name: Pixie Agentic Access
  operation_count: 4
  slug: pixie-agentic-access
  summary_line: 4 operations · 1 acting
api_count: 5
apis:
- description: Python-dialect domain-specific language and API for querying and analyzing telemetry data collected by Pixie within a Kubernetes cluster. PxL scripts allow developers to filter, aggregate, and visuali
  name: Pixie PxL Script API
  slug: pixie-pxl-api
- description: Plugin API that allows configuring PxL scripts to export observability data from Pixie at regularly scheduled intervals to external systems. Supports integrations including a Grafana datasource plugin
  name: Pixie Plugin System API
  slug: pixie-plugin-api
- description: Operations for listing and inspecting Pixie-instrumented Kubernetes clusters connected to the Pixie Cloud.
  name: Pixie Clusters API
  slug: pixie-clusters-api
- description: Health and status endpoints for the Pixie service.
  name: Pixie Health API
  slug: pixie-health-api
- description: Operations for executing PxL scripts against a cluster and retrieving telemetry query results.
  name: Pixie Scripts API
  slug: pixie-scripts-api
artifact_total: 16
collections:
- collection_type: open
  name: Pixie API
  slug: open-pixie
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/pixie-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/pixie-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/pixie-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/pixieai
- group: company
  title: ''
  type: Website
  url: https://px.dev/
- group: design
  title: ''
  type: JSONLD
  url: json-ld/pixie-context.jsonld
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/pixie-pxl-script-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/pixie-plugin-schema.json
- group: docs
  title: ''
  type: Documentation
  url: https://docs.px.dev/
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.px.dev/installing-pixie/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/pixie-io
- group: build
  title: ''
  type: GitHubRepository
  url: https://github.com/pixie-io/pixie
- group: company
  title: ''
  type: Blog
  url: https://blog.px.dev/
- group: operate
  title: ''
  type: Community
  url: https://px.dev/community/
- group: operate
  title: ''
  type: Slack
  url: https://slackin.px.dev/
created: '2026-03-16'
description: Pixie is a Kubernetes observability platform that uses eBPF to automatically collect telemetry data including full-body application requests, resource and network metrics, and application profiles without manual instrumentation.
finops:
- name: Pixie Finops
  service_category: Observability
  slug: pixie-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/pixie.png
json_schemas:
- name: Pixie Plugin Configuration
  property_count: 7
  slug: pixie-plugin
- name: Pixie PxL Script
  property_count: 10
  slug: pixie-pxl-script
jsonld:
- class_count: 0
  name: Pixie Context
  property_count: 7
  slug: pixie-context
layout: provider
modified: '2026-05-19'
name: Pixie
nav: Providers
network: true
overview: 'Pixie publishes 3 APIs on the [APIs.io](https://apis.io/) network: Clusters API, Health API, and Scripts API. Tagged areas include eBPF, Kubernetes, Monitoring, and Observability.


  The Pixie catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Pixie''s developer surface includes authentication, documentation, getting-started guide, engineering blog, and 11 more developer resources.'
plans:
- name: Pixie Plans Pricing
  plan_count: 1
  slug: pixie-plans-pricing
random_paper: 33
rate_limits:
- limit_count: 2
  name: Pixie Rate Limits
  slug: pixie-rate-limits
rules:
- name: Pixie API Rules
  rule_count: 6
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 4
  slug: pixie-jsonschema-spectral-rules
score:
  band: developing
  composite: 47.1
  delta: 0.0
  facets:
    commercial_clarity: 28.9
    contract_quality: 64.6
    developer_ergonomics: 37.0
    discoverability: 55.0
    governance: 73.7
    operational_transparency: 26.3
  previous_composite: 47.1
  schema_version: 0.5
  scored_at: '2026-07-23'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/pixie/refs/heads/main/screenshots/pixie-2026-06-20T191740.png
security:
- kind: authentication
  name: Pixie Authentication
  slug: pixie-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Pixie Domain Security
  slug: pixie-domain-security
  summary_line: TLSv1.3 · HSTS
slug: pixie
tags:
- eBPF
- Kubernetes
- Monitoring
- Observability
website: https://px.dev/
---
