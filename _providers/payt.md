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
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: true
    idempotency: documented
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 31.5
  scored_at: '2026-08-26'
agentic_access:
- acting_count: 23
  human_in_the_loop: 0
  name: Payt Agentic Access
  operation_count: 54
  slug: payt-agentic-access
  summary_line: 54 operations · 23 acting
api_count: 20
apis:
- description: Operations about administrations
  name: Payt administrations API
  slug: payt-administrations-api
- description: Operations about companies
  name: Payt companies API
  slug: payt-companies-api
- description: Operations about contacts
  name: Payt contacts API
  slug: payt-contacts-api
- description: Operations about credit_cases
  name: Payt credit_cases API
  slug: payt-credit-cases-api
- description: Operations about debtors
  name: Payt debtors API
  slug: payt-debtors-api
- description: Operations about files
  name: Payt files API
  slug: payt-files-api
- description: Operations about invoices
  name: Payt invoices API
  slug: payt-invoices-api
- description: Operations about messages
  name: Payt messages API
  slug: payt-messages-api
- description: Operations about notes
  name: Payt notes API
  slug: payt-notes-api
- description: Operations about notifications
  name: Payt notifications API
  slug: payt-notifications-api
- description: Operations about order_lines
  name: Payt order_lines API
  slug: payt-order-lines-api
- description: Operations about orders
  name: Payt orders API
  slug: payt-orders-api
- description: Operations about payment_conditions
  name: Payt payment_conditions API
  slug: payt-payment-conditions-api
- description: Operations about payment_plans
  name: Payt payment_plans API
  slug: payt-payment-plans-api
- description: Operations about payments
  name: Payt payments API
  slug: payt-payments-api
- description: Operations about psp_mandates
  name: Payt psp_mandates API
  slug: payt-psp-mandates-api
- description: Operations about psp_transactions
  name: Payt psp_transactions API
  slug: payt-psp-transactions-api
- description: Operations about sign_ups
  name: Payt sign_up API
  slug: payt-sign-up-api
- description: Operations about tasks
  name: Payt tasks API
  slug: payt-tasks-api
- description: Operations about vat_rates
  name: Payt vat_rates API
  slug: payt-vat-rates-api
artifact_total: 46
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: API Endpoints administrations API
  slug: open-payt-administrations-api
- collection_type: open
  name: API Endpoints administrations companies API
  slug: open-payt-companies-api
- collection_type: open
  name: API Endpoints administrations contacts API
  slug: open-payt-contacts-api
- collection_type: open
  name: API Endpoints administrations credit_cases API
  slug: open-payt-credit-cases-api
- collection_type: open
  name: API Endpoints administrations debtors API
  slug: open-payt-debtors-api
- collection_type: open
  name: API Endpoints administrations files API
  slug: open-payt-files-api
- collection_type: open
  name: API Endpoints administrations invoices API
  slug: open-payt-invoices-api
- collection_type: open
  name: API Endpoints administrations messages API
  slug: open-payt-messages-api
- collection_type: open
  name: API Endpoints administrations notes API
  slug: open-payt-notes-api
- collection_type: open
  name: API Endpoints administrations notifications API
  slug: open-payt-notifications-api
- collection_type: open
  name: API Endpoints administrations order_lines API
  slug: open-payt-order-lines-api
- collection_type: open
  name: API Endpoints administrations orders API
  slug: open-payt-orders-api
- collection_type: open
  name: API Endpoints administrations payment_conditions API
  slug: open-payt-payment-conditions-api
- collection_type: open
  name: API Endpoints administrations payment_plans API
  slug: open-payt-payment-plans-api
- collection_type: open
  name: API Endpoints administrations payments API
  slug: open-payt-payments-api
- collection_type: open
  name: API Endpoints administrations psp_mandates API
  slug: open-payt-psp-mandates-api
- collection_type: open
  name: API Endpoints administrations psp_transactions API
  slug: open-payt-psp-transactions-api
- collection_type: open
  name: API Endpoints administrations sign_up API
  slug: open-payt-sign-up-api
- collection_type: open
  name: API Endpoints administrations tasks API
  slug: open-payt-tasks-api
- collection_type: open
  name: API Endpoints administrations vat_rates API
  slug: open-payt-vat-rates-api
common:
- group: other
  title: ''
  type: Overlay
  url: overlays/payt-openapi-original-overlay.yaml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/payt-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/payt-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/payt-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/payt-scopes.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/payt-conventions.yml
