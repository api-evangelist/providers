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
    agentic_access: derived
    asyncapi_events: true
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: derived
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 36.7
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 104
  human_in_the_loop: 0
  name: Flowaccount Agentic Access
  operation_count: 153
  slug: flowaccount-agentic-access
  summary_line: 153 operations · 104 acting
api_count: 19
apis:
- description: The BatchImport API from FlowAccount — 10 operation(s) for batchimport.
  name: FlowAccount BatchImport API
  slug: flowaccount-batchimport-api
- description: The BillingNote API from FlowAccount — 8 operation(s) for billingnote.
  name: FlowAccount BillingNote API
  slug: flowaccount-billingnote-api
- description: The CashInvoice API from FlowAccount — 8 operation(s) for cashinvoice.
  name: FlowAccount CashInvoice API
  slug: flowaccount-cashinvoice-api
- description: The CompanyCurrency API from FlowAccount — 2 operation(s) for companycurrency.
  name: FlowAccount CompanyCurrency API
  slug: flowaccount-companycurrency-api
- description: The Contact API from FlowAccount — 4 operation(s) for contact.
  name: FlowAccount Contact API
  slug: flowaccount-contact-api
- description: The CreditNote API from FlowAccount — 9 operation(s) for creditnote.
  name: FlowAccount CreditNote API
  slug: flowaccount-creditnote-api
- description: The DebitNote API from FlowAccount — 9 operation(s) for debitnote.
  name: FlowAccount DebitNote API
  slug: flowaccount-debitnote-api
- description: The Employee API from FlowAccount — 3 operation(s) for employee.
  name: FlowAccount Employee API
  slug: flowaccount-employee-api
- description: The Expense API from FlowAccount — 12 operation(s) for expense.
  name: FlowAccount Expense API
  slug: flowaccount-expense-api
- description: The ProductCategory API from FlowAccount — 2 operation(s) for productcategory.
  name: FlowAccount ProductCategory API
  slug: flowaccount-productcategory-api
- description: The ProductInventory API from FlowAccount — 2 operation(s) for productinventory.
  name: FlowAccount ProductInventory API
  slug: flowaccount-productinventory-api
- description: The Products API from FlowAccount — 3 operation(s) for products.
  name: FlowAccount Products API
  slug: flowaccount-products-api
- description: The ProductUnit API from FlowAccount — 2 operation(s) for productunit.
  name: FlowAccount ProductUnit API
  slug: flowaccount-productunit-api
- description: The Purchase API from FlowAccount — 8 operation(s) for purchase.
  name: FlowAccount Purchase API
  slug: flowaccount-purchase-api
- description: The PurchaseOrder API from FlowAccount — 8 operation(s) for purchaseorder.
  name: FlowAccount PurchaseOrder API
  slug: flowaccount-purchaseorder-api
- description: The Quotation API from FlowAccount — 10 operation(s) for quotation.
  name: FlowAccount Quotation API
  slug: flowaccount-quotation-api
- description: The Receipt API from FlowAccount — 10 operation(s) for receipt.
  name: FlowAccount Receipt API
  slug: flowaccount-receipt-api
- description: The ReceivableInvoice API from FlowAccount — 8 operation(s) for receivableinvoice.
  name: FlowAccount ReceivableInvoice API
  slug: flowaccount-receivableinvoice-api
- description: The TaxInvoice API from FlowAccount — 9 operation(s) for taxinvoice.
  name: FlowAccount TaxInvoice API
  slug: flowaccount-taxinvoice-api
artifact_total: 26
asyncapis:
- description: ''
  name: Flowaccount Webhooks
  slug: flowaccount-webhooks
common:
- group: company
  title: ''
  type: Website
  url: https://flowaccount.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developers.flowaccount.com/
- group: docs
  title: ''
  type: Documentation
  url: https://developers.flowaccount.com/
- group: start
  title: ''
  type: GettingStarted
  url: https://form.flowaccount.com/request-openapi
