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
api_count: 0
artifact_total: 4
common:
- group: company
  title: ''
  type: Website
  url: https://www.duroflexworld.com/
- group: agent
  title: ''
  type: MCPServer
  url: mcp/duroflexworld-mcp.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/duroflexworld-well-known.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/duroflexworld-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/duroflexworld-scopes.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/duroflexworld-llms.txt
- group: auth
  title: ''
  type: DomainSecurity
  url: security/duroflexworld-domain-security.yml
- group: company
  title: ''
  type: Blog
  url: https://www.duroflexworld.com/blogs/news
- group: operate
  title: ''
  type: Support
  url: https://www.duroflexworld.com/pages/contact-us
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.duroflexworld.com/policies/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.duroflexworld.com/policies/privacy-policy
created: '2026-07-17'
description: 'Duroflex (duroflexworld.com) is one of India''s most trusted sleep-solutions brands, selling mattresses, sofas, recliners, beds, pillows and mattress protectors direct-to-consumer with up to a 10-year warranty, free shipping and EMI options. The online store runs on Shopify and exposes real agent-facing commerce surfaces discovered by the API Evangelist enrichment pipeline: a hosted Storefront MCP server at /api/mcp (catalog search, cart, product details, and shop policy/FAQ tools that conform to the UCP catalog capability) and a Shopify Customer Account API secured with OAuth 2.0 / OpenID Connect, advertising an agent-oriented customer-account-mcp-api scope. Surfaced originally as a Norwest Venture Partners portfolio lead, the profile is now enriched with its MCP, well-known OIDC discovery, authentication, scopes and domain-security artifacts.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/duroflexworld.png
layout: provider
mcp_servers:
- description: Shopify Storefront MCP server for the Duroflex (duroflexworld.com) online store. Exposes catalog search, cart management, product lookup, and shop policy/FAQ retrieval to AI agents. Hosted and operate
  name: Duroflexworld Storefront MCP
  slug: duroflexworld-storefront-mcp
modified: '2026-07-18'
name: Duroflexworld
nav: Providers
network: true
overview: 'Duroflexworld is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, E-Commerce, Retail, Sleep, and Mattresses.


  Duroflexworld''s developer surface includes authentication, engineering blog, support, and 8 more developer resources.'
random_paper: 18
scopes:
- name: Duroflexworld Scopes
  scope_count: 4
  slug: duroflexworld-scopes
  summary_line: 4 scopes · authorizationCode
screenshot: https://raw.githubusercontent.com/api-evangelist/duroflexworld/refs/heads/main/screenshots/duroflexworld-2026-08-07T164615.png
security:
- kind: authentication
  name: Duroflexworld Authentication
  slug: duroflexworld-authentication
  summary_line: oauth2/openIdConnect · 2 schemes
- kind: domain-security
  name: Duroflexworld Domain Security
  slug: duroflexworld-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: duroflexworld
tags:
- Company
- E-Commerce
- Retail
- Sleep
- Mattresses
- Furniture
- Shopify
- MCP
- Consumer Goods
- India
website: https://www.duroflexworld.com/
---
