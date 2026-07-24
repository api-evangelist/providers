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
agent_readiness:
  band: agent-aware
  dimensions:
    agent_skills: false
    agentic_access: false
    asyncapi_events: false
    auth_clarity: false
    consent_identity: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.1
  score: 17.3
  scored_at: '2026-07-23'
api_count: 2
apis:
- description: Modern REST API for Sage Intacct's cloud accounting and financial management platform covering general ledger, AP, AR, cash management, orders, purchasing, projects, and dimensions. Uses OAuth 2.0 Bea
  name: Sage Intacct REST API
  slug: rest-api
- description: Legacy XML-based API for Sage Intacct accounting and financial management, providing broad coverage of every object in the platform via SOAP-style function calls.
  name: Sage Intacct XML API
  slug: xml-api
artifact_total: 4
common:
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/sage-intacct-accounting-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/sage-intacct-accounting-domain-security.yml
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
- group: commercial
  title: ''
  type: Pricing
  url: https://www.sage.com/en-us/sage-business-cloud/intacct/pricing/
- group: start
  title: ''
  type: Login
  url: https://www.intacct.com/ia/acct/login.phtml
- group: company
  title: ''
  type: Blog
  url: https://www.sage.com/en-us/blog/category/intacct/
- group: operate
  title: ''
  type: Support
  url: https://www.sage.com/en-us/support/
- group: operate
  title: ''
  type: Community
  url: https://communityhub.sage.com/us/sage_intacct
created: '2026-05-11'
description: Sage Intacct is a cloud-based accounting and financial management platform positioned for mid-market businesses, multi-entity organizations, nonprofits, and accounting firms. It delivers core accounting (general ledger, accounts payable, accounts receivable, cash management, order management, purchasing) alongside advanced capabilities for revenue recognition, project accounting, multi-entity consolidations, and dimensional reporting. The Sage Intacct REST API provides programmatic access to accounting and financial objects using OAuth 2.0 Bearer token authentication.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/sage-intacct-accounting.png
layout: provider
modified: '2026-05-11'
name: Sage Intacct Accounting
nav: Providers
network: true
overview: 'Sage Intacct Accounting publishes 1 API on the [APIs.io](https://apis.io/) network: Sage Intacct REST API. Tagged areas include Accounting, Financial Management, ERP, Cloud Accounting, and General Ledger.


  Sage Intacct Accounting''s developer surface includes documentation, pricing, engineering blog, support, and 8 more developer resources.'
random_paper: 20
score:
  band: emerging
  composite: 28.9
  delta: 0.0
  facets:
    commercial_clarity: 23.7
    contract_quality: 37.7
    developer_ergonomics: 23.9
    discoverability: 92.5
    governance: 0.0
    operational_transparency: 5.3
  previous_composite: 28.9
  schema_version: 0.5
  scored_at: '2026-07-23'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/sage-intacct-accounting/refs/heads/main/screenshots/sage-intacct-accounting-2026-06-20T193328.png
security:
- kind: domain-security
  name: Sage Intacct Accounting Domain Security
  slug: sage-intacct-accounting-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Sage Intacct Accounting Vulnerability Disclosure
  slug: sage-intacct-accounting-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: sage-intacct-accounting
tags:
- Accounting
- Financial Management
- ERP
- Cloud Accounting
- General Ledger
- Accounts Payable
- Accounts Receivable
- Revenue Recognition
- Multi-Entity
website: https://www.sage.com/en-us/sage-business-cloud/intacct/
---
