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
    mcp_server: documented
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 23.2
  scored_at: '2026-09-01'
agentic_access:
- acting_count: 5
  human_in_the_loop: 0
  name: Jina Ai Agentic Access
  operation_count: 9
  slug: jina-ai-agentic-access
  summary_line: 9 operations · 5 acting
api_count: 3
apis:
- description: Asynchronous batch embedding jobs
  name: Jina AI Batch API
  slug: jina-ai-batch-api
- description: Synchronous embedding generation
  name: Jina AI Embeddings API
  slug: jina-ai-embeddings-api
- description: URL-to-markdown extraction
  name: Jina AI Reader API
  slug: jina-ai-reader-api
- description: Cross-encoder reranking
  name: Jina AI Reranker API
  slug: jina-ai-reranker-api
artifact_total: 19
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Jina AI Embeddings Batch API
  slug: open-jina-ai-batch-api
- collection_type: open
  name: Jina AI Batch Embeddings API
  slug: open-jina-ai-embeddings-api
- collection_type: open
  name: Jina AI Embeddings API
  slug: open-jina-ai-embeddings
- collection_type: open
  name: Jina AI Embeddings Batch Reader API
  slug: open-jina-ai-reader-api
- collection_type: open
  name: Jina AI Reader API
  slug: open-jina-ai-reader
- collection_type: open
  name: Jina AI Embeddings Batch Reranker API
  slug: open-jina-ai-reranker-api
- collection_type: open
  name: Jina AI Reranker API
  slug: open-jina-ai-reranker
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/jina-ai-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/jina-ai-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/jina-ai-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/jinaai
- group: company
  title: ''
  type: Website
  url: https://jina.ai
- group: start
  title: ''
  type: Portal
  url: https://jina.ai/api-dashboard/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.jina.ai/
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.jina.ai/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/jina-ai
- group: start
  title: ''
  type: Signup
  url: https://jina.ai/api-dashboard/
- group: agent
  title: ''
  type: MCPServer
  url: https://github.com/jina-ai/MCP
- group: agent
  title: ''
  type: LlmsText
  url: https://docs.jina.ai/llms.txt
created: '2025-02-06'
description: Jina AI provides Search Foundation APIs for AI-powered applications, offering embeddings, reranking, and web reading capabilities. Their Reader API converts URLs to LLM-friendly input by simply adding r.jina.ai in front.
finops:
- name: Jina Ai Finops
  service_category: AI Infrastructure
  slug: jina-ai-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/jina-ai.png
layout: provider
mcp_servers:
- description: ''
  name: MCP Server
  slug: mcp-server
modified: '2026-05-19'
name: Jina AI
nav: Providers
network: true
overview: 'Jina AI publishes 4 APIs on the [APIs.io](https://apis.io/) network, including Batch API, Embeddings API, Reader API, and 1 more. Tagged areas include Artificial Intelligence, Embeddings, Machine-Learning, Reranking, and Search.


  Jina AI''s developer surface includes authentication, developer portal, documentation, getting-started guide, signup flow, and 7 more developer resources.'
plans:
- name: Jina Ai Plans Pricing
  plan_count: 5
  slug: jina-ai-plans-pricing
random_paper: 14
rate_limits:
- limit_count: 9
  name: Jina Ai Rate Limits
  slug: jina-ai-rate-limits
score:
  band: thin
  composite: 35.0
  coverage:
    artifact_dirs: 10
    catalog_gap: 66.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 28.9
    commercial_clarity: 28.9
    contract_governance: 0.0
    contract_quality: 54.1
    developer_ergonomics: 31.0
    discoverability: 81.5
    governance: 0.0
    operational_transparency: 10.5
  previous_composite: 35.0
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 4
  schema_version: 0.17.2
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/jina-ai/refs/heads/main/screenshots/jina-ai-2026-06-20T183733.png
security:
- kind: authentication
  name: Jina Ai Authentication
  slug: jina-ai-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Jina Ai Domain Security
  slug: jina-ai-domain-security
  summary_line: TLSv1.3 · DMARC
slug: jina-ai
tags:
- Artificial Intelligence
- Embeddings
- Machine-Learning
- Reranking
- Search
website: https://jina.ai
---
