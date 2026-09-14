---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source: []
  trial: false
  try_now: false
api_count: 2
apis:
- description: The authenticated fleet-management and over-the-air update API behind Aethero's "Aether" user portal at cloud.aethero.com. The service is a self-hosted deployment of RDFM (Remote Device Fleet Manager)
  name: Aether Fleet Management (RDFM)
  slug: aether-rdfm
- description: 'The backend API of AMATDT, Aethero''s first-party model annotation, training and deployment tool, served at amatdt.aethero.com/api by a NestJS application. Probed 2026-09-12: https://amatdt.aethero.com'
  name: AMATDT API
  slug: amatdt
artifact_total: 5
common:
- group: commercial
  title: ''
  type: Pricing
  url: https://www.aethero.com/altus/
- group: company
  title: ''
  type: BlogRSS
  url: https://www.aethero.com/feed/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Aethero-ECM
- group: company
  title: ''
  type: Twitter
  url: https://x.com/AetheroSpace
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/aethero/
- group: other
  title: ''
  type: SecondaryMarket
  url: https://equityzen.com/company/aetherospace
- group: commercial
  title: ''
  type: Plans
  url: plans/aethero-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/aethero-rate-limits.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/aethero-llms.txt
- group: company
  title: ''
  type: Website
  url: https://www.aethero.com/
- group: company
  title: ''
  type: Blog
  url: https://www.aethero.com/news/
- group: auth
  title: ''
  type: DomainSecurity
  url: security/aethero-domain-security.yml
created: '2026-07-17'
description: Aethero designs and manufactures radiation-hardened, space-rated edge computing systems and AI/ML software for satellites, space stations, and orbital data centers, enabling autonomous on-orbit processing of imagery and sensor data rather than downlinking raw feeds. Its NVIDIA Jetson Orin/Thor-based NxN-ECM and NxA-ECM edge computing modules, Titan and Phobos platforms, the Aether fleet-management software framework, and the AMATDT model annotation/training/deployment tool let spacecraft run AI inference in orbit. Founded in 2023 and headquartered in San Francisco, Aethero raised an $8.4M seed round led by Kindred Ventures in June 2025. Aethero exposes no public web API today; this profile captures the company's identity and its live domain-security posture for the API Evangelist network.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/aethero.png
layout: provider
modified: '2026-07-18'
name: Aethero
nav: Providers
network: true
overview: 'Aethero publishes 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Space, Edge Computing, Satellites, and Artificial Intelligence.


  Aethero''s developer surface includes pricing, engineering blog, and 10 more developer resources.'
plans:
- name: Aethero Plans Pricing
  plan_count: 4
  slug: aethero-plans-pricing
random_paper: 9
rate_limits:
- limit_count: 0
  name: Aethero Rate Limits
  slug: aethero-rate-limits
screenshot: https://raw.githubusercontent.com/api-evangelist/aethero/refs/heads/main/screenshots/aethero-2026-07-25T181737.png
security:
- kind: domain-security
  name: Aethero Domain Security
  slug: aethero-domain-security
  summary_line: TLSv1.2 · DNSSEC · DMARC
slug: aethero
tags:
- Company
- Space
- Edge Computing
- Satellites
- Artificial Intelligence
- Machine-Learning
- Aerospace
- Defense
- Hardware
website: https://www.aethero.com/
---
