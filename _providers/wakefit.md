---
api_count: 0
artifact_total: 3
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/wakefit-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.wakefit.co/
- group: company
  title: ''
  type: Blog
  url: https://www.wakefit.co/blog/
- group: operate
  title: ''
  type: Support
  url: https://www.wakefit.co/contact-us
- group: operate
  title: ''
  type: HelpCenter
  url: https://www.wakefit.co/helpcenter/faq/all
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.wakefit.co/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.wakefit.co/privacy
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/wakefit-llms.txt
- group: commercial
  title: ''
  type: Plans
  url: plans/wakefit-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/wakefit-rate-limits.yml
coverage:
  checked: '2026-09-04'
  detail: Wakefit is a direct-to-consumer mattress and furniture retailer with no developer program at all — no developer.wakefit.co or docs.wakefit.co exists in DNS, and the only API-named host, api.wakefit.co, is a private Django helpdesk dashboard that returns a real 404 for every discovery path and a login form at /wakefit/login/.
  evidence:
  - status: 404
    url: https://api.wakefit.co/openapi.json
  - status: 200
    url: https://api.wakefit.co/wakefit/login/
  - status: 403
    url: https://www.wakefit.co/.well-known/api-catalog
  reason: no-developer-program
  state: none
created: '2026-09-04'
description: 'Wakefit Innovations Limited (wakefit.co) is an Indian direct-to-consumer home and sleep-solutions company founded in 2016 in Bengaluru, selling memory-foam and orthopaedic mattresses, beds, sofas, wardrobes, bedding, decor and the Wakefit Zense connected-sleep line (Regul8 mattress temperature controller and Track8 contactless sleep tracker) through its own e-commerce storefront, an offline retail network and Indian marketplaces. Wakefit operates as a retailer rather than a platform: it publishes no public developer program, no API documentation and no machine-readable API contract, and its storefront back end at api.wakefit.co is a private, login-gated internal dashboard. This profile records the company identity and the public pages it does serve.'
image: https://www.wakefit.co/favicon.ico
layout: provider
modified: '2026-09-04'
name: Wakefit
nav: Providers
network: true
overview: 'Wakefit is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Retail, E-Commerce, Consumer Goods, and Furniture.


  Wakefit''s developer surface includes engineering blog, support, and 8 more developer resources.'
plans:
- name: Wakefit Plans Pricing
  plan_count: 0
  slug: wakefit-plans-pricing
random_paper: 12
rate_limits:
- limit_count: 0
  name: Wakefit Rate Limits
  slug: wakefit-rate-limits
security:
- kind: domain-security
  name: Wakefit Domain Security
  slug: wakefit-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
slug: wakefit
tags:
- Company
- Retail
- E-Commerce
- Consumer Goods
- Furniture
- Home
- Sleep
- Direct To Consumer
- India
- Internet of Things
website: https://www.wakefit.co/
---
