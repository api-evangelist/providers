---
access_model:
  confidence: medium
  label: Free
  onboarding: unknown
  pricing: free
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
api_count: 3
apis:
- description: REST API used to trigger and manage test executions, query test run status, and retrieve results for tests authored in Testim. Authentication is via a personal access token issued from the Testim work
  name: Testim REST API
  slug: rest
- description: Authoring and execution surface for HTTP API tests inside Testim. Lets teams compose, chain, assert, and run API test steps alongside UI tests from the same Testim project, and trigger them via the Te
  name: Testim API Testing
  slug: api-testing
- description: Command-line interface used to run Testim tests locally and from CI/CD pipelines (Jenkins, GitHub Actions, GitLab CI, CircleCI, Azure DevOps). Accepts a project token and test/suite identifiers and st
  name: Testim CLI
  slug: cli
artifact_total: 7
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/testim-domain-security.yml
- group: company
  title: ''
  type: Blog
  url: https://www.testim.io/feed/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/testim-io
- group: company
  title: ''
  type: Website
  url: https://www.testim.io/
- group: docs
  title: ''
  type: Documentation
  url: https://help.testim.io/docs/testim-overview
- group: build
  title: ''
  type: GitHub
  url: https://github.com/testimio
- group: operate
  title: ''
  type: ChangeLog
  url: https://help.testim.io/changelog
- group: other
  title: ''
  type: Parent
  url: https://www.tricentis.com/
- group: commercial
  title: ''
  type: Plans
  url: plans/testim-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/testim-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/testim-finops.yml
created: '2026-05-23'
description: Testim (acquired by Tricentis in 2022) is an AI-powered functional and end-to-end test automation platform. The platform records, runs, and stabilises codeless and code-based UI tests using AI-driven Smart Locators that learn DOM changes and reduce flakiness. Testim covers web, mobile web, Salesforce, and Mainframe testing, ships a Testim CLI for CI/CD integration, and exposes a REST API for triggering test runs and retrieving execution results. Most platform endpoints are partner-gated behind a workspace login and account-issued API token.
finops:
- name: Testim Finops
  service_category: API
  slug: testim-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/testim.png
layout: provider
modified: '2026-05-23'
name: Testim
nav: Providers
network: true
overview: 'Testim publishes 3 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Testing, Test Automation, QA, AI Testing, and End-to-End Testing.


  Testim''s developer surface includes engineering blog, documentation, GitHub presence, changelog, and 7 more developer resources.'
plans:
- name: Testim Plans Pricing
  plan_count: 1
  slug: testim-plans-pricing
random_paper: 46
rate_limits:
- limit_count: 2
  name: Testim Rate Limits
  slug: testim-rate-limits
score:
  band: emerging
  composite: 20.8
  delta: -2.6
  facets:
    commercial_clarity: 28.9
    contract_quality: 0.0
    developer_ergonomics: 10.9
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 42.1
  previous_composite: 23.4
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/testim/refs/heads/main/screenshots/testim-2026-06-20T195153.png
security:
- kind: domain-security
  name: Testim Domain Security
  slug: testim-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: testim
tags:
- Testing
- Test Automation
- QA
- AI Testing
- End-to-End Testing
- CI/CD
website: https://www.testim.io/
---