- group: start
  title: ''
  type: SignUp
  url: https://auth.flowaccount.com/th/Account/Register
- group: start
  title: ''
  type: Login
  url: https://auth.flowaccount.com
- group: commercial
  title: ''
  type: Pricing
  url: https://flowaccount.com/pricing
- group: company
  title: ''
  type: Blog
  url: https://flowaccount.com/blog/
- group: operate
  title: ''
  type: Support
  url: https://flowaccount.com/help-center
- group: commercial
  title: ''
  type: TermsOfService
  url: https://flowaccount.com/term-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://flowaccount.com/privacy-statement
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/flowaccount
- group: operate
  title: ''
  type: StatusPage
  url: https://flowaccount.statuspage.io
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/flowaccount-lifecycle.yml
- group: operate
  title: ''
  type: ChangeLog
  url: https://developers.flowaccount.com/
- group: build
  title: ''
  type: Packages
  url: packages/flowaccount-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/flowaccount-packages.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/flowaccount-mcp.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/flowaccount-agentic-access.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/flowaccount-authentication.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/flowaccount-llms.txt
- group: auth
  title: ''
  type: DomainSecurity
  url: security/flowaccount-domain-security.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/flowaccount-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: security/flowaccount-vulnerability-disclosure.yml
created: '2026-07-17'
description: FlowAccount is a Thai cloud accounting platform serving 130,000+ SMEs, 17,000+ accountants and admins, and 5,900+ accounting firms. Its products cover online accounting (quotations, invoices, tax invoices, receipts, expenses), MobilePOS point-of-sale, Payroll with bank integration, and AutoKey document capture. The FlowAccount Open API is an OAuth 2.0 (client-credentials) REST API of 153 operations across sandbox and production environments, letting integrations create and manage sales/purchase documents, contacts, and products, receive webhook event callbacks, and sync POS transactions. First-party SDKs are published for JavaScript/TypeScript, Java, PHP, .NET, and Go.
image: https://flowaccountcdn.com/favicon/landing/FlowAccount.png
layout: provider
mcp_servers:
- description: ''
  name: flowaccount-mcp.yml
  slug: flowaccount-mcpyml
modified: '2026-07-19'
name: FlowAccount
nav: Providers
network: true
overview: 'FlowAccount publishes 19 APIs on the [APIs.io](https://apis.io/) network, including BatchImport API, BillingNote API, CashInvoice API, and 16 more. Tagged areas include Company, Accounting, Invoicing, Payroll, and Point of Sale.


  The FlowAccount catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  FlowAccount''s developer surface includes documentation, getting-started guide, signup flow, pricing, engineering blog, support, changelog, and 18 more developer resources.'
random_paper: 55
scopes:
- name: Flowaccount Scopes
  scope_count: 1
  slug: flowaccount-scopes
  summary_line: 1 scope
score:
  band: developing
  composite: 51.1
  delta: -1.7
  facets:
    commercial_clarity: 44.7
    contract_quality: 56.6
    developer_ergonomics: 56.0
    discoverability: 92.6
    governance: 11.5
    operational_transparency: 47.4
  previous_composite: 52.8
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 19
    mcp: derived
    skills: derived
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/flowaccount/refs/heads/main/screenshots/flowaccount-2026-07-25T214832.png
security:
- kind: authentication
  name: Flowaccount Authentication
  slug: flowaccount-authentication
  summary_line: oauth2/http · 2 schemes
- kind: domain-security
  name: Flowaccount Domain Security
  slug: flowaccount-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Flowaccount Vulnerability Disclosure
  slug: flowaccount-vulnerability-disclosure
  summary_line: Hackerone · contact published
slug: flowaccount
tags:
- Company
- Accounting
- Invoicing
- Payroll
- Point of Sale
- SME
- Finance
- Tax
- Thailand
- Bookkeeping
website: https://flowaccount.com
---
