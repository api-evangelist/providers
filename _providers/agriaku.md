---
api_count: 0
artifact_total: 3
common:
- group: company
  title: ''
  type: Website
  url: https://agriaku.com/
- group: company
  title: ''
  type: About
  url: https://agriaku.com/about-us/
- group: company
  title: ''
  type: Blog
  url: https://agriaku.com/blog/
- group: company
  title: ''
  type: BlogRSS
  url: https://agriaku.com/feed/
- group: operate
  title: ''
  type: Support
  url: https://agriaku.com/contact-us/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://agriaku.com/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://agriaku.com/privacy-policy
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Agriaku
- group: company
  title: ''
  type: Partners
  url: https://agriaku.com/mitra/
- group: auth
  title: ''
  type: DomainSecurity
  url: security/agriaku-domain-security.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/agriaku-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/agriaku-rate-limits.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/agriaku-llms.txt
coverage:
  checked: '2026-09-12'
  detail: AgriAku ships only first-party end-user apps (Mitra, Logistik Kurir, a vendor platform) - there is no developer portal, API reference or published contract on agriaku.com or on any of the 19 subdomains in its certificate-transparency record, every spec path 404s, and the one API host it ever named, api.agriaku.com, is now a dangling CNAME to an AWS load balancer that no longer resolves.
  evidence:
  - status: 404
    url: https://agriaku.com/openapi.json
  - status: 404
    url: https://agriaku.com/.well-known/api-catalog
  - status: 401
    url: https://agriaku.com/wp-json/
  - status: 404
    url: https://agriaku.com/llms.txt
  reason: no-developer-program
  state: none
created: '2026-09-12'
description: 'AgriAku (PT Agriaku Digital Indonesia) is a Jakarta-based agritech company founded in 2021 that digitizes the distribution of agricultural inputs - seeds, fertilizers, crop protection, nutrients and farm tools - to Indonesia''s network of independent farm-supply shops (toko tani). Partner shops order from a catalog of more than 15,000 agricultural products through the AgriAku Mitra Android app, while separate vendor, seller and courier applications cover the rest of the supply chain. The company reports more than 23,390 partners across Indonesia and has raised roughly USD 46M from Alpha JWC Ventures, Go-Ventures and MDI Ventures. AgriAku operates no public developer program: every API host it runs is a private backend for its own first-party mobile and web applications.'
image: https://agriaku.com/wp-content/uploads/2021/06/Final-Logo-Highres-full-color-min.png
layout: provider
modified: '2026-09-12'
name: AgriAku
nav: Providers
network: true
overview: 'AgriAku is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Agriculture, AgTech, E-Commerce, and Marketplace.


  AgriAku''s developer surface includes engineering blog, support, and 11 more developer resources.'
plans:
- name: Agriaku Plans Pricing
  plan_count: 0
  slug: agriaku-plans-pricing
random_paper: 5
rate_limits:
- limit_count: 0
  name: Agriaku Rate Limits
  slug: agriaku-rate-limits
security:
- kind: domain-security
  name: Agriaku Domain Security
  slug: agriaku-domain-security
  summary_line: TLSv1.3
slug: agriaku
tags:
- Company
- Agriculture
- AgTech
- E-Commerce
- Marketplace
- Supply Chain
- Distribution
- Indonesia
- B2B
- Mobile
website: https://agriaku.com/
---
