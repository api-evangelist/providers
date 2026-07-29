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
- acting_count: 7
  human_in_the_loop: 0
  name: Testmo Agentic Access
  operation_count: 23
  slug: testmo-agentic-access
  summary_line: 23 operations · 7 acting
api_count: 7
apis:
- description: Automation runs submitted from CI/CD, with aggregated statistics.
  name: Testmo Automation Runs API
  slug: testmo-automation-runs-api
- description: Automation sources grouping runs, with aggregated metrics.
  name: Testmo Automation Sources API
  slug: testmo-automation-sources-api
- description: Milestones and their linked run and session statistics.
  name: Testmo Milestones API
  slug: testmo-milestones-api
- description: Top-level projects that contain runs, sessions, milestones, and cases.
  name: Testmo Projects API
  slug: testmo-projects-api
- description: Exploratory test sessions and session note statistics.
  name: Testmo Sessions API
  slug: testmo-sessions-api
- description: Beta read/write API for cases, folders, and attachments.
  name: Testmo Test Case Management API
  slug: testmo-test-case-management-api
- description: Manual test runs and their individual results.
  name: Testmo Test Runs API
  slug: testmo-test-runs-api
artifact_total: 13
collections:
- collection_type: open
  name: Testmo REST API
  slug: open-testmo
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/testmo-agentic-access.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/testmo-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/testmo
- group: company
  title: ''
  type: Website
  url: https://www.testmo.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.testmo.com/
- group: commercial
  title: ''
  type: Plans
  url: plans/testmo-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/testmo-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/testmo-finops.yml
- group: company
  title: ''
  type: Blog
  url: https://www.testmo.com/blog/
created: '2026-07-11'
description: Testmo is a unified test management platform that brings manual test cases, test automation, and exploratory testing together in one tool, with reporting, milestones, and issue-tracker and CI integrations. Testmo exposes a documented REST API (per-instance base https://{instance}.testmo.net/api/v1, Bearer API-token auth) that reads projects, test runs, run results, automation runs, automation sources, exploratory sessions, and milestones for custom analytics, reporting, and integrations - plus a beta test case management API and a CLI (@testmo/testmo-cli) that submits automation results from CI/CD pipelines.
finops:
- name: Testmo Finops
  service_category: Software as a Service - Test Management
  slug: testmo-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/testmo.png
layout: provider
modified: '2026-07-11'
name: Testmo
nav: Providers
network: true
overview: 'Testmo publishes 7 APIs on the [APIs.io](https://apis.io/) network, including Automation Runs API, Automation Sources API, Milestones API, and 4 more. Tagged areas include Test Runs, Test Management, Test Automation, QA, and Exploratory Testing.


  Testmo''s developer surface includes authentication, documentation, engineering blog, and 6 more developer resources.'
plans:
- name: Testmo Plans Pricing
  plan_count: 4
  slug: testmo-plans-pricing
random_paper: 28
rate_limits:
- limit_count: 5
  name: Testmo Rate Limits
  slug: testmo-rate-limits
score:
  band: thin
  composite: 38.8
  delta: -2.1
  facets:
    commercial_clarity: 39.5
    contract_quality: 60.2
    developer_ergonomics: 21.7
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 31.6
  previous_composite: 40.9
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 7
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
security:
- kind: authentication
  name: Testmo Authentication
  slug: testmo-authentication
  summary_line: http · 1 scheme
slug: testmo
tags:
- Test Runs
- Test Management
- Test Automation
- QA
- Exploratory Testing
- CI/CD
- Quality Assurance
website: https://www.testmo.com/
---
