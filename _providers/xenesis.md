---
api_count: 0
artifact_total: 1
common:
- group: company
  title: ''
  type: Website
  url: https://xenesis.io/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/xenesis-io/
- group: company
  title: ''
  type: Twitter
  url: https://twitter.com/xenesisio
- group: operate
  title: ''
  type: Contact
  url: mailto:info@xenesis.io
- group: other
  title: ''
  type: SecondaryMarket
  url: https://forgeglobal.com/xenesis_stock/
- group: other
  title: ''
  type: SecondaryMarket
  url: https://www.nasdaqprivatemarket.com/company/xenesis/
- group: auth
  title: ''
  type: DomainSecurity
  url: security/xenesis-domain-security.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/xenesis-llms.txt
coverage:
  checked: '2026-09-04'
  detail: Xenesis sells free-space optical terminals (the Xen-Hub) and planned satellite network capacity to government and commercial satellite operators — software is not the product — and its entire xenesis.io origin now answers HTTP 401 behind a Flywheel managed-WordPress site-wide password lock, so even the marketing site is unreadable; the last complete archived version of the site carried only Home, News and About Us in its navigation, with no developer portal, API, docs or SDK section.
  evidence:
  - status: 401
    url: https://xenesis.io/
  - status: 401
    url: https://xenesis.io/.well-known/security.txt
  - status: 401
    url: https://xenesis.io/openapi.json
  - status: 401
    url: https://xenesis.io/llms.txt
  - status: 200
    url: https://web.archive.org/web/20240910001501/https://xenesis.io/
  - status: 404
    url: https://registry.npmjs.org/xenesis
  reason: not-a-software-company
  state: none
created: '2026-09-04'
description: 'Xenesis, Inc. is an optical satellite communications company founded in 2017 by Mark LaPenna and headquartered in Lisle, Illinois. It builds the Xen-Hub, a free-space optical (laser) communications terminal enabled by a technology transfer from NASA''s Jet Propulsion Laboratory and rated at greater than 10 Gbps, and plans Intercessor, a space-to-ground optical mesh network intended to backhaul high-bandwidth data with lower latency and higher capacity than radio-frequency or terrestrial fiber links. The company has taken Space Development Agency optical-terminal awards (Phase 1 in August 2022, a Phase 2 follow-on in December 2023) built to the SDA OCT v3.1 and v4.0 standards, signed a payload agreement with Airbus for a Bartolomeo demonstration slot on the International Space Station, and holds a $1.2M agreement with Georgia Tech for satellite optical communications work. Xenesis is a space hardware and telecommunications-infrastructure company, not a software vendor: as of
  this profiling pass it publishes no public API, developer portal, SDK, or machine-readable contract of any kind, and its own website is currently returning an HTTP 401 site-wide password lock.'
layout: provider
modified: '2026-09-04'
name: Xenesis
nav: Providers
network: true
overview: Xenesis is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Space, Satellite, Optical Communications, and Free Space Optics.
random_paper: 11
security:
- kind: domain-security
  name: Xenesis Domain Security
  slug: xenesis-domain-security
  summary_line: TLSv1.3
slug: xenesis
tags:
- Company
- Space
- Satellite
- Optical Communications
- Free Space Optics
- Laser Communications
- Telecommunications
- Aerospace
- Defense
- Connectivity
website: https://xenesis.io/
---
