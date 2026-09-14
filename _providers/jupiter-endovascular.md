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
  url: security/jupiter-endovascular-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://jupiterendo.com/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://jupiterendo.com/privacy-policy/
coverage:
  checked: '2026-08-23'
  detail: Jupiter Endovascular is a pre-commercial clinical-stage manufacturer of a physical Class III catheter device (the Vertex Pulmonary Embolectomy System, in the SPIRARE I and II trials) — software is not the product, and the only web property is a SiteGround-hosted WordPress marketing site at jupiterendo.com that answers every path, including a deliberately bogus control path, with an identical 202 sg-captcha interstitial; there is no GitHub organization, no package on npm or PyPI, and the api/developer/docs subdomains all wildcard to a NameBright parking host rather than to any developer surface.
  evidence:
  - status: 202
    url: https://jupiterendo.com/openapi.json
  - status: 202
    url: https://jupiterendo.com/.well-known/agent-card.json
  - status: 404
    url: https://api.github.com/orgs/jupiter-endovascular
  - status: 404
    url: https://registry.npmjs.org/jupiter-endovascular
  reason: not-a-software-company
  state: none
created: '2026-08-23'
description: Jupiter Endovascular, Inc. is a privately held medical technology company headquartered in Menlo Park, California, developing Endoportal Control, a platform technology that fixes a flexibly navigated endoportal device into a stable state inside the vasculature so a catheter-based intervention can be delivered with the precision and control of direct surgical access. Its lead product is the Vertex Pulmonary Embolectomy System for acute pulmonary embolism, evaluated in the SPIRARE I first-in-human study (NCT06571760) and the FDA-approved SPIRARE II U.S. pivotal study. The company exited stealth with $21M and later closed an oversubscribed Series B surpassing its $40M target, led by Sonder Capital. Jupiter Endovascular is a pre-commercial clinical-stage device manufacturer and publishes no developer program, no API, and no machine-readable interface of any kind.
layout: provider
modified: '2026-08-23'
name: Jupiter Endovascular
nav: Providers
network: true
overview: Jupiter Endovascular is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Medical Devices, Medical Technology, Healthcare, and Interventional Cardiology.
random_paper: 3
screenshot: https://raw.githubusercontent.com/api-evangelist/jupiter-endovascular/refs/heads/main/screenshots/jupiter-endovascular-2026-09-02T150003.png
security:
- kind: domain-security
  name: Jupiter Endovascular Domain Security
  slug: jupiter-endovascular-domain-security
  summary_line: TLSv1.3 · DMARC
slug: jupiter-endovascular
tags:
- Company
- Medical Devices
- Medical Technology
- Healthcare
- Interventional Cardiology
- Pulmonary Embolism
- Clinical Trials
website: https://jupiterendo.com/
---
