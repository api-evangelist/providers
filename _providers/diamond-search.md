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
  trial: false
  try_now: false
agentic_access:
- acting_count: 3
  human_in_the_loop: 0
  name: Diamond Search Agentic Access
  operation_count: 3
  slug: diamond-search-agentic-access
  summary_line: 3 operations · 3 acting
api_count: 3
apis:
- baseURL: https://api.idexonline.com/onsite/api
  baseurl_source: declared
  description: The Fullfeed API from Diamond Search — 1 operation(s) for fullfeed.
  name: Diamond Search Fullfeed API
  slug: diamond-search-fullfeed-api
- baseURL: https://api.idexonline.com/onsite/api
  baseurl_source: declared
  description: The Getreport3 API from Diamond Search — 1 operation(s) for getreport3.
  name: Diamond Search Getreport3 API
  slug: diamond-search-getreport3-api
- baseURL: https://api.idexonline.com/onsite/api
  baseurl_source: declared
  description: The Labgrownfullfile API from Diamond Search — 1 operation(s) for labgrownfullfile.
  name: Diamond Search Labgrownfullfile API
  slug: diamond-search-labgrownfullfile-api
artifact_total: 16
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Diamond Search IDEX Data API - Report 3 Fullfeed API
  slug: open-diamond-search-fullfeed-api
- collection_type: open
  name: Diamond Search IDEX Data API - Report 3 Fullfeed Getreport3 API
  slug: open-diamond-search-getreport3-api
- collection_type: open
  name: Diamond Search IDEX Data API - Report 3 Fullfeed Labgrownfullfile API
  slug: open-diamond-search-labgrownfullfile-api
- collection_type: open
  name: Diamond Search IDEX Data API - Report 3
  slug: open-idex-data-report-api
- collection_type: open
  name: Diamond Search Lab Grown Diamond Feed API
  slug: open-idex-lab-grown-file-api
- collection_type: open
  name: Diamond Search IDEX Onsite Full Feed API
  slug: open-idex-onsite-full-feed-api
common:
- group: company
  title: ''
  type: Website
  url: https://www.idexonline.com/
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/diamond-search-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/diamond-search-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/diamond-search-authentication.yml
- group: company
  title: ''
  type: Newsroom
  url: http://www.idexonline.com/rssfeeds
- group: start
  title: ''
  type: Login
  url: https://www.idexonline.com/ns24/auth/login.aspx
- group: start
  title: ''
  type: Signup
  url: https://www.idexonline.com/register.aspx
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: http://www.idexonline.com/Privacy
- group: commercial
  title: ''
  type: TermsOfService
  url: http://www.idexonline.com/Conditions
created: '2024-11-13'
description: IDEX Online is the leading polished diamonds trading platform for professionals, providing unbiased, market-driven diamond pricing tools, news and research. The IDEX Onsite and Data Report APIs deliver natural diamond, lab grown diamond, and market data feeds to subscribers of the IDEX trading platform.
finops:
- name: Diamond Search Finops
  service_category: Market Data / Diamond Trading
  slug: diamond-search-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/diamond-search.png
layout: provider
modified: '2026-05-19'
name: Diamond Search
nav: Providers
network: true
overview: 'Diamond Search publishes 3 APIs on the [APIs.io](https://apis.io/) network: Fullfeed API, Getreport3 API, and Labgrownfullfile API. Tagged areas include Diamonds, Lab Grown, Pricing, and Trading.


  Diamond Search''s developer surface includes authentication, signup flow, and 7 more developer resources.'
plans:
- name: Diamond Search Plans Pricing
  plan_count: 4
  slug: diamond-search-plans-pricing
random_paper: 0
rate_limits:
- limit_count: 1
  name: Diamond Search Rate Limits
  slug: diamond-search-rate-limits
screenshot: https://raw.githubusercontent.com/api-evangelist/diamond-search/refs/heads/main/screenshots/diamond-search-2026-06-20T180003.png
security:
- kind: authentication
  name: Diamond Search Authentication
  slug: diamond-search-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Diamond Search Domain Security
  slug: diamond-search-domain-security
  summary_line: TLSv1.2 · DMARC
slug: diamond-search
tags:
- Diamonds
- Lab Grown
- Pricing
- Trading
website: https://www.idexonline.com/
---
