---
access_model:
  confidence: medium
  label: Requires approval
  onboarding: approval
  pricing: unknown
  public: false
  source: []
  trial: false
  try_now: false
api_count: 0
artifact_total: 1
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/foot-locker-domain-security.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/foot-locker-llms.txt
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/footlocker
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/footlocker
- group: company
  title: ''
  type: Website
  url: https://www.footlocker.com/
- group: other
  title: ''
  type: CorporateSite
  url: https://www.footlocker-inc.com/
- group: company
  title: ''
  type: InvestorRelations
  url: https://investors.footlocker-inc.com/
- group: company
  title: ''
  type: Careers
  url: https://careers.footlocker.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.footlocker.com/help/terms-of-use.html
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.footlocker.com/help/privacy-statement.html
- group: other
  title: ''
  type: AffiliateProgram
  url: https://www.footlocker.com/affiliates.html
coverage:
  checked: '2026-09-10'
  detail: Foot Locker publishes no developer site of its own — its one real API, the Foot Locker/Eastbay supplier inventory feed, is documented inside CommerceHub's Dsco platform, whose docs host answers HTTP 403 behind a TLS certificate that expired in December 2025.
  evidence:
  - status: 403
    url: https://gandalf.dsco.io/platform_content/fleast-updatinginventory-api/
  - status: 404
    url: https://www.footlocker.com/.well-known/api-catalog
  - status: 200
    url: https://www.footlocker.com/openapi.json
  reason: marketplace-only
  state: gated
created: '2026-03-21'
description: 'Foot Locker, Inc. is a global retailer of athletic footwear and apparel, operating the Foot Locker, Kids Foot Locker, Champs Sports, WSS and atmos banners across North America, Europe, Asia and Australia. DICK''S Sporting Goods completed its acquisition of Foot Locker, Inc. on September 8, 2025 and continues to operate the Foot Locker brand suite. Foot Locker publishes no public developer portal, API reference or machine-readable contract. Trading-partner integration runs through third-party host platforms rather than a first-party developer site: supplier inventory and dropship through CommerceHub Dsco, and the Storefronts creator/affiliate program through impact.com, each requiring a commercial agreement. The former api.footlocker.com Apigee gateway no longer resolves.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/foot-locker.png
layout: provider
modified: '2026-09-10'
name: Foot Locker
nav: Providers
network: true
overview: Foot Locker is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Fortune 500, Retail, Footwear, Apparel, and E-Commerce.
press:
- date: '2026-05-25'
  title: FOOT LOCKER, INC. REPORTS PRELIMINARY FIRST ...
  url: https://www.prnewswire.com/news-releases/foot-locker-inc-reports-preliminary-first-quarter-2025-financial-results-302456491.html
- date: '2026-05-25'
  title: Foot Locker analyzes customer feedback with AI
  url: https://chainstoreage.com/foot-locker-analyzes-customer-feedback-ai
- date: '2026-05-25'
  title: How Foot Locker Stepped Into a Gen AI Marketing Journey
  url: https://www.smartly.io/resources/how-foot-locker-stepped-into-a-gen-ai-marketing-journey
- date: '2026-05-25'
  title: DICK'S Sporting Goods Completes Acquisition of Foot Locker
  url: https://www.prnewswire.com/news-releases/dicks-sporting-goods-completes-acquisition-of-foot-locker-302548690.html
- date: '2026-05-25'
  title: Foot Locker – InMoment
  url: https://inmoment.com/customer-stories/foot-locker-uses-ai-npl-text-analytics/
random_paper: 12
security:
- kind: domain-security
  name: Foot Locker Domain Security
  slug: foot-locker-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: foot-locker
tags:
- Fortune 500
- Retail
- Footwear
- Apparel
- E-Commerce
- Sneakers
- Omnichannel
website: https://www.footlocker.com/
---
