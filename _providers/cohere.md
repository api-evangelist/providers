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
    error_semantics: verified
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 43.2
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 11
  human_in_the_loop: 0
  name: Cohere Agentic Access
  operation_count: 18
  slug: cohere-agentic-access
  summary_line: 18 operations · 11 acting
api_count: 9
apis:
- description: 'The Cohere Chat API enables developers to integrate large language model text generation capabilities into their applications through a conversational interface. It supports multi-turn conversations, '
  name: Cohere Chat API
  slug: chat-api
- description: The Cohere Embed API generates vector embeddings from text and images, enabling semantic search, clustering, and classification use cases. It supports multilingual content and can process both text an
  name: Cohere Embed API
  slug: embed-api
- description: The Cohere Rerank API takes a query and a list of text documents and returns them ordered by relevance with assigned relevance scores. It is commonly used as a second-stage ranker in retrieval-augment
  name: Cohere Rerank API
  slug: rerank-api
- description: 'The Cohere Classify API performs text classification by assigning labels to input text based on provided examples. It can be used for sentiment analysis, content moderation, topic categorization, and '
  name: Cohere Classify API
  slug: classify-api
- description: The Cohere Embed Jobs API allows developers to create and manage batch embedding jobs for processing large volumes of text data asynchronously. Rather than embedding texts one at a time, developers ca
  name: Cohere Embed Jobs API
  slug: embed-jobs-api
- description: The Cohere Datasets API provides endpoints for uploading, managing, and retrieving datasets used with other Cohere services such as fine-tuning and embed jobs. Developers can create datasets from file
  name: Cohere Datasets API
  slug: datasets-api
- description: The Cohere Models API allows developers to list and retrieve information about available Cohere models, including the Command, Embed, and Rerank model families. It provides details such as model names
  name: Cohere Models API
  slug: models-api
- description: The Cohere Tokenize API splits input text into tokens using the tokenizer associated with a specified model. It returns both the token strings and their corresponding token IDs. This is useful for und
  name: Cohere Tokenize API
  slug: tokenize-api
- description: The Cohere Detokenize API converts a sequence of token IDs back into their corresponding text string using the tokenizer for a specified model. It is the inverse operation of the Tokenize API and is u
  name: Cohere Detokenize API
  slug: detokenize-api
artifact_total: 80
asyncapis:
- description: 'AsyncAPI definition for Cohere''s HTTP+SSE streaming endpoints. Cohere''s streaming responses are NOT delivered via WebSockets. They are delivered as Server-Sent Events (SSE) over plain HTTPS, returned '
  name: Cohere Streaming API
  slug: cohere-asyncapi
collections:
- collection_type: open
  name: Cohere Chat API
  slug: open-cohere-chat-api
- collection_type: open
  name: Cohere Classify API
  slug: open-cohere-classify-api
- collection_type: open
  name: Cohere Datasets API
  slug: open-cohere-datasets-api
- collection_type: open
  name: Cohere Detokenize API
  slug: open-cohere-detokenize-api
- collection_type: open
  name: Cohere Embed API
  slug: open-cohere-embed-api
- collection_type: open
  name: Cohere Embed Jobs API
  slug: open-cohere-embed-jobs-api
- collection_type: open
  name: Cohere Models API
  slug: open-cohere-models-api
- collection_type: open
  name: Cohere Rerank API
  slug: open-cohere-rerank-api
- collection_type: open
  name: Cohere Tokenize API
  slug: open-cohere-tokenize-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/cohere-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/cohere-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/cohere-authentication.yml
- group: company
  title: ''
  type: Blog
  url: https://cohere.com/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/cohere-ai
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/cohere-ai
- group: design
  title: ''
  type: JSONLD
  url: json-ld/cohere-context.jsonld
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/cohere-chat-message-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/cohere-embedding-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/cohere-model-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/cohere-dataset-schema.json
- group: agent
  title: ''
  type: LlmsText
  url: https://docs.cohere.com/llms.txt
description: Generates a text response to a user message and streams it down, token by token.
features:
- Command at $1/$2 per MTok input/output
- Command-light at $0.30/$0.60
- Command R at $0.50/$1.50
- Command R+ 08-2024 at $2.50/$10
- Command R+ 04-2024 at $3/$15
- Aya Expanse multilingual at $0.50/$1.50
- Embed v3 with English/multilingual
- Rerank for relevance scoring
- 'Production keys: 10K req/min Chat, 2K Embed, 10K Rerank'
- 'Trial keys: 20/min Chat, 100/min Embed'
- Connectors for RAG over data sources
- Tool use and function calling
- Compass for unstructured data search
- Available on AWS Bedrock, Azure, Oracle Cloud
- Fine-tuning for Command and Aya
- OpenAI-compatible Chat Completions endpoint
finops:
- name: Cohere Finops
  service_category: AI and Machine Learning
  slug: cohere-finops
