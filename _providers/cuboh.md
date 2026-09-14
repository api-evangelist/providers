---
access_model:
  confidence: medium
  label: Paid
  onboarding: unknown
  pricing: paid
  public: false
  source:
  - plans
  - authentication
  - security
  trial: false
  try_now: false
agentic_access:
- acting_count: 13
  human_in_the_loop: 0
  name: Cuboh Agentic Access
  operation_count: 20
  slug: cuboh-agentic-access
  summary_line: 20 operations · 13 acting
api_count: 1
apis:
- baseURL: https://core.cuboh.net
  baseurl_source: declared
  description: Merchant (location) status and integration completion.
  name: Cuboh Locations API
  slug: cuboh-locations-api
- baseURL: https://core.cuboh.net
  baseurl_source: declared
  description: Menu retrieval, push, creation, update, and validation.
  name: Cuboh Menu API
  slug: cuboh-menu-api
- baseURL: https://core.cuboh.net
  baseurl_source: declared
  description: Order creation, retrieval, and lifecycle actions.
  name: Cuboh Orders API
  slug: cuboh-orders-api
- baseURL: https://core.cuboh.net
  baseurl_source: declared
  description: Signed event notifications delivered to partner-hosted URLs.
  name: Cuboh Webhooks API
  slug: cuboh-webhooks-api
artifact_total: 15
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Cuboh Integration Locations API
  slug: open-cuboh-locations-api
- collection_type: open
  name: Cuboh Integration Locations Menu API
  slug: open-cuboh-menu-api
- collection_type: open
  name: Cuboh Integration Locations Orders API
  slug: open-cuboh-orders-api
- collection_type: open
  name: Cuboh Integration API
  slug: open-cuboh
common:
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/cuboh-capability-edges.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/cuboh-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/cuboh-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/cuboh-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/getcuboh
- group: company
  title: ''
  type: Website
  url: https://www.cuboh.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.cuboh.com/direct
- group: commercial
  title: ''
  type: Plans
  url: plans/cuboh-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/cuboh-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/cuboh-finops.yml
created: '2026-06-21'
description: Cuboh is a restaurant online-ordering management platform that consolidates third-party delivery and pickup orders (DoorDash, Uber Eats, Grubhub, and more) onto a single tablet and into the restaurant POS. For technology partners, Cuboh exposes partner-gated Direct and Connect integration APIs covering orders, menus, merchant locations, and webhooks. API access is provisioned by Cuboh during a partner onboarding and QA-certification process; there is no public self-serve signup.
finops:
- name: Cuboh Finops
  service_category: Management and Governance
  slug: cuboh-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/cuboh.png
layout: provider
modified: '2026-06-21'
name: Cuboh
nav: Providers
network: true
overview: 'Cuboh publishes 4 APIs on the [APIs.io](https://apis.io/) network, including Locations API, Menu API, Orders API, and 1 more. Tagged areas include Restaurant, Online Ordering, Delivery, Point-of-Sale, and Order Aggregation.


  Cuboh''s developer surface includes authentication, documentation, and 8 more developer resources.'
plans:
- name: Cuboh Plans Pricing
  plan_count: 5
  slug: cuboh-plans-pricing
random_paper: 4
rate_limits:
- limit_count: 5
  name: Cuboh Rate Limits
  slug: cuboh-rate-limits
screenshot: https://raw.githubusercontent.com/api-evangelist/cuboh/refs/heads/main/screenshots/cuboh-2026-07-25T210903.png
security:
- kind: authentication
  name: Cuboh Authentication
  slug: cuboh-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Cuboh Domain Security
  slug: cuboh-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: cuboh
tags:
- Restaurant
- Online Ordering
- Delivery
- Point-of-Sale
- Order Aggregation
website: https://www.cuboh.com/
---
