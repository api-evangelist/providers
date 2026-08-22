---
access_model:
  confidence: high
  label: Freemium (free trial) · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  trial: true
  try_now: true
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 29.1
  scored_at: '2026-08-19'
agentic_access:
- acting_count: 21
  human_in_the_loop: 0
  name: Weclapp Agentic Access
  operation_count: 42
  slug: weclapp-agentic-access
  summary_line: 42 operations · 21 acting
api_count: 7
apis:
- description: Articles / products in the catalog.
  name: weclapp Article API
  slug: weclapp-article-api
- description: Customer master data (a party in the customer role).
  name: weclapp Customer API
  slug: weclapp-customer-api
- description: Purchase orders to suppliers.
  name: weclapp Purchase Order API
  slug: weclapp-purchase-order-api
- description: Sales quotations / quotes.
  name: weclapp Quotation API
  slug: weclapp-quotation-api
- description: Sales invoices.
  name: weclapp Sales Invoice API
  slug: weclapp-sales-invoice-api
- description: Sales orders.
  name: weclapp Sales Order API
  slug: weclapp-sales-order-api
- description: Outbound shipments / deliveries.
  name: weclapp Shipment API
  slug: weclapp-shipment-api
artifact_total: 22
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: weclapp REST Article API
  slug: open-weclapp-article-api
- collection_type: open
  name: weclapp REST Article Customer API
  slug: open-weclapp-customer-api
- collection_type: open
  name: weclapp REST Article Purchase Order API
  slug: open-weclapp-purchase-order-api
- collection_type: open
  name: weclapp REST Article Quotation API
  slug: open-weclapp-quotation-api
- collection_type: open
  name: weclapp REST Article Sales Invoice API
  slug: open-weclapp-sales-invoice-api
- collection_type: open
  name: weclapp REST Article Sales Order API
  slug: open-weclapp-sales-order-api
- collection_type: open
  name: weclapp REST Article Shipment API
  slug: open-weclapp-shipment-api
- collection_type: open
  name: weclapp REST API
  slug: open-weclapp
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/weclapp-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/weclapp-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/weclapp-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/weclapp
- group: company
  title: ''
  type: Website
  url: https://www.weclapp.com/
- group: docs
  title: ''
  type: Documentation
  url: https://www.weclapp.com/api/
- group: commercial
  title: ''
  type: Plans
  url: plans/weclapp-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/weclapp-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/weclapp-finops.yml
created: '2026-07-12'
description: weclapp is a German cloud ERP / CRM / commerce platform for small and mid-sized businesses, combining CRM, sales, order management, accounting, inventory / warehouse management, purchasing, and e-commerce in one SaaS suite. Every weclapp tenant exposes a documented REST API at https://<tenant>.weclapp.com/webapp/api/v1/ with a live Swagger, covering 150+ business entities - parties (customers, suppliers, contacts, leads), articles, sales orders, quotations, sales invoices, shipments, purchase orders, warehouses, and more. Authentication is a per-user API token sent in the AuthenticationToken request header.
finops:
- name: Weclapp Finops
  service_category: Business Applications
  slug: weclapp-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/weclapp.png
layout: provider
modified: '2026-07-12'
name: weclapp
nav: Providers
network: true
overview: 'weclapp publishes 7 APIs on the [APIs.io](https://apis.io/) network, including Article API, Customer API, Purchase Order API, and 4 more. Tagged areas include ERP, CRM, Cloud ERP, Accounting, and Inventory.


  weclapp''s developer surface includes authentication, documentation, and 7 more developer resources.'
plans:
- name: Weclapp Plans Pricing
  plan_count: 5
  slug: weclapp-plans-pricing
random_paper: 13
rate_limits:
- limit_count: 2
  name: Weclapp Rate Limits
  slug: weclapp-rate-limits
score:
  band: thin
  composite: 35.9
  delta: -0.2
  facets:
    access_clarity: 39.5
    commercial_clarity: 39.5
    contract_governance: 0.0
    contract_quality: 54.3
    developer_ergonomics: 21.4
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 21.1
  previous_composite: 36.1
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 7
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: flat
security:
- kind: authentication
  name: Weclapp Authentication
  slug: weclapp-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Weclapp Domain Security
  slug: weclapp-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: weclapp
tags:
- ERP
- CRM
- Cloud ERP
- Accounting
- Inventory
- Commerce
- Germany
- Order Management
- Business Software
- SaaS
website: https://www.weclapp.com/
---
