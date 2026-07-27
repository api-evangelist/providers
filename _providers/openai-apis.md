---
access_model:
  confidence: high
  label: Paid · Self-serve signup
  onboarding: self-serve
  pricing: paid
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_skills: false
    agentic_access: true
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: true
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.1
  score: 48.1
  scored_at: '2026-07-27'
agentic_access:
- acting_count: 21
  human_in_the_loop: 0
  name: Openai Apis Agentic Access
  operation_count: 28
  slug: openai-apis-agentic-access
  summary_line: 28 operations · 21 acting
api_count: 12
apis:
- description: Manage AI assistants
  name: OpenAI APIs Assistants API
  slug: openai-apis-assistants-api
- description: Chat completion operations
  name: OpenAI APIs Chat API
  slug: openai-apis-chat-api
- description: Legacy text completion operations
  name: OpenAI APIs Completions API
  slug: openai-apis-completions-api
- description: Text embedding operations
  name: OpenAI APIs Embeddings API
  slug: openai-apis-embeddings-api
- description: Image generation, editing, and variation operations
  name: OpenAI APIs Images API
  slug: openai-apis-images-api
- description: Manage messages within threads
  name: OpenAI APIs Messages API
  slug: openai-apis-messages-api
- description: Content moderation operations
  name: OpenAI APIs Moderations API
  slug: openai-apis-moderations-api
- description: Execute assistants on threads
  name: OpenAI APIs Runs API
  slug: openai-apis-runs-api
- description: Text-to-speech operations
  name: OpenAI APIs Speech API
  slug: openai-apis-speech-api
- description: Manage conversation threads
  name: OpenAI APIs Threads API
  slug: openai-apis-threads-api
- description: Speech-to-text transcription operations
  name: OpenAI APIs Transcription API
  slug: openai-apis-transcription-api
- description: Audio translation operations
  name: OpenAI APIs Translation API
  slug: openai-apis-translation-api
artifact_total: 68
collections:
- collection_type: open
  name: OpenAI APIs OpenAI Assistants API
  slug: open-openai-assistants
- collection_type: open
  name: OpenAI APIs OpenAI Audio API
  slug: open-openai-audio
- collection_type: open
  name: OpenAI APIs OpenAI Chat Completions API
  slug: open-openai-chat-completions
- collection_type: open
  name: OpenAI APIs OpenAI Completions API
  slug: open-openai-completions
- collection_type: open
  name: OpenAI APIs OpenAI Embeddings API
  slug: open-openai-embeddings
- collection_type: open
  name: OpenAI APIs OpenAI Images API
  slug: open-openai-images
- collection_type: open
  name: OpenAI APIs OpenAI Moderations API
  slug: open-openai-moderations
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/openai-apis-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/openai-apis-trust-center.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/openai-apis-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/openai-apis-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/openai-apis-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/openai
- group: auth
  title: ''
  type: Authentication
  url: https://platform.openai.com/docs/api-reference/authentication
- group: commercial
  title: ''
  type: Pricing
  url: https://openai.com/api/pricing/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://openai.com/policies/terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://openai.com/policies/privacy-policy
- group: operate
  title: ''
  type: StatusPage
  url: https://status.openai.com/
- group: company
  title: ''
  type: Blog
  url: https://openai.com/news/rss.xml
created: '2024-01-01'
description: Collection of OpenAI's artificial intelligence APIs for natural language processing, image generation, speech, and embeddings including Chat Completions, Completions, Images, Audio, Embeddings, Moderations, and Assistants APIs.
finops:
- name: Openai Apis Finops
  service_category: AI Infrastructure
  slug: openai-apis-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/openai-apis.png
json_schemas:
- name: Assistant
  property_count: 12
  slug: openai-apis-assistant
- name: ChatCompletionResponse
  property_count: 7
  slug: openai-apis-chatcompletionresponse
- name: ChatMessage
  property_count: 5
  slug: openai-apis-chatmessage
- name: CompletionResponse
  property_count: 7
  slug: openai-apis-completionresponse
- name: CreateAssistantRequest
  property_count: 9
  slug: openai-apis-createassistantrequest
- name: CreateChatCompletionRequest
  property_count: 17
  slug: openai-apis-createchatcompletionrequest
- name: CreateCompletionRequest
  property_count: 16
  slug: openai-apis-createcompletionrequest
- name: CreateEmbeddingRequest
  property_count: 5
  slug: openai-apis-createembeddingrequest
- name: CreateImageEditRequest
  property_count: 8
  slug: openai-apis-createimageeditrequest
- name: CreateImageRequest
  property_count: 8
  slug: openai-apis-createimagerequest
