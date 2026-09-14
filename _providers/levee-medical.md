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
  url: security/levee-medical-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://leveemedical.com/
- group: company
  title: ''
  type: Blog
  url: https://leveemedical.com/feed/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://leveemedical.com/privacy-policy/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://leveemedical.com/terms/
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/levee-medical-llms.txt
coverage:
  checked: '2026-08-25'
  detail: Levee Medical manufactures a single investigational bioabsorbable implant (the Voro Urologic Scaffold) and its entire web presence is a five-page WordPress marketing and clinical-trial site — there is no developer subdomain (api./developer./docs./status.leveemedical.com are all NXDOMAIN) and the only machine-readable endpoint on the domain is the default WordPress core REST API at /wp-json/, which is CMS scaffolding rather than a product API.
  evidence:
  - status: 404
    url: https://leveemedical.com/openapi.json
  - status: 404
    url: https://leveemedical.com/.well-known/agent-card.json
  - status: 404
    url: https://leveemedical.com/llms.txt
  - status: 200
    url: https://leveemedical.com/wp-json/
  reason: not-a-software-company
  state: none
created: '2026-08-25'
description: 'Levee Medical, Inc. is a privately held, clinical-stage medical device company headquartered in Durham, North Carolina, developing the Voro Urologic Scaffold — a bioabsorbable implant designed to support and stabilize the bladder neck and urethra following radical prostatectomy, in order to accelerate the return of continence and reduce the risk of chronic post-prostatectomy urinary incontinence. The device is investigational, is not approved for commercial sale, and is being evaluated in the FDA-approved ARID II IDE multicenter randomized pivotal trial. The company was founded in 2018 and has raised Series A and Series B financing. Levee Medical is a physical medical device manufacturer: it publishes no public API, developer portal, SDK, or machine-readable specification, and its only web surface is a WordPress marketing and clinical-trial site.'
image: https://leveemedical.com/wp-content/uploads/2024/09/open-graph-image.png
layout: provider
modified: '2026-08-25'
name: Levee Medical
nav: Providers
network: true
overview: 'Levee Medical is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Medical Devices, Healthcare, MedTech, and Urology.


  Levee Medical''s developer surface includes engineering blog and 5 more developer resources.'
random_paper: 12
screenshot: https://raw.githubusercontent.com/api-evangelist/levee-medical/refs/heads/main/screenshots/levee-medical-2026-09-02T150243.png
security:
- kind: domain-security
  name: Levee Medical Domain Security
  slug: levee-medical-domain-security
  summary_line: TLSv1.3
slug: levee-medical
tags:
- Company
- Medical Devices
- Healthcare
- MedTech
- Urology
- Prostate Cancer
- Clinical Trials
- Implantable Devices
website: https://leveemedical.com/
---
