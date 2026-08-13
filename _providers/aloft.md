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
    auth_clarity: true
    consent_identity: false
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
  score: 38.1
  scored_at: '2026-08-12'
agentic_access:
- acting_count: 99
  human_in_the_loop: 0
  name: Aloft Agentic Access
  operation_count: 180
  slug: aloft-agentic-access
  summary_line: 180 operations · 99 acting
api_count: 36
apis:
- description: Accounts
  name: Aloft Accounts API
  slug: aloft-accounts-api
- description: Activity
  name: Aloft Activity API
  slug: aloft-activity-api
- description: Aircraft
  name: Aloft Aircraft API
  slug: aloft-aircraft-api
- description: AirMesh
  name: Aloft AirMesh API
  slug: aloft-airmesh-api
- description: Airspace
  name: Aloft Airspace API
  slug: aloft-airspace-api
- description: Alert Recipients
  name: Aloft Alert Recipients API
  slug: aloft-alert-recipients-api
- description: Alerts
  name: Aloft Alerts API
  slug: aloft-alerts-api
- description: Application Notices
  name: Aloft Application Notices API
  slug: aloft-application-notices-api
- description: Auth
  name: Aloft Auth API
  slug: aloft-auth-api
- description: Auto Tags
  name: Aloft Auto Tags API
  slug: aloft-auto-tags-api
- description: Batteries
  name: Aloft Batteries API
  slug: aloft-batteries-api
- description: Certification Renewal
  name: Aloft Certification Renewal API
  slug: aloft-certification-renewal-api
- description: Certifications
  name: Aloft Certifications API
  slug: aloft-certifications-api
- description: Checklist Executions
  name: Aloft Checklist Executions API
  slug: aloft-checklist-executions-api
- description: Checklists
  name: Aloft Checklists API
  slug: aloft-checklists-api
- description: Components
  name: Aloft Components API
  slug: aloft-components-api
- description: Connections
  name: Aloft Connections API
  slug: aloft-connections-api
- description: Files
  name: Aloft Files API
  slug: aloft-files-api
- description: Files by Resource
  name: Aloft Files by Resource API
  slug: aloft-files-by-resource-api
- description: Flight Logs
  name: Aloft Flight Logs API
  slug: aloft-flight-logs-api
- description: Flight Sessions
  name: Aloft Flight Sessions API
  slug: aloft-flight-sessions-api
- description: Flights
  name: Aloft Flights API
  slug: aloft-flights-api
- description: Incidents
  name: Aloft Incidents API
  slug: aloft-incidents-api
- description: Maintenance
  name: Aloft Maintenance API
  slug: aloft-maintenance-api
- description: Maintenance Recommendations
  name: Aloft Maintenance Recommendations API
  slug: aloft-maintenance-recommendations-api
- description: Maintenance Schedules (Beta)
  name: Aloft Maintenance Schedules (Beta) API
  slug: aloft-maintenance-schedules-beta-api
- description: Missions
  name: Aloft Missions API
  slug: aloft-missions-api
- description: Notify & Fly
  name: Aloft Notify & Fly API
  slug: aloft-notify-fly-api
- description: Risk Assessment Executions
  name: Aloft Risk Assessment Executions API
  slug: aloft-risk-assessment-executions-api
- description: Risk Assessments
  name: Aloft Risk Assessments API
  slug: aloft-risk-assessments-api
- description: Tag Associations
  name: Aloft Tag Associations API
  slug: aloft-tag-associations-api
- description: Tag Groups
  name: Aloft Tag Groups API
  slug: aloft-tag-groups-api
- description: Tags
  name: Aloft Tags API
  slug: aloft-tags-api
- description: Users
  name: Aloft Users API
  slug: aloft-users-api
- description: VideoStreaming
  name: Aloft VideoStreaming API
  slug: aloft-videostreaming-api
- description: Workflows
  name: Aloft Workflows API
  slug: aloft-workflows-api
