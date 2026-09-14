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
  url: security/neuros-medical-domain-security.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/neuros-medical-llms.txt
- group: company
  title: ''
  type: Website
  url: https://www.neurosmedical.com/
- group: company
  title: ''
  type: About
  url: https://www.neurosmedical.com/about/
- group: operate
  title: ''
  type: Support
  url: https://www.neurosmedical.com/contact-us/
- group: company
  title: ''
  type: Blog
  url: https://www.neurosmedical.com/news/
- group: company
  title: ''
  type: BlogRSS
  url: https://www.neurosmedical.com/feed/
- group: operate
  title: ''
  type: FAQ
  url: https://www.neurosmedical.com/faq/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.neurosmedical.com/terms-of-use/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.neurosmedical.com/privacy-policy-terms-of-use/
- group: company
  title: ''
  type: Careers
  url: https://www.neurosmedical.com/employment/
coverage:
  checked: '2026-08-26'
  detail: Neuros Medical sells an implanted nerve-block device (Altius pulse generator, nerve cuff electrode and a handheld patient controller) to hospitals and pain physicians; neurosmedical.com is a WordPress patient-education site with no developer section, and every contract-discovery path including /openapi.json, /graphql, /developers and all /.well-known/* returned 404.
  evidence:
  - status: 404
    url: https://www.neurosmedical.com/openapi.json
  - status: 404
    url: https://www.neurosmedical.com/developers
  - status: 404
    url: https://www.neurosmedical.com/graphql
  - status: 404
    url: https://www.neurosmedical.com/.well-known/api-catalog
  - status: 404
    url: https://www.neurosmedical.com/.well-known/agent-card.json
  - status: 200
    url: https://www.neurosmedical.com/
  reason: not-a-software-company
  state: none
created: '2026-08-26'
description: Neuros Medical is a privately held medical device company headquartered in Arden Hills, Minnesota, and the maker of the Altius Direct Electrical Nerve Stimulation System — an implantable, patient-controlled high-frequency nerve block indicated as an aid in the management of chronic intractable phantom and residual lower limb post-amputation pain in adult amputees. The system pairs a nerve cuff electrode placed around a peripheral nerve with an implantable pulse generator and a handheld patient controller, and received FDA approval in 2024 after FDA Breakthrough Device Designation and the QUEST pivotal trial. The company sells an implantable therapy to health systems, pain physicians and amputees; it operates a marketing and patient-education website and publishes no developer program, public API, SDK or machine-readable contract.
image: https://www.neurosmedical.com/wp-content/uploads/2024/04/cropped-Neuros-Logo-270x270.png
layout: provider
modified: '2026-08-26'
name: Neuros Medical
nav: Providers
network: true
overview: 'Neuros Medical is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Medical Devices, Neuromodulation, Neurostimulation, and Pain Management.


  Neuros Medical''s developer surface includes support, engineering blog, FAQ, and 8 more developer resources.'
random_paper: 4
screenshot: https://raw.githubusercontent.com/api-evangelist/neuros-medical/refs/heads/main/screenshots/neuros-medical-2026-09-02T150742.png
security:
- kind: domain-security
  name: Neuros Medical Domain Security
  slug: neuros-medical-domain-security
  summary_line: TLSv1.3 · DMARC
slug: neuros-medical
tags:
- Company
- Medical Devices
- Neuromodulation
- Neurostimulation
- Pain Management
- Healthcare
- Implantable Devices
- Life Sciences
website: https://www.neurosmedical.com/
---
