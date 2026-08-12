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
    openapi_examples: partial
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 33.8
  scored_at: '2026-08-11'
agentic_access:
- acting_count: 21
  human_in_the_loop: 5
  name: Qstash Agentic Access
  operation_count: 31
  slug: qstash-agentic-access
  summary_line: 31 operations · 21 acting · 5 human-in-the-loop
api_count: 7
apis:
- description: Manage dead letter queue messages
  name: QStash Dead Letter Queue API
  slug: qstash-dead-letter-queue-api
- description: Manage flow control keys for rate and parallelism limiting
  name: QStash Flow Control API
  slug: qstash-flow-control-api
- description: Retrieve message delivery logs
  name: QStash Logs API
  slug: qstash-logs-api
- description: Publish and manage messages
  name: QStash Messages API
  slug: qstash-messages-api
- description: Manage FIFO queues
  name: QStash Queues API
  slug: qstash-queues-api
- description: Create and manage CRON-based scheduled messages
  name: QStash Schedules API
  slug: qstash-schedules-api
- description: Manage URL groups for fan-out delivery
  name: QStash URL Groups API
  slug: qstash-url-groups-api
artifact_total: 20
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/qstash-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/qstash-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/qstash-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://upstash.com/qstash
- group: docs
  title: ''
  type: Documentation
  url: https://upstash.com/docs/qstash/overall/getstarted
- group: build
  title: ''
  type: GitHubOrg
  url: https://github.com/upstash
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/upstash
- group: company
  title: ''
  type: Blog
  url: https://upstash.com/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://upstash.com/pricing/qstash
- group: operate
  title: ''
  type: StatusPage
  url: https://status.upstash.com/
- group: other
  title: ''
  type: X
  url: https://x.com/upstash
- group: commercial
  title: ''
  type: Plans
  url: plans/qstash-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/qstash-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/qstash-finops.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/qstash-vocabulary.yml
- group: design
  title: ''
  type: JSONLDContext
  url: json-ld/qstash-context.jsonld
created: '2026-06-12'
description: QStash is a serverless message queue and task scheduling REST API from Upstash that delivers HTTP messages to endpoints reliably without requiring any long-lived connections or infrastructure management. Built entirely on stateless HTTP requests, it is designed for serverless and edge runtimes where traditional message brokers are impractical. QStash supports automatic retries, CRON-based scheduling up to one year in advance, URL group broadcasting for fan-out delivery, FIFO queuing, dead-letter queues, and message deduplication. Developers simply POST a message with a destination URL and QStash handles guaranteed delivery with configurable retry logic and flow control.
examples:
- key_count: 4
  name: Batch Publish
  slug: batch-publish
- key_count: 4
  name: Create Schedule
  slug: create-schedule
- key_count: 4
  name: Publish Message
  slug: publish-message
finops:
- name: Qstash Finops
  service_category: ''
  slug: qstash-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/qstash.png
json_schemas:
- name: QStash Message
  property_count: 17
  slug: qstash-message
- name: QStash Schedule
  property_count: 8
  slug: qstash-schedule
jsonld:
- class_count: 10
  name: Qstash Context
  property_count: 31
  slug: qstash-context
layout: provider
modified: '2026-06-12'
name: QStash
nav: Providers
network: true
overview: 'QStash publishes 7 APIs on the [APIs.io](https://apis.io/) network, including Dead Letter Queue API, Flow Control API, Logs API, and 4 more. Tagged areas include Message Queue, Task Scheduling, Serverless, HTTP Messaging, and Background Jobs.


  The QStash catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  QStash''s developer surface includes authentication, documentation, engineering blog, pricing, and 12 more developer resources.'
plans:
- name: Qstash Plans Pricing
  plan_count: 5
  slug: qstash-plans-pricing
random_paper: 80
rate_limits:
- limit_count: 10
  name: Qstash Rate Limits
  slug: qstash-rate-limits
rules:
- name: QStash API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: qstash-jsonschema-spectral-rules
score:
  band: developing
  composite: 54.2
  delta: -0.7
  facets:
    commercial_clarity: 50.0
    contract_quality: 69.5
    developer_ergonomics: 21.7
    discoverability: 74.1
    governance: 68.8
    operational_transparency: 52.6
  previous_composite: 54.9
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 7
  schema_version: 0.11.0
  scored_at: '2026-08-11'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/qstash/refs/heads/main/screenshots/qstash-2026-06-20T192402.png
security:
- kind: authentication
  name: Qstash Authentication
  slug: qstash-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Qstash Domain Security
  slug: qstash-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: qstash
tags:
- Message Queue
- Task Scheduling
- Serverless
- HTTP Messaging
- Background Jobs
- Webhooks
- Dead Letter Queue
- CRON
- Upstash
website: https://upstash.com/qstash
---
