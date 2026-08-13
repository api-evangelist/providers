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
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 0.0
  scored_at: '2026-08-12'
api_count: 0
artifact_total: 1
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/conteller-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://conteller.com
coverage:
  checked: '2026-08-10'
  detail: Conteller's entire web presence is offline — conteller.com answers HTTP 402 "Payment required / DEPLOYMENT_DISABLED" from Vercel on every path including the root and all /.well-known/* probes, blog.conteller.com returns Cloudflare error 1014 and admin.conteller.com a 522, and the Internet Archive has no successful capture after 2025-07-16.
  evidence:
  - status: 402
    url: https://conteller.com/
  - status: 402
    url: https://conteller.com/.well-known/agent-card.json
  - status: 402
    url: https://conteller.com/openapi.json
  - status: 403
    url: https://blog.conteller.com/
  - status: 522
    url: https://admin.conteller.com/
  reason: defunct
  state: none
created: '2026-07-17'
description: 'Conteller is a user-generated content (UGC) marketplace where brands pay for authentic media directly from their own customers and everyday, non-famous creators. Brands publish media briefs and the platform lets creators capture, submit, and store photos, videos, and TikTok-style content, then handles paying those creators for approved submissions. A Mexican/Spanish startup (Madrid) selected for Batch 19 of 500 Global''s Somos Lucha accelerator program in Latin America, Conteller has run pilots spanning roughly 1,400 creators and a dozen brands. It was added to the API Evangelist network as a portfolio lead of 500 Global. The public site is no longer serving: conteller.com and www.conteller.com both return HTTP 402 "Payment required / DEPLOYMENT_DISABLED" from Vercel on every path, the blog subdomain returns a Cloudflare 1014 and the admin subdomain a 522, and the Internet Archive holds no successful capture of the site after 2025-07-16. No public developer portal, API, documentation,
  OpenAPI, GraphQL, MCP or agent-card surface has ever been found for Conteller, and its GitHub organization publishes no repositories.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/conteller.png
layout: provider
modified: '2026-08-10'
name: Conteller
nav: Providers
network: true
overview: Conteller is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, User Generated Content, Content Marketing, Creator Economy, and Marketing.
random_paper: 8
score:
  band: minimal
  composite: 5.0
  delta: 0.0
  facets:
    commercial_clarity: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 5.0
  schema_version: 0.11.0
  scored_at: '2026-08-12'
  trend: flat
security:
- kind: domain-security
  name: Conteller Domain Security
  slug: conteller-domain-security
  summary_line: TLSv1.3 · DMARC
slug: conteller
tags:
- Company
- User Generated Content
- Content Marketing
- Creator Economy
- Marketing
- Media
- Startup
website: https://conteller.com
---
