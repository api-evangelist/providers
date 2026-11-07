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
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: derived
    idempotency: false
    mcp_server: platform
    mcp_tool_quality: na
    openapi_examples: verified
    operation_distinctiveness: distinct
    pagination_ratio: false
    protected_resource_metadata: false
    rate_limit_signal: verified
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 36.4
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 6
  human_in_the_loop: 0
  name: Deepl Agentic Access
  operation_count: 15
  slug: deepl-agentic-access
  summary_line: 15 operations · 6 acting
api_count: 1
apis:
- baseURL: https://api.deepl.com/v3
  baseurl_source: declared
  description: The DeepL Voice API provides real-time speech transcription and translation. A POST to /v3/voice/realtime issues an ephemeral token and WebSocket streaming URL; clients then open a WSS channel to stre
  name: DeepL Voice API
  slug: deepl-voice-api
- baseURL: https://api.deepl.com/v3
  baseurl_source: declared
  description: Endpoints for organization administrators to manage API keys and retrieve usage analytics.
  name: DeepL Admin API
  slug: deepl-adminapi-api
- baseURL: https://api.deepl.com/v3
  baseurl_source: declared
  description: The `correct` endpoint fixes spelling and grammar errors without broader rephrasing. Use it when you want a minimal-change correction pass rather than the broader rewriting performed by `rephrase`.
  name: DeepL Correct Text API
  slug: deepl-correcttext-api
- baseURL: https://api.deepl.com/v3
  baseurl_source: declared
  description: Please note that this is the spec for the (old) v2 glossary endpoint. We recommend users switch to the newer v3 glossary endpoints, which support editability and multilinguality. The *glossary* functi
  name: DeepL Manage Glossaries API
  slug: deepl-manageglossaries-api
- baseURL: https://api.deepl.com/v3
  baseurl_source: declared
  description: The *glossary* functions allow you to create, inspect, edit and delete glossaries. Glossaries created with the glossary function can be used in translate requests by specifying the `glossary_id` param
  name: DeepL Manage Multilingual Glossaries API
  slug: deepl-managemultilingualglossaries-api
- baseURL: https://api.deepl.com/v3
  baseurl_source: declared
  description: 'The *Spoken Terms* functions allow you to create, inspect, edit and delete Spoken Terms collections. Spoken Terms improve speech recognition in the Voice API: they ensure specific words and phrases, s'
  name: DeepL Manage Spoken Terms API
  slug: deepl-managespokenterms-api
- baseURL: https://api.deepl.com/v3
  baseurl_source: declared
  description: Information about API usage and value ranges
  name: DeepL Meta Information API
  slug: deepl-metainformation-api
- baseURL: https://api.deepl.com/v3
  baseurl_source: declared
  description: '**Beta.** Retrieve a quality evaluation report for a document DeepL has translated. Reports are requested with `enable_quality_evaluation` on `POST /v2/document` and polled here. A report lists per-se'
  name: DeepL Quality Evaluation API
  slug: deepl-qualityevaluation-api
- baseURL: https://api.deepl.com/v3
  baseurl_source: declared
  description: The `rephrase` endpoint is used to make corrections and adjustments to texts based on style or tone.
  name: DeepL Rephrase Text API
  slug: deepl-rephrasetext-api
- baseURL: https://api.deepl.com/v3
  baseurl_source: declared
  description: The Style Rules API from DeepL — 5 operation(s) for style rules.
  name: DeepL Style Rules API
  slug: deepl-style-rules-api
- baseURL: https://api.deepl.com/v3
  baseurl_source: declared
  description: 'The document translation API allows you to translate whole documents and supports the following file types and extensions: * `docx` - Microsoft Word Document * `pptx` - Microsoft PowerPoint Document *'
  name: DeepL Translate Documents API
  slug: deepl-translatedocuments-api
- baseURL: https://api.deepl.com/v3
  baseurl_source: declared
  description: The text-translation API currently consists of a single endpoint, `translate`, which is described below.
  name: DeepL Translate Text API
  slug: deepl-translatetext-api
