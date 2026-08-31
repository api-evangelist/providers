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
  band: agent-aware
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
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 19.8
  scored_at: '2026-08-30'
agentic_access:
- acting_count: 6
  human_in_the_loop: 0
  name: Cometapi Agentic Access
  operation_count: 7
  slug: cometapi-agentic-access
  summary_line: 7 operations · 6 acting
api_count: 1
apis:
- description: Speech synthesis, transcription, and translation.
  name: CometAPI Audio API
  slug: cometapi-audio-api
- description: Chat completions across LLM providers.
  name: CometAPI Chat API
  slug: cometapi-chat-api
- description: Vector embeddings for retrieval and similarity.
  name: CometAPI Embeddings API
  slug: cometapi-embeddings-api
- description: Text-to-image and image-to-image generation.
  name: CometAPI Images API
  slug: cometapi-images-api
- description: List of supported models routable by CometAPI.
  name: CometAPI Models API
  slug: cometapi-models-api
- description: Text-to-video, image-to-video, and video extension.
  name: CometAPI Video API
  slug: cometapi-video-api
artifact_total: 25
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: CometAPI Unified Audio API
  slug: open-cometapi-audio-api
- collection_type: open
  name: CometAPI Unified Audio Chat API
  slug: open-cometapi-chat-api
- collection_type: open
  name: CometAPI Unified Audio Embeddings API
  slug: open-cometapi-embeddings-api
- collection_type: open
  name: CometAPI Unified Audio Images API
  slug: open-cometapi-images-api
- collection_type: open
  name: CometAPI Unified Audio Models API
  slug: open-cometapi-models-api
- collection_type: open
  name: CometAPI Unified API
  slug: open-cometapi-unified-api
- collection_type: open
  name: CometAPI Unified Audio Video API
  slug: open-cometapi-video-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/cometapi-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/cometapi-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/cometapi-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/cometapi-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/CometAPI-dev
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/cometapi
- group: company
  title: ''
  type: Website
  url: https://www.cometapi.com/
- group: docs
  title: ''
  type: Documentation
  url: https://apidoc.cometapi.com/
- group: operate
  title: ''
  type: HelpCenter
  url: https://apidoc.cometapi.com/help-center
- group: start
  title: ''
  type: GettingStarted
  url: https://apidoc.cometapi.com/how-to-use-cometapi-1792005m0
- group: design
  title: ''
  type: JSONLD
  url: json-ld/cometapi-context.jsonld
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/cometapi-chat-completion-schema.json
- group: design
  title: ''
  type: Spectral
  url: rules/cometapi-rules.yml
- group: agent
  title: ''
  type: LlmsText
  url: https://www.cometapi.com/llms.txt
- group: company
  title: ''
  type: Blog
  url: https://www.cometapi.com/blog
created: '2026-03-16'
description: CometAPI is an AI API aggregator that consolidates access to 500+ models from multiple providers (OpenAI, Anthropic, Google, xAI, DeepSeek, Alibaba, and more) behind a single OpenAI-compatible REST surface. It supports chat completions, embeddings, image generation, text-to-video and image-to-video, speech synthesis, and audio transcription. CometAPI positions itself as a drop-in replacement for the OpenAI SDK (changing only the base URL and key), with pay-as-you-go pricing reportedly 20-40% cheaper than direct vendor rates, sub-400ms median latency, and 99.9% service availability.
finops:
- name: Cometapi Finops
  service_category: API
  slug: cometapi-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/cometapi.png
json_schemas:
- name: CometAPI Chat Completion Response
  property_count: 6
  slug: cometapi-chat-completion
jsonld:
- class_count: 0
  name: Cometapi Context
  property_count: 4
  slug: cometapi-context
layout: provider
modified: '2026-05-19'
name: CometAPI
nav: Providers
network: true
overview: 'CometAPI publishes 6 APIs on the [APIs.io](https://apis.io/) network, including Audio API, Chat API, Embeddings API, and 3 more. Tagged areas include Artificial Intelligence, Aggregator, Audio, Chat, and Embeddings.


  The CometAPI catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  CometAPI''s developer surface includes authentication, documentation, getting-started guide, engineering blog, and 11 more developer resources.'
plans:
- name: Cometapi Plans Pricing
  plan_count: 3
  slug: cometapi-plans-pricing
random_paper: 10
rate_limits:
- limit_count: 5
  name: Cometapi Rate Limits
  slug: cometapi-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: CometAPI API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: cometapi-jsonschema-spectral-rules
- effective_rule_count: 50
  extends:
  - spectral:oas
  name: CometAPI API Rules
  rule_count: 9
  severity_counts:
    error: 4
    hint: 0
    info: 2
    warn: 3
  slug: cometapi-rules
score:
  band: thin
  composite: 34.7
  coverage:
    artifact_dirs: 14
    catalog_gap: 59.5
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: -0.5
  facets:
    access_clarity: 23.7
    commercial_clarity: 23.7
    contract_governance: 13.6
    contract_quality: 58.3
    developer_ergonomics: 23.8
    discoverability: 75.9
    governance: 13.6
    operational_transparency: 10.5
  previous_composite: 35.2
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 6
  schema_version: 0.17.2
  scored_at: '2026-08-30'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/cometapi/refs/heads/main/screenshots/cometapi-2026-06-20T174808.png
security:
- kind: authentication
  name: Cometapi Authentication
  slug: cometapi-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Cometapi Domain Security
  slug: cometapi-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: trust-center
  name: Cometapi Trust Center
  slug: cometapi-trust-center
  summary_line: trust center published
slug: cometapi
tags:
- Artificial Intelligence
- Aggregator
- Audio
- Chat
- Embeddings
- Generative AI
- Image
- LLM
- Multi-Model
- OpenAI-Compatible
- Video
website: https://www.cometapi.com/
---
