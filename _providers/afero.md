---
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    auth_clarity: true
    consent_identity: true
    dry_run_mode: false
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: derived
    openapi_examples: partial
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 40.8
  scored_at: '2026-08-12'
agentic_access:
- acting_count: 12
  human_in_the_loop: 0
  name: Afero Agentic Access
  operation_count: 25
  slug: afero-agentic-access
  summary_line: 25 operations · 12 acting
api_count: 4
apis:
- description: The OAuth 2.0 token endpoint for the Afero Cloud. A partner authenticates with HTTP Basic using the OAuth Client ID and Client Secret issued in the Afero Profile Editor, posts the end-user credentials
  name: Afero Cloud Authentication API
  slug: authentication-api
- description: 'The Afero Cloud Users API returns the profile of the authenticated end-user: the Afero accounts the user can access and the privileges held on each, the sign-in credential and its verification state, '
  name: Afero Cloud Users API
  slug: users-api
- description: The Afero Cloud Devices API lists the devices linked to an Afero account and, via the expansions query parameter, returns device state (available, visible, connected, connectable, linked, RSSI, locati
  name: Afero Cloud Devices API
  slug: devices-api
- description: 'The Afero Over-the-Air (OTA) Update API lets a partner drive firmware releases from their own CI/CD pipeline instead of the OTA Manager web application. It creates and updates partner firmware types, '
  name: Afero Cloud OTA Firmware API
  slug: ota-api
artifact_total: 9
common:
- group: agent
  title: ''
  type: MCPServer
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
mcp_servers:
- description: ''
  name: afero-mcp.yml
  slug: afero-mcpyml
modified: '2026-08-02'
name: Afero
nav: Providers
network: true
overview: 'Afero publishes 4 APIs on the [APIs.io](https://apis.io/) network, including Cloud Authentication API, Cloud Users API, Cloud Devices API, and 1 more. Tagged areas include Company, Internet of Things, IoT Platform, Connected Devices, and Device Management.


  Afero''s developer surface includes authentication, documentation, API reference, getting-started guide, developer console, support, engineering blog, and 27 more developer resources.'
random_paper: 45
score:
  band: developing
  composite: 49.0
  delta: 0.0
  facets:
    commercial_clarity: 34.2
    contract_quality: 63.8
    developer_ergonomics: 69.0
    discoverability: 81.5
    governance: 11.5
    operational_transparency: 31.6
  previous_composite: 49.0
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 4
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Energy & Utilities
    regime_id: energy_utilities
    score: 41.9
  schema_version: 0.11.0
  scored_at: '2026-08-12'
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
