---
access_model:
  confidence: high
  gated: none
  gated_source:
  - onboarding
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  - scopes
  - security
  - sandbox
  trial: false
  try_now: true
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: true
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: paginated
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 28.3
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 104
  human_in_the_loop: 0
  name: Flowaccount Agentic Access
  operation_count: 153
  slug: flowaccount-agentic-access
  summary_line: 153 operations · 104 acting
api_count: 1
apis:
- baseURL: https://openapi.flowaccount.com/v3-alpha
  baseurl_source: declared
  description: The BillingNote API from FlowAccount — 8 operation(s) for billingnote.
  name: FlowAccount BillingNote API
  slug: flowaccount-billingnote-api
- baseURL: https://openapi.flowaccount.com/v3-alpha
  baseurl_source: declared
  description: The CashInvoice API from FlowAccount — 8 operation(s) for cashinvoice.
  name: FlowAccount CashInvoice API
  slug: flowaccount-cashinvoice-api
- baseURL: https://openapi.flowaccount.com/v3-alpha
  baseurl_source: declared
  description: The CompanyCurrency API from FlowAccount — 2 operation(s) for companycurrency.
  name: FlowAccount CompanyCurrency API
  slug: flowaccount-companycurrency-api
- baseURL: https://openapi.flowaccount.com/v3-alpha
  baseurl_source: declared
  description: The Contact API from FlowAccount — 4 operation(s) for contact.
  name: FlowAccount Contact API
  slug: flowaccount-contact-api
- baseURL: https://openapi.flowaccount.com/v3-alpha
  baseurl_source: declared
  description: The DebitNote API from FlowAccount — 9 operation(s) for debitnote.
  name: FlowAccount DebitNote API
  slug: flowaccount-debitnote-api
- baseURL: https://openapi.flowaccount.com/v3-alpha
  baseurl_source: declared
  description: The Employee API from FlowAccount — 3 operation(s) for employee.
  name: FlowAccount Employee API
  slug: flowaccount-employee-api
- baseURL: https://openapi.flowaccount.com/v3-alpha
  baseurl_source: declared
  description: The Expense API from FlowAccount — 12 operation(s) for expense.
  name: FlowAccount Expense API
  slug: flowaccount-expense-api
- baseURL: https://openapi.flowaccount.com/v3-alpha
  baseurl_source: declared
  description: The Products API from FlowAccount — 3 operation(s) for products.
  name: FlowAccount Products API
  slug: flowaccount-products-api
- baseURL: https://openapi.flowaccount.com/v3-alpha
  baseurl_source: declared
  description: The ProductUnit API from FlowAccount — 2 operation(s) for productunit.
  name: FlowAccount ProductUnit API
  slug: flowaccount-productunit-api
- baseURL: https://openapi.flowaccount.com/v3-alpha
  baseurl_source: declared
  description: The Purchase API from FlowAccount — 8 operation(s) for purchase.
  name: FlowAccount Purchase API
  slug: flowaccount-purchase-api
- baseURL: https://openapi.flowaccount.com/v3-alpha
  baseurl_source: declared
  description: The Quotation API from FlowAccount — 10 operation(s) for quotation.
  name: FlowAccount Quotation API
  slug: flowaccount-quotation-api
- baseURL: https://openapi.flowaccount.com/v3-alpha
  baseurl_source: declared
  description: The Receipt API from FlowAccount — 10 operation(s) for receipt.
  name: FlowAccount Receipt API
  slug: flowaccount-receipt-api
- baseURL: https://openapi.flowaccount.com/v3-alpha
  baseurl_source: declared
  description: The ReceivableInvoice API from FlowAccount — 8 operation(s) for receivableinvoice.
  name: FlowAccount ReceivableInvoice API
  slug: flowaccount-receivableinvoice-api
- baseURL: https://openapi.flowaccount.com/v3-alpha
  baseurl_source: declared
  description: The TaxInvoice API from FlowAccount — 9 operation(s) for taxinvoice.
  name: FlowAccount TaxInvoice API
  slug: flowaccount-taxinvoice-api
- baseURL: https://openapi.flowaccount.com/v3-alpha
  baseurl_source: declared
  description: The Batch Import API from FlowAccount — 10 operation(s) for batch import.
  name: FlowAccount Batch Import API
  slug: flowaccount-batch-import-api
- baseURL: https://openapi.flowaccount.com/v3-alpha
  baseurl_source: declared
  description: The Credit Note API from FlowAccount — 9 operation(s) for credit note.
  name: FlowAccount Credit Note API
  slug: flowaccount-credit-note-api
