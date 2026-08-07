---
agent_readiness:
  band: human-only
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
    rate_limit_signal: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 0.0
  scored_at: '2026-08-06'
api_count: 0
artifact_total: 1
common:
- group: company
  title: ''
  type: Website
  url: https://teradar.com/
- group: other
  title: ''
  type: Products
  url: https://teradar.com/products/
- group: company
  title: ''
  type: About
  url: https://teradar.com/company/
- group: operate
  title: ''
  type: ContactUs
  url: https://teradar.com/contact-us/
- group: company
  title: ''
  type: Careers
  url: https://teradar.com/careers/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://teradar.com/privacy-policy/
- group: other
  title: ''
  type: Media
  url: https://teradar.com/media/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/teradar
- group: learn
  title: ''
  type: YouTube
  url: https://www.youtube.com/channel/UChtcEwZbyk1GWgO2cWNf2ew
- group: other
  title: ''
  type: Sitemap
  url: https://teradar.com/sitemap_index.xml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/teradar-llms.txt
- group: auth
  title: ''
  type: DomainSecurity
  url: security/teradar-domain-security.yml
- group: company
  title: ''
  type: InvestorProfile
  url: https://forgeglobal.com/teradar_stock/
coverage:
  checked: '2026-08-05'
  detail: Teradar sells terahertz sensor silicon and modules to automakers and defense primes, not software — the whole public site is a nine-page WordPress marketing brochure whose only machine-readable surfaces are a Yoast-generated llms.txt and the CMS's own /wp-json/ endpoint, and api./docs./developer. teradar.com do not resolve in DNS.
  evidence:
  - status: 200
    url: https://teradar.com/llms.txt
  - status: 404
    url: https://teradar.com/developers
  - status: 404
    url: https://teradar.com/openapi.json
  - status: 404
    url: https://teradar.com/.well-known/agent-card.json
  - status: 0
    url: https://api.teradar.com/
  reason: not-a-software-company
  state: none
created: '2026-08-05'
description: 'Teradar is a Boston, Massachusetts semiconductor and sensing company founded in 2020 by Matthew Carey, Gregory Charvat and Nicholas Saiz that is commercializing terahertz-band vision sensors for vehicles, defense and security screening. Its Modular Terahertz Engine (MTE) is an all-solid-state chip architecture built from proprietary transmit (TX), receive (RX) and Teracore processing silicon, delivering 0.13-degree native angular resolution at 300+ meters in day, night, rain, fog and snow, positioned to sit alongside cameras and to displace radar and lidar in SAE L1-L5 driver assistance and autonomy programs. The company emerged from stealth in late 2025 with a $150M Series B led by VXI Capital with Ibex Investors, Capricorn Investment Group, The Engine Ventures and Lockheed Martin Ventures, and is working with global OEMs and Tier-One suppliers toward a 2028 model-year launch. Teradar is a hardware and silicon company: it publishes a marketing site and product specification
  sheets, but no public developer program, API, SDK, or machine-readable interface contract.'
image: https://teradar.com/wp-content/themes/teradar-theme/assets/images/teradar-logo-grey.svg
layout: provider
modified: '2026-08-05'
name: Teradar
nav: Providers
network: true
overview: 'Teradar is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Sensors, Semiconductors, Terahertz, and Automotive.


  Teradar''s developer surface includes YouTube channel and 12 more developer resources.'
random_paper: 61
score:
  band: minimal
  composite: 9.0
  facets:
    commercial_clarity: 10.5
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 0.0
  schema_version: 0.9.1
  scored_at: '2026-08-06'
security:
- kind: domain-security
  name: Teradar Domain Security
  slug: teradar-domain-security
  summary_line: TLSv1.3 · DMARC
slug: teradar
tags:
- Company
- Sensors
- Semiconductors
- Terahertz
- Automotive
- Autonomous Vehicles
- Radar
- Lidar
- Perception
- Defense
- Hardware
website: https://teradar.com/
---
