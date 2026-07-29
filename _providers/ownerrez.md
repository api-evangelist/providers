---
access_model:
  confidence: high
  label: Freemium (free trial) · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  trial: true
  try_now: true
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 30.6
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 34
  human_in_the_loop: 0
  name: Ownerrez Agentic Access
  operation_count: 79
  slug: ownerrez-agentic-access
  summary_line: 79 operations · 34 acting
api_count: 23
apis:
- description: Reservations against a property, including dates, guest, and charges.
  name: OwnerRez Bookings API
  slug: ownerrez-bookings-api
- description: Security and damage deposits.
  name: OwnerRez Deposits API
  slug: ownerrez-deposits-api
- description: Discount rules.
  name: OwnerRez Discounts API
  slug: ownerrez-discounts-api
- description: Fees applied to bookings and quotes.
  name: OwnerRez Fees API
  slug: ownerrez-fees-api
- description: Definitions of custom fields.
  name: OwnerRez FieldDefinitions API
  slug: ownerrez-fielddefinitions-api
- description: Custom field values attached to records.
  name: OwnerRez Fields API
  slug: ownerrez-fields-api
- description: Guest contact records and their addresses, emails, and phones.
  name: OwnerRez Guests API
  slug: ownerrez-guests-api
- description: Inbound guest inquiries and leads.
  name: OwnerRez Inquiries API
  slug: ownerrez-inquiries-api
- description: Public listing content and channel listing sites for properties.
  name: OwnerRez Listings API
  slug: ownerrez-listings-api
- description: Guest messaging threads and outbound messages.
  name: OwnerRez Messages API
  slug: ownerrez-messages-api
- description: Property owners.
  name: OwnerRez Owners API
  slug: ownerrez-owners-api
- description: Payments recorded against bookings.
  name: OwnerRez Payments API
  slug: ownerrez-payments-api
- description: Rental properties managed in OwnerRez.
  name: OwnerRez Properties API
  slug: ownerrez-properties-api
- description: Availability and criteria search across properties.
  name: OwnerRez PropertySearch API
  slug: ownerrez-propertysearch-api
- description: Price quotes generated for a stay.
  name: OwnerRez Quotes API
  slug: ownerrez-quotes-api
- description: Refunds issued against payments.
  name: OwnerRez Refunds API
  slug: ownerrez-refunds-api
- description: Guest reviews collected for stays and properties.
  name: OwnerRez Reviews API
  slug: ownerrez-reviews-api
- description: Ad hoc nightly spot-rate overrides.
  name: OwnerRez SpotRates API
  slug: ownerrez-spotrates-api
- description: Surcharge rules applied to bookings and quotes.
  name: OwnerRez Surcharges API
  slug: ownerrez-surcharges-api
- description: Definitions of tags.
  name: OwnerRez TagDefinitions API
  slug: ownerrez-tagdefinitions-api
- description: Tag values applied to records.
  name: OwnerRez Tags API
  slug: ownerrez-tags-api
- description: The authenticated user context.
  name: OwnerRez Users API
  slug: ownerrez-users-api
- description: Outbound webhook subscriptions and their event categories.
  name: OwnerRez WebhookSubscriptions API
  slug: ownerrez-webhooksubscriptions-api
artifact_total: 31
collections:
- collection_type: open
  name: OwnerRez API v2
  slug: open-ownerrez
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/ownerrez-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/ownerrez-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/ownerrez-authentication.yml
- group: auth
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
  title: ''
  type: Plans
  url: plans/ownerrez-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/ownerrez-rate-limits.yml
- group: commercial
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
- name: Ownerrez Finops
  service_category: Property Management Software
  slug: ownerrez-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/ownerrez.png
layout: provider
modified: '2026-07-03'
name: OwnerRez
nav: Providers
network: true
overview: 'OwnerRez publishes 23 APIs on the [APIs.io](https://apis.io/) network, including Bookings API, Deposits API, Discounts API, and 20 more. Tagged areas include Vacation Rental, Short-Term Rental, Property Management, Hospitality, and Bookings.


  OwnerRez''s developer surface includes authentication, documentation, engineering blog, and 9 more developer resources.'
plans:
- name: Ownerrez Plans Pricing
  plan_count: 3
  slug: ownerrez-plans-pricing
random_paper: 1
rate_limits:
- limit_count: 1
  name: Ownerrez Rate Limits
  slug: ownerrez-rate-limits
scopes:
- name: Ownerrez Scopes
  scope_count: 2
  slug: ownerrez-scopes
  summary_line: 2 scopes · authorizationCode
score:
  band: thin
  composite: 38.1
  delta: -2.2
  facets:
    commercial_clarity: 39.5
    contract_quality: 60.2
    developer_ergonomics: 21.7
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 26.3
  previous_composite: 40.3
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 23
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
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
- Vacation Rental
- Short-Term Rental
- Property Management
- Hospitality
- Bookings
- Channel Manager
website: https://www.ownerrez.com
---
