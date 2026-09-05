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
    agentic_commerce: false
    auth_clarity: false
    consent_identity: false
    delegated_identity: false
    dry_run_mode: na
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: na
    mcp_server: false
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 22.9
  scored_at: '2026-09-04'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Pulse Grow Agentic Access
  operation_count: 19
  slug: pulse-grow-agentic-access
  summary_line: 19 operations
api_count: 1
apis:
- baseURL: https://api.pulsegrow.com
  baseurl_source: declared
  description: A collection of API operations related to devices.
  name: Pulse Grow AllDevices API
  slug: pulse-grow-alldevices-api
- baseURL: https://api.pulsegrow.com
  baseurl_source: declared
  description: A collection of API operations related to devices.
  name: Pulse Grow Devices API
  slug: pulse-grow-devices-api
- baseURL: https://api.pulsegrow.com
  baseurl_source: declared
  description: A collection of API operations related to users.
  name: Pulse Grow Hub API
  slug: pulse-grow-hub-api
- baseURL: https://api.pulsegrow.com
  baseurl_source: declared
  description: A collection of API operations related to inviting users.
  name: Pulse Grow Invitation API
  slug: pulse-grow-invitation-api
- baseURL: https://api.pulsegrow.com
  baseurl_source: declared
  description: A collection of API operations related to light readings.
  name: Pulse Grow ProLightReading API
  slug: pulse-grow-prolightreading-api
- baseURL: https://api.pulsegrow.com
  baseurl_source: declared
  description: A collection of API operations related to devices.
  name: Pulse Grow Sensors API
  slug: pulse-grow-sensors-api
- baseURL: https://api.pulsegrow.com
  baseurl_source: declared
  description: A collection of API operations related to timeline events.
  name: Pulse Grow TimeLineEvent API
  slug: pulse-grow-timelineevent-api
- baseURL: https://api.pulsegrow.com
  baseurl_source: declared
  description: A collection of API operations related to timeline events.
  name: Pulse Grow TriggeredThreshold API
  slug: pulse-grow-triggeredthreshold-api
- baseURL: https://api.pulsegrow.com
  baseurl_source: declared
  description: A collection of API operations related to users.
  name: Pulse Grow User API
  slug: pulse-grow-user-api
artifact_total: 25
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Pulse Api AllDevices API
  slug: open-pulse-grow-alldevices-api
- collection_type: open
  name: Pulse Api AllDevices Devices API
  slug: open-pulse-grow-devices-api
- collection_type: open
  name: Pulse Api AllDevices Hub API
  slug: open-pulse-grow-hub-api
- collection_type: open
  name: Pulse Api AllDevices Invitation API
  slug: open-pulse-grow-invitation-api
- collection_type: open
  name: Pulse Api AllDevices ProLightReading API
  slug: open-pulse-grow-prolightreading-api
- collection_type: open
  name: Pulse Api AllDevices Sensors API
  slug: open-pulse-grow-sensors-api
- collection_type: open
  name: Pulse Api AllDevices TimeLineEvent API
  slug: open-pulse-grow-timelineevent-api
- collection_type: open
  name: Pulse Api AllDevices TriggeredThreshold API
  slug: open-pulse-grow-triggeredthreshold-api
- collection_type: open
  name: Pulse Api AllDevices User API
  slug: open-pulse-grow-user-api
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
random_paper: 16
rate_limits:
- limit_count: 5
  name: Pulse Grow Rate Limits
  slug: pulse-grow-rate-limits
score:
  band: emerging
  composite: 20.5
  coverage:
    artifact_dirs: 8
    catalog_earned: 35.0
    catalog_earned_first_party: 0.0
    catalog_gap: 65.0
    catalog_max: 100.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 46.6
    developer_ergonomics: 9.5
    discoverability: 59.3
    governance: 0.0
    operational_transparency: 7.9
  previous_composite: 20.5
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 9
  schema_version: 0.18.3
  scored_at: '2026-09-04'
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
