---
access_model:
  confidence: high
  label: Enterprise (free trial) · Self-serve signup
  onboarding: self-serve
  pricing: enterprise
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
  scored_at: '2026-09-01'
agentic_access:
- acting_count: 3
  human_in_the_loop: 0
  name: Wm Agentic Access
  operation_count: 27
  slug: wm-agentic-access
  summary_line: 27 operations · 3 acting
api_count: 1
apis:
- description: Notes, email, and issue activity on an account.
  name: WM Activities API
  slug: wm-activities-api
- description: Service cases and pickup tickets.
  name: WM Cases & Tickets API
  slug: wm-cases-tickets-api
- description: Billing and service contacts on an account.
  name: WM Contacts API
  slug: wm-contacts-api
- description: Invoice history and account balance.
  name: WM Invoices & Balance API
  slug: wm-invoices-balance-api
- description: Account profile settings and communication preferences.
  name: WM Profiles & Preferences API
  slug: wm-profiles-preferences-api
- description: Routing and hauling material information.
  name: WM Service Operations & Materials API
  slug: wm-service-operations-materials-api
- description: Base rates and invoice fees.
  name: WM Service Pricing API
  slug: wm-service-pricing-api
- description: Account services, schedule, status, and ETA.
  name: WM Services API
  slug: wm-services-api
artifact_total: 24
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: WM Customer Activities API
  slug: open-wm-activities-api
- collection_type: open
  name: WM Customer Activities Cases & Tickets API
  slug: open-wm-cases-tickets-api
- collection_type: open
  name: WM Customer Activities Contacts API
  slug: open-wm-contacts-api
- collection_type: open
  name: WM Customer Activities Invoices & Balance API
  slug: open-wm-invoices-balance-api
- collection_type: open
  name: WM Customer Activities Profiles & Preferences API
  slug: open-wm-profiles-preferences-api
- collection_type: open
  name: WM Customer Activities Service Operations & Materials API
  slug: open-wm-service-operations-materials-api
- collection_type: open
  name: WM Customer Activities Service Pricing API
  slug: open-wm-service-pricing-api
- collection_type: open
  name: WM Customer Activities Services API
  slug: open-wm-services-api
- collection_type: open
  name: WM Customer API
  slug: open-wm
common:
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/wm-capability-edges.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/wm-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/wm-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/wm-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://www.wm.com
- group: docs
  title: ''
  type: Documentation
  url: https://api.wm.com/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/waste-management
- group: commercial
  title: ''
  type: Plans
  url: plans/wm-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/wm-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/wm-finops.yml
created: '2026-07-03'
description: WM (formerly Waste Management, Inc.) is North America's largest integrated environmental solutions company, serving nearly 20 million municipal, commercial, industrial, and residential customers through collection, transfer, recycling, landfill, and waste-to-energy operations. WM does not run a self-serve, publicly-signup developer platform. It publishes a documented partner/customer REST API at api.wm.com covering account-level service and billing data - service details and pickup schedules, live service status and truck ETA, routing and hauling material information, pricing, invoices and aging balance, communication preferences, contacts, cases, tickets, and account activity notes. Access requires a WM-issued ClientId plus a JSON Web Token (JWT) and is granted on request to existing commercial/enterprise customers and integration partners by emailing apiaccess@wm.com; there is no open, self-serve API key signup.
finops:
- name: Wm Finops
  service_category: Field Services and Waste Management
  slug: wm-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/wm.png
layout: provider
modified: '2026-07-03'
name: WM
nav: Providers
network: true
overview: 'WM publishes 8 APIs on the [APIs.io](https://apis.io/) network, including Activities API, Cases & Tickets API, Contacts API, and 5 more. Tagged areas include Waste Management, Recycling, Environmental Services, Field Services, and Logistics.


  WM''s developer surface includes authentication, documentation, and 8 more developer resources.'
plans:
- name: Wm Plans Pricing
  plan_count: 1
  slug: wm-plans-pricing
random_paper: 18
rate_limits:
- limit_count: 1
  name: Wm Rate Limits
  slug: wm-rate-limits
score:
  band: thin
  composite: 35.0
  coverage:
    artifact_dirs: 9
    catalog_gap: 59.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 28.9
    commercial_clarity: 28.9
    contract_governance: 0.0
    contract_quality: 55.8
    developer_ergonomics: 28.6
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 21.1
  previous_composite: 35.0
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 8
  schema_version: 0.18.0
  scored_at: '2026-09-01'
  trend: flat
security:
- kind: authentication
  name: Wm Authentication
  slug: wm-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Wm Domain Security
  slug: wm-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: wm
tags:
- Waste Management
- Recycling
- Environmental Services
- Field Services
- Logistics
- Account Management
- Enterprise
- B2B
website: https://www.wm.com
---
