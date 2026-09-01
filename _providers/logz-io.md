---
access_model:
  confidence: medium
  label: Paid
  onboarding: unknown
  pricing: paid
  public: false
  source:
  - plans
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 22.2
  scored_at: '2026-09-01'
api_count: 19
apis:
- description: 'Query indexed logs against the Logz.io managed Elasticsearch / OpenSearch cluster using a request body that mirrors the upstream Elasticsearch Search API. Includes `/v1/search` for ad-hoc queries and '
  name: Logz.io Search Logs API
  slug: logz-io-search-logs-api
- description: Configure long-term archive destinations (S3, ADLS, Google Cloud Storage), test connectivity, list and delete archive settings, then restore archived logs back into Logz.io for replay or compliance re
  name: Logz.io Archive and Restore API
  slug: logz-io-archive-restore-api
- description: Create, list, activate, deactivate, and delete drop filters that discard matching events before they enter Logz.io's hot index. The primary tool for trimming ingest volume and managing observability c
  name: Logz.io Drop Filters API
  slug: logz-io-drop-filters-api
- description: Manage Logz.io alert rules — create, retrieve, update, enable, disable, and delete log-based and multi-account alerts via `/v2/alerts`, list currently triggered alerts via `/v1/alerts/triggered-alerts
  name: Logz.io Alerts API
  slug: logz-io-alerts-api
- description: Manage downstream notification destinations attached to alerts. Supports Slack, PagerDuty, Microsoft Teams, BigPanda, OpsGenie, ServiceNow, VictorOps, custom HTTPS webhooks, and email endpoints. Endpo
  name: Logz.io Notification Endpoints API
  slug: logz-io-notification-endpoints-api
- description: List, create, update, suspend, and delete users in the main account and across all associated sub-accounts. Includes authentication groups (SSO group-to-role mappings), the `whoami` introspection endp
  name: Logz.io Users API
  slug: logz-io-users-api
- description: 'Manage the three Logz.io credential types — API tokens (account control plane), log-shipping tokens (ingest authentication for shippers like Filebeat, Fluentd, OpenTelemetry, and the Logz.io agents), '
  name: Logz.io Tokens API
  slug: logz-io-tokens-api
- description: Provision and resize time-based log sub-accounts and metrics accounts. Lets owners split daily ingest quotas across environments, teams, or customers and reshape retention without re-shipping data. In
  name: Logz.io Accounts API
  slug: logz-io-accounts-api
- description: 'Prometheus-compatible read path against the Logz.io Infrastructure Monitoring backend. Implements `query`, `query_range`, `series`, `labels`, and `label/{name}/values` exactly as upstream Prometheus, '
  name: Logz.io Metrics Prometheus API
  slug: logz-io-metrics-prometheus-api
- description: Pass-through API to the Logz.io fork of Grafana plus a subset of upstream Grafana endpoints. Covers dashboards (`/api/dashboards`), folders, alert rules and silences (`/api/v1/provisioning/alert-rules
  name: Logz.io Grafana API
  slug: logz-io-grafana-api
- description: Logz.io's Perses-compatible dashboard API (Perses is the CNCF observability dashboard project Logz.io helps maintain). Manages projects, dashboards, global datasources, and the Perses-flavored dashboa
  name: Logz.io Perses API
  slug: logz-io-perses-api
- description: Logz.io Cloud SIEM control plane — manage detection rules (correlation and threshold), retrieve raised security events, and administer the SIEM sub-account. Backs the detect → triage → respond workflo
  name: Logz.io Cloud SIEM API
  slug: logz-io-cloud-siem-api
- description: Provision the Logz.io managed pull-side log shippers. Connect AWS CloudTrail streams and S3 buckets (with IAM assume-role) directly from the API so customers can stand up log collection without deploy
  name: Logz.io Log Shipping API
  slug: logz-io-log-shipping-api
- description: Manage Sawmill log-type pipelines and external mapping uploads. Sawmill is Logz.io's open-source JSON transformation engine; this API lets customers attach declarative parsing pipelines per log-type a
  name: Logz.io Parsing Pipelines API
  slug: logz-io-parsing-pipelines-api
- description: 'CRUD for reference data used to enrich and filter logs and alerts. Customers upload lookup lists of IPs, hostnames, user IDs, or business identifiers and reference them by name in alerts and queries, '
  name: Logz.io Lookup Lists API
  slug: logz-io-lookup-lists-api
