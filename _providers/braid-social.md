---
access_model:
  confidence: medium
  label: Freemium SaaS, no public API
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - https://www.trybraid.io/
  trial: true
  try_now: false
agent_readiness:
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: false
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 2.5
  scored_at: '2026-08-26'
api_count: 0
artifact_total: 3
common:
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/braidsocial
- group: company
  title: ''
  type: Website
  url: https://www.trybraid.io/
- group: company
  title: ''
  type: Blog
  url: https://www.trybraid.io/blog
- group: operate
  title: ''
  type: Support
  url: https://www.trybraid.io/support
- group: commercial
  title: ''
  type: Plans
  url: plans/braid-social-plans-pricing.yml
- group: commercial
  title: ''
  type: Pricing
  url: https://www.trybraid.io/
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/braid-social-rate-limits.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/braid-social-lifecycle.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/braid-social-domain-security.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/braid-social-llms.txt
coverage:
  checked: '2026-08-13'
  detail: Braid Social ships Braid Teams only as a Slack end-user app — its full public site is three pages (/, /support, /blog per its own sitemap), the private backend core.trybraid.io answers {"status":"ok"} at root and 404s every spec and /.well-known/ path, and no GitHub org, SDK or developer portal exists under any Braid name.
  evidence:
  - status: 200
    url: https://www.trybraid.io/sitemap.xml
  - status: 404
    url: https://core.trybraid.io/openapi.json
  - status: 200
    url: https://core.trybraid.io/
  - status: 404
    url: https://api.github.com/orgs/trybraid
  - status: 403
    url: https://braid.ai/
  reason: no-developer-program
  state: none
created: '2026-07-17'
description: 'Braid Social, Inc. is a venture-backed startup that has run two products under the Braid name. It launched as a creator-economy, direct-to-fan engagement platform — founded by former Facebook product designer Matthew Cahill and software engineer Chris Piro — letting creators build customizable landing pages that consolidated their work across the web (blog posts, videos, podcasts, and commerce links), collect fan phone numbers, and reach followers directly through SMS, push notifications, and mailing lists, with link tracking and cross-platform analytics. It raised a $6.8M seed round in August 2023 led by Andreessen Horowitz (a16z) with Initialized Capital. The original domain braid.ai is now a domain-for-sale listing at atom.com and braid.social no longer resolves. The same legal entity now ships "Braid Teams" at trybraid.io (mirrored at braidsocial.com) — an AI-powered employee-engagement copilot that runs inside Slack, automating icebreakers, games, polls, events, reminders,
  leaderboards, and engagement reporting for distributed teams, on a free / $5-per-user Premium / contact-us Enterprise plan. Braid Teams is a Slack-app product with no public developer program: no developer portal, no documentation, no OpenAPI, no SDKs, and no GitHub organization. The only machine surface is the private application backend at core.trybraid.io, which answers {"status":"ok"} at its root and 404s every spec, docs and /.well-known/ path. The homepage states the product is "Currently not accepting new users" and the Slack install endpoint returns HTTP 500.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/braid-social.png
layout: provider
modified: '2026-08-13'
name: Braid Social
nav: Providers
network: true
overview: 'Braid Social is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Employee Engagement, Slack, Collaboration, and Team Building.


  Braid Social''s developer surface includes engineering blog, support, pricing, and 7 more developer resources.'
plans:
- name: Braid Social Plans Pricing
  plan_count: 3
  slug: braid-social-plans-pricing
random_paper: 18
rate_limits:
- limit_count: 0
  name: Braid Social Rate Limits
  slug: braid-social-rate-limits
score:
  band: emerging
  composite: 14.8
  delta: 0.0
  facets:
    access_clarity: 42.1
    commercial_clarity: 42.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 7.1
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 14.8
  schema_version: 0.15.0
  scored_at: '2026-08-26'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/braid-social/refs/heads/main/screenshots/braid-social-2026-07-25T203659.png
security:
- kind: domain-security
  name: Braid Social Domain Security
  slug: braid-social-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: braid-social
tags:
- Company
- Employee Engagement
- Slack
- Collaboration
- Team Building
- HR Tech
- Creator Economy
- Social
- Messaging
- Landing Pages
- Analytics
- Consumer
- Direct-to-Fan
- Software-as-a-Service
website: https://www.trybraid.io/
---
