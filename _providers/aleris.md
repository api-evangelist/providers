---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source: []
  trial: false
  try_now: false
api_count: 0
artifact_total: 3
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/aleris-domain-security.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/aleris-llms.txt
- group: commercial
  title: ''
  type: Plans
  url: plans/aleris-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/aleris-rate-limits.yml
- group: company
  title: ''
  type: Website
  url: https://novelis.com
coverage:
  checked: '2026-09-04'
  detail: Aleris ceased to exist as an independent company when Novelis completed its acquisition on 2020-04-14; aleris.com still resolves to 3.220.245.86 but no longer answers HTTP on 443 or 80, so there is no site, no developer portal and no contract to read on any Aleris host.
  evidence:
  - status: 0
    url: https://www.aleris.com/
  - status: 0
    url: https://aleris.com/.well-known/agent-card.json
  - status: 404
    url: https://novelis.com/.well-known/apis.json
  - status: 200
    url: https://novelis.com/llms.txt
  reason: defunct
  state: none
created: '2026-03-24'
description: Aleris was a global producer of rolled aluminum products serving the aerospace, automotive, building and construction, and other industrial end-use markets. Founded as IMCO Recycling and later renamed Aleris International, the company operated manufacturing plants across North America, Europe, and Asia. Aleris was acquired by Novelis Inc. (a subsidiary of Hindalco Industries) on April 14, 2020 for approximately $2.8 billion. The company's primary product lines included aluminum sheet, plate, and engineered products for demanding applications such as aerospace structures and automotive body panels. As a manufacturing-focused business, Aleris did not maintain a public developer API program, but engaged in B2B EDI integrations with major customers and suppliers across its supply chain. The Aleris brand has since been absorbed into Novelis and aleris.com no longer serves a website.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/aleris.png
layout: provider
modified: '2026-09-04'
name: Aleris
nav: Providers
network: true
overview: Aleris is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Aluminum, Manufacturing, Aerospace, Automotive, and Industrial.
plans:
- name: Aleris Plans Pricing
  plan_count: 0
  slug: aleris-plans-pricing
random_paper: 10
rate_limits:
- limit_count: 0
  name: Aleris Rate Limits
  slug: aleris-rate-limits
security:
- kind: domain-security
  name: Aleris Domain Security
  slug: aleris-domain-security
  summary_line: TLSv1.3 · DMARC
slug: aleris
tags:
- Aluminum
- Manufacturing
- Aerospace
- Automotive
- Industrial
- Materials
website: https://novelis.com
---
