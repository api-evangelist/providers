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
artifact_total: 2
common:
- group: company
  title: ''
  type: Website
  url: https://www.matter.com/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.matter.com/privacy-policy
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/matter-intelligence
- group: auth
  title: ''
  type: DomainSecurity
  url: security/matter-intelligence-domain-security.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/matter-intelligence-plans-pricing.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/matter-intelligence-llms.txt
coverage:
  checked: '2026-08-25'
  detail: Matter Intelligence is a pre-launch ultraspectral sensing company whose entire public surface is a seven-page Webflow marketing site plus an Early Access Typeform; no api./docs./developer. subdomain of matter.com resolves at all and every spec and /.well-known/ path on www.matter.com returns 404.
  evidence:
  - status: 404
    url: https://www.matter.com/openapi.json
  - status: 404
    url: https://www.matter.com/.well-known/api-catalog
  - status: 404
    url: https://www.matter.com/.well-known/agent-card.json
  - status: 200
    url: https://www.matter.com/sitemap.xml
  - status: 200
    url: https://github.com/matter-intelligence
  reason: no-developer-program
  state: none
created: '2026-08-25'
description: 'Matter Intelligence is a California-based remote sensing and physical-AI company founded in 2024 by former NASA Jet Propulsion Laboratory engineers Vishnu Sridhar and Thomas Chrien with former Caltech scientist Nathan Stein. The company builds ultraspectral imaging sensors that capture roughly 2,000 spectral bands from deep ultraviolet through thermal infrared — enough to read the molecular chemistry of a surface rather than only its color — and pairs them with Large Geospatial Models that reason over that data. Its sensors are designed for satellites, aircraft, drones and robots, and its first satellite, EARTH-1, is intended to deliver sub-meter hyperspectral and thermal imaging and to build a global encyclopedia of Earth''s material composition. Target applications named on its site include mining and mineral exploration, agriculture, insurance and risk, infrastructure monitoring, emissions and methane detection, and defense ISR. The company emerged from stealth in October
  2024 with a $12M seed round led by Lowercarbon Capital, with Toyota Ventures, Pear VC, E2MC and Mark Cuban participating. As of this profile it is pre-launch and pre-product: matter.com is a marketing site with an Early Access request form, and Matter Intelligence publishes no public API, developer portal, documentation, SDK or machine-readable contract of any kind.'
image: https://www.matter.com/images/cdn/opengraph.jpg
layout: provider
modified: '2026-08-25'
name: Matter Intelligence
nav: Providers
network: true
overview: Matter Intelligence is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Remote Sensing, Earth Observation, Hyperspectral Imaging, and Geospatial.
plans:
- name: Matter Intelligence Plans Pricing
  plan_count: 0
  slug: matter-intelligence-plans-pricing
random_paper: 12
screenshot: https://raw.githubusercontent.com/api-evangelist/matter-intelligence/refs/heads/main/screenshots/matter-intelligence-2026-09-02T150443.png
security:
- kind: domain-security
  name: Matter Intelligence Domain Security
  slug: matter-intelligence-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: matter-intelligence
tags:
- Company
- Remote Sensing
- Earth Observation
- Hyperspectral Imaging
- Geospatial
- Satellite Imagery
- Sensors
- Artificial Intelligence
- Climate
- Aerospace
website: https://www.matter.com/
---