- group: design
  title: ''
  type: Idempotency
  url: conventions/payt-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/payt-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/payt-lifecycle.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://status.paytsoftware.com
- group: operate
  title: ''
  type: Deprecation
  url: lifecycle/payt-lifecycle.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/payt-changelog.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/payt-conformance.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/payt-data-model.yml
- group: design
  title: ''
  type: Webhooks
  url: webhooks/payt-webhooks.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/payt-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/payt-llms.txt
- group: start
  title: ''
  type: Sandbox
  url: sandbox/payt-sandbox.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.paytsoftware.com
- group: docs
  title: ''
  type: Documentation
  url: https://docs.paytsoftware.com
- group: docs
  title: ''
  type: APIReference
  url: https://docs.paytsoftware.com/api-reference/administrations/get-administrations
- group: operate
  title: ''
  type: Support
  url: https://support.paytsoftware.com
- group: company
  title: ''
  type: Blog
  url: https://paytsoftware.com/blogs/
- group: commercial
  title: ''
  type: Pricing
  url: https://paytsoftware.com/pricing/
- group: start
  title: ''
  type: SignUp
  url: https://app.paytsoftware.com
- group: build
  title: ''
  type: Postman
  url: https://app.getpostman.com/run-collection/3632280-9fea4bff-cf10-4b58-ab7f-fcf38bfb7576?action=collection%2Ffork&source=rip_markdown&collection-url=entityId%3D3632280-9fea4bff-cf10-4b58-ab7f-fcf38bfb7576%26entityType%3Dcollection%26workspaceId%3D8830f8ca-b754-4c55-b91f-c082749d1809
- group: commercial
  title: ''
  type: TermsOfService
  url: https://paytsoftware.com/terms-and-conditions/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://paytsoftware.com/privacy-and-cookies/
- group: company
  title: ''
  type: Website
  url: https://www.paytsoftware.com/
created: '2026-07-17'
description: 'Payt (Payt B.V.) is a Netherlands-based accounts receivable management platform that automates invoice follow-up and payment collection while keeping personal contact with customers. It syncs invoices and debtor data from accounting and ERP systems, then runs the collections workflow: automated reminders, flexible payment plans, debt-collection cases, creditworthiness checks, electronic (UBL/Peppol) invoicing, a self-service debtor portal, and payment reconciliation. Payt exposes a REST Customer API (api.paytsoftware.com, v1) with OAuth 2.0 authorization, cursor pagination and incremental sync, a rich signed-webhook event surface, and bulk CSV/XML/JSON imports. Surfaced as a portfolio company of Partech and enriched into the API Evangelist network.'
image: https://paytsoftware.nl/wp-content/uploads/2024/06/Logo-background-white-1.png
layout: provider
mcp_servers:
- description: ''
  name: Payt MCP Server
  slug: payt-mcp-server
modified: '2026-07-20'
name: Payt
nav: Providers
network: true
overview: 'Payt publishes 20 APIs on the [APIs.io](https://apis.io/) network, including administrations API, companies API, contacts API, and 17 more. Tagged areas include Company, Applicative Saas, Accounts Receivable, Order-to-Cash, and Invoicing.


  Payt''s developer surface includes authentication, changelog, sandbox, documentation, API reference, support, engineering blog, and 23 more developer resources.'
random_paper: 5
scopes:
- name: Payt Scopes
  scope_count: 0
  slug: payt-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: developing
  composite: 50.1
  delta: 2.4
  facets:
    access_clarity: 15.8
    commercial_clarity: 15.8
    contract_governance: 30.3
    contract_quality: 54.5
    developer_ergonomics: 64.9
    discoverability: 81.5
    governance: 30.3
    operational_transparency: 47.4
  previous_composite: 47.7
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 20
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 48.4
  schema_version: 0.15.0
  scored_at: '2026-08-26'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/payt/refs/heads/main/screenshots/payt-2026-08-07T191658.png
security:
- kind: authentication
  name: Payt Authentication
  slug: payt-authentication
  summary_line: oauth2/http · 4 schemes
- kind: domain-security
  name: Payt Domain Security
  slug: payt-domain-security
  summary_line: TLSv1.2 · DNSSEC · DMARC
slug: payt
tags:
- Company
- Applicative Saas
- Accounts Receivable
- Order-to-Cash
- Invoicing
- Debt Collection
- Payments
- Fintech
- Credit Management
- Netherlands
website: https://www.paytsoftware.com/
---
