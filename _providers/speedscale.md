---
access_model:
  confidence: medium
  label: Freemium
  onboarding: unknown
  pricing: freemium
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
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 3.2
  scored_at: '2026-08-03'
api_count: 1
apis:
- description: Speedscale captures production API traffic and replays it in lower environments for load testing, regression testing, and chaos testing. It provides traffic capture, replay, mocking of backend depende
  name: Speedscale Platform
  slug: speedscale-platform
artifact_total: 11
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/speedscale-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://speedscale.com
- group: docs
  title: ''
  type: Documentation
  url: https://docs.speedscale.com
- group: company
  title: ''
  type: Blog
  url: https://speedscale.com/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://speedscale.com/pricing/
- group: start
  title: ''
  type: Login
  url: https://app.speedscale.com
- group: start
  title: ''
  type: Signup
  url: https://app.speedscale.com/signup
- group: operate
  title: ''
  type: Support
  url: https://docs.speedscale.com/support/
- group: build
  title: ''
  type: GitHub
  url: https://github.com/speedscale
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/speedscale
- group: company
  title: ''
  type: Twitter
  url: https://twitter.com/speedscaleinc
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/speedscale
- group: learn
  title: ''
  type: YouTube
  url: https://www.youtube.com/@speedscale
- group: build
  title: ''
  type: CLI
  url: https://github.com/speedscale/speedscale-cli
- group: other
  title: ''
  type: HelmChart
  url: https://github.com/speedscale/operator-helm
- group: build
  title: ''
  type: Samples
  url: https://github.com/speedscale/proxymock-examples
- group: agent
  title: ''
  type: LlmsText
  url: https://docs.speedscale.com/llms.txt
created: '2026-03-26'
description: Speedscale is an API traffic replay and performance testing platform that captures production API traffic and replays it in test environments for load testing, regression testing, and validation of AI-generated code. It enables teams to simulate realistic traffic patterns without building test scripts from scratch, with native Kubernetes support, service virtualization for backend mocking, PII-safe replay, and MCP integration for AI coding agents (Claude Code, Cursor, Copilot).
examples:
- key_count: 10
  name: Speedscale Snapshot Example
  slug: speedscale-snapshot-example
finops:
- name: Speedscale Finops
  service_category: API
  slug: speedscale-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/speedscale.png
json_schemas:
- name: Speedscale Traffic Snapshot
  property_count: 10
  slug: speedscale-traffic
json_structures:
- name: Speedscale Traffic Structure
  property_count: 0
  slug: speedscale-traffic-structure
jsonld:
- class_count: 7
  name: Speedscale Context
  property_count: 11
  slug: speedscale-context
layout: provider
modified: '2026-05-02'
name: Speedscale
nav: Providers
network: true
overview: 'Speedscale publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include API Mocking, API Testing, Kubernetes, Load Testing, and Performance Testing.


  The Speedscale catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Speedscale''s developer surface includes documentation, engineering blog, pricing, signup flow, support, GitHub presence, YouTube channel, and 10 more developer resources.'
plans:
- name: Speedscale Plans Pricing
  plan_count: 3
  slug: speedscale-plans-pricing
random_paper: 4
rate_limits:
- limit_count: 5
  name: Speedscale Rate Limits
  slug: speedscale-rate-limits
rules:
- name: Speedscale API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: speedscale-jsonschema-spectral-rules
- name: Speedscale API Rules
  rule_count: 4
  severity_counts:
    error: 1
    hint: 0
    info: 1
    warn: 2
  slug: speedscale-rules
score:
  band: developing
  composite: 42.5
  delta: 0.0
  facets:
    commercial_clarity: 63.2
    contract_quality: 27.4
    developer_ergonomics: 21.7
    discoverability: 68.5
    governance: 58.3
    operational_transparency: 36.8
  previous_composite: 42.5
  schema_version: 0.9
  scored_at: '2026-08-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/speedscale/refs/heads/main/screenshots/speedscale-2026-06-20T194303.png
security:
- kind: domain-security
  name: Speedscale Domain Security
  slug: speedscale-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: speedscale
tags:
- API Mocking
- API Testing
- Kubernetes
- Load Testing
- Performance Testing
- Regression Testing
- Service Virtualization
- Traffic Replay
website: https://speedscale.com
---
