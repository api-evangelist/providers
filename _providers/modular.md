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
  scored_at: '2026-09-01'
api_count: 1
apis:
- description: OpenAI-compatible inference API served by MAX. Exposes /v1/chat/completions, /v1/completions, /v1/embeddings, /v1/responses (image and video generation), and /v1/models. Hosted at api.modular.com with
  name: MAX Inference REST API
  slug: max-inference-rest-api
artifact_total: 4
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/modular-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.modular.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://console.modular.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.modular.com/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.modular.com/max/rest-api/
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.modular.com/max/get-started/
- group: company
  title: ''
  type: Blog
  url: https://www.modular.com/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/modular
- group: operate
  title: ''
  type: Support
  url: https://www.modular.com/community
- group: commercial
  title: ''
  type: Pricing
  url: https://www.modular.com/pricing
- group: start
  title: ''
  type: SignUp
  url: https://console.modular.com/signup
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.modular.com/legal/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.modular.com/legal/privacy
- group: operate
  title: ''
  type: StatusPage
  url: https://status.modular.com
- group: auth
  title: ''
  type: Compliance
  url: https://www.modular.com/pricing
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/modular-llms.txt
- group: build
  title: ''
  type: Packages
  url: packages/modular-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/modular-packages.yml
- group: build
  title: ''
  type: CLI
  url: cli/modular-cli.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/modular-changelog.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/modular-lifecycle.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/modular-well-known.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/modular-conformance.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/modular-conventions.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/modular-authentication.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/modular-trust-center.yml
created: '2026-07-17'
description: Modular is an AI infrastructure company building a unified inference stack that runs GenAI models from custom GPU kernels up to production cloud serving. Its open-source MAX framework (Modular Accelerated Xecution) and the Mojo systems programming language let teams serve frontier open models on NVIDIA, AMD, and Apple Silicon hardware. Modular exposes an OpenAI-compatible inference REST API (chat completions, completions, embeddings, and image/video responses) available as self-hosted containers, shared per-token endpoints, dedicated per-minute endpoints, and bring-your-own-cloud deployments through the Modular Console.
image: https://docs.modular.com/images/modular-metadata.png
layout: provider
modified: '2026-07-20'
name: Modular
nav: Providers
network: true
overview: 'Modular publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Artificial Intelligence, Machine-Learning, Inference, and LLM.


  Modular''s developer surface includes documentation, API reference, getting-started guide, engineering blog, support, pricing, signup flow, and 19 more developer resources.'
random_paper: 0
score:
  band: thin
  composite: 34.0
  coverage:
    artifact_dirs: 12
    catalog_gap: 78.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 47.4
    commercial_clarity: 47.4
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 61.9
    discoverability: 75.9
    governance: 18.2
    operational_transparency: 18.4
  previous_composite: 34.0
  provenance:
    conformance: first-party
  schema_version: 0.17.2
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/modular/refs/heads/main/screenshots/modular-2026-08-07T184028.png
security:
- kind: authentication
  name: Modular Authentication
  slug: modular-authentication
  summary_line: http · 2 schemes
- kind: domain-security
  name: Modular Domain Security
  slug: modular-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
- kind: trust-center
  name: Modular Trust Center
  slug: modular-trust-center
  summary_line: SOC 2 Type 2
slug: modular
tags:
- Company
- Artificial Intelligence
- Machine-Learning
- Inference
- LLM
- GPU
- Developer Tools
- Infrastructure
website: https://www.modular.com/
---
