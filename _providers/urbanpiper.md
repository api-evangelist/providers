---
access_model:
  confidence: medium
  label: Enterprise
  onboarding: unknown
  pricing: enterprise
  public: false
  source:
  - plans
  - authentication
  - security
  trial: false
  try_now: false
agentic_access:
- acting_count: 14
  human_in_the_loop: 0
  name: Urbanpiper Agentic Access
  operation_count: 16
  slug: urbanpiper-agentic-access
  summary_line: 16 operations · 14 acting
api_count: 1
apis:
- baseURL: https://pos-int.urbanpiper.com
  baseurl_source: declared
  description: Aggregator-specific feature actions.
  name: UrbanPiper Aggregator API
  slug: urbanpiper-aggregator-api
- baseURL: https://pos-int.urbanpiper.com
  baseurl_source: declared
  description: Catalogue push and item/option availability.
  name: UrbanPiper Menu API
  slug: urbanpiper-menu-api
- baseURL: https://pos-int.urbanpiper.com
  baseurl_source: declared
  description: Order status updates and stock-out on active orders.
  name: UrbanPiper Orders API
  slug: urbanpiper-orders-api
- baseURL: https://pos-int.urbanpiper.com
  baseurl_source: declared
  description: Create, update and toggle stores/locations.
  name: UrbanPiper Stores API
  slug: urbanpiper-stores-api
- baseURL: https://pos-int.urbanpiper.com
  baseurl_source: declared
  description: Register and manage outbound webhook endpoints.
  name: UrbanPiper Webhooks API
  slug: urbanpiper-webhooks-api
artifact_total: 18
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: UrbanPiper POS Integration Aggregator API
  slug: open-urbanpiper-aggregator-api
- collection_type: open
  name: UrbanPiper POS Integration Aggregator Menu API
  slug: open-urbanpiper-menu-api
- collection_type: open
  name: UrbanPiper POS Integration Aggregator Orders API
  slug: open-urbanpiper-orders-api
- collection_type: open
  name: UrbanPiper POS Integration Aggregator Stores API
  slug: open-urbanpiper-stores-api
- collection_type: open
  name: UrbanPiper POS Integration Aggregator Webhooks API
  slug: open-urbanpiper-webhooks-api
- collection_type: open
  name: Urbanpiper
  slug: open-urbanpiper
common:
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/urbanpiper-capability-edges.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/urbanpiper-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/urbanpiper-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/urbanpiper-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/urbanpiper
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/urbanpiper
- group: company
  title: ''
  type: Website
  url: https://www.urbanpiper.com
- group: docs
  title: ''
  type: Documentation
  url: https://api-docs.urbanpiper.com/downstream/
- group: commercial
  title: ''
  type: Plans
  url: plans/urbanpiper-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/urbanpiper-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/urbanpiper-finops.yml
created: '2026-06-21'
description: UrbanPiper is a restaurant commerce platform whose POS-integration API connects a restaurant's POS/ERP to online ordering aggregators (Swiggy, Zomato, UberEats, DoorDash, Deliveroo, Talabat, Amazon, Careem and more). The REST API covers catalogue/menu management, store and item/option availability, order relay and order status updates, and outbound webhooks, powering the Prime, Hub and Atlas products.
finops:
- name: Urbanpiper Finops
  service_category: Restaurant Commerce Platform
  slug: urbanpiper-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/urbanpiper.png
layout: provider
modified: '2026-06-21'
name: UrbanPiper
nav: Providers
network: true
overview: 'UrbanPiper publishes 5 APIs on the [APIs.io](https://apis.io/) network, including Aggregator API, Menu API, Orders API, and 2 more. Tagged areas include Restaurant, Food Delivery, Ordering, Point-of-Sale, and Aggregators.


  UrbanPiper''s developer surface includes authentication, documentation, and 9 more developer resources.'
plans:
- name: Urbanpiper Plans Pricing
  plan_count: 4
  slug: urbanpiper-plans-pricing
random_paper: 9
rate_limits:
- limit_count: 3
  name: Urbanpiper Rate Limits
  slug: urbanpiper-rate-limits
screenshot: https://raw.githubusercontent.com/api-evangelist/urbanpiper/refs/heads/main/screenshots/urbanpiper-2026-09-02T165211.png
security:
- kind: authentication
  name: Urbanpiper Authentication
  slug: urbanpiper-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Urbanpiper Domain Security
  slug: urbanpiper-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: urbanpiper
tags:
- Restaurant
- Food Delivery
- Ordering
- Point-of-Sale
- Aggregators
- Commerce
website: https://www.urbanpiper.com
---
