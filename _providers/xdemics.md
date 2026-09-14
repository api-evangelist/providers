---
api_count: 0
artifact_total: 1
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/xdemics-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.xdemics.com/
- group: company
  title: ''
  type: Blog
  url: https://www.xdemics.com/news
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.xdemics.com/privacy-policy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.xdemics.com/terms-of-use
- group: company
  title: ''
  type: About
  url: https://www.xdemics.com/about-us
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/xdemics-corporation
coverage:
  checked: '2026-09-04'
  detail: XDemics sells physical HDCR cultureware and bioreactors — its entire nine-page Webflow site is product, news, team and protocol pages with no developer, API or integrations section, no api/developer/docs subdomain resolves in DNS, and every OpenAPI and .well-known discovery path on xdemics.com returns the Webflow 404 or the fixed "Invalid .well-known request" body.
  evidence:
  - status: 404
    url: https://www.xdemics.com/openapi.json
  - status: 404
    url: https://www.xdemics.com/llms.txt
  - status: 404
    url: https://www.xdemics.com/.well-known/api-catalog
  - status: 404
    url: https://www.xdemics.com/.well-known/agent-card.json
  - status: 200
    url: https://www.xdemics.com/sitemap.xml
  - status: 200
    url: https://www.xdemics.com/about-us
  reason: not-a-software-company
  state: none
created: '2026-09-04'
description: 'XDemics Corporation is a Caltech and City of Hope spin-out in San Rafael, California that develops High Density Cell Respiration (HDCR) cell-culture hardware for biomedical research and biomanufacturing. Its gas-permeable, tissue-mimicking Expansify cultureware — a 24-well plate and a single-well plate — and its Profusion bioreactor line under development let mammalian cells reach 10-100X higher densities than conventional flasks and plates, targeting CAR-T and cell therapy, viral vector production, stem cell and regenerative medicine, drug screening, and biologics workflows. The company sells physical laboratory consumables and instrumentation, distributed through VWR, and its biological testing laboratories sit at the Buck Institute in Novato. It is a hardware and life-science company, not a software company: it publishes no public API, SDK, developer portal, or machine-readable specification of any kind.'
image: https://cdn.prod.website-files.com/67d1078fe4c4695ced4cb783/67ed9a56129717ba3602ecdb_Open%20Graph.jpg
layout: provider
modified: '2026-09-04'
name: XDemics
nav: Providers
network: true
overview: 'XDemics is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Biotechnology, Life Sciences, Cell Culture, Bioprocessing, and Cell and Gene Therapy.


  XDemics'' developer surface includes engineering blog and 6 more developer resources.'
random_paper: 14
security:
- kind: domain-security
  name: Xdemics Domain Security
  slug: xdemics-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: xdemics
tags:
- Biotechnology
- Life Sciences
- Cell Culture
- Bioprocessing
- Cell and Gene Therapy
- Laboratory Equipment
- Manufacturing
- Hardware
- Company
website: https://www.xdemics.com/
---
