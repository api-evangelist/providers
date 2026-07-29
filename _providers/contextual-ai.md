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
- acting_count: 16
  human_in_the_loop: 0
  name: Contextual Ai Agentic Access
  operation_count: 25
  slug: contextual-ai-agentic-access
  summary_line: 25 operations · 16 acting
api_count: 9
apis:
- description: Create, configure, and manage RAG agents.
  name: Contextual AI Agents API
  slug: contextual-ai-agents-api
- description: Query agents for grounded responses, retrievals, metrics, and feedback.
  name: Contextual AI Agents Query API
  slug: contextual-ai-agents-query-api
- description: Create and manage datastores that hold ingested knowledge.
  name: Contextual AI Datastores API
  slug: contextual-ai-datastores-api
- description: Ingest and manage documents within a datastore.
  name: Contextual AI Documents API
  slug: contextual-ai-documents-api
- description: Grounded generation with the Grounded Language Model (GLM).
  name: Contextual AI Generate API
  slug: contextual-ai-generate-api
- description: Evaluate model responses with natural-language unit tests.
  name: Contextual AI LMUnit API
  slug: contextual-ai-lmunit-api
- description: Parse documents into structured, AI-ready markdown.
  name: Contextual AI Parse API
  slug: contextual-ai-parse-api
- description: Instruction-following reranking of retrieved passages.
  name: Contextual AI Rerank API
  slug: contextual-ai-rerank-api
- description: Manage workspace users.
  name: Contextual AI Users API
  slug: contextual-ai-users-api
artifact_total: 20
asyncapis:
- description: AsyncAPI 2.6 description of Contextual AI's **agent query streaming** surface. Contextual AI does not publish a WebSocket API. The only asynchronous / event-style transport documented at https://docs.
  name: Contextual AI Agent Query Streaming (HTTP + SSE)
  slug: contextual-ai-asyncapi
collections:
- collection_type: open
  name: Contextual AI Platform API
  slug: open-contextual-ai
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/contextual-ai-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/contextual-ai-trust-center.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/contextual-ai-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/contextual-ai-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/contextual-ai-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/ContextualAI
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/contextual-ai
- group: company
  title: ''
  type: Website
  url: https://contextual.ai/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.contextual.ai
- group: commercial
  title: ''
  type: Plans
  url: plans/contextual-ai-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/contextual-ai-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/contextual-ai-finops.yml
- group: company
  title: ''
  type: Blog
  url: https://contextual.ai/blog
created: '2026-06-20'
description: Contextual AI is an enterprise RAG platform built around a Grounded Language Model (GLM) engineered to minimize hallucinations. Its REST API exposes end-to-end RAG agents (create, configure, query) plus standalone component APIs - Generate, Rerank, Parse, and LMUnit - over datastores of ingested documents, all authenticated with a Bearer API key.
finops:
- name: Contextual Ai Finops
  service_category: AI and Machine Learning
  slug: contextual-ai-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/contextual-ai.png
layout: provider
modified: '2026-06-20'
name: Contextual AI
nav: Providers
network: true
overview: 'Contextual AI publishes 9 APIs on the [APIs.io](https://apis.io/) network, including Agents API, Agents Query API, Datastores API, and 6 more. Tagged areas include AI, RAG, LLM, Grounded Language Model, and Enterprise.


  The Contextual AI catalog on APIs.io includes 1 event-driven AsyncAPI specification and 1 Spectral governance ruleset.


  Contextual AI''s developer surface includes authentication, documentation, engineering blog, and 10 more developer resources.'
plans:
- name: Contextual Ai Plans Pricing
  plan_count: 2
  slug: contextual-ai-plans-pricing
random_paper: 46
rate_limits:
- limit_count: 6
  name: Contextual Ai Rate Limits
  slug: contextual-ai-rate-limits
rules:
- name: Contextual AI API Rules
  rule_count: 8
  severity_counts:
    error: 1
    hint: 0
    info: 0
    warn: 7
  slug: contextual-ai-asyncapi-spectral-rules
score:
  band: developing
  composite: 45.8
  delta: -3.5
  facets:
    commercial_clarity: 36.8
    contract_quality: 67.5
    developer_ergonomics: 21.7
    discoverability: 74.1
    governance: 41.7
    operational_transparency: 36.8
  previous_composite: 49.3
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
screenshot: https://raw.githubusercontent.com/api-evangelist/contextual-ai/refs/heads/main/screenshots/contextual-ai-2026-06-20T174932.png
security:
- kind: authentication
  name: Contextual Ai Authentication
  slug: contextual-ai-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Contextual Ai Domain Security
  slug: contextual-ai-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Contextual Ai Vulnerability Disclosure
  slug: contextual-ai-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Contextual Ai Trust Center
  slug: contextual-ai-trust-center
  summary_line: SOC 2, ISO 27017, PCI DSS, CSA STAR
slug: contextual-ai
tags:
- AI
- RAG
- LLM
- Grounded Language Model
- Enterprise
website: https://contextual.ai/
---
