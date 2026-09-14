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
- description: Agent-facing Universal Commerce Protocol (UCP) shopping surface for the Hawthorne Shopify store — catalog search/lookup, cart, checkout, fulfillment, discount and order capabilities over an MCP endpoi
  name: Hawthorne UCP Commerce (Shopify)
  slug: hawthorne-ucp-commerce-shopify
artifact_total: 5
common:
- group: company
  title: ''
  type: Website
  url: https://hawthorne.co/
- group: agent
  title: ''
  type: WellKnown
  url: well-known/hawthorne-well-known.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/hawthorne-llms.txt
- group: agent
  title: ''
  type: MCPServer
  url: mcp/hawthorne-mcp.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/hawthorne-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/hawthorne-scopes.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/hawthorne-conventions.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/hawthorne-domain-security.yml
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://hawthorne.co/policies/privacy-policy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://hawthorne.co/policies/terms-of-service
created: '2026-07-17'
description: 'Hawthorne is an internet-first men''s personal care and grooming brand founded in 2016 in New York City (a Techstars alum, later Series B). It sells personalized, long-lasting fragrance and grooming products — cologne, deodorant, body wash, face and hair care — tuned to a customer''s body chemistry and lifestyle through an onboarding quiz and a smart-subscription model built around its "Surround Scent" technology. The direct-to-consumer storefront at hawthorne.co runs on Shopify and exposes a modern agent-commerce surface: a published /llms.txt and /agents.md, Shopify Customer Account OpenID Connect discovery, and a live Universal Commerce Protocol (UCP) MCP endpoint so AI shopping agents can search the catalog, build a cart, and complete a buyer-approved checkout.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/hawthorne.png
layout: provider
mcp_servers:
- description: ''
  name: Hawthorne MCP Server
  slug: hawthorne-mcp-server
modified: '2026-07-19'
name: Hawthorne
nav: Providers
network: true
overview: 'Hawthorne publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, E-Commerce, Retail, Consumer Goods, and Personal Care.


  Hawthorne''s developer surface includes authentication and 9 more developer resources.'
random_paper: 10
scopes:
- name: Hawthorne Scopes
  scope_count: 4
  slug: hawthorne-scopes
  summary_line: 4 scopes · authorizationCode
screenshot: https://raw.githubusercontent.com/api-evangelist/hawthorne/refs/heads/main/screenshots/hawthorne-2026-08-07T170020.png
security:
- kind: authentication
  name: Hawthorne Authentication
  slug: hawthorne-authentication
  summary_line: oauth2/openIdConnect · 1 scheme
- kind: domain-security
  name: Hawthorne Domain Security
  slug: hawthorne-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: hawthorne
tags:
- Company
- E-Commerce
- Retail
- Consumer Goods
- Personal Care
- Grooming
- Agentic Commerce
- Shopify
website: https://hawthorne.co/
---
