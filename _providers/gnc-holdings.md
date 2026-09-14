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
artifact_total: 1
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/gnc-holdings-domain-security.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/gnc-holdings-llms.txt
- group: company
  title: ''
  type: Website
  url: https://www.gnc.com/
- group: company
  title: ''
  type: About
  url: https://www.gnc.com/about-gnc/about-us.html
- group: operate
  title: ''
  type: Support
  url: https://www.gnc.com/help-center.html
- group: company
  title: ''
  type: Blog
  url: https://www.gnc.com/learn
- group: operate
  title: ''
  type: Press Releases
  url: https://www.gnc.com/learn/newsroom
- group: other
  title: ''
  type: Stores
  url: https://stores.gnc.com/
- group: company
  title: ''
  type: Careers
  url: https://myjobs.adp.com/gnc/cx
- group: other
  title: ''
  type: Affiliate
  url: https://www.gnc.com/affiliate.html
- group: other
  title: ''
  type: Franchise
  url: https://gncfranchising.com/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.gnc.com/privacy-policy.html
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.gnc.com/help/safety-security-privacy.html
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/gnc
coverage:
  checked: '2026-09-12'
  detail: GNC is a physical-goods supplement retailer with no developer surface of any kind — api.gnc.com and developer.gnc.com do not resolve, none of the 3,819 URLs in its own sitemap is a developer or API page, and every /.well-known/ path plus /apis.json, /openapi.json and /llms.txt returns 404 on www.gnc.com, stores.gnc.com and gncfranchising.com; its storefront runs on Salesforce Commerce Cloud and its store locator on Yext, but neither vendor contract is published by GNC.
  evidence:
  - status: 404
    url: https://www.gnc.com/apis.json
  - status: 404
    url: https://www.gnc.com/llms.txt
  - status: 404
    url: https://www.gnc.com/.well-known/agent-card.json
  - status: 404
    url: https://www.gnc.com/.well-known/api-catalog
  - status: 404
    url: https://stores.gnc.com/openapi.json
  reason: not-a-software-company
  state: none
created: '2026-03-24'
description: GNC Holdings, LLC (General Nutrition Centers) is an American specialty retailer of health, wellness, and performance products including vitamins, minerals, herbal supplements, sports nutrition, diet, and energy products. Founded in 1935 and headquartered in Pittsburgh, Pennsylvania, GNC is a wholly owned subsidiary of Harbin Pharmaceutical Group following its 2020 acquisition. The company operates owned and franchised retail locations, online stores, and retail partnerships across approximately 50 countries.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/gnc-holdings.png
layout: provider
modified: '2026-09-12'
name: GNC Holdings
nav: Providers
network: true
overview: 'GNC Holdings is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Diet, Health, Nutrition, Retail, and Sports Nutrition.


  GNC Holdings'' developer surface includes support, engineering blog, and 12 more developer resources.'
press:
- date: '2026-05-25'
  title: GNC Becomes First Major Retailer to Launch GLP-1 ...
  url: https://www.prnewswire.com/news-releases/gnc-becomes-first-major-retailer-to-launch-glp-1-support-program-302129429.html
- date: '2026-05-25'
  title: GNC Holdings Inc.
  url: https://www.nytimes.com/topic/company/gnc-holdings-inc
- date: '2026-05-25'
  title: GNC reports sale of substantially of its assets to Harbin ...
  url: https://www.torys.com/work/2020/10/gnc-reports-sale-of-substantially-of-its-assets-to-harbin-pharmaceutical
- date: '2026-05-25'
  title: XBRL Viewer
  url: https://www.sec.gov/ix?doc=/Archives/edgar/data/1502034/000119312520144118/d882272d8k.htm
- date: '2026-05-25'
  title: Nutrient Content Market Hits New High | Major Giants GNC
  url: https://www.openpr.com/news/4412307/nutrient-content-market-hits-new-high-major-giants-gnc
random_paper: 16
screenshot: https://raw.githubusercontent.com/api-evangelist/gnc-holdings/refs/heads/main/screenshots/gnc-holdings-2026-06-20T181935.png
security:
- kind: domain-security
  name: Gnc Holdings Domain Security
  slug: gnc-holdings-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: gnc-holdings
tags:
- Diet
- Health
- Nutrition
- Retail
- Sports Nutrition
- Supplements
- Vitamins
- Wellness
- Fortune 1000
website: https://www.gnc.com/
---
