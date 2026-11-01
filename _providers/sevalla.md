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
    agent_card: false
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: false
    protected_resource_metadata: verified
    rate_limit_signal: derived
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 37.5
  scored_at: '2026-10-31'
agentic_access:
- acting_count: 19
  human_in_the_loop: 0
  name: Sevalla Agentic Access
  operation_count: 36
  slug: sevalla-agentic-access
  summary_line: 36 operations · 19 acting
api_count: 1
apis:
- baseURL: https://api.sevalla.com/v3
  baseurl_source: declared
  description: Deploy and manage applications from Git or Docker.
  name: Sevalla Applications API
  slug: sevalla-applications-api
- baseURL: https://api.sevalla.com/v3
  baseurl_source: declared
  description: Company users, projects, usage, and API keys.
  name: Sevalla Company API
  slug: sevalla-company-api
- baseURL: https://api.sevalla.com/v3
  baseurl_source: declared
  description: Provision and manage managed databases.
  name: Sevalla Databases API
  slug: sevalla-databases-api
- baseURL: https://api.sevalla.com/v3
  baseurl_source: declared
  description: Trigger, inspect, and roll back deployments.
  name: Sevalla Deployments API
  slug: sevalla-deployments-api
- baseURL: https://api.sevalla.com/v3
  baseurl_source: declared
  description: S3-compatible object storage buckets.
  name: Sevalla Object Storage API
  slug: sevalla-object-storage-api
- baseURL: https://api.sevalla.com/v3
  baseurl_source: declared
  description: Multi-stage promotion pipelines and preview environments.
  name: Sevalla Pipelines API
  slug: sevalla-pipelines-api
- baseURL: https://api.sevalla.com/v3
  baseurl_source: declared
  description: Build and deploy Git-backed static sites to the edge.
  name: Sevalla Static Sites API
  slug: sevalla-static-sites-api
artifact_total: 22
collections:
- collection_type: open
  name: Sevalla Applications API
  slug: open-sevalla-applications-api
- collection_type: open
  name: Sevalla Applications Company API
  slug: open-sevalla-company-api
- collection_type: open
  name: Sevalla Applications Databases API
  slug: open-sevalla-databases-api
- collection_type: open
  name: Sevalla Applications Deployments API
  slug: open-sevalla-deployments-api
- collection_type: open
  name: Sevalla Applications Object Storage API
  slug: open-sevalla-object-storage-api
- collection_type: open
  name: Sevalla Applications Pipelines API
  slug: open-sevalla-pipelines-api
- collection_type: open
  name: Sevalla Applications Static Sites API
  slug: open-sevalla-static-sites-api
- collection_type: open
  name: Sevalla API
  slug: open-sevalla
common:
- group: other
  href: https://artifacts.apis.io/sevalla/capabilities/sevalla-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/sevalla-capability-edges.yml
- group: agent
  href: https://artifacts.apis.io/sevalla/agentic-access/sevalla-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/sevalla-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/sevalla/security/sevalla-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/sevalla-domain-security.yml
- group: auth
  href: https://artifacts.apis.io/sevalla/authentication/sevalla-authentication.yml
  title: ''
  type: Authentication
  url: authentication/sevalla-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/sevalla-hosting
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/sevalla
- group: company
  title: ''
  type: Website
  url: https://sevalla.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.sevalla.com/
- group: commercial
  href: https://artifacts.apis.io/sevalla/plans/sevalla-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/sevalla-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/sevalla/rate-limits/sevalla-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/sevalla-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/sevalla/finops/sevalla-finops.yml
  title: ''
  type: FinOps
  url: finops/sevalla-finops.yml
- group: company
  title: ''
  type: Blog
  url: https://sevalla.com/blog/
created: '2026-07-01'
description: Sevalla is an application, database, and static-site hosting platform-as-a-service by Kinsta, built on Google Cloud Platform and Cloudflare. It lets teams deploy apps from Git or Docker, provision managed databases (PostgreSQL, MySQL, MariaDB, MongoDB, Redis, Valkey), host static sites on a global edge, and run S3-compatible object storage. The public REST API (base https://api.sevalla.com/v3, Bearer API token) exposes 200+ endpoints to manage the entire platform programmatically.
finops:
- has_sources: true
  method: generated
  name: Sevalla Finops
  primary_unit: ''
  service_category: Compute
  slug: sevalla-finops
  template: false
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/sevalla.png
layout: provider
mcp_servers:
- description: Remote MCP server at mcp.sevalla.com over HTTP.
  name: Sevalla MCP Server
  slug: sevalla
modified: '2026-07-01'
name: Sevalla
nav: Providers
network: true
overview: 'Sevalla publishes 7 API contracts indexed on the [APIs.io](https://apis.io/) network, including Applications API, Company API, Databases API, and 4 more. Tagged areas include Hosting, Platform-as-a-Service, Cloud, Deployment, and Database.


  Sevalla''s developer surface includes authentication, documentation, engineering blog, and 9 more developer resources.'
plans:
- name: Sevalla Plans Pricing
  plan_count: 4
  slug: sevalla-plans-pricing
random_paper: 0
rate_limits:
- limit_count: 5
  name: Sevalla Rate Limits
  slug: sevalla-rate-limits
score:
  band: thin
  composite: 26.7
  coverage:
    artifact_dirs: 15
    catalog_earned: 43.0
    catalog_earned_first_party: 0.0
    catalog_gap: 72.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 7.9
    contract_governance: 0.0
    contract_quality: 44.3
    developer_ergonomics: 31.0
    discoverability: 66.1
    operational_transparency: 13.2
  previous_composite: 26.7
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 7
    mcp: first-party
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 11.8
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/sevalla/sevalla-2026-09-02T155032.png
security:
- kind: authentication
  name: Sevalla Authentication
  slug: sevalla-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Sevalla Domain Security
  slug: sevalla-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: sevalla
tags:
- Hosting
- Platform-as-a-Service
- Cloud
- Deployment
- Database
- Static Sites
- Object Storage
website: https://sevalla.com/
---
