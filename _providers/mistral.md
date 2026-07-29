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
- acting_count: 19
  human_in_the_loop: 0
  name: Mistral Agentic Access
  operation_count: 29
  slug: mistral-agentic-access
  summary_line: 29 operations · 19 acting
api_count: 11
apis:
- description: Agent completion operations
  name: Mistral AI Agents API
  slug: mistral-agents-api
- description: Audio transcription operations
  name: Mistral AI Audio API
  slug: mistral-audio-api
- description: Batch inference job operations
  name: Mistral AI Batch Jobs API
  slug: mistral-batch-jobs-api
- description: Chat completion operations
  name: Mistral AI Chat API
  slug: mistral-chat-api
- description: Text embedding operations
  name: Mistral AI Embeddings API
  slug: mistral-embeddings-api
- description: File management operations
  name: Mistral AI Files API
  slug: mistral-files-api
- description: Fill-in-the-Middle code completion operations
  name: Mistral AI FIM API
  slug: mistral-fim-api
- description: Create and manage fine-tuning jobs
  name: Mistral AI Fine-Tuning Jobs API
  slug: mistral-fine-tuning-jobs-api
- description: Model management operations
  name: Mistral AI Models API
  slug: mistral-models-api
- description: Content moderation and classification operations
  name: Mistral AI Moderation API
  slug: mistral-moderation-api
- description: Document OCR and text extraction operations
  name: Mistral AI OCR API
  slug: mistral-ocr-api
artifact_total: 102
asyncapis:
- description: 'AsyncAPI definition for Mistral AI streaming completion endpoints. Mistral is OpenAI-compatible and delivers streamed completions as Server-Sent Events (SSE) over HTTP when `stream: true` is set on th'
  name: Mistral AI Streaming Completions API
  slug: mistral-asyncapi
collections:
- collection_type: open
  name: Mistral AI Agents API
  slug: open-mistral-agents
- collection_type: open
  name: Mistral AI Audio Transcription API
  slug: open-mistral-audio-transcription
- collection_type: open
  name: Mistral AI Batch API
  slug: open-mistral-batch
- collection_type: open
  name: Mistral AI Chat API
  slug: open-mistral-chat
- collection_type: open
  name: Mistral AI Mistral Embeddings API
  slug: open-mistral-embeddings
- collection_type: open
  name: Mistral AI Files API
  slug: open-mistral-files
- collection_type: open
  name: Mistral AI FIM API
  slug: open-mistral-fim
- collection_type: open
  name: Mistral AI Fine-Tuning API
  slug: open-mistral-fine-tuning
- collection_type: open
  name: Mistral AI Models API
  slug: open-mistral-models
- collection_type: open
  name: Mistral AI Mistral Moderation API
  slug: open-mistral-moderation
- collection_type: open
  name: Mistral AI OCR API
  slug: open-mistral-ocr
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/mistral-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/mistral-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/mistral-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://mistral.ai
- group: docs
  title: ''
  type: Documentation
  url: https://docs.mistral.ai
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.mistral.ai/getting-started/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://mistral.ai/terms/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://mistral.ai/privacy/
- group: commercial
  title: ''
  type: Pricing
  url: https://mistral.ai/technology/#pricing
- group: operate
  title: ''
  type: StatusPage
  url: https://status.mistral.ai
- group: build
  title: ''
  type: GitHub
  url: https://github.com/mistralai
- group: company
  title: ''
  type: Twitter
  url: https://twitter.com/MistralAI
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/mistralai
- group: operate
  title: ''
  type: Discord
  url: https://discord.gg/mistralai
- group: start
  title: ''
  type: Portal
  url: https://docs.mistral.ai/api
- group: company
  title: ''
  type: Blog
  url: https://mistral.ai/news
- group: operate
  title: ''
  type: ChangeLog
  url: https://docs.mistral.ai/getting-started/changelog
- group: start
  title: ''
  type: Signup
  url: https://console.mistral.ai
- group: commercial
  title: ''
  type: Pricing
  url: https://mistral.ai/pricing
- group: build
  title: ''
  type: SDKs
  url: https://docs.mistral.ai/getting-started/clients
