---
access_model:
  confidence: high
  label: Paid · Sales-gated onboarding
  onboarding: unknown
  pricing: paid
  public: false
  source:
  - plans
  - website
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
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 0.0
  scored_at: '2026-08-17'
api_count: 0
artifact_total: 2
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/memoir-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.trymemoir.ai/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.trymemoir.ai/pricing/
- group: commercial
  title: ''
  type: Plans
  url: plans/memoir-plans-pricing.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/memoir-llms.txt
- group: start
  title: ''
  type: Login
  url: https://www.trymemoir.ai/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.trymemoir.ai/terms/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.trymemoir.ai/privacy/
- group: operate
  title: ''
  type: Support
  url: mailto:maanav@trymemoir.ai
coverage:
  checked: '2026-08-13'
  detail: 'Memoir ships an end-user marketing SaaS only — there is no developer surface of any kind: www.trymemoir.ai/developers, /docs, /api-docs and /llms.txt all return 404 from the Vercel SPA, and the single backend host api.trymemoir.ai answers every path, including /openapi.json, /graphql, /mcp and /.well-known/*, with a blanket HTTP 401 {"detail":"Not signed in"}.'
  evidence:
  - status: 404
    url: https://www.trymemoir.ai/developers
  - status: 404
    url: https://www.trymemoir.ai/llms.txt
  - status: 401
    url: https://api.trymemoir.ai/openapi.json
  - status: 401
    url: https://api.trymemoir.ai/.well-known/agent-card.json
  reason: no-developer-program
  state: none
created: '2026-07-17'
description: 'Memoir, operated by Tachyon Labs, Inc., is an AI-powered marketing automation platform in Y Combinator''s Spring 2026 batch, founded in 2026 by Maanav Agrawal and Jason Zhan. It connects to the systems where product work happens — GitHub, Linear and Slack on every plan, plus Jira, Notion, Google Docs, Drive and CRM on higher tiers — and turns shipped product updates into multi-channel marketing content: social posts, blog posts, changelogs, launch pages, ads, demo videos and customer updates generated in the company''s brand voice and routed through human approval. The product is organized around "Memory" (Atlas) for building context about a company and "Motion" (market-motion) for producing and distributing content as teams ship features. Published customers include Datost, Smol Machines, TraceRoot and Zatanna. Pricing is published at three tiers — Starter $300/mo, Scale $1,500/mo and a custom Enterprise tier — all sold through a demo conversation rather than self-serve checkout.
  Memoir is a marketing SaaS product with no developer program: it exposes only a private session- authenticated backend (api.trymemoir.ai answers every path, including /.well-known/*, with HTTP 401 "Not signed in") and publishes no public API, developer portal, API reference, machine-readable specification, SDK, CLI or MCP server.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/memoir.png
layout: provider
modified: '2026-08-13'
name: Memoir
nav: Providers
network: true
overview: 'Memoir is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Marketing, Marketing Automation, Artificial Intelligence, and Content Generation.


  Memoir''s developer surface includes pricing, support, and 7 more developer resources.'
plans:
- name: Memoir Plans Pricing
  plan_count: 3
  slug: memoir-plans-pricing
random_paper: 53
score:
  band: emerging
  composite: 21.9
  delta: 7.1
  facets:
    commercial_clarity: 76.3
    contract_quality: 0.0
    developer_ergonomics: 4.3
    discoverability: 57.4
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 14.8
  schema_version: 0.11.0
  scored_at: '2026-08-17'
  trend: rising
screenshot: https://raw.githubusercontent.com/api-evangelist/memoir/refs/heads/main/screenshots/memoir-2026-08-07T172457.png
security:
- kind: domain-security
  name: Memoir Domain Security
  slug: memoir-domain-security
  summary_line: TLSv1.3 · HSTS
slug: memoir
tags:
- Company
- Marketing
- Marketing Automation
- Artificial Intelligence
- Content Generation
- Developer Marketing
- SaaS
- Y Combinator
website: https://www.trymemoir.ai/
---
