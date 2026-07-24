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
  band: agent-ready
  dimensions:
    agent_skills: false
    agentic_access: true
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: true
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.1
  score: 48.1
  scored_at: '2026-07-23'
agentic_access:
- acting_count: 32
  human_in_the_loop: 0
  name: Testrail Agentic Access
  operation_count: 56
  slug: testrail-agentic-access
  summary_line: 56 operations · 32 acting
api_count: 11
apis:
- description: Reusable test cases in the repository.
  name: TestRail Cases API
  slug: testrail-cases-api
- description: Configuration groups (e.g. browsers, OSes) plan entries expand across.
  name: TestRail Configurations API
  slug: testrail-configurations-api
- description: Releases and deadlines that runs and plans report toward.
  name: TestRail Milestones API
  slug: testrail-milestones-api
- description: Groups of runs, optionally across configurations.
  name: TestRail Plans API
  slug: testrail-plans-api
- description: Top-level containers owning suites, cases, runs, plans, and milestones.
  name: TestRail Projects API
  slug: testrail-projects-api
- description: Recorded outcomes for tests and cases.
  name: TestRail Results API
  slug: testrail-results-api
- description: Executions of a set of test cases (test runs).
  name: TestRail Runs API
  slug: testrail-runs-api
- description: Folder-like grouping of test cases inside a suite.
  name: TestRail Sections API
  slug: testrail-sections-api
- description: Collections of test cases within a project.
  name: TestRail Suites API
  slug: testrail-suites-api
- description: Instances of a case within a specific run.
  name: TestRail Tests API
  slug: testrail-tests-api
- description: TestRail user lookup.
  name: TestRail Users API
  slug: testrail-users-api
artifact_total: 17
collections:
- collection_type: open
  name: TestRail API (v2)
  slug: open-testrail
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/testrail-agentic-access.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/testrail-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/testrail
- group: company
  title: ''
  type: Website
  url: https://www.testrail.com
- group: docs
  title: ''
  type: Documentation
  url: https://support.testrail.com/hc/en-us/articles/7077083596436-Introduction-to-the-TestRail-API
- group: commercial
  title: ''
  type: Plans
  url: plans/testrail-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/testrail-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/testrail-finops.yml
- group: commercial
  title: ''
  type: Pricing
  url: https://www.testrail.com/pricing/
created: '2026-07-11'
description: TestRail is a web-based test case management and QA platform (originally by Gurock, now part of IDERA) for organizing test cases, running test runs and test plans, and recording test results across manual and automated testing. Its HTTP API (v2) exposes projects, suites, sections, cases, runs, plans, tests, results, milestones, configurations, and users so teams can push automated results, create and close test runs, and sync test cases programmatically. The API is available on TestRail Cloud (per-instance host, e.g. https://{instance}.testrail.io) and on self-hosted TestRail Server/Enterprise, and uses the distinctive index.php?/api/v2/ URL style with HTTP Basic authentication (email plus password or API key).
finops:
- name: Testrail Finops
  service_category: Software and Development Tools
  slug: testrail-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/testrail.png
layout: provider
modified: '2026-07-11'
name: TestRail
nav: Providers
network: true
overview: 'TestRail publishes 11 APIs on the [APIs.io](https://apis.io/) network, including Cases API, Configurations API, Milestones API, and 8 more. Tagged areas include Test Runs, Test Management, QA, Test Cases, and Test Results.


  TestRail''s developer surface includes authentication, documentation, pricing, and 6 more developer resources.'
plans:
- name: Testrail Plans Pricing
  plan_count: 4
  slug: testrail-plans-pricing
random_paper: 5
rate_limits:
- limit_count: 4
  name: Testrail Rate Limits
  slug: testrail-rate-limits
score:
  band: thin
  composite: 38.6
  delta: 0.0
  facets:
    commercial_clarity: 50.0
    contract_quality: 55.2
    developer_ergonomics: 19.6
    discoverability: 67.5
    governance: 0.0
    operational_transparency: 31.6
  previous_composite: 38.6
  schema_version: 0.5
  scored_at: '2026-07-23'
  trend: flat
security:
- kind: authentication
  name: Testrail Authentication
  slug: testrail-authentication
  summary_line: http · 1 scheme
slug: testrail
tags:
- Test Runs
- Test Management
- QA
- Test Cases
- Test Results
- Test Plans
- Testing
- Test Automation
website: https://www.testrail.com
---
