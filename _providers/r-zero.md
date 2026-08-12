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
    well_known_catalog: true
  schema_version: 0.2
  score: 3.6
  scored_at: '2026-08-11'
api_count: 2
apis:
- description: CoWorkr's standard REST API for pulling workplace analytical data - historical and current occupancy, utilization and device records for WorkPoints, WorkSpace Counters, WorkHubs, WorkPlaces, FloorPlan
  name: CoWorkr REST API
  slug: coworkr-rest-api
- description: CoWorkr's real-time Stream API. Built on Node.js and DDP (the Meteor Distributed Data Protocol), it pushes utilization sensor updates as they happen - a raw feed used by partner workplace-experience a
  name: CoWorkr Stream API
  slug: coworkr-stream-api
artifact_total: 4
common:
- group: auth
  title: ''
  type: TrustCenter
  url: security/r-zero-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/r-zero-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://rzero.com/
- group: docs
  title: ''
  type: Documentation
  url: https://rzerosystems.zendesk.com/hc/en-us
- group: docs
  title: ''
  type: APIReference
  url: https://rzerosystems.zendesk.com/hc/en-us/sections/4408250694295-API
- group: operate
  title: ''
  type: Support
  url: https://rzerosystems.zendesk.com/hc/en-us
- group: operate
  title: ''
  type: HelpCenter
  url: https://rzerosystems.zendesk.com/hc/en-us
- group: operate
  title: ''
  type: Contact
  url: https://rzero.com/contact/
- group: company
  title: ''
  type: Blog
  url: https://rzero.com/blog/
- group: company
  title: ''
  type: BlogRSS
  url: https://rzero.com/feed/
- group: start
  title: ''
  type: Login
  url: https://app.rzero.com/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://rzero.com/legal/terms-and-conditions/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://rzero.com/legal/privacy-policy/
- group: other
  title: ''
  type: EULA
  url: https://rzero.com/legal/end-user-license-agreement/
- group: auth
  title: ''
  type: Compliance
  url: https://rzero.com/security/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.rzero.com/
- group: company
  title: ''
  type: Careers
  url: https://rzero.com/careers/
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/r-zero-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/r-zero-conformance.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/r-zero-conventions.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/r-zero-data-model.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/r-zero-vocabulary.yml
- group: build
  title: ''
  type: Packages
  url: packages/r-zero-packages.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/r-zero-llms.txt
created: '2026-08-02'
description: 'R-Zero Systems is a San Francisco based building-intelligence company founded in 2020 that combines privacy-first occupancy sensors, indoor-air-quality monitoring and AI to autonomously optimize HVAC ventilation in commercial real estate, healthcare and higher-education buildings, claiming 20-40% HVAC energy savings without retrofits or capital investment. Its software platform, R-Zero Connect, turns raw sensor telemetry into occupancy analytics, space-utilization insights and portfolio reporting. R-Zero acquired the workplace-sensor company CoWorkr, whose platform still carries the company''s developer surface: a REST API for pulling historical workplace utilization data into BI tooling and a Node.js/DDP Stream API that pushes real-time occupancy events into reservation and workplace-experience applications (AgilQuest, Comfy, iOffice Hummingbird, Serraview, Teem, Tactic, Siemens). Both APIs are account-gated - documentation is served inside the authenticated application and
  access is granted on request - so no public OpenAPI, GraphQL, MCP or A2A surface is published.'
image: https://rzero.com/wp-content/uploads/2023/12/r-zero-logo-icon.png
layout: provider
modified: '2026-08-02'
name: R-Zero
nav: Providers
network: true
overview: 'R-Zero publishes 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Smart Buildings, Occupancy, Sensors, and Internet of Things.


  R-Zero''s developer surface includes documentation, API reference, support, engineering blog, and 20 more developer resources.'
random_paper: 27
score:
  band: thin
  composite: 28.5
  delta: 0.7
  facets:
    commercial_clarity: 50.0
    contract_quality: 0.0
    developer_ergonomics: 21.7
    discoverability: 87.0
    governance: 22.9
    operational_transparency: 15.8
  previous_composite: 27.8
  provenance:
    conformance: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Energy & Utilities
    regime_id: energy_utilities
    score: 32.4
  schema_version: 0.11.0
  scored_at: '2026-08-11'
  trend: flat
security:
- kind: domain-security
  name: R Zero Domain Security
  slug: r-zero-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: R Zero Trust Center
  slug: r-zero-trust-center
  summary_line: SOC 2 Type II
slug: r-zero
tags:
- Company
- Smart Buildings
- Occupancy
- Sensors
- Internet of Things
- Indoor Air Quality
- Energy Efficiency
- HVAC
- Analytics
- Commercial Real Estate
- Workplace
website: https://rzero.com/
---
