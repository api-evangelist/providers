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
    agent_skills: true
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
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 30.2
  scored_at: '2026-09-01'
agentic_access:
- acting_count: 3
  human_in_the_loop: 0
  name: Google Gemini Agentic Access
  operation_count: 3
  slug: google-gemini-agentic-access
  summary_line: 3 operations · 3 acting
api_count: 1
apis:
- description: Advanced reasoning and complex task handling.
  name: Gemini Pro API
  slug: gemini-pro-api
- description: Multimodal understanding of text and images.
  name: Gemini Pro Vision API
  slug: gemini-pro-vision-api
- description: Most capable model for highly complex tasks.
  name: Gemini Ultra API
  slug: gemini-ultra-api
- description: Generate text embedding vectors for semantic search, classification, clustering, and retrieval tasks using the gemini-embedding-001 model.
  name: Gemini Embedding API
  slug: gemini-embedding-api
- description: Low-latency real-time voice and video interactions with Gemini using WebSockets for streaming multimodal input and output.
  name: Gemini Live API
  slug: gemini-live-api
- description: Cache input tokens for repeated use across multiple requests to reduce costs and improve latency for large context workloads.
  name: Gemini Context Caching API
  slug: gemini-context-caching-api
- description: Customize Gemini model behavior for specific tasks using supervised fine-tuning with your own training data.
  name: Gemini Fine-Tuning API
  slug: gemini-fine-tuning-api
- description: Unified interface for interacting with Gemini models and agents providing a consistent way to manage multi-turn conversations and tool use.
  name: Gemini Interactions API
  slug: gemini-interactions-api
- description: Enterprise-grade access to Gemini models through Google Cloud Vertex AI with advanced features including grounding, safety filters, and regional endpoints.
  name: Vertex AI Gemini API
  slug: vertex-ai-gemini-api
- description: Generate and edit images using Google Imagen models on Vertex AI for high-quality image creation from text prompts.
  name: Vertex AI Imagen API
  slug: vertex-ai-imagen-api
- description: Enterprise real-time multimodal streaming API on Vertex AI for building low-latency voice and video AI agents.
  name: Vertex AI Gemini Live API
  slug: vertex-ai-gemini-live-api
- description: Generate text embeddings for semantic search and classification tasks using Google embedding models on Vertex AI.
  name: Vertex AI Text Embeddings API
  slug: vertex-ai-text-embeddings-api
- description: Access Gemini API capabilities through Firebase SDKs for mobile and web applications with built-in security and authentication.
  name: Firebase AI Logic API
  slug: firebase-ai-logic-api
- description: Generate content using Gemini models with text, image, audio, and video inputs. Supports multimodal prompts, function calling, structured output, and configurable safety settings.
  name: Google Gemini Content Generation API
  slug: google-gemini-content-generation-api
- description: Generate text embedding vectors for semantic search, classification, clustering, and retrieval tasks using Gemini embedding models.
  name: Google Gemini Embeddings API
  slug: google-gemini-embeddings-api
artifact_total: 59
asyncapis:
- description: 'AsyncAPI specification describing Google Gemini''s real-time and streaming surface area: * The Live API bidirectional WebSocket service (BidiGenerateContent) used for low-latency multimodal voice, vide'
  name: Google Gemini Streaming and Live API
  slug: google-gemini-asyncapi
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Google Gemini API
  slug: open-google-gemini-api
- collection_type: open
  name: Google Gemini Content Generation API
  slug: open-google-gemini-content-generation-api
- collection_type: open
  name: Google Gemini Content Generation Embeddings API
  slug: open-google-gemini-embeddings-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/google-gemini-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/google-gemini-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/google-gemini-authentication.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://ai.google.dev/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://policies.google.com/privacy
- group: operate
  title: ''
  type: StatusPage
  url: https://status.cloud.google.com/
- group: operate
  title: ''
  type: Support
  url: https://ai.google.dev/docs/support
- group: company
  title: ''
  type: Blog
  url: https://developers.googleblog.com/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/google-gemini
- group: operate
  title: ''
  type: Discord
  url: https://discord.gg/google-dev
- group: operate
  title: ''
  type: Forums
  url: https://discuss.ai.google.dev/
- group: learn
  title: ''
  type: Cookbook
  url: https://github.com/google-gemini/cookbook
- group: other
  title: ''
  type: Google AI Studio
  url: https://aistudio.google.com/
- group: other
  title: ''
  type: Safety Guidance
  url: https://ai.google.dev/gemini-api/docs/safety-guidance
- group: other
  title: ''
  type: Vertex AI Studio
  url: https://cloud.google.com/generative-ai-studio
- group: docs
  title: ''
  type: Google Cloud Documentation
  url: https://docs.cloud.google.com/vertex-ai/generative-ai/docs
- group: agent
  title: ''
  type: AgentSkills
  url: https://github.com/google-gemini/gemini-skills
created: '2024-01-01'
description: Google's multimodal AI model APIs for text, image, audio, and video understanding.
finops:
- name: Google Gemini Finops
  service_category: AI Infrastructure / LLM
  slug: google-gemini-finops
