---
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
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 25.2
  scored_at: '2026-08-06'
api_count: 1
apis:
- description: AI visibility / AEO audit API with x402 micropayments. No API key required.
  name: Visibility AI Audit API
  slug: visibility-ai-audit-api
artifact_total: 3
common:
- group: company
  title: ''
  type: Website
  url: https://visibility.gleefulai.com
- group: docs
  title: ''
  type: Documentation
  url: https://visibility.gleefulai.com/docs
- group: commercial
  title: ''
  type: Pricing
  url: https://visibility.gleefulai.com/api/pricing
- group: agent
  title: ''
  type: LlmsText
  url: https://visibility.gleefulai.com/llms.txt
- group: auth
  title: ''
  type: Authentication
  url: authentication/gleefulai-authentication.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/gleefulai-plans.yml
created: '2026-08-03'
description: 'Gleeful AI publishes Visibility, an AI-visibility and answer-engine-optimization audit API: it scores how visible and understandable a website is to AI assistants and agents, audits AI crawler access (GPTBot, ClaudeBot and others), generates a production-ready llms.txt and schema.org markup, checks brand citation across assistants, and runs competitor gap analysis. The access model is the notable part — there are no API keys. Every priced endpoint answers an unauthenticated request with HTTP 402 and an x402 v2 challenge in a Payment-Required header, settled in USDC on Base at prices from $0.06 to $0.55 a call, published machine-readably at /api/pricing alongside /api/capabilities and /api/catalog. Discovery, pricing and two preview endpoints are free. It is an agent-native API in both directions: built to be paid for and called by an agent, and built to measure whether agents can read you.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/gleefulai.png
layout: provider
modified: '2026-08-03'
name: Gleeful AI
nav: Providers
network: true
overview: 'Gleeful AI publishes 1 API on the [APIs.io](https://apis.io/) network: Visibility AI Audit API. Tagged areas include Artificial Intelligence, Agents, x402, Micropayments, and SEO.


  Gleeful AI''s developer surface includes documentation, pricing, authentication, and 3 more developer resources.'
plans:
- name: Gleefulai Plans
  plan_count: 0
  slug: gleefulai-plans
random_paper: 38
score:
  band: emerging
  composite: 23.3
  delta: 0.0
  facets:
    commercial_clarity: 10.5
    contract_quality: 38.8
    developer_ergonomics: 19.6
    discoverability: 75.9
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 23.3
  schema_version: 0.9.1
  scored_at: '2026-08-06'
  trend: flat
security:
- kind: authentication
  name: Gleefulai Authentication
  slug: gleefulai-authentication
  summary_line: 1 scheme
slug: gleefulai
tags:
- Artificial Intelligence
- Agents
- x402
- Micropayments
- SEO
- Audit
- Website
- Content
- Crawlers
- Monetization
website: https://visibility.gleefulai.com
---
