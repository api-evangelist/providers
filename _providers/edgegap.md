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
  human_in_the_loop: 3
  name: Edgegap Agentic Access
  operation_count: 34
  slug: edgegap-agentic-access
  summary_line: 34 operations · 19 acting · 3 human-in-the-loop
api_count: 8
apis:
- description: Manage container image versions for an application.
  name: Edgegap App Versions API
  slug: edgegap-app-versions-api
- description: Manage applications registered on Edgegap.
  name: Edgegap Applications API
  slug: edgegap-applications-api
- description: Deploy, inspect, and stop dedicated game servers at the edge.
  name: Edgegap Deployments API
  slug: edgegap-deployments-api
- description: Private fleet deployments and host inventory.
  name: Edgegap Fleets API
  slug: edgegap-fleets-api
- description: Create and poll matchmaking tickets.
  name: Edgegap Matchmaking API
  slug: edgegap-matchmaking-api
- description: Monitoring and telemetry for deployments.
  name: Edgegap Metrics API
  slug: edgegap-metrics-api
- description: Distributed relay sessions and per-user authorization.
  name: Edgegap Relays API
  slug: edgegap-relays-api
- description: Add and remove players or groups on a running deployment.
  name: Edgegap Sessions API
  slug: edgegap-sessions-api
artifact_total: 15
collections:
- collection_type: open
  name: Edgegap Arbitrium API
  slug: open-edgegap
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/edgegap-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/edgegap-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/edgegap-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/edgegap
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/edgegap
- group: company
  title: ''
  type: Website
  url: https://edgegap.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.edgegap.com/
- group: commercial
  title: ''
  type: Plans
  url: plans/edgegap-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/edgegap-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/edgegap-finops.yml
created: '2026-07-01'
description: Edgegap provides distributed edge game-server orchestration, hosting, and matchmaking. Its Arbitrium platform auto-deploys dedicated game servers as containers to the optimal edge location out of 615+ locations worldwide, reducing latency for players. The REST API covers applications, versions, deployments, sessions, matchmaking, distributed relays, monitoring, and private fleets.
finops:
- name: Edgegap Finops
  service_category: Compute
  slug: edgegap-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/edgegap.png
layout: provider
modified: '2026-07-01'
name: Edgegap
nav: Providers
network: true
overview: 'Edgegap publishes 8 APIs on the [APIs.io](https://apis.io/) network, including App Versions API, Applications API, Deployments API, and 5 more. Tagged areas include Game Servers, Orchestration, Edge Computing, Matchmaking, and Hosting.


  Edgegap''s developer surface includes authentication, documentation, and 8 more developer resources.'
plans:
- name: Edgegap Plans Pricing
  plan_count: 3
  slug: edgegap-plans-pricing
random_paper: 52
rate_limits:
- limit_count: 4
  name: Edgegap Rate Limits
  slug: edgegap-rate-limits
score:
  band: thin
  composite: 38.1
  delta: 0.0
  facets:
    commercial_clarity: 39.5
    contract_quality: 56.4
    developer_ergonomics: 19.6
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 36.8
  previous_composite: 38.1
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 8
  schema_version: 0.9
  scored_at: '2026-08-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/edgegap/refs/heads/main/screenshots/edgegap-2026-07-25T212833.png
security:
- kind: authentication
  name: Edgegap Authentication
  slug: edgegap-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Edgegap Domain Security
  slug: edgegap-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: edgegap
tags:
- Game Servers
- Orchestration
- Edge Computing
- Matchmaking
- Hosting
website: https://edgegap.com/
---
