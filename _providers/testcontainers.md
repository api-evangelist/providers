---
access_model:
  confidence: medium
  label: Freemium (free trial)
  onboarding: unknown
  pricing: freemium
  public: false
  source:
  - plans
  trial: true
  try_now: false
agent_readiness:
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    asyncapi_events: false
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 3.2
  scored_at: '2026-07-28'
api_count: 2
apis:
- description: The Testcontainers Cloud Agent API enables CI/CD pipelines and desktop environments to allocate hosted Docker container workers in the cloud. Authentication is performed via TC_CLOUD_TOKEN service acc
  name: Testcontainers Cloud Agent API
  slug: cloud-agent-api
- description: A family of open-source libraries providing a programmatic API for spinning up and tearing down Docker containers in automated tests. Implementations exist for Java, Go, .NET, Node.js, Python, Rust, H
  name: Testcontainers Open-Source Libraries
  slug: open-source-libraries
artifact_total: 7
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/testcontainers-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://testcontainers.com/
- group: docs
  title: ''
  type: Documentation
  url: https://testcontainers.com/cloud/docs/
- group: start
  title: ''
  type: GettingStarted
  url: https://testcontainers.com/getting-started/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/testcontainers
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/atomicjar
- group: company
  title: ''
  type: Blog
  url: https://atomicjar.com/category/testcontainers/
- group: company
  title: ''
  type: Newsletter
  url: https://newsletter.testcontainers.com/
- group: commercial
  title: ''
  type: Pricing
  url: https://testcontainers.com/cloud/pricing/
- group: other
  title: ''
  type: X
  url: https://x.com/testcontainers
- group: operate
  title: ''
  type: Slack
  url: https://slack.testcontainers.org/
- group: commercial
  title: ''
  type: Plans
  url: plans/testcontainers-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/testcontainers-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/testcontainers-finops.yml
- group: company
  title: ''
  type: BlogFeed
  url: blogs/blogs.json
- group: design
  title: ''
  type: JSONLDContext
  url: json-ld/testcontainers-context.jsonld
created: '2026-06-12'
description: Testcontainers is an open-source library ecosystem that provides throwaway, lightweight Docker container instances for integration testing across more than a dozen programming languages including Java, Go, .NET, Node.js, and Python. Developers define real test dependencies — databases, message brokers, browsers — as code rather than relying on mocks or shared environments. Testcontainers Cloud extends the library to a hosted container runtime service that runs container-backed tests in the cloud, eliminating the need for a local Docker daemon and enabling parallel execution in CI/CD pipelines. The platform authenticates via a TC_CLOUD_TOKEN environment variable or service account token, and usage is metered in Worker Minutes bundled with Docker Pro, Team, and Business subscriptions.
finops:
- name: Testcontainers Finops
  service_category: Developer Tools
  slug: testcontainers-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/testcontainers.png
jsonld:
- class_count: 10
  name: Testcontainers Context
  property_count: 8
  slug: testcontainers-context
layout: provider
modified: '2026-06-12'
name: Testcontainers
nav: Providers
network: true
overview: 'Testcontainers publishes 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Testing, Integration Testing, Docker, Containers, and CI/CD.


  The Testcontainers catalog on APIs.io includes 1 JSON-LD context.


  Testcontainers'' developer surface includes documentation, getting-started guide, engineering blog, pricing, and 12 more developer resources.'
plans:
- name: Testcontainers Plans Pricing
  plan_count: 5
  slug: testcontainers-plans-pricing
random_paper: 68
rate_limits:
- limit_count: 6
  name: Testcontainers Rate Limits
  slug: testcontainers-rate-limits
score:
  band: thin
  composite: 29.2
  delta: -2.9
  facets:
    commercial_clarity: 50.0
    contract_quality: 12.9
    developer_ergonomics: 21.7
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 36.8
  previous_composite: 32.1
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/testcontainers/refs/heads/main/screenshots/testcontainers-2026-06-20T195150.png
security:
- kind: domain-security
  name: Testcontainers Domain Security
  slug: testcontainers-domain-security
  summary_line: TLSv1.3 · HSTS
slug: testcontainers
tags:
- Testing
- Integration Testing
- Docker
- Containers
- CI/CD
- Developer Tools
website: https://testcontainers.com/
---
