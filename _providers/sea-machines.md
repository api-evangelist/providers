---
access_model:
  confidence: medium
  label: Enterprise
  onboarding: unknown
  pricing: enterprise
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
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 15.5
  scored_at: '2026-09-04'
api_count: 1
apis:
- baseURL: https://sea-machines.com
  baseurl_source: spec
  description: Partner-gated interface announced September 2025 that delivers real-time SM300 vessel telemetry and data feeds (position, heading, mechanical and navigational state) to external command-and-control an
  name: SMLink Streaming-API
  slug: smlink-streaming-api
- baseURL: https://sea-machines.com
  baseurl_source: spec
  description: Partner-gated interface announced September 2025 that grants select partners the ability to command SM300 autonomy functions directly from third-party mission software. Supported on the SM300-SP and S
  name: SMLink Control-API
  slug: smlink-control-api
- description: Industrial-grade vessel intelligence system providing operator-in-the-loop autonomous command and control, multi-waypoint missions, search and survey, patrol and surveillance, and remote command. Avai
  name: SM300 Autonomous Command and Control
  slug: sm300-autonomous-control
- description: AI-ris (Artificial Intelligence Recognition and Identification System) ingests 4K imagery and processes it on-device with embedded AI/ML to detect, track, classify, and geolocate vessel traffic and ob
  name: AI-ris Computer Vision
  slug: ai-ris-perception
- description: 'Browser-based fleet monitoring and analysis platform for SM300-equipped vessels, offering real-time and historical telemetry at 5-second intervals, mechanical and navigational data (radar, ARPA, AIS, '
  name: FleetViewer
  slug: fleetviewer
artifact_total: 11
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Sea Machines SMLink API
  slug: open-sea-machines
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/sea-machines-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/sea-machines
- group: company
  title: ''
  type: Website
  url: https://sea-machines.com/
- group: docs
  title: ''
  type: Documentation
  url: https://sea-machines.com/sea-machines-launches-marine-autonomy-apis-for-third-party-c2-systems/
- group: commercial
  title: ''
  type: Plans
  url: plans/sea-machines-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/sea-machines-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/sea-machines-finops.yml
- group: company
  title: ''
  type: Blog
  url: https://sea-machines.com/category/blog/
created: '2026-06-20'
description: Sea Machines Robotics builds autonomous command-and-control systems (SM300-SP, SM300-NG) and computer-vision perception (AI-ris) for commercial and defense marine vessels. In September 2025 it announced the SMLink Streaming-API and SMLink Control-API, partner-gated interfaces that stream real-time vessel telemetry to external systems and let approved third parties command SM300 autonomy functions from their own mission software. These interfaces are embedded, vessel-side product features, not a self-service public developer platform; access is arranged through Sea Machines sales.
finops:
- name: Sea Machines Finops
  service_category: Marine Autonomy and Robotics
  slug: sea-machines-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/sea-machines.png
layout: provider
modified: '2026-06-20'
name: Sea Machines Robotics
nav: Providers
network: true
overview: 'Sea Machines Robotics publishes 2 APIs on the [APIs.io](https://apis.io/) network: SMLink Streaming-API and SMLink Control-API. Tagged areas include Marine, Autonomy, Robotics, Maritime, and Computer-Vision.


  Sea Machines Robotics'' developer surface includes documentation, engineering blog, and 6 more developer resources.'
plans:
- name: Sea Machines Plans Pricing
  plan_count: 1
  slug: sea-machines-plans-pricing
random_paper: 1
rate_limits:
- limit_count: 2
  name: Sea Machines Rate Limits
  slug: sea-machines-rate-limits
score:
  band: emerging
  composite: 23.8
  coverage:
    artifact_dirs: 8
    catalog_earned: 51.0
    catalog_earned_first_party: 0.0
    catalog_gap: 64.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 28.9
    commercial_clarity: 28.9
    contract_governance: 0.0
    contract_quality: 27.9
    developer_ergonomics: 11.9
    discoverability: 59.3
    governance: 0.0
    operational_transparency: 21.1
  previous_composite: 23.8
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/sea-machines/refs/heads/main/screenshots/sea-machines-2026-06-20T193612.png
security:
- kind: domain-security
  name: Sea Machines Domain Security
  slug: sea-machines-domain-security
  summary_line: TLSv1.3 · DMARC
slug: sea-machines
tags:
- Marine
- Autonomy
- Robotics
- Maritime
- Computer-Vision
- Telemetry
website: https://sea-machines.com/
---
