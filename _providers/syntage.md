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
  band: agent-native
  dimensions:
    agent_skills: true
    agentic_access: true
    asyncapi_events: true
    auth_clarity: true
    consent_identity: false
    error_semantics: true
    idempotency: false
    mcp_server: true
    openapi_examples: false
    rate_limit_signal: true
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.1
  score: 81.7
  scored_at: '2026-07-27'
agentic_access:
- acting_count: 45
  human_in_the_loop: 1
  name: Syntage Agentic Access
  operation_count: 176
  slug: syntage-agentic-access
  summary_line: 176 operations · 45 acting · 1 human-in-the-loop
api_count: 65
apis:
- description: The Accounts Payable Insight API from Syntage — 1 operation(s) for accounts payable insight.
  name: Syntage Accounts Payable Insight API
  slug: syntage-accounts-payable-insight-api
- description: The Accounts Receivable Insight API from Syntage — 1 operation(s) for accounts receivable insight.
  name: Syntage Accounts Receivable Insight API
  slug: syntage-accounts-receivable-insight-api
- description: Background checks provide comprehensive verification and screening data for entities. These checks gather information from various databases and sources to assess risk, verify identity, and provide in
  name: Syntage Background Checks API
  slug: syntage-background-checks-api
- description: The Balance Sheet Insight API from Syntage — 1 operation(s) for balance sheet insight.
  name: Syntage Balance Sheet Insight API
  slug: syntage-balance-sheet-insight-api
- description: The Cash Flow Insight API from Syntage — 1 operation(s) for cash flow insight.
  name: Syntage Cash Flow Insight API
  slug: syntage-cash-flow-insight-api
- description: Company Verification Reports provide verification of company details and supporting files extracted from trusted sources. Use these endpoints to retrieve reports for a specific entity, list all report
  name: Syntage Company Verification Reports API
  slug: syntage-company-verification-reports-api
- description: The Corporate Structure Insight API from Syntage — 1 operation(s) for corporate structure insight.
  name: Syntage Corporate Structure Insight API
  slug: syntage-corporate-structure-insight-api
- description: The Customer Concentration Insight API from Syntage — 1 operation(s) for customer concentration insight.
  name: Syntage Customer Concentration Insight API
  slug: syntage-customer-concentration-insight-api
- description: The Customer Network Insight API from Syntage — 1 operation(s) for customer network insight.
  name: Syntage Customer Network Insight API
  slug: syntage-customer-network-insight-api
- description: The DS MX BIL Reports API from Syntage — 2 operation(s) for ds mx bil reports.
  name: Syntage DS MX BIL Reports API
  slug: syntage-ds-mx-bil-reports-api
- description: Buró de Crédito authorizations store the consent, RFC, address, and identity data required before Syntage can request Buró de Crédito reports for an entity.
  name: Syntage DS MX Buró de Crédito Authorizations API
  slug: syntage-ds-mx-bur-de-cr-dito-authorizations-api
- description: Buró de Crédito reports contain credit bureau data generated for an entity by the `buro_de_credito_report` extractor. Reports include the selected product type, provider report ID, parsed provider res
  name: Syntage DS MX Buró de Crédito Reports API
  slug: syntage-ds-mx-bur-de-cr-dito-reports-api
- description: RPC actos are commercial registry acts associated with an RPC entidade. They can include extracted act data and file references for registry documents.
  name: Syntage DS MX RPC Actos API
  slug: syntage-ds-mx-rpc-actos-api
- description: RPC entidades are company records extracted from the Registro Publico de Comercio. They group registration profile data, related registry acts, and shareholder records found for an entity.
  name: Syntage DS MX RPC Entidades API
  slug: syntage-ds-mx-rpc-entidades-api
- description: RPC socios are shareholder or partner records found in RPC filings.
  name: Syntage DS MX RPC Socios API
  slug: syntage-ds-mx-rpc-socios-api
- description: RUG guarantees are movable collateral guarantees registered in Mexico's Registro Unico de Garantias Mobiliarias.
  name: Syntage DS MX RUG Garantias API
  slug: syntage-ds-mx-rug-garantias-api
- description: RUG operations are registry acts associated with a movable collateral guarantee. They include operation metadata, guarantee numbers, grantors, parsed boleta data, and file references when available.
  name: Syntage DS MX RUG Operaciones API
  slug: syntage-ds-mx-rug-operaciones-api
- description: The DS MX SAT Certificates API from Syntage — 2 operation(s) for ds mx sat certificates.
  name: Syntage DS MX SAT Certificates API
  slug: syntage-ds-mx-sat-certificates-api
