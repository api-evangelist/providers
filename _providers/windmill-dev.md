---
access_model:
  confidence: medium
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  - security
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
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 21.5
  scored_at: '2026-09-04'
agentic_access:
- acting_count: 19
  human_in_the_loop: 1
  name: Windmill Dev Agentic Access
  operation_count: 49
  slug: windmill-dev-agentic-access
  summary_line: 49 operations · 19 acting · 1 human-in-the-loop
api_count: 1
apis:
- baseURL: https://app.windmill.dev/api
  baseurl_source: declared
  description: Low-code UIs backed by scripts and flows.
  name: Windmill Apps API
  slug: windmill-dev-apps-api
- baseURL: https://app.windmill.dev/api
  baseurl_source: declared
  description: Audit log entries (Enterprise Edition).
  name: Windmill Audit API
  slug: windmill-dev-audit-api
- baseURL: https://app.windmill.dev/api
  baseurl_source: declared
  description: DAG workflows composing scripts with branches, loops, and approvals.
  name: Windmill Flows API
  slug: windmill-dev-flows-api
- baseURL: https://app.windmill.dev/api
  baseurl_source: declared
  description: Ownership and permission boundaries for workspace assets.
  name: Windmill Folders API
  slug: windmill-dev-folders-api
- baseURL: https://app.windmill.dev/api
  baseurl_source: declared
  description: User groups for role-based access control.
  name: Windmill Groups API
  slug: windmill-dev-groups-api
- baseURL: https://app.windmill.dev/api
  baseurl_source: declared
  description: Execution of scripts and flows - run, inspect, and cancel jobs.
  name: Windmill Jobs API
  slug: windmill-dev-jobs-api
- baseURL: https://app.windmill.dev/api
  baseurl_source: declared
  description: Short-lived OIDC token issuance (Enterprise Edition).
  name: Windmill OIDC API
  slug: windmill-dev-oidc-api
- baseURL: https://app.windmill.dev/api
  baseurl_source: declared
  description: Typed connection objects and resource types.
  name: Windmill Resources API
  slug: windmill-dev-resources-api
- baseURL: https://app.windmill.dev/api
  baseurl_source: declared
  description: Cron schedules attached to runnables.
  name: Windmill Schedules API
  slug: windmill-dev-schedules-api
- baseURL: https://app.windmill.dev/api
  baseurl_source: declared
  description: Code runnables in Python, TypeScript, Go, Bash, SQL, and more.
  name: Windmill Scripts API
  slug: windmill-dev-scripts-api
- baseURL: https://app.windmill.dev/api
  baseurl_source: declared
  description: Event triggers - HTTP, WebSocket, Kafka, NATS, Postgres, SQS, MQTT.
  name: Windmill Triggers API
  slug: windmill-dev-triggers-api
- baseURL: https://app.windmill.dev/api
  baseurl_source: declared
  description: Users, authentication, tokens, and service accounts.
  name: Windmill Users API
  slug: windmill-dev-users-api
- baseURL: https://app.windmill.dev/api
  baseurl_source: declared
  description: Encrypted, path-scoped variables and secrets.
  name: Windmill Variables API
  slug: windmill-dev-variables-api
- baseURL: https://app.windmill.dev/api
  baseurl_source: declared
  description: The distributed worker fleet executing jobs.
  name: Windmill Workers API
  slug: windmill-dev-workers-api
- baseURL: https://app.windmill.dev/api
  baseurl_source: declared
  description: Isolated tenants and their settings.
  name: Windmill Workspaces API
  slug: windmill-dev-workspaces-api
artifact_total: 38
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Windmill Apps API
  slug: open-windmill-dev-apps-api
- collection_type: open
  name: Windmill Apps Audit API
  slug: open-windmill-dev-audit-api
- collection_type: open
  name: Windmill Apps Flows API
  slug: open-windmill-dev-flows-api
- collection_type: open
  name: Windmill Apps Folders API
  slug: open-windmill-dev-folders-api
- collection_type: open
  name: Windmill Apps Groups API
  slug: open-windmill-dev-groups-api
- collection_type: open
  name: Windmill Apps Jobs API
  slug: open-windmill-dev-jobs-api
- collection_type: open
  name: Windmill Apps OIDC API
  slug: open-windmill-dev-oidc-api
- collection_type: open
  name: Windmill Apps Resources API
  slug: open-windmill-dev-resources-api
- collection_type: open
  name: Windmill Apps Schedules API
  slug: open-windmill-dev-schedules-api
- collection_type: open
  name: Windmill Apps Scripts API
  slug: open-windmill-dev-scripts-api
- collection_type: open
  name: Windmill Apps Triggers API
  slug: open-windmill-dev-triggers-api
- collection_type: open
  name: Windmill Apps Users API
  slug: open-windmill-dev-users-api
- collection_type: open
  name: Windmill Apps Variables API
  slug: open-windmill-dev-variables-api
- collection_type: open
  name: Windmill Apps Workers API
  slug: open-windmill-dev-workers-api
- collection_type: open
  name: Windmill Apps Workspaces API
  slug: open-windmill-dev-workspaces-api
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
random_paper: 10
rate_limits:
- limit_count: 6
  name: Windmill Dev Rate Limits
  slug: windmill-dev-rate-limits
score:
  band: thin
  composite: 39.0
  coverage:
    artifact_dirs: 10
    catalog_earned: 64.0
    catalog_earned_first_party: 0.0
    catalog_gap: 51.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -0.8
  facets:
    access_clarity: 39.5
    commercial_clarity: 39.5
    contract_governance: 0.0
    contract_quality: 53.7
    developer_ergonomics: 32.1
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 34.2
  previous_composite: 39.8
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 15
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/windmill-dev/refs/heads/main/screenshots/windmill-dev-2026-09-02T170815.png
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
- Open-Source
website: https://www.windmill.dev
---
