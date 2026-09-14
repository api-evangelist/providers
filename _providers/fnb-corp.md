---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - security
  trial: false
  try_now: false
api_count: 1
apis:
- description: F.N.B. Corporation publishes no first-party developer API. Consumer-permissioned account, balance and transaction data for First National Bank of Pennsylvania is available only through third-party dat
  name: FNB Consumer Data Access (Aggregator-Only)
  slug: fnb-aggregator-data-access
artifact_total: 2
common:
- group: start
  title: ''
  type: Login
  url: https://www.fnb-online.com/documentcenter/account/login
- group: auth
  title: ''
  type: DomainSecurity
  url: security/fnb-corp-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.fnb-online.com/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.fnb-online.com/privacy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.fnb-online.com/terms-of-use
- group: operate
  title: ''
  type: Support
  url: https://www.fnb-online.com/contact-us
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/f-n-b--corporation
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/fnb-corp-llms.txt
created: '2026-07-23'
description: 'F.N.B. Corporation (NYSE: FNB) is a diversified financial services holding company headquartered in Pittsburgh, Pennsylvania, and the parent of First National Bank of Pennsylvania, an FDIC-insured, state-chartered commercial bank. With roughly $50 billion in total assets at year-end 2025, FNB is a regional super-community bank operating around 350 branches across seven states and Washington, D.C. (Pennsylvania, Ohio, Maryland, West Virginia, North Carolina, South Carolina and Virginia), offering commercial banking, consumer banking and wealth management through its eStore digital platform. On open finance, FNB exposes NO first-party public developer portal or documented API: the developer/api subdomains of fnb-online.com redirect to the marketing homepage and no developer documentation is published. Consumer-permissioned account and transaction data is reachable only through third-party aggregators (notably Plaid), not a first-party FNB API. No direct Financial Data Exchange
  (FDX) membership or public CFPB Section 1033 posture is documented by the institution as of this profile.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/apis-json-logo.jpg
layout: provider
modified: '2026-07-23'
name: F.N.B. Corporation
nav: Providers
network: true
overview: 'F.N.B. Corporation publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Financial-Services, Banking, United States, Regional Bank, and Consumer Banking.


  F.N.B. Corporation''s developer surface includes support and 7 more developer resources.'
random_paper: 14
screenshot: https://raw.githubusercontent.com/api-evangelist/fnb-corp/refs/heads/main/screenshots/fnb-corp-2026-07-25T214900.png
security:
- kind: domain-security
  name: Fnb Corp Domain Security
  slug: fnb-corp-domain-security
  summary_line: TLSv1.2 · HSTS · DNSSEC · DMARC
slug: fnb-corp
tags:
- Financial-Services
- Banking
- United States
- Regional Bank
- Consumer Banking
- Commercial Banking
- Wealth Management
- Data Aggregation
- Open Finance
website: https://www.fnb-online.com/
---
