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
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 32.1
  scored_at: '2026-08-19'
agentic_access:
- acting_count: 17
  human_in_the_loop: 2
  name: Hathora Agentic Access
  operation_count: 36
  slug: hathora-agentic-access
  summary_line: 36 operations · 17 acting · 2 human-in-the-loop
api_count: 11
apis:
- description: Create and manage your organization's applications.
  name: Hathora AppsV2 API
  slug: hathora-appsv2-api
- description: Player authentication - issue short-lived player tokens.
  name: Hathora AuthV1 API
  slug: hathora-authv1-api
- description: Account balance, invoices, payment method, and Stripe portal.
  name: Hathora BillingV1 API
  slug: hathora-billingv1-api
- description: Upload and manage game server build artifacts.
  name: Hathora BuildsV3 API
  slug: hathora-buildsv3-api
- description: Versioned runtime configuration for a build.
  name: Hathora DeploymentsV3 API
  slug: hathora-deploymentsv3-api
- description: Region ping endpoints for latency-based routing.
  name: Hathora DiscoveryV2 API
  slug: hathora-discoveryv2-api
- description: Stream and download logs for processes.
  name: Hathora LogsV1 API
  slug: hathora-logsv1-api
- description: Read CPU, memory, egress, and connection metrics for a process.
  name: Hathora MetricsV1 API
  slug: hathora-metricsv1-api
- description: Launch, inspect, and stop running game server processes.
  name: Hathora ProcessesV3 API
  slug: hathora-processesv3-api
- description: Create, inspect, and destroy rooms and get connection info.
  name: Hathora RoomsV2 API
  slug: hathora-roomsv2-api
- description: Create, list, and revoke organization API tokens.
  name: Hathora TokensV1 API
  slug: hathora-tokensv1-api
artifact_total: 30
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Hathora Cloud AppsV2 API
  slug: open-hathora-appsv2-api
- collection_type: open
  name: Hathora Cloud AppsV2 AuthV1 API
  slug: open-hathora-authv1-api
- collection_type: open
  name: Hathora Cloud AppsV2 BillingV1 API
  slug: open-hathora-billingv1-api
- collection_type: open
  name: Hathora Cloud AppsV2 BuildsV3 API
  slug: open-hathora-buildsv3-api
- collection_type: open
  name: Hathora Cloud AppsV2 DeploymentsV3 API
  slug: open-hathora-deploymentsv3-api
- collection_type: open
  name: Hathora Cloud AppsV2 DiscoveryV2 API
  slug: open-hathora-discoveryv2-api
- collection_type: open
  name: Hathora Cloud AppsV2 LogsV1 API
  slug: open-hathora-logsv1-api
- collection_type: open
  name: Hathora Cloud AppsV2 MetricsV1 API
  slug: open-hathora-metricsv1-api
- collection_type: open
  name: Hathora Cloud AppsV2 ProcessesV3 API
  slug: open-hathora-processesv3-api
- collection_type: open
  name: Hathora Cloud AppsV2 RoomsV2 API
  slug: open-hathora-roomsv2-api
- collection_type: open
  name: Hathora Cloud AppsV2 TokensV1 API
  slug: open-hathora-tokensv1-api
- collection_type: open
  name: Hathora Cloud API
  slug: open-hathora
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/hathora-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/hathora-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/hathora-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/hathora
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/hathora
- group: company
  title: ''
  type: Website
  url: https://hathora.dev/
- group: docs
  title: ''
  type: Documentation
  url: https://hathora.dev/docs
- group: commercial
  title: ''
  type: Plans
  url: plans/hathora-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/hathora-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/hathora-finops.yml
- group: company
  title: ''
  type: Blog
  url: https://gamefabric.com/blog
created: '2026-07-01'
description: Hathora provides on-demand, globally distributed dedicated compute for multiplayer games. Hathora Cloud spins game server processes up and down across regions in response to player demand, exposing a REST API to manage applications, builds, deployments, processes, rooms, discovery/ping, logs, metrics, billing, and organization tokens, plus a player-authentication surface that issues short-lived player tokens.
finops:
- name: Hathora Finops
  service_category: Compute
  slug: hathora-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/hathora.png
layout: provider
modified: '2026-07-01'
name: Hathora
nav: Providers
network: true
overview: 'Hathora publishes 11 APIs on the [APIs.io](https://apis.io/) network, including AppsV2 API, AuthV1 API, BillingV1 API, and 8 more. Tagged areas include Game Servers, Multiplayer, Compute, Hosting, and Orchestration.


  Hathora''s developer surface includes authentication, documentation, engineering blog, and 8 more developer resources.'
plans:
- name: Hathora Plans Pricing
  plan_count: 3
  slug: hathora-plans-pricing
random_paper: 147
rate_limits:
- limit_count: 5
  name: Hathora Rate Limits
  slug: hathora-rate-limits
score:
  band: thin
  composite: 35.3
  delta: -2.6
  facets:
    access_clarity: 39.5
    commercial_clarity: 39.5
    contract_governance: 0.0
    contract_quality: 50.8
    developer_ergonomics: 14.3
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 34.2
  previous_composite: 37.9
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 11
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/hathora/refs/heads/main/screenshots/hathora-2026-07-25T220753.png
security:
- kind: authentication
  name: Hathora Authentication
  slug: hathora-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Hathora Domain Security
  slug: hathora-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: hathora
tags:
- Game Servers
- Multiplayer
- Compute
- Hosting
- Orchestration
website: https://hathora.dev/
---
