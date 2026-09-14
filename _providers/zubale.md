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
agentic_access:
- acting_count: 19
  human_in_the_loop: 0
  name: Zubale Agentic Access
  operation_count: 21
  slug: zubale-agentic-access
  summary_line: 21 operations · 19 acting
api_count: 1
apis:
- baseURL: https://api.zubale.com
  baseurl_source: spec
  description: The API Documentation for External Notification Handler API from Zubale — 1 operation(s) for api documentation for external notification handler.
  name: Zubale API Documentation for External Notification Handler API
  slug: zubale-api-documentation-for-external-notification-handler-api
- baseURL: https://api.zubale.com
  baseurl_source: spec
  description: The Cancel tasks API from Zubale — 2 operation(s) for cancel tasks.
  name: Zubale Cancel tasks API
  slug: zubale-cancel-tasks-api
- baseURL: https://api.zubale.com
  baseurl_source: spec
  description: The Delivery API API from Zubale — 3 operation(s) for delivery api.
  name: Zubale Delivery API API
  slug: zubale-delivery-api-api
- baseURL: https://api.zubale.com
  baseurl_source: spec
  description: The External outbound API from Zubale — 1 operation(s) for external outbound.
  name: Zubale External outbound API
  slug: zubale-external-outbound-api
- baseURL: https://api.zubale.com
  baseurl_source: spec
  description: The Live Tracking For Cencosud API from Zubale — 4 operation(s) for live tracking for cencosud.
  name: Zubale Live Tracking For Cencosud API
  slug: zubale-live-tracking-for-cencosud-api
- baseURL: https://api.zubale.com
  baseurl_source: spec
  description: The Picking & Delivery API API from Zubale — 4 operation(s) for picking & delivery api.
  name: Zubale Picking & Delivery API API
  slug: zubale-picking-delivery-api-api
- baseURL: https://api.zubale.com
  baseurl_source: spec
  description: The Product catalog API from Zubale — 3 operation(s) for product catalog.
  name: Zubale Product catalog API
  slug: zubale-product-catalog-api
- baseURL: https://api.zubale.com
  baseurl_source: spec
  description: 'The Webhook: Payload Structure for Order Notification API from Zubale — 1 operation(s) for webhook: payload structure for order notification.'
  name: 'Zubale Webhook: Payload Structure for Order Notification API'
  slug: zubale-webhook-payload-structure-for-order-notification-api
artifact_total: 24
asyncapis:
- description: ''
  name: Zubale Webhooks
  slug: zubale-webhooks
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Zubale API Documentation for External Notification Handler API
  slug: open-zubale-api-documentation-for-external-notification-handler-api
- collection_type: open
  name: Zubale API Documentation for External Notification Handler Cancel tasks API
  slug: open-zubale-cancel-tasks-api
- collection_type: open
  name: Zubale API Documentation for External Notification Handler Delivery API API
  slug: open-zubale-delivery-api-api
- collection_type: open
  name: Zubale API Documentation for External Notification Handler External outbound API
  slug: open-zubale-external-outbound-api
- collection_type: open
  name: Zubale API Documentation for External Notification Handler Live Tracking For Cencosud API
  slug: open-zubale-live-tracking-for-cencosud-api
- collection_type: open
  name: Zubale API Documentation for External Notification Handler Picking & Delivery API API
  slug: open-zubale-picking-delivery-api-api
- collection_type: open
  name: Zubale API Documentation for External Notification Handler Product catalog API
  slug: open-zubale-product-catalog-api
- collection_type: open
  name: 'Zubale API Documentation for External Notification Handler Webhook: Payload Structure for Order Notification API'
  slug: open-zubale-webhook-payload-structure-for-order-notification-api
common:
- group: agent
  title: ''
  type: X-MCPServerCandidate
  url: mcp/zubale-mcp.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/zubale-openapi-overlay.yaml
- group: auth
  title: ''
  type: TrustCenter
  url: security/zubale-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/zubale-domain-security.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/zubale-agentic-access.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/zubale-scopes.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/zubale-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://zubale.com
created: '2026-07-17'
description: 'Zubale is a company surfaced as a portfolio company of felicis, qed-investors and added to the API Evangelist network as a stub for enrichment. Sector: ecommerce. This profile is a lead awaiting the enrichment pipeline.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/zubale.png
layout: provider
modified: '2026-07-17'
name: Zubale
nav: Providers
network: true
overview: 'Zubale publishes 8 APIs on the [APIs.io](https://apis.io/) network, including API Documentation for External Notification Handler API, Cancel tasks API, Delivery API API, and 5 more. Tagged areas include Company and E-Commerce.


  The Zubale catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Zubale''s developer surface includes authentication and 7 more developer resources.'
random_paper: 13
scopes:
- name: Zubale Scopes
  scope_count: 0
  slug: zubale-scopes
  summary_line: OAuth 2.0 · no documented scopes
screenshot: https://raw.githubusercontent.com/api-evangelist/zubale/refs/heads/main/screenshots/zubale-2026-09-02T171850.png
security:
- kind: authentication
  name: Zubale Authentication
  slug: zubale-authentication
  summary_line: http/oauth2 · 3 schemes
- kind: domain-security
  name: Zubale Domain Security
  slug: zubale-domain-security
  summary_line: TLSv1.2 · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Zubale Vulnerability Disclosure
  slug: zubale-vulnerability-disclosure
  summary_line: Hackerone · contact published
- kind: trust-center
  name: Zubale Trust Center
  slug: zubale-trust-center
  summary_line: ISO 27001, SOC 3, CAIQ
slug: zubale
tags:
- Company
- E-Commerce
website: https://zubale.com
---
