---
access_model:
  confidence: medium
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  - security
  trial: false
  try_now: true
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
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
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 19.8
  scored_at: '2026-09-04'
agentic_access:
- acting_count: 7
  human_in_the_loop: 0
  name: Gameanalytics Agentic Access
  operation_count: 12
  slug: gameanalytics-agentic-access
  summary_line: 12 operations · 7 acting
api_count: 1
apis:
- description: PipelineIQ raw data export streams every gameplay event as JSON objects (a metadata wrapper plus an event data object) in real time, with historical backfill, into a customer's own cloud environment -
  name: GameAnalytics Data Export (PipelineIQ)
  slug: gameanalytics-data-export-api
- baseURL: https://api.gameanalytics.com/v2
  baseurl_source: declared
  description: HMAC-signed event ingestion (Collector API).
  name: GameAnalytics Collection API
  slug: gameanalytics-collection-api
- baseURL: https://api.gameanalytics.com/v2
  baseurl_source: declared
  description: Aggregated gameplay metrics and reporting.
  name: GameAnalytics Metrics API
  slug: gameanalytics-metrics-api
- baseURL: https://api.gameanalytics.com/v2
  baseurl_source: declared
  description: Programmatic administration of games, studios, users, and permissions.
  name: GameAnalytics Organization API
  slug: gameanalytics-organization-api
artifact_total: 17
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: GameAnalytics REST APIs Collection API
  slug: open-gameanalytics-collection-api
- collection_type: open
  name: GameAnalytics REST APIs Collection Metrics API
  slug: open-gameanalytics-metrics-api
- collection_type: open
  name: GameAnalytics REST APIs Collection Organization API
  slug: open-gameanalytics-organization-api
- collection_type: open
  name: GameAnalytics REST APIs
  slug: open-gameanalytics
common:
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/gameanalytics-capability-edges.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/gameanalytics-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/gameanalytics-trust-center.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/gameanalytics-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/gameanalytics-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/gameanalytics-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/GameAnalytics
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/gameanalytics
- group: company
  title: ''
  type: Website
  url: https://gameanalytics.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.gameanalytics.com/
- group: commercial
  title: ''
  type: Plans
  url: plans/gameanalytics-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/gameanalytics-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/gameanalytics-finops.yml
- group: company
  title: ''
  type: Blog
  url: https://www.gameanalytics.com/blog/rss.xml
created: '2026-07-01'
description: GameAnalytics is a free analytics platform purpose-built for games, used to track player behavior, retention and cohorts, progression funnels, in-game economy and resource flows, and monetization and ads analytics. Data is collected through the HMAC-signed Collection (Collector) REST API or platform SDKs, queried through the Metrics API, streamed to a customer's own cloud via PipelineIQ Data Export, and administered through the Organization API.
finops:
- name: Gameanalytics Finops
  service_category: Analytics
  slug: gameanalytics-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/gameanalytics.png
layout: provider
modified: '2026-07-01'
name: GameAnalytics
nav: Providers
network: true
overview: 'GameAnalytics publishes 3 APIs on the [APIs.io](https://apis.io/) network: Collection API, Metrics API, and Organization API. Tagged areas include Analytics, Games, Gaming, Player Behavior, and Retention.


  GameAnalytics'' developer surface includes authentication, documentation, engineering blog, and 11 more developer resources.'
plans:
- name: Gameanalytics Plans Pricing
  plan_count: 3
  slug: gameanalytics-plans-pricing
random_paper: 13
rate_limits:
- limit_count: 5
  name: Gameanalytics Rate Limits
  slug: gameanalytics-rate-limits
score:
  band: developing
  composite: 40.7
  coverage:
    artifact_dirs: 11
    catalog_earned: 64.0
    catalog_earned_first_party: 0.0
    catalog_gap: 51.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -0.8
  facets:
    access_clarity: 47.4
    commercial_clarity: 47.4
    contract_governance: 0.0
    contract_quality: 54.2
    developer_ergonomics: 32.1
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 34.2
  previous_composite: 41.5
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 3
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/gameanalytics/refs/heads/main/screenshots/gameanalytics-2026-07-25T215409.png
security:
- kind: authentication
  name: Gameanalytics Authentication
  slug: gameanalytics-authentication
  summary_line: apiKey · 2 schemes
- kind: domain-security
  name: Gameanalytics Domain Security
  slug: gameanalytics-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Gameanalytics Vulnerability Disclosure
  slug: gameanalytics-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Gameanalytics Trust Center
  slug: gameanalytics-trust-center
  summary_line: SOC 2, ISO 27001
slug: gameanalytics
tags:
- Analytics
- Games
- Gaming
- Player Behavior
- Retention
- Monetization
- Ad Analytics
- Telemetry
website: https://gameanalytics.com/
---