- baseURL: https://openapi.flowaccount.com/v3-alpha
  baseurl_source: declared
  description: The Product Category API from FlowAccount — 2 operation(s) for product category.
  name: FlowAccount Product Category API
  slug: flowaccount-product-category-api
- baseURL: https://openapi.flowaccount.com/v3-alpha
  baseurl_source: declared
  description: The Product Inventory API from FlowAccount — 2 operation(s) for product inventory.
  name: FlowAccount Product Inventory API
  slug: flowaccount-product-inventory-api
- baseURL: https://openapi.flowaccount.com/v3-alpha
  baseurl_source: declared
  description: The Purchase Order API from FlowAccount — 8 operation(s) for purchase order.
  name: FlowAccount Purchase Order API
  slug: flowaccount-purchase-order-api
artifact_total: 50
asyncapis:
- description: ''
  name: Flowaccount Webhooks
  slug: flowaccount-webhooks
collections:
- collection_type: open
  name: FlowAccount Open BatchImport API
  slug: open-flowaccount-batchimport-api
- collection_type: open
  name: FlowAccount Open BatchImport BillingNote API
  slug: open-flowaccount-billingnote-api
- collection_type: open
  name: FlowAccount Open BatchImport CashInvoice API
  slug: open-flowaccount-cashinvoice-api
- collection_type: open
  name: FlowAccount Open BatchImport CompanyCurrency API
  slug: open-flowaccount-companycurrency-api
- collection_type: open
  name: FlowAccount Open BatchImport Contact API
  slug: open-flowaccount-contact-api
- collection_type: open
  name: FlowAccount Open BatchImport CreditNote API
  slug: open-flowaccount-creditnote-api
- collection_type: open
  name: FlowAccount Open BatchImport DebitNote API
  slug: open-flowaccount-debitnote-api
- collection_type: open
  name: FlowAccount Open BatchImport Employee API
  slug: open-flowaccount-employee-api
- collection_type: open
  name: FlowAccount Open BatchImport Expense API
  slug: open-flowaccount-expense-api
- collection_type: open
  name: FlowAccount Open BatchImport ProductCategory API
  slug: open-flowaccount-productcategory-api
- collection_type: open
  name: FlowAccount Open BatchImport ProductInventory API
  slug: open-flowaccount-productinventory-api
- collection_type: open
  name: FlowAccount Open BatchImport Products API
  slug: open-flowaccount-products-api
- collection_type: open
  name: FlowAccount Open BatchImport ProductUnit API
  slug: open-flowaccount-productunit-api
- collection_type: open
  name: FlowAccount Open BatchImport Purchase API
  slug: open-flowaccount-purchase-api
- collection_type: open
  name: FlowAccount Open BatchImport PurchaseOrder API
  slug: open-flowaccount-purchaseorder-api
- collection_type: open
  name: FlowAccount Open BatchImport Quotation API
  slug: open-flowaccount-quotation-api
- collection_type: open
  name: FlowAccount Open BatchImport Receipt API
  slug: open-flowaccount-receipt-api
- collection_type: open
  name: FlowAccount Open BatchImport ReceivableInvoice API
  slug: open-flowaccount-receivableinvoice-api
- collection_type: open
  name: FlowAccount Open BatchImport TaxInvoice API
  slug: open-flowaccount-taxinvoice-api
common:
- group: commercial
  href: https://artifacts.apis.io/flowaccount/plans/flowaccount-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/flowaccount-plans-pricing.yml
- group: company
  title: ''
  type: BlogRSS
  url: https://flowaccount.com/blog/feed/
- group: other
  href: https://artifacts.apis.io/flowaccount/capabilities/flowaccount-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/flowaccount-capability-edges.yml
- group: other
  href: https://artifacts.apis.io/flowaccount/overlays/flowaccount-openapi-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/flowaccount-openapi-overlay.yaml
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
  href: https://artifacts.apis.io/flowaccount/lifecycle/flowaccount-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/flowaccount-lifecycle.yml
- group: operate
  title: ''
  type: ChangeLog
  url: https://developers.flowaccount.com/
- group: build
  href: https://artifacts.apis.io/flowaccount/packages/flowaccount-packages.yml
  title: ''
  type: Packages
  url: packages/flowaccount-packages.yml
- group: build
  href: https://artifacts.apis.io/flowaccount/packages/flowaccount-packages.yml
  title: ''
  type: SDKs
  url: packages/flowaccount-packages.yml
