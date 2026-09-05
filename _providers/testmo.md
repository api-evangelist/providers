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
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 19.8
  scored_at: '2026-09-04'
agentic_access:
- acting_count: 7
  human_in_the_loop: 0
  name: Testmo Agentic Access
  operation_count: 23
  slug: testmo-agentic-access
  summary_line: 23 operations · 7 acting
api_count: 1
apis:
- baseURL: https://{instance}.testmo.net/api/v1
  baseurl_source: declared
  description: Automation runs submitted from CI/CD, with aggregated statistics.
  name: Testmo Automation Runs API
  slug: testmo-automation-runs-api
- baseURL: https://{instance}.testmo.net/api/v1
  baseurl_source: declared
  description: Automation sources grouping runs, with aggregated metrics.
  name: Testmo Automation Sources API
  slug: testmo-automation-sources-api
- baseURL: https://{instance}.testmo.net/api/v1
  baseurl_source: declared
  description: Milestones and their linked run and session statistics.
  name: Testmo Milestones API
  slug: testmo-milestones-api
- baseURL: https://{instance}.testmo.net/api/v1
  baseurl_source: declared
  description: Top-level projects that contain runs, sessions, milestones, and cases.
  name: Testmo Projects API
  slug: testmo-projects-api
- baseURL: https://{instance}.testmo.net/api/v1
  baseurl_source: declared
  description: Exploratory test sessions and session note statistics.
  name: Testmo Sessions API
  slug: testmo-sessions-api
- baseURL: https://{instance}.testmo.net/api/v1
  baseurl_source: declared
  description: Beta read/write API for cases, folders, and attachments.
  name: Testmo Test Case Management API
  slug: testmo-test-case-management-api
- baseURL: https://{instance}.testmo.net/api/v1
  baseurl_source: declared
  description: Manual test runs and their individual results.
  name: Testmo Test Runs API
  slug: testmo-test-runs-api
artifact_total: 21
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Testmo REST Automation Runs API
  slug: open-testmo-automation-runs-api
- collection_type: open
  name: Testmo REST Automation Runs Automation Sources API
  slug: open-testmo-automation-sources-api
- collection_type: open
  name: Testmo REST Automation Runs Milestones API
  slug: open-testmo-milestones-api
- collection_type: open
  name: Testmo REST Automation Runs Projects API
  slug: open-testmo-projects-api
- collection_type: open
  name: Testmo REST Automation Runs Sessions API
  slug: open-testmo-sessions-api
- collection_type: open
  name: Testmo REST Automation Runs Test Case Management API
  slug: open-testmo-test-case-management-api
- collection_type: open
  name: Testmo REST Automation Runs Test Runs API
  slug: open-testmo-test-runs-api
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
random_paper: 17
rate_limits:
- limit_count: 5
  name: Testmo Rate Limits
  slug: testmo-rate-limits
score:
  band: developing
  composite: 40.2
  coverage:
    artifact_dirs: 9
    catalog_earned: 64.0
    catalog_earned_first_party: 0.0
    catalog_gap: 51.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -0.7
  facets:
    access_clarity: 39.5
    commercial_clarity: 39.5
    contract_governance: 0.0
    contract_quality: 59.8
    developer_ergonomics: 32.1
    discoverability: 68.5
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
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/testmo/refs/heads/main/screenshots/testmo-2026-09-02T163235.png
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
