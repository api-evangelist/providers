---
api_count: 1
apis:
- description: The agent-facing commerce surface of the 4th & Heart online store, implemented by Shopify's native Universal Commerce Protocol support on the merchant's own domain. A remote MCP server at https://four
  name: 4th & Heart Agentic Commerce (UCP / MCP)
  slug: 4th-heart-commerce
artifact_total: 7
common:
- group: company
  title: ''
  type: Website
  url: https://fourthandheart.com/
- group: docs
  title: ''
  type: Documentation
  url: https://fourthandheart.com/agents.md
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/4th-heart-llms.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/4th-heart-well-known.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/4th-heart-mcp.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/4th-heart-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/4th-heart-lifecycle.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/4th-heart-domain-security.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/4th-heart-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/4th-heart-rate-limits.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: company
  title: ''
  type: Blog
  url: https://fourthandheart.com/blogs/recipes
- group: operate
  title: ''
  type: Support
  url: https://fourthandheart.com/pages/contact-us
- group: start
  title: ''
  type: SignUp
  url: https://fourthandheart.com/account/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://fourthandheart.com/policies/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://fourthandheart.com/policies/privacy-policy
created: '2026-09-05'
description: '4th & Heart is a California-based consumer packaged goods company that makes grass-fed, pasture-raised ghee (clarified butter) and ghee-based spreads, sold direct-to-consumer from its own Shopify storefront at fourthandheart.com and through national grocery retail. It is not a software vendor and publishes no developer program, but the storefront exposes a real, unauthenticated agent-commerce surface: a Universal Commerce Protocol (UCP) merchant profile at /.well-known/ucp, a live Model Context Protocol server at /api/ucp/mcp serving 13 catalog, cart, checkout and order tools with full JSON Schema, an /llms.txt and /agents.md agent instruction document, and Shopify customer-account OAuth 2.0 / OpenID Connect discovery metadata on its own domain.'
image: https://fourthandheart.com/cdn/shop/files/4thandHeartGhee.png?v=1730292913
layout: provider
mcp_servers:
- description: ''
  name: 4th & Heart MCP Server
  slug: 4th-heart-mcp-server
modified: '2026-09-05'
name: 4th & Heart
nav: Providers
network: true
overview: '4th & Heart publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Food and Beverage, Consumer Packaged Goods, Retail, and E-Commerce.


  4th & Heart''s developer surface includes documentation, engineering blog, support, signup flow, and 12 more developer resources.'
plans:
- name: 4Th Heart Plans Pricing
  plan_count: 0
  slug: 4th-heart-plans-pricing
random_paper: 9
rate_limits:
- limit_count: 0
  name: 4Th Heart Rate Limits
  slug: 4th-heart-rate-limits
scopes:
- name: 4Th Heart Scopes
  scope_count: 4
  slug: 4th-heart-scopes
  summary_line: 4 scopes · authorizationCode
security:
- kind: authentication
  name: 4Th Heart Authentication
  slug: 4th-heart-authentication
  summary_line: none/oauth2/openIdConnect · 4 schemes
- kind: domain-security
  name: 4Th Heart Domain Security
  slug: 4th-heart-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: 4th-heart
tags:
- Company
- Food and Beverage
- Consumer Packaged Goods
- Retail
- E-Commerce
- Agentic Commerce
- Universal Commerce Protocol
- Model Context Protocol
- Shopify
- Direct to Consumer
website: https://fourthandheart.com/
---
