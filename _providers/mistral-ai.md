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
- acting_count: 13
  human_in_the_loop: 0
  name: Mistral Ai Agentic Access
  operation_count: 21
  slug: mistral-ai-agentic-access
  summary_line: 21 operations · 13 acting
api_count: 8
apis:
- description: Endpoints for interacting with Mistral AI agents that can handle complex tasks with tool use and multi-step reasoning.
  name: Mistral AI Agents API
  slug: mistral-ai-agents-api
- description: Endpoints for creating, listing, retrieving, and cancelling batch processing jobs for asynchronous request handling.
  name: Mistral AI Batch Jobs API
  slug: mistral-ai-batch-jobs-api
- description: Endpoints for generating chat completions using Mistral language models in a conversational format.
  name: Mistral AI Chat Completions API
  slug: mistral-ai-chat-completions-api
- description: Endpoints for generating vector embeddings from text inputs using Mistral embedding models.
  name: Mistral AI Embeddings API
  slug: mistral-ai-embeddings-api
- description: Endpoints for creating, managing, and monitoring fine-tuning jobs on Mistral AI models.
  name: Mistral AI Fine-Tuning Jobs API
  slug: mistral-ai-fine-tuning-jobs-api
- description: Endpoints for listing, retrieving, updating, and deleting models available on the Mistral AI platform.
  name: Mistral AI Models API
  slug: mistral-ai-models-api
- description: Endpoints for extracting text and structured content from documents and images using optical character recognition.
  name: Mistral AI OCR API
  slug: mistral-ai-ocr-api
- description: Endpoints for creating and managing training jobs including pre-training, supervised fine-tuning, and reinforcement learning pipelines.
  name: Mistral AI Training Jobs API
  slug: mistral-ai-training-jobs-api
artifact_total: 71
collections:
- collection_type: open
  name: Mistral AI Agents API
  slug: open-mistral-ai-agents
- collection_type: open
  name: Mistral AI Batch API
  slug: open-mistral-ai-batch
- collection_type: open
  name: Mistral AI Chat Completions API
  slug: open-mistral-ai-chat-completions
- collection_type: open
  name: Mistral AI Embeddings API
  slug: open-mistral-ai-embeddings
- collection_type: open
  name: Mistral AI Fine-Tuning API
  slug: open-mistral-ai-fine-tuning
- collection_type: open
  name: Mistral AI Forge API
  slug: open-mistral-ai-forge
- collection_type: open
  name: Mistral AI Models API
  slug: open-mistral-ai-models
- collection_type: open
  name: Mistral AI OCR API
  slug: open-mistral-ai-ocr
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/mistral-ai-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/mistral-ai-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/mistral-ai-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/mistralai
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/mistralai
- group: start
  title: ''
  type: Portal
  url: https://console.mistral.ai/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.mistral.ai/
- group: company
  title: ''
  type: Website
  url: https://mistral.ai/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://mistral.ai/terms/#privacy-policy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://mistral.ai/terms/#terms-of-use
- group: company
  title: ''
  type: Blog
  url: https://mistral.ai/news/
- group: start
  title: ''
  type: Login
  url: https://console.mistral.ai/
- group: design
  title: ''
  type: JSONLD
  url: json-ld/mistral-ai-context.jsonld
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/mistral-ai-chat-completion-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/mistral-ai-model-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/mistral-ai-fine-tuning-job-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/mistral-ai-batch-job-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/mistral-ai-ocr-response-schema.json
- group: agent
  title: ''
  type: LlmsText
  url: https://docs.mistral.ai/llms.txt
created: '2025-03-07'
description: Mistral AI is a French artificial intelligence company that develops and provides frontier large language models and APIs for developers and enterprises. Their developer platform offers APIs for chat completions, embeddings, fine-tuning, OCR, batch processing, and agentic workflows, enabling teams to build sophisticated AI-powered applications.
finops:
- name: Mistral Ai Finops
  service_category: AI Infrastructure
  slug: mistral-ai-finops
