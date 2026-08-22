---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source: []
  trial: false
  try_now: false
agent_readiness:
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 0.0
  scored_at: '2026-08-19'
api_count: 0
artifact_total: 2
common:
- group: company
  title: ''
  type: Website
  url: https://massive-dynamic.ai
- group: company
  title: ''
  type: Careers
  url: https://massive-dynamic.notion.site/
- group: auth
  title: ''
  type: DomainSecurity
  url: security/massive-dynamic-domain-security.yml
- group: start
  title: ''
  type: Login
  url: https://app.massive-dynamic.ai
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/massive-dynamic-llms.txt
- group: commercial
  title: ''
  type: Plans
  url: plans/massive-dynamic-plans-pricing.yml
coverage:
  checked: '2026-08-12'
  detail: Massive Dynamic ships only an end-user product — a login-gated Next.js app at app.massive-dynamic.ai titled "Quantum One" backed by a private Express service at api.massive-dynamic.ai that answers "Cannot GET /" for every path including /openapi.json, /graphql and /mcp — and its Figma Sites marketing page offers no developer link at all, only a "Request a demo" button.
  evidence:
  - status: 404
    url: https://api.massive-dynamic.ai/openapi.json
  - status: 404
    url: https://api.massive-dynamic.ai/
  - status: 404
    url: https://massive-dynamic.ai/llms.txt
  - status: 404
    url: https://massive-dynamic.ai/.well-known/agent-card.json
  - status: 404
    url: https://massive-dynamic.ai/privacy
  - status: 200
    url: https://app.massive-dynamic.ai/
  reason: no-developer-program
  state: none
created: '2026-07-17'
description: Massive Dynamic is an AI-powered advertising platform that bills itself as "The Advertising Copilot" and "the human-AI interface for massive scale." It helps media and advertising teams coordinate large-scale digital ad campaigns by pairing an AI Analysis Copilot (automating daily analytics checks, quarterly business reviews, and Media Mix Modeling) with Execution Delegation, where an AI agent handles operational campaign setup so strategists can focus on decisions. The tool works inside existing Slack and email workflows as a conduit between strategy and activation teams, and emphasizes enterprise-grade data governance with ring-fenced customer data and an explicit commitment not to use customer data to train or improve models. Founded in Paris in 2025 by Trystan Chabert (formerly Head of Growth at Voodoo) and Guillaume le Roy (formerly Head of Engineering at Qonto), the company raised a roughly EUR 3M pre-seed led by Seedcamp in July 2025, with Founders Future, Kima Ventures
  and others participating, and is deployed with a select group of early design partners. It sells its product as an end-user application — the marketing site is a Figma Sites page whose only call to action is "Request a demo", and the product itself is a login-gated web app at app.massive-dynamic.ai. As of the 2026-08-12 enrichment pass Massive Dynamic publishes no public API, no developer documentation, no SDKs, and no machine-readable contract of any kind — every OpenAPI, GraphQL, MCP, agent-card and /.well-known/ probe against its marketing, API and app hosts returned 404 or an application shell.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/massive-dynamic.png
layout: provider
modified: '2026-08-12'
name: Massive Dynamic
nav: Providers
network: true
overview: Massive Dynamic is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Advertising, Advertising Technology, Artificial Intelligence, and Marketing.
plans:
- name: Massive Dynamic Plans Pricing
  plan_count: 0
  slug: massive-dynamic-plans-pricing
random_paper: 13
score:
  band: minimal
  composite: 7.1
  delta: -1.3
  facets:
    access_clarity: 6.6
    commercial_clarity: 6.6
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 57.4
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 8.4
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/massive-dynamic/refs/heads/main/screenshots/massive-dynamic-2026-07-25T230328.png
security:
- kind: domain-security
  name: Massive Dynamic Domain Security
  slug: massive-dynamic-domain-security
  summary_line: TLSv1.3
slug: massive-dynamic
tags:
- Company
- Advertising
- Advertising Technology
- Artificial Intelligence
- Marketing
- Media
- Analytics
- Automation
- Agents
website: https://massive-dynamic.ai
---
