---
access_model:
  confidence: high
  label: Enterprise · Self-serve signup
  onboarding: self-serve
  pricing: enterprise
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    asyncapi_events: false
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
  score: 30.6
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 6
  human_in_the_loop: 0
  name: Truphone Agentic Access
  operation_count: 17
  slug: truphone-agentic-access
  summary_line: 17 operations · 6 acting
api_count: 5
apis:
- description: Data sessions, call detail records, status, and location updates.
  name: Truphone (1GLOBAL) Connectivity API
  slug: truphone-connectivity-api
- description: Connected device management and automation rules.
  name: Truphone (1GLOBAL) Devices API
  slug: truphone-devices-api
- description: Tags and custom attributes for organizing SIM fleets.
  name: Truphone (1GLOBAL) Organization API
  slug: truphone-organization-api
- description: Rate plans and SIM subscriptions.
  name: Truphone (1GLOBAL) Plans API
  slug: truphone-plans-api
- description: SIM / eSIM listing, retrieval, update, and lifecycle status changes.
  name: Truphone (1GLOBAL) SIMs API
  slug: truphone-sims-api
artifact_total: 12
collections:
- collection_type: open
  name: Truphone (1GLOBAL) IoT Portal API
  slug: open-truphone
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/truphone-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/truphone-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/truphone-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Truphone
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/1global
- group: company
  title: ''
  type: Website
  url: https://www.1global.com
- group: docs
  title: ''
  type: Documentation
  url: https://docs.1global.com
- group: commercial
  title: ''
  type: Plans
  url: plans/truphone-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/truphone-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/truphone-finops.yml
created: '2026-06-21'
description: Truphone is a global eSIM, IoT, and enterprise connectivity provider now operating as 1GLOBAL after its 2022 acquisition. It runs its own global mobile network supplemented by roaming across 600+ partner networks in 190+ countries, and exposes REST APIs for SIM/eSIM lifecycle management, data usage and connectivity, rate plans, and IoT device management across its 1GLOBAL IoT Portal, 1GLOBAL Connect, and the 1GLOBAL platform API.
finops:
- name: Truphone Finops
  service_category: IoT and Connectivity
  slug: truphone-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/truphone.png
layout: provider
modified: '2026-06-21'
name: Truphone (1GLOBAL)
nav: Providers
network: true
overview: 'Truphone (1GLOBAL) publishes 5 APIs on the [APIs.io](https://apis.io/) network, including Connectivity API, Devices API, Organization API, and 2 more. Tagged areas include eSIM, IoT, Connectivity, SIM Management, and Telecom.


  Truphone (1GLOBAL)''s developer surface includes authentication, documentation, and 8 more developer resources.'
plans:
- name: Truphone Plans Pricing
  plan_count: 4
  slug: truphone-plans-pricing
random_paper: 75
rate_limits:
- limit_count: 2
  name: Truphone Rate Limits
  slug: truphone-rate-limits
score:
  band: thin
  composite: 33.8
  delta: -5.2
  facets:
    commercial_clarity: 39.5
    contract_quality: 56.8
    developer_ergonomics: 19.6
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 26.3
  previous_composite: 39.0
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 5
  regulatory:
    applies: true
    matched_via: tags
    regime: Telecommunications
    regime_id: telecommunications
    score: 16.7
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: falling
security:
- kind: authentication
  name: Truphone Authentication
  slug: truphone-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Truphone Domain Security
  slug: truphone-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: truphone
tags:
- eSIM
- IoT
- Connectivity
- SIM Management
- Telecom
- Mobile Network
website: https://www.1global.com
---
