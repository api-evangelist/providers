---
api_count: 0
artifact_total: 1
common:
- group: company
  title: ''
  type: Website
  url: https://www.adasky.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.adasky.com/terms-of-use/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.adasky.com/privacy-policy/
- group: operate
  title: ''
  type: ContactUs
  url: https://www.adasky.com/contact-us/
- group: company
  title: ''
  type: Newsroom
  url: https://www.adasky.com/news/
- group: company
  title: ''
  type: Careers
  url: https://www.adasky.com/join-us/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/adasky
- group: learn
  title: ''
  type: YouTube
  url: https://www.youtube.com/channel/UCiOhA19ovGGIP7_GKBce-pA
- group: auth
  title: ''
  type: DomainSecurity
  url: security/adasky-domain-security.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/adasky-llms.txt
coverage:
  checked: '2026-09-07'
  detail: ADASKY sells an LWIR thermal camera whose perception software ships embedded in the hardware under OEM engagement, and its entire web presence is a 17-page WordPress marketing site with no /developers, /docs, /api or /graphql path, no api./docs./developer. subdomain (nine developer-shaped labels all NXDOMAIN), an empty GitHub organization (github.com/ADASKY, 0 public repositories since 2016), zero packages on npm, PyPI or crates.io, and all seven RFC 8615 well-known paths 404 on both www.adasky.com and adasky.com — the only machine-readable endpoint on the domain is WordPress core's own /wp-json/, which is the CMS and not an Adasky product API.
  evidence:
  - status: 404
    url: https://www.adasky.com/developers
  - status: 404
    url: https://www.adasky.com/openapi.json
  - status: 404
    url: https://www.adasky.com/graphql
  - status: 404
    url: https://www.adasky.com/llms.txt
  - status: 404
    url: https://www.adasky.com/.well-known/api-catalog
  - status: 404
    url: https://www.adasky.com/.well-known/agent-card.json
  - status: 200
    url: https://api.github.com/orgs/ADASKY/repos
  - status: 200
    url: https://www.adasky.com/wp-json/
  reason: no-developer-program
  state: none
created: '2026-09-07'
description: ADASKY (Adasky Ltd.) is an Israeli automotive sensor company founded in January 2016 and headquartered in Yokneam, Israel, that develops and manufactures automotive-grade long-wave infrared (LWIR) thermal imaging cameras and the perception software that runs on them. Its flagship product, Viper, is a compact solid-state shutterless thermal camera with 50mK sensitivity, object detection to about 300 metres and living-being classification beyond 200 metres, sold into ADAS and autonomous-vehicle programs for pedestrian, cyclist and wildlife detection, free-space detection and automatic emergency braking in darkness, glare and fog. A second line, SharpVision, serves intelligent transportation, V2X and smart-city infrastructure. ADASKY publishes no developer program, API reference, SDK or machine-readable specification; its software ships embedded in the camera under commercial OEM engagement.
image: https://www.adasky.com/wp-content/themes/adasky-v3/images/logo-header.png
layout: provider
modified: '2026-09-07'
name: Adasky
nav: Providers
network: true
overview: 'Adasky is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Automotive, Thermal Imaging, Sensors, and ADAS.


  Adasky''s developer surface includes YouTube channel and 9 more developer resources.'
random_paper: 7
security:
- kind: domain-security
  name: Adasky Domain Security
  slug: adasky-domain-security
  summary_line: TLSv1.3 · DMARC
slug: adasky
tags:
- Company
- Automotive
- Thermal Imaging
- Sensors
- ADAS
- Autonomous Vehicles
- Computer Vision
- Smart Cities
- Hardware
- Israel
- No Developer Program
website: https://www.adasky.com/
---
