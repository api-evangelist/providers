---
api_count: 0
artifact_total: 2
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/adagiomedical-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://adagiomedical.com/
- group: operate
  title: ''
  type: Support
  url: https://adagiomedical.com/us/contact
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://adagiomedical.com/us/privacy-policy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://adagiomedical.com/us/terms-of-use
- group: auth
  title: ''
  type: Security
  url: https://adagiomedical.com/us/product-security
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/adagiomedical-vulnerability-disclosure.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/adagiomedical-llms.txt
coverage:
  checked: '2026-09-06'
  detail: Adagio Medical is a NASDAQ-listed cardiac-ablation device manufacturer whose entire public web presence is 18 marketing, clinical-evidence and careers pages across /us and /eu; the only /api path on the site is the Next.js internal route that its own robots.txt disallows, and every contract-discovery probe (openapi.json, swagger.json, apis.json, llms.txt, agent-card, OAuth/OIDC discovery) returned 404 on every host.
  evidence:
  - status: 200
    url: https://adagiomedical.com/us/sitemap.xml
  - status: 404
    url: https://adagiomedical.com/openapi.json
  - status: 404
    url: https://adagiomedical.com/.well-known/agent-card.json
  - status: 404
    url: https://adagiomedical.com/llms.txt
  - status: 404
    url: https://api.github.com/orgs/adagiomedical
  reason: not-a-software-company
  state: none
created: '2026-09-06'
description: 'Adagio Medical, Inc. is a Laguna Hills, California medical device company and an operating subsidiary of Adagio Medical Holdings, Inc. (NASDAQ: ADGM). It develops catheter-based cardiac ablation systems built on its proprietary Ultra-Low Temperature Cryoablation (ULTC) platform and an emerging Pulsed Field Cryoablation (PFCA) platform, designed to create large, durable, transmural lesions for the treatment of ventricular tachycardia, atrial fibrillation and atrial flutter. Its CE-marked vCLAS Cryoablation System holds FDA Breakthrough Device Designation and is under U.S. evaluation in the FULCRUM-VT pivotal IDE study. Adagio Medical sells regulated physical devices to hospitals and electrophysiology labs; it publishes no public API, developer portal, SDK or machine-readable contract. It does publish a coordinated product-security vulnerability disclosure policy.'
image: https://adagiomedical.com/adagio-logo.svg
layout: provider
modified: '2026-09-06'
name: Adagio Medical
nav: Providers
network: true
overview: 'Adagio Medical is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Medical Devices, Health, Cardiology, and Medical Technology.


  Adagio Medical''s developer surface includes support and 7 more developer resources.'
random_paper: 9
security:
- kind: domain-security
  name: Adagiomedical Domain Security
  slug: adagiomedical-domain-security
  summary_line: TLSv1.3 · HSTS
- kind: vulnerability-disclosure
  name: Adagiomedical Vulnerability Disclosure
  slug: adagiomedical-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: adagiomedical
tags:
- Company
- Medical Devices
- Health
- Cardiology
- Medical Technology
- Cryoablation
- Electrophysiology
website: https://adagiomedical.com/
---
