---
access_model:
  confidence: high
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: true
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    asyncapi_events: true
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: verified
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 49.5
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 32
  human_in_the_loop: 0
  name: New Relic Agentic Access
  operation_count: 62
  slug: new-relic-agentic-access
  summary_line: 62 operations · 32 acting
api_count: 41
apis:
- description: NerdGraph is New Relic's primary GraphQL API for querying observability data, managing account configuration, and accessing the full breadth of New Relic platform capabilities. It is the recommended A
  name: New Relic NerdGraph API
  slug: new-relic-nerdgraph-api
- description: The New Relic Alerts REST API provides endpoints for programmatically managing alert policies, conditions, notification channels, and muting rules. New Relic recommends using NerdGraph for new alert m
  name: New Relic Alerts API
  slug: new-relic-alerts-api
- description: The New Relic Synthetics API, available through NerdGraph, allows you to programmatically create, update, delete, and query synthetic monitors including ping monitors, scripted API monitors, browser m
  name: New Relic Synthetics API
  slug: new-relic-synthetics-api
- description: 'The New Relic Infrastructure Alerts REST API provides endpoints for creating and managing infrastructure-specific alert conditions such as host, process, and integration alert conditions. It uses the '
  name: New Relic Infrastructure Alerts API
  slug: new-relic-infrastructure-alerts-api
- description: The New Relic Browser API provides JavaScript methods for extending and customizing browser monitoring data collection within the New Relic browser agent. Developers can use it to add custom attribute
  name: New Relic Browser API
  slug: new-relic-browser-api
- description: The New Relic Partnership API is a web service API for New Relic partners that enables them to create, edit, upgrade, downgrade, and cancel New Relic accounts on behalf of their customers. It is avail
  name: New Relic Partnership API
  slug: new-relic-partnership-api
- description: The New Relic Telemetry SDKs are open source client libraries for sending metrics, events, logs, and traces (MELT) to New Relic using the ingest APIs. SDKs are available for Java, Python, Node.js, Go,
  name: New Relic Telemetry SDKs
  slug: new-relic-telemetry-sdk
- description: New Relic provides a native OTLP (OpenTelemetry Protocol) endpoint that accepts metrics, traces, and logs from any OpenTelemetry-instrumented application or OTLP exporter. It supports both gRPC and HT
  name: New Relic OpenTelemetry OTLP Endpoint
  slug: new-relic-opentelemetry-otlp
- description: New Relic Control is an observability control plane that unifies Fleet Control, Agent Control, and Pipeline Control into a single management layer. It enables DevOps and platform teams to remotely dep
  name: New Relic Control
  slug: new-relic-control
- description: 'The New Relic NRQL Lookups API is a REST API for managing lookup tables that can be used to enrich NRQL query results. It supports creating, updating, downloading, listing, and deleting lookup tables '
  name: New Relic NRQL Lookups API
  slug: new-relic-nrql-lookups-api
- description: 'The New Relic Security Data API allows vulnerability and security finding data to be sent directly to New Relic via HTTP POST. It accepts JSON payloads describing detected vulnerabilities or security '
  name: New Relic Security Data API
  slug: new-relic-security-data-api
- description: The New Relic Mobile SDK provides iOS and Android APIs for extending mobile monitoring data collection beyond what the agent captures automatically. Developers can add custom attributes, record custom
  name: New Relic Mobile SDK
  slug: new-relic-mobile-sdk
- description: The Alerts API from New Relic — 23 operation(s) for alerts.
  name: New Relic Alerts API
  slug: new-relic-alerts-api
- description: The Applications API from New Relic — 18 operation(s) for applications.
  name: New Relic Applications API
  slug: new-relic-applications-api
- description: The Channel API from New Relic — 1 operation(s) for channel.
  name: New Relic Channel API
  slug: new-relic-channel-api
- description: The Channels API from New Relic — 3 operation(s) for channels.
  name: New Relic Channels API
  slug: new-relic-channels-api
- description: The Condition API from New Relic — 5 operation(s) for condition.
  name: New Relic Condition API
  slug: new-relic-condition-api
- description: The Conditions API from New Relic — 15 operation(s) for conditions.
  name: New Relic Conditions API
  slug: new-relic-conditions-api
- description: The Data API from New Relic — 4 operation(s) for data.
  name: New Relic Data API
  slug: new-relic-data-api
- description: The Delete API from New Relic — 11 operation(s) for delete.
  name: New Relic Delete API
  slug: new-relic-delete-api
- description: The Deployments API from New Relic — 2 operation(s) for deployments.
  name: New Relic Deployments API
  slug: new-relic-deployments-api
- description: The Entity API from New Relic — 1 operation(s) for entity.
  name: New Relic Entity API
  slug: new-relic-entity-api
- description: Custom event ingestion endpoints
  name: New Relic Events API
  slug: new-relic-events-api
- description: The External API from New Relic — 3 operation(s) for external.
  name: New Relic External API
  slug: new-relic-external-api
- description: The Failure API from New Relic — 2 operation(s) for failure.
  name: New Relic Failure API
  slug: new-relic-failure-api
- description: The Get API from New Relic — 30 operation(s) for get.
  name: New Relic Get API
  slug: new-relic-get-api
- description: The Hosts API from New Relic — 4 operation(s) for hosts.
  name: New Relic Hosts API
  slug: new-relic-hosts-api
- description: The Identifiers API from New Relic — 30 operation(s) for identifiers.
  name: New Relic Identifiers API
  slug: new-relic-identifiers-api
- description: The Instance API from New Relic — 2 operation(s) for instance.
  name: New Relic Instance API
  slug: new-relic-instance-api
- description: The Instances API from New Relic — 4 operation(s) for instances.
  name: New Relic Instances API
  slug: new-relic-instances-api
- description: The Keys API from New Relic — 2 operation(s) for keys.
  name: New Relic Keys API
  slug: new-relic-keys-api
- description: The Location API from New Relic — 2 operation(s) for location.
  name: New Relic Location API
  slug: new-relic-location-api
- description: Log data ingestion endpoints
  name: New Relic Logs API
  slug: new-relic-logs-api
- description: Metric data ingestion endpoints
  name: New Relic Metrics API
  slug: new-relic-metrics-api
- description: The Mobile API from New Relic — 4 operation(s) for mobile.
  name: New Relic Mobile API
  slug: new-relic-mobile-api
- description: The Policies API from New Relic — 8 operation(s) for policies.
  name: New Relic Policies API
  slug: new-relic-policies-api
- description: The Post API from New Relic — 8 operation(s) for post.
  name: New Relic Post API
  slug: new-relic-post-api
- description: The Put API from New Relic — 9 operation(s) for put.
  name: New Relic Put API
  slug: new-relic-put-api
- description: Distributed trace span ingestion
  name: New Relic Traces API
  slug: new-relic-traces-api
- description: The Transactions API from New Relic — 2 operation(s) for transactions.
  name: New Relic Transactions API
  slug: new-relic-transactions-api
- description: The Violations API from New Relic — 1 operation(s) for violations.
  name: New Relic Violations API
  slug: new-relic-violations-api
arazzos:
- description: Resolve an app, branch on health status, and pull recent metric data.
  name: New Relic Application Health Triage
  slug: new-relic-application-health-triage-workflow
- description: Create a policy condition then associate an entity with it.
  name: New Relic Associate Entity With Condition
  slug: new-relic-associate-entity-with-condition-workflow
- description: Create a notification channel and associate it with an alert policy.
  name: New Relic Attach Notification Channel To Policy
  slug: new-relic-attach-notification-channel-to-policy-workflow
- description: Create an alert policy and attach an APM metric condition to it.
  name: New Relic Create Alert Policy With Condition
  slug: new-relic-create-alert-policy-with-condition-workflow
- description: Create an alert policy and attach a NRQL alert condition to it.
  name: New Relic Create NRQL Alert Policy
  slug: new-relic-create-nrql-alert-policy-workflow
- description: Resolve a policy by name and attach a Synthetics monitor condition to it.
  name: New Relic Create Synthetics Alert Condition
  slug: new-relic-create-synthetics-alert-condition-workflow
- description: Resolve an alert policy by name and list its metric conditions.
  name: New Relic Find Policy And List Conditions
  slug: new-relic-find-policy-and-list-conditions-workflow
- description: Resolve an app, pick a host, list its metric names, and pull metric data.
  name: New Relic Host Metric Drilldown
  slug: new-relic-host-metric-drilldown-workflow
- description: Record a deployment marker then emit a matching custom deployment event.
  name: New Relic Ingest Deployment Telemetry
  slug: new-relic-ingest-deployment-telemetry-workflow
- description: Send a metric batch then send a correlated log batch in one flow.
  name: New Relic Ingest Metrics And Logs
  slug: new-relic-ingest-metrics-and-logs-workflow
- description: Send a distributed trace then emit a correlated custom event.
  name: New Relic Ingest Trace And Event
  slug: new-relic-ingest-trace-and-event-workflow
- description: Resolve a key transaction by name and read its detail record.
  name: New Relic Key Transaction Metric Report
  slug: new-relic-key-transaction-metric-report-workflow
- description: List mobile applications, select one, and pull its crash metric data.
  name: New Relic Mobile App Crash Report
  slug: new-relic-mobile-app-crash-report-workflow
- description: List open violations and branch into incident or event detail.
  name: New Relic Open Violations Triage
  slug: new-relic-open-violations-triage-workflow
- description: Create a policy, attach a NRQL condition, and wire a notification channel.
  name: New Relic Provision Alerting Stack
  slug: new-relic-provision-alerting-stack-workflow
- description: Resolve a policy by name, list its NRQL conditions, and delete one.
  name: New Relic Prune NRQL Condition
  slug: new-relic-prune-nrql-condition-workflow
- description: Resolve an application by name and record a deployment marker on it.
  name: New Relic Record Deployment Marker
  slug: new-relic-record-deployment-marker-workflow
- description: Resolve an application by name and update its display alias.
  name: New Relic Rename Application
  slug: new-relic-rename-application-workflow
- description: Resolve an app, find its latest deployment marker, and delete it.
  name: New Relic Rollback Deployment Marker
  slug: new-relic-rollback-deployment-marker-workflow
- description: Resolve a policy by name, update it, then update one of its conditions.
  name: New Relic Update Policy And Condition
  slug: new-relic-update-policy-and-condition-workflow
artifact_total: 957
asyncapis:
- description: Describes New Relic's documented event-driven and streaming surfaces. New Relic does not publish a customer-facing WebSocket or Server-Sent Events streaming endpoint, and the NerdGraph GraphQL API doe
  name: New Relic Streaming and Event-Driven Surfaces
  slug: new-relic-streaming-asyncapi
collections:
- collection_type: postman
  name: New Relic Event API
  slug: postman-new-relic-event-api
- collection_type: postman
  name: New Relic Log API
  slug: postman-new-relic-log-api
- collection_type: postman
  name: New Relic Metric API
  slug: postman-new-relic-metric-api
- collection_type: postman
  name: New Relic Trace API
  slug: postman-new-relic-trace-api
- collection_type: postman
  name: New Relic
  slug: postman-new-relic
- collection_type: open
  name: New Relic Event API
  slug: open-new-relic-event-api
- collection_type: open
  name: New Relic Log API
  slug: open-new-relic-log-api
- collection_type: open
  name: New Relic Metric API
  slug: open-new-relic-metric-api
- collection_type: open
  name: New Relic Trace API
  slug: open-new-relic-trace-api
- collection_type: open
  name: New Relic
  slug: open-new-relic
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/new-relic-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/new-relic-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/new-relic-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/new-relic-authentication.yml
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/new-relic/overview
- group: design
  title: ''
  type: Arazzo
  url: arazzo/new-relic-application-health-triage-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/new-relic-associate-entity-with-condition-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/new-relic-attach-notification-channel-to-policy-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/new-relic-create-alert-policy-with-condition-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/new-relic-create-nrql-alert-policy-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/new-relic-create-synthetics-alert-condition-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/new-relic-find-policy-and-list-conditions-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/new-relic-host-metric-drilldown-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/new-relic-ingest-deployment-telemetry-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/new-relic-ingest-metrics-and-logs-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/new-relic-ingest-trace-and-event-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/new-relic-key-transaction-metric-report-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/new-relic-mobile-app-crash-report-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/new-relic-open-violations-triage-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/new-relic-provision-alerting-stack-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/new-relic-prune-nrql-condition-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/new-relic-record-deployment-marker-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/new-relic-rename-application-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/new-relic-rollback-deployment-marker-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/new-relic-update-policy-and-condition-workflow.yml
- group: start
  title: ''
  type: Portal
  url: https://newrelic.com/
- group: commercial
  title: ''
  type: Pricing
  url: https://newrelic.com/pricing
- group: docs
  title: ''
  type: Documentation
  url: https://docs.newrelic.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://newrelic.com/termsandconditions/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://newrelic.com/termsandconditions/privacy
- group: company
  title: ''
  type: Blog
  url: https://newrelic.com/blog
- group: company
  title: ''
  type: Partners
  url: https://newrelic.com/solutions/partners
- group: auth
  title: ''
  type: TrustCenter
  url: https://trust.newrelic.com/
- group: start
  title: ''
  type: Login
  url: https://login.newrelic.com/login
- group: start
  title: ''
  type: Signup
  url: https://newrelic.com/signup
- group: start
  title: ''
  type: Console
  url: https://one.newrelic.com/
- group: start
  title: ''
  type: Portal
  url: https://developer.newrelic.com/
- group: auth
  title: ''
  type: Authentication
  url: https://docs.newrelic.com/docs/apis/intro-apis/new-relic-api-keys/
