---
api_count: 0
artifact_total: 1
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/vita-therapeutics-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.vitatx.com/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/vita-therapeutics
coverage:
  checked: '2026-09-04'
  detail: 'Vita Therapeutics is a clinical-stage iPSC cell-therapy developer whose product is a biologic, not software: there is no developer program, no GitHub organization, no package on any registry, and its own corporate site at www.vitatx.com is currently unpublished and returns a Webflow 404 on every path, while the apex vitatx.com fails the TLS handshake outright.'
  evidence:
  - status: 404
    url: https://www.vitatx.com/
  - status: 404
    url: https://www.vitatx.com/.well-known/agent-card.json
  - status: 404
    url: https://www.vitatx.com/openapi.json
  - status: 404
    url: https://www.vitatx.com/llms.txt
  - status: 0
    url: https://vitatx.com/
  reason: not-a-software-company
  state: none
created: '2026-09-04'
description: 'Vita Therapeutics is a Baltimore, Maryland cell engineering company, spun out of Johns Hopkins University in 2019 and formally founded in 2020, that develops induced pluripotent stem cell (iPSC) derived cellular therapies for neuromuscular disease and solid tumors. Its programs pair an autologous approach with an allogeneic, universal hypoimmunogenic approach, and include VTA-100 and VTA-110 for limb-girdle muscular dystrophy and related muscular dystrophies such as FSHD. The company raised a $31M Series B led by Cambrian BioPharma and Solve FSHD and operates from the University of Maryland BioPark. It is a clinical-stage biotechnology company: it sells no software, runs no developer program, and publishes no public API, SDK, webhook or machine-readable contract of any kind.'
layout: provider
modified: '2026-09-04'
name: Vita Therapeutics
nav: Providers
network: true
overview: Vita Therapeutics is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Biotechnology, Cell Therapy, Life Sciences, and Health.
random_paper: 14
security:
- kind: domain-security
  name: Vita Therapeutics Domain Security
  slug: vita-therapeutics-domain-security
  summary_line: TLSv1.3 · DMARC
slug: vita-therapeutics
tags:
- Company
- Biotechnology
- Cell Therapy
- Life Sciences
- Health
- Pharmaceuticals
- Research
website: https://www.vitatx.com/
---
