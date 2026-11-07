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
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: false
    event_surface_described: false
    idempotency: documented
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: false
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 34.2
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: 'CallUpOnIt API as documented publicly: 11 operations. Contract generated from the documentation by API Evangelist (2026-11-04); not the provider''s own document.'
  name: CallUpOnIt API
  slug: calluponit-com-api
artifact_total: 11
common:
- group: design
  href: https://artifacts.apis.io/calluponit-com/rules/calluponit-com-rules.yml
  title: ''
  type: Spectral
  url: rules/calluponit-com-rules.yml
- group: design
  href: https://artifacts.apis.io/calluponit-com/json-ld/calluponit-com-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/calluponit-com-context.jsonld
- group: design
  href: https://artifacts.apis.io/calluponit-com/vocabulary/calluponit-com-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/calluponit-com-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/calluponit-com/data-model/calluponit-com-data-model.yml
  title: ''
  type: DataModel
  url: data-model/calluponit-com-data-model.yml
- group: design
  href: https://artifacts.apis.io/calluponit-com/conventions/calluponit-com-conventions.yml
  title: ''
  type: Idempotency
  url: conventions/calluponit-com-conventions.yml
- group: design
  href: https://artifacts.apis.io/calluponit-com/conventions/calluponit-com-conventions.yml
  title: ''
  type: Conventions
  url: conventions/calluponit-com-conventions.yml
- group: auth
  href: https://artifacts.apis.io/calluponit-com/authentication/calluponit-com-authentication.yml
  title: ''
  type: Authentication
  url: authentication/calluponit-com-authentication.yml
- group: design
  href: https://artifacts.apis.io/calluponit-com/conformance/calluponit-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/calluponit-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/calluponit-com/llms/calluponit-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/calluponit-com-llms.txt
- group: agent
  href: https://artifacts.apis.io/calluponit-com/well-known/calluponit-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/calluponit-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/calluponit-com/hosts/calluponit-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/calluponit-com-hosts.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://calluponit.com/terms
- group: operate
  title: ''
  type: Support
  url: https://calluponit.com/support
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://calluponit.com/privacy
- group: start
  title: ''
  type: Login
  url: https://calluponit.com/login
- group: start
  title: ''
  type: GettingStarted
  url: https://calluponit.com/agent-api
- group: auth
  href: https://artifacts.apis.io/calluponit-com/security/calluponit-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/calluponit-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://calluponit.com/
coverage:
  detail: the company serves an API surface but requires credentials before any description of it can be read
  evidence:
  - status: 401
    url: https://calluponit.com/mcp
  - status: 200
    url: https://calluponit.com/
  reason: partner-login
  state: gated
created: '2026-11-04'
description: CallUpOnIt is a web-based reminder service that lets users schedule personal messages via SMS, WhatsApp, email, or voice calls. Users can create one‑time or recurring reminders, set pricing plans, and manage their notes without installing an app. The platform is provided by The Boggler Inc., offering a simple interface for self‑reminders and productivity.
image: https://calluponit.com/og-image.png
json_schemas:
- name: PostApiV1BillingCheckoutRequest
  property_count: 1
  slug: calluponit-com-post-api-v1-billing-checkout-request
- name: PostApiV1DeliveriesRequest
  property_count: 1
  slug: calluponit-com-post-api-v1-deliveries-request
- name: PostApiV1MediaRequest
  property_count: 1
  slug: calluponit-com-post-api-v1-media-request
- name: PostApiV1RemindersRequest
  property_count: 5
  slug: calluponit-com-post-api-v1-reminders-request
- name: PutApiV1RemindersIdRequest
  property_count: 7
  slug: calluponit-com-put-api-v1-reminders-id-request
- name: PutApiV1VoicesRequest
  property_count: 1
  slug: calluponit-com-put-api-v1-voices-request
jsonld:
- class_count: 9
  name: Calluponit Com Context
  property_count: 12
  slug: calluponit-com-context
layout: provider
modified: '2026-11-04'
name: CallUpOnIt
nav: Providers
network: true
overview: 'CallUpOnIt is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Reminders, voice-calls, Email Scheduling, and AI Agents.


  The CallUpOnIt catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  CallUpOnIt''s developer surface includes authentication, support, getting-started guide, and 15 more developer resources.'
random_paper: 7
rules:
- authorship: generated
  effective_rule_count: 82
  extends:
  - spectral:oas
  name: CallUpOnIt API Rules
  rule_count: 41
  severity_counts:
    error: 39
    hint: 0
    info: 1
    warn: 1
  slug: calluponit-com-rules
score:
  band: emerging
  composite: 21.9
  coverage:
    artifact_dirs: 17
    catalog_earned: 52.8
    catalog_earned_first_party: 0.0
    catalog_gap: 62.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 17.1
    contract_governance: 22.0
    contract_quality: 24.7
    developer_ergonomics: 20.2
    discoverability: 48.2
    operational_transparency: 0.0
  provenance:
    conformance: derived
    contracts:
      callable: 0.0
      derived: 1
      marker_coverage: 100.0
      total: 1
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 20.6
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Calluponit Com Authentication
  slug: calluponit-com-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Calluponit Com Domain Security
  slug: calluponit-com-domain-security
  summary_line: TLSv1.3
slug: calluponit-com
tags:
- Reminders
- voice-calls
- Email Scheduling
- AI Agents
website: https://calluponit.com/
---
