---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - authentication
  - security
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
  scored_at: '2026-09-04'
api_count: 0
artifact_total: 2
common:
- group: company
  title: ''
  type: Website
  url: https://www.tensorzero.com/
- group: docs
  title: ''
  type: Documentation
  url: https://github.com/tensorzero/tensorzero/tree/main/docs
- group: docs
  title: ''
  type: APIReference
  url: https://www.tensorzero.com/docs/gateway/api-reference
- group: start
  title: ''
  type: GettingStarted
  url: https://www.tensorzero.com/docs/quickstart
- group: company
  title: ''
  type: Blog
  url: https://www.tensorzero.com/blog/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/tensorzero
- group: operate
  title: ''
  type: Support
  url: https://www.tensorzero.com/slack
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.tensorzero.com/terms/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.tensorzero.com/privacy/
- group: operate
  title: ''
  type: ChangeLog
  url: https://github.com/tensorzero/tensorzero/releases
- group: build
  title: ''
  type: Packages
  url: packages/tensorzero-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/tensorzero-packages.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/tensorzero-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/tensorzero-conventions.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/tensorzero-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/tensorzero-lifecycle.yml
- group: operate
  title: ''
  type: Deprecation
  url: lifecycle/tensorzero-lifecycle.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/tensorzero-well-known.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/tensorzero-domain-security.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/tensorzero-llms.txt
created: '2026-07-17'
description: 'TensorZero is an open-source, self-hosted LLMOps platform that unifies five capabilities behind one stack: a high-performance LLM Gateway that accesses every major model provider (Anthropic, OpenAI, AWS Bedrock/SageMaker, Azure, GCP Vertex, Mistral, Groq, xAI and more) through a single OpenAI-compatible API with sub-millisecond p99 overhead; Observability that stores inferences and feedback in your own database; Evaluation via heuristics and LLM judges; Optimization of prompts, models, and inference strategies from metrics and human feedback; and Experimentation with built-in A/B testing, routing, retries, and fallbacks. Written in Rust and deployed as a single Docker container, it plays nicely with the OpenAI SDK and OpenTelemetry. NOTE: as of 2026 TensorZero is no longer maintained — the source remains available on GitHub (all org repositories archived) and the final Python client (2026.6.0) is on PyPI, but the hosted product has wound down.'
image: https://github.com/tensorzero.png
layout: provider
modified: '2026-07-21'
name: TensorZero
nav: Providers
network: true
overview: 'TensorZero is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Ai Ml, LLM, LLMOps, and AI Gateway.


  TensorZero''s developer surface includes documentation, API reference, getting-started guide, engineering blog, support, changelog, authentication, and 13 more developer resources.'
random_paper: 2
score:
  band: thin
  composite: 26.5
  coverage:
    artifact_dirs: 10
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 21.1
    commercial_clarity: 21.1
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 54.8
    discoverability: 57.4
    governance: 18.2
    operational_transparency: 26.3
  previous_composite: 26.5
  provenance:
    conformance: first-party
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/tensorzero/refs/heads/main/screenshots/tensorzero-2026-09-02T163134.png
security:
- kind: authentication
  name: Tensorzero Authentication
  slug: tensorzero-authentication
  summary_line: http/apiKey · 2 schemes
- kind: domain-security
  name: Tensorzero Domain Security
  slug: tensorzero-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
slug: tensorzero
tags:
- Company
- Ai Ml
- LLM
- LLMOps
- AI Gateway
- Inference
- Observability
- Open-Source
- Model Routing
website: https://www.tensorzero.com/
---