- group: operate
  title: ''
  type: Support
  url: https://support.newrelic.com/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.newrelic.com/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/newrelic
- group: operate
  title: ''
  type: Support
  url: https://discuss.newrelic.com/
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.newrelic.com/docs/new-relic-solutions/get-started/intro-new-relic/
- group: operate
  title: ''
  type: ChangeLog
  url: https://docs.newrelic.com/whats-new/
- group: operate
  title: ''
  type: ChangeLog
  url: https://docs.newrelic.com/docs/release-notes/
- group: operate
  title: ''
  type: RateLimits
  url: https://docs.newrelic.com/docs/data-apis/manage-data/view-system-limits/
- group: operate
  title: ''
  type: StackOverflow
  url: https://stackoverflow.com/questions/tagged/new-relic
- group: build
  title: ''
  type: GitHubOrganization
  url: https://opensource.newrelic.com/
- group: learn
  title: ''
  type: YouTube
  url: https://www.youtube.com/@NewRelicInc
- group: design
  title: ''
  type: JSONLD
  url: json-ld/new-relic-context.jsonld
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/new-relic-metric-payload-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/new-relic-event-payload-schema.json
- group: other
  title: ''
  type: X
  url: https://twitter.com/newrelic
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/new-relic-inc-
- group: auth
  title: ''
  type: Security
  url: https://newrelic.com/security
- group: auth
  title: ''
  type: Security
  url: https://newrelic.com/security/compliance-certifications
- group: build
  title: ''
  type: CLI
  url: https://github.com/newrelic/newrelic-cli
- group: build
  title: ''
  type: CLI
  url: https://docs.newrelic.com/docs/new-relic-solutions/build-nr-ui/newrelic-cli/
- group: build
  title: ''
  type: GitHubRepository
  url: https://registry.terraform.io/providers/newrelic/newrelic/latest/docs
- group: build
  title: ''
  type: GitHubRepository
  url: https://github.com/newrelic/terraform-provider-newrelic
- group: other
  title: ''
  type: Resources
  url: https://www.postman.com/new-relic/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.newrelic.com/docs/apis/intro-apis/introduction-new-relic-apis/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.newrelic.com/docs/nrql/get-started/introduction-nrql-new-relics-query-language/
- group: build
  title: Java Agent
  type: SDKs
  url: https://github.com/newrelic/newrelic-java-agent
- group: build
  title: Python Agent
  type: SDKs
  url: https://github.com/newrelic/newrelic-python-agent
- group: build
  title: Node.js Agent
  type: SDKs
  url: https://github.com/newrelic/node-newrelic
- group: build
  title: Go Agent
  type: SDKs
  url: https://github.com/newrelic/go-agent
- group: build
  title: .NET Agent
  type: SDKs
  url: https://github.com/newrelic/newrelic-dotnet-agent
- group: build
  title: Ruby Agent
  type: SDKs
  url: https://github.com/newrelic/newrelic-ruby-agent
- group: build
  title: PHP Agent
  type: SDKs
  url: https://github.com/newrelic/newrelic-php-agent
- group: build
  title: ''
  type: SDKs
  url: https://github.com/newrelic/infrastructure-agent
- group: build
  title: ''
  type: GitHubRepository
  url: https://github.com/newrelic/helm-charts
- group: build
  title: ''
  type: CodeExamples
  url: https://github.com/newrelic/newrelic-opentelemetry-examples
- group: design
  title: ''
  type: SpectralRules
  url: rules/new-relic-spectral-rules.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/new-relic-vocabulary.yaml
created: '2025-01-13'
description: New Relic provides observability platform APIs for monitoring, analyzing, and optimizing your entire software stack with real-time insights into applications, infrastructure, and customer experience.
examples:
- key_count: 2
  name: Event Api Custom Event Example
  slug: event-api-custom-event-example
- key_count: 2
  name: Event Api Success Response Example
  slug: event-api-success-response-example
- key_count: 1
  name: Log Api Accepted Response Example
  slug: log-api-accepted-response-example
- key_count: 2
  name: Log Api Common Block Example
  slug: log-api-common-block-example
- key_count: 2
  name: Log Api Log Data Object Example
  slug: log-api-log-data-object-example
- key_count: 5
  name: Log Api Log Record Example
  slug: log-api-log-record-example
- key_count: 1
  name: Metric Api Accepted Response Example
  slug: metric-api-accepted-response-example
- key_count: 3
  name: Metric Api Common Block Example
  slug: metric-api-common-block-example
- key_count: 2
  name: Metric Api Metric Data Object Example
  slug: metric-api-metric-data-object-example
- key_count: 6
  name: Metric Api Metric Data Point Example
  slug: metric-api-metric-data-point-example
- key_count: 4
  name: Metric Api Summary Value Example
  slug: metric-api-summary-value-example
- key_count: 3
  name: New Relic App Settings Body Example
  slug: new-relic-app-settings-body-example
- key_count: 4
  name: New Relic App Settings Response Example
  slug: new-relic-app-settings-response-example
- key_count: 5
  name: New Relic App Summary Data Response Example
  slug: new-relic-app-summary-data-response-example
- key_count: 8
  name: New Relic App Summary Response Example
  slug: new-relic-app-summary-response-example
- key_count: 2
  name: New Relic Application Body Example
  slug: new-relic-application-body-example
- key_count: 1
  name: New Relic Application Example
  slug: new-relic-application-example
- key_count: 3
  name: New Relic Application Host Links Response Example
  slug: new-relic-application-host-links-response-example
- key_count: 1
  name: New Relic Application Host Response Example
  slug: new-relic-application-host-response-example
- key_count: 8
  name: New Relic Application Host Response Type Example
  slug: new-relic-application-host-response-type-example
- key_count: 3
  name: New Relic Application Instance Links Response Example
  slug: new-relic-application-instance-links-response-example
- key_count: 1
  name: New Relic Application Instance Response Example
  slug: new-relic-application-instance-response-example
- key_count: 9
  name: New Relic Application Instance Response Type Example
  slug: new-relic-application-instance-response-type-example
- key_count: 3
  name: New Relic Application Links Response Example
  slug: new-relic-application-links-response-example
- key_count: 1
  name: New Relic Application Response Example
  slug: new-relic-application-response-example
- key_count: 10
  name: New Relic Application Response Type Example
  slug: new-relic-application-response-type-example
- key_count: 1
  name: New Relic Browser Application Body Example
  slug: new-relic-browser-application-body-example
- key_count: 1
  name: New Relic Browser Application Example
  slug: new-relic-browser-application-example
- key_count: 1
  name: New Relic Browser Application Response Example
  slug: new-relic-browser-application-response-example
- key_count: 4
  name: New Relic Browser Application Response Type Example
  slug: new-relic-browser-application-response-type-example
- key_count: 3
  name: New Relic Channel Body Example
  slug: new-relic-channel-body-example
- key_count: 1
  name: New Relic Channel Example
  slug: new-relic-channel-example
- key_count: 1
  name: New Relic Channel Links Response Example
  slug: new-relic-channel-links-response-example
- key_count: 1
  name: New Relic Channel Response Example
  slug: new-relic-channel-response-example
- key_count: 5
  name: New Relic Channel Response Type Example
  slug: new-relic-channel-response-type-example
- key_count: 10
  name: New Relic Condition Body Example
  slug: new-relic-condition-body-example
- key_count: 1
  name: New Relic Condition Example
  slug: new-relic-condition-example
- key_count: 1
  name: New Relic Condition Response Example
  slug: new-relic-condition-response-example
- key_count: 12
  name: New Relic Condition Response Type Example
  slug: new-relic-condition-response-type-example
- key_count: 4
  name: New Relic Crash Summary Response Example
  slug: new-relic-crash-summary-response-example
- key_count: 6
  name: New Relic Deletealertschannelschannelid Example
  slug: new-relic-deletealertschannelschannelid-example
- key_count: 6
  name: New Relic Deletealertsconditionsconditionid Example
  slug: new-relic-deletealertsconditionsconditionid-example
- key_count: 6
  name: New Relic Deletealertsentityconditionsentityid Example
  slug: new-relic-deletealertsentityconditionsentityid-example
- key_count: 6
  name: New Relic Deletealertsexternalserviceconditionsconditionid Example
  slug: new-relic-deletealertsexternalserviceconditionsconditionid-example
- key_count: 6
  name: New Relic Deletealertslocationfailureconditionsconditionid Example
  slug: new-relic-deletealertslocationfailureconditionsconditionid-example
- key_count: 6
  name: New Relic Deletealertsnrqlconditionsconditionid Example
  slug: new-relic-deletealertsnrqlconditionsconditionid-example
- key_count: 6
  name: New Relic Deletealertspoliciespolicyid Example
  slug: new-relic-deletealertspoliciespolicyid-example
- key_count: 6
  name: New Relic Deletealertspolicychannels Example
  slug: new-relic-deletealertspolicychannels-example
- key_count: 6
  name: New Relic Deletealertssyntheticsconditionsconditionid Example
  slug: new-relic-deletealertssyntheticsconditionsconditionid-example
- key_count: 6
  name: New Relic Deleteapplicationsid Example
  slug: new-relic-deleteapplicationsid-example
- key_count: 6
  name: New Relic Deleteapplicationsiddeploymentsid Example
  slug: new-relic-deleteapplicationsiddeploymentsid-example
- key_count: 4
  name: New Relic Deployment Body Example
  slug: new-relic-deployment-body-example
- key_count: 1
  name: New Relic Deployment Example
  slug: new-relic-deployment-example
- key_count: 1
  name: New Relic Deployment Links Response Example
  slug: new-relic-deployment-links-response-example
- key_count: 1
  name: New Relic Deployment Response Example
  slug: new-relic-deployment-response-example
- key_count: 7
  name: New Relic Deployment Response Type Example
  slug: new-relic-deployment-response-type-example
- key_count: 3
  name: New Relic End User Summary Data Response Example
  slug: new-relic-end-user-summary-data-response-example
- key_count: 4
  name: New Relic End User Summary Response Example
  slug: new-relic-end-user-summary-response-example
- key_count: 2
  name: New Relic Event Custom Event Example
  slug: new-relic-event-custom-event-example
- key_count: 3
  name: New Relic Event Error Response Example
  slug: new-relic-event-error-response-example
- key_count: 2
  name: New Relic Event Success Response Example
  slug: new-relic-event-success-response-example
- key_count: 8
  name: New Relic External Service Condition Body Example
  slug: new-relic-external-service-condition-body-example
- key_count: 1
  name: New Relic External Service Condition Example
  slug: new-relic-external-service-condition-example
- key_count: 1
  name: New Relic External Service Condition Response Example
  slug: new-relic-external-service-condition-response-example
- key_count: 9
  name: New Relic External Service Condition Response Type Example
  slug: new-relic-external-service-condition-response-type-example
- key_count: 6
  name: New Relic Getalertschannels Example
  slug: new-relic-getalertschannels-example
- key_count: 6
  name: New Relic Getalertsconditions Example
  slug: new-relic-getalertsconditions-example
- key_count: 6
  name: New Relic Getalertsentityconditionsentityid Example
  slug: new-relic-getalertsentityconditionsentityid-example
- key_count: 6
  name: New Relic Getalertsevents Example
  slug: new-relic-getalertsevents-example
- key_count: 6
  name: New Relic Getalertsexternalserviceconditions Example
  slug: new-relic-getalertsexternalserviceconditions-example
- key_count: 6
  name: New Relic Getalertsincidents Example
  slug: new-relic-getalertsincidents-example
- key_count: 6
  name: New Relic Getalertslocationfailureconditionspoliciespolicyid Example
  slug: new-relic-getalertslocationfailureconditionspoliciespolicyid-example
- key_count: 6
  name: New Relic Getalertsnrqlconditions Example
  slug: new-relic-getalertsnrqlconditions-example
- key_count: 6
  name: New Relic Getalertspolicies Example
  slug: new-relic-getalertspolicies-example
- key_count: 6
  name: New Relic Getalertssyntheticsconditions Example
  slug: new-relic-getalertssyntheticsconditions-example
- key_count: 6
  name: New Relic Getalertsviolations Example
  slug: new-relic-getalertsviolations-example
- key_count: 6
  name: New Relic Getapplications Example
  slug: new-relic-getapplications-example
- key_count: 6
  name: New Relic Getapplicationsid Example
  slug: new-relic-getapplicationsid-example
- key_count: 6
  name: New Relic Getapplicationsiddeployments Example
  slug: new-relic-getapplicationsiddeployments-example
- key_count: 6
  name: New Relic Getapplicationsidhosts Example
  slug: new-relic-getapplicationsidhosts-example
- key_count: 6
  name: New Relic Getapplicationsidhostshostidmetrics Example
  slug: new-relic-getapplicationsidhostshostidmetrics-example
- key_count: 6
  name: New Relic Getapplicationsidhostshostidmetricsdata Example
  slug: new-relic-getapplicationsidhostshostidmetricsdata-example
- key_count: 6
  name: New Relic Getapplicationsidhostsid Example
  slug: new-relic-getapplicationsidhostsid-example
- key_count: 6
  name: New Relic Getapplicationsidinstances Example
  slug: new-relic-getapplicationsidinstances-example
- key_count: 6
  name: New Relic Getapplicationsidinstancesid Example
  slug: new-relic-getapplicationsidinstancesid-example
- key_count: 6
  name: New Relic Getapplicationsidinstancesinstanceidmetrics Example
  slug: new-relic-getapplicationsidinstancesinstanceidmetrics-example
