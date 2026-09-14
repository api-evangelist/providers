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
api_count: 2
apis:
- description: 'Modern REST API for Sage Intacct using OAuth 2.0 Bearer token authentication. Provides standard HTTP verbs for managing core financial objects (GL, AP, AR), dimensions, customers, vendors, and custom '
  name: Sage Intacct REST API
  slug: rest-api
- description: Legacy XML API providing programmatic access to general ledger, accounts payable, accounts receivable, order entry, purchasing, inventory, projects, and platform services. Uses session-based authentic
  name: Sage Intacct XML API
  slug: xml-api
artifact_total: 5
common:
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/sage-intacct-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/sage-intacct-domain-security.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/intacct
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/sageintacct
- group: company
  title: ''
  type: Website
  url: https://www.sage.com/en-us/sage-business-cloud/intacct/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.sage.com/intacct
- group: docs
  title: ''
  type: Documentation
  url: https://developer.sage.com/intacct/docs/
- group: operate
  title: ''
  type: Community
  url: https://developer-community.sage.com/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.sage.com/en-us/sage-business-cloud/intacct/pricing/
- group: company
  title: ''
  type: Blog
  url: https://www.sage.com/en-us/blog/feed/
created: '2026-05-11'
description: Sage Intacct is a cloud-based financial management and accounting platform built for growing and mid-market businesses, covering core financials, multi-entity consolidations, project and revenue accounting, and advanced reporting. Sage Intacct offers both a modern REST API (OAuth 2.0) and a long-standing XML API for programmatic access to general ledger, accounts payable, accounts receivable, cash management, order entry, purchasing, and custom dimensions.
graphqls:
- description: This conceptual GraphQL schema represents the Sage Intacct cloud financial management data model. Sage Intacct exposes its data through a REST API (OAuth 2.0) and a legacy XML API. This schema maps th
  name: Sage Intacct GraphQL Schema
  slug: sage-intacct-graphql
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/sage-intacct.png
layout: provider
modified: '2026-05-11'
name: Sage Intacct
nav: Providers
network: true
overview: 'Sage Intacct publishes 1 API on the [APIs.io](https://apis.io/) network: REST API. Tagged areas include Accounting, Financial Management, ERP, General Ledger, and Accounts Payable.


  Sage Intacct''s developer surface includes documentation, pricing, engineering blog, and 7 more developer resources.'
random_paper: 6
screenshot: https://raw.githubusercontent.com/api-evangelist/sage-intacct/refs/heads/main/screenshots/sage-intacct-2026-06-20T193327.png
security:
- kind: domain-security
  name: Sage Intacct Domain Security
  slug: sage-intacct-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Sage Intacct Vulnerability Disclosure
  slug: sage-intacct-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: sage-intacct
tags:
- Accounting
- Financial Management
- ERP
- General Ledger
- Accounts Payable
- Accounts Receivable
- Mid-Market
website: https://www.sage.com/en-us/sage-business-cloud/intacct/
---
