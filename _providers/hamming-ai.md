---
access_model:
  confidence: high
  label: Enterprise · Self-serve signup
  onboarding: self-serve
  pricing: enterprise
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_skills: false
    agentic_access: true
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: true
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.1
  score: 48.1
  scored_at: '2026-07-23'
agentic_access:
- acting_count: 11
  human_in_the_loop: 0
  name: Hamming Ai Agentic Access
  operation_count: 16
  slug: hamming-ai-agentic-access
  summary_line: 16 operations · 11 acting
api_count: 6
apis:
- description: Manage datasets of test cases and scenarios.
  name: Hamming AI Datasets API
  slug: hamming-ai-datasets-api
- description: Create and run experiments and experiment items.
  name: Hamming AI Experiments API
  slug: hamming-ai-experiments-api
- description: Ingest traces, logs, and production call logs.
  name: Hamming AI Monitoring API
  slug: hamming-ai-monitoring-api
- description: List and fetch versioned prompts from the registry.
  name: Hamming AI Prompts API
  slug: hamming-ai-prompts-api
- description: Register custom scoring functions.
  name: Hamming AI Scoring API
  slug: hamming-ai-scoring-api
- description: Run voice agents against datasets and retrieve experiment calls.
  name: Hamming AI Voice Testing API
  slug: hamming-ai-voice-testing-api
artifact_total: 13
collections:
- collection_type: open
  name: Hamming AI REST API
  slug: open-hamming-ai
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/hamming-ai-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/hamming-ai-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/hamming-ai-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/HammingHQ
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/hammingai
- group: company
  title: ''
  type: Website
  url: https://hamming.ai/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.hamming.ai
- group: commercial
  title: ''
  type: Plans
  url: plans/hamming-ai-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/hamming-ai-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/hamming-ai-finops.yml
created: '2026-06-21'
description: Hamming AI is a testing, evaluation, and observability platform for voice and LLM AI agents. Its REST API runs experiments and voice/call test runs against your agents, manages datasets, registers custom scorers and evaluations, and ingests traces, logs, and production call logs for monitoring. A prompt optimizer and registry round out the platform.
finops:
- name: Hamming Ai Finops
  service_category: AI and Machine Learning
  slug: hamming-ai-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/hamming-ai.png
layout: provider
modified: '2026-06-21'
name: Hamming AI
nav: Providers
network: true
overview: 'Hamming AI publishes 6 APIs on the [APIs.io](https://apis.io/) network, including Datasets API, Experiments API, Monitoring API, and 3 more. Tagged areas include AI, Voice Agents, LLM, Testing, and Evaluation.


  Hamming AI''s developer surface includes authentication, documentation, and 8 more developer resources.'
plans:
- name: Hamming Ai Plans Pricing
  plan_count: 2
  slug: hamming-ai-plans-pricing
random_paper: 15
rate_limits:
- limit_count: 3
  name: Hamming Ai Rate Limits
  slug: hamming-ai-rate-limits
score:
  band: thin
  composite: 35.8
  delta: 0.0
  facets:
    commercial_clarity: 28.9
    contract_quality: 58.4
    developer_ergonomics: 19.6
    discoverability: 67.5
    governance: 0.0
    operational_transparency: 36.8
  previous_composite: 35.8
  schema_version: 0.5
  scored_at: '2026-07-23'
  trend: flat
security:
- kind: authentication
  name: Hamming Ai Authentication
  slug: hamming-ai-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Hamming Ai Domain Security
  slug: hamming-ai-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: hamming-ai
tags:
- AI
- Voice Agents
- LLM
- Testing
- Evaluation
- Observability
website: https://hamming.ai/
---
