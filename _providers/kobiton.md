---
access_model:
  confidence: high
  label: Paid · Self-serve signup
  onboarding: self-serve
  pricing: paid
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: false
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
- acting_count: 19
  human_in_the_loop: 0
  name: Kobiton Agentic Access
  operation_count: 26
  slug: kobiton-agentic-access
  summary_line: 26 operations · 19 acting
api_count: 7
apis:
- description: Kobiton's Appium/WebDriver endpoint for scripted mobile automation. Point an Appium or Selenium client at the hub with Kobiton desired capabilities to allocate a real device and execute a scripted tes
  name: Kobiton Appium Automation Hub
  slug: kobiton-appium-automation-hub
- description: The app repository of builds under test.
  name: Kobiton Apps API
  slug: kobiton-apps-api
- description: Data-driven testing input sets.
  name: Kobiton Data Sets API
  slug: kobiton-data-sets-api
- description: Real devices available in the Kobiton device cloud.
  name: Kobiton Devices API
  slug: kobiton-devices-api
- description: Organization member administration.
  name: Kobiton Organization API
  slug: kobiton-organization-api
- description: No-code test runs driven by revisit plans.
  name: Kobiton Scriptless Automation API
  slug: kobiton-scriptless-automation-api
- description: Test-run sessions and their captured commands.
  name: Kobiton Sessions API
  slug: kobiton-sessions-api
artifact_total: 13
collections:
- collection_type: open
  name: Kobiton REST API
  slug: open-kobiton
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/kobiton-agentic-access.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/kobiton-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/kobiton
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/kobiton
- group: company
  title: ''
  type: Website
  url: https://kobiton.com
- group: docs
  title: ''
  type: Documentation
  url: https://docs.kobiton.com
- group: commercial
  title: ''
  type: Plans
  url: plans/kobiton-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/kobiton-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/kobiton-finops.yml
- group: company
  title: ''
  type: Blog
  url: https://kobiton.com/blog
created: '2026-07-11'
description: Kobiton is a mobile device cloud and app testing platform that lets teams run manual, automated, scriptless, and visual tests against real iOS and Android devices in the cloud (or on privately managed local devices). Its REST API at https://api.kobiton.com/v1 exposes the real device cloud, test sessions and their captured commands, the app repository, data-driven test data sets, and scriptless (no-code) test runs, while an Appium/WebDriver hub at https://api.kobiton.com/wd/hub drives scripted automation. All REST requests authenticate with HTTP Basic auth using a Kobiton username (or email) and an API key.
finops:
- name: Kobiton Finops
  service_category: Software Testing and Quality Assurance
  slug: kobiton-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/kobiton.png
layout: provider
modified: '2026-07-11'
name: Kobiton
nav: Providers
network: true
overview: 'Kobiton publishes 6 APIs on the [APIs.io](https://apis.io/) network, including Apps API, Data Sets API, Devices API, and 3 more. Tagged areas include Mobile Testing, Test Runs, Device Cloud, Real Devices, and Appium.


  Kobiton''s developer surface includes authentication, documentation, engineering blog, and 7 more developer resources.'
plans:
- name: Kobiton Plans Pricing
  plan_count: 4
  slug: kobiton-plans-pricing
random_paper: 29
rate_limits:
- limit_count: 4
  name: Kobiton Rate Limits
  slug: kobiton-rate-limits
score:
  band: thin
  composite: 38.8
  delta: -2.2
  facets:
    commercial_clarity: 39.5
    contract_quality: 57.6
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
screenshot: https://raw.githubusercontent.com/api-evangelist/kobiton/refs/heads/main/screenshots/kobiton-2026-07-25T224033.png
security:
- kind: authentication
  name: Kobiton Authentication
  slug: kobiton-authentication
  summary_line: http · 1 scheme
slug: kobiton
tags:
- Mobile Testing
- Test Runs
- Device Cloud
- Real Devices
- Appium
- Automation Testing
- Visual Testing
- QA
- Mobile
website: https://kobiton.com
---
