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
  scored_at: '2026-09-05'
agentic_access:
- acting_count: 21
  human_in_the_loop: 0
  name: Weclapp Agentic Access
  operation_count: 42
  slug: weclapp-agentic-access
  summary_line: 42 operations · 21 acting
api_count: 1
apis:
- baseURL: https://{tenant}.weclapp.com/webapp/api/v1
  baseurl_source: declared
  description: Articles / products in the catalog.
  name: weclapp Article API
  slug: weclapp-article-api
- baseURL: https://{tenant}.weclapp.com/webapp/api/v1
  baseurl_source: declared
  description: Customer master data (a party in the customer role).
  name: weclapp Customer API
  slug: weclapp-customer-api
- baseURL: https://{tenant}.weclapp.com/webapp/api/v1
  baseurl_source: declared
  description: Purchase orders to suppliers.
  name: weclapp Purchase Order API
  slug: weclapp-purchase-order-api
- baseURL: https://{tenant}.weclapp.com/webapp/api/v1
  baseurl_source: declared
  description: Sales quotations / quotes.
  name: weclapp Quotation API
  slug: weclapp-quotation-api
- baseURL: https://{tenant}.weclapp.com/webapp/api/v1
  baseurl_source: declared
  description: Sales invoices.
  name: weclapp Sales Invoice API
  slug: weclapp-sales-invoice-api
- baseURL: https://{tenant}.weclapp.com/webapp/api/v1
  baseurl_source: declared
  description: Sales orders.
  name: weclapp Sales Order API
  slug: weclapp-sales-order-api
- baseURL: https://{tenant}.weclapp.com/webapp/api/v1
  baseurl_source: declared
  description: Outbound shipments / deliveries.
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
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/weclapp-capability-edges.yml
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


  weclapp''s developer surface includes authentication, documentation, and 8 more developer resources.'
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
  composite: 36.7
  coverage:
    artifact_dirs: 10
    catalog_earned: 60.0
    catalog_earned_first_party: 0.0
    catalog_gap: 55.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 39.5
    commercial_clarity: 39.5
    contract_governance: 0.0
    contract_quality: 52.9
    developer_ergonomics: 29.8
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 21.1
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - germany
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - dach
    - europe
  previous_composite: 36.7
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 7
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/weclapp/refs/heads/main/screenshots/weclapp-2026-09-02T170543.png
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
- Software-as-a-Service
website: https://www.weclapp.com/
---
