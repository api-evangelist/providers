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
  - sandbox
  trial: false
  try_now: false
agentic_access:
- acting_count: 1
  human_in_the_loop: 0
  name: Gemnote Agentic Access
  operation_count: 7
  slug: gemnote-agentic-access
  summary_line: 7 operations · 1 acting
api_count: 1
apis:
- baseURL: https://api.gemnote.com
  baseurl_source: declared
  description: The catalog of gifts available to send.
  name: Gemnote Gifts API
  slug: gemnote-gifts-api
- baseURL: https://api.gemnote.com
  baseurl_source: declared
  description: The catalog of greeting cards / postcards available to include.
  name: Gemnote Greeting Cards API
  slug: gemnote-greeting-cards-api
- baseURL: https://api.gemnote.com
  baseurl_source: declared
  description: Orders that send a gift and optional greeting card to a recipient.
  name: Gemnote Shipments API
  slug: gemnote-shipments-api
artifact_total: 10
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Gemnote Gifts API
  slug: open-gemnote-gifts-api
- collection_type: open
  name: Gemnote Gifts Greeting Cards API
  slug: open-gemnote-greeting-cards-api
- collection_type: open
  name: Gemnote Gifts Shipments API
  slug: open-gemnote-shipments-api
common:
- group: agent
  title: ''
  type: AgentSkill
  url: skills/gemnote-send-a-gift.md
- group: agent
  title: ''
  type: X-MCPServerCandidate
  url: mcp/gemnote-mcp.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/gemnote-openapi-overlay.yaml
- group: company
  title: ''
  type: Website
  url: https://www.gemnote.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://github.com/gemnote/api
- group: docs
  title: ''
  type: Documentation
  url: https://github.com/gemnote/api
- group: docs
  title: ''
  type: APIReference
  url: https://github.com/gemnote/api
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/gemnote
- group: company
  title: ''
  type: Blog
  url: https://www.gemnote.com/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://www.gemnote.com/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.gemnote.com/terms
- group: operate
  title: ''
  type: Support
  url: https://support.gemnote.com/hc/en-us
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/gemnote-llms.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/gemnote-well-known.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/gemnote-domain-security.yml
created: '2026-07-17'
description: Gemnote is a corporate gifting and swag management platform that helps businesses design, produce, warehouse, and ship custom branded merchandise and gifts worldwide. Founded in 2014 and based in Union City, California, and backed by Y Combinator, Gemnote pairs a swag management app (inventory, order tracking, e-commerce swag stores, and Shopify integration) with human design and fulfillment expertise, and is used by companies such as Reddit, Google, Airbnb, and Sephora for employee swag, new-hire kits, PR and influencer kits, event giveaways, and packaging. Gemnote also publishes a JSON:API-style REST API that lets partners list gifts and greeting cards, create shipments to recipients, and track fulfillment programmatically, with a sandbox environment for testing.
image: https://www.gemnote.com/favicon.ico
layout: provider
modified: '2026-07-19'
name: Gemnote
nav: Providers
network: true
overview: 'Gemnote publishes 3 APIs on the [APIs.io](https://apis.io/) network: Gifts API, Greeting Cards API, and Shipments API. Tagged areas include Company, Corporate Gifting, Swag Management, Branded Merchandise, and Fulfillment.


  Gemnote''s developer surface includes documentation, API reference, engineering blog, pricing, support, and 10 more developer resources.'
random_paper: 16
screenshot: https://raw.githubusercontent.com/api-evangelist/gemnote/refs/heads/main/screenshots/gemnote-2026-07-25T215530.png
security:
- kind: authentication
  name: Gemnote Authentication
  slug: gemnote-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Gemnote Domain Security
  slug: gemnote-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: gemnote
tags:
- Company
- Corporate Gifting
- Swag Management
- Branded Merchandise
- Fulfillment
- E-Commerce
- Shipping
- Y Combinator
website: https://www.gemnote.com/
---
