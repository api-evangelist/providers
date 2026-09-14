---
api_count: 2
apis:
- baseURL: https://www.wowmomo.com/wp-json
  baseurl_source: declared
  description: The live WordPress REST API served by www.wowmomo.com, advertised in the head of every page as <link rel="https://api.w.org/">. Its route-discovery document declares 396 routes across 36 namespaces; t
  name: WOW! Momo Content API
  slug: wow-momo-content-api
- description: A first-party application backend on api.wowmomo.com behind an AWS Application Load Balancer, running an Express service scaffolded with DhiWise (its root serves a "welcome to node.js" page carrying t
  name: WOW! Momo App Backend
  slug: wow-momo-app-backend
artifact_total: 6
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/wow-momo-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.wowmomo.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.wowmomo.com/terms-conditions/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.wowmomo.com/privacy/
- group: other
  title: ''
  type: Franchise
  url: https://www.wowmomo.com/franchise-form/
- group: other
  title: ''
  type: StoreLocator
  url: https://restaurants.wowmomo.com/
- group: company
  title: ''
  type: BlogRSS
  url: https://www.wowmomo.com/feed/
- group: company
  title: ''
  type: LinkedIn
  url: https://in.linkedin.com/company/wow-momo
- group: docs
  title: ''
  type: OpenAPI
  url: openapi/_ae-authored/wow-momo-content-api-openapi.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/wow-momo-content-api-overlay.yaml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/wow-momo-llms.txt
- group: agent
  title: ''
  type: X-MCPServerCandidate
  url: mcp/wow-momo-mcp.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/wow-momo-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/wow-momo-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/wow-momo-problem-types.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/wow-momo-data-model.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/wow-momo-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/wow-momo-conformance.yml
- group: build
  title: ''
  type: Packages
  url: packages/wow-momo-packages.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/wow-momo-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/wow-momo-rate-limits.yml
created: '2026-09-04'
description: 'WOW! Momo Foods Private Limited is the Kolkata, India quick-service restaurant company founded in August 2008 by St. Xavier''s College alumni Sagar J. Daryani and Binod K. Homagai, which built a national chain around the momo and now operates three brands — WOW! Momo, WOW! China and WOW! Chicken (launched December 2021) — across roughly 650 outlets in more than 30 Indian cities, backed by Lighthouse Funds, Tiger Global, Khazanah Nasional and Oaks Capital. WOW! Momo runs no developer programme: it publishes no API documentation, developer portal, SDK, API pricing or support channel, and no company-authored OpenAPI, AsyncAPI or GraphQL contract exists anywhere public. It is catalogued here because www.wowmomo.com serves a live, anonymously readable WordPress REST API — advertised in the head of every page as <link rel="https://api.w.org/"> — exposing the site''s pages, media library, taxonomies, search index, oEmbed 1.0 provider endpoint and Yoast SEO head document, alongside
  a separate first-party application backend on api.wowmomo.com that answers every anonymous request, including a control path that cannot exist, with an identical NO_AUTH body.'
image: https://www.wowmomo.com/wp-content/uploads/2022/03/Wow-Momo-Logo.png
layout: provider
modified: '2026-09-04'
name: WOW! Momo
nav: Providers
network: true
overview: 'WOW! Momo publishes 1 API on the [APIs.io](https://apis.io/) network: Content API. Tagged areas include Company, Restaurants, Food and Beverage, Quick Service Restaurant, and Retail.


  WOW! Momo''s developer surface includes authentication and 21 more developer resources.'
plans:
- name: Wow Momo Plans Pricing
  plan_count: 0
  slug: wow-momo-plans-pricing
random_paper: 15
rate_limits:
- limit_count: 0
  name: Wow Momo Rate Limits
  slug: wow-momo-rate-limits
security:
- kind: authentication
  name: Wow Momo Authentication
  slug: wow-momo-authentication
  summary_line: http/apiKey/opaque-application-credential · 3 schemes
- kind: domain-security
  name: Wow Momo Domain Security
  slug: wow-momo-domain-security
  summary_line: TLSv1.3 · DMARC
slug: wow-momo
tags:
- Company
- Restaurants
- Food and Beverage
- Quick Service Restaurant
- Retail
- Hospitality
- Consumer
- Franchising
- Content
- WordPress
- oEmbed
- India
- Kolkata
website: https://www.wowmomo.com/
---
