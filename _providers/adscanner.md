---
api_count: 0
artifact_total: 3
common:
- group: company
  title: ''
  type: Website
  url: https://www.alleyesonscreens.com/
- group: docs
  title: ''
  type: Documentation
  url: https://www.alleyesonscreens.com/faq
- group: operate
  title: ''
  type: Support
  url: https://www.alleyesonscreens.com/getintouch
- group: start
  title: ''
  type: SignUp
  url: https://cockpit.alleyesonscreens.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.alleyesonscreens.com/toc
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.alleyesonscreens.com/privacypolicy
- group: auth
  title: ''
  type: DomainSecurity
  url: security/adscanner-domain-security.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/adscanner-llms.txt
- group: commercial
  title: ''
  type: Plans
  url: plans/adscanner-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/adscanner-rate-limits.yml
coverage:
  checked: '2026-09-07'
  detail: The company's own FAQ states "our data can be obtained via reporting (pdf, Excel, CSV, json) and API on request", but there is no developer portal, no API reference and no spec anywhere on the site — the 29-URL sitemap has no /developers, /docs or /api page, and info@alleyesonscreens.com plus the /getintouch form are the only stated routes to the API.
  evidence:
  - status: 200
    url: https://www.alleyesonscreens.com/faq
  - status: 200
    url: https://www.alleyesonscreens.com/sitemap.xml
  - status: 404
    url: https://api.alleyesonscreens.com/openapi.json
  - status: 403
    url: https://api.alleyesonscreens.com/.well-known/api-catalog
  reason: sales-gate
  state: gated
created: '2026-09-07'
description: AdScanner — now trading as all eyes on screens (AEOS), the legal entity all eyes on screens d.o.o. of Zagreb, Croatia, formerly Adscanner d.o.o. — is a European TV and video advertising measurement, planning and activation platform founded in 2012. In-house AI video-recognition software matches broadcast ad creatives second-by-second against viewing data supplied by IPTV and telco partners, producing cross-channel reach, frequency and attribution measurement for linear, addressable and connected TV. Products include the AdScanner/AEOS Cockpit analytics dashboard, the Apollo AI-based ex-ante planning module, TV Boost data activation on post-code segments, and TV Match cross-device targeting and TV-sync signals that fire digital campaigns when a spot airs. AEOS operates in Croatia, Austria, Germany, Bulgaria and Switzerland. The company states in its own FAQ that its data can be obtained via reporting (PDF, Excel, CSV, JSON) and API on request, but publishes no public developer
  portal, API reference or machine-readable contract.
layout: provider
modified: '2026-09-07'
name: Adscanner
nav: Providers
network: true
overview: 'Adscanner is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Advertising, AdTech, Television, and Media Measurement.


  Adscanner''s developer surface includes documentation, support, signup flow, and 7 more developer resources.'
plans:
- name: Adscanner Plans Pricing
  plan_count: 0
  slug: adscanner-plans-pricing
random_paper: 19
rate_limits:
- limit_count: 0
  name: Adscanner Rate Limits
  slug: adscanner-rate-limits
security:
- kind: domain-security
  name: Adscanner Domain Security
  slug: adscanner-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: adscanner
tags:
- Company
- Advertising
- AdTech
- Television
- Media Measurement
- Analytics
- Attribution
- Connected TV
- Addressable TV
- Audience Data
- Artificial Intelligence
- Croatia
website: https://www.alleyesonscreens.com/
---
