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
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 25.6
  scored_at: '2026-10-31'
api_count: 2
apis:
- description: Unified API providing access to OpenAI, Claude, Gemini, DeepSeek and other models via a single endpoint.
  name: Store API
  slug: store-api
- description: 'store-api-com API as documented publicly: 3 operations. Contract generated from the documentation by API Evangelist (2026-10-31); not the provider''s own document.'
  name: store-api-com API
  slug: store-api-com-api
artifact_total: 14
common:
- group: design
  href: https://artifacts.apis.io/store-api-com/rules/store-api-com-rules.yml
  title: ''
  type: Spectral
  url: rules/store-api-com-rules.yml
- group: design
  href: https://artifacts.apis.io/store-api-com/json-ld/store-api-com-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/store-api-com-context.jsonld
- group: design
  href: https://artifacts.apis.io/store-api-com/vocabulary/store-api-com-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/store-api-com-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/store-api-com/data-model/store-api-com-data-model.yml
  title: ''
  type: DataModel
  url: data-model/store-api-com-data-model.yml
- group: auth
  href: https://artifacts.apis.io/store-api-com/authentication/store-api-com-authentication.yml
  title: ''
  type: Authentication
  url: authentication/store-api-com-authentication.yml
- group: design
  href: https://artifacts.apis.io/store-api-com/errors/store-api-com-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/store-api-com-problem-types.yml
- group: design
  href: https://artifacts.apis.io/store-api-com/conformance/store-api-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/store-api-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/store-api-com/llms/store-api-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/store-api-com-llms.txt
- group: agent
  href: https://artifacts.apis.io/store-api-com/mcp/store-api-com-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/store-api-com-mcp.yml
- group: other
  href: https://artifacts.apis.io/store-api-com/hosts/store-api-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/store-api-com-hosts.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://store-api.com/status
- group: start
  title: ''
  type: Sandbox
  url: https://store-api.com/playground
- group: auth
  href: https://artifacts.apis.io/store-api-com/security/store-api-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/store-api-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://store-api.com/
- group: docs
  title: ''
  type: Documentation
  url: https://store-api.com/docs
- group: docs
  title: ''
  type: APIReference
  url: https://store-api.com/docs
- group: start
  title: ''
  type: GettingStarted
  url: https://store-api.com/docs
- group: operate
  title: ''
  type: Support
  url: https://store-api.com/contacts
- group: company
  title: ''
  type: Blog
  url: https://store-api.com/blog
- group: start
  title: ''
  type: SignUp
  url: https://store-api.com/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://store-api.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://store-api.com/privacy
- group: commercial
  title: ''
  type: Pricing
  url: https://store-api.com/#plans
created: '2026-10-31'
description: Store API (store-api.com) provides a unified API key for accessing OpenAI, Claude, Gemini, and DeepSeek models from within Russia. It offers fast token‑based activation, Russian‑card payments, no VPN requirement, and transparent pricing. The service includes documentation, a playground, and support tailored for Russian developers and businesses. By aggregating multiple large‑language‑model providers, Store API simplifies integration, handling authentication, request routing, and billing in a single endpoint, enabling developers to build AI‑powered applications quickly and cost‑effectively.
image: https://store-api.com/icon.svg
json_schemas:
- name: GetV1ModelsResponse
  property_count: 1
  slug: store-api-com-get-v1-models-response
- name: PostV1ChatCompletionsRequest
  property_count: 2
  slug: store-api-com-post-v1-chat-completions-request
- name: PostV1ImagesGenerationsRequest
  property_count: 3
  slug: store-api-com-post-v1-images-generations-request
- name: PostV1ImagesGenerationsResponse
  property_count: 2
  slug: store-api-com-post-v1-images-generations-response
jsonld:
- class_count: 4
  name: Store Api Com Context
  property_count: 6
  slug: store-api-com-context
layout: provider
mcp_servers:
- description: Remote MCP server at store-api.com requiring an API key.
  name: store-api-com MCP Server
  slug: store-api-com-mcp-yml
modified: '2026-10-31'
name: store-api-com
nav: Providers
network: true
overview: 'store-api-com is listed with 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Company, AI, Machine-Learning, OpenAI, and Claude.


  The store-api-com catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  store-api-com''s developer surface includes authentication, sandbox, documentation, API reference, getting-started guide, support, engineering blog, and 16 more developer resources.'
plans:
- name: Store Api Com Plans Pricing
  plan_count: 0
  slug: store-api-com-plans-pricing
random_paper: 8
rate_limits:
- limit_count: 0
  name: Store Api Com Rate Limits
  slug: store-api-com-rate-limits
rules:
- authorship: generated
  effective_rule_count: 53
  extends:
  - spectral:oas
  name: store-api-com API Rules
  rule_count: 12
  severity_counts:
    error: 10
    hint: 0
    info: 1
    warn: 1
  slug: store-api-com-rules
scopes:
- name: Store Api Com Scopes
  scope_count: 0
  slug: store-api-com-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: developing
  composite: 50.4
  coverage:
    artifact_dirs: 28
    catalog_earned: 66.7
    catalog_earned_first_party: 0.0
    catalog_gap: 48.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 44.7
    contract_governance: 79.1
    contract_quality: 47.5
    developer_ergonomics: 54.8
    discoverability: 56.7
    operational_transparency: 15.8
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 29.2
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Store Api Com Authentication
  slug: store-api-com-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Store Api Com Domain Security
  slug: store-api-com-domain-security
  summary_line: TLSv1.3 · DNSSEC
slug: store-api-com
tags:
- Company
- AI
- Machine-Learning
- OpenAI
- Claude
- Gemini
- Russia
- Payments
website: https://store-api.com/
---
