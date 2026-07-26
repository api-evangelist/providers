---
access_model:
  confidence: medium
  label: Paid
  onboarding: unknown
  pricing: paid
  public: false
  source:
  - plans
  trial: false
  try_now: false
api_count: 2
apis:
- description: Matternet's proprietary cloud platform that receives customer delivery requests, generates routes, and commands, controls, and monitors all operating Matternet assets. A consistent internal Hasura-pow
  name: Matternet Cloud Software Platform
  slug: matternet-cloud-platform
- description: Operator-facing logistics surface for requesting deliveries and tracking payload chain-of-custody across hospital, laboratory, and pharmacy workflows. Matternet has referenced a secure medical drone d
  name: Matternet Logistics Integration
  slug: matternet-logistics-integration
artifact_total: 7
collections:
- collection_type: open
  name: Matternet Cloud Platform API
  slug: open-matternet
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/matternet-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/matternet-inc
- group: company
  title: ''
  type: Website
  url: https://www.matternet.com/
- group: docs
  title: ''
  type: Documentation
  url: https://www.matternet.com/our-system
- group: commercial
  title: ''
  type: Plans
  url: plans/matternet-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/matternet-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/matternet-finops.yml
- group: company
  title: ''
  type: Blog
  url: https://www.matternet.com/newsroom
- group: other
  title: ''
  type: ProductPage
  url: https://www.matternet.com/our-system-landing-station
created: '2026-06-20'
description: Matternet designs, builds, and operates autonomous urban drone-logistics networks for healthcare and on-demand delivery. The integrated system pairs the FAA type-certified M2 aircraft with the Matternet Station and a proprietary cloud Software Platform that routes, commands, and monitors flights. Telemetry streams from drones and stations to the cloud over an MQTT broker (HiveMQ) as protobuf messages, and a consistent internal Hasura-powered GraphQL data layer serves Matternet's operator and client applications. As of this profile, Matternet does not publish a public or self-serve developer API; integrations are delivered through partner and operator engagements.
finops:
- name: Matternet Finops
  service_category: Logistics and Delivery
  slug: matternet-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/matternet.png
layout: provider
modified: '2026-07-25'
name: Matternet
nav: Providers
network: true
overview: 'Matternet publishes 2 APIs on the [APIs.io](https://apis.io/) network: Cloud Software Platform and Logistics Integration. Tagged areas include Drone Delivery, Logistics, Healthcare, Autonomous, and UAS.


  Matternet''s developer surface includes documentation, engineering blog, and 7 more developer resources.'
plans:
- name: Matternet Plans Pricing
  plan_count: 1
  slug: matternet-plans-pricing
random_paper: 35
rate_limits:
- limit_count: 3
  name: Matternet Rate Limits
  slug: matternet-rate-limits
screenshot: https://raw.githubusercontent.com/api-evangelist/matternet/refs/heads/main/screenshots/matternet-2026-06-20T185042.png
security:
- kind: domain-security
  name: Matternet Domain Security
  slug: matternet-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: matternet
tags:
- Drone Delivery
- Logistics
- Healthcare
- Autonomous
- UAS
- Telemetry
website: https://www.matternet.com/
---
