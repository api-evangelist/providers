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
    auth_clarity: true
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
  score: 30.6
  scored_at: '2026-08-03'
agentic_access:
- acting_count: 23
  human_in_the_loop: 0
  name: Phorest Agentic Access
  operation_count: 62
  slug: phorest-agentic-access
  summary_line: 62 operations · 23 acting
api_count: 14
apis:
- description: Appointment lifecycle - list, retrieve, update, cancel, confirm, check in.
  name: Phorest Appointments API
  slug: phorest-appointments-api
- description: Booking creation and lifecycle, plus real-time availability checks.
  name: Phorest Bookings API
  slug: phorest-bookings-api
- description: Branches (locations), rooms, machines, and tax rates.
  name: Phorest Branches API
  slug: phorest-branches-api
- description: Client (customer) records and client categories.
  name: Phorest Clients API
  slug: phorest-clients-api
- description: Course templates and a client's purchased course sessions.
  name: Phorest Courses API
  slug: phorest-courses-api
- description: Marketing leads and lead statistics.
  name: Phorest Leads API
  slug: phorest-leads-api
- description: Client loyalty point adjustments.
  name: Phorest Loyalty API
  slug: phorest-loyalty-api
- description: Retail products and inventory.
  name: Phorest Products API
  slug: phorest-products-api
- description: Point-of-sale purchases, stock adjustments, and till balances.
  name: Phorest Purchases API
  slug: phorest-purchases-api
- description: Asynchronous CSV export jobs for sale-level reporting.
  name: Phorest Reporting API
  slug: phorest-reporting-api
- description: Client reviews for syndication to external review platforms.
  name: Phorest Reviews API
  slug: phorest-reviews-api
- description: Services, service categories, packages, and special offers.
  name: Phorest Services API
  slug: phorest-services-api
- description: Staff records, rota/work-time tables, and staff breaks.
  name: Phorest Staff API
  slug: phorest-staff-api
- description: Gift voucher creation, lookup, and balance updates.
  name: Phorest Vouchers API
  slug: phorest-vouchers-api
artifact_total: 23
collections:
- collection_type: open
  name: Phorest Third-Party API
  slug: open-phorest
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/phorest-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/phorest-trust-center.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/phorest-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/phorest-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/phorest-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/phorest
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/phorest
- group: company
  title: ''
  type: Website
  url: https://www.phorest.com/
- group: docs
  title: ''
  type: Documentation
  url: https://developer.phorest.com/docs/getting-started
- group: commercial
  title: ''
  type: Plans
  url: plans/phorest-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/phorest-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/phorest-finops.yml
- group: company
  title: ''
  type: Blog
  url: https://www.phorest.com/blog/feed/
created: '2026-07-03'
description: Phorest is salon and spa business management software (scheduling, point of sale, client marketing, online booking, and reporting) used by hair, beauty, and med-spa businesses across the UK, Ireland, mainland Europe, North America, and Australia. Partner-gated access is granted to the Phorest API (also called Phorest Connect by some partners) on request - a REST, basic-authenticated API scoped per business and branch that exposes clients, appointments/bookings, staff, services, products, purchases, vouchers, and reporting data so approved developers can build custom booking flows, e-commerce integrations, call-centre lookups, and reporting tools on top of a salon's Phorest data.
finops:
- name: Phorest Finops
  service_category: Vertical SaaS - Salon and Spa Business Management
  slug: phorest-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/phorest.png
layout: provider
modified: '2026-07-03'
name: Phorest
nav: Providers
network: true
overview: 'Phorest publishes 14 APIs on the [APIs.io](https://apis.io/) network, including Appointments API, Bookings API, Branches API, and 11 more. Tagged areas include Salon Software, Spa Software, Scheduling, Point of Sale, and Business Management.


  Phorest''s developer surface includes authentication, documentation, engineering blog, and 10 more developer resources.'
plans:
- name: Phorest Plans Pricing
  plan_count: 7
  slug: phorest-plans-pricing
random_paper: 13
rate_limits:
- limit_count: 5
  name: Phorest Rate Limits
  slug: phorest-rate-limits
score:
  band: thin
  composite: 41.8
  delta: 0.0
  facets:
    commercial_clarity: 47.4
    contract_quality: 63.1
    developer_ergonomics: 21.7
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 36.8
  previous_composite: 41.8
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 14
  schema_version: 0.9
  scored_at: '2026-08-03'
  trend: flat
security:
- kind: authentication
  name: Phorest Authentication
  slug: phorest-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Phorest Domain Security
  slug: phorest-domain-security
  summary_line: TLSv1.2 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Phorest Vulnerability Disclosure
  slug: phorest-vulnerability-disclosure
  summary_line: disclosure policy published
- kind: trust-center
  name: Phorest Trust Center
  slug: phorest-trust-center
  summary_line: PCI DSS, HIPAA, GDPR
slug: phorest
tags:
- Salon Software
- Spa Software
- Scheduling
- Point of Sale
- Business Management
- Vertical SaaS
website: https://www.phorest.com/
---
