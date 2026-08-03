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
  scored_at: '2026-08-03'
agentic_access:
- acting_count: 23
  human_in_the_loop: 0
  name: Qase Agentic Access
  operation_count: 37
  slug: qase-agentic-access
  summary_line: 37 operations · 23 acting
api_count: 7
apis:
- description: Test cases stored in a project repository.
  name: Qase cases API
  slug: qase-cases-api
- description: Defects raised against failed test results.
  name: Qase defects API
  slug: qase-defects-api
- description: Test plans - reusable selections of test cases.
  name: Qase plans API
  slug: qase-plans-api
- description: Test projects that contain cases, suites, runs, and results.
  name: Qase projects API
  slug: qase-projects-api
- description: Test run results, including bulk publishing from CI/automation.
  name: Qase results API
  slug: qase-results-api
- description: Test runs - executions of selected test cases in a project.
  name: Qase runs API
  slug: qase-runs-api
- description: Test suites that group and organize test cases.
  name: Qase suites API
  slug: qase-suites-api
artifact_total: 13
collections:
- collection_type: open
  name: Qase TestOps API v1
  slug: open-qase
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/qase-agentic-access.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/qase-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/qase-tms
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/qaseio
- group: company
  title: ''
  type: Website
  url: https://qase.io
- group: docs
  title: ''
  type: Documentation
  url: https://developers.qase.io
- group: commercial
  title: ''
  type: Plans
  url: plans/qase-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/qase-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/qase-finops.yml
- group: build
  title: ''
  type: SourceCode
  url: https://github.com/qase-tms/specs
- group: company
  title: ''
  type: Blog
  url: https://qase.io/blog/
created: '2026-07-11'
description: Qase is a cloud test management platform (TestOps) for QA and engineering teams to author test cases, organize them into suites and plans, launch and complete test runs, publish automated results from CI pipelines, and track defects. The Qase TestOps API v1 is a token-authenticated REST API at https://api.qase.io/v1 covering Projects, Test Cases, Suites, Test Runs, Test Results, Defects, and Plans, with a machine-readable OpenAPI specification published on GitHub (qase-tms/specs) and pre-generated clients for PHP, Python, JavaScript/TypeScript, Java, and Go. Automation reporters use the bulk results endpoint to publish test run results directly from CI.
finops:
- name: Qase Finops
  service_category: Software - Test Management
  slug: qase-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/qase.png
layout: provider
modified: '2026-07-11'
name: Qase
nav: Providers
network: true
overview: 'Qase publishes 7 APIs on the [APIs.io](https://apis.io/) network, including cases API, defects API, plans API, and 4 more. Tagged areas include Test Runs, Test Management, Test Cases, QA, and Testing.


  Qase''s developer surface includes authentication, documentation, engineering blog, and 8 more developer resources.'
plans:
- name: Qase Plans Pricing
  plan_count: 4
  slug: qase-plans-pricing
random_paper: 46
rate_limits:
- limit_count: 3
  name: Qase Rate Limits
  slug: qase-rate-limits
score:
  band: thin
  composite: 40.3
  delta: 0.0
  facets:
    commercial_clarity: 39.5
    contract_quality: 63.6
    developer_ergonomics: 21.7
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 36.8
  previous_composite: 40.3
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 7
  schema_version: 0.9
  scored_at: '2026-08-03'
  trend: flat
security:
- kind: authentication
  name: Qase Authentication
  slug: qase-authentication
  summary_line: apiKey · 1 scheme
slug: qase
tags:
- Test Runs
- Test Management
- Test Cases
- QA
- Testing
- TestOps
- Test Results
- Defects
- Quality Assurance
- Test Automation
website: https://qase.io
---
