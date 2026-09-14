---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - '{''url'': ''https://www.behaviosec.com'', ''status'': 301, ''note'': ''declared website redirects to https://risk.lexisnexis.com/products/behaviosec — a different registrable domain (behaviosec.com -> lexisnexis.com), possible rename or acquisition (probed 2026-09-03, roadmap#169)''}'
  trial: false
  try_now: false
api_count: 0
artifact_total: 1
common:
- group: other
  title: ''
  type: ParentCompany
  url: https://apis.io/providers/lexisnexis-risk-solutions/
- group: company
  title: ''
  type: Website
  url: https://www.behaviosec.com
- group: other
  title: ''
  type: ProductPage
  url: https://risk.lexisnexis.com/products/behaviosec
- group: auth
  title: ''
  type: DomainSecurity
  url: security/behaviosec-domain-security.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/behaviosec-llms.txt
created: '2026-07-17'
description: BehavioSec is a behavioral biometrics and behavioral intelligence platform that continuously authenticates users and detects fraud by analyzing how people interact with digital environments — mouse movements, typing rhythm and cadence, touch gestures, and device handling — producing real-time, explainable risk scores. Originally a Swedish company spun out of research at Luleå University of Technology, BehavioSec was acquired by LexisNexis Risk Solutions in 2022 and is now delivered as part of the LexisNexis Dynamic Decision Platform, integrating with ThreatMetrix for combined device and behavioral intelligence. It detects account takeover, bots, remote access tool (RAT) fraud, and social-engineering scams across financial services, ecommerce, gaming, telecommunications, and travel. Access is via an enterprise API; there is no public developer portal.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/behaviosec.png
layout: provider
modified: '2026-07-18'
name: BehavioSec
nav: Providers
network: true
overview: BehavioSec is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Enterprise, Behavioral Biometrics, Fraud Detection, and Authentication.
random_paper: 20
screenshot: https://raw.githubusercontent.com/api-evangelist/behaviosec/refs/heads/main/screenshots/behaviosec-2026-07-25T202659.png
security:
- kind: domain-security
  name: Behaviosec Domain Security
  slug: behaviosec-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC
slug: behaviosec
tags:
- Company
- Enterprise
- Behavioral Biometrics
- Fraud Detection
- Authentication
- Identity
- Security
- Risk
- Continuous Authentication
website: https://www.behaviosec.com
---
