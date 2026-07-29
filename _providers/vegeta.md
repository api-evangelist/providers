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
api_count: 1
apis:
- description: Vegeta is an open source HTTP load testing tool and library written in Go for generating constant request rates. Supports targets from files or stdin, rate limiting (req/s), duration control, configur
  name: Vegeta Load Testing Tool
  slug: vegeta
artifact_total: 24
common:
- group: company
  title: ''
  type: Website
  url: https://github.com/tsenart/vegeta
- group: docs
  title: ''
  type: Documentation
  url: https://github.com/tsenart/vegeta#readme
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/tsenart
- group: build
  title: ''
  type: GitHubRepository
  url: https://github.com/tsenart/vegeta
- group: design
  title: Vegeta Vocabulary
  type: Vocabulary
  url: vocabulary/vegeta-vocabulary.yml
created: '2026-03-25'
description: Vegeta is an open source HTTP load testing tool and library written in Go for generating constant request rates to measure API performance and reliability under sustained load. Supports CLI and library usage with attack plans, rate limiting, duration control, and detailed result metrics including latency histograms and success rates.
examples:
- key_count: 11
  name: Vegeta Attack Example
  slug: vegeta-attack-example
- key_count: 14
  name: Vegeta Metrics Example
  slug: vegeta-metrics-example
- key_count: 11
  name: Vegeta Result Example
  slug: vegeta-result-example
features:
- description: Generates HTTP requests at a constant rate (requests per second) for a specified duration, simulating sustained load on API endpoints.
  name: Constant Rate Attack
- description: Supports text, JSON, and binary result output formats with encoding/decoding support for pipeline-based workflows.
  name: Multiple Output Formats
- description: Produces detailed latency histograms with configurable buckets for analyzing p50, p95, p99, and max latency distributions.
  name: Latency Histograms
- description: Accepts HTTP targets from files or stdin with support for custom headers, request bodies, and per-target configuration.
  name: Target Formats
- description: Configurable TLS settings including certificate pinning, insecure mode, and redirect following for testing secured endpoints.
  name: TLS and Redirects
- description: Go library (vegeta/lib) for programmatic integration of load testing into test suites, CI/CD pipelines, and monitoring tools.
  name: Library API
finops:
- name: Vegeta Finops
  service_category: API
  slug: vegeta-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/vegeta.png
json_schemas:
- name: VegetaAttack
  property_count: 12
  slug: vegeta-attack
- name: VegetaMetrics
  property_count: 14
  slug: vegeta-metrics
- name: VegetaResult
  property_count: 12
  slug: vegeta-result
json_structures:
- name: Vegeta Attack Structure
  property_count: 12
  slug: vegeta-attack-structure
- name: Vegeta Metrics Structure
  property_count: 14
  slug: vegeta-metrics-structure
- name: Vegeta Result Structure
  property_count: 12
  slug: vegeta-result-structure
layout: provider
modified: '2026-05-03'
name: Vegeta
nav: Providers
network: true
overview: 'Vegeta publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Go, HTTP, Load Testing, Performance, and Testing.


  The Vegeta catalog on APIs.io includes 1 Spectral governance ruleset.


  Vegeta''s developer surface includes documentation and 4 more developer resources.'
plans:
- name: Vegeta Plans Pricing
  plan_count: 3
  slug: vegeta-plans-pricing
random_paper: 20
rate_limits:
- limit_count: 5
  name: Vegeta Rate Limits
  slug: vegeta-rate-limits
rules:
- name: Vegeta API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: vegeta-jsonschema-spectral-rules
score:
  band: thin
  composite: 32.6
  delta: -5.0
  facets:
    commercial_clarity: 39.5
    contract_quality: 16.1
    developer_ergonomics: 8.7
    discoverability: 59.3
    governance: 68.8
    operational_transparency: 36.8
  previous_composite: 37.6
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: falling
screenshot: https://raw.githubusercontent.com/api-evangelist/vegeta/refs/heads/main/screenshots/vegeta-2026-06-20T200856.png
slug: vegeta
tags:
- Go
- HTTP
- Load Testing
- Performance
- Testing
use_cases:
- description: Measure API throughput, latency percentiles, and success rates at various request rates to establish performance baselines and SLA compliance.
  name: API Performance Benchmarking
- description: Integrate vegeta as a library in Go test suites to run automated load tests as part of continuous integration pipelines.
  name: Load Testing in CI/CD
- description: Determine maximum sustainable request rates before latency degradation or error rates exceed acceptable thresholds for capacity planning.
  name: Capacity Planning
- description: Compare latency and throughput metrics across API versions to detect performance regressions before deployment to production.
  name: Regression Detection
---