- baseURL: https://api.deepl.com/v3
  baseurl_source: declared
  description: 'The translation memory endpoints allow you to manage your account''s translation memories, used to store and reuse previously created translations. You can list and retrieve translation memories, page '
  name: DeepL Translation Memories API
  slug: deepl-translationmemories-api
- baseURL: https://api.deepl.com/v3
  baseurl_source: declared
  description: 'The Voice API provides real-time voice transcription and translation services. Use a two-step flow: first request a streaming URL via REST, then establish a WebSocket connection for streaming audio an'
  name: DeepL Voice API
  slug: deepl-voiceapi-api
- baseURL: https://api.deepl.com/v3
  baseurl_source: declared
  description: '**Alpha.** Async voice translation jobs. This API may change without notice.'
  name: DeepL Voice Translate Job API
  slug: deepl-voicetranslatejob-api
artifact_total: 47
asyncapis:
- description: WebSocket streaming API for real-time voice transcription and translation. After obtaining a streaming URL and token via the REST API (POST /v3/voice/realtime), establish a WebSocket connection to str
  name: DeepL Voice API - WebSocket Streaming
  slug: deepl-voice-api-asyncapi
collections:
- collection_type: postman
  name: DeepL Translation Documents API
  slug: postman-deepl-documents-api
- collection_type: postman
  name: DeepL Translation Documents Glossaries API
  slug: postman-deepl-glossaries-api
- collection_type: postman
  name: DeepL Translation Documents Languages API
  slug: postman-deepl-languages-api
- collection_type: postman
  name: DeepL Translation Documents Translate API
  slug: postman-deepl-translate-api
- collection_type: postman
  name: DeepL Translation Documents Usage API
  slug: postman-deepl-usage-api
- collection_type: postman
  name: DeepL Translation Documents Voice API
  slug: postman-deepl-voice-api
- collection_type: postman
  name: DeepL Translation Documents Write API
  slug: postman-deepl-write-api
- collection_type: open
  name: DeepL Translation Documents API
  slug: open-deepl-documents-api
- collection_type: open
  name: DeepL Translation Documents Glossaries API
  slug: open-deepl-glossaries-api
- collection_type: open
  name: DeepL Translation Documents Languages API
  slug: open-deepl-languages-api
- collection_type: open
  name: DeepL Translation Documents Translate API
  slug: open-deepl-translate-api
- collection_type: open
  name: DeepL Translation API
  slug: open-deepl-translation-api
- collection_type: open
  name: DeepL Translation Documents Usage API
  slug: open-deepl-usage-api
- collection_type: open
  name: DeepL Translation Documents Voice API
  slug: open-deepl-voice-api
- collection_type: open
  name: DeepL Translation Documents Write API
  slug: open-deepl-write-api
common:
- group: commercial
  href: https://artifacts.apis.io/deepl/plans/deepl-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/deepl-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/deepl/rate-limits/deepl-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/deepl-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/deepl/finops/deepl-finops.yml
  title: ''
  type: FinOps
  url: finops/deepl-finops.yml
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/deepl/overview
- group: agent
  href: https://artifacts.apis.io/deepl/agentic-access/deepl-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/deepl-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/deepl/security/deepl-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/deepl-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/deepl/security/deepl-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/deepl-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/deepl/security/deepl-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/deepl-domain-security.yml
- group: auth
  href: https://artifacts.apis.io/deepl/authentication/deepl-authentication.yml
  title: ''
  type: Authentication
  url: authentication/deepl-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/deepl
- group: company
  title: ''
  type: Website
  url: https://www.deepl.com/
- group: start
  title: ''
  type: Portal
  url: https://developers.deepl.com/
- group: docs
  title: ''
  type: Documentation
  url: https://developers.deepl.com/docs
- group: auth
  title: ''
  type: Authentication
  url: https://developers.deepl.com/docs/getting-started/auth
- group: commercial
  title: ''
  type: Pricing
  url: https://www.deepl.com/pro
- group: build
  title: ''
  type: SDKs
  url: https://github.com/DeepLcom/deepl-python
- group: build
  title: ''
  type: SDKs
  url: https://github.com/DeepLcom/deepl-node
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.deepl.com/pro-license
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.deepl.com/privacy
- group: design
  href: https://artifacts.apis.io/deepl/json-ld/deepl-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/deepl-context.jsonld
