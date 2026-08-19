---
access_model:
  confidence: medium
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 33.5
  scored_at: '2026-08-19'
agentic_access:
- acting_count: 3
  human_in_the_loop: 0
  name: Recursal Ai Inc Agentic Access
  operation_count: 5
  slug: recursal-ai-inc-agentic-access
  summary_line: 5 operations · 3 acting
api_count: 3
apis:
- description: Plan and concurrency information
  name: Recursal AI, Inc. Account API
  slug: recursal-ai-inc-account-api
- description: OpenAI-compatible chat and text completion generation
  name: Recursal AI, Inc. Chat API
  slug: recursal-ai-inc-chat-api
- description: Model catalog and metadata
  name: Recursal AI, Inc. Models API
  slug: recursal-ai-inc-models-api
artifact_total: 12
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Featherless AI Serverless Inference Account API
  slug: open-recursal-ai-inc-account-api
- collection_type: open
  name: Featherless AI Serverless Inference Account Chat API
  slug: open-recursal-ai-inc-chat-api
- collection_type: open
  name: Featherless AI Serverless Inference Account Models API
  slug: open-recursal-ai-inc-models-api
common:
- group: other
  title: ''
  type: Overlay
  url: overlays/recursal-ai-inc-featherless-overlay.yaml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/recursal-ai-inc-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://featherless.ai
- group: company
  title: ''
  type: CompanyWebsite
  url: https://recursal.ai
- group: start
  title: ''
  type: DeveloperPortal
  url: https://featherless.ai/docs/overview
- group: docs
  title: ''
  type: Documentation
  url: https://featherless.ai/docs/overview
- group: docs
  title: ''
  type: APIReference
  url: https://featherless.ai/docs/api-overview-and-common-options
- group: start
  title: ''
  type: GettingStarted
  url: https://featherless.ai/docs/getting-started
- group: start
  title: ''
  type: Quickstart
  url: https://featherless.ai/docs/quickstart-guide
- group: commercial
  title: ''
  type: Pricing
  url: https://featherless.ai/#pricing
- group: start
  title: ''
  type: SignUp
  url: https://featherless.ai/register
- group: commercial
  title: ''
  type: TermsOfService
  url: https://featherless.ai/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://featherless.ai/privacy
- group: company
  title: ''
  type: Blog
  url: https://featherless.ai/blog
- group: operate
  title: ''
  type: Support
  url: https://featherless.ai/discord
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/recursal
- group: operate
  title: ''
  type: StatusPage
  url: https://featherless.ai/status
- group: other
  title: ''
  type: Models
  url: https://featherless.ai/models
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/recursal-ai-inc-llms.txt
- group: auth
  title: ''
  type: Authentication
  url: authentication/recursal-ai-inc-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/recursal-ai-inc-conventions.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/recursal-ai-inc-rate-limits.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/recursal-ai-inc-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/recursal-ai-inc-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/recursal-ai-inc-conformance.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/recursal-ai-inc-data-model.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/recursal-ai-inc-mcp.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/recursal-ai-inc-agentic-access.yml
created: '2026-07-17'
description: Recursal AI, Inc. operates Featherless AI, a serverless AI inference platform that provides unified, OpenAI-compatible API access to tens of thousands of open-weight large language models sourced from Hugging Face. A single API key and base URL (https://api.featherless.ai/v1) give developers drop-in access to models ranging from small 7B instruct models to 405B-plus parameter models, under flat-rate, concurrency-based subscriptions with unlimited monthly requests and a no-logging policy on prompts and chat history. The platform is built by researchers who contribute to RWKV, a Linux Foundation project, and has raised a $20M Series A. Recursal AI was surfaced as a portfolio company of 500 Global and enriched by the API Evangelist pipeline.
image: https://cdn.prod.website-files.com/6979c6c70c21b50639123793/69a171cf1a87499ba814df9c_OG%20Image_%20Home.png
layout: provider
mcp_servers:
- description: ''
  name: recursal-ai-inc-mcp.yml
  slug: recursal-ai-inc-mcpyml
modified: '2026-07-21'
name: Recursal AI, Inc.
nav: Providers
network: true
overview: 'Recursal AI, Inc. publishes 3 APIs on the [APIs.io](https://apis.io/) network: Account API, Chat API, and Models API. Tagged areas include Company, Artificial Intelligence, Machine Learning, LLM, and Inference.


  Recursal AI, Inc.''s developer surface includes documentation, API reference, getting-started guide, quickstart, pricing, signup flow, engineering blog, and 22 more developer resources.'
random_paper: 130
rate_limits:
- limit_count: 0
  name: Recursal Ai Inc Rate Limits
  slug: recursal-ai-inc-rate-limits
score:
  band: developing
  composite: 47.4
  delta: 0.1
  facets:
    access_clarity: 44.7
    commercial_clarity: 44.7
    contract_governance: 16.7
    contract_quality: 56.6
    developer_ergonomics: 58.9
    discoverability: 81.5
    governance: 16.7
    operational_transparency: 18.4
  previous_composite: 47.3
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 3
    mcp: derived
    skills: derived
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/recursal-ai-inc/refs/heads/main/screenshots/recursal-ai-inc-2026-08-17T081505.png
security:
- kind: authentication
  name: Recursal Ai Inc Authentication
  slug: recursal-ai-inc-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Recursal Ai Inc Domain Security
  slug: recursal-ai-inc-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: recursal-ai-inc
tags:
- Company
- Artificial Intelligence
- Machine Learning
- LLM
- Inference
- Serverless
- Generative AI
- Developer Tools
- OpenAI Compatible
- RWKV
website: https://featherless.ai
---