graphqls:
- description: Google Gemini is a family of multimodal AI models (Gemini 1.5 Pro, Flash, Ultra). The Gemini API covers text generation, vision, audio, code generation, embeddings, function calling, system instructio
  name: Google Gemini GraphQL API
  slug: google-gemini-graphql
image: https://www.gstatic.com/lamda/images/gemini_sparkle_v002_d4735304ff6292a690345.svg
json_schemas:
- name: Blob
  property_count: 2
  slug: google-gemini-blob
- name: Candidate
  property_count: 6
  slug: google-gemini-candidate
- name: CitationMetadata
  property_count: 1
  slug: google-gemini-citationmetadata
- name: CitationSource
  property_count: 4
  slug: google-gemini-citationsource
- name: Content
  property_count: 2
  slug: google-gemini-content
- name: ContentEmbedding
  property_count: 1
  slug: google-gemini-contentembedding
- name: EmbedContentRequest
  property_count: 4
  slug: google-gemini-embedcontentrequest
- name: EmbedContentResponse
  property_count: 1
  slug: google-gemini-embedcontentresponse
- name: ErrorResponse
  property_count: 1
  slug: google-gemini-errorresponse
- name: FileData
  property_count: 2
  slug: google-gemini-filedata
- name: FunctionCall
  property_count: 2
  slug: google-gemini-functioncall
- name: FunctionCallingConfig
  property_count: 2
  slug: google-gemini-functioncallingconfig
- name: FunctionDeclaration
  property_count: 3
  slug: google-gemini-functiondeclaration
- name: FunctionResponse
  property_count: 2
  slug: google-gemini-functionresponse
- name: Google Gemini Generate Content Schema
  property_count: 0
  slug: google-gemini-generate-content
- name: GenerateContentRequest
  property_count: 7
  slug: google-gemini-generatecontentrequest
- name: GenerateContentResponse
  property_count: 5
  slug: google-gemini-generatecontentresponse
- name: GenerationConfig
  property_count: 11
  slug: google-gemini-generationconfig
- name: Part
  property_count: 5
  slug: google-gemini-part
- name: PromptFeedback
  property_count: 2
  slug: google-gemini-promptfeedback
- name: SafetyRating
  property_count: 3
  slug: google-gemini-safetyrating
- name: SafetySetting
  property_count: 2
  slug: google-gemini-safetysetting
- name: Tool
  property_count: 2
  slug: google-gemini-tool
- name: ToolConfig
  property_count: 1
  slug: google-gemini-toolconfig
- name: UsageMetadata
  property_count: 4
  slug: google-gemini-usagemetadata
json_structures:
- name: Google Gemini Structure
  property_count: 0
  slug: google-gemini-structure
jsonld:
- class_count: 0
  name: Google Gemini Context
  property_count: 23
  slug: google-gemini-context
layout: provider
modified: '2026-05-29'
name: Google Gemini
nav: Providers
network: true
overview: 'Google Gemini publishes 2 APIs on the [APIs.io](https://apis.io/) network: Content Generation API and Embeddings API. Tagged areas include Agentic AI, Artificial Intelligence, Code Generation, Embeddings, and Generative AI.


  The Google Gemini catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 2 Spectral governance rulesets.


  Google Gemini''s developer surface includes authentication, support, engineering blog, and 14 more developer resources.'
plans:
- name: Google Gemini Plans Pricing
  plan_count: 7
  slug: google-gemini-plans-pricing
random_paper: 13
rate_limits:
- limit_count: 7
  name: Google Gemini Rate Limits
  slug: google-gemini-rate-limits
rules:
- effective_rule_count: 36
  extends:
  - spectral:asyncapi
  name: Google Gemini API Rules
  rule_count: 9
  severity_counts:
    error: 1
    hint: 0
    info: 1
    warn: 7
  slug: google-gemini-asyncapi-spectral-rules
- effective_rule_count: 6
  extends: []
  name: Google Gemini API Rules
  rule_count: 6
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 4
  slug: google-gemini-jsonschema-spectral-rules
score:
  band: developing
  composite: 53.2
  coverage:
    artifact_dirs: 19
    catalog_gap: 60.5
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 47.4
    commercial_clarity: 47.4
    contract_governance: 13.6
    contract_quality: 77.7
    developer_ergonomics: 57.1
    discoverability: 57.4
    governance: 13.6
    operational_transparency: 42.1
  previous_composite: 53.2
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 2
  schema_version: 0.17.2
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/google-gemini/refs/heads/main/screenshots/google-gemini-2026-06-20T182205.png
security:
- kind: authentication
  name: Google Gemini Authentication
  slug: google-gemini-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Google Gemini Domain Security
  slug: google-gemini-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
skill_count: 3
skills:
- name: gemini-api-dev
  slug: gemini-api-dev
- name: gemini-interactions-api
  slug: gemini-interactions-api
- name: gemini-live-api-dev
  slug: gemini-live-api-dev
slug: google-gemini
tags:
- Agentic AI
- Artificial Intelligence
- Code Generation
- Embeddings
- Generative AI
- Image-Generation
- LLM
- Machine-Learning
- Multi-Modal
website: https://ai.google.dev/
---
