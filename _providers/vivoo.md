---
access_model:
  confidence: medium
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - authentication
  trial: false
  try_now: false
api_count: 1
apis:
- description: 'Hosted Universal Commerce Protocol (UCP) shopping MCP server exposed natively by the Shopify-hosted Vivoo storefront: agent-driven catalog search, cart, and buyer-approved checkout. Checkout requires '
  name: Vivoo UCP Shopping (MCP)
  slug: vivoo-ucp-shopping-mcp
artifact_total: 5
common:
- group: company
  title: ''
  type: Website
  url: https://vivoo.io
- group: agent
  title: ''
  type: MCPServer
  url: mcp/vivoo-mcp.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/vivoo-well-known.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/vivoo-llms.txt
- group: auth
  title: ''
  type: Authentication
  url: authentication/vivoo-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/vivoo-scopes.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/vivoo-domain-security.yml
- group: operate
  title: ''
  type: Support
  url: https://vivoo.io/pages/contact
- group: operate
  title: ''
  type: HelpCenter
  url: https://vivoo.io/pages/faqs
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.vivoo.io/policies/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.vivoo.io/policies/privacy-policy
created: '2026-07-17'
description: 'Vivoo is a wellness technology company offering science-backed, at-home urine test strips paired with a mobile app that turns results into personalized nutrition and lifestyle recommendations. Its lineup includes the 8-parameter Vivoo Wellness Test, an at-home UTI test, fertility/ovulation and vaginal pH tests, and a connected Smart Toilet. The direct-to-consumer store runs on Shopify and exposes a native agent-commerce surface: a published llms.txt/agents.md, a Universal Commerce Protocol (UCP) merchant profile at /.well-known/ucp, and a hosted UCP shopping MCP server for agent-driven catalog search, cart, and buyer-approved checkout. Backed by 500 Global and Techstars.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/vivoo.png
layout: provider
mcp_servers:
- description: ''
  name: Vivoo MCP Server
  slug: vivoo-mcp-server
modified: '2026-07-21'
name: Vivoo
nav: Providers
network: true
overview: 'Vivoo publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Health, Wellness, Consumer Health, and Nutrition.


  Vivoo''s developer surface includes authentication, support, and 9 more developer resources.'
random_paper: 17
scopes:
- name: Vivoo Scopes
  scope_count: 4
  slug: vivoo-scopes
  summary_line: 4 scopes · authorizationCode
screenshot: https://raw.githubusercontent.com/api-evangelist/vivoo/refs/heads/main/screenshots/vivoo-2026-09-02T170145.png
security:
- kind: authentication
  name: Vivoo Authentication
  slug: vivoo-authentication
  summary_line: oauth2/openIdConnect · 1 scheme
- kind: domain-security
  name: Vivoo Domain Security
  slug: vivoo-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: vivoo
tags:
- Company
- Health
- Wellness
- Consumer Health
- Nutrition
- Diagnostics
- E-Commerce
- Agentic Commerce
- MCP
website: https://vivoo.io
---
