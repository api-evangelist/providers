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
    agentic_access: false
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: documented
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 15.8
  scored_at: '2026-07-28'
api_count: 2
apis:
- description: 'The Lightning AI control-plane API used by the lightning-sdk Python SDK, the @lightningai/sdk JavaScript SDK and the lightning CLI to programmatically manage platform resources: Studios, Jobs, Deploym'
  name: Lightning AI Platform API
  slug: platform-api
- description: Hosted inference API that serves frontier and open models behind a Lightning API key, billed per token with a free monthly token allowance. Accessible through the litai Python client and through OpenA
  name: Lightning AI Model APIs
  slug: model-apis
artifact_total: 6
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/lightning-ai-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://lightning.ai/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://lightning.ai/docs/platform/developers
- group: docs
  title: ''
  type: Documentation
  url: https://lightning.ai/docs/
- group: docs
  title: ''
  type: APIReference
  url: https://lightning.ai/docs/platform/developers/sdk
- group: start
  title: ''
  type: GettingStarted
  url: https://lightning.ai/docs/platform/overview/getting-started
- group: start
  title: ''
  type: Quickstart
  url: https://lightning.ai/docs/platform/overview/quick-start
- group: operate
  title: ''
  type: Support
  url: https://lightning.ai/community/
- group: company
  title: ''
  type: Blog
  url: https://lightning.ai/blog/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Lightning-AI
- group: commercial
  title: ''
  type: Pricing
  url: https://lightning.ai/pricing/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://lightning.ai/policies/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://lightning.ai/policies/
- group: operate
  title: ''
  type: ChangeLog
  url: https://lightning.ai/pages/releases/
- group: other
  title: ''
  type: OpenSource
  url: https://lightning.ai/open-source/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.lightning.ai/
- group: auth
  title: ''
  type: Compliance
  url: https://lightning.ai/docs/platform/security/compliance
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/lightning-ai-llms.txt
- group: build
  title: ''
  type: Packages
  url: packages/lightning-ai-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/lightning-ai-packages.yml
- group: build
  title: ''
  type: CLI
  url: cli/lightning-ai-cli.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/lightning-ai-sandbox.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/lightning-ai-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/lightning-ai-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/lightning-ai-error-codes.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/lightning-ai-data-model.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/lightning-ai-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/lightning-ai-conformance.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/lightning-ai-rate-limits.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/lightning-ai-plans.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/lightning-ai-changelog.yml
created: '2026-07-17'
description: Lightning AI is an AI development platform from the team behind PyTorch Lightning. It provides cloud AI Studios (persistent GPU-backed development workspaces), ephemeral Sandboxes for running untrusted or agent-generated code, multi-node training and finetuning, batch and real-time inference deployments, and hosted Model APIs that expose frontier LLMs behind an API key. The platform is driven programmatically through the lightning-sdk Python SDK, the @lightningai/sdk JavaScript Sandbox SDK, and the lightning CLI, and is backed by a family of widely adopted open-source libraries including PyTorch Lightning, Lightning Fabric, LitServe, LitData, TorchMetrics and Thunder. Lightning AI runs as a fully managed cloud or inside a customer VPC (bring your own cloud), and is SOC 2 Type II and HIPAA certified.
image: https://avatars.githubusercontent.com/u/58386951?v=4
layout: provider
modified: '2026-07-19'
name: Lightning AI
nav: Providers
network: true
overview: 'Lightning AI publishes 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Ai Ml, Machine Learning, GPU Cloud, and Model Inference.


  Lightning AI''s developer surface includes documentation, API reference, getting-started guide, quickstart, support, engineering blog, pricing, and 24 more developer resources.'
plans:
- name: Lightning Ai Plans
  plan_count: 4
  slug: lightning-ai-plans
random_paper: 26
rate_limits:
- limit_count: 0
  name: Lightning Ai Rate Limits
  slug: lightning-ai-rate-limits
score:
  band: developing
  composite: 43.5
  delta: 0.9
  facets:
    commercial_clarity: 71.1
    contract_quality: 0.0
    developer_ergonomics: 71.7
    discoverability: 87.0
    governance: 12.5
    operational_transparency: 36.8
  previous_composite: 42.6
  provenance:
    conformance: first-party
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/lightning-ai/refs/heads/main/screenshots/lightning-ai-2026-07-25T225123.png
security:
- kind: authentication
  name: Lightning Ai Authentication
  slug: lightning-ai-authentication
  summary_line: apiKey · 3 schemes
- kind: domain-security
  name: Lightning Ai Domain Security
  slug: lightning-ai-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: lightning-ai
tags:
- Company
- Ai Ml
- Machine Learning
- GPU Cloud
- Model Inference
- Model Training
- Developer Platform
- Sandboxes
- LLM APIs
- Open Source
website: https://lightning.ai/
---
