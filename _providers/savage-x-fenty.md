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
  scored_at: '2026-08-17'
api_count: 0
artifact_total: 1
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/savage-x-fenty-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.savagex.com/
- group: operate
  title: ''
  type: Support
  url: https://help.savagex.com/hc/en-us
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.savagex.com/termsandconditions
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.savagex.com/privacy
coverage:
  checked: '2026-08-05'
  detail: 'Savage X Fenty ships only an end-user shopping site and mobile apps: its one first-party API host, the AWS API Gateway at gateway.savagex.com, answers {"message":"Forbidden"} to every path including /openapi.json and /.well-known/*, its docs.savagex.com GitHub Pages site 302s into TechStyle''s private GitHub Enterprise SSO (github.com/enterprises/techstyle-emu), developer.savagex.com does not resolve, and there is no public GitHub org — so there is no developer program to profile, only internal plumbing.'
  evidence:
  - status: 403
    url: https://gateway.savagex.com/openapi.json
  - status: 403
    url: https://gateway.savagex.com/.well-known/agent-card.json
  - status: 200
    url: https://docs.savagex.com/
  - status: 404
    url: https://www.savagex.com/robots.txt
  - status: 404
    url: https://www.savagex.com/.well-known/security.txt
  - status: 404
    url: https://www.savagex.com/.well-known/agent-card.json
  - status: 404
    url: https://www.savagex.com/.well-known/agent.json
  - status: 404
    url: https://api.github.com/orgs/savagex
  reason: no-developer-program
  state: none
created: '2026-08-05'
description: Savage X Fenty is a direct-to-consumer lingerie, intimates, sleepwear and loungewear brand co-founded by Rihanna in 2018 and operated as part of TechStyle Fashion Group. It sells through savagex.com and its own iOS and Android shopping apps on a membership model — Savage X Rewards — where members unlock member pricing and store credits, or "skip the month" between the 1st and 5th to avoid the charge. The commerce stack is a custom TechStyle backend fronted by Next.js and Builder.io, behind a Cloudflare edge, with an AWS API Gateway at gateway.savagex.com. Savage X Fenty publishes no public developer program, no API reference, and no machine-readable contract; its first-party API gateway and its engineering docs site are both closed to the public.
image: https://cdn.builder.io/api/v1/image/assets%2F380497d2350243c7a3f60aeae82dfc2d%2F20c959ce5dc147ddae2db44ec7c2bce2
layout: provider
modified: '2026-08-05'
name: Savage X Fenty
nav: Providers
network: true
overview: 'Savage X Fenty is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Fashion, Apparel, Lingerie, and Retail.


  Savage X Fenty''s developer surface includes support and 4 more developer resources.'
random_paper: 50
score:
  band: minimal
  composite: 10.1
  delta: 0.0
  facets:
    commercial_clarity: 21.1
    contract_quality: 0.0
    developer_ergonomics: 4.3
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 10.1
  schema_version: 0.11.0
  scored_at: '2026-08-17'
  trend: flat
security:
- kind: domain-security
  name: Savage X Fenty Domain Security
  slug: savage-x-fenty-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: savage-x-fenty
tags:
- Company
- Fashion
- Apparel
- Lingerie
- Retail
- E-commerce
- Direct to Consumer
- Subscription
website: https://www.savagex.com/
---
