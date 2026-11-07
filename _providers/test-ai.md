---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - authentication
  - rate-limits
  - security
  trial: false
  try_now: false
agent_readiness:
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: derived
    event_surface_described: false
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 0.0
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: gRPC service that classifies UI element screenshots into semantic labels. A single RPC, ClassifyElements, takes a map of element id to PNG bytes plus a label hint, a confidence threshold and a weaker-
  name: test.ai Classifier
  slug: testai-classifier
- baseURL: http://api.opentestdata.org
  baseurl_source: declared
  description: The Data API from test.ai — 2 operation(s) for data.
  name: test.ai Data API
  slug: test-ai-data-api
- baseURL: http://api.opentestdata.org
  baseurl_source: declared
  description: The Ping API from test.ai — 1 operation(s) for ping.
  name: test.ai Ping API
  slug: test-ai-ping-api
- baseURL: http://api.opentestdata.org
  baseurl_source: declared
  description: The Search API from test.ai — 1 operation(s) for search.
  name: test.ai Search API
  slug: test-ai-search-api
- baseURL: http://api.opentestdata.org
  baseurl_source: declared
  description: The Tests API from test.ai — 2 operation(s) for tests.
  name: test.ai Tests API
  slug: test-ai-tests-api
- baseURL: http://api.opentestdata.org
  baseurl_source: declared
  description: The Users API from test.ai — 7 operation(s) for users.
  name: test.ai Users API
  slug: test-ai-users-api
artifact_total: 11
common:
- group: other
  href: https://artifacts.apis.io/test-ai/capabilities/test-ai-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/test-ai-capability-edges.yml
- group: other
  href: https://artifacts.apis.io/test-ai/overlays/test-ai-opentestdata-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/test-ai-opentestdata-overlay.yaml
- group: commercial
  title: ''
  type: License
  url: https://github.com/testdotai/opentestdata-api/blob/master/LICENSE
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/testdotai
- group: docs
  title: ''
  type: Documentation
  url: https://github.com/testdotai/testai-build-your-own-SDK-documentation
- group: start
  title: ''
  type: GettingStarted
  url: https://github.com/testdotai/interactive_walkthrough
- group: build
  href: https://artifacts.apis.io/test-ai/packages/test-ai-packages.yml
  title: ''
  type: Packages
  url: packages/test-ai-packages.yml
- group: build
  href: https://artifacts.apis.io/test-ai/packages/test-ai-packages.yml
  title: ''
  type: SDKs
  url: packages/test-ai-packages.yml
- group: design
  href: https://artifacts.apis.io/test-ai/conformance/test-ai-conformance.yml
  title: ''
  type: Conformance
  url: conformance/test-ai-conformance.yml
- group: design
  href: https://artifacts.apis.io/test-ai/lifecycle/test-ai-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/test-ai-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/test-ai/conventions/test-ai-conventions.yml
  title: ''
  type: Conventions
  url: conventions/test-ai-conventions.yml
- group: auth
  href: https://artifacts.apis.io/test-ai/security/test-ai-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/test-ai-domain-security.yml
- group: agent
  href: https://artifacts.apis.io/test-ai/llms/test-ai-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/test-ai-llms.txt
- group: commercial
  href: https://artifacts.apis.io/test-ai/plans/test-ai-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/test-ai-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/test-ai/rate-limits/test-ai-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/test-ai-rate-limits.yml
created: '2026-08-30'
description: 'test.ai (formerly Appdiff, Inc.) built an AI-powered test-automation platform that used computer vision and machine-learning element classification to make Selenium and Appium tests resilient to UI change. It published first-party Java, Python, Node.js and Ruby SDKs, a gRPC "Classifier" service that labelled UI elements from screenshots, an Appium classifier plugin, and OpenTestData — a free open database of automated test fixture data with its own REST API. The company raised over $30M and was sold; its founder has since moved on to other ventures. As of 2026-08-30 test.ai serves no website of its own: the domain has no HTTPS listener and every HTTP path redirects off-domain. The artifacts profiled here are the contracts and packages the company published while operating, all of which remain publicly retrievable from its own GitHub organization and from the npm, PyPI, RubyGems and Maven Central registries.'
image: https://avatars.githubusercontent.com/u/36999702?s=200&v=4
layout: provider
modified: '2026-08-30'
name: test.ai
nav: Providers
network: true
overview: 'test.ai publishes 6 API contracts indexed on the [APIs.io](https://apis.io/) network, including Data API, Ping API, Search API, and 3 more. Tagged areas include Company, Testing, Test Automation, Quality Assurance, and Artificial Intelligence.


  The test.ai catalog on APIs.io includes 1 Spectral governance ruleset.


  test.ai''s developer surface includes documentation, getting-started guide, and 13 more developer resources.'
plans:
- name: Test Ai Plans Pricing
  plan_count: 0
  slug: test-ai-plans-pricing
random_paper: 23
rate_limits:
- limit_count: 0
  name: Test Ai Rate Limits
  slug: test-ai-rate-limits
rules:
- authorship: generated
  effective_rule_count: 76
  extends:
  - spectral:oas
  name: test.ai API Rules
  rule_count: 35
  severity_counts:
    error: 33
    hint: 0
    info: 1
    warn: 1
  slug: test-ai-rules
score:
  band: minimal
  composite: 0.0
  coverage:
    artifact_dirs: 21
    catalog_earned: 36.5
    catalog_earned_first_party: 0.0
    catalog_gap: 78.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 0.0
    operational_transparency: 0.0
  lifecycle: defunct
  previous_composite: 0.0
  provenance:
    conformance: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 5
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 15.5
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/test-ai/test-ai-2026-09-02T163223.png
security:
- kind: authentication
  name: Test Ai Authentication
  slug: test-ai-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Test Ai Domain Security
  slug: test-ai-domain-security
  summary_line: HSTS
slug: test-ai
tags:
- Company
- Testing
- Test Automation
- Quality Assurance
- Artificial Intelligence
- Machine Learning
- Computer Vision
- Selenium
- Appium
- Developer Tools
- gRPC
- Defunct
---
