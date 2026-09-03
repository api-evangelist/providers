---
access_model:
  confidence: low
  label: Requires approval
  onboarding: approval
  pricing: unknown
  public: false
  source:
  - plans
  - rate-limits
  - security
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
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 2.5
  scored_at: '2026-09-03'
api_count: 0
artifact_total: 3
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/lumotive-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://lumotive.com/
- group: company
  title: ''
  type: Blog
  url: https://lumotive.com/news/
- group: company
  title: ''
  type: BlogRSS
  url: https://lumotive.com/feed/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://lumotive.com/privacy-policy/
- group: operate
  title: ''
  type: Support
  url: https://lumotive.com/contact/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/lumotive
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/lumotive-llms.txt
- group: commercial
  title: ''
  type: Plans
  url: plans/lumotive-plans-pricing.yml
coverage:
  checked: '2026-08-25'
  detail: Lumotive markets an "Open Lidar API" for software-defined lidar, but its own announcement says the API "and its supporting hardware platform are available now to selected partners by contacting Lumotive" — the C/C++ control libraries and Python bindings ship only inside the LCM Evaluation Kit, and lumotive.com serves no developer, docs or API-reference page at all (none appears in its own page sitemap).
  evidence:
  - status: 200
    url: https://lumotive.com/press-releases/lumotive-introduces-open-lidar-api-to-accelerate-market-adoption-of-software-defined-solid-state-lidar-2-0-solutions/
  - status: 200
    url: https://lumotive.com/products/lek/
  - status: 404
    url: https://lumotive.com/developers/
  - status: 404
    url: https://lumotive.com/docs/
  - status: 404
    url: https://lumotive.com/openapi.json
  - status: 404
    url: https://lumotive.com/.well-known/agent-card.json
  reason: sales-gate
  state: gated
created: '2026-08-25'
description: 'Lumotive is a Seattle-based semiconductor company building programmable optics on its patented Light Control Metasurface (LCM) technology — solid-state, software-defined beam steering implemented in a standard CMOS process with no moving parts. Its products include the LM10 and LX10 LCM beam-steering chips, the LCM Evaluation Kit (LEK), the M30 iToF and NM120 3D-sensing development kits, and the M30/TX10 reference designs, applied to industrial automation, intelligent traffic systems, automotive ADAS and autonomy, defense, and optical circuit switching for AI data centers. Lumotive publishes an "Open Lidar API" — a real-time control interface for software-defined Lidar 2.0 hardware covering region-of-interest scanning, frame rate, resolution and range, plus a common point-cloud format — and ships C/C++ LCM control libraries with Python bindings alongside its evaluation kits. That interface is an embedded hardware-control API, not a public web API: no developer portal, documentation
  site, machine-readable specification, or self-service sign-up is published, and access is granted to selected partners through the Technology Access Program by contacting the company.'
image: https://lumotive.com/wp-content/uploads/2024/10/LM10-chip-1024x787.png
layout: provider
modified: '2026-08-25'
name: Lumotive
nav: Providers
network: true
overview: 'Lumotive is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Semiconductors, Photonics, LiDAR, and 3D Sensing.


  Lumotive''s developer surface includes engineering blog, support, and 7 more developer resources.'
plans:
- name: Lumotive Plans Pricing
  plan_count: 0
  slug: lumotive-plans-pricing
random_paper: 3
rate_limits:
- limit_count: 0
  name: Lumotive Rate Limits
  slug: lumotive-rate-limits
score:
  band: minimal
  composite: 9.6
  coverage:
    artifact_dirs: 8
    catalog_gap: 88.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 10.5
    commercial_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 7.1
    discoverability: 57.4
    governance: 0.0
    operational_transparency: 2.6
  previous_composite: 9.6
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/lumotive/refs/heads/main/screenshots/lumotive-2026-09-02T150336.png
security:
- kind: domain-security
  name: Lumotive Domain Security
  slug: lumotive-domain-security
  summary_line: TLSv1.3 · DMARC
slug: lumotive
tags:
- Company
- Semiconductors
- Photonics
- LiDAR
- 3D Sensing
- Programmable Optics
- Beam Steering
- Robotics
- Automotive
- Industrial Automation
- Defense
- Optical Networking
- Hardware
website: https://lumotive.com/
---
