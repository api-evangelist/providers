---
agent_readiness:
  band: agent-aware
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
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 24.3
  scored_at: '2026-08-30'
api_count: 2
apis:
- description: REST API behind opentestdata.org, test.ai's free and open database of automated test fixture data. 13 paths / 16 operations covering user signup and login, e-mail confirmation, avatars, admin promotio
  name: OpenTestData API
  slug: opentestdata-api
- description: gRPC service that classifies UI element screenshots into semantic labels. A single RPC, ClassifyElements, takes a map of element id to PNG bytes plus a label hint, a confidence threshold and a weaker-
  name: test.ai Classifier
  slug: testai-classifier
artifact_total: 6
common:
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
  title: ''
  type: Packages
  url: packages/test-ai-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/test-ai-packages.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/test-ai-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/test-ai-lifecycle.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/test-ai-conventions.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/test-ai-domain-security.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/test-ai-llms.txt
- group: commercial
  title: ''
  type: Plans
  url: plans/test-ai-plans-pricing.yml
- group: operate
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
overview: 'test.ai publishes 1 API on the [APIs.io](https://apis.io/) network: OpenTestData API. Tagged areas include Company, Testing, Test Automation, Quality Assurance, and Artificial Intelligence.


  test.ai''s developer surface includes documentation, getting-started guide, and 10 more developer resources.'
plans:
- name: Test Ai Plans Pricing
  plan_count: 0
  slug: test-ai-plans-pricing
random_paper: 2
rate_limits:
- limit_count: 0
  name: Test Ai Rate Limits
  slug: test-ai-rate-limits
score:
  band: thin
  composite: 26.6
  coverage:
    artifact_dirs: 16
    catalog_gap: 83.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 18.2
    contract_quality: 40.1
    developer_ergonomics: 40.5
    discoverability: 59.3
    governance: 18.2
    operational_transparency: 2.6
  schema_version: 0.17.2
  scored_at: '2026-08-30'
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
- Machine-Learning
- Computer-Vision
- Selenium
- Appium
- Developer Tools
- gRPC
- Defunct
---
