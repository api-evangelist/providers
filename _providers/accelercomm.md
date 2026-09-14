---
api_count: 0
artifact_total: 1
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/accelercomm-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.accelercomm.com/
- group: company
  title: ''
  type: Blog
  url: https://www.accelercomm.com/insights
- group: company
  title: ''
  type: About
  url: https://www.accelercomm.com/about-us
- group: company
  title: ''
  type: Careers
  url: https://www.accelercomm.com/careers
- group: operate
  title: ''
  type: Contact
  url: https://www.accelercomm.com/contact
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/AccelerComm
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/accelercomm-llms.txt
coverage:
  checked: '2026-09-06'
  detail: AccelerComm licenses 5G physical-layer silicon IP — LDPC/Polar channel-coding cores and the LEOphy NTN High-PHY modem — which customers integrate over AXI hardware interfaces rather than over a network, and the company's own /llms.txt enumerates its entire site (solutions, markets, insights, resources, about-us, careers, contact) with no developer, API or docs entry; api./docs./developer.accelercomm.com do not resolve, its GitHub organisation carries zero public repositories, and no package exists on npm, PyPI, RubyGems or crates.io. Every HTML page on www.accelercomm.com sits behind a Cloudflare managed challenge, so the finding rests on the machine-readable and third-party surfaces listed below rather than on the marketing pages.
  evidence:
  - status: 200
    url: https://www.accelercomm.com/llms.txt
  - status: 403
    url: https://www.accelercomm.com/openapi.json
  - status: 404
    url: https://www.accelercomm.com/.well-known/agent-card.json
  - status: 404
    url: https://www.accelercomm.com/.well-known/api-catalog
  - status: 200
    url: https://api.github.com/orgs/accelercomm
  - status: 404
    url: https://pypi.org/pypi/accelercomm/json
  - status: 0
    url: https://api.accelercomm.com/
  reason: no-developer-program
  state: none
created: '2026-09-06'
description: 'AccelerComm Limited is a British semiconductor and wireless physical-layer IP company headquartered at Southampton Science Park, spun out of the University of Southampton in 2016 by Professor Rob Maunder. It designs and licenses channel-coding (forward error correction) intellectual property — LDPC and Polar encoders/decoders, CRC acceleration, rate matching, soft-decision demodulation, channel estimation and equalisation — delivered as RTL/FPGA IP cores, optimised software libraries and hardware-acceleration architectures for 5G NR and 4G LTE baseband. Its LEOphy product is a complete Split-6 RU High-PHY layer 1 modem for low-earth-orbit 5G Non-Terrestrial Network satellite payloads, and the company was selected for the Airbus UpNext SpaceRAN software-defined-satellite demonstrator. AccelerComm raised £21.5m in growth funding, counts IP Group among its investors, and holds more than 56 granted international patents. Its products are integrated by silicon and RAN vendors over
  hardware interfaces such as AXI rather than over the network: AccelerComm publishes no public API, developer portal, SDK or machine-readable contract, and its GitHub organisation carries no public repositories. The one machine-readable document it does serve is an /llms.txt at the root of its marketing site.'
image: https://avatars.githubusercontent.com/u/26278252?v=4
layout: provider
modified: '2026-09-06'
name: AccelerComm
nav: Providers
network: true
overview: 'AccelerComm is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Semiconductors, Semiconductor IP, Telecommunications, and Wireless.


  AccelerComm''s developer surface includes engineering blog and 7 more developer resources.'
random_paper: 13
security:
- kind: domain-security
  name: Accelercomm Domain Security
  slug: accelercomm-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: accelercomm
tags:
- Company
- Semiconductors
- Semiconductor IP
- Telecommunications
- Wireless
- 5G
- Non-Terrestrial Networks
- Satellite Communications
- Channel Coding
- Forward Error Correction
- Physical Layer
- Radio Access Networks
- FPGA
- United Kingdom
website: https://www.accelercomm.com/
---
