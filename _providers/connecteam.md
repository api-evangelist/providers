---
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: verified
    event_surface_described: derived
    idempotency: false
    mcp_server: verified
    openapi_examples: partial
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.2
  score: 54.9
  scored_at: '2026-08-19'
agentic_access:
- acting_count: 85
  human_in_the_loop: 0
  name: Connecteam Agentic Access
  operation_count: 145
  slug: connecteam-agentic-access
  summary_line: 145 operations · 85 acting
api_count: 1
apis:
- description: The Connecteam public REST API. 145 operations across users, admins, smart groups and custom fields; time clock, time activities, geofences, breadcrumbs and lock days; job scheduling and shifts (v1 an
  name: Connecteam API
  slug: api
artifact_total: 11
asyncapis:
- description: ''
  name: Connecteam Events Webhooks
  slug: connecteam-events-webhooks
collections:
- collection_type: open
  name: Connecteam API documentation
  slug: open-connecteam-openapi-original
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/connecteam-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/connecteam-domain-security.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/connecteam-scopes.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/connecteam-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://connecteam.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.connecteam.com/
- group: docs
  title: ''
  type: Documentation
  url: https://developer.connecteam.com/docs/introduction-1
- group: docs
  title: ''
  type: APIReference
  url: https://developer.connecteam.com/reference/
- group: start
  title: ''
  type: GettingStarted
  url: https://developer.connecteam.com/docs/introduction-1
- group: operate
  title: ''
  type: Support
  url: https://help.connecteam.com/en/
- group: operate
  title: ''
  type: HelpCenter
  url: https://help.connecteam.com/en/
- group: company
  title: ''
  type: Blog
  url: https://connecteam.com/blog/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Connecteam
- group: commercial
  title: ''
  type: Pricing
  url: https://connecteam.com/pricing/
- group: start
  title: ''
  type: SignUp
  url: https://connecteam.com/employee-app-360-funnel/
- group: start
  title: ''
  type: Login
  url: https://connecteam.com/login/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://connecteam.com/terms-conditions/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://connecteam.com/privacy/
- group: operate
  title: ''
  type: StatusPage
  url: https://connecteam.statuspage.io/
- group: operate
  title: ''
  type: ChangeLog
  url: https://developer.connecteam.com/changelog
- group: auth
  title: ''
  type: TrustCenter
  url: security/connecteam-trust-center.yml
- group: auth
  title: ''
  type: Compliance
  url: https://connecteam.com/trust-center/
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/connecteam-llms.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/connecteam-well-known.yml
- group: other
  title: ''
  type: APICatalog
  url: well-known/connecteam-api-catalog.json
- group: build
  title: ''
  type: Packages
  url: packages/connecteam-packages.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/connecteam-conventions.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/connecteam-rate-limits.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/connecteam-plans.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/connecteam-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/connecteam-lifecycle.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/connecteam-changelog.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/connecteam-conformance.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/connecteam-data-model.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/connecteam-api-overlay.yaml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/connecteam-events-webhooks.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/connecteam-mcp.yml
created: '2026-08-01'
description: Connecteam is a mobile-first workforce management platform for deskless and non-desk teams, bundling time clock and GPS timesheets, job scheduling, task boards, digital forms and checklists, chat and company communication, HR onboarding, time off, pay rates and sales data into three purchasable hubs (Operations, Communications, HR & Skills). Its public REST API at api.connecteam.com is described by an OpenAPI 3.1 contract covering 145 operations across 98 paths, authenticated either with a company X-API-KEY header or OAuth 2.0 client-credentials tokens scoped across 61 named permissions, and it declares 41 webhook events for time activity, shifts, users, tasks, forms and chat. API access is gated to the Expert plan and above, with per-plan rate limits surfaced in x-ratelimit-* response headers.
image: https://connecteam.com/wp-content/uploads/2024/03/Share-image-homepage.png
layout: provider
mcp_servers:
- description: ''
  name: connecteam-mcp.yml
  slug: connecteam-mcpyml
modified: '2026-08-01'
name: Connecteam
nav: Providers
network: true
overview: 'Connecteam publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Workforce Management, Human Resources, Time Tracking, and Scheduling.


  The Connecteam catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Connecteam''s developer surface includes authentication, documentation, API reference, getting-started guide, support, engineering blog, pricing, and 31 more developer resources.'
plans:
- name: Connecteam Plans
  plan_count: 5
  slug: connecteam-plans
random_paper: 10
rate_limits:
- limit_count: 6
  name: Connecteam Rate Limits
  slug: connecteam-rate-limits
scopes:
- name: Connecteam Scopes
  scope_count: 62
  slug: connecteam-scopes
  summary_line: 62 scopes · clientCredentials
score:
  band: strong
  composite: 63.7
  delta: -3.8
  facets:
    access_clarity: 92.1
    commercial_clarity: 92.1
    contract_governance: 16.7
    contract_quality: 67.9
    developer_ergonomics: 39.9
    discoverability: 87.0
    governance: 16.7
    operational_transparency: 73.7
  previous_composite: 67.5
  provenance:
    agentic_access: derived
    conformance: derived
    mcp: first-party
    skills: derived
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/connecteam/refs/heads/main/screenshots/connecteam-2026-08-07T163740.png
security:
- kind: authentication
  name: Connecteam Authentication
  slug: connecteam-authentication
  summary_line: apiKey/http/oauth2 · 3 schemes
- kind: domain-security
  name: Connecteam Domain Security
  slug: connecteam-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Connecteam Trust Center
  slug: connecteam-trust-center
  summary_line: SOC 2 Type 2, ISO/IEC 27001, GDPR, HIPAA, CCPA, PCI DSS
slug: connecteam
tags:
- Company
- Workforce Management
- Human Resources
- Time Tracking
- Scheduling
- Employee Communication
- Task Management
- Forms
- Deskless
- SaaS
website: https://connecteam.com/
---
