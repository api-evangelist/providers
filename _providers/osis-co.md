---
access_model:
  confidence: high
  label: Freemium
  onboarding: unknown
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  - rate-limits
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-native
  dimensions:
    agent_card: conformant
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: platform
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: verified
    event_surface_described: true
    idempotency: verified
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: partial
    operation_distinctiveness: distinct
    pagination_ratio: false
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 63.9
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 31
  human_in_the_loop: 0
  name: Osis Co Agentic Access
  operation_count: 55
  slug: osis-co-agentic-access
  summary_line: 55 operations · 31 acting
api_count: 1
apis:
- baseURL: https://osis.co/api/v1/comms
  baseurl_source: declared
  description: The AI API from osis-co — 2 operation(s) for ai.
  name: osis-co AI API
  slug: osis-co-ai-api
- baseURL: https://osis.co/api/v1/comms
  baseurl_source: declared
  description: The Calls API from osis-co — 11 operation(s) for calls.
  name: osis-co Calls API
  slug: osis-co-calls-api
- baseURL: https://osis.co/api/v1/comms
  baseurl_source: declared
  description: The Capabilities API from osis-co — 1 operation(s) for capabilities.
  name: osis-co Capabilities API
  slug: osis-co-capabilities-api
- baseURL: https://osis.co/api/v1/comms
  baseurl_source: declared
  description: The Conversations API from osis-co — 4 operation(s) for conversations.
  name: osis-co Conversations API
  slug: osis-co-conversations-api
- baseURL: https://osis.co/api/v1/comms
  baseurl_source: declared
  description: The Events API from osis-co — 1 operation(s) for events.
  name: osis-co Events API
  slug: osis-co-events-api
- baseURL: https://osis.co/api/v1/comms
  baseurl_source: declared
  description: The Groups API from osis-co — 1 operation(s) for groups.
  name: osis-co Groups API
  slug: osis-co-groups-api
- baseURL: https://osis.co/api/v1/comms
  baseurl_source: declared
  description: The Lines API from osis-co — 6 operation(s) for lines.
  name: osis-co Lines API
  slug: osis-co-lines-api
- baseURL: https://osis.co/api/v1/comms
  baseurl_source: declared
  description: The Messages API from osis-co — 6 operation(s) for messages.
  name: osis-co Messages API
  slug: osis-co-messages-api
- baseURL: https://osis.co/api/v1/comms
  baseurl_source: declared
  description: The Number Changes API from osis-co — 1 operation(s) for number changes.
  name: osis-co Number Changes API
  slug: osis-co-number-changes-api
- baseURL: https://osis.co/api/v1/comms
  baseurl_source: declared
  description: The Payments API from osis-co — 8 operation(s) for payments.
  name: osis-co Payments API
  slug: osis-co-payments-api
- baseURL: https://osis.co/api/v1/comms
  baseurl_source: declared
  description: The Webhooks API from osis-co — 1 operation(s) for webhooks.
  name: osis-co Webhooks API
  slug: osis-co-webhooks-api
artifact_total: 27
asyncapis:
- description: ''
  name: Osis Co Webhooks
  slug: osis-co-webhooks
common:
- group: agent
  href: https://artifacts.apis.io/osis-co/agentic-access/osis-co-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/osis-co-agentic-access.yml
- group: operate
  href: https://artifacts.apis.io/osis-co/rate-limits/osis-co-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/osis-co-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/osis-co/plans/osis-co-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/osis-co-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/osis-co/rules/osis-co-rules.yml
  title: ''
  type: Spectral
  url: rules/osis-co-rules.yml
- group: design
  href: https://artifacts.apis.io/osis-co/json-ld/osis-co-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/osis-co-context.jsonld
- group: design
  href: https://artifacts.apis.io/osis-co/vocabulary/osis-co-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/osis-co-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/osis-co/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/osis-co/asyncapi/osis-co-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/osis-co-webhooks.yml
- group: design
  href: https://artifacts.apis.io/osis-co/data-model/osis-co-data-model.yml
  title: ''
  type: DataModel
  url: data-model/osis-co-data-model.yml
- group: design
  href: https://artifacts.apis.io/osis-co/conventions/osis-co-conventions.yml
  title: ''
  type: Idempotency
  url: conventions/osis-co-conventions.yml
- group: design
  href: https://artifacts.apis.io/osis-co/conventions/osis-co-conventions.yml
  title: ''
  type: Conventions
  url: conventions/osis-co-conventions.yml
- group: auth
  href: https://artifacts.apis.io/osis-co/authentication/osis-co-authentication.yml
  title: ''
  type: Authentication
  url: authentication/osis-co-authentication.yml
- group: design
  href: https://artifacts.apis.io/osis-co/errors/osis-co-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/osis-co-problem-types.yml
- group: design
  href: https://artifacts.apis.io/osis-co/conformance/osis-co-conformance.yml
  title: ''
  type: Conformance
  url: conformance/osis-co-conformance.yml
