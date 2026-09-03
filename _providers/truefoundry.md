---
access_model:
  confidence: medium
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
    agent_card: near-conformant
    agent_skills: true
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
    mcp_server: documented
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 30.3
  scored_at: '2026-09-02'
agentic_access:
- acting_count: 10
  human_in_the_loop: 0
  name: Truefoundry Agentic Access
  operation_count: 14
  slug: truefoundry-agentic-access
  summary_line: 14 operations · 10 acting
api_count: 1
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
- baseURL: https://gateway.truefoundry.ai/api/llm
  baseurl_source: declared
  description: Speech and audio processing
  name: TrueFoundry Audio API
  slug: truefoundry-audio-api
- baseURL: https://gateway.truefoundry.ai/api/llm
  baseurl_source: declared
  description: Batch request processing
  name: TrueFoundry Batches API
  slug: truefoundry-batches-api
- baseURL: https://gateway.truefoundry.ai/api/llm
  baseurl_source: declared
  description: Chat completion operations for LLM conversation
  name: TrueFoundry Chat API
  slug: truefoundry-chat-api
- baseURL: https://gateway.truefoundry.ai/api/llm
  baseurl_source: declared
  description: Text embedding operations
  name: TrueFoundry Embeddings API
  slug: truefoundry-embeddings-api
- baseURL: https://gateway.truefoundry.ai/api/llm
  baseurl_source: declared
  description: File upload and management
  name: TrueFoundry Files API
  slug: truefoundry-files-api
- baseURL: https://gateway.truefoundry.ai/api/llm
  baseurl_source: declared
  description: Image generation and manipulation
  name: TrueFoundry Images API
  slug: truefoundry-images-api
- baseURL: https://gateway.truefoundry.ai/api/llm
  baseurl_source: declared
  description: Available model listing
  name: TrueFoundry Models API
  slug: truefoundry-models-api
- baseURL: https://gateway.truefoundry.ai/api/llm
  baseurl_source: declared
  description: Content moderation
  name: TrueFoundry Moderations API
  slug: truefoundry-moderations-api
- baseURL: https://gateway.truefoundry.ai/api/llm
  baseurl_source: declared
  description: Reranking for search relevance
  name: TrueFoundry Rerank API
  slug: truefoundry-rerank-api
artifact_total: 67
collections:
- collection_type: postman
  name: TrueFoundry AI Gateway Audio API
  slug: postman-truefoundry-audio-api
- collection_type: postman
  name: TrueFoundry AI Gateway Audio Batches API
  slug: postman-truefoundry-batches-api
- collection_type: postman
  name: TrueFoundry AI Gateway Audio Chat API
  slug: postman-truefoundry-chat-api
- collection_type: postman
  name: TrueFoundry AI Gateway Audio Embeddings API
  slug: postman-truefoundry-embeddings-api
- collection_type: postman
  name: TrueFoundry AI Gateway Audio Files API
  slug: postman-truefoundry-files-api
- collection_type: postman
  name: TrueFoundry AI Gateway Audio Images API
  slug: postman-truefoundry-images-api
- collection_type: postman
  name: TrueFoundry AI Gateway Audio Models API
  slug: postman-truefoundry-models-api
- collection_type: postman
  name: TrueFoundry AI Gateway Audio Moderations API
  slug: postman-truefoundry-moderations-api
- collection_type: postman
  name: TrueFoundry AI Gateway Audio Rerank API
  slug: postman-truefoundry-rerank-api
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: TrueFoundry AI Gateway API
  slug: open-truefoundry-ai-gateway
- collection_type: open
  name: TrueFoundry AI Gateway Audio API
  slug: open-truefoundry-audio-api
- collection_type: open
  name: TrueFoundry AI Gateway Audio Batches API
  slug: open-truefoundry-batches-api
- collection_type: open
  name: TrueFoundry AI Gateway Audio Chat API
  slug: open-truefoundry-chat-api
- collection_type: open
  name: TrueFoundry AI Gateway Audio Embeddings API
  slug: open-truefoundry-embeddings-api
- collection_type: open
  name: TrueFoundry AI Gateway Audio Files API
  slug: open-truefoundry-files-api
- collection_type: open
  name: TrueFoundry AI Gateway Audio Images API
  slug: open-truefoundry-images-api
- collection_type: open
  name: TrueFoundry AI Gateway Audio Models API
  slug: open-truefoundry-models-api
- collection_type: open
  name: TrueFoundry AI Gateway Audio Moderations API
  slug: open-truefoundry-moderations-api
- collection_type: open
  name: TrueFoundry AI Gateway Audio Rerank API
  slug: open-truefoundry-rerank-api
common:
- group: operate
  title: ''
  type: IssueTracker
  url: https://github.com/truefoundry/truefoundry-python-sdk/issues
- group: operate
  title: ''
  type: Releases
  url: https://github.com/truefoundry/truefoundry-python-sdk/releases
- group: docs
  title: ''
  type: ContributionGuide
  url: https://github.com/truefoundry/truefoundry-python-sdk/blob/main/CONTRIBUTING.md
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/truefoundry/overview
- group: other
  title: ''
  type: AgentCard
  url: a2a/truefoundry-a2a.yml
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
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/apis-json-logo.jpg
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
mcp_servers:
- description: ''
  name: MCP Server
  slug: mcp-server
modified: '2026-05-19'
name: TrueFoundry
nav: Providers
network: true
overview: 'TrueFoundry publishes 9 APIs on the [APIs.io](https://apis.io/) network, including Audio API, Batches API, Chat API, and 6 more. Tagged areas include AI Platform, Enterprise AI, Kubernetes, LLM Gateway, and MLOps.


  The TrueFoundry catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  TrueFoundry''s developer surface includes authentication, documentation, getting-started guide, pricing, engineering blog, changelog, signup flow, and 16 more developer resources.'
plans:
- name: Truefoundry Plans Pricing
  plan_count: 4
  slug: truefoundry-plans-pricing
random_paper: 5
rate_limits:
- limit_count: 6
  name: Truefoundry Rate Limits
  slug: truefoundry-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: TrueFoundry API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: truefoundry-jsonschema-spectral-rules
- effective_rule_count: 50
  extends:
  - spectral:oas
  name: TrueFoundry API Rules
  rule_count: 9
  severity_counts:
    error: 3
    hint: 2
    info: 0
    warn: 4
  slug: truefoundry-rules
score:
  band: developing
  composite: 51.6
  coverage:
    artifact_dirs: 19
    catalog_gap: 45.5
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 47.4
    commercial_clarity: 47.4
    contract_governance: 28.8
    contract_quality: 64.7
    developer_ergonomics: 61.9
    discoverability: 68.5
    governance: 28.8
    operational_transparency: 26.3
  open_source:
    applies: true
    score: 50.0
  previous_composite: 51.6
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 9
  schema_version: 0.18.0
  scored_at: '2026-09-02'
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
