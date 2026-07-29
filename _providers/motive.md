---
access_model:
  confidence: medium
  label: Freemium
  onboarding: unknown
  pricing: freemium
  public: false
  source:
  - plans
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    asyncapi_events: false
    auth_clarity: false
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
  score: 19.4
  scored_at: '2026-07-28'
api_count: 1
apis:
- description: Core REST API providing access to driver management, vehicle tracking, Hours of Service logs, IFTA trip reports, inspection reports, dashcam events, dispatch workflows, geofencing, messaging, fuel pur
  name: Motive Fleet API
  slug: motive-fleet-api
artifact_total: 7
common:
- group: auth
  title: ''
  type: TrustCenter
  url: security/motive-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/motive-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://gomotive.com/
- group: docs
  title: ''
  type: Documentation
  url: https://developer-docs.gomotive.com/docs/introduction
- group: docs
  title: ''
  type: APIReference
  url: https://developer-docs.gomotive.com/reference/introduction
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.gomotive.com/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/KeepTruckin
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/motive-inc
- group: other
  title: ''
  type: X
  url: https://twitter.com/Motive_inc
- group: company
  title: ''
  type: Blog
  url: https://gomotive.com/blog/
- group: company
  title: ''
  type: BlogRSS
  url: https://gomotive.com/blog/feed
- group: operate
  title: ''
  type: StatusPage
  url: https://status.gomotive.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://gomotive.com/legal/api-terms-of-service/
- group: commercial
  title: ''
  type: Plans
  url: plans/motive-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/motive-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/motive-finops.yml
- group: start
  title: ''
  type: BlogIndex
  url: blogs/blogs.json
- group: design
  title: ''
  type: JSONLDContext
  url: json-ld/motive-context.jsonld
created: 2026-06-12
description: Motive (formerly KeepTruckin) is a fleet management platform serving more than 120,000 businesses across trucking, logistics, construction, agriculture, and field service industries. The Motive REST API provides programmatic access to driver management, vehicle tracking, Hours of Service (HOS) compliance, IFTA reporting, dashcam events, dispatch workflows, geofencing, and real-time location data. Developers authenticate via OAuth 2.0 with scoped access tokens and can reach endpoints at api.gomotive.com (or the legacy api.keeptruckin.com base URL). The self-serve Developer Portal allows partners to build and publish apps to the Motive App Marketplace, and Postman collections are available alongside interactive API reference documentation.
finops:
- name: Motive Finops
  service_category: ''
  slug: motive-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/motive.png
jsonld:
- class_count: 30
  name: Motive Context
  property_count: 0
  slug: motive-context
layout: provider
modified: 2026-06-12
name: Motive
nav: Providers
network: true
overview: 'Motive publishes 1 API on the [APIs.io](https://apis.io/) network: Fleet API. Tagged areas include Fleet Management, Trucking, Logistics, GPS Tracking, and Hours of Service.


  The Motive catalog on APIs.io includes 1 JSON-LD context.


  Motive''s developer surface includes documentation, API reference, engineering blog, and 15 more developer resources.'
plans:
- name: Motive Plans Pricing
  plan_count: 3
  slug: motive-plans-pricing
random_paper: 44
rate_limits:
- limit_count: 0
  name: Motive Rate Limits
  slug: motive-rate-limits
score:
  band: thin
  composite: 37.7
  delta: -4.3
  facets:
    commercial_clarity: 57.9
    contract_quality: 45.2
    developer_ergonomics: 26.1
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 21.1
  previous_composite: 42.0
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/motive/refs/heads/main/screenshots/motive-2026-06-20T185825.png
security:
- kind: domain-security
  name: Motive Domain Security
  slug: motive-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: trust-center
  name: Motive Trust Center
  slug: motive-trust-center
  summary_line: SOC 2, ISO 27001, PCI DSS
slug: motive
tags:
- Fleet Management
- Trucking
- Logistics
- GPS Tracking
- Hours of Service
- ELD
- IFTA
- Dashcam
- Dispatch
- Compliance
- Driver Management
website: https://gomotive.com/
---
