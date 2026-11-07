---
access_model:
  confidence: medium
  gated: none
  gated_source:
  - onboarding
  label: Freemium (free trial) · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  - security
  trial: true
  try_now: true
agent_readiness:
  band: agent-native
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: verified
    event_surface_described: false
    idempotency: verified
    mcp_server: verified
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: mostly
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: derived
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 56.5
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 17
  human_in_the_loop: 0
  name: Apaleo Agentic Access
  operation_count: 41
  slug: apaleo-agentic-access
  summary_line: 41 operations · 17 acting
api_count: 2
apis:
- baseURL: https://api.apaleo.com/booking/v1
  baseurl_source: declared
  description: Real-time availability for units, unit groups, and services.
  name: apaleo Availability API
  slug: apaleo-availability-api
- baseURL: https://api.apaleo.com/booking/v1
  baseurl_source: declared
  description: Bookings, reservations, blocks, groups, and offers.
  name: apaleo Booking API
  slug: apaleo-booking-api
- baseURL: https://api.apaleo.com/booking/v1
  baseurl_source: declared
  description: Folios, payments, refunds, invoices, and accounts.
  name: apaleo Finance API
  slug: apaleo-finance-api
- baseURL: https://api.apaleo.com/booking/v1
  baseurl_source: declared
  description: Properties, units, unit groups, and unit attributes.
  name: apaleo Inventory API
  slug: apaleo-inventory-api
- baseURL: https://api.apaleo.com/booking/v1
  baseurl_source: declared
  description: Rate plans, rates, services, and policies.
  name: apaleo Rate Plan API
  slug: apaleo-rate-plan-api
- baseURL: https://api.apaleo.com/booking/v1
  baseurl_source: declared
  description: Account- and property-level configuration.
  name: apaleo Settings API
  slug: apaleo-settings-api
- baseURL: https://api.apaleo.com/booking/v1
  baseurl_source: declared
  description: The Authorization API from apaleo — 6 operation(s) for authorization.
  name: apaleo Authorization API
  slug: apaleo-authorization-api
- baseURL: https://api.apaleo.com/booking/v1
  baseurl_source: declared
  description: The AuthorizationActions API from apaleo — 5 operation(s) for authorizationactions.
  name: apaleo Authorization Actions API
  slug: apaleo-authorizationactions-api
- baseURL: https://api.apaleo.com/booking/v1
  baseurl_source: declared
  description: The Block API from apaleo — 4 operation(s) for block.
  name: apaleo Block API
  slug: apaleo-block-api
- baseURL: https://api.apaleo.com/booking/v1
  baseurl_source: declared
  description: The BlockActions API from apaleo — 8 operation(s) for blockactions.
  name: apaleo Block Actions API
  slug: apaleo-blockactions-api
- baseURL: https://api.apaleo.com/booking/v1
  baseurl_source: declared
  description: The Group API from apaleo — 4 operation(s) for group.
  name: apaleo Group API
  slug: apaleo-group-api
- baseURL: https://api.apaleo.com/booking/v1
  baseurl_source: declared
  description: The GroupActions API from apaleo — 1 operation(s) for groupactions.
  name: apaleo Group Actions API
  slug: apaleo-groupactions-api
- baseURL: https://api.apaleo.com/booking/v1
  baseurl_source: declared
  description: The Offer API from apaleo — 5 operation(s) for offer.
  name: apaleo Offer API
  slug: apaleo-offer-api
- baseURL: https://api.apaleo.com/booking/v1
  baseurl_source: declared
  description: The PaymentAccountActions API from apaleo — 5 operation(s) for paymentaccountactions.
  name: apaleo Payment Account Actions API
  slug: apaleo-paymentaccountactions-api
- baseURL: https://api.apaleo.com/booking/v1
  baseurl_source: declared
  description: The Reservation API from apaleo — 6 operation(s) for reservation.
  name: apaleo Reservation API
  slug: apaleo-reservation-api
- baseURL: https://api.apaleo.com/booking/v1
  baseurl_source: declared
  description: The ReservationActions API from apaleo — 19 operation(s) for reservationactions.
  name: apaleo Reservation Actions API
  slug: apaleo-reservationactions-api
- baseURL: https://api.apaleo.com/booking/v1
  baseurl_source: declared
  description: The Types API from apaleo — 2 operation(s) for types.
  name: apaleo Types API
  slug: apaleo-types-api
- baseURL: https://api.apaleo.com/booking/v1
  baseurl_source: declared
  description: The Payment Account API from apaleo — 8 operation(s) for payment account.
  name: apaleo Payment Account API
  slug: apaleo-payment-account-api
artifact_total: 34
collections:
- collection_type: open
  name: apaleo Platform Availability API
  slug: open-apaleo-availability-api
