---
access_model:
  confidence: high
  label: Enterprise · Self-serve signup
  onboarding: self-serve
  pricing: enterprise
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: false
agentic_access:
- acting_count: 22
  human_in_the_loop: 0
  name: Expedia Group Agentic Access
  operation_count: 49
  slug: expedia-group-agentic-access
  summary_line: 49 operations · 22 acting
api_count: 5
apis:
- baseURL: https://test.ean.com/v3
  baseurl_source: spec
  description: The primary itinerary method of the Booking API creates a reservation for the selected hotel, room, rate and occupancy.
  name: Expedia Group Bookings API
  slug: expedia-group-bookings-api
- baseURL: https://test.ean.com/v3
  baseurl_source: spec
  description: This section outlines the API calls available to you to access property content.
  name: Expedia Group Content API
  slug: expedia-group-content-api
- baseURL: https://services.expediapartnercentral.com/
  baseurl_source: spec
  description: The Deposit resource
  name: Expedia Group Deposit API
  slug: expedia-group-deposit-api
- baseURL: https://test.ean.com/v3
  baseurl_source: spec
  description: The EPS Geography API provides geography content for regions around the world.
  name: Expedia Group Geography API
  slug: expedia-group-geography-api
- baseURL: https://test.analytics.ean.com/template/v1
  baseurl_source: spec
  description: Template Loyalty Earn API
  name: Expedia Group Loyalty API
  slug: expedia-group-loyalty-api
- baseURL: https://test.ean.com/v3
  baseurl_source: spec
  description: Retrieve existing itineraries or cancel existing rooms.
  name: Expedia Group Manage Booking API
  slug: expedia-group-manage-booking-api
- baseURL: https://test.ean.com/v3
  baseurl_source: spec
  description: Requests test notifications and undelivered notifications.
  name: Expedia Group Notifications API
  slug: expedia-group-notifications-api
- baseURL: https://api.sandbox.expediagroup.com/fraud-prevention/v2
  baseurl_source: spec
  description: The OrderPurchaseScreen API from Expedia Group — 1 operation(s) for orderpurchasescreen.
  name: Expedia Group OrderPurchaseScreen API
  slug: expedia-group-orderpurchasescreen-api
- baseURL: https://api.sandbox.expediagroup.com/fraud-prevention/v2
  baseurl_source: spec
  description: The OrderPurchaseUpdate API from Expedia Group — 1 operation(s) for orderpurchaseupdate.
  name: Expedia Group OrderPurchaseUpdate API
  slug: expedia-group-orderpurchaseupdate-api
- baseURL: https://services.expediapartnercentral.com/
  baseurl_source: spec
  description: The property resource
  name: Expedia Group Property API
  slug: expedia-group-property-api
- baseURL: https://services.expediapartnercentral.com/
  baseurl_source: spec
  description: The rate plan resource
  name: Expedia Group Rate Plan API
  slug: expedia-group-rate-plan-api
- baseURL: https://services.expediapartnercentral.com/
  baseurl_source: spec
  description: Manage room types Rate Verification Thresholds
  name: Expedia Group Rate Verification Thresholds API
  slug: expedia-group-rate-verification-thresholds-api
- baseURL: https://services.expediapartnercentral.com/
  baseurl_source: spec
  description: Manage room type amenities
  name: Expedia Group Room Type Amenities API
  slug: expedia-group-room-type-amenities-api
- baseURL: https://services.expediapartnercentral.com/
  baseurl_source: spec
  description: Manage room types
  name: Expedia Group Room Type API
  slug: expedia-group-room-type-api
- baseURL: https://test.ean.com/v3
  baseurl_source: spec
  description: The EPS shopping APIs provide you with access to live rates & availability.
  name: Expedia Group Shopping API
  slug: expedia-group-shopping-api
artifact_total: 41
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Expedia Group EPS Deposit Bookings API
  slug: open-expedia-group-bookings-api
- collection_type: open
  name: Expedia Group EPS Deposit Bookings Content API
  slug: open-expedia-group-content-api
- collection_type: open
  name: Expedia Group EPS Bookings Deposit API
  slug: open-expedia-group-deposit-api
- collection_type: open
  name: Expedia Group EPS Deposit Bookings Geography API
  slug: open-expedia-group-geography-api
- collection_type: open
  name: Expedia Group EPS Deposit Bookings Loyalty API
  slug: open-expedia-group-loyalty-api
