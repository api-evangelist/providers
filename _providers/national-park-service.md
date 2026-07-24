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
  scored_at: '2026-07-23'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: National Park Service Agentic Access
  operation_count: 11
  slug: national-park-service-agentic-access
  summary_line: 11 operations
api_count: 11
apis:
- description: The Activities API from National Park Service — 1 operation(s) for activities.
  name: National Park Service Activities API
  slug: national-park-service-activities-api
- description: The Alerts API from National Park Service — 1 operation(s) for alerts.
  name: National Park Service Alerts API
  slug: national-park-service-alerts-api
- description: The Articles API from National Park Service — 1 operation(s) for articles.
  name: National Park Service Articles API
  slug: national-park-service-articles-api
- description: The Campgrounds API from National Park Service — 1 operation(s) for campgrounds.
  name: National Park Service Campgrounds API
  slug: national-park-service-campgrounds-api
- description: The Events API from National Park Service — 1 operation(s) for events.
  name: National Park Service Events API
  slug: national-park-service-events-api
- description: The Newsreleases API from National Park Service — 1 operation(s) for newsreleases.
  name: National Park Service Newsreleases API
  slug: national-park-service-newsreleases-api
- description: The Parks API from National Park Service — 1 operation(s) for parks.
  name: National Park Service Parks API
  slug: national-park-service-parks-api
- description: The People API from National Park Service — 1 operation(s) for people.
  name: National Park Service People API
  slug: national-park-service-people-api
- description: The Places API from National Park Service — 1 operation(s) for places.
  name: National Park Service Places API
  slug: national-park-service-places-api
- description: The Topics API from National Park Service — 1 operation(s) for topics.
  name: National Park Service Topics API
  slug: national-park-service-topics-api
- description: The Visitorcenters API from National Park Service — 1 operation(s) for visitorcenters.
  name: National Park Service Visitorcenters API
  slug: national-park-service-visitorcenters-api
artifact_total: 18
collections:
- collection_type: open
  name: National Park Service Data API
  slug: open-national-park-service
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/national-park-service-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/national-park-service-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/national-park-service-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/nationalparkservice
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/nationalparkservice
- group: company
  title: ''
  type: Website
  url: https://www.nps.gov/
- group: start
  title: ''
  type: Portal
  url: https://www.nps.gov/subjects/developer/index.htm
created: '2024-12-03'
description: The National Park Service is a federal agency responsible for managing and protecting the United States' national parks, monuments, and historic sites. Established in 1916, the NPS works to preserve natural and cultural resources for future generations while providing opportunities for the public to enjoy and learn from these special places.
finops:
- name: National Park Service Finops
  service_category: API
  slug: national-park-service-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/national-park-service.png
layout: provider
modified: '2026-05-19'
name: National Park Service
nav: Providers
network: true
overview: 'National Park Service publishes 11 APIs on the [APIs.io](https://apis.io/) network, including Activities API, Alerts API, Articles API, and 8 more. Tagged areas include Conservation, Federal Government, and Parks.


  National Park Service''s developer surface includes authentication, developer portal, and 5 more developer resources.'
plans:
- name: National Park Service Plans Pricing
  plan_count: 3
  slug: national-park-service-plans-pricing
random_paper: 36
rate_limits:
- limit_count: 5
  name: National Park Service Rate Limits
  slug: national-park-service-rate-limits
score:
  band: thin
  composite: 33.9
  delta: 0.0
  facets:
    commercial_clarity: 39.5
    contract_quality: 47.0
    developer_ergonomics: 19.6
    discoverability: 55.0
    governance: 0.0
    operational_transparency: 36.8
  previous_composite: 33.9
  schema_version: 0.5
  scored_at: '2026-07-23'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/national-park-service/refs/heads/main/screenshots/national-park-service-2026-06-20T190036.png
security:
- kind: authentication
  name: National Park Service Authentication
  slug: national-park-service-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: National Park Service Domain Security
  slug: national-park-service-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: national-park-service
tags:
- Conservation
- Federal Government
- Parks
website: https://www.nps.gov/
---
