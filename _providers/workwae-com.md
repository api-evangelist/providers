---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - authentication
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: derived
    event_surface_described: true
    idempotency: documented
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 30.2
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: Email, calendar and contacts sync API for Gmail, Microsoft 365, IMAP/SMTP mailboxes.
  name: Workwae API
  slug: workwae-api
- baseURL: https://api.workwae.com
  baseurl_source: declared
  description: Email, calendar and contacts sync for Gmail and Microsoft 365 accounts, and email sync for
  name: Workwae API V1 API
  slug: workwae-api-v1-api
artifact_total: 14
asyncapis:
- description: ''
  name: Workwae Com Webhooks
  slug: workwae-com-webhooks
common:
- group: design
  href: https://artifacts.apis.io/workwae-com/rules/workwae-com-rules.yml
  title: ''
  type: Spectral
  url: rules/workwae-com-rules.yml
- group: design
  href: https://artifacts.apis.io/workwae-com/json-ld/workwae-com-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/workwae-com-context.jsonld
- group: design
  href: https://artifacts.apis.io/workwae-com/vocabulary/workwae-com-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/workwae-com-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/workwae-com/conformance/workwae-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/workwae-com-conformance.yml
- group: design
  href: https://artifacts.apis.io/workwae-com/asyncapi/workwae-com-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/workwae-com-webhooks.yml
- group: design
  href: https://artifacts.apis.io/workwae-com/data-model/workwae-com-data-model.yml
  title: ''
  type: DataModel
  url: data-model/workwae-com-data-model.yml
- group: design
  href: https://artifacts.apis.io/workwae-com/conventions/workwae-com-conventions.yml
  title: ''
  type: Idempotency
  url: conventions/workwae-com-conventions.yml
- group: design
  href: https://artifacts.apis.io/workwae-com/conventions/workwae-com-conventions.yml
  title: ''
  type: Conventions
  url: conventions/workwae-com-conventions.yml
- group: auth
  href: https://artifacts.apis.io/workwae-com/authentication/workwae-com-authentication.yml
  title: ''
  type: Authentication
  url: authentication/workwae-com-authentication.yml
- group: design
  href: https://artifacts.apis.io/workwae-com/errors/workwae-com-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/workwae-com-problem-types.yml
- group: agent
  href: https://artifacts.apis.io/workwae-com/llms/workwae-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/workwae-com-llms.txt
- group: auth
  href: https://artifacts.apis.io/workwae-com/well-known/workwae-com-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/workwae-com-security.txt
- group: agent
  href: https://artifacts.apis.io/workwae-com/well-known/workwae-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/workwae-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/workwae-com/hosts/workwae-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/workwae-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/workwae-com/vendors/workwae-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/workwae-com-vendors.yml
- group: build
  href: https://artifacts.apis.io/workwae-com/packages/workwae-com-packages.yml
  title: ''
  type: Packages
  url: packages/workwae-com-packages.yml
- group: design
  title: ''
  type: Webhooks
  url: https://workwae.com/features/webhooks
- group: operate
  title: ''
  type: StatusPage
  url: https://status.workwae.com
- group: auth
  title: ''
  type: Security
  url: https://workwae.com/security
- group: build
  title: ''
  type: SDKs
  url: https://workwae.com/sdk
- group: start
  title: ''
  type: Login
  url: https://app.workwae.com/sign-in
- group: operate
  title: ''
  type: ChangeLog
  url: https://workwae.com/changelog
- group: auth
  href: https://artifacts.apis.io/workwae-com/security/workwae-com-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/workwae-com-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/workwae-com/security/workwae-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/workwae-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://workwae.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.workwae.com/
- group: docs
  title: ''
  type: APIReference
  url: https://api.workwae.com/v1/openapi.json
- group: start
  title: ''
  type: GettingStarted
  url: https://workwae.com/quickstart
- group: operate
  title: ''
  type: Support
  url: https://workwae.com/support
- group: company
  title: ''
  type: Blog
  url: https://workwae.com/blog/
- group: commercial
  title: ''
  type: Pricing
  url: https://workwae.com/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://workwae.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://workwae.com/privacy
- group: build
  title: ''
  type: Postman
  url: https://www.postman.com/workwae/workspace
coverage:
  detail: the company serves an API surface but requires credentials before any description of it can be read
  evidence:
  - status: null
    url: https://api.workwae.com/v1/openapi.json
  - status: 401
    url: https://api.workwae.com/mcp
  - status: 200
    url: https://workwae.com/
  reason: partner-login
  state: gated
created: '2026-10-31'
description: Workwae provides a unified API that connects inboxes, calendars, and contact books across major platforms such as Gmail, Microsoft 365, and CardDAV. It offers features like mail sync, calendar event management, bookings, contacts, meetings, webhooks, AI-powered reply classification, and MCP server agents with scoped access. The platform supports both hosted and headless sign‑in flows, domain‑wide access, and integrates with tools like Zoom and Webex, aiming to streamline communication and scheduling for CRM, recruiting, and support use cases.
image: https://cdn.workwae.com/og/v2/site.jpg
json_schemas:
- name: CalendarEventDetail
  property_count: 30
  slug: workwae-com-calendar-event-detail
- name: CalendarEvent
  property_count: 29
  slug: workwae-com-calendar-event
- name: Message
  property_count: 25
  slug: workwae-com-message
- name: OutboxEntry
  property_count: 20
  slug: workwae-com-outbox-entry
- name: QueuedSend
  property_count: 21
  slug: workwae-com-queued-send
- name: SchedulingLink
  property_count: 20
  slug: workwae-com-scheduling-link
jsonld:
- class_count: 120
  name: Workwae Com Context
  property_count: 206
  slug: workwae-com-context
layout: provider
modified: '2026-10-31'
name: workwae-com
nav: Providers
network: true
overview: 'workwae-com publishes 2 API contracts indexed on the [APIs.io](https://apis.io/) network, including Workwae API V1 API, and 1 more. Tagged areas include Company, Email, Calendar, Contacts, and Scheduling.


  The workwae-com catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 1 Spectral governance ruleset.


  workwae-com''s developer surface includes authentication, changelog, documentation, API reference, getting-started guide, support, engineering blog, and 27 more developer resources.'
random_paper: 4
rules:
- authorship: generated
  effective_rule_count: 58
  extends:
  - spectral:oas
  name: workwae-com API Rules
  rule_count: 17
  severity_counts:
    error: 14
    hint: 0
    info: 2
    warn: 1
  slug: workwae-com-rules
score:
  band: developing
  composite: 42.5
  coverage:
    artifact_dirs: 20
    catalog_earned: 62.8
    catalog_earned_first_party: 0.0
    catalog_gap: 52.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -12.3
  facets:
    access_clarity: 22.4
    contract_governance: 22.0
    contract_quality: 64.9
    developer_ergonomics: 39.3
    discoverability: 66.1
    operational_transparency: 25.0
  previous_composite: 54.8
  provenance:
    conformance: derived
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 24.5
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Workwae Com Authentication
  slug: workwae-com-authentication
  summary_line: 2 schemes
- kind: domain-security
  name: Workwae Com Domain Security
  slug: workwae-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Workwae Com Vulnerability Disclosure
  slug: workwae-com-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: workwae-com
tags:
- Company
- Email
- Calendar
- Contacts
- Scheduling
- Artificial Intelligence
website: https://workwae.com/
---
