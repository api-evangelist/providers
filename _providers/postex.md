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
api_count: 1
apis:
- baseURL: https://api.postex.pk/services/integration/api/order
  baseurl_source: declared
  description: Booking, tracking, and listing shipment orders
  name: PostEx Orders API
  slug: postex-orders-api
- baseURL: https://api.postex.pk/services/integration/api/order
  baseurl_source: declared
  description: Operational cities and merchant address reference data
  name: PostEx Reference API
  slug: postex-reference-api
artifact_total: 7
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: PostEx Merchant Order Integration Orders API
  slug: open-postex-orders-api
- collection_type: open
  name: PostEx Merchant Order Integration Orders Reference API
  slug: open-postex-reference-api
common:
- group: other
  title: ''
  type: Overlay
  url: overlays/postex-order-overlay.yaml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/postex-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://postex.pk
- group: agent
  title: ''
  type: X-MCPServerCandidate
  url: mcp/postex-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/postex-llms.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/postex-well-known.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/postex-authentication.yml
created: '2026-07-17'
description: PostEx is a Pakistani e-commerce logistics, courier, and fintech platform that provides cash-on-delivery parcel fulfilment with instant upfront payments to online merchants, alongside a business suite for expense management, working- capital financing, and the XPay payment gateway. Merchants and order- management systems integrate with PostEx through its merchant Order Integration API (https://api.postex.pk) to book shipments, look up operational cities and pickup addresses, track parcels, and reconcile orders. This profile was enriched by API Evangelist by live-probing the production API host, which confirmed a real merchant integration surface authenticated with a token request header. PostEx is backed by 500 Global.
image: https://postex.pk/favicon.ico
layout: provider
modified: '2026-07-20'
name: PostEx
nav: Providers
network: true
overview: 'PostEx publishes 2 APIs on the [APIs.io](https://apis.io/) network: Orders API and Reference API. Tagged areas include Company, Logistics, Couriers, Shipping, and E-Commerce.


  PostEx''s developer surface includes authentication and 7 more developer resources.'
random_paper: 3
screenshot: https://raw.githubusercontent.com/api-evangelist/postex/refs/heads/main/screenshots/postex-2026-09-02T151830.png
security:
- kind: authentication
  name: Postex Authentication
  slug: postex-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Postex Domain Security
  slug: postex-domain-security
  summary_line: TLSv1.3 · DMARC
slug: postex
tags:
- Company
- Logistics
- Couriers
- Shipping
- E-Commerce
- Fulfillment
- Cash on Delivery
- Payments
- Fintech
- Pakistan
website: https://postex.pk
---