- group: design
  href: https://artifacts.apis.io/deepl/vocabulary/deepl-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/deepl-vocabulary.yml
- group: agent
  title: ''
  type: LlmsText
  url: https://developers.deepl.com/llms.txt
- group: company
  title: ''
  type: Blog
  url: https://www.deepl.com/en/blog/rss.xml
created: '2024-11-07'
description: DeepL is an AI-powered translation service that delivers high-quality machine translation between dozens of languages, with support for context-aware translation, document translation, glossaries, and rephrasing/improvement via DeepL Write. The DeepL API is offered in Pro and Free tiers and exposes endpoints for text translation, document translation, glossaries, language metadata, usage, and write/rephrase.
finops:
- has_sources: true
  method: derived
  name: Deepl Finops
  primary_unit: user/month
  service_category: ''
  slug: deepl-finops
  template: false
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/deepl.png
json_schemas:
- name: DeepL Glossary
  property_count: 7
  slug: deepl-glossary
- name: DeepL Translation
  property_count: 1
  slug: deepl-translation
jsonld:
- class_count: 3
  name: Deepl Context
  property_count: 9
  slug: deepl-context
layout: provider
mcp_servers:
- description: Remote MCP server at developers.deepl.com over HTTP; 3 tools listed.
  name: DeepL MCP Server
  slug: deepl
modified: '2026-05-30'
name: DeepL
nav: Providers
network: true
overview: 'DeepL publishes 15 API contracts indexed on the [APIs.io](https://apis.io/) network, including Voice API, Admin API, Correct Text API, and 12 more. Tagged areas include Artificial Intelligence, Deep Learning, Glossary, Localization, and Machine Learning.


  The DeepL catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 3 Spectral governance rulesets.


  DeepL''s developer surface includes authentication, developer portal, documentation, pricing, engineering blog, and 18 more developer resources.'
plans:
- name: Deepl Plans Pricing
  plan_count: 6
  slug: deepl-plans-pricing
- name: Deepl Price Estimates
  plan_count: 0
  slug: deepl-price-estimates
random_paper: 18
rate_limits:
- limit_count: 5
  name: Deepl Rate Limits
  slug: deepl-rate-limits
rules:
- authorship: generated
  effective_rule_count: 32
  extends:
  - spectral:asyncapi
  name: DeepL — asyncapi rules
  rule_count: 5
  severity_counts:
    error: 1
    hint: 0
    info: 0
    warn: 4
  slug: deepl-asyncapi-spectral-rules
- authorship: generated
  effective_rule_count: 5
  extends: []
  name: DeepL — jsonschema rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: deepl-jsonschema-spectral-rules
- authorship: unmarked
  effective_rule_count: 46
  extends:
  - spectral:oas
  name: DeepL — translation api rules
  rule_count: 5
  severity_counts:
    error: 2
    hint: 0
    info: 0
    warn: 3
  slug: deepl-translation-api-rules
score:
  band: strong
  composite: 60.8
  coverage:
    artifact_dirs: 22
    catalog_earned: 78.0
    catalog_earned_first_party: 12.0
    catalog_gap: 37.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 1.0
  facets:
    access_clarity: 78.9
    contract_governance: 27.3
    contract_quality: 76.0
    developer_ergonomics: 48.8
    discoverability: 75.0
    operational_transparency: 18.4
  previous_composite: 59.8
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 63.6
      total: 22
    mcp: first-party
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 32.7
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 11.1
screenshot: https://apis.io/screenshots/deepl/deepl-2026-06-20T175808.png
security:
- kind: authentication
  name: Deepl Authentication
  slug: deepl-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Deepl Domain Security
  slug: deepl-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Deepl Vulnerability Disclosure
  slug: deepl-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Deepl Trust Center
  slug: deepl-trust-center
  summary_line: SOC 2, ISO 27001, HIPAA, GDPR
slug: deepl
tags:
- Artificial Intelligence
- Deep Learning
- Glossary
- Localization
- Machine Learning
- Machine Translation
- Translation
- Real-Time
website: https://www.deepl.com/
---