- group: agent
  href: https://artifacts.apis.io/flowaccount/mcp/flowaccount-mcp.yml
  title: ''
  type: X-MCPServerCandidate
  url: mcp/flowaccount-mcp.yml
- group: agent
  href: https://artifacts.apis.io/flowaccount/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  href: https://artifacts.apis.io/flowaccount/agentic-access/flowaccount-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/flowaccount-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/flowaccount/authentication/flowaccount-authentication.yml
  title: ''
  type: Authentication
  url: authentication/flowaccount-authentication.yml
- group: agent
  href: https://artifacts.apis.io/flowaccount/llms/flowaccount-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/flowaccount-llms.txt
- group: auth
  href: https://artifacts.apis.io/flowaccount/security/flowaccount-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/flowaccount-domain-security.yml
- group: auth
  href: https://artifacts.apis.io/flowaccount/security/flowaccount-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/flowaccount-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/flowaccount/security/flowaccount-vulnerability-disclosure.yml
  title: ''
  type: Security
  url: security/flowaccount-vulnerability-disclosure.yml
created: '2026-07-17'
description: FlowAccount is a Thai cloud accounting platform serving 130,000+ SMEs, 17,000+ accountants and admins, and 5,900+ accounting firms. Its products cover online accounting (quotations, invoices, tax invoices, receipts, expenses), MobilePOS point-of-sale, Payroll with bank integration, and AutoKey document capture. The FlowAccount Open API is an OAuth 2.0 (client-credentials) REST API of 153 operations across sandbox and production environments, letting integrations create and manage sales/purchase documents, contacts, and products, receive webhook event callbacks, and sync POS transactions. First-party SDKs are published for JavaScript/TypeScript, Java, PHP, .NET, and Go.
finops:
- has_sources: true
  method: derived
  name: Flowaccount Finops
  primary_unit: แพ็กเกจ
  service_category: ''
  slug: flowaccount-finops
  template: false
image: https://flowaccountcdn.com/favicon/landing/FlowAccount.png
layout: provider
modified: '2026-10-06'
name: FlowAccount
nav: Providers
network: true
overview: 'FlowAccount publishes 19 API contracts indexed on the [APIs.io](https://apis.io/) network, including BillingNote API, CashInvoice API, CompanyCurrency API, and 16 more. Tagged areas include Company, Accounting, Invoicing, Payroll, and Point-of-Sale.


  The FlowAccount catalog on APIs.io includes 1 event-driven AsyncAPI specification and 1 Spectral governance ruleset.


  FlowAccount''s developer surface includes documentation, getting-started guide, signup flow, pricing, engineering blog, support, changelog, and 22 more developer resources.'
plans:
- name: Flowaccount Plans Pricing
  plan_count: 6
  slug: flowaccount-plans-pricing
random_paper: 13
rules:
- authorship: generated
  effective_rule_count: 89
  extends:
  - spectral:oas
  name: FlowAccount API Rules
  rule_count: 48
  severity_counts:
    error: 39
    hint: 0
    info: 2
    warn: 7
  slug: flowaccount-rules
scopes:
- name: Flowaccount Scopes
  scope_count: 1
  slug: flowaccount-scopes
  summary_line: 1 scope
score:
  band: exemplar
  composite: 68.8
  coverage:
    artifact_dirs: 29
    catalog_earned: 56.5
    catalog_earned_first_party: 12.0
    catalog_gap: 58.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 84.2
    contract_governance: 18.2
    contract_quality: 54.0
    developer_ergonomics: 73.2
    discoverability: 73.2
    operational_transparency: 52.6
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - thailand
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - southeast-asia
  previous_composite: 68.8
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
  regulatory:
    applies: true
    matched_via: tags
    regime: Employment & Payroll
    regime_id: employment_payroll
    score: 40.2
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 50.0
screenshot: https://apis.io/screenshots/flowaccount/flowaccount-2026-07-25T214832.png
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
skill_count: 3
skills:
- name: Record a cash sale and receive payment
  slug: flowaccount-cash-sale-and-payment
- name: Create a contact and issue a quotation
  slug: flowaccount-create-contact-and-quote
- name: Manage products and inventory
  slug: flowaccount-manage-products
slug: flowaccount
tags:
- Company
- Accounting
- Invoicing
- Payroll
- Point-of-Sale
- Small Business
- Finance
- Tax
- Thailand
- Bookkeeping
website: https://flowaccount.com
---
