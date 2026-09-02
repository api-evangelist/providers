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
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 21.5
  scored_at: '2026-09-01'
agentic_access:
- acting_count: 58
  human_in_the_loop: 0
  name: Shopmonkey Agentic Access
  operation_count: 98
  slug: shopmonkey-agentic-access
  summary_line: 98 operations · 58 acting
api_count: 1
apis:
- description: Schedule, search, confirm, cancel, and update appointments.
  name: Shopmonkey Appointments API
  slug: shopmonkey-appointments-api
- description: Create, update, search, and manage customer records, emails, and phone numbers.
  name: Shopmonkey Customers API
  slug: shopmonkey-customers-api
- description: Manage Shopmonkey users (employees), roles, and the authenticated user's own profile.
  name: Shopmonkey Employees API
  slug: shopmonkey-employees-api
- description: Search the parts catalog, find compatible parts, and manage line-item assignments of parts/tires/labor.
  name: Shopmonkey Inventory & Parts API
  slug: shopmonkey-inventory-parts-api
- description: Shared (customer-facing) invoices/PDFs on an order, and manual payment and refund entries.
  name: Shopmonkey Invoices & Payments API
  slug: shopmonkey-invoices-payments-api
- description: Manage shop location details for a multi-location company.
  name: Shopmonkey Locations API
  slug: shopmonkey-locations-api
- description: Create, update, and look up vehicles, VIN/plate validation, year/make/model data, mileage, and tire-pressure logs.
  name: Shopmonkey Vehicles API
  slug: shopmonkey-vehicles-api
- description: Register and manage webhook subscriptions for Shopmonkey events.
  name: Shopmonkey Webhooks API
  slug: shopmonkey-webhooks-api
- description: Create and manage repair orders, order line items (services, parts, labor, fees, tires, subcontracts), authorizations, files, and PDFs.
  name: Shopmonkey Work Orders API
  slug: shopmonkey-work-orders-api
artifact_total: 26
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Shopmonkey Appointments API
  slug: open-shopmonkey-appointments-api
- collection_type: open
  name: Shopmonkey Appointments Customers API
  slug: open-shopmonkey-customers-api
- collection_type: open
  name: Shopmonkey Appointments Employees API
  slug: open-shopmonkey-employees-api
- collection_type: open
  name: Shopmonkey Appointments Inventory & Parts API
  slug: open-shopmonkey-inventory-parts-api
- collection_type: open
  name: Shopmonkey Appointments Invoices & Payments API
  slug: open-shopmonkey-invoices-payments-api
- collection_type: open
  name: Shopmonkey Appointments Locations API
  slug: open-shopmonkey-locations-api
- collection_type: open
  name: Shopmonkey Appointments Vehicles API
  slug: open-shopmonkey-vehicles-api
- collection_type: open
  name: Shopmonkey Appointments Webhooks API
  slug: open-shopmonkey-webhooks-api
- collection_type: open
  name: Shopmonkey Appointments Work Orders API
  slug: open-shopmonkey-work-orders-api
- collection_type: open
  name: Shopmonkey API
  slug: open-shopmonkey
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/shopmonkey-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/shopmonkey-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/shopmonkey-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/shopmonkeyus
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/shopmonkey
- group: company
  title: ''
  type: Website
  url: https://www.shopmonkey.io/
- group: docs
  title: ''
  type: Documentation
  url: https://shopmonkey.dev/overview
- group: commercial
  title: ''
  type: Plans
  url: plans/shopmonkey-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/shopmonkey-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/shopmonkey-finops.yml
created: '2026-07-04'
description: Shopmonkey is a cloud-based shop management platform for auto repair, tire, and powersports shops, covering estimates, work orders, customer communication, parts/inventory, scheduling, invoicing, and payments. Shopmonkey publishes a documented public API at developer.shopmonkey.io / shopmonkey.dev (base https://api.shopmonkey.cloud/v3). Despite being commonly assumed to be GraphQL, the confirmed public API is REST/JSON (v3), authenticated with a Bearer API key, covering 50+ resources - Work Orders, Customers, Vehicles, Parts/Inventory, Invoices/Payments, Appointments, Employees (Users), Locations, and Webhooks. No GraphQL endpoint, schema, or query/mutation language is documented anywhere on Shopmonkey's developer site. Enterprise accounts can also run the open-source Enterprise Data Streaming (EDS) server for near-real-time change data capture into a customer-controlled destination.
finops:
- name: Shopmonkey Finops
  service_category: Vertical SaaS - Auto Repair Shop Management
  slug: shopmonkey-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/shopmonkey.png
layout: provider
modified: '2026-07-04'
name: Shopmonkey
nav: Providers
network: true
overview: 'Shopmonkey publishes 9 APIs on the [APIs.io](https://apis.io/) network, including Appointments API, Customers API, Employees API, and 6 more. Tagged areas include Auto Repair, Shop Management, Field Service, REST, and Not GraphQL.


  Shopmonkey''s developer surface includes authentication, documentation, and 8 more developer resources.'
plans:
- name: Shopmonkey Plans Pricing
  plan_count: 4
  slug: shopmonkey-plans-pricing
random_paper: 9
rate_limits:
- limit_count: 1
  name: Shopmonkey Rate Limits
  slug: shopmonkey-rate-limits
score:
  band: thin
  composite: 32.7
  coverage:
    artifact_dirs: 8
    catalog_gap: 55.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 39.5
    commercial_clarity: 39.5
    contract_governance: 0.0
    contract_quality: 36.7
    developer_ergonomics: 28.6
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 23.7
  previous_composite: 32.7
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 4
      marker_coverage: 44.4
      total: 9
  schema_version: 0.18.0
  scored_at: '2026-09-01'
  trend: flat
security:
- kind: authentication
  name: Shopmonkey Authentication
  slug: shopmonkey-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Shopmonkey Domain Security
  slug: shopmonkey-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: shopmonkey
tags:
- Auto Repair
- Shop Management
- Field Service
- REST
- Not GraphQL
website: https://www.shopmonkey.io/
---
