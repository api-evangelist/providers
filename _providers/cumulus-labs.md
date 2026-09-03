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
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 2.5
  scored_at: '2026-09-02'
api_count: 1
apis:
- description: OpenAI-compatible HTTP inference gateway. One client works against every upstream provider; per-workflow routing rules pick the model, provider, and infrastructure, with a layered exact/prefix/semanti
  name: Cumulus Inference Gateway
  slug: cumulus-inference-gateway
artifact_total: 3
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/cumulus-labs-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://cumuluslabs.io/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.cumuluslabs.io/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.cumuluslabs.io/
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.cumuluslabs.io/getting-started/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.cumuluslabs.io/inference/overview/
- group: company
  title: ''
  type: Blog
  url: https://cumulus.blog/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/cumulus-compute-labs
- group: operate
  title: ''
  type: Support
  url: mailto:founders@cumuluslabs.io
- group: commercial
  title: ''
  type: TermsOfService
  url: https://cumuluslabs.io/terms-of-service.pdf
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://cumuluslabs.io/privacy-policy.pdf
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/cumuluscomputelabs/
- group: company
  title: ''
  type: Twitter
  url: https://x.com/cumuluslabsio
- group: auth
  title: ''
  type: Authentication
  url: authentication/cumulus-labs-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/cumulus-labs-conventions.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/cumulus-labs-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/cumulus-labs-lifecycle.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/cumulus-labs-llms.txt
created: '2026-07-17'
description: Cumulus Labs is a Y Combinator (W26) company building a unified inference platform for production AI. Cumulus consolidates the eight subsystems teams normally assemble from separate vendors — an OpenAI-compatible gateway, a per-workflow router, a layered prompt/KV cache, request-level observability, continuous shadow evaluation, one-click LoRA fine-tuning, custom open-weight hosting, and the proprietary Ion inference engine running on NVIDIA Grace and Blackwell GPUs — behind a single OpenAI-compatible API at api.cumuluslabs.io/v1. Ion's custom attention kernels deliver 30-50% more throughput than stock vLLM and SGLang, and the gateway is a drop-in replacement for the OpenAI, Anthropic, LangChain, LlamaIndex, and Vercel AI SDKs — change one line of configuration and keep your existing code.
image: https://cumuluslabs.io/cumulus-logo/Cumulus-White.svg
layout: provider
modified: '2026-07-18'
name: Cumulus Labs
nav: Providers
network: true
overview: 'Cumulus Labs publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Inference, LLM, AI Infrastructure, and GPU.


  Cumulus Labs'' developer surface includes documentation, getting-started guide, API reference, engineering blog, support, authentication, and 12 more developer resources.'
random_paper: 6
score:
  band: emerging
  composite: 25.8
  coverage:
    artifact_dirs: 8
    catalog_gap: 78.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 21.1
    commercial_clarity: 21.1
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 57.1
    discoverability: 75.9
    governance: 18.2
    operational_transparency: 2.6
  previous_composite: 25.8
  provenance:
    conformance: first-party
  schema_version: 0.18.0
  scored_at: '2026-09-02'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/cumulus-labs/refs/heads/main/screenshots/cumulus-labs-2026-07-25T210923.png
security:
- kind: authentication
  name: Cumulus Labs Authentication
  slug: cumulus-labs-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Cumulus Labs Domain Security
  slug: cumulus-labs-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
slug: cumulus-labs
tags:
- Company
- Inference
- LLM
- AI Infrastructure
- GPU
- Machine-Learning
- Model Serving
- Fine-Tuning
- API Gateway
- Y Combinator
website: https://cumuluslabs.io/
---
