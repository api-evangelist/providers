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
  scored_at: '2026-08-10'
api_count: 17
apis:
- description: The Audit API from Gleeful AI — 3 operation(s) for audit.
  name: Gleeful AI Audit API
  slug: gleefulai-audit-api
- description: The Bots API from Gleeful AI — 1 operation(s) for bots.
  name: Gleeful AI Bots API
  slug: gleefulai-bots-api
- description: The Capabilities API from Gleeful AI — 1 operation(s) for capabilities.
  name: Gleeful AI Capabilities API
  slug: gleefulai-capabilities-api
- description: The Catalog API from Gleeful AI — 1 operation(s) for catalog.
  name: Gleeful AI Catalog API
  slug: gleefulai-catalog-api
- description: The Cite API from Gleeful AI — 2 operation(s) for cite.
  name: Gleeful AI Cite API
  slug: gleefulai-cite-api
- description: The Compare API from Gleeful AI — 2 operation(s) for compare.
  name: Gleeful AI Compare API
  slug: gleefulai-compare-api
- description: The Content API from Gleeful AI — 1 operation(s) for content.
  name: Gleeful AI Content API
  slug: gleefulai-content-api
- description: The Examples API from Gleeful AI — 1 operation(s) for examples.
  name: Gleeful AI Examples API
  slug: gleefulai-examples-api
- description: The Fixes API from Gleeful AI — 1 operation(s) for fixes.
  name: Gleeful AI Fixes API
  slug: gleefulai-fixes-api
- description: The Health API from Gleeful AI — 1 operation(s) for health.
  name: Gleeful AI Health API
  slug: gleefulai-health-api
- description: The Llms API from Gleeful AI — 1 operation(s) for llms.
  name: Gleeful AI Llms API
  slug: gleefulai-llms-api
- description: The Meta API from Gleeful AI — 1 operation(s) for meta.
  name: Gleeful AI Meta API
  slug: gleefulai-meta-api
- description: The Preview API from Gleeful AI — 2 operation(s) for preview.
  name: Gleeful AI Preview API
  slug: gleefulai-preview-api
- description: The Pricing API from Gleeful AI — 1 operation(s) for pricing.
  name: Gleeful AI Pricing API
  slug: gleefulai-pricing-api
- description: The Probe API from Gleeful AI — 1 operation(s) for probe.
  name: Gleeful AI Probe API
  slug: gleefulai-probe-api
- description: The Schema API from Gleeful AI — 1 operation(s) for schema.
  name: Gleeful AI Schema API
  slug: gleefulai-schema-api
- description: The Status API from Gleeful AI — 1 operation(s) for status.
  name: Gleeful AI Status API
  slug: gleefulai-status-api
artifact_total: 19
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
overview: 'Gleeful AI publishes 17 APIs on the [APIs.io](https://apis.io/) network, including Audit API, Bots API, Capabilities API, and 14 more. Tagged areas include Artificial Intelligence, Agents, x402, Micropayments, and SEO.


  Gleeful AI''s developer surface includes documentation, pricing, authentication, and 3 more developer resources.'
plans:
- name: Gleefulai Plans
  plan_count: 0
  slug: gleefulai-plans
random_paper: 14
score:
  band: emerging
  composite: 24.6
  delta: 1.3
  facets:
    commercial_clarity: 10.5
    contract_quality: 41.6
    developer_ergonomics: 19.6
    discoverability: 81.5
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 23.3
  schema_version: 0.9.1
  scored_at: '2026-08-10'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/gleefulai/refs/heads/main/screenshots/gleefulai-2026-08-07T165729.png
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
