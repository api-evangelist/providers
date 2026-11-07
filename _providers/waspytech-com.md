---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - authentication
  - rate-limits
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: conformant
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: false
    event_surface_described: true
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 47.1
  scored_at: '2026-11-06'
api_count: 2
apis:
- description: API for WaspyTech WhatsApp CRM platform
  name: WaspyTech API
  slug: waspytech-api
- baseURL: https://api.waspytech.com
  baseurl_source: declared
  description: 'waspytech-com API as documented publicly: 26 operations. Contract generated from the documentation by API Evangelist (2026-10-31); not the provider''s own document.'
  name: waspytech-com API
  slug: waspytech-com-api
artifact_total: 14
asyncapis:
- description: ''
  name: Waspytech Com Webhooks
  slug: waspytech-com-webhooks
common:
- group: start
  title: ''
  type: SignUp
  url: https://waspytech.com/register
- group: operate
  href: https://artifacts.apis.io/waspytech-com/rate-limits/waspytech-com-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/waspytech-com-rate-limits.yml
- group: design
  href: https://artifacts.apis.io/waspytech-com/rules/waspytech-com-rules.yml
  title: ''
  type: Spectral
  url: rules/waspytech-com-rules.yml
- group: design
  href: https://artifacts.apis.io/waspytech-com/json-ld/waspytech-com-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/waspytech-com-context.jsonld
- group: design
  href: https://artifacts.apis.io/waspytech-com/vocabulary/waspytech-com-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/waspytech-com-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/waspytech-com/asyncapi/waspytech-com-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/waspytech-com-webhooks.yml
- group: design
  href: https://artifacts.apis.io/waspytech-com/data-model/waspytech-com-data-model.yml
  title: ''
  type: DataModel
  url: data-model/waspytech-com-data-model.yml
- group: design
  href: https://artifacts.apis.io/waspytech-com/conventions/waspytech-com-conventions.yml
  title: ''
  type: Conventions
  url: conventions/waspytech-com-conventions.yml
- group: auth
  href: https://artifacts.apis.io/waspytech-com/authentication/waspytech-com-authentication.yml
  title: ''
  type: Authentication
  url: authentication/waspytech-com-authentication.yml
- group: design
  href: https://artifacts.apis.io/waspytech-com/conformance/waspytech-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/waspytech-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/waspytech-com/llms/waspytech-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/waspytech-com-llms.txt
- group: other
  href: https://artifacts.apis.io/waspytech-com/a2a/waspytech-com-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/waspytech-com-a2a.yml
- group: agent
  href: https://artifacts.apis.io/waspytech-com/well-known/waspytech-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/waspytech-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/waspytech-com/hosts/waspytech-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/waspytech-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/waspytech-com/vendors/waspytech-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/waspytech-com-vendors.yml
- group: design
  title: ''
  type: Webhooks
  url: https://waspytech.com/help/desarrolladores/webhooks
- group: commercial
  title: ''
  type: TermsOfService
  url: https://waspytech.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://waspytech.com/privacy
- group: auth
  href: https://artifacts.apis.io/waspytech-com/security/waspytech-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/waspytech-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://waspytech.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.waspytech.com/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.waspytech.com/api-reference/introduction
- group: start
  title: ''
  type: GettingStarted
  url: https://waspytech.com/planes
- group: company
  title: ''
  type: Blog
  url: https://waspytech.com/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://waspytech.com/planes
- group: operate
  title: ''
  type: Support
  url: https://waspytech.com/help
coverage:
  checked: '2026-10-31'
  detail: Docs are public but no OpenAPI, AsyncAPI, GraphQL, gRPC, or WSDL contract could be found despite probing common endpoints and docs pages.
  evidence:
  - status: 404
    url: https://api.waspytech.com/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-31'
description: WaspyTech provides a WhatsApp CRM platform that enables businesses to integrate the official WhatsApp API quickly, without bans. It offers multi‑agent support, automated messaging, templates approved by Meta, and real‑time analytics. The service includes plans, integrations with e‑commerce platforms, and 24/7 developer support, targeting SMEs and larger enterprises seeking reliable WhatsApp communication.
image: https://waspytech.com/og-home.png
json_schemas:
- name: GetApiV2ContactsResponse
  property_count: 2
  slug: waspytech-com-get-api-v2-contacts-response
- name: GetApiV2SocialAccountSummaryResponse
  property_count: 7
  slug: waspytech-com-get-api-v2-social-account-summary-response
- name: GetApiV2SocialPostsResponse
  property_count: 2
  slug: waspytech-com-get-api-v2-social-posts-response
- name: GetChannelsResponse
  property_count: 11
  slug: waspytech-com-get-channels-response
- name: GetMessagesIdResponse
  property_count: 11
  slug: waspytech-com-get-messages-id-response
- name: PostMessagesRequest
  property_count: 10
  slug: waspytech-com-post-messages-request
jsonld:
- class_count: 26
  name: Waspytech Com Context
  property_count: 57
  slug: waspytech-com-context
layout: provider
modified: '2026-10-31'
name: waspytech-com
nav: Providers
network: true
overview: 'waspytech-com is listed with 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Company, CRM, WhatsApp, Messaging, and Software-as-a-Service.


  The waspytech-com catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 1 Spectral governance ruleset.


  waspytech-com''s developer surface includes signup flow, authentication, documentation, API reference, getting-started guide, engineering blog, pricing, and 19 more developer resources.'
random_paper: 4
rate_limits:
- limit_count: 1
  name: Waspytech Com Rate Limits
  slug: waspytech-com-rate-limits
rules:
- authorship: generated
  effective_rule_count: 85
  extends:
  - spectral:oas
  name: waspytech-com API Rules
  rule_count: 44
  severity_counts:
    error: 41
    hint: 0
    info: 1
    warn: 2
  slug: waspytech-com-rules
score:
  band: thin
  composite: 34.1
  coverage:
    artifact_dirs: 21
    catalog_earned: 70.8
    catalog_earned_first_party: 8.0
    catalog_gap: 44.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -5.2
  facets:
    access_clarity: 28.9
    contract_governance: 22.0
    contract_quality: 36.1
    developer_ergonomics: 29.8
    discoverability: 66.1
    operational_transparency: 25.0
  previous_composite: 39.3
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
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
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Waspytech Com Authentication
  slug: waspytech-com-authentication
  summary_line: 2 schemes
- kind: domain-security
  name: Waspytech Com Domain Security
  slug: waspytech-com-domain-security
  summary_line: TLSv1.3 · DMARC
slug: waspytech-com
tags:
- Company
- CRM
- WhatsApp
- Messaging
- Software-as-a-Service
website: https://waspytech.com/
---
