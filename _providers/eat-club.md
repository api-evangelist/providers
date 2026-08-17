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
  url: security/eat-club-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.eatclub.com/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/eatclub
- group: operate
  title: ''
  type: Support
  url: https://www.eatclub.com/faq
- group: start
  title: ''
  type: Login
  url: https://www.eatclub.com/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.eatclub.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.eatclub.com/privacy
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/eat-club
- group: other
  title: ''
  type: SecondaryMarket
  url: https://forgeglobal.com/eat-club_stock/
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/eat-club-llms.txt
coverage:
  checked: '2026-08-12'
  detail: 'EAT Club ships only an end-user ordering product: every developer-shaped host (api., developer., developers., docs., app., portal., admin.eatclub.com) is NXDOMAIN, all seven /.well-known/ paths and every spec path on www.eatclub.com return the application''s own 404 page, and the sole JSON surface — the undocumented, session-authenticated backend of the "aphrodite" ordering SPA at https://www.eatclub.com/api/v3/ — rejects unauthenticated calls with "Unauthenticated user with no location in session" and has no reference, no key issuance and no terms covering programmatic access, so there is no developer program to profile.'
  evidence:
  - status: 404
    url: https://www.eatclub.com/openapi.json
  - status: 404
    url: https://www.eatclub.com/swagger.json
  - status: 404
    url: https://www.eatclub.com/graphql
  - status: 404
    url: https://www.eatclub.com/.well-known/security.txt
  - status: 404
    url: https://www.eatclub.com/.well-known/agent-card.json
  - status: 404
    url: https://www.eatclub.com/.well-known/agent.json
  - status: 404
    url: https://www.eatclub.com/llms.txt
  - status: 400
    url: https://www.eatclub.com/api/v3/menu-dates/
  - status: 404
    url: https://www.eatclub.com/pricing
  reason: no-developer-program
  state: none
created: '2026-08-12'
description: EAT Club is a corporate meal-delivery platform founded in 2010 in Redwood City, California by Kevin Yang and Rodrigo Santibanez, built around the idea of a "virtual cafeteria" for offices with no on-site dining. Instead of tray-style catering, each employee picks an individually packaged meal from a rotating daily menu produced by EAT Club's own kitchens and restaurant partners, and every order for a building arrives in one synchronized delivery. The company markets the program as an employee lunch benefit and reports 21 million meals delivered to roughly 1,145 companies across nine cities. Compass Group USA acquired EAT Club in October 2020 and folded its ordering, production and delivery technology into Compass Digital Labs, where it now underpins workplace, education and healthcare dining accounts across the US and Canada. The consumer-facing product is a React ordering app served from www.eatclub.com; EAT Club publishes no developer program, no API reference, no SDK and
  no machine-readable contract of any kind.
image: https://cdn.prod.website-files.com/6324aa1c42c9fa2cf506f5fb/6324c038b740701b09ee39c6_EATClub-logo.png
layout: provider
modified: '2026-08-12'
name: EAT Club
nav: Providers
network: true
overview: 'EAT Club is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Food Service, Corporate Catering, Meal Delivery, and Food Tech.


  EAT Club''s developer surface includes support and 9 more developer resources.'
plans:
- name: Eat Club Plans Pricing
  plan_count: 0
  slug: eat-club-plans-pricing
random_paper: 36
rate_limits:
- limit_count: 0
  name: Eat Club Rate Limits
  slug: eat-club-rate-limits
score:
  band: emerging
  composite: 14.1
  delta: 0.0
  facets:
    commercial_clarity: 34.2
    contract_quality: 0.0
    developer_ergonomics: 4.3
    discoverability: 57.4
    governance: 0.0
    operational_transparency: 5.3
  previous_composite: 14.1
  schema_version: 0.11.0
  scored_at: '2026-08-17'
  trend: flat
security:
- kind: domain-security
  name: Eat Club Domain Security
  slug: eat-club-domain-security
  summary_line: TLSv1.2 · HSTS · DMARC
slug: eat-club
tags:
- Company
- Food Service
- Corporate Catering
- Meal Delivery
- Food Tech
- Workplace
- Employee Benefits
- Logistics
- Hospitality
website: https://www.eatclub.com/
---
