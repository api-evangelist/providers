---
access_model:
  confidence: high
  label: Docs public, access sales-gated
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - https://developers.cvent.com/docs/legacy-api/jifflenow-api/introduction
  - https://developers.cvent.com/docs/legacy-api/jifflenow-api/getting-started
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: true
  schema_version: 0.2
  score: 18.4
  scored_at: '2026-08-19'
api_count: 1
apis:
- description: The Jifflenow REST API exposes the meeting-automation core of Cvent Jifflenow as JSON over HTTPS. Documented modules cover user management (list users, push users into an event, block a user's calenda
  name: Jifflenow REST API
  slug: jifflenow-rest-api
artifact_total: 7
common:
- group: auth
  title: ''
  type: Compliance
  url: https://www.cvent.com/en/trust
- group: auth
  title: ''
  type: TrustCenter
  url: security/jifflenow-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/jifflenow-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.jifflenow.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developers.cvent.com/
- group: docs
  title: ''
  type: Documentation
  url: https://developers.cvent.com/docs/legacy-api/jifflenow-api/introduction
- group: docs
  title: ''
  type: APIReference
  url: https://developers.cvent.com/docs/legacy-api/jifflenow-api/api-request-response
- group: start
  title: ''
  type: GettingStarted
  url: https://developers.cvent.com/docs/legacy-api/jifflenow-api/getting-started
- group: operate
  title: ''
  type: Support
  url: https://support.cvent.com/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.cvent.com/en/event-management-software/cvent-pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.cvent.com/en/company/legal
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.cvent.com/en/privacy-policy
- group: operate
  title: ''
  type: StatusPage
  url: https://status.cvent.com
- group: auth
  title: ''
  type: Authentication
  url: authentication/jifflenow-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/jifflenow-scopes.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/jifflenow-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/jifflenow-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/jifflenow-lifecycle.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/jifflenow-data-model.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/jifflenow-sandbox.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/jifflenow-conformance.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/jifflenow-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/jifflenow-rate-limits.yml
- group: build
  title: ''
  type: Packages
  url: packages/jifflenow-packages.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/jifflenow-llms.txt
created: '2026-07-17'
description: 'Jifflenow is a B2B meeting automation and scheduling platform for trade shows, conferences, and corporate events, now part of Cvent (acquired 2021) as Cvent Jifflenow. It lets sales and event teams request, approve, and confirm meetings before attendees arrive on the show floor, with automated routing and notifications, a unified calendar that combines customer meetings and internal staff activities, on-site mobile check-in and no-show tracking, and reporting dashboards that tie meeting volume and outcomes back to pipeline. It integrates with Salesforce (native CRM sync of accounts, opportunities, campaigns, and leads), Outlook, and iCapture badge scanning. The standalone jifflenow.com now redirects to Cvent, but the Jifflenow REST API remains live and publicly documented on the acquirer''s developer portal at developers.cvent.com under its legacy-API section: roughly twenty JSON operations over events, meetings, sessions, meeting types, users, calendar blocks, event topics,
  badge-scan ingestion, and shared meeting links, served from a per-tenant https://<companyname>.jifflenow.com/api host and secured with OAuth 2.0 client credentials. No OpenAPI, SDK, webhook surface, or agent surface is published for it.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/jifflenow.png
layout: provider
modified: '2026-08-13'
name: Jifflenow
nav: Providers
network: true
overview: 'Jifflenow publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Automation, Events, Meetings, and Scheduling.


  Jifflenow''s developer surface includes documentation, API reference, getting-started guide, support, pricing, authentication, sandbox, and 18 more developer resources.'
plans:
- name: Jifflenow Plans Pricing
  plan_count: 0
  slug: jifflenow-plans-pricing
random_paper: 70
rate_limits:
- limit_count: 0
  name: Jifflenow Rate Limits
  slug: jifflenow-rate-limits
scopes:
- name: Jifflenow Scopes
  scope_count: 1
  slug: jifflenow-scopes
  summary_line: 1 scope · clientCredentials
score:
  band: thin
  composite: 34.8
  delta: 1.8
  facets:
    access_clarity: 47.4
    commercial_clarity: 47.4
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 61.9
    discoverability: 87.0
    governance: 18.2
    operational_transparency: 15.8
  previous_composite: 33.0
  provenance:
    conformance: first-party
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/jifflenow/refs/heads/main/screenshots/jifflenow-2026-07-25T223147.png
security:
- kind: authentication
  name: Jifflenow Authentication
  slug: jifflenow-authentication
  summary_line: oauth2 · 2 schemes
- kind: domain-security
  name: Jifflenow Domain Security
  slug: jifflenow-domain-security
  summary_line: TLSv1.2 · HSTS · DMARC
- kind: trust-center
  name: Jifflenow Trust Center
  slug: jifflenow-trust-center
  summary_line: SOC 2, ISO 27001, PCI DSS, GDPR, CSA STAR
slug: jifflenow
tags:
- Company
- Automation
- Events
- Meetings
- Scheduling
- Event Marketing
- B2B
- Sales
- Trade Shows
- Meeting Automation
- Appointments
- Badge Scanning
website: https://www.jifflenow.com
---
