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
  band: agent-ready
  band_gated_from: agent-native
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
    mcp_server: verified
    mcp_tool_quality: full
    openapi_examples: partial
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: derived
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 41.4
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 11
  human_in_the_loop: 0
  name: Cohere Agentic Access
  operation_count: 18
  slug: cohere-agentic-access
  summary_line: 18 operations · 11 acting
api_count: 1
apis:
- baseURL: https://api.cohere.com
  baseurl_source: declared
  description: 'The Cohere Chat API enables developers to integrate large language model text generation capabilities into their applications through a conversational interface. It supports multi-turn conversations, '
  name: Cohere Chat API
  slug: chat-api
- baseURL: https://api.cohere.com
  baseurl_source: declared
  description: The Cohere Embed API generates vector embeddings from text and images, enabling semantic search, clustering, and classification use cases. It supports multilingual content and can process both text an
  name: Cohere Embed API
  slug: embed-api
- baseURL: https://api.cohere.com
  baseurl_source: declared
  description: The Cohere Rerank API takes a query and a list of text documents and returns them ordered by relevance with assigned relevance scores. It is commonly used as a second-stage ranker in retrieval-augment
  name: Cohere Rerank API
  slug: rerank-api
- baseURL: https://api.cohere.com
  baseurl_source: declared
  description: 'The Cohere Classify API performs text classification by assigning labels to input text based on provided examples. It can be used for sentiment analysis, content moderation, topic categorization, and '
  name: Cohere Classify API
  slug: classify-api
- baseURL: https://api.cohere.com
  baseurl_source: declared
  description: The Cohere Datasets API provides endpoints for uploading, managing, and retrieving datasets used with other Cohere services such as fine-tuning and embed jobs. Developers can create datasets from file
  name: Cohere Datasets API
  slug: datasets-api
- baseURL: https://api.cohere.com
  baseurl_source: declared
  description: The Cohere Models API allows developers to list and retrieve information about available Cohere models, including the Command, Embed, and Rerank model families. It provides details such as model names
  name: Cohere Models API
  slug: models-api
- baseURL: https://api.cohere.com
  baseurl_source: declared
  description: The Cohere Tokenize API splits input text into tokens using the tokenizer associated with a specified model. It returns both the token strings and their corresponding token IDs. This is useful for und
  name: Cohere Tokenize API
  slug: tokenize-api
- baseURL: https://api.cohere.com
  baseurl_source: declared
  description: The Cohere Detokenize API converts a sequence of token IDs back into their corresponding text string using the tokenizer for a specified model. It is the inverse operation of the Tokenize API and is u
  name: Cohere Detokenize API
  slug: detokenize-api
- baseURL: https://api.cohere.com
  baseurl_source: declared
  description: The batches API from Cohere — 3 operation(s) for batches.
  name: Cohere Batches API
  slug: cohere-batches-api
- baseURL: https://api.cohere.com
  baseurl_source: declared
  description: The Check Api Key API from Cohere — 1 operation(s) for check api key.
  name: Cohere Check Api Key API
  slug: cohere-check-api-key-api
- baseURL: https://api.cohere.com
  baseurl_source: declared
  description: The connectors API from Cohere — 3 operation(s) for connectors.
  name: Cohere Connectors API
  slug: cohere-connectors-api
- baseURL: https://api.cohere.com
  baseurl_source: declared
  description: The embedJobs API from Cohere — 3 operation(s) for embedjobs.
  name: Cohere Embed Jobs API
  slug: cohere-embedjobs-api
- baseURL: https://api.cohere.com
  baseurl_source: declared
  description: The /finetuning API from Cohere — 4 operation(s) for /finetuning.
  name: Cohere /finetuning API
  slug: cohere-finetuning-api
- baseURL: https://api.cohere.com
  baseurl_source: declared
  description: The Generate API from Cohere — 1 operation(s) for generate.
  name: Cohere Generate API
  slug: cohere-generate-api
- baseURL: https://api.cohere.com
  baseurl_source: declared
  description: The Parse API from Cohere — 1 operation(s) for parse.
  name: Cohere Parse API
  slug: cohere-parse-api
- baseURL: https://api.cohere.com
  baseurl_source: declared
  description: The Summarize API from Cohere — 1 operation(s) for summarize.
  name: Cohere Summarize API
  slug: cohere-summarize-api
- baseURL: https://api.cohere.com
  baseurl_source: declared
  description: The transcriptions API from Cohere — 1 operation(s) for transcriptions.
  name: Cohere Transcriptions API
  slug: cohere-transcriptions-api
artifact_total: 88
asyncapis:
- description: 'AsyncAPI definition for Cohere''s HTTP+SSE streaming endpoints. Cohere''s streaming responses are NOT delivered via WebSockets. They are delivered as Server-Sent Events (SSE) over plain HTTPS, returned '
  name: Cohere Streaming API
  slug: cohere-asyncapi
collections:
- collection_type: open
  name: Cohere Chat API
  slug: open-cohere-chat-api
