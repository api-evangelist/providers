---
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
  url: security/stem-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://stemai.vc/
- group: start
  title: ''
  type: SignUp
  url: https://stemai.vc/apply
- group: other
  title: ''
  type: SecondaryMarket
  url: https://forgeglobal.com/stem-ai_stock/
coverage:
  checked: '2026-08-05'
  detail: StemAI is an accelerator and early-stage fund (Stem AI SAS, Paris) that writes $250k SAFEs into LLM-product founders; stemai.vc is a four-page Gatsby brochure site whose only interactive surface is an Airtable application form, so there is no product and nothing to expose as an API.
  evidence:
  - status: 200
    url: https://stemai.vc/
  - status: 404
    url: https://stemai.vc/openapi.json
  - status: 404
    url: https://stemai.vc/.well-known/agent-card.json
  - status: 404
    url: https://stemai.vc/llms.txt
  reason: not-a-software-company
  state: none
created: '2026-08-05'
description: StemAI (Stem AI SAS) is a Paris-based accelerator and early-stage investment program for founders building LLM-powered products. Its stated thesis is that large language models are already capable enough to build great products today, so the program backs product and user experience rather than research breakthroughs. Each accepted company receives a $250,000 SAFE investment, $350,000 in partner cloud credits, recurring checkpoints with AI advisors, help accessing follow-on funding, and a founder summit hosted in Paris. The program is led by Nicolas Granatino, with a board that includes Mehdi Ghissassi (AI71) and Severine Gregoire (Zebox Ventures), and advisors in residence drawn from Hugging Face, Datadog, InstaDeep, Dust, Photoroom, Helsing, Nabla, QuantHouse and Parrot. StemAI is a private company whose shares are quoted on the secondary markets (Forge, Hiive, EquityZen). It publishes no API, SDK, developer portal or machine-readable specification of any kind.
image: https://stemai.vc/icons/icon-512x512.png
layout: provider
modified: '2026-08-05'
name: Stem AI
nav: Providers
network: true
overview: 'Stem AI is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Venture Capital, Accelerator, Artificial Intelligence, and Large Language Models.


  Stem AI''s developer surface includes signup flow and 3 more developer resources.'
random_paper: 81
score:
  band: minimal
  composite: 7.6
  delta: 0.0
  facets:
    commercial_clarity: 13.2
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 7.6
  schema_version: 0.11.0
  scored_at: '2026-08-12'
  trend: flat
security:
- kind: domain-security
  name: Stem Domain Security
  slug: stem-domain-security
  summary_line: TLSv1.3
slug: stem
tags:
- Company
- Venture Capital
- Accelerator
- Artificial Intelligence
- Large Language Models
- Startups
- France
- Investment
website: https://stemai.vc/
---