- group: build
  title: ''
  type: PythonSDK
  url: https://github.com/mistralai/client-python
- group: build
  title: ''
  type: TypeScriptSDK
  url: https://github.com/mistralai/client-ts
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.mistral.ai/getting-started/quickstart
- group: design
  title: ''
  type: JSONLD
  url: json-ld/mistral-context.jsonld
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/mistral-chat-completion-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/mistral-model-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/mistral-fine-tuning-job-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/mistral-file-schema.json
- group: agent
  title: ''
  type: LlmsText
  url: https://docs.mistral.ai/llms.txt
created: '2024'
description: Mistral AI provides state-of-the-art large language models and AI APIs for developers and enterprises.
features:
- Mistral Large 2 at $2/$6 per MTok
- Mistral Medium 3 at $0.40/$2
- Mistral Small 3 at $0.10/$0.30
- Ministral 3B at $0.04/$0.04 (smallest commercial model)
- Mistral Nemo at $0.02/$0.04 (cheapest tier)
- Codestral at $0.30/$0.90 for code completion/FIM
- Pixtral Large for vision
- Mixtral 8x22B mixture-of-experts
- La Plateforme free tier with 1 RPS
- 'Paid tier: 10 RPS, 5M TPM'
- OpenAI-compatible Chat Completions
- Function calling and tool use
- JSON mode and guided generation
- Embed model for semantic search
- Available on AWS Bedrock, Azure AI, Vertex AI
- Fine-tuning service for select models
finops:
- name: Mistral Finops
  service_category: AI and Machine Learning
  slug: mistral-finops
graphqls:
- description: Conceptual GraphQL schema for the Mistral AI API. Mistral AI exposes a REST API (OpenAI-compatible) at `https://api.mistral.ai/v1`. This schema translates those REST resources into GraphQL types, quer
  name: Mistral AI GraphQL Schema
  slug: mistral-graphql
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/mistral.png
json_schemas:
- name: AgentCompletionRequest
  property_count: 8
  slug: mistral-agentcompletionrequest
- name: AgentCompletionResponse
  property_count: 6
  slug: mistral-agentcompletionresponse
- name: AgentCompletionStreamResponse
  property_count: 5
  slug: mistral-agentcompletionstreamresponse
- name: BatchJob
  property_count: 16
  slug: mistral-batchjob
- name: BatchJobList
  property_count: 3
  slug: mistral-batchjoblist
- name: Mistral Chat Completion
  property_count: 6
  slug: mistral-chat-completion
- name: ChatCompletionRequest
  property_count: 12
  slug: mistral-chatcompletionrequest
- name: ChatCompletionResponse
  property_count: 6
  slug: mistral-chatcompletionresponse
- name: ChatCompletionStreamResponse
  property_count: 5
  slug: mistral-chatcompletionstreamresponse
- name: ChatModerationRequest
  property_count: 2
  slug: mistral-chatmoderationrequest
- name: Choice
  property_count: 3
  slug: mistral-choice
- name: ContentPart
  property_count: 3
  slug: mistral-contentpart
- name: CreateBatchJobRequest
  property_count: 5
  slug: mistral-createbatchjobrequest
- name: CreateFineTuningJobRequest
  property_count: 7
  slug: mistral-createfinetuningjobrequest
- name: DeleteFileResponse
  property_count: 3
  slug: mistral-deletefileresponse
- name: DeleteModelResponse
  property_count: 3
  slug: mistral-deletemodelresponse
- name: DocumentInput
  property_count: 4
  slug: mistral-documentinput
- name: Embedding
  property_count: 3
  slug: mistral-embedding
- name: EmbeddingRequest
  property_count: 3
  slug: mistral-embeddingrequest
- name: EmbeddingResponse
  property_count: 5
  slug: mistral-embeddingresponse
- name: Error
  property_count: 4
  slug: mistral-error
- name: ExtractedImage
  property_count: 6
  slug: mistral-extractedimage
- name: Mistral File
  property_count: 8
  slug: mistral-file
- name: FileList
  property_count: 3
  slug: mistral-filelist
