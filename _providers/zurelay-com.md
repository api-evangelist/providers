---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - authentication
  - security
  trial: false
  try_now: false
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
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: false
    pagination_ratio: false
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 34.0
  scored_at: '2026-11-06'
api_count: 1
apis:
- baseURL: https://api.zurelay.com
  baseurl_source: declared
  description: 'zurelay-com API as documented publicly: 16 operations. Contract generated from the documentation by API Evangelist (2026-10-31); not the provider''s own document.'
  name: zurelay-com API
  slug: zurelay-com-api
artifact_total: 12
asyncapis:
- description: ''
  name: Zurelay Com Webhooks
  slug: zurelay-com-webhooks
common:
- group: design
  href: https://artifacts.apis.io/zurelay-com/rules/zurelay-com-rules.yml
  title: ''
  type: Spectral
  url: rules/zurelay-com-rules.yml
- group: design
  href: https://artifacts.apis.io/zurelay-com/json-ld/zurelay-com-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/zurelay-com-context.jsonld
- group: design
  href: https://artifacts.apis.io/zurelay-com/vocabulary/zurelay-com-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/zurelay-com-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/zurelay-com/asyncapi/zurelay-com-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/zurelay-com-webhooks.yml
- group: design
  href: https://artifacts.apis.io/zurelay-com/data-model/zurelay-com-data-model.yml
  title: ''
  type: DataModel
  url: data-model/zurelay-com-data-model.yml
- group: auth
  href: https://artifacts.apis.io/zurelay-com/authentication/zurelay-com-authentication.yml
  title: ''
  type: Authentication
  url: authentication/zurelay-com-authentication.yml
- group: design
  href: https://artifacts.apis.io/zurelay-com/conformance/zurelay-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/zurelay-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/zurelay-com/llms/zurelay-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/zurelay-com-llms.txt
- group: agent
  href: https://artifacts.apis.io/zurelay-com/well-known/zurelay-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/zurelay-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/zurelay-com/hosts/zurelay-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/zurelay-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/zurelay-com/vendors/zurelay-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/zurelay-com-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://zurelay.com/legal/terms
- group: operate
  title: ''
  type: Support
  url: https://zurelay.com/support
- group: operate
  title: ''
  type: StatusPage
  url: https://zurelay.com/status
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://zurelay.com/legal/privacy
- group: start
  title: ''
  type: Login
  url: https://zurelay.com/login
- group: docs
  title: ''
  type: Documentation
  url: https://zurelay.com/docs
- group: start
  title: ''
  type: GettingStarted
  url: https://zurelay.com/docs/quickstart
- group: auth
  href: https://artifacts.apis.io/zurelay-com/security/zurelay-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/zurelay-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://zurelay.com/
coverage:
  checked: '2026-10-31'
  detail: No OpenAPI, AsyncAPI, GraphQL, gRPC, or WSDL contracts were found on the provider's documented API host.
  evidence:
  - status: 404
    url: https://api.zurelay.com/openapi.json
  - status: 404
    url: https://api.zurelay.com/openapi.yaml
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-31'
description: Zurelay provides a unified API that gives developers access to a wide range of AI models—including Claude, GPT, Gemini, Grok, DeepSeek, and many others—at significantly reduced costs, often up to 90% cheaper than the original providers. The platform offers OpenAI‑compatible endpoints, automatic failover, smart routing, and a single API key to manage usage across models, supporting text, image, video, and audio generation, as well as embeddings and decision tools. Zurelay aims to simplify AI integration while delivering cost savings and reliability for developers and enterprises.
image: https://zurelay.com/og.png
json_schemas:
- name: GetV1ImagesIdResponse
  property_count: 11
  slug: zurelay-com-get-v1-images-id-response
- name: PostV1AudioSpeechRequest
  property_count: 3
  slug: zurelay-com-post-v1-audio-speech-request
- name: PostV1ChatCompletionsRequest
  property_count: 14
  slug: zurelay-com-post-v1-chat-completions-request
- name: PostV1ChatCompletionsResponse
  property_count: 6
  slug: zurelay-com-post-v1-chat-completions-response
- name: PostV1MessagesCountTokensRequest
  property_count: 4
  slug: zurelay-com-post-v1-messages-count-tokens-request
- name: PostV1SystemoneRequest
  property_count: 3
  slug: zurelay-com-post-v1-systemone-request
jsonld:
- class_count: 10
  name: Zurelay Com Context
  property_count: 36
  slug: zurelay-com-context
layout: provider
modified: '2026-10-31'
name: zurelay-com
nav: Providers
network: true
overview: 'zurelay-com is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Artificial Intelligence, Cloud, Machine Learning, and Cost-Saving.


  The zurelay-com catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 1 Spectral governance ruleset.


  zurelay-com''s developer surface includes authentication, support, documentation, getting-started guide, and 16 more developer resources.'
random_paper: 16
rules:
- authorship: generated
  effective_rule_count: 52
  extends:
  - spectral:oas
  name: zurelay-com API Rules
  rule_count: 11
  severity_counts:
    error: 9
    hint: 0
    info: 1
    warn: 1
  slug: zurelay-com-rules
score:
  band: thin
  composite: 28.7
  coverage:
    artifact_dirs: 16
    catalog_earned: 62.8
    catalog_earned_first_party: 0.0
    catalog_gap: 52.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -7.7
  facets:
    access_clarity: 17.1
    contract_governance: 22.0
    contract_quality: 33.7
    developer_ergonomics: 25.0
    discoverability: 66.1
    operational_transparency: 15.8
  previous_composite: 36.4
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
    score: 19.1
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Zurelay Com Authentication
  slug: zurelay-com-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Zurelay Com Domain Security
  slug: zurelay-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: zurelay-com
tags:
- Company
- Artificial Intelligence
- Cloud
- Machine Learning
- Cost-Saving
website: https://zurelay.com/
---
