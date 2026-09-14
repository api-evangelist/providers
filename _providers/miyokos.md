---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - authentication
  - security
  trial: false
  try_now: false
api_count: 0
artifact_total: 3
common:
- group: company
  title: ''
  type: Website
  url: https://miyokos.com
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.miyokos.com/policies/privacy-policy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.miyokos.com/policies/terms-of-service
- group: agent
  title: ''
  type: WellKnown
  url: well-known/miyokos-well-known.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/miyokos-llms.txt
- group: agent
  title: ''
  type: MCPServer
  url: mcp/miyokos-mcp.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/miyokos-authentication.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/miyokos-domain-security.yml
created: '2026-07-17'
description: 'Miyoko''s Creamery (miyokos.com) is a plant-based dairy company in the planetary-health sector, backed by Obvious Ventures, making vegan butter and cheese from cultured cashews, oats, and legumes. The company does not publish a first-party developer REST API; its digital surface is a Shopify-hosted storefront. That storefront exposes a genuine agent-commerce surface: a Universal Commerce Protocol (UCP) merchant profile at /.well-known/ucp, a hosted shopping MCP endpoint for search/cart/checkout, Shopify Customer Account OIDC/OAuth for identity, and an /llms.txt with agent instructions. This profile was enriched by probing that public surface.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/miyokos.png
layout: provider
mcp_servers:
- description: ''
  name: Miyoko's Creamery Shopping (UCP)
  slug: miyokos-creamery-shopping-ucp
modified: '2026-07-20'
name: Miyokos
nav: Providers
network: true
overview: 'Miyokos is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Planetary Health, Plant-Based, Food and Beverage, and E-Commerce.


  Miyokos'' developer surface includes authentication and 7 more developer resources.'
random_paper: 2
screenshot: https://raw.githubusercontent.com/api-evangelist/miyokos/refs/heads/main/screenshots/miyokos-2026-08-07T183958.png
security:
- kind: authentication
  name: Miyokos Authentication
  slug: miyokos-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Miyokos Domain Security
  slug: miyokos-domain-security
  summary_line: TLSv1.3 · HSTS
slug: miyokos
tags:
- Company
- Planetary Health
- Plant-Based
- Food and Beverage
- E-Commerce
- Shopify
- Agent Commerce
- UCP
website: https://miyokos.com
---
