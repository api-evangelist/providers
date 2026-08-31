---
access_model:
  confidence: medium
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: verified
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 33.2
  scored_at: '2026-08-30'
agentic_access:
- acting_count: 241
  human_in_the_loop: 0
  name: Influxdata Agentic Access
  operation_count: 403
  slug: influxdata-agentic-access
  summary_line: 403 operations · 241 acting
api_count: 2
apis:
- description: Create and manage authorizations (API tokens). An _authorization_ contains a list of `read` and `write` permissions for organization resources and provides an API token for authentication. An authoriz
  name: InfluxData Authorizations (API tokens) API
  slug: influxdata-authorizations-api-tokens-api
- description: The Backup API from InfluxData — 3 operation(s) for backup.
  name: InfluxData Backup API
  slug: influxdata-backup-api
- description: The Bucket Schemas API from InfluxData — 2 operation(s) for bucket schemas.
  name: InfluxData Bucket Schemas API
  slug: influxdata-bucket-schemas-api
- description: Store your data in InfluxDB [buckets](https://docs.influxdata.com/influxdb/cloud/reference/glossary/#bucket). A bucket is a named location where time series data is stored. All buckets have a [retenti
  name: InfluxData Buckets API
  slug: influxdata-buckets-api
- description: The Cells API from InfluxData — 3 operation(s) for cells.
  name: InfluxData Cells API
  slug: influxdata-cells-api
- description: The Checks API from InfluxData — 5 operation(s) for checks.
  name: InfluxData Checks API
  slug: influxdata-checks-api
- description: The Config API from InfluxData — 2 operation(s) for config.
  name: InfluxData Config API
  slug: influxdata-config-api
- description: The Dashboards API from InfluxData — 11 operation(s) for dashboards.
  name: InfluxData Dashboards API
  slug: influxdata-dashboards-api
- description: The Data I/O endpoints API from InfluxData — 6 operation(s) for data i/o endpoints.
  name: InfluxData Data I/O endpoints API
  slug: influxdata-data-i-o-endpoints-api
- description: The InfluxDB 1.x data model includes [databases](https://docs.influxdata.com/influxdb/v1.8/concepts/glossary/#database) and [retention policies](https://docs.influxdata.com/influxdb/v1.8/concepts/glos
  name: InfluxData DBRPs API
  slug: influxdata-dbrps-api
- description: Generate profiling and trace reports. Use routes under `/debug/pprof` to analyze the Go runtime of InfluxDB. These endpoints generate [Go runtime profiles](https://pkg.go.dev/runtime/pprof) and **trac
  name: InfluxData Debug API
  slug: influxdata-debug-api
- description: Delete data from an InfluxDB bucket.
  name: InfluxData Delete API
  slug: influxdata-delete-api
- description: The Health API from InfluxData — 1 operation(s) for health.
  name: InfluxData Health API
  slug: influxdata-health-api
- description: The Labels API from InfluxData — 2 operation(s) for labels.
  name: InfluxData Labels API
  slug: influxdata-labels-api
- description: The Limits API from InfluxData — 1 operation(s) for limits.
  name: InfluxData Limits API
  slug: influxdata-limits-api
- description: The Metrics API from InfluxData — 1 operation(s) for metrics.
  name: InfluxData Metrics API
  slug: influxdata-metrics-api
- description: The NotificationEndpoints API from InfluxData — 4 operation(s) for notificationendpoints.
  name: InfluxData NotificationEndpoints API
  slug: influxdata-notificationendpoints-api
- description: The NotificationRules API from InfluxData — 4 operation(s) for notificationrules.
  name: InfluxData NotificationRules API
  slug: influxdata-notificationrules-api
- description: Manage your [organization](https://docs.influxdata.com/influxdb/cloud/reference/glossary/#organization). An organization is a workspace for a group of users. Organizations can be used to separate diff
  name: InfluxData Organizations API
  slug: influxdata-organizations-api
- description: The Ping API from InfluxData — 1 operation(s) for ping.
  name: InfluxData Ping API
  slug: influxdata-ping-api
- description: Retrieve data, analyze queries, and get query suggestions.
  name: InfluxData Query API
  slug: influxdata-query-api
- description: The Ready API from InfluxData — 1 operation(s) for ready.
  name: InfluxData Ready API
  slug: influxdata-ready-api
- description: The RemoteConnections API from InfluxData — 2 operation(s) for remoteconnections.
  name: InfluxData RemoteConnections API
  slug: influxdata-remoteconnections-api
- description: The Replications API from InfluxData — 3 operation(s) for replications.
  name: InfluxData Replications API
  slug: influxdata-replications-api
- description: The Resources API from InfluxData — 1 operation(s) for resources.
  name: InfluxData Resources API
  slug: influxdata-resources-api
- description: The Restore API from InfluxData — 5 operation(s) for restore.
  name: InfluxData Restore API
  slug: influxdata-restore-api
- description: The Routes API from InfluxData — 1 operation(s) for routes.
  name: InfluxData Routes API
  slug: influxdata-routes-api
- description: The Rules API from InfluxData — 1 operation(s) for rules.
  name: InfluxData Rules API
  slug: influxdata-rules-api
- description: The Scraper Targets API from InfluxData — 8 operation(s) for scraper targets.
  name: InfluxData Scraper Targets API
  slug: influxdata-scraper-targets-api
- description: The Secrets API from InfluxData — 3 operation(s) for secrets.
  name: InfluxData Secrets API
  slug: influxdata-secrets-api
- description: The Security and access endpoints API from InfluxData — 16 operation(s) for security and access endpoints.
  name: InfluxData Security and access endpoints API
  slug: influxdata-security-and-access-endpoints-api
- description: The Setup API from InfluxData — 2 operation(s) for setup.
  name: InfluxData Setup API
  slug: influxdata-setup-api
- description: The Signin API from InfluxData — 1 operation(s) for signin.
  name: InfluxData Signin API
  slug: influxdata-signin-api
- description: The Signout API from InfluxData — 1 operation(s) for signout.
  name: InfluxData Signout API
  slug: influxdata-signout-api
- description: The Sources API from InfluxData — 4 operation(s) for sources.
  name: InfluxData Sources API
  slug: influxdata-sources-api
- description: The System information endpoints API from InfluxData — 17 operation(s) for system information endpoints.
  name: InfluxData System information endpoints API
  slug: influxdata-system-information-endpoints-api
- description: Process and analyze your data with [tasks](https://docs.influxdata.com/influxdb/cloud/reference/glossary/#task) in the InfluxDB task engine. Use the `/api/v2/tasks` endpoints to schedule and manage ta
  name: InfluxData Tasks API
  slug: influxdata-tasks-api
- description: The Telegraf Plugins API from InfluxData — 1 operation(s) for telegraf plugins.
  name: InfluxData Telegraf Plugins API
  slug: influxdata-telegraf-plugins-api
- description: The Telegrafs API from InfluxData — 8 operation(s) for telegrafs.
  name: InfluxData Telegrafs API
  slug: influxdata-telegrafs-api
- description: Export and apply InfluxDB **templates**. Manage **stacks** of templated InfluxDB resources. InfluxDB templates are prepackaged configurations for resources. Use InfluxDB templates to configure a fresh
  name: InfluxData Templates API
  slug: influxdata-templates-api
- description: The Usage API from InfluxData — 1 operation(s) for usage.
  name: InfluxData Usage API
  slug: influxdata-usage-api
- description: Retrieve specific users. InfluxDB Cloud lets you invite and collaborate with multiple users in your organization. To invite and remove users from your organization, use the InfluxDB Cloud user interfa
  name: InfluxData Users API
  slug: influxdata-users-api
- description: The Variables API from InfluxData — 4 operation(s) for variables.
  name: InfluxData Variables API
  slug: influxdata-variables-api
- description: The Views API from InfluxData — 1 operation(s) for views.
  name: InfluxData Views API
  slug: influxdata-views-api
- description: Write time series data to [buckets](https://docs.influxdata.com/influxdb/cloud/reference/glossary/#bucket).
  name: InfluxData Write API
  slug: influxdata-write-api
artifact_total: 97
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: InfluxDB Cloud API Service Authorizations (API tokens) Authorizations (API tokens) Authorizations (API tokens) API
  slug: open-influxdata-authorizations-api-tokens-api
- collection_type: open
  name: InfluxDB Cloud API Service Authorizations (API tokens) Authorizations (API tokens) Backup API
  slug: open-influxdata-backup-api
- collection_type: open
  name: InfluxDB Cloud API Service Authorizations (API tokens) Authorizations (API tokens) Bucket Schemas API
  slug: open-influxdata-bucket-schemas-api
- collection_type: open
  name: InfluxDB Cloud API Service Authorizations (API tokens) Authorizations (API tokens) Buckets API
  slug: open-influxdata-buckets-api
- collection_type: open
  name: InfluxDB Cloud API Service Authorizations (API tokens) Authorizations (API tokens) Cells API
  slug: open-influxdata-cells-api
- collection_type: open
  name: InfluxDB Cloud API Service Authorizations (API tokens) Authorizations (API tokens) Checks API
  slug: open-influxdata-checks-api
- collection_type: open
  name: InfluxDB Cloud API Service Authorizations (API tokens) Authorizations (API tokens) Config API
  slug: open-influxdata-config-api
- collection_type: open
  name: InfluxDB Cloud API Service Authorizations (API tokens) Authorizations (API tokens) Dashboards API
  slug: open-influxdata-dashboards-api
- collection_type: open
  name: InfluxDB Cloud API Service Authorizations (API tokens) Authorizations (API tokens) Data I/O endpoints API
  slug: open-influxdata-data-i-o-endpoints-api
- collection_type: open
  name: InfluxDB Cloud API Service Authorizations (API tokens) Authorizations (API tokens) DBRPs API
  slug: open-influxdata-dbrps-api
- collection_type: open
  name: InfluxDB Cloud API Service Authorizations (API tokens) Authorizations (API tokens) Debug API
  slug: open-influxdata-debug-api
- collection_type: open
  name: InfluxDB Cloud API Service Authorizations (API tokens) Authorizations (API tokens) Delete API
  slug: open-influxdata-delete-api
- collection_type: open
  name: InfluxDB Cloud API Service Authorizations (API tokens) Authorizations (API tokens) Health API
  slug: open-influxdata-health-api
- collection_type: open
  name: InfluxDB Cloud API Service Authorizations (API tokens) Authorizations (API tokens) Labels API
  slug: open-influxdata-labels-api
- collection_type: open
  name: InfluxDB Cloud API Service Authorizations (API tokens) Authorizations (API tokens) Limits API
  slug: open-influxdata-limits-api
- collection_type: open
  name: InfluxDB Cloud API Service Authorizations (API tokens) Authorizations (API tokens) Metrics API
  slug: open-influxdata-metrics-api
- collection_type: open
  name: InfluxDB Cloud API Service Authorizations (API tokens) Authorizations (API tokens) NotificationEndpoints API
  slug: open-influxdata-notificationendpoints-api
- collection_type: open
  name: InfluxDB Cloud API Service Authorizations (API tokens) Authorizations (API tokens) NotificationRules API
  slug: open-influxdata-notificationrules-api
- collection_type: open
  name: InfluxDB Cloud API Service Authorizations (API tokens) Authorizations (API tokens) Organizations API
  slug: open-influxdata-organizations-api
- collection_type: open
  name: InfluxDB Cloud API Service Authorizations (API tokens) Authorizations (API tokens) Ping API
  slug: open-influxdata-ping-api
- collection_type: open
  name: InfluxDB Cloud API Service Authorizations (API tokens) Authorizations (API tokens) Query API
  slug: open-influxdata-query-api
- collection_type: open
  name: InfluxDB Cloud API Service Authorizations (API tokens) Authorizations (API tokens) Ready API
  slug: open-influxdata-ready-api
- collection_type: open
  name: InfluxDB Cloud API Service Authorizations (API tokens) Authorizations (API tokens) RemoteConnections API
  slug: open-influxdata-remoteconnections-api
- collection_type: open
  name: InfluxDB Cloud API Service Authorizations (API tokens) Authorizations (API tokens) Replications API
  slug: open-influxdata-replications-api
- collection_type: open
  name: InfluxDB Cloud API Service Authorizations (API tokens) Authorizations (API tokens) Resources API
  slug: open-influxdata-resources-api
- collection_type: open
  name: InfluxDB Cloud API Service Authorizations (API tokens) Authorizations (API tokens) Restore API
  slug: open-influxdata-restore-api
- collection_type: open
  name: InfluxDB Cloud API Service Authorizations (API tokens) Authorizations (API tokens) Routes API
  slug: open-influxdata-routes-api
- collection_type: open
  name: InfluxDB Cloud API Service Authorizations (API tokens) Authorizations (API tokens) Rules API
  slug: open-influxdata-rules-api
- collection_type: open
  name: InfluxDB Cloud API Service Authorizations (API tokens) Authorizations (API tokens) Scraper Targets API
  slug: open-influxdata-scraper-targets-api
- collection_type: open
  name: InfluxDB Cloud API Service Authorizations (API tokens) Authorizations (API tokens) Secrets API
  slug: open-influxdata-secrets-api
- collection_type: open
  name: InfluxDB Cloud API Service Authorizations (API tokens) Authorizations (API tokens) Security and access endpoints API
  slug: open-influxdata-security-and-access-endpoints-api
- collection_type: open
  name: InfluxDB Cloud API Service Authorizations (API tokens) Authorizations (API tokens) Setup API
  slug: open-influxdata-setup-api
- collection_type: open
  name: InfluxDB Cloud API Service Authorizations (API tokens) Authorizations (API tokens) Signin API
  slug: open-influxdata-signin-api
- collection_type: open
  name: InfluxDB Cloud API Service Authorizations (API tokens) Authorizations (API tokens) Signout API
  slug: open-influxdata-signout-api
- collection_type: open
  name: InfluxDB Cloud API Service Authorizations (API tokens) Authorizations (API tokens) Sources API
  slug: open-influxdata-sources-api
- collection_type: open
  name: InfluxDB Cloud API Service Authorizations (API tokens) Authorizations (API tokens) System information endpoints API
  slug: open-influxdata-system-information-endpoints-api
- collection_type: open
  name: InfluxDB Cloud API Service Authorizations (API tokens) Authorizations (API tokens) Tasks API
  slug: open-influxdata-tasks-api
- collection_type: open
  name: InfluxDB Cloud API Service Authorizations (API tokens) Authorizations (API tokens) Telegraf Plugins API
  slug: open-influxdata-telegraf-plugins-api
- collection_type: open
  name: InfluxDB Cloud API Service Authorizations (API tokens) Authorizations (API tokens) Telegrafs API
  slug: open-influxdata-telegrafs-api
- collection_type: open
  name: InfluxDB Cloud API Service Authorizations (API tokens) Authorizations (API tokens) Templates API
  slug: open-influxdata-templates-api
- collection_type: open
  name: InfluxDB Cloud API Service Authorizations (API tokens) Authorizations (API tokens) Usage API
  slug: open-influxdata-usage-api
- collection_type: open
  name: InfluxDB Cloud API Service Authorizations (API tokens) Authorizations (API tokens) Users API
  slug: open-influxdata-users-api
- collection_type: open
  name: InfluxDB Cloud API Service Authorizations (API tokens) Authorizations (API tokens) Variables API
  slug: open-influxdata-variables-api
- collection_type: open
  name: InfluxDB Cloud API Service Authorizations (API tokens) Authorizations (API tokens) Views API
  slug: open-influxdata-views-api
- collection_type: open
  name: InfluxDB Cloud API Service Authorizations (API tokens) Authorizations (API tokens) Write API
  slug: open-influxdata-write-api
common:
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/influxdata-capability-edges.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/influxdata-cloud-overlay.yaml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/influxdata-domain-security.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/influxdata-agentic-access.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/influxdata-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://www.influxdata.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.influxdata.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.influxdata.com/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.influxdata.com/influxdb/cloud/api/
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.influxdata.com/influxdb/cloud/get-started/
- group: operate
  title: ''
  type: Support
  url: https://support.influxdata.com/s/
- group: operate
  title: ''
  type: HelpCenter
  url: https://community.influxdata.com/
- group: company
  title: ''
  type: Blog
  url: https://www.influxdata.com/blog/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/influxdata
- group: commercial
  title: ''
  type: Pricing
  url: https://www.influxdata.com/influxdb-pricing/
- group: start
  title: ''
  type: SignUp
  url: https://www.influxdata.com/influxdb-signup/
- group: start
  title: ''
  type: Login
  url: https://cloud2.influxdata.com/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.influxdata.com/legal/terms-of-use/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.influxdata.com/legal/privacy-policy/
- group: build
  title: ''
  type: Packages
  url: packages/influxdata-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/influxdata-packages.yml
- group: build
  title: ''
  type: CLI
  url: cli/influxdata-cli.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/influxdata-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/influxdata-llms.txt
- group: design
  title: ''
  type: Conformance
  url: conformance/influxdata-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: https://www.influxdata.com/security/
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/influxdata-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/influxdata-lifecycle.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://status.influxdata.com/
- group: design
  title: ''
  type: Conventions
  url: conventions/influxdata-conventions.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/influxdata-changelog.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/influxdata-data-model.yml
- group: design
  title: ''
  type: Components
  url: components/influxdata-components.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/influxdata-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: https://www.influxdata.com/how-to-report-security-vulnerabilities/
- group: auth
  title: ''
  type: TrustCenter
  url: https://www.influxdata.com/security/
created: '2026-07-17'
description: InfluxData is the company behind InfluxDB, the leading open source time series database purpose-built for real-time analytics, monitoring, IoT and sensor data, application metrics, and observability workloads. InfluxDB ingests millions of data points per second and ships as open source (InfluxDB OSS), a fully managed multi-cloud service (InfluxDB Cloud), and dedicated/clustered offerings. The platform exposes a REST /api/v2 HTTP API for writing line-protocol data, querying with Flux and InfluxQL/SQL, and managing buckets, organizations, tasks, API tokens, and dashboards, alongside official client libraries, the influx CLI, and the Telegraf collection agent.
image: https://github.com/influxdata.png
layout: provider
mcp_servers:
- description: ''
  name: InfluxData MCP Server
  slug: influxdata-mcp-server
modified: '2026-07-19'
name: InfluxData
nav: Providers
network: true
overview: 'InfluxData publishes 45 APIs on the [APIs.io](https://apis.io/) network, including Authorizations (API tokens) API, Backup API, Bucket Schemas API, and 42 more. Tagged areas include Time Series Database, Database, Monitoring, Observability, and IoT.


  InfluxData''s developer surface includes authentication, documentation, API reference, getting-started guide, support, engineering blog, pricing, and 30 more developer resources.'
random_paper: 1
score:
  band: developing
  composite: 51.2
  coverage:
    artifact_dirs: 21
    catalog_gap: 91.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: -2.4
  facets:
    access_clarity: 60.5
    commercial_clarity: 60.5
    contract_governance: 4.5
    contract_quality: 51.6
    developer_ergonomics: 73.2
    discoverability: 51.9
    governance: 4.5
    operational_transparency: 44.7
  previous_composite: 53.6
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 45
    mcp: derived
    skills: derived
  schema_version: 0.17.2
  scored_at: '2026-08-30'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/influxdata/refs/heads/main/screenshots/influxdata-2026-07-25T222417.png
security:
- kind: authentication
  name: Influxdata Authentication
  slug: influxdata-authentication
  summary_line: apiKey/http · 2 schemes
- kind: domain-security
  name: Influxdata Domain Security
  slug: influxdata-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Influxdata Vulnerability Disclosure
  slug: influxdata-vulnerability-disclosure
  summary_line: contact published
- kind: trust-center
  name: Influxdata Trust Center
  slug: influxdata-trust-center
  summary_line: SOC 2 Type 2, ISO/IEC 27001, ISO/IEC 27018
slug: influxdata
tags:
- Time Series Database
- Database
- Monitoring
- Observability
- IoT
- Metrics
- Analytics
- DevOps
- Real-Time Data
- InfluxDB
- Telegraf
- Company
website: https://www.influxdata.com/
---
