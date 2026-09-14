---
api_count: 0
artifact_total: 1
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/accurateinternational-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://en.bio-accurate.com/
- group: company
  title: ''
  type: Blog
  url: https://en.bio-accurate.com/news/dynamic/
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/accurateinternational-llms.txt
coverage:
  checked: '2026-09-06'
  detail: ACCURATE is a Guangzhou organoid biotech selling culture media, microfluidic chips, detectors and clinical drug-sensitivity testing — its only digital assets (the AOD Tronchip organoid database and a 2024 cancer AI model) are internal R&D tooling with no public interface, and bio-accurate.com has no developer section, no /.well-known/ documents on either host, and no api/db/data/developer subdomain in DNS.
  evidence:
  - status: 200
    url: https://en.bio-accurate.com/
  - status: 404
    url: https://en.bio-accurate.com/.well-known/agent-card.json
  - status: 404
    url: https://en.bio-accurate.com/.well-known/api-catalog
  - status: 404
    url: https://www.bio-accurate.com/.well-known/security.txt
  reason: no-developer-program
  state: none
created: '2026-09-06'
description: 'Accurate International Biotechnology (trading as ACCURATE, 广州创芯国际生物科技有限公司) is a Guangzhou, China biotechnology company founded in 2018 that builds the full industry chain around organoid technology for cancer precision medicine, new drug research and regenerative medicine. Its products are wet-lab reagents, instruments and consumables rather than software: Accuroid organoid culture media, the AccuArray microarray organoid chip, the AOMF microfluidic organoid chip and 3D bioprinter, the AccuLumi high-throughput chemiluminescence detector, and Accuauto automated organoid culture workstations. On top of those it sells services — BUDcare and BUDhealth patient-derived tumor organoid drug-sensitivity testing delivered through Guangzhou Chuangxin Independent Clinical Laboratory, and organoid-model new-drug R&D services for pharma — and reports 32,000+ organoid cultures, 5,000+ tumor organoid models, 200+ clinical collaborators and 100+ filed patents. It holds subsidiaries in Beijing,
  Shanghai and Macau plus a European entity, and has raised Pre-A (2020), Series A (2021), a 100M RMB Pre-B (2022) and a Series B (2024). ACCURATE describes internal digital assets — the AOD Tronchip organoid database launched in 2023 and a cancer "deep-thinking" AI model built in 2024 — but publishes no developer portal, API reference, SDK, CLI, status page or public GitHub organization, and no OpenAPI, AsyncAPI, GraphQL, MCP or A2A agent-card surface was found on any host it operates.'
image: https://en.bio-accurate.com/dist/images/logo.png
layout: provider
modified: '2026-09-06'
name: Accurate International
nav: Providers
network: true
overview: 'Accurate International is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Biotechnology, Life Sciences, Precision Medicine, and Oncology.


  Accurate International''s developer surface includes engineering blog and 3 more developer resources.'
random_paper: 14
security:
- kind: domain-security
  name: Accurateinternational Domain Security
  slug: accurateinternational-domain-security
  summary_line: TLSv1.3 · HSTS
slug: accurateinternational
tags:
- Company
- Biotechnology
- Life Sciences
- Precision Medicine
- Oncology
- Organoids
- Laboratory Instruments
- Clinical Diagnostics
- Drug Discovery
- China
website: https://en.bio-accurate.com/
---
