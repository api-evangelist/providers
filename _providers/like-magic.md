---
agent_readiness:
  band: agent-aware
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
    error_semantics: false
    event_surface_described: true
    idempotency: false
    mcp_server: false
    openapi_examples: false
    operation_distinctiveness: false
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 24.6
  scored_at: '2026-10-31'
api_count: 2
apis:
- description: API documentation is provided at the developer portal but no machine‑readable contract was found.
  name: Like Magic API
  slug: like-magic-api-2
- description: 'LIKE MAGIC API as documented publicly: 19 operations. Contract generated from the documentation by API Evangelist (2026-10-28); not the provider''s own document.'
  name: LIKE MAGIC API
  slug: like-magic-api
artifact_total: 15
asyncapis:
- description: ''
  name: Like Magic Webhooks
  slug: like-magic-webhooks
common:
- group: operate
  href: https://artifacts.apis.io/like-magic/rate-limits/like-magic-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/like-magic-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/like-magic/plans/like-magic-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/like-magic-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/like-magic/rules/like-magic-rules.yml
  title: ''
  type: Spectral
  url: rules/like-magic-rules.yml
- group: design
  href: https://artifacts.apis.io/like-magic/json-ld/like-magic-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/like-magic-context.jsonld
- group: design
  href: https://artifacts.apis.io/like-magic/vocabulary/like-magic-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/like-magic-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/like-magic/asyncapi/like-magic-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/like-magic-webhooks.yml
- group: design
  href: https://artifacts.apis.io/like-magic/data-model/like-magic-data-model.yml
  title: ''
  type: DataModel
  url: data-model/like-magic-data-model.yml
- group: operate
  href: https://artifacts.apis.io/like-magic/changelog/like-magic-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/like-magic-changelog.yml
- group: auth
  href: https://artifacts.apis.io/like-magic/authentication/like-magic-authentication.yml
  title: ''
  type: Authentication
  url: authentication/like-magic-authentication.yml
- group: design
  href: https://artifacts.apis.io/like-magic/conformance/like-magic-conformance.yml
  title: ''
  type: Conformance
  url: conformance/like-magic-conformance.yml
- group: agent
  href: https://artifacts.apis.io/like-magic/llms/like-magic-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/like-magic-llms.txt
- group: auth
  href: https://artifacts.apis.io/like-magic/well-known/like-magic-status-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/like-magic-status-security.txt
- group: agent
  href: https://artifacts.apis.io/like-magic/well-known/like-magic-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/like-magic-well-known.yml
- group: other
  href: https://artifacts.apis.io/like-magic/hosts/like-magic-hosts.yml
  title: ''
  type: Hosts
  url: hosts/like-magic-hosts.yml
- group: other
  href: https://artifacts.apis.io/like-magic/vendors/like-magic-vendors.yml
  title: ''
  type: Vendors
  url: vendors/like-magic-vendors.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://status.likemagic.tech/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://likemagic.tech/privacy-policy
- group: operate
  title: ''
  type: ChangeLog
  url: https://api-docs.likemagic.tech/release-notes/
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.likemagic.tech/docs/category/getting-started/
- group: auth
  href: https://artifacts.apis.io/like-magic/security/like-magic-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/like-magic-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://likemagic.tech/
- group: docs
  title: ''
  type: Documentation
  url: https://likemagic.tech/api-integrations
- group: commercial
  title: ''
  type: Pricing
  url: https://likemagic.tech/pricing
- group: company
  title: ''
  type: Blog
  url: https://likemagic.tech/blog
coverage:
  checked: '2026-10-28'
  detail: The API reference site renders documentation via JavaScript, providing no machine‑readable OpenAPI spec.
  evidence:
  - status: 200
    url: https://api-docs.likemagic.tech/api-spec/
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-27'
description: LIKE MAGIC is a Swiss hospitality technology company providing a connected guest journey and hotel operations platform. It aims to increase efficiency, drive revenue, and create a game‑changing experience for guests and hotel staff through its integrated solutions for reservations, check‑in, room service, and AI‑powered personalization.
image: https://likemagic.tech/assets/img/og-share.jpg
json_schemas:
- name: GetUserProfilesIdResponse
  property_count: 6
  slug: like-magic-get-user-profiles-id-response
- name: PostApiUnifiedMessagingServiceGuestConversationsMessagesRequ
  property_count: 5
  slug: like-magic-post-api-unified-messaging-service-guest-conversations-messages-requ
- name: PostApiUnifiedMessagingServiceGuestConversationsSendMessageR
  property_count: 10
  slug: like-magic-post-api-unified-messaging-service-guest-conversations-send-message-r
- name: PostBookingRes99812Request
  property_count: 4
  slug: like-magic-post-booking-res99812-request
- name: PostManualsMicrowavePdfRequest
  property_count: 5
  slug: like-magic-post-manuals-microwave-pdf-request
- name: PostTokenResponse
  property_count: 4
  slug: like-magic-post-token-response
jsonld:
- class_count: 10
  name: Like Magic Context
  property_count: 32
  slug: like-magic-context
layout: provider
modified: '2026-10-27'
name: LIKE MAGIC
nav: Providers
network: true
overview: 'LIKE MAGIC is listed with 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Hospitality, Technology, Guest Experience, and Hotel Operations.


  The LIKE MAGIC catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 1 Spectral governance ruleset.


  LIKE MAGIC''s developer surface includes changelog, authentication, getting-started guide, documentation, pricing, engineering blog, and 18 more developer resources.'
plans:
- name: Like Magic Plans Pricing
  plan_count: 2
  slug: like-magic-plans-pricing
random_paper: 19
rate_limits:
- limit_count: 1
  name: Like Magic Rate Limits
  slug: like-magic-rate-limits
rules:
- authorship: generated
  effective_rule_count: 51
  extends:
  - spectral:oas
  name: LIKE MAGIC API Rules
  rule_count: 10
  severity_counts:
    error: 8
    hint: 0
    info: 1
    warn: 1
  slug: like-magic-rules
score:
  band: developing
  composite: 42.2
  coverage:
    artifact_dirs: 20
    catalog_earned: 73.8
    catalog_earned_first_party: 16.0
    catalog_gap: 41.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 42.1
    contract_governance: 22.0
    contract_quality: 32.7
    developer_ergonomics: 35.7
    discoverability: 57.1
    operational_transparency: 71.1
  provenance:
    conformance: derived
    contracts:
      callable: 0.0
      derived: 13
      marker_coverage: 100.0
      total: 13
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 20.6
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Like Magic Authentication
  slug: like-magic-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Like Magic Domain Security
  slug: like-magic-domain-security
  summary_line: TLSv1.3 · DMARC
slug: like-magic
tags:
- Company
- Hospitality
- Technology
- Guest Experience
- Hotel Operations
website: https://likemagic.tech/
---
