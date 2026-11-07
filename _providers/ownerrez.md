---
access_model:
  confidence: high
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
  - scopes
  - security
  trial: true
  try_now: true
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: negotiable
    consent_identity: false
    delegated_identity: documented
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: false
    protected_resource_metadata: false
    rate_limit_signal: derived
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 25.4
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 34
  human_in_the_loop: 0
  name: Ownerrez Agentic Access
  operation_count: 79
  slug: ownerrez-agentic-access
  summary_line: 79 operations · 34 acting
api_count: 1
apis:
- baseURL: https://api.ownerrez.com/v2
  baseurl_source: declared
  description: Reservations against a property, including dates, guest, and charges.
  name: OwnerRez Bookings API
  slug: ownerrez-bookings-api
- baseURL: https://api.ownerrez.com/v2
  baseurl_source: declared
  description: Security and damage deposits.
  name: OwnerRez Deposits API
  slug: ownerrez-deposits-api
- baseURL: https://api.ownerrez.com/v2
  baseurl_source: declared
  description: Discount rules.
  name: OwnerRez Discounts API
  slug: ownerrez-discounts-api
- baseURL: https://api.ownerrez.com/v2
  baseurl_source: declared
  description: Fees applied to bookings and quotes.
  name: OwnerRez Fees API
  slug: ownerrez-fees-api
- baseURL: https://api.ownerrez.com/v2
  baseurl_source: declared
  description: Custom field values attached to records.
  name: OwnerRez Fields API
  slug: ownerrez-fields-api
- baseURL: https://api.ownerrez.com/v2
  baseurl_source: declared
  description: Guest contact records and their addresses, emails, and phones.
  name: OwnerRez Guests API
  slug: ownerrez-guests-api
- baseURL: https://api.ownerrez.com/v2
  baseurl_source: declared
  description: Inbound guest inquiries and leads.
  name: OwnerRez Inquiries API
  slug: ownerrez-inquiries-api
- baseURL: https://api.ownerrez.com/v2
  baseurl_source: declared
  description: Public listing content and channel listing sites for properties.
  name: OwnerRez Listings API
  slug: ownerrez-listings-api
- baseURL: https://api.ownerrez.com/v2
  baseurl_source: declared
  description: Guest messaging threads and outbound messages.
  name: OwnerRez Messages API
  slug: ownerrez-messages-api
- baseURL: https://api.ownerrez.com/v2
  baseurl_source: declared
  description: Property owners.
  name: OwnerRez Owners API
  slug: ownerrez-owners-api
- baseURL: https://api.ownerrez.com/v2
  baseurl_source: declared
  description: Payments recorded against bookings.
  name: OwnerRez Payments API
  slug: ownerrez-payments-api
- baseURL: https://api.ownerrez.com/v2
  baseurl_source: declared
  description: Rental properties managed in OwnerRez.
  name: OwnerRez Properties API
  slug: ownerrez-properties-api
- baseURL: https://api.ownerrez.com/v2
  baseurl_source: declared
  description: Price quotes generated for a stay.
  name: OwnerRez Quotes API
  slug: ownerrez-quotes-api
- baseURL: https://api.ownerrez.com/v2
  baseurl_source: declared
  description: Refunds issued against payments.
  name: OwnerRez Refunds API
  slug: ownerrez-refunds-api
- baseURL: https://api.ownerrez.com/v2
  baseurl_source: declared
  description: Guest reviews collected for stays and properties.
  name: OwnerRez Reviews API
  slug: ownerrez-reviews-api
- baseURL: https://api.ownerrez.com/v2
  baseurl_source: declared
  description: Ad hoc nightly spot-rate overrides.
  name: OwnerRez SpotRates API
  slug: ownerrez-spotrates-api
- baseURL: https://api.ownerrez.com/v2
  baseurl_source: declared
  description: Surcharge rules applied to bookings and quotes.
  name: OwnerRez Surcharges API
  slug: ownerrez-surcharges-api
- baseURL: https://api.ownerrez.com/v2
  baseurl_source: declared
  description: Definitions of tags.
  name: OwnerRez TagDefinitions API
  slug: ownerrez-tagdefinitions-api
