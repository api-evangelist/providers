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
    agent_card: false
    agent_skills: false
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: verified
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 38.8
  scored_at: '2026-08-24'
agentic_access:
- acting_count: 26
  human_in_the_loop: 2
  name: Trigger Dev Agentic Access
  operation_count: 44
  slug: trigger-dev-agentic-access
  summary_line: 44 operations · 26 acting · 2 human-in-the-loop
api_count: 10
apis:
- description: The Trigger.dev Realtime API streams live run state and typed stream data to backend and frontend clients. Backend SDK methods include runs.subscribeToRun, runs.subscribeToRunsWithTag, and runs.subscr
  name: Trigger.dev Realtime API
  slug: trigger-dev-realtime
- description: Create and retrieve large-scale batch runs.
  name: Trigger.dev Batches API
  slug: trigger-dev-batches-api
- description: List deployments and promote versions to production.
  name: Trigger.dev Deployments API
  slug: trigger-dev-deployments-api
- description: Create, read, update, delete, and import environment variables per project and environment.
  name: Trigger.dev Environment Variables API
  slug: trigger-dev-environment-variables-api
- description: Execute TRQL queries against runs, tasks, and metrics for dashboards and analytics.
  name: Trigger.dev Query API
  slug: trigger-dev-query-api
- description: Manage task queues including pause, resume, and concurrency overrides.
  name: Trigger.dev Queues API
  slug: trigger-dev-queues-api
- description: List, retrieve, cancel, replay, reschedule, tag, and inspect run events, results, and traces.
  name: Trigger.dev Runs API
  slug: trigger-dev-runs-api
- description: Create and manage cron schedules with IANA timezone support.
  name: Trigger.dev Schedules API
  slug: trigger-dev-schedules-api
- description: Trigger individual or batched task runs.
  name: Trigger.dev Tasks API
  slug: trigger-dev-tasks-api
- description: Create, list, retrieve, and complete waitpoint tokens for human-in-the-loop workflows.
  name: Trigger.dev Waitpoints API
  slug: trigger-dev-waitpoints-api
artifact_total: 50
collections:
- collection_type: postman
  name: Trigger.dev Management Batches API
  slug: postman-trigger-dev-batches-api
- collection_type: postman
  name: Trigger.dev Management Batches Deployments API
  slug: postman-trigger-dev-deployments-api
- collection_type: postman
  name: Trigger.dev Management Batches Environment Variables API
  slug: postman-trigger-dev-environment-variables-api
- collection_type: postman
  name: Trigger.dev Management Batches Query API
  slug: postman-trigger-dev-query-api
- collection_type: postman
  name: Trigger.dev Management Batches Queues API
  slug: postman-trigger-dev-queues-api
- collection_type: postman
  name: Trigger.dev Management Batches Runs API
  slug: postman-trigger-dev-runs-api
- collection_type: postman
  name: Trigger.dev Management Batches Schedules API
  slug: postman-trigger-dev-schedules-api
- collection_type: postman
  name: Trigger.dev Management Batches Tasks API
  slug: postman-trigger-dev-tasks-api
- collection_type: postman
  name: Trigger.dev Management Batches Waitpoints API
  slug: postman-trigger-dev-waitpoints-api
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Trigger.dev Management Batches API
  slug: open-trigger-dev-batches-api
- collection_type: open
  name: Trigger.dev Management Batches Deployments API
  slug: open-trigger-dev-deployments-api
- collection_type: open
  name: Trigger.dev Management Batches Environment Variables API
  slug: open-trigger-dev-environment-variables-api
- collection_type: open
  name: Trigger.dev Management API
  slug: open-trigger-dev-management
- collection_type: open
  name: Trigger.dev Management Batches Query API
  slug: open-trigger-dev-query-api
- collection_type: open
  name: Trigger.dev Management Batches Queues API
  slug: open-trigger-dev-queues-api
- collection_type: open
  name: Trigger.dev Management Batches Runs API
  slug: open-trigger-dev-runs-api
- collection_type: open
  name: Trigger.dev Management Batches Schedules API
  slug: open-trigger-dev-schedules-api
- collection_type: open
  name: Trigger.dev Management Batches Tasks API
  slug: open-trigger-dev-tasks-api
- collection_type: open
  name: Trigger.dev Management Batches Waitpoints API
  slug: open-trigger-dev-waitpoints-api
common:
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/triggerdev/overview
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/trigger-dev-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/trigger-dev-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/trigger-dev-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/trigger-dev-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/triggerdotdev
- group: company
  title: ''
  type: Website
  url: https://trigger.dev
- group: docs
  title: ''
  type: Documentation
  url: https://trigger.dev/docs
- group: start
  title: ''
  type: GettingStarted
  url: https://trigger.dev/docs/introduction
- group: build
  title: ''
  type: GitHub
  url: https://github.com/triggerdotdev
- group: build
  title: ''
  type: SDKs
  url: https://www.npmjs.com/package/@trigger.dev/sdk
- group: build
  title: ''
  type: CLI
  url: https://www.npmjs.com/package/trigger.dev