- name: FimCompletionRequest
  property_count: 10
  slug: mistral-fimcompletionrequest
- name: FimCompletionResponse
  property_count: 6
  slug: mistral-fimcompletionresponse
- name: FimCompletionStreamResponse
  property_count: 5
  slug: mistral-fimcompletionstreamresponse
- name: Mistral Fine-Tuning Job
  property_count: 13
  slug: mistral-fine-tuning-job
- name: FineTuningJob
  property_count: 12
  slug: mistral-finetuningjob
- name: FineTuningJobList
  property_count: 2
  slug: mistral-finetuningjoblist
- name: FunctionDefinition
  property_count: 3
  slug: mistral-functiondefinition
- name: Hyperparameters
  property_count: 6
  slug: mistral-hyperparameters
- name: Integration
  property_count: 4
  slug: mistral-integration
- name: Message
  property_count: 4
  slug: mistral-message
- name: Mistral Model
  property_count: 11
  slug: mistral-model
- name: ModelList
  property_count: 2
  slug: mistral-modellist
- name: ModerationRequest
  property_count: 2
  slug: mistral-moderationrequest
- name: ModerationResponse
  property_count: 3
  slug: mistral-moderationresponse
- name: ModerationResult
  property_count: 2
  slug: mistral-moderationresult
- name: OcrPage
  property_count: 4
  slug: mistral-ocrpage
- name: OcrRequest
  property_count: 6
  slug: mistral-ocrrequest
- name: OcrResponse
  property_count: 3
  slug: mistral-ocrresponse
- name: Segment
  property_count: 5
  slug: mistral-segment
- name: StreamChoice
  property_count: 3
  slug: mistral-streamchoice
- name: Tool
  property_count: 2
  slug: mistral-tool
- name: ToolCall
  property_count: 3
  slug: mistral-toolcall
- name: TrainingFile
  property_count: 2
  slug: mistral-trainingfile
- name: TranscriptionRequest
  property_count: 8
  slug: mistral-transcriptionrequest
- name: TranscriptionResponse
  property_count: 5
  slug: mistral-transcriptionresponse
- name: UpdateModelRequest
  property_count: 2
  slug: mistral-updatemodelrequest
- name: Usage
  property_count: 3
  slug: mistral-usage
- name: Word
  property_count: 4
  slug: mistral-word
json_structures:
- name: Mistral Structure
  property_count: 0
  slug: mistral-structure
jsonld:
- class_count: 0
  name: Mistral Context
  property_count: 11
  slug: mistral-context
layout: provider
modified: '2026-05-29'
name: Mistral AI
nav: Providers
network: true
overview: 'Mistral AI publishes 11 APIs on the [APIs.io](https://apis.io/) network, including Agents API, Audio API, Batch Jobs API, and 8 more.


  The Mistral AI catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 2 Spectral governance rulesets.


  Mistral AI''s developer surface includes authentication, documentation, getting-started guide, pricing, GitHub presence, developer portal, engineering blog, and 22 more developer resources.'
plans:
- name: Mistral Plans Pricing
  plan_count: 6
  slug: mistral-plans-pricing
random_paper: 71
rate_limits:
- limit_count: 4
  name: Mistral Rate Limits
  slug: mistral-rate-limits
rules:
- name: Mistral AI API Rules
  rule_count: 9
  severity_counts:
    error: 1
    hint: 0
    info: 0
    warn: 8
  slug: mistral-asyncapi-spectral-rules
- name: Mistral AI API Rules
  rule_count: 6
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 5
  slug: mistral-jsonschema-spectral-rules
score:
  band: strong
  composite: 64.4
  delta: -2.1
  facets:
    commercial_clarity: 71.1
    contract_quality: 81.8
    developer_ergonomics: 47.8
    discoverability: 63.0
    governance: 41.7
    operational_transparency: 68.4
  previous_composite: 66.5
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 11
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/mistral/refs/heads/main/screenshots/mistral-2026-06-20T185615.png
security:
- kind: authentication
  name: Mistral Authentication
  slug: mistral-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Mistral Domain Security
  slug: mistral-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: mistral
website: https://mistral.ai
---
