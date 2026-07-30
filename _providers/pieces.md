---
access_model:
  confidence: medium
  label: Freemium
  onboarding: unknown
  pricing: freemium
  public: false
  source:
  - plans
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    asyncapi_events: true
    auth_clarity: false
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
  score: 27.0
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 14
  human_in_the_loop: 0
  name: Pieces Agentic Access
  operation_count: 28
  slug: pieces-agentic-access
  summary_line: 28 operations · 14 acting
api_count: 8
apis:
- description: Application registration and sessions.
  name: Pieces Applications API
  slug: pieces-applications-api
- description: Saved snippets stored in the local Pieces OS database.
  name: Pieces Assets API
  slug: pieces-assets-api
- description: Copilot conversations and their messages.
  name: Pieces Conversations API
  slug: pieces-conversations-api
- description: Fragment representations that back each asset.
  name: Pieces Formats API
  slug: pieces-formats-api
- description: Local and cloud LLMs available to Pieces OS.
  name: Pieces Models API
  slug: pieces-models-api
- description: Pieces Copilot generative engine (question, relevance, stream).
  name: Pieces QGPT API
  slug: pieces-qgpt-api
- description: Local user context.
  name: Pieces User API
  slug: pieces-user-api
- description: Health and version of the local Pieces OS instance.
  name: Pieces Well Known API
  slug: pieces-well-known-api
artifact_total: 16
asyncapis:
- description: 'AsyncAPI 2.6 description of the Pieces Copilot **QGPT streaming** surface. Pieces runs **on-device**. Pieces OS is a local process that serves its API over the loopback interface at `http://localhost:'
  name: Pieces Copilot (QGPT) Streaming (On-Device WebSocket)
  slug: pieces-asyncapi
collections:
- collection_type: open
  name: Pieces OS Local API
  slug: open-pieces
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/pieces-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/pieces-domain-security.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/pieces-app
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/getpieces
- group: company
  title: ''
  type: Website
  url: https://pieces.app
- group: docs
  title: ''
  type: Documentation
  url: https://docs.pieces.app
- group: commercial
  title: ''
  type: Plans
  url: plans/pieces-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/pieces-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/pieces-finops.yml
- group: company
  title: ''
  type: Blog
  url: https://pieces.app/blog
created: '2026-06-20'
description: Pieces is an on-device AI developer assistant and long-term memory tool. Pieces OS runs locally on the developer's machine and exposes a documented local REST API at http://localhost:1000 covering saved snippets (assets), the Pieces Copilot (QGPT) question/stream endpoints, local and cloud models, formats, applications, conversations, and workspace context. The same on-device API powers official OpenAPI-generated SDKs for Python, TypeScript, Dart, Kotlin, and C#.
finops:
- name: Pieces Finops
  service_category: AI and Machine Learning
  slug: pieces-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/pieces.png
layout: provider
modified: '2026-06-20'
name: Pieces
nav: Providers
network: true
overview: 'Pieces publishes 8 APIs on the [APIs.io](https://apis.io/) network, including Applications API, Assets API, Conversations API, and 5 more. Tagged areas include AI, Developer Tools, On-Device, Local API, and Long-Term Memory.


  The Pieces catalog on APIs.io includes 1 event-driven AsyncAPI specification and 1 Spectral governance ruleset.


  Pieces'' developer surface includes documentation, engineering blog, and 8 more developer resources.'
plans:
- name: Pieces Plans Pricing
  plan_count: 3
  slug: pieces-plans-pricing
random_paper: 59
rate_limits:
- limit_count: 4
  name: Pieces Rate Limits
  slug: pieces-rate-limits
rules:
- name: Pieces API Rules
  rule_count: 1
  severity_counts:
    error: 0
    hint: 0
    info: 0
    warn: 1
  slug: pieces-asyncapi-spectral-rules
score:
  band: thin
  composite: 39.9
  delta: -4.4
  facets:
    commercial_clarity: 39.5
    contract_quality: 49.2
    developer_ergonomics: 10.9
    discoverability: 64.8
    governance: 52.1
    operational_transparency: 36.8
  previous_composite: 44.3
  provenance:
    agentic_access: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 8
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/pieces/refs/heads/main/screenshots/pieces-2026-06-20T191813.png
security:
- kind: domain-security
  name: Pieces Domain Security
  slug: pieces-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: pieces
tags:
- AI
- Developer Tools
- On-Device
- Local API
- Long-Term Memory
website: https://pieces.app
---
