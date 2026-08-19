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
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 28.4
  scored_at: '2026-08-19'
api_count: 19
apis:
- description: The Chart of Accounts API from AppZen — 3 operation(s) for chart of accounts.
  name: AppZen Chart of Accounts API
  slug: appzen-chart-of-accounts-api
- description: The Custom Data Sets API from AppZen — 3 operation(s) for custom data sets.
  name: AppZen Custom Data Sets API
  slug: appzen-custom-data-sets-api
- description: The Documents API from AppZen — 1 operation(s) for documents.
  name: AppZen Documents API
  slug: appzen-documents-api
- description: The Entities API from AppZen — 4 operation(s) for entities.
  name: AppZen Entities API
  slug: appzen-entities-api
- description: The Externally Processed Invoices API from AppZen — 2 operation(s) for externally processed invoices.
  name: AppZen Externally Processed Invoices API
  slug: appzen-externally-processed-invoices-api
- description: The Goods Receipt API from AppZen — 2 operation(s) for goods receipt.
  name: AppZen Goods Receipt API
  slug: appzen-goods-receipt-api
- description: The Invoice Audit Results API from AppZen — 2 operation(s) for invoice audit results.
  name: AppZen Invoice Audit Results API
  slug: appzen-invoice-audit-results-api
- description: The Invoice Status Sync API from AppZen — 1 operation(s) for invoice status sync.
  name: AppZen Invoice Status Sync API
  slug: appzen-invoice-status-sync-api
- description: The Invoices API from AppZen — 3 operation(s) for invoices.
  name: AppZen Invoices API
  slug: appzen-invoices-api
- description: The Lookup Item API from AppZen — 3 operation(s) for lookup item.
  name: AppZen Lookup Item API
  slug: appzen-lookup-item-api
- description: The Lookup Table API from AppZen — 3 operation(s) for lookup table.
  name: AppZen Lookup Table API
  slug: appzen-lookup-table-api
- description: The Payment Terms API from AppZen — 4 operation(s) for payment terms.
  name: AppZen Payment Terms API
  slug: appzen-payment-terms-api
- description: The Processed Invoices API from AppZen — 1 operation(s) for processed invoices.
  name: AppZen Processed Invoices API
  slug: appzen-processed-invoices-api
- description: The Purchase Orders API from AppZen — 4 operation(s) for purchase orders.
  name: AppZen Purchase Orders API
  slug: appzen-purchase-orders-api
- description: The Suppliers API from AppZen — 4 operation(s) for suppliers.
  name: AppZen Suppliers API
  slug: appzen-suppliers-api
- description: The Tax Master API from AppZen — 3 operation(s) for tax master.
  name: AppZen Tax Master API
  slug: appzen-tax-master-api
- description: The Unit of Measures API from AppZen — 3 operation(s) for unit of measures.
  name: AppZen Unit of Measures API
  slug: appzen-unit-of-measures-api
- description: The User Groups API from AppZen — 3 operation(s) for user groups.
  name: AppZen User Groups API
  slug: appzen-user-groups-api
- description: The Vat API from AppZen — 4 operation(s) for vat.
  name: AppZen Vat API
  slug: appzen-vat-api
artifact_total: 42
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Autonomous AP APIs Chart of Accounts API
  slug: open-appzen-chart-of-accounts-api
- collection_type: open
  name: Autonomous AP APIs Chart of Accounts Custom Data Sets API
  slug: open-appzen-custom-data-sets-api
- collection_type: open
  name: Autonomous AP APIs Chart of Accounts Documents API
  slug: open-appzen-documents-api
- collection_type: open
  name: Autonomous AP APIs Chart of Accounts Entities API
  slug: open-appzen-entities-api
- collection_type: open
  name: Autonomous AP APIs Chart of Accounts Externally Processed Invoices API
  slug: open-appzen-externally-processed-invoices-api
- collection_type: open
  name: Autonomous AP APIs Chart of Accounts Goods Receipt API
  slug: open-appzen-goods-receipt-api
- collection_type: open
  name: Autonomous AP APIs Chart of Accounts Invoice Audit Results API
  slug: open-appzen-invoice-audit-results-api
- collection_type: open
  name: Autonomous AP APIs Chart of Accounts Invoice Status Sync API
  slug: open-appzen-invoice-status-sync-api
- collection_type: open
  name: Autonomous AP APIs Chart of Accounts Invoices API
  slug: open-appzen-invoices-api
- collection_type: open
  name: Autonomous AP APIs Chart of Accounts Lookup Item API
  slug: open-appzen-lookup-item-api
