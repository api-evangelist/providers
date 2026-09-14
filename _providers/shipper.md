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
api_count: 1
apis:
- description: HTTP-based API (v3) for interacting with Shipper's location, pricing, and shipment features — search location by keyword and administrative area, retrieve domestic multi-courier pricing, create orders
  name: Shipper Logistics API
  slug: shipper-logistics-api
artifact_total: 4
asyncapis:
- description: ''
  name: Shipper Webhooks
  slug: shipper-webhooks
common:
- group: company
  title: ''
  type: Website
  url: https://shipper.id/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://logistics-docs.shipper.id/
- group: docs
  title: ''
  type: Documentation
  url: https://logistics-docs.shipper.id/docs/overview
- group: docs
  title: ''
  type: APIReference
  url: https://logistics-docs.shipper.id/
- group: start
  title: ''
  type: GettingStarted
  url: https://logistics-docs.shipper.id/docs/overview
- group: auth
  title: ''
  type: Authentication
  url: authentication/shipper-authentication.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/shipper-sandbox.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/shipper-webhooks.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/shipper-conventions.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/shipper-lifecycle.yml
- group: agent
  title: ''
  type: X-MCPServerCandidate
  url: mcp/shipper-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/shipper-llms.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/shipper-well-known.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/shipper-domain-security.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/shipper-conformance.yml
- group: start
  title: ''
  type: SignUp
  url: https://bos.sandbox.shipper.id
- group: operate
  title: ''
  type: Support
  url: http://faq.shipper.id/
- group: company
  title: ''
  type: Blog
  url: https://shipper.id/en/blog/
created: '2026-07-17'
description: Shipper is an Indonesian technology-driven logistics aggregator that connects merchants and e-commerce sellers to hundreds of third-party courier and last-mile delivery partners through a single platform. Its services span a logistics aggregator (multi-courier rate check, order creation, pickup and tracking), nationwide fulfillment and warehousing, contract logistics, international freight forwarding, and e-commerce enablement. Developers integrate via the HTTP-based Shipper Logistics API (v3), which exposes location search, domestic pricing, order creation (including COD), shipping label and receipt generation, pickup request, and shipment status tracking, with real-time delivery-status webhooks. Backed by Lightspeed Venture Partners, Partech, and Prosus Ventures.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/shipper.png
layout: provider
modified: '2026-07-21'
name: Shipper
nav: Providers
network: true
overview: 'Shipper publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Logistics, Shipping, Fulfillment, and Supply Chain.


  The Shipper catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Shipper''s developer surface includes documentation, API reference, getting-started guide, authentication, sandbox, signup flow, support, and 11 more developer resources.'
random_paper: 7
screenshot: https://raw.githubusercontent.com/api-evangelist/shipper/refs/heads/main/screenshots/shipper-2026-09-02T155228.png
security:
- kind: authentication
  name: Shipper Authentication
  slug: shipper-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Shipper Domain Security
  slug: shipper-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: shipper
tags:
- Company
- Logistics
- Shipping
- Fulfillment
- Supply Chain
- E-Commerce
- Last Mile Delivery
- Couriers
- Indonesia
website: https://shipper.id/
---
