---
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
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 0.0
  scored_at: '2026-09-01'
api_count: 0
artifact_total: 1
common:
- group: company
  title: ''
  type: Website
  url: https://huckberry.com/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Huckberry
- group: operate
  title: ''
  type: Support
  url: https://help.huckberry.com/hc/en-us
- group: commercial
  title: ''
  type: TermsOfService
  url: https://huckberry.com/terms
- group: auth
  title: ''
  type: DomainSecurity
  url: security/huckberry-domain-security.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/huckberry-llms.txt
coverage:
  checked: '2026-08-22'
  detail: 'Huckberry is a direct-to-consumer retailer with no developer program: api., developer., developers., partners., status. and mcp.huckberry.com do not resolve in DNS, its public GitHub organization (Huckberry Inc) is eight repositories of which seven are forks of third-party Ruby e-commerce gems, affiliate integration is outsourced to Partnerize, and the only anonymously readable machine surface on any Huckberry host is Zendesk''s own Help Center API on the help.huckberry.com tenant; huckberry.com itself answers every path — /llms.txt, /openapi.json, /graphql, /api/mcp and all /.well-known/* — with an identical HTTP 403 Cloudflare managed challenge, so absence on that host is unconfirmed rather than measured.'
  evidence:
  - status: 403
    url: https://huckberry.com/.well-known/agent-card.json
  - status: 403
    url: https://huckberry.com/openapi.json
  - status: 404
    url: https://help.huckberry.com/.well-known/api-catalog
  - status: 200
    url: https://help.huckberry.com/api/v2/help_center/en-us/articles.json
  - status: 200
    url: https://api.github.com/orgs/Huckberry
  reason: no-developer-program
  state: none
created: '2026-08-22'
description: 'Huckberry is an American direct-to-consumer online retailer of men''s apparel, outdoor gear and lifestyle goods, founded in 2010 by Andy Forch and Richard Greiner and headquartered in San Francisco with offices in Austin and Columbus. It pairs a first-party e-commerce storefront with a large editorial operation — the Huckberry Journal — and an in-house brand portfolio, selling an "everyday adventure" assortment that sits between traditional outdoor retail and menswear. Huckberry is a retailer, not a software vendor: it publishes no developer program, no public API, no SDK and no machine-readable contract. Its public GitHub organization (Huckberry Inc) holds eight repositories, seven of them forks of third-party Ruby e-commerce gems — Solidus AvaTax, Affirm, Paperclip, omniauth-slack — which evidence a self-hosted Ruby storefront rather than a published platform. Partner and affiliate integration is outsourced to the Partnerize network, and customer self-service runs on a Zendesk
  help center tenant at help.huckberry.com.'
layout: provider
modified: '2026-08-22'
name: Huckberry
nav: Providers
network: true
overview: 'Huckberry is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, E-Commerce, Retail, Direct to Consumer, and Apparel.


  Huckberry''s developer surface includes support and 5 more developer resources.'
random_paper: 9
score:
  band: minimal
  composite: 8.0
  coverage:
    artifact_dirs: 3
    catalog_gap: 90.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 10.5
    commercial_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 4.8
    discoverability: 46.3
    governance: 0.0
    operational_transparency: 2.6
  previous_composite: 8.0
  schema_version: 0.17.2
  scored_at: '2026-09-01'
  trend: flat
security:
- kind: domain-security
  name: Huckberry Domain Security
  slug: huckberry-domain-security
  summary_line: TLSv1.3 · DMARC
slug: huckberry
tags:
- Company
- E-Commerce
- Retail
- Direct to Consumer
- Apparel
- Outdoor
- Consumer Goods
- Media
website: https://huckberry.com/
---
