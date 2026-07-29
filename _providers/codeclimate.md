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
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 30.6
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 4
  human_in_the_loop: 0
  name: Codeclimate Agentic Access
  operation_count: 15
  slug: codeclimate-agentic-access
  summary_line: 15 operations · 4 acting
api_count: 6
apis:
- description: The Issues API from Code Climate — 1 operation(s) for issues.
  name: Code Climate Issues API
  slug: codeclimate-issues-api
- description: The Organizations API from Code Climate — 2 operation(s) for organizations.
  name: Code Climate Organizations API
  slug: codeclimate-organizations-api
- description: The Repositories API from Code Climate — 4 operation(s) for repositories.
  name: Code Climate Repositories API
  slug: codeclimate-repositories-api
- description: The Services API from Code Climate — 1 operation(s) for services.
  name: Code Climate Services API
  slug: codeclimate-services-api
- description: The Snapshots API from Code Climate — 1 operation(s) for snapshots.
  name: Code Climate Snapshots API
  slug: codeclimate-snapshots-api
- description: The Test Coverage API from Code Climate — 5 operation(s) for test coverage.
  name: Code Climate Test Coverage API
  slug: codeclimate-test-coverage-api
artifact_total: 14
collections:
- collection_type: open
  name: Code Climate Quality API
  slug: open-codeclimate
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/codeclimate-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/codeclimate-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/codeclimate-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/codeclimate-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/codeclimate
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/code-climate
- group: company
  title: ''
  type: Website
  url: https://codeclimate.com
- group: docs
  title: ''
  type: Documentation
  url: https://developer.codeclimate.com/
- group: commercial
  title: ''
  type: Plans
  url: plans/codeclimate-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/codeclimate-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/codeclimate-finops.yml
- group: company
  title: ''
  type: Blog
  url: http://codeclimate.com/blog
created: '2026-06-21'
description: Code Climate provides automated code review and engineering intelligence for software teams. The Quality REST API (v1) exposes organizations, repositories, maintainability and test-coverage analysis, snapshots, and issues, while Velocity surfaces engineering analytics across the software delivery lifecycle.
finops:
- name: Codeclimate Finops
  service_category: Developer Tools
  slug: codeclimate-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/codeclimate.png
layout: provider
modified: '2026-06-21'
name: Code Climate
nav: Providers
network: true
overview: 'Code Climate publishes 6 APIs on the [APIs.io](https://apis.io/) network, including Issues API, Organizations API, Repositories API, and 3 more. Tagged areas include Code Quality, Static Analysis, Test Coverage, Engineering Analytics, and DevOps.


  Code Climate''s developer surface includes authentication, documentation, engineering blog, and 9 more developer resources.'
plans:
- name: Codeclimate Plans Pricing
  plan_count: 4
  slug: codeclimate-plans-pricing
random_paper: 26
rate_limits:
- limit_count: 3
  name: Codeclimate Rate Limits
  slug: codeclimate-rate-limits
score:
  band: thin
  composite: 38.0
  delta: -3.0
  facets:
    commercial_clarity: 39.5
    contract_quality: 54.2
    developer_ergonomics: 21.7
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 36.8
  previous_composite: 41.0
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 6
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/codeclimate/refs/heads/main/screenshots/codeclimate-2026-07-25T205913.png
security:
- kind: authentication
  name: Codeclimate Authentication
  slug: codeclimate-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Codeclimate Domain Security
  slug: codeclimate-domain-security
  summary_line: TLSv1.2 · HSTS
- kind: vulnerability-disclosure
  name: Codeclimate Vulnerability Disclosure
  slug: codeclimate-vulnerability-disclosure
  summary_line: disclosure policy published
slug: codeclimate
tags:
- Code Quality
- Static Analysis
- Test Coverage
- Engineering Analytics
- DevOps
website: https://codeclimate.com
---