- collection_type: open
  name: Autonomous AP APIs Chart of Accounts Lookup Table API
  slug: open-appzen-lookup-table-api
- collection_type: open
  name: Autonomous AP APIs Chart of Accounts Payment Terms API
  slug: open-appzen-payment-terms-api
- collection_type: open
  name: Autonomous AP APIs Chart of Accounts Processed Invoices API
  slug: open-appzen-processed-invoices-api
- collection_type: open
  name: Autonomous AP APIs Chart of Accounts Purchase Orders API
  slug: open-appzen-purchase-orders-api
- collection_type: open
  name: Autonomous AP APIs Chart of Accounts Suppliers API
  slug: open-appzen-suppliers-api
- collection_type: open
  name: Autonomous AP APIs Chart of Accounts Tax Master API
  slug: open-appzen-tax-master-api
- collection_type: open
  name: Autonomous AP APIs Chart of Accounts Unit of Measures API
  slug: open-appzen-unit-of-measures-api
- collection_type: open
  name: Autonomous AP APIs Chart of Accounts User Groups API
  slug: open-appzen-user-groups-api
- collection_type: open
  name: Autonomous AP APIs Chart of Accounts Vat API
  slug: open-appzen-vat-api
common:
- group: other
  title: ''
  type: Overlay
  url: overlays/appzen-autonomous-ap-overlay.yaml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/appzen-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/appzen-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/appzen-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/appzen-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/appzen-lifecycle.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/appzen-sandbox.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/appzen-data-model.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/appzen-conformance.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/appzen-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/appzen-llms.txt
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://api-docs.appzen.com/
- group: docs
  title: ''
  type: Documentation
  url: https://support.appzen.com/hc/en-us/categories/13996913056659-AppZen-REST-API
- group: docs
  title: ''
  type: APIReference
  url: https://api-docs.appzen.com/swagger/apis.html
- group: start
  title: ''
  type: GettingStarted
  url: https://support.appzen.com/hc/en-us/articles/12682580110739-Introduction
- group: operate
  title: ''
  type: Support
  url: https://support.appzen.com/
- group: company
  title: ''
  type: Blog
  url: https://www.appzen.com/blog
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.appzen.com/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.appzen.com/privacy-policy-appzen
- group: company
  title: ''
  type: Website
  url: https://appzen.com
created: '2026-07-17'
description: AppZen is an AI platform for finance teams that automates accounts payable and expense auditing. Its Autonomous AP product ingests invoices, purchase orders, goods receipts and supporting master data, then applies AI to run validation checks, assign risk scores, and audit spend before payment. The public Autonomous AP REST API (Swagger 2.0, 54 operations) lets ERP and accounting systems such as SAP, Oracle, NetSuite, Coupa, Workday and Microsoft Dynamics push documents into AppZen and retrieve audit results. Authentication is via three API-key headers issued by AppZen Support, with US sandbox and production environments (EU coming soon).
image: https://api-docs.appzen.com/img/appzen-logo.svg
layout: provider
mcp_servers:
- description: ''
  name: appzen-mcp.yml
  slug: appzen-mcpyml
modified: '2026-07-18'
name: AppZen
nav: Providers
network: true
overview: 'AppZen publishes 19 APIs on the [APIs.io](https://apis.io/) network, including Chart of Accounts API, Custom Data Sets API, Documents API, and 16 more. Tagged areas include Company, Finance, Accounts Payable, Expense Management, and Invoice Processing.


  AppZen''s developer surface includes authentication, sandbox, documentation, API reference, getting-started guide, support, engineering blog, and 14 more developer resources.'
random_paper: 58
score:
  band: developing
  composite: 39.7
  delta: 1.1
  facets:
    access_clarity: 21.1
    commercial_clarity: 21.1
    contract_governance: 16.7
    contract_quality: 48.3
    developer_ergonomics: 66.1
    discoverability: 81.5
    governance: 16.7
    operational_transparency: 0.0
  previous_composite: 38.6
  provenance:
    conformance: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 19
    mcp: derived
    skills: derived
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/appzen/refs/heads/main/screenshots/appzen-2026-07-25T200859.png
security:
- kind: authentication
  name: Appzen Authentication
  slug: appzen-authentication
  summary_line: apiKey · 3 schemes
- kind: domain-security
  name: Appzen Domain Security
  slug: appzen-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: appzen
tags:
- Company
- Finance
- Accounts Payable
- Expense Management
- Invoice Processing
- Spend Audit
- Artificial Intelligence
- ERP Integration
website: https://appzen.com
---
