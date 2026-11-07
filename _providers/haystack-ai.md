---
access_model:
  confidence: medium
  gated: none
  gated_source:
  - onboarding
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
    agent_card: false
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: verified
    mcp_tool_quality: three_quarters
    openapi_examples: partial
    operation_distinctiveness: false
    pagination_ratio: false
    protected_resource_metadata: false
    rate_limit_signal: derived
    reversibility_documented: verified
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 38.5
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 21
  human_in_the_loop: 0
  name: Haystack Ai Agentic Access
  operation_count: 37
  slug: haystack-ai-agentic-access
  summary_line: 37 operations · 21 acting
api_count: 5
apis:
- description: Apache-2.0 licensed Python framework for composable LLM orchestration. Build modular Pipelines from Components (retrievers, routers, embedders, generators, evaluators) over Document Stores for RAG, se
  name: Haystack Framework (Open Source)
  slug: haystack-framework
- description: Hayhooks turns a Haystack pipeline into a self-hosted REST API (and optional MCP server) with one command, auto-generating OpenAPI/Swagger docs and HTTP run endpoints. The deployed surface is generate
  name: Hayhooks REST Deployment
  slug: hayhooks-rest-deployment
- baseURL: https://github.com/deepset-ai/haystack
  baseurl_source: declared
  description: Upload, list, delete, and annotate files; manage upload sessions.
  name: Haystack / deepset Files API
  slug: haystack-ai-files-api
- baseURL: https://github.com/deepset-ai/haystack
  baseurl_source: declared
  description: Create, list, deploy, and undeploy Haystack pipelines.
  name: Haystack / deepset Pipelines API
  slug: haystack-ai-pipelines-api
- baseURL: https://github.com/deepset-ai/haystack
  baseurl_source: declared
  description: Run queries against deployed pipelines.
  name: Haystack / deepset Search API
  slug: haystack-ai-search-api
- baseURL: https://github.com/deepset-ai/haystack
  baseurl_source: declared
  description: Manage workspaces that isolate pipelines and data.
  name: Haystack / deepset Workspaces API
  slug: haystack-ai-workspaces-api
- baseURL: https://github.com/deepset-ai/haystack
  baseurl_source: declared
  description: The config API from Haystack / deepset — 4 operation(s) for config.
  name: Haystack / deepset Config API
  slug: haystack-ai-config-api
- baseURL: https://github.com/deepset-ai/haystack
  baseurl_source: declared
  description: The dashboard API from Haystack / deepset — 5 operation(s) for dashboard.
  name: Haystack / deepset Dashboard API
  slug: haystack-ai-dashboard-api
- baseURL: https://github.com/deepset-ai/haystack
  baseurl_source: declared
  description: The openai API from Haystack / deepset — 8 operation(s) for openai.
  name: Haystack / deepset Openai API
  slug: haystack-ai-openai-api
- baseURL: https://github.com/deepset-ai/haystack
  baseurl_source: declared
  description: The status API from Haystack / deepset — 2 operation(s) for status.
  name: Haystack / deepset Status API
  slug: haystack-ai-status-api
artifact_total: 23
collections:
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
- group: other
  href: https://artifacts.apis.io/haystack-ai/capabilities/haystack-ai-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/haystack-ai-capability-edges.yml
- group: agent
  href: https://artifacts.apis.io/haystack-ai/agentic-access/haystack-ai-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/haystack-ai-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/haystack-ai/security/haystack-ai-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/haystack-ai-domain-security.yml
- group: auth
  href: https://artifacts.apis.io/haystack-ai/authentication/haystack-ai-authentication.yml
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
  href: https://artifacts.apis.io/haystack-ai/plans/haystack-ai-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/haystack-ai-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/haystack-ai/rate-limits/haystack-ai-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/haystack-ai-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/haystack-ai/finops/haystack-ai-finops.yml
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
- has_sources: true
  method: generated
  name: Haystack Ai Finops
  primary_unit: ''
  service_category: AI and Machine Learning
  slug: haystack-ai-finops
  template: false
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/haystack-ai.png
layout: provider
mcp_servers:
- description: Remote MCP server at docs.haystack.deepset.ai over HTTP.
  name: Haystack / deepset MCP Server
  slug: haystack-ai
modified: '2026-08-08'
name: Haystack / deepset
nav: Providers
network: true
overview: 'Haystack / deepset publishes 10 API contracts indexed on the [APIs.io](https://apis.io/) network, including Files API, Pipelines API, Search API, and 7 more. Tagged areas include Artificial Intelligence, LLM, RAG, Open Source, and Orchestration.


  The Haystack / deepset catalog on APIs.io includes 1 Spectral governance ruleset.


  Haystack / deepset''s developer surface includes authentication, documentation, engineering blog, and 10 more developer resources.'
plans:
- name: Haystack Ai Plans Pricing
  plan_count: 2
  slug: haystack-ai-plans-pricing
random_paper: 23
rate_limits:
- limit_count: 5
  name: Haystack Ai Rate Limits
  slug: haystack-ai-rate-limits
rules:
- authorship: generated
  effective_rule_count: 105
  extends:
  - spectral:oas
  name: Haystack / deepset API Rules
  rule_count: 64
  severity_counts:
    error: 37
    hint: 0
    info: 8
    warn: 19
  slug: haystack-ai-rules
score:
  band: thin
  composite: 32.5
  coverage:
    artifact_dirs: 19
    catalog_earned: 49.5
    catalog_earned_first_party: 0.0
    catalog_gap: 65.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.1
  facets:
    access_clarity: 5.3
    contract_governance: 13.6
    contract_quality: 47.4
    developer_ergonomics: 44.0
    discoverability: 80.0
    operational_transparency: 10.5
  previous_composite: 32.4
  provenance:
    agentic_access: derived
    contracts:
      callable: 91.1
      derived: 0
      marker_coverage: 8.9
      total: 45
    mcp: first-party
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 10.9
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 11.1
screenshot: https://apis.io/screenshots/haystack-ai/haystack-ai-2026-06-20T182543.png
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
- Artificial Intelligence
- LLM
- RAG
- Open Source
- Orchestration
website: https://haystack.deepset.ai
---
