---
api_count: 1
apis:
- description: An anonymous remote Model Context Protocol endpoint served on Agragene's own host and advertised in the company's llms.txt. Nine tools let an agent read business details, search site content, mint a v
  name: Agragene Site MCP
  slug: site-mcp
artifact_total: 6
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/agragene-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.agragene.com/
- group: company
  title: ''
  type: About
  url: https://www.agragene.com/about
- group: company
  title: ''
  type: Blog
  url: https://www.agragene.com/news
- group: company
  title: ''
  type: BlogRSS
  url: https://www.agragene.com/blog-feed.xml
- group: operate
  title: ''
  type: FAQ
  url: https://www.agragene.com/faq
- group: operate
  title: ''
  type: Support
  url: mailto:info@agragene.com
- group: company
  title: ''
  type: Careers
  url: https://www.agragene.com/careers
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/agragene-llms.txt
- group: agent
  title: ''
  type: MCPServer
  url: mcp/agragene-mcp.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/agragene-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/agragene-conventions.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/agragene-conformance.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/agragene-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/agragene-rate-limits.yml
created: '2026-09-12'
description: Agragene is an agricultural biotechnology company using CRISPR-based genome engineering to build Precision-Guided Sterile Insect Technology (pgSIT), a modern evolution of the sterile insect technique that breeds insect lines producing only sterile males. Released into a field, those males mate with wild female crop pests and produce no viable offspring, giving growers season-long local pest suppression without chemical pesticides or irradiation. Founded in San Diego in 2017 and now headquartered in St. Louis, Missouri, the company's first product, KNOCKOUT-SWD, targets Spotted Wing Drosophila — a pest behind more than $500M in annual US berry losses — with a limited launch stated for 2027. Agragene has no developer program and publishes no API product; its only machine-readable surface is an anonymous Wix site MCP endpoint plus a company-authored llms.txt.
image: https://static.wixstatic.com/media/252b8c_d34caf2c23cc4a398147d692f5ee7fc2~mv2.png/v1/fit/w_2500,h_1330,al_c/252b8c_d34caf2c23cc4a398147d692f5ee7fc2~mv2.png
layout: provider
mcp_servers:
- description: Agragene serves a live, unauthenticated remote MCP endpoint at https://www.agragene.com/_api/mcp, advertised in the company's own /llms.txt under an "AI Agent Access" section. An anonymous JSON-RPC in
  name: Agragene Site MCP manifest
  slug: agragene-site-mcp-manifest
modified: '2026-09-12'
name: Agragene
nav: Providers
network: true
overview: 'Agragene publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Agriculture, Agtech, Biotechnology, Gene Editing, and Pest Control.


  Agragene''s developer surface includes engineering blog, FAQ, support, authentication, and 11 more developer resources.'
plans:
- name: Agragene Plans Pricing
  plan_count: 0
  slug: agragene-plans-pricing
random_paper: 7
rate_limits:
- limit_count: 0
  name: Agragene Rate Limits
  slug: agragene-rate-limits
security:
- kind: authentication
  name: Agragene Authentication
  slug: agragene-authentication
  summary_line: 2 schemes
- kind: domain-security
  name: Agragene Domain Security
  slug: agragene-domain-security
  summary_line: TLSv1.3 · HSTS
slug: agragene
tags:
- Agriculture
- Agtech
- Biotechnology
- Gene Editing
- Pest Control
- Sustainability
- Food and Beverage
- Life Sciences
- Company
website: https://www.agragene.com/
---
