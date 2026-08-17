---
access_model:
  confidence: medium
  label: Enterprise
  onboarding: unknown
  pricing: enterprise
  public: false
  source:
  - plans
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: true
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: documented
    event_surface_described: true
    idempotency: false
    mcp_server: false
    openapi_examples: partial
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 47.3
  scored_at: '2026-08-17'
agentic_access:
- acting_count: 15
  human_in_the_loop: 1
  name: Leanplum Agentic Access
  operation_count: 27
  slug: leanplum-agentic-access
  summary_line: 27 operations · 15 acting · 1 human-in-the-loop
api_count: 8
apis:
- description: 'The complete Leanplum REST API as Leanplum itself publishes it — one OpenAPI 3.0.0 document (x-api-id "leanplum-api") covering all 42 methods across eight tags: User Behavior, User Information, Messag'
  name: Leanplum API
  slug: leanplum-api
- description: The A/B Tests API from Leanplum — 3 operation(s) for a/b tests.
  name: Leanplum A/B Tests API
  slug: leanplum-a-b-tests-api
- description: The Content & Variables API from Leanplum — 3 operation(s) for content & variables.
  name: Leanplum Content & Variables API
  slug: leanplum-content-variables-api
- description: The Data Export API from Leanplum — 5 operation(s) for data export.
  name: Leanplum Data Export API
  slug: leanplum-data-export-api
- description: The Events & Tracking API from Leanplum — 7 operation(s) for events & tracking.
  name: Leanplum Events & Tracking API
  slug: leanplum-events-tracking-api
- description: The Messaging API from Leanplum — 3 operation(s) for messaging.
  name: Leanplum Messaging API
  slug: leanplum-messaging-api
- description: The Postbacks & Batch API from Leanplum — 2 operation(s) for postbacks & batch.
  name: Leanplum Postbacks & Batch API
  slug: leanplum-postbacks-batch-api
- description: The User & Device Attributes API from Leanplum — 4 operation(s) for user & device attributes.
  name: Leanplum User & Device Attributes API
  slug: leanplum-user-device-attributes-api
artifact_total: 26
asyncapis:
- description: ''
  name: Leanplum Postbacks Webhooks
  slug: leanplum-postbacks-webhooks
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Leanplum A/B Tests API
  slug: open-leanplum-a-b-tests-api
- collection_type: open
  name: API
  slug: open-leanplum-api
- collection_type: open
  name: Leanplum A/B Tests Content & Variables API
  slug: open-leanplum-content-variables-api
- collection_type: open
  name: Leanplum A/B Tests Data Export API
  slug: open-leanplum-data-export-api
- collection_type: open
  name: Leanplum A/B Tests Events & Tracking API
  slug: open-leanplum-events-tracking-api
- collection_type: open
  name: Leanplum A/B Tests Messaging API
  slug: open-leanplum-messaging-api
- collection_type: open
  name: Leanplum A/B Tests Postbacks & Batch API
  slug: open-leanplum-postbacks-batch-api
- collection_type: open
  name: Leanplum A/B Tests User & Device Attributes API
  slug: open-leanplum-user-device-attributes-api
- collection_type: open
  name: Leanplum API
  slug: open-leanplum
common:
- group: auth
  title: ''
  type: Authentication
  url: authentication/leanplum-authentication.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/leanplum-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/leanplum-domain-security.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Leanplum
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/leanplum
- group: company
  title: ''
  type: Website
  url: https://www.leanplum.com
- group: docs
  title: ''
  type: Documentation
  url: https://docs.leanplum.com
- group: commercial
  title: ''
  type: Plans
  url: plans/leanplum-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/leanplum-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/leanplum-finops.yml
- group: build
  title: ''
  type: Packages
  url: packages/leanplum-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/leanplum-packages.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/leanplum-llms.txt
- group: design
  title: ''
  type: Conformance
  url: conformance/leanplum-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: security/leanplum-trust-center.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/leanplum-trust-center.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/leanplum-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/leanplum-lifecycle.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/leanplum-conventions.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/leanplum-changelog.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/leanplum-sandbox.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/leanplum-data-model.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/leanplum-postbacks-webhooks.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/leanplum-api-overlay.yaml
- group: build
  title: ''
  type: Postman
  url: https://www.getpostman.com/collections/378a83c1424d632661d0
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.leanplum.com/reference/overview
- group: docs
  title: ''
  type: APIReference
  url: https://docs.leanplum.com/reference/api-methods
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.leanplum.com/reference/api-introduction
- group: operate
  title: ''
  type: Support
  url: https://docs.leanplum.com/docs/leanplum-help-center
- group: company
  title: ''
  type: Blog
  url: https://clevertap.com/blog/
- group: commercial
  title: ''
  type: Pricing
  url: https://clevertap.com/pricing/
- group: start
  title: ''
  type: Login
  url: https://www.leanplum.com/dashboard/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://clevertap.com/terms-service/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://clevertap.com/privacy-policy/
created: '2026-07-03'
description: Leanplum is a mobile marketing and multichannel customer engagement platform offering push notifications, in-app and email messaging, behavioral event tracking and analytics, A/B testing, and remotely configurable content variables. Leanplum was acquired by CleverTap in 2022 and now operates as "Leanplum by CleverTap"; the brand and its documented REST API remain active while customers are migrated onto the CleverTap platform (CleverTap has wrapped its own methods behind the Leanplum API surface to smooth that transition). All API requests are made to https://api.leanplum.com/api and authenticated with an appId plus an operation-specific clientKey (production, development, data export, or content read-only).
finops:
- name: Leanplum Finops
  service_category: Marketing and Customer Engagement
  slug: leanplum-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/leanplum.png
layout: provider
modified: '2026-08-13'
name: Leanplum
nav: Providers
network: true
overview: 'Leanplum publishes 8 APIs on the [APIs.io](https://apis.io/) network, including A/B Tests API, Content & Variables API, and 6 more. Tagged areas include Mobile Marketing, Customer Engagement, Push Notifications, Messaging, and A/B Testing.


  The Leanplum catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Leanplum''s developer surface includes authentication, documentation, changelog, sandbox, API reference, getting-started guide, support, and 28 more developer resources.'
plans:
- name: Leanplum Plans Pricing
  plan_count: 2
  slug: leanplum-plans-pricing
random_paper: 117
rate_limits:
- limit_count: 10
  name: Leanplum Rate Limits
  slug: leanplum-rate-limits
score:
  band: exemplar
  composite: 66.8
  delta: 33.9
  facets:
    commercial_clarity: 89.5
    contract_quality: 60.8
    developer_ergonomics: 76.1
    discoverability: 81.5
    governance: 20.8
    operational_transparency: 60.5
  previous_composite: 32.9
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 7
  schema_version: 0.11.0
  scored_at: '2026-08-17'
  trend: rising
screenshot: https://raw.githubusercontent.com/api-evangelist/leanplum/refs/heads/main/screenshots/leanplum-2026-07-25T224746.png
security:
- kind: authentication
  name: Leanplum Authentication
  slug: leanplum-authentication
  summary_line: apiKey · 2 schemes
- kind: domain-security
  name: Leanplum Domain Security
  slug: leanplum-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Leanplum Trust Center
  slug: leanplum-trust-center
  summary_line: SOC 2 Type II, ISO 27001, GDPR, CCPA, HIPAA
slug: leanplum
tags:
- Mobile Marketing
- Customer Engagement
- Push Notifications
- Messaging
- A/B Testing
- Analytics
- CleverTap
website: https://www.leanplum.com
---
