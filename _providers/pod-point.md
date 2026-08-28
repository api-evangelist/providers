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
    openapi_examples: documented
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 6.7
  scored_at: '2026-08-26'
api_count: 1
apis:
- description: 'Pod''s Open Charge Point Interface (OCPI) 2.2.1 service in the Charge Point Operator role, used for e-mobility roaming and as the technical vehicle named by the UK Public Charge Point Regulations 2023 '
  name: Pod OCPI 2.2.1 CPO API
  slug: pod-point-ocpi-cpo-api
artifact_total: 8
common:
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/pod-point-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/pod-point-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://podenergy.com/
- group: company
  title: ''
  type: Blog
  url: https://podenergy.com/news
- group: operate
  title: ''
  type: Support
  url: https://help.pod-point.com/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Pod-Point
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/podpoint
- group: company
  title: ''
  type: Careers
  url: https://careers.pod-point.com/
- group: auth
  title: ''
  type: Security
  url: https://podenergy.com/security
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/pod-point-security.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/pod-point-well-known.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/pod-point-authentication.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/pod-point-conformance.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/pod-point-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/pod-point-error-codes.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/pod-point-lifecycle.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/pod-point-data-model.yml
- group: build
  title: ''
  type: Examples
  url: examples/pod-point-examples.yml
- group: build
  title: ''
  type: Packages
  url: packages/pod-point-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/pod-point-packages.yml
- group: design
  title: ''
  type: Components
  url: components/pod-point-components.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/pod-point-llms.txt
- group: commercial
  title: ''
  type: TermsOfService
  url: https://podenergy.com/general-terms-and-conditions
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://podenergy.com/legal/privacy-notice
created: '2026-07-27'
description: 'Pod Point — trading as Pod since its February 2026 rebrand, with pod-point.com now 301-redirecting to podenergy.com — is a British electric vehicle charging company founded in London in 2009 and wholly owned by EDF since its delisting from the London Stock Exchange in August 2025. It sells and installs home, workplace and fleet chargers, operates the third-largest public charging network in the United Kingdom across Tesco and Lidl car parks, and acquired depot-charging specialist EO Charging in May 2026. It sits on the demand side of the UK electricity value chain, between the driver and the electricity supplier, as a Charge Point Operator rather than a metering, network or settlement body. Its API posture is narrow but real and honestly split: there is no developer portal, no OpenAPI, no Swagger and no consumer data API, yet a live OCPI 2.2.1 Charge Point Operator service runs at ocpi.podenergy.com whose version negotiation answers anonymously and enumerates a full module
  set, while every data module — locations, tariffs, sessions, CDRs — returns 401 Unauthorized without a bilaterally exchanged OCPI credentials token. Britain''s Public Charge Point Regulations 2023 name OCPI 2.2.1 as the vehicle for open charge point data; the plumbing that regulation names is verifiably in place at Pod, but the open part of it is not obtainable anonymously from outside, and the company publishes no open data page, no OCPI token policy and no developer onboarding of any kind.'
examples:
- key_count: 4
  name: Pod Point Ocpi Health
  slug: pod-point-ocpi-health
- key_count: 3
  name: Pod Point Ocpi Unauthorized
  slug: pod-point-ocpi-unauthorized
- key_count: 4
  name: Pod Point Ocpi Version Detail
  slug: pod-point-ocpi-version-detail
- key_count: 4
  name: Pod Point Ocpi Versions
  slug: pod-point-ocpi-versions
image: https://podenergy.com/themes/custom/podpoint/images/favicon-96x96.png
layout: provider
modified: '2026-07-27'
name: Pod Point
nav: Providers
network: true
overview: 'Pod Point publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Energy, United Kingdom, EV Charging, Electric Vehicles, and Utilities.


  Pod Point''s developer surface includes engineering blog, support, authentication, code examples, and 20 more developer resources.'
random_paper: 19
score:
  band: thin
  composite: 29.7
  delta: 2.6
  facets:
    access_clarity: 21.1
    commercial_clarity: 21.1
    contract_governance: 18.2
    contract_quality: 6.7
    developer_ergonomics: 39.3
    discoverability: 87.0
    governance: 18.2
    operational_transparency: 13.2
  previous_composite: 27.1
  provenance:
    conformance: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Energy & Utilities
    regime_id: energy_utilities
    score: 41.9
  schema_version: 0.15.0
  scored_at: '2026-08-26'
  trend: flat
security:
- kind: authentication
  name: Pod Point Authentication
  slug: pod-point-authentication
  summary_line: http · 3 schemes
- kind: domain-security
  name: Pod Point Domain Security
  slug: pod-point-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Pod Point Vulnerability Disclosure
  slug: pod-point-vulnerability-disclosure
  summary_line: Hackerone · security.txt · contact published
slug: pod-point
tags:
- Energy
- United Kingdom
- EV Charging
- Electric Vehicles
- Utilities
- Electricity
- OCPI
- Charge Point Operator
- Smart Charging
- Grid
website: https://podenergy.com/
---
