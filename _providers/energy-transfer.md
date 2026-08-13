---
access_model:
  confidence: high
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
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
  scored_at: '2026-08-12'
agentic_access:
- acting_count: 1
  human_in_the_loop: 0
  name: Energy Transfer Agentic Access
  operation_count: 4
  slug: energy-transfer-agentic-access
  summary_line: 4 operations · 1 acting
api_count: 3
apis:
- description: Manage gas pipeline nominations.
  name: Energy Transfer Nominations API
  slug: energy-transfer-nominations-api
- description: Retrieve pipeline information and status.
  name: Energy Transfer Pipelines API
  slug: energy-transfer-pipelines-api
- description: Access gas scheduling and capacity data.
  name: Energy Transfer Schedules API
  slug: energy-transfer-schedules-api
artifact_total: 10
collections:
- collection_type: open
  name: Energy Transfer Messenger+ API
  slug: open-energy-transfer-messenger-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/energy-transfer-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/energy-transfer-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/energy-transfer-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/energy-transfer
created: '2026-03-21'
description: Energy Transfer is one of the largest and most diversified midstream energy companies in North America, owning and operating natural gas, crude oil, NGL, and refined products pipelines, terminals, and storage facilities.
finops:
- name: Energy Transfer Finops
  service_category: Pipeline & Midstream Services
  slug: energy-transfer-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/energy-transfer.png
layout: provider
modified: '2026-05-19'
name: Energy Transfer
nav: Providers
network: true
overview: 'Energy Transfer publishes 3 APIs on the [APIs.io](https://apis.io/) network: Nominations API, Pipelines API, and Schedules API. Tagged areas include Energy, Pipelines, Midstream, Gas Scheduling, and Fortune 100.


  Energy Transfer''s developer surface includes authentication and 3 more developer resources.'
plans:
- name: Energy Transfer Plans Pricing
  plan_count: 1
  slug: energy-transfer-plans-pricing
random_paper: 4
rate_limits:
- limit_count: 1
  name: Energy Transfer Rate Limits
  slug: energy-transfer-rate-limits
score:
  band: emerging
  composite: 25.0
  delta: 0.0
  facets:
    commercial_clarity: 13.2
    contract_quality: 54.5
    developer_ergonomics: 10.9
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 5.3
  previous_composite: 25.0
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 3
  regulatory:
    applies: true
    matched_via: tags
    regime: Energy & Utilities
    regime_id: energy_utilities
    score: 16.2
  schema_version: 0.11.0
  scored_at: '2026-08-12'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/energy-transfer/refs/heads/main/screenshots/energy-transfer-2026-06-20T180705.png
security:
- kind: authentication
  name: Energy Transfer Authentication
  slug: energy-transfer-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Energy Transfer Domain Security
  slug: energy-transfer-domain-security
  summary_line: TLSv1.3 · DMARC
slug: energy-transfer
tags:
- Energy
- Pipelines
- Midstream
- Gas Scheduling
- Fortune 100
---
