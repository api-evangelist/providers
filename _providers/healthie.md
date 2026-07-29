---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source: []
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    asyncapi_events: true
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: documented
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 35.4
  scored_at: '2026-07-28'
api_count: 1
apis:
- description: The Healthie GraphQL API is the single contract behind the entire Healthie platform — the same API that powers the Healthie web, iOS, and Android applications is available to partners building branded
  name: Healthie GraphQL API
  slug: healthie-graphql-api
artifact_total: 21
asyncapis:
- description: Best-effort AsyncAPI 2.6 description of the Healthie webhook surface. Healthie delivers webhook notifications as HTTP POST requests with an `application/json` body whenever a subscribed event occurs o
  name: Healthie Webhooks
  slug: healthie-webhooks-asyncapi
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/healthie-domain-security.yml
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
modified: '2026-05-30'
name: Healthie
nav: Providers
network: true
overview: 'Healthie publishes 1 API on the [APIs.io](https://apis.io/) network: GraphQL API. Tagged areas include API-First, Appointments, Billing, Care Plans, and Charting.


  The Healthie catalog on APIs.io includes 1 event-driven AsyncAPI specification and 1 Spectral governance ruleset.


  Healthie''s developer surface includes developer portal, documentation, getting-started guide, authentication, tooling, code examples, engineering blog, and 15 more developer resources.'
random_paper: 66
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
  band: thin
  composite: 38.1
  delta: 1.3
  facets:
    commercial_clarity: 10.5
    contract_quality: 51.6
    developer_ergonomics: 47.8
    discoverability: 68.5
    governance: 41.7
    operational_transparency: 44.7
  previous_composite: 36.8
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 15.0
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/healthie/refs/heads/main/screenshots/healthie-2026-06-20T182600.png
security:
- kind: domain-security
  name: Healthie Domain Security
  slug: healthie-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
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
