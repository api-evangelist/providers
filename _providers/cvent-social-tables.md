---
access_model:
  confidence: high
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
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
- acting_count: 55
  human_in_the_loop: 3
  name: Cvent Social Tables Agentic Access
  operation_count: 86
  slug: cvent-social-tables-agentic-access
  summary_line: 86 operations · 55 acting · 3 human-in-the-loop
api_count: 18
apis:
- description: The legacy Social Tables Events API provided REST access to events, venues, floor plans, diagrams, and seating arrangements created in Social Tables. With Social Tables now part of Cvent's Hospitality
  name: Social Tables Events API (Legacy)
  slug: events-api
- description: The Authentication API from Cvent Social Tables — 1 operation(s) for authentication.
  name: Cvent Social Tables Authentication API
  slug: cvent-social-tables-authentication-api
- description: The Diagram Favorites API from Cvent Social Tables — 3 operation(s) for diagram favorites.
  name: Cvent Social Tables Diagram Favorites API
  slug: cvent-social-tables-diagram-favorites-api
- description: The Diagram Layouts API from Cvent Social Tables — 3 operation(s) for diagram layouts.
  name: Cvent Social Tables Diagram Layouts API
  slug: cvent-social-tables-diagram-layouts-api
- description: The Diagram Template Presets API from Cvent Social Tables — 2 operation(s) for diagram template presets.
  name: Cvent Social Tables Diagram Template Presets API
  slug: cvent-social-tables-diagram-template-presets-api
- description: The Diagrams API from Cvent Social Tables — 6 operation(s) for diagrams.
  name: Cvent Social Tables Diagrams API
  slug: cvent-social-tables-diagrams-api
- description: The Events API from Cvent Social Tables — 3 operation(s) for events.
  name: Cvent Social Tables Events API
  slug: cvent-social-tables-events-api
- description: The Guest Checkin API from Cvent Social Tables — 4 operation(s) for guest checkin.
  name: Cvent Social Tables Guest Checkin API
  slug: cvent-social-tables-guest-checkin-api
- description: The Guest Groups API from Cvent Social Tables — 7 operation(s) for guest groups.
  name: Cvent Social Tables Guest Groups API
  slug: cvent-social-tables-guest-groups-api
- description: The Guest Lists API from Cvent Social Tables — 6 operation(s) for guest lists.
  name: Cvent Social Tables Guest Lists API
  slug: cvent-social-tables-guest-lists-api
- description: The Guest Meals API from Cvent Social Tables — 3 operation(s) for guest meals.
  name: Cvent Social Tables Guest Meals API
  slug: cvent-social-tables-guest-meals-api
- description: The Guest Tags API from Cvent Social Tables — 3 operation(s) for guest tags.
  name: Cvent Social Tables Guest Tags API
  slug: cvent-social-tables-guest-tags-api
- description: The Guests API from Cvent Social Tables — 12 operation(s) for guests.
  name: Cvent Social Tables Guests API
  slug: cvent-social-tables-guests-api
- description: The Layout Automation API from Cvent Social Tables — 2 operation(s) for layout automation.
  name: Cvent Social Tables Layout Automation API
  slug: cvent-social-tables-layout-automation-api
- description: The Properties API from Cvent Social Tables — 2 operation(s) for properties.
  name: Cvent Social Tables Properties API
  slug: cvent-social-tables-properties-api
- description: The Rooms API from Cvent Social Tables — 2 operation(s) for rooms.
  name: Cvent Social Tables Rooms API
  slug: cvent-social-tables-rooms-api
- description: The SNC Event Integration API from Cvent Social Tables — 1 operation(s) for snc event integration.
  name: Cvent Social Tables SNC Event Integration API
  slug: cvent-social-tables-snc-event-integration-api
- description: The Users API from Cvent Social Tables — 1 operation(s) for users.
  name: Cvent Social Tables Users API
  slug: cvent-social-tables-users-api
artifact_total: 26
collections:
- collection_type: open
  name: Social Tables API Gateway
  slug: open-cvent-social-tables
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/cvent-social-tables-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/cvent-social-tables-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/cvent-social-tables-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/cvent-social-tables-scopes.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/socialtables
- group: company
  title: ''
  type: Website
  url: https://www.socialtables.com
- group: other
  title: ''
  type: ProductPage
  url: https://www.cvent.com/en/diagramming-event-design
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.socialtables.com
- group: start
  title: ''
  type: ParentDeveloperPortal
  url: https://developers.cvent.com/
- group: start
  title: ''
  type: Login
  url: https://app.socialtables.com/login
- group: operate
  title: ''
  type: Support
  url: https://support.cvent.com/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.cvent.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.cvent.com/en/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.cvent.com/en/privacy-policy
- group: company
  title: ''
  type: Blog
  url: https://www.socialtables.com/blog
- group: company
  title: ''
  type: Twitter
  url: https://twitter.com/socialtables
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/showcase/social-tables/
created: '2025-03-14'
description: Social Tables, a Cvent product, is event diagramming, room-design, and seating software for hospitality venues, hotels, and meeting planners. Planners design 2D / 3D floor plans, manage seating arrangements, build attendee guest lists, and collaborate with venues. Social Tables has been integrated into the Cvent Hospitality Cloud and Diagramming product line. The legacy Social Tables developer portal exposed a REST API for events, floor plans, and diagrams; new programmatic integration is generally delivered through the Cvent Platform REST API and the Cvent Diagramming product.
finops:
- name: Cvent Social Tables Finops
  service_category: API
  slug: cvent-social-tables-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/cvent-social-tables.png
layout: provider
modified: '2026-04-28'
name: Cvent Social Tables
nav: Providers
network: true
overview: 'Cvent Social Tables publishes 17 APIs on the [APIs.io](https://apis.io/) network, including Authentication API, Diagram Favorites API, Diagram Layouts API, and 14 more. Tagged areas include 3D Design, Catering, Diagramming, Event Design, and Event Management.


  Cvent Social Tables'' developer surface includes authentication, support, engineering blog, and 14 more developer resources.'
plans:
- name: Cvent Social Tables Plans Pricing
  plan_count: 3
  slug: cvent-social-tables-plans-pricing
random_paper: 18
rate_limits:
- limit_count: 5
  name: Cvent Social Tables Rate Limits
  slug: cvent-social-tables-rate-limits
scopes:
- name: Cvent Social Tables Scopes
  scope_count: 3
  slug: cvent-social-tables-scopes
  summary_line: 3 scopes · authorizationCode
score:
  band: developing
  composite: 42.3
  delta: -3.9
  facets:
    commercial_clarity: 73.7
    contract_quality: 32.3
    developer_ergonomics: 26.1
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 52.6
  previous_composite: 46.2
  provenance:
    agentic_access: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 17
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/cvent-social-tables/refs/heads/main/screenshots/cvent-social-tables-2026-06-20T175404.png
security:
- kind: authentication
  name: Cvent Social Tables Authentication
  slug: cvent-social-tables-authentication
  summary_line: apiKey/oauth2 · 3 schemes
- kind: domain-security
  name: Cvent Social Tables Domain Security
  slug: cvent-social-tables-domain-security
  summary_line: TLSv1.2 · HSTS · DMARC
slug: cvent-social-tables
tags:
- 3D Design
- Catering
- Diagramming
- Event Design
- Event Management
- Events
- Floor Plans
- Hospitality
- Hotel
- Meetings
- Seating
- Seating Charts
- Venues
website: https://www.socialtables.com
---
