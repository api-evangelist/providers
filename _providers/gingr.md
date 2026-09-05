---
access_model:
  confidence: medium
  label: Paid
  onboarding: unknown
  pricing: paid
  public: false
  source:
  - plans
  - authentication
  - security
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
  scored_at: '2026-09-04'
agentic_access:
- acting_count: 22
  human_in_the_loop: 0
  name: Gingr Agentic Access
  operation_count: 48
  slug: gingr-agentic-access
  summary_line: 48 operations · 22 acting
api_count: 1
apis:
- baseURL: https://api.gingr.io/v1
  baseurl_source: declared
  description: Invoices and charges.
  name: Gingr Invoices API
  slug: gingr-invoices-api
- baseURL: https://api.gingr.io/v1
  baseurl_source: declared
  description: Owner/client ("parent") records.
  name: Gingr Owners API
  slug: gingr-owners-api
- baseURL: https://api.gingr.io/v1
  baseurl_source: declared
  description: Charging and refunding cards on file, invoices, and deposits.
  name: Gingr Payments API
  slug: gingr-payments-api
- baseURL: https://api.gingr.io/v1
  baseurl_source: declared
  description: Pet profiles belonging to an owner.
  name: Gingr Pets API
  slug: gingr-pets-api
- baseURL: https://api.gingr.io/v1
  baseurl_source: declared
  description: Daily activity report cards generated for a pet's stay.
  name: Gingr Report Cards API
  slug: gingr-report-cards-api
- baseURL: https://api.gingr.io/v1
  baseurl_source: declared
  description: Bookings/reservations for daycare, boarding, training, and grooming.
  name: Gingr Reservations API
  slug: gingr-reservations-api
- baseURL: https://api.gingr.io/v1
  baseurl_source: declared
  description: Service catalog and facility configuration.
  name: Gingr Services API
  slug: gingr-services-api
- baseURL: https://api.gingr.io/v1
  baseurl_source: declared
  description: Pet immunization/vaccination records.
  name: Gingr Vaccinations API
  slug: gingr-vaccinations-api
- baseURL: https://api.gingr.io/v1
  baseurl_source: declared
  description: Managing bookings that are on the facility waitlist.
  name: Gingr Waitlist API
  slug: gingr-waitlist-api
artifact_total: 26
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Gingr Partner Invoices API
  slug: open-gingr-invoices-api
- collection_type: open
  name: Gingr Partner Invoices Owners API
  slug: open-gingr-owners-api
- collection_type: open
  name: Gingr Partner Invoices Payments API
  slug: open-gingr-payments-api
- collection_type: open
  name: Gingr Partner Invoices Pets API
  slug: open-gingr-pets-api
- collection_type: open
  name: Gingr Partner Invoices Report Cards API
  slug: open-gingr-report-cards-api
- collection_type: open
  name: Gingr Partner Invoices Reservations API
  slug: open-gingr-reservations-api
- collection_type: open
  name: Gingr Partner Invoices Services API
  slug: open-gingr-services-api
- collection_type: open
  name: Gingr Partner Invoices Vaccinations API
  slug: open-gingr-vaccinations-api
- collection_type: open
  name: Gingr Partner Invoices Waitlist API
  slug: open-gingr-waitlist-api
- collection_type: open
  name: Gingr Partner API
  slug: open-gingr
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/gingr-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/gingr-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/gingr-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/gingr-llc
- group: company
  title: ''
  type: Website
  url: https://www.gingrapp.com
- group: docs
  title: ''
  type: Documentation
  url: https://support.gingrapp.com/hc/en-us
- group: commercial
  title: ''
  type: Plans
  url: plans/gingr-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/gingr-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/gingr-finops.yml
- group: company
  title: ''
  type: Blog
  url: https://www.gingrapp.com/blog
created: '2026-07-04'
description: Gingr is pet-care business management software for dog daycare, boarding, training, and grooming facilities, covering reservations, check-in/checkout, client and pet records, feeding and medication schedules, immunizations, report cards, point of sale, and payments. Gingr publishes a JSON:API-style Partner API (api.gingr.io, X-Api-Key header, live OpenAPI/Swagger and Postman collection at docs.gingr.io) covering owners (parents), pets, bookings/reservations, invoices and payments, immunizations, and report cards, alongside an older subdomain-scoped legacy reporting API used for read-only pulls of owners and reservations.
finops:
- name: Gingr Finops
  service_category: Vertical SaaS - Pet Care Business Management
  slug: gingr-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/gingr.png
layout: provider
modified: '2026-07-04'
name: Gingr
nav: Providers
network: true
overview: 'Gingr publishes 9 APIs on the [APIs.io](https://apis.io/) network, including Invoices API, Owners API, Payments API, and 6 more. Tagged areas include Pet Care, Pet Daycare, Boarding, Grooming, and Vertical SaaS.


  Gingr''s developer surface includes authentication, documentation, engineering blog, and 7 more developer resources.'
plans:
- name: Gingr Plans Pricing
  plan_count: 4
  slug: gingr-plans-pricing
random_paper: 10
rate_limits:
- limit_count: 3
  name: Gingr Rate Limits
  slug: gingr-rate-limits
score:
  band: thin
  composite: 35.0
  coverage:
    artifact_dirs: 10
    catalog_earned: 64.0
    catalog_earned_first_party: 0.0
    catalog_gap: 51.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 39.5
    commercial_clarity: 39.5
    contract_governance: 0.0
    contract_quality: 53.9
    developer_ergonomics: 23.8
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 31.6
  previous_composite: 35.0
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 9
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 18.8
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/gingr/refs/heads/main/screenshots/gingr-2026-07-25T215825.png
security:
- kind: authentication
  name: Gingr Authentication
  slug: gingr-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Gingr Domain Security
  slug: gingr-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: gingr
tags:
- Pet Care
- Pet Daycare
- Boarding
- Grooming
- Vertical SaaS
- Scheduling
- Payments
website: https://www.gingrapp.com
---
