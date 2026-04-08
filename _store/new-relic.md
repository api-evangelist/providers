---
aid: new-relic
url: https://raw.githubusercontent.com/api-evangelist/new-relic/refs/heads/main/apis.yml
apis:
- aid: new-relic:new-relic-rest-api-v2
  name: New Relic REST API v2
  description: The New Relic REST API v2 is the original HTTP REST interface for querying application performance data, configuring alerts, and managing account settings. New Relic recommends NerdGraph (GraphQL) for new integrations, as the REST API v2 is in maintenance mode with minimal ongoing development.
  image: https://newrelic.com/themes/custom/erno/assets/mediakit/new_relic_logo_horizontal.png
  humanURL: https://docs.newrelic.com/docs/apis/rest-api-v2/get-started/introduction-new-relic-rest-api-v2/
  baseURL: https://api.newrelic.com/v2/
  properties:
  - type: Documentation
    url: https://docs.newrelic.com/docs/apis/rest-api-v2/get-started/introduction-new-relic-rest-api-v2/
  - type: OpenAPI
    url: openapi/new-relic-openapi.yml
  - type: Authentication
    url: https://docs.newrelic.com/docs/apis/intro-apis/new-relic-api-keys/
  - type: Reference
    url: https://docs.newrelic.com/docs/apis/rest-api-v2/api-explorer-v2/introduction-new-relics-rest-api-explorer/
  tags:
  - APM
  - Applications
  - Monitoring
  - REST
- aid: new-relic:new-relic-nerdgraph-api
  name: New Relic NerdGraph API
  description: NerdGraph is New Relic's primary GraphQL API for querying observability data, managing account configuration, and accessing the full breadth of New Relic platform capabilities. It is the recommended API for new integrations, replacing the older REST API v2 for most use cases.
  image: https://newrelic.com/themes/custom/erno/assets/mediakit/new_relic_logo_horizontal.png
  humanURL: https://docs.newrelic.com/docs/apis/nerdgraph/get-started/introduction-new-relic-nerdgraph/
  baseURL: https://api.newrelic.com/graphql
  properties:
  - type: Documentation
    url: https://docs.newrelic.com/docs/apis/nerdgraph/get-started/introduction-new-relic-nerdgraph/
  - type: Reference
    url: https://docs.newrelic.com/docs/apis/nerdgraph/get-started/nerdgraph-explorer/
  - type: Authentication
    url: https://docs.newrelic.com/docs/apis/intro-apis/new-relic-api-keys/
  - type: Rate Limits
    url: https://docs.newrelic.com/docs/apis/nerdgraph/nerdgraph-usage-limits/
  - type: Getting Started
    url: https://docs.newrelic.com/docs/apis/nerdgraph/get-started/introduction-new-relic-nerdgraph/
  - type: GraphQL Explorer
    url: https://api.newrelic.com/graphiql
  - type: Postman Collection
    url: https://www.postman.com/new-relic/new-relic-graphql-api-collection/documentation/btuxnnc/new-relic-nerdgraph-graphql-api-collection
  tags:
  - GraphQL
  - Monitoring
  - Observability
  - Platform
- aid: new-relic:new-relic-metric-api
  name: New Relic Metric API
  description: The New Relic Metric API is an HTTP endpoint for ingesting dimensional metric data directly into the New Relic platform. It accepts JSON payloads via POST requests and is the underlying API used by Telemetry SDKs and open source exporters such as Prometheus and DropWizard.
  image: https://newrelic.com/themes/custom/erno/assets/mediakit/new_relic_logo_horizontal.png
  humanURL: https://docs.newrelic.com/docs/data-apis/ingest-apis/metric-api/introduction-metric-api/
  baseURL: https://metric-api.newrelic.com/metric/v1
  properties:
  - type: Documentation
    url: https://docs.newrelic.com/docs/data-apis/ingest-apis/metric-api/introduction-metric-api/
  - type: Reference
    url: https://docs.newrelic.com/docs/data-apis/ingest-apis/metric-api/report-metrics-metric-api/
  - type: Authentication
    url: https://docs.newrelic.com/docs/apis/intro-apis/new-relic-api-keys/
  - type: Rate Limits
    url: https://docs.newrelic.com/docs/data-apis/ingest-apis/metric-api/metric-api-limits-restricted-attributes/
  - type: OpenAPI
    url: openapi/new-relic-metric-api-openapi.yml
  - type: JSONSchema
    url: json-schema/new-relic-metric-payload-schema.json
  tags:
  - Ingest
  - Metrics
  - Monitoring
  - Telemetry