- collection_type: open
  name: Cohere Chat Classify API
  slug: open-cohere-classify-api
- collection_type: open
  name: Cohere Chat Datasets API
  slug: open-cohere-datasets-api
- collection_type: open
  name: Cohere Chat Detokenize API
  slug: open-cohere-detokenize-api
- collection_type: open
  name: Cohere Chat Embed API
  slug: open-cohere-embed-api
- collection_type: open
  name: Cohere Chat Embed Jobs API
  slug: open-cohere-embed-jobs-api
- collection_type: open
  name: Cohere Chat Models API
  slug: open-cohere-models-api
- collection_type: open
  name: Cohere Chat Rerank API
  slug: open-cohere-rerank-api
- collection_type: open
  name: Cohere Chat Tokenize API
  slug: open-cohere-tokenize-api
common:
- group: other
  href: https://artifacts.apis.io/cohere/capabilities/cohere-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/cohere-capability-edges.yml
- group: operate
  href: https://artifacts.apis.io/cohere/rate-limits/cohere-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/cohere-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/cohere/finops/cohere-finops.yml
  title: ''
  type: FinOps
  url: finops/cohere-finops.yml
- group: commercial
  title: ''
  type: Pricing
  url: https://cohere.com/pricing
- group: commercial
  href: https://artifacts.apis.io/cohere/plans/cohere-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/cohere-plans-pricing.yml
- group: company
  title: ''
  type: Website
  url: https://www.cohere.com/
- group: agent
  href: https://artifacts.apis.io/cohere/agentic-access/cohere-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/cohere-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/cohere/security/cohere-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/cohere-domain-security.yml
- group: auth
  href: https://artifacts.apis.io/cohere/authentication/cohere-authentication.yml
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
  href: https://artifacts.apis.io/cohere/json-ld/cohere-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/cohere-context.jsonld
- group: docs
  href: https://artifacts.apis.io/cohere/json-schema/cohere-chat-message-schema.json
  title: ''
  type: JSONSchema
  url: json-schema/cohere-chat-message-schema.json
- group: docs
  href: https://artifacts.apis.io/cohere/json-schema/cohere-embedding-schema.json
  title: ''
  type: JSONSchema
  url: json-schema/cohere-embedding-schema.json
- group: docs
  href: https://artifacts.apis.io/cohere/json-schema/cohere-model-schema.json
  title: ''
  type: JSONSchema
  url: json-schema/cohere-model-schema.json
- group: docs
  href: https://artifacts.apis.io/cohere/json-schema/cohere-dataset-schema.json
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
- has_sources: true
  method: generated
  name: Cohere Finops
  primary_unit: ''
  service_category: AI and Machine Learning
  slug: cohere-finops
  template: false
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
mcp_servers:
- description: Remote MCP server at docs.cohere.com over HTTP.
  name: Cohere MCP Server
  slug: cohere
modified: '2026-09-16'
name: Cohere
nav: Providers
network: true
overview: 'Cohere publishes 17 API contracts indexed on the [APIs.io](https://apis.io/) network, including Chat API, Embed API, Rerank API, and 14 more. Tagged areas include Artificial Intelligence, Natural Language Processing, Embeddings, Vector Search, and LLM.


  The Cohere catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 2 Spectral governance rulesets.


  Cohere''s developer surface includes pricing, authentication, engineering blog, and 15 more developer resources.'
plans:
- name: Cohere Plans Pricing
  plan_count: 24
  slug: cohere-plans-pricing
random_paper: 6
rate_limits:
- limit_count: 5
  name: Cohere Rate Limits
  slug: cohere-rate-limits
rules:
- authorship: generated
  effective_rule_count: 36
  extends:
  - spectral:asyncapi
  name: Cohere — asyncapi rules
  rule_count: 9
  severity_counts:
    error: 1
    hint: 0
    info: 0
    warn: 8
  slug: cohere-asyncapi-spectral-rules
- authorship: generated
  effective_rule_count: 6
  extends: []
  name: Cohere — jsonschema rules
  rule_count: 6
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 5
  slug: cohere-jsonschema-spectral-rules
score:
  band: thin
  composite: 36.4
  coverage:
    artifact_dirs: 25
    catalog_earned: 56.5
    catalog_earned_first_party: 12.0
    catalog_gap: 58.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -1.4
  facets:
    access_clarity: 36.8
    contract_governance: 13.6
    contract_quality: 64.7
    developer_ergonomics: 23.8
    discoverability: 61.7
    operational_transparency: 10.5
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - canada
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - north-america
  previous_composite: 37.8
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 17
    mcp: first-party
  regulatory:
    applies: true
    matched_via: residual_tags
    regime: AI & Biometrics
    regime_id: ai_biometrics
    score: 15.5
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/cohere/cohere-2026-06-20T174719.png
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
tags:
- Artificial Intelligence
- Natural Language Processing
- Embeddings
- Vector Search
- LLM
- Canada
- Foundation Models
website: https://www.cohere.com/
---
