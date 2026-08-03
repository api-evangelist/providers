---
access_model:
  confidence: high
  label: Freemium (free trial) · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  trial: true
  try_now: true
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: documented
    event_surface_described: derived
    idempotency: false
    mcp_server: derived
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 37.2
  scored_at: '2026-08-03'
api_count: 3
apis:
- description: Read triaged, deduplicated bugs and their analysis runs.
  name: Sonarly Bugs API
  slug: sonarly-bugs-api
- description: Read incidents and their analysis runs.
  name: Sonarly Incidents API
  slug: sonarly-incidents-api
- description: Device-code style setup-session API to onboard a tenant.
  name: Sonarly Setup API
  slug: sonarly-setup-api
artifact_total: 9
asyncapis:
- description: Sonarly delivers signed outbound webhooks on bug and incident lifecycle events. Register a receiver via POST /api/setup/webhook-endpoint (the URL is SSRF-checked; a whsec_ signing secret is returned o
  name: Sonarly Webhooks
  slug: sonarly-events-asyncapi
common:
- group: start
  title: ''
  type: DeveloperPortal
  url: https://sonarly.com/docs/public-api
- group: docs
  title: ''
  type: Documentation
  url: https://sonarly.com/docs/public-api
- group: docs
  title: ''
  type: APIReference
  url: https://sonarly.com/docs/public-api
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/sonarly-llms.txt
- group: auth
  title: ''
  type: Authentication
  url: authentication/sonarly-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/sonarly-conventions.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/sonarly-rate-limits.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/sonarly-problem-types.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/sonarly-data-model.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/sonarly-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/sonarly-conformance.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/sonarly-mcp.yml
- group: docs
  title: ''
  type: AsyncAPI
  url: asyncapi/sonarly-events-asyncapi.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/sonarly-events-asyncapi.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/sonarly-domain-security.yml
- group: commercial
  title: ''
  type: Pricing
  url: https://sonarly.com/pricing
- group: commercial
  title: ''
  type: Plans
  url: plans/sonarly-plans.yml
- group: start
  title: ''
  type: SignUp
  url: https://sonarly.com/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/sonarly
created: '2026-07-17'
description: Sonarly is an AI production-reliability platform (Y Combinator W2026, Paris) that turns noisy production alerts into clear, deduplicated bug reports and ships ready-to-merge fix pull requests. It connects to a team's code (GitHub/GitLab) and their error and observability stack — Sentry, Datadog, Grafana, New Relic, SigNoz, CloudWatch, GCP, and many more — then triages every alert to remove noise and duplicates, investigates logs, traces and metrics to find the root cause, and generates a fix PR or alerting-rule recommendation. Sonarly exposes a read-only public REST API (v1) for pulling bugs, incidents and analysis runs into custom dashboards, signed outbound webhooks for live events, and a device-code style setup-session API that lets a coding agent (Claude Code, Cursor) onboard a tenant end-to-end. Onboarding is fully agent-native and documented at sonarly.com/llms.txt.
image: https://sonarly.com/logo_sonarly.png
layout: provider
mcp_servers:
- description: ''
  name: sonarly-mcp.yml
  slug: sonarly-mcpyml
modified: '2026-07-21'
name: Sonarly
nav: Providers
network: true
overview: 'Sonarly publishes 3 APIs on the [APIs.io](https://apis.io/) network: Bugs API, Incidents API, and Setup API. Tagged areas include Company, Reliability, Observability, Monitoring, and Bug Detection.


  The Sonarly catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Sonarly''s developer surface includes documentation, API reference, authentication, pricing, signup flow, and 15 more developer resources.'
plans:
- name: Sonarly Plans
  plan_count: 4
  slug: sonarly-plans
random_paper: 16
rate_limits:
- limit_count: 1
  name: Sonarly Rate Limits
  slug: sonarly-rate-limits
score:
  band: developing
  composite: 48.9
  delta: 0.0
  facets:
    commercial_clarity: 55.3
    contract_quality: 68.7
    developer_ergonomics: 38.6
    discoverability: 81.5
    governance: 3.1
    operational_transparency: 34.2
  previous_composite: 48.9
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 3
    mcp: derived
    skills: derived
  schema_version: 0.9
  scored_at: '2026-08-03'
  trend: flat
security:
- kind: authentication
  name: Sonarly Authentication
  slug: sonarly-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Sonarly Domain Security
  slug: sonarly-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: sonarly
tags:
- Company
- Reliability
- Observability
- Monitoring
- Bug Detection
- Incident Management
- Root Cause Analysis
- AI Agents
- Developer Tools
- DevOps
website: https://sonarly.com/docs/public-api
---