- aid: new-relic:new-relic-event-api
  name: New Relic Event API
  description: The New Relic Event API allows you to send custom event data to the New Relic platform via HTTP POST. Custom events submitted through this API can be queried and visualized using NRQL, making it suitable for tracking arbitrary business or application events.
  image: https://newrelic.com/themes/custom/erno/assets/mediakit/new_relic_logo_horizontal.png
  humanURL: https://docs.newrelic.com/docs/data-apis/ingest-apis/event-api/introduction-event-api/
  baseURL: https://insights-collector.newrelic.com/v1/accounts
  properties:
  - type: Documentation
    url: https://docs.newrelic.com/docs/data-apis/ingest-apis/event-api/introduction-event-api/
  - type: Authentication
    url: https://docs.newrelic.com/docs/apis/intro-apis/new-relic-api-keys/
  - type: OpenAPI
    url: openapi/new-relic-event-api-openapi.yml
  - type: JSONSchema
    url: json-schema/new-relic-event-payload-schema.json
  - type: Rate Limits
    url: https://docs.newrelic.com/docs/data-apis/custom-data/custom-events/data-requirements-limits-custom-event-data/
  tags:
  - Custom Data
  - Events
  - Ingest
  - Telemetry
- aid: new-relic:new-relic-log-api
  name: New Relic Log API
  description: The New Relic Log API enables log data to be sent directly to the New Relic platform via HTTP POST requests. It accepts compressed JSON payloads and provides an alternative to log forwarding agents when direct integration is preferred.
  image: https://newrelic.com/themes/custom/erno/assets/mediakit/new_relic_logo_horizontal.png
  humanURL: https://docs.newrelic.com/docs/logs/log-api/introduction-log-api/
  baseURL: https://log-api.newrelic.com/log/v1
  properties:
  - type: Documentation
    url: https://docs.newrelic.com/docs/logs/log-api/introduction-log-api/
  - type: Authentication
    url: https://docs.newrelic.com/docs/apis/intro-apis/new-relic-api-keys/
  - type: Reference
    url: https://docs.newrelic.com/docs/logs/forward-logs/enable-log-management-new-relic/
  - type: OpenAPI
    url: openapi/new-relic-log-api-openapi.yml
  tags:
  - Ingest
  - Log Management
  - Logs
  - Telemetry
- aid: new-relic:new-relic-trace-api
  name: New Relic Trace API
  description: The New Relic Trace API allows distributed tracing data to be sent directly to New Relic in either New Relic format or Zipkin JSON v2 format. It is used by Telemetry SDKs, open source integrations, and custom tracing implementations that need to report span data without a full APM agent.
  image: https://newrelic.com/themes/custom/erno/assets/mediakit/new_relic_logo_horizontal.png
  humanURL: https://docs.newrelic.com/docs/distributed-tracing/trace-api/introduction-trace-api/
  baseURL: https://trace-api.newrelic.com/trace/v1
  properties:
  - type: Documentation
    url: https://docs.newrelic.com/docs/distributed-tracing/trace-api/introduction-trace-api/
  - type: Reference
    url: https://docs.newrelic.com/docs/distributed-tracing/trace-api/trace-api-general-requirements-limits/
  - type: Authentication
    url: https://docs.newrelic.com/docs/apis/intro-apis/new-relic-api-keys/
  - type: OpenAPI
    url: openapi/new-relic-trace-api-openapi.yml
  - type: Rate Limits
    url: https://docs.newrelic.com/docs/distributed-tracing/trace-api/trace-api-general-requirements-limits/
  tags:
  - Distributed Tracing
  - Ingest
  - Telemetry
  - Traces
- aid: new-relic:new-relic-alerts-api
  name: New Relic Alerts API
  description: The New Relic Alerts REST API provides endpoints for programmatically managing alert policies, conditions, notification channels, and muting rules. New Relic recommends using NerdGraph for new alert management integrations, as the REST Alerts API is in maintenance mode.
  image: https://newrelic.com/themes/custom/erno/assets/mediakit/new_relic_logo_horizontal.png
  humanURL: https://docs.newrelic.com/docs/alerts/scale-automate/rest-api/rest-api-calls-alerts/
  baseURL: https://api.newrelic.com/v2/
  properties:
  - type: Documentation
    url: https://docs.newrelic.com/docs/alerts/scale-automate/rest-api/rest-api-calls-alerts/
  - type: Authentication
    url: https://docs.newrelic.com/docs/apis/intro-apis/new-relic-api-keys/
  tags:
  - Alerts
  - Monitoring
  - Notifications
  - REST
