---
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
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 33.8
  scored_at: '2026-10-31'
api_count: 7
apis:
- description: The Concentrate AI Responses API provides a unified interface for interacting with multiple AI model providers.
  name: Concentrate API
  slug: concentrate-api-2
- baseURL: https://api.concentrate.ai
  baseurl_source: declared
  description: The Decisions API from Concentrate — 1 operation(s) for decisions.
  name: Concentrate Decisions API
  slug: concentrate-decisions-api
- baseURL: https://api.concentrate.ai
  baseurl_source: declared
  description: The Messages API from Concentrate — 2 operation(s) for messages.
  name: Concentrate Messages API
  slug: concentrate-messages-api
- baseURL: https://api.concentrate.ai
  baseurl_source: declared
  description: The Models API from Concentrate — 4 operation(s) for models.
  name: Concentrate Models API
  slug: concentrate-models-api
- baseURL: https://api.concentrate.ai
  baseurl_source: declared
  description: The Responses API from Concentrate — 3 operation(s) for responses.
  name: Concentrate Responses API
  slug: concentrate-responses-api
- baseURL: https://api.concentrate.ai
  baseurl_source: declared
  description: The Systemone API from Concentrate — 2 operation(s) for systemone.
  name: Concentrate Systemone API
  slug: concentrate-systemone-api
- baseURL: https://api.concentrate.ai
  baseurl_source: declared
  description: The Chat Completions API from Concentrate — 2 operation(s) for chat completions.
  name: Concentrate Chat Completions API
  slug: concentrate-chat-completions-api
artifact_total: 21
common:
- group: design
  href: https://artifacts.apis.io/concentrate/rules/concentrate-rules.yml
  title: ''
  type: Spectral
  url: rules/concentrate-rules.yml
- group: design
  href: https://artifacts.apis.io/concentrate/json-ld/concentrate-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/concentrate-context.jsonld
- group: design
  href: https://artifacts.apis.io/concentrate/vocabulary/concentrate-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/concentrate-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/concentrate/data-model/concentrate-data-model.yml
  title: ''
  type: DataModel
  url: data-model/concentrate-data-model.yml
- group: auth
  title: ''
  type: Compliance
  url: https://trust.concentrate.ai/
- group: auth
  href: https://artifacts.apis.io/concentrate/authentication/concentrate-authentication.yml
  title: ''
  type: Authentication
  url: authentication/concentrate-authentication.yml
- group: design
  href: https://artifacts.apis.io/concentrate/errors/concentrate-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/concentrate-problem-types.yml
- group: design
  href: https://artifacts.apis.io/concentrate/conformance/concentrate-conformance.yml
  title: ''
  type: Conformance
  url: conformance/concentrate-conformance.yml
- group: agent
  href: https://artifacts.apis.io/concentrate/llms/concentrate-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/concentrate-llms.txt
- group: agent
  href: https://artifacts.apis.io/concentrate/well-known/concentrate-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/concentrate-well-known.yml
- group: other
  href: https://artifacts.apis.io/concentrate/hosts/concentrate-hosts.yml
  title: ''
  type: Hosts
  url: hosts/concentrate-hosts.yml
- group: other
  href: https://artifacts.apis.io/concentrate/vendors/concentrate-vendors.yml
  title: ''
  type: Vendors
  url: vendors/concentrate-vendors.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://status.concentrate.ai/
- group: start
  title: ''
  type: GettingStarted
  url: https://concentrate.ai/docs/getting-started/quickstart
- group: docs
  title: ''
  type: APIReference
  url: https://concentrate.ai/docs/llms.txt
- group: auth
  href: https://artifacts.apis.io/concentrate/security/concentrate-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/concentrate-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/concentrate/security/concentrate-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/concentrate-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://concentrate.ai
- group: docs
  title: ''
  type: Documentation
  url: https://concentrate.ai/docs/api-reference/introduction
- group: company
  title: ''
  type: Blog
  url: https://concentrate.ai/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://concentrate.ai/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://concentrate.ai/legal/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://concentrate.ai/legal/privacy-policy
- group: start
  title: ''
  type: SignUp
  url: https://concentrate.ai/auth/login
coverage:
  checked: '2026-10-29'
  detail: OpenAPI spec at https://concentrate.ai/docs/api-reference/openapi.json is unrelated to Concentrate and cannot be used.
  evidence:
  - status: 200
    url: https://concentrate.ai/docs/api-reference/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-29'
description: Concentrate.ai is a managed LLM gateway that unifies access to dozens of large language models through a single API. It provides spend tracking, fallbacks, team controls, audit logs, security features like SOC 2 Type II compliance, data redaction, and zero‑data‑retention options, enabling teams to integrate AI safely and cost‑effectively.
image: https://concentrate.ai/og-image.png
json_schemas:
- name: GetV1DecisionsResponse
  property_count: 5
  slug: concentrate-get-v1-decisions-response
- name: PostV1ChatCompletionsRequest2
  property_count: 36
  slug: concentrate-post-v1-chat-completions-request2
- name: PostV1ChatCompletionsResponse
  property_count: 10
  slug: concentrate-post-v1-chat-completions-response
- name: PostV1MessagesRequest
  property_count: 28
  slug: concentrate-post-v1-messages-request
- name: PostV1ResponsesRequest
  property_count: 31
  slug: concentrate-post-v1-responses-request
- name: PostV1SystemoneRequest2
  property_count: 4
  slug: concentrate-post-v1-systemone-request2
jsonld:
- class_count: 22
  name: Concentrate Context
  property_count: 90
  slug: concentrate-context
layout: provider
modified: '2026-10-29'
name: Concentrate
nav: Providers
network: true
overview: 'Concentrate is listed with 7 APIs on the [APIs.io](https://apis.io/) network, including Decisions API, Messages API, Models API, and 4 more. Tagged areas include Company, AI, LLM, Gateway, and Platform.


  The Concentrate catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Concentrate''s developer surface includes authentication, getting-started guide, API reference, documentation, engineering blog, pricing, signup flow, and 17 more developer resources.'
plans:
- name: Concentrate Plans Pricing
  plan_count: 0
  slug: concentrate-plans-pricing
random_paper: 22
rate_limits:
- limit_count: 0
  name: Concentrate Rate Limits
  slug: concentrate-rate-limits
rules:
- authorship: generated
  effective_rule_count: 51
  extends:
  - spectral:oas
  name: Concentrate API Rules
  rule_count: 10
  severity_counts:
    error: 8
    hint: 0
    info: 1
    warn: 1
  slug: concentrate-rules
scopes:
- name: Concentrate Scopes
  scope_count: 0
  slug: concentrate-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: developing
  composite: 42.2
  coverage:
    artifact_dirs: 24
    catalog_earned: 65.8
    catalog_earned_first_party: 0.0
    catalog_gap: 49.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 60.5
    contract_governance: 22.0
    contract_quality: 25.9
    developer_ergonomics: 42.9
    discoverability: 71.4
    operational_transparency: 15.8
  provenance:
    conformance: derived
    contracts:
      callable: 87.5
      derived: 7
      marker_coverage: 87.5
      total: 8
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 36.4
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Concentrate Authentication
  slug: concentrate-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Concentrate Domain Security
  slug: concentrate-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: trust-center
  name: Concentrate Trust Center
  slug: concentrate-trust-center
  summary_line: SOC 2, HIPAA
slug: concentrate
tags:
- Company
- AI
- LLM
- Gateway
- Platform
- API
website: https://concentrate.ai
---
