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
  band: agent-native
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: verified
    event_surface_described: true
    idempotency: documented
    mcp_server: false
    openapi_examples: partial
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 48.9
  scored_at: '2026-08-24'
agentic_access:
- acting_count: 27
  human_in_the_loop: 1
  name: Flock Safety Agentic Access
  operation_count: 43
  slug: flock-safety-agentic-access
  summary_line: 43 operations · 27 acting · 1 human-in-the-loop
api_count: 10
apis:
- description: The Alerts API from Flock Safety — 3 operation(s) for alerts.
  name: Flock Safety Alerts API
  slug: flock-safety-alerts-api
- description: The CAD Events API from Flock Safety — 7 operation(s) for cad events.
  name: Flock Safety CAD Events API
  slug: flock-safety-cad-events-api
- description: The Custom Hotlists API from Flock Safety — 5 operation(s) for custom hotlists.
  name: Flock Safety Custom Hotlists API
  slug: flock-safety-custom-hotlists-api
- description: The Devices API from Flock Safety — 3 operation(s) for devices.
  name: Flock Safety Devices API
  slug: flock-safety-devices-api
- description: The LPR Hotlist Alert Subscriptions API from Flock Safety — 2 operation(s) for lpr hotlist alert subscriptions.
  name: Flock Safety LPR Hotlist Alert Subscriptions API
  slug: flock-safety-lpr-hotlist-alert-subscriptions-api
- description: The OAuth2 API from Flock Safety — 1 operation(s) for oauth2.
  name: Flock Safety OAuth2 API
  slug: flock-safety-oauth2-api
- description: The Plate Reads API from Flock Safety — 2 operation(s) for plate reads.
  name: Flock Safety Plate Reads API
  slug: flock-safety-plate-reads-api
- description: The Tracked Subject Types API from Flock Safety — 2 operation(s) for tracked subject types.
  name: Flock Safety Tracked Subject Types API
  slug: flock-safety-tracked-subject-types-api
- description: The Tracked Subjects API from Flock Safety — 2 operation(s) for tracked subjects.
  name: Flock Safety Tracked Subjects API
  slug: flock-safety-tracked-subjects-api
- description: The Vehicle Images API from Flock Safety — 1 operation(s) for vehicle images.
  name: Flock Safety Vehicle Images API
  slug: flock-safety-vehicle-images-api
