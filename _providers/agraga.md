---
api_count: 0
artifact_total: 3
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/agraga-domain-security.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/agraga-llms.txt
- group: commercial
  title: ''
  type: Plans
  url: plans/agraga-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/agraga-rate-limits.yml
- group: company
  title: ''
  type: Website
  url: https://www.agraga.com/
- group: company
  title: ''
  type: About
  url: https://www.agraga.com/about
- group: other
  title: ''
  type: Services
  url: https://www.agraga.com/products
- group: operate
  title: ''
  type: Support
  url: https://www.agraga.com/contact
- group: start
  title: ''
  type: SignUp
  url: https://booking.agraga.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.agraga.com/terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.agraga.com/privacy-policy
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/agraga
coverage:
  checked: '2026-09-12'
  detail: 'Agraga sells freight, not software: its marketing site is a seven-route React SPA whose bundle never once contains the string "API", there is no GitHub organization (api.github.com/orgs/agraga returns 404) and no package in any registry, and the only API hosts that exist - api.agraga.com and pricing.agraga.com, both found in Agraga''s own booking-app bundle - are private backends that answer every anonymous path, well-known namespace included, with 401 {"error":"Invalid Token"}.'
  evidence:
  - status: 401
    url: https://api.agraga.com/openapi.json
  - status: 401
    url: https://api.agraga.com/.well-known/agent-card.json
  - status: 401
    url: https://pricing.agraga.com/
  - status: 404
    url: https://api.github.com/orgs/agraga
  - status: 404
    url: https://notify.agraga.com/.well-known/api-catalog
  - status: 401
    url: https://api.agraga.com/api-docs
  - status: 404
    url: https://files.agraga.com/.well-known/security.txt
  reason: no-developer-program
  state: none
created: '2026-09-12'
description: Agraga (operated by Virya Logistics Technologies Private Limited) is a Chennai, India based digital cross-border logistics platform founded in 2021 by Anoop Raghavan and Venkatesh Narayanaswamy. It positions itself as a single operator for every leg of a shipment, bringing ocean freight, air freight, domestic transport, customs broking, warehousing, e-commerce fulfilment and embedded trade finance onto one booking and tracking platform aimed at underserved Indian MSME exporters and importers. It reports 700+ customers and 1,000+ vendors across 40-plus markets, and raised INR 100 crore in a pre-Series B round led by Bajaj Finserv with IvyCap Ventures. As of this profile Agraga publishes no public developer program, API documentation, SDK or machine-readable API contract; its platform backends are private and answer every anonymous request with an authentication error.
image: https://www.agraga.com/assets/agraga-logo-BtkIvqFd.png
layout: provider
modified: '2026-09-12'
name: Agraga
nav: Providers
network: true
overview: 'Agraga is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Logistics, Freight, Freight Forwarding, Supply Chain, and Shipping.


  Agraga''s developer surface includes support, signup flow, and 10 more developer resources.'
plans:
- name: Agraga Plans Pricing
  plan_count: 0
  slug: agraga-plans-pricing
random_paper: 2
rate_limits:
- limit_count: 0
  name: Agraga Rate Limits
  slug: agraga-rate-limits
security:
- kind: domain-security
  name: Agraga Domain Security
  slug: agraga-domain-security
  summary_line: TLSv1.3 · DMARC
slug: agraga
tags:
- Logistics
- Freight
- Freight Forwarding
- Supply Chain
- Shipping
- Customs
- Warehousing
- Embedded Finance
- Trade
- India
- Company
website: https://www.agraga.com/
---
