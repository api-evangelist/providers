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
  url: security/clerio-vision-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.cleriovision.com/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/clerio-vision-inc.
coverage:
  checked: '2026-08-09'
  detail: Clerio Vision sells femtosecond-laser systems and LIRIC-written contact lenses, not software; cleriovision.com is a single-page WordPress site whose sitemap contains exactly one URL, there is no developer, docs or api subdomain in DNS, and the GitHub account referenced in search results does not exist.
  evidence:
  - status: 200
    url: https://www.cleriovision.com/
  - status: 404
    url: https://www.cleriovision.com/developers
  - status: 404
    url: https://www.cleriovision.com/openapi.json
  - status: 404
    url: https://www.cleriovision.com/.well-known/agent-card.json
  - status: 200
    url: https://www.cleriovision.com/sitemap_index.xml
  - status: 404
    url: https://api.github.com/users/cleriovision
  reason: not-a-software-company
  state: none
created: '2026-08-09'
description: 'Clerio Vision is a development-stage ophthalmic medical device company based in Rochester, New York, commercializing LIRIC (Laser Induced Refractive Index Change) — a non-invasive femtosecond-laser platform, licensed from the University of Rochester''s Center for Visual Science, that alters the refractive index of corneal tissue and of polymer optics without cutting or removing material. The company applies LIRIC across four ophthalmic segments: multifocal soft contact lenses for presbyopia, myopia control in children, post-implant intraocular lens (IOL) optimization after cataract surgery, and incisionless corneal refractive correction. Clerio has raised roughly $40 million from Safar Partners, Armory Square Ventures, Topmark Partners, Proxima Ventures, Atma Capital, Hegemon Capital and the National Science Foundation, and holds more than 90 patents across over 30 families. Its products are lasers, optics and lenses rather than software; the company publishes a single-page
  marketing and investor website and operates no public developer program, API, SDK or developer portal.'
image: https://www.cleriovision.com/Images/CV_logo.jpeg
layout: provider
modified: '2026-08-09'
name: Clerio Vision
nav: Providers
network: true
overview: Clerio Vision is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Medical Devices, Ophthalmology, Vision Care, and Health.
random_paper: 3
screenshot: https://raw.githubusercontent.com/api-evangelist/clerio-vision/refs/heads/main/screenshots/clerio-vision-2026-09-02T145103.png
security:
- kind: domain-security
  name: Clerio Vision Domain Security
  slug: clerio-vision-domain-security
  summary_line: TLSv1.3 · DMARC
slug: clerio-vision
tags:
- Company
- Medical Devices
- Ophthalmology
- Vision Care
- Health
- Laser Systems
- Contact Lenses
- Medical Technology
website: https://www.cleriovision.com/
---
