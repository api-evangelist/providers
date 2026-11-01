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
    openapi_examples: partial
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 28.0
  scored_at: '2026-10-31'
api_count: 4
apis:
- description: FastMetal AI provides an OpenAI‑compatible API for text, image, and video generation across 90+ models.
  name: FastMetal AI API
  slug: fastmetal-ai-api
- baseURL: https://api.fastmetal.ai
  baseurl_source: declared
  description: 'fastmetal-ai api API as documented publicly: 7 operations. Contract generated from the documentation by API Evangelist (2026-10-30); not the provider''s own document.'
  name: fastmetal-ai api API
  slug: api-api
- baseURL: https://api.fastmetal.ai
  baseurl_source: declared
  description: 'fastmetal-ai core API as documented publicly: 4 operations. Contract generated from the documentation by API Evangelist (2026-10-30); not the provider''s own document.'
  name: fastmetal-ai core API
  slug: core-api
- baseURL: https://api.fastmetal.ai
  baseurl_source: declared
  description: 'fastmetal-ai All guides API as documented publicly: 3 operations. Contract generated from the documentation by API Evangelist (2026-10-30); not the provider''s own document.'
  name: fastmetal-ai All guides API
  slug: guides-api
artifact_total: 24
common:
- group: design
  href: https://artifacts.apis.io/fastmetal-ai/rules/fastmetal-ai-rules.yml
  title: ''
  type: Spectral
  url: rules/fastmetal-ai-rules.yml
- group: design
  href: https://artifacts.apis.io/fastmetal-ai/json-ld/fastmetal-ai-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/fastmetal-ai-context.jsonld
- group: design
  href: https://artifacts.apis.io/fastmetal-ai/vocabulary/fastmetal-ai-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/fastmetal-ai-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/fastmetal-ai/data-model/fastmetal-ai-data-model.yml
  title: ''
  type: DataModel
  url: data-model/fastmetal-ai-data-model.yml
- group: auth
  href: https://artifacts.apis.io/fastmetal-ai/authentication/fastmetal-ai-authentication.yml
  title: ''
  type: Authentication
  url: authentication/fastmetal-ai-authentication.yml
- group: design
  href: https://artifacts.apis.io/fastmetal-ai/errors/fastmetal-ai-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/fastmetal-ai-problem-types.yml
- group: design
  href: https://artifacts.apis.io/fastmetal-ai/conformance/fastmetal-ai-conformance.yml
  title: ''
  type: Conformance
  url: conformance/fastmetal-ai-conformance.yml
- group: agent
  href: https://artifacts.apis.io/fastmetal-ai/llms/fastmetal-ai-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/fastmetal-ai-llms.txt
- group: agent
  href: https://artifacts.apis.io/fastmetal-ai/mcp/fastmetal-ai-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/fastmetal-ai-mcp.yml
- group: other
  href: https://artifacts.apis.io/fastmetal-ai/hosts/fastmetal-ai-hosts.yml
  title: ''
  type: Hosts
  url: hosts/fastmetal-ai-hosts.yml
- group: other
  href: https://artifacts.apis.io/fastmetal-ai/vendors/fastmetal-ai-vendors.yml
  title: ''
  type: Vendors
  url: vendors/fastmetal-ai-vendors.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://fastmetal.ai/status
- group: auth
  href: https://artifacts.apis.io/fastmetal-ai/security/fastmetal-ai-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/fastmetal-ai-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://fastmetal.ai/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://fastmetal.ai/docs
- group: docs
  title: ''
  type: Documentation
  url: https://fastmetal.ai/docs
- group: docs
  title: ''
  type: APIReference
  url: https://fastmetal.ai/docs/api/overview
- group: start
  title: ''
  type: GettingStarted
  url: https://fastmetal.ai/docs/guides/mcp
- group: operate
  title: ''
  type: Support
  url: https://fastmetal.ai/contact
- group: company
  title: ''
  type: Blog
  url: https://fastmetal.ai/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://fastmetal.ai/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://fastmetal.ai/legal/terms
