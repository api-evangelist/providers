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
  scored_at: '2026-08-19'
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
artifact_total: 19
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: deepset Cloud API (deepset AI Platform) Files API
  slug: open-haystack-ai-files-api
- collection_type: open
  name: deepset Cloud API (deepset AI Platform) Files Pipelines API
  slug: open-haystack-ai-pipelines-api
- collection_type: open
  name: deepset Cloud API (deepset AI Platform) Files Search API
  slug: open-haystack-ai-search-api
- collection_type: open
  name: deepset Cloud API (deepset AI Platform) Files Workspaces API
  slug: open-haystack-ai-workspaces-api
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
- group: agent
  title: ''
  type: LlmsText
  url: https://docs.haystack.deepset.ai/llms.txt
created: '2026-06-20'
description: Haystack is deepset's open-source Python framework for building context-engineered, production-ready LLM applications - modular Pipelines and agent workflows assembled from 100+ Components and document stores for RAG, semantic search, and agents. Haystack pipelines deploy as REST services via Hayhooks, and the commercial deepset AI Platform (deepset Cloud) exposes a hosted REST API at api.cloud.deepset.ai for pipelines, search, files, and workspaces.
finops:
- name: Haystack Ai Finops
  service_category: AI and Machine Learning
  slug: haystack-ai-finops
graphqls:
- description: Haystack is an open-source NLP framework. The Deepset Cloud API covers pipeline management, document store operations, querying, user management, evaluation sets, and deployment of NLP search and QA p
  name: Haystack GraphQL API
  slug: haystack-ai-graphql
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/haystack-ai.png
layout: provider
modified: '2026-08-08'
name: Haystack / deepset
nav: Providers
network: true
overview: 'Haystack / deepset publishes 4 APIs on the [APIs.io](https://apis.io/) network, including Files API, Pipelines API, Search API, and 1 more. Tagged areas include AI, LLM, RAG, Open Source, and Orchestration.


  Haystack / deepset''s developer surface includes authentication, documentation, engineering blog, and 9 more developer resources.'
plans:
- name: Haystack Ai Plans Pricing
  plan_count: 2
  slug: haystack-ai-plans-pricing
random_paper: 60
rate_limits:
- limit_count: 5
  name: Haystack Ai Rate Limits
  slug: haystack-ai-rate-limits
score:
  band: thin
  composite: 36.8
  delta: -0.7
  facets:
    access_clarity: 28.9
    commercial_clarity: 28.9
    contract_governance: 0.0
    contract_quality: 54.6
    developer_ergonomics: 23.8
    discoverability: 81.5
    governance: 0.0
    operational_transparency: 34.2
  previous_composite: 37.5
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 4
  schema_version: 0.12.0
  scored_at: '2026-08-19'
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