- collection_type: open
  name: Expedia Group EPS Deposit Bookings Manage Booking API
  slug: open-expedia-group-manage-booking-api
- collection_type: open
  name: Expedia Group EPS Deposit Bookings Notifications API
  slug: open-expedia-group-notifications-api
- collection_type: open
  name: Expedia Group EPS Deposit Bookings OrderPurchaseScreen API
  slug: open-expedia-group-orderpurchasescreen-api
- collection_type: open
  name: Expedia Group EPS Deposit Bookings OrderPurchaseUpdate API
  slug: open-expedia-group-orderpurchaseupdate-api
- collection_type: open
  name: Expedia Group EPS Deposit Bookings Property API
  slug: open-expedia-group-property-api
- collection_type: open
  name: Expedia Group EPS Deposit Bookings Rate Plan API
  slug: open-expedia-group-rate-plan-api
- collection_type: open
  name: Expedia Group EPS Deposit Bookings Rate Verification Thresholds API
  slug: open-expedia-group-rate-verification-thresholds-api
- collection_type: open
  name: Expedia Group EPS Deposit Bookings Room Type Amenities API
  slug: open-expedia-group-room-type-amenities-api
- collection_type: open
  name: Expedia Group EPS Deposit Bookings Room Type API
  slug: open-expedia-group-room-type-api
- collection_type: open
  name: Expedia Group EPS Deposit Bookings Shopping API
  slug: open-expedia-group-shopping-api
common:
- group: company
  title: ''
  type: Website
  url: https://www.expediagroup.com/
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/expedia-group-capability-edges.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/expedia-group-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/expedia-group-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/expedia-group-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/expedia-group-scopes.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/expediagroup
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/expediagroup
- group: start
  title: ''
  type: Portal
  url: https://developers.expediagroup.com/docs/
- group: build
  title: ''
  type: SDKs
  url: https://developers.expediagroup.com/docs/sdk
- group: company
  title: ''
  type: Blog
  url: https://medium.com/expedia-group-tech
- group: company
  title: ''
  type: BlogRSS
  url: https://medium.com/feed/expedia-group-tech
- group: operate
  title: ''
  type: Support
  url: https://developers.expediagroup.com/docs/support
- group: operate
  title: ''
  type: StatusPage
  url: https://status.developers.expediagroup.com/
created: '2024-06-07'
description: Expedia Group is an American travel technology company that owns and operates travel fare aggregators and travel metasearch engines, including Expedia, Hotels.com, Vrbo, Travelocity, Hotwire.com, Orbitz, Ebookers, CheapTickets, CarRentals.com, and Trivago. Their developer platform provides APIs for travel inventory, lodging, and analytics.
features:
- 'Expedia Group: API access via partner / B2B contracts only'
- No public API pricing published — contact enterprise sales
- Expedia Group Rapid API (formerly EAN) and Partner Central require commercial agreements.
finops:
- name: Expedia Group Finops
  service_category: Travel / Hospitality
  slug: expedia-group-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/expedia-group.png
layout: provider
modified: '2026-05-19'
name: Expedia Group
nav: Providers
network: true
overview: 'Expedia Group publishes 15 APIs on the [APIs.io](https://apis.io/) network, including Bookings API, Content API, Deposit API, and 12 more. Tagged areas include Flights, Hotels, Lodging, Travel, and Fortune 500.


  Expedia Group''s developer surface includes authentication, developer portal, engineering blog, support, and 10 more developer resources.'
plans:
- name: Expedia Group Plans Pricing
  plan_count: 1
  slug: expedia-group-plans-pricing
random_paper: 15
rate_limits:
- limit_count: 1
  name: Expedia Group Rate Limits
  slug: expedia-group-rate-limits
scopes:
- name: Expedia Group Scopes
  scope_count: 3
  slug: expedia-group-scopes
  summary_line: 3 scopes · clientCredentials
screenshot: https://raw.githubusercontent.com/api-evangelist/expedia-group/refs/heads/main/screenshots/expedia-group-2026-06-20T180935.png
security:
- kind: authentication
  name: Expedia Group Authentication
  slug: expedia-group-authentication
  summary_line: apiKey/http/oauth2 · 3 schemes
- kind: domain-security
  name: Expedia Group Domain Security
  slug: expedia-group-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: expedia-group
tags:
- Flights
- Hotels
- Lodging
- Travel
- Fortune 500
website: https://www.expediagroup.com/
---
