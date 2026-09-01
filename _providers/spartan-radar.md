---
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
  scored_at: '2026-09-01'
api_count: 0
artifact_total: 2
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/spartan-radar-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.spartanradar.com/
- group: company
  title: ''
  type: About
  url: https://www.spartanradar.com/about
- group: operate
  title: ''
  type: Contact
  url: https://www.spartanradar.com/contact
- group: company
  title: ''
  type: News
  url: https://www.spartanradar.com/about/news-media
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.spartanradar.com/privacy-policy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.spartanradar.com/terms-of-use
- group: commercial
  title: ''
  type: Plans
  url: plans/spartan-radar-plans-pricing.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/spartan-radar-llms.txt
coverage:
  checked: '2026-08-28'
  detail: Spartan Radar sells embedded radar perception software (Clarify) and a heavy-vehicle collision-avoidance system (Hoplo) to commercial-vehicle OEMs and fleets; its entire public surface is a seven-page Webflow marketing site whose only call to action is a contact form, and api./docs./developer.spartanradar.com do not resolve in DNS at all.
  evidence:
  - status: 200
    url: https://www.spartanradar.com/
  - status: 200
    url: https://www.spartanradar.com/software-solution
  - status: 404
    url: https://spartanradar.com/openapi.json
  - status: 404
    url: https://www.spartanradar.com/.well-known/agent-card.json
  - status: 404
    url: https://www.spartanradar.com/pricing
  - status: 0
    url: https://api.spartanradar.com/openapi.json
  reason: no-developer-program
  state: none
created: '2026-08-28'
description: Spartan Radar is an automotive radar software and sensing company, now operating as the radar technology brand of Pro-Vision Solutions, LLC following its 2025 acquisition. Its Clarify software applies proprietary digital signal processing and machine-learning perception to existing automotive radar sensors, raising resolution 3-8x on commodity silicon (ARM Cortex, Texas Instruments TDA4VM and AWR, NVIDIA Orin and DRIVE, NXP SAF85xx/SAF86xx) without new hardware, and its Hoplo product is a software-defined collision-avoidance and blind-spot warning system for commercial and heavy vehicles across mining, construction, material handling and logistics. Spartan sells to commercial-vehicle OEMs, Tier 1 suppliers and fleet operators as embedded software and hardware; it publishes no public developer program, API, SDK or machine-readable interface contract.
image: https://cdn.prod.website-files.com/64dd1fb693f80b411c6fb30b/69d3d0d6638a8e4ff84a994b_EndorserBrand_SpartanRadar_PV_Logo.png
layout: provider
modified: '2026-08-28'
name: Spartan Radar
nav: Providers
network: true
overview: 'Spartan Radar is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Automotive, Radar, Sensors, and ADAS.


  Spartan Radar''s developer surface includes product news and 8 more developer resources.'
plans:
- name: Spartan Radar Plans Pricing
  plan_count: 0
  slug: spartan-radar-plans-pricing
random_paper: 5
score:
  band: minimal
  composite: 10.0
  coverage:
    artifact_dirs: 4
    catalog_gap: 88.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 21.1
    commercial_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 57.4
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 10.0
  schema_version: 0.17.2
  scored_at: '2026-09-01'
  trend: flat
security:
- kind: domain-security
  name: Spartan Radar Domain Security
  slug: spartan-radar-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: spartan-radar
tags:
- Company
- Automotive
- Radar
- Sensors
- ADAS
- Autonomous Vehicles
- Perception
- Signal Processing
- Commercial Vehicles
- Embedded Software
- Safety
website: https://www.spartanradar.com/
---
