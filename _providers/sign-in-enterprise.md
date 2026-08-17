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
    event_surface_described: derived
    idempotency: documented
    mcp_server: derived
    openapi_examples: verified
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 50.2
  scored_at: '2026-08-17'
agentic_access:
- acting_count: 18
  human_in_the_loop: 0
  name: Sign In Enterprise Agentic Access
  operation_count: 43
  slug: sign-in-enterprise-agentic-access
  summary_line: 43 operations · 18 acting
api_count: 14
apis:
- description: All endpoints related to the AuditLog model.
  name: Sign In Enterprise AuditLogs API
  slug: sign-in-enterprise-auditlogs-api
- description: All endpoints related to Batch-type actions.
  name: Sign In Enterprise Batches API
  slug: sign-in-enterprise-batches-api
- description: All endpoints related to Capacity management.
  name: Sign In Enterprise Capacities API
  slug: sign-in-enterprise-capacities-api
- description: All endpoints relating to operations for the EmailTemplate model
  name: Sign In Enterprise EmailTemplates API
  slug: sign-in-enterprise-emailtemplates-api
- description: All endpoints related to Group Visits (Appointments).
  name: Sign In Enterprise GroupVisits API
  slug: sign-in-enterprise-groupvisits-api
- description: All endpoints relating to the Host model
  name: Sign In Enterprise Hosts API
  slug: sign-in-enterprise-hosts-api
- description: All endpoints relating to the Invite model
  name: Sign In Enterprise Invites API
  slug: sign-in-enterprise-invites-api
- description: All endpoints relating to the Location model, aka. DeviceConfigurations
  name: Sign In Enterprise Locations API
  slug: sign-in-enterprise-locations-api
- description: All endpoints relating to the Packages model
  name: Sign In Enterprise Packages API
  slug: sign-in-enterprise-packages-api
- description: All endpoint related to the parking feature, including the ParkingLot and ParkingStallRange models
  name: Sign In Enterprise Parking API
  slug: sign-in-enterprise-parking-api
- description: All endpoints related to Registrations.
  name: Sign In Enterprise Registrations API
  slug: sign-in-enterprise-registrations-api
- description: All endpoints related to models that track signing in and out of a location. E.g., Signin, Signout, SigninAcknowledgment models
  name: Sign In Enterprise Signins API
  slug: sign-in-enterprise-signins-api
- description: All endpoints related to the User model
  name: Sign In Enterprise Users API
  slug: sign-in-enterprise-users-api
- description: All endpoint related to the Watchlist model
  name: Sign In Enterprise Watchlists API
  slug: sign-in-enterprise-watchlists-api
artifact_total: 36
asyncapis:
- description: ''
  name: Sign In Enterprise Webhooks
  slug: sign-in-enterprise-webhooks
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Sign In Solutions VMS AuditLogs API
  slug: open-sign-in-enterprise-auditlogs-api
- collection_type: open
  name: Sign In Solutions VMS AuditLogs Batches API
  slug: open-sign-in-enterprise-batches-api
- collection_type: open
  name: Sign In Solutions VMS AuditLogs Capacities API
  slug: open-sign-in-enterprise-capacities-api
- collection_type: open
  name: Sign In Solutions VMS AuditLogs EmailTemplates API
  slug: open-sign-in-enterprise-emailtemplates-api
- collection_type: open
  name: Sign In Solutions VMS AuditLogs GroupVisits API
  slug: open-sign-in-enterprise-groupvisits-api
- collection_type: open
  name: Sign In Solutions VMS AuditLogs Hosts API
  slug: open-sign-in-enterprise-hosts-api
- collection_type: open
  name: Sign In Solutions VMS AuditLogs Invites API
  slug: open-sign-in-enterprise-invites-api
- collection_type: open
  name: Sign In Solutions VMS AuditLogs Locations API
  slug: open-sign-in-enterprise-locations-api
- collection_type: open
  name: Sign In Solutions VMS AuditLogs Packages API
  slug: open-sign-in-enterprise-packages-api
- collection_type: open
  name: Sign In Solutions VMS AuditLogs Parking API
  slug: open-sign-in-enterprise-parking-api
- collection_type: open
  name: Sign In Solutions VMS AuditLogs Registrations API
  slug: open-sign-in-enterprise-registrations-api
- collection_type: open
  name: Sign In Solutions VMS AuditLogs Signins API
  slug: open-sign-in-enterprise-signins-api
- collection_type: open
  name: Sign In Solutions VMS AuditLogs Users API
  slug: open-sign-in-enterprise-users-api
- collection_type: open
  name: Sign In Solutions VMS AuditLogs Watchlists API
  slug: open-sign-in-enterprise-watchlists-api
