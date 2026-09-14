---
access_model:
  confidence: medium
  label: Requires approval
  onboarding: approval
  pricing: unknown
  public: false
  source:
  - plans
  trial: false
  try_now: false
api_count: 1
apis:
- description: Limited partner-facing endpoints for inventory and order integration with Whatnot. Not a publicly documented developer API; access is contingent on Whatnot Seller approval and partnership.
  name: Whatnot Seller / Partner API
  slug: seller-api
artifact_total: 5
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/whatnot-domain-security.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Whatnot-Inc
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/whatnot-inc
- group: company
  title: ''
  type: Website
  url: https://www.whatnot.com/
- group: other
  title: ''
  type: Developer
  url: https://www.whatnot.com/sellers
- group: commercial
  title: ''
  type: Plans
  url: plans/whatnot-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/whatnot-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/whatnot-finops.yml
created: '2026-05-08'
description: Whatnot is a live-stream commerce marketplace focused on collectibles and resale categories. Whatnot offers limited public APIs for sellers/streamers and approved partners; integration is largely managed through the Whatnot Seller App and partner program rather than a self-serve developer portal.
finops:
- name: Whatnot Finops
  service_category: Marketplace
  slug: whatnot-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/whatnot.png
layout: provider
modified: '2026-05-08'
name: Whatnot
nav: Providers
network: true
overview: Whatnot publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Marketplace, Live Commerce, Collectibles, and Resale.
plans:
- name: Whatnot Plans Pricing
  plan_count: 1
  slug: whatnot-plans-pricing
random_paper: 17
rate_limits:
- limit_count: 1
  name: Whatnot Rate Limits
  slug: whatnot-rate-limits
screenshot: https://raw.githubusercontent.com/api-evangelist/whatnot/refs/heads/main/screenshots/whatnot-2026-06-20T201430.png
security:
- kind: domain-security
  name: Whatnot Domain Security
  slug: whatnot-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: whatnot
tags:
- Marketplace
- Live Commerce
- Collectibles
- Resale
website: https://www.whatnot.com/
---
