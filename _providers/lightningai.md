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
    agent_skills: true
    agentic_access: false
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
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 15.8
  scored_at: '2026-08-19'
api_count: 2
apis:
- description: OpenAI-compatible LLM gateway. Call hosted models from OpenAI, Anthropic, Google and open-weights providers through a single Bearer-authenticated endpoint with one bill, using provider/model names suc
  name: Lightning AI Model APIs
  slug: model-apis
- description: The v1 REST surface behind the Lightning AI platform — Studios, Jobs, multi-machine training, Deployments, Sandboxes, teamspaces, memberships, datasets and the model checkpoint registry. Authenticated
  name: Lightning AI Platform API
  slug: platform-api
artifact_total: 5
common:
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
  url: https://lightning.ai/docs
- group: docs
  title: ''
  type: APIReference
  url: https://lightning.ai/docs/overview/sdk-reference
- group: start
  title: ''
  type: GettingStarted
  url: https://lightning.ai/docs/platform/overview/getting-started
- group: company
  title: ''
  type: Blog
  url: https://lightning.ai/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Lightning-AI
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.grid.ai/privacy-policy/
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
  url: llms/lightningai-llms.txt
- group: build
  title: ''
  type: Packages
  url: packages/lightningai-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/lightningai-packages.yml
- group: build
  title: ''
  type: CLI
  url: cli/lightningai-cli.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/lightningai-well-known.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/lightningai-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/lightningai-conventions.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/lightningai-rate-limits.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/lightningai-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/lightningai-lifecycle.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/lightningai-sandbox.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/lightningai-domain-security.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-07-17'
description: Lightning AI is an AI development cloud from the creators of PyTorch Lightning. The platform bundles browser-based GPU Studios, batch and multi-node training jobs, autoscaled model and container deployments, ephemeral code-execution Sandboxes, teamspace data and model registries, and an OpenAI-compatible LLM gateway (Model APIs) that fronts hosted models from OpenAI, Anthropic, Google and open-weights providers behind one key and one bill. Developers reach the platform through the lightning-sdk Python package and its lightning CLI, an @lightningai/sdk TypeScript SDK for Sandboxes, and a v1 REST surface reachable with the `lightning api` escape hatch. Lightning AI also publishes an llms.txt, a docs manifest registry, and six first-party Agent Skills in SKILL.md format for coding agents.
image: https://avatars.githubusercontent.com/u/58386951?s=200&v=4
layout: provider
modified: '2026-07-19'
name: Lightning.AI
nav: Providers
network: true
overview: 'Lightning.AI publishes 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Ai Infrastructure, Artificial Intelligence, Machine Learning, and GPU Cloud.


  Lightning.AI''s developer surface includes documentation, API reference, getting-started guide, engineering blog, CLI, authentication, sandbox, and 16 more developer resources.'
random_paper: 11
rate_limits:
- limit_count: 0
  name: Lightningai Rate Limits
  slug: lightningai-rate-limits
score:
  band: emerging
  composite: 22.4
  delta: -7.9
  facets:
    access_clarity: 10.5
    commercial_clarity: 10.5
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 40.5
    discoverability: 75.9
    governance: 18.2
    operational_transparency: 18.4
  previous_composite: 30.3
  provenance:
    conformance: first-party
    skills: first-party
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: falling
screenshot: https://raw.githubusercontent.com/api-evangelist/lightningai/refs/heads/main/screenshots/lightningai-2026-07-25T225125.png
security:
- kind: authentication
  name: Lightningai Authentication
  slug: lightningai-authentication
  summary_line: http-basic/http-bearer · 2 schemes
- kind: domain-security
  name: Lightningai Domain Security
  slug: lightningai-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: lightningai
tags:
- Company
- Ai Infrastructure
- Artificial Intelligence
- Machine Learning
- GPU Cloud
- Model Inference
- LLM Gateway
- Developer Tools
- MLOps
- Deployment
website: https://lightning.ai/
---
