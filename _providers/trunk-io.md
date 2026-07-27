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
  band: agent-ready
  dimensions:
    agent_skills: false
    agentic_access: true
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: true
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.1
  score: 48.1
  scored_at: '2026-07-27'
agentic_access:
- acting_count: 15
  human_in_the_loop: 0
  name: Trunk Io Agentic Access
  operation_count: 16
  slug: trunk-io-agentic-access
  summary_line: 16 operations · 15 acting
api_count: 5
apis:
- description: CI test-result ingestion surface. The trunk-analytics-cli (and the trunk-io/analytics-uploader GitHub Action) uploads JUnit XML, Bazel BEP, and XCResult test reports to Trunk for flaky-test detection,
  name: Trunk Test Uploads (Analytics CLI)
  slug: test-uploads-api
- description: Svix-powered outbound webhooks for subscribing to Flaky Tests events (test_case.status_changed, test_case.monitor_status_changed, test_case.investigation_completed) and Merge Queue events (pull_reques
  name: Trunk Webhooks
  slug: webhooks-api
- description: Meta-linter and static analysis manager exposed through the trunk CLI and a local daemon (no public REST API). Commands include trunk init, trunk check, and trunk check --all; it hermetically installs
  name: Trunk Code Quality CLI
  slug: code-quality-cli
- description: Query Flaky Tests state and link tickets.
  name: Trunk Flaky Tests API
  slug: trunk-io-flaky-tests-api
- description: Control the Trunk Merge Queue.
  name: Trunk Merge Queue API
  slug: trunk-io-merge-queue-api
artifact_total: 13
collections:
- collection_type: open
  name: Trunk API
  slug: open-trunk-io
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/trunk-io-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/trunk-io-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/trunk-io-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/trunk-io-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/trunk-io
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/trunkhq
- group: company
  title: ''
  type: Website
  url: https://trunk.io/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.trunk.io
- group: commercial
  title: ''
  type: Plans
  url: plans/trunk-io-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/trunk-io-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/trunk-io-finops.yml
- group: company
  title: ''
  type: Blog
  url: https://trunk.io/feed.xml
created: '2026-06-20'
description: Trunk builds developer experience and CI reliability tooling. Its platform spans Code Quality (a meta-linter and static analysis manager driven by the trunk CLI), a flake-aware parallel Merge Queue, and Flaky Tests detection/CI Analytics. Test results are uploaded from CI via the Trunk Analytics CLI/GitHub Action, and an HTTP REST API at api.trunk.io exposes Flaky Tests and Merge Queue control plus Svix-powered webhooks.
finops:
- name: Trunk Io Finops
  service_category: Developer Tools
  slug: trunk-io-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/trunk-io.png
layout: provider
modified: '2026-06-20'
name: Trunk
nav: Providers
network: true
overview: 'Trunk publishes 2 APIs on the [APIs.io](https://apis.io/) network: Flaky Tests API and Merge Queue API. Tagged areas include Developer Tools, CI/CD, Code Quality, Flaky Tests, and Merge Queue.


  Trunk''s developer surface includes authentication, documentation, engineering blog, and 9 more developer resources.'
plans:
- name: Trunk Io Plans Pricing
  plan_count: 3
  slug: trunk-io-plans-pricing
random_paper: 9
rate_limits:
- limit_count: 3
  name: Trunk Io Rate Limits
  slug: trunk-io-rate-limits
score:
  band: thin
  composite: 41.8
  delta: 3.2
  facets:
    commercial_clarity: 39.5
    contract_quality: 59.3
    developer_ergonomics: 21.7
    discoverability: 100.0
    governance: 0.0
    operational_transparency: 36.8
  previous_composite: 38.6
  schema_version: 0.5
  scored_at: '2026-07-27'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/trunk-io/refs/heads/main/screenshots/trunk-io-2026-06-20T195810.png
security:
- kind: authentication
  name: Trunk Io Authentication
  slug: trunk-io-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Trunk Io Domain Security
  slug: trunk-io-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Trunk Io Vulnerability Disclosure
  slug: trunk-io-vulnerability-disclosure
  summary_line: disclosure policy published
slug: trunk-io
tags:
- Developer Tools
- CI/CD
- Code Quality
- Flaky Tests
- Merge Queue
website: https://trunk.io/
---
