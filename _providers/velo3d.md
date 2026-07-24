---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - plans
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_skills: false
    agentic_access: false
    asyncapi_events: false
    auth_clarity: false
    consent_identity: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: true
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.1
  score: 24.0
  scored_at: '2026-07-23'
api_count: 4
apis:
- description: The Sapphire family (Sapphire, Sapphire XC, Sapphire 1MZ) of laser powder bed fusion metal 3D printers, using multiple 1-kilowatt lasers to produce large-format support-free parts. Product feature - n
  name: Velo3D Sapphire Printers
  slug: sapphire-printers
- description: Flow print-preparation software with native CAD import for designing and preparing support-free builds, including Flow Developer for engineers to tune process parameters within the Sapphire ecosystem.
  name: Velo3D Flow Print Preparation
  slug: flow-print-prep
- description: The Assure quality-assurance and control system, a real-time dashboard using multi-sensor physics-based detection to validate powder health, chamber atmosphere, optics, and per-layer melt-pool data du
  name: Velo3D Assure Quality Assurance
  slug: assure-qa
- description: The Intelligent Fusion manufacturing process that integrates the Sapphire printers, Flow, and Assure into an end-to-end metal additive-manufacturing workflow. Process technology - no documented public
  name: Velo3D Intelligent Fusion
  slug: intelligent-fusion
artifact_total: 9
collections:
- collection_type: open
  name: Velo3D
  slug: open-velo3d
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/velo3d-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/velo3d
- group: company
  title: ''
  type: Website
  url: https://velo3d.com/
- group: docs
  title: ''
  type: Documentation
  url: https://support.velo3d.com/
- group: commercial
  title: ''
  type: Plans
  url: plans/velo3d-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/velo3d-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/velo3d-finops.yml
- group: company
  title: ''
  type: Blog
  url: https://velo3d.com/blogs
created: '2026-06-20'
description: Velo3D builds metal additive-manufacturing systems for aerospace, defense, and energy - the Sapphire family of laser powder bed fusion printers, Flow print-preparation software, the Assure quality-assurance and control system, all powered by the Intelligent Fusion manufacturing process. These are enterprise hardware and software products; Velo3D does not publish a documented public developer API.
finops:
- name: Velo3D Finops
  service_category: Manufacturing
  slug: velo3d-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/velo3d.png
layout: provider
modified: '2026-06-20'
name: Velo3D
nav: Providers
network: true
overview: 'Velo3D publishes 4 APIs on the [APIs.io](https://apis.io/) network, including Sapphire Printers, Flow Print Preparation, Assure Quality Assurance, and 1 more. Tagged areas include Additive Manufacturing, Metal 3D Printing, Laser Powder Bed Fusion, Aerospace, and Defense.


  Velo3D''s developer surface includes documentation, engineering blog, and 6 more developer resources.'
plans:
- name: Velo3D Plans Pricing
  plan_count: 2
  slug: velo3d-plans-pricing
random_paper: 28
rate_limits:
- limit_count: 0
  name: Velo3D Rate Limits
  slug: velo3d-rate-limits
score:
  band: emerging
  composite: 24.1
  delta: 0.0
  facets:
    commercial_clarity: 28.9
    contract_quality: 37.7
    developer_ergonomics: 10.9
    discoverability: 67.5
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 24.1
  schema_version: 0.5
  scored_at: '2026-07-23'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/velo3d/refs/heads/main/screenshots/velo3d-2026-06-20T200904.png
security:
- kind: domain-security
  name: Velo3D Domain Security
  slug: velo3d-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: velo3d
tags:
- Additive Manufacturing
- Metal 3D Printing
- Laser Powder Bed Fusion
- Aerospace
- Defense
website: https://velo3d.com/
---
