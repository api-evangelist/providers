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
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    asyncapi_events: false
    auth_clarity: true
    consent_identity: true
    dry_run_mode: false
    error_semantics: verified
    idempotency: false
    mcp_server: derived
    openapi_examples: partial
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.2
  score: 45.7
  scored_at: '2026-07-28'
api_count: 22
apis:
- description: Card account associated to one of Yokoy's card programs. Only active card accounts are allowed to order new cards.
  name: Yokoy Card account API
  slug: yokoy-card-account-api
- description: Company card entity in Yokoy. Company cards can be Yokoy Pay cards or external cards.
  name: Yokoy Company card API
  slug: yokoy-company-card-api
- description: Cost objects (also called cost centers) is a hierarchical construct to which costs that occur within a company can be assigned. Cost objects are created at legal entity level and can be used for expen
  name: Yokoy Cost center API
  slug: yokoy-cost-center-api
- description: Daily CAMT statement files associated with a card account. Statements provide a daily summary of transactions in a standardized banking format.
  name: Yokoy Daily statement API
  slug: yokoy-daily-statement-api
- description: An expense is a cost incurred during the performance of a business activity. Employees can create reimbursable or non-reimbursable expenses. The Expense endpoints let you query all expense types manag
  name: Yokoy Expense API
  slug: yokoy-expense-api
- description: Categories for expenses (also called booking accounts). These categories only apply to expenses and trips. For invoices, use supplier invoice categories.
  name: Yokoy Expense category API
  slug: yokoy-expense-category-api
- description: Invoices that are not present in Yokoy, but that are used for matching in purchase orders and goods receipts.
  name: Yokoy External invoice API
  slug: yokoy-external-invoice-api
- description: 'Finance export mechanism in Yokoy. The Yokoy API exposes three different endpoints for the management of finance exports: 1. `/export-tasks` to trigger an export (separate endpoints for the expense an'
  name: Yokoy Finance export API
  slug: yokoy-finance-export-api
- description: Extend the offered and Yokoy-managed foreign exchange rates (Open Exchange Rates, CNB, NPB and NBS national bank rates) with your own customer-specific FX rates. The created FX rate sources are equiva
  name: Yokoy FX rates API
  slug: yokoy-fx-rates-api
