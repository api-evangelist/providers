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
      - type: APIReference
        url: https://docs.newrelic.com/docs/apis/rest-api-v2/api-explorer-v2/introduction-new-relics-rest-api-explorer/
      - type: JSONSchema
        url: json-schema/openapi-mobile-application-response-type-schema.json
      - type: JSONSchema
        url: json-schema/openapi-synthetics-condition-schema.json
      - type: JSONSchema
        url: json-schema/openapi-metric-parser-response-type-schema.json
      - type: JSONSchema
        url: json-schema/openapi-application-links-response-schema.json
      - type: JSONSchema
        url: json-schema/openapi-external-service-condition-body-schema.json
      - type: JSONSchema
        url: json-schema/openapi-label-body-schema.json
      - type: JSONSchema
        url: json-schema/openapi-label-schema.json
      - type: JSONSchema
        url: json-schema/openapi-external-service-condition-response-type-schema.json
      - type: JSONSchema
        url: json-schema/openapi-metric-data-response-schema.json
      - type: JSONSchema
        url: json-schema/openapi-policy-channels-response-type-schema.json
      - type: JSONSchema
        url: json-schema/openapi-deployment-response-type-schema.json
      - type: JSONSchema
        url: json-schema/openapi-application-instance-response-type-schema.json
      - type: JSONSchema
        url: json-schema/openapi-app-summary-data-response-schema.json
      - type: JSONSchema
        url: json-schema/openapi-deployment-schema.json
      - type: JSONSchema
        url: json-schema/openapi-browser-application-schema.json
      - type: JSONSchema
        url: json-schema/openapi-app-summary-response-schema.json
      - type: JSONSchema
        url: json-schema/openapi-policy-response-schema.json
      - type: JSONSchema
        url: json-schema/openapi-application-instance-links-response-schema.json
      - type: JSONSchema
        url: json-schema/openapi-policy-channels-response-schema.json
      - type: JSONSchema
        url: json-schema/openapi-incident-response-type-schema.json
      - type: JSONSchema
        url: json-schema/openapi-channel-response-type-schema.json
      - type: JSONSchema
        url: json-schema/openapi-channel-response-schema.json
      - type: JSONSchema
        url: json-schema/openapi-application-schema.json
      - type: JSONSchema
        url: json-schema/openapi-label-origins-response-schema.json
      - type: JSONSchema
        url: json-schema/openapi-violation-response-schema.json
      - type: JSONSchema
        url: json-schema/openapi-app-settings-response-schema.json
      - type: JSONSchema
        url: json-schema/openapi-condition-response-schema.json
      - type: JSONSchema
        url: json-schema/openapi-deployment-links-response-schema.json
      - type: JSONSchema
        url: json-schema/openapi-incident-response-schema.json
      - type: JSONSchema
        url: json-schema/openapi-metric-response-schema.json
      - type: JSONSchema
        url: json-schema/openapi-metric-data-response-type-schema.json
      - type: JSONSchema
        url: json-schema/openapi-key-transaction-response-schema.json
      - type: JSONSchema
        url: json-schema/openapi-mobile-application-response-schema.json
      - type: JSONSchema
        url: json-schema/openapi-condition-body-schema.json
      - type: JSONSchema
        url: json-schema/openapi-label-links-response-schema.json
      - type: JSONSchema
        url: json-schema/openapi-application-body-schema.json
      - type: JSONSchema
        url: json-schema/openapi-policy-response-type-schema.json
      - type: JSONSchema
        url: json-schema/openapi-application-instance-response-schema.json
      - type: JSONSchema
        url: json-schema/openapi-ijkterms-type-schema.json
      - type: JSONSchema
        url: json-schema/openapi-violation-entity-response-schema.json
      - type: JSONSchema
        url: json-schema/openapi-recent-event-response-type-schema.json
      - type: JSONSchema
        url: json-schema/openapi-external-service-condition-schema.json
      - type: JSONSchema
        url: json-schema/openapi-label-response-schema.json
      - type: JSONSchema
        url: json-schema/openapi-deployment-response-schema.json
      - type: JSONSchema
        url: json-schema/openapi-nrql-body-schema.json
      - type: JSONSchema
        url: json-schema/openapi-browser-application-body-schema.json
      - type: JSONSchema
        url: json-schema/openapi-browser-application-response-type-schema.json
      - type: JSONSchema
        url: json-schema/openapi-channel-schema.json
      - type: JSONSchema
        url: json-schema/openapi-incident-links-response-schema.json
      - type: JSONSchema
        url: json-schema/openapi-condition-response-type-schema.json
      - type: JSONSchema
        url: json-schema/openapi-application-response-type-schema.json
      - type: JSONSchema
        url: json-schema/openapi-timeslice-response-schema.json
      - type: JSONSchema
        url: json-schema/openapi-violation-response-type-schema.json
      - type: JSONSchema
        url: json-schema/openapi-end-user-summary-data-response-schema.json
      - type: JSONSchema
        url: json-schema/openapi-condition-schema.json
      - type: JSONSchema
        url: json-schema/openapi-metric-list-response-schema.json
      - type: JSONSchema
        url: json-schema/openapi-application-host-links-response-schema.json
      - type: JSONSchema
        url: json-schema/openapi-channel-body-schema.json
      - type: JSONSchema
        url: json-schema/openapi-external-service-condition-response-schema.json
      - type: JSONSchema
        url: json-schema/openapi-channel-links-response-schema.json
      - type: JSONSchema
        url: json-schema/openapi-nrql-condition-schema.json
      - type: JSONSchema
        url: json-schema/openapi-synthetics-condition-response-schema.json
      - type: JSONSchema
        url: json-schema/openapi-policy-body-schema.json
      - type: JSONSchema
        url: json-schema/openapi-end-user-summary-response-schema.json
      - type: JSONSchema
        url: json-schema/openapi-synthetics-condition-body-schema.json
      - type: JSONSchema
        url: json-schema/openapi-application-host-response-type-schema.json
      - type: JSONSchema
        url: json-schema/openapi-browser-application-response-schema.json
      - type: JSONSchema
        url: json-schema/openapi-nrql-condition-body-schema.json
      - type: JSONSchema
        url: json-schema/openapi-key-transaction-response-type-schema.json
      - type: JSONSchema
        url: json-schema/openapi-metric-parser-response-schema.json
      - type: JSONSchema
        url: json-schema/openapi-nrql-response-schema.json
      - type: JSONSchema
        url: json-schema/openapi-application-host-response-schema.json
      - type: JSONSchema
        url: json-schema/openapi-app-settings-body-schema.json
      - type: JSONSchema
        url: json-schema/openapi-nrql-condition-response-type-schema.json
      - type: JSONSchema
        url: json-schema/openapi-violation-links-response-schema.json
      - type: JSONSchema
        url: json-schema/openapi-key-transaction-links-response-schema.json
      - type: JSONSchema
        url: json-schema/openapi-recent-event-response-schema.json
      - type: JSONSchema
        url: json-schema/openapi-synthetics-condition-response-type-schema.json
      - type: JSONSchema
        url: json-schema/openapi-user-defined-condition-body-schema.json
      - type: JSONSchema
        url: json-schema/openapi-user-defined-condition-response-schema.json
      - type: JSONSchema
        url: json-schema/openapi-deployment-body-schema.json
      - type: JSONSchema
        url: json-schema/openapi-nrql-condition-response-schema.json
      - type: JSONSchema
        url: json-schema/openapi-crash-summary-response-schema.json
      - type: JSONSchema
        url: json-schema/openapi-policy-schema.json
      - type: JSONSchema
        url: json-schema/openapi-label-response-type-schema.json
      - type: JSONSchema
        url: json-schema/openapi-application-response-schema.json
      - type: JSONSchema
        url: json-schema/openapi-label-links-body-schema.json
      - type: JSONSchema
        url: json-schema/openapi-mobile-summary-data-response-schema.json
      - type: JSONLD
        url: json-ld/new-relic-openapi-context.jsonld
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
      - type: APIReference
        url: https://docs.newrelic.com/docs/apis/nerdgraph/get-started/nerdgraph-explorer/
      - type: Authentication
        url: https://docs.newrelic.com/docs/apis/intro-apis/new-relic-api-keys/
      - type: RateLimits
        url: https://docs.newrelic.com/docs/apis/nerdgraph/nerdgraph-usage-limits/
      - type: GettingStarted
        url: https://docs.newrelic.com/docs/apis/nerdgraph/get-started/introduction-new-relic-nerdgraph/
      - type: Console
        url: https://api.newrelic.com/graphiql
      - type: Resources
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
      - type: APIReference
        url: https://docs.newrelic.com/docs/data-apis/ingest-apis/metric-api/report-metrics-metric-api/
      - type: Authentication
        url: https://docs.newrelic.com/docs/apis/intro-apis/new-relic-api-keys/
      - type: RateLimits
        url: https://docs.newrelic.com/docs/data-apis/ingest-apis/metric-api/metric-api-limits-restricted-attributes/
      - type: OpenAPI
        url: openapi/new-relic-metric-api-openapi.yml
      - type: JSONSchema
        url: json-schema/new-relic-metric-payload-schema.json
      - type: JSONSchema
        url: json-schema/metric-api-common-block-schema.json
      - type: JSONSchema
        url: json-schema/metric-api-summary-value-schema.json
      - type: JSONSchema
        url: json-schema/metric-api-metric-data-object-schema.json
      - type: JSONSchema
        url: json-schema/metric-api-metric-data-point-schema.json
      - type: JSONSchema
        url: json-schema/metric-api-metric-payload-schema.json
      - type: JSONSchema
        url: json-schema/metric-api-accepted-response-schema.json
      - type: JSONLD
        url: json-ld/new-relic-metric-api-context.jsonld
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
      - type: RateLimits
        url: https://docs.newrelic.com/docs/data-apis/custom-data/custom-events/data-requirements-limits-custom-event-data/
      - type: JSONSchema
        url: json-schema/event-api-success-response-schema.json
      - type: JSONSchema
        url: json-schema/event-api-custom-event-schema.json
      - type: JSONSchema
        url: json-schema/event-api-event-payload-schema.json
      - type: JSONLD
        url: json-ld/new-relic-event-api-context.jsonld
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
      - type: APIReference
        url: https://docs.newrelic.com/docs/logs/forward-logs/enable-log-management-new-relic/
      - type: OpenAPI
        url: openapi/new-relic-log-api-openapi.yml
      - type: JSONSchema
        url: json-schema/log-api-log-data-object-schema.json
      - type: JSONSchema
        url: json-schema/log-api-accepted-response-schema.json
      - type: JSONSchema
        url: json-schema/log-api-log-record-schema.json
      - type: JSONSchema
        url: json-schema/log-api-common-block-schema.json
      - type: JSONSchema
        url: json-schema/log-api-log-payload-schema.json
      - type: JSONLD
        url: json-ld/new-relic-log-api-context.jsonld
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
      - type: APIReference
        url: https://docs.newrelic.com/docs/distributed-tracing/trace-api/trace-api-general-requirements-limits/
      - type: Authentication
        url: https://docs.newrelic.com/docs/apis/intro-apis/new-relic-api-keys/
      - type: OpenAPI
        url: openapi/new-relic-trace-api-openapi.yml
      - type: RateLimits
        url: https://docs.newrelic.com/docs/distributed-tracing/trace-api/trace-api-general-requirements-limits/
      - type: JSONSchema
        url: json-schema/trace-api-new-relic-trace-payload-schema.json
      - type: JSONSchema
        url: json-schema/trace-api-accepted-response-schema.json
      - type: JSONSchema
        url: json-schema/trace-api-common-block-schema.json
      - type: JSONSchema
        url: json-schema/trace-api-zipkin-span-schema.json
      - type: JSONSchema
        url: json-schema/trace-api-span-schema.json
      - type: JSONSchema
        url: json-schema/trace-api-zipkin-trace-payload-schema.json
      - type: JSONSchema
        url: json-schema/trace-api-span-batch-schema.json
      - type: JSONLD
        url: json-ld/new-relic-trace-api-context.jsonld
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
      - type: APIReference
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
      - type: SDK
        url: https://github.com/newrelic/newrelic-browser-agent
        title: Browser Agent SDK
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
      - type: SDK
        url: https://docs.newrelic.com/docs/data-apis/ingest-apis/telemetry-sdks-report-custom-telemetry-data/
      - type: GitHubRepository
        url: https://github.com/newrelic/newrelic-telemetry-sdk-java
      - type: SDK
        url: https://github.com/newrelic/newrelic-telemetry-sdk-python
        title: Python Telemetry SDK
      - type: SDK
        url: https://github.com/newrelic/newrelic-telemetry-sdk-go
        title: Go Telemetry SDK
      - type: SDK
        url: https://github.com/newrelic/newrelic-telemetry-sdk-dotnet
        title: .NET Telemetry SDK
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
      - type: GettingStarted
        url: https://docs.newrelic.com/docs/opentelemetry/opentelemetry-introduction/
      - type: APIReference
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
      - type: APIReference
        url: https://docs.newrelic.com/docs/new-relic-control/fleet-control/overview/
      - type: GettingStarted
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
      - type: APIReference
        url: https://docs.newrelic.com/docs/mobile-monitoring/new-relic-mobile-ios/get-started/introduction-new-relic-mobile-ios/
      - type: GitHubRepository
        url: https://github.com/newrelic/newrelic-ios-agent
      - type: SDK
        url: https://github.com/newrelic/newrelic-android-agent
        title: Android Agent SDK
      - type: SDK
        url: https://github.com/newrelic/newrelic-unity-agent
        title: Unity Agent SDK
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
created: '2025-01-13'
modified: '2026-05-04'
position: Consumer
description: New Relic provides observability platform APIs for monitoring, analyzing, and optimizing your entire software stack with real-time insights into applications, infrastructure, and customer experience.
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
specificationVersion: '0.19'
common:
  - name: New Relic | Monitor, Debug and Improve Your Entire Stack
    description: 'null'
    url: https://newrelic.com/
    type: Portal
  - name: Transparent Pricing - Start for Free | New Relic
    description: 'null'
    url: https://newrelic.com/pricing
    type: Pricing
  - name: New Relic Documentation
    description: 'null'
    url: https://docs.newrelic.com/
    type: Documentation
  - name: Terms of Service Agreement | New Relic
    description: 'null'
    url: https://newrelic.com/termsandconditions/terms
    type: TermsOfService
  - name: General Data Privacy Notice
    description: 'null'
    url: https://newrelic.com/termsandconditions/privacy
    type: PrivacyPolicy
  - name: The New Relic Blog | New Relic
    description: 'null'
    url: https://newrelic.com/blog
    type: Blog
  - name: New Relic Partner Program | New Relic
    description: 'null'
    url: https://newrelic.com/solutions/partners
    type: Partners
  - name: New Relic Trust Center
    description: 'null'
    url: https://trust.newrelic.com/
    type: TrustCenter
  - name: Log in to New Relic
    description: 'null'
    url: https://login.newrelic.com/login
    type: Login
  - name: Sign Up
    description: 'null'
    url: https://newrelic.com/signup
    type: SignUp
  - url: https://one.newrelic.com/
    name: New Relic Platform Console
    type: Console
  - url: https://developer.newrelic.com/
    name: New Relic Developer Portal
    type: Portal
  - url: https://docs.newrelic.com/docs/apis/intro-apis/new-relic-api-keys/
    name: New Relic API Keys
    type: Authentication
  - url: https://support.newrelic.com/
    name: New Relic Support
    type: Support
  - url: https://status.newrelic.com/
    name: New Relic Status
    type: StatusPage
  - url: https://github.com/newrelic
    name: New Relic GitHub Organization
    type: GitHubOrganization
  - url: https://discuss.newrelic.com/
    name: New Relic Explorers Hub Community Forum
    type: Support
  - url: https://docs.newrelic.com/docs/new-relic-solutions/get-started/intro-new-relic/
    name: Get Started with New Relic
    type: GettingStarted
  - url: https://docs.newrelic.com/whats-new/
    name: What's New in New Relic
    type: ChangeLog
  - url: https://docs.newrelic.com/docs/release-notes/
    name: New Relic Release Notes
    type: ChangeLog
  - url: https://docs.newrelic.com/docs/data-apis/manage-data/view-system-limits/
    name: New Relic Data Limits
    type: RateLimits
  - url: https://stackoverflow.com/questions/tagged/new-relic
    name: New Relic on Stack Overflow
    type: StackOverflow
  - url: https://opensource.newrelic.com/
    name: New Relic Open Source
    type: GitHubOrganization
  - url: https://www.youtube.com/@NewRelicInc
    name: New Relic YouTube Channel
    type: YouTube
  - url: json-ld/new-relic-context.jsonld
    name: New Relic JSON-LD Context
    type: JSON-LD
  - url: json-schema/new-relic-metric-payload-schema.json
    name: New Relic Metric Payload Schema
    type: JSONSchema
  - url: json-schema/new-relic-event-payload-schema.json
    name: New Relic Event Payload Schema
    type: JSONSchema
  - url: https://twitter.com/newrelic
    name: New Relic on X (Twitter)
    type: X
  - url: https://www.linkedin.com/company/new-relic-inc-
    name: New Relic on LinkedIn
    type: LinkedIn
  - url: https://newrelic.com/security
    name: New Relic Security Overview
    type: Security
  - url: https://newrelic.com/security/compliance-certifications
    name: New Relic Compliance and Certifications
    type: Security
  - url: https://github.com/newrelic/newrelic-cli
    name: New Relic CLI
    type: CLI
  - url: https://docs.newrelic.com/docs/new-relic-solutions/build-nr-ui/newrelic-cli/
    name: New Relic CLI Reference
    type: CLI
  - url: https://registry.terraform.io/providers/newrelic/newrelic/latest/docs
    name: New Relic Terraform Provider
    type: GitHubRepository
  - url: https://github.com/newrelic/terraform-provider-newrelic
    name: New Relic Terraform Provider GitHub Repository
    type: GitHubRepository
  - url: https://www.postman.com/new-relic/
    name: New Relic Postman Workspace
    type: Resources
  - url: https://docs.newrelic.com/docs/apis/intro-apis/introduction-new-relic-apis/
    name: Introduction to New Relic APIs
    type: Documentation
  - url: https://docs.newrelic.com/docs/nrql/get-started/introduction-nrql-new-relics-query-language/
    name: Introduction to NRQL
    type: Documentation
  - type: Features
    name: New Relic Platform Features
    data:
      - 'Free: 100 GB/mo ingest, 1 full-platform user, unlimited basic users'
      - 'Standard: $10 first user, $99 additional (max 5)'
      - 'Pro: $349/user/yr unlimited full-platform users'
      - 'Enterprise: FedRAMP/HIPAA, 1-hr critical SLA'
      - $0.40/GB Original Data, $0.60/GB Data Plus beyond 100 GB free
      - NerdGraph (GraphQL) API at api.newrelic.com/graphql
      - 'NerdGraph rate limit: 3,000 req/min/user-key'
      - 'Insights query API: 1,000 queries/min'
      - 'Insights insert: 100,000 events/min'
      - 'Metric API: 100,000 req/min'
      - OpenTelemetry, Prometheus, Pixie, AWS, GCP, Azure integrations
      - APM, Browser, Mobile, Logs, Infrastructure, Synthetics
      - AI Monitoring for LLM observability
      - User keys, license keys, ingest keys
      - Live archive (Data Plus)
      - Custom dashboards via NRQL
    sources:
      - https://newrelic.com/pricing
    updated: '2026-05-04'
  - type: UseCases
    name: New Relic Use Cases
    data:
      - name: Full-Stack Observability
        description: Gain unified visibility across applications, infrastructure, and digital experiences to quickly identify and resolve issues.
      - name: Cloud Migration Monitoring
        description: Monitor and validate cloud migration progress with baseline comparisons and performance tracking across hybrid environments.
      - name: DevOps and CI/CD Integration
        description: Integrate observability into development workflows with deployment markers, error tracking, and automated testing.
      - name: Site Reliability Engineering
        description: Define and track SLOs, manage error budgets, and implement reliability practices with data-driven insights.
      - name: Incident Response and Management
        description: Detect, diagnose, and resolve incidents faster with correlated telemetry, anomaly detection, and automated workflows.
      - name: Digital Experience Monitoring
        description: Measure and optimize end-user experience across web, mobile, and synthetic channels.
      - name: Capacity Planning
        description: Analyze resource utilization trends and forecast capacity needs to optimize infrastructure spending.
      - name: Compliance and Audit
        description: Maintain audit trails, security compliance, and data governance across observability data.
  - type: Integrations
    name: New Relic Integrations
    url: https://newrelic.com/instant-observability
    data:
      - name: Amazon Web Services
        description: Monitor AWS services including EC2, Lambda, RDS, S3, ECS, EKS, and CloudWatch with native integration.
      - name: Microsoft Azure
        description: Monitor Azure services including VMs, App Service, Functions, AKS, and Azure Monitor with native integration.
      - name: Google Cloud Platform
        description: Monitor GCP services including Compute Engine, Cloud Functions, GKE, BigQuery, and Cloud Monitoring.
      - name: Kubernetes
        description: Monitor Kubernetes clusters with automatic discovery, Pixie integration, and OpenTelemetry support.
      - name: Prometheus
        description: Ingest Prometheus metrics using remote write or the Prometheus OpenMetrics integration.
      - name: OpenTelemetry
        description: Native OTLP endpoint support for ingesting metrics, traces, and logs from OpenTelemetry-instrumented applications.
      - name: Terraform
        description: Provision and manage New Relic resources as code using the official Terraform provider.
      - name: Grafana
        description: Query New Relic data from Grafana dashboards using the Grafana data source plugin.
      - name: PagerDuty
        description: Send alert notifications to PagerDuty for incident management and on-call escalation.
      - name: Slack
        description: Receive alert notifications and share observability insights directly in Slack channels.
      - name: Jira
        description: Create Jira issues from New Relic errors and alerts for issue tracking and resolution workflows.
      - name: ServiceNow
        description: Integrate with ServiceNow for ITSM workflows, incident creation, and change management.
      - name: GitHub
        description: Connect repositories for code-level visibility, error linking, and deployment tracking via CodeStream.
      - name: Docker
        description: Monitor Docker containers with automatic instrumentation and container-level metrics.
      - name: Apache Kafka
        description: Monitor Kafka clusters, topics, consumer groups, and message throughput.
      - name: MySQL
        description: Monitor MySQL database performance with query analysis, connection tracking, and replication metrics.
      - name: PostgreSQL
        description: Monitor PostgreSQL database performance with query analysis, index usage, and connection metrics.
      - name: MongoDB
        description: Monitor MongoDB instances with query performance, replication status, and cluster metrics.
      - name: Redis
        description: Monitor Redis instances with memory usage, command statistics, and key metrics.
      - name: Nginx
        description: Monitor Nginx web server performance with request rates, error rates, and upstream metrics.
  - type: SDK
    url: https://github.com/newrelic/newrelic-java-agent
    name: New Relic Java Agent
    title: Java Agent
  - type: SDK
    url: https://github.com/newrelic/newrelic-python-agent
    name: New Relic Python Agent
    title: Python Agent
  - type: SDK
    url: https://github.com/newrelic/node-newrelic
    name: New Relic Node.js Agent
    title: Node.js Agent
  - type: SDK
    url: https://github.com/newrelic/go-agent
    name: New Relic Go Agent
    title: Go Agent
  - type: SDK
    url: https://github.com/newrelic/newrelic-dotnet-agent
    name: New Relic .NET Agent
    title: .NET Agent
  - type: SDK
    url: https://github.com/newrelic/newrelic-ruby-agent
    name: New Relic Ruby Agent
    title: Ruby Agent
  - type: SDK
    url: https://github.com/newrelic/newrelic-php-agent
    name: New Relic PHP Agent
    title: PHP Agent
  - type: SDK
    url: https://github.com/newrelic/infrastructure-agent
    name: New Relic Infrastructure Agent
  - type: GitHubRepository
    url: https://github.com/newrelic/helm-charts
    name: New Relic Helm Charts
  - type: CodeExamples
    url: https://github.com/newrelic/newrelic-opentelemetry-examples
    name: New Relic OpenTelemetry Examples
  - type: SpectralRules
    url: rules/new-relic-spectral-rules.yml
    name: New Relic Spectral Rules
  - type: Vocabulary
    url: vocabulary/new-relic-vocabulary.yaml
    name: New Relic Vocabulary
  - type: NaftikoCapability
    url: capabilities/application-monitoring.yaml
    name: New Relic Application Monitoring
  - type: NaftikoCapability
    url: capabilities/full-stack-observability.yaml
    name: New Relic Full Stack Observability
  - type: NaftikoCapability
    url: capabilities/telemetry-ingestion.yaml
    name: New Relic Telemetry Ingestion
---
