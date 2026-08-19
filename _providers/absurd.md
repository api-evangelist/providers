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
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 3.0
  scored_at: '2026-08-19'
api_count: 0
artifact_total: 3
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/absurd-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://absurd.com/
- group: other
  title: ''
  type: Portfolio
  url: https://absurd.com/portfolio
- group: company
  title: ''
  type: Careers
  url: https://absurd.com/careers
- group: operate
  title: ''
  type: Contact
  url: https://absurd.com/contact
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/absurd/
- group: other
  title: ''
  type: X
  url: https://x.com/withabsurd
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/absurd-llms.txt
coverage:
  checked: '2026-08-12'
  detail: 'Absurd sells managed AI ad production through a four-route marketing site and a contact form, so full STEP 0b contract discovery across all four of its live hosts found no machine-readable contract: api.absurd.com is a real FastAPI backend (/health returns {"status":"healthy"}) but its /openapi.json, /docs and /redoc routes are disabled and return JSON 404s, and absurd.com answers every /.well-known/* path with a soft-200 single-page-app shell rather than a document.'
  evidence:
  - status: 200
    url: https://api.absurd.com/health
  - status: 404
    url: https://api.absurd.com/openapi.json
  - status: 404
    url: https://api.absurd.com/docs
  - status: 404
    url: https://api.absurd.com/.well-known/agent-card.json
  - status: 401
    url: https://lp.absurd.com/rest/v1/
  - status: 200
    url: https://absurd.com/sitemap.xml
  reason: no-developer-program
  state: none
created: '2026-07-17'
description: 'Absurd is an AI video creation platform positioning itself as "the Creative OS for AI video." It uses autonomous AI agents to handle scripting, scene planning, and video generation, letting companies produce brand and performance advertisements at scale in roughly 72 hours instead of weeks. Based in Los Angeles and part of Y Combinator''s Fall 2025 batch, Absurd works with brands such as Hims, Kalshi, Replit, Brex, Whop, and Reforge, with some of its generated videos reaching over a million organic views. The company runs a managed, sales-led production motion rather than a self-serve platform: its published sitemap declares exactly four routes (home, portfolio, careers, contact), and it ships no pricing page, no blog, no developer portal, no documentation, no SDKs, and no GitHub organization. Three Absurd-controlled hosts are live but none is a developer surface — app.absurd.com is the gated customer application, api.absurd.com is its private FastAPI backend with schema and
  docs routes disabled, and lp.absurd.com is a key-gated Supabase project serving the landing page. This entry was enriched from public web sources and live unauthenticated probes, and will be upgraded if a developer surface appears.'
image: https://absurd.com/logo.jpeg
layout: provider
modified: '2026-08-12'
name: Absurd
nav: Providers
network: true
overview: Absurd is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Artificial Intelligence, Generative AI, Video, and Advertising.
plans:
- name: Absurd Plans Pricing
  plan_count: 0
  slug: absurd-plans-pricing
random_paper: 45
rate_limits:
- limit_count: 0
  name: Absurd Rate Limits
  slug: absurd-rate-limits
score:
  band: minimal
  composite: 5.7
  delta: 0.0
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 57.4
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 5.7
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/absurd/refs/heads/main/screenshots/absurd-2026-07-25T181425.png
security:
- kind: domain-security
  name: Absurd Domain Security
  slug: absurd-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: absurd
tags:
- Company
- Artificial Intelligence
- Generative AI
- Video
- Advertising
- Marketing
- Media
- Creative
website: https://absurd.com/
---
