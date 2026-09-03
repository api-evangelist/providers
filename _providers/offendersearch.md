---
api_count: 1
apis:
- description: REST API for national sex-offender screening; API-key authenticated, JSON responses, synchronous and asynchronous search across all 58 US registries.
  name: Offendersearch API
  slug: offendersearch-api
artifact_total: 7
asyncapis:
- description: ''
  name: Offendersearch Webhooks
  slug: offendersearch-webhooks
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/offendersearch-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/offendersearch-authentication.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/offendersearch-llms.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/offendersearch-well-known.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/offendersearch-mcp.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://offendersearch.app/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://offendersearch.app/privacy
- group: operate
  title: ''
  type: Support
  url: https://offendersearch.app/contact
- group: company
  title: ''
  type: Blog
  url: https://offendersearch.app/blog
- group: start
  title: ''
  type: SignUp
  url: https://offendersearch.app/sign-up
- group: start
  title: ''
  type: Login
  url: https://offendersearch.app/sign-in
created: '2026-08-23'
description: A commercial REST API (and private-beta MCP server) for nationwide US sex-offender registry screening, searching 58 US registries through one API with scored matches and per-source provenance.
image: https://offendersearch.app/opengraph-image.png
layout: provider
mcp_servers:
- description: 'Offendersearch operates an official hosted (remote) MCP server. The marketing page (/mcp-server) describes it as private beta — "the hosted endpoint is not yet open to self-serve signups" — and shows '
  name: Offendersearch MCP Server
  slug: offendersearch-mcp-server
modified: '2026-09-03'
name: Offendersearch
nav: Providers
network: true
overview: 'Offendersearch publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Background Screening, Identity & risk, Trust and Safety, Public Records, and Criminal data.


  The Offendersearch catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Offendersearch''s developer surface includes authentication, support, engineering blog, signup flow, and 8 more developer resources.'
plans:
- name: Offendersearch Plans Pricing
  plan_count: 4
  slug: offendersearch-plans-pricing
random_paper: 1
rate_limits:
- limit_count: 0
  name: Offendersearch Rate Limits
  slug: offendersearch-rate-limits
screenshot: https://raw.githubusercontent.com/api-evangelist/offendersearch/refs/heads/main/screenshots/offendersearch-2026-09-02T150825.png
security:
- kind: authentication
  name: Offendersearch Authentication
  slug: offendersearch-authentication
  summary_line: apiKey/http · 4 schemes
- kind: domain-security
  name: Offendersearch Domain Security
  slug: offendersearch-domain-security
  summary_line: TLSv1.3 · DMARC
slug: offendersearch
tags:
- Background Screening
- Identity & risk
- Trust and Safety
- Public Records
- Criminal data
- Compliance
- Sex-offender registry data
- Staffing & recruiting
- Tenant Screening
- Healthcare
- Gig marketplaces
---
