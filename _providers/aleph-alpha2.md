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
    agent_skills: false
    agentic_access: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 9.0
  scored_at: '2026-08-12'
api_count: 1
apis:
- description: The PhariaInference HTTP API provides access to Aleph Alpha's specialized language models for text completion, chat completions, embeddings, semantic (symmetric and asymmetric) search, tokenization/de
  name: PhariaInference API
  slug: phariainference-api
artifact_total: 3
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/aleph-alpha2-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://aleph-alpha.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.aleph-alpha.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.aleph-alpha.com/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.aleph-alpha.com/phariaai-dev-guide/latest/pharia-openapi/index.html
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.aleph-alpha.com/products/apis/pharia-inference/
- group: company
  title: ''
  type: Blog
  url: https://aleph-alpha.com/blog/
- group: operate
  title: ''
  type: Support
  url: https://supportportal.aleph-alpha.com
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Aleph-Alpha
- group: start
  title: ''
  type: SignUp
  url: https://app.aleph-alpha.com
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://aleph-alpha.com/datenschutz/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://aleph-alpha.com/impressum/
- group: build
  title: ''
  type: Packages
  url: packages/aleph-alpha2-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/aleph-alpha2-packages.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/aleph-alpha2-authentication.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/aleph-alpha2-well-known.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/aleph-alpha2-llms.txt
created: '2026-07-17'
description: Aleph Alpha is a Heidelberg, Germany-based artificial intelligence company building sovereign, specialized large language models (SLLMs) for European enterprises and public-sector organizations operating in regulated and sensitive domains. Its PhariaAI suite is an end-to-end, self-hostable stack — PhariaStudio for building AI applications, PhariaAssistant for knowledge workers, and PhariaOS for resource management, alongside the PhariaInference, PhariaSearch, and PhariaData APIs — engineered for data sovereignty, transparency, and EU regulatory compliance while running on European infrastructure. The PhariaInference HTTP API exposes text completion, chat, embeddings, semantic search, tokenization, and explainability, accessed with a bearer token issued from app.aleph-alpha.com and supported by an official open-source Python client.
image: https://raw.githubusercontent.com/api-evangelist/aleph-alpha2/refs/heads/main/apis.yml
layout: provider
modified: '2026-07-17'
name: Aleph Alpha2
nav: Providers
network: true
overview: 'Aleph Alpha2 publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Artificial Intelligence, Large Language Models, Machine Learning, and Generative AI.


  Aleph Alpha2''s developer surface includes documentation, API reference, getting-started guide, engineering blog, support, signup flow, authentication, and 10 more developer resources.'
random_paper: 55
score:
  band: emerging
  composite: 26.9
  delta: 0.0
  facets:
    commercial_clarity: 34.2
    contract_quality: 0.0
    developer_ergonomics: 58.7
    discoverability: 75.9
    governance: 0.0
    operational_transparency: 5.3
  previous_composite: 26.9
  schema_version: 0.11.0
  scored_at: '2026-08-12'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/aleph-alpha2/refs/heads/main/screenshots/aleph-alpha2-2026-07-25T195554.png
security:
- kind: authentication
  name: Aleph Alpha2 Authentication
  slug: aleph-alpha2-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Aleph Alpha2 Domain Security
  slug: aleph-alpha2-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: aleph-alpha2
tags:
- Company
- Artificial Intelligence
- Large Language Models
- Machine Learning
- Generative AI
- Sovereign AI
- Inference API
- Embeddings
- Europe
- Germany
- Enterprise AI
website: https://aleph-alpha.com/
---
