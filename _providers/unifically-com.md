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
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 45.9
  scored_at: '2026-10-31'
api_count: 2
apis:
- description: Create and manage AI generation tasks with a unified interface.
  name: Unified Tasks API
  slug: unified-tasks-api
- baseURL: https://api.unifically.com
  baseurl_source: declared
  description: 'unifically-com API as documented publicly: 21 operations. Contract generated from the documentation by API Evangelist (2026-10-31); not the provider''s own document.'
  name: unifically-com API
  slug: unifically-com-api
artifact_total: 16
common:
- group: design
  href: https://artifacts.apis.io/unifically-com/rules/unifically-com-rules.yml
  title: ''
  type: Spectral
  url: rules/unifically-com-rules.yml
- group: design
  href: https://artifacts.apis.io/unifically-com/json-ld/unifically-com-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/unifically-com-context.jsonld
- group: design
  href: https://artifacts.apis.io/unifically-com/vocabulary/unifically-com-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/unifically-com-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/unifically-com/data-model/unifically-com-data-model.yml
  title: ''
  type: DataModel
  url: data-model/unifically-com-data-model.yml
- group: auth
  href: https://artifacts.apis.io/unifically-com/authentication/unifically-com-authentication.yml
  title: ''
  type: Authentication
  url: authentication/unifically-com-authentication.yml
- group: design
  href: https://artifacts.apis.io/unifically-com/errors/unifically-com-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/unifically-com-problem-types.yml
- group: design
  href: https://artifacts.apis.io/unifically-com/conformance/unifically-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/unifically-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/unifically-com/llms/unifically-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/unifically-com-llms.txt
- group: other
  href: https://artifacts.apis.io/unifically-com/a2a/unifically-com-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/unifically-com-a2a.yml
- group: agent
  href: https://artifacts.apis.io/unifically-com/mcp/unifically-com-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/unifically-com-mcp.yml
- group: agent
  href: https://artifacts.apis.io/unifically-com/well-known/unifically-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/unifically-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/unifically-com/hosts/unifically-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/unifically-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/unifically-com/vendors/unifically-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/unifically-com-vendors.yml
- group: build
  href: https://artifacts.apis.io/unifically-com/packages/unifically-com-packages.yml
  title: ''
  type: SDKs
  url: packages/unifically-com-packages.yml
- group: build
  href: https://artifacts.apis.io/unifically-com/packages/unifically-com-packages.yml
  title: ''
  type: Packages
  url: packages/unifically-com-packages.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://unifically.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://unifically.com/privacy
- group: start
  title: ''
  type: DeveloperPortal
  url: https://api.unifically.com`
- group: auth
  href: https://artifacts.apis.io/unifically-com/security/unifically-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/unifically-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://unifically.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.unifically.com/introduction
- group: docs
  title: ''
  type: APIReference
  url: https://docs.unifically.com/introduction
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.unifically.com/introduction
- group: operate
  title: ''
  type: Support
  url: https://unifically.com/contact
- group: commercial
  title: ''
  type: Pricing
  url: https://unifically.com/pricing
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/unifically
coverage:
  checked: '2026-10-31'
  detail: Docs provide API reference but no OpenAPI/AsyncAPI/GraphQL spec was found.
  evidence:
  - status: 404
    url: https://api.unifically.com/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-31'
description: UnificAlly provides a unified AI API offering over 120 video, image, audio, and text models, including Veo 3.1, Kling, Suno, Nano Banana, Claude, and GPT. It delivers cost‑effective rates up to 85% lower than official pricing, targeting developers and enterprises seeking scalable media AI capabilities. The platform is based in Tbilisi, Georgia, and emphasizes easy integration via a single endpoint.
image: https://unifically.com/static/brand/logo.png
json_schemas:
- name: GetV1ChatCompletionsResponse
  property_count: 6
  slug: unifically-com-get-v1-chat-completions-response
- name: GetV1MessagesResponse
  property_count: 7
  slug: unifically-com-get-v1-messages-response
- name: GetV1ModelsModelidResponse
  property_count: 8
  slug: unifically-com-get-v1-models-modelid-response
- name: GetV1ResourcesGrokVoicesResponse
  property_count: 2
  slug: unifically-com-get-v1-resources-grok-voices-response
- name: GetV1ResponsesResponse
  property_count: 7
  slug: unifically-com-get-v1-responses-response
- name: GetV1TasksResponse
  property_count: 4
  slug: unifically-com-get-v1-tasks-response
jsonld:
- class_count: 26
  name: Unifically Com Context
  property_count: 30
  slug: unifically-com-context
layout: provider
mcp_servers:
- description: Remote MCP server at docs.unically.com.
  name: unifically-com MCP Server
  slug: unifically-com-mcp-yml
modified: '2026-10-31'
name: unifically-com
nav: Providers
network: true
overview: 'unifically-com is listed with 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include AI, Media, Machine-Learning, Startup, and Platform.


  The unifically-com catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  unifically-com''s developer surface includes authentication, documentation, API reference, getting-started guide, support, pricing, and 20 more developer resources.'
plans:
- name: Unifically Com Plans Pricing
  plan_count: 0
  slug: unifically-com-plans-pricing
random_paper: 20
rate_limits:
- limit_count: 0
  name: Unifically Com Rate Limits
  slug: unifically-com-rate-limits
rules:
- authorship: generated
  effective_rule_count: 55
  extends:
  - spectral:oas
  name: unifically-com API Rules
  rule_count: 14
  severity_counts:
    error: 11
    hint: 0
    info: 1
    warn: 2
  slug: unifically-com-rules
scopes:
- name: Unifically Com Scopes
  scope_count: 0
  slug: unifically-com-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: developing
  composite: 49.3
  coverage:
    artifact_dirs: 28
    catalog_earned: 77.7
    catalog_earned_first_party: 0.0
    catalog_gap: 37.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 31.6
    contract_governance: 79.1
    contract_quality: 45.6
    developer_ergonomics: 61.9
    discoverability: 65.0
    operational_transparency: 5.3
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
  name: Unifically Com Authentication
  slug: unifically-com-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Unifically Com Domain Security
  slug: unifically-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: unifically-com
tags:
- AI
- Media
- Machine-Learning
- Startup
- Platform
website: https://unifically.com/
---
