---
agent_readiness:
  band: agent-aware
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
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 12.9
  scored_at: '2026-10-17'
api_count: 11
apis:
- description: Explore available APIs and their documentation, including Reseller API and Customer API.
  name: SJ API
  slug: sj-api
- baseURL: https://login.microsoftonline.com
  baseurl_source: declared
  description: The Availabilities API from SJ — 2 operation(s) for availabilities.
  name: SJ Availabilities API
  slug: sj-se-availabilities-api
- baseURL: https://login.microsoftonline.com
  baseurl_source: declared
  description: The Booking API from SJ — 2 operation(s) for booking.
  name: SJ Booking API
  slug: sj-se-booking-api
- baseURL: https://login.microsoftonline.com
  baseurl_source: declared
  description: The Bookings API from SJ — 2 operation(s) for bookings.
  name: SJ Bookings API
  slug: sj-se-bookings-api
- baseURL: https://login.microsoftonline.com
  baseurl_source: declared
  description: The Contacts API from SJ — 1 operation(s) for contacts.
  name: SJ Contacts API
  slug: sj-se-contacts-api
- baseURL: https://login.microsoftonline.com
  baseurl_source: declared
  description: The Exchange Offers API from SJ — 1 operation(s) for exchange offers.
  name: SJ Exchange Offers API
  slug: sj-se-exchange-offers-api
- baseURL: https://login.microsoftonline.com
  baseurl_source: declared
  description: The Exchange Operations API from SJ — 1 operation(s) for exchange operations.
  name: SJ Exchange Operations API
  slug: sj-se-exchange-operations-api
- baseURL: https://login.microsoftonline.com
  baseurl_source: declared
  description: The Fulfillments API from SJ — 1 operation(s) for fulfillments.
  name: SJ Fulfillments API
  slug: sj-se-fulfillments-api
- baseURL: https://login.microsoftonline.com
  baseurl_source: declared
  description: The Offers API from SJ — 2 operation(s) for offers.
  name: SJ Offers API
  slug: sj-se-offers-api
- baseURL: https://login.microsoftonline.com
  baseurl_source: declared
  description: The Passenger API from SJ — 1 operation(s) for passenger.
  name: SJ Passenger API
  slug: sj-se-passenger-api
- baseURL: https://login.microsoftonline.com
  baseurl_source: declared
  description: The Tenant Id API from SJ — 1 operation(s) for tenant id.
  name: SJ Tenant Id API
  slug: sj-se-tenant-id-api
artifact_total: 20
common:
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/sj-se/refs/heads/main/rules/sj-se-rules.yml
  title: ''
  type: Spectral
  url: rules/sj-se-rules.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/sj-se/refs/heads/main/json-ld/sj-se-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/sj-se-context.jsonld
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/sj-se/refs/heads/main/vocabulary/sj-se-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/sj-se-vocabulary.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/sj-se/refs/heads/main/data-model/sj-se-data-model.yml
  title: ''
  type: DataModel
  url: data-model/sj-se-data-model.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/sj-se/refs/heads/main/conformance/sj-se-conformance.yml
  title: ''
  type: Conformance
  url: conformance/sj-se-conformance.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/sj-se/refs/heads/main/hosts/sj-se-hosts.yml
  title: ''
  type: Hosts
  url: hosts/sj-se-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/sj-se/refs/heads/main/vendors/sj-se-vendors.yml
  title: ''
  type: Vendors
  url: vendors/sj-se-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://developer.sj.se/terms-and-conditions
- group: operate
  title: ''
  type: StatusPage
  url: https://developer.sj.se/status
- group: docs
  title: ''
  type: Documentation
  url: https://developer.sj.se/
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/sj-se/refs/heads/main/security/sj-se-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/sj-se-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://sj.se/
coverage:
  detail: the company publishes no developer documentation host and no machine-readable contract on its own domain
  evidence:
  - status: 200
    url: https://sj.se/
  reason: no-developer-program
  state: none
created: '2026-10-15'
description: 'SJ is a company surfaced via the API Evangelist harvest backlog (source: stockholm-trip) and added to the network as a stub for full-pipeline profiling.'
json_schemas:
- name: PatchPassengerRequest
  property_count: 2
  slug: sj-se-patch-passenger-request
- name: PostBookingRequest
  property_count: 5
  slug: sj-se-post-booking-request
- name: PostBookingRequest2
  property_count: 3
  slug: sj-se-post-booking-request2
- name: PostContactsContactidResponse
  property_count: 2
  slug: sj-se-post-contacts-contactid-response
- name: PostOffersRequest
  property_count: 4
  slug: sj-se-post-offers-request
- name: PostOffersRequest2
  property_count: 4
  slug: sj-se-post-offers-request2
jsonld:
- class_count: 16
  name: Sj Se Context
  property_count: 21
  slug: sj-se-context
layout: provider
modified: '2026-10-15'
name: SJ
nav: Providers
network: true
overview: 'SJ is listed with 11 APIs on the [APIs.io](https://apis.io/) network, including Availabilities API, Booking API, Bookings API, and 8 more. Tagged areas include Company.


  The SJ catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  SJ''s developer surface includes documentation and 11 more developer resources.'
random_paper: 20
rules:
- authorship: generated
  effective_rule_count: 50
  extends:
  - spectral:oas
  name: SJ API Rules
  rule_count: 9
  severity_counts:
    error: 8
    hint: 0
    info: 1
    warn: 0
  slug: sj-se-rules
score:
  band: emerging
  composite: 17.9
  coverage:
    artifact_dirs: 12
    catalog_earned: 48.0
    catalog_earned_first_party: 0.0
    catalog_gap: 67.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 10.5
    contract_governance: 19.7
    contract_quality: 24.4
    developer_ergonomics: 9.5
    discoverability: 41.1
    operational_transparency: 15.8
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 11
      marker_coverage: 100.0
      total: 11
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 14.7
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: true
    score: 0.0
security:
- kind: domain-security
  name: Sj Se Domain Security
  slug: sj-se-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: sj-se
tags:
- Company
website: https://sj.se/
---
