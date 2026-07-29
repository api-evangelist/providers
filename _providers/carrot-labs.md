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
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: documented
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 13.1
  scored_at: '2026-07-28'
api_count: 1
apis:
- description: 'The SuperPenguin platform tracks and attributes AI spend per request, per customer, per feature, and per prompt version across 14+ LLM, speech, and gateway providers. Access is via first-party Python '
  name: SuperPenguin AI Spend Intelligence
  slug: superpenguin-ai-spend-intelligence
artifact_total: 3
common:
- group: company
  title: ''
  type: Website
  url: https://superpenguin.ai
- group: start
  title: ''
  type: DeveloperPortal
  url: https://superpenguin.ai/docs
- group: docs
  title: ''
  type: Documentation
  url: https://superpenguin.ai/docs
- group: docs
  title: ''
  type: APIReference
  url: https://superpenguin.ai/docs
- group: start
  title: ''
  type: GettingStarted
  url: https://superpenguin.ai/docs
- group: commercial
  title: ''
  type: Pricing
  url: https://superpenguin.ai/#pricing
- group: start
  title: ''
  type: SignUp
  url: https://superpenguin.ai/signup
- group: start
  title: ''
  type: Login
  url: https://superpenguin.ai/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://superpenguin.ai/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://superpenguin.ai/privacy
- group: company
  title: ''
  type: Blog
  url: https://superpenguin.ai/blog
- group: company
  title: ''
  type: BlogRSS
  url: https://superpenguin.ai/blog/rss.xml
- group: company
  title: ''
  type: Twitter
  url: https://x.com/carrotlabs__ai
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/carrot-labs-ai
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/carrot-labs-llms.txt
- group: build
  title: ''
  type: Packages
  url: packages/carrot-labs-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/carrot-labs-packages.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/carrot-labs-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/carrot-labs-conventions.yml
- group: design
  title: ''
  type: Idempotency
  url: conventions/carrot-labs-conventions.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/carrot-labs-domain-security.yml
created: '2026-07-17'
description: Carrot Labs is the company behind SuperPenguin, an AI spend intelligence platform that tracks, attributes, and forecasts spending across 14+ LLM, speech, and gateway providers including OpenAI, Anthropic, Google Gemini, AWS Bedrock, Vercel AI Gateway, Deepgram, ElevenLabs, LiveKit, and LiteLLM. SuperPenguin provides per-request cost attribution (by customer, feature, team, environment, prompt key, and prompt version), a multi-provider spend dashboard, prompt version analytics, engineering ROI via Cursor pull-request cost attribution, billing reconciliation against actual provider invoices, and spend alerts over Slack, email, or Discord. It ships lightweight first-party Python (`pip install superpenguin`) and TypeScript (`npm install @superpenguin/js`) SDKs that wrap native provider clients, add sub-10ms overhead, and capture cost metadata without storing prompt or response content by default. Carrot Labs is a Y Combinator (Winter 2026) company based in San Francisco.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/carrot-labs.png
layout: provider
modified: '2026-07-18'
name: Carrot Labs
nav: Providers
network: true
overview: 'Carrot Labs publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Artificial Intelligence, FinOps, AIOps, and Cost Management.


  Carrot Labs'' developer surface includes documentation, API reference, getting-started guide, pricing, signup flow, engineering blog, authentication, and 14 more developer resources.'
random_paper: 8
score:
  band: emerging
  composite: 27.4
  delta: -1.7
  facets:
    commercial_clarity: 44.7
    contract_quality: 0.0
    developer_ergonomics: 54.3
    discoverability: 75.9
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 29.1
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/carrot-labs/refs/heads/main/screenshots/carrot-labs-2026-07-25T204642.png
security:
- kind: authentication
  name: Carrot Labs Authentication
  slug: carrot-labs-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Carrot Labs Domain Security
  slug: carrot-labs-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: carrot-labs
tags:
- Company
- Artificial Intelligence
- FinOps
- AIOps
- Cost Management
- LLM
- Observability
- Developer Tools
website: https://superpenguin.ai
---
