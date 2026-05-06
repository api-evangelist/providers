---
name: Test Rate Limit Check
description: Testing and validation of API rate limiting implementations to ensure that APIs correctly enforce request quotas, return appropriate error responses, and recover gracefully when limits are exceeded. Rate limit testing verifies throttling behavior, retry-after headers, burst allowances, and quota reset mechanisms across different API consumers and usage tiers.
url: https://en.wikipedia.org/wiki/Rate_limiting
tags:
  - API Governance
  - API Management
  - API Testing
  - Performance Testing
  - Rate Limiting
  - Testing
created: '2026-05-03'
modified: '2026-05-03'
apis:
  - name: Kong Gateway Admin API
    description: Admin REST API for Kong API Gateway, providing endpoints to configure rate limiting plugins, quotas, consumers, and traffic policies for API rate limit enforcement.
    humanURL: https://docs.konghq.com/gateway/latest/admin-api/
    baseURL: https://your-kong.example.com:8001
    tags:
      - API Gateway
      - API Management
      - Rate Limiting
      - Traffic Control
    properties:
      - type: Documentation
        url: https://docs.konghq.com/gateway/latest/admin-api/
      - type: OpenAPI
        url: https://docs.konghq.com/gateway/latest/admin-api/
  - name: AWS API Gateway API
    description: AWS REST API for managing API Gateway usage plans, API keys, throttling limits, and quota enforcement across API deployments.
    humanURL: https://docs.aws.amazon.com/apigateway/latest/developerguide/api-ref.html
    baseURL: https://apigateway.amazonaws.com
    tags:
      - AWS
      - API Gateway
      - Cloud
      - Rate Limiting
    properties:
      - type: Documentation
        url: https://docs.aws.amazon.com/apigateway/latest/developerguide/api-ref.html
  - name: Apigee API
    description: REST API for Google Apigee API management platform supporting rate limit policy configuration, quota management, spike arrest, and traffic shaping for API testing.
    humanURL: https://cloud.google.com/apigee/docs/reference/apis/apigee/rest
    baseURL: https://apigee.googleapis.com/v1
    tags:
      - API Management
      - Google Cloud
      - Quotas
      - Rate Limiting
    properties:
      - type: Documentation
        url: https://cloud.google.com/apigee/docs/reference/apis/apigee/rest
  - name: Azure API Management API
    description: REST API for Azure API Management service supporting subscription quotas, rate limit policies, and throttling configuration for testing rate limit implementations.
    humanURL: https://learn.microsoft.com/en-us/rest/api/apimanagement/
    baseURL: https://management.azure.com/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ApiManagement/service/{serviceName}
    tags:
      - API Management
      - Azure
      - Microsoft
      - Rate Limiting
    properties:
      - type: Documentation
        url: https://learn.microsoft.com/en-us/rest/api/apimanagement/
  - name: Tyk API Management API
    description: REST API for Tyk open-source API gateway supporting rate limiting, quota management, key expiry, and throttling policy configuration and testing.
    humanURL: https://tyk.io/docs/tyk-gateway-api/
    baseURL: https://your-tyk.example.com/api
    tags:
      - API Gateway
      - API Management
      - Open Source
      - Rate Limiting
    properties:
      - type: Documentation
        url: https://tyk.io/docs/tyk-gateway-api/
      - type: OpenAPI
        url: https://raw.githubusercontent.com/TykTechnologies/tyk/master/apidef/oas/schema/x-tyk-gateway.json
  - name: Grafana API
    description: REST API for Grafana observability platform, enabling rate limit test monitoring through dashboards, alerts, and metrics visualization for API traffic and throttling behavior.
    humanURL: https://grafana.com/docs/grafana/latest/developers/http_api/
    baseURL: https://your-grafana.example.com/api
    tags:
      - Dashboards
      - Metrics
      - Monitoring
      - Observability
    properties:
      - type: Documentation
        url: https://grafana.com/docs/grafana/latest/developers/http_api/
      - type: OpenAPI
        url: https://raw.githubusercontent.com/grafana/grafana/main/public/api-spec.json
common:
  - type: Documentation
    url: https://en.wikipedia.org/wiki/Rate_limiting
  - type: Documentation
    url: https://www.rfc-editor.org/rfc/rfc6585#section-4
  - type: Features
    data:
      - name: Rate Limit Header Validation
        description: Verify that APIs return correct X-RateLimit-Limit, X-RateLimit-Remaining, and Retry-After headers.
      - name: 429 Response Testing
        description: Confirm that APIs return HTTP 429 Too Many Requests when rate limits are exceeded.
      - name: Quota Reset Verification
        description: Test that rate limit counters reset correctly after the defined window period.
      - name: Burst Allowance Testing
        description: Validate burst rate limits that allow short-term traffic spikes above baseline quotas.
      - name: Per-Consumer Rate Limiting
        description: Test that rate limits are correctly scoped to individual API keys or consumers.
      - name: Concurrent Request Testing
        description: Verify rate limiting behavior under concurrent parallel request loads.
  - type: UseCases
    data:
      - name: API Gateway Rate Limit Validation
        description: Verify that API gateway rate limiting plugins correctly enforce configured quotas.
      - name: Throttling Behavior Testing
        description: Test that API clients receive appropriate throttling signals and can implement retry logic.
      - name: Usage Tier Enforcement
        description: Validate that different subscription tiers enforce their respective rate limits correctly.
      - name: Rate Limit Recovery Testing
        description: Confirm that APIs correctly recover and allow traffic after rate limit windows reset.
      - name: Load Test Rate Limit Interaction
        description: Understand how rate limits interact with load testing to avoid false failures.
  - type: Integrations
    data:
      - name: k6
        description: Use k6 load testing tool to generate traffic for rate limit validation and testing.
      - name: Apache JMeter
        description: Use JMeter to send concurrent requests and validate rate limit enforcement.
      - name: Postman
        description: Use Postman test scripts to assert rate limit headers and 429 responses.
      - name: Prometheus
        description: Monitor rate limit metrics with Prometheus for alerting and trend analysis.
  - type: JSONSchema
    url: json-schema/test-rate-limit-check-rate-limit-config-schema.json
  - type: JSONSchema
    url: json-schema/test-rate-limit-check-rate-limit-response-schema.json
  - type: JSONSchema
    url: json-schema/test-rate-limit-check-quota-schema.json
  - type: JSONLD
    url: json-ld/test-rate-limit-check-context.jsonld
  - type: Vocabulary
    url: vocabulary/test-rate-limit-check-vocabulary.yml
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
    url: https://apievangelist.com
---
