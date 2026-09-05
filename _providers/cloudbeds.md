---
access_model:
  confidence: high
  label: Free · Self-serve signup
  onboarding: self-serve
  pricing: free
  public: false
  source:
  - plans
  - authentication
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
    delegated_identity: documented
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: documented
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 23.2
  scored_at: '2026-09-04'
agentic_access:
- acting_count: 13
  human_in_the_loop: 0
  name: Cloudbeds Agentic Access
  operation_count: 29
  slug: cloudbeds-agentic-access
  summary_line: 29 operations · 13 acting
api_count: 1
apis:
- description: Earlier supported version of the Cloudbeds REST API. New integrations should target v1.3.
  name: Cloudbeds REST API v1.2 (Legacy)
  slug: rest-api-v1-2
- description: GraphQL API offering a typed query interface for reservations, properties, and inventory alongside the REST API.
  name: Cloudbeds GraphQL API
  slug: graphql
- description: Event-driven webhooks for reservation, guest, room, and payment state changes. Use webhooks instead of polling list endpoints.
  name: Cloudbeds Webhooks
  slug: webhooks
- baseURL: https://hotels.cloudbeds.com/api/v1.3
  baseurl_source: declared
  description: The Access Token API from Cloudbeds — 1 operation(s) for access token.
  name: Cloudbeds Access Token API
  slug: cloudbeds-access-token-api
- baseURL: https://hotels.cloudbeds.com/api/v1.3
  baseurl_source: declared
  description: The DeleteWebhook API from Cloudbeds — 1 operation(s) for deletewebhook.
  name: Cloudbeds DeleteWebhook API
  slug: cloudbeds-deletewebhook-api
- baseURL: https://hotels.cloudbeds.com/api/v1.3
  baseurl_source: declared
  description: The GetAvailableRoomTypes API from Cloudbeds — 1 operation(s) for getavailableroomtypes.
  name: Cloudbeds GetAvailableRoomTypes API
  slug: cloudbeds-getavailableroomtypes-api
- baseURL: https://hotels.cloudbeds.com/api/v1.3
  baseurl_source: declared
  description: The GetDashboard API from Cloudbeds — 1 operation(s) for getdashboard.
  name: Cloudbeds GetDashboard API
  slug: cloudbeds-getdashboard-api
- baseURL: https://hotels.cloudbeds.com/api/v1.3
  baseurl_source: declared
  description: The GetGuest API from Cloudbeds — 1 operation(s) for getguest.
  name: Cloudbeds GetGuest API
  slug: cloudbeds-getguest-api
- baseURL: https://hotels.cloudbeds.com/api/v1.3
  baseurl_source: declared
  description: The GetGuestList API from Cloudbeds — 1 operation(s) for getguestlist.
  name: Cloudbeds GetGuestList API
  slug: cloudbeds-getguestlist-api
- baseURL: https://hotels.cloudbeds.com/api/v1.3
  baseurl_source: declared
  description: The GetHotelDetails API from Cloudbeds — 1 operation(s) for gethoteldetails.
  name: Cloudbeds GetHotelDetails API
  slug: cloudbeds-gethoteldetails-api
- baseURL: https://hotels.cloudbeds.com/api/v1.3
  baseurl_source: declared
  description: The GetHotels API from Cloudbeds — 1 operation(s) for gethotels.
  name: Cloudbeds GetHotels API
  slug: cloudbeds-gethotels-api
- baseURL: https://hotels.cloudbeds.com/api/v1.3
  baseurl_source: declared
  description: The GetPaymentMethods API from Cloudbeds — 1 operation(s) for getpaymentmethods.
  name: Cloudbeds GetPaymentMethods API
  slug: cloudbeds-getpaymentmethods-api
- baseURL: https://hotels.cloudbeds.com/api/v1.3
  baseurl_source: declared
  description: The GetRate API from Cloudbeds — 1 operation(s) for getrate.
  name: Cloudbeds GetRate API
  slug: cloudbeds-getrate-api
- baseURL: https://hotels.cloudbeds.com/api/v1.3
  baseurl_source: declared
  description: The GetRatePlans API from Cloudbeds — 1 operation(s) for getrateplans.
  name: Cloudbeds GetRatePlans API
  slug: cloudbeds-getrateplans-api
- baseURL: https://hotels.cloudbeds.com/api/v1.3
  baseurl_source: declared
  description: The GetReservation API from Cloudbeds — 1 operation(s) for getreservation.
  name: Cloudbeds GetReservation API
  slug: cloudbeds-getreservation-api
