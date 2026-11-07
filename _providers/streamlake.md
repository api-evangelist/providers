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
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 18.3
  scored_at: '2026-11-06'
api_count: 1
apis:
- baseURL: https://vanchin.streamlake.ai/api/gateway/v1/endpoints
  baseurl_source: declared
  description: The Gateway API from StreamLake — 1 operation(s) for gateway.
  name: StreamLake Gateway API
  slug: streamlake-gateway-api
artifact_total: 9
common:
- group: commercial
  href: https://artifacts.apis.io/streamlake/plans/streamlake-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/streamlake-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/streamlake/rules/streamlake-rules.yml
  title: ''
  type: Spectral
  url: rules/streamlake-rules.yml
- group: design
  href: https://artifacts.apis.io/streamlake/json-ld/streamlake-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/streamlake-context.jsonld
- group: design
  href: https://artifacts.apis.io/streamlake/vocabulary/streamlake-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/streamlake-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/streamlake/data-model/streamlake-data-model.yml
  title: ''
  type: DataModel
  url: data-model/streamlake-data-model.yml
- group: operate
  href: https://artifacts.apis.io/streamlake/changelog/streamlake-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/streamlake-changelog.yml
- group: auth
  href: https://artifacts.apis.io/streamlake/authentication/streamlake-authentication.yml
  title: ''
  type: Authentication
  url: authentication/streamlake-authentication.yml
- group: design
  href: https://artifacts.apis.io/streamlake/lifecycle/streamlake-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/streamlake-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/streamlake/errors/streamlake-error-codes.yml
  title: ''
  type: ErrorCatalog
  url: errors/streamlake-error-codes.yml
- group: design
  href: https://artifacts.apis.io/streamlake/conformance/streamlake-conformance.yml
  title: ''
  type: Conformance
  url: conformance/streamlake-conformance.yml
- group: other
  href: https://artifacts.apis.io/streamlake/hosts/streamlake-hosts.yml
  title: ''
  type: Hosts
  url: hosts/streamlake-hosts.yml
- group: auth
  href: https://artifacts.apis.io/streamlake/security/streamlake-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/streamlake-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://streamlake.ai
- group: docs
  title: ''
  type: Documentation
  url: https://streamlake.ai/document
- group: docs
  title: ''
  type: APIReference
  url: https://streamlake.ai/document/DOC/mj9z6fh8lxn87i86jrp
- group: start
  title: ''
  type: GettingStarted
  url: https://streamlake.ai/document/DOC/mg6k6nlp8j6qxicx4c9
- group: auth
  title: ''
  type: Authentication
  url: https://streamlake.ai/document/DOC/mkaylxzkso38sqxcpa
- group: commercial
  title: ''
  type: Pricing
  url: https://streamlake.ai/document/DOC/mgrnm4xm362hvp5wyce
- group: operate
  title: ''
  type: Support
  url: https://streamlake.ai/support/support-help
- group: start
  title: ''
  type: SignUp
  url: https://console.streamlake.ai/console/user/sign-up/tenant
- group: start
  title: ''
  type: Login
  url: https://console.streamlake.ai/console/user/tenant-login
- group: start
  title: ''
  type: Console
  url: https://console.streamlake.ai/console/home/index
- group: commercial
  title: ''
  type: TermsOfService
  url: https://streamlake.ai/document/DOC/mgkchnd89grpt1961fw
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://streamlake.ai/document/DOC/mgkci47q13qr66h9i54
- group: company
  title: ''
  type: Newsroom
  url: https://www.streamlake.ai/product/wanqing/components/news
- group: build
  title: ''
  type: SDKs
  url: https://www.streamlake.ai/product/sdk
- group: operate
  title: ''
  type: StatusPage
  url: https://status.streamlake.ai
created: '2026-10-13'
description: StreamLake (STREAMLAKE PTE. LTD.) is the cloud and AI model platform of Kuaishou. Its Vanchin model service offers pay-as-you-go and Coding Plan access to KwaiKAT (KAT-Coder) models and hosted third-party open models (Qwen, DeepSeek, GLM, Kimi, MiniMax, MiMo) through an OpenAI-compatible chat completions endpoint and a Claude Code compatible proxy at vanchin.streamlake.ai, alongside audio and video SDKs for capture, editing and playback.
finops:
- has_sources: true
  method: derived
  name: Streamlake Finops
  primary_unit: million tokens
  service_category: ''
  slug: streamlake-finops
  template: false
image: https://www.streamlake.ai/img/StreamLake_1200-630.png
json_schemas:
- name: PostApiGatewayV1EndpointsChatCompletionsRequest
  property_count: 10
  slug: streamlake-post-api-gateway-v1-endpoints-chat-completions-request
- name: PostApiGatewayV1EndpointsChatCompletionsResponse
  property_count: 7
  slug: streamlake-post-api-gateway-v1-endpoints-chat-completions-response
jsonld:
- class_count: 2
  name: Streamlake Context
  property_count: 16
  slug: streamlake-context
layout: provider
modified: '2026-10-13'
name: StreamLake
nav: Providers
network: true
overview: 'StreamLake is listed with 1 API on the [APIs.io](https://apis.io/) network: Gateway API. Tagged areas include Company, Artificial Intelligence, LLM, Model Inference, and Chat Completions.


  The StreamLake catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  StreamLake''s developer surface includes changelog, authentication, documentation, API reference, getting-started guide, pricing, support, and 20 more developer resources.'
plans:
- name: Streamlake Plans Pricing
  plan_count: 9
  slug: streamlake-plans-pricing
random_paper: 9
rules:
- authorship: generated
  effective_rule_count: 54
  extends:
  - spectral:oas
  name: StreamLake API Rules
  rule_count: 13
  severity_counts:
    error: 11
    hint: 0
    info: 1
    warn: 1
  slug: streamlake-rules
score:
  band: thin
  composite: 37.2
  coverage:
    artifact_dirs: 21
    catalog_earned: 74.8
    catalog_earned_first_party: 12.0
    catalog_gap: 40.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -11.4
  facets:
    access_clarity: 61.8
    contract_governance: 22.0
    contract_quality: 23.5
    developer_ergonomics: 33.3
    discoverability: 67.0
    operational_transparency: 23.7
  previous_composite: 48.6
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 2
      marker_coverage: 100.0
      total: 2
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 19.1
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/streamlake/streamlake-2026-11-03T143914.png
security:
- kind: authentication
  name: Streamlake Authentication
  slug: streamlake-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Streamlake Domain Security
  slug: streamlake-domain-security
  summary_line: TLSv1.2
slug: streamlake
tags:
- Company
- Artificial Intelligence
- LLM
- Model Inference
- Chat Completions
- AI Coding
- Kuaishou
website: https://streamlake.ai
---
