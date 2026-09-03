---
access_model:
  confidence: medium
  label: Requires approval
  onboarding: approval
  pricing: unknown
  public: false
  source:
  - plans
  - authentication
  - rate-limits
  - security
  trial: false
  try_now: false
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
    event_surface_described: true
    idempotency: documented
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 28.4
  scored_at: '2026-09-03'
api_count: 2
apis:
- description: Two-way WebSocket-Secure interface between ChargePilot (acting as the Charging Management System, CMS) and an upstream Depot Management, Fleet Management or ITCS system, implemented against the VDV 46
  name: ChargePilot VDV 463 Interface
  slug: the-mobility-house-chargepilot-vdv-463
- description: Outbound cloud-to-cloud push of billing-relevant charging session records. On completion of a charging session ChargePilot POSTs a JSON payload over HTTPS to a customer-supplied endpoint, batched by d
  name: ChargePilot Charging Data Push-API
  slug: the-mobility-house-chargepilot-charging-data-push-api
artifact_total: 7
asyncapis:
- description: ''
  name: The Mobility House Webhooks
  slug: the-mobility-house-webhooks
common:
- group: company
  title: ''
  type: Website
  url: https://www.mobilityhouse.com/int_en/
- group: docs
  title: ''
  type: Documentation
  url: https://tmh-help.freshdesk.com/en/support/solutions/203000060458
- group: docs
  title: ''
  type: APIReference
  url: https://vdv-docs.tmh.energy/
- group: start
  title: ''
  type: GettingStarted
  url: https://vdv-docs.tmh.energy/initial-connection/initial-connection/
- group: operate
  title: ''
  type: Support
  url: https://tmh-help.freshdesk.com/en/support/home
- group: operate
  title: ''
  type: HelpCenter
  url: https://tmh-help.freshdesk.com/en/support/home
- group: company
  title: ''
  type: Blog
  url: https://www.mobilityhouse.com/int_en/unser-unternehmen/newsroom
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/mobilityhouse
- group: start
  title: ''
  type: SignUp
  url: https://www.mobilityhouse.com/int_en/contact
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.mobilityhouse.com/int_en/terms-conditions
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.mobilityhouse.com/int_en/privacy-policy
- group: operate
  title: ''
  type: StatusPage
  url: https://status.tmh.energy/
- group: operate
  title: ''
  type: ChangeLog
  url: https://www.mobilityhouse.com/int_en/chargepilot/product-updates
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/the-mobility-house-llms.txt
- group: build
  title: ''
  type: Packages
  url: packages/the-mobility-house-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/the-mobility-house-packages.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/the-mobility-house-webhooks.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/the-mobility-house-authentication.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/the-mobility-house-problem-types.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/the-mobility-house-conventions.yml
- group: design
  title: ''
  type: Idempotency
  url: conventions/the-mobility-house-conventions.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/the-mobility-house-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/the-mobility-house-lifecycle.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/the-mobility-house-data-model.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/the-mobility-house-changelog.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/the-mobility-house-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/the-mobility-house-rate-limits.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/the-mobility-house-domain-security.yml
created: '2026-08-30'
description: 'The Mobility House (TMH) is a Munich-headquartered electric-mobility and energy technology company, founded in 2009, with offices in Zurich, Montreal, Paris, Singapore and Belmont (USA). Its ChargePilot smart charging and energy management system pairs an on-site controller with a cloud dashboard to run dynamic load management across mixed-vendor AC and DC charging infrastructure, and its Vehicle-to-Grid (V2G) platform markets electric-vehicle battery capacity into energy and grid-balancing markets. ChargePilot integrates with third-party systems over open, standards-based interfaces rather than a public REST developer program: OCPP to charging stations, a VDV 463 WebSocket interface to depot and fleet management systems, a Modbus TCP/IP server for building and site energy management systems, and an outbound Charging Data Push-API that delivers completed charging sessions as JSON to a customer endpoint.'
image: https://cdn-website.mobilityhouse.com/Open-Graph-Image_575018da3f191243c105ceb22aba34e4.png
layout: provider
modified: '2026-08-30'
name: The Mobility House
nav: Providers
network: true
overview: 'The Mobility House publishes 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Energy, Electric Vehicles, EV Charging, and Smart Charging.


  The The Mobility House catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  The Mobility House''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, signup flow, changelog, and 21 more developer resources.'
plans:
- name: The Mobility House Plans Pricing
  plan_count: 0
  slug: the-mobility-house-plans-pricing
random_paper: 5
rate_limits:
- limit_count: 0
  name: The Mobility House Rate Limits
  slug: the-mobility-house-rate-limits
score:
  band: developing
  composite: 43.6
  coverage:
    artifact_dirs: 17
    catalog_gap: 78.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 34.2
    commercial_clarity: 34.2
    contract_governance: 18.2
    contract_quality: 41.6
    developer_ergonomics: 54.8
    discoverability: 75.9
    governance: 18.2
    operational_transparency: 26.3
  previous_composite: 43.6
  provenance:
    conformance: first-party
    mcp: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Energy & Utilities
    regime_id: energy_utilities
    score: 33.8
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/the-mobility-house/refs/heads/main/screenshots/the-mobility-house-2026-09-02T163358.png
security:
- kind: authentication
  name: The Mobility House Authentication
  slug: the-mobility-house-authentication
  summary_line: 4 schemes
- kind: domain-security
  name: The Mobility House Domain Security
  slug: the-mobility-house-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: the-mobility-house
tags:
- Company
- Energy
- Electric Vehicles
- EV Charging
- Smart Charging
- Energy Management
- Vehicle-to-Grid
- Load Management
- Fleet
- OCPP
- VDV 463
- Modbus
- Germany
website: https://www.mobilityhouse.com/int_en/
---