- description: The DS MX SAT Credentials API from Syntage — 3 operation(s) for ds mx sat credentials.
  name: Syntage DS MX SAT Credentials API
  slug: syntage-ds-mx-sat-credentials-api
- description: The DS MX SAT Credit Notes API from Syntage — 5 operation(s) for ds mx sat credit notes.
  name: Syntage DS MX SAT Credit Notes API
  slug: syntage-ds-mx-sat-credit-notes-api
- description: The DS MX SAT Electronic Accounting API from Syntage — 2 operation(s) for ds mx sat electronic accounting.
  name: Syntage DS MX SAT Electronic Accounting API
  slug: syntage-ds-mx-sat-electronic-accounting-api
- description: Batch payments are derived from payment receipt CFDIs, also known as type `P` invoices. A batch payment groups one or more invoice payments into the payment transaction reported by SAT. Use batch paym
  name: Syntage DS MX SAT Invoice Batch Payments API
  slug: syntage-ds-mx-sat-invoice-batch-payments-api
- description: The DS MX SAT Invoice Line Items API from Syntage — 3 operation(s) for ds mx sat invoice line items.
  name: Syntage DS MX SAT Invoice Line Items API
  slug: syntage-ds-mx-sat-invoice-line-items-api
- description: Invoice payments are derived from payment receipt CFDIs, also known as type `P` invoices. A payment receipt records payment activity for a previously issued deferred invoice. Each payment belongs to a
  name: Syntage DS MX SAT Invoice Payments API
  slug: syntage-ds-mx-sat-invoice-payments-api
- description: Invoice relations represent CFDI relationships between invoices, such as substitutions, credit notes, or other SAT-defined relation types. Each relation includes the source invoice, related invoice wh
  name: Syntage DS MX SAT Invoice Relations API
  slug: syntage-ds-mx-sat-invoice-relations-api
- description: Invoices represent CFDI documents issued or received by an entity. Invoice records include SAT identifiers, issuer and receiver data, monetary totals, payment status, cancellation status, invoice rela
  name: Syntage DS MX SAT Invoices API
  slug: syntage-ds-mx-sat-invoices-api
- description: A tax compliance check maps the content of Opinion de Cumplimiento de Obligaciones Fiscales, an official SAT document that states whether an RFC is complying with its tax obligations. Each tax complia
  name: Syntage DS MX SAT Tax Compliance Checks API
  slug: syntage-ds-mx-sat-tax-compliance-checks-api
- description: The DS MX SAT Tax Retentions API from Syntage — 3 operation(s) for ds mx sat tax retentions.
  name: Syntage DS MX SAT Tax Retentions API
  slug: syntage-ds-mx-sat-tax-retentions-api
- description: The DS MX SAT Tax Returns API from Syntage — 4 operation(s) for ds mx sat tax returns.
  name: Syntage DS MX SAT Tax Returns API
  slug: syntage-ds-mx-sat-tax-returns-api
- description: The DS MX SAT Tax Status API from Syntage — 3 operation(s) for ds mx sat tax status.
  name: Syntage DS MX SAT Tax Status API
  slug: syntage-ds-mx-sat-tax-status-api
- description: Syntage Score calculates an internal score for a company entity from SAT annual tax return data and tax compliance data.
  name: Syntage DS Syntage Score API
  slug: syntage-ds-syntage-score-api
- description: The Employees Insight API from Syntage — 1 operation(s) for employees insight.
  name: Syntage Employees Insight API
  slug: syntage-employees-insight-api
- description: An Entity is a resource that represents a person or company. Entities can be added via Add Entity, or automatically when a credential is validated (when the status becomes "valid"). This resource cont
  name: Syntage Entities API
  slug: syntage-entities-api
- description: 'Events record meaningful changes to resources in your organization. When something changes, Syntage creates an Event resource. For example, submitting an entity''s SAT credential can create credential '
  name: Syntage Events API
  slug: syntage-events-api
- description: The Expenditures Insight API from Syntage — 1 operation(s) for expenditures insight.
  name: Syntage Expenditures Insight API
  slug: syntage-expenditures-insight-api
- description: Export invoices data in csv or xlsx format. Once you requested an export you will receive an email with a link to download the generated file
  name: Syntage Exports API
  slug: syntage-exports-api
- description: Extractions are tasks that retrieve data for an entity from a datasource. They are used to collect invoices, tax returns, tax status, tax compliance checks, RPC records, RUG guarantees, Buró de Crédit
  name: Syntage Extractions API
  slug: syntage-extractions-api
- description: Files associated to resources
  name: Syntage Files API
  slug: syntage-files-api
