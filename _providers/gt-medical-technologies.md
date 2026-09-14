---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - rate-limits
  - security
  trial: false
  try_now: false
api_count: 0
artifact_total: 3
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/gt-medical-technologies-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://gammatile.com/
- group: company
  title: ''
  type: About
  url: https://gammatile.com/about-gt-medical-technologies/
- group: other
  title: ''
  type: Product
  url: https://gammatile.com/gammatile/about/
- group: other
  title: ''
  type: HowItWorks
  url: https://gammatile.com/gammatile/how-it-works/
- group: operate
  title: ''
  type: Contact
  url: https://gammatile.com/contact/
- group: operate
  title: ''
  type: Support
  url: https://gammatile.com/hcp/contact/
- group: company
  title: ''
  type: News
  url: https://gammatile.com/hcp/resource-center/news/
- group: other
  title: ''
  type: Research
  url: https://gammatile.com/hcp/resource-center/publications/
- group: start
  title: ''
  type: Login
  url: https://orders.gammatile.com/orders/s/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://gammatile.com/terms-of-use/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://gammatile.com/privacy-policy/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/gt-medical-technologies-inc
- group: agent
  title: ''
  type: WellKnown
  url: well-known/gt-medical-technologies-well-known.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/gt-medical-technologies-llms.txt
- group: build
  title: ''
  type: Packages
  url: packages/gt-medical-technologies-packages.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/gt-medical-technologies-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/gt-medical-technologies-rate-limits.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/gt-medical-technologies-conformance.yml
coverage:
  checked: '2026-08-22'
  detail: GT Medical Technologies manufactures GammaTile, a physical Cesium-131 collagen implant placed during brain surgery, and its entire web estate is a 44-page Next.js marketing and clinical site for patients and neurosurgeons; the only application it runs is a Salesforce Experience Cloud ordering portal at orders.gammatile.com whose stock platform OIDC discovery document is the sole machine-readable file anywhere on a company-controlled host, while every OpenAPI, GraphQL, MCP, agent-card and llms.txt path on gammatile.com returns a hard 404 and the legacy gtmedtech.com domain answers HTTP 200 with an identical 104899-byte copy of the homepage for every path including a nonsense control, making it a soft-404 catch-all rather than a developer surface.
  evidence:
  - status: 404
    url: https://gammatile.com/openapi.json
  - status: 404
    url: https://gammatile.com/llms.txt
  - status: 404
    url: https://gammatile.com/.well-known/agent-card.json
  - status: 404
    url: https://gammatile.com/.well-known/security.txt
  - status: 200
    url: https://orders.gammatile.com/orders/.well-known/openid-configuration
  - status: 200
    url: https://gtmedtech.com/nonexistent-control-98765
  - status: 404
    url: https://api.github.com/orgs/gtmedtech
  reason: not-a-software-company
  state: none
created: '2026-08-22'
description: GT Medical Technologies, Inc. is a Tempe, Arizona medical device company founded by brain tumor specialists to commercialize GammaTile, an FDA-cleared, bioabsorbable collagen implant embedded with Cesium-131 radiation seeds. Surgeons place the tiles directly into the resection cavity at the time of brain tumor removal, delivering immediate, targeted radiation without the weeks-long healing delay conventional external beam radiotherapy requires. The company sells a physical, prescription-only implant to hospitals and neurosurgical centers through a direct sales force and a Salesforce-based ordering portal; it publishes no public API, SDK, developer portal, or machine-readable specification of any kind.
image: https://gammatile.com/opengraph-image-1imx6w.png?opengraph-image.15hodd663qzs1.png
layout: provider
modified: '2026-08-22'
name: GT Medical Technologies
nav: Providers
network: true
overview: 'GT Medical Technologies is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Medical Devices, Healthcare, Oncology, and Radiation Therapy.


  GT Medical Technologies'' developer surface includes support, product news, and 17 more developer resources.'
plans:
- name: Gt Medical Technologies Plans Pricing
  plan_count: 0
  slug: gt-medical-technologies-plans-pricing
random_paper: 2
rate_limits:
- limit_count: 0
  name: Gt Medical Technologies Rate Limits
  slug: gt-medical-technologies-rate-limits
screenshot: https://raw.githubusercontent.com/api-evangelist/gt-medical-technologies/refs/heads/main/screenshots/gt-medical-technologies-2026-09-02T145642.png
security:
- kind: domain-security
  name: Gt Medical Technologies Domain Security
  slug: gt-medical-technologies-domain-security
  summary_line: TLSv1.3 · DMARC
slug: gt-medical-technologies
tags:
- Company
- Medical Devices
- Healthcare
- Oncology
- Radiation Therapy
- Brachytherapy
- Neurosurgery
- Brain Tumors
- Medical Technology
- Arizona
website: https://gammatile.com/
---
