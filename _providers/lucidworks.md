---
access_model:
  confidence: high
  label: Enterprise · Self-serve signup
  onboarding: self-serve
  pricing: enterprise
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 29.1
  scored_at: '2026-08-24'
agentic_access:
- acting_count: 20
  human_in_the_loop: 0
  name: Lucidworks Agentic Access
  operation_count: 33
  slug: lucidworks-agentic-access
  summary_line: 33 operations · 20 acting
api_count: 12
apis:
- description: Fusion REST APIs administer collections, indexing pipelines, query pipelines, connectors, and search apps inside the Lucidworks Fusion platform. The legacy Custom Rules API for Fusion 5.7 is part of t
  name: Lucidworks Fusion REST API
  slug: fusion
- description: Split content into chunks
  name: Lucidworks Chunking API
  slug: lucidworks-chunking-api
- description: Predict ranked labels
  name: Lucidworks Classification API
  slug: lucidworks-classification-api
- description: Manage model deployments
  name: Lucidworks Deployments API
  slug: lucidworks-deployments-api
- description: Generate vector encodings
  name: Lucidworks Embeddings API
  slug: lucidworks-embeddings-api
- description: Manage models
  name: Lucidworks Models API
  slug: lucidworks-models-api
- description: Submit prediction requests by use case
  name: Lucidworks Predictions API
  slug: lucidworks-predictions-api
- description: Manage query rewrite rules
  name: Lucidworks QueryRewrites API
  slug: lucidworks-queryrewrites-api
- description: Fetch prediction results
  name: Lucidworks Results API
  slug: lucidworks-results-api
- description: Manage custom business rules
  name: Lucidworks Rules API
  slug: lucidworks-rules-api
- description: Capture and retrieve user behavior signals
  name: Lucidworks Signals API
  slug: lucidworks-signals-api
- description: Tokenize text by model
  name: Lucidworks Tokenization API
  slug: lucidworks-tokenization-api
artifact_total: 57
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Lucidworks AI Platform API
  slug: open-lucidworks-ai-platform
- collection_type: open
  name: Lucidworks AI Platform Chunking API
  slug: open-lucidworks-chunking-api
- collection_type: open
  name: Lucidworks Content Chunking API
  slug: open-lucidworks-chunking
- collection_type: open
  name: Lucidworks AI Platform Chunking Classification API
  slug: open-lucidworks-classification-api
- collection_type: open
  name: Lucidworks AI Platform Chunking Deployments API
  slug: open-lucidworks-deployments-api
- collection_type: open
  name: Lucidworks AI Platform Chunking Embeddings API
  slug: open-lucidworks-embeddings-api
- collection_type: open
  name: Lucidworks Embeddings and Classification API
  slug: open-lucidworks-embeddings
- collection_type: open
  name: Lucidworks AI Platform Chunking Models API
  slug: open-lucidworks-models-api
- collection_type: open
  name: Lucidworks Model Management API
  slug: open-lucidworks-models
- collection_type: open
  name: Lucidworks AI Platform Chunking Predictions API
  slug: open-lucidworks-predictions-api
- collection_type: open
  name: Lucidworks AI Platform Chunking QueryRewrites API
  slug: open-lucidworks-queryrewrites-api
- collection_type: open
  name: Lucidworks AI Platform Chunking Results API
  slug: open-lucidworks-results-api
- collection_type: open
  name: Lucidworks AI Platform Chunking Rules API
  slug: open-lucidworks-rules-api
- collection_type: open
  name: Lucidworks Rules and Query Rewrites API
  slug: open-lucidworks-rules
- collection_type: open
  name: Lucidworks AI Platform Chunking Signals API
  slug: open-lucidworks-signals-api
- collection_type: open
  name: Lucidworks Signals API
  slug: open-lucidworks-signals
- collection_type: open
  name: Lucidworks AI Platform Chunking Tokenization API
  slug: open-lucidworks-tokenization-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/lucidworks-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/lucidworks-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/lucidworks-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/lucidworks-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/lucidworks
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/lucidworks
- group: company
  title: ''
  type: Website
  url: https://lucidworks.com
- group: docs
  title: ''
  type: Documentation
  url: https://doc.lucidworks.com
- group: docs
  title: ''
  type: APIReference
  url: https://doc.lucidworks.com/api-reference
- group: auth
  title: ''
  type: Authentication
  url: https://doc.lucidworks.com/api-reference/request-access-token/request-access-token
