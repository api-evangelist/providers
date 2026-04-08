---
aid: scalability-testing
url: https://raw.githubusercontent.com/api-evangelist/scalability-testing/refs/heads/main/apis.yml
apis:
- name: Load Testing API
  description: API for creating and managing load tests to evaluate system performance under various load conditions.
  image: https://example.com/images/load-testing.png
  humanURL: https://scalability-testing.example.com/load-testing
  baseURL: https://api.scalability-testing.example.com/v1/load
  tags:
  - Load Testing
  - Performance
  - Testing
  properties:
  - type: Documentation
    url: https://scalability-testing.example.com/docs/load-testing
  - type: OpenAPI
    url: https://api.scalability-testing.example.com/v1/load/openapi.json
  - type: Swagger
    url: https://api.scalability-testing.example.com/v1/load/swagger
  - type: Authentication
    url: https://scalability-testing.example.com/docs/authentication
  contact:
  - type: Email
    url: support@scalability-testing.example.com
  - type: Support
    url: https://scalability-testing.example.com/support
- name: Stress Testing API
  description: API for conducting stress tests to determine breaking points and system limits.
  image: https://example.com/images/stress-testing.png
  humanURL: https://scalability-testing.example.com/stress-testing
  baseURL: https://api.scalability-testing.example.com/v1/stress
  tags:
  - Limits
  - Performance
  - Stress Testing
  properties:
  - type: Documentation
    url: https://scalability-testing.example.com/docs/stress-testing
  - type: OpenAPI
    url: https://api.scalability-testing.example.com/v1/stress/openapi.json
  - type: Pricing
    url: https://scalability-testing.example.com/pricing
  contact:
  - type: Email
    url: support@scalability-testing.example.com
- name: Metrics & Analytics API
  description: API for retrieving test results, performance metrics, and scalability analytics.
  image: https://example.com/images/metrics.png
  humanURL: https://scalability-testing.example.com/metrics
  baseURL: https://api.scalability-testing.example.com/v1/metrics
  tags:
  - Analytics
  - Metrics
  - Performance
  - Reporting
  properties:
  - type: Documentation
    url: https://scalability-testing.example.com/docs/metrics
  - type: OpenAPI
    url: https://api.scalability-testing.example.com/v1/metrics/openapi.json
  - type: Dashboard
    url: https://dashboard.scalability-testing.example.com
  contact:
  - type: Email
    url: support@scalability-testing.example.com
- name: Resource Monitoring API
  description: API for monitoring system resources during scalability tests including CPU, memory, and network usage.
  image: https://example.com/images/monitoring.png
  humanURL: https://scalability-testing.example.com/monitoring
  baseURL: https://api.scalability-testing.example.com/v1/monitoring
  tags:
  - Monitoring
  - Real-Time
  - Resources
  properties:
  - type: Documentation
    url: https://scalability-testing.example.com/docs/monitoring
  - type: OpenAPI
    url: https://api.scalability-testing.example.com/v1/monitoring/openapi.json
  - type: WebSocket
    url: wss://api.scalability-testing.example.com/v1/monitoring/stream
  contact:
  - type: Email
    url: support@scalability-testing.example.com
- name: Test Configuration API
  description: API for managing test configurations, scenarios, and user load patterns.
  image: https://example.com/images/configuration.png
  humanURL: https://scalability-testing.example.com/configuration
  baseURL: https://api.scalability-testing.example.com/v1/config
  tags:
  - Configuration
  - Management
  - Test Scenarios
  properties:
  - type: Documentation
    url: https://scalability-testing.example.com/docs/configuration
  - type: OpenAPI
    url: https://api.scalability-testing.example.com/v1/config/openapi.json
  - type: Examples
    url: https://scalability-testing.example.com/docs/examples
  contact:
  - type: Email
    url: support@scalability-testing.example.com
name: Scalability Testing
tags:
- Analytics
- API Testing
- Load Testing
- Monitoring
- Performance Testing
- Scalability
- Stress Testing
type: Contract
image: https://example.com/images/scalability-testing-logo.png
access: 3rd-Party
created: '2026-03-29'
modified: '2026-04-07'
position: Consuming
description: A collection of APIs for performing scalability and load testing.
maintainers:
- FN: Kin Lane
  email: info@apievangelist.com
specificationVersion: '0.19'
---

