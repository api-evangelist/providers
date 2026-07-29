---
access_model:
  confidence: medium
  label: Enterprise
  onboarding: unknown
  pricing: enterprise
  public: false
  source:
  - plans
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    asyncapi_events: false
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 19.4
  scored_at: '2026-07-28'
api_count: 6
apis:
- description: Manage charging stations and charge points (EVSE) - registration, status, health, and availability - within the EV Connect charge point management platform. Endpoints and base URL are not publicly doc
  name: EV Connect Stations / Charge Points API
  slug: stations-charge-points
- description: Start, stop, and retrieve charging sessions and transaction records, including energy delivered and usage tracked in real time. Endpoints and base URL are not publicly documented; access is partner/sa
  name: EV Connect Sessions API
  slug: sessions
- description: Inspect connectors on a charge point - type, power level, and live availability/status. Endpoints and base URL are not publicly documented; access is partner/sales-gated via the EV Connect API Gateway
  name: EV Connect Connectors API
  slug: connectors
- description: Manage drivers and their charging accounts, enabling custom driver apps, coupons pushed at plug-in, and loyalty-program tie-ins. Endpoints and base URL are not publicly documented; access is partner/s
  name: EV Connect Drivers API
  slug: drivers
- description: Configure charging pricing, tariffs, and payment handling that govern how sessions are billed across a network. Endpoints and base URL are not publicly documented; access is partner/sales-gated via th
  name: EV Connect Pricing / Plans API
  slug: pricing-plans
- description: Event notifications for charging lifecycle changes (e.g., session start, stop, and station status). EV Connect markets event-driven integrations, but no public webhook event catalog or payloads are do
  name: EV Connect Webhooks
  slug: webhooks
artifact_total: 12
collections:
- collection_type: open
  name: EV Connect API Platform
  slug: open-ev-connect
common:
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/ev-connect-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/ev-connect-domain-security.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/evconnect
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/ev-connect
- group: company
  title: ''
  type: Website
  url: https://www.evconnect.com
- group: docs
  title: ''
  type: Documentation
  url: https://www.evconnect.com/platform/
- group: commercial
  title: ''
  type: Plans
  url: plans/ev-connect-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/ev-connect-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/ev-connect-finops.yml
- group: company
  title: ''
  type: Blog
  url: https://www.evconnect.com/blog/
created: '2026-06-21'
description: EV Connect is an EV charging network and charge-station management platform (a CPMS / charge point management system) now part of Schneider Electric. Its API Platform exposes open, standards-based APIs through an API Gateway so operators can white-label driver apps and integrate charging into commerce, loyalty, fleet, and energy systems, backed by OCPP station certification and OCPI roaming. Developer documentation and credentials are partner/sales-gated; no public base URL, endpoints, or authentication details are published.
finops:
- name: Ev Connect Finops
  service_category: EV Charging and Energy Management
  slug: ev-connect-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/ev-connect.png
layout: provider
modified: '2026-06-21'
name: EV Connect
nav: Providers
network: true
overview: 'EV Connect publishes 6 APIs on the [APIs.io](https://apis.io/) network, including Stations / Charge Points API, Sessions API, Connectors API, and 3 more. Tagged areas include EV Charging, Charge Point Management, CPMS, Mobility, and Energy.


  EV Connect''s developer surface includes documentation, engineering blog, and 8 more developer resources.'
plans:
- name: Ev Connect Plans Pricing
  plan_count: 1
  slug: ev-connect-plans-pricing
random_paper: 9
rate_limits:
- limit_count: 1
  name: Ev Connect Rate Limits
  slug: ev-connect-rate-limits
score:
  band: emerging
  composite: 24.5
  delta: -5.1
  facets:
    commercial_clarity: 28.9
    contract_quality: 32.3
    developer_ergonomics: 10.9
    discoverability: 64.8
    governance: 0.0
    operational_transparency: 26.3
  previous_composite: 29.6
  regulatory:
    applies: true
    matched_via: tags
    regime: Energy & Utilities
    regime_id: energy_utilities
    score: 16.2
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: falling
screenshot: https://raw.githubusercontent.com/api-evangelist/ev-connect/refs/heads/main/screenshots/ev-connect-2026-07-25T213703.png
security:
- kind: domain-security
  name: Ev Connect Domain Security
  slug: ev-connect-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Ev Connect Vulnerability Disclosure
  slug: ev-connect-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: ev-connect
tags:
- EV Charging
- Charge Point Management
- CPMS
- Mobility
- Energy
- OCPP
- OCPI
website: https://www.evconnect.com
---
