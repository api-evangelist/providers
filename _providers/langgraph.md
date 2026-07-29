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
    error_semantics: verified
    idempotency: false
    mcp_server: false
    openapi_examples: partial
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 41.0
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 20
  human_in_the_loop: 1
  name: Langgraph Agentic Access
  operation_count: 39
  slug: langgraph-agentic-access
  summary_line: 39 operations · 20 acting · 1 human-in-the-loop
api_count: 5
apis:
- description: The Agent Connections (v2) API from LangGraph — 2 operation(s) for agent connections (v2).
  name: LangGraph Agent Connections (v2) API
  slug: langgraph-agent-connections-v2-api
- description: The Auth Service (v2) API from LangGraph — 13 operation(s) for auth service (v2).
  name: LangGraph Auth Service (v2) API
  slug: langgraph-auth-service-v2-api
- description: The Deployments (v2) API from LangGraph — 5 operation(s) for deployments (v2).
  name: LangGraph Deployments (v2) API
  slug: langgraph-deployments-v2-api
- description: The Integrations (v1) API from LangGraph — 4 operation(s) for integrations (v1).
  name: LangGraph Integrations (v1) API
  slug: langgraph-integrations-v1-api
- description: The Listeners (v2) API from LangGraph — 2 operation(s) for listeners (v2).
  name: LangGraph Listeners (v2) API
  slug: langgraph-listeners-v2-api
artifact_total: 12
collections:
- collection_type: open
  name: LangSmith Deployment Control Plane API
  slug: open-langgraph
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/langgraph-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/langgraph-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/langgraph-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://www.langchain.com/langgraph
- group: docs
  title: ''
  type: Documentation
  url: https://docs.langchain.com/langgraph-platform
- group: build
  title: ''
  type: GitHub
  url: https://github.com/langchain-ai/langgraph
- group: other
  title: ''
  type: ParentCompany
  url: https://www.langchain.com/
- group: company
  title: ''
  type: Blog
  url: https://www.langchain.com/blog/rss.xml
created: '2026-01-02'
description: LangGraph is an open-source framework from LangChain for building stateful, multi-actor agent workflows with low-level primitives for greater control over agent behavior. LangGraph Platform (LangSmith Deployment) provides managed infrastructure for running agents in production with assistants, threads, and runs.
finops:
- name: Langgraph Finops
  service_category: API
  slug: langgraph-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/langgraph.png
layout: provider
modified: '2026-05-19'
name: LangGraph
nav: Providers
network: true
overview: 'LangGraph publishes 5 APIs on the [APIs.io](https://apis.io/) network, including Agent Connections (v2) API, Auth Service (v2) API, Deployments (v2) API, and 2 more. Tagged areas include Agents, Artificial Intelligence, Large Language Models, Workflows, and Orchestration.


  LangGraph''s developer surface includes authentication, documentation, GitHub presence, engineering blog, and 4 more developer resources.'
plans:
- name: Langgraph Plans Pricing
  plan_count: 3
  slug: langgraph-plans-pricing
random_paper: 24
rate_limits:
- limit_count: 5
  name: Langgraph Rate Limits
  slug: langgraph-rate-limits
score:
  band: thin
  composite: 37.2
  delta: -3.2
  facets:
    commercial_clarity: 39.5
    contract_quality: 51.1
    developer_ergonomics: 21.7
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 36.8
  previous_composite: 40.4
  provenance:
    agentic_access: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 5
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/langgraph/refs/heads/main/screenshots/langgraph-2026-06-20T184305.png
security:
- kind: authentication
  name: Langgraph Authentication
  slug: langgraph-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Langgraph Domain Security
  slug: langgraph-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: langgraph
tags:
- Agents
- Artificial Intelligence
- Large Language Models
- Workflows
- Orchestration
website: https://www.langchain.com/langgraph
---