- collection_type: open
  name: apaleo Platform Availability Booking API
  slug: open-apaleo-booking-api
- collection_type: open
  name: apaleo Platform Availability Finance API
  slug: open-apaleo-finance-api
- collection_type: open
  name: apaleo Platform Availability Inventory API
  slug: open-apaleo-inventory-api
- collection_type: open
  name: apaleo Platform Availability Rate Plan API
  slug: open-apaleo-rate-plan-api
- collection_type: open
  name: apaleo Platform Availability Settings API
  slug: open-apaleo-settings-api
- collection_type: open
  name: apaleo Platform API
  slug: open-apaleo
common:
- group: other
  href: https://artifacts.apis.io/apaleo/capabilities/apaleo-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/apaleo-capability-edges.yml
- group: agent
  href: https://artifacts.apis.io/apaleo/agentic-access/apaleo-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/apaleo-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/apaleo/security/apaleo-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/apaleo-domain-security.yml
- group: auth
  href: https://artifacts.apis.io/apaleo/authentication/apaleo-authentication.yml
  title: ''
  type: Authentication
  url: authentication/apaleo-authentication.yml
- group: auth
  href: https://artifacts.apis.io/apaleo/scopes/apaleo-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/apaleo-scopes.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/apaleo
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/apaleo
- group: company
  title: ''
  type: Website
  url: https://www.apaleo.com
- group: docs
  title: ''
  type: Documentation
  url: https://apaleo.dev
- group: commercial
  href: https://artifacts.apis.io/apaleo/plans/apaleo-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/apaleo-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/apaleo/rate-limits/apaleo-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/apaleo-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/apaleo/finops/apaleo-finops.yml
  title: ''
  type: FinOps
  url: finops/apaleo-finops.yml
- group: company
  title: ''
  type: Blog
  url: https://apaleo.com/blog/home
created: '2026-06-25'
description: apaleo is an API-first cloud hotel property-management system (PMS) and platform. Every capability - reservations, bookings, blocks, inventory, rate plans, availability, and finance - is exposed through documented REST APIs secured with OAuth 2.0, published as OpenAPI, with webhooks for real-time events, enabling an open marketplace of integrations.
finops:
- has_sources: true
  method: generated
  name: Apaleo Finops
  primary_unit: ''
  service_category: Hospitality and Property Management
  slug: apaleo-finops
  template: false
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/apaleo.png
layout: provider
mcp_servers:
- description: Remote MCP server at mcp.apaleo.com over HTTP.
  name: apaleo MCP Server
  slug: apaleo
modified: '2026-06-25'
name: apaleo
nav: Providers
network: true
overview: 'apaleo publishes 18 API contracts indexed on the [APIs.io](https://apis.io/) network, including Availability API, Booking API, Finance API, and 15 more. Tagged areas include Hospitality, PMS, Property Management, Hotels, and API-First.


  The apaleo catalog on APIs.io includes 1 Spectral governance ruleset.


  apaleo''s developer surface includes authentication, documentation, engineering blog, and 10 more developer resources.'
plans:
- name: Apaleo Plans Pricing
  plan_count: 3
  slug: apaleo-plans-pricing
random_paper: 2
rate_limits:
- limit_count: 2
  name: Apaleo Rate Limits
  slug: apaleo-rate-limits
rules:
- authorship: generated
  effective_rule_count: 104
  extends:
  - spectral:oas
  name: apaleo API Rules
  rule_count: 63
  severity_counts:
    error: 50
    hint: 0
    info: 4
    warn: 9
  slug: apaleo-rules
scopes:
- name: Apaleo Scopes
  scope_count: 10
  slug: apaleo-scopes
  summary_line: 10 scopes · clientCredentials/authorizationCode
score:
  band: thin
  composite: 28.6
  coverage:
    artifact_dirs: 20
    catalog_earned: 46.5
    catalog_earned_first_party: 0.0
    catalog_gap: 68.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -0.2
  facets:
    access_clarity: 7.9
    contract_governance: 13.6
    contract_quality: 44.2
    developer_ergonomics: 31.0
    discoverability: 68.3
    operational_transparency: 7.9
  previous_composite: 28.8
  provenance:
    agentic_access: derived
    contracts:
      callable: 52.0
      derived: 0
      marker_coverage: 0.0
      total: 25
    mcp: first-party
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 21.6
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/apaleo/apaleo-2026-07-25T200530.png
security:
- kind: authentication
  name: Apaleo Authentication
  slug: apaleo-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Apaleo Domain Security
  slug: apaleo-domain-security
  summary_line: TLSv1.2 · HSTS · DMARC
slug: apaleo
tags:
- Hospitality
- PMS
- Property Management
- Hotels
- API-First
website: https://www.apaleo.com
---
