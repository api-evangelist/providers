---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - '{''url'': ''https://forhims.com'', ''status'': 301, ''note'': ''declared website redirects to https://www.hims.com/ — a different registrable domain (forhims.com -> hims.com), possible rename or acquisition (probed 2026-09-03, roadmap#169)''}'
  trial: false
  try_now: false
api_count: 0
artifact_total: 2
common:
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/hims-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: https://forhims.com/vulnerability-disclosure-terms
- group: auth
  title: ''
  type: DomainSecurity
  url: security/hims-domain-security.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/hims-well-known.yml
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/hims-well-known.yml
- group: company
  title: ''
  type: Website
  url: https://forhims.com
created: '2026-07-17'
description: 'Hims is the men''s brand of Hims & Hers Health, Inc. (NYSE: HIMS), a U.S.-based direct-to-consumer telehealth platform. Through forhims.com it connects patients with licensed medical providers and affiliated pharmacies to offer treatment for sexual health, hair loss, dermatology and skincare, mental health, and weight loss, including provider consultations, personalized prescriptions, and recurring subscription fulfillment shipped to the customer. Hims & Hers operates the sibling Hers brand for women and runs its own pharmacy and fulfillment operations. This API Evangelist profile tracks the company''s public developer, security, and trust surface; Hims does not currently publish a public developer API, so this record is identity- and security-focused rather than spec-bearing.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/hims.png
layout: provider
modified: '2026-07-19'
name: Hims
nav: Providers
network: true
overview: Hims is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Health, Healthcare, Telehealth, and Wellness.
random_paper: 13
security:
- kind: domain-security
  name: Hims Domain Security
  slug: hims-domain-security
  summary_line: TLSv1.2 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Hims Vulnerability Disclosure
  slug: hims-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: hims
tags:
- Company
- Health
- Healthcare
- Telehealth
- Wellness
- Pharmacy
- Consumer
- E-Commerce
website: https://forhims.com
---