- key_count: 6
  name: New Relic Getapplicationsidinstancesinstanceidmetricsdata Example
  slug: new-relic-getapplicationsidinstancesinstanceidmetricsdata-example
- key_count: 6
  name: New Relic Getapplicationsidmetrics Example
  slug: new-relic-getapplicationsidmetrics-example
- key_count: 6
  name: New Relic Getapplicationsidmetricsdata Example
  slug: new-relic-getapplicationsidmetricsdata-example
- key_count: 6
  name: New Relic Getkeytransactions Example
  slug: new-relic-getkeytransactions-example
- key_count: 6
  name: New Relic Getkeytransactionsid Example
  slug: new-relic-getkeytransactionsid-example
- key_count: 6
  name: New Relic Getmobileapplications Example
  slug: new-relic-getmobileapplications-example
- key_count: 6
  name: New Relic Getmobileapplicationsid Example
  slug: new-relic-getmobileapplicationsid-example
- key_count: 6
  name: New Relic Getmobileapplicationsmobileapplicationidmetrics Example
  slug: new-relic-getmobileapplicationsmobileapplicationidmetrics-example
- key_count: 6
  name: New Relic Getmobileapplicationsmobileapplicationidmetricsdata Example
  slug: new-relic-getmobileapplicationsmobileapplicationidmetricsdata-example
- key_count: 5
  name: New Relic Ijk Terms Type Example
  slug: new-relic-ijk-terms-type-example
- key_count: 1
  name: New Relic Key Transaction Links Response Example
  slug: new-relic-key-transaction-links-response-example
- key_count: 1
  name: New Relic Key Transaction Response Example
  slug: new-relic-key-transaction-response-example
- key_count: 9
  name: New Relic Key Transaction Response Type Example
  slug: new-relic-key-transaction-response-type-example
- key_count: 3
  name: New Relic Label Body Example
  slug: new-relic-label-body-example
- key_count: 1
  name: New Relic Label Example
  slug: new-relic-label-example
- key_count: 2
  name: New Relic Label Links Body Example
  slug: new-relic-label-links-body-example
- key_count: 2
  name: New Relic Label Links Response Example
  slug: new-relic-label-links-response-example
- key_count: 3
  name: New Relic Label Origins Response Example
  slug: new-relic-label-origins-response-example
- key_count: 1
  name: New Relic Label Response Example
  slug: new-relic-label-response-example
- key_count: 5
  name: New Relic Label Response Type Example
  slug: new-relic-label-response-type-example
- key_count: 1
  name: New Relic Log Accepted Response Example
  slug: new-relic-log-accepted-response-example
- key_count: 2
  name: New Relic Log Common Block Example
  slug: new-relic-log-common-block-example
- key_count: 2
  name: New Relic Log Error Response Example
  slug: new-relic-log-error-response-example
- key_count: 2
  name: New Relic Log Log Data Object Example
  slug: new-relic-log-log-data-object-example
- key_count: 5
  name: New Relic Log Log Record Example
  slug: new-relic-log-log-record-example
- key_count: 1
  name: New Relic Metric Accepted Response Example
  slug: new-relic-metric-accepted-response-example
- key_count: 3
  name: New Relic Metric Common Block Example
  slug: new-relic-metric-common-block-example
- key_count: 1
  name: New Relic Metric Data Response Example
  slug: new-relic-metric-data-response-example
- key_count: 5
  name: New Relic Metric Data Response Type Example
  slug: new-relic-metric-data-response-type-example
- key_count: 2
  name: New Relic Metric Error Response Example
  slug: new-relic-metric-error-response-example
- key_count: 1
  name: New Relic Metric List Response Example
  slug: new-relic-metric-list-response-example
- key_count: 2
  name: New Relic Metric Metric Data Object Example
  slug: new-relic-metric-metric-data-object-example
- key_count: 6
  name: New Relic Metric Metric Data Point Example
  slug: new-relic-metric-metric-data-point-example
- key_count: 1
  name: New Relic Metric Parser Response Example
  slug: new-relic-metric-parser-response-example
- key_count: 2
  name: New Relic Metric Parser Response Type Example
  slug: new-relic-metric-parser-response-type-example
- key_count: 2
  name: New Relic Metric Response Example
  slug: new-relic-metric-response-example
- key_count: 4
  name: New Relic Metric Summary Value Example
  slug: new-relic-metric-summary-value-example
- key_count: 1
  name: New Relic Mobile Application Response Example
  slug: new-relic-mobile-application-response-example
- key_count: 6
  name: New Relic Mobile Application Response Type Example
  slug: new-relic-mobile-application-response-type-example
- key_count: 8
  name: New Relic Mobile Summary Data Response Example
  slug: new-relic-mobile-summary-data-response-example
- key_count: 2
  name: New Relic Nrql Body Example
  slug: new-relic-nrql-body-example
- key_count: 8
  name: New Relic Nrql Condition Body Example
  slug: new-relic-nrql-condition-body-example
- key_count: 1
  name: New Relic Nrql Condition Example
  slug: new-relic-nrql-condition-example
- key_count: 1
  name: New Relic Nrql Condition Response Example
  slug: new-relic-nrql-condition-response-example
- key_count: 10
  name: New Relic Nrql Condition Response Type Example
  slug: new-relic-nrql-condition-response-type-example
- key_count: 2
  name: New Relic Nrql Response Example
  slug: new-relic-nrql-response-example
- key_count: 2
  name: New Relic Policy Body Example
  slug: new-relic-policy-body-example
- key_count: 1
  name: New Relic Policy Channels Response Example
  slug: new-relic-policy-channels-response-example
- key_count: 2
  name: New Relic Policy Channels Response Type Example
  slug: new-relic-policy-channels-response-type-example
- key_count: 1
  name: New Relic Policy Example
  slug: new-relic-policy-example
- key_count: 1
  name: New Relic Policy Response Example
  slug: new-relic-policy-response-example
- key_count: 5
  name: New Relic Policy Response Type Example
  slug: new-relic-policy-response-type-example
- key_count: 6
  name: New Relic Postalertschannels Example
  slug: new-relic-postalertschannels-example
- key_count: 6
  name: New Relic Postalertsconditionspoliciespolicyid Example
  slug: new-relic-postalertsconditionspoliciespolicyid-example
- key_count: 6
  name: New Relic Postalertsexternalserviceconditionspoliciespolicyid Example
  slug: new-relic-postalertsexternalserviceconditionspoliciespolicyid-example
- key_count: 6
  name: New Relic Postalertslocationfailureconditionspoliciespolicyid Example
  slug: new-relic-postalertslocationfailureconditionspoliciespolicyid-example
- key_count: 6
  name: New Relic Postalertsnrqlconditionspoliciespolicyid Example
  slug: new-relic-postalertsnrqlconditionspoliciespolicyid-example
- key_count: 6
  name: New Relic Postalertspolicies Example
  slug: new-relic-postalertspolicies-example
- key_count: 6
  name: New Relic Postalertssyntheticsconditionspoliciespolicyid Example
  slug: new-relic-postalertssyntheticsconditionspoliciespolicyid-example
- key_count: 6
  name: New Relic Postapplicationsiddeployments Example
  slug: new-relic-postapplicationsiddeployments-example
- key_count: 6
  name: New Relic Putalertsconditionsconditionid Example
  slug: new-relic-putalertsconditionsconditionid-example
- key_count: 6
  name: New Relic Putalertsentityconditionsentityid Example
  slug: new-relic-putalertsentityconditionsentityid-example
- key_count: 6
  name: New Relic Putalertsexternalserviceconditionsconditionid Example
  slug: new-relic-putalertsexternalserviceconditionsconditionid-example
- key_count: 6
  name: New Relic Putalertslocationfailureconditionsconditionid Example
  slug: new-relic-putalertslocationfailureconditionsconditionid-example
- key_count: 6
  name: New Relic Putalertsnrqlconditionsconditionid Example
  slug: new-relic-putalertsnrqlconditionsconditionid-example
- key_count: 6
  name: New Relic Putalertspoliciespolicyid Example
  slug: new-relic-putalertspoliciespolicyid-example
- key_count: 6
  name: New Relic Putalertspolicychannels Example
  slug: new-relic-putalertspolicychannels-example
- key_count: 6
  name: New Relic Putalertssyntheticsconditionsconditionid Example
  slug: new-relic-putalertssyntheticsconditionsconditionid-example
- key_count: 6
  name: New Relic Putapplicationsid Example
  slug: new-relic-putapplicationsid-example
- key_count: 1
  name: New Relic Recent Event Response Example
  slug: new-relic-recent-event-response-example
- key_count: 10
  name: New Relic Recent Event Response Type Example
  slug: new-relic-recent-event-response-type-example
- key_count: 6
  name: New Relic Sendevents Example
  slug: new-relic-sendevents-example
- key_count: 6
  name: New Relic Sendlogs Example
  slug: new-relic-sendlogs-example
- key_count: 6
  name: New Relic Sendmetrics Example
  slug: new-relic-sendmetrics-example
- key_count: 6
  name: New Relic Sendtraces Example
  slug: new-relic-sendtraces-example
- key_count: 4
  name: New Relic Synthetics Condition Body Example
  slug: new-relic-synthetics-condition-body-example
- key_count: 1
  name: New Relic Synthetics Condition Example
  slug: new-relic-synthetics-condition-example
- key_count: 1
  name: New Relic Synthetics Condition Response Example
  slug: new-relic-synthetics-condition-response-example
- key_count: 5
  name: New Relic Synthetics Condition Response Type Example
  slug: new-relic-synthetics-condition-response-type-example
- key_count: 3
  name: New Relic Timeslice Response Example
  slug: new-relic-timeslice-response-example
- key_count: 1
  name: New Relic Trace Accepted Response Example
  slug: new-relic-trace-accepted-response-example
- key_count: 1
  name: New Relic Trace Common Block Example
  slug: new-relic-trace-common-block-example
- key_count: 2
  name: New Relic Trace Error Response Example
  slug: new-relic-trace-error-response-example
- key_count: 2
  name: New Relic Trace Span Batch Example
  slug: new-relic-trace-span-batch-example
- key_count: 4
  name: New Relic Trace Span Example
  slug: new-relic-trace-span-example
- key_count: 11
  name: New Relic Trace Zipkin Span Example
  slug: new-relic-trace-zipkin-span-example
- key_count: 2
  name: New Relic User Defined Condition Body Example
  slug: new-relic-user-defined-condition-body-example
- key_count: 2
  name: New Relic User Defined Condition Response Example
  slug: new-relic-user-defined-condition-response-example
- key_count: 5
  name: New Relic Violation Entity Response Example
  slug: new-relic-violation-entity-response-example
- key_count: 3
  name: New Relic Violation Links Response Example
  slug: new-relic-violation-links-response-example
- key_count: 1
  name: New Relic Violation Response Example
  slug: new-relic-violation-response-example
- key_count: 10
  name: New Relic Violation Response Type Example
  slug: new-relic-violation-response-type-example
- key_count: 3
  name: Openapi App Settings Body Example
  slug: openapi-app-settings-body-example
- key_count: 4
  name: Openapi App Settings Response Example
  slug: openapi-app-settings-response-example
- key_count: 5
  name: Openapi App Summary Data Response Example
  slug: openapi-app-summary-data-response-example
- key_count: 8
  name: Openapi App Summary Response Example
  slug: openapi-app-summary-response-example
- key_count: 2
  name: Openapi Application Body Example
  slug: openapi-application-body-example
- key_count: 1
  name: Openapi Application Example
  slug: openapi-application-example
- key_count: 3
  name: Openapi Application Host Links Response Example
  slug: openapi-application-host-links-response-example
- key_count: 1
  name: Openapi Application Host Response Example
  slug: openapi-application-host-response-example
- key_count: 8
  name: Openapi Application Host Response Type Example
  slug: openapi-application-host-response-type-example
- key_count: 3
  name: Openapi Application Instance Links Response Example
  slug: openapi-application-instance-links-response-example
- key_count: 1
  name: Openapi Application Instance Response Example
  slug: openapi-application-instance-response-example
- key_count: 9
  name: Openapi Application Instance Response Type Example
  slug: openapi-application-instance-response-type-example
- key_count: 3
  name: Openapi Application Links Response Example
  slug: openapi-application-links-response-example
- key_count: 1
  name: Openapi Application Response Example
  slug: openapi-application-response-example
- key_count: 10
  name: Openapi Application Response Type Example
  slug: openapi-application-response-type-example
- key_count: 1
  name: Openapi Browser Application Body Example
  slug: openapi-browser-application-body-example
- key_count: 1
  name: Openapi Browser Application Example
  slug: openapi-browser-application-example
- key_count: 1
  name: Openapi Browser Application Response Example
  slug: openapi-browser-application-response-example
- key_count: 4
  name: Openapi Browser Application Response Type Example
  slug: openapi-browser-application-response-type-example
- key_count: 3
  name: Openapi Channel Body Example
  slug: openapi-channel-body-example
- key_count: 1
  name: Openapi Channel Example
  slug: openapi-channel-example
- key_count: 1
  name: Openapi Channel Links Response Example
  slug: openapi-channel-links-response-example
- key_count: 1
  name: Openapi Channel Response Example
  slug: openapi-channel-response-example
- key_count: 5
  name: Openapi Channel Response Type Example
  slug: openapi-channel-response-type-example
- key_count: 10
  name: Openapi Condition Body Example
  slug: openapi-condition-body-example
- key_count: 1
  name: Openapi Condition Example
  slug: openapi-condition-example
- key_count: 1
  name: Openapi Condition Response Example
  slug: openapi-condition-response-example