graphqls:
- description: This directory contains a conceptual GraphQL schema for the Mistral AI API, derived from the official REST API documented at [https://docs.mistral.ai/api/](https://docs.mistral.ai/api/). Mistral AI do
  name: Mistral AI GraphQL Schema
  slug: mistral-ai-graphql
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/mistral-ai.png
json_schemas:
- name: AgentCompletionChoice
  property_count: 3
  slug: mistral-ai-agentcompletionchoice
- name: AgentCompletionRequest
  property_count: 8
  slug: mistral-ai-agentcompletionrequest
- name: AgentCompletionResponse
  property_count: 6
  slug: mistral-ai-agentcompletionresponse
- name: Mistral AI Batch Job
  property_count: 16
  slug: mistral-ai-batch-job
- name: BatchJob
  property_count: 16
  slug: mistral-ai-batchjob
- name: BatchJobList
  property_count: 2
  slug: mistral-ai-batchjoblist
- name: Mistral AI Chat Completion
  property_count: 6
  slug: mistral-ai-chat-completion
- name: ChatCompletionChoice
  property_count: 3
  slug: mistral-ai-chatcompletionchoice
- name: ChatCompletionRequest
  property_count: 14
  slug: mistral-ai-chatcompletionrequest
- name: ChatCompletionResponse
  property_count: 6
  slug: mistral-ai-chatcompletionresponse
- name: ChatMessage
  property_count: 4
  slug: mistral-ai-chatmessage
- name: CreateBatchJobRequest
  property_count: 6
  slug: mistral-ai-createbatchjobrequest
- name: CreateFineTuningJobRequest
  property_count: 7
  slug: mistral-ai-createfinetuningjobrequest
- name: CreateTrainingJobRequest
  property_count: 5
  slug: mistral-ai-createtrainingjobrequest
- name: DeleteModelResponse
  property_count: 3
  slug: mistral-ai-deletemodelresponse
- name: DocumentInput
  property_count: 4
  slug: mistral-ai-documentinput
- name: EmbeddingObject
  property_count: 3
  slug: mistral-ai-embeddingobject
- name: EmbeddingRequest
  property_count: 3
  slug: mistral-ai-embeddingrequest
- name: EmbeddingResponse
  property_count: 5
  slug: mistral-ai-embeddingresponse
- name: Error
  property_count: 3
  slug: mistral-ai-error
- name: ExtractedImage
  property_count: 3
  slug: mistral-ai-extractedimage
- name: Mistral AI Fine-Tuning Job
  property_count: 13
  slug: mistral-ai-fine-tuning-job
- name: FineTuningJob
  property_count: 12
  slug: mistral-ai-finetuningjob
- name: FineTuningJobList
  property_count: 2
  slug: mistral-ai-finetuningjoblist
- name: ForgeHyperparameters
  property_count: 5
  slug: mistral-ai-forgehyperparameters
- name: FunctionDefinition
  property_count: 3
  slug: mistral-ai-functiondefinition
- name: Hyperparameters
  property_count: 4
  slug: mistral-ai-hyperparameters
- name: Integration
  property_count: 4
  slug: mistral-ai-integration
- name: Mistral AI Model
  property_count: 11
  slug: mistral-ai-model
- name: ModelCapabilities
  property_count: 5
  slug: mistral-ai-modelcapabilities
- name: ModelConfig
  property_count: 4
  slug: mistral-ai-modelconfig
- name: ModelList
  property_count: 2
  slug: mistral-ai-modellist
- name: Mistral AI OCR Response
  property_count: 3
  slug: mistral-ai-ocr-response
- name: OcrPage
  property_count: 4
  slug: mistral-ai-ocrpage
- name: OcrRequest
  property_count: 6
  slug: mistral-ai-ocrrequest
- name: OcrResponse
  property_count: 3
  slug: mistral-ai-ocrresponse
- name: OcrUsage
  property_count: 2
  slug: mistral-ai-ocrusage
- name: PageDimensions
  property_count: 2
  slug: mistral-ai-pagedimensions
- name: Tool
  property_count: 2
  slug: mistral-ai-tool
- name: ToolCall
  property_count: 3
  slug: mistral-ai-toolcall
- name: TrainingFile
  property_count: 2
  slug: mistral-ai-trainingfile
- name: TrainingJob
  property_count: 8
  slug: mistral-ai-trainingjob
- name: TrainingJobList
  property_count: 2
  slug: mistral-ai-trainingjoblist
- name: UpdateModelRequest
  property_count: 2
  slug: mistral-ai-updatemodelrequest
- name: Usage
  property_count: 3
  slug: mistral-ai-usage
json_structures:
- name: Mistral Ai Structure
  property_count: 0
  slug: mistral-ai-structure
jsonld:
- class_count: 0
  name: Mistral Ai Context
  property_count: 8
  slug: mistral-ai-context
layout: provider
modified: '2026-05-19'
name: Mistral AI
nav: Providers
network: true
overview: 'Mistral AI publishes 8 APIs on the [APIs.io](https://apis.io/) network, including Agents API, Batch Jobs API, Chat Completions API, and 5 more. Tagged areas include Agents, Artificial Intelligence, Batch Processing, Chat, and Embeddings.


  The Mistral AI catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Mistral AI''s developer surface includes authentication, developer portal, documentation, engineering blog, and 15 more developer resources.'
plans:
- name: Mistral Ai Plans Pricing
  plan_count: 6
  slug: mistral-ai-plans-pricing
random_paper: 59
rate_limits:
- limit_count: 3
  name: Mistral Ai Rate Limits
  slug: mistral-ai-rate-limits
rules:
- name: Mistral AI API Rules
  rule_count: 6
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 5
  slug: mistral-ai-jsonschema-spectral-rules
score:
  band: strong
  composite: 61.1
  delta: 3.2
  facets:
    commercial_clarity: 73.7
    contract_quality: 66.8
    developer_ergonomics: 30.4
    discoverability: 100.0
    governance: 73.7
    operational_transparency: 36.8
  previous_composite: 57.9
  schema_version: 0.5
  scored_at: '2026-07-27'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/mistral-ai/refs/heads/main/screenshots/mistral-ai-2026-06-20T185616.png
security:
- kind: authentication
  name: Mistral Ai Authentication
  slug: mistral-ai-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Mistral Ai Domain Security
  slug: mistral-ai-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: mistral-ai
tags:
- Agents
- Artificial Intelligence
- Batch Processing
- Chat
- Embeddings
- Fine-Tuning
- Large Language Models
- OCR
website: https://mistral.ai/
---
