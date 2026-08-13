---
access_model:
  confidence: high
  label: Freemium (free trial) · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  trial: true
  try_now: true
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 30.6
  scored_at: '2026-08-12'
agentic_access:
- acting_count: 36
  human_in_the_loop: 1
  name: Drone Agentic Access
  operation_count: 61
  slug: drone-agentic-access
  summary_line: 61 operations · 36 acting · 1 human-in-the-loop
api_count: 10
apis:
- description: Build creation, management, and log access.
  name: Drone Builds API
  slug: drone-builds-api
- description: Cron job scheduling for automated builds.
  name: Drone Cron API
  slug: drone-cron-api
- description: Runner node management.
  name: Drone Nodes API
  slug: drone-nodes-api
- description: Build queue management.
  name: Drone Queue API
  slug: drone-queue-api
- description: Repository activation and management.
  name: Drone Repos API
  slug: drone-repos-api
- description: Secret variable management for repos and organizations.
  name: Drone Secrets API
  slug: drone-secrets-api
- description: System information.
  name: Drone System API
  slug: drone-system-api
- description: Reusable pipeline template management.
  name: Drone Templates API
  slug: drone-templates-api
- description: Current authenticated user operations.
  name: Drone User API
  slug: drone-user-api
- description: User account management (admin).
  name: Drone Users API
  slug: drone-users-api
artifact_total: 24
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/drone-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/drone-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/drone-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://www.drone.io/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.drone.io/
- group: build
  title: ''
  type: GitHubOrg
  url: https://github.com/drone
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/drone-io
- group: company
  title: ''
  type: Blog
  url: https://blog.drone.io
- group: commercial
  title: ''
  type: Pricing
  url: https://docs.drone.io/enterprise/
- group: other
  title: ''
  type: X
  url: https://twitter.com/droneio
- group: commercial
  title: ''
  type: Plans
  url: plans/drone-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/drone-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/drone-finops.yml
- group: company
  title: ''
  type: BlogRSS
  url: https://blog.drone.io/index.xml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/drone-vocabulary.yml
- group: design
  title: ''
  type: JSONLDContext
  url: json-ld/drone-context.jsonld
created: '2026-06-12'
description: Drone is an open-source, container-native continuous integration and continuous delivery platform that automates software build, testing, and deployment pipelines entirely through Docker containers. Acquired by Harness in 2021, Drone enables development teams to define pipelines as code using simple YAML configuration files committed alongside their source code. The platform provides a comprehensive REST API for managing builds, repositories, secrets, cron jobs, templates, and user accounts in both self-hosted and cloud deployments. Drone supports multiple source control providers including GitHub, GitHub Enterprise, Bitbucket, and GitLab, and is available as a free open-source edition (Apache 2 license) or a paid enterprise edition for larger organizations.
examples:
- key_count: 28
  name: Drone Build Example
  slug: drone-build-example
- key_count: 29
  name: Drone Repo Example
  slug: drone-repo-example
- key_count: 4
  name: Drone Secret Example
  slug: drone-secret-example
finops:
- name: Drone Finops
  service_category: ''
  slug: drone-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/drone.png
json_schemas:
- name: Build
  property_count: 35
  slug: drone-build
- name: Repository
  property_count: 29
  slug: drone-repo
- name: Secret
  property_count: 5
  slug: drone-secret
jsonld:
- class_count: 62
  name: Drone Context
  property_count: 0
  slug: drone-context
layout: provider
modified: '2026-06-12'
name: Drone
nav: Providers
network: true
overview: 'Drone publishes 10 APIs on the [APIs.io](https://apis.io/) network, including Builds API, Cron API, Nodes API, and 7 more. Tagged areas include CI/CD, Continuous Integration, Continuous Delivery, DevOps, and Containers.


  The Drone catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Drone''s developer surface includes authentication, documentation, engineering blog, pricing, and 12 more developer resources.'
plans:
- name: Drone Plans Pricing
  plan_count: 3
  slug: drone-plans-pricing
random_paper: 56
rate_limits:
- limit_count: 0
  name: Drone Rate Limits
  slug: drone-rate-limits
rules:
- name: Drone API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: drone-jsonschema-spectral-rules
score:
  band: developing
  composite: 46.5
  delta: 0.0
  facets:
    commercial_clarity: 50.0
    contract_quality: 63.1
    developer_ergonomics: 21.7
    discoverability: 74.1
    governance: 68.8
    operational_transparency: 5.3
  previous_composite: 46.5
  provenance:
    agentic_access: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 10
  schema_version: 0.11.0
  scored_at: '2026-08-12'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/drone/refs/heads/main/screenshots/drone-2026-06-20T180238.png
security:
- kind: authentication
  name: Drone Authentication
  slug: drone-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Drone Domain Security
  slug: drone-domain-security
  summary_line: TLSv1.3 · HSTS
slug: drone
tags:
- CI/CD
- Continuous Integration
- Continuous Delivery
- DevOps
- Containers
- Docker
- Build Automation
- Open Source
- Self-Hosted
website: https://www.drone.io/
---
