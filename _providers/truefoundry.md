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
  band: agent-native
  dimensions:
    agent_skills: true
    agentic_access: true
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    error_semantics: false
    idempotency: false
    mcp_server: true
    openapi_examples: false
    rate_limit_signal: true
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.1
  score: 64.4
  scored_at: '2026-07-23'
agentic_access:
- acting_count: 10
  human_in_the_loop: 0
  name: Truefoundry Agentic Access
  operation_count: 14
  slug: truefoundry-agentic-access
  summary_line: 14 operations · 10 acting
api_count: 13
apis:
- description: The TrueFoundry MCP (Model Context Protocol) Gateway provides a centralized registry and proxy for managing MCP servers accessible to AI agents. It handles authentication, access control, schema valid
  name: TrueFoundry MCP Gateway API
  slug: truefoundry-mcp-gateway-api
- description: The TrueFoundry Platform API provides programmatic access to the TrueFoundry MLOps platform for managing applications, deployments, users, and infrastructure resources. It enables automation of servic
  name: TrueFoundry Platform API
  slug: truefoundry-platform-api
- description: TrueFoundry's Model Serving capability enables deployment and management of LLM and embedding models using backends like vLLM and Triton on Kubernetes infrastructure. It provides APIs for deploying mo
  name: TrueFoundry Model Serving API
  slug: truefoundry-model-serving-api
- description: 'The TrueFoundry Model Registry provides a versioned repository for storing and managing machine learning models backed by cloud storage such as S3, GCS, Azure Blob, or Minio. It supports programmatic '
  name: TrueFoundry Model Registry API
  slug: truefoundry-model-registry-api
- description: Speech and audio processing
  name: TrueFoundry Audio API
  slug: truefoundry-audio-api
- description: Batch request processing
  name: TrueFoundry Batches API
  slug: truefoundry-batches-api
- description: Chat completion operations for LLM conversation
  name: TrueFoundry Chat API
  slug: truefoundry-chat-api
- description: Text embedding operations
  name: TrueFoundry Embeddings API
  slug: truefoundry-embeddings-api
- description: File upload and management
  name: TrueFoundry Files API
  slug: truefoundry-files-api
- description: Image generation and manipulation
  name: TrueFoundry Images API
  slug: truefoundry-images-api
- description: Available model listing
  name: TrueFoundry Models API
  slug: truefoundry-models-api
- description: Content moderation
  name: TrueFoundry Moderations API
  slug: truefoundry-moderations-api
- description: Reranking for search relevance
  name: TrueFoundry Rerank API
  slug: truefoundry-rerank-api
artifact_total: 47
collections:
- collection_type: open
  name: TrueFoundry AI Gateway API
  slug: open-truefoundry-ai-gateway
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/truefoundry-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/truefoundry-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/truefoundry-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/truefoundry-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/truefoundry
- group: company
  title: ''
  type: Website
  url: https://www.truefoundry.com/
- group: docs
  title: ''
  type: Documentation
  url: https://www.truefoundry.com/docs
- group: start
  title: ''
  type: GettingStarted
  url: https://www.truefoundry.com/docs/ai-gateway/quick-start
- group: auth
  title: ''
  type: Authentication
  url: https://www.truefoundry.com/docs/ai-gateway/authentication
- group: commercial
  title: ''
  type: Pricing
  url: https://www.truefoundry.com/pricing
- group: company
  title: ''
  type: Blog
  url: https://www.truefoundry.com/blog
- group: operate
  title: ''
  type: ChangeLog
  url: https://www.truefoundry.com/docs/changelog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/truefoundry
- group: build
  title: ''
  type: GitHubRepository
  url: https://github.com/truefoundry/truefoundry-python-sdk
- group: build
  title: ''
  type: SDKs
  url: https://github.com/truefoundry/truefoundry-python-sdk
- group: start
  title: ''
  type: Signup
  url: https://app.truefoundry.com/signup
- group: agent
  title: ''
  type: MCPServer
  url: https://github.com/truefoundry/mcp-servers
- group: agent
  title: ''
  type: AgentSkills
  url: https://github.com/truefoundry/skills
created: '2026-03-16'
description: TrueFoundry is a Kubernetes-native enterprise AI platform for deploying and managing agentic AI workloads. It provides an AI Gateway, MCP Gateway, model serving, fine-tuning, and a full MLOps platform that works across on-premises, VPC, hybrid, or public cloud environments.
examples:
- key_count: 2
  name: Truefoundry Chat Completion Example
  slug: truefoundry-chat-completion-example
