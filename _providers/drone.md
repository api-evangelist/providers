---
access_model:
  confidence: medium
  label: Freemium (free trial) · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  - security
  trial: true
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
  scored_at: '2026-09-04'
agentic_access:
- acting_count: 36
  human_in_the_loop: 1
  name: Drone Agentic Access
  operation_count: 61
  slug: drone-agentic-access
  summary_line: 61 operations · 36 acting · 1 human-in-the-loop
api_count: 1
apis:
- baseURL: https://your-drone-server/api
  baseurl_source: declared
  description: Build creation, management, and log access.
  name: Drone Builds API
  slug: drone-builds-api
- baseURL: https://your-drone-server/api
  baseurl_source: declared
  description: Cron job scheduling for automated builds.
  name: Drone Cron API
  slug: drone-cron-api
- baseURL: https://your-drone-server/api
  baseurl_source: declared
  description: Runner node management.
  name: Drone Nodes API
  slug: drone-nodes-api
- baseURL: https://your-drone-server/api
  baseurl_source: declared
  description: Build queue management.
  name: Drone Queue API
  slug: drone-queue-api
- baseURL: https://your-drone-server/api
  baseurl_source: declared
  description: Repository activation and management.
  name: Drone Repos API
  slug: drone-repos-api
- baseURL: https://your-drone-server/api
  baseurl_source: declared
  description: Secret variable management for repos and organizations.
  name: Drone Secrets API
  slug: drone-secrets-api
- baseURL: https://your-drone-server/api
  baseurl_source: declared
  description: System information.
  name: Drone System API
  slug: drone-system-api
- baseURL: https://your-drone-server/api
  baseurl_source: declared
  description: Reusable pipeline template management.
  name: Drone Templates API
  slug: drone-templates-api
- baseURL: https://your-drone-server/api
  baseurl_source: declared
  description: Current authenticated user operations.
  name: Drone User API
  slug: drone-user-api
- baseURL: https://your-drone-server/api
  baseurl_source: declared
  description: User account management (admin).
  name: Drone Users API
  slug: drone-users-api
- description: Bearer-token authenticated REST API exposed by every Drone server. Endpoints under /api/ for repos, builds, cron, secrets, users, templates, logs and queue status. Default port 8080.
  name: Drone Server REST API
  slug: rest
- description: The Builds API from Drone — 9 operation(s) for builds.
  name: Drone Builds API
  slug: drone-ci-builds-api
- description: The Cron API from Drone — 1 operation(s) for cron.
  name: Drone Cron API
  slug: drone-ci-cron-api
- description: The Secrets API from Drone — 1 operation(s) for secrets.
  name: Drone Secrets API
  slug: drone-ci-secrets-api
- description: The Templates API from Drone — 1 operation(s) for templates.
  name: Drone Templates API
  slug: drone-ci-templates-api
- description: The User API from Drone — 1 operation(s) for user.
  name: Drone User API
  slug: drone-ci-user-api
artifact_total: 41
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Drone REST Builds API
  slug: open-drone-builds-api
- collection_type: open
  name: Drone REST Builds Cron API
  slug: open-drone-cron-api
- collection_type: open
  name: Drone REST Builds Nodes API
  slug: open-drone-nodes-api
- collection_type: open
  name: Drone REST Builds Queue API
  slug: open-drone-queue-api
- collection_type: open
  name: Drone REST Builds Repos API
  slug: open-drone-repos-api
- collection_type: open
  name: Drone REST Builds Secrets API
  slug: open-drone-secrets-api
- collection_type: open
  name: Drone REST Builds System API
  slug: open-drone-system-api
- collection_type: open
  name: Drone REST Builds Templates API
  slug: open-drone-templates-api
- collection_type: open
  name: Drone REST Builds User API
  slug: open-drone-user-api
- collection_type: open
  name: Drone REST Builds Users API
  slug: open-drone-users-api
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
- group: company
  title: ''
  type: Blog
  url: https://www.harness.io/blog/rss.xml
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
overview: 'Drone publishes 15 APIs on the [APIs.io](https://apis.io/) network, including Builds API, Cron API, Nodes API, and 12 more. Tagged areas include CI/CD, Continuous Integration, Continuous Delivery, DevOps, and Containers.


  The Drone catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Drone''s developer surface includes authentication, documentation, engineering blog, pricing, and 13 more developer resources.'
plans:
- name: Drone Plans Pricing
  plan_count: 3
  slug: drone-plans-pricing
random_paper: 11
rate_limits:
- limit_count: 0
  name: Drone Rate Limits
  slug: drone-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: Drone API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: drone-jsonschema-spectral-rules
score:
  band: developing
  composite: 42.0
  coverage:
    artifact_dirs: 15
    catalog_earned: 68.3
    catalog_earned_first_party: 0.0
    catalog_gap: 46.8
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 50.0
    commercial_clarity: 50.0
    contract_governance: 25.0
    contract_quality: 61.2
    developer_ergonomics: 31.0
    discoverability: 68.5
    governance: 25.0
    operational_transparency: 5.3
  previous_composite: 42.0
  provenance:
    agentic_access: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 10
  schema_version: 0.18.3
  scored_at: '2026-09-04'
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
- Open-Source
- Self-Hosted
website: https://www.drone.io/
---
