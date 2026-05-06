---
aid: speedscale
name: Speedscale
description: Speedscale is an API traffic replay and performance testing platform that captures production API traffic and replays it in test environments for load testing, regression testing, and validation of AI-generated code. It enables teams to simulate realistic traffic patterns without building test scripts from scratch, with native Kubernetes support, service virtualization for backend mocking, PII-safe replay, and MCP integration for AI coding agents (Claude Code, Cursor, Copilot).
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - API Mocking
  - API Testing
  - Kubernetes
  - Load Testing
  - Performance Testing
  - Regression Testing
  - Service Virtualization
  - Traffic Replay
url: https://raw.githubusercontent.com/api-evangelist/speedscale/refs/heads/main/apis.yml
created: '2026-03-26'
modified: '2026-05-02'
specificationVersion: '0.19'
apis:
  - aid: speedscale:speedscale-platform
    name: Speedscale Platform
    description: Speedscale captures production API traffic and replays it in lower environments for load testing, regression testing, and chaos testing. It provides traffic capture, replay, mocking of backend dependencies, performance assertions for Kubernetes-based applications, and MCP integration for AI coding agents.
    humanURL: https://speedscale.com
    baseURL: https://app.speedscale.com
    tags:
      - API Mocking
      - API Testing
      - Kubernetes
      - Load Testing
      - Performance Testing
      - Regression Testing
      - Traffic Replay
    properties:
      - type: Documentation
        url: https://docs.speedscale.com
      - type: GettingStarted
        url: https://docs.speedscale.com/guides/getting-started/
      - type: CLI
        url: https://docs.speedscale.com/reference/cli/
      - type: Pricing
        url: https://speedscale.com/pricing/
      - type: Blog
        url: https://speedscale.com/blog
      - type: GitHub
        url: https://github.com/speedscale
      - type: Twitter
        url: https://twitter.com/speedscaleinc
      - type: LinkedIn
        url: https://www.linkedin.com/company/speedscale
      - type: YouTube
        url: https://www.youtube.com/@speedscale
      - type: JSONSchema
        url: https://raw.githubusercontent.com/api-evangelist/speedscale/refs/heads/main/json-schema/speedscale-traffic-schema.json
      - type: JSONStructure
        url: https://raw.githubusercontent.com/api-evangelist/speedscale/refs/heads/main/json-structure/speedscale-traffic-structure.json
      - type: JSONLDContext
        url: https://raw.githubusercontent.com/api-evangelist/speedscale/refs/heads/main/json-ld/speedscale-context.jsonld
      - type: Vocabulary
        url: https://raw.githubusercontent.com/api-evangelist/speedscale/refs/heads/main/vocabulary/speedscale-vocabulary.yml
common:
  - type: Website
    url: https://speedscale.com
  - type: Documentation
    url: https://docs.speedscale.com
  - type: Blog
    url: https://speedscale.com/blog
  - type: Pricing
    url: https://speedscale.com/pricing/
  - type: Login
    url: https://app.speedscale.com
  - type: Signup
    url: https://app.speedscale.com/signup
  - type: Support
    url: https://docs.speedscale.com/support/
  - type: GitHub
    url: https://github.com/speedscale
  - type: GitHubOrganization
    url: https://github.com/speedscale
  - type: Twitter
    url: https://twitter.com/speedscaleinc
  - type: LinkedIn
    url: https://www.linkedin.com/company/speedscale
  - type: YouTube
    url: https://www.youtube.com/@speedscale
  - type: CLI
    url: https://github.com/speedscale/speedscale-cli
    x-name: Speedscale CLI (speedctl)
  - type: HelmChart
    url: https://github.com/speedscale/operator-helm
    x-name: Speedscale Operator Helm Chart
  - type: Samples
    url: https://github.com/speedscale/proxymock-examples
    x-name: Proxymock Examples
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
