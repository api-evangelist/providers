---
access_model:
  confidence: medium
  label: Paid
  onboarding: unknown
  pricing: paid
  public: false
  source:
  - plans
  trial: false
  try_now: false
agent_readiness:
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: false
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
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 0.0
  scored_at: '2026-09-05'
api_count: 6
apis:
- description: Manage customers, their service locations, and installed equipment records (make, model, age, and service history). Endpoint paths are modeled from FieldEdge's documented Customers & Locations module;
  name: FieldEdge Customers API
  slug: fieldedge-customers-api
- description: Create and track work orders (service calls / jobs) through their lifecycle, including status transitions, notes, attachments (photos), and technician signatures captured in the mobile app. Endpoint p
  name: FieldEdge Work Orders API
  slug: fieldedge-work-orders-api
- description: Read and manage appointments on the dispatch board - assigning jobs to technicians and viewing scheduled work across technicians and time windows. Endpoint paths are modeled from FieldEdge's documente
  name: FieldEdge Dispatch & Scheduling API
  slug: fieldedge-dispatch-api
- description: Generate and retrieve invoices from completed work and record payments, feeding the QuickBooks accounting sync. Endpoint paths are modeled from FieldEdge's documented Invoices/Payments module; the aut
  name: FieldEdge Invoices & Payments API
  slug: fieldedge-invoices-api
- description: Manage recurring service agreements (maintenance plans) tied to customers and equipment, including covered visits and renewal tracking. Endpoint paths are modeled from FieldEdge's documented Service A
  name: FieldEdge Service Agreements API
  slug: fieldedge-service-agreements-api
- description: Read the flat-rate pricebook of services, parts, and materials used to build quotes and invoices in the field. Endpoint paths are modeled from FieldEdge's documented Pricebook module; the authoritativ
  name: FieldEdge Pricebook API
  slug: fieldedge-pricebook-api
artifact_total: 8
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/fieldedge-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/fieldedge
- group: company
  title: ''
  type: Website
  url: https://fieldedge.com
- group: docs
  title: ''
  type: Documentation
  url: https://docs.api.fieldedge.com
- group: commercial
  title: ''
  type: Pricing
  url: https://fieldedge.com/pricing/
- group: commercial
  title: ''
  type: Plans
  url: plans/fieldedge-plans-pricing.yml
- group: company
  title: ''
  type: Blog
  url: https://fieldedge.com/blog/feed/
created: '2026-07-03'
description: FieldEdge is field service management (FSM) software for HVAC, plumbing, electrical, and other home- and commercial-services contractors, owned by Xplor Technologies (branded "FieldEdge by Xplor"). It provides customer management, dispatching and scheduling, work orders, a technician mobile app, flat-rate pricebook, service agreements, invoicing and payments, and QuickBooks accounting sync. FieldEdge operates a partner-gated API delivered through an Azure API Management developer portal (docs.api.fieldedge.com); API products and keys are restricted to approved integration partners rather than being openly self-serve. The logical APIs listed here are honestly modeled from FieldEdge's documented product modules and its partner/integration surface - endpoint paths are modeled, not copied from a published public reference, because the reference and OpenAPI live behind the partner portal sign-in.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/fieldedge.png
layout: provider
modified: '2026-07-03'
name: FieldEdge
nav: Providers
network: true
overview: 'FieldEdge publishes 6 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Field Service Management, FSM, HVAC, Plumbing, and Electrical.


  FieldEdge''s developer surface includes documentation, pricing, engineering blog, and 4 more developer resources.'
plans:
- name: Fieldedge Plans Pricing
  plan_count: 2
  slug: fieldedge-plans-pricing
random_paper: 18
score:
  band: emerging
  composite: 16.1
  coverage:
    artifact_dirs: 4
    catalog_earned: 48.0
    catalog_earned_first_party: 0.0
    catalog_gap: 67.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 31.6
    commercial_clarity: 31.6
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 11.9
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 16.1
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/fieldedge/refs/heads/main/screenshots/fieldedge-2026-07-25T214426.png
security:
- kind: domain-security
  name: Fieldedge Domain Security
  slug: fieldedge-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: fieldedge
tags:
- Field Service Management
- FSM
- HVAC
- Plumbing
- Electrical
- Home Services
- Dispatch
- Work Orders
- Contractors
- Xplor
website: https://fieldedge.com
---
