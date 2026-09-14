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
- baseURL: https://openbanking.api.rabobank.com.au/public/cds-au/v1/banking/products
  baseurl_source: declared
  description: Banking Account Balance endpoints
  name: Rabobank Australia Banking Account Balances API
  slug: rabobank-australia-banking-account-balances-api
- baseURL: https://openbanking.api.rabobank.com.au/public/cds-au/v1/banking/products
  baseurl_source: declared
  description: Banking Account Direct Debit endpoints
  name: Rabobank Australia Banking Account Direct Debits API
  slug: rabobank-australia-banking-account-direct-debits-api
- baseURL: https://openbanking.api.rabobank.com.au/public/cds-au/v1/banking/products
  baseurl_source: declared
  description: Banking Account Scheduled Payment endpoints
  name: Rabobank Australia Banking Account Scheduled Payments API
  slug: rabobank-australia-banking-account-scheduled-payments-api
- baseURL: https://openbanking.api.rabobank.com.au/public/cds-au/v1/banking/products
  baseurl_source: declared
  description: Banking Account Transaction endpoints
  name: Rabobank Australia Banking Account Transactions API
  slug: rabobank-australia-banking-account-transactions-api
- baseURL: https://openbanking.api.rabobank.com.au/public/cds-au/v1/banking/products
  baseurl_source: declared
  description: Banking Account endpoints
  name: Rabobank Australia Banking Accounts API
  slug: rabobank-australia-banking-accounts-api
- baseURL: https://openbanking.api.rabobank.com.au/public/cds-au/v1/banking/products
  baseurl_source: declared
  description: Banking Payee endpoints
  name: Rabobank Australia Banking Payees API
  slug: rabobank-australia-banking-payees-api
- baseURL: https://openbanking.api.rabobank.com.au/public/cds-au/v1/banking/products
  baseurl_source: declared
  description: Banking Product endpoints
  name: Rabobank Australia Banking Products API
  slug: rabobank-australia-banking-products-api
artifact_total: 18
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: CDR Banking Banking Account Balances API
  slug: open-rabobank-australia-banking-account-balances-api
- collection_type: open
  name: CDR Banking Banking Account Balances Banking Account Direct Debits API
  slug: open-rabobank-australia-banking-account-direct-debits-api
- collection_type: open
  name: CDR Banking Banking Account Balances Banking Account Scheduled Payments API
  slug: open-rabobank-australia-banking-account-scheduled-payments-api
- collection_type: open
  name: CDR Banking Banking Account Balances Banking Account Transactions API
  slug: open-rabobank-australia-banking-account-transactions-api
- collection_type: open
  name: CDR Banking Banking Account Balances Banking Accounts API
  slug: open-rabobank-australia-banking-accounts-api
- collection_type: open
  name: CDR Banking Banking Account Balances Banking Payees API
  slug: open-rabobank-australia-banking-payees-api
- collection_type: open
  name: CDR Banking Banking Account Balances Banking Products API
  slug: open-rabobank-australia-banking-products-api
common:
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/rabobank-australia-capability-edges.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/rabobank-australia-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/rabobank-australia-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/rabobank-australia-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/rabobank-australia-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/rabobank-australia-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/rabobank-australia-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: conformance/rabobank-australia-conformance.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/rabobank-australia-scopes.yml
- group: operate
  title: ''
  type: Deprecation
  url: lifecycle/rabobank-australia-lifecycle.yml
- group: docs
  title: ''
  type: APIReference
  url: https://consumerdatastandardsaustralia.github.io/standards/#banking-apis
- group: design
  title: ''
  type: DataModel
  url: data-model/rabobank-australia-data-model.yml
- group: agent
  title: ''
  type: X-MCPServerCandidate
  url: mcp/rabobank-australia-mcp.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/rabobank-australia-list-products.md
- group: other
  title: ''
  type: Overlay
  url: overlays/rabobank-australia-cds-banking-products-overlay.yaml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/rabobank-australia-llms.txt
- group: company
  title: ''
  type: Website
  url: https://www.rabobank.com.au/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://openbanking.api.rabobank.com.au/ob/
- group: docs
  title: ''
  type: Documentation
  url: https://www.rabobank.com.au/support/open-banking
- group: operate
  title: ''
  type: Support
  url: https://www.rabobank.com.au/support/faqs/open-banking
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.rabobank.com.au/termsandconditions
- group: company
  title: ''
  type: LinkedIn
  url: https://au.linkedin.com/company/rabobankaustralia
created: '2026-07-20'
description: Rabobank Australia is the Australian arm of Rabobank Group, the Netherlands-headquartered cooperative bank and one of the world's leading food and agribusiness specialist lenders. In Australia it operates as an Authorised Deposit-taking Institution (ADI), offering rural and agribusiness finance alongside consumer online savings accounts and term deposits, including SMSF products. As a member-focused, cooperatively owned institution rather than a shareholder-driven bank, its Australian retail and business deposit products fall under the Consumer Data Right (CDR / Open Banking). Rabobank therefore exposes a public, unauthenticated Product Reference Data (PRD) API that conforms to the Data Standards Body (DSB) Consumer Data Standards, while authenticated consumer data sharing follows the CDR accredited data recipient (ADR) model built on OAuth2 / OpenID Connect (FAPI).
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/rabobank-australia.png
layout: provider
modified: '2026-07-21'
name: Rabobank Australia
nav: Providers
network: true
overview: 'Rabobank Australia publishes 7 APIs on the [APIs.io](https://apis.io/) network, including Banking Account Balances API, Banking Account Direct Debits API, Banking Account Scheduled Payments API, and 4 more. Tagged areas include Financial, Banks, Open Banking, CDR, and Consumer Banking.


  Rabobank Australia''s developer surface includes authentication, API reference, documentation, support, and 18 more developer resources.'
random_paper: 16
scopes:
- name: Rabobank Australia Scopes
  scope_count: 10
  slug: rabobank-australia-scopes
  summary_line: 10 scopes
screenshot: https://raw.githubusercontent.com/api-evangelist/rabobank-australia/refs/heads/main/screenshots/rabobank-australia-2026-07-21T114745.png
security:
- kind: authentication
  name: Rabobank Australia Authentication
  slug: rabobank-australia-authentication
  summary_line: none/oauth2/openIdConnect · 2 schemes
- kind: domain-security
  name: Rabobank Australia Domain Security
  slug: rabobank-australia-domain-security
  summary_line: TLSv1.3 · DMARC
slug: rabobank-australia
tags:
- Financial
- Banks
- Open Banking
- CDR
- Consumer Banking
- Australia
- Agribusiness
- Product Reference Data
website: https://www.rabobank.com.au/
---
