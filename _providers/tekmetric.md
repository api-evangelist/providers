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
    auth_clarity: negotiable
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
  score: 22.7
  scored_at: '2026-09-02'
agentic_access:
- acting_count: 1
  human_in_the_loop: 0
  name: Tekmetric Agentic Access
  operation_count: 17
  slug: tekmetric-agentic-access
  summary_line: 17 operations · 1 acting
api_count: 1
apis:
- baseURL: https://shop.tekmetric.com/api/v1
  baseurl_source: declared
  description: Scheduled shop appointments.
  name: Tekmetric Appointments API
  slug: tekmetric-appointments-api
- baseURL: https://shop.tekmetric.com/api/v1
  baseurl_source: declared
  description: Pre-built menu services bundling standard labor and parts.
  name: Tekmetric Canned Jobs API
  slug: tekmetric-canned-jobs-api
- baseURL: https://shop.tekmetric.com/api/v1
  baseurl_source: declared
  description: Shop customers and their contact information.
  name: Tekmetric Customers API
  slug: tekmetric-customers-api
- baseURL: https://shop.tekmetric.com/api/v1
  baseurl_source: declared
  description: Shop technicians and staff.
  name: Tekmetric Employees API
  slug: tekmetric-employees-api
- baseURL: https://shop.tekmetric.com/api/v1
  baseurl_source: declared
  description: Parts and tire inventory.
  name: Tekmetric Inventory API
  slug: tekmetric-inventory-api
- baseURL: https://shop.tekmetric.com/api/v1
  baseurl_source: declared
  description: Individual services (labor and parts) within a repair order.
  name: Tekmetric Jobs API
  slug: tekmetric-jobs-api
- baseURL: https://shop.tekmetric.com/api/v1
  baseurl_source: declared
  description: Estimates and invoices tracking a vehicle's work.
  name: Tekmetric Repair Orders API
  slug: tekmetric-repair-orders-api
- baseURL: https://shop.tekmetric.com/api/v1
  baseurl_source: declared
  description: Shop locations, hours, labor rates, and settings.
  name: Tekmetric Shops API
  slug: tekmetric-shops-api
- baseURL: https://shop.tekmetric.com/api/v1
  baseurl_source: declared
  description: Customer vehicles serviced by the shop.
  name: Tekmetric Vehicles API
  slug: tekmetric-vehicles-api
artifact_total: 28
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Tekmetric Appointments API
  slug: open-tekmetric-appointments-api
- collection_type: open
  name: Tekmetric Appointments Canned Jobs API
  slug: open-tekmetric-canned-jobs-api
- collection_type: open
  name: Tekmetric Appointments Customers API
  slug: open-tekmetric-customers-api
- collection_type: open
  name: Tekmetric Appointments Employees API
  slug: open-tekmetric-employees-api
- collection_type: open
  name: Tekmetric Appointments Inventory API
  slug: open-tekmetric-inventory-api
- collection_type: open
  name: Tekmetric Appointments Jobs API
  slug: open-tekmetric-jobs-api
- collection_type: open
  name: Tekmetric Appointments Repair Orders API
  slug: open-tekmetric-repair-orders-api
- collection_type: open
  name: Tekmetric Appointments Shops API
  slug: open-tekmetric-shops-api
- collection_type: open
  name: Tekmetric Appointments Vehicles API
  slug: open-tekmetric-vehicles-api
- collection_type: open
  name: Tekmetric API
  slug: open-tekmetric
common:
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/tekmetric-capability-edges.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/tekmetric-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/tekmetric-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/tekmetric-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/tekmetric-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/tekmetric-scopes.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Tekmetric
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/tekmetric
- group: company
  title: ''
  type: Website
  url: https://www.tekmetric.com/
- group: docs
  title: ''
  type: Documentation
  url: https://api.tekmetric.com
- group: commercial
  title: ''
  type: Plans
  url: plans/tekmetric-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/tekmetric-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/tekmetric-finops.yml
created: '2026-07-04'
description: Tekmetric is a cloud-based auto repair shop management platform (digital vehicle inspections, estimates, repair orders, inventory, job/technician tracking, and customer communication). Tekmetric operates a partner-gated REST API - access requires requesting credentials at api.tekmetric.com and waiting for Tekmetric's approval (no self-serve signup or public API reference); approved partners authenticate with OAuth 2.0 client credentials against a sandbox or production base URL and read shop, customer, vehicle, repair order, job, employee, appointment, canned job, and inventory data.
finops:
- name: Tekmetric Finops
  service_category: Vertical SaaS - Auto Repair Shop Management
  slug: tekmetric-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/tekmetric.png
layout: provider
modified: '2026-07-04'
name: Tekmetric
nav: Providers
network: true
overview: 'Tekmetric publishes 9 APIs on the [APIs.io](https://apis.io/) network, including Appointments API, Canned Jobs API, Customers API, and 6 more. Tagged areas include Automotive, Auto Repair, Shop Management, Fleet, and Vertical SaaS.


  Tekmetric''s developer surface includes authentication, documentation, and 11 more developer resources.'
plans:
- name: Tekmetric Plans Pricing
  plan_count: 6
  slug: tekmetric-plans-pricing
random_paper: 2
rate_limits:
- limit_count: 2
  name: Tekmetric Rate Limits
  slug: tekmetric-rate-limits
scopes:
- name: Tekmetric Scopes
  scope_count: 0
  slug: tekmetric-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: thin
  composite: 36.1
  coverage:
    artifact_dirs: 11
    catalog_gap: 55.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 47.4
    commercial_clarity: 47.4
    contract_governance: 0.0
    contract_quality: 53.3
    developer_ergonomics: 16.7
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 23.7
  previous_composite: 36.1
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 9
  schema_version: 0.18.0
  scored_at: '2026-09-02'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/tekmetric/refs/heads/main/screenshots/tekmetric-2026-09-02T162726.png
security:
- kind: authentication
  name: Tekmetric Authentication
  slug: tekmetric-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Tekmetric Domain Security
  slug: tekmetric-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Tekmetric Trust Center
  slug: tekmetric-trust-center
  summary_line: SOC 2, ISO 27001
slug: tekmetric
tags:
- Automotive
- Auto Repair
- Shop Management
- Fleet
- Vertical SaaS
website: https://www.tekmetric.com/
---
