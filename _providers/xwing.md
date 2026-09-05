---
agent_readiness:
  band: agent-aware
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
    mcp_server: documented
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 6.0
  scored_at: '2026-09-04'
api_count: 0
artifact_total: 4
common:
- group: company
  title: ''
  type: Website
  url: https://www.xwing.com/
- group: company
  title: ''
  type: About
  url: https://www.xwing.com/about
- group: company
  title: ''
  type: Careers
  url: https://www.xwing.com/careers
- group: company
  title: ''
  type: Blog
  url: https://www.xwing.com/blog
- group: company
  title: ''
  type: BlogRSS
  url: https://www.xwing.com/blog-feed.xml
- group: company
  title: ''
  type: Newsroom
  url: https://www.xwing.com/news-1-1
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/xwing-llms.txt
- group: agent
  title: ''
  type: MCPServer
  url: mcp/xwing-mcp.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/xwing-domain-security.yml
coverage:
  checked: '2026-09-04'
  detail: Xwing sold embedded aircraft autonomy (Superpilot) and a Part 135 cargo operation, never a developer product — www.xwing.com has no /developers or /api page (both 404), every OpenAPI/Swagger/GraphQL path returns the Wix error shell, and the site's only machine-readable surfaces are the llms.txt and /_api/mcp endpoint that Wix generates for every site it hosts.
  evidence:
  - status: 404
    url: https://www.xwing.com/developers
  - status: 404
    url: https://www.xwing.com/api
  - status: 400
    url: https://www.xwing.com/openapi.json
  - status: 404
    url: https://www.xwing.com/graphql
  - status: 200
    url: https://www.xwing.com/llms.txt
  - status: 200
    url: https://www.xwing.com/_api/mcp
  reason: no-developer-program
  state: none
created: '2026-09-04'
description: Xwing, Inc. is a San Francisco and Concord, California aviation company founded in 2016 that built Superpilot, a modular retrofit autonomy system enabling ground-supervised, uncrewed gate-to-gate flight on conventional fixed-wing aircraft. Flying a Cessna 208B Grand Caravan testbed, Xwing completed more than 250 fully autonomous flights and over 500 auto-landings, and in April 2023 became the first company to receive an FAA project designation toward certification of a large unmanned aircraft system. Joby Aviation acquired Xwing's autonomy division in June 2024; Xwing retained its Part 135 air cargo operation, and www.xwing.com is now an archived marketing site pointing visitors to Joby. Xwing never published a developer program, public API, SDK or machine-readable contract; the domain's only agent-readable surfaces are the llms.txt and Site MCP endpoint that Wix generates for every site it hosts.
image: https://static.wixstatic.com/media/38a3e6_e4ab1806ac414f0181a3a0b1b32ee29f~mv2.png
layout: provider
mcp_servers:
- description: ''
  name: Site Visitor Assistant for site "Xwing"
  slug: site-visitor-assistant-for-site-xwing
modified: '2026-09-04'
name: Xwing
nav: Providers
network: true
overview: 'Xwing is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Aviation, Autonomy, Aerospace, and Unmanned Aircraft.


  Xwing''s developer surface includes engineering blog and 8 more developer resources.'
plans:
- name: Xwing Plans Pricing
  plan_count: 0
  slug: xwing-plans-pricing
random_paper: 11
rate_limits:
- limit_count: 0
  name: Xwing Rate Limits
  slug: xwing-rate-limits
score:
  band: minimal
  composite: 5.5
  coverage:
    artifact_dirs: 7
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 2.4
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 0.0
  provenance:
    mcp: first-party
  schema_version: 0.18.3
  scored_at: '2026-09-04'
security:
- kind: domain-security
  name: Xwing Domain Security
  slug: xwing-domain-security
  summary_line: TLSv1.3 · HSTS
slug: xwing
tags:
- Company
- Aviation
- Autonomy
- Aerospace
- Unmanned Aircraft
- Air Cargo
- Defense
- Robotics
- Acquired
website: https://www.xwing.com/
---
