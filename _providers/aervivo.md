---
api_count: 0
artifact_total: 6
common:
- group: company
  title: ''
  type: Website
  url: https://www.aervivo.com/
- group: company
  title: ''
  type: About
  url: https://www.aervivo.com/company
- group: company
  title: ''
  type: Blog
  url: https://www.aervivo.com/newsroom
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.aervivo.com/privacy-policy
- group: start
  title: ''
  type: Login
  url: https://portal.aervivo.com/
- group: company
  title: ''
  type: Careers
  url: https://www.aervivo.com/careers
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/aervivo-llms.txt
- group: agent
  title: ''
  type: MCPServer
  url: mcp/aervivo-mcp.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/aervivo-well-known.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/aervivo-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/aervivo-scopes.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/aervivo-conformance.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/aervivo-domain-security.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/aervivo-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/aervivo-rate-limits.yml
coverage:
  checked: '2026-09-12'
  detail: Aervivo markets a "modularized, API architecture" for its Aervivo Cloud OSS/BSS but runs no developer site at all; its only application surface, portal.aervivo.com, is a Salesforce Experience Cloud community that redirects every anonymous request to a bare username/password SiteLogin, and api/docs/developer.aervivo.com do not resolve.
  evidence:
  - status: 200
    url: https://portal.aervivo.com/
  - status: 200
    url: https://portal.aervivo.com/SiteLogin
  - status: 400
    url: https://www.aervivo.com/openapi.json
  - status: 404
    url: https://www.aervivo.com/api-docs
  reason: partner-login
  state: gated
created: '2026-09-12'
description: Aervivo, Inc. is a San Diego, California company founded in 2020 that sells the Aervivo Connectivity Platform, a cloud operating system paired with the Aervivo Hybrid Edge ecosystem of fiber and fixed-wireless networking equipment (AerHub, AerSwitch). It lets multifamily property owners, fiber overbuilders, WISPs and incumbent ISPs deploy and operate community-wide gigabit managed WiFi without a full fiber build, bundling a virtualized core network with cloud-based OSS and BSS. Aervivo publishes no developer portal, API reference or machine-readable contract; its partner surface is a Salesforce Experience Cloud portal behind a login at portal.aervivo.com, and the only anonymous machine surface on its own hosts is the Wix Site MCP endpoint its marketing site serves.
image: https://static.wixstatic.com/media/91fe64_ffda9adaafb74ce3b07da6de65ed20cd~mv2.png/v1/fill/w_2039,h_1102,al_c/91fe64_ffda9adaafb74ce3b07da6de65ed20cd~mv2.png
layout: provider
mcp_servers:
- description: Aervivo's marketing site (www.aervivo.com) is built on Wix, and Wix serves a Model Context Protocol endpoint at /_api/mcp on the site's own host. A tools/list call returned HTTP 200 with nine tools, s
  name: Aervivo Site MCP (Wix Site MCP runtime)
  slug: aervivo-site-mcp-wix-site-mcp-runtime
modified: '2026-09-12'
name: Aervivo
nav: Providers
network: true
overview: 'Aervivo is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Telecommunications, Internet Service Provider, Fixed Wireless, and Networking.


  Aervivo''s developer surface includes engineering blog, authentication, and 13 more developer resources.'
plans:
- name: Aervivo Plans Pricing
  plan_count: 0
  slug: aervivo-plans-pricing
random_paper: 8
rate_limits:
- limit_count: 0
  name: Aervivo Rate Limits
  slug: aervivo-rate-limits
scopes:
- name: Aervivo Scopes
  scope_count: 36
  slug: aervivo-scopes
  summary_line: 36 scopes
security:
- kind: authentication
  name: Aervivo Authentication
  slug: aervivo-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Aervivo Domain Security
  slug: aervivo-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC
slug: aervivo
tags:
- Company
- Telecommunications
- Internet Service Provider
- Fixed Wireless
- Networking
- WiFi
- OSS BSS
- Connectivity
- Real Estate
- Cloud
website: https://www.aervivo.com/
---