artifact_total: 42
common:
- group: other
  title: ''
  type: Overlay
  url: overlays/aloft-openapi-overlay.yaml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/aloft-agentic-access.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/aloft-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/aloft-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/aloft-problem-types.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/aloft-data-model.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/aloft-lifecycle.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://status.aloft.ai
- group: design
  title: ''
  type: Conformance
  url: conformance/aloft-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: https://www.aloft.ai/security/
- group: auth
  title: ''
  type: TrustCenter
  url: security/aloft-trust-center.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/aloft-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: https://www.aloft.ai/security/
- group: auth
  title: ''
  type: DomainSecurity
  url: security/aloft-domain-security.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/aloft-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/aloft-llms.txt
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://www.aloft.ai/developer/
- group: docs
  title: ''
  type: Documentation
  url: https://api.aloft.ai/v1/docs
- group: docs
  title: ''
  type: APIReference
  url: https://api.aloft.ai/v1/docs
- group: operate
  title: ''
  type: Support
  url: https://www.aloft.ai/support/
- group: company
  title: ''
  type: Blog
  url: https://www.aloft.ai/news/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Kittyhawkio
- group: start
  title: ''
  type: Login
  url: https://www.aloft.ai/login/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.aloft.ai/terms/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.aloft.ai/privacy/
created: '2026-07-17'
description: 'Aloft (aloft.ai, formerly Kittyhawk.io) is the leading FAA-approved provider of drone airspace and fleet-management software in the United States, powering the majority of LAANC airspace authorizations and unmanned traffic management (UTM) for government, public-safety, enterprise, and recreational drone pilots. The Aloft API V1 is an http-bearer-authenticated REST API exposing 180 operations across 36 resource groups: airspace advisories and weather, LAANC / Notify & Fly, flights and flight logs, aircraft, batteries and maintenance, missions, risk assessments, checklists, incidents, alerts, files, workflows, and map tile layers. Aloft is SOC 2 Type II and ISO 27001 certified. This profile was enriched by the API Evangelist pipeline from Aloft''s public OpenAPI and developer surface.'
image: https://www.aloft.ai/wp-content/uploads/2019/11/1-2.jpg
layout: provider
mcp_servers:
- description: ''
  name: aloft-mcp.yml
  slug: aloft-mcpyml
modified: '2026-07-18'
name: Aloft
nav: Providers
network: true
overview: 'Aloft publishes 36 APIs on the [APIs.io](https://apis.io/) network, including Accounts API, Activity API, Aircraft API, and 33 more. Tagged areas include Drones, Airspace, UTM, LAANC, and Aviation.


  Aloft''s developer surface includes authentication, documentation, API reference, support, engineering blog, and 21 more developer resources.'
random_paper: 54
score:
  band: developing
  composite: 48.3
  delta: 0.0
  facets:
    commercial_clarity: 50.0
    contract_quality: 58.0
    developer_ergonomics: 45.1
    discoverability: 81.5
    governance: 20.8
    operational_transparency: 31.6
  previous_composite: 48.3
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 36
    mcp: derived
    skills: derived
  schema_version: 0.11.0
  scored_at: '2026-08-12'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/aloft/refs/heads/main/screenshots/aloft-2026-07-25T195743.png
security:
- kind: authentication
  name: Aloft Authentication
  slug: aloft-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Aloft Domain Security
  slug: aloft-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: vulnerability-disclosure
  name: Aloft Vulnerability Disclosure
  slug: aloft-vulnerability-disclosure
  summary_line: contact published
- kind: trust-center
  name: Aloft Trust Center
  slug: aloft-trust-center
  summary_line: SOC 2 Type II, ISO 27001, FAA LAANC
slug: aloft
tags:
- Drones
- Airspace
- UTM
- LAANC
- Aviation
- Fleet Management
- Geospatial
- Public Safety
website: https://www.aloft.ai/developer/
---