- name: CreateImageVariationRequest
  property_count: 6
  slug: openai-apis-createimagevariationrequest
- name: CreateMessageRequest
  property_count: 3
  slug: openai-apis-createmessagerequest
- name: CreateModerationRequest
  property_count: 2
  slug: openai-apis-createmoderationrequest
- name: CreateRunRequest
  property_count: 7
  slug: openai-apis-createrunrequest
- name: CreateSpeechRequest
  property_count: 5
  slug: openai-apis-createspeechrequest
- name: CreateThreadRequest
  property_count: 2
  slug: openai-apis-createthreadrequest
- name: CreateTranscriptionRequest
  property_count: 7
  slug: openai-apis-createtranscriptionrequest
- name: CreateTranslationRequest
  property_count: 5
  slug: openai-apis-createtranslationrequest
- name: DeleteResponse
  property_count: 3
  slug: openai-apis-deleteresponse
- name: Embedding
  property_count: 3
  slug: openai-apis-embedding
- name: EmbeddingResponse
  property_count: 4
  slug: openai-apis-embeddingresponse
- name: ImageResponse
  property_count: 2
  slug: openai-apis-imageresponse
- name: ListResponse
  property_count: 5
  slug: openai-apis-listresponse
- name: Message
  property_count: 9
  slug: openai-apis-message
- name: ModerationResponse
  property_count: 3
  slug: openai-apis-moderationresponse
- name: ModerationResult
  property_count: 3
  slug: openai-apis-moderationresult
- name: ModifyAssistantRequest
  property_count: 9
  slug: openai-apis-modifyassistantrequest
- name: Run
  property_count: 17
  slug: openai-apis-run
- name: Thread
  property_count: 4
  slug: openai-apis-thread
- name: Tool
  property_count: 2
  slug: openai-apis-tool
- name: ToolCall
  property_count: 3
  slug: openai-apis-toolcall
- name: TranscriptionResponse
  property_count: 6
  slug: openai-apis-transcriptionresponse
- name: TranslationResponse
  property_count: 1
  slug: openai-apis-translationresponse
- name: Usage
  property_count: 3
  slug: openai-apis-usage
- name: OpenAI Assistant
  property_count: 12
  slug: openai-assistant
- name: OpenAI Chat Completion
  property_count: 7
  slug: openai-chat-completion
- name: OpenAI Embedding
  property_count: 3
  slug: openai-embedding
- name: OpenAI Moderation Result
  property_count: 3
  slug: openai-moderation
json_structures:
- name: Openai Apis Structure
  property_count: 0
  slug: openai-apis-structure
jsonld:
- class_count: 0
  name: Openai Context
  property_count: 13
  slug: openai-context
layout: provider
modified: '2026-05-19'
name: OpenAI APIs
nav: Providers
network: true
overview: 'OpenAI APIs publishes 12 APIs on the [APIs.io](https://apis.io/) network, including Assistants API, Chat API, Completions API, and 9 more. Tagged areas include Artificial Intelligence, Embeddings, Image Generation, Language Models, and Speech.


  The OpenAI APIs catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  OpenAI APIs'' developer surface includes authentication, pricing, engineering blog, and 9 more developer resources.'
plans:
- name: Openai Apis Plans Pricing
  plan_count: 6
  slug: openai-apis-plans-pricing
random_paper: 22
rate_limits:
- limit_count: 7
  name: Openai Apis Rate Limits
  slug: openai-apis-rate-limits
rules:
- name: OpenAI APIs API Rules
  rule_count: 6
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 5
  slug: openai-apis-jsonschema-spectral-rules
score:
  band: strong
  composite: 61.4
  delta: 3.3
  facets:
    commercial_clarity: 78.9
    contract_quality: 69.3
    developer_ergonomics: 13.0
    discoverability: 100.0
    governance: 73.7
    operational_transparency: 52.6
  previous_composite: 58.1
  schema_version: 0.5
  scored_at: '2026-07-27'
  trend: flat
security:
- kind: authentication
  name: Openai Apis Authentication
  slug: openai-apis-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Openai Apis Domain Security
  slug: openai-apis-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Openai Apis Vulnerability Disclosure
  slug: openai-apis-vulnerability-disclosure
  summary_line: Bugcrowd · security.txt · contact published
- kind: trust-center
  name: Openai Apis Trust Center
  slug: openai-apis-trust-center
  summary_line: SOC 2, ISO 27001, ISO 27017, ISO 27018, PCI DSS, FedRAMP, GDPR, CSA STAR
slug: openai-apis
tags:
- Artificial Intelligence
- Embeddings
- Image Generation
- Language Models
- Speech
---
