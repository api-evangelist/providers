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
  - '{''url'': ''https://www.spod.com'', ''status'': 301, ''note'': ''declared website redirects to https://www.spreadshop.com/spreadconnect/ — a different registrable domain (spod.com -> spreadshop.com), possible rename or acquisition (probed 2026-09-03, roadmap#169)''}'
  trial: false
  try_now: false
agentic_access:
- acting_count: 12
  human_in_the_loop: 0
  name: Spod Agentic Access
  operation_count: 23
  slug: spod-agentic-access
  summary_line: 23 operations · 12 acting
api_count: 1
apis:
- baseURL: https://rest.spod.com
  baseurl_source: declared
  description: The Articles API from SPOD — 2 operation(s) for articles.
  name: SPOD Articles API
  slug: spod-articles-api
- baseURL: https://rest.spod.com
  baseurl_source: declared
  description: The Common API from SPOD — 1 operation(s) for common.
  name: SPOD Common API
  slug: spod-common-api
- baseURL: https://rest.spod.com
  baseurl_source: declared
  description: The Orders API from SPOD — 4 operation(s) for orders.
  name: SPOD Orders API
  slug: spod-orders-api
- baseURL: https://rest.spod.com
  baseurl_source: declared
  description: The Product Types API from SPOD — 2 operation(s) for product types.
  name: SPOD Product Types API
  slug: spod-product-types-api
- baseURL: https://rest.spod.com
  baseurl_source: declared
  description: The Shipping API from SPOD — 3 operation(s) for shipping.
  name: SPOD Shipping API
  slug: spod-shipping-api
- baseURL: https://rest.spod.com
  baseurl_source: declared
  description: The Stock API from SPOD — 2 operation(s) for stock.
  name: SPOD Stock API
  slug: spod-stock-api
- baseURL: https://rest.spod.com
  baseurl_source: declared
  description: The Subscriptions API from SPOD — 5 operation(s) for subscriptions.
  name: SPOD Subscriptions API
  slug: spod-subscriptions-api
artifact_total: 23
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: SPOD (Spreadconnect) Fulfillment REST Articles API
  slug: open-spod-articles-api
- collection_type: open
  name: SPOD (Spreadconnect) Fulfillment REST Articles Common API
  slug: open-spod-common-api
- collection_type: open
  name: SPOD (Spreadconnect) Fulfillment REST Articles Orders API
  slug: open-spod-orders-api
- collection_type: open
  name: SPOD (Spreadconnect) Fulfillment REST Articles Product Types API
  slug: open-spod-product-types-api
- collection_type: open
  name: SPOD (Spreadconnect) Fulfillment REST Articles Shipping API
  slug: open-spod-shipping-api
- collection_type: open
  name: SPOD (Spreadconnect) Fulfillment REST Articles Stock API
  slug: open-spod-stock-api
- collection_type: open
  name: SPOD (Spreadconnect) Fulfillment REST Articles Subscriptions API
  slug: open-spod-subscriptions-api
- collection_type: open
  name: SPOD (Spreadconnect) Fulfillment REST API
  slug: open-spod
common:
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/spod-capability-edges.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/spod-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/spod-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/spod-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/spod-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/SP0D
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/spod-spreadshirt-print-on-demand
- group: company
  title: ''
  type: Website
  url: https://www.spod.com
- group: docs
  title: ''
  type: Documentation
  url: https://rest.spod.com/docs/
- group: commercial
  title: ''
  type: Plans
  url: plans/spod-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/spod-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/spod-finops.yml
created: '2026-07-11'
description: SPOD (Spreadshirt Print-On-Demand), now branded Spreadconnect, is the print-on-demand and dropshipping fulfillment service from Spreadshirt. Its REST API (base https://rest.spod.com) lets any shop system create customizable articles from designs, place and manage orders, choose shipping types and track shipments, browse the catalog of 250+ product types, check stock, and subscribe to webhook notifications for article, order, and shipment events. Authentication is a per-account API access token sent in the X-SPOD-ACCESS-TOKEN header. There are no setup or monthly fees; sellers are invoiced per fulfilled order (base product price plus print and shipping costs).
finops:
- name: Spod Finops
  service_category: Print on Demand and Fulfillment
  slug: spod-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/spod.png
layout: provider
modified: '2026-07-11'
name: SPOD
nav: Providers
network: true
overview: 'SPOD publishes 7 APIs on the [APIs.io](https://apis.io/) network, including Articles API, Common API, Orders API, and 4 more. Tagged areas include Print on Demand, POD, Dropshipping, Fulfillment, and E-Commerce.


  SPOD''s developer surface includes authentication, documentation, and 10 more developer resources.'
plans:
- name: Spod Plans Pricing
  plan_count: 1
  slug: spod-plans-pricing
random_paper: 18
rate_limits:
- limit_count: 2
  name: Spod Rate Limits
  slug: spod-rate-limits
screenshot: https://raw.githubusercontent.com/api-evangelist/spod/refs/heads/main/screenshots/spod-2026-09-02T160535.png
security:
- kind: authentication
  name: Spod Authentication
  slug: spod-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Spod Domain Security
  slug: spod-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Spod Vulnerability Disclosure
  slug: spod-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: spod
tags:
- Print on Demand
- POD
- Dropshipping
- Fulfillment
- E-Commerce
- Merchandise
- Spreadshirt
- Spreadconnect
website: https://www.spod.com
---
