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
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: derived
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 32.7
  scored_at: '2026-08-03'
api_count: 5
apis:
- description: The Apps API from SideQuest — 1 operation(s) for apps.
  name: SideQuest Apps API
  slug: sidequest-apps-api
- description: The Developers API from SideQuest — 1 operation(s) for developers.
  name: SideQuest Developers API
  slug: sidequest-developers-api
- description: The OAuth2 API from SideQuest — 3 operation(s) for oauth2.
  name: SideQuest OAuth2 API
  slug: sidequest-oauth2-api
- description: The Users API from SideQuest — 2 operation(s) for users.
  name: SideQuest Users API
  slug: sidequest-users-api
- description: The UsersApps API from SideQuest — 1 operation(s) for usersapps.
  name: SideQuest UsersApps API
  slug: sidequest-usersapps-api
artifact_total: 9
common:
- group: docs
  title: ''
  type: OpenAPI
  url: openapi/sidequest-openapi.json
- group: auth
  title: ''
  type: Authentication
  url: authentication/sidequest-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/sidequest-scopes.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/sidequest-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/sidequest-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/sidequest-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/sidequest-conformance.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/sidequest-data-model.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/sidequest-openapi-overlay.yaml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/sidequest-mcp.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/sidequest-llms.txt
- group: build
  title: ''
  type: Packages
  url: packages/sidequest-packages.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/sidequest-domain-security.yml
- group: docs
  title: ''
  type: Documentation
  url: https://api.sidequestvr.com/docs
- group: start
  title: ''
  type: DeveloperPortal
  url: https://sidequestvr.com/developers
- group: company
  title: ''
  type: Website
  url: sidequestvr.com
created: '2026-07-17'
description: SideQuest is a VR content-discovery platform and independent app store for Meta Quest, PCVR, Pico, Magic Leap and WebXR headsets — the home of sideload-only, early-access and indie VR apps and games, plus tools to help users get more from their VR headset. SideQuest operates a public REST API (api.sidequestvr.com) for browsing the app catalog and reading user profiles and achievements, secured with OAuth 2.0 bearer tokens and a device-style short-code login. Backed by GV.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/sidequest.png
layout: provider
mcp_servers:
- description: ''
  name: sidequest-mcp.yml
  slug: sidequest-mcpyml
modified: '2026-07-21'
name: SideQuest
nav: Providers
network: true
overview: 'SideQuest publishes 5 APIs on the [APIs.io](https://apis.io/) network, including Apps API, Developers API, OAuth2 API, and 2 more. Tagged areas include Company, Consumer, Virtual Reality, VR, and XR.


  SideQuest''s developer surface includes authentication, documentation, and 15 more developer resources.'
random_paper: 33
scopes:
- name: Sidequest Scopes
  scope_count: 0
  slug: sidequest-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: thin
  composite: 30.7
  delta: 0.0
  facets:
    commercial_clarity: 0.0
    contract_quality: 54.6
    developer_ergonomics: 32.1
    discoverability: 92.6
    governance: 11.5
    operational_transparency: 0.0
  previous_composite: 30.7
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 5
    mcp: derived
    skills: derived
  schema_version: 0.9
  scored_at: '2026-08-03'
  trend: flat
security:
- kind: authentication
  name: Sidequest Authentication
  slug: sidequest-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Sidequest Domain Security
  slug: sidequest-domain-security
  summary_line: TLSv1.3 · DMARC
slug: sidequest
tags:
- Company
- Consumer
- Virtual Reality
- VR
- XR
- Gaming
- App Store
- Developers
website: https://sidequestvr.com/developers
---