common:
- group: other
  title: ''
  type: Overlay
  url: overlays/sign-in-enterprise-guest-api-overlay.yaml
- group: auth
  title: ''
  type: TrustCenter
  url: security/sign-in-enterprise-trust-center.yml
- group: company
  title: ''
  type: Website
  url: https://signinsolutions.com/signinenterprise
- group: start
  title: ''
  type: DeveloperPortal
  url: https://signinsolutions.com/developer-api
- group: docs
  title: ''
  type: Documentation
  url: https://developers.signinenterprise.com/
- group: docs
  title: ''
  type: APIReference
  url: https://developers.signinenterprise.com/
- group: commercial
  title: ''
  type: Pricing
  url: https://signinsolutions.com/pricing
- group: company
  title: ''
  type: Blog
  url: https://signinsolutions.com/blog
- group: operate
  title: ''
  type: Support
  url: https://help.signinsolutions.com/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://signinsolutions.com/privacy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://signinsolutions.com/terms-and-conditions
- group: start
  title: ''
  type: Login
  url: https://us.tractionguest.com/users/sign_in
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/tractionguest
- group: auth
  title: ''
  type: Compliance
  url: https://signinsolutions.com/compliance-hub
- group: build
  title: ''
  type: Packages
  url: packages/sign-in-enterprise-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/sign-in-enterprise-packages.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/sign-in-enterprise-well-known.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/sign-in-enterprise-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/sign-in-enterprise-scopes.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/sign-in-enterprise-conventions.yml
- group: design
  title: ''
  type: Idempotency
  url: conventions/sign-in-enterprise-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/sign-in-enterprise-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/sign-in-enterprise-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/sign-in-enterprise-conformance.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/sign-in-enterprise-data-model.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/sign-in-enterprise-webhooks.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/sign-in-enterprise-mcp.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/sign-in-enterprise-agentic-access.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/sign-in-enterprise-llms.txt
- group: auth
  title: ''
  type: DomainSecurity
  url: security/sign-in-enterprise-domain-security.yml
created: '2026-07-17'
description: 'Sign In Enterprise (formerly Traction Guest, now part of Sign In Solutions) is an enterprise visitor management system (VMS) used by security-conscious organizations in aerospace and defense, government, manufacturing, pharmaceuticals, and technology. Its REST API — branded "Guest Connect" and published as the Sign In Solutions VMS API — lets developers retrieve and modify visitor and employee sign-in data to extend workflows: managing hosts, invites, sign-ins, registrations, locations, capacities, parking, group visits, watchlists, email templates, and audit logs. The API is REST over JSON, secured with OAuth 2.0 / OpenID Connect scoped access, and supports idempotent writes via an Idempotency-Key header.'
image: https://signinsolutions.com/hubfs/Creatives/Logos/Sign%20In%20Solutions%20Logo.svg
layout: provider
mcp_servers:
- description: ''
  name: sign-in-enterprise-mcp.yml
  slug: sign-in-enterprise-mcpyml
modified: '2026-07-21'
name: Sign In Enterprise
nav: Providers
network: true
overview: 'Sign In Enterprise publishes 14 APIs on the [APIs.io](https://apis.io/) network, including AuditLogs API, Batches API, Capacities API, and 11 more. Tagged areas include Company, Vertical Software, Visitor Management, Physical Security, and Workplace Experience.


  The Sign In Enterprise catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Sign In Enterprise''s developer surface includes documentation, API reference, pricing, engineering blog, support, authentication, and 25 more developer resources.'
random_paper: 39
scopes:
- name: Sign In Enterprise Scopes
  scope_count: 48
  slug: sign-in-enterprise-scopes
  summary_line: 48 scopes · authorizationCode
score:
  band: developing
  composite: 52.0
  delta: 0.0
  facets:
    commercial_clarity: 60.5
    contract_quality: 68.9
    developer_ergonomics: 51.6
    discoverability: 81.5
    governance: 20.8
    operational_transparency: 13.2
  previous_composite: 52.0
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 14
    mcp: derived
    skills: derived
  schema_version: 0.11.0
  scored_at: '2026-08-17'
  trend: flat
security:
- kind: authentication
  name: Sign In Enterprise Authentication
  slug: sign-in-enterprise-authentication
  summary_line: openIdConnect/oauth2 · 1 scheme
- kind: domain-security
  name: Sign In Enterprise Domain Security
  slug: sign-in-enterprise-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Sign In Enterprise Trust Center
  slug: sign-in-enterprise-trust-center
  summary_line: SOC 2, ISO 27001
slug: sign-in-enterprise
tags:
- Company
- Vertical Software
- Visitor Management
- Physical Security
- Workplace Experience
- Identity
- Compliance
- Access Control
website: https://signinsolutions.com/signinenterprise
---