- baseURL: https://api.ownerrez.com/v2
  baseurl_source: declared
  description: Tag values applied to records.
  name: OwnerRez Tags API
  slug: ownerrez-tags-api
- baseURL: https://api.ownerrez.com/v2
  baseurl_source: declared
  description: The authenticated user context.
  name: OwnerRez Users API
  slug: ownerrez-users-api
- baseURL: https://api.ownerrez.com/v2
  baseurl_source: declared
  description: Definitions of custom fields.
  name: OwnerRez Field Definitions API
  slug: ownerrez-field-definitions-api
- baseURL: https://api.ownerrez.com/v2
  baseurl_source: declared
  description: Availability and criteria search across properties.
  name: OwnerRez Property Search API
  slug: ownerrez-property-search-api
- baseURL: https://api.ownerrez.com/v2
  baseurl_source: declared
  description: Outbound webhook subscriptions and their event categories.
  name: OwnerRez Webhook Subscriptions API
  slug: ownerrez-webhook-subscriptions-api
artifact_total: 54
collections:
- collection_type: open
  name: OwnerRez API v2 Bookings API
  slug: open-ownerrez-bookings-api
- collection_type: open
  name: OwnerRez API v2 Bookings Deposits API
  slug: open-ownerrez-deposits-api
- collection_type: open
  name: OwnerRez API v2 Bookings Discounts API
  slug: open-ownerrez-discounts-api
- collection_type: open
  name: OwnerRez API v2 Bookings Fees API
  slug: open-ownerrez-fees-api
- collection_type: open
  name: OwnerRez API v2 Bookings FieldDefinitions API
  slug: open-ownerrez-fielddefinitions-api
- collection_type: open
  name: OwnerRez API v2 Bookings Fields API
  slug: open-ownerrez-fields-api
- collection_type: open
  name: OwnerRez API v2 Bookings Guests API
  slug: open-ownerrez-guests-api
- collection_type: open
  name: OwnerRez API v2 Bookings Inquiries API
  slug: open-ownerrez-inquiries-api
- collection_type: open
  name: OwnerRez API v2 Bookings Listings API
  slug: open-ownerrez-listings-api
- collection_type: open
  name: OwnerRez API v2 Bookings Messages API
  slug: open-ownerrez-messages-api
- collection_type: open
  name: OwnerRez API v2 Bookings Owners API
  slug: open-ownerrez-owners-api
- collection_type: open
  name: OwnerRez API v2 Bookings Payments API
  slug: open-ownerrez-payments-api
- collection_type: open
  name: OwnerRez API v2 Bookings Properties API
  slug: open-ownerrez-properties-api
- collection_type: open
  name: OwnerRez API v2 Bookings PropertySearch API
  slug: open-ownerrez-propertysearch-api
- collection_type: open
  name: OwnerRez API v2 Bookings Quotes API
  slug: open-ownerrez-quotes-api
- collection_type: open
  name: OwnerRez API v2 Bookings Refunds API
  slug: open-ownerrez-refunds-api
- collection_type: open
  name: OwnerRez API v2 Bookings SpotRates API
  slug: open-ownerrez-spotrates-api
- collection_type: open
  name: OwnerRez API v2 Bookings Surcharges API
  slug: open-ownerrez-surcharges-api
- collection_type: open
  name: OwnerRez API v2 Bookings TagDefinitions API
  slug: open-ownerrez-tagdefinitions-api
- collection_type: open
  name: OwnerRez API v2 Bookings Tags API
  slug: open-ownerrez-tags-api
- collection_type: open
  name: OwnerRez API v2 Bookings Users API
  slug: open-ownerrez-users-api
- collection_type: open
  name: OwnerRez API v2 Bookings WebhookSubscriptions API
  slug: open-ownerrez-webhooksubscriptions-api
- collection_type: open
  name: OwnerRez API v2
  slug: open-ownerrez
common:
- group: other
  href: https://artifacts.apis.io/ownerrez/capabilities/ownerrez-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/ownerrez-capability-edges.yml
- group: agent
  href: https://artifacts.apis.io/ownerrez/agentic-access/ownerrez-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/ownerrez-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/ownerrez/security/ownerrez-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/ownerrez-domain-security.yml
