---
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: na
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: true
    idempotency: na
    mcp_server: false
    openapi_examples: documented
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 28.7
  scored_at: '2026-09-01'
api_count: 1
apis:
- description: The individual Utilita services tracked on the status page.
  name: Utilita Components API
  slug: utilita-components-api
- description: Unplanned service incidents and their update timeline.
  name: Utilita Incidents API
  slug: utilita-incidents-api
- description: Planned maintenance windows.
  name: Utilita Scheduled Maintenance API
  slug: utilita-scheduled-maintenance-api
- description: Overall page status and rolled-up summary.
  name: Utilita Status API
  slug: utilita-status-api
artifact_total: 14
asyncapis:
- description: ''
  name: Utilita Status Webhooks
  slug: utilita-status-webhooks
collections:
- collection_type: open
  name: Utilita Status API
  slug: open-utilita-status
common:
- group: agent
  title: ''
  type: AgentSkill
  url: skills/utilita-check-service-status.md
- group: company
  title: ''
  type: Website
  url: https://utilita.co.uk/
- group: company
  title: ''
  type: About
  url: https://utilita.co.uk/about-us
- group: docs
  title: ''
  type: Documentation
  url: https://status.utilita.co.uk/api
- group: docs
  title: ''
  type: APIReference
  url: https://status.utilita.co.uk/api
- group: operate
  title: ''
  type: StatusPage
  url: https://status.utilita.co.uk/
- group: docs
  title: ''
  type: OpenAPI
  url: openapi/utilita-status-openapi.yml
- group: build
  title: ''
  type: Examples
  url: examples/_index.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/utilita-status-webhooks.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/utilita-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/utilita-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/utilita-problem-types.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/utilita-data-model.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/utilita-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/utilita-conformance.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/utilita-domain-security.yml
- group: agent
  title: ''
  type: WellKnownProbe
  url: well-known/utilita-well-known.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/utilita-llms.txt
- group: start
  title: ''
  type: CustomerPortal
  url: https://my.utilita.co.uk/login
- group: start
  title: ''
  type: SignUp
  url: https://join.utilita.co.uk/
- group: commercial
  title: ''
  type: Pricing
  url: https://utilita.co.uk/tariffs
- group: operate
  title: ''
  type: Help
  url: https://utilita.co.uk/help
- group: operate
  title: ''
  type: Support
  url: https://utilita.co.uk/contact
- group: operate
  title: ''
  type: Community
  url: https://community.utilita.co.uk/
- group: company
  title: ''
  type: Blog
  url: https://utilita.co.uk/blog
- group: commercial
  title: ''
  type: TermsOfService
  url: https://utilita.co.uk/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://utilita.co.uk/privacy-notice
- group: other
  title: ''
  type: CookiePolicy
  url: https://utilita.co.uk/cookie-policy
- group: company
  title: ''
  type: Careers
  url: https://utilita.co.uk/careers
- group: company
  title: ''
  type: Press
  url: https://www.luxion.group/utilita-press-corner
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/utilita-energy
created: '2026-07-27'
description: 'Utilita Energy is a United Kingdom household electricity and gas supplier founded in 2003 and headquartered in Eastleigh, Hampshire, specialising in smart Pay As You Go (prepayment) energy for roughly 800,000 mostly lower-income homes. It sits at the retail end of the GB energy value chain — buying wholesale, holding an Ofgem supply licence, and acceding to the Smart Energy Code as a DCC user — and it was the first company in Great Britain to install a residential smart electricity meter (2005) and a combined smart gas and electricity system (2008). Its ENERGY DATA posture is closed on every axis. Britain mandated the smart-meter INFRASTRUCTURE (the Smart DCC, the Smart Energy Code, SMETS1/SMETS2 devices) rather than a consumer data right, so no CDR- or Green-Button-style obligation compels Utilita to publish a customer data API, and it publishes none: no developer portal, no customer usage API, and no open market or grid data — developer., developers., api., docs. and data.utilita.co.uk
  do not resolve, and /developers, /api, /docs, /data and /openapi.json all return 404. Customer usage and top-up data reaches people only through the My Utilita web portal and mobile app behind an account login; third parties reach GB smart-meter data through the DCC "Other User" route under the Data Access and Privacy Framework, not through Utilita. Utilita does, however, run one genuine public API: the anonymous, CORS-open, documented Utilita Status API at status.utilita.co.uk/api/v2, which reports the live health of 21 tracked components — SMETS1/SMETS2 smart meters, Guest Payments, Open Banking, PayPoint and PayZone top-up channels, the My Utilita app and web portal, Power-up, the websites, the contact centre, smart meter installations and the smart metering network — along with incident and scheduled-maintenance history and self-serve webhook, RSS and Atom notifications. Recorded here as an honest closed-supplier baseline for the UK energy sector, with an operational-transparency surface
  that is real and usable.'
examples:
- key_count: 2
  name: Utilita Status Active Maintenances
  slug: utilita-status-active-maintenances
- key_count: 2
  name: Utilita Status Components
  slug: utilita-status-components
- key_count: 2
  name: Utilita Status Status
  slug: utilita-status-status
- key_count: 5
  name: Utilita Status Summary
  slug: utilita-status-summary
- key_count: 2
  name: Utilita Status Unresolved Incidents
  slug: utilita-status-unresolved-incidents
- key_count: 2
  name: Utilita Status Upcoming Maintenances
  slug: utilita-status-upcoming-maintenances
image: https://utilita.co.uk/favicon.ico
layout: provider
modified: '2026-07-27'
name: Utilita
nav: Providers
network: true
overview: 'Utilita publishes 4 APIs on the [APIs.io](https://apis.io/) network, including Components API, Incidents API, Scheduled Maintenance API, and 1 more. Tagged areas include Energy, United Kingdom, Utilities, Electricity, and Gas.


  The Utilita catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Utilita''s developer surface includes documentation, API reference, code examples, authentication, signup flow, pricing, support, and 25 more developer resources.'
random_paper: 8
score:
  band: developing
  composite: 49.7
  coverage:
    artifact_dirs: 16
    catalog_gap: 78.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 44.7
    commercial_clarity: 44.7
    contract_governance: 4.5
    contract_quality: 65.5
    developer_ergonomics: 37.5
    discoverability: 68.5
    governance: 4.5
    operational_transparency: 23.7
  previous_composite: 49.7
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 1
    skills: derived
  regulatory:
    applies: true
    jurisdictions:
    - jurisdiction: GB
      standard: smart-energy-code
    jurisdictions_satisfied: 1
    matched_via: tags
    regime: Energy & Utilities
    regime_id: energy_utilities
    score: 62.2
  schema_version: 0.17.2
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/utilita/refs/heads/main/screenshots/utilita-2026-08-17T082702.png
security:
- kind: authentication
  name: Utilita Authentication
  slug: utilita-authentication
  summary_line: none · 1 scheme
- kind: domain-security
  name: Utilita Domain Security
  slug: utilita-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: utilita
tags:
- Energy
- United Kingdom
- Utilities
- Electricity
- Gas
- Smart Metering
- Prepayment
- Energy Retail
- Status
- Operational Transparency
website: https://utilita.co.uk/
---
