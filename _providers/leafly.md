---
access_model:
  confidence: high
  label: Paid · Requires approval
  onboarding: approval
  pricing: paid
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: false
agentic_access:
- acting_count: 3
  human_in_the_loop: 0
  name: Leafly Agentic Access
  operation_count: 5
  slug: leafly-agentic-access
  summary_line: 5 operations · 3 acting
api_count: 1
apis:
- description: Order (Reservations) API that lets any cannabis POS provider integrate Leafly online orders into its own system, taking ownership of the order integration rather than relying on a bespoke Leafly-built
  name: Leafly Order API
  slug: leafly-order-api
- baseURL: https://api.leafly.com/v2/menu_integration
  baseurl_source: declared
  description: The Menu API from Leafly — 2 operation(s) for menu.
  name: Leafly Menu API
  slug: leafly-menu-api
- baseURL: https://api.leafly.com/v2/menu_integration
  baseurl_source: declared
  description: The Status API from Leafly — 1 operation(s) for status.
  name: Leafly Status API
  slug: leafly-status-api
artifact_total: 13
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Leafly Integration Menu API
  slug: open-leafly-menu-api
- collection_type: open
  name: Leafly Integration Menu Status API
  slug: open-leafly-status-api
common:
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/leafly-capability-edges.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/leafly-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/leafly-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/leafly-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/leafly-scopes.yml
- group: company
  title: ''
  type: Website
  url: https://www.leafly.com
- group: docs
  title: ''
  type: Documentation
  url: https://docs.leafly.io/menu-integration-docs/v2.html
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/leafly
- group: start
  title: ''
  type: Signup
  url: https://success.leafly.com/retail
- group: operate
  title: ''
  type: Support
  url: https://help.leafly.com/hc/en-us/categories/20959505132051-Developer-FAQs
- group: commercial
  title: ''
  type: Plans
  url: plans/leafly-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/leafly-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/leafly-finops.yml
- group: company
  title: ''
  type: Blog
  url: https://www.leafly.com/feed
created: '2026-07-03'
description: Leafly is a cannabis discovery marketplace where consumers research strains, read reviews, and browse and order from licensed dispensaries and brands. For retailers and point-of-sale (POS) providers, Leafly exposes a documented Menu Integration API that keeps a dispensary's Leafly menu in near-real-time sync with its system of record - pushing product/item data, variants, inventory, pricing, strain, and cannabinoid information - and a partner-gated Order (Reservations) API that lets a POS system receive and manage online orders placed on Leafly. The Menu Integration API is publicly documented (OpenAPI via ReDoc) across V1, V1.1, and V2; the Order API's full specification sits behind Cloudflare Access and is available to onboarded partners. Actual use requires a paid Leafly for Retailers subscription and a Leafly-issued menu integration key - there is no self-serve public signup or consumer-facing data API.
finops:
- name: Leafly Finops
  service_category: Marketing and Marketplace
  slug: leafly-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/leafly.png
layout: provider
modified: '2026-07-03'
name: Leafly
nav: Providers
network: true
overview: 'Leafly publishes 2 APIs on the [APIs.io](https://apis.io/) network: Menu API and Status API. Tagged areas include Cannabis, Dispensary, Menu Sync, POS Integration, and Retail.


  Leafly''s developer surface includes authentication, documentation, signup flow, support, engineering blog, and 9 more developer resources.'
plans:
- name: Leafly Plans Pricing
  plan_count: 2
  slug: leafly-plans-pricing
random_paper: 7
rate_limits:
- limit_count: 3
  name: Leafly Rate Limits
  slug: leafly-rate-limits
scopes:
- name: Leafly Scopes
  scope_count: 0
  slug: leafly-scopes
  summary_line: OAuth 2.0 · no documented scopes
screenshot: https://raw.githubusercontent.com/api-evangelist/leafly/refs/heads/main/screenshots/leafly-2026-07-25T224732.png
security:
- kind: authentication
  name: Leafly Authentication
  slug: leafly-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Leafly Domain Security
  slug: leafly-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: leafly
tags:
- Cannabis
- Dispensary
- Menu Sync
- POS Integration
- Retail
- Marketplace
- Strains
- E-Commerce
website: https://www.leafly.com
---
