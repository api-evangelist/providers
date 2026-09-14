---
api_count: 1
apis:
- description: Agent-native content surface exposing machine-readable summaries via llms.txt and llms-full.txt for AI assistants and crawlers to help players find Lineage 2 servers.
  name: L2Calendar Agent-Native Content
  slug: l2calendar-agent-native-content
artifact_total: 3
common:
- group: company
  title: ''
  type: Website
  url: https://l2calendar.com
- group: auth
  title: ''
  type: DomainSecurity
  url: security/l2calendar-domain-security.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/l2calendar-plans-pricing.yml
- group: commercial
  title: ''
  type: Pricing
  url: https://l2calendar.com/addnews_vip
- group: company
  title: ''
  type: Blog
  url: https://l2calendar.com/blog
- group: start
  title: ''
  type: SignUp
  url: https://l2calendar.com/addnews
coverage:
  checked: '2026-09-13'
  detail: L2Calendar is a Next.js content platform that publishes llms.txt and llms-full.txt for agents but exposes no public API; every OpenAPI/GraphQL/MCP and /.well-known probe 404s and the only /api/ path is an internal Next.js route that 301-redirects and is Disallowed in robots.txt.
  evidence:
  - status: 404
    url: https://l2calendar.com/openapi.json
  - status: 404
    url: https://l2calendar.com/graphql
  - status: 301
    url: https://l2calendar.com/api/
  - status: 200
    url: https://l2calendar.com/llms.txt
  reason: no-developer-program
  state: none
created: '2026-09-12'
description: Multilingual Lineage 2 private server listing platform tracking upcoming and past server openings across every game chronicle, with filters by chronicle, rates, labels, and opening date. Server owners publish announcements with optional VIP placement.
image: https://l2calendar.com/images/logo.png
layout: provider
modified: '2026-09-13'
name: L2Calendar
nav: Providers
network: true
overview: 'L2Calendar publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include lineage2, mmorpg, game-servers, gaming, and server-listing.


  L2Calendar''s developer surface includes pricing, engineering blog, signup flow, and 3 more developer resources.'
plans:
- name: L2Calendar Plans Pricing
  plan_count: 5
  slug: l2calendar-plans-pricing
random_paper: 18
security:
- kind: domain-security
  name: L2Calendar Domain Security
  slug: l2calendar-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: l2calendar
tags:
- lineage2
- mmorpg
- game-servers
- gaming
- server-listing
- llms-txt
- agent-native-content
website: https://l2calendar.com
---
