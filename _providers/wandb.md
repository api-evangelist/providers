---
access_model:
  confidence: medium
  label: Free · Self-serve signup
  onboarding: self-serve
  pricing: free
  public: false
  source:
  - plans
  - authentication
  - security
  trial: false
  try_now: true
agentic_access:
- acting_count: 27
  human_in_the_loop: 0
  name: Wandb Agentic Access
  operation_count: 29
  slug: wandb-agentic-access
  summary_line: 29 operations · 27 acting
api_count: 1
apis:
- description: Primary programmatic surface for W&B Models. The Python public API (wandb.Api) speaks GraphQL against api.wandb.ai to query and manage runs, projects, sweeps, artifacts, registries, reports, automatio
  name: W&B GraphQL API
  slug: graphql
- description: REST endpoints exposed by the W&B platform for ingestion, artifact upload, file storage, and integration callbacks. Used internally by the wandb SDK and CLI, and available to customers for direct inte
  name: W&B REST API
  slug: rest
- description: LLM observability and evaluation platform providing tracing, output evaluation, cost estimation, prompt playground, guardrails, and a Python and TypeScript SDK. Traces and evaluations are persisted to
  name: W&B Weave (LLM Observability)
  slug: weave
- description: Official Python SDK (wandb) for logging runs, metrics, gradients, media, and artifacts; running sweeps; and interacting with the W&B public API. Apache-2.0 licensed.
  name: W&B Python SDK
  slug: python-sdk
- description: Command-line interface bundled with the wandb Python package for login, sweep orchestration, artifact management, and local agent execution.
  name: W&B CLI
  slug: cli
- description: OpenAI-compatible inference API for hosted open-source foundation models, running on CoreWeave GPU infrastructure with native Weave tracing and usage tracking.
  name: W&B Serverless Inference (CoreWeave)
  slug: serverless-inference
- description: Outbound webhook integrations driven by W&B automations. Customers register endpoints that W&B POSTs to when configured events fire (artifact created, alias added, run state changes, registry events).
  name: W&B Webhook Automations
  slug: webhook-automations
- baseURL: https://api.wandb.ai/graphql
  baseurl_source: declared
  description: The Calls API from Weights and Biases — 8 operation(s) for calls.
  name: Weights and Biases Calls API
  slug: wandb-calls-api
- baseURL: https://api.wandb.ai/graphql
  baseurl_source: declared
  description: The Costs API from Weights and Biases — 3 operation(s) for costs.
  name: Weights and Biases Costs API
  slug: wandb-costs-api
- baseURL: https://api.wandb.ai/graphql
  baseurl_source: declared
  description: The Feedback API from Weights and Biases — 4 operation(s) for feedback.
  name: Weights and Biases Feedback API
  slug: wandb-feedback-api
- baseURL: https://api.wandb.ai/graphql
  baseurl_source: declared
  description: The Files API from Weights and Biases — 2 operation(s) for files.
  name: Weights and Biases Files API
  slug: wandb-files-api
- baseURL: https://api.wandb.ai/graphql
  baseurl_source: declared
  description: The Objects API from Weights and Biases — 4 operation(s) for objects.
  name: Weights and Biases Objects API
  slug: wandb-objects-api
- baseURL: https://api.wandb.ai/graphql
  baseurl_source: declared
  description: The Refs API from Weights and Biases — 1 operation(s) for refs.
  name: Weights and Biases Refs API
  slug: wandb-refs-api
- baseURL: https://api.wandb.ai/graphql
  baseurl_source: declared
  description: The Service API from Weights and Biases — 2 operation(s) for service.
  name: Weights and Biases Service API
  slug: wandb-service-api
- baseURL: https://api.wandb.ai/graphql
  baseurl_source: declared
  description: The Table API from Weights and Biases — 1 operation(s) for table.
  name: Weights and Biases Table API
  slug: wandb-table-api
- baseURL: https://api.wandb.ai/graphql
  baseurl_source: declared
  description: The Tables API from Weights and Biases — 4 operation(s) for tables.
  name: Weights and Biases Tables API
  slug: wandb-tables-api
artifact_total: 35
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Fast Calls API
  slug: open-wandb-calls-api
- collection_type: open
  name: Fast Calls Costs API
  slug: open-wandb-costs-api
- collection_type: open
  name: Fast Calls Feedback API
  slug: open-wandb-feedback-api
- collection_type: open
  name: Fast Calls Files API
  slug: open-wandb-files-api
- collection_type: open
  name: Fast Calls Objects API
  slug: open-wandb-objects-api