- description: Retrieve the cognitive-insights and anomaly findings surfaced by Logz.io's AI observability layer. Returns ranked operational insights — Exceptions, Slow Transactions, Critical Events — for downstream
  name: Logz.io Insights API
  slug: logz-io-insights-api
- description: Post deployment events into Logz.io as markers so they overlay on dashboards and contextual searches. The mechanism release pipelines use to correlate spikes in error logs or latency with the deployme
  name: Logz.io Deployment Markers API
  slug: logz-io-deployments-api
- description: Drive the OpenSearch / Kibana saved-object snapshot lifecycle inside Logz.io — import and export visualizations, searches, and dashboard objects programmatically. The promotion-path used to ship Kiban
  name: Logz.io OpenSearch Snapshots API
  slug: logz-io-snapshots-api
- description: Query the Logz.io account-level audit trail and list the event types it emits. Customers wire this into their own SIEM or governance pipelines for ISO 27001 / SOC 2-style activity tracking over Logz.i
  name: Logz.io Audit Trail API
  slug: logz-io-audit-trail-api
arazzos:
- description: Confirm which account a token belongs to, then list its associated accounts.
  name: Logz.io Verify Token And Discover Accounts
  slug: logz-io-account-verify-workflow
- description: Create an alert, refine its threshold, then list all alerts to confirm it.
  name: Logz.io Alert Create, Update, And List
  slug: logz-io-alert-create-update-list-workflow
- description: Create an alert, disable it for a maintenance window, re-enable it, and verify.
  name: Logz.io Alert Enable/Disable Lifecycle
  slug: logz-io-alert-lifecycle-workflow
- description: Create a custom webhook notification endpoint and an alert that routes to it.
  name: Logz.io Custom Webhook Endpoint Then Alert
  slug: logz-io-custom-endpoint-then-alert-workflow
- description: Create a Grafana folder, save a dashboard into it, and read it back by uid.
  name: Logz.io Grafana Dashboard In New Folder
  slug: logz-io-dashboard-in-folder-workflow
- description: List notification endpoints, confirm one by id, and delete it.
  name: Logz.io Notification Endpoint Cleanup
  slug: logz-io-endpoint-cleanup-workflow
- description: Create a Slack notification endpoint, then wire a new alert to notify it.
  name: Logz.io Notification Endpoint Then Alert
  slug: logz-io-endpoint-then-alert-workflow
- description: Create a Grafana contact point, confirm it by name, and list alert rules.
  name: Logz.io Grafana Contact Point Setup
  slug: logz-io-grafana-contact-point-workflow
- description: Discover label names, list matching series, then run an instant PromQL query.
  name: Logz.io Metrics Explore And Query
  slug: logz-io-metrics-explore-workflow
- description: Run a log search, then open a scroll to page through the full result set.
  name: Logz.io Search Then Scroll Logs
  slug: logz-io-search-then-scroll-workflow
- description: List sub accounts, fetch one by id to confirm, and delete it.
  name: Logz.io Sub Account Cleanup
  slug: logz-io-subaccount-cleanup-workflow
- description: Create a time-based log sub account, read it back, and adjust its retention.
  name: Logz.io Provision a Sub Account
  slug: logz-io-subaccount-provision-workflow
- description: Find an alert by title and update it if it exists, otherwise create it.
  name: Logz.io Upsert an Alert
  slug: logz-io-upsert-alert-workflow
artifact_total: 44
common:
- group: auth
  title: ''
  type: TrustCenter
  url: security/logz-io-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/logz-io-domain-security.yml
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/logzio/overview
- group: design
  title: ''
  type: Arazzo
  url: arazzo/logz-io-account-verify-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/logz-io-alert-create-update-list-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/logz-io-alert-lifecycle-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/logz-io-custom-endpoint-then-alert-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/logz-io-dashboard-in-folder-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/logz-io-endpoint-cleanup-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/logz-io-endpoint-then-alert-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/logz-io-grafana-contact-point-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/logz-io-metrics-explore-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/logz-io-search-then-scroll-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/logz-io-subaccount-cleanup-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/logz-io-subaccount-provision-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/logz-io-upsert-alert-workflow.yml
- group: start
  title: ''
  type: Portal
  url: https://logz.io/
- group: start
  title: ''
  type: Login
  url: https://app.logz.io/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.logz.io/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.logz.io/api/
