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
    agentic_access: derived
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: verified
    idempotency: false
    mcp_server: derived
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 38.5
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 15
  human_in_the_loop: 1
  name: Coram Ai Agentic Access
  operation_count: 26
  slug: coram-ai-agentic-access
  summary_line: 26 operations · 15 acting · 1 human-in-the-loop
api_count: 8
apis:
- description: The alerts API from Coram Ai — 5 operation(s) for alerts.
  name: Coram Ai alerts API
  slug: coram-ai-alerts-api
- description: Organize cameras into logical collections for easier management. Camera groups allow you to categorize cameras by location, purpose, or any custom criteria. Use these endpoints to create, update, list
  name: Coram Ai camera-groups API
  slug: coram-ai-camera-groups-api
- description: Manage individual cameras within your organization. Use these endpoints to register new cameras, update camera settings, retrieve camera information and status, move cameras between locations, and del
  name: Coram Ai cameras API
  slug: coram-ai-cameras-api
- description: List access control doors and trigger momentary remote unlocks. The same per-door permission checks the in-app unlock flow runs apply here — a key whose creator cannot unlock a door in the UI cannot u
  name: Coram Ai doors API
  slug: coram-ai-doors-api
- description: Query access control device events (card scans, REX presses, forced-open / held-open alarms, battery alerts, …) and fetch the MP4 video clip recorded by the door's primary camera around an event's tim
  name: Coram Ai events API
  slug: coram-ai-events-api
- description: Manage physical site configurations where cameras and NVRs are deployed. Locations represent your facilities, buildings, or areas. Use these endpoints to create, update, list, and delete locations.
  name: Coram Ai locations API
  slug: coram-ai-locations-api
- description: Control and monitor Network Video Recorders (NVRs) in your infrastructure. NVRs are hardware devices that record and store video from connected cameras. Use these endpoints to register NVRs, update th
  name: Coram Ai nvrs API
  slug: coram-ai-nvrs-api
- description: Bulk-import your school reunification roster — schools, students (with guardians), teachers, staff, and class sections — programmatically, the API equivalent of the in-app CSV upload. Each import is a
  name: Coram Ai reunification API
  slug: coram-ai-reunification-api
artifact_total: 12
common:
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.coram.ai/
- group: docs
  title: ''
  type: Documentation
  url: https://developer.coram.ai/
- group: docs
  title: ''
  type: APIReference
  url: https://developer.coram.ai/
- group: start
  title: ''
  type: GettingStarted
  url: https://developer.coram.ai/
- group: auth
  title: ''
  type: Authentication
  url: authentication/coram-ai-authentication.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/coram-ai-mcp.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/coram-ai-agentic-access.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/coram-ai-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/coram-ai-error-codes.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/coram-ai-data-model.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/coram-ai-conformance.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/coram-ai-openapi-overlay.yaml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/coram-ai-llms.txt
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/coram-ai-lifecycle.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://status.coram.ai
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/coram-ai-changelog.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/coram-ai-domain-security.yml
- group: company
  title: ''
  type: Blog
  url: https://www.coram.ai/blog
- group: operate
  title: ''
  type: Support
  url: https://help.coram.ai/en/
- group: start
  title: ''
  type: SignUp
  url: https://app.coram.ai
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.coram.ai/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.coram.ai/privacy-policy
- group: company
  title: ''
  type: Website
  url: https://coram.ai
created: '2026-07-17'
description: Coram AI is an AI-native unified physical security platform that brings video surveillance, access control, emergency management, and visitor verification into a single cloud system that works with existing IP cameras. Its Developer API offers programmatic access to cameras, camera groups, NVRs, locations, access-control doors and events, and firearm-detection alerts, plus bulk school-reunification roster imports. Features include natural-language AI video search, firearm and fall detection, license plate and facial recognition, tailgating alerts, and remote door unlock. Coram is backed by 8VC and Battery Ventures.
image: https://cdn.prod.website-files.com/630e00312de75c578a95ebfb/6a1ed1f27828fd211e840fd7_Open%20Graph.png
layout: provider
mcp_servers:
- description: ''
  name: coram-ai-mcp.yml
  slug: coram-ai-mcpyml
modified: '2026-07-18'
name: Coram Ai
nav: Providers
network: true
overview: 'Coram Ai publishes 8 APIs on the [APIs.io](https://apis.io/) network, including alerts API, camera-groups API, cameras API, and 5 more. Tagged areas include Company, Physical Security, Video Surveillance, Access Control, and Artificial Intelligence.


  Coram Ai''s developer surface includes documentation, API reference, getting-started guide, authentication, changelog, engineering blog, support, and 17 more developer resources.'
random_paper: 7
score:
  band: developing
  composite: 45.7
  delta: -2.2
  facets:
    commercial_clarity: 34.2
    contract_quality: 55.9
    developer_ergonomics: 56.0
    discoverability: 81.5
    governance: 11.5
    operational_transparency: 31.6
  previous_composite: 47.9
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 8
    mcp: derived
    skills: derived
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/coram-ai/refs/heads/main/screenshots/coram-ai-2026-07-25T210425.png
security:
- kind: authentication
  name: Coram Ai Authentication
  slug: coram-ai-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Coram Ai Domain Security
  slug: coram-ai-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: coram-ai
tags:
- Company
- Physical Security
- Video Surveillance
- Access Control
- Artificial Intelligence
- Security Cameras
- Emergency Management
- Computer Vision
website: https://coram.ai
---