- collection_type: open
  name: Fast Calls Refs API
  slug: open-wandb-refs-api
- collection_type: open
  name: Fast Calls Service API
  slug: open-wandb-service-api
- collection_type: open
  name: Fast Calls Table API
  slug: open-wandb-table-api
- collection_type: open
  name: Fast Calls Tables API
  slug: open-wandb-tables-api
- collection_type: open
  name: FastAPI
  slug: open-wandb
common:
- group: other
  title: ''
  type: ParentCompany
  url: https://apis.io/providers/coreweave/
- group: operate
  title: ''
  type: IssueTracker
  url: https://github.com/wandb/weave/issues
- group: operate
  title: ''
  type: Releases
  url: https://github.com/wandb/weave/releases
- group: auth
  title: ''
  type: SecurityPolicy
  url: https://github.com/wandb/weave/blob/master/SECURITY.md
- group: docs
  title: ''
  type: ContributionGuide
  url: https://github.com/wandb/weave/blob/master/CONTRIBUTING.md
- group: commercial
  title: ''
  type: License
  url: https://github.com/wandb/weave/blob/master/LICENSE
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/wandb-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/wandb-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/wandb-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/wandb-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/wandbai
- group: company
  title: ''
  type: Website
  url: https://wandb.ai/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.wandb.ai/
- group: build
  title: ''
  type: GitHub
  url: https://github.com/wandb
- group: other
  title: ''
  type: Weave
  url: https://weave-docs.wandb.ai/
- group: commercial
  title: ''
  type: Pricing
  url: https://wandb.ai/site/pricing/
- group: other
  title: ''
  type: Parent
  url: https://www.coreweave.com/
- group: commercial
  title: ''
  type: Plans
  url: plans/wandb-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/wandb-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/wandb-finops.yml
- group: agent
  title: ''
  type: LlmsText
  url: https://docs.wandb.ai/llms.txt
- group: company
  title: ''
  type: Blog
  url: https://wandb.ai/fully-connected
created: '2026-05-23'
description: 'Weights and Biases (W&B) is an MLOps and AI developer platform covering the full lifecycle of model and LLM application development. W&B Models provides experiment tracking, hyperparameter sweeps, artifacts, model registry, and reports. W&B Weave provides LLM tracing, evaluation, cost tracking, guardrails, and prompt/playground tooling for production AI applications. Three CoreWeave- powered serverless capabilities sit alongside the core platform: Serverless Inference (OpenAI-compatible API for open-source foundation models), Serverless RL (post-training with ART/RULER), and Serverless Sandboxes (isolated code execution). The platform exposes a Python SDK, a public REST API, and a GraphQL API at api.wandb.ai, with CLI tooling and webhook integrations. W&B was acquired by CoreWeave in 2025.'
finops:
- name: Wandb Finops
  service_category: API
  slug: wandb-finops
graphqls:
- description: Primary programmatic surface for W&B Models. The Python public API (wandb.Api) speaks GraphQL against api.wandb.ai to query and manage runs, projects, sweeps, artifacts, registries, reports, automatio
  name: Weights and Biases GraphQL API
  slug: wandb-graphql
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/wandb.png
layout: provider
modified: '2026-05-23'
name: Weights and Biases
nav: Providers
network: true
overview: 'Weights and Biases publishes 9 APIs on the [APIs.io](https://apis.io/) network, including Calls API, Costs API, Feedback API, and 6 more. Tagged areas include MLOps, Experiment Tracking, LLM Observability, Model Registry, and AI Platform.


  Weights and Biases'' developer surface includes authentication, documentation, GitHub presence, pricing, engineering blog, and 17 more developer resources.'
plans:
- name: Wandb Plans Pricing
  plan_count: 1
  slug: wandb-plans-pricing
random_paper: 20
rate_limits:
- limit_count: 2
  name: Wandb Rate Limits
  slug: wandb-rate-limits
screenshot: https://raw.githubusercontent.com/api-evangelist/wandb/refs/heads/main/screenshots/wandb-2026-06-20T201222.png
security:
- kind: authentication
  name: Wandb Authentication
  slug: wandb-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Wandb Domain Security
  slug: wandb-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Wandb Vulnerability Disclosure
  slug: wandb-vulnerability-disclosure
  summary_line: disclosure policy published
slug: wandb
tags:
- MLOps
- Experiment Tracking
- LLM Observability
- Model Registry
- AI Platform
- Evaluation
- Tracing
website: https://wandb.ai/
---
