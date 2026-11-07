---
access_model:
  confidence: medium
  gated: none
  gated_source:
  - onboarding
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  - security
  trial: false
  try_now: true
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: partial
    operation_distinctiveness: distinct
    pagination_ratio: partial
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 42.5
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 9
  human_in_the_loop: 0
  name: Blinkinbox Club Agentic Access
  operation_count: 19
  slug: blinkinbox-club-agentic-access
  summary_line: 19 operations · 9 acting
api_count: 1
apis:
- baseURL: https://api.blinkinbox.club/api/v1
  baseurl_source: declared
  description: The Account API from blinkinbox-club — 1 operation(s) for account.
  name: blinkinbox-club Account API
  slug: blinkinbox-club-account-api
- baseURL: https://api.blinkinbox.club/api/v1
  baseurl_source: declared
  description: The Domains API from blinkinbox-club — 3 operation(s) for domains.
  name: blinkinbox-club Domains API
  slug: blinkinbox-club-domains-api
- baseURL: https://api.blinkinbox.club/api/v1
  baseurl_source: declared
  description: The Inboxes API from blinkinbox-club — 2 operation(s) for inboxes.
  name: blinkinbox-club Inboxes API
  slug: blinkinbox-club-inboxes-api
- baseURL: https://api.blinkinbox.club/api/v1
  baseurl_source: declared
  description: The Messages API from blinkinbox-club — 5 operation(s) for messages.
  name: blinkinbox-club Messages API
  slug: blinkinbox-club-messages-api
- baseURL: https://api.blinkinbox.club/api/v1
  baseurl_source: declared
  description: The Webhooks API from blinkinbox-club — 3 operation(s) for webhooks.
  name: blinkinbox-club Webhooks API
  slug: blinkinbox-club-webhooks-api
artifact_total: 17
common:
- group: agent
  href: https://artifacts.apis.io/blinkinbox-club/agentic-access/blinkinbox-club-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/blinkinbox-club-agentic-access.yml
- group: commercial
  href: https://artifacts.apis.io/blinkinbox-club/plans/blinkinbox-club-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/blinkinbox-club-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/blinkinbox-club/rules/blinkinbox-club-rules.yml
  title: ''
  type: Spectral
  url: rules/blinkinbox-club-rules.yml
- group: design
  href: https://artifacts.apis.io/blinkinbox-club/json-ld/blinkinbox-club-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/blinkinbox-club-context.jsonld
- group: design
  href: https://artifacts.apis.io/blinkinbox-club/vocabulary/blinkinbox-club-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/blinkinbox-club-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/blinkinbox-club/data-model/blinkinbox-club-data-model.yml
  title: ''
  type: DataModel
  url: data-model/blinkinbox-club-data-model.yml
- group: design
  href: https://artifacts.apis.io/blinkinbox-club/errors/blinkinbox-club-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/blinkinbox-club-problem-types.yml
- group: design
  href: https://artifacts.apis.io/blinkinbox-club/conformance/blinkinbox-club-conformance.yml
  title: ''
  type: Conformance
  url: conformance/blinkinbox-club-conformance.yml
- group: agent
  href: https://artifacts.apis.io/blinkinbox-club/llms/blinkinbox-club-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/blinkinbox-club-llms.txt
- group: agent
  href: https://artifacts.apis.io/blinkinbox-club/well-known/blinkinbox-club-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/blinkinbox-club-well-known.yml
- group: other
  href: https://artifacts.apis.io/blinkinbox-club/hosts/blinkinbox-club-hosts.yml
  title: ''
  type: Hosts
  url: hosts/blinkinbox-club-hosts.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://blinkinbox.club/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://blinkinbox.club/privacy
- group: commercial
  title: ''
  type: Pricing
  url: https://blinkinbox.club/pricing
- group: docs
  title: ''
  type: Documentation
  url: https://blinkinbox.club/guides
- group: start
  title: ''
  type: GettingStarted
  url: https://blinkinbox.club/mcp
- group: docs
  title: ''
  type: APIReference
  url: https://blinkinbox.club/developers
- group: auth
  href: https://artifacts.apis.io/blinkinbox-club/authentication/blinkinbox-club-authentication.yml
  title: ''
  type: Authentication
  url: authentication/blinkinbox-club-authentication.yml
- group: auth
  href: https://artifacts.apis.io/blinkinbox-club/security/blinkinbox-club-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/blinkinbox-club-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://blinkinbox.club/
coverage:
  detail: the company serves an API surface but requires credentials before any description of it can be read
  evidence:
  - status: 401
    url: https://api.blinkinbox.club/api/mcp
  - status: 200
    url: https://blinkinbox.club/
  reason: partner-login
  state: gated
created: '2026-10-30'
description: BlinkInbox provides a free temporary disposable email service with an API and MCP server for developers. It offers instant inboxes without signup, OTP and magic‑link extraction, and tiered pricing for higher limits. The REST API enables end‑to‑end testing, while the MCP server supports AI agents. Features include customizable address prefixes, domain‑based inboxes for paid plans, and automatic email deletion after expiry.
image: https://blinkinbox.club/og-image.png
json_schemas:
- name: Domain
  property_count: 6
  slug: blinkinbox-club-domain
- name: Inbox
  property_count: 9
  slug: blinkinbox-club-inbox
- name: Message
  property_count: 15
  slug: blinkinbox-club-message
- name: MessageSummary
  property_count: 10
  slug: blinkinbox-club-message-summary
- name: Otp
  property_count: 6
  slug: blinkinbox-club-otp
- name: Webhook
  property_count: 8
  slug: blinkinbox-club-webhook
jsonld:
- class_count: 7
  name: Blinkinbox Club Context
  property_count: 32
  slug: blinkinbox-club-context
layout: provider
modified: '2026-10-30'
name: blinkinbox-club
nav: Providers
network: true
overview: 'blinkinbox-club publishes 5 API contracts indexed on the [APIs.io](https://apis.io/) network, including Account API, Domains API, Inboxes API, and 2 more. Tagged areas include Email, MCP, Developer Tools, and Disposable.


  The blinkinbox-club catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  blinkinbox-club''s developer surface includes pricing, documentation, getting-started guide, API reference, authentication, and 15 more developer resources.'
plans:
- name: Blinkinbox Club Plans Pricing
  plan_count: 4
  slug: blinkinbox-club-plans-pricing
random_paper: 3
rules:
- authorship: generated
  effective_rule_count: 58
  extends:
  - spectral:oas
  name: blinkinbox-club API Rules
  rule_count: 17
  severity_counts:
    error: 15
    hint: 0
    info: 1
    warn: 1
  slug: blinkinbox-club-rules
score:
  band: developing
  composite: 39.3
  coverage:
    artifact_dirs: 20
    catalog_earned: 69.8
    catalog_earned_first_party: 12.0
    catalog_gap: 45.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -7.5
  facets:
    access_clarity: 47.4
    contract_governance: 22.0
    contract_quality: 58.9
    developer_ergonomics: 26.2
    discoverability: 64.3
    operational_transparency: 0.0
  previous_composite: 46.8
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 5
    mcp: derived
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
screenshot: https://apis.io/screenshots/blinkinbox-club/blinkinbox-club-2026-11-03T121934.png
security:
- kind: authentication
  name: Blinkinbox Club Authentication
  slug: blinkinbox-club-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Blinkinbox Club Domain Security
  slug: blinkinbox-club-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: blinkinbox-club
tags:
- Email
- MCP
- Developer Tools
- Disposable
website: https://blinkinbox.club/
---