- key_count: 2
  name: Truefoundry Embeddings Example
  slug: truefoundry-embeddings-example
finops:
- name: Truefoundry Finops
  service_category: AI Gateway / LLMOps
  slug: truefoundry-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/truefoundry.png
json_schemas:
- name: BatchObject
  property_count: 9
  slug: truefoundry-batchobject
- name: Chat Completion Request
  property_count: 7
  slug: truefoundry-chat-completion
- name: ChatCompletionRequest
  property_count: 15
  slug: truefoundry-chatcompletionrequest
- name: ChatCompletionResponse
  property_count: 8
  slug: truefoundry-chatcompletionresponse
- name: EmbeddingRequest
  property_count: 5
  slug: truefoundry-embeddingrequest
- name: EmbeddingResponse
  property_count: 4
  slug: truefoundry-embeddingresponse
- name: FileObject
  property_count: 6
  slug: truefoundry-fileobject
- name: ImageGenerationRequest
  property_count: 6
  slug: truefoundry-imagegenerationrequest
- name: ImageGenerationResponse
  property_count: 2
  slug: truefoundry-imagegenerationresponse
- name: ModelObject
  property_count: 4
  slug: truefoundry-modelobject
json_structures:
- name: Truefoundry Chat Completion Structure
  property_count: 0
  slug: truefoundry-chat-completion-structure
- name: Truefoundry Structure
  property_count: 0
  slug: truefoundry-structure
jsonld:
- class_count: 28
  name: Truefoundry Context
  property_count: 1
  slug: truefoundry-context
layout: provider
modified: '2026-05-19'
name: TrueFoundry
nav: Providers
network: true
overview: 'TrueFoundry publishes 9 APIs on the [APIs.io](https://apis.io/) network, including Audio API, Batches API, Chat API, and 6 more. Tagged areas include AI Platform, Enterprise AI, Kubernetes, LLM Gateway, and MLOps.


  The TrueFoundry catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  TrueFoundry''s developer surface includes authentication, documentation, getting-started guide, pricing, engineering blog, changelog, signup flow, and 11 more developer resources.'
plans:
- name: Truefoundry Plans Pricing
  plan_count: 4
  slug: truefoundry-plans-pricing
random_paper: 50
rate_limits:
- limit_count: 6
  name: Truefoundry Rate Limits
  slug: truefoundry-rate-limits
rules:
- name: TrueFoundry API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: truefoundry-jsonschema-spectral-rules
- name: TrueFoundry API Rules
  rule_count: 9
  severity_counts:
    error: 3
    hint: 2
    info: 0
    warn: 4
  slug: truefoundry-rules
score:
  band: developing
  composite: 59.7
  delta: 0.0
  facets:
    commercial_clarity: 57.9
    contract_quality: 64.7
    developer_ergonomics: 47.8
    discoverability: 67.5
    governance: 73.7
    operational_transparency: 52.6
  previous_composite: 59.7
  schema_version: 0.5
  scored_at: '2026-07-23'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/truefoundry/refs/heads/main/screenshots/truefoundry-2026-06-20T195805.png
security:
- kind: authentication
  name: Truefoundry Authentication
  slug: truefoundry-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Truefoundry Domain Security
  slug: truefoundry-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Truefoundry Trust Center
  slug: truefoundry-trust-center
  summary_line: HIPAA, GDPR
skill_count: 9
skills:
- name: truefoundry-agents
  slug: truefoundry-agents
- name: truefoundry-gateway
  slug: truefoundry-gateway
- name: truefoundry-integrate-gateway
  slug: truefoundry-integrate-gateway
- name: truefoundry-mcp-servers
  slug: truefoundry-mcp-servers
- name: truefoundry-observability
  slug: truefoundry-observability
- name: truefoundry-onboard
  slug: truefoundry-onboard
- name: truefoundry-platform
  slug: truefoundry-platform
- name: truefoundry-prompts
  slug: truefoundry-prompts
- name: truefoundry-skills-registry
  slug: truefoundry-skills-registry
slug: truefoundry
tags:
- AI Platform
- Enterprise AI
- Kubernetes
- LLM Gateway
- MLOps
website: https://www.truefoundry.com/
---
