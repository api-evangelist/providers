---
access_model:
  confidence: high
  label: Paid · Self-serve signup
  onboarding: self-serve
  pricing: paid
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
  scored_at: '2026-07-23'
agentic_access:
- acting_count: 13
  human_in_the_loop: 0
  name: Hologram Agentic Access
  operation_count: 23
  slug: hologram-agentic-access
  summary_line: 23 operations · 13 acting
api_count: 8
apis:
- description: The Cellular Links API from Hologram — 6 operation(s) for cellular links.
  name: Hologram Cellular Links API
  slug: hologram-cellular-links-api
- description: The Devices API from Hologram — 3 operation(s) for devices.
  name: Hologram Devices API
  slug: hologram-devices-api
- description: The Messaging API from Hologram — 1 operation(s) for messaging.
  name: Hologram Messaging API
  slug: hologram-messaging-api
- description: The Plans API from Hologram — 2 operation(s) for plans.
  name: Hologram Plans API
  slug: hologram-plans-api
- description: The SMS API from Hologram — 1 operation(s) for sms.
  name: Hologram SMS API
  slug: hologram-sms-api
- description: The Tags API from Hologram — 4 operation(s) for tags.
  name: Hologram Tags API
  slug: hologram-tags-api
- description: The Usage API from Hologram — 3 operation(s) for usage.
  name: Hologram Usage API
  slug: hologram-usage-api
- description: The Webhooks API from Hologram — 1 operation(s) for webhooks.
  name: Hologram Webhooks API
  slug: hologram-webhooks-api
artifact_total: 15
collections:
- collection_type: open
  name: Hologram REST API
  slug: open-hologram
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/hologram-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/hologram-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/hologram-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/hologram-io
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/hologramio
- group: company
  title: ''
  type: Website
  url: https://www.hologram.io/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.hologram.io/
- group: commercial
  title: ''
  type: Plans
  url: plans/hologram-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/hologram-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/hologram-finops.yml
created: '2026-06-21'
description: Hologram is a global cellular IoT connectivity platform providing eUICC SIMs that roam across 550+ carrier networks in 200+ countries. The Hologram REST API lets developers activate and manage SIMs and devices, query data and SMS usage, send SMS and cloud messages to devices, manage plans and tags, and open secure Spacebridge tunnels.
finops:
- name: Hologram Finops
  service_category: IoT and Connectivity
  slug: hologram-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/hologram.png
layout: provider
modified: '2026-06-21'
name: Hologram
nav: Providers
network: true
overview: 'Hologram publishes 8 APIs on the [APIs.io](https://apis.io/) network, including Cellular Links API, Devices API, Messaging API, and 5 more. Tagged areas include IoT, Cellular, Connectivity, SIM, and M2M.


  Hologram''s developer surface includes authentication, documentation, and 8 more developer resources.'
plans:
- name: Hologram Plans Pricing
  plan_count: 2
  slug: hologram-plans-pricing
random_paper: 41
rate_limits:
- limit_count: 2
  name: Hologram Rate Limits
  slug: hologram-rate-limits
score:
  band: thin
  composite: 32.6
  delta: 0.0
  facets:
    commercial_clarity: 28.9
    contract_quality: 50.9
    developer_ergonomics: 19.6
    discoverability: 67.5
    governance: 0.0
    operational_transparency: 26.3
  previous_composite: 32.6
  schema_version: 0.5
  scored_at: '2026-07-23'
  trend: flat
security:
- kind: authentication
  name: Hologram Authentication
  slug: hologram-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Hologram Domain Security
  slug: hologram-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: hologram
tags:
- IoT
- Cellular
- Connectivity
- SIM
- M2M
website: https://www.hologram.io/
---