- group: build
  title: ''
  type: SDKs
  url: https://doc.lucidworks.com/docs/5/fusion/dev-portal/connectors-sdk/overview
- group: company
  title: ''
  type: Blog
  url: https://lucidworks.com/blog
- group: agent
  title: ''
  type: LlmsText
  url: https://lucidworks.ai/llms.txt
created: '2025-01-07'
description: Lucidworks builds AI-powered search, discovery, and agent platforms used by enterprise commerce, support, and workplace teams. The Lucidworks AI Platform, Fusion, Neural Hybrid Search, Agent Studio, Commerce Studio, and Analytics Studio expose REST APIs for prediction, embedding, classification, signals capture, query rewriting, custom rule management, content chunking, and model deployment.
finops:
- name: Lucidworks Finops
  service_category: Enterprise Search
  slug: lucidworks-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/lucidworks.png
json_schemas:
- name: ChunkAck
  property_count: 2
  slug: lucidworks-chunkack
- name: ChunkRequest
  property_count: 4
  slug: lucidworks-chunkrequest
- name: ChunkResult
  property_count: 3
  slug: lucidworks-chunkresult
- name: ClassifyRequest
  property_count: 2
  slug: lucidworks-classifyrequest
- name: ClassifyResponse
  property_count: 1
  slug: lucidworks-classifyresponse
- name: Deployment
  property_count: 4
  slug: lucidworks-deployment
- name: Embedding
  property_count: 2
  slug: lucidworks-embedding
- name: EncodeRequest
  property_count: 1
  slug: lucidworks-encoderequest
- name: Model
  property_count: 5
  slug: lucidworks-model
- name: PredictionAck
  property_count: 2
  slug: lucidworks-predictionack
- name: PredictionRequest
  property_count: 2
  slug: lucidworks-predictionrequest
- name: PredictionResult
  property_count: 3
  slug: lucidworks-predictionresult
- name: QueryRewrite
  property_count: 5
  slug: lucidworks-queryrewrite
- name: Rule
  property_count: 6
  slug: lucidworks-rule
- name: Signal
  property_count: 5
  slug: lucidworks-signal
- name: SignalList
  property_count: 2
  slug: lucidworks-signallist
- name: TokenRequest
  property_count: 3
  slug: lucidworks-tokenrequest
- name: TokenResponse
  property_count: 3
  slug: lucidworks-tokenresponse
json_structures:
- name: Lucidworks Structure
  property_count: 0
  slug: lucidworks-structure
layout: provider
modified: '2026-05-19'
name: Lucidworks
nav: Providers
network: true
overview: 'Lucidworks publishes 11 APIs on the [APIs.io](https://apis.io/) network, including Chunking API, Classification API, Deployments API, and 8 more. Tagged areas include Search, Artificial Intelligence, Enterprise Search, Vector Search, and RAG.


  The Lucidworks catalog on APIs.io includes 1 Spectral governance ruleset.


  Lucidworks'' developer surface includes authentication, documentation, API reference, engineering blog, and 9 more developer resources.'
plans:
- name: Lucidworks Plans Pricing
  plan_count: 1
  slug: lucidworks-plans-pricing
random_paper: 3
rate_limits:
- limit_count: 2
  name: Lucidworks Rate Limits
  slug: lucidworks-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: Lucidworks API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: lucidworks-jsonschema-spectral-rules
score:
  band: thin
  composite: 34.6
  delta: 0.0
  facets:
    access_clarity: 21.1
    commercial_clarity: 21.1
    contract_governance: 9.8
    contract_quality: 56.3
    developer_ergonomics: 38.1
    discoverability: 64.8
    governance: 9.8
    operational_transparency: 7.9
  previous_composite: 34.6
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 11
  schema_version: 0.12.1
  scored_at: '2026-08-24'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/lucidworks/refs/heads/main/screenshots/lucidworks-2026-06-20T184745.png
security:
- kind: authentication
  name: Lucidworks Authentication
  slug: lucidworks-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Lucidworks Domain Security
  slug: lucidworks-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Lucidworks Trust Center
  slug: lucidworks-trust-center
  summary_line: SOC 2, ISO 27001, GDPR, CSA STAR
slug: lucidworks
tags:
- Search
- Artificial Intelligence
- Enterprise Search
- Vector Search
- RAG
- Commerce
website: https://lucidworks.com
---