- group: auth
  href: https://artifacts.apis.io/ownerrez/authentication/ownerrez-authentication.yml
  title: ''
  type: Authentication
  url: authentication/ownerrez-authentication.yml
- group: auth
  href: https://artifacts.apis.io/ownerrez/scopes/ownerrez-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/ownerrez-scopes.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/ownerrez
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/ownerrez
- group: company
  title: ''
  type: Website
  url: https://www.ownerrez.com
- group: docs
  title: ''
  type: Documentation
  url: https://api.ownerrez.com/help/v2
- group: commercial
  href: https://artifacts.apis.io/ownerrez/plans/ownerrez-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/ownerrez-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/ownerrez/rate-limits/ownerrez-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/ownerrez-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/ownerrez/finops/ownerrez-finops.yml
  title: ''
  type: FinOps
  url: finops/ownerrez-finops.yml
- group: company
  title: ''
  type: Blog
  url: https://www.ownerrez.com/blog
created: '2026-07-03'
description: OwnerRez is vacation-rental and short-term-rental property management software for hosts, owners, and property managers, covering channel management, bookings, guest CRM, quoting, payments, messaging, reviews, and a hosted booking website. The OwnerRez API v2 is a REST/JSON API served under https://api.ownerrez.com/v2 that exposes bookings, properties, listings, guests, inquiries, quotes, reviews, guest messaging, payments and financials, custom fields and tags, owners, and outbound webhook subscriptions. Requests are authenticated with an OAuth 2.0 access token (Authorization Code Grant) or with an API key / Personal Access Token via HTTP Basic auth, and server-to-app events are delivered through outbound webhooks.
finops:
- has_sources: true
  method: generated
  name: Ownerrez Finops
  primary_unit: ''
  service_category: Property Management Software
  slug: ownerrez-finops
  template: false
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/ownerrez.png
layout: provider
modified: '2026-07-03'
name: OwnerRez
nav: Providers
network: true
overview: 'OwnerRez publishes 23 API contracts indexed on the [APIs.io](https://apis.io/) network, including Bookings API, Deposits API, Discounts API, and 20 more. Tagged areas include Vacation Rentals, Short-Term Rental, Property Management, Hospitality, and Booking.


  The OwnerRez catalog on APIs.io includes 1 Spectral governance ruleset.


  OwnerRez''s developer surface includes authentication, documentation, engineering blog, and 10 more developer resources.'
plans:
- name: Ownerrez Plans Pricing
  plan_count: 3
  slug: ownerrez-plans-pricing
random_paper: 4
rate_limits:
- limit_count: 1
  name: Ownerrez Rate Limits
  slug: ownerrez-rate-limits
rules:
- authorship: generated
  effective_rule_count: 108
  extends:
  - spectral:oas
  name: OwnerRez API Rules
  rule_count: 67
  severity_counts:
    error: 62
    hint: 0
    info: 1
    warn: 4
  slug: ownerrez-rules
scopes:
- name: Ownerrez Scopes
  scope_count: 2
  slug: ownerrez-scopes
  summary_line: 2 scopes · authorizationCode
score:
  band: thin
  composite: 30.3
  coverage:
    artifact_dirs: 18
    catalog_earned: 46.5
    catalog_earned_first_party: 0.0
    catalog_gap: 68.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 7.9
    contract_governance: 13.6
    contract_quality: 52.1
    developer_ergonomics: 31.0
    discoverability: 66.1
    operational_transparency: 7.9
  previous_composite: 30.3
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 23
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
screenshot: https://apis.io/screenshots/ownerrez/ownerrez-2026-08-07T191158.png
security:
- kind: authentication
  name: Ownerrez Authentication
  slug: ownerrez-authentication
  summary_line: http/oauth2 · 2 schemes
- kind: domain-security
  name: Ownerrez Domain Security
  slug: ownerrez-domain-security
  summary_line: TLSv1.2 · DMARC
slug: ownerrez
tags:
- Vacation Rentals
- Short-Term Rental
- Property Management
- Hospitality
- Booking
- Channel Manager
website: https://www.ownerrez.com
---
