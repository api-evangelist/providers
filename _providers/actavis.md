---
api_count: 0
artifact_total: 1
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/actavis-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.actavis.co.id/
coverage:
  checked: '2026-09-13'
  detail: Actavis was absorbed into Teva in August 2016; www.actavis.com now resolves to Teva's 192.115.248.118, which refuses TCP 443 outright (ECONNREFUSED) and never answers HTTP, and actavis.bg redirects to teva.bg — the only reachable Actavis-branded host left is PT Actavis Indonesia's marketing site, which 404s every discovery path.
  evidence:
  - status: 0
    url: https://www.actavis.com/
  - status: 404
    url: https://www.actavis.co.id/.well-known/api-catalog
  - status: 200
    url: https://actavis.bg/
  - status: 404
    url: https://api.github.com/orgs/actavis
  reason: defunct
  state: none
created: '2026-09-13'
description: Actavis is a pharmaceutical manufacturer of generic, branded-generic and over-the-counter medicines that no longer exists as an independent company. Actavis plc renamed itself Allergan plc in June 2015, and on 2 August 2016 Teva Pharmaceutical Industries completed its acquisition of the Actavis Generics business for roughly $40.5 billion. What survives of the name is a product label and a handful of Teva regional affiliates such as PT Actavis Indonesia. The historic corporate domains (actavis.com, actavis.us, actavis.co.uk) are delegated to Teva nameservers and no longer answer HTTP at all, and actavis.bg redirects to teva.bg. Actavis published no developer program, no API, no SDKs and no machine-readable specification; in this industry "API" means Active Pharmaceutical Ingredient, not a software interface.
layout: provider
modified: '2026-09-13'
name: Actavis
nav: Providers
network: true
overview: Actavis is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Pharmaceuticals, Generic Drugs, Healthcare, and Manufacturing.
random_paper: 12
security:
- kind: domain-security
  name: Actavis Domain Security
  slug: actavis-domain-security
  summary_line: TLSv1.3 · DMARC
slug: actavis
tags:
- Company
- Pharmaceuticals
- Generic Drugs
- Healthcare
- Manufacturing
- Acquired
website: https://www.actavis.co.id/
---
