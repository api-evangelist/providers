---
api_count: 0
artifact_total: 1
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/advanced-ionics-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://advanced-ionics.com/
coverage:
  checked: '2026-09-07'
  detail: Advanced Ionics manufactures Symbion water-vapor electrolyzers as physical industrial hardware, and certificate-transparency logs show only the apex domain advanced-ionics.com has ever been issued a certificate — no api, docs, developer or portal host has ever existed — with no GitHub organization and no package in any public registry to accompany one.
  evidence:
  - status: 200
    url: https://crt.sh/?q=%25.advanced-ionics.com&output=json
  - status: 404
    url: https://api.github.com/orgs/advanced-ionics
  - status: 202
    url: https://advanced-ionics.com/.well-known/api-catalog
  reason: not-a-software-company
  state: none
created: '2026-09-07'
description: Advanced Ionics is a Milwaukee, Wisconsin based clean-energy hardware company developing the Symbion water-vapor electrolyzer, a green hydrogen production technology that uses process and waste heat together with low-cost renewable or nuclear electricity to cut the energy needed per kilogram of hydrogen to roughly 35 kWh, well below the 50-plus kWh required by conventional commercial electrolyzers. Founded in 2017 and relocated to Milwaukee in 2018, the company targets decarbonization of heavy industry — steel, ammonia, refining and other hydrogen-intensive sectors — and has run pilot and demonstration projects with Shell through its GameChanger program and with the Entrepreneurs Fund of the Repsol Foundation, and signed a collaboration MOU with ACWA Power. Advanced Ionics manufactures electrolyzer hardware; it does not operate a public developer program, and no public API, SDK, or machine-readable specification was found.
layout: provider
modified: '2026-09-07'
name: Advanced Ionics
nav: Providers
network: true
overview: Advanced Ionics is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Energy, Hydrogen, Clean Energy, and Electrolyzer.
random_paper: 0
security:
- kind: domain-security
  name: Advanced Ionics Domain Security
  slug: advanced-ionics-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
slug: advanced-ionics
tags:
- Company
- Energy
- Hydrogen
- Clean Energy
- Electrolyzer
- Manufacturing
- Industrial
- Hardware
- Climate Tech
website: https://advanced-ionics.com/
---
