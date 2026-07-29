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
    asyncapi_events: true
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: verified
    idempotency: false
    mcp_server: derived
    openapi_examples: partial
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 44.8
  scored_at: '2026-07-28'
api_count: 4
apis:
- description: '**Powerful generic endpoints** for reading and writing any collection type. Works with all collections using field UUIDs. Query `/fields` first to discover the schema, then use these endpoints for fle'
  name: Teambridge Collections (Unified API) API
  slug: teambridge-collections-unified-api-api
- description: Endpoints for uploading and managing documents.
  name: Teambridge Documents API
  slug: teambridge-documents-api
- description: Endpoints for managing external system mappings. Mappings link Teambridge records to entities in external systems (like Bullhorn, ADP, etc.) by storing the external provider code, external ID, and obj
  name: Teambridge Mappings API
  slug: teambridge-mappings-api
- description: Utility endpoints for timezone information and other general-purpose data.
  name: Teambridge Utilities API
  slug: teambridge-utilities-api
artifact_total: 10
asyncapis:
- description: ''
  name: Teambridge Webhooks
  slug: teambridge-webhooks
common:
- group: company
  title: ''
  type: Website
  url: https://teambridge.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.teambridge.com
- group: docs
  title: ''
  type: Documentation
  url: https://docs.teambridge.com
- group: docs
  title: ''
  type: APIReference
  url: https://docs.teambridge.com
- group: auth
  title: ''
  type: Authentication
  url: authentication/teambridge-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/teambridge-scopes.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/teambridge-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/teambridge-problem-types.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/teambridge-webhooks.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/teambridge-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/teambridge-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: https://security.teambridge.com/
- group: design
  title: ''
  type: DataModel
  url: data-model/teambridge-data-model.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/teambridge-external-api-overlay.yaml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/teambridge-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/teambridge-llms.txt
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/teambridge-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/teambridge-domain-security.yml
- group: commercial
  title: ''
  type: Pricing
  url: https://teambridge.com/pricing
- group: company
  title: ''
  type: Blog
  url: https://teambridge.com/blog
- group: start
  title: ''
  type: Login
  url: https://app.teambridge.com
- group: start
  title: ''
  type: SignUp
  url: https://teambridge.com/book-demo
- group: commercial
  title: ''
  type: TermsOfService
  url: https://teambridge.com/terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://teambridge.com/privacy-policy
created: '2026-07-17'
description: Teambridge is an AI-native workforce-management platform for frontline and hourly teams, unifying scheduling, time tracking, instant pay, team communication, onboarding, compliance, and payroll behind autonomous AI agents. For integrators it publishes the Teambridge External API, a unified Collections API (OpenAPI 3.1.0) that reads and writes shifts, users, placements, locations, and custom collections, authenticated with OAuth 2.0 client credentials and complemented by HMAC-signed outbound webhooks for real-time change notification. Teambridge is backed by General Catalyst and Mayfield and reports SOC 2 Type II, ISO 27001, HIPAA, and GDPR compliance.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/teambridge.png
layout: provider
mcp_servers:
- description: ''
  name: teambridge-mcp.yml
  slug: teambridge-mcpyml
modified: '2026-07-21'
name: Teambridge
nav: Providers
network: true
overview: 'Teambridge publishes 4 APIs on the [APIs.io](https://apis.io/) network, including Collections (Unified API) API, Documents API, Mappings API, and 1 more. Tagged areas include Company, Workforce Management, Scheduling, Time Tracking, and Payroll.


  The Teambridge catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Teambridge''s developer surface includes documentation, API reference, authentication, pricing, engineering blog, signup flow, and 19 more developer resources.'
random_paper: 4
scopes:
- name: Teambridge Scopes
  scope_count: 1
  slug: teambridge-scopes
  summary_line: 1 scope · clientCredentials
score:
  band: developing
  composite: 50.1
  delta: -0.7
  facets:
    commercial_clarity: 60.5
    contract_quality: 68.2
    developer_ergonomics: 40.8
    discoverability: 92.6
    governance: 20.8
    operational_transparency: 7.9
  previous_composite: 50.8
  provenance:
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 4
    mcp: derived
    skills: derived
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
security:
- kind: authentication
  name: Teambridge Authentication
  slug: teambridge-authentication
  summary_line: apiKey/oauth2 · 2 schemes
- kind: domain-security
  name: Teambridge Domain Security
  slug: teambridge-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Teambridge Trust Center
  slug: teambridge-trust-center
  summary_line: SOC 2, ISO 27001, HIPAA, GDPR
slug: teambridge
tags:
- Company
- Workforce Management
- Scheduling
- Time Tracking
- Payroll
- HR
- Frontline
- Webhooks
website: https://teambridge.com
---
