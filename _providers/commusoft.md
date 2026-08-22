---
access_model:
  confidence: high
  label: Enterprise · Self-serve signup
  onboarding: self-serve
  pricing: enterprise
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
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: partial
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 32.1
  scored_at: '2026-08-19'
agentic_access:
- acting_count: 15
  human_in_the_loop: 0
  name: Commusoft Agentic Access
  operation_count: 27
  slug: commusoft-agentic-access
  summary_line: 27 operations · 15 acting
api_count: 9
apis:
- description: REST API for programmatic access to Commusoft's field service management platform, enabling management of jobs, customers, engineers, quotes, invoices, parts, and service histories for trades business
  name: Commusoft API
  slug: commusoft-api
- description: Obtain API access tokens
  name: Commusoft Authentication API
  slug: commusoft-authentication-api
- description: Manage contacts linked to customers or suppliers
  name: Commusoft Contacts API
  slug: commusoft-contacts-api
- description: Manage customer records including addresses, contacts, and property details
  name: Commusoft Customers API
  slug: commusoft-customers-api
- description: Manage calendar and scheduling diary events
  name: Commusoft Diary Events API
  slug: commusoft-diary-events-api
- description: Manage location/site records
  name: Commusoft Locations API
  slug: commusoft-locations-api
- description: Manage supplier records and contact details
  name: Commusoft Suppliers API
  slug: commusoft-suppliers-api
- description: Manage title settings (Mr, Mrs, Dr, etc.)
  name: Commusoft Titles API
  slug: commusoft-titles-api
- description: Retrieve user records
  name: Commusoft Users API
  slug: commusoft-users-api
artifact_total: 35
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Commusoft Authentication API
  slug: open-commusoft-authentication-api
- collection_type: open
  name: Commusoft Authentication Contacts API
  slug: open-commusoft-contacts-api
- collection_type: open
  name: Commusoft Authentication Customers API
  slug: open-commusoft-customers-api
- collection_type: open
  name: Commusoft Authentication Diary Events API
  slug: open-commusoft-diary-events-api
- collection_type: open
  name: Commusoft Authentication Locations API
  slug: open-commusoft-locations-api
- collection_type: open
  name: Commusoft Authentication Suppliers API
  slug: open-commusoft-suppliers-api
- collection_type: open
  name: Commusoft Authentication Titles API
  slug: open-commusoft-titles-api
- collection_type: open
  name: Commusoft Authentication Users API
  slug: open-commusoft-users-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/commusoft-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/commusoft-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/commusoft-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://www.commusoft.com/
- group: docs
  title: ''
  type: Documentation
  url: https://commusoft.docs.apiary.io/
- group: company
  title: ''
  type: Blog
  url: https://www.commusoft.com/en-us/blog/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.commusoft.com/en-us/plans/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.commusoft.com/public-api
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/commusoft
- group: other
  title: ''
  type: X
  url: https://x.com/commusoft
- group: commercial
  title: ''
  type: Plans
  url: plans/commusoft-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/commusoft-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/commusoft-finops.yml
created: '2026-06-13'
description: Commusoft is a cloud-based field service management software platform founded in 2006, purpose-built for trades businesses including HVAC, plumbing, electrical, and building maintenance contractors. The platform provides a comprehensive REST API that enables developers and integration partners to manage jobs, customers, engineers, quotes, invoices, parts, and service histories programmatically. Commusoft's API powers integrations with accounting tools such as QuickBooks, Xero, and Sage, as well as payment processors like Stripe and GoCardless, and workflow automation platforms like Zapier. The API is documented on Apiary and supports OAuth-based authentication, enabling secure third-party access to job management workflows and customer data. With over 10,000 active users completing 2.1 million jobs annually, Commusoft sits at the intersection of field operations and digital integration for service businesses.
examples:
- key_count: 15
  name: Customer Example
  slug: customer-example
- key_count: 12
  name: Diary Event Example
  slug: diary-event-example
- key_count: 10
  name: Supplier Example
  slug: supplier-example
finops:
- name: Commusoft Finops
  service_category: ''
  slug: commusoft-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/commusoft.png
json_schemas:
- name: AccountingSettings
  property_count: 3
  slug: accounting-settings
- name: Address
  property_count: 6
  slug: address
- name: Customer
  property_count: 15
  slug: customer
- name: DiaryEvent
  property_count: 12
  slug: diary-event
- name: PropertyDetails
  property_count: 5
  slug: property-details
- name: Supplier
  property_count: 10
  slug: supplier
jsonld:
- class_count: 44
  name: Commusoft Context
  property_count: 5
  slug: commusoft-context
layout: provider
modified: '2026-06-13'
name: Commusoft
nav: Providers
network: true
overview: 'Commusoft publishes 8 APIs on the [APIs.io](https://apis.io/) network, including Authentication API, Contacts API, Customers API, and 5 more. Tagged areas include Field Service Management, Job Management, HVAC, Plumbing, and Trades.


  The Commusoft catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Commusoft''s developer surface includes authentication, documentation, engineering blog, pricing, and 9 more developer resources.'
plans:
- name: Commusoft Plans Pricing
  plan_count: 5
  slug: commusoft-plans-pricing
random_paper: 2
rate_limits:
- limit_count: 0
  name: Commusoft Rate Limits
  slug: commusoft-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: Commusoft API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: commusoft-jsonschema-spectral-rules
score:
  band: developing
  composite: 40.7
  delta: -6.4
  facets:
    access_clarity: 50.0
    commercial_clarity: 50.0
    contract_governance: 9.8
    contract_quality: 64.9
    developer_ergonomics: 19.0
    discoverability: 74.1
    governance: 9.8
    operational_transparency: 15.8
  previous_composite: 47.1
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 8
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: falling
screenshot: https://raw.githubusercontent.com/api-evangelist/commusoft/refs/heads/main/screenshots/commusoft-2026-06-20T174826.png
security:
- kind: authentication
  name: Commusoft Authentication
  slug: commusoft-authentication
  summary_line: apiKey · 2 schemes
- kind: domain-security
  name: Commusoft Domain Security
  slug: commusoft-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: commusoft
tags:
- Field Service Management
- Job Management
- HVAC
- Plumbing
- Trades
- Scheduling
- Invoicing
- Engineers
- Customers
- Service History
website: https://www.commusoft.com/
---
