---
access_model:
  confidence: medium
  label: Freemium
  onboarding: unknown
  pricing: freemium
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
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 18.0
  scored_at: '2026-08-30'
api_count: 20
apis:
- description: The full Grafana HTTP API surface for self-managed Grafana and Grafana Enterprise. Covers dashboards, folders, data sources, organizations, users, teams, service accounts, API keys, access control (RB
  name: Grafana HTTP API
  slug: grafana-http-api
- description: Create, read, update, delete, search, version, and permission dashboards. Exposes the Kubernetes-style `/apis/dashboard.grafana.app/v1/namespaces/:namespace/dashboards` resource (and the legacy `/api/
  name: Grafana Dashboard API
  slug: grafana-dashboard-api
- description: 'Manage Grafana folders, perform cross-folder dashboard search, and administer folder-level permissions. Folders are the primary organizational unit for grouping dashboards and applying access control '
  name: Grafana Folder and Search API
  slug: grafana-folder-api
- description: 'Programmatically register and manage Grafana data sources (Prometheus, Loki, Tempo, Mimir, Pyroscope, Postgres, MySQL, Elasticsearch, InfluxDB, CloudWatch, Azure Monitor, Google Cloud Monitoring, and '
  name: Grafana Data Source API
  slug: grafana-data-source-api
- description: Provision Grafana Alerting resources programmatically — alert rules, contact points, mute timings, notification policies, and notification templates. Supports headers for file-provisioning workflows a
  name: Grafana Alerting Provisioning API
  slug: grafana-alerting-api
- description: Create, read, update, and delete annotations on Grafana dashboards. Annotations mark events (deploys, incidents, releases) on time-series panels and can be scoped to a dashboard, panel, or organizatio
  name: Grafana Annotations API
  slug: grafana-annotations-api
- description: Manage Grafana organizations, users, teams, team membership, external team sync, and user or org-scoped preferences (default home dashboard, theme, timezone, week start).
  name: Grafana Organization and Users API
  slug: grafana-org-api
- description: 'Manage fine-grained role-based access control assignments, custom roles, permission grants against folders/dashboards/data sources, service accounts, service account tokens, and SSO provider settings '
  name: Grafana Access Control (RBAC) API
  slug: grafana-rbac-api
- description: Server-wide administrative endpoints including global users, settings, server stats, encryption keys, pause-all-alerts, plus Grafana Enterprise extensions for licensing, scheduled PDF/CSV reporting, a
  name: Grafana Admin API
  slug: grafana-admin-api
- description: 'Manage reusable library panels and library variables. Library elements let dashboard authors define a panel or variable once and reference it across many dashboards, with updates propagating to every '
  name: Grafana Library Elements API
  slug: grafana-library-elements-api
- description: Define correlations between data sources to enable in-place pivoting (e.g. trace ID in Tempo to logs in Loki) inside Explore and dashboards. Powers the "click a value, jump to related telemetry" UX th
  name: Grafana Correlations API
  slug: grafana-correlations-api
- description: Capture and share dashboard snapshots (rendered point-in-time copies including data), generate short URLs for long Explore queries and dashboard links, and read or write a user's Explore query history
  name: Grafana Snapshot, Short URL, and Query History API
  slug: grafana-snapshot-shorturl-api
- description: Manage Grafana Cloud stacks (instances), plugins, data sources, regions, access policies, and tokens at `https://grafana.com/api`. Authenticated with Cloud Access Policy bearer tokens. The recommended
  name: Grafana Cloud API
  slug: grafana-cloud-api
- description: Query and push logs to Grafana Loki. Endpoints include `/loki/api/v1/push` (log ingestion), `/loki/api/v1/query` and `/query_range` (LogQL), `/loki/api/v1/labels`, `/loki/api/v1/series`, `/loki/api/v1
  name: Grafana Loki HTTP API
  slug: loki-http-api
- description: Horizontally scalable, multi-tenant, long-term Prometheus-compatible metrics storage. Exposes Prometheus remote-write at `/api/v1/push`, the full Prometheus query API (`/api/v1/query`, `/query_range`,
  name: Grafana Mimir HTTP API
  slug: mimir-http-api
- description: High-volume, minimal-dependency distributed tracing backend. Supports OTLP ingestion, trace lookup by ID (`/api/traces/{traceID}`), TraceQL search (`/api/search`), tag and value listing, and metrics d
  name: Grafana Tempo HTTP API
  slug: tempo-http-api
- description: 'Continuous profiling backend. Ingest pprof and Pyroscope-format CPU, memory, and lock profiles, query flame graphs and merge profiles, and run profile-based comparisons. Pyroscope merged with Grafana '
  name: Grafana Pyroscope HTTP API
  slug: pyroscope-http-api
- description: Programmatically trigger, list, and manage cloud-hosted k6 load tests, projects, organizations, test runs, thresholds, and results. Pairs with the open-source `k6` CLI for JavaScript-authored performa
  name: Grafana k6 Cloud API
  slug: k6-cloud-api
- description: Programmatic access to OnCall alert groups, integrations, escalation chains, schedules, on-call shifts, routes, slack channels, webhooks, and users. Powers on-call rotation management and alert routin
  name: Grafana OnCall API
  slug: oncall-api
- description: Create and manage synthetic probes (HTTP, HTTPS, DNS, TCP, ICMP/ping, traceroute, multi-step scripted browser, gRPC) executed from Grafana Labs' global probe network plus optional private probes. Resu
  name: Grafana Synthetic Monitoring API
  slug: synthetic-monitoring-api
artifact_total: 64
common:
- group: auth
  title: ''
  type: TrustCenter
  url: security/grafana-com-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/grafana-com-domain-security.yml
- group: start
  title: ''
  type: Portal
  url: https://grafana.com
- group: docs
  title: ''
  type: Documentation
  url: https://grafana.com/docs/
- group: docs
  title: ''
  type: Documentation
  url: https://grafana.com/docs/grafana/latest/
- group: docs
  title: ''
  type: Documentation
  url: https://grafana.com/docs/grafana-cloud/
- group: docs
  title: ''
  type: Documentation
  url: https://grafana.com/docs/grafana/latest/developers/http_api/
- group: docs
  title: ''
  type: OpenAPI
  url: https://github.com/grafana/grafana/blob/main/public/api-merged.json
- group: docs
  title: ''
  type: Documentation
  url: https://grafana.com/docs/grafana/latest/developers/
- group: auth
  title: ''
  type: Authentication
  url: https://grafana.com/docs/grafana/latest/developers/http_api/authentication/
- group: auth
  title: ''
  type: Authentication
  url: https://grafana.com/docs/grafana-cloud/account-management/authentication-and-permissions/access-policies/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/grafana
- group: build
  title: ''
  type: SourceCode
  url: https://github.com/grafana/grafana
- group: docs
  title: ''
  type: Documentation
  url: https://grafana.com/grafana/dashboards/
- group: docs
  title: ''
  type: Documentation
  url: https://grafana.com/grafana/plugins/
- group: docs
  title: ''
  type: Documentation
  url: https://grafana.com/docs/plugins/
- group: build
  title: ''
  type: Tools
  url: https://grafana.com/developers/plugin-tools/
- group: docs
  title: ''
  type: Documentation
  url: https://grafana.com/developers/scenes
- group: docs
  title: ''
  type: Documentation
  url: https://grafana.com/developers/saga-design-system/
- group: build
  title: ''
  type: SDKs
  url: https://github.com/grafana/grafana-foundation-sdk
- group: build
  title: ''
  type: SDKs
  url: https://github.com/grafana/grafana-openapi-client-go
- group: build
  title: ''
  type: SDKs
  url: https://github.com/grafana/grafana-api-golang-client
- group: build
  title: ''
  type: Tools
  url: https://github.com/grafana/terraform-provider-grafana
- group: docs
  title: ''
  type: Documentation
  url: https://registry.terraform.io/providers/grafana/grafana/latest/docs
- group: build
  title: ''
  type: Tools
  url: https://github.com/grafana/grafana-operator
- group: build
  title: ''
  type: Tools
  url: https://github.com/grafana/helm-charts
- group: build
  title: ''
  type: Tools
  url: https://github.com/grafana/grafana-image-renderer
- group: build
  title: ''
  type: SDKs
  url: https://github.com/grafana/grafonnet
- group: build
  title: ''
  type: Tools
  url: https://github.com/grafana/grizzly
- group: build
  title: ''
  type: SourceCode
  url: https://github.com/grafana/loki
- group: build
  title: ''
  type: SourceCode
  url: https://github.com/grafana/mimir
- group: build
  title: ''
  type: SourceCode
  url: https://github.com/grafana/tempo
- group: build
  title: ''
  type: SourceCode
  url: https://github.com/grafana/pyroscope
- group: build
  title: ''
  type: SourceCode
  url: https://github.com/grafana/k6
- group: build
  title: ''
  type: SourceCode
  url: https://github.com/grafana/alloy
- group: build
  title: ''
  type: SourceCode
  url: https://github.com/grafana/beyla
- group: build
  title: ''
  type: SDKs
  url: https://github.com/grafana/faro-web-sdk
- group: build
  title: ''
  type: SourceCode
  url: https://github.com/grafana/oncall
- group: build
  title: ''
  type: SourceCode
  url: https://github.com/grafana/synthetic-monitoring-agent
- group: build
  title: ''
  type: SDKs
  url: https://github.com/grafana/grafana-plugin-sdk-go
- group: commercial
  title: ''
  type: Pricing
  url: https://grafana.com/pricing/
- group: commercial
  title: ''
  type: Pricing
  url: https://grafana.com/pricing/
- group: operate
  title: ''
  type: RateLimits
  url: https://grafana.com/docs/grafana/latest/setup-grafana/configure-grafana/configure-rate-limit-data-source/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.grafana.com
- group: company
  title: ''
  type: Blog
  url: https://grafana.com/blog/
- group: company
  title: ''
  type: Blog
  url: https://grafana.com/blog/categories/engineering/
- group: docs
  title: ''
  type: Documentation
  url: https://grafana.com/about/team/
- group: other
  title: ''
  type: Events
  url: https://grafana.com/about/events/
- group: other
  title: ''
  type: Events
  url: https://grafana.com/events/grafanacon/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://grafana.com/legal/terms/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://grafana.com/legal/privacy-policy/
- group: auth
  title: ''
  type: TrustCenter
  url: https://trust.grafana.com/
- group: start
  title: ''
  type: Signup
  url: https://grafana.com/auth/sign-up
- group: start
  title: ''
  type: Portal
  url: https://grafana.com/products/cloud/
- group: start
  title: ''
  type: Portal
  url: https://grafana.com/products/enterprise/
- group: start
  title: ''
  type: Sandbox
  url: https://grafana.com/play/
- group: operate
  title: ''
  type: Forums
  url: https://community.grafana.com/
- group: operate
  title: ''
  type: Support
  url: https://grafana.com/contact
- group: operate
  title: ''
  type: Forums
  url: https://github.com/grafana/grafana/discussions
- group: learn
  title: ''
  type: Training
  url: https://grafana.com/tutorials/
- group: learn
  title: ''
  type: Training
  url: https://university.grafana.com/
- group: design
  title: ''
  type: Versioning
  url: https://grafana.com/docs/release-life-cycle/
- group: operate
  title: ''
  type: ChangeLog
  url: https://grafana.com/docs/grafana/latest/whatsnew/
- group: docs
  title: ''
  type: Documentation
  url: https://grafana.com/about/careers/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/grafana-labs
- group: company
  title: ''
  type: Twitter
  url: https://twitter.com/grafana
- group: learn
  title: ''
  type: YouTube
  url: https://www.youtube.com/c/Grafana
- group: company
  title: ''
  type: Mastodon
  url: https://fosstodon.org/@grafana
created: '2026-05-25T00:00:00.000Z'
description: Grafana Labs builds the open and composable observability stack used by millions of engineers to visualize, query, alert on, and explore their metrics, logs, traces, and profiles. The flagship Grafana OSS dashboarding platform is paired with Grafana Loki (logs), Grafana Mimir (Prometheus-compatible metrics), Grafana Tempo (distributed traces), and Grafana Pyroscope (continuous profiling) — all under the LGTM stack. Grafana Cloud delivers the entire portfolio as a managed SaaS with a generous free tier, while Grafana Enterprise extends self-managed deployments with premium plugins, reporting, RBAC, LBAC, and caching. The ecosystem extends to Grafana k6 (load testing), Grafana Alloy (OpenTelemetry-native collector), Grafana Beyla (eBPF auto-instrumentation), Grafana Faro (frontend observability), Grafana OnCall (incident response), and Synthetic Monitoring. A canonical OpenAPI specification at public/api-merged.json powers the official Go client, the Terraform provider, the Grafana
  Operator, and a deep dashboards-as-code toolchain (Foundation SDK, Grafonnet, Grizzly, Scenes).
features:
- Open-source Grafana — composable observability and dashboarding platform (AGPLv3)
- Grafana Cloud — fully managed observability SaaS with free tier
- Grafana Enterprise — self-managed commercial distribution with premium plugins and features
- Grafana Loki — Prometheus-style label model applied to logs with LogQL query language
- Grafana Mimir — horizontally scalable, multi-tenant, long-term Prometheus-compatible metrics storage
- Grafana Tempo — minimal-dependency distributed tracing backend with TraceQL search
- Grafana Pyroscope — continuous profiling backend (CPU, memory, lock, goroutine)
- Grafana k6 — JavaScript-authored load and performance testing with Cloud execution
- Grafana Alloy — OpenTelemetry-native distribution of the OpenTelemetry Collector
- Grafana Beyla — eBPF-based zero-instrumentation observability for HTTP/gRPC/SQL services
- Grafana Faro — frontend observability SDK for real user monitoring
- Grafana OnCall — on-call scheduling, escalation, and alert routing
- Grafana Incident and IRM (Incident Response Management) suite
- Grafana SLO — declarative service level objectives backed by Prometheus
- Grafana Synthetic Monitoring — global probe network for HTTP, DNS, TCP, ICMP, scripted browser, gRPC
- Grafana Application Observability — OpenTelemetry-driven APM
- Grafana Kubernetes Monitoring — preconfigured Kubernetes observability stack
- Adaptive Metrics — automated cardinality reduction (up to 80% savings)
- Adaptive Logs — log volume reduction (~50%)
- Adaptive Telemetry — unified Adaptive Metrics / Logs / Traces cost optimization
- 150+ data sources (Prometheus, InfluxDB, Elasticsearch, OpenSearch, MySQL, Postgres, MSSQL, CloudWatch, Azure Monitor, Google Cloud Monitoring, Snowflake, Splunk, Datadog, BigQuery, MongoDB, and more)
- 500+ community plugins (panels, data sources, apps)
- Library panels and library variables for reusable dashboard components
- Dashboards-as-code via Foundation SDK, Grafonnet, Grizzly, and Terraform Provider
- Grafana Operator for Kubernetes-native dashboard, alert, and data source provisioning
- Scenes framework for composable dashboard authoring
- Plugin SDK and create-plugin (plugin-tools) for community and enterprise plugin development
- RBAC with custom roles, service accounts, and folder/dashboard/data source permission grants
- SSO via SAML, OAuth, LDAP with team sync
- Public dashboards and snapshot sharing
- OpenTelemetry-first ingestion via Alloy with OTLP, Prometheus remote write, Loki, and Tempo protocols
- Unified Alerting with rule provisioning API, contact points, mute timings, notification templates
- Correlations between data sources for click-through pivots across metrics, logs, traces, profiles
- Data source Label-Based Access Control (LBAC) for tenant isolation
- Query and resource caching (Enterprise)
- Scheduled PDF/CSV reporting (Enterprise)
- Federal Cloud, Public Cloud, and Bring Your Own Cloud deployment options
- FedRAMP Moderate, SOC 2 Type II, PCI DSS, GDPR, HIPAA-eligible compliance posture
- Canonical OpenAPI 2.0 specification (api-merged.json) drives Go client, Terraform provider, and SDKs
finops:
- name: Grafana Com Finops
  service_category: Observability and Monitoring
  slug: grafana-com-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/grafana-com.png
layout: provider
modified: '2026-05-25'
name: Grafana
nav: Providers
network: true
overview: 'Grafana publishes 12 APIs on the [APIs.io](https://apis.io/) network, including HTTP API, Dashboard API, Folder and Search API, and 9 more. Tagged areas include Observability, Monitoring, Dashboards, Logs, and Metrics.


  Grafana''s developer surface includes developer portal, documentation, authentication, tooling, pricing, engineering blog, signup flow, and 61 more developer resources.'
plans:
- name: Grafana Com Plans Pricing
  plan_count: 5
  slug: grafana-com-plans-pricing
random_paper: 13
rate_limits:
- limit_count: 7
  name: Grafana Com Rate Limits
  slug: grafana-com-rate-limits
score:
  band: developing
  composite: 52.3
  coverage:
    artifact_dirs: 6
    catalog_gap: 56.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 92.1
    commercial_clarity: 92.1
    contract_governance: 0.0
    contract_quality: 26.7
    developer_ergonomics: 61.9
    discoverability: 59.3
    governance: 0.0
    operational_transparency: 68.4
  previous_composite: 52.3
  schema_version: 0.17.2
  scored_at: '2026-08-30'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/grafana-com/refs/heads/main/screenshots/grafana-com-2026-06-20T182343.png
security:
- kind: domain-security
  name: Grafana Com Domain Security
  slug: grafana-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Grafana Com Trust Center
  slug: grafana-com-trust-center
  summary_line: SOC 2, ISO 27001, PCI DSS, FedRAMP, GDPR, CSA STAR
slug: grafana-com
tags:
- Observability
- Monitoring
- Dashboards
- Logs
- Metrics
- Traces
- Profiling
- Alerting
- Open-Source
- Grafana Labs
website: https://grafana.com
---
