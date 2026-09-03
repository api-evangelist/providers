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
  scored_at: '2026-09-02'
agentic_access:
- acting_count: 19
  human_in_the_loop: 0
  name: Kobiton Agentic Access
  operation_count: 26
  slug: kobiton-agentic-access
  summary_line: 26 operations · 19 acting
api_count: 1
apis:
- description: Kobiton's Appium/WebDriver endpoint for scripted mobile automation. Point an Appium or Selenium client at the hub with Kobiton desired capabilities to allocate a real device and execute a scripted tes
  name: Kobiton Appium Automation Hub
  slug: kobiton-appium-automation-hub
- baseURL: https://api.kobiton.com/v1
  baseurl_source: declared
  description: The app repository of builds under test.
  name: Kobiton Apps API
  slug: kobiton-apps-api
- baseURL: https://api.kobiton.com/v1
  baseurl_source: declared
  description: Data-driven testing input sets.
  name: Kobiton Data Sets API
  slug: kobiton-data-sets-api
- baseURL: https://api.kobiton.com/v1
  baseurl_source: declared
  description: Real devices available in the Kobiton device cloud.
  name: Kobiton Devices API
  slug: kobiton-devices-api
- baseURL: https://api.kobiton.com/v1
  baseurl_source: declared
  description: Organization member administration.
  name: Kobiton Organization API
  slug: kobiton-organization-api
- baseURL: https://api.kobiton.com/v1
  baseurl_source: declared
  description: No-code test runs driven by revisit plans.
  name: Kobiton Scriptless Automation API
  slug: kobiton-scriptless-automation-api
- baseURL: https://api.kobiton.com/v1
  baseurl_source: declared
  description: Test-run sessions and their captured commands.
  name: Kobiton Sessions API
  slug: kobiton-sessions-api
artifact_total: 20
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Kobiton REST Apps API
  slug: open-kobiton-apps-api
- collection_type: open
  name: Kobiton REST Apps Data Sets API
  slug: open-kobiton-data-sets-api
- collection_type: open
  name: Kobiton REST Apps Devices API
  slug: open-kobiton-devices-api
- collection_type: open
  name: Kobiton REST Apps Organization API
  slug: open-kobiton-organization-api
- collection_type: open
  name: Kobiton REST Apps Scriptless Automation API
  slug: open-kobiton-scriptless-automation-api
- collection_type: open
  name: Kobiton REST Apps Sessions API
  slug: open-kobiton-sessions-api
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
random_paper: 2
rate_limits:
- limit_count: 4
  name: Kobiton Rate Limits
  slug: kobiton-rate-limits
score:
  band: thin
  composite: 29.7
  coverage:
    artifact_dirs: 9
    catalog_gap: 51.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 39.5
    commercial_clarity: 39.5
    contract_governance: 0.0
    contract_quality: 13.4
    developer_ergonomics: 35.7
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 34.2
  previous_composite: 29.7
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 6
      marker_coverage: 100.0
      total: 6
  schema_version: 0.18.0
  scored_at: '2026-09-02'
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
