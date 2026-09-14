---
access_model:
  confidence: medium
  label: Freemium
  onboarding: unknown
  pricing: freemium
  public: false
  source:
  - plans
  trial: false
  try_now: false
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Bureau Of Economic Analysis Agentic Access
  operation_count: 1
  slug: bureau-of-economic-analysis-agentic-access
  summary_line: 1 operation
api_count: 1
apis:
- description: Gross Domestic Product (GDP) data from the BEA, available quarterly and annually. Includes GDP growth rates, GDP by expenditure components, and real vs. nominal GDP measures.
  name: BEA GDP Data
  slug: bea-gdp-data
- baseURL: https://apps.bea.gov/api/data
  baseurl_source: declared
  description: The Bureau Of Economic Analysis (BEA) API API from Bureau of Economic Analysis — 1 operation(s) for bureau of economic analysis (bea) api.
  name: Bureau of Economic Analysis Bureau Of Economic Analysis (BEA) API API
  slug: bureau-of-economic-analysis-bureau-of-economic-analysis-bea-api-api
artifact_total: 10
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Bureau of Economic Analysis (BEA) API
  slug: open-bureau-of-economic-analysis-bea-api
- collection_type: open
  name: Bureau of Economic Analysis (BEA) Bureau Of Economic Analysis (BEA) API API
  slug: open-bureau-of-economic-analysis-bureau-of-economic-analysis-bea-api-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/bureau-of-economic-analysis-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/bureau-of-economic-analysis-domain-security.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/us-bea
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/bureau-of-economic-analysis
- group: start
  title: ''
  type: Portal
  url: https://www.bea.gov/tools/
- group: docs
  title: ''
  type: Documentation
  url: https://apps.bea.gov/API/docs/index.htm
- group: start
  title: ''
  type: GettingStarted
  url: https://www.bea.gov/tools/faq
- group: company
  title: ''
  type: Website
  url: https://www.bea.gov/
- group: start
  title: ''
  type: Signup
  url: https://apps.bea.gov/API/signup/index.cfm
- group: other
  title: ''
  type: Data Visualizations
  url: https://www.bea.gov/itable/
- group: operate
  title: ''
  type: Press Releases
  url: https://www.bea.gov/news
- group: company
  title: ''
  type: Blog
  url: https://apps.bea.gov/rss/rss.xml
created: '2024-01-01'
description: The U.S. Bureau of Economic Analysis (BEA) is a principal federal statistical agency that produces accurate and objective data about the U.S. economy. BEA publishes GDP, personal income, corporate profits, international trade and investment data, and industry-level economic accounts. The BEA Data API provides programmatic access to these economic statistics.
finops:
- name: Bureau Of Economic Analysis Finops
  service_category: API
  slug: bureau-of-economic-analysis-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/bureau-of-economic-analysis.png
layout: provider
modified: '2026-05-19'
name: Bureau of Economic Analysis
nav: Providers
network: true
overview: 'Bureau of Economic Analysis publishes 1 API on the [APIs.io](https://apis.io/) network: Bureau Of Economic Analysis (BEA) API API. Tagged areas include Economics, Federal-Government, GDP, National Accounts, and Statistics.


  Bureau of Economic Analysis'' developer surface includes developer portal, documentation, getting-started guide, signup flow, engineering blog, and 7 more developer resources.'
plans:
- name: Bureau Of Economic Analysis Plans Pricing
  plan_count: 3
  slug: bureau-of-economic-analysis-plans-pricing
random_paper: 17
rate_limits:
- limit_count: 5
  name: Bureau Of Economic Analysis Rate Limits
  slug: bureau-of-economic-analysis-rate-limits
screenshot: https://raw.githubusercontent.com/api-evangelist/bureau-of-economic-analysis/refs/heads/main/screenshots/bureau-of-economic-analysis-2026-06-20T173804.png
security:
- kind: domain-security
  name: Bureau Of Economic Analysis Domain Security
  slug: bureau-of-economic-analysis-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: bureau-of-economic-analysis
tags:
- Economics
- Federal-Government
- GDP
- National Accounts
- Statistics
- Trade
website: https://www.bea.gov/
---