- key_count: 12
  name: Openapi Condition Response Type Example
  slug: openapi-condition-response-type-example
- key_count: 4
  name: Openapi Crash Summary Response Example
  slug: openapi-crash-summary-response-example
- key_count: 4
  name: Openapi Deployment Body Example
  slug: openapi-deployment-body-example
- key_count: 1
  name: Openapi Deployment Example
  slug: openapi-deployment-example
- key_count: 1
  name: Openapi Deployment Links Response Example
  slug: openapi-deployment-links-response-example
- key_count: 1
  name: Openapi Deployment Response Example
  slug: openapi-deployment-response-example
- key_count: 7
  name: Openapi Deployment Response Type Example
  slug: openapi-deployment-response-type-example
- key_count: 3
  name: Openapi End User Summary Data Response Example
  slug: openapi-end-user-summary-data-response-example
- key_count: 4
  name: Openapi End User Summary Response Example
  slug: openapi-end-user-summary-response-example
- key_count: 8
  name: Openapi External Service Condition Body Example
  slug: openapi-external-service-condition-body-example
- key_count: 1
  name: Openapi External Service Condition Example
  slug: openapi-external-service-condition-example
- key_count: 1
  name: Openapi External Service Condition Response Example
  slug: openapi-external-service-condition-response-example
- key_count: 9
  name: Openapi External Service Condition Response Type Example
  slug: openapi-external-service-condition-response-type-example
- key_count: 5
  name: Openapi Ijkterms Type Example
  slug: openapi-ijkterms-type-example
- key_count: 2
  name: Openapi Incident Links Response Example
  slug: openapi-incident-links-response-example
- key_count: 1
  name: Openapi Incident Response Example
  slug: openapi-incident-response-example
- key_count: 5
  name: Openapi Incident Response Type Example
  slug: openapi-incident-response-type-example
- key_count: 1
  name: Openapi Key Transaction Links Response Example
  slug: openapi-key-transaction-links-response-example
- key_count: 1
  name: Openapi Key Transaction Response Example
  slug: openapi-key-transaction-response-example
- key_count: 9
  name: Openapi Key Transaction Response Type Example
  slug: openapi-key-transaction-response-type-example
- key_count: 3
  name: Openapi Label Body Example
  slug: openapi-label-body-example
- key_count: 1
  name: Openapi Label Example
  slug: openapi-label-example
- key_count: 2
  name: Openapi Label Links Body Example
  slug: openapi-label-links-body-example
- key_count: 2
  name: Openapi Label Links Response Example
  slug: openapi-label-links-response-example
- key_count: 3
  name: Openapi Label Origins Response Example
  slug: openapi-label-origins-response-example
- key_count: 1
  name: Openapi Label Response Example
  slug: openapi-label-response-example
- key_count: 5
  name: Openapi Label Response Type Example
  slug: openapi-label-response-type-example
- key_count: 1
  name: Openapi Metric Data Response Example
  slug: openapi-metric-data-response-example
- key_count: 5
  name: Openapi Metric Data Response Type Example
  slug: openapi-metric-data-response-type-example
- key_count: 1
  name: Openapi Metric List Response Example
  slug: openapi-metric-list-response-example
- key_count: 1
  name: Openapi Metric Parser Response Example
  slug: openapi-metric-parser-response-example
- key_count: 2
  name: Openapi Metric Parser Response Type Example
  slug: openapi-metric-parser-response-type-example
- key_count: 2
  name: Openapi Metric Response Example
  slug: openapi-metric-response-example
- key_count: 1
  name: Openapi Mobile Application Response Example
  slug: openapi-mobile-application-response-example
- key_count: 6
  name: Openapi Mobile Application Response Type Example
  slug: openapi-mobile-application-response-type-example
- key_count: 8
  name: Openapi Mobile Summary Data Response Example
  slug: openapi-mobile-summary-data-response-example
- key_count: 2
  name: Openapi Nrql Body Example
  slug: openapi-nrql-body-example
- key_count: 8
  name: Openapi Nrql Condition Body Example
  slug: openapi-nrql-condition-body-example
- key_count: 1
  name: Openapi Nrql Condition Example
  slug: openapi-nrql-condition-example
- key_count: 1
  name: Openapi Nrql Condition Response Example
  slug: openapi-nrql-condition-response-example
- key_count: 10
  name: Openapi Nrql Condition Response Type Example
  slug: openapi-nrql-condition-response-type-example
- key_count: 2
  name: Openapi Nrql Response Example
  slug: openapi-nrql-response-example
- key_count: 2
  name: Openapi Policy Body Example
  slug: openapi-policy-body-example
- key_count: 1
  name: Openapi Policy Channels Response Example
  slug: openapi-policy-channels-response-example
- key_count: 2
  name: Openapi Policy Channels Response Type Example
  slug: openapi-policy-channels-response-type-example
- key_count: 1
  name: Openapi Policy Example
  slug: openapi-policy-example
- key_count: 1
  name: Openapi Policy Response Example
  slug: openapi-policy-response-example
- key_count: 5
  name: Openapi Policy Response Type Example
  slug: openapi-policy-response-type-example
- key_count: 1
  name: Openapi Recent Event Response Example
  slug: openapi-recent-event-response-example
- key_count: 10
  name: Openapi Recent Event Response Type Example
  slug: openapi-recent-event-response-type-example
- key_count: 4
  name: Openapi Synthetics Condition Body Example
  slug: openapi-synthetics-condition-body-example
- key_count: 1
  name: Openapi Synthetics Condition Example
  slug: openapi-synthetics-condition-example
- key_count: 1
  name: Openapi Synthetics Condition Response Example
  slug: openapi-synthetics-condition-response-example
- key_count: 5
  name: Openapi Synthetics Condition Response Type Example
  slug: openapi-synthetics-condition-response-type-example
- key_count: 3
  name: Openapi Timeslice Response Example
  slug: openapi-timeslice-response-example
- key_count: 2
  name: Openapi User Defined Condition Body Example
  slug: openapi-user-defined-condition-body-example
- key_count: 2
  name: Openapi User Defined Condition Response Example
  slug: openapi-user-defined-condition-response-example
- key_count: 5
  name: Openapi Violation Entity Response Example
  slug: openapi-violation-entity-response-example
- key_count: 3
  name: Openapi Violation Links Response Example
  slug: openapi-violation-links-response-example
- key_count: 1
  name: Openapi Violation Response Example
  slug: openapi-violation-response-example
- key_count: 10
  name: Openapi Violation Response Type Example
  slug: openapi-violation-response-type-example
- key_count: 1
  name: Trace Api Accepted Response Example
  slug: trace-api-accepted-response-example
- key_count: 1
  name: Trace Api Common Block Example
  slug: trace-api-common-block-example
- key_count: 2
  name: Trace Api Span Batch Example
  slug: trace-api-span-batch-example
- key_count: 4
  name: Trace Api Span Example
  slug: trace-api-span-example
- key_count: 11
  name: Trace Api Zipkin Span Example
  slug: trace-api-zipkin-span-example
features:
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
finops:
- name: New Relic Finops
  service_category: Observability
  slug: new-relic-finops
graphqls:
- description: NerdGraph is New Relic's primary GraphQL API for querying observability data, managing account configuration, and accessing the full breadth of New Relic platform capabilities. It is the recommended A
  name: New Relic GraphQL API
  slug: new-relic-graphql
image: https://newrelic.com/themes/custom/erno/assets/mediakit/new_relic_logo_horizontal.png
integrations:
- description: Monitor AWS services including EC2, Lambda, RDS, S3, ECS, EKS, and CloudWatch with native integration.
  name: Amazon Web Services
- description: Monitor Azure services including VMs, App Service, Functions, AKS, and Azure Monitor with native integration.
  name: Microsoft Azure
- description: Monitor GCP services including Compute Engine, Cloud Functions, GKE, BigQuery, and Cloud Monitoring.
  name: Google Cloud Platform
- description: Monitor Kubernetes clusters with automatic discovery, Pixie integration, and OpenTelemetry support.
  name: Kubernetes
- description: Ingest Prometheus metrics using remote write or the Prometheus OpenMetrics integration.
  name: Prometheus
- description: Native OTLP endpoint support for ingesting metrics, traces, and logs from OpenTelemetry-instrumented applications.
  name: OpenTelemetry
- description: Provision and manage New Relic resources as code using the official Terraform provider.
  name: Terraform
- description: Query New Relic data from Grafana dashboards using the Grafana data source plugin.
  name: Grafana
- description: Send alert notifications to PagerDuty for incident management and on-call escalation.
  name: PagerDuty
- description: Receive alert notifications and share observability insights directly in Slack channels.
  name: Slack
- description: Create Jira issues from New Relic errors and alerts for issue tracking and resolution workflows.
  name: Jira
- description: Integrate with ServiceNow for ITSM workflows, incident creation, and change management.
  name: ServiceNow
- description: Connect repositories for code-level visibility, error linking, and deployment tracking via CodeStream.
  name: GitHub
- description: Monitor Docker containers with automatic instrumentation and container-level metrics.
  name: Docker
- description: Monitor Kafka clusters, topics, consumer groups, and message throughput.
  name: Apache Kafka
- description: Monitor MySQL database performance with query analysis, connection tracking, and replication metrics.
  name: MySQL
- description: Monitor PostgreSQL database performance with query analysis, index usage, and connection metrics.
  name: PostgreSQL
- description: Monitor MongoDB instances with query performance, replication status, and cluster metrics.
  name: MongoDB
- description: Monitor Redis instances with memory usage, command statistics, and key metrics.
  name: Redis
- description: Monitor Nginx web server performance with request rates, error rates, and upstream metrics.
  name: Nginx
json_schemas:
- name: CustomEvent
  property_count: 2
  slug: event-api-custom-event
- name: EventPayload
  property_count: 0
  slug: event-api-event-payload
- name: SuccessResponse
  property_count: 2
  slug: event-api-success-response
- name: AcceptedResponse
  property_count: 1
  slug: log-api-accepted-response
- name: CommonBlock
  property_count: 2
  slug: log-api-common-block
- name: LogDataObject
  property_count: 2
  slug: log-api-log-data-object
- name: LogPayload
  property_count: 0
  slug: log-api-log-payload
- name: LogRecord
  property_count: 5
  slug: log-api-log-record
- name: AcceptedResponse
  property_count: 1
  slug: metric-api-accepted-response
- name: CommonBlock
  property_count: 3
  slug: metric-api-common-block
- name: MetricDataObject
  property_count: 2
  slug: metric-api-metric-data-object
- name: MetricDataPoint
  property_count: 6
  slug: metric-api-metric-data-point
- name: MetricPayload
  property_count: 0
  slug: metric-api-metric-payload
- name: SummaryValue
  property_count: 4
  slug: metric-api-summary-value
- name: AcceptedResponse
  property_count: 1
  slug: new-relic-acceptedresponse
- name: AppSettingsBody
  property_count: 3
  slug: new-relic-app-settings-body
- name: AppSettingsResponse
  property_count: 4
  slug: new-relic-app-settings-response
- name: AppSummaryDataResponse
  property_count: 5
  slug: new-relic-app-summary-data-response
- name: AppSummaryResponse
  property_count: 8
  slug: new-relic-app-summary-response
- name: ApplicationBody
  property_count: 2
  slug: new-relic-application-body
- name: ApplicationHostLinksResponse
  property_count: 3
  slug: new-relic-application-host-links-response
- name: ApplicationHostResponse
  property_count: 1
  slug: new-relic-application-host-response
- name: ApplicationHostResponseType
  property_count: 8
  slug: new-relic-application-host-response-type
- name: ApplicationInstanceLinksResponse
  property_count: 3
  slug: new-relic-application-instance-links-response
- name: ApplicationInstanceResponse
  property_count: 1
  slug: new-relic-application-instance-response
- name: ApplicationInstanceResponseType
  property_count: 9
  slug: new-relic-application-instance-response-type
- name: ApplicationLinksResponse
  property_count: 3
  slug: new-relic-application-links-response
- name: ApplicationResponse
  property_count: 1
  slug: new-relic-application-response
- name: ApplicationResponseType
  property_count: 10
  slug: new-relic-application-response-type
- name: Application
  property_count: 1
  slug: new-relic-application
- name: ApplicationBody
  property_count: 2
  slug: new-relic-applicationbody
- name: ApplicationHostLinksResponse
  property_count: 3
  slug: new-relic-applicationhostlinksresponse
- name: ApplicationHostResponse
  property_count: 1
  slug: new-relic-applicationhostresponse
- name: ApplicationHostResponseType
  property_count: 8
  slug: new-relic-applicationhostresponsetype
- name: ApplicationInstanceLinksResponse
  property_count: 3
  slug: new-relic-applicationinstancelinksresponse
- name: ApplicationInstanceResponse
  property_count: 1
  slug: new-relic-applicationinstanceresponse
- name: ApplicationInstanceResponseType
  property_count: 9
  slug: new-relic-applicationinstanceresponsetype
- name: ApplicationLinksResponse
  property_count: 3
  slug: new-relic-applicationlinksresponse
- name: ApplicationResponse
  property_count: 1
  slug: new-relic-applicationresponse
- name: ApplicationResponseType
  property_count: 10
  slug: new-relic-applicationresponsetype
- name: AppSettingsBody
  property_count: 3
  slug: new-relic-appsettingsbody
- name: AppSettingsResponse
  property_count: 4
  slug: new-relic-appsettingsresponse
- name: AppSummaryDataResponse
  property_count: 5
  slug: new-relic-appsummarydataresponse
- name: AppSummaryResponse
  property_count: 8
  slug: new-relic-appsummaryresponse