- group: docs
  title: ''
  type: Documentation
  url: https://api-docs.logz.io/docs/logz/logz-io-api
- group: auth
  title: ''
  type: Authentication
  url: https://app.logz.io/#/dashboard/settings/manage-tokens/api
- group: other
  title: ''
  type: Regions
  url: https://docs.logz.io/user-guide/accounts/account-region.html
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.logz.io/user-guide/giveittome/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://logz.io/about-us/terms-of-use/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://logz.io/about-us/privacy-policy/
- group: auth
  title: ''
  type: Security
  url: https://logz.io/learn/security-and-compliance/
- group: auth
  title: ''
  type: TrustCenter
  url: https://logz.io/trust-center/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.logz.io/
- group: company
  title: ''
  type: Blog
  url: https://logz.io/blog/
- group: operate
  title: ''
  type: ChangeLog
  url: https://logz.io/blog/category/news/
- group: operate
  title: ''
  type: Support
  url: https://logz.io/support/
- group: operate
  title: ''
  type: Support
  url: https://docs.logz.io/contact-support.html
- group: operate
  title: ''
  type: ContactUs
  url: https://logz.io/about/contact-us/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/logzio
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/logz.io/
- group: company
  title: ''
  type: Twitter
  url: https://twitter.com/logzio
- group: learn
  title: ''
  type: YouTube
  url: https://www.youtube.com/channel/UCRtxh4MS8gWQ8mTCnTcLZ-Q
- group: company
  title: ''
  type: Careers
  url: https://logz.io/about-us/careers/
- group: company
  title: ''
  type: AboutUs
  url: https://logz.io/about-us/
- group: commercial
  title: ''
  type: License
  url: https://logz.io/about-us/forked-statement/
- group: other
  title: ''
  type: CaseStudies
  url: https://logz.io/customers/
- group: company
  title: ''
  type: Partners
  url: https://logz.io/partners/
- group: other
  title: ''
  type: Events
  url: https://logz.io/events/
- group: other
  title: ''
  type: Containers
  url: https://hub.docker.com/u/logzio
- group: docs
  title: ''
  type: Documentation
  url: https://docs.logz.io/integrations/terraform/
- group: build
  title: ''
  type: Tools
  url: https://github.com/logzio/terraform-provider-logzio
- group: build
  title: ''
  type: SDKs
  url: https://github.com/logzio/logzio_terraform_client
- group: build
  title: ''
  type: SDKs
  url: https://github.com/logzio/logzio-go
- group: build
  title: ''
  type: SDKs
  url: https://github.com/logzio/logzio-nodejs
- group: build
  title: ''
  type: SDKs
  url: https://github.com/logzio/logzio-browser
- group: build
  title: ''
  type: SDKs
  url: https://github.com/logzio/logzio-java-sender
- group: build
  title: ''
  type: SDKs
  url: https://github.com/logzio/logzio-dotnet
- group: build
  title: ''
  type: SDKs
  url: https://github.com/logzio/logzio-python-handler
- group: build
  title: ''
  type: SDKs
  url: https://github.com/logzio/logzio-ruby
- group: build
  title: ''
  type: SDKs
  url: https://github.com/logzio/logzio-bunyan
- group: build
  title: ''
  type: SDKs
  url: https://github.com/logzio/logzio-log4j2-appender
- group: build
  title: ''
  type: SDKs
  url: https://github.com/logzio/logzio-logback-appender
- group: build
  title: ''
  type: Tools
  url: https://github.com/logzio/logzio-helm
- group: build
  title: ''
  type: Tools
  url: https://github.com/logzio/logzio-k8s
- group: build
  title: ''
  type: Tools
  url: https://github.com/logzio/logzio_aws_serverless
- group: build
  title: ''
  type: Tools
  url: https://github.com/logzio/logzio-azure-serverless
- group: build
  title: ''
  type: Tools
  url: https://github.com/logzio/grafana-logzio-datasource
- group: build
  title: ''
  type: Tools
  url: https://github.com/logzio/docker-collector-logs
- group: build
  title: ''
  type: Tools
  url: https://github.com/logzio/docker-collector-metrics
- group: build
  title: ''
  type: Tools
  url: https://github.com/logzio/docker-logging-plugin
- group: build
  title: ''
  type: Tools
  url: https://github.com/logzio/fluent-bit-logzio-output
