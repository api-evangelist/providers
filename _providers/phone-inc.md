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
    event_surface_described: true
    idempotency: derived
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 38.5
  scored_at: '2026-11-06'
api_count: 1
apis:
- baseURL: https://app.phone.inc
  baseurl_source: declared
  description: 'Phone Inc API as documented publicly: 46 operations. Contract generated from the documentation by API Evangelist (2026-10-24); not the provider''s own document.'
  name: Phone Inc API
  slug: phone-inc-api
artifact_total: 13
asyncapis:
- description: ''
  name: Phone Inc Webhooks
  slug: phone-inc-webhooks
common:
- group: commercial
  href: https://artifacts.apis.io/phone-inc/plans/phone-inc-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/phone-inc-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/phone-inc/rules/phone-inc-rules.yml
  title: ''
  type: Spectral
  url: rules/phone-inc-rules.yml
- group: design
  href: https://artifacts.apis.io/phone-inc/json-ld/phone-inc-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/phone-inc-context.jsonld
- group: design
  href: https://artifacts.apis.io/phone-inc/vocabulary/phone-inc-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/phone-inc-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/phone-inc/asyncapi/phone-inc-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/phone-inc-webhooks.yml
- group: design
  href: https://artifacts.apis.io/phone-inc/data-model/phone-inc-data-model.yml
  title: ''
  type: DataModel
  url: data-model/phone-inc-data-model.yml
- group: design
  href: https://artifacts.apis.io/phone-inc/conventions/phone-inc-conventions.yml
  title: ''
  type: Idempotency
  url: conventions/phone-inc-conventions.yml
- group: design
  href: https://artifacts.apis.io/phone-inc/conventions/phone-inc-conventions.yml
  title: ''
  type: Conventions
  url: conventions/phone-inc-conventions.yml
- group: auth
  href: https://artifacts.apis.io/phone-inc/authentication/phone-inc-authentication.yml
  title: ''
  type: Authentication
  url: authentication/phone-inc-authentication.yml
- group: design
  href: https://artifacts.apis.io/phone-inc/conformance/phone-inc-conformance.yml
  title: ''
  type: Conformance
  url: conformance/phone-inc-conformance.yml
- group: agent
  href: https://artifacts.apis.io/phone-inc/llms/phone-inc-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/phone-inc-llms.txt
- group: agent
  href: https://artifacts.apis.io/phone-inc/well-known/phone-inc-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/phone-inc-well-known.yml
- group: other
  href: https://artifacts.apis.io/phone-inc/hosts/phone-inc-hosts.yml
  title: ''
  type: Hosts
  url: hosts/phone-inc-hosts.yml
- group: other
  href: https://artifacts.apis.io/phone-inc/vendors/phone-inc-vendors.yml
  title: ''
  type: Vendors
  url: vendors/phone-inc-vendors.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://status.phone.inc/
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.phone.inc/api/quickstart
- group: auth
  href: https://artifacts.apis.io/phone-inc/security/phone-inc-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/phone-inc-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.phone.inc/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.phone.inc
- group: commercial
  title: ''
  type: Pricing
  url: https://www.phone.inc/pricing
- group: operate
  title: ''
  type: Support
  url: https://www.phone.inc/support
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.phone.inc/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.phone.inc/privacy
coverage:
  detail: the company serves an API surface but requires credentials before any description of it can be read
  evidence:
  - status: null
    url: https://docs.phone.inc/api/mcp
  - status: 401
    url: https://app.phone.inc/mcp
  - status: 200
    url: https://www.phone.inc/
  reason: partner-login
  state: gated
created: '2026-10-24'
description: Phone Inc provides a cloud‑based business phone platform that transforms a personal mobile device into a full‑featured business phone system. It offers features such as a dedicated business number, call routing, AI‑powered reception, spam filtering, messaging, integrations with Shopify, CRM tools, and an extensible API for developers to build custom workflows and AI assistants. The service targets small to medium businesses seeking to modernize their communications.
image: https://ogkit.dev/img/2VNDYJI5.jpeg?url=https%3A%2F%2Fwww.phone.inc%2F%3Fv%3D3
json_schemas:
- name: GetApiV1CallsActiveResponse
  property_count: 4
  slug: phone-inc-get-api-v1-calls-active-response
- name: GetApiV1Calls0193F4Ba12347C009E3D2B2B8A7F1C11Response
  property_count: 18
  slug: phone-inc-get-api-v1-calls0193-f4-ba12347-c009-e3-d2-b2-b8-a7-f1-c11-response
- name: GetV1CallsIdResponse
  property_count: 18
  slug: phone-inc-get-v1-calls-id-response
- name: GetV1CompanyResponse
  property_count: 14
  slug: phone-inc-get-v1-company-response
- name: PatchV1CompanyResponse
  property_count: 14
  slug: phone-inc-patch-v1-company-response
- name: PostApiV1CallsResponse
  property_count: 2
  slug: phone-inc-post-api-v1-calls-response
jsonld:
- class_count: 54
  name: Phone Inc Context
  property_count: 95
  slug: phone-inc-context
layout: provider
modified: '2026-10-24'
name: Phone Inc
nav: Providers
network: true
overview: 'Phone Inc is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Communications, Cloud, and Business.


  The Phone Inc catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 1 Spectral governance ruleset.


  Phone Inc''s developer surface includes authentication, getting-started guide, documentation, pricing, support, and 18 more developer resources.'
plans:
- name: Phone Inc Plans Pricing
  plan_count: 2
  slug: phone-inc-plans-pricing
random_paper: 9
rules:
- authorship: generated
  effective_rule_count: 52
  extends:
  - spectral:oas
  name: Phone Inc API Rules
  rule_count: 11
  severity_counts:
    error: 9
    hint: 0
    info: 1
    warn: 1
  slug: phone-inc-rules
score:
  band: thin
  composite: 35.7
  coverage:
    artifact_dirs: 21
    catalog_earned: 65.8
    catalog_earned_first_party: 8.0
    catalog_gap: 49.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -8.3
  facets:
    access_clarity: 36.8
    contract_governance: 22.0
    contract_quality: 37.4
    developer_ergonomics: 25.0
    discoverability: 64.3
    operational_transparency: 15.8
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 44.0
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 1
      marker_coverage: 100.0
      total: 1
    mcp: unknown
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
    applies: true
    score: 27.8
screenshot: https://apis.io/screenshots/phone-inc/phone-inc-2026-11-03T141156.png
security:
- kind: authentication
  name: Phone Inc Authentication
  slug: phone-inc-authentication
  summary_line: 2 schemes
- kind: domain-security
  name: Phone Inc Domain Security
  slug: phone-inc-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: phone-inc
tags:
- Company
- Communications
- Cloud
- Business
website: https://www.phone.inc/
---