- baseURL: https://hotels.cloudbeds.com/api/v1.3
  baseurl_source: declared
  description: The GetReservations API from Cloudbeds — 1 operation(s) for getreservations.
  name: Cloudbeds GetReservations API
  slug: cloudbeds-getreservations-api
- baseURL: https://hotels.cloudbeds.com/api/v1.3
  baseurl_source: declared
  description: The GetRooms API from Cloudbeds — 1 operation(s) for getrooms.
  name: Cloudbeds GetRooms API
  slug: cloudbeds-getrooms-api
- baseURL: https://hotels.cloudbeds.com/api/v1.3
  baseurl_source: declared
  description: The GetRoomTypes API from Cloudbeds — 1 operation(s) for getroomtypes.
  name: Cloudbeds GetRoomTypes API
  slug: cloudbeds-getroomtypes-api
- baseURL: https://hotels.cloudbeds.com/api/v1.3
  baseurl_source: declared
  description: The GetUsers API from Cloudbeds — 1 operation(s) for getusers.
  name: Cloudbeds GetUsers API
  slug: cloudbeds-getusers-api
- baseURL: https://hotels.cloudbeds.com/api/v1.3
  baseurl_source: declared
  description: The GetWebhooks API from Cloudbeds — 1 operation(s) for getwebhooks.
  name: Cloudbeds GetWebhooks API
  slug: cloudbeds-getwebhooks-api
- baseURL: https://hotels.cloudbeds.com/api/v1.3
  baseurl_source: declared
  description: The PostCharge API from Cloudbeds — 1 operation(s) for postcharge.
  name: Cloudbeds PostCharge API
  slug: cloudbeds-postcharge-api
- baseURL: https://hotels.cloudbeds.com/api/v1.3
  baseurl_source: declared
  description: The PostGuest API from Cloudbeds — 1 operation(s) for postguest.
  name: Cloudbeds PostGuest API
  slug: cloudbeds-postguest-api
- baseURL: https://hotels.cloudbeds.com/api/v1.3
  baseurl_source: declared
  description: The PostPayment API from Cloudbeds — 1 operation(s) for postpayment.
  name: Cloudbeds PostPayment API
  slug: cloudbeds-postpayment-api
- baseURL: https://hotels.cloudbeds.com/api/v1.3
  baseurl_source: declared
  description: The PostReservation API from Cloudbeds — 1 operation(s) for postreservation.
  name: Cloudbeds PostReservation API
  slug: cloudbeds-postreservation-api
- baseURL: https://hotels.cloudbeds.com/api/v1.3
  baseurl_source: declared
  description: The PostRoomAssign API from Cloudbeds — 1 operation(s) for postroomassign.
  name: Cloudbeds PostRoomAssign API
  slug: cloudbeds-postroomassign-api
- baseURL: https://hotels.cloudbeds.com/api/v1.3
  baseurl_source: declared
  description: The PostRoomCheckIn API from Cloudbeds — 1 operation(s) for postroomcheckin.
  name: Cloudbeds PostRoomCheckIn API
  slug: cloudbeds-postroomcheckin-api
- baseURL: https://hotels.cloudbeds.com/api/v1.3
  baseurl_source: declared
  description: The PostRoomCheckOut API from Cloudbeds — 1 operation(s) for postroomcheckout.
  name: Cloudbeds PostRoomCheckOut API
  slug: cloudbeds-postroomcheckout-api
- baseURL: https://hotels.cloudbeds.com/api/v1.3
  baseurl_source: declared
  description: The PostWebhook API from Cloudbeds — 1 operation(s) for postwebhook.
  name: Cloudbeds PostWebhook API
  slug: cloudbeds-postwebhook-api
- baseURL: https://hotels.cloudbeds.com/api/v1.3
  baseurl_source: declared
  description: The PutGuest API from Cloudbeds — 1 operation(s) for putguest.
  name: Cloudbeds PutGuest API
  slug: cloudbeds-putguest-api
- baseURL: https://hotels.cloudbeds.com/api/v1.3
  baseurl_source: declared
  description: The PutRate API from Cloudbeds — 1 operation(s) for putrate.
  name: Cloudbeds PutRate API
  slug: cloudbeds-putrate-api
- baseURL: https://hotels.cloudbeds.com/api/v1.3
  baseurl_source: declared
  description: The PutReservation API from Cloudbeds — 1 operation(s) for putreservation.
  name: Cloudbeds PutReservation API
  slug: cloudbeds-putreservation-api
- baseURL: https://hotels.cloudbeds.com/api/v1.3
  baseurl_source: declared
  description: The Userinfo API from Cloudbeds — 1 operation(s) for userinfo.
  name: Cloudbeds Userinfo API
  slug: cloudbeds-userinfo-api
