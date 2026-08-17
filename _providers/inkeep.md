---
access_model:
  confidence: high
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: true
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: derived
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 32.0
  scored_at: '2026-08-17'
agentic_access:
- acting_count: 4
  human_in_the_loop: 0
  name: Inkeep Agentic Access
  operation_count: 5
  slug: inkeep-agentic-access
  summary_line: 5 operations · 4 acting
api_count: 3
apis:
- description: REST management surface for the Inkeep Agents framework - create and operate agents, sub-agents, projects, tools, MCP servers, conversations, and feedback for building no-code or TypeScript-SDK AI age
  name: Inkeep Agents / Management API
  slug: inkeep-agents-management-api
- description: Log conversations, feedback, and custom interaction events.
  name: Inkeep Analytics API
  slug: inkeep-analytics-api
- description: OpenAI-compatible RAG chat completions over your content.
  name: Inkeep Chat API
  slug: inkeep-chat-api
artifact_total: 16
asyncapis:
- description: AsyncAPI 2.6 description of Inkeep's **chat completion streaming** surface. Inkeep does not publish a WebSocket API. The only asynchronous / event-style transport documented at https://docs.inkeep.com
  name: Inkeep Chat Completions Streaming (HTTP + SSE)
  slug: inkeep-asyncapi
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Inkeep AI & Analytics API
  slug: open-inkeep-analytics-api
- collection_type: open
  name: Inkeep AI & Analytics Chat API
  slug: open-inkeep-chat-api
- collection_type: open
  name: Inkeep AI & Analytics API
  slug: open-inkeep
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/inkeep-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/inkeep-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/inkeep-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/inkeep-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/inkeep
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/inkeep
- group: company
  title: ''
  type: Website
  url: https://inkeep.com
- group: docs
  title: ''
  type: Documentation
  url: https://docs.inkeep.com
- group: commercial
  title: ''
  type: Plans
  url: plans/inkeep-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/inkeep-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/inkeep-finops.yml
- group: company
  title: ''
  type: Blog
  url: https://inkeep.com/blog/rss.xml
created: '2026-06-20'
description: Inkeep is an AI support and agent platform for documentation and products. Its developer platform exposes an OpenAI-compatible RAG / chat completions API over your own content, an Analytics API for logging conversations, feedback, and events, and an Agents / management surface for building and operating AI agents and copilot experiences.
finops:
- name: Inkeep Finops
  service_category: AI and Machine Learning
  slug: inkeep-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/inkeep.png
layout: provider
modified: '2026-06-20'
name: Inkeep
nav: Providers
network: true
overview: 'Inkeep publishes 2 APIs on the [APIs.io](https://apis.io/) network: Analytics API and Chat API. Tagged areas include AI, Support, RAG, Agents, and Documentation.


  The Inkeep catalog on APIs.io includes 1 event-driven AsyncAPI specification and 1 Spectral governance ruleset.


  Inkeep''s developer surface includes authentication, documentation, engineering blog, and 9 more developer resources.'
plans:
- name: Inkeep Plans Pricing
  plan_count: 4
  slug: inkeep-plans-pricing
random_paper: 40
rate_limits:
- limit_count: 5
  name: Inkeep Rate Limits
  slug: inkeep-rate-limits
rules:
- name: Inkeep API Rules
  rule_count: 5
  severity_counts:
    error: 1
    hint: 0
    info: 0
    warn: 4
  slug: inkeep-asyncapi-spectral-rules
score:
  band: developing
  composite: 48.0
  delta: 0.0
  facets:
    commercial_clarity: 47.4
    contract_quality: 67.9
    developer_ergonomics: 21.7
    discoverability: 74.1
    governance: 41.7
    operational_transparency: 36.8
  previous_composite: 48.0
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 2
  schema_version: 0.11.0
  scored_at: '2026-08-17'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/inkeep/refs/heads/main/screenshots/inkeep-2026-06-20T183352.png
security:
- kind: authentication
  name: Inkeep Authentication
  slug: inkeep-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Inkeep Domain Security
  slug: inkeep-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Inkeep Trust Center
  slug: inkeep-trust-center
  summary_line: SOC 2, GDPR
slug: inkeep
tags:
- AI
- Support
- RAG
- Agents
- Documentation
website: https://inkeep.com
---
