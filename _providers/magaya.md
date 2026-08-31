---
access_model:
  confidence: high
  label: Paid · Self-serve signup
  onboarding: self-serve
  pricing: paid
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 19.8
  scored_at: '2026-08-30'
agentic_access:
- acting_count: 4
  human_in_the_loop: 0
  name: Magaya Agentic Access
  operation_count: 14
  slug: magaya-agentic-access
  summary_line: 14 operations · 4 acting
api_count: 1
apis:
- description: Accounts-receivable invoices and their charge lines.
  name: Magaya Invoices API
  slug: magaya-invoices-api
- description: Item and commodity master data referenced across transactions.
  name: Magaya Items API
  slug: magaya-items-api
- description: Air, ocean, and ground shipment records and their tracking events.
  name: Magaya Shipments API
  slug: magaya-shipments-api
- description: Generic Magaya transaction documents - orders, bookings, quotes, releases.
  name: Magaya Transactions API
  slug: magaya-transactions-api
- description: Cargo received into a Magaya-managed warehouse and inventory balances.
  name: Magaya Warehouse Receipts API
  slug: magaya-warehouse-receipts-api
artifact_total: 18
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Magaya API (Modeled) Invoices API
  slug: open-magaya-invoices-api
- collection_type: open
  name: Magaya API (Modeled) Invoices Items API
  slug: open-magaya-items-api
- collection_type: open
  name: Magaya API (Modeled) Invoices Shipments API
  slug: open-magaya-shipments-api
- collection_type: open
  name: Magaya API (Modeled) Invoices Transactions API
  slug: open-magaya-transactions-api
- collection_type: open
  name: Magaya API (Modeled) Invoices Warehouse Receipts API
  slug: open-magaya-warehouse-receipts-api
- collection_type: open
  name: Magaya API (Modeled)
  slug: open-magaya
common:
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/magaya-capability-edges.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/magaya-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/magaya-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/magaya-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/magaya-dev
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/magaya-corporation-inc-
- group: company
  title: ''
  type: Website
  url: https://www.magaya.com/
- group: docs
  title: ''
  type: Documentation
  url: https://help.magaya.com/s/document-item?language=en_US&bundleId=magaya-api
- group: docs
  title: ''
  type: APIReference
  url: https://developer.qwykportals.com/
- group: start
  title: ''
  type: SignUp
  url: https://www.magaya.com/start-here/
- group: commercial
  title: ''
  type: Plans
  url: plans/magaya-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/magaya-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/magaya-finops.yml
created: '2026-07-05'
description: Magaya is a logistics and supply chain software company whose cloud Digital Freight Platform runs freight forwarding, warehouse management, customs compliance, rate management, and a digital customer experience portal. Magaya exposes programmatic access to the logistics objects inside a customer's system - Shipments, Warehouse Receipts, Invoices, Items, and financial Transactions - through the Magaya API (a SOAP/XML Web Service) and the newer Magaya Open API collection of web services, plus a REST Digital Freight Portal API inherited from the Qwyk acquisition. API access is gated behind a Magaya subscription and a dedicated API user configured in the customer's own tenant (base URL of the form https://SYSTEMID.magayacloud.com/api); the reference documentation is public but runtime access requires a licensed system, so the resource paths below are honestly modeled from Magaya's published object model rather than confirmed against an open self-serve reference.
finops:
- name: Magaya Finops
  service_category: Logistics and Supply Chain Software
  slug: magaya-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/magaya.png
layout: provider
modified: '2026-07-05'
name: Magaya
nav: Providers
network: true
overview: 'Magaya publishes 5 APIs on the [APIs.io](https://apis.io/) network, including Invoices API, Items API, Shipments API, and 2 more. Tagged areas include Logistics, Supply Chain, Freight Forwarding, Warehouse Management, and Shipping.


  Magaya''s developer surface includes authentication, documentation, API reference, signup flow, and 9 more developer resources.'
plans:
- name: Magaya Plans Pricing
  plan_count: 2
  slug: magaya-plans-pricing
random_paper: 15
rate_limits:
- limit_count: 3
  name: Magaya Rate Limits
  slug: magaya-rate-limits
score:
  band: thin
  composite: 38.5
  coverage:
    artifact_dirs: 10
    catalog_gap: 55.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: -0.5
  facets:
    access_clarity: 42.1
    commercial_clarity: 42.1
    contract_governance: 0.0
    contract_quality: 48.3
    developer_ergonomics: 33.3
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 34.2
  previous_composite: 39.0
  provenance:
    agentic_access: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 5
  schema_version: 0.17.2
  scored_at: '2026-08-30'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/magaya/refs/heads/main/screenshots/magaya-2026-07-25T225839.png
security:
- kind: authentication
  name: Magaya Authentication
  slug: magaya-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Magaya Domain Security
  slug: magaya-domain-security
  summary_line: TLSv1.2 · DMARC
slug: magaya
tags:
- Logistics
- Supply Chain
- Freight Forwarding
- Warehouse Management
- Shipping
- Customs
- Transportation
website: https://www.magaya.com/
---
