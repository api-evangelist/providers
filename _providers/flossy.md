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
- group: company
  title: ''
  type: Website
  url: https://www.flossy.com/
- group: company
  title: ''
  type: Blog
  url: https://www.flossy.com/blog
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.flossy.com/tos
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.flossy.com/privacy
- group: start
  title: ''
  type: Login
  url: https://hq.flossy.com/
- group: operate
  title: ''
  type: Support
  url: mailto:hello@flossy.com
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/flossy/
- group: company
  title: ''
  type: Careers
  url: https://flossy.breezy.hr/
- group: design
  title: ''
  type: Components
  url: components/flossy-components.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/flossy-domain-security.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/flossy-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/flossy-rate-limits.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/flossy-llms.txt
coverage:
  checked: '2026-08-16'
  detail: 'Flossy ships AI agents only as an end-user product for practices — there is no developer portal, API reference or spec anywhere on its surface: /developers, /developer, /api and /docs all 404, developer.flossy.com and docs.flossy.com do not resolve, api.flossy.com is a dangling CNAME to a Heroku Private Space with no public A record, and the one live API host (scheduler-api.flossy.com) answers 200 on its root but 404s every OpenAPI/Swagger/docs path and requires an x-api-key.'
  evidence:
  - status: 404
    url: https://www.flossy.com/developers
  - status: 404
    url: https://www.flossy.com/docs
  - status: 404
    url: https://scheduler-api.flossy.com/openapi.json
  - status: 404
    url: https://www.flossy.com/.well-known/agent-card.json
  - status: 200
    url: https://hq.flossy.com/fiona-widget.js
  reason: no-developer-program
  state: none
created: '2026-08-16'
description: 'Flossy is a Santa Monica, California healthcare technology company that builds AI agents ("AI coworkers") for dental practices, veterinary clinics and med spas. Its named agents cover front-office and revenue-cycle work: Fiona handles inbound and outbound patient communication and scheduling across phone, SMS and web chat; Betsy scores call-center quality and marketing performance; Michael captures insurance, verifies benefits and surfaces billing insights; and Reid forecasts revenue and optimizes schedule capacity and staffing. FlossyHQ is the operator console the practice works in, and Agent Builder lets practices assemble custom agents. Founded in 2020 by Miles Beckett and Steve Seigel, Flossy began as a pay-as-you-go dental care marketplace and has since repositioned around agentic automation for practice operations. Flossy publishes no public developer program, API reference or machine-readable specification; the one publicly reachable first-party integration surface is
  the embeddable Fiona web-chat widget.'
image: https://cdn.prod.website-files.com/5fdcd779f4e21f75c74a0997/67cb891c40136f07a823f79b_og-flossy.png
layout: provider
modified: '2026-08-16'
name: Flossy
nav: Providers
network: true
overview: 'Flossy is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Artificial Intelligence, AI Agents, Health Care, and Dental.


  Flossy''s developer surface includes engineering blog, support, and 11 more developer resources.'
plans:
- name: Flossy Plans Pricing
  plan_count: 0
  slug: flossy-plans-pricing
random_paper: 0
rate_limits:
- limit_count: 0
  name: Flossy Rate Limits
  slug: flossy-rate-limits
score:
  band: emerging
  composite: 13.6
  delta: -1.8
  facets:
    access_clarity: 27.6
    commercial_clarity: 27.6
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 7.1
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 15.4
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 17.5
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: flat
security:
- kind: domain-security
  name: Flossy Domain Security
  slug: flossy-domain-security
  summary_line: TLSv1.3 · DMARC
slug: flossy
tags:
- Company
- Artificial Intelligence
- AI Agents
- Health Care
- Dental
- Veterinary
- Scheduling
- Voice
- Practice Management
- Revenue Cycle
website: https://www.flossy.com/
---