- group: build
  title: ''
  type: Tools
  url: https://github.com/logzio/sawmill
- group: docs
  title: ''
  type: Documentation
  url: https://github.com/logzio/logz-docs
- group: operate
  title: ''
  type: Community
  url: https://github.com/logzio/community
- group: learn
  title: ''
  type: Learning
  url: https://logz.io/learn/complete-guide-elk-stack/
- group: learn
  title: ''
  type: Learning
  url: https://logz.io/learn/
- group: commercial
  title: ''
  type: Plans
  url: https://logz.io/pricing/
- group: commercial
  title: ''
  type: Pricing
  url: https://logz.io/pricing/
- group: docs
  title: ''
  type: OpenAPI
  url: openapi/logz-io-api-openapi.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/logz-io-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/logz-io-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/logz-io-finops.yml
- group: design
  title: ''
  type: JSONLD
  url: json-ld/logz-io-context.jsonld
created: '2026-05-25'
description: Logz.io is a managed cloud observability platform built on the ELK Stack (Elasticsearch / Logstash / Kibana, plus OpenSearch and Grafana) that unifies log management, infrastructure monitoring, distributed tracing, and Cloud SIEM behind a consumption-based pricing model. The platform pairs an AI Agent layer for root-cause analysis with native OpenTelemetry, Prometheus, Grafana, and Perses compatibility, and exposes its entire control plane through a single OpenAPI 2.0-described public API covering search, alerting, sub-account management, security rules, parsing pipelines, archive / restore, and visualization-as-code via the Logz.io fork of Grafana and Perses.
finops:
- name: Logz Io Finops
  service_category: Management and Governance
  slug: logz-io-finops
graphqls:
- description: Conceptual GraphQL schema for the Logz.io cloud observability platform. Logz.io unifies log management, infrastructure metrics, distributed tracing, and Cloud SIEM behind a single API surface. This sc
  name: Logz.io GraphQL Schema
  slug: logz-io-graphql
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/logz-io.png
json_schemas:
- name: Logz.io Alert Rule
  property_count: 10
  slug: logz-io-alert-rule
- name: Logz.io Log Document
  property_count: 16
  slug: logz-io-log-document
- name: Logz.io Metric Sample
  property_count: 3
  slug: logz-io-metric-sample
- name: Logz.io Search Request
  property_count: 8
  slug: logz-io-search-request
jsonld:
- class_count: 0
  name: Logz Io Context
  property_count: 40
  slug: logz-io-context
layout: provider
modified: '2026-05-25'
name: Logz.io
nav: Providers
network: true
overview: 'Logz.io publishes 19 APIs on the [APIs.io](https://apis.io/) network, including Search Logs API, Archive and Restore API, Drop Filters API, and 16 more. Tagged areas include Observability, Logging, Metrics, Tracing, and SIEM.


  The Logz.io catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Logz.io''s developer surface includes developer portal, documentation, authentication, getting-started guide, engineering blog, changelog, support, and 72 more developer resources.'
plans:
- name: Logz Io Plans Pricing
  plan_count: 7
  slug: logz-io-plans-pricing
random_paper: 12
rate_limits:
- limit_count: 1
  name: Logz Io Rate Limits
  slug: logz-io-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: Logz.io API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: logz-io-jsonschema-spectral-rules
score:
  band: strong
  composite: 65.2
  coverage:
    artifact_dirs: 14
    catalog_gap: 30.8
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 92.1
    commercial_clarity: 92.1
    contract_governance: 9.8
    contract_quality: 60.1
    developer_ergonomics: 71.4
    discoverability: 74.1
    governance: 9.8
    operational_transparency: 68.4
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: no_resolvable_host
  previous_composite: 65.2
  provenance:
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 1
  schema_version: 0.17.2
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/logz-io/refs/heads/main/screenshots/logz-io-2026-06-20T184702.png
security:
- kind: domain-security
  name: Logz Io Domain Security
  slug: logz-io-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Logz Io Trust Center
  slug: logz-io-trust-center
  summary_line: SOC 2, HIPAA, FedRAMP
slug: logz-io
tags:
- Observability
- Logging
- Metrics
- Tracing
- SIEM
- ELK
- Elasticsearch
- OpenSearch
- Prometheus
- Grafana
- OpenTelemetry
- AIOps
- Cloud Observability
- Managed ELK
- Cost Management
website: https://logz.io/
---
