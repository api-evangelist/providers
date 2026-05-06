---
aid: artillery
name: Artillery
description: Artillery is an open source load testing and performance testing platform for APIs, microservices, and web applications. Built with Node.js and available as an npm package, Artillery supports HTTP/1, HTTP/2, WebSocket, Socket.IO, gRPC, and custom protocols through plugins. It includes a YAML-based test scenario definition language, a plugin ecosystem for extending functionality, and Artillery Cloud for distributed load testing, CI/CD integration, and centralized reporting. Artillery is used by developers, QA engineers, and SREs to run load tests, performance benchmarks, Playwright-based synthetic monitoring, and end-to-end tests at scale. The project is licensed under MPL-2.0 and maintained by Artilleryio.
url: https://raw.githubusercontent.com/api-evangelist/artillery/refs/heads/main/apis.yml
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Load Testing
  - Performance Testing
  - Open Source
  - Testing
  - DevOps
  - Node.js
created: '2026-03-25'
modified: '2026-04-19'
specificationVersion: '0.19'
apis:
  - aid: artillery:artillery-cloud-api
    name: Artillery Cloud API
    description: Artillery Cloud provides a hosted platform for running distributed load tests at scale, storing test results, team collaboration, and integrating with CI/CD pipelines. The Artillery Cloud API enables programmatic triggering of test runs, retrieval of test results, and management of test configurations.
    humanURL: https://www.artillery.io/docs/reference/cli/run-test
    baseURL: https://app.artillery.io/api
    tags:
      - Load Testing
      - Cloud
      - CI/CD
      - Performance
    properties:
      - type: Documentation
        url: https://www.artillery.io/docs/reference/cli/run-test
      - type: GettingStarted
        url: https://www.artillery.io/docs/get-started/get-artillery
common:
  - type: Portal
    url: https://www.artillery.io/
    title: Artillery Website
  - type: Documentation
    url: https://www.artillery.io/docs
    title: Documentation
  - type: GitHubOrganization
    url: https://github.com/artilleryio
    title: Artillery GitHub Organization
  - type: GitHubRepository
    url: https://github.com/artilleryio/artillery
    title: Artillery Source Repository
  - type: ReleaseNotes
    url: https://github.com/artilleryio/artillery/blob/main/CHANGELOG.md
    title: Changelog
  - type: Pricing
    url: https://www.artillery.io/pricing
    title: Pricing
  - type: Features
    data:
      - name: HTTP Load Testing
        description: Load test HTTP/1 and HTTP/2 REST APIs, GraphQL endpoints, and web applications with configurable virtual users, arrival rates, and scenario definitions.
      - name: WebSocket and Socket.IO Testing
        description: Test real-time applications with WebSocket and Socket.IO protocol support, enabling load testing of chat, notifications, and streaming applications.
      - name: Playwright Integration
        description: Run Playwright browser-based end-to-end scenarios under load, enabling realistic user simulation and synthetic monitoring from the same test framework.
      - name: Plugin Ecosystem
        description: Extensible plugin system with official plugins for gRPC, Kafka, AWS Lambda, Kinesis, and community plugins for many other protocols.
      - name: Artillery Cloud
        description: Hosted cloud platform for running distributed load tests at massive scale across multiple cloud regions, with centralized results and team collaboration features.
      - name: YAML Test Scenarios
        description: Human-readable YAML test scenario definitions supporting think time, loops, conditional logic, data CSV files, and custom JavaScript functions.
  - type: UseCases
    data:
      - name: API Load Testing
        description: Backend developers and QA engineers run load tests against REST and GraphQL APIs to identify performance bottlenecks and ensure stability under expected traffic volumes.
      - name: CI/CD Performance Gates
        description: Engineering teams integrate Artillery into CI/CD pipelines to run performance tests on every pull request, failing builds that exceed latency or error rate thresholds.
      - name: Synthetic Monitoring
        description: SREs use Artillery with Playwright to run synthetic monitors that continuously validate critical user journeys from multiple cloud regions.
      - name: Pre-Launch Stress Testing
        description: Product teams run stress tests before major launches or sales events to identify the maximum capacity of their infrastructure.
  - type: Integrations
    data:
      - name: GitHub Actions
        description: Official Artillery GitHub Action for running load tests in CI/CD pipelines with automatic reporting and performance gate enforcement.
      - name: Datadog
        description: Artillery publishes metrics to Datadog for real-time monitoring and alerting during load test runs.
      - name: AWS Lambda
        description: Artillery can run distributed load tests using AWS Lambda as the execution backend, enabling serverless-scale testing.
      - name: Playwright
        description: Native Playwright integration for browser-based load testing and synthetic monitoring scenarios.
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
