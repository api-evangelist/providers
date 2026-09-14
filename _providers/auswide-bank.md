---
access_model:
  confidence: medium
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - authentication
  trial: false
  try_now: false
api_count: 1
apis:
- baseURL: https://api.auswidebank.com.au/openbanking/cds-au/v1
  baseurl_source: declared
  description: Banking Account Balance endpoints
  name: Auswide Bank Banking Account Balances API
  slug: auswide-bank-banking-account-balances-api
- baseURL: https://api.auswidebank.com.au/openbanking/cds-au/v1
  baseurl_source: declared
  description: Banking Account Direct Debit endpoints
  name: Auswide Bank Banking Account Direct Debits API
  slug: auswide-bank-banking-account-direct-debits-api
- baseURL: https://api.auswidebank.com.au/openbanking/cds-au/v1
  baseurl_source: declared
  description: Banking Account Scheduled Payment endpoints
  name: Auswide Bank Banking Account Scheduled Payments API
  slug: auswide-bank-banking-account-scheduled-payments-api
- baseURL: https://api.auswidebank.com.au/openbanking/cds-au/v1
  baseurl_source: declared
  description: Banking Account Transaction endpoints
  name: Auswide Bank Banking Account Transactions API
  slug: auswide-bank-banking-account-transactions-api
- baseURL: https://api.auswidebank.com.au/openbanking/cds-au/v1
  baseurl_source: declared
  description: Banking Account endpoints
  name: Auswide Bank Banking Accounts API
  slug: auswide-bank-banking-accounts-api
- baseURL: https://api.auswidebank.com.au/openbanking/cds-au/v1
  baseurl_source: declared
  description: Banking Payee endpoints
  name: Auswide Bank Banking Payees API
  slug: auswide-bank-banking-payees-api
- baseURL: https://api.auswidebank.com.au/openbanking/cds-au/v1
  baseurl_source: declared
  description: Banking Product endpoints
  name: Auswide Bank Banking Products API
  slug: auswide-bank-banking-products-api
artifact_total: 18
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: CDR Banking Banking Account Balances API
  slug: open-auswide-bank-banking-account-balances-api
- collection_type: open
  name: CDR Banking Banking Account Balances Banking Account Direct Debits API
  slug: open-auswide-bank-banking-account-direct-debits-api
- collection_type: open
  name: CDR Banking Banking Account Balances Banking Account Scheduled Payments API
  slug: open-auswide-bank-banking-account-scheduled-payments-api
- collection_type: open
  name: CDR Banking Banking Account Balances Banking Account Transactions API
  slug: open-auswide-bank-banking-account-transactions-api
- collection_type: open
  name: CDR Banking Banking Account Balances Banking Accounts API
  slug: open-auswide-bank-banking-accounts-api
- collection_type: open
  name: CDR Banking Banking Account Balances Banking Payees API
  slug: open-auswide-bank-banking-payees-api
- collection_type: open
  name: CDR Banking Banking Account Balances Banking Products API
  slug: open-auswide-bank-banking-products-api
common:
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/auswide-bank-capability-edges.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/auswide-bank-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/auswide-bank-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/auswide-bank-scopes.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/auswide-bank-conformance.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/auswide-bank-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/auswide-bank-lifecycle.yml
- group: operate
  title: ''
  type: Deprecation
  url: lifecycle/auswide-bank-lifecycle.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/auswide-bank-conventions.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/auswide-bank-data-model.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/auswide-bank-cds-banking-products-overlay.yaml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/auswide-bank-llms.txt
- group: agent
  title: ''
  type: X-MCPServerCandidate
  url: mcp/auswide-bank-mcp.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/auswide-bank-product-lookup.md
- group: company
  title: ''
  type: Website
  url: https://www.auswidebank.com.au/
- group: docs
  title: ''
  type: Documentation
  url: https://www.auswidebank.com.au/help/banking-support/open-banking/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/auswide-bank-ltd/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.auswidebank.com.au/about/privacy-policy/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.auswidebank.com.au/about/website-terms-of-use/
- group: operate
  title: ''
  type: Support
  url: https://www.auswidebank.com.au/about/contact-us/
created: '2026-07-20'
description: Auswide Bank Ltd is an Australian authorised deposit-taking institution (ADI) headquartered in Bundaberg, Queensland, offering home loans, savings and transaction accounts, term deposits, credit cards, and personal and business banking. Formerly Wide Bay Australia and previously ASX-listed (ABA), Auswide is now a division of MyState Bank Limited, a wholly owned subsidiary of the ASX-listed MyState Limited (ASX MYS) following the 2025 merger. As an active CDR data holder under Australia's Consumer Data Right (Open Banking), Auswide exposes a public, unauthenticated Product Reference Data (PRD) API conforming to the DSB Consumer Data Standards, alongside the accredited-data-recipient consumer data sharing channels required of every Australian bank.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/auswide-bank.png
layout: provider
modified: '2026-07-21'
name: Auswide Bank
nav: Providers
network: true
overview: 'Auswide Bank publishes 7 APIs on the [APIs.io](https://apis.io/) network, including Banking Account Balances API, Banking Account Direct Debits API, Banking Account Scheduled Payments API, and 4 more. Tagged areas include Financial, Banks, Open Banking, CDR, and Consumer Banking.


  Auswide Bank''s developer surface includes authentication, documentation, support, and 17 more developer resources.'
random_paper: 14
scopes:
- name: Auswide Bank Scopes
  scope_count: 5
  slug: auswide-bank-scopes
  summary_line: 5 scopes · authorizationCode
screenshot: https://raw.githubusercontent.com/api-evangelist/auswide-bank/refs/heads/main/screenshots/auswide-bank-2026-07-21T114702.png
security:
- kind: authentication
  name: Auswide Bank Authentication
  slug: auswide-bank-authentication
  summary_line: none/oauth2/openIdConnect/mutualTLS · 4 schemes
- kind: domain-security
  name: Auswide Bank Domain Security
  slug: auswide-bank-domain-security
  summary_line: TLSv1.2 · HSTS · DMARC
slug: auswide-bank
tags:
- Financial
- Banks
- Open Banking
- CDR
- Consumer Banking
- Australia
- Product Reference Data
- ADI
website: https://www.auswidebank.com.au/
---
