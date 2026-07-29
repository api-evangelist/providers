---
access_model:
  confidence: medium
  label: Freemium
  onboarding: unknown
  pricing: freemium
  public: false
  source:
  - plans
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    asyncapi_events: false
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: partial
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 24.8
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Pulse Grow Agentic Access
  operation_count: 19
  slug: pulse-grow-agentic-access
  summary_line: 19 operations
api_count: 9
apis:
- description: A collection of API operations related to devices.
  name: Pulse Grow AllDevices API
  slug: pulse-grow-alldevices-api
- description: A collection of API operations related to devices.
  name: Pulse Grow Devices API
  slug: pulse-grow-devices-api
- description: A collection of API operations related to users.
  name: Pulse Grow Hub API
  slug: pulse-grow-hub-api
- description: A collection of API operations related to inviting users.
  name: Pulse Grow Invitation API
  slug: pulse-grow-invitation-api
- description: A collection of API operations related to light readings.
  name: Pulse Grow ProLightReading API
  slug: pulse-grow-prolightreading-api
- description: A collection of API operations related to devices.
  name: Pulse Grow Sensors API
  slug: pulse-grow-sensors-api
- description: A collection of API operations related to timeline events.
  name: Pulse Grow TimeLineEvent API
  slug: pulse-grow-timelineevent-api
- description: A collection of API operations related to timeline events.
  name: Pulse Grow TriggeredThreshold API
  slug: pulse-grow-triggeredthreshold-api
- description: A collection of API operations related to users.
  name: Pulse Grow User API
  slug: pulse-grow-user-api
artifact_total: 15
collections:
- collection_type: open
  name: Pulse Api
  slug: open-pulse-grow
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/pulse-grow-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/pulse-grow-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/pulsegrow
created: '2025-02-24'
description: The Pulse API is an HTTP API that is designed to interact with your pulse account and devices.
finops:
- name: Pulse Grow Finops
  service_category: API
  slug: pulse-grow-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/pulse-grow.png
layout: provider
modified: '2026-05-19'
name: Pulse Grow
nav: Providers
network: true
overview: Pulse Grow publishes 9 APIs on the [APIs.io](https://apis.io/) network, including AllDevices API, Devices API, Hub API, and 6 more. Tagged areas include Devices, Sensors, Hub, Monitoring, and Growing.
plans:
- name: Pulse Grow Plans Pricing
  plan_count: 3
  slug: pulse-grow-plans-pricing
random_paper: 44
rate_limits:
- limit_count: 5
  name: Pulse Grow Rate Limits
  slug: pulse-grow-rate-limits
score:
  band: thin
  composite: 28.6
  delta: -2.8
  facets:
    commercial_clarity: 39.5
    contract_quality: 40.6
    developer_ergonomics: 0.0
    discoverability: 64.8
    governance: 0.0
    operational_transparency: 31.6
  previous_composite: 31.4
  provenance:
    agentic_access: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 9
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/pulse-grow/refs/heads/main/screenshots/pulse-grow-2026-06-20T192255.png
security:
- kind: domain-security
  name: Pulse Grow Domain Security
  slug: pulse-grow-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
slug: pulse-grow
tags:
- Devices
- Sensors
- Hub
- Monitoring
- Growing
---
