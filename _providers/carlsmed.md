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
  url: https://carlsmed.com/
- group: company
  title: ''
  type: Blog
  url: https://carlsmed.com/newsroom/
- group: operate
  title: ''
  type: Support
  url: https://carlsmed.com/contact-us/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://carlsmed.com/privacy-policy/
- group: commercial
  title: ''
  type: ConsumerHealthDataPrivacy
  url: https://carlsmed.com/consumer-health-data-privacy-policy/
- group: company
  title: ''
  type: Careers
  url: https://carlsmed.com/carlsmed-careers/
- group: other
  title: ''
  type: Patents
  url: https://carlsmed.com/patents/
- group: company
  title: ''
  type: InvestorRelations
  url: https://investors.carlsmed.com/
- group: other
  title: ''
  type: SecondaryMarket
  url: https://forgeglobal.com/carlsmed_stock/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/carlsmed
- group: other
  title: ''
  type: MobileApp
  url: https://apps.apple.com/us/app/id1645347993
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/carlsmed-llms.txt
- group: auth
  title: ''
  type: DomainSecurity
  url: security/carlsmed-domain-security.yml
coverage:
  checked: '2026-08-09'
  detail: Carlsmed ships real clinical software — the aprevo AI planning platform and the myaprevo surgeon app — but only as an end-user product distributed through the Apple App Store and a sales representative; carlsmed.com has no api./developer./docs./app. hostname in DNS, and the only machine-readable JSON on the host is the marketing site's stock WordPress core REST API at /wp-json/.
  evidence:
  - status: 404
    url: https://carlsmed.com/openapi.json
  - status: 404
    url: https://carlsmed.com/.well-known/agent-card.json
  - status: 404
    url: https://carlsmed.com/.well-known/security.txt
  - status: 404
    url: https://carlsmed.com/llms.txt
  - status: 404
    url: https://carlsmed.com/graphql
  - status: 200
    url: https://carlsmed.com/wp-json/
  - status: 200
    url: https://carlsmed.com/myaprevo/
  reason: no-developer-program
  state: none
created: '2026-08-09'
description: 'Carlsmed (Nasdaq: CARL) is a Carlsbad, California medical technology company that builds personalized spine surgery. Its aprevo technology platform combines AI-enabled segmentation of a patient''s own imaging with prior-outcomes data to produce a personalized surgical plan and patient-specific interbody fusion devices, manufactured on a digital production line and delivered to hospitals in under ten days. The platform is FDA-cleared for lumbar and cervical indications, holds FDA Breakthrough Device Designation, and earned CMS New Technology Add-On Payment status for cervical fusion in 2025. Surgeons review, approve and track plans through the myaprevo iOS application. Carlsmed operates under ISO 13485 and MDSAP certification and completed its IPO in July 2025. It publishes no public developer program, API documentation, or machine-readable API contract.'
image: https://carlsmed.com/wp-content/uploads/2024/10/Frame-3-1.png
layout: provider
modified: '2026-08-09'
name: Carlsmed
nav: Providers
network: true
overview: 'Carlsmed is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Healthcare, Medical Devices, Surgery, and Spine.


  Carlsmed''s developer surface includes engineering blog, support, and 11 more developer resources.'
random_paper: 3
screenshot: https://raw.githubusercontent.com/api-evangelist/carlsmed/refs/heads/main/screenshots/carlsmed-2026-09-02T145017.png
security:
- kind: domain-security
  name: Carlsmed Domain Security
  slug: carlsmed-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: carlsmed
tags:
- Company
- Healthcare
- Medical Devices
- Surgery
- Spine
- Artificial Intelligence
- Personalized Medicine
- Medical Imaging
- Implants
- Digital Manufacturing
website: https://carlsmed.com/
---
