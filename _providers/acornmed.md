---
api_count: 0
artifact_total: 3
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/acornmed-domain-security.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/acornmed-llms.txt
- group: commercial
  title: ''
  type: Plans
  url: plans/acornmed-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/acornmed-rate-limits.yml
- group: company
  title: ''
  type: Website
  url: https://en.acornmed.com/
- group: company
  title: ''
  type: About
  url: https://en.acornmed.com/about/index.html
- group: operate
  title: ''
  type: Support
  url: https://en.acornmed.com/SupportContactUs/index.html
- group: company
  title: ''
  type: Blog
  url: https://www.acornmed.com/news
- group: company
  title: ''
  type: Partners
  url: https://en.acornmed.com/Partnering/index.html
coverage:
  checked: '2026-09-06'
  detail: 'AcornMed sells CAP/ISO 15189 laboratory testing and IVD products, not software: its English and Chinese sites carry only Home/About/Tests/Partnering/Support navigation, the one page named /dev-service is 药企研发合作 (pharma R&D services) rather than a developer platform, and no api., docs., developer. or open. subdomain resolves in DNS.'
  evidence:
  - status: 200
    url: https://en.acornmed.com/
  - status: 200
    url: https://www.acornmed.com/dev-service
  - status: 302
    url: https://en.acornmed.com/openapi.json
  - status: 404
    url: https://www.acornmed.com/openapi.json
  - status: 404
    url: https://acornmed.com/.well-known/agent-card.json
  - status: 404
    url: https://acornmed.com/apis.json
  reason: not-a-software-company
  state: none
created: '2026-09-06'
description: 'AcornMed Biotechnology Co., Ltd. (金橡医学) is a Beijing-headquartered precision-oncology company founded in 2018, with subsidiaries in Tianjin and Qingdao. It develops and operates next-generation-sequencing (NGS) diagnostics for solid tumors and hematologic malignancies — the AcornUI urine-based series for bladder, ureteral and renal-pelvic cancer rule-out and recurrence monitoring, AcornUPro-SEEK for prostate cancer screening, AcornOne 808 for solid tumors and AcornHema 521 for blood cancers — alongside CAP/ISO 15189 central-laboratory testing, companion-diagnostic co-development and real-world-data services for pharmaceutical partners. AcornMed is a clinical laboratory and IVD developer: it sells testing services to hospitals, physicians and pharma sponsors and publishes no public developer program, API, or machine-readable contract of any kind.'
image: https://en.acornmed.com/uploads/20240808/64de09767d8debd0f5ac3fc159834a0c.png
layout: provider
modified: '2026-09-06'
name: Acornmed
nav: Providers
network: true
overview: 'Acornmed is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Health, Healthcare, Life Sciences, and Biotechnology.


  Acornmed''s developer surface includes support, engineering blog, and 7 more developer resources.'
plans:
- name: Acornmed Plans Pricing
  plan_count: 0
  slug: acornmed-plans-pricing
random_paper: 1
rate_limits:
- limit_count: 0
  name: Acornmed Rate Limits
  slug: acornmed-rate-limits
security:
- kind: domain-security
  name: Acornmed Domain Security
  slug: acornmed-domain-security
  summary_line: TLSv1.3 · HSTS
slug: acornmed
tags:
- Company
- Health
- Healthcare
- Life Sciences
- Biotechnology
- Genomics
- Diagnostics
- Oncology
- Precision Medicine
- Clinical Laboratory
- China
website: https://en.acornmed.com/
---
