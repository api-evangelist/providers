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
  scored_at: '2026-09-02'
api_count: 0
artifact_total: 1
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/robodock-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.robodock.tech/
- group: operate
  title: ''
  type: Support
  url: https://www.robodock.tech/contact-us
created: '2026-07-17'
description: RoboDock is an autonomous robotics company (Y Combinator W2026) building the robotics layer that powers autonomous EV and AV depots, starting with charging and inspections. Its robots automate depot operations for electric and autonomous vehicle fleets, handling vision-guided plug insertion with verified connection, automated post-trip vehicle inspection, and closed-loop learning that improves efficiency with each charge event. The company targets live EV and AV depots, ports, and logistics yards where charging and core depot operations are still performed manually multiple times per day across mixed fleets. RoboDock is a hardware and robotics business rather than an API provider; as of this profile it publishes no public developer API, SDK, or technical documentation. Founded by Zinny Weli (CEO, ex-Zipline and Amazon robotics) and Celine Wang (CTO, ex-Plus autonomous systems).
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/robodock.png
layout: provider
modified: '2026-07-21'
name: RoboDock
nav: Providers
network: true
overview: 'RoboDock is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Robotics, Autonomous Vehicles, EV Charging, and Fleet Automation.


  RoboDock''s developer surface includes support and 2 more developer resources.'
random_paper: 11
score:
  band: minimal
  composite: 4.3
  coverage:
    artifact_dirs: 2
    catalog_gap: 88.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 4.8
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 4.3
  regulatory:
    applies: true
    matched_via: tags
    regime: Energy & Utilities
    regime_id: energy_utilities
    score: 8.1
  schema_version: 0.18.0
  scored_at: '2026-09-02'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/robodock/refs/heads/main/screenshots/robodock-2026-09-02T154010.png
security:
- kind: domain-security
  name: Robodock Domain Security
  slug: robodock-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: robodock
tags:
- Company
- Robotics
- Autonomous Vehicles
- EV Charging
- Fleet Automation
- Depot Operations
- Logistics Automation
- Vehicle Inspection
website: https://www.robodock.tech/
---