- description: Goods receipt are usually provided by suppliers when the goods of an order are delivered. Yokoy uses goods receipts to perform three-way matching (controlling invoice spending by checking quantities i
  name: Yokoy Goods receipt API
  slug: yokoy-goods-receipt-api
- description: In the Yokoy API, invoices can only be created or retrieved. You can only update custom information via API. To update other attributes or delete the invoice, use the Yokoy web app.
  name: Yokoy Invoice API
  slug: yokoy-invoice-api
- description: Categories for invoices (equivalent to GL accounts in financial systems). These categories only apply to invoices. For expenses and trips, use expense categories.
  name: Yokoy Invoice category API
  slug: yokoy-invoice-category-api
- description: Payment terms determine the expectation of payment agreed between the company and the supplier. By default, all payment terms can be used with any supplier of the legal entity. However, you can restri
  name: Yokoy Invoice payment terms API
  slug: yokoy-invoice-payment-terms-api
- description: Legal entity or company. An organization can have multiple legal entities.
  name: Yokoy Legal entity API
  slug: yokoy-legal-entity-api
- description: 'An employee policy determines the settings made available to a group of employees. A policy determines: - **categories**: the categories available to users to select. - **tags**: tags applicable to th'
  name: Yokoy Policy API
  slug: yokoy-policy-api
- description: Purchase orders are legal orders that companies send to their suppliers to buy items, services, products. Yokoy uses purchase orders to perform two-way and three-way matching (matching invoice line it
  name: Yokoy Purchase order API
  slug: yokoy-purchase-order-api
- description: 'Companies that supply your company with goods, services, items. The Supplier entity contains information on the name, address, and bank accounts of the supplier. Suppliers can be set up for different '
  name: Yokoy Supplier API
  slug: yokoy-supplier-api
- description: Tag is a custom dimension that can be added to each category that help map additional information to that spend and use it at multiple levels, such as analytics or for accounting purposes. Tags are of
  name: Yokoy Tag API
  slug: yokoy-tag-api
- description: Tax rates. Tax rates apply to expenses, trips, and invoices. In Yokoy, you can consult them in **Admin > VAT / Tax rates**. For invoices, you can set up advanced tax components to adjust to complex ta
  name: Yokoy Tax rates API
  slug: yokoy-tax-rates-api
- description: A transaction is a cleared payment that is made using a credit, debit, or prepaid card. The card issuer can be either Yokoy or a third party that has been integrated with Yokoy.
  name: Yokoy Transaction API
  slug: yokoy-transaction-api
- description: A trip is a collection of various types of expenses that occurred on a business trip over a period of time.
  name: Yokoy Trip API
  slug: yokoy-trip-api
- description: Users in Yokoy reflect the fundamental roles of submitter, approver, and finance user. Mandatory user information depends on the specific organization requirements and Yokoy features enabled. Email ad
  name: Yokoy User API
  slug: yokoy-user-api
artifact_total: 28
common:
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.yokoy.ai/
- group: docs
  title: ''
  type: Documentation
  url: https://developer.yokoy.ai/docs/overview
- group: docs
  title: ''
  type: APIReference
  url: https://developer.yokoy.ai/api-reference/
- group: start
  title: ''
  type: GettingStarted
  url: https://developer.yokoy.ai/docs/overview/getting-started
- group: operate
  title: ''
  type: Support
  url: https://help.yokoy.ai/
- group: operate
  title: ''
  type: ChangeLog
  url: https://developer.yokoy.ai/docs/release-notes
- group: operate
  title: ''
  type: StatusPage
  url: https://status.perk.com/
- group: operate
  title: ''
  type: Deprecation
  url: lifecycle/yokoy-lifecycle.yml
- group: auth
  title: ''
  type: Compliance
  url: https://www.perk.com/security/
- group: auth
  title: ''
  type: TrustCenter
  url: https://trustcenter.perk.com/
- group: auth
  title: ''
  type: Security
  url: https://yokoy.io/.well-known/security.txt
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/yokoy-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/yokoy-security.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/yokoy-well-known.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/yokoy-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/yokoy-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/yokoy-conventions.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/yokoy-lifecycle.yml
- group: build
  title: ''
  type: Packages
  url: packages/yokoy-packages.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/yokoy-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/yokoy-llms.txt
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: company
  title: ''
  type: Website
  url: https://yokoy.io/
created: '2026-07-17'
description: Yokoy (now part of Perk / TravelPerk) is an AI-powered spend-management platform for expenses, supplier invoices and corporate cards. Its public REST API (OpenAPI 3.0, 105 operations) imports master and configuration data into Yokoy and exports financial data — expenses, trips, invoices, transactions, journal entries and FX rates — to third-party ERP and accounting systems. Authentication uses the OAuth2 client-credentials flow; every request is scoped to an organization ID and most resources to a legal entity (company). The API spans expenses, invoices, trips, transactions, company cards and card accounts, cost centers, categories, tax rates, suppliers, users, policies, tags and finance-export tasks.
image: https://yokoy.io/favicon.ico
layout: provider
mcp_servers:
- description: ''
  name: yokoy-mcp.yml
  slug: yokoy-mcpyml
modified: '2026-07-21'
name: Yokoy
nav: Providers
network: true
overview: 'Yokoy publishes 22 APIs on the [APIs.io](https://apis.io/) network, including Card account API, Company card API, Cost center API, and 19 more. Tagged areas include Company, Spend Management, Expense Management, Invoice Management, and Finance Automation.


  Yokoy''s developer surface includes documentation, API reference, getting-started guide, support, changelog, authentication, and 17 more developer resources.'
random_paper: 79
scopes:
- name: Yokoy Scopes
  scope_count: 0
  slug: yokoy-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: developing
  composite: 46.5
  delta: -0.7
  facets:
    commercial_clarity: 15.8
    contract_quality: 57.1
    developer_ergonomics: 53.8
    discoverability: 92.6
    governance: 20.8
    operational_transparency: 50.0
  previous_composite: 47.2
  provenance:
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 22
    mcp: derived
    skills: derived
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
security:
- kind: authentication
  name: Yokoy Authentication
  slug: yokoy-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Yokoy Domain Security
  slug: yokoy-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: vulnerability-disclosure
  name: Yokoy Vulnerability Disclosure
  slug: yokoy-vulnerability-disclosure
  summary_line: Intigriti · security.txt · contact published
- kind: trust-center
  name: Yokoy Trust Center
  slug: yokoy-trust-center
  summary_line: ISO 27001, SOC 2, Cyber Essentials, GDPR
slug: yokoy
tags:
- Company
- Spend Management
- Expense Management
- Invoice Management
- Finance Automation
- Corporate Cards
- Fintech
- SaaS
website: https://yokoy.io/
---
