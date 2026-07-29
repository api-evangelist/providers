---
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: documented
    idempotency: false
    mcp_server: false
    openapi_examples: documented
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.2
  score: 38.3
  scored_at: '2026-07-28'
api_count: 2
apis:
- description: Chargefox's documented REST API for fleet customers, described by an OpenAPI 3.0.1 contract titled "Fleets API" version 1.0 that the company renders publicly with Redoc at https://app.chargefox.com/de
  name: Chargefox Fleets API
  slug: chargefox-fleets-api
- description: Chargefox's Open Charge Point Interface implementation in the Charge Point Operator role, used for roaming so that another network's drivers can authorise, charge and be billed on Chargefox infrastruc
  name: Chargefox OCPI CPO API
  slug: chargefox-ocpi-cpo-api
artifact_total: 10
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/chargefox-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/chargefox-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://www.chargefox.com/
- group: docs
  title: ''
  type: Documentation
  url: https://app.chargefox.com/developers/docs/getting_started
- group: docs
  title: ''
  type: APIReference
  url: https://app.chargefox.com/developers/docs/fleets
- group: operate
  title: ''
  type: RateLimits
  url: https://app.chargefox.com/developers/docs/rate_limits
- group: other
  title: ''
  type: Application
  url: https://app.chargefox.com/
- group: company
  title: ''
  type: Blog
  url: https://www.chargefox.com/news
- group: operate
  title: ''
  type: Support
  url: https://support.chargefox.com/hc/en-au
- group: operate
  title: ''
  type: Contact
  url: https://www.chargefox.com/get-in-touch
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.chargefox.com/legal/privacy-policy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.chargefox.com/legal/terms-conditions
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/chargefox
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/chargefox
- group: company
  title: ''
  type: About
  url: https://www.chargefox.com/company
- group: start
  title: ''
  type: DeveloperPortal
  url: https://app.chargefox.com/developers/docs
- group: start
  title: ''
  type: GettingStarted
  url: https://app.chargefox.com/developers/docs/getting_started
- group: start
  title: ''
  type: Login
  url: https://app.chargefox.com/users/sign_in
- group: operate
  title: ''
  type: StatusPage
  url: https://www.chargefox.com/status
- group: auth
  title: ''
  type: TrustCenter
  url: https://trust.chargefox.com/
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/chargefox-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/chargefox-conformance.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/chargefox-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/chargefox-problem-types.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/chargefox-data-model.yml
- group: build
  title: ''
  type: Packages
  url: packages/chargefox-packages.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/chargefox-well-known.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/chargefox-llms.txt
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: build
  title: ''
  type: Examples
  url: examples/_index.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/chargefox-fleets-api-overlay.yaml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/chargefox-rate-limits.yml
created: '2026-07-27'
description: 'Chargefox is Australia''s largest public electric-vehicle charging network and, since 2023, a charging software platform rather than a hardware owner. Founded in 2017 and headquartered in Melbourne, it was acquired outright in 2022 by Australian Motoring Services, the joint vehicle of six state motoring clubs — NRMA, RACV, RACQ, RAA, RAC and RACT — which makes it one of the very few member-owned pieces of national energy infrastructure in the country. Its own company page claims 2,200+ public charging plugs, 5,000+ charging sessions a day and 170,000+ app downloads. In the Australian energy value chain it sits downstream of the retailer and the meter: it does not generate, transmit or sell electricity as a licensed retailer, it operates the charge points other businesses, councils and governments own, authorises drivers, meters the session, prices it and settles it. That position is exactly why the Consumer Data Right does not touch it. Chargefox does NOT appear among the 84
  energy data-holder brands on the ACCC CDR Register checked on 2026-07-27 — even though Arcline by RACV, an energy retailer owned by one of Chargefox''s own shareholder clubs, does — so the statutory mandate that produced Australia''s identical fifty-bank banking contract stops at the retail electricity licence and never reaches the charge point. What Chargefox has instead is an entirely voluntary, entirely commercial API posture built on a genuine industry standard. It publishes a real, anonymously readable developer documentation site at https://app.chargefox.com/developers/docs carrying a Redoc-rendered OpenAPI 3.0.1 contract for a four-endpoint Fleets API, and its own rate-limit documentation enumerates a full Open Charge Point Interface CPO implementation across OCPI 2.1.1, 2.2 and 2.2.1 covering locations, sessions, CDRs, tariffs, tokens and commands. Every one of those endpoints is closed. Anonymous probes returned 401 with `WWW-Authenticate: Token realm="Application"` on the OCPI
  paths and 401 on the Fleets paths, and no anonymous locations, tariff or network-status feed of any kind could be found, so Chargefox publishes zero open market data and zero consumer data — a documented standard, fully implemented, entirely behind a commercial gate.'
examples:
- key_count: 2
  name: Chargefox Fleets Invoices 200
  slug: chargefox-fleets-invoices-200
- key_count: 2
  name: Chargefox Fleets Sessions 200
  slug: chargefox-fleets-sessions-200
- key_count: 2
  name: Chargefox Fleets Usage 200
  slug: chargefox-fleets-usage-200
- key_count: 2
  name: Chargefox Fleets Vehicles 200
  slug: chargefox-fleets-vehicles-200
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/chargefox.png
layout: provider
modified: '2026-07-27'
name: Chargefox
nav: Providers
network: true
overview: 'Chargefox publishes 1 API on the [APIs.io](https://apis.io/) network: Fleets API. Tagged areas include Energy, Australia, EV Charging, Electricity, and Utilities.


  Chargefox''s developer surface includes authentication, documentation, API reference, engineering blog, support, getting-started guide, code examples, and 25 more developer resources.'
random_paper: 71
rate_limits:
- limit_count: 25
  name: Chargefox Rate Limits
  slug: chargefox-rate-limits
score:
  band: developing
  composite: 44.6
  delta: -1.1
  facets:
    commercial_clarity: 42.1
    contract_quality: 32.3
    developer_ergonomics: 53.8
    discoverability: 87.0
    governance: 20.8
    operational_transparency: 52.6
  previous_composite: 45.7
  provenance:
    conformance: first-party
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Energy & Utilities
    regime_id: energy_utilities
    score: 40.5
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
security:
- kind: authentication
  name: Chargefox Authentication
  slug: chargefox-authentication
  summary_line: http/custom · 2 schemes
- kind: domain-security
  name: Chargefox Domain Security
  slug: chargefox-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Chargefox Trust Center
  slug: chargefox-trust-center
  summary_line: trust center published
slug: chargefox
tags:
- Energy
- Australia
- EV Charging
- Electricity
- Utilities
- OCPI
- Charge Point Operator
- Roaming
- Fleets
- Mobility
- Charging Sessions
- Electrification
website: https://www.chargefox.com/
---
