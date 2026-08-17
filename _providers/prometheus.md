---
access_model:
  confidence: high
  label: Free · Open access
  onboarding: open
  pricing: free
  public: true
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
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: verified
    event_surface_described: derived
    idempotency: false
    mcp_server: derived
    openapi_examples: partial
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 45.0
  scored_at: '2026-08-17'
agentic_access:
- acting_count: 17
  human_in_the_loop: 1
  name: Prometheus Agentic Access
  operation_count: 47
  slug: prometheus-agentic-access
  summary_line: 47 operations · 17 acting · 1 human-in-the-loop
api_count: 14
apis:
- description: The Prometheus Remote Write API defines a standard protocol for sending time series data from Prometheus or compatible agents to remote storage backends via HTTP POST with Snappy-compressed protobuf p
  name: Prometheus Remote Write API
  slug: prometheus-remote-write-api
- description: Prometheus provides official client libraries for Go, Java/Scala, Python, Ruby, and Rust that enable application instrumentation. Libraries implement the Prometheus metric types (Counter, Gauge, Histo
  name: Prometheus Client Libraries
  slug: prometheus-client-libraries
- description: Administrative endpoints for TSDB management including snapshots and tombstone cleanup. Requires --web.enable-admin-api flag.
  name: Prometheus Admin API
  slug: prometheus-admin-api
- description: Endpoints for listing and creating alerts in the Alertmanager.
  name: Prometheus Alerts API
  slug: prometheus-alerts-api
- description: Endpoints for managing the Prometheus server lifecycle including configuration reloads and graceful shutdown. Requires --web.enable-lifecycle flag.
  name: Prometheus Lifecycle API
  slug: prometheus-lifecycle-api
- description: Endpoints for querying label names, label values, series metadata, and metric metadata without executing PromQL expressions.
  name: Prometheus Metadata API
  slug: prometheus-metadata-api
- description: Endpoints for pushing, replacing, and deleting metric groups. Metrics are grouped by job and optional additional labels.
  name: Prometheus Metrics API
  slug: prometheus-metrics-api
- description: PromQL instant and range query endpoints for evaluating expressions against the time series database.
  name: Prometheus Query API
  slug: prometheus-query-api
- description: Endpoints for listing configured alert receivers.
  name: Prometheus Receivers API
  slug: prometheus-receivers-api
- description: Endpoints for retrieving loaded recording rules and alerting rules.
  name: Prometheus Rules API
  slug: prometheus-rules-api
- description: Endpoints for creating, listing, updating, and expiring silences that mute matching alerts.
  name: Prometheus Silences API
  slug: prometheus-silences-api
- description: Endpoints for retrieving Alertmanager configuration, cluster status, and version information.
  name: Prometheus Status API
  slug: prometheus-status-api
- description: Endpoints for discovering scrape targets and their current health status.
  name: Prometheus Targets API
  slug: prometheus-targets-api
- description: Endpoints for querying TSDB statistics and deleting time series data.
  name: Prometheus TSDB API
  slug: prometheus-tsdb-api
arazzos:
- description: Follow one alert from its rule, through Prometheus, into Alertmanager, to find where it stopped.
  name: Prometheus Triage an Alert That Never Notified
  slug: prometheus-alert-notification-triage-workflow
- description: Preview what a selector matches, delete it, clean the tombstones, and verify.
  name: Prometheus Delete Series and Reclaim the Space
  slug: prometheus-delete-series-reclaim-space-workflow
- description: Walk from "what metrics exist?" to an evaluated PromQL result.
  name: Prometheus Discover and Query a Metric
  slug: prometheus-discover-and-query-metric-workflow
- description: Find an active silence, inspect what it mutes, expire it, and confirm it is gone.
  name: Prometheus Expire a Silence Early
  slug: prometheus-expire-silence-workflow
- description: Evaluate an expression too long for a URL, first instant then across a range.
  name: Prometheus Run a Large PromQL Expression via POST
  slug: prometheus-large-promql-query-post-workflow
- description: Find a stale metric group left by a decommissioned job and delete it.
  name: Prometheus Purge a Retired Job's Pushed Metrics
  slug: prometheus-purge-retired-job-metrics-workflow
- description: Publish a short-lived job's results so Prometheus can scrape them after the job exits.
  name: Prometheus Push Batch Job Metrics to the Pushgateway
  slug: prometheus-push-batch-job-metrics-workflow
- description: Push, update, verify, and tear down metrics scoped by instance-level grouping labels.
  name: Prometheus Manage a Grouped Metric Group End to End
  slug: prometheus-push-grouped-metrics-lifecycle-workflow
- description: Validate an expression, graph it over a time range, then link the spikes to traces.
  name: Prometheus Chart a Range Query and Pull Its Exemplars
  slug: prometheus-range-query-with-exemplars-workflow
- description: Trigger a config reload and prove the new configuration and rules are live.
  name: Prometheus Reload Configuration and Verify It Applied
  slug: prometheus-reload-config-verify-workflow
- description: Confirm a restarted or upgraded server is healthy, past WAL replay, and running the expected build.
  name: Prometheus Verify Server Readiness After a Restart
  slug: prometheus-server-restart-readiness-workflow
- description: Find a firing alert, silence it by its labels, and confirm the silence took hold.
  name: Prometheus Silence a Firing Alert
  slug: prometheus-silence-firing-alert-workflow
- description: Send a synthetic alert and follow it through to the receiver that will be paged.
  name: Prometheus Test an Alertmanager Routing Path
  slug: prometheus-test-alert-routing-workflow
- description: Work out why a target's metrics are missing — dropped, down, or never configured.
  name: Prometheus Troubleshoot a Missing Scrape Target
  slug: prometheus-troubleshoot-scrape-target-workflow
- description: Size the TSDB, snapshot it, and capture the snapshot directory name.
  name: Prometheus Take a TSDB Snapshot for Backup
  slug: prometheus-tsdb-snapshot-backup-workflow
artifact_total: 58
asyncapis:
- description: The Prometheus Alertmanager webhook receiver sends HTTP POST requests to configured endpoints when alert groups are triggered. Each webhook payload contains a group of alerts sharing common routing la
  name: Prometheus Alertmanager Webhook Events
  slug: prometheus-alertmanager-webhook-asyncapi
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Prometheus Alertmanager Admin API
  slug: open-prometheus-admin-api
- collection_type: open
  name: Prometheus Alertmanager API
  slug: open-prometheus-alertmanager-api
- collection_type: open
  name: Prometheus Alertmanager Admin Alerts API
  slug: open-prometheus-alerts-api
- collection_type: open
  name: Prometheus HTTP API
  slug: open-prometheus-http-api
- collection_type: open
  name: Prometheus Alertmanager Admin Lifecycle API
  slug: open-prometheus-lifecycle-api
- collection_type: open
  name: Prometheus Management API
  slug: open-prometheus-management-api
- collection_type: open
  name: Prometheus Alertmanager Admin Metadata API
  slug: open-prometheus-metadata-api
- collection_type: open
  name: Prometheus Alertmanager Admin Metrics API
  slug: open-prometheus-metrics-api
- collection_type: open
  name: Prometheus Pushgateway API
  slug: open-prometheus-pushgateway-api
- collection_type: open
  name: Prometheus Alertmanager Admin Query API
  slug: open-prometheus-query-api
- collection_type: open
  name: Prometheus Alertmanager Admin Receivers API
  slug: open-prometheus-receivers-api
- collection_type: open
  name: Prometheus Alertmanager Admin Rules API
  slug: open-prometheus-rules-api
- collection_type: open
  name: Prometheus Alertmanager Admin Silences API
  slug: open-prometheus-silences-api
- collection_type: open
  name: Prometheus Alertmanager Admin Status API
  slug: open-prometheus-status-api
- collection_type: open
  name: Prometheus Alertmanager Admin Targets API
  slug: open-prometheus-targets-api
- collection_type: open
  name: Prometheus Alertmanager Admin TSDB API
  slug: open-prometheus-tsdb-api
common:
- group: other
  title: ''
  type: Overlay
  url: overlays/prometheus-alertmanager-api-overlay.yaml
- group: commercial
  title: ''
  type: License
  url: https://github.com/prometheus/prometheus/blob/main/LICENSE
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/prometheus-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/prometheus-domain-security.yml
- group: build
  title: ''
  type: Packages
  url: packages/prometheus-packages.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/prometheus-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/prometheus-llms.txt
- group: design
  title: ''
  type: Conformance
  url: conformance/prometheus-conformance.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/prometheus-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/prometheus-lifecycle.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/prometheus-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/prometheus-conventions.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/prometheus-changelog.yml
- group: build
  title: ''
  type: CLI
  url: cli/prometheus-cli.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/prometheus-data-model.yml
- group: design
  title: ''
  type: JSONLD
  url: json-ld/prometheus-context.jsonld
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/prometheus-metrics-schema.json
- group: company
  title: ''
  type: Website
  url: https://prometheus.io
- group: docs
  title: ''
  type: Documentation
  url: https://prometheus.io/docs/
- group: start
  title: ''
  type: GettingStarted
  url: https://prometheus.io/docs/introduction/getting_started/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/prometheus
- group: build
  title: ''
  type: GitHubRepository
  url: https://github.com/prometheus/prometheus
- group: company
  title: ''
  type: Blog
  url: https://prometheus.io/blog/
- group: operate
  title: ''
  type: Community
  url: https://prometheus.io/community/
- group: operate
  title: ''
  type: ChangeLog
  url: https://github.com/prometheus/prometheus/releases
- group: operate
  title: ''
  type: StackOverflow
  url: https://stackoverflow.com/questions/tagged/prometheus
- group: design
  title: ''
  type: Arazzo
  url: arazzo/prometheus-discover-and-query-metric-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/prometheus-range-query-with-exemplars-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/prometheus-large-promql-query-post-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/prometheus-troubleshoot-scrape-target-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/prometheus-alert-notification-triage-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/prometheus-silence-firing-alert-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/prometheus-expire-silence-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/prometheus-test-alert-routing-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/prometheus-push-batch-job-metrics-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/prometheus-push-grouped-metrics-lifecycle-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/prometheus-purge-retired-job-metrics-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/prometheus-reload-config-verify-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/prometheus-server-restart-readiness-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/prometheus-tsdb-snapshot-backup-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/prometheus-delete-series-reclaim-space-workflow.yml
created: '2024-01-01'
description: An open-source systems monitoring and alerting toolkit originally built at SoundCloud. Prometheus collects and stores metrics as time series data and provides a powerful query language (PromQL) for analysis.
finops:
- name: Prometheus Finops
  service_category: Observability
  slug: prometheus-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/prometheus.png
json_schemas:
- name: Prometheus Metrics and Alerting Schema
  property_count: 0
  slug: prometheus-metrics
jsonld:
- class_count: 0
  name: Prometheus Context
  property_count: 13
  slug: prometheus-context
layout: provider
mcp_servers:
- description: ''
  name: prometheus-mcp.yml
  slug: prometheus-mcpyml
modified: '2026-06-20'
name: Prometheus
nav: Providers
network: true
overview: 'Prometheus publishes 12 APIs on the [APIs.io](https://apis.io/) network, including Admin API, Alerts API, Lifecycle API, and 9 more. Tagged areas include Alerting, Metrics, Monitoring, Observability, and Time Series.


  The Prometheus catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 2 Spectral governance rulesets.


  Prometheus'' developer surface includes authentication, changelog, CLI, documentation, getting-started guide, engineering blog, Stack Overflow tag, and 34 more developer resources.'
plans:
- name: Prometheus Plans Pricing
  plan_count: 1
  slug: prometheus-plans-pricing
random_paper: 57
rate_limits:
- limit_count: 2
  name: Prometheus Rate Limits
  slug: prometheus-rate-limits
rules:
- name: Prometheus API Rules
  rule_count: 3
  severity_counts:
    error: 1
    hint: 0
    info: 1
    warn: 1
  slug: prometheus-asyncapi-spectral-rules
- name: Prometheus API Rules
  rule_count: 6
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 4
  slug: prometheus-jsonschema-spectral-rules
score:
  band: developing
  composite: 45.0
  delta: 0.0
  facets:
    commercial_clarity: 13.2
    contract_quality: 71.8
    developer_ergonomics: 45.7
    discoverability: 72.2
    governance: 38.5
    operational_transparency: 26.3
  previous_composite: 45.0
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 12
    mcp: derived
  schema_version: 0.11.0
  scored_at: '2026-08-17'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/prometheus/refs/heads/main/screenshots/prometheus-2026-06-20T192155.png
security:
- kind: authentication
  name: Prometheus Authentication
  slug: prometheus-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Prometheus Domain Security
  slug: prometheus-domain-security
  summary_line: TLSv1.3 · HSTS
slug: prometheus
tags:
- Alerting
- Metrics
- Monitoring
- Observability
- Time Series
website: https://prometheus.io
---
