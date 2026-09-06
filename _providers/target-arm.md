---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source: []
  trial: false
  try_now: false
agent_readiness:
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: false
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
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 0.0
  scored_at: '2026-09-05'
api_count: 0
artifact_total: 1
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/target-arm-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://targetarm.com/
created: '2026-07-17'
description: Target Arm is a robotics company building systems to autonomously launch and recover drones from moving vehicles without stopping. Its Ralar robotic arm captures drones mid-air, recharges them, and relaunches them, while TRACKR sensor-fusion, TurboFly autopilot, and Maestro mission-control software coordinate drone fleets across commercial delivery, first-responder, agriculture, energy-inspection, and defense/ISR use cases. A Techstars-backed hardware startup with no public API or developer program at this time; this network profile captures identity and infrastructure signals only.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/target-arm.png
layout: provider
modified: '2026-07-21'
name: Target Arm
nav: Providers
network: true
overview: Target Arm is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Robotics, Drones, UAV, and Autonomous Systems.
random_paper: 4
score:
  band: minimal
  composite: 5.0
  coverage:
    artifact_dirs: 2
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 5.0
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/target-arm/refs/heads/main/screenshots/target-arm-2026-09-02T162542.png
security:
- kind: domain-security
  name: Target Arm Domain Security
  slug: target-arm-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: target-arm
tags:
- Company
- Robotics
- Drones
- UAV
- Autonomous Systems
- Defense
- Hardware
- Aerospace
website: https://targetarm.com/
---
