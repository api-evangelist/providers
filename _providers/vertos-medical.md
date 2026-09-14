---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - security
  - '{''url'': ''https://www.vertosmed.com/'', ''status'': 301, ''note'': ''declared website redirects to https://www.stryker.com/us/en/interventional-spine.html — a different registrable domain (vertosmed.com -> stryker.com), possible rename or acquisition (probed 2026-09-03, roadmap#169)''}'
  trial: false
  try_now: false
api_count: 0
artifact_total: 1
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/vertos-medical-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.vertosmed.com/
- group: company
  title: ''
  type: About
  url: https://www.stryker.com/us/en/interventional-spine.html
- group: operate
  title: ''
  type: PressReleases
  url: https://www.stryker.com/us/en/about/news/2024/stryker-completes-acquisition-of-vertos-medical-inc-expanding-interventional-pain-management-solutions.html
coverage:
  checked: '2026-08-05'
  detail: Vertos Medical was acquired by Stryker on October 1, 2024, and vertosmed.com now answers every path — including /robots.txt, /llms.txt, /sitemap.xml and every /.well-known/* probe — with the same site-wide HTTP 301 to Stryker's Interventional Spine page, so no Vertos developer surface survives to profile.
  evidence:
  - status: 301
    url: https://www.vertosmed.com/
  - status: 301
    url: https://www.vertosmed.com/this-path-definitely-does-not-exist-9z8x7/
  - status: 301
    url: https://www.vertosmed.com/.well-known/agent-card.json
  - status: 301
    url: https://www.vertosmed.com/llms.txt
  - status: 0
    url: https://api.vertosmed.com/
  - status: 0
    url: https://developer.vertosmed.com/
  - status: 404
    url: https://api.github.com/orgs/vertos-medical
  reason: defunct
  state: none
created: '2026-08-05'
description: Vertos Medical, Inc. is a medical device company founded in 2005 and headquartered in Aliso Viejo, California, that developed the mild (minimally invasive lumbar decompression) procedure for treating lumbar spinal stenosis caused by hypertrophic ligamentum flavum. The mild device kit removes excess ligament tissue through a 5.1 mm treatment portal with no implants, no general anesthesia and no stitches; it received FDA clearance in 2006 and CE mark approval in 2019. Stryker announced a definitive agreement to acquire Vertos Medical in August 2024 and completed the acquisition on October 1, 2024, folding the mild procedure into its Interventional Spine business. The vertosmed.com domain now answers every path with a site-wide HTTP 301 redirect to Stryker, and Vertos Medical publishes no developer program, API, SDK or machine-readable specification of its own.
layout: provider
modified: '2026-08-05'
name: Vertos Medical
nav: Providers
network: true
overview: Vertos Medical is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Medical Devices, Healthcare, Spine, and Interventional Pain Management.
random_paper: 11
screenshot: https://raw.githubusercontent.com/api-evangelist/vertos-medical/refs/heads/main/screenshots/vertos-medical-2026-09-02T165812.png
security:
- kind: domain-security
  name: Vertos Medical Domain Security
  slug: vertos-medical-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: vertos-medical
tags:
- Company
- Medical Devices
- Healthcare
- Spine
- Interventional Pain Management
- Minimally Invasive Surgery
- Acquired
website: https://www.vertosmed.com/
---