- name: BrowserApplicationBody
  property_count: 1
  slug: new-relic-browser-application-body
- name: BrowserApplicationResponse
  property_count: 1
  slug: new-relic-browser-application-response
- name: BrowserApplicationResponseType
  property_count: 4
  slug: new-relic-browser-application-response-type
- name: BrowserApplication
  property_count: 1
  slug: new-relic-browser-application
- name: BrowserApplication
  property_count: 1
  slug: new-relic-browserapplication
- name: BrowserApplicationBody
  property_count: 1
  slug: new-relic-browserapplicationbody
- name: BrowserApplicationResponse
  property_count: 1
  slug: new-relic-browserapplicationresponse
- name: BrowserApplicationResponseType
  property_count: 4
  slug: new-relic-browserapplicationresponsetype
- name: ChannelBody
  property_count: 3
  slug: new-relic-channel-body
- name: ChannelLinksResponse
  property_count: 1
  slug: new-relic-channel-links-response
- name: ChannelResponse
  property_count: 1
  slug: new-relic-channel-response
- name: ChannelResponseType
  property_count: 5
  slug: new-relic-channel-response-type
- name: Channel
  property_count: 1
  slug: new-relic-channel
- name: ChannelBody
  property_count: 3
  slug: new-relic-channelbody
- name: ChannelLinksResponse
  property_count: 1
  slug: new-relic-channellinksresponse
- name: ChannelResponse
  property_count: 1
  slug: new-relic-channelresponse
- name: ChannelResponseType
  property_count: 5
  slug: new-relic-channelresponsetype
- name: CommonBlock
  property_count: 2
  slug: new-relic-commonblock
- name: ConditionBody
  property_count: 10
  slug: new-relic-condition-body
- name: ConditionResponse
  property_count: 1
  slug: new-relic-condition-response
- name: ConditionResponseType
  property_count: 12
  slug: new-relic-condition-response-type
- name: Condition
  property_count: 1
  slug: new-relic-condition
- name: ConditionBody
  property_count: 10
  slug: new-relic-conditionbody
- name: ConditionResponse
  property_count: 1
  slug: new-relic-conditionresponse
- name: ConditionResponseType
  property_count: 12
  slug: new-relic-conditionresponsetype
- name: CrashSummaryResponse
  property_count: 4
  slug: new-relic-crash-summary-response
- name: CrashSummaryResponse
  property_count: 4
  slug: new-relic-crashsummaryresponse
- name: CustomEvent
  property_count: 2
  slug: new-relic-customevent
- name: DeploymentBody
  property_count: 4
  slug: new-relic-deployment-body
- name: DeploymentLinksResponse
  property_count: 1
  slug: new-relic-deployment-links-response
- name: DeploymentResponse
  property_count: 1
  slug: new-relic-deployment-response
- name: DeploymentResponseType
  property_count: 7
  slug: new-relic-deployment-response-type
- name: Deployment
  property_count: 1
  slug: new-relic-deployment
- name: DeploymentBody
  property_count: 4
  slug: new-relic-deploymentbody
- name: DeploymentLinksResponse
  property_count: 1
  slug: new-relic-deploymentlinksresponse
- name: DeploymentResponse
  property_count: 1
  slug: new-relic-deploymentresponse
- name: DeploymentResponseType
  property_count: 7
  slug: new-relic-deploymentresponsetype
- name: EndUserSummaryDataResponse
  property_count: 3
  slug: new-relic-end-user-summary-data-response
- name: EndUserSummaryResponse
  property_count: 4
  slug: new-relic-end-user-summary-response
- name: EndUserSummaryDataResponse
  property_count: 3
  slug: new-relic-endusersummarydataresponse
- name: EndUserSummaryResponse
  property_count: 4
  slug: new-relic-endusersummaryresponse
- name: ErrorResponse
  property_count: 3
  slug: new-relic-errorresponse
- name: CustomEvent
  property_count: 2
  slug: new-relic-event-custom-event
- name: ErrorResponse
  property_count: 3
  slug: new-relic-event-error-response
- name: EventPayload
  property_count: 0
  slug: new-relic-event-event-payload
- name: New Relic Event API Payload
  property_count: 0
  slug: new-relic-event-payload
- name: SuccessResponse
  property_count: 2
  slug: new-relic-event-success-response
- name: EventPayload
  property_count: 0
  slug: new-relic-eventpayload
- name: ExternalServiceConditionBody
  property_count: 8
  slug: new-relic-external-service-condition-body
- name: ExternalServiceConditionResponse
  property_count: 1
  slug: new-relic-external-service-condition-response
- name: ExternalServiceConditionResponseType
  property_count: 9
  slug: new-relic-external-service-condition-response-type
- name: ExternalServiceCondition
  property_count: 1
  slug: new-relic-external-service-condition
- name: ExternalServiceCondition
  property_count: 1
  slug: new-relic-externalservicecondition
- name: ExternalServiceConditionBody
  property_count: 8
  slug: new-relic-externalserviceconditionbody
- name: ExternalServiceConditionResponse
  property_count: 1
  slug: new-relic-externalserviceconditionresponse
- name: ExternalServiceConditionResponseType
  property_count: 9
  slug: new-relic-externalserviceconditionresponsetype
- name: IJKTermsType
  property_count: 5
  slug: new-relic-ijk-terms-type
- name: IJKTermsType
  property_count: 5
  slug: new-relic-ijktermstype
- name: IncidentLinksResponse
  property_count: 2
  slug: new-relic-incident-links-response
- name: IncidentResponse
  property_count: 1
  slug: new-relic-incident-response
- name: IncidentResponseType
  property_count: 5
  slug: new-relic-incident-response-type
- name: IncidentLinksResponse
  property_count: 2
  slug: new-relic-incidentlinksresponse
- name: IncidentResponse
  property_count: 1
  slug: new-relic-incidentresponse
- name: IncidentResponseType
  property_count: 5
  slug: new-relic-incidentresponsetype
- name: KeyTransactionLinksResponse
  property_count: 1
  slug: new-relic-key-transaction-links-response
- name: KeyTransactionResponse
  property_count: 1
  slug: new-relic-key-transaction-response
- name: KeyTransactionResponseType
  property_count: 9
  slug: new-relic-key-transaction-response-type
- name: KeyTransactionLinksResponse
  property_count: 1
  slug: new-relic-keytransactionlinksresponse
- name: KeyTransactionResponse
  property_count: 1
  slug: new-relic-keytransactionresponse
- name: KeyTransactionResponseType
  property_count: 9
  slug: new-relic-keytransactionresponsetype
- name: LabelBody
  property_count: 3
  slug: new-relic-label-body
- name: LabelLinksBody
  property_count: 2
  slug: new-relic-label-links-body
- name: LabelLinksResponse
  property_count: 2
  slug: new-relic-label-links-response
- name: LabelOriginsResponse
  property_count: 3
  slug: new-relic-label-origins-response
- name: LabelResponse
  property_count: 1
  slug: new-relic-label-response
- name: LabelResponseType
  property_count: 5
  slug: new-relic-label-response-type
- name: Label
  property_count: 1
  slug: new-relic-label
- name: LabelBody
  property_count: 3
  slug: new-relic-labelbody
- name: LabelLinksBody
  property_count: 2
  slug: new-relic-labellinksbody
- name: LabelLinksResponse
  property_count: 2
  slug: new-relic-labellinksresponse
- name: LabelOriginsResponse
  property_count: 3
  slug: new-relic-labeloriginsresponse
- name: LabelResponse
  property_count: 1
  slug: new-relic-labelresponse
- name: LabelResponseType
  property_count: 5
  slug: new-relic-labelresponsetype
- name: AcceptedResponse
  property_count: 1
  slug: new-relic-log-accepted-response
- name: CommonBlock
  property_count: 2
  slug: new-relic-log-common-block
- name: ErrorResponse
  property_count: 2
  slug: new-relic-log-error-response
- name: LogDataObject
  property_count: 2
  slug: new-relic-log-log-data-object
- name: LogPayload
  property_count: 0
  slug: new-relic-log-log-payload
- name: LogRecord
  property_count: 5
  slug: new-relic-log-log-record
- name: LogDataObject
  property_count: 2
  slug: new-relic-logdataobject
- name: LogPayload
  property_count: 0
  slug: new-relic-logpayload
- name: LogRecord
  property_count: 5
  slug: new-relic-logrecord
- name: AcceptedResponse
  property_count: 1
  slug: new-relic-metric-accepted-response
- name: CommonBlock
  property_count: 3
  slug: new-relic-metric-common-block
- name: MetricDataResponse
  property_count: 1
  slug: new-relic-metric-data-response
- name: MetricDataResponseType
  property_count: 5
  slug: new-relic-metric-data-response-type
- name: ErrorResponse
  property_count: 2
  slug: new-relic-metric-error-response
- name: MetricListResponse
  property_count: 1
  slug: new-relic-metric-list-response
- name: MetricDataObject
  property_count: 2
  slug: new-relic-metric-metric-data-object
- name: MetricDataPoint
  property_count: 6
  slug: new-relic-metric-metric-data-point
- name: MetricPayload
  property_count: 0
  slug: new-relic-metric-metric-payload
- name: MetricParserResponse
  property_count: 1
  slug: new-relic-metric-parser-response
- name: MetricParserResponseType
  property_count: 2
  slug: new-relic-metric-parser-response-type
- name: New Relic Metric API Payload
  property_count: 0
  slug: new-relic-metric-payload
- name: MetricResponse
  property_count: 2
  slug: new-relic-metric-response
- name: SummaryValue
  property_count: 4
  slug: new-relic-metric-summary-value
- name: MetricDataObject
  property_count: 2
  slug: new-relic-metricdataobject
- name: MetricDataPoint
  property_count: 6
  slug: new-relic-metricdatapoint
- name: MetricDataResponse
  property_count: 1
  slug: new-relic-metricdataresponse
- name: MetricDataResponseType
  property_count: 5
  slug: new-relic-metricdataresponsetype
- name: MetricListResponse
  property_count: 1
  slug: new-relic-metriclistresponse
- name: MetricParserResponse
  property_count: 1
  slug: new-relic-metricparserresponse
- name: MetricParserResponseType
  property_count: 2
  slug: new-relic-metricparserresponsetype
- name: MetricPayload
  property_count: 0
  slug: new-relic-metricpayload
- name: MetricResponse
  property_count: 2
  slug: new-relic-metricresponse
- name: MobileApplicationResponse
  property_count: 1
  slug: new-relic-mobile-application-response
- name: MobileApplicationResponseType
  property_count: 6
  slug: new-relic-mobile-application-response-type
- name: MobileSummaryDataResponse
  property_count: 8
  slug: new-relic-mobile-summary-data-response
- name: MobileApplicationResponse
  property_count: 1
  slug: new-relic-mobileapplicationresponse
- name: MobileApplicationResponseType
  property_count: 6
  slug: new-relic-mobileapplicationresponsetype
- name: MobileSummaryDataResponse
  property_count: 8
  slug: new-relic-mobilesummarydataresponse
- name: NewRelicTracePayload
  property_count: 0
  slug: new-relic-newrelictracepayload
- name: NrqlBody
  property_count: 2
  slug: new-relic-nrql-body
- name: NrqlConditionBody
  property_count: 8
  slug: new-relic-nrql-condition-body
- name: NrqlConditionResponse
  property_count: 1
  slug: new-relic-nrql-condition-response
- name: NrqlConditionResponseType
  property_count: 10
  slug: new-relic-nrql-condition-response-type
- name: NrqlCondition
  property_count: 1
  slug: new-relic-nrql-condition
- name: NrqlResponse
  property_count: 2
  slug: new-relic-nrql-response
- name: NrqlBody
  property_count: 2
  slug: new-relic-nrqlbody
- name: NrqlCondition
  property_count: 1
  slug: new-relic-nrqlcondition
- name: NrqlConditionBody
  property_count: 8
  slug: new-relic-nrqlconditionbody
- name: NrqlConditionResponse
  property_count: 1
  slug: new-relic-nrqlconditionresponse
- name: NrqlConditionResponseType
  property_count: 10
  slug: new-relic-nrqlconditionresponsetype
- name: NrqlResponse
  property_count: 2
  slug: new-relic-nrqlresponse
- name: PolicyBody
  property_count: 2
  slug: new-relic-policy-body
- name: PolicyChannelsResponse
  property_count: 1
  slug: new-relic-policy-channels-response
- name: PolicyChannelsResponseType
  property_count: 2
  slug: new-relic-policy-channels-response-type
- name: PolicyResponse
  property_count: 1
  slug: new-relic-policy-response
- name: PolicyResponseType
  property_count: 5
  slug: new-relic-policy-response-type
- name: Policy
  property_count: 1
  slug: new-relic-policy
- name: PolicyBody
  property_count: 2
  slug: new-relic-policybody
- name: PolicyChannelsResponse
  property_count: 1
  slug: new-relic-policychannelsresponse
- name: PolicyChannelsResponseType
  property_count: 2
  slug: new-relic-policychannelsresponsetype
- name: PolicyResponse
  property_count: 1
  slug: new-relic-policyresponse
- name: PolicyResponseType
  property_count: 5
  slug: new-relic-policyresponsetype
- name: RecentEventResponse
  property_count: 1
  slug: new-relic-recent-event-response
- name: RecentEventResponseType
  property_count: 10
  slug: new-relic-recent-event-response-type
- name: RecentEventResponse
  property_count: 1
  slug: new-relic-recenteventresponse
- name: RecentEventResponseType
  property_count: 10
  slug: new-relic-recenteventresponsetype