artifact_total: 82
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Cloudbeds REST API v1.3 Access Token API
  slug: open-cloudbeds-access-token-api
- collection_type: open
  name: Cloudbeds REST API v1.3 Access Token DeleteWebhook API
  slug: open-cloudbeds-deletewebhook-api
- collection_type: open
  name: Cloudbeds REST API v1.3 Access Token GetAvailableRoomTypes API
  slug: open-cloudbeds-getavailableroomtypes-api
- collection_type: open
  name: Cloudbeds REST API v1.3 Access Token GetDashboard API
  slug: open-cloudbeds-getdashboard-api
- collection_type: open
  name: Cloudbeds REST API v1.3 Access Token GetGuest API
  slug: open-cloudbeds-getguest-api
- collection_type: open
  name: Cloudbeds REST API v1.3 Access Token GetGuestList API
  slug: open-cloudbeds-getguestlist-api
- collection_type: open
  name: Cloudbeds REST API v1.3 Access Token GetHotelDetails API
  slug: open-cloudbeds-gethoteldetails-api
- collection_type: open
  name: Cloudbeds REST API v1.3 Access Token GetHotels API
  slug: open-cloudbeds-gethotels-api
- collection_type: open
  name: Cloudbeds REST API v1.3 Access Token GetPaymentMethods API
  slug: open-cloudbeds-getpaymentmethods-api
- collection_type: open
  name: Cloudbeds REST API v1.3 Access Token GetRate API
  slug: open-cloudbeds-getrate-api
- collection_type: open
  name: Cloudbeds REST API v1.3 Access Token GetRatePlans API
  slug: open-cloudbeds-getrateplans-api
- collection_type: open
  name: Cloudbeds REST API v1.3 Access Token GetReservation API
  slug: open-cloudbeds-getreservation-api
- collection_type: open
  name: Cloudbeds REST API v1.3 Access Token GetReservations API
  slug: open-cloudbeds-getreservations-api
- collection_type: open
  name: Cloudbeds REST API v1.3 Access Token GetRooms API
  slug: open-cloudbeds-getrooms-api
- collection_type: open
  name: Cloudbeds REST API v1.3 Access Token GetRoomTypes API
  slug: open-cloudbeds-getroomtypes-api
- collection_type: open
  name: Cloudbeds REST API v1.3 Access Token GetUsers API
  slug: open-cloudbeds-getusers-api
- collection_type: open
  name: Cloudbeds REST API v1.3 Access Token GetWebhooks API
  slug: open-cloudbeds-getwebhooks-api
- collection_type: open
  name: Cloudbeds REST API v1.3 Access Token PostCharge API
  slug: open-cloudbeds-postcharge-api
- collection_type: open
  name: Cloudbeds REST API v1.3 Access Token PostGuest API
  slug: open-cloudbeds-postguest-api
- collection_type: open
  name: Cloudbeds REST API v1.3 Access Token PostPayment API
  slug: open-cloudbeds-postpayment-api
- collection_type: open
  name: Cloudbeds REST API v1.3 Access Token PostReservation API
  slug: open-cloudbeds-postreservation-api
- collection_type: open
  name: Cloudbeds REST API v1.3 Access Token PostRoomAssign API
  slug: open-cloudbeds-postroomassign-api
- collection_type: open
  name: Cloudbeds REST API v1.3 Access Token PostRoomCheckIn API
  slug: open-cloudbeds-postroomcheckin-api
- collection_type: open
  name: Cloudbeds REST API v1.3 Access Token PostRoomCheckOut API
  slug: open-cloudbeds-postroomcheckout-api
- collection_type: open
  name: Cloudbeds REST API v1.3 Access Token PostWebhook API
  slug: open-cloudbeds-postwebhook-api
- collection_type: open
  name: Cloudbeds REST API v1.3 Access Token PutGuest API
  slug: open-cloudbeds-putguest-api
- collection_type: open
  name: Cloudbeds REST API v1.3 Access Token PutRate API
  slug: open-cloudbeds-putrate-api
- collection_type: open
  name: Cloudbeds REST API v1.3 Access Token PutReservation API
  slug: open-cloudbeds-putreservation-api
- collection_type: open
  name: Cloudbeds REST API v1.3 Access Token Userinfo API
  slug: open-cloudbeds-userinfo-api
- collection_type: open
  name: Cloudbeds REST API v1.3
  slug: open-cloudbeds