- group: agent
  href: https://artifacts.apis.io/osis-co/llms/osis-co-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/osis-co-llms.txt
- group: other
  href: https://artifacts.apis.io/osis-co/a2a/osis-co-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/osis-co-a2a.yml
- group: agent
  href: https://artifacts.apis.io/osis-co/well-known/osis-co-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/osis-co-well-known.yml
- group: other
  href: https://artifacts.apis.io/osis-co/hosts/osis-co-hosts.yml
  title: ''
  type: Hosts
  url: hosts/osis-co-hosts.yml
- group: other
  href: https://artifacts.apis.io/osis-co/vendors/osis-co-vendors.yml
  title: ''
  type: Vendors
  url: vendors/osis-co-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://comms.osis.co/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://comms.osis.co/privacy
- group: start
  title: ''
  type: Login
  url: https://comms.osis.co/auth/login
- group: auth
  href: https://artifacts.apis.io/osis-co/security/osis-co-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/osis-co-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://osis.co/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.osis.co/
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.osis.co/quickstart
- group: docs
  title: ''
  type: APIReference
  url: https://docs.osis.co
- group: start
  title: ''
  type: DeveloperPortal
  url: https://comms.osis.co/developers
- group: commercial
  title: ''
  type: Pricing
  url: https://comms.osis.co/pricing
- group: company
  title: ''
  type: Blog
  url: https://comms.osis.co/blog
coverage:
  detail: the company serves an API surface but requires credentials before any description of it can be read
  evidence:
  - status: null
    url: https://docs.osis.co/openapi.json
  - status: null
    url: https://docs.osis.co/mcp
  - status: 401
    url: https://osis.co/api/mcp
  - status: 401
    url: https://comms.osis.co/api/mcp
  - status: 200
    url: https://osis.co/
  reason: partner-login
  state: gated
created: '2026-10-30'
description: Comms (osis.co) provides a unified Customer Messaging API enabling developers to send and receive messages across iMessage, RCS, SMS, and WhatsApp, as well as manage voice calls and payments. The platform offers hosted MCP tools for AI assistants, detailed developer guides, quickstarts, and webhooks for real‑time event handling, targeting ecommerce sellers, SaaS products, and enterprises.
image: https://comms.osis.co/og.jpg?v=2
json_schemas:
- name: Call
  property_count: 23
  slug: osis-co-call
- name: MerchantStatus
  property_count: 5
  slug: osis-co-merchant-status
- name: Message
  property_count: 20
  slug: osis-co-message
- name: PaymentRequest
  property_count: 27
  slug: osis-co-payment-request
- name: SendContactCardRequest
  property_count: 16
  slug: osis-co-send-contact-card-request
- name: SendMessageRequest
  property_count: 12
  slug: osis-co-send-message-request
jsonld:
- class_count: 53
  name: Osis Co Context
  property_count: 194
  slug: osis-co-context
layout: provider
modified: '2026-10-30'
name: osis-co
nav: Providers
network: true
overview: 'osis-co publishes 11 API contracts indexed on the [APIs.io](https://apis.io/) network, including AI API, Calls API, Capabilities API, and 8 more. Tagged areas include Messaging, Communications, Software-as-a-Service, and Customer Service.


  The osis-co catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 1 Spectral governance ruleset.


  osis-co''s developer surface includes authentication, documentation, getting-started guide, API reference, pricing, engineering blog, and 24 more developer resources.'
plans:
- name: Osis Co Plans Pricing
  plan_count: 4
  slug: osis-co-plans-pricing
random_paper: 5
rate_limits:
- limit_count: 3
  name: Osis Co Rate Limits
  slug: osis-co-rate-limits
rules:
- authorship: generated
  effective_rule_count: 100
  extends:
  - spectral:oas
  name: osis-co API Rules
  rule_count: 59
  severity_counts:
    error: 47
    hint: 0
    info: 1
    warn: 11
  slug: osis-co-rules
score:
  band: developing
  composite: 49.8
  coverage:
    artifact_dirs: 28
    catalog_earned: 81.8
    catalog_earned_first_party: 24.0
    catalog_gap: 33.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -10.0
  facets:
    access_clarity: 53.9
    contract_governance: 22.0
    contract_quality: 71.8
    developer_ergonomics: 33.9
    discoverability: 57.1
    operational_transparency: 39.5
  previous_composite: 59.8
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 11
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 20.6
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/osis-co/osis-co-2026-11-03T140744.png
security:
- kind: authentication
  name: Osis Co Authentication
  slug: osis-co-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Osis Co Domain Security
  slug: osis-co-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
skill_count: 2
skills:
- name: osis-co-create-and-retrieve-payment
  slug: osis-co-create-and-retrieve-payment
- name: osis-co-place-call
  slug: osis-co-place-call
slug: osis-co
tags:
- Messaging
- Communications
- Software-as-a-Service
- Customer Service
website: https://osis.co/
---
