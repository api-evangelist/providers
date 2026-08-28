---
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: documented
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 25.9
  scored_at: '2026-08-26'
api_count: 1
apis:
- description: OpenAI-compatible inference API for CompactifAI's compressed and third-party large language models. Covers chat completions, text completions, the Responses API, batch jobs, file upload, model discove
  name: CompactifAI API
  slug: multiverse-computing-compactifai-api
artifact_total: 5
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/multiverse-computing-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/multiverse-computing-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://multiversecomputing.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.compactif.ai/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.compactif.ai/introduction/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.compactif.ai/api_reference/
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.compactif.ai/quickstart/
- group: operate
  title: ''
  type: Support
  url: https://docs.compactif.ai/support-contact/
- group: operate
  title: ''
  type: Community
  url: https://discord.com/invite/KfqDt3En
- group: company
  title: ''
  type: Blog
  url: https://multiversecomputing.com/resources
- group: commercial
  title: ''
  type: Pricing
  url: https://docs.compactif.ai/pricing/
- group: start
  title: ''
  type: SignUp
  url: https://auth.multiverseapp.ai/sign-up?redirect_url=https%3A%2F%2Fdashboard.compactif.ai%2F
- group: start
  title: ''
  type: Login
  url: https://dashboard.compactif.ai/
- group: commercial
  title: ''
  type: TermsOfUse
  url: https://multiversecomputing.com/legal-notice
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://multiversecomputing.com/privacy-policy
- group: operate
  title: ''
  type: StatusPage
  url: https://status.compactif.ai/
- group: build
  title: ''
  type: Packages
  url: packages/multiverse-computing-packages.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/multiverse-computing-llms.txt
- group: other
  title: ''
  type: Overlay
  url: overlays/multiverse-computing-compactifai-overlay.yaml
- group: design
  title: ''
  type: Conformance
  url: conformance/multiverse-computing-conformance.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/multiverse-computing-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/multiverse-computing-lifecycle.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/multiverse-computing-conventions.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/multiverse-computing-changelog.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/multiverse-computing-data-model.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/multiverse-computing-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/multiverse-computing-rate-limits.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: operate
  title: ''
  type: ReleaseNotes
  url: https://docs.compactif.ai/changelog/
- group: build
  title: ''
  type: Examples
  url: examples/multiverse-computing-compactifai-examples.yml
- group: docs
  title: ''
  type: OpenAPI
  url: openapi/multiverse-computing-compactifai-openapi.yml
created: '2026-08-26'
description: Multiverse Computing, S.L. is a Donostia-San Sebastian (Spain) quantum- and AI-software company whose commercial developer surface is the CompactifAI API — an OpenAI-compatible LLM inference service serving tensor-network-compressed versions of frontier open models (Hypernova 60B, Carina 60B, Mistral Small 3.1 Slim, Whisper Large V3 Turbo Slim) alongside uncompressed third-party models (GPT-OSS 120B, GLM 5.1/5.2, Quasar 438B, Qwen 3.6 27B, Nemotron 3 Nano Omni). The API is published at api.compactif.ai with regional EU and US endpoints, documented at docs.compactif.ai, billed pay-as-you-go per million tokens, and also sold through the AWS Marketplace. The company additionally sells Singularity, a quantum and quantum-inspired optimization product for finance, energy and manufacturing, which has no public developer documentation.
image: https://multiversecomputing.com/icon.png
layout: provider
modified: '2026-08-26'
name: Multiverse Computing
nav: Providers
network: true
overview: 'Multiverse Computing publishes 1 API on the [APIs.io](https://apis.io/) network: CompactifAI API. Tagged areas include Artificial Intelligence, Machine Learning, LLM Inference, Model Compression, and Quantum Computing.


  Multiverse Computing''s developer surface includes authentication, documentation, API reference, getting-started guide, support, engineering blog, pricing, and 24 more developer resources.'
plans:
- name: Multiverse Computing Plans Pricing
  plan_count: 2
  slug: multiverse-computing-plans-pricing
random_paper: 10
rate_limits:
- limit_count: 0
  name: Multiverse Computing Rate Limits
  slug: multiverse-computing-rate-limits
score:
  band: developing
  composite: 51.6
  facets:
    access_clarity: 59.2
    commercial_clarity: 59.2
    contract_governance: 16.7
    contract_quality: 59.9
    developer_ergonomics: 58.9
    discoverability: 68.5
    governance: 16.7
    operational_transparency: 31.6
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 1
    mcp: derived
    skills: derived
  schema_version: 0.15.0
  scored_at: '2026-08-26'
security:
- kind: authentication
  name: Multiverse Computing Authentication
  slug: multiverse-computing-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Multiverse Computing Domain Security
  slug: multiverse-computing-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: multiverse-computing
tags:
- Artificial Intelligence
- Machine Learning
- LLM Inference
- Model Compression
- Quantum Computing
- Speech to Text
- OpenAI Compatible
- Developer Tools
- Spain
- Company
website: https://multiversecomputing.com/
---
