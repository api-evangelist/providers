---
api_count: 0
artifact_total: 4
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/adore-me-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.adoreme.com/
- group: company
  title: ''
  type: Blog
  url: https://www.adoreme.com/blog
- group: operate
  title: ''
  type: Support
  url: https://help.adoreme.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.adoreme.com/terms-conditions
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.adoreme.com/privacy-policy
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/adore-me
- group: operate
  title: ''
  type: StatusPage
  url: https://status.adoreme.com/
- group: auth
  title: ''
  type: Security
  url: https://bugcrowd.com/adoreme-vdp
- group: company
  title: ''
  type: Press
  url: https://www.adoreme.com/press
- group: company
  title: ''
  type: About
  url: https://www.adoreme.com/our-story
- group: other
  title: ''
  type: iOSApp
  url: https://apps.apple.com/us/app/adore-me-lingerie-womenswear/id661053119
- group: other
  title: ''
  type: AndroidApp
  url: https://play.google.com/store/apps/details?id=com.adoreme.android
- group: other
  title: ''
  type: SecondaryMarket
  url: https://forgeglobal.com/adore-me_stock/
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/adore-me-llms.txt
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/adore-me-lifecycle.yml
- group: build
  title: ''
  type: Packages
  url: packages/adore-me-packages.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/adore-me-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/adore-me-rate-limits.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/adore-me-vulnerability-disclosure.yml
coverage:
  checked: '2026-09-07'
  detail: Adore Me is a direct-to-consumer lingerie retailer with no developer program at all — no api./developer./docs. host resolves, the sitemap lists 67 pages that are entirely consumer retail content, and the storefront's own /api/v1 backend answers every unauthenticated request with the same 400 validation_error envelope while publishing no contract that describes it.
  evidence:
  - status: 400
    url: https://www.adoreme.com/api/v1
  - status: 404
    url: https://www.adoreme.com/.well-known/api-catalog
  - status: 200
    url: https://www.adoreme.com/v7/sitemap/pages.xml
  - status: 0
    url: https://developer.adoreme.com/
  reason: no-developer-program
  state: none
created: '2026-09-07'
description: 'Adore Me is a New York City based direct-to-consumer intimate apparel brand founded in 2011 by Morgan Hermand-Waiche, selling bras, panties, lingerie sets, sleepwear, swimwear, activewear and loungewear across an inclusive size range (bands 30-46, cups A-I, apparel XS-4X) through adoreme.com, native iOS and Android apps, and a small physical retail footprint. The company built a proprietary e-commerce and merchandising platform rather than buying a hosted storefront, and is known for the Elite Box home try-on program, an annual Premier membership, and published environmental, social and governance impact reporting. Victoria''s Secret & Co. acquired Adore Me for $400 million in cash, signing on 1 November 2022 and closing on 3 January 2023; Adore Me continues to operate as its own brand and its technology is being used to modernize the VS&Co digital platform. Adore Me operates no public developer program: it publishes no developer portal, no API reference, and no machine-readable
  API contract of any kind. Its storefront JSON backend under /api/ is an undocumented internal surface that rejects every unauthenticated request with a validation error. The public technical surface enrichment could verify is a well-formed provider-authored llms.txt covering the whole catalog, mobile app-association documents at /.well-known/, an Atlassian Statuspage, and a Bugcrowd vulnerability disclosure program.'
image: https://www.adoreme.com/assets/favicon/apple-touch-icon.png
layout: provider
modified: '2026-09-07'
name: Adore Me
nav: Providers
network: true
overview: 'Adore Me is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, E-Commerce, Retail, Apparel, and Intimate Apparel.


  Adore Me''s developer surface includes engineering blog, support, and 18 more developer resources.'
plans:
- name: Adore Me Plans Pricing
  plan_count: 0
  slug: adore-me-plans-pricing
random_paper: 1
rate_limits:
- limit_count: 0
  name: Adore Me Rate Limits
  slug: adore-me-rate-limits
security:
- kind: domain-security
  name: Adore Me Domain Security
  slug: adore-me-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Adore Me Vulnerability Disclosure
  slug: adore-me-vulnerability-disclosure
  summary_line: Bugcrowd
slug: adore-me
tags:
- Company
- E-Commerce
- Retail
- Apparel
- Intimate Apparel
- Direct to Consumer
- Fashion
- Consumer
- Subscription Commerce
- Mobile
website: https://www.adoreme.com/
---