- aid: new-relic:new-relic-synthetics-api
  name: New Relic Synthetics API
  description: The New Relic Synthetics API, available through NerdGraph, allows you to programmatically create, update, delete, and query synthetic monitors including ping monitors, scripted API monitors, browser monitors, and broken links monitors. A legacy REST-based Synthetics API is also available but NerdGraph is the recommended approach.
  image: https://newrelic.com/themes/custom/erno/assets/mediakit/new_relic_logo_horizontal.png
  humanURL: https://docs.newrelic.com/docs/synthetics/synthetic-monitoring/administration/synthetics-api/
  baseURL: https://api.newrelic.com/graphql
  properties:
  - type: Documentation
    url: https://docs.newrelic.com/docs/synthetics/synthetic-monitoring/administration/synthetics-api/
  - type: Reference
    url: https://docs.newrelic.com/docs/apis/nerdgraph/examples/synthetics-api/overview/
  - type: Authentication
    url: https://docs.newrelic.com/docs/apis/intro-apis/new-relic-api-keys/
  tags:
  - Monitoring
  - Synthetics
  - Testing
  - Uptime Monitoring
- aid: new-relic:new-relic-infrastructure-alerts-api
  name: New Relic Infrastructure Alerts API
  description: The New Relic Infrastructure Alerts REST API provides endpoints for creating and managing infrastructure-specific alert conditions such as host, process, and integration alert conditions. It uses the infra-api.newrelic.com endpoint and is separate from the general Alerts REST API.
  image: https://newrelic.com/themes/custom/erno/assets/mediakit/new_relic_logo_horizontal.png
  humanURL: https://docs.newrelic.com/docs/infrastructure/infrastructure-alerts/rest-api-calls-new-relic-infrastructure-alerts/
  baseURL: https://infra-api.newrelic.com/v2/
  properties:
  - type: Documentation
    url: https://docs.newrelic.com/docs/infrastructure/infrastructure-alerts/rest-api-calls-new-relic-infrastructure-alerts/
  - type: Authentication
    url: https://docs.newrelic.com/docs/apis/intro-apis/new-relic-api-keys/
  tags:
  - Alerts
  - Infrastructure
  - Monitoring
  - REST
- aid: new-relic:new-relic-browser-api
  name: New Relic Browser API
  description: The New Relic Browser API provides JavaScript methods for extending and customizing browser monitoring data collection within the New Relic browser agent. Developers can use it to add custom attributes, record custom events, track page actions, and control agent behavior programmatically.
  image: https://newrelic.com/themes/custom/erno/assets/mediakit/new_relic_logo_horizontal.png
  humanURL: https://docs.newrelic.com/docs/browser/new-relic-browser/browser-apis/using-browser-apis/
  baseURL: https://bam.nr-data.net
  properties:
  - type: Documentation
    url: https://docs.newrelic.com/docs/browser/new-relic-browser/browser-apis/using-browser-apis/
  - type: Authentication
    url: https://docs.newrelic.com/docs/apis/intro-apis/new-relic-api-keys/
  tags:
  - Browser
  - JavaScript
  - Monitoring
  - Real User Monitoring
- aid: new-relic:new-relic-partnership-api
  name: New Relic Partnership API
  description: The New Relic Partnership API is a web service API for New Relic partners that enables them to create, edit, upgrade, downgrade, and cancel New Relic accounts on behalf of their customers. It is available only to New Relic partner accounts with partnership-level access.
  image: https://newrelic.com/themes/custom/erno/assets/mediakit/new_relic_logo_horizontal.png
  humanURL: https://docs.newrelic.com/docs/new-relic-partnerships/partner-integration-guide/partner-account-maintenance/partner-api/
  baseURL: https://rpm.newrelic.com/api/v2/partners/
  properties:
  - type: Documentation
    url: https://docs.newrelic.com/docs/new-relic-partnerships/partner-integration-guide/partner-account-maintenance/partner-api/
  - type: Authentication
    url: https://docs.newrelic.com/docs/apis/intro-apis/new-relic-api-keys/
  tags:
  - Account Management
  - Partners
  - Platform
