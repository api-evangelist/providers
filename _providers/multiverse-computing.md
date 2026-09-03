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
  - rate-limits
  - security
  trial: false
  try_now: true
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
  scored_at: '2026-09-02'
api_count: 2
apis:
- baseURL: https://api.compactif.ai
  baseurl_source: declared
  description: The audio API from Multiverse Computing — 1 operation(s) for audio.
  name: Multiverse Computing Audio API
  slug: multiverse-computing-audio-api
- baseURL: https://api.compactif.ai
  baseurl_source: declared
  description: The batches API from Multiverse Computing — 3 operation(s) for batches.
  name: Multiverse Computing Batches API
  slug: multiverse-computing-batches-api
- baseURL: https://api.compactif.ai
  baseurl_source: declared
  description: The completions API from Multiverse Computing — 2 operation(s) for completions.
  name: Multiverse Computing Completions API
  slug: multiverse-computing-completions-api
- baseURL: https://api.compactif.ai
  baseurl_source: declared
  description: The files API from Multiverse Computing — 2 operation(s) for files.
  name: Multiverse Computing Files API
  slug: multiverse-computing-files-api
- baseURL: https://api.compactif.ai
  baseurl_source: declared
  description: The Model info API from Multiverse Computing — 2 operation(s) for model info.
  name: Multiverse Computing Model info API
  slug: multiverse-computing-model-info-api
- baseURL: https://api.compactif.ai
  baseurl_source: declared
  description: The responses API from Multiverse Computing — 2 operation(s) for responses.
  name: Multiverse Computing Responses API
  slug: multiverse-computing-responses-api
artifact_total: 10
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
overview: 'Multiverse Computing publishes 6 APIs on the [APIs.io](https://apis.io/) network, including Audio API, Batches API, Completions API, and 3 more. Tagged areas include Artificial Intelligence, Machine-Learning, LLM Inference, Model Compression, and Quantum Computing.


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
  composite: 50.5
  coverage:
    artifact_dirs: 20
    catalog_gap: 70.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 59.2
    commercial_clarity: 59.2
    contract_governance: 4.5
    contract_quality: 58.5
    developer_ergonomics: 58.9
    discoverability: 75.9
    governance: 4.5
    operational_transparency: 31.6
  previous_composite: 50.5
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 6
    mcp: derived
    skills: derived
  schema_version: 0.18.0
  scored_at: '2026-09-02'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/multiverse-computing/refs/heads/main/screenshots/multiverse-computing-2026-09-02T150656.png
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
- Machine-Learning
- LLM Inference
- Model Compression
- Quantum Computing
- Speech-to-Text
- OpenAI-Compatible
- Developer Tools
- Spain
- Company
website: https://multiversecomputing.com/
---