- group: start
  title: ''
  type: Signup
  url: https://cloud.trigger.dev/login
- group: commercial
  title: ''
  type: Pricing
  url: https://trigger.dev/pricing
- group: commercial
  title: ''
  type: PricingPlans
  url: plans/trigger-dev-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/trigger-dev-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/trigger-dev-finops.yml
- group: other
  title: ''
  type: Limits
  url: https://trigger.dev/docs/limits
- group: company
  title: ''
  type: Blog
  url: https://trigger.dev/blog
- group: operate
  title: ''
  type: ChangeLog
  url: https://trigger.dev/changelog
- group: operate
  title: ''
  type: StatusPage
  url: https://status.trigger.dev
- group: other
  title: ''
  type: SelfHosting
  url: https://github.com/triggerdotdev/docker
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/trigger-dev-vocabulary.yml
- group: design
  title: ''
  type: JSONLD
  url: json-ld/trigger-dev-context.jsonld
created: '2026-03-27'
description: Trigger.dev is an open source platform for building and deploying fully-managed AI agents and background workflows in TypeScript. It provides durable task execution without timeout constraints, automatic retries, scheduled cron tasks, queues with concurrency controls, real-time observability, React hooks for streaming run status, human-in-the-loop waitpoints, batch triggering, and a comprehensive Management API. Cloud-hosted at cloud.trigger.dev and self-hostable via Docker or Fly.io.
examples:
- key_count: 2
  name: Trigger Dev Create Schedule Example
  slug: trigger-dev-create-schedule-example
- key_count: 2
  name: Trigger Dev Create Waitpoint Example
  slug: trigger-dev-create-waitpoint-example
- key_count: 2
  name: Trigger Dev Execute Query Example
  slug: trigger-dev-execute-query-example
- key_count: 2
  name: Trigger Dev List Runs Example
  slug: trigger-dev-list-runs-example
- key_count: 2
  name: Trigger Dev Retrieve Run Events Example
  slug: trigger-dev-retrieve-run-events-example
- key_count: 2
  name: Trigger Dev Trigger Task Example
  slug: trigger-dev-trigger-task-example
finops:
- name: Trigger Dev Finops
  service_category: API
  slug: trigger-dev-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/trigger-dev.png
json_schemas:
- name: Trigger.dev Run
  property_count: 15
  slug: trigger-dev-run
- name: Trigger.dev Schedule
  property_count: 10
  slug: trigger-dev-schedule
- name: Trigger.dev Waitpoint Token
  property_count: 10
  slug: trigger-dev-waitpoint-token
json_structures:
- name: Trigger Dev Run Structure
  property_count: 0
  slug: trigger-dev-run-structure
jsonld:
- class_count: 10
  name: Trigger Dev Context
  property_count: 41
  slug: trigger-dev-context
layout: provider
modified: '2026-05-22'
name: Trigger.dev
nav: Providers
network: true
overview: 'Trigger.dev publishes 9 APIs on the [APIs.io](https://apis.io/) network, including Batches API, Deployments API, Environment Variables API, and 6 more. Tagged areas include Developer-First, Workflow-Automation, Background Jobs, Durable Execution, and TypeScript.


  The Trigger.dev catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Trigger.dev''s developer surface includes authentication, documentation, getting-started guide, GitHub presence, CLI, signup flow, pricing, and 17 more developer resources.'
plans:
- name: Trigger Dev Plans Pricing
  plan_count: 4
  slug: trigger-dev-plans-pricing
random_paper: 7
rate_limits:
- limit_count: 23
  name: Trigger Dev Rate Limits
  slug: trigger-dev-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: Trigger.dev API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: trigger-dev-jsonschema-spectral-rules
- effective_rule_count: 52
  extends:
  - spectral:oas
  name: Trigger.dev API Rules
  rule_count: 11
  severity_counts:
    error: 4
    hint: 2
    info: 0
    warn: 5
  slug: trigger-dev-rules
score:
  band: developing
  composite: 52.6
  delta: 0.0
  facets:
    access_clarity: 47.4
    commercial_clarity: 47.4
    contract_governance: 28.8
    contract_quality: 73.9
    developer_ergonomics: 54.8
    discoverability: 64.8
    governance: 28.8
    operational_transparency: 28.9
  previous_composite: 52.6
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 9
  schema_version: 0.12.1
  scored_at: '2026-08-24'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/trigger-dev/refs/heads/main/screenshots/trigger-dev-2026-06-20T195710.png
security:
- kind: authentication
  name: Trigger Dev Authentication
  slug: trigger-dev-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Trigger Dev Domain Security
  slug: trigger-dev-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: trust-center
  name: Trigger Dev Trust Center
  slug: trigger-dev-trust-center
  summary_line: SOC 2, HIPAA, GDPR
slug: trigger-dev
tags:
- Developer-First
- Workflow-Automation
- Background Jobs
- Durable Execution
- TypeScript
- AI Agents
- Real-Time
- Open-Source
website: https://trigger.dev
---
