---
access_model:
  confidence: medium
  label: Paid
  onboarding: unknown
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
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: derived
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 19.6
  scored_at: '2026-11-06'
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
- baseURL: https://api.kobiton.com/wd/hub
  baseurl_source: declared
  description: Data-driven testing input sets.
  name: Kobiton Datasets API
  slug: kobiton-datasets-api
artifact_total: 20
collections:
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
- group: other
  href: https://artifacts.apis.io/kobiton/capabilities/kobiton-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/kobiton-capability-edges.yml
- group: agent
  href: https://artifacts.apis.io/kobiton/agentic-access/kobiton-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/kobiton-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/kobiton/authentication/kobiton-authentication.yml
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
  href: https://artifacts.apis.io/kobiton/plans/kobiton-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/kobiton-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/kobiton/rate-limits/kobiton-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/kobiton-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/kobiton/finops/kobiton-finops.yml
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
- has_sources: true
  method: generated
  name: Kobiton Finops
  primary_unit: ''
  service_category: Software Testing and Quality Assurance
  slug: kobiton-finops
  template: false
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/kobiton.png
layout: provider
modified: '2026-07-11'
name: Kobiton
nav: Providers
network: true
overview: 'Kobiton publishes 7 API contracts indexed on the [APIs.io](https://apis.io/) network, including Apps API, Devices API, Organization API, and 4 more. Tagged areas include Mobile Testing, Test Runs, Device Cloud, Real Devices, and Appium.


  The Kobiton catalog on APIs.io includes 1 Spectral governance ruleset.


  Kobiton''s developer surface includes authentication, documentation, engineering blog, and 8 more developer resources.'
plans:
- name: Kobiton Plans Pricing
  plan_count: 4
  slug: kobiton-plans-pricing
random_paper: 14
rate_limits:
- limit_count: 4
  name: Kobiton Rate Limits
  slug: kobiton-rate-limits
rules:
- authorship: generated
  effective_rule_count: 100
  extends:
  - spectral:oas
  name: Kobiton API Rules
  rule_count: 59
  severity_counts:
    error: 55
    hint: 0
    info: 1
    warn: 3
  slug: kobiton-rules
score:
  band: emerging
  composite: 25.6
  coverage:
    artifact_dirs: 16
    catalog_earned: 47.5
    catalog_earned_first_party: 0.0
    catalog_gap: 67.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 7.9
    contract_governance: 13.6
    contract_quality: 40.3
    developer_ergonomics: 32.1
    discoverability: 66.1
    operational_transparency: 10.5
  previous_composite: 25.6
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 6
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 5.9
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/kobiton/kobiton-2026-07-25T224033.png
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
