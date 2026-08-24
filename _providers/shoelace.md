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
  scored_at: '2026-08-24'
api_count: 0
artifact_total: 1
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/shoelace-domain-security.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/shoelace-llms.txt
- group: company
  title: ''
  type: Website
  url: https://shoelace.com
- group: company
  title: ''
  type: About
  url: https://shoelace.com/about
- group: company
  title: ''
  type: Blog
  url: https://shoelace.com/journal
- group: other
  title: ''
  type: CaseStudies
  url: https://shoelace.com/work
- group: operate
  title: ''
  type: Contact
  url: https://shoelace.com/contact
- group: other
  title: ''
  type: Resources
  url: https://shoelace.com/library
- group: other
  title: ''
  type: Glossary
  url: https://shoelace.com/library/glossary
coverage:
  checked: '2026-08-12'
  detail: Shoelace sells managed paid-media and retention campaign work, not software — its own llms.txt enumerates fifteen marketing pages and no developer surface, api./docs./developer.shoelace.com do not resolve, and the only OpenAPI reachable on the domain (https://shoelace.com/api/openapi.json) is the Base44 App Management API belonging to the platform the marketing site is built on.
  evidence:
  - status: 200
    url: https://shoelace.com/llms.txt
  - status: 200
    url: https://shoelace.com/api/openapi.json
  - status: 404
    url: https://shoelace.com/.well-known/agent-card.json
  - status: 0
    url: https://developer.shoelace.com
  reason: no-developer-program
  state: none
created: '2026-07-17'
description: Shoelace is an omni-channel growth marketing agency for direct-to-consumer (DTC) and e-commerce brands, founded in 2015 and trusted by 300+ brands. The team plans, creates, and optimizes paid acquisition across Meta, Google, TikTok and YouTube alongside email and SMS retention, performance creative, UGC, and in-house photo and video production. Shoelace operates as a managed growth partner delivering marketing services — it sells campaign management, not software, and publishes no developer API, SDK, webhook surface, or developer portal. This API Evangelist profile tracks the company as a 500 Global portfolio lead and captures its public web presence, its published llms.txt, and its domain-security posture.
image: https://media.base44.com/images/public/6a554b6210f2878725464b3e/f71197d73_logo.png
layout: provider
modified: '2026-08-12'
name: Shoelace
nav: Providers
network: true
overview: 'Shoelace is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Marketing, Growth Marketing, Direct to Consumer, and E-Commerce.


  Shoelace''s developer surface includes engineering blog and 8 more developer resources.'
random_paper: 17
score:
  band: minimal
  composite: 6.9
  delta: 0.0
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 6.9
  schema_version: 0.12.1
  scored_at: '2026-08-24'
  trend: flat
security:
- kind: domain-security
  name: Shoelace Domain Security
  slug: shoelace-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: shoelace
tags:
- Company
- Marketing
- Growth Marketing
- Direct to Consumer
- E-Commerce
- Advertising
- Paid Media
- Email Marketing
- Agency
website: https://shoelace.com
---
