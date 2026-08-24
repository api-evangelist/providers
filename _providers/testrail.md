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
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 29.1
  scored_at: '2026-08-24'
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
artifact_total: 29
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: TestRail API (v2) Cases API
  slug: open-testrail-cases-api
- collection_type: open
  name: TestRail API (v2) Cases Configurations API
  slug: open-testrail-configurations-api
- collection_type: open
  name: TestRail API (v2) Cases Milestones API
  slug: open-testrail-milestones-api
- collection_type: open
  name: TestRail API (v2) Cases Plans API
  slug: open-testrail-plans-api
- collection_type: open
  name: TestRail API (v2) Cases Projects API
  slug: open-testrail-projects-api
- collection_type: open
  name: TestRail API (v2) Cases Results API
  slug: open-testrail-results-api
- collection_type: open
  name: TestRail API (v2) Cases Runs API
  slug: open-testrail-runs-api
- collection_type: open
  name: TestRail API (v2) Cases Sections API
  slug: open-testrail-sections-api
- collection_type: open
  name: TestRail API (v2) Cases Suites API
  slug: open-testrail-suites-api
- collection_type: open
  name: TestRail API (v2) Cases Tests API
  slug: open-testrail-tests-api
- collection_type: open
  name: TestRail API (v2) Cases Users API
  slug: open-testrail-users-api
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
random_paper: 11
rate_limits:
- limit_count: 4
  name: Testrail Rate Limits
  slug: testrail-rate-limits
score:
  band: developing
  composite: 39.5
  delta: 0.0
  facets:
    access_clarity: 50.0
    commercial_clarity: 50.0
    contract_governance: 0.0
    contract_quality: 54.8
    developer_ergonomics: 21.4
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 31.6
  previous_composite: 39.5
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 11
  schema_version: 0.12.1
  scored_at: '2026-08-24'
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
