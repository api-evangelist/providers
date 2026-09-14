---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source: []
  trial: false
  try_now: false
api_count: 0
artifact_total: 3
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/world-kinect-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.world-kinect.com
- group: company
  title: ''
  type: About
  url: https://www.world-kinect.com/about-us
- group: operate
  title: ''
  type: Support
  url: https://www.world-kinect.com/about-us/contact-world-kinect
- group: start
  title: ''
  type: Login
  url: https://www.world-kinect.com/fuel-lubricants/world-kinect-customer-portals
- group: company
  title: ''
  type: Blog
  url: https://www.world-kinect.com/news-insights
- group: company
  title: ''
  type: BlogRSS
  url: https://www.world-kinect.com/rss.xml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.world-kinect.com/website-terms-and-conditions
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.world-kinect.com/your-privacy-center
- group: company
  title: ''
  type: Careers
  url: https://www.world-kinect.com/careers
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/world-kinect
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/world-kinect-llms.txt
- group: commercial
  title: ''
  type: Plans
  url: plans/world-kinect-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/world-kinect-rate-limits.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/world-kinect-conformance.yml
coverage:
  checked: '2026-09-04'
  detail: World Kinect's fuel-price and AVCARD API is real and reaches operators through third-party flight-operations platforms, but it has no public reference — the only route in is the Portal Access request form, and every myWorld portal host answers HTTP 200 with an Angular SPA shell for /api-docs, /openapi.json and every /.well-known/ path.
  evidence:
  - status: 200
    url: https://www.world-kinect.com/about-us/contact-us/portal-access-form
  - status: 200
    url: https://myworld.air.wfscorp.com/api-docs
  - status: 404
    url: https://www.world-kinect.com/llms.txt
  - status: 200
    url: https://www.world-kinect.com/sitemap.xml
  reason: customer-only-docs
  state: gated
created: '2026-03-21'
description: 'World Kinect Corporation (NYSE: WKC), formerly World Fuel Services, is a Fortune 500 energy, commodities and services company headquartered in Doral, Florida. It supplies and manages aviation, marine and land fuel, lubricants, natural gas, power, water and carbon-management services for airlines, business aviation operators, shipping lines, commercial fleets, fuel retailers and industrial customers in more than 200 countries. Its digital surface is a family of authenticated customer portals — myWorld for aviation, land, marine and carbon management, World Kinect Online for energy services, and the Flyers Energy and Quick Fuel Vantage/Advantage portals — plus a fuel-price and AVCARD integration that reaches operators through third-party flight-operations platforms. World Kinect publishes no public developer portal, API reference or machine-readable API contract.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/world-kinect.png
layout: provider
modified: '2026-09-04'
name: World Kinect
nav: Providers
network: true
overview: 'World Kinect is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Fortune 500, Energy, Fuel, Aviation, and Marine.


  World Kinect''s developer surface includes support, engineering blog, and 13 more developer resources.'
plans:
- name: World Kinect Plans Pricing
  plan_count: 0
  slug: world-kinect-plans-pricing
random_paper: 17
rate_limits:
- limit_count: 0
  name: World Kinect Rate Limits
  slug: world-kinect-rate-limits
screenshot: https://raw.githubusercontent.com/api-evangelist/world-kinect/refs/heads/main/screenshots/world-kinect-2026-06-20T201623.png
security:
- kind: domain-security
  name: World Kinect Domain Security
  slug: world-kinect-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: world-kinect
tags:
- Fortune 500
- Energy
- Fuel
- Aviation
- Marine
- Transportation
- Sustainability
- Commodities
- Logistics
website: https://www.world-kinect.com
---