- description: The Financial Institutions Insight API from Syntage — 1 operation(s) for financial institutions insight.
  name: Syntage Financial Institutions Insight API
  slug: syntage-financial-institutions-insight-api
- description: The Financial Ratios Insight API from Syntage — 1 operation(s) for financial ratios insight.
  name: Syntage Financial Ratios Insight API
  slug: syntage-financial-ratios-insight-api
- description: The Government Customers Insight API from Syntage — 1 operation(s) for government customers insight.
  name: Syntage Government Customers Insight API
  slug: syntage-government-customers-insight-api
- description: The Income Statement Insight API from Syntage — 1 operation(s) for income statement insight.
  name: Syntage Income Statement Insight API
  slug: syntage-income-statement-insight-api
- description: Insight exports return supported entity insights as CSV or XLSX files.
  name: Syntage Insight Exports API
  slug: syntage-insight-exports-api
- description: The Invoicing Annual Comparison Insight API from Syntage — 1 operation(s) for invoicing annual comparison insight.
  name: Syntage Invoicing Annual Comparison Insight API
  slug: syntage-invoicing-annual-comparison-insight-api
- description: The Invoicing Blacklist Insight API from Syntage — 1 operation(s) for invoicing blacklist insight.
  name: Syntage Invoicing Blacklist Insight API
  slug: syntage-invoicing-blacklist-insight-api
- description: The Invoicing Concentration Insight API from Syntage — 1 operation(s) for invoicing concentration insight.
  name: Syntage Invoicing Concentration Insight API
  slug: syntage-invoicing-concentration-insight-api
- description: The Mexico Addresses API from Syntage — 1 operation(s) for mexico addresses.
  name: Syntage Mexico Addresses API
  slug: syntage-mexico-addresses-api
- description: The Moratory Interest Insight API from Syntage — 1 operation(s) for moratory interest insight.
  name: Syntage Moratory Interest Insight API
  slug: syntage-moratory-interest-insight-api
- description: The Products and Services Insight API from Syntage — 2 operation(s) for products and services insight.
  name: Syntage Products and Services Insight API
  slug: syntage-products-and-services-insight-api
- description: Reports group entity insights into a configurable layout. A report is rendered in the dashboard's Reports section and can be downloaded as a PDF document with the [Exports API](/api-reference/exports/
  name: Syntage Reports API
  slug: syntage-reports-api
- description: The Risks Insight API from Syntage — 1 operation(s) for risks insight.
  name: Syntage Risks Insight API
  slug: syntage-risks-insight-api
- description: The RPC Shareholders Insight API from Syntage — 1 operation(s) for rpc shareholders insight.
  name: Syntage RPC Shareholders Insight API
  slug: syntage-rpc-shareholders-insight-api
- description: The Sales Revenue Insight API from Syntage — 1 operation(s) for sales revenue insight.
  name: Syntage Sales Revenue Insight API
  slug: syntage-sales-revenue-insight-api
- description: The Scheduler Rules API from Syntage — 2 operation(s) for scheduler rules.
  name: Syntage Scheduler Rules API
  slug: syntage-scheduler-rules-api
- description: The Schedulers API from Syntage — 2 operation(s) for schedulers.
  name: Syntage Schedulers API
  slug: syntage-schedulers-api
- description: The Scores Insight API from Syntage — 4 operation(s) for scores insight.
  name: Syntage Scores Insight API
  slug: syntage-scores-insight-api
- description: Shareholders represent individuals or entities that own shares in a company. This resource provides information about shareholders, their relationships with entities, and the sources of shareholder in
  name: Syntage Shareholders API
  slug: syntage-shareholders-api
- description: The Shareholders Insight API from Syntage — 1 operation(s) for shareholders insight.
  name: Syntage Shareholders Insight API
  slug: syntage-shareholders-insight-api
- description: The Summary Insight API from Syntage — 1 operation(s) for summary insight.
  name: Syntage Summary Insight API
  slug: syntage-summary-insight-api
- description: The Tags API from Syntage — 2 operation(s) for tags.
  name: Syntage Tags API
  slug: syntage-tags-api
- description: The Trial Balance Insight API from Syntage — 1 operation(s) for trial balance insight.
  name: Syntage Trial Balance Insight API
  slug: syntage-trial-balance-insight-api
- description: The Vendor Concentration Insight API from Syntage — 1 operation(s) for vendor concentration insight.
  name: Syntage Vendor Concentration Insight API
  slug: syntage-vendor-concentration-insight-api
