---
agent_readiness:
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: false
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
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 0.0
  scored_at: '2026-10-03'
api_count: 0
artifact_total: 30
common:
- group: start
  title: ''
  type: Portal
  url: https://apievangelist.com
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/api-evangelist
created: '2026-05-19'
description: An index and topic collection covering API and web performance, including load testing, performance benchmarking, real user monitoring (RUM), Core Web Vitals measurement, latency profiling, distributed tracing, and application performance monitoring (APM). Performance engineering ensures that APIs and web applications meet latency, throughput, and reliability expectations under realistic and adversarial load. This collection brings together open-source load generators like k6, Apache JMeter, Locust, Gatling, and Artillery; managed load and chaos platforms like StormForge and Speedscale; synthetic and real-user measurement tools like Google PageSpeed, Pingdom, and Akamai; and APM and tracing platforms like Datadog, New Relic, Dynatrace, AppDynamics, Sentry, Honeycomb, Instana, Lightstep, SigNoz, Uptrace, OpenTelemetry, Jaeger, Grafana Tempo, Google Cloud Profiler, Google Cloud Trace, and AWS X-Ray.
examples:
- key_count: 10
  name: Performance Load Test Run Example
  slug: performance-load-test-run-example
- key_count: 11
  name: Performance Web Vital Sample Example
  slug: performance-web-vital-sample-example
features:
- description: Open-source and managed load generators like k6, Apache JMeter, Locust, Gatling, and Artillery simulate concurrent users and traffic patterns against APIs to characterize throughput, error rate, and latency under load.
  name: Load and Stress Testing
- description: Repeatable, scripted benchmark runs establish performance baselines and detect regressions in CI/CD pipelines using tools like k6 Cloud, BlazeMeter, and StormForge.
  name: Performance Benchmarking
- description: RUM products like Akamai mPulse, Datadog RUM, New Relic Browser, Sentry Performance, and Pingdom capture latency, errors, and Core Web Vitals from real browser sessions in production.
  name: Real User Monitoring (RUM)
- description: Synthetic checks and lab-based audits from Google PageSpeed (Lighthouse), WebPageTest, and Pingdom measure Core Web Vitals (LCP, INP, CLS) and uptime from controlled environments.
  name: Synthetic Monitoring and Web Vitals
- description: OpenTelemetry, Jaeger, Grafana Tempo, Honeycomb, Lightstep, Google Cloud Trace, and AWS X-Ray collect distributed traces across microservice calls to attribute latency to specific spans.
  name: Distributed Tracing
- description: APM platforms like Datadog APM, New Relic, Dynatrace, AppDynamics, Instana, SigNoz, and Uptrace correlate traces, metrics, and logs to surface slow transactions and code-level bottlenecks.
  name: Application Performance Monitoring (APM)
- description: Continuous profilers like Google Cloud Profiler and Datadog Continuous Profiler identify CPU, memory, and lock contention hotspots in running services.
  name: Profiling and Code Hotspots
- description: Tools like GoReplay and Speedscale capture production traffic and replay it against staging or new versions to validate performance and behavior before release.
  name: Traffic Replay and Chaos
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/apis-json-logo.jpg
integrations:
- description: Open-source Grafana Labs load testing tool that uses JavaScript test scripts to drive load against HTTP, gRPC, and WebSocket APIs, with optional k6 Cloud for distributed runs.
  name: k6
- description: Open-source Apache Software Foundation load testing tool for HTTP, REST, databases, JMS, and more, widely used for protocol-level performance testing.
  name: Apache JMeter
- description: High-throughput, Scala-based open-source load testing tool with code-as-test scenarios and detailed HTML reports.
  name: Gatling
- description: Modern Node.js load testing toolkit with YAML and JavaScript scenarios, designed for serverless and Kubernetes-native workloads.
  name: Artillery
- description: Performance and load testing platform that uses machine learning to optimize Kubernetes resource configurations and validate scalability.
  name: StormForge
- description: Observability and APM platform offering distributed tracing, real user monitoring, synthetic monitoring, and continuous profiling.
  name: Datadog
- description: Full-stack observability platform with APM, browser-based RUM, synthetic monitoring, distributed tracing, and infrastructure metrics.
  name: New Relic
- description: Vendor-neutral CNCF standard for collecting traces, metrics, and logs, used to instrument applications for any compatible APM or tracing backend.
  name: OpenTelemetry
json_schemas:
- name: LoadTestRun
  property_count: 10
  slug: performance-load-test-run
- name: WebVitalSample
  property_count: 11
  slug: performance-web-vital-sample
json_structures:
- name: Performance Load Test Run Structure
  property_count: 10
  slug: performance-load-test-run-structure
- name: Performance Web Vital Sample Structure
  property_count: 11
  slug: performance-web-vital-sample-structure
jsonld:
- class_count: 7
  name: Performance Context
  property_count: 37
  slug: performance-context
layout: provider
modified: '2026-05-19'
name: Performance
nav: Providers
network: true
overview: 'Performance is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Performance, Load Testing, Performance Testing, Real User Monitoring, and Core Web Vitals.


  The Performance catalog on APIs.io includes 1 JSON-LD context.


  Performance''s developer surface includes developer portal and 1 more developer resources.'
random_paper: 4
score:
  band: minimal
  composite: 9.5
  coverage:
    artifact_dirs: 9
    catalog_earned: 38.0
    catalog_earned_first_party: 0.0
    catalog_gap: 77.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 14.7
    developer_ergonomics: 9.5
    discoverability: 48.2
    operational_transparency: 5.3
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: never_enriched
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 4.9
  schema_version: 0.23.0
  scored_at: '2026-10-03'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
slug: performance
tags:
- Performance
- Load Testing
- Performance Testing
- Real User Monitoring
- Core Web Vitals
- APM
- Distributed Tracing
- Latency
use_cases:
- description: Engineering teams run k6 or JMeter scenarios on every pull request to verify that p95 latency and error rates stay within service-level objectives before merging.
  name: Pre-Release Load Testing in CI/CD
- description: Web teams use Google PageSpeed, WebPageTest, and RUM data to optimize LCP, INP, and CLS to meet Google ranking and user-experience thresholds.
  name: Core Web Vitals Optimization
- description: Platform teams use StormForge and BlazeMeter to drive sustained load tests against staging environments to determine maximum sustainable throughput and right-size infrastructure.
  name: Capacity Planning and Scalability Validation
- description: APM platforms like Datadog, New Relic, and Dynatrace alert on p95 and p99 latency regressions per endpoint or trace span after each deploy.
  name: Latency Regression Detection
- description: Teams use GoReplay or Speedscale to record real production traffic and replay it against release candidates to find performance and correctness regressions before rollout.
  name: Production Traffic Replay
- description: SREs use Honeycomb, Lightstep, Jaeger, or Grafana Tempo to drill into slow distributed traces and pinpoint the service, query, or downstream call responsible for tail latency.
  name: Distributed Trace Root-Cause Analysis
- description: Backend teams use Google Cloud Profiler or Datadog Continuous Profiler to identify CPU and memory hotspots in running services without rebuilding or redeploying.
  name: Continuous Profiling of Hot Paths
website: https://apievangelist.com
---
