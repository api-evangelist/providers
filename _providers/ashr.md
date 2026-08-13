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
api_count: 0
artifact_total: 2
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/ashr-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://ashr.io
- group: docs
  title: ''
  type: Documentation
  url: https://ashr.io/docs/python-sdk/overview/
- group: start
  title: ''
  type: GettingStarted
  url: https://ashr.io/docs/python-sdk/overview/
- group: company
  title: ''
  type: Blog
  url: https://ashr.io/blog/
- group: commercial
  title: ''
  type: Pricing
  url: https://ashr.io/#pricing
- group: start
  title: ''
  type: Login
  url: https://lab.ashr.io
- group: commercial
  title: ''
  type: TermsOfService
  url: https://ashr.io/user_agreement.html
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://ashr.io/privacy.html
- group: operate
  title: ''
  type: Support
  url: mailto:support@ashr.io
- group: build
  title: ''
  type: Packages
  url: packages/ashr-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/ashr-packages.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/ashr-authentication.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/ashr-llms.txt
created: '2026-07-17'
description: Ashr (Ashr Labs) is a testing and evaluation platform for AI agents. It lets teams test agents in real environments, generate realistic user-journey datasets, run graded evaluations across text, voice, image, and file modalities, catch regressions, and monitor agents in production. Ashr integrates as a Python or TypeScript SDK (pip install ashr-labs) into an existing codebase, exposing an AshrLabsClient plus EvalRunner and RunBuilder to fetch a dataset, run it against your agent, submit results for server-side grading, poll graded metrics, and trace production runs. The hosted Ashr Labs console at lab.ashr.io provides datasets, test timelines, prompt versioning, and analytics. Founded by Shreyas Kaps and Rohan Kulkarni; Y Combinator Winter 2026; based in San Francisco.
image: https://ashr.io/ashr_transparent.png
layout: provider
modified: '2026-07-18'
name: Ashr
nav: Providers
network: true
overview: 'Ashr is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, AI Agents, Agent Testing, Evaluation, and Observability.


  Ashr''s developer surface includes documentation, getting-started guide, engineering blog, pricing, support, authentication, and 8 more developer resources.'
random_paper: 70
score:
  band: emerging
  composite: 23.4
  delta: 0.0
  facets:
    commercial_clarity: 44.7
    contract_quality: 0.0
    developer_ergonomics: 43.5
    discoverability: 57.4
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 23.4
  schema_version: 0.11.0
  scored_at: '2026-08-12'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/ashr/refs/heads/main/screenshots/ashr-2026-07-25T201424.png
security:
- kind: authentication
  name: Ashr Authentication
  slug: ashr-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Ashr Domain Security
  slug: ashr-domain-security
  summary_line: TLSv1.3 · DMARC
slug: ashr
tags:
- Company
- AI Agents
- Agent Testing
- Evaluation
- Observability
- LLM
- Developer Tools
- SDK
website: https://ashr.io
---