- name: Span
  property_count: 4
  slug: new-relic-span
- name: SpanBatch
  property_count: 2
  slug: new-relic-spanbatch
- name: SuccessResponse
  property_count: 2
  slug: new-relic-successresponse
- name: SummaryValue
  property_count: 4
  slug: new-relic-summaryvalue
- name: SyntheticsConditionBody
  property_count: 4
  slug: new-relic-synthetics-condition-body
- name: SyntheticsConditionResponse
  property_count: 1
  slug: new-relic-synthetics-condition-response
- name: SyntheticsConditionResponseType
  property_count: 5
  slug: new-relic-synthetics-condition-response-type
- name: SyntheticsCondition
  property_count: 1
  slug: new-relic-synthetics-condition
- name: SyntheticsCondition
  property_count: 1
  slug: new-relic-syntheticscondition
- name: SyntheticsConditionBody
  property_count: 4
  slug: new-relic-syntheticsconditionbody
- name: SyntheticsConditionResponse
  property_count: 1
  slug: new-relic-syntheticsconditionresponse
- name: SyntheticsConditionResponseType
  property_count: 5
  slug: new-relic-syntheticsconditionresponsetype
- name: TimesliceResponse
  property_count: 3
  slug: new-relic-timeslice-response
- name: TimesliceResponse
  property_count: 3
  slug: new-relic-timesliceresponse
- name: AcceptedResponse
  property_count: 1
  slug: new-relic-trace-accepted-response
- name: CommonBlock
  property_count: 1
  slug: new-relic-trace-common-block
- name: ErrorResponse
  property_count: 2
  slug: new-relic-trace-error-response
- name: NewRelicTracePayload
  property_count: 0
  slug: new-relic-trace-new-relic-trace-payload
- name: SpanBatch
  property_count: 2
  slug: new-relic-trace-span-batch
- name: Span
  property_count: 4
  slug: new-relic-trace-span
- name: ZipkinSpan
  property_count: 11
  slug: new-relic-trace-zipkin-span
- name: ZipkinTracePayload
  property_count: 0
  slug: new-relic-trace-zipkin-trace-payload
- name: UserDefinedConditionBody
  property_count: 2
  slug: new-relic-user-defined-condition-body
- name: UserDefinedConditionResponse
  property_count: 2
  slug: new-relic-user-defined-condition-response
- name: UserDefinedConditionBody
  property_count: 2
  slug: new-relic-userdefinedconditionbody
- name: UserDefinedConditionResponse
  property_count: 2
  slug: new-relic-userdefinedconditionresponse
- name: ViolationEntityResponse
  property_count: 5
  slug: new-relic-violation-entity-response
- name: ViolationLinksResponse
  property_count: 3
  slug: new-relic-violation-links-response
- name: ViolationResponse
  property_count: 1
  slug: new-relic-violation-response
- name: ViolationResponseType
  property_count: 10
  slug: new-relic-violation-response-type
- name: ViolationEntityResponse
  property_count: 5
  slug: new-relic-violationentityresponse
- name: ViolationLinksResponse
  property_count: 3
  slug: new-relic-violationlinksresponse
- name: ViolationResponse
  property_count: 1
  slug: new-relic-violationresponse
- name: ViolationResponseType
  property_count: 10
  slug: new-relic-violationresponsetype
- name: ZipkinSpan
  property_count: 11
  slug: new-relic-zipkinspan
- name: ZipkinTracePayload
  property_count: 0
  slug: new-relic-zipkintracepayload
- name: AppSettingsBody
  property_count: 3
  slug: openapi-app-settings-body
- name: AppSettingsResponse
  property_count: 4
  slug: openapi-app-settings-response
- name: AppSummaryDataResponse
  property_count: 5
  slug: openapi-app-summary-data-response
- name: AppSummaryResponse
  property_count: 8
  slug: openapi-app-summary-response
- name: ApplicationBody
  property_count: 2
  slug: openapi-application-body
- name: ApplicationHostLinksResponse
  property_count: 3
  slug: openapi-application-host-links-response
- name: ApplicationHostResponse
  property_count: 1
  slug: openapi-application-host-response
- name: ApplicationHostResponseType
  property_count: 8
  slug: openapi-application-host-response-type
- name: ApplicationInstanceLinksResponse
  property_count: 3
  slug: openapi-application-instance-links-response
- name: ApplicationInstanceResponse
  property_count: 1
  slug: openapi-application-instance-response
- name: ApplicationInstanceResponseType
  property_count: 9
  slug: openapi-application-instance-response-type
- name: ApplicationLinksResponse
  property_count: 3
  slug: openapi-application-links-response
- name: ApplicationResponse
  property_count: 1
  slug: openapi-application-response
- name: ApplicationResponseType
  property_count: 10
  slug: openapi-application-response-type
- name: Application
  property_count: 1
  slug: openapi-application
- name: BrowserApplicationBody
  property_count: 1
  slug: openapi-browser-application-body
- name: BrowserApplicationResponse
  property_count: 1
  slug: openapi-browser-application-response
- name: BrowserApplicationResponseType
  property_count: 4
  slug: openapi-browser-application-response-type
- name: BrowserApplication
  property_count: 1
  slug: openapi-browser-application
- name: ChannelBody
  property_count: 3
  slug: openapi-channel-body
- name: ChannelLinksResponse
  property_count: 1
  slug: openapi-channel-links-response
- name: ChannelResponse
  property_count: 1
  slug: openapi-channel-response
- name: ChannelResponseType
  property_count: 5
  slug: openapi-channel-response-type
- name: Channel
  property_count: 1
  slug: openapi-channel
- name: ConditionBody
  property_count: 10
  slug: openapi-condition-body
- name: ConditionResponse
  property_count: 1
  slug: openapi-condition-response
- name: ConditionResponseType
  property_count: 12
  slug: openapi-condition-response-type
- name: Condition
  property_count: 1
  slug: openapi-condition
- name: CrashSummaryResponse
  property_count: 4
  slug: openapi-crash-summary-response
- name: DeploymentBody
  property_count: 4
  slug: openapi-deployment-body
- name: DeploymentLinksResponse
  property_count: 1
  slug: openapi-deployment-links-response
- name: DeploymentResponse
  property_count: 1
  slug: openapi-deployment-response
- name: DeploymentResponseType
  property_count: 7
  slug: openapi-deployment-response-type
- name: Deployment
  property_count: 1
  slug: openapi-deployment
- name: EndUserSummaryDataResponse
  property_count: 3
  slug: openapi-end-user-summary-data-response
- name: EndUserSummaryResponse
  property_count: 4
  slug: openapi-end-user-summary-response
- name: ExternalServiceConditionBody
  property_count: 8
  slug: openapi-external-service-condition-body
- name: ExternalServiceConditionResponse
  property_count: 1
  slug: openapi-external-service-condition-response
- name: ExternalServiceConditionResponseType
  property_count: 9
  slug: openapi-external-service-condition-response-type
- name: ExternalServiceCondition
  property_count: 1
  slug: openapi-external-service-condition
- name: IJKTermsType
  property_count: 5
  slug: openapi-ijkterms-type
- name: IncidentLinksResponse
  property_count: 2
  slug: openapi-incident-links-response
- name: IncidentResponse
  property_count: 1
  slug: openapi-incident-response
- name: IncidentResponseType
  property_count: 5
  slug: openapi-incident-response-type
- name: KeyTransactionLinksResponse
  property_count: 1
  slug: openapi-key-transaction-links-response
- name: KeyTransactionResponse
  property_count: 1
  slug: openapi-key-transaction-response
- name: KeyTransactionResponseType
  property_count: 9
  slug: openapi-key-transaction-response-type
- name: LabelBody
  property_count: 3
  slug: openapi-label-body
- name: LabelLinksBody
  property_count: 2
  slug: openapi-label-links-body
- name: LabelLinksResponse
  property_count: 2
  slug: openapi-label-links-response
- name: LabelOriginsResponse
  property_count: 3
  slug: openapi-label-origins-response
- name: LabelResponse
  property_count: 1
  slug: openapi-label-response
- name: LabelResponseType
  property_count: 5
  slug: openapi-label-response-type
- name: Label
  property_count: 1
  slug: openapi-label
- name: MetricDataResponse
  property_count: 1
  slug: openapi-metric-data-response
- name: MetricDataResponseType
  property_count: 5
  slug: openapi-metric-data-response-type
- name: MetricListResponse
  property_count: 1
  slug: openapi-metric-list-response
- name: MetricParserResponse
  property_count: 1
  slug: openapi-metric-parser-response
- name: MetricParserResponseType
  property_count: 2
  slug: openapi-metric-parser-response-type
- name: MetricResponse
  property_count: 2
  slug: openapi-metric-response
- name: MobileApplicationResponse
  property_count: 1
  slug: openapi-mobile-application-response
- name: MobileApplicationResponseType
  property_count: 6
  slug: openapi-mobile-application-response-type
- name: MobileSummaryDataResponse
  property_count: 8
  slug: openapi-mobile-summary-data-response
- name: NrqlBody
  property_count: 2
  slug: openapi-nrql-body
- name: NrqlConditionBody
  property_count: 8
  slug: openapi-nrql-condition-body
- name: NrqlConditionResponse
  property_count: 1
  slug: openapi-nrql-condition-response
- name: NrqlConditionResponseType
  property_count: 10
  slug: openapi-nrql-condition-response-type
- name: NrqlCondition
  property_count: 1
  slug: openapi-nrql-condition
- name: NrqlResponse
  property_count: 2
  slug: openapi-nrql-response
- name: PolicyBody
  property_count: 2
  slug: openapi-policy-body
- name: PolicyChannelsResponse
  property_count: 1
  slug: openapi-policy-channels-response
- name: PolicyChannelsResponseType
  property_count: 2
  slug: openapi-policy-channels-response-type
- name: PolicyResponse
  property_count: 1
  slug: openapi-policy-response
- name: PolicyResponseType
  property_count: 5
  slug: openapi-policy-response-type
- name: Policy
  property_count: 1
  slug: openapi-policy
- name: RecentEventResponse
  property_count: 1
  slug: openapi-recent-event-response
- name: RecentEventResponseType
  property_count: 10
  slug: openapi-recent-event-response-type
- name: SyntheticsConditionBody
  property_count: 4
  slug: openapi-synthetics-condition-body
- name: SyntheticsConditionResponse
  property_count: 1
  slug: openapi-synthetics-condition-response
- name: SyntheticsConditionResponseType
  property_count: 5
  slug: openapi-synthetics-condition-response-type
- name: SyntheticsCondition
  property_count: 1
  slug: openapi-synthetics-condition
- name: TimesliceResponse
  property_count: 3
  slug: openapi-timeslice-response
- name: UserDefinedConditionBody
  property_count: 2
  slug: openapi-user-defined-condition-body
- name: UserDefinedConditionResponse
  property_count: 2
  slug: openapi-user-defined-condition-response
- name: ViolationEntityResponse
  property_count: 5
  slug: openapi-violation-entity-response
- name: ViolationLinksResponse
  property_count: 3
  slug: openapi-violation-links-response
- name: ViolationResponse
  property_count: 1
  slug: openapi-violation-response
- name: ViolationResponseType
  property_count: 10
  slug: openapi-violation-response-type
- name: AcceptedResponse
  property_count: 1
  slug: trace-api-accepted-response
- name: CommonBlock
  property_count: 1
  slug: trace-api-common-block
- name: NewRelicTracePayload
  property_count: 0
  slug: trace-api-new-relic-trace-payload
- name: SpanBatch
  property_count: 2
  slug: trace-api-span-batch
- name: Span
  property_count: 4
  slug: trace-api-span
- name: ZipkinSpan
  property_count: 11
  slug: trace-api-zipkin-span
- name: ZipkinTracePayload
  property_count: 0
  slug: trace-api-zipkin-trace-payload
json_structures:
- name: Event Api Custom Event Structure
  property_count: 2
  slug: event-api-custom-event-structure
- name: Event Api Event Payload Structure
  property_count: 0
  slug: event-api-event-payload-structure
- name: Event Api Success Response Structure
  property_count: 2
  slug: event-api-success-response-structure
- name: Log Api Accepted Response Structure
  property_count: 1
  slug: log-api-accepted-response-structure
- name: Log Api Common Block Structure
  property_count: 2
  slug: log-api-common-block-structure
- name: Log Api Log Data Object Structure
  property_count: 2
  slug: log-api-log-data-object-structure
- name: Log Api Log Payload Structure
  property_count: 0
  slug: log-api-log-payload-structure
- name: Log Api Log Record Structure
  property_count: 5
  slug: log-api-log-record-structure
- name: Metric Api Accepted Response Structure
  property_count: 1
  slug: metric-api-accepted-response-structure
- name: Metric Api Common Block Structure
  property_count: 3
  slug: metric-api-common-block-structure
- name: Metric Api Metric Data Object Structure
  property_count: 2
  slug: metric-api-metric-data-object-structure
- name: Metric Api Metric Data Point Structure
  property_count: 6
  slug: metric-api-metric-data-point-structure
- name: Metric Api Metric Payload Structure
  property_count: 0
  slug: metric-api-metric-payload-structure
- name: Metric Api Summary Value Structure
  property_count: 4
  slug: metric-api-summary-value-structure
- name: New Relic App Settings Body Structure
  property_count: 3
  slug: new-relic-app-settings-body-structure
- name: New Relic App Settings Response Structure
  property_count: 4
  slug: new-relic-app-settings-response-structure
- name: New Relic App Summary Data Response Structure
  property_count: 5
  slug: new-relic-app-summary-data-response-structure
