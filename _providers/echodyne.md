---
access_model:
  confidence: medium
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - authentication
  - scopes
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
    auth_clarity: served
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 10.8
  scored_at: '2026-09-03'
api_count: 2
apis:
- description: EchoWare is Echodyne's software platform for MESA radar. It manages a network of Echodyne radars as a single radar instance with one Track ID per object, and supports headless operation in which a com
  name: EchoWare Radar Management and Data API
  slug: echoware
- description: The Echodyne Customer Portal is the login-gated distribution point for radar software, manuals, tools, the ATAK plugin and support. It runs on Salesforce Experience Cloud and publishes an anonymous Op
  name: Echodyne Customer Portal Identity (OpenID Connect)
  slug: portal-identity
artifact_total: 5
common:
- group: company
  title: ''
  type: Website
  url: https://www.echodyne.com/
- group: other
  title: ''
  type: Company
  url: https://www.echodyne.com/company
- group: docs
  title: ''
  type: Documentation
  url: https://www.echodyne.com/radar-systems/echoware
- group: operate
  title: ''
  type: Support
  url: https://www.echodyne.com/contact
- group: operate
  title: ''
  type: HelpCenter
  url: https://portal.echodyne.com/s/login/
- group: start
  title: ''
  type: Portal
  url: https://portal.echodyne.com/s/login/
- group: start
  title: ''
  type: Login
  url: https://portal.echodyne.com/s/login/
- group: company
  title: ''
  type: Blog
  url: https://www.echodyne.com/newsroom
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.echodyne.com/privacy-policy
- group: build
  title: ''
  type: Library
  url: https://www.echodyne.com/library
- group: other
  title: ''
  type: Events
  url: https://www.echodyne.com/events
- group: company
  title: ''
  type: Careers
  url: https://www.echodyne.com/careers
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/echodyne/
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/echodyne-llms.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/echodyne-well-known.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/echodyne-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/echodyne-scopes.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/echodyne-domain-security.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/echodyne-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/echodyne-lifecycle.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/echodyne-conventions.yml
- group: build
  title: ''
  type: Packages
  url: packages/echodyne-packages.yml
created: '2026-08-01'
description: Echodyne Corp is a Kirkland, Washington radar platform company that designs and manufactures metamaterials electronically scanned array (MESA) radar systems for defense, government, critical infrastructure protection, uncrewed aircraft systems (UAS), advanced air mobility (AAM) and autonomous platforms. Its product line spans the compact K-band EchoGuard 4D surveillance radar, the medium-range Ku-band EchoShield multi-mission 4D radar, the airborne EchoFlight radar, and EchoWare — the software platform that manages a network of radars as a single instance and exposes radar management and data output to external command-and-control systems. Radar data (range-Doppler spectrograms, detections, measurements, tracks and radar status) is delivered in a proprietary format over standard TCP/IP Gigabit and 10 Gbps Ethernet, with multiple data-rich output options available via API. Developer-facing material — API documentation, manuals, tooling and the ATAK plugin — is distributed through
  the login-gated Echodyne Customer Portal rather than a public developer portal, so no machine-readable OpenAPI, AsyncAPI or GraphQL contract is published on the open web.
image: https://cdn.prod.website-files.com/69148caed4c3689c36578812/69149528cc715e60ae698ce0_echodyne-logo.png
layout: provider
modified: '2026-08-01'
name: Echodyne
nav: Providers
network: true
overview: 'Echodyne publishes 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Radar, Defense, Government, and Critical Infrastructure.


  Echodyne''s developer surface includes documentation, support, developer portal, engineering blog, authentication, and 17 more developer resources.'
random_paper: 7
scopes:
- name: Echodyne Scopes
  scope_count: 36
  slug: echodyne-scopes
  summary_line: 36 scopes · authorizationCode/implicit
score:
  band: thin
  composite: 26.6
  coverage:
    artifact_dirs: 12
    catalog_gap: 83.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 23.7
    commercial_clarity: 23.7
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 38.1
    discoverability: 66.7
    governance: 18.2
    operational_transparency: 0.0
  previous_composite: 26.6
  provenance:
    conformance: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Government & Public Sector
    regime_id: government
    score: 57.4
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/echodyne/refs/heads/main/screenshots/echodyne-2026-08-07T164712.png
security:
- kind: authentication
  name: Echodyne Authentication
  slug: echodyne-authentication
  summary_line: openIdConnect/oauth2 · 1 scheme
- kind: domain-security
  name: Echodyne Domain Security
  slug: echodyne-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: echodyne
tags:
- Company
- Radar
- Defense
- Government
- Critical Infrastructure
- Counter-UAS
- Drone Detection
- Sensors
- Situational Awareness
- Aerospace
- Hardware
- Public Safety
website: https://www.echodyne.com/
---
