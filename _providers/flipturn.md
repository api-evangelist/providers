---
access_model:
  confidence: medium
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: derived
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 38.1
  scored_at: '2026-08-17'
agentic_access:
- acting_count: 11
  human_in_the_loop: 0
  name: Flipturn Agentic Access
  operation_count: 26
  slug: flipturn-agentic-access
  summary_line: 26 operations · 11 acting
api_count: 13
apis:
- description: RFID cards and vehicle MAC IDs used to authorize charging.
  name: Flipturn Access IDs API
  slug: flipturn-access-ids-api
- description: Alerts raised by the platform.
  name: Flipturn Alerts API
  slug: flipturn-alerts-api
- description: Uptime, error, and utilization statistics.
  name: Flipturn Charger Health API
  slug: flipturn-charger-health-api
- description: Individual charger detail lookups.
  name: Flipturn Chargers API
  slug: flipturn-chargers-api
- description: Historical and in-progress charging sessions.
  name: Flipturn Charging Sessions API
  slug: flipturn-charging-sessions-api
- description: Scheduled vehicle departure times synced from a TMS.
  name: Flipturn Departure Times API
  slug: flipturn-departure-times-api
- description: Charger error records.
  name: Flipturn Errors API
  slug: flipturn-errors-api
- description: Scheduled maintenance windows for chargers.
  name: Flipturn Maintenance Windows API
  slug: flipturn-maintenance-windows-api
- description: Raw OCPP protocol messages for a charger.
  name: Flipturn OCPP Messages API
  slug: flipturn-ocpp-messages-api
- description: OCPP ReserveNow / CancelReservation port reservations.
  name: Flipturn Reservations API
  slug: flipturn-reservations-api
- description: Cost and capacity power limits for a site.
  name: Flipturn Site Power Limits API
  slug: flipturn-site-power-limits-api
- description: Sites, their chargers and ports, and current status.
  name: Flipturn Sites API
  slug: flipturn-sites-api
- description: Electric vehicles and their associated access IDs.
  name: Flipturn Vehicles API
  slug: flipturn-vehicles-api
artifact_total: 33
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Flipturn Access IDs API
  slug: open-flipturn-access-ids-api
- collection_type: open
  name: Flipturn Access IDs Alerts API
  slug: open-flipturn-alerts-api
- collection_type: open
  name: Flipturn Access IDs Charger Health API
  slug: open-flipturn-charger-health-api
- collection_type: open
  name: Flipturn Access IDs Chargers API
  slug: open-flipturn-chargers-api
- collection_type: open
  name: Flipturn Access IDs Charging Sessions API
  slug: open-flipturn-charging-sessions-api
- collection_type: open
  name: Flipturn Access IDs Departure Times API
  slug: open-flipturn-departure-times-api
- collection_type: open
  name: Flipturn Access IDs Errors API
  slug: open-flipturn-errors-api
- collection_type: open
  name: Flipturn Access IDs Maintenance Windows API
  slug: open-flipturn-maintenance-windows-api
- collection_type: open
  name: Flipturn Access IDs OCPP Messages API
  slug: open-flipturn-ocpp-messages-api
- collection_type: open
  name: Flipturn Access IDs Reservations API
  slug: open-flipturn-reservations-api
- collection_type: open
  name: Flipturn Access IDs Site Power Limits API
  slug: open-flipturn-site-power-limits-api
- collection_type: open
  name: Flipturn Access IDs Sites API
  slug: open-flipturn-sites-api
- collection_type: open
  name: Flipturn Access IDs Vehicles API
  slug: open-flipturn-vehicles-api
common:
- group: other
  title: ''
  type: Overlay
  url: overlays/flipturn-openapi-overlay.yaml
- group: company
  title: ''
  type: Website
  url: http://www.getflipturn.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://api-docs.getflipturn.com/
- group: docs
  title: ''
  type: Documentation
  url: https://api-docs.getflipturn.com/
- group: docs
  title: ''
  type: APIReference
  url: https://api-docs.getflipturn.com/
