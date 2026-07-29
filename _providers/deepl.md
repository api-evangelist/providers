---
access_model:
  confidence: high
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: true
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    asyncapi_events: true
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 36.0
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 6
  human_in_the_loop: 0
  name: Deepl Agentic Access
  operation_count: 15
  slug: deepl-agentic-access
  summary_line: 15 operations · 6 acting
api_count: 7
apis:
- description: The DeepL Voice API provides real-time speech transcription and translation. A POST to /v3/voice/realtime issues an ephemeral token and WebSocket streaming URL; clients then open a WSS channel to stre
  name: DeepL Voice API
  slug: deepl-voice-api
- description: The Documents API from DeepL — 3 operation(s) for documents.
  name: DeepL Documents API
  slug: deepl-documents-api
- description: The Glossaries API from DeepL — 4 operation(s) for glossaries.
  name: DeepL Glossaries API
  slug: deepl-glossaries-api
- description: The Languages API from DeepL — 1 operation(s) for languages.
  name: DeepL Languages API
  slug: deepl-languages-api
- description: The Translate API from DeepL — 1 operation(s) for translate.
  name: DeepL Translate API
  slug: deepl-translate-api
- description: The Usage API from DeepL — 1 operation(s) for usage.
  name: DeepL Usage API
  slug: deepl-usage-api
- description: The Write API from DeepL — 1 operation(s) for write.
  name: DeepL Write API
  slug: deepl-write-api
artifact_total: 31
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
  name: DeepL Translation API
  slug: open-deepl-translation-api
- collection_type: open
  name: DeepL Voice API
  slug: open-deepl-voice-api
common:
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/deepl/overview
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/deepl-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/deepl-trust-center.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/deepl-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/deepl-domain-security.yml
- group: auth
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
  title: ''
  type: JSONLD
  url: json-ld/deepl-context.jsonld
- group: design
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
- name: Deepl Finops
  service_category: API
  slug: deepl-finops
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
modified: '2026-05-30'
name: DeepL
nav: Providers
network: true
overview: 'DeepL publishes 7 APIs on the [APIs.io](https://apis.io/) network, including Voice API, Documents API, Glossaries API, and 4 more. Tagged areas include Artificial Intelligence, Deep Learning, Glossaries, Localization, and Machine Learning.


  The DeepL catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 3 Spectral governance rulesets.


  DeepL''s developer surface includes authentication, developer portal, documentation, pricing, engineering blog, and 15 more developer resources.'
plans:
- name: Deepl Plans Pricing
  plan_count: 3
  slug: deepl-plans-pricing
random_paper: 36
rate_limits:
- limit_count: 5
  name: Deepl Rate Limits
  slug: deepl-rate-limits
rules:
- name: DeepL API Rules
  rule_count: 5
  severity_counts:
    error: 1
    hint: 0
    info: 0
    warn: 4
  slug: deepl-asyncapi-spectral-rules
- name: DeepL API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: deepl-jsonschema-spectral-rules
- name: DeepL API Rules
  rule_count: 5
  severity_counts:
    error: 2
    hint: 0
    info: 0
    warn: 3
  slug: deepl-translation-api-rules
score:
  band: strong
  composite: 60.9
  delta: -3.1
  facets:
    commercial_clarity: 78.9
    contract_quality: 76.3
    developer_ergonomics: 41.3
    discoverability: 74.1
    governance: 52.1
    operational_transparency: 31.6
  previous_composite: 64.0
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 7
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/deepl/refs/heads/main/screenshots/deepl-2026-06-20T175808.png
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
- Glossaries
- Localization
- Machine Learning
- Machine Translation
- Translation
website: https://www.deepl.com/
---
