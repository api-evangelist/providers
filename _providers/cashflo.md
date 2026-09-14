---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - authentication
  - security
  trial: false
  try_now: false
api_count: 1
apis:
- baseURL: https://developer.cashflo.io
  baseurl_source: declared
  description: The Ingest API from CashFlo — 3 operation(s) for ingest.
  name: CashFlo Ingest API
  slug: cashflo-ingest-api
artifact_total: 5
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Cashflo Data Ingestion API Documentation Ingest API
  slug: open-cashflo-ingest-api
common:
- group: company
  title: ''
  type: Website
  url: https://www.cashflo.io/
- group: agent
  title: ''
  type: AgentSkill
  url: skills/cashflo-ingest-grns.md
- group: agent
  title: ''
  type: X-MCPServerCandidate
  url: mcp/cashflo-mcp.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/cashflo-data-ingestion-overlay.yaml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.cashflo.io
- group: docs
  title: ''
  type: Documentation
  url: https://developer.cashflo.io
- group: docs
  title: ''
  type: APIReference
  url: https://developer.cashflo.io
- group: auth
  title: ''
  type: Authentication
  url: authentication/cashflo-authentication.yml
- group: design
  title: ''
  type: Idempotency
  url: conventions/cashflo-conventions.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/cashflo-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/cashflo-lifecycle.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/cashflo-domain-security.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/cashflo-llms.txt
- group: auth
  title: ''
  type: TrustCenter
  url: https://trust.cashflo.io
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/cashflo
- group: company
  title: ''
  type: Blog
  url: https://www.cashflo.io/magazine
- group: start
  title: ''
  type: Login
  url: https://app.cashflo.io/#/account/login
- group: operate
  title: ''
  type: Support
  url: https://www.cashflo.io/talk-to-us
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.cashflo.io/tnc/terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.cashflo.io/tnc/privacy-policy
created: '2026-07-17'
description: CashFlo is an India-based fintech platform that automates enterprise finance operations across accounts payable, payments, GST compliance, vendor management, and supply-chain financing. Its modules cover invoice OCR and n-way matching, approval workflows, multi-bank payments and reconciliation, GST filing / e-invoicing / e-way bills, vendor onboarding and KYC, and dynamic cash discounting for working-capital optimization. CashFlo connects to major ERPs (SAP ECC/S4 HANA/Business One, Oracle NetSuite/Fusion/EBS, Microsoft Dynamics 365/NAV/Business Central) and exposes a JWT-secured Data Ingestion API for pushing purchase orders and goods-receipt notes into the platform. Backed by General Catalyst.
image: https://cdn.prod.website-files.com/649d312d8aeae2926e7af2fe/674acdb7d5b408c0e8e9cf34_Homepage.webp
layout: provider
modified: '2026-07-18'
name: CashFlo
nav: Providers
network: true
overview: 'CashFlo publishes 1 API on the [APIs.io](https://apis.io/) network: Ingest API. Tagged areas include Company, Fintech, Accounts Payable, Payments, and Working Capital.


  CashFlo''s developer surface includes documentation, API reference, authentication, engineering blog, support, and 15 more developer resources.'
random_paper: 1
screenshot: https://raw.githubusercontent.com/api-evangelist/cashflo/refs/heads/main/screenshots/cashflo-2026-07-25T204721.png
security:
- kind: authentication
  name: Cashflo Authentication
  slug: cashflo-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Cashflo Domain Security
  slug: cashflo-domain-security
  summary_line: TLSv1.3 · DMARC
slug: cashflo
tags:
- Company
- Fintech
- Accounts Payable
- Payments
- Working Capital
- Supply Chain Finance
- ERP Integration
- Compliance
- India
website: https://www.cashflo.io/
---
