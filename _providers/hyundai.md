---
access_model:
  confidence: high
  label: Free today, commercialization review required for production
  onboarding: unknown
  pricing: free
  public: true
  source:
  - plans
  - '{''url'': ''https://developers.hyundai.com/web/v1/hyundai/faqs'', ''status'': 200, ''note'': ''provider states API use has been free to date and that charging is decided in consultation at commercialization review (probed 2026-09-13)''}'
  - '{''url'': ''https://developers.hyundai.com/api/v1/sampleTest/getSampleTestInfo'', ''status'': 200, ''note'': ''anonymous public sample-test tier issues a token and five fixture vehicles with no signup (probed 2026-09-13)''}'
  - '{''url'': ''https://www.hyundai.com/'', ''status'': 301, ''note'': ''declared corporate website redirects to https://www.hyundaiusa.com/us/en for US clients, but continues to serve /.well-known/security.txt and /llms.txt directly (probed 2026-09-13)''}'
  trial: true
  try_now: true
api_count: 1
apis:
- description: 'Hyundai Developers exposes connected-car data from Bluelink-enrolled vehicles to third-party services over a REST API on prd.kr-ccapi.hyundai.com. Nineteen operations are published across five groups:'
  name: Hyundai Developers Connected Car API
  slug: hyundai-developer-api
artifact_total: 8
asyncapis:
- description: ''
  name: Hyundai Webhooks
  slug: hyundai-webhooks
common:
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developers.hyundai.com/
- group: docs
  title: ''
  type: Documentation
  url: https://developers.hyundai.com/web/v1/hyundai/data_api
- group: docs
  title: ''
  type: APIReference
  url: https://developers.hyundai.com/web/v1/hyundai/specification/account
- group: start
  title: ''
  type: GettingStarted
  url: https://developers.hyundai.com/web/v1/hyundai/guide_developers
- group: operate
  title: ''
  type: Support
  url: https://developers.hyundai.com/web/v1/hyundai/tech_support
- group: operate
  title: ''
  type: HelpCenter
  url: https://developers.hyundai.com/web/v1/hyundai/faqs
- group: start
  title: ''
  type: SignUp
  url: https://console.developers.hyundai.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://developers.hyundai.com/web/v1/hyundai/terms_of_use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://privacy.hyundai.com/overview/full-policy
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/hyundai-changelog.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/hyundai-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/hyundai-conformance.yml
- group: build
  title: ''
  type: Packages
  url: packages/hyundai-packages.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/hyundai-llms.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/hyundai-well-known.yml
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/hyundai-security.txt
- group: auth
  title: ''
  type: Security
  url: security/hyundai-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/hyundai-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/hyundai-domain-security.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/hyundai-plans-pricing.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/hyundai-motor-company
- group: company
  title: ''
  type: Website
  url: https://www.hyundai.com/
- group: company
  title: ''
  type: Newsroom
  url: https://www.hyundainews.com/
created: '2025-02-25'
description: Hyundai Motor Company is a South Korean multinational automotive manufacturer and, through Hyundai Developers, the operator of a connected-car data platform for third-party developers. The platform exposes the Hyundai integrated account over OAuth 2.0 and serves nineteen documented REST operations covering user profile, vehicle list, connected-service contract dates, odometer, distance-to-empty, EV battery and charging state, and seven warning-light indicators, sourced from vehicles enrolled in Bluelink. Access is governed by a two-stage consent model built around the Korean Personal Information Protection Act — a per-vehicle OAuth consent plus a separate third-party data-provision consent — and a manual commercialization review before any real customer vehicle data is released. The API reference, a public sample-test tier with fixture vehicles, and the developer guide are all readable without an account; data is limited to vehicles in South Korea.
finops:
- name: Hyundai Finops
  service_category: API
  slug: hyundai-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/hyundai.png
layout: provider
modified: '2026-09-13'
name: Hyundai
nav: Providers
network: true
overview: 'Hyundai publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Automobiles, Cars, Connected Vehicles, Mobility, and Vehicles.


  The Hyundai catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Hyundai''s developer surface includes documentation, API reference, getting-started guide, support, signup flow, changelog, and 17 more developer resources.'
plans:
- name: Hyundai Plans Pricing
  plan_count: 0
  slug: hyundai-plans-pricing
random_paper: 19
rate_limits:
- limit_count: 1
  name: Hyundai Rate Limits
  slug: hyundai-rate-limits
screenshot: https://raw.githubusercontent.com/api-evangelist/hyundai/refs/heads/main/screenshots/hyundai-2026-06-20T183205.png
security:
- kind: authentication
  name: Hyundai Authentication
  slug: hyundai-authentication
  summary_line: 4 schemes
- kind: domain-security
  name: Hyundai Domain Security
  slug: hyundai-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Hyundai Vulnerability Disclosure
  slug: hyundai-vulnerability-disclosure
  summary_line: Hackerone · security.txt · contact published
slug: hyundai
tags:
- Automobiles
- Cars
- Connected Vehicles
- Mobility
- Vehicles
- Automotive
- Telematics
- Electric Vehicles
- Vehicle Data
- South Korea
website: https://www.hyundai.com/
---
