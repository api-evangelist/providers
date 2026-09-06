---
access_model:
  confidence: medium
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  - security
  trial: false
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
    event_surface_described: true
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 25.8
  scored_at: '2026-09-05'
agentic_access:
- acting_count: 35
  human_in_the_loop: 0
  name: Tito Agentic Access
  operation_count: 57
  slug: tito-agentic-access
  summary_line: 57 operations · 35 acting
api_count: 1
apis:
- baseURL: https://api.tito.io/v3
  baseurl_source: declared
  description: Authentication check and account discovery.
  name: Tito Account API
  slug: tito-account-api
- baseURL: https://api.tito.io/v3
  baseurl_source: declared
  description: Capacity-bound sessions releases can attach to.
  name: Tito Activities API
  slug: tito-activities-api
- baseURL: https://api.tito.io/v3
  baseurl_source: declared
  description: Lists defining which tickets can be checked in.
  name: Tito Check-in Lists API
  slug: tito-check-in-lists-api
- baseURL: https://api.tito.io/v3
  baseurl_source: declared
  description: Percentage or fixed discounts applied at checkout.
  name: Tito Discount Codes API
  slug: tito-discount-codes-api
- baseURL: https://api.tito.io/v3
  baseurl_source: declared
  description: Events that tickets are sold for.
  name: Tito Events API
  slug: tito-events-api
- baseURL: https://api.tito.io/v3
  baseurl_source: declared
  description: Refund records against registrations.
  name: Tito Refunds API
  slug: tito-refunds-api
- baseURL: https://api.tito.io/v3
  baseurl_source: declared
  description: Orders that group one or more tickets.
  name: Tito Registrations API
  slug: tito-registrations-api
- baseURL: https://api.tito.io/v3
  baseurl_source: declared
  description: Ticket types (releases) for an event.
  name: Tito Releases API
  slug: tito-releases-api
- baseURL: https://api.tito.io/v3
  baseurl_source: declared
  description: Individual tickets held by attendees.
  name: Tito Tickets API
  slug: tito-tickets-api
- baseURL: https://api.tito.io/v3
  baseurl_source: declared
  description: Endpoints Tito POSTs event notifications to.
  name: Tito Webhook Endpoints API
  slug: tito-webhook-endpoints-api
- baseURL: https://api.tito.io/v3
  baseurl_source: declared
  description: The Tito Admin API API from Tito — 0 operation(s) for tito admin api.
  name: Tito Tito Admin API
  slug: tito-tito-admin-api-api
artifact_total: 29
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Tito Admin Account API
  slug: open-tito-account-api
- collection_type: open
  name: Tito Admin Account Activities API
  slug: open-tito-activities-api
- collection_type: open
  name: Tito Admin Account Check-in Lists API
  slug: open-tito-check-in-lists-api
- collection_type: open
  name: Tito Admin Account Discount Codes API
  slug: open-tito-discount-codes-api
- collection_type: open
  name: Tito Admin Account Events API
  slug: open-tito-events-api
- collection_type: open
  name: Tito Admin Account Refunds API
  slug: open-tito-refunds-api
- collection_type: open
  name: Tito Admin Account Registrations API
  slug: open-tito-registrations-api
- collection_type: open
  name: Tito Admin Account Releases API
  slug: open-tito-releases-api
- collection_type: open
  name: Tito Admin Account Tickets API
  slug: open-tito-tickets-api
- collection_type: open
  name: Tito Admin Account Webhook Endpoints API
  slug: open-tito-webhook-endpoints-api
- collection_type: open
  name: Tito Admin API
  slug: open-tito
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/tito-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/tito-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/tito-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/teamtito
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/usetito
- group: company
  title: ''
  type: Website
  url: https://ti.to
- group: docs
  title: ''
  type: Documentation
  url: https://ti.to/docs/api
- group: commercial
  title: ''
  type: Plans
  url: plans/tito-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/tito-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/tito-finops.yml
- group: company
  title: ''
  type: Blog
  url: https://blog.tito.io/
created: '2026-07-12'
description: Tito (ti.to) is an event registration and ticketing platform from Team Tito in Dublin, Ireland, used to sell tickets, collect registrations, and check in attendees for conferences and events. Organizers can sell through Tito-hosted event pages or an embeddable widget. The Admin API is a REST/JSON interface at https://api.tito.io/v3 for managing accounts, events, releases (ticket types), tickets, registrations, discount codes, activities, check-in lists, and refunds, authenticated with a secret API token. Tito also emits outbound webhooks for ticket, registration, check-in, and interested-user events, and exposes a separate unauthenticated Check-in API.
finops:
- name: Tito Finops
  service_category: Event Ticketing and Registration
  slug: tito-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/tito.png
layout: provider
modified: '2026-07-12'
name: Tito
nav: Providers
network: true
overview: 'Tito publishes 11 APIs on the [APIs.io](https://apis.io/) network, including Account API, Activities API, Check-in Lists API, and 8 more. Tagged areas include Event Ticketing, Event, Registration, Ticketing, and Conferences.


  Tito''s developer surface includes authentication, documentation, engineering blog, and 8 more developer resources.'
plans:
- name: Tito Plans Pricing
  plan_count: 3
  slug: tito-plans-pricing
random_paper: 7
rate_limits:
- limit_count: 2
  name: Tito Rate Limits
  slug: tito-rate-limits
score:
  band: emerging
  composite: 24.3
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
    contract_quality: 0.0
    developer_ergonomics: 32.1
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 23.7
  previous_composite: 24.3
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 11
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/tito/refs/heads/main/screenshots/tito-2026-09-02T163823.png
security:
- kind: authentication
  name: Tito Authentication
  slug: tito-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Tito Domain Security
  slug: tito-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: tito
tags:
- Event Ticketing
- Event
- Registration
- Ticketing
- Conferences
- Event Management
- Attendees
- Webhook
- Software-as-a-Service
website: https://ti.to
---