coverage:
  checked: '2026-10-30'
  detail: Public documentation exists but no OpenAPI, AsyncAPI, GraphQL, or other machine‑readable spec is published.
  evidence:
  - status: 200
    url: https://fastmetal.ai/docs/api/overview
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-30'
description: FastMetal AI provides an OpenAI‑compatible gateway to over 90 AI models spanning text, image, and video generation. Developers can access a unified API with a single API key, paying per token in yen or US dollars. The platform offers flexible pricing, enterprise plans, and extensive documentation to integrate AI capabilities quickly. FastMetal AI aims to simplify AI adoption across industries by delivering high‑performance, scalable inference through a cloud‑native service.
image: https://fastmetal.ai/landing/og-preview.jpg
json_schemas:
- name: GetKeyInfoResponse
  property_count: 2
  slug: fastmetal-ai-get-key-info-response
- name: GetV1ChatCompletionsResponse
  property_count: 3
  slug: fastmetal-ai-get-v1-chat-completions-response
- name: GetV1VideosJobsIdResponse
  property_count: 4
  slug: fastmetal-ai-get-v1-videos-jobs-id-response
- name: PostMcpRequest
  property_count: 4
  slug: fastmetal-ai-post-mcp-request
- name: PostV1ChatCompletionsRequest
  property_count: 3
  slug: fastmetal-ai-post-v1-chat-completions-request
- name: PostV1CompletionsRequest
  property_count: 4
  slug: fastmetal-ai-post-v1-completions-request
- name: PostV1DecisionsJev113Request
  property_count: 2
  slug: fastmetal-ai-post-v1-decisions-jev113-request
- name: PostV1MessagesCountTokensRequest
  property_count: 2
  slug: fastmetal-ai-post-v1-messages-count-tokens-request
- name: PostV1MessagesRequest
  property_count: 9
  slug: fastmetal-ai-post-v1-messages-request
- name: PostV1MessagesResponse
  property_count: 7
  slug: fastmetal-ai-post-v1-messages-response
- name: PostV1VideosCreateRequest
  property_count: 2
  slug: fastmetal-ai-post-v1-videos-create-request
- name: PostV1VideosCreateResponse
  property_count: 3
  slug: fastmetal-ai-post-v1-videos-create-response
jsonld:
- class_count: 15
  name: Fastmetal Ai Context
  property_count: 30
  slug: fastmetal-ai-context
layout: provider
mcp_servers:
- description: Remote MCP server at fastmetal.ai.
  name: fastmetal-ai MCP Server
  slug: fastmetal-ai-mcp-yml
modified: '2026-10-30'
name: fastmetal-ai
nav: Providers
network: true
overview: 'fastmetal-ai is listed with 4 APIs on the [APIs.io](https://apis.io/) network, including api API, core API, All guides API, and 1 more. Tagged areas include Company, AI, API, Platform, and Cloud.


  The fastmetal-ai catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  fastmetal-ai''s developer surface includes authentication, documentation, API reference, getting-started guide, support, engineering blog, pricing, and 15 more developer resources.'
plans:
- name: Fastmetal Ai Plans Pricing
  plan_count: 0
  slug: fastmetal-ai-plans-pricing
random_paper: 8
rate_limits:
- limit_count: 0
  name: Fastmetal Ai Rate Limits
  slug: fastmetal-ai-rate-limits
rules:
- authorship: generated
  effective_rule_count: 54
  extends:
  - spectral:oas
  name: fastmetal-ai API Rules
  rule_count: 13
  severity_counts:
    error: 11
    hint: 0
    info: 1
    warn: 1
  slug: fastmetal-ai-rules
scopes:
- name: Fastmetal Ai Scopes
  scope_count: 0
  slug: fastmetal-ai-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: developing
  composite: 49.7
  coverage:
    artifact_dirs: 23
    catalog_earned: 80.7
    catalog_earned_first_party: 0.0
    catalog_gap: 34.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 21.1
    contract_governance: 79.1
    contract_quality: 54.1
    developer_ergonomics: 57.1
    discoverability: 70.0
    operational_transparency: 15.8
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 28.2
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Fastmetal Ai Authentication
  slug: fastmetal-ai-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Fastmetal Ai Domain Security
  slug: fastmetal-ai-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: fastmetal-ai
tags:
- Company
- AI
- API
- Platform
- Cloud
website: https://fastmetal.ai/
---
