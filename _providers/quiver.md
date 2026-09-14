---
access_model:
  confidence: medium
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  - security
  trial: false
  try_now: true
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Quiver Agentic Access
  operation_count: 6
  slug: quiver-agentic-access
  summary_line: 6 operations
api_count: 1
apis:
- description: The Quiver Quantitative API provides REST access to alternative financial datasets including Congressional and Senate stock trading, insider transactions, lobbying disclosures, government contracts, c
  name: Quiver Quantitative API
  slug: quiver
- baseURL: https://api.quiverquant.com
  baseurl_source: declared
  description: The Beta API from Quiver Quantitative — 6 operation(s) for beta.
  name: Quiver Quantitative Beta API
  slug: quiver-beta-api
artifact_total: 11
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Quiver Quantitative Beta API
  slug: open-quiver-beta-api
- collection_type: open
  name: Quiver Quantitative API
  slug: open-quiver
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/quiver-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/quiver-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/quiver-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/quiver-quantitative
- group: company
  title: ''
  type: Website
  url: https://www.quiverquant.com/
- group: docs
  title: ''
  type: Documentation
  url: https://api.quiverquant.com/docs/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.quiverquant.com/pricing/
- group: start
  title: ''
  type: Signup
  url: https://www.quiverquant.com/signup/
- group: company
  title: ''
  type: Blog
  url: https://www.quiverquant.com/blog/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.quiverquant.com/terms/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.quiverquant.com/privacy/
created: '2025-02-12'
description: Quiver Quantitative is an alternative-data platform that aggregates non-traditional financial datasets and exposes them through a single API. The platform covers congressional and Senate trading, insider trading, lobbying activity, government contracts, corporate patents, executive compensation, institutional and ETF holdings, off-exchange activity, app ratings, and more, giving developers and quantitative researchers programmatic access to alternative data signals starting at $10 per month.
finops:
- name: Quiver Finops
  service_category: API
  slug: quiver-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/quiver.png
layout: provider
modified: '2026-04-28'
name: Quiver Quantitative
nav: Providers
network: true
overview: 'Quiver Quantitative publishes 1 API on the [APIs.io](https://apis.io/) network: Beta API. Tagged areas include Alternative Data, Financial Data, Investment Research, Market Data, and Government Data.


  Quiver Quantitative''s developer surface includes authentication, documentation, pricing, signup flow, engineering blog, and 6 more developer resources.'
plans:
- name: Quiver Plans Pricing
  plan_count: 3
  slug: quiver-plans-pricing
random_paper: 17
rate_limits:
- limit_count: 5
  name: Quiver Rate Limits
  slug: quiver-rate-limits
screenshot: https://raw.githubusercontent.com/api-evangelist/quiver/refs/heads/main/screenshots/quiver-2026-06-20T192443.png
security:
- kind: authentication
  name: Quiver Authentication
  slug: quiver-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Quiver Domain Security
  slug: quiver-domain-security
  summary_line: TLSv1.3 · DMARC
slug: quiver
tags:
- Alternative Data
- Financial Data
- Investment Research
- Market Data
- Government Data
- Congressional Trading
website: https://www.quiverquant.com/
---
