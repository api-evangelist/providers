---
access_model:
  confidence: medium
  gated: none
  gated_source:
  - onboarding
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
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: false
    protected_resource_metadata: false
    rate_limit_signal: derived
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 24.4
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 19
  human_in_the_loop: 3
  name: Edgegap Agentic Access
  operation_count: 34
  slug: edgegap-agentic-access
  summary_line: 34 operations · 19 acting · 3 human-in-the-loop
api_count: 1
apis:
- baseURL: https://api.edgegap.com
  baseurl_source: declared
  description: Manage applications registered on Edgegap.
  name: Edgegap Applications API
  slug: edgegap-applications-api
- baseURL: https://api.edgegap.com
  baseurl_source: declared
  description: Deploy, inspect, and stop dedicated game servers at the edge.
  name: Edgegap Deployments API
  slug: edgegap-deployments-api
- baseURL: https://api.edgegap.com
  baseurl_source: declared
  description: Private fleet deployments and host inventory.
  name: Edgegap Fleets API
  slug: edgegap-fleets-api
- baseURL: https://api.edgegap.com
  baseurl_source: declared
  description: Monitoring and telemetry for deployments.
  name: Edgegap Metrics API
  slug: edgegap-metrics-api
- baseURL: https://api.edgegap.com
  baseurl_source: declared
  description: Distributed relay sessions and per-user authorization.
  name: Edgegap Relays API
  slug: edgegap-relays-api
- baseURL: https://api.edgegap.com
  baseurl_source: declared
  description: Add and remove players or groups on a running deployment.
  name: Edgegap Sessions API
  slug: edgegap-sessions-api
- baseURL: https://api.edgegap.com
  baseurl_source: declared
  description: Container Registry API
  name: Edgegap Container Registry API
  slug: edgegap-container-registry-api
- baseURL: https://api.edgegap.com
  baseurl_source: declared
  description: Deployment Tags API - Deployment Tags related operations.
  name: Edgegap Deployment Tags API
  slug: edgegap-deployment-tags-api
- baseURL: https://api.edgegap.com
  baseurl_source: declared
  description: Endpoint Storage Control API - Please refer to <a href='https://docs.edgegap.com/docs/deployment/endpoint-storage' target='_blank'>this documentation</a> to get started with storage.
  name: Edgegap Endpoint Storage API
  slug: edgegap-endpoint-storage-api
- baseURL: https://api.edgegap.com
  baseurl_source: declared
  description: IP API - IP addresses related operations.
  name: Edgegap IP Lookup API
  slug: edgegap-ip-lookup-api
- baseURL: https://api.edgegap.com
  baseurl_source: declared
  description: Locations API - Please refer to <a href='https://docs.edgegap.com/docs/deployment/locations/beacons' target='_blank'>this documentation</a> to get started with locations beacons.
  name: Edgegap Locations API
  slug: edgegap-locations-api
- baseURL: https://api.edgegap.com
  baseurl_source: declared
  description: API to report one of your game server
  name: Edgegap Report Deployment API
  slug: edgegap-report-deployment-api
artifact_total: 28
collections:
- collection_type: open
  name: Edgegap Arbitrium App Versions API
  slug: open-edgegap-app-versions-api
- collection_type: open
  name: Edgegap Arbitrium App Versions Applications API
  slug: open-edgegap-applications-api
- collection_type: open
  name: Edgegap Arbitrium App Versions Deployments API
  slug: open-edgegap-deployments-api
- collection_type: open
  name: Edgegap Arbitrium App Versions Fleets API
  slug: open-edgegap-fleets-api
- collection_type: open
  name: Edgegap Arbitrium App Versions Matchmaking API
  slug: open-edgegap-matchmaking-api
- collection_type: open
  name: Edgegap Arbitrium App Versions Metrics API
  slug: open-edgegap-metrics-api
- collection_type: open
  name: Edgegap Arbitrium App Versions Relays API
  slug: open-edgegap-relays-api
- collection_type: open
  name: Edgegap Arbitrium App Versions Sessions API
  slug: open-edgegap-sessions-api
- collection_type: open
  name: Edgegap Arbitrium API
  slug: open-edgegap
common:
- group: company
  title: ''
  type: Blog
  url: https://edgegap.com/blog
- group: agent
  href: https://artifacts.apis.io/edgegap/agentic-access/edgegap-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/edgegap-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/edgegap/security/edgegap-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/edgegap-domain-security.yml
- group: auth
  href: https://artifacts.apis.io/edgegap/authentication/edgegap-authentication.yml
  title: ''
  type: Authentication
  url: authentication/edgegap-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/edgegap
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/edgegap
- group: company
  title: ''
  type: Website
  url: https://edgegap.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.edgegap.com/
- group: commercial
  href: https://artifacts.apis.io/edgegap/plans/edgegap-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/edgegap-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/edgegap/rate-limits/edgegap-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/edgegap-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/edgegap/finops/edgegap-finops.yml
  title: ''
  type: FinOps
  url: finops/edgegap-finops.yml
created: '2026-07-01'
description: Edgegap provides distributed edge game-server orchestration, hosting, and matchmaking. Its Arbitrium platform auto-deploys dedicated game servers as containers to the optimal edge location out of 615+ locations worldwide, reducing latency for players. The REST API covers applications, versions, deployments, sessions, matchmaking, distributed relays, monitoring, and private fleets.
finops:
- has_sources: true
  method: generated
  name: Edgegap Finops
  primary_unit: ''
  service_category: Compute
  slug: edgegap-finops
  template: false
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/edgegap.png
layout: provider
modified: '2026-10-06'
name: Edgegap
nav: Providers
network: true
overview: 'Edgegap publishes 12 API contracts indexed on the [APIs.io](https://apis.io/) network, including Applications API, Deployments API, Fleets API, and 9 more. Tagged areas include Game Servers, Edge Computing, Matchmaking, Hosting, and Container Orchestration.


  The Edgegap catalog on APIs.io includes 1 Spectral governance ruleset.


  Edgegap''s developer surface includes engineering blog, authentication, documentation, and 8 more developer resources.'
plans:
- name: Edgegap Plans Pricing
  plan_count: 3
  slug: edgegap-plans-pricing
random_paper: 21
rate_limits:
- limit_count: 4
  name: Edgegap Rate Limits
  slug: edgegap-rate-limits
rules:
- authorship: generated
  effective_rule_count: 107
  extends:
  - spectral:oas
  name: Edgegap API Rules
  rule_count: 66
  severity_counts:
    error: 51
    hint: 0
    info: 1
    warn: 14
  slug: edgegap-rules
score:
  band: thin
  composite: 28.6
  coverage:
    artifact_dirs: 15
    catalog_earned: 47.5
    catalog_earned_first_party: 0.0
    catalog_gap: 67.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.8
  facets:
    access_clarity: 7.9
    contract_governance: 13.6
    contract_quality: 55.5
    developer_ergonomics: 23.8
    discoverability: 66.1
    operational_transparency: 10.5
  previous_composite: 27.8
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 57.1
      total: 21
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 11.8
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/edgegap/edgegap-2026-07-25T212833.png
security:
- kind: authentication
  name: Edgegap Authentication
  slug: edgegap-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Edgegap Domain Security
  slug: edgegap-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: edgegap
tags:
- Game Servers
- Edge Computing
- Matchmaking
- Hosting
- Container Orchestration
website: https://edgegap.com/
---
