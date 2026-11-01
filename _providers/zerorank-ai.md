---
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
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 47.4
  scored_at: '2026-10-31'
api_count: 2
apis:
- description: API for ZeroRank data access.
  name: ZeroRank API
  slug: zerorank-api
- baseURL: https://api.zerorank.ai/api/v1
  baseurl_source: declared
  description: 'ZeroRank API as documented publicly: 12 operations. Contract generated from the documentation by API Evangelist (2026-10-29); not the provider''s own document.'
  name: ZeroRank API
  slug: zerorank-ai-api
artifact_total: 20
common:
- group: operate
  href: https://artifacts.apis.io/zerorank-ai/rate-limits/zerorank-ai-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/zerorank-ai-rate-limits.yml
- group: design
  href: https://artifacts.apis.io/zerorank-ai/rules/zerorank-ai-rules.yml
  title: ''
  type: Spectral
  url: rules/zerorank-ai-rules.yml
- group: design
  href: https://artifacts.apis.io/zerorank-ai/json-ld/zerorank-ai-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/zerorank-ai-context.jsonld
- group: design
  href: https://artifacts.apis.io/zerorank-ai/vocabulary/zerorank-ai-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/zerorank-ai-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/zerorank-ai/data-model/zerorank-ai-data-model.yml
  title: ''
  type: DataModel
  url: data-model/zerorank-ai-data-model.yml
- group: auth
  href: https://artifacts.apis.io/zerorank-ai/authentication/zerorank-ai-authentication.yml
  title: ''
  type: Authentication
  url: authentication/zerorank-ai-authentication.yml
- group: auth
  href: https://artifacts.apis.io/zerorank-ai/scopes/zerorank-ai-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/zerorank-ai-scopes.yml
- group: design
  href: https://artifacts.apis.io/zerorank-ai/conformance/zerorank-ai-conformance.yml
  title: ''
  type: Conformance
  url: conformance/zerorank-ai-conformance.yml
- group: agent
  href: https://artifacts.apis.io/zerorank-ai/llms/zerorank-ai-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/zerorank-ai-llms.txt
- group: other
  href: https://artifacts.apis.io/zerorank-ai/a2a/zerorank-ai-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/zerorank-ai-a2a.yml
- group: build
  href: https://artifacts.apis.io/zerorank-ai/mcp/zerorank-ai-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/zerorank-ai-tool-crosswalk.yml
- group: agent
  href: https://artifacts.apis.io/zerorank-ai/mcp/zerorank-ai-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/zerorank-ai-mcp.yml
- group: agent
  href: https://artifacts.apis.io/zerorank-ai/well-known/zerorank-ai-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/zerorank-ai-well-known.yml
- group: other
  href: https://artifacts.apis.io/zerorank-ai/hosts/zerorank-ai-hosts.yml
  title: ''
  type: Hosts
  url: hosts/zerorank-ai-hosts.yml
- group: other
  href: https://artifacts.apis.io/zerorank-ai/vendors/zerorank-ai-vendors.yml
  title: ''
  type: Vendors
  url: vendors/zerorank-ai-vendors.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://status.zerorank.ai/en/
- group: start
  title: ''
  type: SignUp
  url: https://app.zerorank.ai/signup
- group: operate
  title: ''
  type: Roadmap
  url: https://zerorank.ai/roadmap
- group: start
  title: ''
  type: DeveloperPortal
  url: https://dev.zerorank.ai/
- group: operate
  title: ''
  type: ChangeLog
  url: https://zerorank.ai/changelog
- group: auth
  href: https://artifacts.apis.io/zerorank-ai/security/zerorank-ai-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/zerorank-ai-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://zerorank.ai
- group: docs
  title: ''
  type: Documentation
  url: https://docs.zerorank.ai
- group: docs
  title: ''
  type: APIReference
  url: https://docs.zerorank.ai/api/overview
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.zerorank.ai/start/what-is-zerorank
- group: company
  title: ''
  type: Blog
  url: https://zerorank.ai/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://zerorank.ai/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://zerorank.ai/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://zerorank.ai/privacy
