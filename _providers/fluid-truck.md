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
  url: security/fluid-truck-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://fluidtruck.com/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/fluidtruck
- group: build
  title: ''
  type: Packages
  url: packages/fluid-truck-packages.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/fluid-truck-llms.txt
coverage:
  checked: '2026-08-16'
  detail: Fluid Truck is wound down — Chapter 11 in Delaware October 2024, assets sold to Kingbee Rentals December 2024, converted to Chapter 7 liquidation September 2025 — and fluidtruck.com now fails the TLS handshake outright on every request while app.fluidtruck.com returns Vercel DEPLOYMENT_NOT_FOUND, so there is no surface left to read and no archived evidence a developer program ever existed.
  evidence:
  - status: 0
    url: https://fluidtruck.com/
  - status: 301
    url: http://fluidtruck.com/
  - status: 404
    url: https://app.fluidtruck.com/
  - status: 200
    url: https://status.fluidtruck.com/
  - status: 200
    url: https://fluidtruck.github.io/helm-charts/index.yaml
  reason: defunct
  state: none
created: '2026-08-16'
description: 'Fluid Truck was a Denver, Colorado peer-to-peer commercial vehicle sharing platform founded in 2016 by James Eberhard and Jenifer Snyder, often described as "the Zipcar of commercial vehicles". It operated an app-based, self-service rental marketplace for cargo vans, box trucks and flatbeds across roughly 400 cities in 32 US states, and ran the Fluid Vehicle Investor Program (FVIP) through which individuals and small businesses bought fleets that Fluid managed and rented out. The company raised over $80 million in venture funding, filed for Chapter 11 bankruptcy in Delaware in October 2024 after an $20.6 million cash loss in 2023, sold substantially all assets to Kingbee Rentals in December 2024, and the case converted to Chapter 7 liquidation in September 2025. The company is wound down: no developer program, API documentation, or machine-readable contract was ever published, and its own web properties no longer serve a valid TLS certificate.'
layout: provider
modified: '2026-08-16'
name: Fluid Truck
nav: Providers
network: true
overview: Fluid Truck is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Transportation, Logistics, Vehicle Rental, and Fleet Management.
random_paper: 17
security:
- kind: domain-security
  name: Fluid Truck Domain Security
  slug: fluid-truck-domain-security
  summary_line: DMARC
slug: fluid-truck
tags:
- Company
- Transportation
- Logistics
- Vehicle Rental
- Fleet Management
- Mobility
- Marketplace
- Defunct
website: https://fluidtruck.com/
---
