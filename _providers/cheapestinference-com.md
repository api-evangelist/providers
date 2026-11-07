---
access_model:
  confidence: medium
  label: Paid
  onboarding: unknown
  pricing: paid
  public: false
  source:
  - plans
  - authentication
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: flavored
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    mcp_tool_quality: na
    openapi_examples: partial
    operation_distinctiveness: mostly
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 28.4
  scored_at: '2026-11-06'
api_count: 4
apis:
- description: Management API for listing pools and billing status.
  name: CheapestInference Management API
  slug: cheapestinference-management-api
- baseURL: https://api.cheapestinference.com
  baseurl_source: declared
  description: 'cheapestinference-com api API as documented publicly: 36 operations. Contract generated from the documentation by API Evangelist (2026-10-30); not the provider''s own document.'
  name: cheapestinference-com api API
  slug: api-api
- baseURL: https://api.cheapestinference.com
  baseurl_source: declared
  description: 'cheapestinference-com core API as documented publicly: 1 operations. Contract generated from the documentation by API Evangelist (2026-10-30); not the provider''s own document.'
  name: cheapestinference-com core API
  slug: core-api
- baseURL: https://api.cheapestinference.com
  baseurl_source: declared
  description: 'cheapestinference-com guides API as documented publicly: 6 operations. Contract generated from the documentation by API Evangelist (2026-10-30); not the provider''s own document.'
  name: cheapestinference-com guides API
  slug: guides-api
artifact_total: 22
common:
- group: commercial
  href: https://artifacts.apis.io/cheapestinference-com/plans/cheapestinference-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/cheapestinference-com-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/cheapestinference-com/rules/cheapestinference-com-rules.yml
  title: ''
  type: Spectral
  url: rules/cheapestinference-com-rules.yml
- group: design
  href: https://artifacts.apis.io/cheapestinference-com/json-ld/cheapestinference-com-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/cheapestinference-com-context.jsonld
- group: design
  href: https://artifacts.apis.io/cheapestinference-com/vocabulary/cheapestinference-com-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/cheapestinference-com-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/cheapestinference-com/data-model/cheapestinference-com-data-model.yml
  title: ''
  type: DataModel
  url: data-model/cheapestinference-com-data-model.yml
- group: auth
  href: https://artifacts.apis.io/cheapestinference-com/authentication/cheapestinference-com-authentication.yml
  title: ''
  type: Authentication
  url: authentication/cheapestinference-com-authentication.yml
- group: design
  href: https://artifacts.apis.io/cheapestinference-com/conformance/cheapestinference-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/cheapestinference-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/cheapestinference-com/llms/cheapestinference-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/cheapestinference-com-llms.txt
- group: other
  href: https://artifacts.apis.io/cheapestinference-com/a2a/cheapestinference-com-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/cheapestinference-com-a2a.yml
- group: other
  href: https://artifacts.apis.io/cheapestinference-com/hosts/cheapestinference-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/cheapestinference-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/cheapestinference-com/vendors/cheapestinference-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/cheapestinference-com-vendors.yml
- group: build
  href: https://artifacts.apis.io/cheapestinference-com/packages/cheapestinference-com-packages.yml
  title: ''
  type: SDKs
  url: packages/cheapestinference-com-packages.yml
- group: build
  href: https://artifacts.apis.io/cheapestinference-com/packages/cheapestinference-com-packages.yml
  title: ''
  type: Packages
  url: packages/cheapestinference-com-packages.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://cheapestinference.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://cheapestinference.com/privacy
- group: operate
  title: ''
  type: ChangeLog
  url: https://cheapestinference.com/docs/changelog/
- group: auth
  href: https://artifacts.apis.io/cheapestinference-com/security/cheapestinference-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/cheapestinference-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://cheapestinference.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://cheapestinference.com/docs/getting-started/overview/
- group: docs
  title: ''
  type: Documentation
  url: https://cheapestinference.com/docs/getting-started/overview/
- group: docs
  title: ''
  type: APIReference
  url: https://cheapestinference.com/docs/getting-started/overview/
- group: start
  title: ''
  type: GettingStarted
  url: https://cheapestinference.com/docs/getting-started/overview/
- group: company
  title: ''
  type: Blog
  url: https://cheapestinference.com/blog/
- group: commercial
  title: ''
  type: Pricing
  url: https://cheapestinference.com/pools/
- group: start
  title: ''
  type: SignUp
  url: https://cheapestinference.com/login
