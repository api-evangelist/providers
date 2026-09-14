---
api_count: 0
artifact_total: 1
common:
- group: company
  title: ''
  type: Website
  url: https://www.aeonindustrial.com/
- group: company
  title: ''
  type: About
  url: https://www.aeonindustrial.com/who-we-are
- group: company
  title: ''
  type: Blog
  url: https://www.aeonindustrial.com/news
- group: operate
  title: ''
  type: Support
  url: https://www.aeonindustrial.com/contact
- group: start
  title: ''
  type: Login
  url: https://www.aeonindustrial.com/login
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/aeoninc/
- group: agent
  title: ''
  type: WellKnown
  url: well-known/aeon-industrial-well-known.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/aeon-industrial-domain-security.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/aeon-industrial-llms.txt
coverage:
  checked: '2026-09-10'
  detail: Aeon Industrial builds precision tactical missile hardware and its embedded ODIN targeting software as a delivered defense product, with no developer program of any kind — the marketing site links only to /portal and /login, its ODIN page advertises an "open architecture" but publishes no interface contract for it, and the only machine-readable documents served anywhere are the WorkOS AuthKit OIDC and OAuth discovery files behind its partner-portal SSO.
  evidence:
  - status: 200
    url: https://www.aeonindustrial.com/
  - status: 200
    url: https://www.aeonindustrial.com/what-we-do/odin
  - status: 404
    url: https://www.aeonindustrial.com/openapi.json
  - status: 404
    url: https://www.aeonindustrial.com/.well-known/agent-card.json
  - status: 307
    url: https://www.aeonindustrial.com/llms.txt
  - status: 200
    url: https://auth.aeonindustrial.com/.well-known/openid-configuration
  reason: no-developer-program
  state: none
created: '2026-09-10'
description: Aeon Industrial is an American defense technology company, founded in 2023 and headquartered in the Austin, Texas area, that designs and manufactures affordable precision tactical weapon systems. Its two named products are ODIN, an autonomous precision targeting software package that observes, detects, interrogates and neutralizes threats and is advertised as an open architecture installable on third-party hardware, and Zeus, a modular software-defined tactical missile system powered by ODIN. The company is vertically integrated, building in-house from commercially available American-made components, and sells to U.S. and allied defense customers. Aeon publishes no public developer program, API, SDK or machine-readable specification; its only public machine-readable documents are the OpenID Connect and OAuth 2.0 discovery files served by its own WorkOS AuthKit identity host for its login-gated partner portal.
image: https://www.aeonindustrial.com/images/og-image.png
layout: provider
modified: '2026-09-10'
name: Aeon Industrial
nav: Providers
network: true
overview: 'Aeon Industrial is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Defense, Defense Technology, Aerospace, and Weapon Systems.


  Aeon Industrial''s developer surface includes engineering blog, support, and 7 more developer resources.'
random_paper: 18
security:
- kind: domain-security
  name: Aeon Industrial Domain Security
  slug: aeon-industrial-domain-security
  summary_line: TLSv1.3 · HSTS
slug: aeon-industrial
tags:
- Company
- Defense
- Defense Technology
- Aerospace
- Weapon Systems
- Manufacturing
- Autonomous Systems
- Targeting Software
- Hardware
- Government
website: https://www.aeonindustrial.com/
---