- name: New Relic App Summary Response Structure
  property_count: 8
  slug: new-relic-app-summary-response-structure
- name: New Relic Application Body Structure
  property_count: 2
  slug: new-relic-application-body-structure
- name: New Relic Application Host Links Response Structure
  property_count: 3
  slug: new-relic-application-host-links-response-structure
- name: New Relic Application Host Response Structure
  property_count: 1
  slug: new-relic-application-host-response-structure
- name: New Relic Application Host Response Type Structure
  property_count: 8
  slug: new-relic-application-host-response-type-structure
- name: New Relic Application Instance Links Response Structure
  property_count: 3
  slug: new-relic-application-instance-links-response-structure
- name: New Relic Application Instance Response Structure
  property_count: 1
  slug: new-relic-application-instance-response-structure
- name: New Relic Application Instance Response Type Structure
  property_count: 9
  slug: new-relic-application-instance-response-type-structure
- name: New Relic Application Links Response Structure
  property_count: 3
  slug: new-relic-application-links-response-structure
- name: New Relic Application Response Structure
  property_count: 1
  slug: new-relic-application-response-structure
- name: New Relic Application Response Type Structure
  property_count: 10
  slug: new-relic-application-response-type-structure
- name: New Relic Application Structure
  property_count: 1
  slug: new-relic-application-structure
- name: New Relic Browser Application Body Structure
  property_count: 1
  slug: new-relic-browser-application-body-structure
- name: New Relic Browser Application Response Structure
  property_count: 1
  slug: new-relic-browser-application-response-structure
- name: New Relic Browser Application Response Type Structure
  property_count: 4
  slug: new-relic-browser-application-response-type-structure
- name: New Relic Browser Application Structure
  property_count: 1
  slug: new-relic-browser-application-structure
- name: New Relic Channel Body Structure
  property_count: 3
  slug: new-relic-channel-body-structure
- name: New Relic Channel Links Response Structure
  property_count: 1
  slug: new-relic-channel-links-response-structure
- name: New Relic Channel Response Structure
  property_count: 1
  slug: new-relic-channel-response-structure
- name: New Relic Channel Response Type Structure
  property_count: 5
  slug: new-relic-channel-response-type-structure
- name: New Relic Channel Structure
  property_count: 1
  slug: new-relic-channel-structure
- name: New Relic Condition Body Structure
  property_count: 10
  slug: new-relic-condition-body-structure
- name: New Relic Condition Response Structure
  property_count: 1
  slug: new-relic-condition-response-structure
- name: New Relic Condition Response Type Structure
  property_count: 12
  slug: new-relic-condition-response-type-structure
- name: New Relic Condition Structure
  property_count: 1
  slug: new-relic-condition-structure
- name: New Relic Crash Summary Response Structure
  property_count: 4
  slug: new-relic-crash-summary-response-structure
- name: New Relic Deployment Body Structure
  property_count: 4
  slug: new-relic-deployment-body-structure
- name: New Relic Deployment Links Response Structure
  property_count: 1
  slug: new-relic-deployment-links-response-structure
- name: New Relic Deployment Response Structure
  property_count: 1
  slug: new-relic-deployment-response-structure
- name: New Relic Deployment Response Type Structure
  property_count: 7
  slug: new-relic-deployment-response-type-structure
- name: New Relic Deployment Structure
  property_count: 1
  slug: new-relic-deployment-structure
- name: New Relic End User Summary Data Response Structure
  property_count: 3
  slug: new-relic-end-user-summary-data-response-structure
- name: New Relic End User Summary Response Structure
  property_count: 4
  slug: new-relic-end-user-summary-response-structure
- name: New Relic Event Custom Event Structure
  property_count: 2
  slug: new-relic-event-custom-event-structure
- name: New Relic Event Error Response Structure
  property_count: 3
  slug: new-relic-event-error-response-structure
- name: New Relic Event Event Payload Structure
  property_count: 0
  slug: new-relic-event-event-payload-structure
- name: New Relic Event Payload Structure
  property_count: 0
  slug: new-relic-event-payload-structure
- name: New Relic Event Success Response Structure
  property_count: 2
  slug: new-relic-event-success-response-structure
- name: New Relic External Service Condition Body Structure
  property_count: 8
  slug: new-relic-external-service-condition-body-structure
- name: New Relic External Service Condition Response Structure
  property_count: 1
  slug: new-relic-external-service-condition-response-structure
- name: New Relic External Service Condition Response Type Structure
  property_count: 9
  slug: new-relic-external-service-condition-response-type-structure
- name: New Relic External Service Condition Structure
  property_count: 1
  slug: new-relic-external-service-condition-structure
- name: New Relic Ijk Terms Type Structure
  property_count: 5
  slug: new-relic-ijk-terms-type-structure
- name: New Relic Incident Links Response Structure
  property_count: 2
  slug: new-relic-incident-links-response-structure
- name: New Relic Incident Response Structure
  property_count: 1
  slug: new-relic-incident-response-structure
- name: New Relic Incident Response Type Structure
  property_count: 5
  slug: new-relic-incident-response-type-structure
- name: New Relic Key Transaction Links Response Structure
  property_count: 1
  slug: new-relic-key-transaction-links-response-structure
- name: New Relic Key Transaction Response Structure
  property_count: 1
  slug: new-relic-key-transaction-response-structure
- name: New Relic Key Transaction Response Type Structure
  property_count: 9
  slug: new-relic-key-transaction-response-type-structure
- name: New Relic Label Body Structure
  property_count: 3
  slug: new-relic-label-body-structure
- name: New Relic Label Links Body Structure
  property_count: 2
  slug: new-relic-label-links-body-structure
- name: New Relic Label Links Response Structure
  property_count: 2
  slug: new-relic-label-links-response-structure
- name: New Relic Label Origins Response Structure
  property_count: 3
  slug: new-relic-label-origins-response-structure
- name: New Relic Label Response Structure
  property_count: 1
  slug: new-relic-label-response-structure
- name: New Relic Label Response Type Structure
  property_count: 5
  slug: new-relic-label-response-type-structure
- name: New Relic Label Structure
  property_count: 1
  slug: new-relic-label-structure
- name: New Relic Log Accepted Response Structure
  property_count: 1
  slug: new-relic-log-accepted-response-structure
- name: New Relic Log Common Block Structure
  property_count: 2
  slug: new-relic-log-common-block-structure
- name: New Relic Log Error Response Structure
  property_count: 2
  slug: new-relic-log-error-response-structure
- name: New Relic Log Log Data Object Structure
  property_count: 2
  slug: new-relic-log-log-data-object-structure
- name: New Relic Log Log Payload Structure
  property_count: 0
  slug: new-relic-log-log-payload-structure
- name: New Relic Log Log Record Structure
  property_count: 5
  slug: new-relic-log-log-record-structure
- name: New Relic Metric Accepted Response Structure
  property_count: 1
  slug: new-relic-metric-accepted-response-structure
- name: New Relic Metric Common Block Structure
  property_count: 3
  slug: new-relic-metric-common-block-structure
- name: New Relic Metric Data Response Structure
  property_count: 1
  slug: new-relic-metric-data-response-structure
- name: New Relic Metric Data Response Type Structure
  property_count: 5
  slug: new-relic-metric-data-response-type-structure
- name: New Relic Metric Error Response Structure
  property_count: 2
  slug: new-relic-metric-error-response-structure
- name: New Relic Metric List Response Structure
  property_count: 1
  slug: new-relic-metric-list-response-structure
- name: New Relic Metric Metric Data Object Structure
  property_count: 2
  slug: new-relic-metric-metric-data-object-structure
- name: New Relic Metric Metric Data Point Structure
  property_count: 6
  slug: new-relic-metric-metric-data-point-structure
- name: New Relic Metric Metric Payload Structure
  property_count: 0
  slug: new-relic-metric-metric-payload-structure
- name: New Relic Metric Parser Response Structure
  property_count: 1
  slug: new-relic-metric-parser-response-structure
- name: New Relic Metric Parser Response Type Structure
  property_count: 2
  slug: new-relic-metric-parser-response-type-structure
- name: New Relic Metric Payload Structure
  property_count: 0
  slug: new-relic-metric-payload-structure
- name: New Relic Metric Response Structure
  property_count: 2
  slug: new-relic-metric-response-structure
- name: New Relic Metric Summary Value Structure
  property_count: 4
  slug: new-relic-metric-summary-value-structure
- name: New Relic Mobile Application Response Structure
  property_count: 1
  slug: new-relic-mobile-application-response-structure
- name: New Relic Mobile Application Response Type Structure
  property_count: 6
  slug: new-relic-mobile-application-response-type-structure
- name: New Relic Mobile Summary Data Response Structure
  property_count: 8
  slug: new-relic-mobile-summary-data-response-structure
- name: New Relic Nrql Body Structure
  property_count: 2
  slug: new-relic-nrql-body-structure
- name: New Relic Nrql Condition Body Structure
  property_count: 8
  slug: new-relic-nrql-condition-body-structure
- name: New Relic Nrql Condition Response Structure
  property_count: 1
  slug: new-relic-nrql-condition-response-structure
- name: New Relic Nrql Condition Response Type Structure
  property_count: 10
  slug: new-relic-nrql-condition-response-type-structure
- name: New Relic Nrql Condition Structure
  property_count: 1
  slug: new-relic-nrql-condition-structure
- name: New Relic Nrql Response Structure
  property_count: 2
  slug: new-relic-nrql-response-structure
- name: New Relic Policy Body Structure
  property_count: 2
  slug: new-relic-policy-body-structure
- name: New Relic Policy Channels Response Structure
  property_count: 1
  slug: new-relic-policy-channels-response-structure
- name: New Relic Policy Channels Response Type Structure
  property_count: 2
  slug: new-relic-policy-channels-response-type-structure
- name: New Relic Policy Response Structure
  property_count: 1
  slug: new-relic-policy-response-structure
- name: New Relic Policy Response Type Structure
  property_count: 5
  slug: new-relic-policy-response-type-structure
- name: New Relic Policy Structure
  property_count: 1
  slug: new-relic-policy-structure
- name: New Relic Recent Event Response Structure
  property_count: 1
  slug: new-relic-recent-event-response-structure
- name: New Relic Recent Event Response Type Structure
  property_count: 10
  slug: new-relic-recent-event-response-type-structure
- name: New Relic Structure
  property_count: 0
  slug: new-relic-structure
- name: New Relic Synthetics Condition Body Structure
  property_count: 4
  slug: new-relic-synthetics-condition-body-structure
- name: New Relic Synthetics Condition Response Structure
  property_count: 1
  slug: new-relic-synthetics-condition-response-structure
- name: New Relic Synthetics Condition Response Type Structure
  property_count: 5
  slug: new-relic-synthetics-condition-response-type-structure
- name: New Relic Synthetics Condition Structure
  property_count: 1
  slug: new-relic-synthetics-condition-structure
- name: New Relic Timeslice Response Structure
  property_count: 3
  slug: new-relic-timeslice-response-structure
- name: New Relic Trace Accepted Response Structure
  property_count: 1
  slug: new-relic-trace-accepted-response-structure
- name: New Relic Trace Common Block Structure
  property_count: 1
  slug: new-relic-trace-common-block-structure
- name: New Relic Trace Error Response Structure
  property_count: 2
  slug: new-relic-trace-error-response-structure
- name: New Relic Trace New Relic Trace Payload Structure
  property_count: 0
  slug: new-relic-trace-new-relic-trace-payload-structure
- name: New Relic Trace Span Batch Structure
  property_count: 2
  slug: new-relic-trace-span-batch-structure
- name: New Relic Trace Span Structure
  property_count: 4
  slug: new-relic-trace-span-structure
- name: New Relic Trace Zipkin Span Structure
  property_count: 11
  slug: new-relic-trace-zipkin-span-structure
- name: New Relic Trace Zipkin Trace Payload Structure
  property_count: 0
  slug: new-relic-trace-zipkin-trace-payload-structure
- name: New Relic User Defined Condition Body Structure
  property_count: 2
  slug: new-relic-user-defined-condition-body-structure
- name: New Relic User Defined Condition Response Structure
  property_count: 2
  slug: new-relic-user-defined-condition-response-structure
- name: New Relic Violation Entity Response Structure
  property_count: 5
  slug: new-relic-violation-entity-response-structure
- name: New Relic Violation Links Response Structure
  property_count: 3
  slug: new-relic-violation-links-response-structure
- name: New Relic Violation Response Structure
  property_count: 1
  slug: new-relic-violation-response-structure
- name: New Relic Violation Response Type Structure
  property_count: 10
  slug: new-relic-violation-response-type-structure
- name: Openapi App Settings Body Structure
  property_count: 3
  slug: openapi-app-settings-body-structure
- name: Openapi App Settings Response Structure
  property_count: 4
  slug: openapi-app-settings-response-structure
- name: Openapi App Summary Data Response Structure
  property_count: 5
  slug: openapi-app-summary-data-response-structure
- name: Openapi App Summary Response Structure
  property_count: 8
  slug: openapi-app-summary-response-structure
- name: Openapi Application Body Structure
  property_count: 2
  slug: openapi-application-body-structure
- name: Openapi Application Host Links Response Structure
  property_count: 3
  slug: openapi-application-host-links-response-structure
- name: Openapi Application Host Response Structure
  property_count: 1
  slug: openapi-application-host-response-structure
- name: Openapi Application Host Response Type Structure
  property_count: 8
  slug: openapi-application-host-response-type-structure
- name: Openapi Application Instance Links Response Structure
  property_count: 3
  slug: openapi-application-instance-links-response-structure