- group: start
  title: ''
  type: Login
  url: https://cheapestinference.com/login
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/cheapestinference
created: '2026-10-30'
description: CheapestInference offers flat-rate, unlimited AI inference for frontier open-source large language models. Customers reserve daily 8-hour time blocks and pay a fixed monthly fee, avoiding per-token billing. Plans start at $22 / month for core models and scale up to premium pools, with support for OpenAI-compatible and Anthropic-compatible SDKs, tool calling, and native Claude Code integration. The service runs on secure, audited infrastructure, provides GDPR-friendly data handling, and does not store user prompts or responses.
image: https://cheapestinference.com/og.png
json_schemas:
- name: GetApiAgentPlansResponse
  property_count: 3
  slug: cheapestinference-com-get-api-agent-plans-response
- name: GetApiPoolsResponse
  property_count: 2
  slug: cheapestinference-com-get-api-pools-response
- name: GetApiUsageKeyidResponse
  property_count: 8
  slug: cheapestinference-com-get-api-usage-keyid-response
- name: GetApiUsageResponse
  property_count: 10
  slug: cheapestinference-com-get-api-usage-response
- name: GetWellKnownAgentJsonResponse
  property_count: 4
  slug: cheapestinference-com-get-well-known-agent-json-response
- name: PostAnthropicV1MessagesRequest
  property_count: 5
  slug: cheapestinference-com-post-anthropic-v1-messages-request
- name: PostApiAgentPlansResponse
  property_count: 2
  slug: cheapestinference-com-post-api-agent-plans-response
- name: PostApiAgentSubscribePoolRequest
  property_count: 4
  slug: cheapestinference-com-post-api-agent-subscribe-pool-request
- name: PostApiAgentSubscribePoolResponse
  property_count: 9
  slug: cheapestinference-com-post-api-agent-subscribe-pool-response
- name: PostV1ChatCompletionsRequest
  property_count: 5
  slug: cheapestinference-com-post-v1-chat-completions-request
- name: PostV1ChatCompletionsResponse
  property_count: 9
  slug: cheapestinference-com-post-v1-chat-completions-response
jsonld:
- class_count: 39
  name: Cheapestinference Com Context
  property_count: 47
  slug: cheapestinference-com-context
layout: provider
modified: '2026-10-30'
name: cheapestinference-com
nav: Providers
network: true
overview: 'cheapestinference-com is listed with 4 APIs on the [APIs.io](https://apis.io/) network, including api API, core API, guides API, and 1 more. Tagged areas include Artificial Intelligence, Inference, LLM, Flat Rate, and Software-as-a-Service.


  The cheapestinference-com catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  cheapestinference-com''s developer surface includes authentication, changelog, documentation, API reference, getting-started guide, engineering blog, pricing, and 20 more developer resources.'
plans:
- name: Cheapestinference Com Plans Pricing
  plan_count: 3
  slug: cheapestinference-com-plans-pricing
random_paper: 16
rate_limits:
- limit_count: 0
  name: Cheapestinference Com Rate Limits
  slug: cheapestinference-com-rate-limits
rules:
- authorship: generated
  effective_rule_count: 52
  extends:
  - spectral:oas
  name: cheapestinference-com API Rules
  rule_count: 11
  severity_counts:
    error: 9
    hint: 0
    info: 1
    warn: 1
  slug: cheapestinference-com-rules
scopes:
- name: Cheapestinference Com Scopes
  scope_count: 0
  slug: cheapestinference-com-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: thin
  composite: 38.1
  coverage:
    artifact_dirs: 30
    catalog_earned: 77.8
    catalog_earned_first_party: 12.0
    catalog_gap: 37.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -10.4
  facets:
    access_clarity: 53.9
    contract_governance: 22.0
    contract_quality: 25.4
    developer_ergonomics: 39.3
    discoverability: 71.4
    operational_transparency: 10.5
  previous_composite: 48.5
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 4
      marker_coverage: 100.0
      total: 4
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 28.2
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/cheapestinference-com/cheapestinference-com-2026-11-03T123922.png
security:
- kind: authentication
  name: Cheapestinference Com Authentication
  slug: cheapestinference-com-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Cheapestinference Com Domain Security
  slug: cheapestinference-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: cheapestinference-com
tags:
- Artificial Intelligence
- Inference
- LLM
- Flat Rate
- Software-as-a-Service
website: https://cheapestinference.com/
---
