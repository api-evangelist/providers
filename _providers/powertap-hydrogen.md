---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - security
  trial: false
  try_now: false
api_count: 0
artifact_total: 1
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/powertap-hydrogen-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.powertapfuels.com/
- group: company
  title: ''
  type: About
  url: https://www.powertapfuels.com/company-overview.php
- group: other
  title: ''
  type: Technology
  url: https://www.powertapfuels.com/powertap.php
- group: operate
  title: ''
  type: Contact
  url: https://www.powertapfuels.com/contact.php
- group: company
  title: ''
  type: InvestorRelations
  url: https://powertapcapital.com/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/powertap-hydrogen-fueling-corp
- group: other
  title: ''
  type: SecondaryMarket
  url: https://www.hiive.com/securities/powertap-hydrogen-stock
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/powertap-hydrogen-llms.txt
coverage:
  checked: '2026-08-26'
  detail: PowerTap builds physical on-site hydrogen production and dispensing stations; its two corporate sites are a static PHP brochure and a WordPress investor site with no developer, API or documentation section, and every openapi/swagger/graphql/llms.txt/.well-known probe on both hosts returned a genuine 404.
  evidence:
  - status: 404
    url: https://www.powertapfuels.com/openapi.json
  - status: 404
    url: https://www.powertapfuels.com/.well-known/agent-card.json
  - status: 404
    url: https://powertapcapital.com/openapi.json
  - status: 404
    url: https://powertapcapital.com/llms.txt
  - status: 200
    url: https://powertapcapital.com/wp-json/
  - status: 200
    url: https://www.powertapfuels.com/
  reason: not-a-software-company
  state: none
created: '2026-08-26'
description: 'PowerTap Hydrogen Fueling Corp. is an Aliso Viejo, California hydrogen fueling technology company founded in 2020 and operated as a wholly owned subsidiary of the publicly traded PowerTap Hydrogen Capital Corp. (NEO: MOVE, OTC: MOTNF, FWB: 2K6B). PowerTap designs and deploys distributed, on-site "blue hydrogen" production and dispensing stations built on a patented small-scale steam methane reforming (SMR) platform with embedded carbon capture, converting natural gas and municipal water into high-purity hydrogen at the point of use rather than trucking it in. The modular station design is marketed as deployable in weeks instead of months, and the company positions it for heavy-duty trucking and light-vehicle refueling as well as baseload power for data centers. PowerTap technology-based stations operate at private enterprise sites and at a public station near LAX, with additional deployments cited in California, Texas, Massachusetts and Maryland. The company publishes no developer
  program, no API, and no machine-readable contract of any kind; it is profiled here as an energy-infrastructure company, not an API provider.'
image: https://www.powertapfuels.com/img/logo.png
layout: provider
modified: '2026-08-26'
name: PowerTap Hydrogen
nav: Providers
network: true
overview: PowerTap Hydrogen is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Energy, Hydrogen, Clean Energy, and Fueling Infrastructure.
random_paper: 6
screenshot: https://raw.githubusercontent.com/api-evangelist/powertap-hydrogen/refs/heads/main/screenshots/powertap-hydrogen-2026-09-02T151846.png
security:
- kind: domain-security
  name: Powertap Hydrogen Domain Security
  slug: powertap-hydrogen-domain-security
  summary_line: TLSv1.2
slug: powertap-hydrogen
tags:
- Company
- Energy
- Hydrogen
- Clean Energy
- Fueling Infrastructure
- Transportation
- Carbon Capture
- Heavy Duty Trucking
website: https://www.powertapfuels.com/
---