- name: Openapi Application Instance Response Structure
  property_count: 1
  slug: openapi-application-instance-response-structure
- name: Openapi Application Instance Response Type Structure
  property_count: 9
  slug: openapi-application-instance-response-type-structure
- name: Openapi Application Links Response Structure
  property_count: 3
  slug: openapi-application-links-response-structure
- name: Openapi Application Response Structure
  property_count: 1
  slug: openapi-application-response-structure
- name: Openapi Application Response Type Structure
  property_count: 10
  slug: openapi-application-response-type-structure
- name: Openapi Application Structure
  property_count: 1
  slug: openapi-application-structure
- name: Openapi Browser Application Body Structure
  property_count: 1
  slug: openapi-browser-application-body-structure
- name: Openapi Browser Application Response Structure
  property_count: 1
  slug: openapi-browser-application-response-structure
- name: Openapi Browser Application Response Type Structure
  property_count: 4
  slug: openapi-browser-application-response-type-structure
- name: Openapi Browser Application Structure
  property_count: 1
  slug: openapi-browser-application-structure
- name: Openapi Channel Body Structure
  property_count: 3
  slug: openapi-channel-body-structure
- name: Openapi Channel Links Response Structure
  property_count: 1
  slug: openapi-channel-links-response-structure
- name: Openapi Channel Response Structure
  property_count: 1
  slug: openapi-channel-response-structure
- name: Openapi Channel Response Type Structure
  property_count: 5
  slug: openapi-channel-response-type-structure
- name: Openapi Channel Structure
  property_count: 1
  slug: openapi-channel-structure
- name: Openapi Condition Body Structure
  property_count: 10
  slug: openapi-condition-body-structure
- name: Openapi Condition Response Structure
  property_count: 1
  slug: openapi-condition-response-structure
- name: Openapi Condition Response Type Structure
  property_count: 12
  slug: openapi-condition-response-type-structure
- name: Openapi Condition Structure
  property_count: 1
  slug: openapi-condition-structure
- name: Openapi Crash Summary Response Structure
  property_count: 4
  slug: openapi-crash-summary-response-structure
- name: Openapi Deployment Body Structure
  property_count: 4
  slug: openapi-deployment-body-structure
- name: Openapi Deployment Links Response Structure
  property_count: 1
  slug: openapi-deployment-links-response-structure
- name: Openapi Deployment Response Structure
  property_count: 1
  slug: openapi-deployment-response-structure
- name: Openapi Deployment Response Type Structure
  property_count: 7
  slug: openapi-deployment-response-type-structure
- name: Openapi Deployment Structure
  property_count: 1
  slug: openapi-deployment-structure
- name: Openapi End User Summary Data Response Structure
  property_count: 3
  slug: openapi-end-user-summary-data-response-structure
- name: Openapi End User Summary Response Structure
  property_count: 4
  slug: openapi-end-user-summary-response-structure
- name: Openapi External Service Condition Body Structure
  property_count: 8
  slug: openapi-external-service-condition-body-structure
- name: Openapi External Service Condition Response Structure
  property_count: 1
  slug: openapi-external-service-condition-response-structure
- name: Openapi External Service Condition Response Type Structure
  property_count: 9
  slug: openapi-external-service-condition-response-type-structure
- name: Openapi External Service Condition Structure
  property_count: 1
  slug: openapi-external-service-condition-structure
- name: Openapi Ijkterms Type Structure
  property_count: 5
  slug: openapi-ijkterms-type-structure
- name: Openapi Incident Links Response Structure
  property_count: 2
  slug: openapi-incident-links-response-structure
- name: Openapi Incident Response Structure
  property_count: 1
  slug: openapi-incident-response-structure
- name: Openapi Incident Response Type Structure
  property_count: 5
  slug: openapi-incident-response-type-structure
- name: Openapi Key Transaction Links Response Structure
  property_count: 1
  slug: openapi-key-transaction-links-response-structure
- name: Openapi Key Transaction Response Structure
  property_count: 1
  slug: openapi-key-transaction-response-structure
- name: Openapi Key Transaction Response Type Structure
  property_count: 9
  slug: openapi-key-transaction-response-type-structure
- name: Openapi Label Body Structure
  property_count: 3
  slug: openapi-label-body-structure
- name: Openapi Label Links Body Structure
  property_count: 2
  slug: openapi-label-links-body-structure
- name: Openapi Label Links Response Structure
  property_count: 2
  slug: openapi-label-links-response-structure
- name: Openapi Label Origins Response Structure
  property_count: 3
  slug: openapi-label-origins-response-structure
- name: Openapi Label Response Structure
  property_count: 1
  slug: openapi-label-response-structure
- name: Openapi Label Response Type Structure
  property_count: 5
  slug: openapi-label-response-type-structure
- name: Openapi Label Structure
  property_count: 1
  slug: openapi-label-structure
- name: Openapi Metric Data Response Structure
  property_count: 1
  slug: openapi-metric-data-response-structure
- name: Openapi Metric Data Response Type Structure
  property_count: 5
  slug: openapi-metric-data-response-type-structure
- name: Openapi Metric List Response Structure
  property_count: 1
  slug: openapi-metric-list-response-structure
- name: Openapi Metric Parser Response Structure
  property_count: 1
  slug: openapi-metric-parser-response-structure
- name: Openapi Metric Parser Response Type Structure
  property_count: 2
  slug: openapi-metric-parser-response-type-structure
- name: Openapi Metric Response Structure
  property_count: 2
  slug: openapi-metric-response-structure
- name: Openapi Mobile Application Response Structure
  property_count: 1
  slug: openapi-mobile-application-response-structure
- name: Openapi Mobile Application Response Type Structure
  property_count: 6
  slug: openapi-mobile-application-response-type-structure
- name: Openapi Mobile Summary Data Response Structure
  property_count: 8
  slug: openapi-mobile-summary-data-response-structure
- name: Openapi Nrql Body Structure
  property_count: 2
  slug: openapi-nrql-body-structure
- name: Openapi Nrql Condition Body Structure
  property_count: 8
  slug: openapi-nrql-condition-body-structure
- name: Openapi Nrql Condition Response Structure
  property_count: 1
  slug: openapi-nrql-condition-response-structure
- name: Openapi Nrql Condition Response Type Structure
  property_count: 10
  slug: openapi-nrql-condition-response-type-structure
- name: Openapi Nrql Condition Structure
  property_count: 1
  slug: openapi-nrql-condition-structure
- name: Openapi Nrql Response Structure
  property_count: 2
  slug: openapi-nrql-response-structure
- name: Openapi Policy Body Structure
  property_count: 2
  slug: openapi-policy-body-structure
- name: Openapi Policy Channels Response Structure
  property_count: 1
  slug: openapi-policy-channels-response-structure
- name: Openapi Policy Channels Response Type Structure
  property_count: 2
  slug: openapi-policy-channels-response-type-structure
- name: Openapi Policy Response Structure
  property_count: 1
  slug: openapi-policy-response-structure
- name: Openapi Policy Response Type Structure
  property_count: 5
  slug: openapi-policy-response-type-structure
- name: Openapi Policy Structure
  property_count: 1
  slug: openapi-policy-structure
- name: Openapi Recent Event Response Structure
  property_count: 1
  slug: openapi-recent-event-response-structure
- name: Openapi Recent Event Response Type Structure
  property_count: 10
  slug: openapi-recent-event-response-type-structure
- name: Openapi Synthetics Condition Body Structure
  property_count: 4
  slug: openapi-synthetics-condition-body-structure
- name: Openapi Synthetics Condition Response Structure
  property_count: 1
  slug: openapi-synthetics-condition-response-structure
- name: Openapi Synthetics Condition Response Type Structure
  property_count: 5
  slug: openapi-synthetics-condition-response-type-structure
- name: Openapi Synthetics Condition Structure
  property_count: 1
  slug: openapi-synthetics-condition-structure
- name: Openapi Timeslice Response Structure
  property_count: 3
  slug: openapi-timeslice-response-structure
- name: Openapi User Defined Condition Body Structure
  property_count: 2
  slug: openapi-user-defined-condition-body-structure
- name: Openapi User Defined Condition Response Structure
  property_count: 2
  slug: openapi-user-defined-condition-response-structure
- name: Openapi Violation Entity Response Structure
  property_count: 5
  slug: openapi-violation-entity-response-structure
- name: Openapi Violation Links Response Structure
  property_count: 3
  slug: openapi-violation-links-response-structure
- name: Openapi Violation Response Structure
  property_count: 1
  slug: openapi-violation-response-structure
- name: Openapi Violation Response Type Structure
  property_count: 10
  slug: openapi-violation-response-type-structure
- name: Trace Api Accepted Response Structure
  property_count: 1
  slug: trace-api-accepted-response-structure
- name: Trace Api Common Block Structure
  property_count: 1
  slug: trace-api-common-block-structure
- name: Trace Api New Relic Trace Payload Structure
  property_count: 0
  slug: trace-api-new-relic-trace-payload-structure
- name: Trace Api Span Batch Structure
  property_count: 2
  slug: trace-api-span-batch-structure
- name: Trace Api Span Structure
  property_count: 4
  slug: trace-api-span-structure
- name: Trace Api Zipkin Span Structure
  property_count: 11
  slug: trace-api-zipkin-span-structure
- name: Trace Api Zipkin Trace Payload Structure
  property_count: 0
  slug: trace-api-zipkin-trace-payload-structure
jsonld:
- class_count: 0
  name: New Relic Context
  property_count: 88
  slug: new-relic-context
- class_count: 2
  name: New Relic Event Api Context
  property_count: 4
  slug: new-relic-event-api-context
- class_count: 0
  name: New Relic Event Context
  property_count: 3
  slug: new-relic-event-context
- class_count: 4
  name: New Relic Log Api Context
  property_count: 8
  slug: new-relic-log-api-context
- class_count: 0
  name: New Relic Log Context
  property_count: 5
  slug: new-relic-log-context
- class_count: 6
  name: New Relic Metric Api Context
  property_count: 12
  slug: new-relic-metric-api-context
- class_count: 0
  name: New Relic Metric Context
  property_count: 6
  slug: new-relic-metric-context
- class_count: 90
  name: New Relic Openapi Context
  property_count: 122
  slug: new-relic-openapi-context
- class_count: 6
  name: New Relic Trace Api Context
  property_count: 15
  slug: new-relic-trace-api-context
- class_count: 0
  name: New Relic Trace Context
  property_count: 6
  slug: new-relic-trace-context
layout: provider
modified: '2026-05-19'
name: New Relic
nav: Providers
network: true
overview: 'New Relic publishes 30 APIs on the [APIs.io](https://apis.io/) network, including Alerts API, Applications API, and 28 more. Tagged areas include Analysis, Analytics, APM, DevOps, and Infrastructure.


  The New Relic catalog on APIs.io includes 1 event-driven AsyncAPI specification, 10 JSON-LD contexts, and 3 Spectral governance rulesets.


  New Relic''s developer surface includes authentication, developer portal, pricing, documentation, engineering blog, signup flow, developer console, and 68 more developer resources.'
plans:
- name: New Relic Plans Pricing
  plan_count: 4
  slug: new-relic-plans-pricing
random_paper: 0
rate_limits:
- limit_count: 4
  name: New Relic Rate Limits
  slug: new-relic-rate-limits
rules:
- name: New Relic API Rules
  rule_count: 8
  severity_counts:
    error: 1
    hint: 0
    info: 1
    warn: 6
  slug: new-relic-asyncapi-spectral-rules
- name: New Relic API Rules
  rule_count: 6
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 5
  slug: new-relic-jsonschema-spectral-rules
- name: New Relic API Rules
  rule_count: 28
  severity_counts:
    error: 19
    hint: 0
    info: 1
    warn: 8
  slug: new-relic-spectral-rules
score:
  band: exemplar
  composite: 79.3
  delta: -3.8
  facets:
    commercial_clarity: 92.1
    contract_quality: 88.2
    developer_ergonomics: 78.3
    discoverability: 59.3
    governance: 58.3
    operational_transparency: 78.9
  previous_composite: 83.1
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 29
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/new-relic/refs/heads/main/screenshots/new-relic-2026-06-20T190230.png
security:
- kind: authentication
  name: New Relic Authentication
  slug: new-relic-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: New Relic Domain Security
  slug: new-relic-domain-security
  summary_line: TLSv1.2 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: New Relic Vulnerability Disclosure
  slug: new-relic-vulnerability-disclosure
  summary_line: Hackerone · security.txt · contact published
slug: new-relic
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
use_cases:
- description: Gain unified visibility across applications, infrastructure, and digital experiences to quickly identify and resolve issues.
  name: Full-Stack Observability
- description: Monitor and validate cloud migration progress with baseline comparisons and performance tracking across hybrid environments.
  name: Cloud Migration Monitoring
- description: Integrate observability into development workflows with deployment markers, error tracking, and automated testing.
  name: DevOps and CI/CD Integration
- description: Define and track SLOs, manage error budgets, and implement reliability practices with data-driven insights.
  name: Site Reliability Engineering
- description: Detect, diagnose, and resolve incidents faster with correlated telemetry, anomaly detection, and automated workflows.
  name: Incident Response and Management
- description: Measure and optimize end-user experience across web, mobile, and synthetic channels.
  name: Digital Experience Monitoring
- description: Analyze resource utilization trends and forecast capacity needs to optimize infrastructure spending.
  name: Capacity Planning
- description: Maintain audit trails, security compliance, and data governance across observability data.
  name: Compliance and Audit
website: https://newrelic.com/
---
