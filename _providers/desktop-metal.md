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
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 19.4
  scored_at: '2026-08-11'
api_count: 3
apis:
- description: 'Live Platform provisions and manages Desktop Metal AM systems and users, and Live Monitor surfaces real-time fleet, printer, and furnace data (job/event status, time reporting, consumable usage, OEE) '
  name: Printer Fleet & Live Suite
  slug: printer-fleet-live-suite
- description: Build preparation and slicing software for Desktop Metal printers. The legacy Fabricate and Fabricate MFG desktop applications have been replaced and upgraded by Live Studio (cloud build preparation f
  name: Fabricate Software
  slug: fabricate-software
- description: Qualified metal, polymer, composite, ceramic, sand, and wood material portfolio for Desktop Metal's binder jet, Bound Metal Deposition, and DLP/polymer systems, with associated material parameters and
  name: Materials
  slug: materials
artifact_total: 8
collections:
- collection_type: open
  name: Desktop Metal
  slug: open-desktop-metal
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/desktop-metal-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/desktop-metal
- group: company
  title: ''
  type: Website
  url: https://www.desktopmetal.com
- group: docs
  title: ''
  type: Documentation
  url: https://www.desktopmetal.com/products/live-suite
- group: commercial
  title: ''
  type: Plans
  url: plans/desktop-metal-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/desktop-metal-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/desktop-metal-finops.yml
created: '2026-06-20'
description: Desktop Metal designs and manufactures additive manufacturing (3D printing) hardware and software for metal and polymer parts, including binder jet and Bound Metal Deposition printers, sintering furnaces, materials, and the cloud/desktop Live Suite software (Live Platform, Live Studio, Live Build, Live Sinter, Live Monitor) that replaced the legacy Fabricate applications. As of April 2025 Desktop Metal is a subsidiary of Nano Dimension. No public or partner developer API is documented; the surfaces below are product features rather than published HTTP APIs.
finops:
- name: Desktop Metal Finops
  service_category: Manufacturing
  slug: desktop-metal-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/desktop-metal.png
layout: provider
modified: '2026-06-20'
name: Desktop Metal
nav: Providers
network: true
overview: 'Desktop Metal publishes 3 APIs on the [APIs.io](https://apis.io/) network: Printer Fleet & Live Suite, Fabricate Software, and Materials. Tagged areas include 3D Printing, Additive Manufacturing, Metal, Hardware, and Manufacturing Software.


  Desktop Metal''s developer surface includes documentation and 6 more developer resources.'
plans:
- name: Desktop Metal Plans Pricing
  plan_count: 1
  slug: desktop-metal-plans-pricing
random_paper: 62
rate_limits:
- limit_count: 0
  name: Desktop Metal Rate Limits
  slug: desktop-metal-rate-limits
score:
  band: emerging
  composite: 21.7
  delta: -0.3
  facets:
    commercial_clarity: 28.9
    contract_quality: 30.6
    developer_ergonomics: 8.7
    discoverability: 64.8
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 22.0
  schema_version: 0.11.0
  scored_at: '2026-08-11'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/desktop-metal/refs/heads/main/screenshots/desktop-metal-2026-06-20T175940.png
security:
- kind: domain-security
  name: Desktop Metal Domain Security
  slug: desktop-metal-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: desktop-metal
tags:
- 3D Printing
- Additive Manufacturing
- Metal
- Hardware
- Manufacturing Software
website: https://www.desktopmetal.com
---
