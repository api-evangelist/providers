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
  url: security/procyrion-domain-security.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/procyrion-conformance.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/procyrion-llms.txt
- group: company
  title: ''
  type: Website
  url: https://www.procyrion.com/
- group: company
  title: ''
  type: Blog
  url: https://www.procyrion.com/news-all
- group: operate
  title: ''
  type: Contact
  url: https://www.procyrion.com/contact
- group: operate
  title: ''
  type: Support
  url: mailto:info@procyrion.com
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.procyrion.com/disclaimer
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/procyrion/
- group: company
  title: ''
  type: Twitter
  url: https://twitter.com/Procyrion
- group: other
  title: ''
  type: SecondaryMarket
  url: https://forgeglobal.com/procyrion_stock/
coverage:
  checked: '2026-08-05'
  detail: Procyrion is a clinical-stage medical device manufacturer whose product is a catheter-deployed blood pump, not software; www.procyrion.com is a Webflow marketing site whose sitemap contains no developer, API or documentation path, and api./developer./docs./portal.procyrion.com have no DNS record at all.
  evidence:
  - status: 404
    url: https://www.procyrion.com/openapi.json
  - status: 404
    url: https://www.procyrion.com/.well-known/agent-card.json
  - status: 404
    url: https://www.procyrion.com/llms.txt
  - status: 200
    url: https://www.procyrion.com/sitemap.xml
  reason: not-a-software-company
  state: none
created: '2026-08-05'
description: Procyrion, Inc. is a privately held, clinical-stage medical device company headquartered in Houston, Texas, developing Aortix, a catheter-deployed percutaneous mechanical circulatory support (pMCS) pump. Aortix is placed in the descending thoracic aorta and uses fluid entrainment to unload the heart and increase perfusion to the kidneys, targeting acute decompensated heart failure with diuretic resistance, prevention of acute kidney injury during cardiac surgery, cardiac unloading to limit myocardial infarct size, and longer-term chronic heart failure therapy. The device is under investigation in the DRAIN-HF pivotal IDE trial and is limited by federal law to investigational use; it is not approved for sale in any geography. Procyrion is a medical hardware and clinical company - it publishes no developer program, public API, SDK, or machine-readable API contract.
image: https://cdn.prod.website-files.com/587e5c5029ad9b731046dd9c/63752bc5ff893ac4d4772909_ProcyrionLogo.svg
layout: provider
modified: '2026-08-05'
name: Procyrion
nav: Providers
network: true
overview: 'Procyrion is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Medical Devices, Healthcare, Cardiology, and Heart Failure.


  Procyrion''s developer surface includes engineering blog, support, and 9 more developer resources.'
random_paper: 10
screenshot: https://raw.githubusercontent.com/api-evangelist/procyrion/refs/heads/main/screenshots/procyrion-2026-09-02T152112.png
security:
- kind: domain-security
  name: Procyrion Domain Security
  slug: procyrion-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: procyrion
tags:
- Company
- Medical Devices
- Healthcare
- Cardiology
- Heart Failure
- Mechanical Circulatory Support
- Medical Technology
- Clinical Trials
website: https://www.procyrion.com/
---
