---
access_model:
  confidence: high
  label: Paid · Self-serve signup
  onboarding: self-serve
  pricing: paid
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 30.6
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 7
  human_in_the_loop: 0
  name: Kapa Ai Agentic Access
  operation_count: 20
  slug: kapa-ai-agentic-access
  summary_line: 20 operations · 7 acting
api_count: 6
apis:
- description: Activity, coverage gaps, and top questions.
  name: kapa.ai Analytics API
  slug: kapa-ai-analytics-api
- description: Ask questions and create threads.
  name: kapa.ai Chat API
  slug: kapa-ai-chat-api
- description: Submit reactions on answers.
  name: kapa.ai Feedback API
  slug: kapa-ai-feedback-api
- description: Projects, integrations, and sources.
  name: kapa.ai Projects API
  slug: kapa-ai-projects-api
- description: Semantic retrieval and keyword search.
  name: kapa.ai Retrieval API
  slug: kapa-ai-retrieval-api
- description: List, retrieve, and continue conversations.
  name: kapa.ai Threads API
  slug: kapa-ai-threads-api
artifact_total: 13
collections:
- collection_type: open
  name: kapa.ai Query API
  slug: open-kapa-ai
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/kapa-ai-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/kapa-ai-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/kapa-ai-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/kapa-ai
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/kapa-ai
- group: company
  title: ''
  type: Website
  url: https://www.kapa.ai
- group: docs
  title: ''
  type: Documentation
  url: https://docs.kapa.ai
- group: commercial
  title: ''
  type: Plans
  url: plans/kapa-ai-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/kapa-ai-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/kapa-ai-finops.yml
- group: company
  title: ''
  type: Blog
  url: https://www.kapa.ai/blog
created: '2026-06-20'
description: kapa.ai is an AI assistant and answer platform that turns technical documentation, GitHub content, forums, and developer products into a retrieval-augmented chat experience. The kapa.ai Query API lets teams ask questions, run threaded conversations with streaming answers, perform semantic retrieval and search, and pull analytics over projects and threads via a REST interface authenticated with an X-API-KEY header.
finops:
- name: Kapa Ai Finops
  service_category: AI and Machine Learning
  slug: kapa-ai-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/kapa-ai.png
layout: provider
modified: '2026-06-20'
name: kapa.ai
nav: Providers
network: true
overview: 'kapa.ai publishes 6 APIs on the [APIs.io](https://apis.io/) network, including Analytics API, Chat API, Feedback API, and 3 more. Tagged areas include AI, Answer Engine, RAG, Documentation, and Developer Tools.


  kapa.ai''s developer surface includes authentication, documentation, engineering blog, and 8 more developer resources.'
plans:
- name: Kapa Ai Plans Pricing
  plan_count: 3
  slug: kapa-ai-plans-pricing
random_paper: 44
rate_limits:
- limit_count: 3
  name: Kapa Ai Rate Limits
  slug: kapa-ai-rate-limits
score:
  band: thin
  composite: 39.5
  delta: -2.4
  facets:
    commercial_clarity: 39.5
    contract_quality: 60.2
    developer_ergonomics: 21.7
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 36.8
  previous_composite: 41.9
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 6
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/kapa-ai/refs/heads/main/screenshots/kapa-ai-2026-06-20T183921.png
security:
- kind: authentication
  name: Kapa Ai Authentication
  slug: kapa-ai-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Kapa Ai Domain Security
  slug: kapa-ai-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: kapa-ai
tags:
- AI
- Answer Engine
- RAG
- Documentation
- Developer Tools
website: https://www.kapa.ai
---
