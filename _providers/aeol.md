---
api_count: 0
artifact_total: 1
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/aeol-domain-security.yml
- group: build
  title: ''
  type: Packages
  url: packages/aeol-packages.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/aeol-conformance.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/aeol-llms.txt
- group: company
  title: ''
  type: Website
  url: https://www.aeolkorea.co.kr/
- group: company
  title: ''
  type: Crunchbase
  url: https://www.crunchbase.com/organization/aeol
- group: other
  title: ''
  type: SecondaryMarket
  url: https://equityzen.com/company/aeol/
coverage:
  checked: '2026-09-10'
  detail: AEOL KOREA is a Seongnam hardware manufacturer that sells MOF desiccant rotors, hybrid dehumidifiers, heat-recovery ventilation units and the CarbonSorV CO2-capture wheel, and its only web property is a Korean-language Cafe24 brochure site with no developer, docs, portal or integration link; every OpenAPI, GraphQL, MCP, agent-card, apis.json and .well-known path probed on aeolkorea.co.kr and www.aeolkorea.co.kr returns the same ~780-byte Cafe24 "CUPID" JavaScript cookie interstitial - including a negative-control path that cannot exist, which proves the origin is a catch-all and that none of those 200s is a served document - while no api./docs./developer./iot. subdomain resolves, no GitHub organization exists under aeol, aeolkorea or aeol-korea, and npm, PyPI, RubyGems, crates.io, Packagist and NuGet return zero first-party packages.
  evidence:
  - status: 200
    url: https://www.aeolkorea.co.kr/
  - status: 200
    url: https://www.aeolkorea.co.kr/openapi.json
  - status: 200
    url: https://www.aeolkorea.co.kr/.well-known/agent-card.json
  - status: 200
    url: https://www.aeolkorea.co.kr/.well-known/aeol-negative-control-7f3ab91c.json
  - status: 404
    url: https://api.github.com/orgs/aeolkorea
  - status: 404
    url: https://pypi.org/pypi/aeol/json
  reason: not-a-software-company
  state: none
created: '2026-09-10'
description: 'AEOL (AEOL KOREA Co., Ltd. / 주식회사 에이올코리아) is a South Korean advanced-materials and climate-technology manufacturer founded in February 2018 out of the Korea University Campus Town programme and headquartered in Seongnam, Gyeonggi Province. The company holds a twenty-year exclusive licence from the Korea Research Institute of Chemical Technology to manufacture and sell Metal-Organic Framework (MOF) materials, and was the first Korean firm to commercialise MOF production at scale. It turns that porous-adsorbent chemistry into physical equipment: MOF desiccant rotors and hybrid dehumidifiers that regenerate at low temperature instead of using refrigerant compression, all-in-one units combining heat-recovery ventilation with UV-LED and HEPA air purification and auxiliary cooling, harmful-gas and odour adsorption products such as the Red Dot-awarded Mofresh Mini, and the CarbonSorV rotary wheel for continuous CO2 capture shown at CES 2025. AEOL won a CES 2024 Innovation Award and
  the FIX 2024 Grand Innovation Award, has raised roughly USD 10-23 million from investors including KU Startup, BlissVine Ventures, JCGI, KNET Investment Partners and NH Venture Investment, and sells through appliance-maker R&D partnerships and distribution agreements in North America and New Zealand. AEOL sells hardware and materials, not software: it operates a single Korean-language Cafe24-hosted corporate site with no developer section, publishes no API documentation, SDK, webhook or machine-readable API contract of any kind, and maintains no public code repositories or package-registry releases.'
layout: provider
modified: '2026-09-10'
name: AEOL
nav: Providers
network: true
overview: AEOL is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Advanced Materials, Metal-Organic Frameworks, Air Purification, and Ventilation.
random_paper: 18
security:
- kind: domain-security
  name: Aeol Domain Security
  slug: aeol-domain-security
  summary_line: TLSv1.2
slug: aeol
tags:
- Company
- Advanced Materials
- Metal-Organic Frameworks
- Air Purification
- Ventilation
- Dehumidification
- Carbon Capture
- HVAC
- Manufacturing
- South Korea
website: https://www.aeolkorea.co.kr/
---
