---
aid: vegeta
name: Vegeta
description: Vegeta is an open source HTTP load testing tool and library written in Go for generating constant request rates to measure API performance and reliability under sustained load. Supports CLI and library usage with attack plans, rate limiting, duration control, and detailed result metrics including latency histograms and success rates.
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Go
  - HTTP
  - Load Testing
  - Performance
  - Testing
url: https://raw.githubusercontent.com/api-evangelist/vegeta/refs/heads/main/apis.yml
created: '2026-03-25'
modified: '2026-05-03'
specificationVersion: '0.19'
apis:
  - aid: vegeta:vegeta
    name: Vegeta Load Testing Tool
    description: Vegeta is an open source HTTP load testing tool and library written in Go for generating constant request rates. Supports targets from files or stdin, rate limiting (req/s), duration control, configurable timeouts, TLS settings, and multiple output formats (text, JSON, binary). Produces detailed result metrics including latency histograms, success rates, status code distributions, and throughput measurements.
    humanURL: https://github.com/tsenart/vegeta
    tags:
      - Go
      - HTTP
      - Load Testing
      - Performance
      - Testing
    properties:
      - type: Documentation
        url: https://github.com/tsenart/vegeta#readme
      - type: GitHub Repository
        url: https://github.com/tsenart/vegeta
      - type: JSONSchema
        url: json-schema/vegeta-attack-schema.json
        title: Attack Configuration Schema
      - type: JSONSchema
        url: json-schema/vegeta-result-schema.json
        title: Result Schema
      - type: JSONSchema
        url: json-schema/vegeta-metrics-schema.json
        title: Metrics Schema
      - type: JSONStructure
        url: json-structure/vegeta-attack-structure.json
        title: Attack Configuration Structure
      - type: JSONStructure
        url: json-structure/vegeta-result-structure.json
        title: Result Structure
      - type: JSONStructure
        url: json-structure/vegeta-metrics-structure.json
        title: Metrics Structure
      - type: Example
        url: examples/vegeta-attack-example.json
        title: Attack Configuration Example
      - type: Example
        url: examples/vegeta-result-example.json
        title: Result Example
      - type: Example
        url: examples/vegeta-metrics-example.json
        title: Metrics Example
common:
  - type: Website
    url: https://github.com/tsenart/vegeta
  - type: Documentation
    url: https://github.com/tsenart/vegeta#readme
  - type: GitHub Organization
    url: https://github.com/tsenart
  - type: GitHub Repository
    url: https://github.com/tsenart/vegeta
  - type: Vocabulary
    url: vocabulary/vegeta-vocabulary.yml
    title: Vegeta Vocabulary
  - type: Features
    data:
      - name: Constant Rate Attack
        description: Generates HTTP requests at a constant rate (requests per second) for a specified duration, simulating sustained load on API endpoints.
      - name: Multiple Output Formats
        description: Supports text, JSON, and binary result output formats with encoding/decoding support for pipeline-based workflows.
      - name: Latency Histograms
        description: Produces detailed latency histograms with configurable buckets for analyzing p50, p95, p99, and max latency distributions.
      - name: Target Formats
        description: Accepts HTTP targets from files or stdin with support for custom headers, request bodies, and per-target configuration.
      - name: TLS and Redirects
        description: Configurable TLS settings including certificate pinning, insecure mode, and redirect following for testing secured endpoints.
      - name: Library API
        description: Go library (vegeta/lib) for programmatic integration of load testing into test suites, CI/CD pipelines, and monitoring tools.
  - type: UseCases
    data:
      - name: API Performance Benchmarking
        description: Measure API throughput, latency percentiles, and success rates at various request rates to establish performance baselines and SLA compliance.
      - name: Load Testing in CI/CD
        description: Integrate vegeta as a library in Go test suites to run automated load tests as part of continuous integration pipelines.
      - name: Capacity Planning
        description: Determine maximum sustainable request rates before latency degradation or error rates exceed acceptable thresholds for capacity planning.
      - name: Regression Detection
        description: Compare latency and throughput metrics across API versions to detect performance regressions before deployment to production.
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