- aid: new-relic:new-relic-telemetry-sdk
  name: New Relic Telemetry SDKs
  description: The New Relic Telemetry SDKs are open source client libraries for sending metrics, events, logs, and traces (MELT) to New Relic using the ingest APIs. SDKs are available for Java, Python, Node.js, Go, .NET, and C, and are released under the Apache 2.0 license on GitHub.
  image: https://newrelic.com/themes/custom/erno/assets/mediakit/new_relic_logo_horizontal.png
  humanURL: https://docs.newrelic.com/docs/data-apis/ingest-apis/telemetry-sdks-report-custom-telemetry-data/
  baseURL: https://metric-api.newrelic.com
  properties:
  - type: Documentation
    url: https://docs.newrelic.com/docs/data-apis/ingest-apis/telemetry-sdks-report-custom-telemetry-data/
  - type: Client Libraries
    url: https://docs.newrelic.com/docs/data-apis/ingest-apis/telemetry-sdks-report-custom-telemetry-data/
  - type: GitHubRepository
    url: https://github.com/newrelic/newrelic-telemetry-sdk-java
  tags:
  - Client Libraries
  - Open Source
  - SDKs
  - Telemetry
- aid: new-relic:new-relic-opentelemetry-otlp
  name: New Relic OpenTelemetry OTLP Endpoint
  description: New Relic provides a native OTLP (OpenTelemetry Protocol) endpoint that accepts metrics, traces, and logs from any OpenTelemetry-instrumented application or OTLP exporter. It supports both gRPC and HTTP/protobuf transport and is the recommended integration path for OpenTelemetry users.
  image: https://newrelic.com/themes/custom/erno/assets/mediakit/new_relic_logo_horizontal.png
  humanURL: https://docs.newrelic.com/docs/opentelemetry/best-practices/opentelemetry-otlp/
  baseURL: https://otlp.nr-data.net
  properties:
  - type: Documentation
    url: https://docs.newrelic.com/docs/opentelemetry/best-practices/opentelemetry-otlp/
  - type: Getting Started
    url: https://docs.newrelic.com/docs/opentelemetry/opentelemetry-introduction/
  - type: Reference
    url: https://docs.newrelic.com/docs/opentelemetry/best-practices/opentelemetry-data-overview/
  tags:
  - Ingest
  - OpenTelemetry
  - OTLP
  - Telemetry
- aid: new-relic:new-relic-control
  name: New Relic Control
  description: New Relic Control is an observability control plane that unifies Fleet Control, Agent Control, and Pipeline Control into a single management layer. It enables DevOps and platform teams to remotely deploy, configure, update, and monitor New Relic agents and OpenTelemetry collectors across Kubernetes clusters and hosts without manual per-host intervention. Fleet Control manages agent lifecycles at scale via a remote configuration API.
  image: https://newrelic.com/themes/custom/erno/assets/mediakit/new_relic_logo_horizontal.png
  humanURL: https://docs.newrelic.com/docs/new-relic-control/getting-started/
  baseURL: https://api.newrelic.com
  properties:
  - type: Documentation
    url: https://docs.newrelic.com/docs/new-relic-control/getting-started/
  - type: Reference
    url: https://docs.newrelic.com/docs/new-relic-control/fleet-control/overview/
  - type: Getting Started
    url: https://docs.newrelic.com/docs/new-relic-control/getting-started/
  tags:
  - Agent Management
  - Automation
  - Fleet Control
  - Observability
  - Platform
- aid: new-relic:new-relic-nrql-lookups-api
  name: New Relic NRQL Lookups API
  description: The New Relic NRQL Lookups API is a REST API for managing lookup tables that can be used to enrich NRQL query results. It supports creating, updating, downloading, listing, and deleting lookup tables in both CSV and JSON formats, enabling automated lookup table maintenance for data enrichment workflows.
  image: https://newrelic.com/themes/custom/erno/assets/mediakit/new_relic_logo_horizontal.png
  humanURL: https://docs.newrelic.com/docs/apis/lookups-service-api/lookups-service-api/
  baseURL: https://nrql-lookup.service.newrelic.com
  properties:
  - type: Documentation
    url: https://docs.newrelic.com/docs/apis/lookups-service-api/lookups-service-api/
  - type: Authentication
    url: https://docs.newrelic.com/docs/apis/intro-apis/new-relic-api-keys/
  tags:
  - Data Enrichment
  - Lookups
  - NRQL
  - REST
