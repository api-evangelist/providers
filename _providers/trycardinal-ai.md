---
access_model:
  confidence: high
  label: Requires approval
  onboarding: approval
  pricing: unknown
  public: false
  source:
  - https://www.trycardinal.com/enterprise
  - https://calendly.com/trycardinal/gtm-chat
  - https://app.trycardinal.ai/login
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
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 3.2
  scored_at: '2026-08-17'
api_count: 0
artifact_total: 3
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/trycardinal-ai-domain-security.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/trycardinal-ai-llms.txt
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/trycardinal-ai-lifecycle.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://status.trycardinal.ai/
- group: commercial
  title: ''
  type: Plans
  url: plans/trycardinal-ai-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/trycardinal-ai-rate-limits.yml
- group: company
  title: ''
  type: Website
  url: https://www.trycardinal.com/
- group: company
  title: ''
  type: Blog
  url: https://www.trycardinal.com/blog
- group: company
  title: ''
  type: About
  url: https://www.trycardinal.com/team
- group: start
  title: ''
  type: Login
  url: https://app.trycardinal.ai/login
- group: operate
  title: ''
  type: Contact
  url: https://calendly.com/trycardinal/gtm-chat
- group: company
  title: ''
  type: Careers
  url: https://www.ycombinator.com/companies/trycardinal-ai/jobs
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/trycardinalai/
- group: company
  title: ''
  type: Twitter
  url: https://x.com/trycardinalai
coverage:
  checked: '2026-08-13'
  detail: 'Cardinal sells a half-software, half-service outbound sales product delivered through a customer application behind a Stytch login, not a developer product: contract discovery across four hosts on two domains found no OpenAPI, GraphQL SDL, AsyncAPI, MCP endpoint, agent card, webhook catalog, SDK, CLI or documentation site of any kind, there is no docs host to find (docs.trycardinal.ai and docs.trycardinal.com have no DNS record), the company''s own eleven-URL sitemap contains no docs, developers, pricing or legal path, and the one API hostname it still publishes (api.trycardinal.ai) is a dangling CNAME to a Render service that answers x-render-routing:no-server and presents no TLS certificate — the only public place the word "API" appears is as the name of the single component on its status page.'
  evidence:
  - status: 301
    url: https://trycardinal.ai/
  - status: 404
    url: https://www.trycardinal.com/openapi.json
  - status: 404
    url: https://www.trycardinal.com/llms.txt
  - status: 200
    url: https://www.trycardinal.com/sitemap.xml
  - status: 401
    url: https://app.trycardinal.ai/api
  - status: 404
    url: https://app.trycardinal.ai/openapi.json
  - status: 404
    url: https://app.trycardinal.ai/.well-known/agent-card.json
  - status: 409
    url: https://api.trycardinal.ai/
  - status: 404
    url: https://coordinator-api-wmxp.onrender.com/openapi.json
  - status: 200
    url: https://status.trycardinal.ai/api/v2/summary.json
  reason: no-developer-program
  state: none
created: '2026-07-17'
description: 'Cardinal is an AI platform for precision outbound sales — it markets itself as "revenue agents for high-growth companies" — built for go-to-market teams that want outbound to run as one engine instead of a stack of disconnected tools. Its agents build and refresh account lists from signals, monitor what prospects post and engage with, generate personalized snippets, and orchestrate end-to-end email and LinkedIn plays, while capturing inbound from website visitors, product signups and ad impressions. The company is a Y Combinator Winter 2026 company founded by Devishi Jha and Jianna Liu, based in San Francisco, and names Mintlify, Deepgram, Greptile, Giga and Luminai among its customers. Cardinal moved its primary web presence from trycardinal.ai to trycardinal.com during 2026: https://trycardinal.ai/ now HTTP 301s to https://www.trycardinal.com/ and the former deep pages on the .ai domain (/company, /product) return 404, though the company still runs its customer application,
  its email and its analytics identity on trycardinal.ai. The product is sold as half-software and half-service ("we wire into your existing stack and build agents around plays that already work for you"), delivered through a customer app at app.trycardinal.ai behind a Stytch login, with a Calendly GTM chat as the only publicly reachable entry point. It reads from and writes back to customer CRMs and says it adds a new integration every two weeks, but names none of them publicly and publishes no outbound API of its own: across four hosts on two domains this pass found no OpenAPI, GraphQL SDL, AsyncAPI, MCP server, agent card, webhook catalog, SDK, CLI, developer portal or documentation site. docs.trycardinal.ai does not resolve in DNS, api.trycardinal.ai is a dangling custom domain whose Render origin answers x-render-routing: no-server, and every /api/* path on the customer app returns HTTP 401 {"error":"Unauthorized"}.'
image: https://framerusercontent.com/assets/OZUI2MB2pSTkOci3gyWuOUWDoiQ.jpg
layout: provider
modified: '2026-08-13'
name: Cardinal
nav: Providers
network: true
overview: 'Cardinal is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Artificial Intelligence, Sales, Outbound Sales, and Sales Automation.


  Cardinal''s developer surface includes engineering blog and 13 more developer resources.'
plans:
- name: Trycardinal Ai Plans Pricing
  plan_count: 0
  slug: trycardinal-ai-plans-pricing
random_paper: 87
rate_limits:
- limit_count: 0
  name: Trycardinal Ai Rate Limits
  slug: trycardinal-ai-rate-limits
score:
  band: minimal
  composite: 10.9
  delta: 3.3
  facets:
    commercial_clarity: 13.2
    contract_quality: 0.0
    developer_ergonomics: 2.2
    discoverability: 57.4
    governance: 0.0
    operational_transparency: 15.8
  previous_composite: 7.6
  schema_version: 0.11.0
  scored_at: '2026-08-17'
  trend: flat
security:
- kind: domain-security
  name: Trycardinal Ai Domain Security
  slug: trycardinal-ai-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: trycardinal-ai
tags:
- Company
- Artificial Intelligence
- Sales
- Outbound Sales
- Sales Automation
- Sales Engagement
- Go-To-Market
- Revenue Operations
- AI Agents
- Lead Generation
- Machine Learning
website: https://www.trycardinal.com/
---
