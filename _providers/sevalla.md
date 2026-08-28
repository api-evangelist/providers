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
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 21.5
  scored_at: '2026-08-26'
agentic_access:
- acting_count: 19
  human_in_the_loop: 0
  name: Sevalla Agentic Access
  operation_count: 36
  slug: sevalla-agentic-access
  summary_line: 36 operations · 19 acting
api_count: 7
apis:
- description: Deploy and manage applications from Git or Docker.
  name: Sevalla Applications API
  slug: sevalla-applications-api
- description: Company users, projects, usage, and API keys.
  name: Sevalla Company API
  slug: sevalla-company-api
- description: Provision and manage managed databases.
  name: Sevalla Databases API
  slug: sevalla-databases-api
- description: Trigger, inspect, and roll back deployments.
  name: Sevalla Deployments API
  slug: sevalla-deployments-api
- description: S3-compatible object storage buckets.
  name: Sevalla Object Storage API
  slug: sevalla-object-storage-api
- description: Multi-stage promotion pipelines and preview environments.
  name: Sevalla Pipelines API
  slug: sevalla-pipelines-api
- description: Build and deploy Git-backed static sites to the edge.
  name: Sevalla Static Sites API
  slug: sevalla-static-sites-api
artifact_total: 22
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
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
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/sevalla-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/sevalla-domain-security.yml
- group: auth
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
  title: ''
  type: Plans
  url: plans/sevalla-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/sevalla-rate-limits.yml
- group: commercial
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
- name: Sevalla Finops
  service_category: Compute
  slug: sevalla-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/sevalla.png
layout: provider
modified: '2026-07-01'
name: Sevalla
nav: Providers
network: true
overview: 'Sevalla publishes 7 APIs on the [APIs.io](https://apis.io/) network, including Applications API, Company API, Databases API, and 4 more. Tagged areas include Hosting, Platform-as-a-Service, Cloud, Deployment, and Databases.


  Sevalla''s developer surface includes authentication, documentation, engineering blog, and 8 more developer resources.'
plans:
- name: Sevalla Plans Pricing
  plan_count: 4
  slug: sevalla-plans-pricing
random_paper: 9
rate_limits:
- limit_count: 5
  name: Sevalla Rate Limits
  slug: sevalla-rate-limits
score:
  band: thin
  composite: 38.7
  delta: 1.4
  facets:
    access_clarity: 39.5
    commercial_clarity: 39.5
    contract_governance: 0.0
    contract_quality: 51.0
    developer_ergonomics: 31.0
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 34.2
  previous_composite: 37.3
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 7
  schema_version: 0.15.0
  scored_at: '2026-08-26'
  trend: flat
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
- Databases
- Static Sites
- Object Storage
website: https://sevalla.com/
---