common:
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/cloudbeds-capability-edges.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/cloudbeds-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/cloudbeds-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/cloudbeds-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/cloudbeds-scopes.yml
- group: company
  title: ''
  type: Blog
  url: https://www.cloudbeds.com/feed/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/cloudbeds
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/cloudbeds
- group: company
  title: ''
  type: Website
  url: https://www.cloudbeds.com/
- group: other
  title: ''
  type: Developer
  url: https://developers.cloudbeds.com/
- group: commercial
  title: ''
  type: Plans
  url: plans/cloudbeds-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/cloudbeds-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/cloudbeds-finops.yml
- group: agent
  title: ''
  type: LlmsText
  url: https://developers.cloudbeds.com/llms.txt
- group: design
  title: ''
  type: SpectralRules
  url: rules/cloudbeds-rules.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/cloudbeds-vocabulary.yml
created: '2026-05-08'
description: Cloudbeds is a San Diego-based hospitality management platform for small and mid-size independent hotels, hostels, and groups, offering PMS, channel manager, booking engine, payments, and a marketplace of integrations. Cloudbeds publishes a public REST API (v1.2 and v1.3), a GraphQL API, blueprints, and webhooks for reservations, guests, rooms, rates, payments, and events.
examples:
- key_count: 19
  name: Cloudbeds Guest Example
  slug: cloudbeds-guest-example
- key_count: 11
  name: Cloudbeds Rate Plan Example
  slug: cloudbeds-rate-plan-example
- key_count: 18
  name: Cloudbeds Reservation Example
  slug: cloudbeds-reservation-example
finops:
- name: Cloudbeds Finops
  service_category: Hospitality
  slug: cloudbeds-finops
graphqls:
- description: GraphQL API offering a typed query interface for reservations, properties, and inventory alongside the REST API.
  name: Cloudbeds GraphQL API
  slug: cloudbeds-graphql
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/cloudbeds.png
json_schemas:
- name: Cloudbeds Guest
  property_count: 19
  slug: cloudbeds-guest
- name: Cloudbeds Rate Plan
  property_count: 12
  slug: cloudbeds-rate-plan
- name: Cloudbeds Reservation
  property_count: 18
  slug: cloudbeds-reservation
json_structures:
- name: Cloudbeds Guest Structure
  property_count: 0
  slug: cloudbeds-guest-structure
- name: Cloudbeds Reservation Structure
  property_count: 0
  slug: cloudbeds-reservation-structure
jsonld:
- class_count: 32
  name: Cloudbeds Context
  property_count: 14
  slug: cloudbeds-context
layout: provider
modified: '2026-05-24'
name: Cloudbeds
nav: Providers
network: true
overview: 'Cloudbeds publishes 29 APIs on the [APIs.io](https://apis.io/) network, including Access Token API, DeleteWebhook API, GetAvailableRoomTypes API, and 26 more. Tagged areas include Hospitality, Hotels, PMS, Property Management, and Channel Manager.


  The Cloudbeds catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Cloudbeds'' developer surface includes authentication, engineering blog, and 14 more developer resources.'
plans:
- name: Cloudbeds Plans Pricing
  plan_count: 2
  slug: cloudbeds-plans-pricing
random_paper: 4
rate_limits:
- limit_count: 1
  name: Cloudbeds Rate Limits
  slug: cloudbeds-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: Cloudbeds API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: cloudbeds-jsonschema-spectral-rules
- effective_rule_count: 0
  extends: []
  name: Cloudbeds API Rules
  rule_count: 0
  severity_counts:
    error: 0
    hint: 0
    info: 0
    warn: 0
  slug: cloudbeds-rules
scopes:
- name: Cloudbeds Scopes
  scope_count: 2
  slug: cloudbeds-scopes
  summary_line: 2 scopes · authorizationCode
score:
  band: thin
  composite: 33.7
  coverage:
    artifact_dirs: 20
    catalog_earned: 65.3
    catalog_earned_first_party: 0.0
    catalog_gap: 49.8
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 13.2
    commercial_clarity: 13.2
    contract_governance: 25.0
    contract_quality: 62.6
    developer_ergonomics: 19.0
    discoverability: 61.1
    governance: 25.0
    operational_transparency: 7.9
  previous_composite: 33.7
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 29
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 42.2
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
security:
- kind: authentication
  name: Cloudbeds Authentication
  slug: cloudbeds-authentication
  summary_line: apiKey/oauth2 · 2 schemes
- kind: domain-security
  name: Cloudbeds Domain Security
  slug: cloudbeds-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: cloudbeds
tags:
- Hospitality
- Hotels
- PMS
- Property Management
- Channel Manager
- Booking Engine
- Payments
website: https://www.cloudbeds.com/
---
