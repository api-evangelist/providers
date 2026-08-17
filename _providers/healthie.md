---
access_model:
  confidence: high
  label: Paid (free trial) · Sales-gated API access
  onboarding: unknown
  pricing: paid
  public: false
  source:
  - https://www.gethealthie.com/pricing
  - https://www.gethealthie.com/plus/api-for-digital-health-startups
  - https://docs.gethealthie.com/guides/api-concepts/environments
  trial: true
  try_now: true
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: true
    agentic_access: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: documented
    event_surface_described: derived
    idempotency: false
    mcp_server: true
    openapi_examples: documented
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 50.2
  scored_at: '2026-08-17'
api_count: 1
apis:
- description: The Healthie GraphQL API is the single contract behind the entire Healthie platform — the same API that powers the Healthie web, iOS, and Android applications is available to partners building branded
  name: Healthie GraphQL API
  slug: healthie-graphql-api
artifact_total: 27
asyncapis:
- description: Best-effort AsyncAPI 2.6 description of the Healthie **GraphQL subscription** surface — the real-time push channel, distinct from the outbound HTTP webhook surface described in `healthie-webhooks-asyn
  name: Healthie GraphQL Subscriptions (WebSocket)
  slug: healthie-subscriptions-asyncapi
- description: Best-effort AsyncAPI 2.6 description of the Healthie webhook surface. Healthie delivers webhook notifications as HTTP POST requests with an `application/json` body whenever a subscribed event occurs o
  name: Healthie Webhooks
  slug: healthie-webhooks-asyncapi
common:
- group: auth
  title: ''
  type: TrustCenter
  url: security/healthie-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/healthie-domain-security.yml
- group: auth
  title: ''
  type: Compliance
  url: https://www.gethealthie.com/security
- group: design
  title: ''
  type: Conformance
  url: conformance/healthie-conformance.yml
- group: docs
  title: ''
  type: APIReference
  url: https://docs.gethealthie.com/reference
- group: docs
  title: ''
  type: GraphQL
  url: graphql/healthie-schema.graphql
- group: auth
  title: ''
  type: Authentication
  url: authentication/healthie-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/healthie-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/healthie-error-codes.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/healthie-rate-limits.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/healthie-data-model.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/healthie-lifecycle.yml
- group: operate
  title: ''
  type: Deprecation
  url: https://docs.gethealthie.com/guides/api-concepts/deprecations
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/healthie-changelog.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/healthie-sandbox.yml
- group: build
  title: ''
  type: Packages
  url: packages/healthie-packages.yml
- group: design
  title: ''
  type: Components
  url: components/healthie-components.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/healthie-mcp.yml
- group: build
  title: ''
  type: ToolCrosswalk
  url: mcp/healthie-tool-crosswalk.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/healthie-llms.txt
- group: docs
  title: ''
  type: AsyncAPI
  url: asyncapi/healthie-subscriptions-asyncapi.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/healthie-plans-pricing.yml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://www.gethealthie.com/api
- group: operate
  title: ''
  type: Support
  url: https://help.gethealthie.com/
- group: operate
  title: ''
  type: Roadmap
  url: https://portal.productboard.com/gethealthie/1-healthie-product-portal/tabs/4-in-development
- group: start
  title: ''
  type: SignUp
  url: https://secure.gethealthie.com/users/sign_up/provider
- group: start
  title: ''
  type: Login
  url: https://secure.gethealthie.com/users/sign_in
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.gethealthie.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.gethealthie.com/privacy
- group: company
  title: ''
  type: Website
  url: https://www.gethealthie.com/
- group: start
  title: ''
  type: Portal
  url: https://www.gethealthie.com/api
- group: docs
  title: ''
  type: Documentation
  url: https://docs.gethealthie.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.gethealthie.com/reference
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.gethealthie.com/guides/quickstart
- group: auth
  title: ''
  type: Authentication
  url: https://docs.gethealthie.com/guides/api-concepts/authentication
- group: design
  title: ''
  type: Versioning
  url: https://docs.gethealthie.com/guides/api-concepts/versioning
- group: operate
  title: ''
  type: RateLimits
  url: https://docs.gethealthie.com/guides/api-concepts/rate-limits
- group: design
  title: ''
  type: Webhooks
  url: https://docs.gethealthie.com/guides/webhooks
- group: other
  title: ''
  type: Environments
  url: https://docs.gethealthie.com/guides/api-concepts/environments
- group: build
  title: ''
  type: SDKs
  url: https://www.npmjs.com/org/healthie
- group: build
  title: ''
  type: Tools
  url: https://github.com/healthie/healthie-dev-assist
- group: build
  title: ''
  type: CodeExamples
  url: https://github.com/healthie/healthie_sample_booking_widget
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/healthie
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/gethealthie/
- group: other
  title: ''
  type: X
  url: https://x.com/gethealthie
- group: company
  title: ''
  type: Blog
  url: https://www.gethealthie.com/blog
- group: operate
  title: ''
  type: StatusPage
  url: https://status.gethealthie.com/
- group: operate
  title: ''
  type: ChangeLog
  url: https://docs.gethealthie.com/guides/api-concepts/versioning
- group: commercial
  title: ''
  type: Pricing
  url: https://www.gethealthie.com/pricing
- group: commercial
  title: ''
  type: Plans
  url: https://www.gethealthie.com/pricing
created: '2026-05-25'
description: Healthie is a cloud, API-first EHR and practice management platform purpose-built for digital health startups, virtual care companies, and modern clinical practices. Healthie packages an EHR, scheduling, charting, telehealth, intake forms, care plans, online programs, messaging, billing, claims (CMS-1500 / ClaimMD), and patient portal behind a single GraphQL API and modular SDKs that power both the Healthie product UI and partner applications. Healthie targets the digital health ecosystem with a "buy the EHR, build the experience" model — the same API that backs the Healthie web and mobile apps is fully exposed to customers building branded patient and provider experiences on top of the platform.
features:
- GraphQL API powering Healthie's own EHR, mobile, and patient portal — same contract for first-party and partners
- Resources span clients, appointments, availability, charting, forms, programs, goals, allergies, immunizations, medications, lab orders, CMS-1500 claims, insurance authorizations, eligibility checks, payments, messaging, fax, conversations, and announcements
- Date-based opt-in API versioning via the `Healthie-GraphQL-API-Version` header — default `2024-06-01`
- 'API-key authentication via `Authorization: Basic` + `AuthorizationSource: API` (plus `AuthorizationShard` for sharded customers)'
- '`createApiKey` GraphQL mutation for programmatic key issuance scoped to individual user accounts'
- Two-environment model — `staging-api.gethealthie.com` sandbox and `api.gethealthie.com` production with no data transfer between them
- Query complexity scoring (max 2000) and 25-level depth limit instead of fixed RPS rate limits
- HMAC-SHA256 signed webhooks with exponential-backoff retry up to 3 days, auto-disable, and email alerts
- Webhook `resource_id_type` covers Appointment, FormAnswerGroup, Entry, and Note events with `changed_fields` deltas
- Parent-organization webhooks aggregate events across sub-organizations
- Modular TypeScript / JavaScript SDKs on npm under `@healthie/sdk`
- Healthie Dev Assist — official MCP server for AI-assisted Healthie development
- Sample Booking Widget reference implementation on GitHub
- Healthie Harbor app marketplace with Google Fit, Apple Health, Fitbit, Stripe, Zoom, ClaimMD, Fullscript Labs, and Change Healthcare integrations
- HIPAA and PCI compliant infrastructure operating ~2.5B API calls/month at 99.99% uptime
- SMART on FHIR / interoperability and US-based data residency options for enterprise
graphqls:
- description: The Healthie GraphQL API is the single contract behind the entire Healthie platform — the same API that powers the Healthie web, iOS, and Android applications is available to partners building branded
  name: Healthie GraphQL API
  slug: healthie-graphql
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/healthie.png
layout: provider
mcp_servers:
- description: ''
  name: Healthie Dev Assist (local stdio)
  slug: healthie-dev-assist-local-stdio
modified: '2026-08-14'
name: Healthie
nav: Providers
network: true
overview: 'Healthie publishes 1 API on the [APIs.io](https://apis.io/) network: GraphQL API. Tagged areas include API-First, Appointments, Billing, Care Plans, and Charting.


  The Healthie catalog on APIs.io includes 2 event-driven AsyncAPI specifications and 1 Spectral governance ruleset.


  Healthie''s developer surface includes API reference, authentication, changelog, sandbox, support, signup flow, developer portal, and 44 more developer resources.'
plans:
- name: Healthie Plans Pricing
  plan_count: 5
  slug: healthie-plans-pricing
random_paper: 91
rate_limits:
- limit_count: 3
  name: Healthie Rate Limits
  slug: healthie-rate-limits
rules:
- name: Healthie API Rules
  rule_count: 5
  severity_counts:
    error: 1
    hint: 0
    info: 0
    warn: 4
  slug: healthie-asyncapi-spectral-rules
score:
  band: exemplar
  composite: 68.7
  delta: 30.8
  facets:
    commercial_clarity: 92.1
    contract_quality: 56.0
    developer_ergonomics: 80.4
    discoverability: 75.9
    governance: 54.2
    operational_transparency: 89.5
  previous_composite: 37.9
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 37.5
  schema_version: 0.11.0
  scored_at: '2026-08-17'
  trend: rising
screenshot: https://raw.githubusercontent.com/api-evangelist/healthie/refs/heads/main/screenshots/healthie-2026-06-20T182600.png
security:
- kind: authentication
  name: Healthie Authentication
  slug: healthie-authentication
  summary_line: apiKey · 4 schemes
- kind: domain-security
  name: Healthie Domain Security
  slug: healthie-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Healthie Trust Center
  slug: healthie-trust-center
  summary_line: HIPAA, SOC 2 Type 2, HITRUST CSF r2, ONC Health IT Certification, PCI DSS Service Provider Level 1 (held by Healthie's payment processor, not by Healthie), GDPR, PIPEDA
slug: healthie
tags:
- API-First
- Appointments
- Billing
- Care Plans
- Charting
- Claims
- Clinical
- Digital Health
- EHR
- EMR
- Forms
- GraphQL
- Health Tech
- Healthcare
- Insurance
- Intake
- Online Programs
- Patient Engagement
- Patient Portal
- Practice Management
- Programs
- Scheduling
- Telehealth
- Wellness
- Webhooks
website: https://www.gethealthie.com/
---