- description: The Vendor Network Insight API from Syntage — 1 operation(s) for vendor network insight.
  name: Syntage Vendor Network Insight API
  slug: syntage-vendor-network-insight-api
- description: Webhook endpoints tell Syntage where to deliver events for your organization. Each endpoint includes the HTTPS delivery URL, subscribed event types, enabled state, payload content type, and signing se
  name: Syntage Webhook Endpoints API
  slug: syntage-webhook-endpoints-api
- description: Webhook requests are delivery attempts from Syntage to a webhook endpoint. Use them to monitor delivery status, inspect failed deliveries, and connect an event to the endpoint that received it.
  name: Syntage Webhook Requests API
  slug: syntage-webhook-requests-api
artifact_total: 71
asyncapis:
- description: ''
  name: Syntage Webhooks
  slug: syntage-webhooks
common:
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.syntage.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.syntage.com/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.syntage.com/api-reference/introduction
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.syntage.com/using-syntage/get-started/quick-start
- group: docs
  title: ''
  type: OpenAPI
  url: openapi/syntage-openapi-original.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/syntage-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/syntage-conventions.yml
- group: operate
  title: ''
  type: RateLimits
  url: conventions/syntage-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/syntage-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/syntage-lifecycle.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://status.syntage.com/
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/syntage-changelog.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/syntage-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: https://www.syntage.com/compania/seguridad
- group: auth
  title: ''
  type: TrustCenter
  url: https://trust.syntage.com
- group: auth
  title: ''
  type: DomainSecurity
  url: security/syntage-domain-security.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/syntage-sandbox.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/syntage-data-model.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/syntage-webhooks.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/syntage-well-known.yml
- group: other
  title: ''
  type: APICatalog
  url: well-known/syntage-api-catalog.json
- group: agent
  title: ''
  type: MCPServer
  url: mcp/syntage-mcp.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/syntage-agentic-access.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/syntage-openapi-overlay.yaml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/syntage-llms.txt
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/syntage
- group: operate
  title: ''
  type: Support
  url: https://support.syntage.com/hc/es
- group: company
  title: ''
  type: Blog
  url: https://www.syntage.com/articulos-y-reportes
- group: start
  title: ''
  type: SignUp
  url: https://app.syntage.com/register
- group: start
  title: ''
  type: Login
  url: https://app.syntage.com/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.syntage.com/terminos-y-condiciones
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.syntage.com/aviso-de-privacidad
- group: company
  title: ''
  type: Website
  url: https://www.syntage.com
created: '2026-07-17'
description: Syntage is a Mexican fintech data platform that aggregates business and fiscal data from official Mexican sources (the SAT tax authority, RPC, RUG, credit bureaus / Buro de Credito, and blacklists) into a single API and dashboard. Financial institutions use it to analyze credit risk, verify CFDI invoices for factoring operations, run KYB/KYC/PLD compliance checks, and monitor taxpayer data changes in real time. Data is consumable via a REST API (JSON-LD / Hydra), an app dashboard, PDF reports, and Excel exports. Reported scale includes 300+ financial-institution clients and billions of transactions processed. ISO/IEC 27001:2022 certified.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/syntage.png
layout: provider
mcp_servers:
- description: ''
  name: syntage-mcp.yml
  slug: syntage-mcpyml
modified: '2026-07-21'
name: Syntage
nav: Providers
network: true
overview: 'Syntage publishes 65 APIs on the [APIs.io](https://apis.io/) network, including Accounts Payable Insight API, Accounts Receivable Insight API, Background Checks API, and 62 more. Tagged areas include Company, Fintech, Mexico, Credit Risk, and Financial Data.


  The Syntage catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Syntage''s developer surface includes documentation, API reference, getting-started guide, authentication, changelog, sandbox, support, and 27 more developer resources.'
random_paper: 15
score:
  band: developing
  composite: 56.0
  delta: 0.0
  facets:
    commercial_clarity: 50.0
    contract_quality: 71.8
    developer_ergonomics: 73.9
    discoverability: 75.0
    governance: 0.0
    operational_transparency: 44.7
  previous_composite: 56.0
  schema_version: 0.5
  scored_at: '2026-07-27'
  trend: flat
security:
- kind: authentication
  name: Syntage Authentication
  slug: syntage-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Syntage Domain Security
  slug: syntage-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: trust-center
  name: Syntage Trust Center
  slug: syntage-trust-center
  summary_line: ISO/IEC 27001:2022
slug: syntage
tags:
- Company
- Fintech
- Mexico
- Credit Risk
- Financial Data
- KYC
- Compliance
- Invoices
- Factoring
- SAT
website: https://www.syntage.com
---
