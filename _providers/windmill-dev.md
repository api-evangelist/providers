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
  scored_at: '2026-08-03'
agentic_access:
- acting_count: 19
  human_in_the_loop: 1
  name: Windmill Dev Agentic Access
  operation_count: 49
  slug: windmill-dev-agentic-access
  summary_line: 49 operations · 19 acting · 1 human-in-the-loop
api_count: 15
apis:
- description: Low-code UIs backed by scripts and flows.
  name: Windmill Apps API
  slug: windmill-dev-apps-api
- description: Audit log entries (Enterprise Edition).
  name: Windmill Audit API
  slug: windmill-dev-audit-api
- description: DAG workflows composing scripts with branches, loops, and approvals.
  name: Windmill Flows API
  slug: windmill-dev-flows-api
- description: Ownership and permission boundaries for workspace assets.
  name: Windmill Folders API
  slug: windmill-dev-folders-api
- description: User groups for role-based access control.
  name: Windmill Groups API
  slug: windmill-dev-groups-api
- description: Execution of scripts and flows - run, inspect, and cancel jobs.
  name: Windmill Jobs API
  slug: windmill-dev-jobs-api
- description: Short-lived OIDC token issuance (Enterprise Edition).
  name: Windmill OIDC API
  slug: windmill-dev-oidc-api
- description: Typed connection objects and resource types.
  name: Windmill Resources API
  slug: windmill-dev-resources-api
- description: Cron schedules attached to runnables.
  name: Windmill Schedules API
  slug: windmill-dev-schedules-api
- description: Code runnables in Python, TypeScript, Go, Bash, SQL, and more.
  name: Windmill Scripts API
  slug: windmill-dev-scripts-api
- description: Event triggers - HTTP, WebSocket, Kafka, NATS, Postgres, SQS, MQTT.
  name: Windmill Triggers API
  slug: windmill-dev-triggers-api
- description: Users, authentication, tokens, and service accounts.
  name: Windmill Users API
  slug: windmill-dev-users-api
- description: Encrypted, path-scoped variables and secrets.
  name: Windmill Variables API
  slug: windmill-dev-variables-api
- description: The distributed worker fleet executing jobs.
  name: Windmill Workers API
  slug: windmill-dev-workers-api
- description: Isolated tenants and their settings.
  name: Windmill Workspaces API
  slug: windmill-dev-workspaces-api
artifact_total: 22
collections:
- collection_type: open
  name: Windmill API
  slug: open-windmill-dev
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/windmill-dev-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/windmill-dev-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/windmill-dev-authentication.yml
- group: company
  title: ''
  type: Blog
  url: https://www.windmill.dev/blog/atom.xml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/windmill-labs
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/windmill-labs
- group: company
  title: ''
  type: Website
  url: https://www.windmill.dev
- group: docs
  title: ''
  type: Documentation
  url: https://www.windmill.dev/docs
- group: commercial
  title: ''
  type: Plans
  url: plans/windmill-dev-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/windmill-dev-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/windmill-dev-finops.yml
created: '2026-07-02'
description: Windmill is an open-source developer platform that turns scripts (Python, TypeScript, Go, Bash, SQL, and more) into internal tools, UIs, workflows, and cron jobs. It runs as Windmill Cloud (app.windmill.dev) or self-hosted, with a distributed worker fleet executing jobs. Everything in a workspace - scripts, flows, apps, schedules, variables, resources, triggers - is addressable over a single REST API (base https://app.windmill.dev/api on Cloud, or /api self-hosted), authenticated with a Bearer token, and is the same surface the Windmill CLI and web UI use.
finops:
- name: Windmill Dev Finops
  service_category: Developer Platform and Workflow Orchestration
  slug: windmill-dev-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/windmill-dev.png
layout: provider
modified: '2026-07-02'
name: Windmill
nav: Providers
network: true
overview: 'Windmill publishes 15 APIs on the [APIs.io](https://apis.io/) network, including Apps API, Audit API, Flows API, and 12 more. Tagged areas include Developer Platform, Workflows, Internal Tools, Job Orchestration, and Cron.


  Windmill''s developer surface includes authentication, engineering blog, documentation, and 8 more developer resources.'
plans:
- name: Windmill Dev Plans Pricing
  plan_count: 5
  slug: windmill-dev-plans-pricing
random_paper: 88
rate_limits:
- limit_count: 6
  name: Windmill Dev Rate Limits
  slug: windmill-dev-rate-limits
score:
  band: thin
  composite: 39.7
  delta: 0.0
  facets:
    commercial_clarity: 39.5
    contract_quality: 61.2
    developer_ergonomics: 21.7
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 36.8
  previous_composite: 39.7
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 15
  schema_version: 0.9
  scored_at: '2026-08-03'
  trend: flat
security:
- kind: authentication
  name: Windmill Dev Authentication
  slug: windmill-dev-authentication
  summary_line: apiKey/http · 2 schemes
- kind: domain-security
  name: Windmill Dev Domain Security
  slug: windmill-dev-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
slug: windmill-dev
tags:
- Developer Platform
- Workflows
- Internal Tools
- Job Orchestration
- Cron
- Open Source
website: https://www.windmill.dev
---
