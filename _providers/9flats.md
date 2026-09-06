---
agent_readiness:
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
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
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 5.0
  scored_at: '2026-09-05'
api_count: 1
apis:
- description: 'The 9flats read API over the marketplace''s listing data: search places, fetch a place with its photos, prices, reviews and monthly availability calendar, and fetch a user with their favourites and (fo'
  name: 9flats API
  slug: 9flats-api
artifact_total: 5
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/9flats-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.9flats.com
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/9flats
- group: build
  title: ''
  type: SourceCode
  url: https://github.com/9flats/nineflats-api
- group: build
  title: ''
  type: Packages
  url: packages/9flats-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/9flats-packages.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/9flats-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/9flats-conventions.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/9flats-data-model.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/9flats-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/9flats-lifecycle.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/9flats-rate-limits.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/9flats-plans-pricing.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/9flats-llms.txt
created: '2026-09-05'
description: '9flats is a European vacation-rental marketplace, founded in Hamburg, Germany in 2010, that lists privately-owned apartments, houses and rooms for short-term stays and takes bookings directly from travellers. It operates 9flats.com in multiple languages and, in 2016, combined with its Berlin-based competitor Wimdu. 9flats published a public read API (v1, later v3) covering place search, place detail, photos, prices, reviews, availability calendars, user profiles, favourites and bookings, authenticated with OAuth 1.0a and shipped with a first-party Ruby SDK. That developer surface has decayed: the SDK was last released in 2011 and is marked unsupported by its own maintainers, and the API reference site the SDK links to has been deleted.'
layout: provider
modified: '2026-09-05'
name: 9flats
nav: Providers
network: true
overview: '9flats publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Travel, Hospitality, Vacation Rentals, and Short-Term Rental.


  9flats'' developer surface includes authentication and 13 more developer resources.'
plans:
- name: 9Flats Plans Pricing
  plan_count: 0
  slug: 9flats-plans-pricing
random_paper: 7
rate_limits:
- limit_count: 0
  name: 9Flats Rate Limits
  slug: 9flats-rate-limits
score:
  band: emerging
  composite: 11.5
  coverage:
    artifact_dirs: 11
    catalog_earned: 35.0
    catalog_earned_first_party: 0.0
    catalog_gap: 80.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 4.5
    contract_quality: 0.0
    developer_ergonomics: 19.0
    discoverability: 64.8
    governance: 4.5
    operational_transparency: 5.3
  provenance:
    conformance: derived
  schema_version: 0.18.3
  scored_at: '2026-09-05'
security:
- kind: authentication
  name: 9Flats Authentication
  slug: 9flats-authentication
  summary_line: 2 schemes
- kind: domain-security
  name: 9Flats Domain Security
  slug: 9flats-domain-security
  summary_line: TLSv1.3 · DMARC
slug: 9flats
tags:
- Company
- Travel
- Hospitality
- Vacation Rentals
- Short-Term Rental
- Accommodation
- Marketplace
- Booking
- Europe
website: https://www.9flats.com
---
