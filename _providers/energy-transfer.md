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
  band: agent-ready
  dimensions:
    agent_skills: false
    agentic_access: true
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: true
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.1
  score: 48.1
  scored_at: '2026-07-27'
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
random_paper: 0
rate_limits:
- limit_count: 1
  name: Energy Transfer Rate Limits
  slug: energy-transfer-rate-limits
score:
  band: thin
  composite: 33.3
  delta: 3.2
  facets:
    commercial_clarity: 28.9
    contract_quality: 50.4
    developer_ergonomics: 10.9
    discoverability: 100.0
    governance: 0.0
    operational_transparency: 21.1
  previous_composite: 30.1
  schema_version: 0.5
  scored_at: '2026-07-27'
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