- group: start
  title: ''
  type: GettingStarted
  url: https://api-docs.getflipturn.com/authorization.md
- group: auth
  title: ''
  type: Authentication
  url: authentication/flipturn-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/flipturn-conventions.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/flipturn-rate-limits.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/flipturn-problem-types.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/flipturn-llms.txt
- group: agent
  title: ''
  type: MCPServer
  url: mcp/flipturn-mcp.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/flipturn-agentic-access.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/flipturn-lifecycle.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://status.getflipturn.com/
- group: design
  title: ''
  type: Conformance
  url: conformance/flipturn-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: https://www.getflipturn.com/product/security
- group: auth
  title: ''
  type: TrustCenter
  url: security/flipturn-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/flipturn-domain-security.yml
- group: operate
  title: ''
  type: Support
  url: https://www.getflipturn.com/contact-us
- group: company
  title: ''
  type: Blog
  url: https://www.getflipturn.com/blog
- group: start
  title: ''
  type: SignUp
  url: https://www.getflipturn.com/getdemo
- group: start
  title: ''
  type: Login
  url: https://cloud.getflipturn.com
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.getflipturn.com/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.getflipturn.com/privacy-policy
created: '2026-07-17'
description: Flipturn is an EV charging management platform that gives businesses and fleet operators one system to monitor chargers, manage energy costs, run fleet charging operations, control access, and handle payments and billing. Its software layer sits on top of OCPP 1.6 and 2.0.1 chargers (with OCPI support for roaming partners) and serves delivery fleets, transit agencies, multifamily housing, dealerships, workplaces, hospitality, retail, parking, and valet. Flipturn also publishes a JSON REST API, secured with a bearer API key, that exposes sites, chargers and ports, charging sessions, charger health and uptime, access IDs (RFID cards and vehicles), vehicles, alerts, charger errors, raw OCPP messages, port reservations, site power limits, vehicle departure times, and maintenance windows — designed for integrating charging data with ticketing platforms, data warehouses, and transportation management systems. Flipturn is backed by Accel and CRV.
image: https://cdn.prod.website-files.com/64b825ce3428b050ac90c545/6a0deea6bb9839d3ec28999f_Opengraph_hi-res.avif
layout: provider
mcp_servers:
- description: ''
  name: flipturn-mcp.yml
  slug: flipturn-mcpyml
modified: '2026-07-19'
name: Flipturn
nav: Providers
network: true
overview: 'Flipturn publishes 13 APIs on the [APIs.io](https://apis.io/) network, including Access IDs API, Alerts API, Charger Health API, and 10 more. Tagged areas include Company, EV Charging, Electric Vehicles, Fleet Management, and Energy.


  Flipturn''s developer surface includes documentation, API reference, getting-started guide, authentication, support, engineering blog, signup flow, and 19 more developer resources.'
random_paper: 139
rate_limits:
- limit_count: 2
  name: Flipturn Rate Limits
  slug: flipturn-rate-limits
score:
  band: developing
  composite: 50.5
  delta: 0.0
  facets:
    commercial_clarity: 50.0
    contract_quality: 62.7
    developer_ergonomics: 56.0
    discoverability: 81.5
    governance: 20.8
    operational_transparency: 36.8
  previous_composite: 50.5
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 13
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Energy & Utilities
    regime_id: energy_utilities
    score: 40.5
  schema_version: 0.11.0
  scored_at: '2026-08-17'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/flipturn/refs/heads/main/screenshots/flipturn-2026-07-25T214806.png
security:
- kind: authentication
  name: Flipturn Authentication
  slug: flipturn-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Flipturn Domain Security
  slug: flipturn-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: trust-center
  name: Flipturn Trust Center
  slug: flipturn-trust-center
  summary_line: SOC 2, GDPR
slug: flipturn
tags:
- Company
- EV Charging
- Electric Vehicles
- Fleet Management
- Energy
- Charging Infrastructure
- OCPP
- OCPI
- Mobility
- REST API
website: http://www.getflipturn.com
---
