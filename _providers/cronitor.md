---
access_model:
  confidence: high
  label: Paid (free trial) · Self-serve signup
  onboarding: self-serve
  pricing: paid
  public: false
  source:
  - plans
  - authentication
  trial: true
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
- acting_count: 12
  human_in_the_loop: 0
  name: Cronitor Agentic Access
  operation_count: 24
  slug: cronitor-agentic-access
  summary_line: 24 operations · 12 acting
api_count: 6
apis:
- description: The Monitors API allows creating, updating, retrieving, deleting, cloning, and pausing monitors for cron jobs, heartbeats, uptime checks, and sites. Monitors are configured with schedules, assertions,
  name: Cronitor Monitors API
  slug: monitors-api
- description: The Cronitor Telemetry API API from Cronitor — 1 operation(s) for cronitor telemetry api.
  name: Cronitor Cronitor Telemetry API API
  slug: cronitor-cronitor-telemetry-api-api
- description: The Groups API from Cronitor — 3 operation(s) for groups.
  name: Cronitor Groups API
  slug: cronitor-groups-api
- description: The Notifications API from Cronitor — 2 operation(s) for notifications.
  name: Cronitor Notifications API
  slug: cronitor-notifications-api
- description: The P API from Cronitor — 1 operation(s) for p.
  name: Cronitor P API
  slug: cronitor-p-api
- description: The Search API from Cronitor — 1 operation(s) for search.
  name: Cronitor Search API
  slug: cronitor-search-api
artifact_total: 20
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/cronitor-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/cronitor-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/cronitor-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://cronitor.io
- group: docs
  title: ''
  type: Documentation
  url: https://cronitor.io/docs
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/cronitorio
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/cronitor
- group: company
  title: ''
  type: Blog
  url: https://cronitor.io/cronicle
- group: commercial
  title: ''
  type: Pricing
  url: https://cronitor.io/pricing
- group: operate
  title: ''
  type: StatusPage
  url: https://status.cronitor.io
- group: other
  title: ''
  type: X
  url: https://x.com/cronitorio
- group: commercial
  title: ''
  type: Plans
  url: plans/cronitor-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/cronitor-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/cronitor-finops.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/cronitor-vocabulary.yml
- group: design
  title: ''
  type: JSONLDContext
  url: json-ld/cronitor-context.jsonld
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/cronitor-monitor-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/cronitor-telemetry-event-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/cronitor-notification-list-schema.json
- group: company
  title: ''
  type: Blog
  url: blogs/blogs.json
created: '2026-06-12'
description: Cronitor is a cron job and scheduled task monitoring platform that provides developers with instant alerts when jobs fail, run too long, or don't run at all. The platform offers a REST API for creating and managing monitors, recording job telemetry events, and configuring alert policies across teams. Cronitor supports job monitoring, heartbeat monitoring, website uptime checks, and Real User Monitoring (RUM), all accessible via a versioned HTTP API using Basic Auth with scoped API keys. SDKs are available for Python, Node.js, Ruby, PHP, Java, Go, and other languages through the cronitorio GitHub organization.
examples:
- key_count: 3
  name: Cronitor Create Monitor Example
  slug: cronitor-create-monitor-example
- key_count: 3
  name: Cronitor List Monitors Example
  slug: cronitor-list-monitors-example
- key_count: 2
  name: Cronitor Telemetry Event Example
  slug: cronitor-telemetry-event-example
finops:
- name: Cronitor Finops
  service_category: Developer Tools
  slug: cronitor-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/cronitor.png
json_schemas:
- name: Cronitor Monitor
  property_count: 26
  slug: cronitor-monitor
- name: Cronitor Notification List
  property_count: 8
  slug: cronitor-notification-list
- name: Cronitor Telemetry Event
  property_count: 7
  slug: cronitor-telemetry-event
jsonld:
- class_count: 6
  name: Cronitor Context
  property_count: 38
  slug: cronitor-context
layout: provider
modified: '2026-06-12'
name: Cronitor
nav: Providers
network: true
overview: 'Cronitor publishes 6 APIs on the [APIs.io](https://apis.io/) network, including Monitors API, Cronitor Telemetry API API, Groups API, and 3 more. Tagged areas include Monitoring, Cron Jobs, Scheduled Tasks, Alerting, and Uptime.


  The Cronitor catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Cronitor''s developer surface includes authentication, documentation, engineering blog, pricing, and 16 more developer resources.'
plans:
- name: Cronitor Plans Pricing
  plan_count: 3
  slug: cronitor-plans-pricing
random_paper: 13
rate_limits:
- limit_count: 5
  name: Cronitor Rate Limits
  slug: cronitor-rate-limits
rules:
- name: Cronitor API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: cronitor-jsonschema-spectral-rules
score:
  band: developing
  composite: 59.4
  delta: 0.0
  facets:
    commercial_clarity: 50.0
    contract_quality: 71.1
    developer_ergonomics: 21.7
    discoverability: 100.0
    governance: 86.8
    operational_transparency: 52.6
  previous_composite: 59.4
  schema_version: 0.5
  scored_at: '2026-07-23'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/cronitor/refs/heads/main/screenshots/cronitor-2026-06-20T175236.png
security:
- kind: authentication
  name: Cronitor Authentication
  slug: cronitor-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Cronitor Domain Security
  slug: cronitor-domain-security
  summary_line: TLSv1.2 · DMARC
slug: cronitor
tags:
- Monitoring
- Cron Jobs
- Scheduled Tasks
- Alerting
- Uptime
- Telemetry
- Status Pages
website: https://cronitor.io
---
