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
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: documented
    event_surface_described: true
    idempotency: false
    mcp_server: derived
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.2
  score: 41.7
  scored_at: '2026-08-06'
api_count: 2
apis:
- description: GraphQL API for clients (property owners and managers) to create and track reactive and recurrent work orders, residents, locations, service requests, invoices, proposals, Turn/Reno projects, ratings,
  name: One Open API v2 - Client
  slug: one-open-api-v2-client
- description: GraphQL/HTTP API for vendors and affiliate technicians to manage assets (service and location assets), attachments, communications and messages, client lists, employees, locations, reactive and recurr
  name: One Open API v2 - Vendor
  slug: one-open-api-v2-vendor
artifact_total: 6
asyncapis:
- description: ''
  name: Sms Assist Webhooks
  slug: sms-assist-webhooks
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/sms-assist-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.lessen.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developers.lessen.com/
- group: docs
  title: ''
  type: Documentation
  url: https://developers.lessen.com/docs/
- group: docs
  title: ''
  type: APIReference
  url: https://developers.lessen.com/docs/#/client/overview
- group: start
  title: ''
  type: GettingStarted
  url: https://developers.lessen.com/docs/#/client/overview
- group: auth
  title: ''
  type: Authentication
  url: authentication/sms-assist-authentication.yml
- group: start
  title: ''
  type: SignUp
  url: https://developers.lessen.com/login
- group: start
  title: ''
  type: Login
  url: https://developers.lessen.com/login
- group: company
  title: ''
  type: Blog
  url: https://www.lessen.com/resources
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.lessen.com/legal/terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.lessen.com/legal/privacy-policy
- group: operate
  title: ''
  type: StatusPage
  url: https://status.lessen.com/
- group: operate
  title: ''
  type: ChangeLog
  url: https://developers.lessen.com/docs/#/client/releaseNotes/client
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/sms-assist-changelog.yml
- group: operate
  title: ''
  type: Deprecation
  url: https://developers.lessen.com/docs/#/vendor/overview
- group: design
  title: ''
  type: Webhooks
  url: https://developers.lessen.com/docs/#/client/guides/webhook/about-webhooks
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/sms-assist-lifecycle.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/sms-assist-conventions.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/sms-assist-sandbox.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/sms-assist-problem-types.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/sms-assist-mcp.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/sms-assist-llms.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/sms-assist-well-known.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/sms-assist-conformance.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/sms-assist-data-model.yml
created: '2026-07-17'
description: SMS Assist (rebranded as Lessen) is a facilities maintenance, repair, and work-order management company. Its "One" Platform coordinates reactive and recurrent maintenance, turn/renovation projects, invoices, proposals, assets, and a nationwide vendor network for residential and commercial properties. Lessen exposes the platform through the One Open API v2 — a GraphQL API split into a Client surface (property owners/managers create and track work orders, residents, locations, invoices, and Turn/Reno projects) and a Vendor surface (affiliate technicians manage assets, communications, and work orders) — plus a rich webhook event catalog, SSO/SCIM provisioning, and isolated sandbox and production environments. The legacy REST Open API v1 and Affiliate API v1 were sunset in favor of the v2 GraphQL platform.
image: https://assets-global.website-files.com/650de1047e0c5de5860e054c/656a1bd286bfe157a42e4b53_brand-logo-global.svg
layout: provider
mcp_servers:
- description: ''
  name: sms-assist-mcp.yml
  slug: sms-assist-mcpyml
modified: '2026-07-21'
name: SMS Assist
nav: Providers
network: true
overview: 'SMS Assist publishes 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Facilities Management, Property Maintenance, Work Orders, and Field Service.


  The SMS Assist catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  SMS Assist''s developer surface includes documentation, API reference, getting-started guide, authentication, signup flow, engineering blog, changelog, and 20 more developer resources.'
random_paper: 30
score:
  band: developing
  composite: 47.7
  delta: 0.0
  facets:
    commercial_clarity: 34.2
    contract_quality: 51.6
    developer_ergonomics: 58.2
    discoverability: 87.0
    governance: 12.5
    operational_transparency: 47.4
  previous_composite: 47.7
  provenance:
    conformance: first-party
    mcp: derived
    skills: derived
  schema_version: 0.9.1
  scored_at: '2026-08-06'
  trend: flat
security:
- kind: authentication
  name: Sms Assist Authentication
  slug: sms-assist-authentication
  summary_line: http/oauth2 · 2 schemes
- kind: domain-security
  name: Sms Assist Domain Security
  slug: sms-assist-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: sms-assist
tags:
- Company
- Facilities Management
- Property Maintenance
- Work Orders
- Field Service
- Maintenance
- Real Estate
- GraphQL
- Webhooks
- Vendor Network
website: https://www.lessen.com/
---
