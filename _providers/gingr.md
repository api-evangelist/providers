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
    mcp_tool_quality: na
    openapi_examples: verified
    operation_distinctiveness: distinct
    pagination_ratio: partial
    protected_resource_metadata: false
    rate_limit_signal: derived
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 27.1
  scored_at: '2026-11-06'
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
  description: Booking Type Rates
  name: Gingr Booking Type Rates API
  slug: gingr-booking-type-rates-api
- baseURL: https://api.gingr.io/v1
  baseurl_source: declared
  description: The **Bookings** group is the core of the Gingr API. A **Booking** (also called a Reservation internally) represents a scheduled service for one or more animals at a specific location and time. The ty
  name: Gingr Bookings API
  slug: gingr-bookings-api
- baseURL: https://api.gingr.io/v1
  baseurl_source: declared
  description: The **Card On File** group manages saved payment methods for a parent. Gingr stores tokenized card details through its payment gateway integration — raw card numbers are never stored or transmitted th
  name: Gingr Card On File API
  slug: gingr-card-on-file-api
- baseURL: https://api.gingr.io/v1
  baseurl_source: declared
  description: The **Config** group exposes read and write endpoints for all organization-level configuration data in Gingr. This includes the lookup tables and settings that everything else depends on — species, br
  name: Gingr Config API
  slug: gingr-config-api
- baseURL: https://api.gingr.io/v1
  baseurl_source: declared
  description: The **Group Classes** group manages enrollment in structured group training and activity sessions. Unlike individual bookings, group classes have a fixed schedule, a capacity limit, and a roster of en
  name: Gingr Group Classes API
  slug: gingr-group-classes-api
- baseURL: https://api.gingr.io/v1
  baseurl_source: declared
  description: The **Parents** group covers everything related to the pet owner — referred to as a **Parent** in Gingr. A Parent is the primary account holder who owns one or more animals and makes bookings. Use thi
  name: Gingr Parents API
  slug: gingr-parents-api
- baseURL: https://api.gingr.io/v1
  baseurl_source: declared
  description: Payment
  name: Gingr Payment API
  slug: gingr-payment-api
- baseURL: https://api.gingr.io/v1
  baseurl_source: declared
  description: The **Precheck** group handles the digital pre-check-in process for bookings. A pre-check collects animal care instructions — feeding, medications, behavioral notes, and custom form answers — before t
  name: Gingr Precheck API
  slug: gingr-precheck-api
- baseURL: https://api.gingr.io/v1
  baseurl_source: declared
  description: The **Upload** group provides endpoints for attaching files to parent and pet records. Supported file types include images (profile photos) and documents (vaccination certificates, signed waivers, etc
  name: Gingr Upload API
  slug: gingr-upload-api
artifact_total: 29
collections:
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
- group: other
  href: https://artifacts.apis.io/gingr/capabilities/gingr-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/gingr-capability-edges.yml
- group: agent
  href: https://artifacts.apis.io/gingr/agentic-access/gingr-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/gingr-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/gingr/security/gingr-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/gingr-domain-security.yml
- group: auth
  href: https://artifacts.apis.io/gingr/authentication/gingr-authentication.yml
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
  href: https://artifacts.apis.io/gingr/plans/gingr-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/gingr-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/gingr/rate-limits/gingr-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/gingr-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/gingr/finops/gingr-finops.yml
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
- has_sources: true
  method: generated
  name: Gingr Finops
  primary_unit: ''
  service_category: Vertical SaaS - Pet Care Business Management
  slug: gingr-finops
  template: false
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/gingr.png
layout: provider
modified: '2026-07-04'
name: Gingr
nav: Providers
network: true
overview: 'Gingr publishes 12 API contracts indexed on the [APIs.io](https://apis.io/) network, including Invoices API, Payments API, Pets API, and 9 more. Tagged areas include Pet Care, Pet Daycare, Boarding, Grooming, and Vertical SaaS.


  The Gingr catalog on APIs.io includes 1 Spectral governance ruleset.


  Gingr''s developer surface includes authentication, documentation, engineering blog, and 8 more developer resources.'
plans:
- name: Gingr Plans Pricing
  plan_count: 4
  slug: gingr-plans-pricing
random_paper: 7
rate_limits:
- limit_count: 3
  name: Gingr Rate Limits
  slug: gingr-rate-limits
rules:
- authorship: generated
  effective_rule_count: 89
  extends:
  - spectral:oas
  name: Gingr API Rules
  rule_count: 48
  severity_counts:
    error: 41
    hint: 0
    info: 1
    warn: 6
  slug: gingr-rules
score:
  band: thin
  composite: 26.3
  coverage:
    artifact_dirs: 17
    catalog_earned: 47.5
    catalog_earned_first_party: 0.0
    catalog_gap: 67.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.7
  facets:
    access_clarity: 7.9
    contract_governance: 13.6
    contract_quality: 50.9
    developer_ergonomics: 23.8
    discoverability: 66.1
    operational_transparency: 7.9
  previous_composite: 25.6
  provenance:
    agentic_access: derived
    contracts:
      callable: 45.5
      derived: 0
      marker_coverage: 54.5
      total: 22
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 10.7
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/gingr/gingr-2026-07-25T215825.png
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
