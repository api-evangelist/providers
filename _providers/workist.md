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
    agentic_access: derived
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
  score: 30.6
  scored_at: '2026-08-24'
agentic_access:
- acting_count: 47
  human_in_the_loop: 0
  name: Workist Agentic Access
  operation_count: 63
  slug: workist-agentic-access
  summary_line: 63 operations · 47 acting
api_count: 8
apis:
- description: The Delivery Notes API from Workist — 5 operation(s) for delivery notes.
  name: Workist Delivery Notes API
  slug: workist-delivery-notes-api
- description: The Invoices API from Workist — 5 operation(s) for invoices.
  name: Workist Invoices API
  slug: workist-invoices-api
- description: The List Of Services API from Workist — 6 operation(s) for list of services.
  name: Workist List Of Services API
  slug: workist-list-of-services-api
- description: The Master Data API from Workist — 12 operation(s) for master data.
  name: Workist Master Data API
  slug: workist-master-data-api
- description: The Order Confirmations API from Workist — 5 operation(s) for order confirmations.
  name: Workist Order Confirmations API
  slug: workist-order-confirmations-api
- description: The Orders API from Workist — 5 operation(s) for orders.
  name: Workist Orders API
  slug: workist-orders-api
- description: The Property Bills API from Workist — 5 operation(s) for property bills.
  name: Workist Property Bills API
  slug: workist-property-bills-api
- description: The Rfq API from Workist — 5 operation(s) for rfq.
  name: Workist Rfq API
  slug: workist-rfq-api
artifact_total: 21
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Workist Integrations & Developer Delivery Notes API
  slug: open-workist-delivery-notes-api
- collection_type: open
  name: Workist Integrations & Developer Delivery Notes Invoices API
  slug: open-workist-invoices-api
- collection_type: open
  name: Workist Integrations & Developer Delivery Notes List Of Services API
  slug: open-workist-list-of-services-api
- collection_type: open
  name: Workist Integrations & Developer Delivery Notes Master Data API
  slug: open-workist-master-data-api
- collection_type: open
  name: Workist Integrations & Developer Delivery Notes Order Confirmations API
  slug: open-workist-order-confirmations-api
- collection_type: open
  name: Workist Integrations & Developer Delivery Notes Orders API
  slug: open-workist-orders-api
- collection_type: open
  name: Workist Integrations & Developer Delivery Notes Property Bills API
  slug: open-workist-property-bills-api
- collection_type: open
  name: Workist Integrations & Developer Delivery Notes Rfq API
  slug: open-workist-rfq-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/workist-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/workist-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/workist-authentication.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/workist-llms.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/workist-well-known.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/workist-mcp.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/workist-integrations-overlay.yaml
- group: design
  title: ''
  type: Conformance
  url: conformance/workist-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: https://www.workist.com/en
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/workist-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/workist-lifecycle.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/workist-conventions.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/workist-data-model.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: company
  title: ''
  type: Website
  url: https://www.workist.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.workist.com/en/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.workist.com/en/
- group: docs
  title: ''
  type: APIReference
  url: https://api.workist.com/v1/swagger/
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.workist.com/en/docs/api-documentation/quickstart/
- group: start
  title: ''
  type: Login
  url: https://wb.workist.com/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.workist.com/en/pricing
- group: company
  title: ''
  type: Blog
  url: https://www.workist.com/en/blog
- group: operate
  title: ''
  type: Support
  url: https://docs.workist.com/en/docs/faq/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/workist
- group: operate
  title: ''
  type: StatusPage
  url: https://status.workist.com
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.workist.com/en/terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.workist.com/en/privacy-policy
created: '2026-07-17'
description: Workist is a Berlin-based AI document-automation company whose WorKI system automates B2B order entry and inquiry handling — extracting data from emails and PDFs, validating it against ERP master data, and writing structured transactions back into 20+ ERP systems such as SAP S/4HANA, Microsoft Dynamics 365, Oracle NetSuite, and Sage. The Workist Integrations & Developer API is a bearer-token REST API for uploading documents (orders, invoices, delivery notes, order confirmations, RFQs, property bills, lists of services), retrieving processed results, and importing ERP master data in batches.
image: https://docs.workist.com/img/workist_icon.svg
layout: provider
mcp_servers:
- description: ''
  name: Workist MCP Server
  slug: workist-mcp-server
modified: '2026-07-21'
name: Workist
nav: Providers
network: true
overview: 'Workist publishes 8 APIs on the [APIs.io](https://apis.io/) network, including Delivery Notes API, Invoices API, List Of Services API, and 5 more. Tagged areas include Documents, Document Processing, Artificial Intelligence, Automation, and Order.


  Workist''s developer surface includes authentication, documentation, API reference, getting-started guide, pricing, engineering blog, support, and 20 more developer resources.'
random_paper: 10
score:
  band: developing
  composite: 49.2
  delta: 0.0
  facets:
    access_clarity: 46.1
    commercial_clarity: 46.1
    contract_governance: 30.3
    contract_quality: 55.9
    developer_ergonomics: 58.9
    discoverability: 81.5
    governance: 30.3
    operational_transparency: 18.4
  previous_composite: 49.2
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 8
    mcp: derived
    skills: derived
  schema_version: 0.12.1
  scored_at: '2026-08-24'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/workist/refs/heads/main/screenshots/workist-2026-08-17T082941.png
security:
- kind: authentication
  name: Workist Authentication
  slug: workist-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Workist Domain Security
  slug: workist-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: workist
tags:
- Documents
- Document Processing
- Artificial Intelligence
- Automation
- Order
- Invoices
- ERP
- B2B
- Master Data
website: https://www.workist.com
---
