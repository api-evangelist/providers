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
- group: company
  title: ''
  type: Website
  url: https://www.levita.com/
- group: company
  title: ''
  type: Blog
  url: https://www.levita.com/blog
- group: company
  title: ''
  type: BlogRSS
  url: https://www.levita.com/feed
- group: operate
  title: ''
  type: Support
  url: https://www.levita.com/contact
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.levita.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.levita.com/privacy
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/levita-magnetics-llms.txt
- group: auth
  title: ''
  type: DomainSecurity
  url: security/levita-magnetics-domain-security.yml
coverage:
  checked: '2026-08-25'
  detail: Levita Magnetics ships a regulated surgical robot (MARS) and a magnetic retractor system to hospitals, and the only machine-readable endpoint on any host it controls is the stock WordPress /wp-json/ CMS API behind its marketing site — there is no developer portal, no API reference, no GitHub organization and no published contract of any kind.
  evidence:
  - status: 404
    url: https://www.levita.com/openapi.json
  - status: 404
    url: https://www.levita.com/.well-known/agent-card.json
  - status: 404
    url: https://api.github.com/orgs/levita-magnetics
  - status: 404
    url: https://www.magneticsurgery.com/openapi.json
  - status: 200
    url: https://www.levita.com/wp-json/
  reason: no-developer-program
  state: none
created: '2026-08-25'
description: Levita Magnetics is a Mountain View, California medical device company, founded by minimally invasive surgeon Dr. Alberto Rodriguez-Navarro and co-founded by Nicolas Luksic, with an additional office in Santiago, Chile. It develops Magnetic Surgery — the Levita Magnetic Surgical System, in which an external magnet placed on the patient's skin controls a shaftless detachable retractor to enable reduced-port laparoscopic procedures — and the MARS (Magnetic-Assisted Robotic Surgery) platform launched in 2023, an FDA-cleared surgical robotic system used in abdominal and, more recently, pediatric procedures. The MARS platform is built on RTI Connext (the DDS real-time connectivity standard) internally, and Levita has demonstrated AI-guided autonomous camera control during surgery. Levita ships regulated surgical hardware and its embedded control software to hospitals; it operates no public developer program, publishes no API documentation, and exposes no machine-readable API contract
  on any host it controls.
image: https://www.levita.com/wp-content/uploads/2023/11/levita-social-logo.png
layout: provider
modified: '2026-08-25'
name: Levita Magnetics
nav: Providers
network: true
overview: 'Levita Magnetics is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Medical Devices, Surgical Robotics, Healthcare, and Robotics.


  Levita Magnetics'' developer surface includes engineering blog, support, and 6 more developer resources.'
random_paper: 7
screenshot: https://raw.githubusercontent.com/api-evangelist/levita-magnetics/refs/heads/main/screenshots/levita-magnetics-2026-09-02T150243.png
security:
- kind: domain-security
  name: Levita Magnetics Domain Security
  slug: levita-magnetics-domain-security
  summary_line: TLSv1.3 · DMARC
slug: levita-magnetics
tags:
- Company
- Medical Devices
- Surgical Robotics
- Healthcare
- Robotics
- Minimally Invasive Surgery
- Medical Technology
- Hardware
website: https://www.levita.com/
---
