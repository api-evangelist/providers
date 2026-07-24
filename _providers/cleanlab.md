---
access_model:
  confidence: high
  label: Freemium (free trial) · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  trial: true
  try_now: true
agent_readiness:
  band: agent-ready
  dimensions:
    agent_skills: false
    agentic_access: true
    asyncapi_events: true
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
  score: 53.8
  scored_at: '2026-07-23'
agentic_access:
- acting_count: 3
  human_in_the_loop: 0
  name: Cleanlab Agentic Access
  operation_count: 3
  slug: cleanlab-agentic-access
  summary_line: 3 operations · 3 acting
api_count: 4
apis:
- description: The original open-source cleanlab Python library for data-centric AI - finds and fixes label errors, outliers, and other data issues using confident learning. Runs locally (pip install cleanlab); free
  name: Open-Source Library
  slug: open-source-library
- description: The Codex API from Cleanlab — 1 operation(s) for codex.
  name: Cleanlab Codex API
  slug: cleanlab-codex-api
- description: The Studio API from Cleanlab — 1 operation(s) for studio.
  name: Cleanlab Studio API
  slug: cleanlab-studio-api
- description: The TLM API from Cleanlab — 1 operation(s) for tlm.
  name: Cleanlab TLM API
  slug: cleanlab-tlm-api
artifact_total: 15
asyncapis:
- description: AsyncAPI 2.6 description of the Trustworthy Language Model (TLM) **chat completion streaming** surface. Cleanlab does not publish a WebSocket API. The TLM is exposed via an OpenAI-compatible Chat Comp
  name: Cleanlab TLM Chat Completions Streaming (HTTP + SSE)
  slug: cleanlab-asyncapi
collections:
- collection_type: open
  name: Cleanlab API
  slug: open-cleanlab
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/cleanlab-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/cleanlab-trust-center.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/cleanlab-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/cleanlab-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/cleanlab-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/cleanlab
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/cleanlab
- group: company
  title: ''
  type: Website
  url: https://cleanlab.ai
- group: docs
  title: ''
  type: Documentation
  url: https://help.cleanlab.ai
- group: commercial
  title: ''
  type: Plans
  url: plans/cleanlab-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/cleanlab-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/cleanlab-finops.yml
- group: company
  title: ''
  type: Blog
  url: https://cleanlab.ai/blog/
created: '2026-06-21'
description: Cleanlab is a data-and-AI trust platform. Its Trustworthy Language Model (TLM) wraps any LLM with a real-time trustworthiness score to catch hallucinations, Cleanlab Studio curates and labels training data and deploys reliable ML models, and Codex adds a safety, guardrail, and remediation layer for AI assistants and RAG. The open-source cleanlab library underpins it all with data-centric AI.
finops:
- name: Cleanlab Finops
  service_category: AI and Machine Learning
  slug: cleanlab-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/cleanlab.png
layout: provider
modified: '2026-06-21'
name: Cleanlab
nav: Providers
network: true
overview: 'Cleanlab publishes 3 APIs on the [APIs.io](https://apis.io/) network: Codex API, Studio API, and TLM API. Tagged areas include AI, LLM, Trustworthiness, Data Quality, and Guardrails.


  The Cleanlab catalog on APIs.io includes 1 event-driven AsyncAPI specification and 1 Spectral governance ruleset.


  Cleanlab''s developer surface includes authentication, documentation, engineering blog, and 10 more developer resources.'
plans:
- name: Cleanlab Plans Pricing
  plan_count: 5
  slug: cleanlab-plans-pricing
random_paper: 2
rate_limits:
- limit_count: 4
  name: Cleanlab Rate Limits
  slug: cleanlab-rate-limits
rules:
- name: Cleanlab API Rules
  rule_count: 5
  severity_counts:
    error: 1
    hint: 0
    info: 0
    warn: 4
  slug: cleanlab-asyncapi-spectral-rules
score:
  band: developing
  composite: 49.2
  delta: 0.0
  facets:
    commercial_clarity: 47.4
    contract_quality: 70.2
    developer_ergonomics: 21.7
    discoverability: 67.5
    governance: 52.6
    operational_transparency: 36.8
  previous_composite: 49.2
  schema_version: 0.5
  scored_at: '2026-07-23'
  trend: flat
security:
- kind: authentication
  name: Cleanlab Authentication
  slug: cleanlab-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Cleanlab Domain Security
  slug: cleanlab-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Cleanlab Vulnerability Disclosure
  slug: cleanlab-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Cleanlab Trust Center
  slug: cleanlab-trust-center
  summary_line: SOC 2
slug: cleanlab
tags:
- AI
- LLM
- Trustworthiness
- Data Quality
- Guardrails
website: https://cleanlab.ai
---
