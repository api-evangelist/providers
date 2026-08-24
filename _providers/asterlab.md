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
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 8.5
  scored_at: '2026-08-24'
api_count: 1
apis:
- description: OpenAI-compatible inference API from Aster serving open-weight models (gpt-oss-120b, gpt-oss-120b-fast, GLM 5.2). Authenticate with an Aster API key created in the inference console and set the base U
  name: Aster Inference API
  slug: aster-inference-api
artifact_total: 3
common:
- group: start
  title: ''
  type: DeveloperPortal
  url: https://www.asterlab.ai/inference/console
- group: docs
  title: ''
  type: Documentation
  url: https://www.asterlab.ai/inference
- group: start
  title: ''
  type: GettingStarted
  url: https://www.asterlab.ai/inference
- group: commercial
  title: ''
  type: Pricing
  url: https://www.asterlab.ai/inference
- group: start
  title: ''
  type: SignUp
  url: https://www.asterlab.ai/inference/console
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.asterlab.ai/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.asterlab.ai/privacy
- group: company
  title: ''
  type: Blog
  url: https://www.asterlab.ai/research/scaling_autonomous_research_to_thousands_of_agents
- group: operate
  title: ''
  type: Support
  url: mailto:info@asterlab.ai
- group: auth
  title: ''
  type: Authentication
  url: authentication/asterlab-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/asterlab-conventions.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/asterlab-well-known.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/asterlab-llms.txt
- group: auth
  title: ''
  type: DomainSecurity
  url: security/asterlab-domain-security.yml
created: '2026-07-17'
description: Aster (Aster AI Labs, PBC), operating as Asterlab, is a San Francisco based Y Combinator (Spring 2026) public benefit corporation building autonomous research systems that coordinate thousands of AI research agents working in parallel to automate open-ended scientific discovery. The company used that same autonomous-research system to optimize its own inference stack and now offers Aster Inference, an OpenAI-compatible inference API serving open-weight models (gpt-oss-120b, gpt-oss-120b-fast, and Z.ai's GLM 5.2) at what it benchmarks as the fastest gpt-oss-120b output speed on GPU (644 tok/s). The API works with the official OpenAI Python and JS SDKs, LangChain, LiteLLM, Cursor, the Vercel AI SDK, and most agent frameworks by pointing the base URL at https://api.asterlab.ai/v1, with zero data retention by default.
image: https://www.asterlab.ai/og/default.png
layout: provider
modified: '2026-07-18'
name: Asterlab
nav: Providers
network: true
overview: 'Asterlab publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Artificial Intelligence, Machine-Learning, LLM, and Inference.


  Asterlab''s developer surface includes documentation, getting-started guide, pricing, signup flow, engineering blog, support, authentication, and 7 more developer resources.'
random_paper: 6
score:
  band: thin
  composite: 26.5
  delta: 0.0
  facets:
    access_clarity: 44.7
    commercial_clarity: 44.7
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 50.0
    discoverability: 75.9
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 26.5
  schema_version: 0.12.1
  scored_at: '2026-08-24'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/asterlab/refs/heads/main/screenshots/asterlab-2026-07-25T201459.png
security:
- kind: authentication
  name: Asterlab Authentication
  slug: asterlab-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Asterlab Domain Security
  slug: asterlab-domain-security
  summary_line: TLSv1.3 · HSTS
slug: asterlab
tags:
- Company
- Artificial Intelligence
- Machine-Learning
- LLM
- Inference
- OpenAI-Compatible
- Autonomous Research
- GPU
- Developer Tools
website: https://www.asterlab.ai/inference/console
---
