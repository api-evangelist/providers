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
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: true
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 31.8
  scored_at: '2026-08-26'
api_count: 1
apis:
- description: 'REST API v3 for the Eagle Eye Networks cloud VMS: devices (bridges, cameras, speakers, switches, multi-cameras), live and recorded media streaming, archiving/exports/downloads, locations/floors/layout'
  name: Eagle Eye Video API Platform (v3)
  slug: eagle-eye-video-api-platform-v3
artifact_total: 6
asyncapis:
- description: ''
  name: Eagle Eye Networks Events Webhooks
  slug: eagle-eye-networks-events-webhooks
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/eagle-eye-networks-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.een.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.eagleeyenetworks.com/
- group: docs
  title: ''
  type: Documentation
  url: https://developer.eagleeyenetworks.com/docs/getting-started
- group: docs
  title: ''
  type: APIReference
  url: https://developer.eagleeyenetworks.com/reference
- group: start
  title: ''
  type: GettingStarted
  url: https://developer.eagleeyenetworks.com/docs/getting-started
- group: company
  title: ''
  type: Blog
  url: https://www.een.com/blog/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/EENCloud
- group: operate
  title: ''
  type: StatusPage
  url: https://status.eagleeyenetworks.com/
- group: operate
  title: ''
  type: Deprecation
  url: https://developer.eagleeyenetworks.com/docs/legacy-apis
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.een.com/privacy-policy/
- group: operate
  title: ''
  type: ChangeLog
  url: https://developer.eagleeyenetworks.com/changelog
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/eagle-eye-networks-changelog.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/eagle-eye-networks-llms.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/eagle-eye-networks-well-known.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/eagle-eye-networks-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/eagle-eye-networks-scopes.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/eagle-eye-networks-conventions.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/eagle-eye-networks-lifecycle.yml
- group: build
  title: ''
  type: Packages
  url: packages/eagle-eye-networks-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/eagle-eye-networks-packages.yml
- group: build
  title: ''
  type: CLI
  url: cli/eagle-eye-networks-cli.yml
- group: design
  title: ''
  type: Components
  url: components/eagle-eye-networks-components.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/eagle-eye-networks-mcp.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/eagle-eye-networks-events-webhooks.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/eagle-eye-networks-problem-types.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/eagle-eye-networks-data-model.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/eagle-eye-networks-conformance.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-07-17'
description: Eagle Eye Networks is a cloud video surveillance and video management system (VMS) provider whose Video API Platform (v3) exposes REST APIs for managing bridges, cameras, speakers, switches and multi-cameras; streaming live and recorded video (HLS, RTSP, MP4, WebRTC two-way audio); archiving, exporting and downloading media; locations, floors, floor plans and layouts; events, alerts, notifications and automations; video analytics deep search, license plate recognition (LPR) and vehicle surveillance; and account, user, role, application and OAuth client management. Authentication is OAuth 2.0 (authorization code, client credentials, refresh token, device code) issued from auth.eagleeyenetworks.com, and the platform ships first-party SDKs (Android/iOS/Web video, two-way audio), an een CLI, webhook event subscriptions and an llms.txt for agent consumption.
image: https://www.een.com/wp-content/uploads/2017/08/Eagle-Eye-Devices-4.png
layout: provider
mcp_servers:
- description: Candidate MCP server surfacing the Eagle Eye Video API Platform (v3) operations as tools. No official hosted Eagle Eye MCP server was found at capture time; this tool list is derived from documented A
  name: Eagle Eye Networks MCP Server
  slug: eagle-eye-networks-mcp-server
modified: '2026-07-18'
name: Eagle Eye Networks
nav: Providers
network: true
overview: 'Eagle Eye Networks publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Security, Video Surveillance, Video Management, and Cloud Video.


  The Eagle Eye Networks catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Eagle Eye Networks'' developer surface includes documentation, API reference, getting-started guide, engineering blog, changelog, authentication, CLI, and 22 more developer resources.'
random_paper: 10
scopes:
- name: Eagle Eye Networks Scopes
  scope_count: 4
  slug: eagle-eye-networks-scopes
  summary_line: 4 scopes · authorizationCode/clientCredentials
score:
  band: thin
  composite: 38.5
  delta: 0.0
  facets:
    access_clarity: 10.5
    commercial_clarity: 10.5
    contract_governance: 18.2
    contract_quality: 42.7
    developer_ergonomics: 49.4
    discoverability: 87.0
    governance: 18.2
    operational_transparency: 38.2
  previous_composite: 38.5
  provenance:
    conformance: first-party
    mcp: derived
    skills: derived
  schema_version: 0.15.0
  scored_at: '2026-08-26'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/eagle-eye-networks/refs/heads/main/screenshots/eagle-eye-networks-2026-07-25T212634.png
security:
- kind: authentication
  name: Eagle Eye Networks Authentication
  slug: eagle-eye-networks-authentication
  summary_line: oauth2/openIdConnect · 2 schemes
- kind: domain-security
  name: Eagle Eye Networks Domain Security
  slug: eagle-eye-networks-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: eagle-eye-networks
tags:
- Company
- Security
- Video Surveillance
- Video Management
- Cloud Video
- Camera
- Physical Security
- Video Analytics
- License Plate Recognition
- Streaming
- Webhook
- Authentication
website: https://www.een.com/
---
