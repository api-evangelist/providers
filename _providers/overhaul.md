---
agent_readiness:
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 0.0
  scored_at: '2026-08-10'
api_count: 5
apis:
- description: Create and manage shipments and receive status-based data updates, including risk summaries, driver details and next-delivery insights. Marketed as part of Overhaul's tiered API subscription. No publi
  name: Overhaul Shipment API
  slug: overhaul-shipment-api
- description: Real-time tracking across modes and regions using customer-owned IoT devices, loggers, tags and sensors or Overhaul's recommended hardware, returning device status, location and associated shipment de
  name: Overhaul Device API
  slug: overhaul-device-api
- description: Delivers shipment risk events and actionable insight, with configurable alerting driven by thresholds for hot zones and route deviations. Part of Overhaul's tiered API subscription; no public referenc
  name: Overhaul Risk Event API
  slug: overhaul-risk-event-api
- description: Predictive estimated-time-of-arrival service used to identify delivery delays in advance and optimise routing to meet delivery windows. Marketed as a standalone offering rather than part of the tiered
  name: Overhaul ETA API
  slug: overhaul-eta-api
- description: 'Carrier and driver verification and risk-scoring service that lets shippers vet carriers before booking, receive immediate notification when a suspicious driver or carrier is added to a shipment, and '
  name: Overhaul FraudWatch API
  slug: overhaul-fraudwatch-api
artifact_total: 7
common:
- group: company
  title: ''
  type: Website
  url: https://www.over-haul.com/
- group: company
  title: ''
  type: Blog
  url: https://www.over-haul.com/resources?category_equal=%5B%22Blogs%22%5D
- group: operate
  title: ''
  type: Support
  url: https://www.over-haul.com/support
- group: operate
  title: ''
  type: HelpCenter
  url: https://help.over-haul.com/hc/en-us
- group: start
  title: ''
  type: Login
  url: https://app.over-haul.com/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.over-haul.com/
- group: operate
  title: ''
  type: ChangeLog
  url: https://www.over-haul.com/product-updates
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.over-haul.com/legal/terms-and-conditions
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.over-haul.com/legal/privacy-policy
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Over-haul
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/overhaul-lifecycle.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/overhaul-changelog.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/overhaul-llms.txt
- group: design
  title: ''
  type: Conformance
  url: conformance/overhaul-conformance.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/overhaul-domain-security.yml
- group: build
  title: ''
  type: Packages
  url: packages/overhaul-packages.yml
created: '2026-08-02'
description: Overhaul is an Austin, Texas based supply-chain visibility, integrity and risk-management platform founded in 2016 that monitors and protects in-transit cargo for global enterprises across pharmaceuticals and life sciences, consumer electronics, AI hardware, automotive, manufacturing, retail and food and beverage. The platform combines data-agnostic multi-modal tracking (customer-owned or Overhaul-supplied IoT loggers, tags and sensors), real-time risk scoring, cold-chain and compliance monitoring, and a 24/7 global risk operations response capability. Product surfaces include Shipment Manager, Shipment Connect and Shipment Connect Go, Risk Monitor, FraudWatch carrier and driver verification, PartView, VINView, InventoryView, DamageView, Asset Manager, SecureBOL and RiskGPT. Overhaul markets a family of transportation and logistics APIs — Shipment, Device, Risk Event, ETA, and FraudWatch carrier performance and risk scoring — sold as a tiered subscription plus standalone offerings,
  but publishes no public developer portal, OpenAPI definition or self-serve API documentation; API access is provisioned to customers.
image: https://cdn.prod.website-files.com/6949339236f925032ea775ce/697401be90430833dbdb2e13_OG%20-%20B.jpg
layout: provider
modified: '2026-08-02'
name: Overhaul
nav: Providers
network: true
overview: 'Overhaul publishes 5 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include supply-chain, supply-chain-visibility, logistics, transportation, and cargo-security.


  Overhaul''s developer surface includes engineering blog, support, changelog, and 13 more developer resources.'
random_paper: 58
score:
  band: emerging
  composite: 23.7
  delta: 0.0
  facets:
    commercial_clarity: 34.2
    contract_quality: 0.0
    developer_ergonomics: 6.5
    discoverability: 92.6
    governance: 12.5
    operational_transparency: 36.8
  previous_composite: 23.7
  provenance:
    conformance: first-party
  schema_version: 0.9.1
  scored_at: '2026-08-10'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/overhaul/refs/heads/main/screenshots/overhaul-2026-08-07T191132.png
security:
- kind: authentication
  name: Overhaul Authentication
  slug: overhaul-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Overhaul Domain Security
  slug: overhaul-domain-security
  summary_line: TLSv1.3 · DMARC
slug: overhaul
tags:
- supply-chain
- supply-chain-visibility
- logistics
- transportation
- cargo-security
- risk-management
- fraud-prevention
- cold-chain
- iot
- track-and-trace
- freight
- compliance
website: https://www.over-haul.com/
---
