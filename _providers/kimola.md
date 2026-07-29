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
    agent_skills: derived
    agentic_access: false
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: documented
    idempotency: false
    mcp_server: derived
    openapi_examples: documented
    rate_limit_signal: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 18.0
  scored_at: '2026-07-28'
api_count: 2
apis:
- description: REST API for presets (pre-trained classification and entity-extraction models), research reports and their analyses, feedback feeds, query consumption, and subscription usage. Authenticated with an HT
  name: Kimola API
  slug: kimola-api
- description: Text-classification API that runs text against custom and pre-built models and returns matching tags with probabilities (batch up to 100 per request), with multi-language results via ISO 639-1 codes.
  name: Kimola Cognitive API
  slug: kimola-cognitive-api
artifact_total: 5
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/kimola-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://kimola.com
- group: docs
  title: ''
  type: Documentation
  url: https://github.com/Kimola/api
- group: docs
  title: ''
  type: APIReference
  url: https://github.com/Kimola/api
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Kimola
- group: operate
  title: ''
  type: Support
  url: https://kimola.com/support
- group: company
  title: ''
  type: Blog
  url: https://kimola.com/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://kimola.com/pricing
- group: start
  title: ''
  type: SignUp
  url: https://kimola.com/sign-up
- group: start
  title: ''
  type: Login
  url: https://kimola.com/sign-in
- group: commercial
  title: ''
  type: TermsOfService
  url: https://kimola.com/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://kimola.com/privacy-policy
- group: operate
  title: ''
  type: StatusPage
  url: https://status.kimola.com/
- group: build
  title: ''
  type: Packages
  url: packages/kimola-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/kimola-packages.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/kimola-authentication.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/kimola-error-codes.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/kimola-lifecycle.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/kimola-conventions.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/kimola-conformance.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/kimola-data-model.yml
- group: build
  title: ''
  type: Examples
  url: examples/kimola-cognitive-examples.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/kimola-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/kimola-llms.txt
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-07-17'
description: Kimola is a market research automation platform that turns customer feedback into research insights. It tracks feedback from social media, reviews, and direct uploads; analyzes it with AI to detect themes, sentiment, and patterns across 30+ languages; and generates executive summaries, customer personas, pain points, and journey maps. Kimola exposes a public REST API for presets (pre-trained classification and entity-extraction models), reports, feedback feeds, query consumption, and subscription usage, plus the Kimola Cognitive API for running text through custom and pre-built classification models and returning tagged predictions with probabilities. Official Python, Node.js, and C# SDKs are published. Kimola is backed by 500 Global.
image: https://kimola.com/images/kimola-og.webp
layout: provider
mcp_servers:
- description: ''
  name: kimola-mcp.yml
  slug: kimola-mcpyml
modified: '2026-07-19'
name: Kimola
nav: Providers
network: true
overview: 'Kimola publishes 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Market Research, Customer Feedback, Text Analytics, and Sentiment Analysis.


  Kimola''s developer surface includes documentation, API reference, support, engineering blog, pricing, signup flow, authentication, and 18 more developer resources.'
random_paper: 21
score:
  band: thin
  composite: 29.3
  delta: -2.5
  facets:
    commercial_clarity: 44.7
    contract_quality: 0.0
    developer_ergonomics: 42.9
    discoverability: 87.0
    governance: 3.1
    operational_transparency: 21.1
  previous_composite: 31.8
  provenance:
    conformance: derived
    mcp: derived
    skills: derived
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/kimola/refs/heads/main/screenshots/kimola-2026-07-25T223754.png
security:
- kind: authentication
  name: Kimola Authentication
  slug: kimola-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Kimola Domain Security
  slug: kimola-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: kimola
tags:
- Company
- Market Research
- Customer Feedback
- Text Analytics
- Sentiment Analysis
- Natural Language Processing
- Consumer Insights
- Machine Learning
- Artificial Intelligence
website: https://kimola.com
---
