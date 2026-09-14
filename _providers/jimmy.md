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
  url: security/jimmy-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.jimmy-energy.eu/
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/jimmy-llms.txt
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Jimmy-Energy
- group: company
  title: ''
  type: Blog
  url: https://www.jimmy-energy.eu/actualites
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.jimmy-energy.eu/mentions-legales
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/jimmy-energy/
- group: other
  title: ''
  type: X
  url: https://twitter.com/Jimmy_Energy_
coverage:
  checked: '2026-08-17'
  detail: Jimmy manufactures and operates nuclear high-temperature thermal generators and sells industrial heat on 20-year contracts, so there is nothing to expose as an API — api., docs. and developer.jimmy-energy.eu do not resolve in DNS and the Webflow marketing site 404s on every spec and /.well-known/ path probed.
  evidence:
  - status: 200
    url: https://www.jimmy-energy.eu/
  - status: 404
    url: https://www.jimmy-energy.eu/openapi.json
  - status: 404
    url: https://www.jimmy-energy.eu/.well-known/agent-card.json
  - status: 404
    url: https://www.jimmy-energy.eu/llms.txt
  reason: not-a-software-company
  state: none
created: '2026-08-17'
description: 'Jimmy (Jimmy Energy SAS) is a French nuclear-technology company, founded in 2020 as a spin-off from the CEA, that designs, builds and operates small modular high-temperature reactors it calls thermal generators — helium-cooled HTR units the company describes as bus-sized — to deliver carbon-free process heat directly to industrial sites under secured 20-year supply-and-price contracts. Jimmy is headquartered in Paris with an industrial platform at Le Creusot in Burgundy, targets food, paper, sugar and chemicals producers that currently burn natural gas for process heat, and filed the first SMR creation-authorization request in France for a generator at the Cristanol site in Bazancourt. Jimmy sells heat, not software: it publishes no API, developer portal, SDK or machine-readable specification, and this profile records that measured absence rather than assuming it.'
image: https://cdn.prod.website-files.com/63497bb96fe7a9a8fa88990d/6352bfaf482c556de506e26e_Jimmy-logo.svg
layout: provider
modified: '2026-08-17'
name: Jimmy
nav: Providers
network: true
overview: 'Jimmy is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Climate Tech, Energy, Nuclear, and Small Modular Reactor.


  Jimmy''s developer surface includes engineering blog and 7 more developer resources.'
random_paper: 4
screenshot: https://raw.githubusercontent.com/api-evangelist/jimmy/refs/heads/main/screenshots/jimmy-2026-09-02T145936.png
security:
- kind: domain-security
  name: Jimmy Domain Security
  slug: jimmy-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: jimmy
tags:
- Company
- Climate Tech
- Energy
- Nuclear
- Small Modular Reactor
- Industrial Heat
- Decarbonization
- Deep Tech
- Manufacturing
- France
website: https://www.jimmy-energy.eu/
---
