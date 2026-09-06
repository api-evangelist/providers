---
access_model:
  confidence: medium
  label: Paid
  onboarding: unknown
  pricing: paid
  public: false
  source:
  - plans
  trial: false
  try_now: false
agent_readiness:
  band: human-only
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
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 0.0
  scored_at: '2026-09-05'
api_count: 5
apis:
- description: 'Programmatic access to an organization''s media catalog - sermons, series, podcasts, blogs, and announcements - for syncing content into external sites, AI/search pipelines, and custom apps. Endpoints '
  name: Subsplash Media Library API
  slug: subsplash-media-library-api
- description: Sync online giving and donation records from Subsplash Giving into accounting, CRM, and church-management systems - donations, donors, funds, and recurring gifts. Endpoints are modeled; access require
  name: Subsplash Giving API
  slug: subsplash-giving-api
- description: People Sync surface for unifying member and contact records across systems, plus Single Sign-On (SSO) user provisioning. Modeled from Subsplash's enterprise integration material (People Sync, SSO); th
  name: Subsplash People API
  slug: subsplash-people-api
- description: Manage groups, group membership, and messaging, and trigger push notifications and in-app messages through Subsplash's communications engine. Endpoints are modeled from public product material; access
  name: Subsplash Groups and Messaging API
  slug: subsplash-groups-messaging-api
- description: Manage events, event registrations, and event payments for syncing sign-ups and transactions into external systems. Endpoints are modeled; the documented reference is released only after the developer
  name: Subsplash Events API
  slug: subsplash-events-api
artifact_total: 8
common:
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/subsplash-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/subsplash-domain-security.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Subsplash
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/subsplash
- group: company
  title: ''
  type: Website
  url: https://www.subsplash.com
- group: docs
  title: ''
  type: Documentation
  url: https://developer.subsplash.com/
- group: start
  title: ''
  type: SignUp
  url: https://developer.subsplash.com/form
- group: commercial
  title: ''
  type: Plans
  url: plans/subsplash-plans-pricing.yml
- group: company
  title: ''
  type: Blog
  url: https://www.subsplash.com/blog
created: '2026-07-03'
description: Subsplash is an all-in-one church and ministry engagement platform - custom mobile and TV apps, websites, media hosting and delivery, online giving, and church management (People, Groups, Events, Volunteers). Subsplash publishes a REST developer API (OAuth 2.0, hosted on core.subsplash.com) for programmatic access to media, giving records, people, groups and messaging, and event registrations. Access is gated - full API documentation is released only after submitting the developer documentation-access form, and API credentials (Client ID / Client Secret) must be provisioned by a Subsplash representative on a qualifying paid plan (Pro / Enterprise). Because the documented endpoint surface is behind that gate, the APIs listed here are modeled from Subsplash's public product, support, and integration material rather than transcribed from an open reference, and are flagged endpointsModeled.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/subsplash.png
layout: provider
modified: '2026-07-03'
name: Subsplash
nav: Providers
network: true
overview: 'Subsplash publishes 5 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Church, Ministry, Non-Profit, Giving, and Media.


  Subsplash''s developer surface includes documentation, signup flow, engineering blog, and 6 more developer resources.'
plans:
- name: Subsplash Plans Pricing
  plan_count: 3
  slug: subsplash-plans-pricing
random_paper: 15
score:
  band: emerging
  composite: 17.2
  coverage:
    artifact_dirs: 4
    catalog_earned: 52.0
    catalog_earned_first_party: 0.0
    catalog_gap: 63.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 44.7
    commercial_clarity: 44.7
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 2.4
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 2.6
  previous_composite: 17.2
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/subsplash/refs/heads/main/screenshots/subsplash-2026-09-02T161101.png
security:
- kind: domain-security
  name: Subsplash Domain Security
  slug: subsplash-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Subsplash Vulnerability Disclosure
  slug: subsplash-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: subsplash
tags:
- Church
- Ministry
- Non-Profit
- Giving
- Media
- Church Management
- ChMS
- Mobile Apps
- Partner API
website: https://www.subsplash.com
---
