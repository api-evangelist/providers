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
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 19.4
  scored_at: '2026-08-11'
api_count: 12
apis:
- description: GraphQL operations over the Accounts domain - search and read client (pet owner) records including contact details, addresses, balances, linked patients, and communication preferences, and create or u
  name: Vetspire Accounts & Clients API
  slug: vetspire-accounts-clients-api
- description: GraphQL operations over the Clinical domain patient records - species, breed, sex, weight history, microchip, alerts, and the owning client - plus mutations to register and update patients (animals).
  name: Vetspire Patients API
  slug: vetspire-patients-api
- description: GraphQL operations over the Schedule domain - list appointments for a location and date range, read provider schedules by location, and create, reschedule, or cancel appointments and appointment types
  name: Vetspire Schedule & Appointments API
  slug: vetspire-schedule-appointments-api
- description: GraphQL operations over the Clinical and Treatment domains - encounters (visits/SOAP notes), treatment sheets, immunizations, prescriptions, and clinical history for a patient, with mutations to creat
  name: Vetspire Encounters & Clinical Records API
  slug: vetspire-encounters-clinical-api
- description: GraphQL operations over the Billing and New Billing domains - invoices, line items, orders, payments, and accounts-receivable balances, with mutations to create invoices, apply charges, and record pay
  name: Vetspire Billing & Invoices API
  slug: vetspire-billing-invoices-api
- description: GraphQL operations over the Inventory domain - products and the product catalog, pricing, stock levels, stock transfers, and vendors, with mutations to manage products and adjust inventory.
  name: Vetspire Inventory & Products API
  slug: vetspire-inventory-products-api
- description: GraphQL operations over the Hospital domain - organization and location records, providers (staff/DVMs), rooms, and operating hours used to scope scheduling, billing, and reporting across a multi-loca
  name: Vetspire Hospital & Locations API
  slug: vetspire-hospital-locations-api
- description: GraphQL operations over the Lab domain - diagnostic lab orders and results linked to encounters and patients, including reference ranges and result status, with mutations to create and update lab orde
  name: Vetspire Lab & Diagnostics API
  slug: vetspire-lab-diagnostics-api
- description: GraphQL operations over the Reminders domain - due and overdue service reminders (vaccinations, wellness, recalls) per patient and client, used to drive compliance reporting and client outreach.
  name: Vetspire Reminders API
  slug: vetspire-reminders-api
- description: GraphQL operations over the Conversations and Marketing domains - client messaging threads (SMS/email), templates, and campaigns, with mutations to send messages and manage conversation state.
  name: Vetspire Conversations & Communications API
  slug: vetspire-conversations-api
- description: GraphQL operations over the Analytics domain - aggregate practice metrics and reporting datasets (production, revenue, appointments, compliance) used for dashboards and data warehousing.
  name: Vetspire Analytics & Reporting API
  slug: vetspire-analytics-api
- description: GraphQL operations over the Events domain - a queryable log of platform events (record created, updated, deleted, and workflow triggers) for auditing, synchronization, and integration polling.
  name: Vetspire Events API
  slug: vetspire-events-api
artifact_total: 18
collections:
- collection_type: open
  name: Vetspire GraphQL API
  slug: open-vetspire
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/vetspire-domain-security.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/vetspire
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/vetspire
- group: company
  title: ''
  type: Website
  url: https://vetspire.com/
- group: docs
  title: ''
  type: Documentation
  url: https://developer.vetspire.com/
- group: commercial
  title: ''
  type: Plans
  url: plans/vetspire-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/vetspire-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/vetspire-finops.yml
- group: operate
  title: ''
  type: Support
  url: https://support.vetspire.com/support/solutions/folders/70000486207
created: '2026-07-04'
description: Vetspire is a cloud-based, AI-enabled veterinary practice management (PIMS) platform for animal hospitals and clinics, covering electronic medical records, scheduling, client communications, billing, inventory, labs, and reminders. Vetspire exposes a single public GraphQL API at https://api.vetspire.com/graphql - every action in the product is powered by GraphQL - authenticated with an Authorization API token and organized by veterinary practice domains (Accounts, Clinical, Schedule, Billing, Inventory, Hospital, Lab, Reminders, Conversations, Analytics, Events). The schema exposes 400+ object types, 248 input objects, and 112 enums, with a maximum query depth of 8.
finops:
- name: Vetspire Finops
  service_category: Veterinary Practice Management Software
  slug: vetspire-finops
graphqls:
- description: 'Vetspire is a cloud-based veterinary practice management platform. Its entire public API is GraphQL - "every action within Vetspire is powered by GraphQL requests." Clients declare exactly the fields '
  name: Vetspire GraphQL API
  slug: vetspire-graphql
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/vetspire.png
layout: provider
modified: '2026-07-04'
name: Vetspire
nav: Providers
network: true
overview: 'Vetspire publishes 12 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Veterinary, Practice Management, PIMS, Healthcare, and GraphQL.


  Vetspire''s developer surface includes documentation, support, and 7 more developer resources.'
plans:
- name: Vetspire Plans Pricing
  plan_count: 4
  slug: vetspire-plans-pricing
random_paper: 70
rate_limits:
- limit_count: 2
  name: Vetspire Rate Limits
  slug: vetspire-rate-limits
score:
  band: thin
  composite: 28.4
  delta: 0.0
  facets:
    commercial_clarity: 39.5
    contract_quality: 43.2
    developer_ergonomics: 13.0
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 26.3
  previous_composite: 28.4
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 7.5
  schema_version: 0.11.0
  scored_at: '2026-08-11'
  trend: flat
security:
- kind: domain-security
  name: Vetspire Domain Security
  slug: vetspire-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: vetspire
tags:
- Veterinary
- Practice Management
- PIMS
- Healthcare
- GraphQL
- Electronic Medical Records
- Scheduling
website: https://vetspire.com/
---