- aid: new-relic:new-relic-security-data-api
  name: New Relic Security Data API
  description: The New Relic Security Data API allows vulnerability and security finding data to be sent directly to New Relic via HTTP POST. It accepts JSON payloads describing detected vulnerabilities or security events, enabling integration with third-party vulnerability assessment tools and custom security scanning solutions for use with New Relic Security RX.
  image: https://newrelic.com/themes/custom/erno/assets/mediakit/new_relic_logo_horizontal.png
  humanURL: https://docs.newrelic.com/docs/data-apis/ingest-apis/security-data-api/
  baseURL: https://security-api.newrelic.com/security/v1
  properties:
  - type: Documentation
    url: https://docs.newrelic.com/docs/data-apis/ingest-apis/security-data-api/
  - type: Authentication
    url: https://docs.newrelic.com/docs/apis/intro-apis/new-relic-api-keys/
  tags:
  - Compliance
  - Ingest
  - Security
  - Vulnerabilities
- aid: new-relic:new-relic-mobile-sdk
  name: New Relic Mobile SDK
  description: The New Relic Mobile SDK provides iOS and Android APIs for extending mobile monitoring data collection beyond what the agent captures automatically. Developers can add custom attributes, record custom events, track user interactions, report handled exceptions, set custom user IDs, and control agent behavior within iOS (Swift/Objective-C) and Android (Java/Kotlin) applications.
  image: https://newrelic.com/themes/custom/erno/assets/mediakit/new_relic_logo_horizontal.png
  humanURL: https://docs.newrelic.com/docs/mobile-monitoring/new-relic-mobile/mobile-sdk/mobile-sdk-api-guide/
  baseURL: https://mobile-collector.newrelic.com
  properties:
  - type: Documentation
    url: https://docs.newrelic.com/docs/mobile-monitoring/new-relic-mobile/mobile-sdk/mobile-sdk-api-guide/
  - type: Reference
    url: https://docs.newrelic.com/docs/mobile-monitoring/new-relic-mobile-ios/get-started/introduction-new-relic-mobile-ios/
  - type: GitHubRepository
    url: https://github.com/newrelic/newrelic-ios-agent
  tags:
  - Android
  - iOS
  - Mobile
  - Monitoring
  - SDK
name: New Relic
tags:
- Analysis
- Analytics
- APM
- DevOps
- Infrastructure
- Monitoring
- Observability
- Performance
- Platform
type: Index
image: https://newrelic.com/themes/custom/erno/assets/mediakit/new_relic_logo_horizontal.png
access: 3rd-Party
common:
- url: https://newrelic.com/
  name: New Relic | Monitor, Debug and Improve Your Entire Stack
  type: Website
  description: 'null'
- url: https://newrelic.com/pricing
  name: Transparent Pricing - Start for Free | New Relic
  type: Pricing
  description: 'null'
- url: https://docs.newrelic.com/
  name: New Relic Documentation
  type: Documentation
  description: 'null'
- url: https://newrelic.com/termsandconditions/terms
  name: Terms of Service Agreement | New Relic
  type: TermsOfService
  description: 'null'
- url: https://newrelic.com/termsandconditions/privacy
  name: General Data Privacy Notice
  type: PrivacyPolicy
  description: 'null'
- url: https://newrelic.com/blog
  name: The New Relic Blog | New Relic
  type: Blog
  description: 'null'
- url: https://newrelic.com/solutions/partners
  name: New Relic Partner Program | New Relic
  type: Partners
  description: 'null'
- url: https://trust.newrelic.com/
  name: New Relic Trust Center
  type: Trust
  description: 'null'
- url: https://login.newrelic.com/?return_to=https%3A%2F%2Fone.newrelic.com%2F%3F_gl%3D1*19a3oxl*_gcl_au*Nzg1NjU0MjMwLjE3NTQzMzY1MDA.*_ga*MTAzNDMwMjA3Ny4xNzU0MzM2NTAw*_ga_R5EF3MCG7B*czE3NTQzMzY1MDAkbzEkZzEkdDE3NTQzMzY2MzgkajUwJGwxJGgxNjk1MTcwNzcy
  name: Log in to New Relic
  type: Login
  description: 'null'
- url: https://newrelic.com/signup?via=login
  name: Sign Up
  type: SignUp
  description: 'null'
created: '2025-01-13'
modified: '2026-04-07'
position: Consumer
description: New Relic provides observability platform APIs for monitoring, analyzing, and optimizing your entire software stack with real-time insights into applications, infrastructure, and customer experience.
maintainers:
- FN: Kin Lane
  email: info@apievangelist.com
specificationVersion: '0.19'
---

