---
access_model:
  confidence: medium
  label: Paid
  onboarding: unknown
  pricing: paid
  public: false
  source:
  - plans
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
  scored_at: '2026-09-01'
api_count: 0
artifact_total: 17
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/autoliv-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/autoliv
- group: company
  title: ''
  type: Website
  url: https://www.autoliv.com
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/autoliv
- group: other
  title: ''
  type: Suppliers
  url: https://autoliv.biz
created: '2026-03-21'
description: Autoliv is the world's largest automotive safety supplier, designing, manufacturing, and selling airbags, seatbelts, steering wheels, inflators, pyrotechnic actuators, and related safety electronics for vehicle manufacturers worldwide. The company operates in 25 countries with 13 technology centers and serves all major OEMs.
features:
- description: Front, side curtain, knee, pedestrian, and center airbag systems for passenger vehicles, commercial vehicles, and motorcycles.
  name: Airbag Systems
- description: Seatbelt assemblies, webbing, and retractors engineered for crash performance across all vehicle segments.
  name: Seatbelt Systems
- description: Steering wheel systems including foldable designs for autonomous vehicles and advanced driver assistance configurations.
  name: Steering Wheels
- description: Inflators, initiators, pyro safety switches, and pyrotechnic actuators for airbag deployment and battery disconnect applications.
  name: Pyrotechnic Components
- description: Software platform supporting occupant safety simulation, virtual testing, and digital validation of safety systems.
  name: HBM Safety Suite
- description: Seat belt and airbag solutions tailored for trucks, buses, and off-road vehicles.
  name: Commercial Vehicle Safety
finops:
- name: Autoliv Finops
  service_category: Automotive Safety / Tier-1 Supplier
  slug: autoliv-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/autoliv.png
integrations:
- description: EDI and system integrations with OEM enterprise resource planning systems for procurement, logistics, and order management.
  name: Automotive OEM ERP Systems
- description: Supply chain management integration with SAP systems used across Autoliv's global manufacturing network.
  name: SAP Supply Chain
- description: Quality management integrations aligned with the IATF 16949 automotive quality management standard.
  name: IATF 16949 Quality Systems
layout: provider
modified: '2026-07-25'
name: Autoliv
nav: Providers
network: true
overview: Autoliv is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Automotive, Automotive Safety, Airbags, Seatbelts, and Safety Systems.
plans:
- name: Autoliv Plans Pricing
  plan_count: 1
  slug: autoliv-plans-pricing
press:
- date: '2026-05-25'
  title: Annual Report 2025
  url: https://www.autoliv.com/sites/autoliv/files/2026-02/ALV_AR_10-K_2025_Horizontal_Final.pdf
- date: '2026-05-25'
  title: Volvo Cars and Autoliv team up with NVIDIA to develop ...
  url: https://www.volvocars.com/us/media/press-releases/E77B5AFE5726BAD5/
- date: '2026-05-25'
  title: Digitalization & Automation at Autoliv
  url: https://www.autoliv.com/company/digitalization-automation-autoliv
- date: '2026-05-25'
  title: Autoliv to Discontinue Manufacturing Operations in Türkiye
  url: https://www.prnewswire.com/news-releases/autoliv-to-discontinue-manufacturing-operations-in-turkiye-302766735.html
- date: '2026-05-25'
  title: NANGA SYSTEMS' Post
  url: https://www.linkedin.com/posts/nanga-systems_the-recent-press-release-that-autoliv-is-activity-7445439948893184000-nIRn
random_paper: 16
rate_limits:
- limit_count: 1
  name: Autoliv Rate Limits
  slug: autoliv-rate-limits
score:
  band: minimal
  composite: 8.7
  coverage:
    artifact_dirs: 8
    catalog_gap: 81.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 13.2
    commercial_clarity: 13.2
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 7.9
  previous_composite: 8.7
  schema_version: 0.18.0
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/autoliv/refs/heads/main/screenshots/autoliv-2026-06-20T172646.png
security:
- kind: domain-security
  name: Autoliv Domain Security
  slug: autoliv-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: autoliv
tags:
- Automotive
- Automotive Safety
- Airbags
- Seatbelts
- Safety Systems
- Manufacturing
- Fortune 500
use_cases:
- description: Tier-1 supplier integration with automotive OEM procurement and logistics systems for just-in-time delivery of safety components.
  name: OEM Supply Chain Integration
- description: Onboarding new suppliers into Autoliv's global supply base through the supplier portal with document management and compliance workflows.
  name: Supplier Onboarding
- description: Integration of Autoliv safety systems with vehicle telematics and connected car platforms for post-crash notification and safety analytics.
  name: Connected Safety
- description: Virtual occupant safety testing and crash simulation using the HBM Safety Suite to accelerate product development and validation.
  name: Safety Simulation
website: https://www.autoliv.com
---
