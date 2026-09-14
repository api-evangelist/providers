---
api_count: 1
apis:
- description: The agent-facing commerce surface of the abcoffee online store. Implemented as Shopify's native Universal Commerce Protocol (UCP) service and exposed over MCP at abcoffee's own domain, it offers 13 to
  name: abcoffee Agentic Commerce (UCP over MCP)
  slug: abcoffee-agentic-commerce-ucp-over-mcp
artifact_total: 7
common:
- group: build
  title: ''
  type: Packages
  url: packages/abcoffee-packages.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/abcoffee-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://abcoffee.in
- group: docs
  title: ''
  type: Documentation
  url: https://abcoffee.in/agents.md
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/abcoffee-llms.txt
- group: agent
  title: ''
  type: MCPServer
  url: mcp/abcoffee-mcp.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/abcoffee-well-known.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/abcoffee-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/abcoffee-scopes.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/abcoffee-conformance.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/abcoffee-conventions.yml
- group: design
  title: ''
  type: Idempotency
  url: conventions/abcoffee-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/abcoffee-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/abcoffee-lifecycle.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/abcoffee-data-model.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/abcoffee-rate-limits.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/abcoffee-plans-pricing.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: operate
  title: ''
  type: Support
  url: https://abcoffee.in/pages/contact
- group: company
  title: ''
  type: Blog
  url: https://abcoffee.in/blogs/news
- group: start
  title: ''
  type: SignUp
  url: https://abcoffee.in/account/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://abcoffee.in/policies/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://abcoffee.in/policies/privacy-policy
created: '2026-09-05'
description: abcoffee (abCoffee, legally AB Coffee India) is a Mumbai-founded, tech-enabled grab-and-go specialty coffee chain operating 90+ kiosk, high-street and corporate outlets across Mumbai, Delhi-NCR and Bengaluru. Founded in 2022 by Abhijeet Anand, the company sources beans directly from Indian growing regions such as Chikmagalur and sells through its own takeaway mobile app and subscription ecosystem alongside its stores. Its public machine-readable surface is not a developer API program but an agentic-commerce one - the abcoffee.in storefront runs on Shopify and publishes an llms.txt/agents.md agent instruction document, a Universal Commerce Protocol (UCP) merchant profile at /.well-known/ucp, OpenID Connect and OAuth 2.0 discovery metadata for Shopify Customer Accounts, and a live, anonymously-listable MCP endpoint at /api/ucp/mcp exposing 13 catalog, cart, checkout and order tools.
image: https://abcoffee.in/cdn/shop/t/24/assets/favicon-512.png
layout: provider
mcp_servers:
- description: ''
  name: Abcoffee MCP Server
  slug: abcoffee-mcp-server
modified: '2026-09-05'
name: Abcoffee
nav: Providers
network: true
overview: 'Abcoffee publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Coffee, Food and Beverage, Retail, and Commerce.


  Abcoffee''s developer surface includes documentation, authentication, support, engineering blog, signup flow, and 18 more developer resources.'
plans:
- name: Abcoffee Plans Pricing
  plan_count: 0
  slug: abcoffee-plans-pricing
random_paper: 13
rate_limits:
- limit_count: 0
  name: Abcoffee Rate Limits
  slug: abcoffee-rate-limits
scopes:
- name: Abcoffee Scopes
  scope_count: 4
  slug: abcoffee-scopes
  summary_line: 4 scopes · authorizationCode
security:
- kind: authentication
  name: Abcoffee Authentication
  slug: abcoffee-authentication
  summary_line: oauth2/openIdConnect/http · 3 schemes
- kind: domain-security
  name: Abcoffee Domain Security
  slug: abcoffee-domain-security
  summary_line: TLSv1.3 · HSTS
slug: abcoffee
tags:
- Company
- Coffee
- Food and Beverage
- Retail
- Commerce
- Agentic Commerce
- MCP
- Universal Commerce Protocol
- Shopify
- India
- Subscriptions
website: https://abcoffee.in
---
