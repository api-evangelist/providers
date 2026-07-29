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
    agent_skills: false
    agentic_access: derived
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: true
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 41.4
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 5
  human_in_the_loop: 0
  name: Jina Ai Agentic Access
  operation_count: 9
  slug: jina-ai-agentic-access
  summary_line: 9 operations · 5 acting
api_count: 4
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
artifact_total: 14
collections:
- collection_type: open
  name: Jina AI Embeddings API
  slug: open-jina-ai-embeddings
- collection_type: open
  name: Jina AI Reader API
  slug: open-jina-ai-reader
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
overview: 'Jina AI publishes 4 APIs on the [APIs.io](https://apis.io/) network, including Batch API, Embeddings API, Reader API, and 1 more. Tagged areas include AI, Embeddings, Machine Learning, Reranking, and Search.


  Jina AI''s developer surface includes authentication, developer portal, documentation, getting-started guide, signup flow, and 7 more developer resources.'
plans:
- name: Jina Ai Plans Pricing
  plan_count: 5
  slug: jina-ai-plans-pricing
random_paper: 33
rate_limits:
- limit_count: 9
  name: Jina Ai Rate Limits
  slug: jina-ai-rate-limits
score:
  band: developing
  composite: 44.2
  delta: -2.7
  facets:
    commercial_clarity: 39.5
    contract_quality: 58.1
    developer_ergonomics: 47.8
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 36.8
  previous_composite: 46.9
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 4
  schema_version: 0.6
  scored_at: '2026-07-28'
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
- AI
- Embeddings
- Machine Learning
- Reranking
- Search
website: https://jina.ai
---