- group: operate
  title: ''
  type: Support
  url: https://zerorank.ai/contact
coverage:
  checked: '2026-10-29'
  detail: The API documentation is public but the OpenAPI spec is only accessible via the MCP tool and not via a direct GET request.
  evidence:
  - status: 200
    url: https://docs.zerorank.ai
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-29'
description: ZeroRank provides AI search visibility tracking, allowing brands to monitor how large language models like ChatGPT, Claude and Google cite them. The platform offers prompt research, AI visibility analytics, on‑page and off‑page optimization, and agentic workflows. Users can access data via a REST API (base https://api.zerorank.ai/api/v1) or MCP chat integration, with rate‑limit headers and JSON responses.
image: https://zerorank.ai/assets/apple-touch-icon.png
json_schemas:
- name: GetApiV1ChatsChatidResponse
  property_count: 3
  slug: zerorank-ai-get-api-v1-chats-chatid-response
- name: GetChatsIdResponse
  property_count: 3
  slug: zerorank-ai-get-chats-id-response
- name: GetChatsResponse
  property_count: 1
  slug: zerorank-ai-get-chats-response
- name: PatchBrandsIdRequest
  property_count: 8
  slug: zerorank-ai-patch-brands-id-request
- name: PatchBrandsIdResponse
  property_count: 3
  slug: zerorank-ai-patch-brands-id-response
- name: PutBrandsIdRequest
  property_count: 1
  slug: zerorank-ai-put-brands-id-request
- name: PutPromptsIdRequest
  property_count: 1
  slug: zerorank-ai-put-prompts-id-request
- name: PutPromptsIdResponse
  property_count: 1
  slug: zerorank-ai-put-prompts-id-response
- name: PutTagsIdRequest
  property_count: 1
  slug: zerorank-ai-put-tags-id-request
- name: PutTopicsIdRequest
  property_count: 1
  slug: zerorank-ai-put-topics-id-request
jsonld:
- class_count: 4
  name: Zerorank Ai Context
  property_count: 14
  slug: zerorank-ai-context
layout: provider
mcp_servers:
- description: Remote MCP server at docs.zerorank.ai.
  name: ZeroRank MCP Server
  slug: zerorank-ai-mcp-yml
modified: '2026-10-29'
name: ZeroRank
nav: Providers
network: true
overview: 'ZeroRank is listed with 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include AI, SearchVisibility, Analytics, Platform, and Company.


  The ZeroRank catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  ZeroRank''s developer surface includes authentication, signup flow, changelog, documentation, API reference, getting-started guide, engineering blog, and 23 more developer resources.'
plans:
- name: Zerorank Ai Plans Pricing
  plan_count: 0
  slug: zerorank-ai-plans-pricing
random_paper: 19
rate_limits:
- limit_count: 1
  name: Zerorank Ai Rate Limits
  slug: zerorank-ai-rate-limits
rules:
- authorship: generated
  effective_rule_count: 53
  extends:
  - spectral:oas
  name: ZeroRank API Rules
  rule_count: 12
  severity_counts:
    error: 10
    hint: 0
    info: 1
    warn: 1
  slug: zerorank-ai-rules
scopes:
- name: Zerorank Ai Scopes
  scope_count: 0
  slug: zerorank-ai-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: developing
  composite: 45.4
  coverage:
    artifact_dirs: 26
    catalog_earned: 67.8
    catalog_earned_first_party: 8.0
    catalog_gap: 47.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 44.7
    contract_governance: 22.0
    contract_quality: 23.5
    developer_ergonomics: 57.1
    discoverability: 65.0
    operational_transparency: 57.9
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 7
      marker_coverage: 100.0
      total: 7
    mcp: first-party
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 31.8
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Zerorank Ai Authentication
  slug: zerorank-ai-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Zerorank Ai Domain Security
  slug: zerorank-ai-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: zerorank-ai
tags:
- AI
- SearchVisibility
- Analytics
- Platform
- Company
website: https://zerorank.ai
---
