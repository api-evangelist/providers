---
access_model:
  confidence: low
  label: Requires approval
  onboarding: approval
  pricing: unknown
  public: false
  source:
  - plans
  - security
  trial: false
  try_now: false
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
screenshot: https://raw.githubusercontent.com/api-evangelist/spartan-radar/refs/heads/main/screenshots/spartan-radar-2026-09-02T160338.png
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
