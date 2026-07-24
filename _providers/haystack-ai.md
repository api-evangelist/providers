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
    agent_skills: false
    agentic_access: true
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: true
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.1
  score: 48.1
  scored_at: '2026-07-23'
agentic_access:
- acting_count: 12
  human_in_the_loop: 0
  name: Haystack Ai Agentic Access
  operation_count: 18
  slug: haystack-ai-agentic-access
  summary_line: 18 operations · 12 acting
api_count: 6
apis:
- description: Apache-2.0 licensed Python framework for composable LLM orchestration. Build modular Pipelines from Components (retrievers, routers, embedders, generators, evaluators) over Document Stores for RAG, se
  name: Haystack Framework (Open Source)
  slug: haystack-framework
- description: Hayhooks turns a Haystack pipeline into a self-hosted REST API (and optional MCP server) with one command, auto-generating OpenAPI/Swagger docs and HTTP run endpoints. The deployed surface is generate
  name: Hayhooks REST Deployment
  slug: hayhooks-rest-deployment
- description: Upload, list, delete, and annotate files; manage upload sessions.
  name: Haystack / deepset Files API
  slug: haystack-ai-files-api
- description: Create, list, deploy, and undeploy Haystack pipelines.
  name: Haystack / deepset Pipelines API
  slug: haystack-ai-pipelines-api
- description: Run queries against deployed pipelines.
  name: Haystack / deepset Search API
  slug: haystack-ai-search-api
- description: Manage workspaces that isolate pipelines and data.
  name: Haystack / deepset Workspaces API
  slug: haystack-ai-workspaces-api
artifact_total: 13
collections:
- collection_type: open
  name: deepset Cloud API (deepset AI Platform)
  slug: open-haystack-ai
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/haystack-ai-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/haystack-ai-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/haystack-ai-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/deepset-ai
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/deepset
- group: company
  title: ''
  type: Website
  url: https://haystack.deepset.ai
- group: docs
  title: ''
  type: Documentation
  url: https://docs.haystack.deepset.ai/docs/intro
- group: commercial
  title: ''
  type: Plans
  url: plans/haystack-ai-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/haystack-ai-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/haystack-ai-finops.yml
- group: company
  title: ''
  type: Blog
  url: https://haystack.deepset.ai/blog
created: '2026-06-20'
description: Haystack is deepset's open-source Python framework for building context-engineered, production-ready LLM applications - modular Pipelines and agent workflows assembled from 100+ Components and document stores for RAG, semantic search, and agents. Haystack pipelines deploy as REST services via Hayhooks, and the commercial deepset AI Platform (deepset Cloud) exposes a hosted REST API at api.cloud.deepset.ai for pipelines, search, files, and workspaces.
finops:
- name: Haystack Ai Finops
  service_category: AI and Machine Learning
  slug: haystack-ai-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/haystack-ai.png
layout: provider
modified: '2026-06-20'
name: Haystack / deepset
nav: Providers
network: true
overview: 'Haystack / deepset publishes 4 APIs on the [APIs.io](https://apis.io/) network, including Files API, Pipelines API, Search API, and 1 more. Tagged areas include AI, LLM, RAG, Open Source, and Orchestration.


  Haystack / deepset''s developer surface includes authentication, documentation, engineering blog, and 8 more developer resources.'
plans:
- name: Haystack Ai Plans Pricing
  plan_count: 2
  slug: haystack-ai-plans-pricing
random_paper: 32
rate_limits:
- limit_count: 5
  name: Haystack Ai Rate Limits
  slug: haystack-ai-rate-limits
score:
  band: thin
  composite: 34.4
  delta: 0.0
  facets:
    commercial_clarity: 28.9
    contract_quality: 50.9
    developer_ergonomics: 21.7
    discoverability: 67.5
    governance: 0.0
    operational_transparency: 36.8
  previous_composite: 34.4
  schema_version: 0.5
  scored_at: '2026-07-23'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/haystack-ai/refs/heads/main/screenshots/haystack-ai-2026-06-20T182543.png
security:
- kind: authentication
  name: Haystack Ai Authentication
  slug: haystack-ai-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Haystack Ai Domain Security
  slug: haystack-ai-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: haystack-ai
tags:
- AI
- LLM
- RAG
- Open Source
- Orchestration
website: https://haystack.deepset.ai
---
