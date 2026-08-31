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
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: true
  schema_version: 0.2
  score: 14.2
  scored_at: '2026-08-30'
api_count: 2
apis:
- description: 'Akita Software provided an API observability platform that used passive traffic monitoring to automatically discover, map, and model APIs without requiring code changes or proxying. It could generate '
  name: Akita Software
  slug: akita-software
- description: Postman Live Insights is the successor to Akita Software, now integrated into the Postman platform. The Postman Insights Agent (open source) makes it easy to see the behavior of production APIs, disco
  name: Postman Live Insights
  slug: postman-live-insights
artifact_total: 21
common:
- group: operate
  title: ''
  type: Releases
  url: https://github.com/postmanlabs/postman-insights-agent/releases
- group: docs
  title: ''
  type: ContributionGuide
  url: https://github.com/postmanlabs/postman-insights-agent/blob/main/CONTRIBUTING.md
- group: commercial
  title: ''
  type: License
  url: https://github.com/postmanlabs/postman-insights-agent/blob/main/LICENSE
- group: auth
  title: ''
  type: DomainSecurity
  url: security/akita-software-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.akitasoftware.com
- group: docs
  title: ''
  type: Documentation
  url: https://learning.postman.com/docs/insights/overview/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/akitasoftware
- group: other
  title: ''
  type: X
  url: https://x.com/akitasoftware
- group: build
  title: ''
  type: Packages
  url: packages/akita-software-packages.yml
- group: build
  title: ''
  type: CLI
  url: cli/akita-software-cli.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/akita-software-changelog.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/akita-software-lifecycle.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/akita-software-authentication.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/akita-software-problem-types.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/akita-software-conventions.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/akita-software-llms.txt
- group: commercial
  title: ''
  type: Plans
  url: plans/akita-software-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/akita-software-rate-limits.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/akita-software/
created: '2025-01-08'
description: Akita Software was an API observability and analysis platform that used passive traffic monitoring to automatically map APIs, detect changes, and identify issues without requiring code changes or proxies. Akita was acquired by Postman in July 2023 (announced 2023-07-19) and its technology has been integrated into the Postman platform as Postman Live Insights. The Akita agent is now available as the open-source Postman Insights Agent.
features:
- description: Monitors API traffic passively without code changes, SDK installation, or proxying, minimizing operational overhead and risk.
  name: Passive Traffic Monitoring
- description: Generates OpenAPI specifications automatically from observed traffic, keeping documentation always up to date.
  name: Automatic API Spec Generation
- description: Detects breaking API changes by comparing observed traffic patterns across deployments and branches.
  name: Breaking Change Detection
- description: Tracks API response times, error rates, and traffic patterns to help identify performance regressions.
  name: API Performance Monitoring
- description: Integrates with Docker, Kubernetes, NGINX, Rails, Django, Flask, FastAPI, and Heroku for broad platform coverage.
  name: Multi-Platform Integration
finops:
- name: Akita Software Finops
  service_category: API
  slug: akita-software-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/akita-software.png
integrations:
- description: Docker extension and container integration for traffic monitoring
  name: Docker
- description: Kubernetes deployment support for monitoring microservice APIs
  name: Kubernetes
- description: NGINX module for mirroring API traffic to the Akita agent
  name: NGINX
- description: Heroku buildpack for integrating Akita with Heroku applications
  name: Heroku
- description: Acquired by Postman in 2023; technology integrated as Postman Live Insights
  name: Postman
layout: provider
modified: '2026-08-30'
name: Akita Software
nav: Providers
network: true
overview: 'Akita Software publishes 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Acquired, API Discovery, API Mapping, API Observability, and Traffic Analysis.


  Akita Software''s developer surface includes documentation, CLI, changelog, authentication, and 15 more developer resources.'
plans:
- name: Akita Software Plans Pricing
  plan_count: 0
  slug: akita-software-plans-pricing
random_paper: 14
rate_limits:
- limit_count: 0
  name: Akita Software Rate Limits
  slug: akita-software-rate-limits
score:
  band: emerging
  composite: 25.8
  coverage:
    artifact_dirs: 16
    catalog_gap: 80.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 8.8
  facets:
    access_clarity: 28.9
    commercial_clarity: 28.9
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 45.2
    discoverability: 59.3
    governance: 0.0
    operational_transparency: 18.4
  open_source:
    applies: true
    score: 50.0
  previous_composite: 17.0
  schema_version: 0.17.2
  scored_at: '2026-08-30'
  trend: rising
security:
- kind: authentication
  name: Akita Software Authentication
  slug: akita-software-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Akita Software Domain Security
  slug: akita-software-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: akita-software
tags:
- Acquired
- API Discovery
- API Mapping
- API Observability
- Traffic Analysis
use_cases:
- description: Engineering teams automatically generate and maintain up-to-date API specs from production traffic without manual effort.
  name: API Documentation Generation
- description: Teams detect unintentional API breaking changes between branches or deployments before they reach production.
  name: API Change Management
- description: Organizations discover undocumented and shadow APIs by monitoring actual network traffic across their services.
  name: API Discovery
- description: DevOps teams monitor API behavior and performance in production to quickly identify and diagnose issues.
  name: Production API Monitoring
website: https://www.akitasoftware.com
---
