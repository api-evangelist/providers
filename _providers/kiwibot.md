---
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 7.9
  scored_at: '2026-08-26'
api_count: 1
apis:
- description: The business-to-business delivery API behind Kiwibot's autonomous last-mile fleet, served from a Google Cloud Endpoints gateway at api.kiwibot.com. Probed anonymously on 2026-08-23 the gateway answers
  name: Kiwibot Delivery Platform API
  slug: kiwibot-delivery-platform-api
artifact_total: 5
common:
- group: build
  title: ''
  type: Packages
  url: packages/kiwibot-packages.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/kiwibot-conventions.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/kiwibot-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/kiwibot-conformance.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/kiwibot-plans-pricing.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/kiwibot-llms.txt
- group: auth
  title: ''
  type: DomainSecurity
  url: security/kiwibot-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://robot.com/
- group: company
  title: ''
  type: Blog
  url: https://robot.com/newsroom
- group: operate
  title: ''
  type: Support
  url: https://robot.com/contact
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/kiwicampus
- group: commercial
  title: ''
  type: TermsOfService
  url: https://robot.com/terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://robot.com/privacy-policy
coverage:
  checked: '2026-08-23'
  detail: api.kiwibot.com is a live Google Cloud Endpoints gateway that answers 401 UNAUTHENTICATED on defined resources /deliveries and /zones, but Robot.com publishes no developer portal, reference or spec on any host (developers./docs./api.robot.com do not resolve) — the only published route to a key is the demo-request form at robot.com/contact.
  evidence:
  - status: 401
    url: https://api.kiwibot.com/deliveries
  - status: 404
    url: https://api.kiwibot.com/openapi.json
  - status: 200
    url: https://robot.com/contact
  - status: 404
    url: https://robot.com/pricing
  reason: sales-gate
  state: gated
created: '2026-08-23'
description: Kiwibot — legally Kiwi Campus, Inc., and rebranded to Robot.com in October 2025 — builds and operates fleets of autonomous sidewalk delivery robots, warehouse logistics robots, quadruped and humanoid platforms, and robot-mounted advertising units. Founded in Berkeley, California in 2017 by Felipe Chavez and Jason Oviedo out of a UC Berkeley campus food-delivery pilot, the company reports more than 1.7 million completed real-world autonomous tasks for campus dining, retail, grocery and enterprise customers across the United States, Canada, Colombia, the United Arab Emirates and Saudi Arabia, and acquired mobile-advertising firm Nickelytics in 2023. Its B2B delivery platform is exposed as an API-key-gated REST service on a Google Cloud Endpoints gateway at api.kiwibot.com — historically integrated by ordering partners such as Shopify and Ordermark — but the company publishes no developer portal, no public API reference, and no machine-readable contract; access runs through the
  sales/demo form. Its autonomy team publishes substantial first-party open source ROS 2 tooling from the github.com/kiwicampus organization.
image: https://avatars.githubusercontent.com/u/31900628?v=4
layout: provider
modified: '2026-08-23'
name: Kiwibot
nav: Providers
network: true
overview: 'Kiwibot publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Robotics, Autonomous Vehicles, Delivery, and Last Mile Delivery.


  Kiwibot''s developer surface includes engineering blog, support, and 11 more developer resources.'
plans:
- name: Kiwibot Plans Pricing
  plan_count: 0
  slug: kiwibot-plans-pricing
random_paper: 5
rate_limits:
- limit_count: 0
  name: Kiwibot Rate Limits
  slug: kiwibot-rate-limits
score:
  band: emerging
  composite: 15.2
  delta: 2.0
  facets:
    access_clarity: 21.1
    commercial_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 19.0
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 2.6
  previous_composite: 13.2
  provenance:
    conformance: first-party
    mcp: derived
  schema_version: 0.15.0
  scored_at: '2026-08-26'
  trend: flat
security:
- kind: authentication
  name: Kiwibot Authentication
  slug: kiwibot-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Kiwibot Domain Security
  slug: kiwibot-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: kiwibot
tags:
- Company
- Robotics
- Autonomous Vehicles
- Delivery
- Last Mile Delivery
- Logistics
- Warehouse Automation
- Advertising
- ROS
- Open Source
website: https://robot.com/
---
