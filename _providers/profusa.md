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
  url: security/profusa-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://profusa.com/
- group: company
  title: ''
  type: About
  url: https://profusa.com/about-profusa/
- group: operate
  title: ''
  type: Support
  url: https://profusa.com/contact-profusa/
- group: company
  title: ''
  type: Blog
  url: https://investors.profusa.com/press-releases
- group: company
  title: ''
  type: BlogRSS
  url: https://profusa.com/feed/
- group: company
  title: ''
  type: Careers
  url: https://profusa.com/careers-profusa/
- group: company
  title: ''
  type: InvestorRelations
  url: https://investors.profusa.com/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/profusa
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/profusa-llms.txt
coverage:
  checked: '2026-08-26'
  detail: Profusa ships a clinical Data Platform and a phone app for its Lumee biosensors but publishes nothing for developers — profusa.com is a WordPress marketing site whose only machine-readable surface is the generic WordPress core REST discovery document at /wp-json/, and every developer path (/developers, /api, /docs, /openapi.json, /llms.txt, /.well-known/*) returns 404, while investors.profusa.com answers 200 with an SPA shell for every path including /.well-known/agent-card.json.
  evidence:
  - status: 404
    url: https://profusa.com/developers
  - status: 404
    url: https://profusa.com/openapi.json
  - status: 404
    url: https://profusa.com/llms.txt
  - status: 404
    url: https://profusa.com/.well-known/agent-card.json
  - status: 200
    url: https://profusa.com/wp-json/
  - status: 200
    url: https://investors.profusa.com/.well-known/agent-card.json
  reason: no-developer-program
  state: none
created: '2026-08-26'
description: 'Profusa, Inc. (Nasdaq: PFSA) is a South San Francisco digital-health and medical-device company that builds tissue-integrated biosensors — injectable, biologically compatible hydrogel microsensors smaller than a grain of rice — for continuous, real-time monitoring of body chemistry. Its Lumee Oxygen Platform reports tissue oxygen for peripheral artery disease, chronic wounds and reconstructive surgery, and a long-duration Lumee glucose sensor is in development. A companion Data Platform turns raw sensor readings into clinical intelligence for clinicians, with EMR integration described as planned rather than shipped. Profusa has received more than USD 23M in NIH and DARPA funding and became publicly traded in July 2025 through a business combination with NorthView Acquisition Corporation. As of this profiling pass the company publishes no developer program, no public API documentation and no machine-readable API contract.'
image: https://profusa.com/wp-content/uploads/2015/12/cropped-profusa-logo-1-270x270.png
layout: provider
modified: '2026-08-26'
name: Profusa
nav: Providers
network: true
overview: 'Profusa is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Health, Medical Devices, Biosensors, and Digital Health.


  Profusa''s developer surface includes support, engineering blog, and 8 more developer resources.'
random_paper: 12
screenshot: https://raw.githubusercontent.com/api-evangelist/profusa/refs/heads/main/screenshots/profusa-2026-09-02T152124.png
security:
- kind: domain-security
  name: Profusa Domain Security
  slug: profusa-domain-security
  summary_line: TLSv1.3 · DMARC
slug: profusa
tags:
- Company
- Health
- Medical Devices
- Biosensors
- Digital Health
- Continuous Monitoring
- Diagnostics
- Life Sciences
website: https://profusa.com/
---