artifact_total: 29
asyncapis:
- description: Real-time webhook that delivers Flock Safety LPR (license plate recognition) hotlist alert events. An alert fires when a plate captured by a Flock LPR camera (owned by, or shared within the First Resp
  name: Flock Safety LPR Hotlist Alerts Webhook
  slug: flock-safety-lpr-alerts-asyncapi
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Flock Safety API Platform (v3) Alerts API
  slug: open-flock-safety-alerts-api
- collection_type: open
  name: Flock Safety API Platform (v3) Alerts CAD Events API
  slug: open-flock-safety-cad-events-api
- collection_type: open
  name: Flock Safety API Platform (v3) Alerts Custom Hotlists API
  slug: open-flock-safety-custom-hotlists-api
- collection_type: open
  name: Flock Safety API Platform (v3) Alerts Devices API
  slug: open-flock-safety-devices-api
- collection_type: open
  name: Flock Safety API Platform (v3) Alerts LPR Hotlist Alert Subscriptions API
  slug: open-flock-safety-lpr-hotlist-alert-subscriptions-api
- collection_type: open
  name: Flock Safety API Platform (v3) Alerts OAuth2 API
  slug: open-flock-safety-oauth2-api
- collection_type: open
  name: Flock Safety API Platform (v3) Alerts Plate Reads API
  slug: open-flock-safety-plate-reads-api
- collection_type: open
  name: Flock Safety API Platform (v3) Alerts Tracked Subject Types API
  slug: open-flock-safety-tracked-subject-types-api
- collection_type: open
  name: Flock Safety API Platform (v3) Alerts Tracked Subjects API
  slug: open-flock-safety-tracked-subjects-api
- collection_type: open
  name: Flock Safety API Platform (v3) Alerts Vehicle Images API
  slug: open-flock-safety-vehicle-images-api
common:
- group: other
  title: ''
  type: Overlay
  url: overlays/flock-safety-api-platform-overlay.yaml
- group: auth
  title: ''
  type: TrustCenter
  url: security/flock-safety-trust-center.yml
- group: company
  title: ''
  type: Website
  url: https://flocksafety.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.flocksafety.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.flocksafety.com/developer-hub/docs/flock-developer-platform-overview
- group: docs
  title: ''
  type: APIReference
  url: https://docs.flocksafety.com/developer-hub/reference/post_oauth-token
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.flocksafety.com/developer-hub/docs/quickstart
- group: operate
  title: ''
  type: Support
  url: https://help.flocksafety.com/s/
- group: company
  title: ''
  type: Blog
  url: https://flocksafety.com/blog
- group: operate
  title: ''
  type: StatusPage
  url: https://status.flocksafety.com/
- group: operate
  title: ''
  type: ChangeLog
  url: https://docs.flocksafety.com/developer-hub/changelog
- group: commercial
  title: ''
  type: Pricing
  url: https://flocksafety.com/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://flocksafety.com/legal/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://flocksafety.com/legal/privacy-notice
- group: auth
  title: ''
  type: Compliance
  url: https://security.flocksafety.com/
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/flock-safety-rate-limits.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Flock-Safety
- group: auth
  title: ''
  type: Authentication
  url: authentication/flock-safety-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/flock-safety-scopes.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/flock-safety-conventions.yml
- group: design
  title: ''
  type: Idempotency
  url: conventions/flock-safety-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/flock-safety-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/flock-safety-lifecycle.yml
- group: operate
  title: ''
  type: Deprecation
  url: lifecycle/flock-safety-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/flock-safety-conformance.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/flock-safety-data-model.yml
- group: build
  title: ''
  type: Packages
  url: packages/flock-safety-packages.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/flock-safety-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/flock-safety-llms.txt
- group: auth
  title: ''
  type: DomainSecurity
  url: security/flock-safety-domain-security.yml
- group: docs
  title: ''
  type: AsyncAPI
  url: asyncapi/flock-safety-lpr-alerts-asyncapi.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/flock-safety-lpr-alerts-asyncapi.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/flock-safety-changelog.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/flock-safety-agentic-access.yml
created: '2026-07-17'
description: Flock Safety is a public safety technology company whose platform connects communities, businesses, and law enforcement through crime detection, investigation, and response tools built around license plate recognition (LPR) cameras, audio detection, video, and the FlockOS situational-awareness platform. Its v3 API Platform (api.flocksafety.com) lets approved customer organizations and third-party developers build "Flock Apps" that bring data in (register hardware as devices, ingest vehicle images for detection, push CAD events, alerts, and geolocation telemetry, manage custom hotlists) and connect Flock data out (retrieve devices, look up license plate reads, and subscribe to real-time LPR hotlist alert webhooks). The APIs use OAuth 2.0 with machine-level (client_credentials) and recommended user-level (authorization_code) flows, role-based access control, audit logging, and data-stewardship requirements.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/flock-safety.png
layout: provider
mcp_servers:
- description: ''
  name: Flock Safety MCP Server
  slug: flock-safety-mcp-server
modified: '2026-07-19'
name: Flock Safety
nav: Providers
network: true
overview: 'Flock Safety publishes 10 APIs on the [APIs.io](https://apis.io/) network, including Alerts API, CAD Events API, Custom Hotlists API, and 7 more. Tagged areas include Company, American Dynamism, Public Safety, Law Enforcement, and License Plate Recognition.


  The Flock Safety catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Flock Safety''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, changelog, pricing, and 28 more developer resources.'
random_paper: 6
rate_limits:
- limit_count: 0
  name: Flock Safety Rate Limits
  slug: flock-safety-rate-limits
scopes:
- name: Flock Safety Scopes
  scope_count: 5
  slug: flock-safety-scopes
  summary_line: 5 scopes · clientCredentials
score:
  band: developing
  composite: 49.8
  delta: 0.0
  facets:
    access_clarity: 47.4
    commercial_clarity: 47.4
    contract_governance: 16.7
    contract_quality: 63.0
    developer_ergonomics: 44.6
    discoverability: 81.5
    governance: 16.7
    operational_transparency: 42.1
  previous_composite: 49.8
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 10
    mcp: derived
    skills: derived
  schema_version: 0.12.1
  scored_at: '2026-08-24'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/flock-safety/refs/heads/main/screenshots/flock-safety-2026-07-25T214812.png
security:
- kind: authentication
  name: Flock Safety Authentication
  slug: flock-safety-authentication
  summary_line: http/oauth2 · 2 schemes
- kind: domain-security
  name: Flock Safety Domain Security
  slug: flock-safety-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: trust-center
  name: Flock Safety Trust Center
  slug: flock-safety-trust-center
  summary_line: SOC 2, ISO 27001, ISO 27017, ISO 27018
slug: flock-safety
tags:
- Company
- American Dynamism
- Public Safety
- Law Enforcement
- License Plate Recognition
- LPR
- Physical Security
- Surveillance
- Computer-Vision
- Webhook
- Geolocation
- CAD
website: https://flocksafety.com
---
