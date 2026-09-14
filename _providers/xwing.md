---
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
