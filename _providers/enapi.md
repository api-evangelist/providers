---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    auth_clarity: true
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
  score: 9.0
  scored_at: '2026-08-06'
api_count: 1
apis:
- description: Enapi's OCPI HUB endpoint for EV charging roaming. Implements the Open Charge Point Interface (OCPI) 2.1.1 / 2.2.1 / 2.3.0 across the Credentials, Locations, Tariffs, Tokens, Sessions, CDRs, Commands,
  name: Enapi OCPI Roaming API
  slug: enapi-ocpi-roaming-api
artifact_total: 3
common:
- group: company
  title: ''
  type: Website
  url: https://enapi.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.enapi.com
- group: docs
  title: ''
  type: Documentation
  url: https://docs.enapi.com
- group: docs
  title: ''
  type: APIReference
  url: https://docs.enapi.com/technical-documentation
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.enapi.com/getting-started
- group: start
  title: ''
  type: Login
  url: https://app.enapi.com/login
- group: start
  title: ''
  type: SignUp
  url: https://calendly.com/enapi/let-s-talk
- group: operate
  title: ''
  type: Support
  url: https://docs.enapi.com/security-compliance-and-slas/incident-management
- group: operate
  title: ''
  type: StatusPage
  url: https://status.enapi.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://enapi.com/terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://enapi.com/privacy-policy
- group: auth
  title: ''
  type: Compliance
  url: https://docs.enapi.com/security-compliance-and-slas/compliance-and-data-residency
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/enapi-llms.txt
- group: auth
  title: ''
  type: Authentication
  url: authentication/enapi-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/enapi-conventions.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/enapi-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/enapi-lifecycle.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/enapi-sandbox.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/enapi-domain-security.yml
created: '2026-07-17'
description: Enapi (ENAPI) operates a unified roaming and clearing platform for the electric vehicle charging industry, brokering transactions between Charge Point Operators (CPOs) and e-Mobility Service Providers (eMSPs). Rather than exposing a proprietary API, Enapi implements the open OCPI (Open Charge Point Interface) standard out-of-the-box across versions 2.1.1, 2.2.1, and 2.3.0, operating as an OCPI HUB that handles version interoperability, message routing, and endpoint fan-out on behalf of partners. Its three product lines are Roaming (peer-to-peer commercial connections while Enapi handles the technical integration), Technical (standardized OCPI onboarding with automated testing and a staging environment), and Financial CDR Clearing (real-time Charge Detail Record validation, dispute flagging, and settlement). As of early 2024 the platform connects over 700,000 charge points and works with most major eMSPs including partners such as TotalEnergies, ChargePoint, ubitricity, Plugsurfing,
  Monta, and Eneco.
image: https://enapi.com/media/pages/home/6908c67d54-1749641656/enapi_blue_inverse-web-1000x.png
layout: provider
modified: '2026-07-19'
name: Enapi
nav: Providers
network: true
overview: 'Enapi publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, EV Charging, OCPI, Roaming, and E-Mobility.


  Enapi''s developer surface includes documentation, API reference, getting-started guide, signup flow, support, authentication, sandbox, and 12 more developer resources.'
random_paper: 73
score:
  band: thin
  composite: 32.5
  delta: 0.0
  facets:
    commercial_clarity: 42.1
    contract_quality: 0.0
    developer_ergonomics: 56.5
    discoverability: 75.9
    governance: 12.5
    operational_transparency: 15.8
  previous_composite: 32.5
  provenance:
    conformance: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Telecommunications
    regime_id: telecommunications
    score: 41.7
  schema_version: 0.9.1
  scored_at: '2026-08-06'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/enapi/refs/heads/main/screenshots/enapi-2026-07-25T213259.png
security:
- kind: authentication
  name: Enapi Authentication
  slug: enapi-authentication
  summary_line: ocpi-token · 1 scheme
- kind: domain-security
  name: Enapi Domain Security
  slug: enapi-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: enapi
tags:
- Company
- EV Charging
- OCPI
- Roaming
- E-Mobility
- Charge Point Operator
- eMSP
- Electric Vehicle
- CDR Clearing
- Interoperability
- Hub
website: https://enapi.com
---
