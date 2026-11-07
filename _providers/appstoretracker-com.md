---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - security
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
    mcp_server: documented
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 3.1
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: Provides access to App Store ranking and analytics data as described in the reference documentation.
  name: App Store Tracker API
  slug: app-store-tracker-api
artifact_total: 2
common:
- group: agent
  href: https://artifacts.apis.io/appstoretracker-com/llms/appstoretracker-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/appstoretracker-com-llms.txt
- group: other
  href: https://artifacts.apis.io/appstoretracker-com/hosts/appstoretracker-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/appstoretracker-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/appstoretracker-com/vendors/appstoretracker-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/appstoretracker-com-vendors.yml
- group: commercial
  title: ''
  type: Pricing
  url: https://www.appstoretracker.com/pricing
- group: company
  title: ''
  type: Newsroom
  url: https://www.appstoretracker.com/us/news
- group: start
  title: ''
  type: DeveloperPortal
  url: https://www.appstoretracker.com/developer/fis-1137739797
- group: docs
  title: ''
  type: APIReference
  url: https://www.appstoretracker.com/us/reference
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/appstoretracker
- group: auth
  href: https://artifacts.apis.io/appstoretracker-com/security/appstoretracker-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/appstoretracker-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://appstoretracker.com/
coverage:
  checked: '2026-11-01'
  detail: No OpenAPI, AsyncAPI, GraphQL, or other machine-readable contract could be retrieved despite accessible documentation.
  evidence:
  - status: 200
    url: https://www.appstoretracker.com/us/reference
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-11-01'
description: App Store Tracker is an independent iOS App Store ranking and analytics tool. It monitors daily top free chart positions, app metadata, and ranking history across 114 storefronts and all 22 App Store categories. Data is sourced from Apple’s public iTunes Search API and updated daily. The service provides insights for developers, marketers, and researchers without scraping the App Store website.
image: https://www.appstoretracker.com/brand/ast-social.png
layout: provider
modified: '2026-11-01'
name: App Store Tracker
nav: Providers
network: true
overview: 'App Store Tracker is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Analytics, iOS, App Store, Rankings, and Data.


  App Store Tracker''s developer surface includes pricing, API reference, and 8 more developer resources.'
random_paper: 22
score:
  band: minimal
  composite: 7.5
  coverage:
    artifact_dirs: 7
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -3.1
  facets:
    access_clarity: 5.3
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 8.3
    discoverability: 58.0
    operational_transparency: 2.6
  previous_composite: 10.6
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 5.9
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Appstoretracker Com Domain Security
  slug: appstoretracker-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: appstoretracker-com
tags:
- Analytics
- iOS
- App Store
- Rankings
- Data
website: https://appstoretracker.com/
---