graphqls:
- description: This document describes a conceptual GraphQL schema for the Cohere AI API, covering the full surface of Cohere's language model, embedding, reranking, classification, tokenization, dataset, connector,
  name: Cohere GraphQL Schema
  slug: cohere-graphql
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/cohere.png
json_schemas:
- name: Cohere Chat Message
  property_count: 5
  slug: cohere-chat-message
- name: ChatRequest
  property_count: 8
  slug: cohere-chatrequest
- name: ChatResponse
  property_count: 4
  slug: cohere-chatresponse
- name: Classification
  property_count: 7
  slug: cohere-classification
- name: ClassifyExample
  property_count: 2
  slug: cohere-classifyexample
- name: ClassifyRequest
  property_count: 5
  slug: cohere-classifyrequest
- name: ClassifyResponse
  property_count: 3
  slug: cohere-classifyresponse
- name: CreateDatasetRequest
  property_count: 6
  slug: cohere-createdatasetrequest
- name: CreateDatasetResponse
  property_count: 1
  slug: cohere-createdatasetresponse
- name: CreateEmbedJobRequest
  property_count: 6
  slug: cohere-createembedjobrequest
- name: CreateEmbedJobResponse
  property_count: 1
  slug: cohere-createembedjobresponse
- name: Cohere Dataset
  property_count: 11
  slug: cohere-dataset
- name: DatasetUsage
  property_count: 1
  slug: cohere-datasetusage
- name: DetokenizeRequest
  property_count: 2
  slug: cohere-detokenizerequest
- name: DetokenizeResponse
  property_count: 2
  slug: cohere-detokenizeresponse
- name: Cohere Embedding
  property_count: 4
  slug: cohere-embedding
- name: EmbedJob
  property_count: 9
  slug: cohere-embedjob
- name: EmbedRequest
  property_count: 6
  slug: cohere-embedrequest
- name: EmbedResponse
  property_count: 4
  slug: cohere-embedresponse
- name: Error
  property_count: 1
  slug: cohere-error
- name: ListDatasetsResponse
  property_count: 1
  slug: cohere-listdatasetsresponse
- name: ListEmbedJobsResponse
  property_count: 1
  slug: cohere-listembedjobsresponse
- name: ListModelsResponse
  property_count: 2
  slug: cohere-listmodelsresponse
- name: Message
  property_count: 4
  slug: cohere-message
- name: Cohere Model
  property_count: 6
  slug: cohere-model
- name: RerankRequest
  property_count: 5
  slug: cohere-rerankrequest
- name: RerankResponse
  property_count: 3
  slug: cohere-rerankresponse
- name: RerankResult
  property_count: 3
  slug: cohere-rerankresult
- name: StreamEvent
  property_count: 2
  slug: cohere-streamevent
- name: TokenizeRequest
  property_count: 2
  slug: cohere-tokenizerequest
- name: TokenizeResponse
  property_count: 3
  slug: cohere-tokenizeresponse
- name: Tool
  property_count: 2
  slug: cohere-tool
- name: ToolCall
  property_count: 3
  slug: cohere-toolcall
- name: Usage
  property_count: 2
  slug: cohere-usage
json_structures:
- name: Cohere Structure
  property_count: 0
  slug: cohere-structure
jsonld:
- class_count: 0
  name: Cohere Context
  property_count: 10
  slug: cohere-context
layout: provider
modified: '2026-05-29'
name: cohere
nav: Providers
network: true
overview: 'cohere publishes 9 APIs on the [APIs.io](https://apis.io/) network, including Chat API, Embed API, Rerank API, and 6 more.


  The cohere catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 2 Spectral governance rulesets.


  cohere''s developer surface includes authentication, engineering blog, and 10 more developer resources.'
plans:
- name: Cohere Plans Pricing
  plan_count: 6
  slug: cohere-plans-pricing
random_paper: 77
rate_limits:
- limit_count: 5
  name: Cohere Rate Limits
  slug: cohere-rate-limits
rules:
- name: cohere API Rules
  rule_count: 9
  severity_counts:
    error: 1
    hint: 0
    info: 0
    warn: 8
  slug: cohere-asyncapi-spectral-rules
- name: cohere API Rules
  rule_count: 6
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 5
  slug: cohere-jsonschema-spectral-rules
score:
  band: developing
  composite: 45.7
  delta: -2.8
  facets:
    commercial_clarity: 39.5
    contract_quality: 81.8
    developer_ergonomics: 13.0
    discoverability: 50.0
    governance: 41.7
    operational_transparency: 36.8
  previous_composite: 48.5
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 9
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/cohere/refs/heads/main/screenshots/cohere-2026-06-20T174719.png
security:
- kind: authentication
  name: Cohere Authentication
  slug: cohere-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Cohere Domain Security
  slug: cohere-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: cohere
---
