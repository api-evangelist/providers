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
  url: security/atia-vision-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://atiavision.com/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/atia-vision
coverage:
  checked: '2026-08-06'
  detail: 'Atia Vision is a clinical-stage implantable-device maker whose product is the OmniVu intraocular lens, not software — no api./docs./developer./portal. host resolves in DNS, no atiavision GitHub organization exists, no npm/PyPI package is published, and every path on the marketing site (including a random control path) is answered identically by a SiteGround `sg-captcha: challenge` interstitial, so there is no developer surface to read behind it either.'
  evidence:
  - status: 404
    url: https://api.github.com/orgs/atiavision
  - status: 202
    url: https://atiavision.com/openapi.json
  - status: 202
    url: https://atiavision.com/.well-known/agent-card.json
  - status: 404
    url: https://registry.npmjs.org/atia-vision
  reason: not-a-software-company
  state: none
created: '2026-08-06'
description: 'Atia Vision, Inc. is a clinical-stage ophthalmic medical device company headquartered in Campbell, California, and a portfolio company of the Shifamed medical innovation hub. It develops the OmniVu modular shape-changing intraocular lens (IOL) — a two-part implant pairing a fluid-filled, shape-changing base with an exchangeable fixed-power front optic — designed to work with the eye''s natural accommodative mechanism to restore a full range of functional vision in cataract patients, and implanted using conventional cataract surgical technique. The company raised a $20M Series D and a $42M Series E, and in May 2025 the U.S. Food and Drug Administration granted it an Investigational Device Exemption to begin a feasibility clinical study of the OmniVu Lens System; the device is investigational and is not approved for sale or use in the United States. Atia Vision is an implantable-device manufacturer: it publishes no developer program, no public API, and no machine-readable specification.'
layout: provider
modified: '2026-08-06'
name: Atia Vision
nav: Providers
network: true
overview: Atia Vision is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Medical Devices, Ophthalmology, Intraocular Lens, and Cataract Surgery.
random_paper: 11
screenshot: https://raw.githubusercontent.com/api-evangelist/atia-vision/refs/heads/main/screenshots/atia-vision-2026-08-07T161850.png
security:
- kind: domain-security
  name: Atia Vision Domain Security
  slug: atia-vision-domain-security
  summary_line: TLSv1.3
slug: atia-vision
tags:
- Company
- Medical Devices
- Ophthalmology
- Intraocular Lens
- Cataract Surgery
- Health
- Clinical Stage
website: https://atiavision.com/
---
