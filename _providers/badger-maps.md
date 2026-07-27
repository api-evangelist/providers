---
access_model:
  confidence: high
  label: Paid · Self-serve signup
  onboarding: self-serve
  pricing: paid
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_skills: false
    agentic_access: true
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: true
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.1
  score: 48.1
  scored_at: '2026-07-27'
agentic_access:
- acting_count: 6
  human_in_the_loop: 0
  name: Badger Maps Agentic Access
  operation_count: 13
  slug: badger-maps-agentic-access
  summary_line: 13 operations · 6 acting
api_count: 5
apis:
- description: Accounts (customers) - the businesses and contacts a rep maps and visits.
  name: Badger Maps Accounts API
  slug: badger-maps-accounts-api
- description: Timestamped activity logs recorded against an account (the /appointments/ resource).
  name: Badger Maps Check-Ins API
  slug: badger-maps-check-ins-api
- description: Physical, geocoded locations attached to an account.
  name: Badger Maps Locations API
  slug: badger-maps-locations-api
- description: Optimized driving routes and their ordered waypoints.
  name: Badger Maps Routes API
  slug: badger-maps-routes-api
- description: Authentication, the authenticated user profile, and user search.
  name: Badger Maps Users API
  slug: badger-maps-users-api
artifact_total: 12
collections:
- collection_type: open
  name: Badger Maps API
  slug: open-badger-maps
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/badger-maps-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/badger-maps-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/badger-maps-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/BadgerMaps
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/badger-maps
- group: company
  title: ''
  type: Website
  url: https://www.badgermapping.com
- group: docs
  title: ''
  type: Documentation
  url: https://badgerupdatedapi.docs.apiary.io/
- group: commercial
  title: ''
  type: Plans
  url: plans/badger-maps-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/badger-maps-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/badger-maps-finops.yml
- group: company
  title: ''
  type: Blog
  url: https://www.badgermapping.com/blog/
created: '2026-07-04'
description: Badger Maps is field sales route planning, mapping, and CRM software for outside sales and field teams - it optimizes daily driving routes, maps and filters accounts on a territory, captures check-ins, and reports on rep activity. Badger Maps also exposes a token-authenticated REST API (base https://badgerapis.badgermapping.com/api/2) that lets teams programmatically manage accounts (customers), account locations, routes, check-ins, and users, and sync data with CRMs and other systems. API/Developer Key access is included with paid plans (max 25k requests per day, per team); the key must be enabled by contacting Badger Maps support.
finops:
- name: Badger Maps Finops
  service_category: Field Sales and Route Planning Software
  slug: badger-maps-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/badger-maps.png
layout: provider
modified: '2026-07-04'
name: Badger Maps
nav: Providers
network: true
overview: 'Badger Maps publishes 5 APIs on the [APIs.io](https://apis.io/) network, including Accounts API, Check-Ins API, Locations API, and 2 more. Tagged areas include Field Sales, Route Planning, Mapping, CRM, and Sales Enablement.


  Badger Maps'' developer surface includes authentication, documentation, engineering blog, and 8 more developer resources.'
plans:
- name: Badger Maps Plans Pricing
  plan_count: 6
  slug: badger-maps-plans-pricing
random_paper: 3
rate_limits:
- limit_count: 3
  name: Badger Maps Rate Limits
  slug: badger-maps-rate-limits
score:
  band: thin
  composite: 41.6
  delta: 3.2
  facets:
    commercial_clarity: 39.5
    contract_quality: 58.4
    developer_ergonomics: 21.7
    discoverability: 100.0
    governance: 0.0
    operational_transparency: 36.8
  previous_composite: 38.4
  schema_version: 0.5
  scored_at: '2026-07-27'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/badger-maps/refs/heads/main/screenshots/badger-maps-2026-07-25T202239.png
security:
- kind: authentication
  name: Badger Maps Authentication
  slug: badger-maps-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Badger Maps Domain Security
  slug: badger-maps-domain-security
  summary_line: TLSv1.2 · HSTS · DMARC
slug: badger-maps
tags:
- Field Sales
- Route Planning
- Mapping
- CRM
- Sales Enablement
- Territory Management
website: https://www.badgermapping.com
---
