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
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 2.5
  scored_at: '2026-08-26'
api_count: 1
apis:
- description: REST API for automating common tasks for debian, rpm, rubygems, python, npm, maven, and helm packages. Supports repository management, package upload and deletion, access token management, GPG key man
  name: packagecloud REST API
  slug: packagecloud-api
artifact_total: 6
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/packagecloud-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://packagecloud.io
- group: docs
  title: ''
  type: Documentation
  url: https://packagecloud.io/docs
- group: build
  title: ''
  type: GitHubOrg
  url: https://github.com/computology
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/packagecloud
- group: company
  title: ''
  type: Blog
  url: https://blog.packagecloud.io
- group: commercial
  title: ''
  type: Pricing
  url: https://packagecloud.io/pricing
- group: operate
  title: ''
  type: StatusPage
  url: https://www.packagecloudstatus.io/
- group: other
  title: ''
  type: X
  url: https://x.com/packagecloudio
- group: commercial
  title: ''
  type: Plans
  url: plans/packagecloud-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/packagecloud-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/packagecloud-finops.yml
created: 2026-06-13
description: packagecloud is a hosted private package repository service with a REST API for managing repositories, uploading and distributing packages across formats including deb, rpm, gem, npm, maven, python, and helm charts. The API enables automation of package lifecycle management, access control via tokens, GPG key management, download statistics, and package promotion across repositories.
finops:
- name: Packagecloud Finops
  service_category: ''
  slug: packagecloud-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/packagecloud.png
jsonld:
- class_count: 10
  name: Packagecloud Context
  property_count: 16
  slug: packagecloud-context
layout: provider
modified: 2026-06-13
name: packagecloud
nav: Providers
network: true
overview: 'packagecloud publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Package Management, Repository Hosting, DevOps, Debian, and RPM.


  The packagecloud catalog on APIs.io includes 1 JSON-LD context.


  packagecloud''s developer surface includes documentation, engineering blog, pricing, and 9 more developer resources.'
plans:
- name: Packagecloud Plans Pricing
  plan_count: 4
  slug: packagecloud-plans-pricing
random_paper: 12
rate_limits:
- limit_count: 4
  name: Packagecloud Rate Limits
  slug: packagecloud-rate-limits
score:
  band: thin
  composite: 29.7
  delta: 0.0
  facets:
    access_clarity: 50.0
    commercial_clarity: 50.0
    contract_governance: 0.0
    contract_quality: 14.7
    developer_ergonomics: 11.9
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 52.6
  previous_composite: 29.7
  schema_version: 0.15.0
  scored_at: '2026-08-26'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/packagecloud/refs/heads/main/screenshots/packagecloud-2026-06-20T191309.png
security:
- kind: domain-security
  name: Packagecloud Domain Security
  slug: packagecloud-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: packagecloud
tags:
- Package Management
- Repository Hosting
- DevOps
- Debian
- RPM
- RubyGems
- npm
- Maven
- Helm
- CI/CD
website: https://packagecloud.io
---
