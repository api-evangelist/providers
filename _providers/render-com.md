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
    asyncapi_events: true
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 36.0
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 61
  human_in_the_loop: 1
  name: Render Com Agentic Access
  operation_count: 110
  slug: render-com-agentic-access
  summary_line: 110 operations · 61 acting · 1 human-in-the-loop
api_count: 17
apis:
- description: Infrastructure-as-code Blueprints (render.yaml).
  name: Render Blueprints API
  slug: render-com-blueprints-api
- description: Custom domains attached to a service, with DNS and TLS.
  name: Render Custom Domains API
  slug: render-com-custom-domains-api
- description: Build and release deploys for a service, plus rollback.
  name: Render Deploys API
  slug: render-com-deploys-api
- description: Persistent disks and snapshots.
  name: Render Disks API
  slug: render-com-disks-api
- description: Reusable groups of environment variables and secret files.
  name: Render Environment Groups API
  slug: render-com-environment-groups-api
- description: Per-service environment variables and secret files.
  name: Render Environment Variables API
  slug: render-com-environment-variables-api
- description: Environments within a project.
  name: Render Environments API
  slug: render-com-environments-api
- description: One-off jobs run in a service environment.
  name: Render Jobs API
  slug: render-com-jobs-api
- description: Redis-compatible Key Value datastores.
  name: Render Key Value API
  slug: render-com-key-value-api
- description: Historical log queries. Real-time streaming is over WebSocket.
  name: Render Logs API
  slug: render-com-logs-api
- description: Time-series metrics for services and datastores.
  name: Render Metrics API
  slug: render-com-metrics-api
- description: Managed Render Postgres instances.
  name: Render Postgres API
  slug: render-com-postgres-api
- description: Projects and their environments.
  name: Render Projects API
  slug: render-com-projects-api
- description: Container registry credentials.
  name: Render Registry Credentials API
  slug: render-com-registry-credentials-api
- description: Web services, static sites, private services, background workers, and cron jobs.
  name: Render Services API
  slug: render-com-services-api
- description: Outbound webhooks for platform events.
  name: Render Webhooks API
  slug: render-com-webhooks-api
- description: Workspaces (owners) and members.
  name: Render Workspaces API
  slug: render-com-workspaces-api
artifact_total: 28
asyncapis:
- description: Render exposes a documented public WebSocket surface for real-time log streaming. A client opens a WebSocket connection to wss://api.render.com/v1/logs/subscribe with an API key Bearer token and query
  name: Render Logs Subscription API
  slug: render-com-asyncapi
collections:
- collection_type: open
  name: Render API
  slug: open-render-com
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/render-com-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/render-com-trust-center.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/render-com-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/render-com-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/render-com-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/renderinc
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/renderco
- group: company
  title: ''
  type: Website
  url: https://render.com
- group: docs
  title: ''
  type: Documentation
  url: https://render.com/docs
- group: commercial
  title: ''
  type: Plans
  url: plans/render-com-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/render-com-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/render-com-finops.yml
- group: company
  title: ''
  type: Blog
  url: https://render.com/blog/feed.rss
created: '2026-07-02'
description: Render is a unified cloud application platform (PaaS) for building, deploying, and scaling web services, static sites, background workers, cron jobs, and one-off jobs alongside managed Postgres and Key Value (Redis-compatible) datastores. The Render REST API (https://api.render.com/v1) exposes almost all Render Dashboard capabilities - services, deploys, custom domains, environment variables and groups, persistent disks, Blueprints, projects and environments, metrics, and logs - with a documented WebSocket surface for real-time log streaming.
finops:
- name: Render Com Finops
  service_category: Compute and Application Hosting
  slug: render-com-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/render-com.png
layout: provider
modified: '2026-07-02'
name: Render
nav: Providers
network: true
overview: 'Render publishes 17 APIs on the [APIs.io](https://apis.io/) network, including Blueprints API, Custom Domains API, Deploys API, and 14 more. Tagged areas include Cloud Hosting, PaaS, Deployment, Web Services, and Databases.


  The Render catalog on APIs.io includes 1 event-driven AsyncAPI specification and 1 Spectral governance ruleset.


  Render''s developer surface includes authentication, documentation, engineering blog, and 10 more developer resources.'
plans:
- name: Render Com Plans Pricing
  plan_count: 4
  slug: render-com-plans-pricing
random_paper: 20
rate_limits:
- limit_count: 7
  name: Render Com Rate Limits
  slug: render-com-rate-limits
rules:
- name: Render API Rules
  rule_count: 4
  severity_counts:
    error: 1
    hint: 0
    info: 0
    warn: 3
  slug: render-com-asyncapi-spectral-rules
score:
  band: developing
  composite: 43.5
  delta: -2.6
  facets:
    commercial_clarity: 47.4
    contract_quality: 62.1
    developer_ergonomics: 21.7
    discoverability: 68.5
    governance: 20.8
    operational_transparency: 36.8
  previous_composite: 46.1
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 17
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
security:
- kind: authentication
  name: Render Com Authentication
  slug: render-com-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Render Com Domain Security
  slug: render-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Render Com Vulnerability Disclosure
  slug: render-com-vulnerability-disclosure
  summary_line: Hackerone · security.txt · contact published
- kind: trust-center
  name: Render Com Trust Center
  slug: render-com-trust-center
  summary_line: SOC 2, ISO 27001, HIPAA, GDPR
slug: render-com
tags:
- Cloud Hosting
- PaaS
- Deployment
- Web Services
- Databases
- DevOps
website: https://render.com
---
