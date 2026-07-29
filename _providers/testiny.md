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
- acting_count: 28
  human_in_the_loop: 0
  name: Testiny Agentic Access
  operation_count: 43
  slug: testiny-agentic-access
  summary_line: 43 operations · 28 acting
api_count: 5
apis:
- description: Automated test cases and test runs submitted from CI/CD.
  name: Testiny Automation API
  slug: testiny-automation-api
- description: Top-level containers for test cases, plans, and runs.
  name: Testiny Projects API
  slug: testiny-projects-api
- description: Manual and automated test cases, folders, and saved queries.
  name: Testiny Test Cases API
  slug: testiny-test-cases-api
- description: Curated selections of test cases executed as runs.
  name: Testiny Test Plans API
  slug: testiny-test-plans-api
- description: Executions of test cases with recorded results.
  name: Testiny Test Runs API
  slug: testiny-test-runs-api
artifact_total: 12
collections:
- collection_type: open
  name: Testiny API
  slug: open-testiny
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/testiny-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/testiny-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/testiny-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/testiny
- group: company
  title: ''
  type: Website
  url: https://www.testiny.io
- group: docs
  title: ''
  type: Documentation
  url: https://www.testiny.io/docs/
- group: start
  title: ''
  type: SignUp
  url: https://app.testiny.io/
- group: commercial
  title: ''
  type: Plans
  url: plans/testiny-plans-pricing.yml
- group: commercial
  title: ''
  type: Pricing
  url: https://www.testiny.io/pricing/
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/testiny-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/testiny-finops.yml
created: '2026-07-11'
description: Testiny is a modern test management platform for QA teams that keeps manual and automated test cases, test plans, test runs, and results in a single place, with reporting and integrations for Jira, GitLab, and GitHub. Everything in the product is backed by a documented REST API (base https://app.testiny.io/api/v1, authenticated with an X-Api-Key header) that exposes projects, test cases, test case folders, test plans, test runs, and automated test runs and results over a consistent CRUD/find/bulk/mapping pattern. Testiny publishes an OpenAPI schema at https://app.testiny.io/api/v1/swagger.json, ships a CLI and npm package (@testiny/cli), and offers an HTTP MCP server so AI assistants can manage test cases, runs, and results. Testiny is available as a hosted cloud service and, for Custom Enterprise, as self-hosted Testiny Server.
finops:
- name: Testiny Finops
  service_category: Software Testing and Quality Assurance
  slug: testiny-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/testiny.png
layout: provider
modified: '2026-07-11'
name: Testiny
nav: Providers
network: true
overview: 'Testiny publishes 5 APIs on the [APIs.io](https://apis.io/) network, including Automation API, Projects API, Test Cases API, and 2 more. Tagged areas include Test Runs, Test Management, QA, Test Cases, and Test Automation.


  Testiny''s developer surface includes authentication, documentation, signup flow, pricing, and 7 more developer resources.'
plans:
- name: Testiny Plans Pricing
  plan_count: 5
  slug: testiny-plans-pricing
random_paper: 64
rate_limits:
- limit_count: 4
  name: Testiny Rate Limits
  slug: testiny-rate-limits
score:
  band: thin
  composite: 41.2
  delta: -2.0
  facets:
    commercial_clarity: 63.2
    contract_quality: 52.4
    developer_ergonomics: 19.6
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 31.6
  previous_composite: 43.2
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 5
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
security:
- kind: authentication
  name: Testiny Authentication
  slug: testiny-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Testiny Domain Security
  slug: testiny-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: testiny
tags:
- Test Runs
- Test Management
- QA
- Test Cases
- Test Automation
- Quality Assurance
- Testing
website: https://www.testiny.io
---
