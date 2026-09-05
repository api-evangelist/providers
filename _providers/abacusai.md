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
api_count: 1
apis:
- description: The Abacus.AI REST API and first-party Python client library for building generative AI, agent, and structured ML applications on the Abacus.AI platform. Authentication is via an API key generated fro
  name: Abacus.AI API
  slug: abacusai-api
artifact_total: 5
common:
- group: company
  title: ''
  type: Website
  url: https://abacus.ai/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://abacus.ai/help/developer-platform/introduction
- group: docs
  title: ''
  type: Documentation
  url: https://abacus.ai/help/
- group: docs
  title: ''
  type: APIReference
  url: https://abacus.ai/help/api/
- group: start
  title: ''
  type: GettingStarted
  url: https://abacus.ai/help/python-sdk/getting-started
- group: company
  title: ''
  type: Blog
  url: https://blog.abacus.ai/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/abacusai
- group: operate
  title: ''
  type: Support
  url: https://abacus.ai/help/
- group: commercial
  title: ''
  type: Pricing
  url: https://abacus.ai/pricing
- group: start
  title: ''
  type: SignUp
  url: https://apps.abacus.ai/chatllm/?isSignUp=1
- group: start
  title: ''
  type: Login
  url: https://apps.abacus.ai/chatllm/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://abacus.ai/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://abacus.ai/privacy
- group: auth
  title: ''
  type: Authentication
  url: authentication/abacusai-authentication.yml
- group: build
  title: ''
  type: Packages
  url: packages/abacusai-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/abacusai-packages.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/abacusai-domain-security.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/abacusai-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: https://abacus.ai/security
- group: auth
  title: ''
  type: TrustCenter
  url: security/abacusai-trust-center.yml
- group: auth
  title: ''
  type: Compliance
  url: https://abacus.ai/security
- group: design
  title: ''
  type: Conformance
  url: conformance/abacusai-conformance.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/abacusai-llms.txt
created: '2026-07-17'
description: Abacus.AI is a San Francisco-based artificial intelligence platform that positions itself as an end-to-end AI system for professionals and enterprises. Its ChatLLM product gives individuals and small teams a single interface to more than 100 AI models (GPT, Claude, Gemini and others) plus AI agents and app building, while the Abacus.AI Enterprise platform delivers enterprise generative AI, structured machine learning (predictive modeling, forecasting, personalization) and optimization. Developers integrate the platform through a documented REST API and a first-party Python client library (the abacusai PyPI package), authenticating with an API key. This profile is maintained by the API Evangelist network and enriched from Abacus.AI's public developer surface.
image: https://abacus.ai/favicon.ico
layout: provider
modified: '2026-07-17'
name: Abacus.ai
nav: Providers
network: true
overview: 'Abacus.ai publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Ai Ml, Artificial Intelligence, Machine-Learning, and Generative AI.


  Abacus.ai''s developer surface includes documentation, API reference, getting-started guide, engineering blog, support, pricing, signup flow, and 16 more developer resources.'
random_paper: 6
score:
  band: thin
  composite: 36.5
  coverage:
    artifact_dirs: 7
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 60.5
    commercial_clarity: 60.5
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 64.3
    discoverability: 75.9
    governance: 18.2
    operational_transparency: 13.2
  previous_composite: 36.5
  provenance:
    conformance: first-party
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/abacusai/refs/heads/main/screenshots/abacusai-2026-07-25T181328.png
security:
- kind: authentication
  name: Abacusai Authentication
  slug: abacusai-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Abacusai Domain Security
  slug: abacusai-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Abacusai Vulnerability Disclosure
  slug: abacusai-vulnerability-disclosure
  summary_line: contact published
- kind: trust-center
  name: Abacusai Trust Center
  slug: abacusai-trust-center
  summary_line: SOC 2, ISO 27001, HIPAA, GDPR
slug: abacusai
tags:
- Company
- Ai Ml
- Artificial Intelligence
- Machine-Learning
- Generative AI
- LLM
- AI Agents
- MLOps
- Enterprise AI
- Data Science
website: https://abacus.ai/
---
