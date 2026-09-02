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
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 19.8
  scored_at: '2026-09-01'
agentic_access:
- acting_count: 1
  human_in_the_loop: 0
  name: Bodytrace Agentic Access
  operation_count: 6
  slug: bodytrace-agentic-access
  summary_line: 6 operations · 1 acting
api_count: 1
apis:
- description: Modeled threshold and connectivity alerts.
  name: BodyTrace Alerts API
  slug: bodytrace-alerts-api
- description: Modeled surface for raw per-transmission device messages.
  name: BodyTrace Data Messages API
  slug: bodytrace-data-messages-api
- description: Modeled device listing and status keyed by IMEI.
  name: BodyTrace Devices API
  slug: bodytrace-devices-api
- description: Confirmed pull surface for device readings (data values).
  name: BodyTrace Observations API
  slug: bodytrace-observations-api
- description: Modeled device enrollment and delivery configuration.
  name: BodyTrace Provisioning API
  slug: bodytrace-provisioning-api
artifact_total: 18
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: BodyTrace RPM Data Alerts API
  slug: open-bodytrace-alerts-api
- collection_type: open
  name: BodyTrace RPM Data Alerts Data Messages API
  slug: open-bodytrace-data-messages-api
- collection_type: open
  name: BodyTrace RPM Data Alerts Devices API
  slug: open-bodytrace-devices-api
- collection_type: open
  name: BodyTrace RPM Data Alerts Observations API
  slug: open-bodytrace-observations-api
- collection_type: open
  name: BodyTrace RPM Data Alerts Provisioning API
  slug: open-bodytrace-provisioning-api
- collection_type: open
  name: BodyTrace RPM Data API
  slug: open-bodytrace
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/bodytrace-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/bodytrace-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/bodytrace-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/bodytrace
- group: company
  title: ''
  type: Website
  url: https://www.bodytrace.com
- group: docs
  title: ''
  type: Documentation
  url: https://www.bodytrace.com/medical/
- group: commercial
  title: ''
  type: Plans
  url: plans/bodytrace-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/bodytrace-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/bodytrace-finops.yml
created: '2026-07-05'
description: BodyTrace makes cellular-connected remote patient monitoring (RPM) devices - blood pressure monitors, body-weight scales, and pulse oximeters - that transmit readings directly over the cellular network with no phone, app, Wi-Fi, or Bluetooth pairing required. Each device encrypts measurements end-to-end and sends them to the BodyTrace platform, which exposes the data to healthcare organizations, EHRs, and RPM programs over a simple HTTP API using HTTP Basic authentication. Consumers can pull device readings (data values) on a polling loop or receive them pushed to a configured HTTP endpoint. BodyTrace sells to organizations, not individuals; API and device provisioning are arranged through BodyTrace sales.
finops:
- name: Bodytrace Finops
  service_category: Healthcare and Medical Devices
  slug: bodytrace-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/bodytrace.png
layout: provider
modified: '2026-07-05'
name: BodyTrace
nav: Providers
network: true
overview: 'BodyTrace publishes 5 APIs on the [APIs.io](https://apis.io/) network, including Alerts API, Data Messages API, Devices API, and 2 more. Tagged areas include Remote Patient Monitoring, RPM, Cellular, Medical Devices, and Digital Health.


  BodyTrace''s developer surface includes authentication, documentation, and 7 more developer resources.'
plans:
- name: Bodytrace Plans Pricing
  plan_count: 2
  slug: bodytrace-plans-pricing
random_paper: 12
rate_limits:
- limit_count: 3
  name: Bodytrace Rate Limits
  slug: bodytrace-rate-limits
score:
  band: thin
  composite: 35.4
  coverage:
    artifact_dirs: 9
    catalog_gap: 55.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 28.9
    commercial_clarity: 28.9
    contract_governance: 0.0
    contract_quality: 55.8
    developer_ergonomics: 26.2
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 31.6
  previous_composite: 35.4
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
    regime: Health
    regime_id: health
    score: 15.0
  schema_version: 0.18.0
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/bodytrace/refs/heads/main/screenshots/bodytrace-2026-07-25T203525.png
security:
- kind: authentication
  name: Bodytrace Authentication
  slug: bodytrace-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Bodytrace Domain Security
  slug: bodytrace-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: bodytrace
tags:
- Remote Patient Monitoring
- RPM
- Cellular
- Medical Devices
- Digital Health
- Blood Pressure
- Connected Devices
- IoT
website: https://www.bodytrace.com
---
