---
access_model:
  confidence: medium
  label: Free
  onboarding: unknown
  pricing: free
  public: false
  source:
  - plans
  trial: false
  try_now: false
agent_readiness:
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 3.2
  scored_at: '2026-08-10'
api_count: 1
apis:
- description: The Zep Cloud API delivers agent memory and temporal knowledge graph services over REST. It exposes endpoints for users, sessions, messages, memory retrieval, the per-user graph, facts, summaries, and
  name: Zep Cloud API
  slug: cloud-api
artifact_total: 6
common:
- group: auth
  title: ''
  type: TrustCenter
  url: security/zep-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/zep-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.getzep.com
- group: docs
  title: ''
  type: Documentation
  url: https://help.getzep.com
- group: company
  title: ''
  type: Blog
  url: https://blog.getzep.com
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/getzep
- group: commercial
  title: ''
  type: Pricing
  url: https://www.getzep.com/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.getzep.com/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.getzep.com/privacy-policy
- group: operate
  title: ''
  type: Discord
  url: https://discord.com/invite/W8Kw6bsgXQ
- group: other
  title: ''
  type: X
  url: https://x.com/zep_ai
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/zep-ai
created: '2026-05-23'
description: Zep is a context engineering and agent memory platform that assembles relevant context from chat history, business data, and user interactions for AI agents. It builds a temporal knowledge graph per user that evolves as new facts arrive, automatically extracts entities, and invalidates facts that are superseded. Zep exposes a Graph RAG layer with customizable context blocks for fast personalization. The platform offers Cloud and self-hosted community editions with Python, TypeScript, and Go SDKs and integrations with LangChain, LangGraph, LlamaIndex, CrewAI, and AutoGen. Zep targets sub-200ms p95 retrieval latency and is SOC 2 Type II and HIPAA aligned for enterprise deployments.
finops:
- name: Zep Finops
  service_category: API
  slug: zep-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/zep.png
layout: provider
modified: '2026-05-23'
name: Zep
nav: Providers
network: true
overview: 'Zep publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Memory, AI Agents, Knowledge Graph, Temporal Graph, and Graph RAG.


  Zep''s developer surface includes documentation, engineering blog, pricing, and 9 more developer resources.'
plans:
- name: Zep Plans Pricing
  plan_count: 1
  slug: zep-plans-pricing
random_paper: 103
rate_limits:
- limit_count: 2
  name: Zep Rate Limits
  slug: zep-rate-limits
score:
  band: emerging
  composite: 26.1
  delta: 0.0
  facets:
    commercial_clarity: 68.4
    contract_quality: 0.0
    developer_ergonomics: 10.9
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 26.3
  previous_composite: 26.1
  schema_version: 0.9.1
  scored_at: '2026-08-10'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/zep/refs/heads/main/screenshots/zep-2026-06-20T201828.png
security:
- kind: domain-security
  name: Zep Domain Security
  slug: zep-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: trust-center
  name: Zep Trust Center
  slug: zep-trust-center
  summary_line: SOC 2, HIPAA
slug: zep
tags:
- Memory
- AI Agents
- Knowledge Graph
- Temporal Graph
- Graph RAG
- Context Engineering
- LangChain
- LlamaIndex
- CrewAI
- LLMs
- Personalization
- Retrieval
website: https://www.getzep.com
---
