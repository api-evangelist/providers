---
access_model:
  confidence: low
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - authentication
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
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
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 23.6
  scored_at: '2026-09-04'
agentic_access:
- acting_count: 12
  human_in_the_loop: 0
  name: Afero Agentic Access
  operation_count: 25
  slug: afero-agentic-access
  summary_line: 25 operations · 12 acting
api_count: 1
apis:
- baseURL: https://api.afero.io
  baseurl_source: declared
  description: The OAuth 2.0 token endpoint for the Afero Cloud. A partner authenticates with HTTP Basic using the OAuth Client ID and Client Secret issued in the Afero Profile Editor, posts the end-user credentials
  name: Afero Cloud Authentication API
  slug: authentication-api
- baseURL: https://api.afero.io
  baseurl_source: declared
  description: 'The Afero Cloud Users API returns the profile of the authenticated end-user: the Afero accounts the user can access and the privileges held on each, the sign-in credential and its verification state, '
  name: Afero Cloud Users API
  slug: users-api
- baseURL: https://api.afero.io
  baseurl_source: declared
  description: The Afero Cloud Devices API lists the devices linked to an Afero account and, via the expansions query parameter, returns device state (available, visible, connected, connectable, linked, RSSI, locati
  name: Afero Cloud Devices API
  slug: devices-api
- baseURL: https://api.afero.io
  baseurl_source: declared
  description: 'The Afero Over-the-Air (OTA) Update API lets a partner drive firmware releases from their own CI/CD pipeline instead of the OTA Manager web application. It creates and updates partner firmware types, '
  name: Afero Cloud OTA Firmware API
  slug: ota-api
artifact_total: 13
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Afero Cloud Authentication API
  slug: open-afero-authentication-api
- collection_type: open
  name: Afero Cloud Devices API
  slug: open-afero-devices-api
- collection_type: open
  name: Afero Cloud Firmware OTA API
  slug: open-afero-ota-api
- collection_type: open
  name: Afero Cloud Users API
  slug: open-afero-users-api
common:
- group: agent
  title: ''
  type: X-MCPServerCandidate
  url: mcp/afero-mcp.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/afero-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/afero-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/afero-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/afero-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://www.afero.io/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://afero-docs.readthedocs.io/en/latest/
- group: docs
  title: ''
  type: Documentation
  url: https://afero-docs.readthedocs.io/en/latest/
- group: docs
  title: ''
  type: APIReference
  url: https://afero-docs.readthedocs.io/en/latest/CloudAPIs/
- group: start
  title: ''
  type: GettingStarted
  url: https://afero-docs.readthedocs.io/en/latest/Tutorials/
- group: start
  title: ''
  type: Console
  url: https://console.afero.io/
- group: start
  title: ''
  type: Login
  url: https://console.afero.io/
- group: operate
  title: ''
  type: Support
  url: https://www.afero.io/html/home/contact-afero.html
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/aferodeveloper
- group: company
  title: ''
  type: Blog
  url: https://www.afero.io/html/home/news.html
- group: other
  title: ''
  type: WhitePapers
  url: https://www.afero.io/html/home/whitepapers.html
- group: commercial
  title: ''
  type: TermsOfService
  url: https://cdn.afero.io/tos/developer/v1/developer.html
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.afero.io/html/home/privacy.html
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/afero
- group: build
  title: ''
  type: Packages
  url: packages/afero-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/afero-packages.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/afero-well-known.yml
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/afero-security.txt
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/afero-llms.txt
- group: design
  title: ''
  type: Conventions
  url: conventions/afero-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/afero-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/afero-lifecycle.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/afero-changelog.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/afero-conformance.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/afero-data-model.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: auth
  title: ''
  type: Security
  url: https://afero.io/html/home/VDP.html
- group: operate
  title: ''
  type: ReleaseNotes
  url: https://afero-docs.readthedocs.io/en/latest/RelNotes/
- group: other
  title: ''
  type: Overlay
  url: overlays/afero-cloud-api-overlay.yaml
created: '2026-08-02'
description: 'Afero, Inc. is a Los Altos, California IoT platform company founded in 2014 by Joe Britt and Shin Matsumura. Afero ships an end-to-end connected-product stack: ASR secure radio modules with a hardware root of trust and an embedded Hardware Security Module, the afLib MCU libraries and Secure Linux Device SDK for firmware, a Bluetooth Low Energy and Wi-Fi onboarding path, the Afero Profile Editor low-code device-modeling tool, Java (Android) and Swift (iOS) mobile SDKs with a Softhub, and the Afero Cloud — a RESTful API at api.afero.io that lists accounts and devices, reports real-time device state, executes attribute read and write actions on connected devices, and drives the over-the-air firmware pipeline. Afero has raised $73.2M from investors including Samsung Catalyst Fund and Crosspoint Capital Partners and reports millions of deployed devices across 200+ product categories in consumer, enterprise and industrial markets.'
image: https://cdn.afero.io/social/afero_logo_114x114.png
layout: provider
modified: '2026-08-02'
name: Afero
nav: Providers
network: true
overview: 'Afero publishes 4 APIs on the [APIs.io](https://apis.io/) network, including Cloud Authentication API, Cloud Users API, Cloud Devices API, and 1 more. Tagged areas include Company, Internet of Things, IoT Platform, Connected Devices, and Device Management.


  Afero''s developer surface includes authentication, documentation, API reference, getting-started guide, developer console, support, engineering blog, and 27 more developer resources.'
random_paper: 0
score:
  band: thin
  composite: 39.0
  coverage:
    artifact_dirs: 19
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 34.2
    commercial_clarity: 34.2
    contract_governance: 4.5
    contract_quality: 14.9
    developer_ergonomics: 66.1
    discoverability: 75.9
    governance: 4.5
    operational_transparency: 28.9
  previous_composite: 39.0
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 4
      marker_coverage: 100.0
      total: 4
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Energy & Utilities
    regime_id: energy_utilities
    score: 41.9
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/afero/refs/heads/main/screenshots/afero-2026-08-07T161019.png
security:
- kind: authentication
  name: Afero Authentication
  slug: afero-authentication
  summary_line: http/oauth2 · 2 schemes
- kind: domain-security
  name: Afero Domain Security
  slug: afero-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Afero Vulnerability Disclosure
  slug: afero-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: afero
tags:
- Company
- Internet of Things
- IoT Platform
- Connected Devices
- Device Management
- Firmware
- Over-the-Air Updates
- Bluetooth Low Energy
- Embedded Security
- Hardware
website: https://www.afero.io/
---
