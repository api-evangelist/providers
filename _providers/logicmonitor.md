---
access_model:
  confidence: high
  label: 14-day trial, pricing by quote
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - plans
  trial: true
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
    error_semantics: documented
    event_surface_described: true
    idempotency: false
    mcp_server: documented
    mcp_tool_quality: na
    openapi_examples: partial
    operation_distinctiveness: false
    pagination_ratio: partial
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 33.7
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 230
  human_in_the_loop: 3
  name: Logicmonitor Agentic Access
  operation_count: 411
  slug: logicmonitor-agentic-access
  summary_line: 411 operations · 230 acting · 3 human-in-the-loop
api_count: 2
apis:
- description: A Model Context Protocol server over the LogicMonitor REST API v3, published to npm as logicmonitor-api-mcp and hosted in the LogicMonitor GitHub organization, exposing 13 resource-shaped tools for de
  name: LogicMonitor MCP Server
  slug: logicmonitor-mcp
- baseURL: https://{account}.logicmonitor.com/santaba/rest
  baseurl_source: declared
  description: The Access Group API from LogicMonitor — 4 operation(s) for access group.
  name: LogicMonitor Access Group API
  slug: logicmonitor-access-group-api
- baseURL: https://{account}.logicmonitor.com/santaba/rest
  baseurl_source: declared
  description: The Action Chains API from LogicMonitor — 2 operation(s) for action chains.
  name: LogicMonitor Action Chains API
  slug: logicmonitor-action-chains-api
- baseURL: https://{account}.logicmonitor.com/santaba/rest
  baseurl_source: declared
  description: The Action Rules API from LogicMonitor — 3 operation(s) for action rules.
  name: LogicMonitor Action Rules API
  slug: logicmonitor-action-rules-api
- baseURL: https://{account}.logicmonitor.com/santaba/rest
  baseurl_source: declared
  description: The Alert Rules API from LogicMonitor — 2 operation(s) for alert rules.
  name: LogicMonitor Alert Rules API
  slug: logicmonitor-alert-rules-api
- baseURL: https://{account}.logicmonitor.com/santaba/rest
  baseurl_source: declared
  description: The Alerts API from LogicMonitor — 5 operation(s) for alerts.
  name: LogicMonitor Alerts API
  slug: logicmonitor-alerts-api
- baseURL: https://{account}.logicmonitor.com/santaba/rest
  baseurl_source: declared
  description: The API Tokens API from LogicMonitor — 3 operation(s) for api tokens.
  name: LogicMonitor API Tokens API
  slug: logicmonitor-api-tokens-api
- baseURL: https://{account}.logicmonitor.com/santaba/rest
  baseurl_source: declared
  description: The ApiPerfStats API from LogicMonitor — 1 operation(s) for apiperfstats.
  name: LogicMonitor API Perf Stats API
  slug: logicmonitor-apiperfstats-api
- baseURL: https://{account}.logicmonitor.com/santaba/rest
  baseurl_source: declared
  description: The AppliesToFunctions API from LogicMonitor — 3 operation(s) for appliestofunctions.
  name: LogicMonitor Applies To Functions API
  slug: logicmonitor-appliestofunctions-api
- baseURL: https://{account}.logicmonitor.com/santaba/rest
  baseurl_source: declared
  description: The Audit Logs API from LogicMonitor — 2 operation(s) for audit logs.
  name: LogicMonitor Audit Logs API
  slug: logicmonitor-audit-logs-api
- baseURL: https://{account}.logicmonitor.com/santaba/rest
  baseurl_source: declared
  description: The Automated Diagnostic & Remediation API from LogicMonitor — 2 operation(s) for automated diagnostic & remediation.
  name: LogicMonitor Automated Diagnostic & Remediation API
  slug: logicmonitor-automated-diagnostic-remediation-api
- baseURL: https://{account}.logicmonitor.com/santaba/rest
  baseurl_source: declared
  description: The Collector Groups API from LogicMonitor — 3 operation(s) for collector groups.
  name: LogicMonitor Collector Groups API
  slug: logicmonitor-collector-groups-api
- baseURL: https://{account}.logicmonitor.com/santaba/rest
  baseurl_source: declared
  description: The Collectors API from LogicMonitor — 15 operation(s) for collectors.
  name: LogicMonitor Collectors API
  slug: logicmonitor-collectors-api
- baseURL: https://{account}.logicmonitor.com/santaba/rest
  baseurl_source: declared
  description: The CollectorVersions API from LogicMonitor — 1 operation(s) for collectorversions.
  name: LogicMonitor Collector Versions API
  slug: logicmonitor-collectorversions-api
- baseURL: https://{account}.logicmonitor.com/santaba/rest
  baseurl_source: declared
  description: The ConfigSources API from LogicMonitor — 5 operation(s) for configsources.
  name: LogicMonitor Config Sources API
  slug: logicmonitor-configsources-api
- baseURL: https://{account}.logicmonitor.com/santaba/rest
  baseurl_source: declared
  description: The Cost Optimization Recommendations API from LogicMonitor — 3 operation(s) for cost optimization recommendations.
  name: LogicMonitor Cost Optimization Recommendations API
  slug: logicmonitor-cost-optimization-recommendations-api
- baseURL: https://{account}.logicmonitor.com/santaba/rest
  baseurl_source: declared
  description: The Dashboard Groups API from LogicMonitor — 3 operation(s) for dashboard groups.
  name: LogicMonitor Dashboard Groups API
  slug: logicmonitor-dashboard-groups-api
- baseURL: https://{account}.logicmonitor.com/santaba/rest
  baseurl_source: declared
  description: The Dashboards API from LogicMonitor — 3 operation(s) for dashboards.
  name: LogicMonitor Dashboards API
  slug: logicmonitor-dashboards-api
- baseURL: https://{account}.logicmonitor.com/santaba/rest
  baseurl_source: declared
  description: The Data API from LogicMonitor — 9 operation(s) for data.
  name: LogicMonitor Data API
  slug: logicmonitor-data-api
- baseURL: https://{account}.logicmonitor.com/santaba/rest
  baseurl_source: declared
  description: The Datasource Instances API from LogicMonitor — 13 operation(s) for datasource instances.
  name: LogicMonitor Datasource Instances API
  slug: logicmonitor-datasource-instances-api
- baseURL: https://{account}.logicmonitor.com/santaba/rest
  baseurl_source: declared
  description: The Debug API from LogicMonitor — 2 operation(s) for debug.
  name: LogicMonitor Debug API
  slug: logicmonitor-debug-api
- baseURL: https://{account}.logicmonitor.com/santaba/rest
  baseurl_source: declared
  description: The Delta API from LogicMonitor — 2 operation(s) for delta.
  name: LogicMonitor Delta API
  slug: logicmonitor-delta-api
- baseURL: https://{account}.logicmonitor.com/santaba/rest
  baseurl_source: declared
  description: The Device Groups API from LogicMonitor — 19 operation(s) for device groups.
  name: LogicMonitor Device Groups API
  slug: logicmonitor-device-groups-api
- baseURL: https://{account}.logicmonitor.com/santaba/rest
  baseurl_source: declared
  description: The Devices API from LogicMonitor — 20 operation(s) for devices.
  name: LogicMonitor Devices API
  slug: logicmonitor-devices-api
- baseURL: https://{account}.logicmonitor.com/santaba/rest
  baseurl_source: declared
  description: The DiagnosticSources API from LogicMonitor — 4 operation(s) for diagnosticsources.
  name: LogicMonitor Diagnostic Sources API
  slug: logicmonitor-diagnosticsources-api
- baseURL: https://{account}.logicmonitor.com/santaba/rest
  baseurl_source: declared
  description: The DNS Mapping API from LogicMonitor — 1 operation(s) for dns mapping.
  name: LogicMonitor DNS Mapping API
  slug: logicmonitor-dns-mapping-api
- baseURL: https://{account}.logicmonitor.com/santaba/rest
  baseurl_source: declared
  description: The DNSMappings API from LogicMonitor — 1 operation(s) for dnsmappings.
  name: LogicMonitor DNS Mappings API
  slug: logicmonitor-dnsmappings-api
- baseURL: https://{account}.logicmonitor.com/santaba/rest
  baseurl_source: declared
  description: The Escalation Chains API from LogicMonitor — 2 operation(s) for escalation chains.
  name: LogicMonitor Escalation Chains API
  slug: logicmonitor-escalation-chains-api
- baseURL: https://{account}.logicmonitor.com/santaba/rest
  baseurl_source: declared
  description: The IntegrationAuditLogs API from LogicMonitor — 1 operation(s) for integrationauditlogs.
  name: LogicMonitor Integration Audit Logs API
  slug: logicmonitor-integrationauditlogs-api
- baseURL: https://{account}.logicmonitor.com/santaba/rest
  baseurl_source: declared
  description: The JobMonitor API from LogicMonitor — 4 operation(s) for jobmonitor.
  name: LogicMonitor Job Monitor API
  slug: logicmonitor-jobmonitor-api
- baseURL: https://{account}.logicmonitor.com/santaba/rest
  baseurl_source: declared
  description: The LogAlertGroups API from LogicMonitor — 2 operation(s) for logalertgroups.
  name: LogicMonitor Log Alert Groups API
  slug: logicmonitor-logalertgroups-api
- baseURL: https://{account}.logicmonitor.com/santaba/rest
  baseurl_source: declared
  description: The LogAlerts API from LogicMonitor — 3 operation(s) for logalerts.
  name: LogicMonitor Log Alerts API
  slug: logicmonitor-logalerts-api
- baseURL: https://{account}.logicmonitor.com/santaba/rest
  baseurl_source: declared
  description: The LogicModules API from LogicMonitor — 1 operation(s) for logicmodules.
  name: LogicMonitor Logic Modules API
  slug: logicmonitor-logicmodules-api
- baseURL: https://{account}.logicmonitor.com/santaba/rest
  baseurl_source: declared
  description: The LogPartitions API from LogicMonitor — 4 operation(s) for logpartitions.
  name: LogicMonitor Log Partitions API
  slug: logicmonitor-logpartitions-api
- baseURL: https://{account}.logicmonitor.com/santaba/rest
  baseurl_source: declared
  description: The LogQueryGroups API from LogicMonitor — 6 operation(s) for logquerygroups.
  name: LogicMonitor Log Query Groups API
  slug: logicmonitor-logquerygroups-api
- baseURL: https://{account}.logicmonitor.com/santaba/rest
  baseurl_source: declared
  description: The Metrics API from LogicMonitor — 2 operation(s) for metrics.
  name: LogicMonitor Metrics API
  slug: logicmonitor-metrics-api
- baseURL: https://{account}.logicmonitor.com/santaba/rest
  baseurl_source: declared
  description: The Netscans API from LogicMonitor — 2 operation(s) for netscans.
  name: LogicMonitor Netscans API
  slug: logicmonitor-netscans-api
- baseURL: https://{account}.logicmonitor.com/santaba/rest
  baseurl_source: declared
  description: The OID API from LogicMonitor — 3 operation(s) for oid.
  name: LogicMonitor OID API
  slug: logicmonitor-oid-api
- baseURL: https://{account}.logicmonitor.com/santaba/rest
  baseurl_source: declared
  description: The Ops Notes API from LogicMonitor — 2 operation(s) for ops notes.
  name: LogicMonitor Ops Notes API
  slug: logicmonitor-ops-notes-api
- baseURL: https://{account}.logicmonitor.com/santaba/rest
  baseurl_source: declared
  description: The PropertySource API from LogicMonitor — 3 operation(s) for propertysource.
  name: LogicMonitor Property Source API
  slug: logicmonitor-propertysource-api
- baseURL: https://{account}.logicmonitor.com/santaba/rest
  baseurl_source: declared
  description: The Recipient Groups API from LogicMonitor — 2 operation(s) for recipient groups.
  name: LogicMonitor Recipient Groups API
  slug: logicmonitor-recipient-groups-api
- baseURL: https://{account}.logicmonitor.com/santaba/rest
  baseurl_source: declared
  description: The RemediationSources API from LogicMonitor — 3 operation(s) for remediationsources.
  name: LogicMonitor Remediation Sources API
  slug: logicmonitor-remediationsources-api
- baseURL: https://{account}.logicmonitor.com/santaba/rest
  baseurl_source: declared
  description: The Report API from LogicMonitor — 4 operation(s) for report.
  name: LogicMonitor Report API
  slug: logicmonitor-report-api
- baseURL: https://{account}.logicmonitor.com/santaba/rest
  baseurl_source: declared
  description: The Report Groups API from LogicMonitor — 2 operation(s) for report groups.
  name: LogicMonitor Report Groups API
  slug: logicmonitor-report-groups-api
- baseURL: https://{account}.logicmonitor.com/santaba/rest
  baseurl_source: declared
  description: The Roles API from LogicMonitor — 2 operation(s) for roles.
  name: LogicMonitor Roles API
  slug: logicmonitor-roles-api
- baseURL: https://{account}.logicmonitor.com/santaba/rest
  baseurl_source: declared
  description: The SDTs API from LogicMonitor — 2 operation(s) for sdts.
  name: LogicMonitor SD Ts API
  slug: logicmonitor-sdts-api
- baseURL: https://{account}.logicmonitor.com/santaba/rest
  baseurl_source: declared
  description: The Thresholds API from LogicMonitor — 5 operation(s) for thresholds.
  name: LogicMonitor Thresholds API
  slug: logicmonitor-thresholds-api
- baseURL: https://{account}.logicmonitor.com/santaba/rest
  baseurl_source: declared
  description: The TopologySource API from LogicMonitor — 3 operation(s) for topologysource.
  name: LogicMonitor Topology Source API
  slug: logicmonitor-topologysource-api
- baseURL: https://{account}.logicmonitor.com/santaba/rest
  baseurl_source: declared
  description: The TrackQueryGroup API from LogicMonitor — 2 operation(s) for trackquerygroup.
  name: LogicMonitor Track Query Group API
  slug: logicmonitor-trackquerygroup-api
- baseURL: https://{account}.logicmonitor.com/santaba/rest
  baseurl_source: declared
  description: The Usage API V3 API from LogicMonitor — 2 operation(s) for usage api v3.
  name: LogicMonitor Usage API V3 API
  slug: logicmonitor-usage-api-v3-api
- baseURL: https://{account}.logicmonitor.com/santaba/rest
  baseurl_source: declared
  description: The Users API from LogicMonitor — 2 operation(s) for users.
  name: LogicMonitor Users API
  slug: logicmonitor-users-api
- baseURL: https://{account}.logicmonitor.com/santaba/rest
  baseurl_source: declared
  description: The Website Groups API from LogicMonitor — 5 operation(s) for website groups.
  name: LogicMonitor Website Groups API
  slug: logicmonitor-website-groups-api
- baseURL: https://{account}.logicmonitor.com/santaba/rest
  baseurl_source: declared
  description: The Websites API from LogicMonitor — 9 operation(s) for websites.
  name: LogicMonitor Websites API
  slug: logicmonitor-websites-api
- baseURL: https://{account}.logicmonitor.com/santaba/rest
  baseurl_source: declared
  description: The Widgets API from LogicMonitor — 2 operation(s) for widgets.
  name: LogicMonitor Widgets API
  slug: logicmonitor-widgets-api
- baseURL: https://{account}.logicmonitor.com/santaba/rest
  baseurl_source: declared
  description: The Batch Jobs API from LogicMonitor — 1 operation(s) for batch jobs.
  name: LogicMonitor Batch Jobs API
  slug: logicmonitor-batch-jobs-api
- baseURL: https://{account}.logicmonitor.com/santaba/rest
  baseurl_source: declared
  description: The Data Sources API from LogicMonitor — 8 operation(s) for data sources.
  name: LogicMonitor Data Sources API
  slug: logicmonitor-data-sources-api
- baseURL: https://{account}.logicmonitor.com/santaba/rest
  baseurl_source: declared
  description: The Event Sources API from LogicMonitor — 4 operation(s) for event sources.
  name: LogicMonitor Event Sources API
  slug: logicmonitor-event-sources-api
- baseURL: https://{account}.logicmonitor.com/santaba/rest
  baseurl_source: declared
  description: The Log Sources API from LogicMonitor — 3 operation(s) for log sources.
  name: LogicMonitor Log Sources API
  slug: logicmonitor-log-sources-api
- baseURL: https://{account}.logicmonitor.com/santaba/rest
  baseurl_source: declared
  description: The User Data API from LogicMonitor — 1 operation(s) for user data.
  name: LogicMonitor User Data API
  slug: logicmonitor-user-data-api
artifact_total: 219
asyncapis:
- description: ''
  name: Logicmonitor Webhooks
  slug: logicmonitor-webhooks
common:
- group: agent
  href: https://artifacts.apis.io/logicmonitor/agentic-access/logicmonitor-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/logicmonitor-agentic-access.yml
- group: commercial
  href: https://artifacts.apis.io/logicmonitor/finops/logicmonitor-finops.yml
  title: ''
  type: FinOps
  url: finops/logicmonitor-finops.yml
- group: design
  href: https://artifacts.apis.io/logicmonitor/rules/logicmonitor-rules.yml
  title: ''
  type: Spectral
  url: rules/logicmonitor-rules.yml
- group: design
  href: https://artifacts.apis.io/logicmonitor/json-ld/logicmonitor-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/logicmonitor-context.jsonld
- group: design
  href: https://artifacts.apis.io/logicmonitor/vocabulary/logicmonitor-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/logicmonitor-vocabulary.yml
- group: auth
  href: https://artifacts.apis.io/logicmonitor/scopes/logicmonitor-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/logicmonitor-scopes.yml
- group: operate
  title: ''
  type: Deprecation
  url: https://www.logicmonitor.com/support/migration-from-logicmonitor-rest-api-v1-to-api-v3
- group: other
  href: https://artifacts.apis.io/logicmonitor/hosts/logicmonitor-hosts.yml
  title: ''
  type: Hosts
  url: hosts/logicmonitor-hosts.yml
- group: other
  href: https://artifacts.apis.io/logicmonitor/vendors/logicmonitor-vendors.yml
  title: ''
  type: Vendors
  url: vendors/logicmonitor-vendors.yml
- group: auth
  title: ''
  type: Security
  url: https://www.logicmonitor.com/security
- group: company
  title: ''
  type: Newsroom
  url: https://www.logicmonitor.com/press
- group: other
  title: ''
  type: Leadership
  url: https://www.logicmonitor.com/leadership
- group: other
  href: https://artifacts.apis.io/logicmonitor/overlays/logicmonitor-rest-api-v3-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/logicmonitor-rest-api-v3-overlay.yaml
- group: commercial
  title: ''
  type: License
  url: https://github.com/logicmonitor/logicmonitor-api-mcp/blob/main/LICENSE
- group: company
  title: ''
  type: Website
  url: https://www.logicmonitor.com
- group: docs
  title: ''
  type: Documentation
  url: https://www.logicmonitor.com/support
- group: start
  title: ''
  type: DeveloperPortal
  url: https://www.logicmonitor.com/support/rest-api-developers-guide/
- group: docs
  title: ''
  type: APIReference
  url: https://www.logicmonitor.com/support/rest-api-v3-swagger-documentation
- group: start
  title: ''
  type: GettingStarted
  url: https://www.logicmonitor.com/support/rest-api-developers-guide/overview/using-logicmonitors-rest-api
- group: operate
  title: ''
  type: Support
  url: https://www.logicmonitor.com/support
- group: operate
  title: ''
  type: Community
  url: https://community.logicmonitor.com/
- group: company
  title: ''
  type: Blog
  url: https://www.logicmonitor.com/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/logicmonitor
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/logicmonitor
- group: commercial
  title: ''
  type: Pricing
  url: https://www.logicmonitor.com/pricing
- group: start
  title: ''
  type: SignUp
  url: https://www.logicmonitor.com/signup
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.logicmonitor.com/legal/terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.logicmonitor.com/legal/privacy-policy
- group: operate
  title: ''
  type: StatusPage
  url: https://status.logicmonitor.com/
- group: operate
  href: https://artifacts.apis.io/logicmonitor/changelog/logicmonitor-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/logicmonitor-changelog.yml
- group: design
  href: https://artifacts.apis.io/logicmonitor/lifecycle/logicmonitor-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/logicmonitor-lifecycle.yml
- group: commercial
  href: https://artifacts.apis.io/logicmonitor/plans/logicmonitor-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/logicmonitor-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/logicmonitor/rate-limits/logicmonitor-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/logicmonitor-rate-limits.yml
- group: build
  href: https://artifacts.apis.io/logicmonitor/packages/logicmonitor-packages.yml
  title: ''
  type: Packages
  url: packages/logicmonitor-packages.yml
- group: build
  href: https://artifacts.apis.io/logicmonitor/packages/logicmonitor-packages.yml
  title: ''
  type: SDKs
  url: packages/logicmonitor-packages.yml
- group: build
  href: https://artifacts.apis.io/logicmonitor/cli/logicmonitor-cli.yml
  title: ''
  type: CLI
  url: cli/logicmonitor-cli.yml
- group: design
  href: https://artifacts.apis.io/logicmonitor/conformance/logicmonitor-conformance.yml
  title: ''
  type: Conformance
  url: conformance/logicmonitor-conformance.yml
- group: auth
  href: https://artifacts.apis.io/logicmonitor/security/logicmonitor-trust-center.yml
  title: ''
  type: Compliance
  url: security/logicmonitor-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/logicmonitor/security/logicmonitor-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/logicmonitor-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/logicmonitor/security/logicmonitor-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/logicmonitor-domain-security.yml
- group: auth
  href: https://artifacts.apis.io/logicmonitor/authentication/logicmonitor-authentication.yml
  title: ''
  type: Authentication
  url: authentication/logicmonitor-authentication.yml
- group: agent
  href: https://artifacts.apis.io/logicmonitor/llms/logicmonitor-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/logicmonitor-llms.txt
- group: agent
  href: https://artifacts.apis.io/logicmonitor/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/logicmonitor/asyncapi/logicmonitor-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/logicmonitor-webhooks.yml
- group: other
  href: https://artifacts.apis.io/logicmonitor/capabilities/logicmonitor-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/logicmonitor-capability-edges.yml
created: '2026-03-27'
description: LogicMonitor is an AI-powered hybrid observability and AIOps platform that monitors infrastructure, cloud and multi-cloud estates, containers, networks, databases, storage, logs, traces, websites and internet performance from a single SaaS portal, with an agentic AIOps layer (Edwin AI) for event correlation and governed remediation. Everything the portal does is addressable through the LogicMonitor REST API v3 — a published Swagger 2.0 contract of 220 paths and 403 operations covering devices, device groups, collectors, alerts, scheduled downtime, dashboards, websites, reports, log pipelines, cost optimization and user administration, with per-operation x-minimum-permissions metadata. First-party Python, Go, PowerShell and Terraform tooling wraps it, and telemetry can be pushed in over OpenTelemetry OTLP, OpenMetrics/Prometheus exposition, and the Push Metrics and LM Logs ingestion APIs.
finops:
- has_sources: true
  method: derived
  name: Logicmonitor Finops
  primary_unit: hybrid unit
  service_category: ''
  slug: logicmonitor-finops
  template: false
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/logicmonitor.png
json_schemas:
- name: AccessGroupPaginationResponse
  property_count: 1
  slug: logicmonitor-access-group-pagination-response
- name: AccessGroup
  property_count: 7
  slug: logicmonitor-access-group
- name: AccessLogPaginationResponse
  property_count: 3
  slug: logicmonitor-access-log-pagination-response
- name: ActionChainPaginationResponse
  property_count: 1
  slug: logicmonitor-action-chain-pagination-response
- name: ActionChain
  property_count: 4
  slug: logicmonitor-action-chain
- name: ActionRulePaginationResponse
  property_count: 1
  slug: logicmonitor-action-rule-pagination-response
- name: ActionRule
  property_count: 12
  slug: logicmonitor-action-rule
- name: ActionRuleStatus
  property_count: 1
  slug: logicmonitor-action-rule-status
- name: AdminPaginationResponse
  property_count: 3
  slug: logicmonitor-admin-pagination-response
- name: Admin
  property_count: 27
  slug: logicmonitor-admin
- name: AdrOutputList
  property_count: 5
  slug: logicmonitor-adr-output-list
- name: AlertAck
  property_count: 1
  slug: logicmonitor-alert-ack
- name: AlertPaginationResponse
  property_count: 3
  slug: logicmonitor-alert-pagination-response
- name: AlertRulePaginationResponse
  property_count: 3
  slug: logicmonitor-alert-rule-pagination-response
- name: AlertRule
  property_count: 14
  slug: logicmonitor-alert-rule
- name: Alert
  property_count: 41
  slug: logicmonitor-alert
- name: ApiPerfMetrics
  property_count: 8
  slug: logicmonitor-api-perf-metrics
- name: ApiTokenPaginationResponse
  property_count: 3
  slug: logicmonitor-api-token-pagination-response
- name: APIToken
  property_count: 11
  slug: logicmonitor-apitoken
- name: AppliesToFunction_2
  property_count: 11
  slug: logicmonitor-applies-to-function-2
- name: AppliesToFunction
  property_count: 4
  slug: logicmonitor-applies-to-function
- name: AuditLog
  property_count: 6
  slug: logicmonitor-audit-log
- name: BatchJobPaginationResponse
  property_count: 3
  slug: logicmonitor-batch-job-pagination-response
- name: BatchJob
  property_count: 23
  slug: logicmonitor-batch-job
- name: CollectorGroupPaginationResponse
  property_count: 3
  slug: logicmonitor-collector-group-pagination-response
- name: CollectorGroup
  property_count: 10
  slug: logicmonitor-collector-group
- name: CollectorPaginationResponse
  property_count: 3
  slug: logicmonitor-collector-pagination-response
- name: Collector
  property_count: 63
  slug: logicmonitor-collector
- name: CollectorVersionPaginationResponse
  property_count: 3
  slug: logicmonitor-collector-version-pagination-response
- name: CompanyMetricsSummary
  property_count: 43
  slug: logicmonitor-company-metrics-summary
- name: ConfigSource
  property_count: 27
  slug: logicmonitor-config-source
- name: ConfigSourceUpdateReasonsPaginationResponse
  property_count: 3
  slug: logicmonitor-config-source-update-reasons-pagination-response
- name: ConfigsourcePaginationResponse
  property_count: 3
  slug: logicmonitor-configsource-pagination-response
- name: DashboardGroup_2
  property_count: 12
  slug: logicmonitor-dashboard-group-2
- name: DashboardGroupPaginationResponse
  property_count: 3
  slug: logicmonitor-dashboard-group-pagination-response
- name: DashboardGroup
  property_count: 12
  slug: logicmonitor-dashboard-group
- name: DashboardPaginationResponse
  property_count: 3
  slug: logicmonitor-dashboard-pagination-response
- name: Dashboard
  property_count: 13
  slug: logicmonitor-dashboard
- name: DataSource_2
  property_count: 30
  slug: logicmonitor-data-source-2
- name: DataSourceOverviewGraph
  property_count: 16
  slug: logicmonitor-data-source-overview-graph
- name: DataSource
  property_count: 20
  slug: logicmonitor-data-source
- name: DataSourceUpdateReasonsPaginationResponse
  property_count: 3
  slug: logicmonitor-data-source-update-reasons-pagination-response
- name: DatasourceOverviewGraphPaginationResponse
  property_count: 3
  slug: logicmonitor-datasource-overview-graph-pagination-response
- name: Debug
  property_count: 4
  slug: logicmonitor-debug
- name: DeviceClusterAlertConfigPaginationResponse
  property_count: 3
  slug: logicmonitor-device-cluster-alert-config-pagination-response
- name: DeviceClusterAlertConfig
  property_count: 12
  slug: logicmonitor-device-cluster-alert-config
- name: DeviceDataSourceAssociatedPaginationResponse
  property_count: 3
  slug: logicmonitor-device-data-source-associated-pagination-response
- name: DeviceDataSourceData
  property_count: 4
  slug: logicmonitor-device-data-source-data
- name: DeviceDataSourceInstanceAlertSettingPaginationResponse
  property_count: 1
  slug: logicmonitor-device-data-source-instance-alert-setting-pagination-response
- name: DeviceDataSourceInstanceAlertSetting
  property_count: 17
  slug: logicmonitor-device-data-source-instance-alert-setting
- name: DeviceDataSourceInstanceConfig_2
  property_count: 18
  slug: logicmonitor-device-data-source-instance-config-2
- name: DeviceDataSourceInstanceConfig
  property_count: 16
  slug: logicmonitor-device-data-source-instance-config
- name: DeviceDataSourceInstanceData
  property_count: 4
  slug: logicmonitor-device-data-source-instance-data
- name: DeviceDataSourceInstanceGroup
  property_count: 7
  slug: logicmonitor-device-data-source-instance-group
- name: DeviceDataSourceInstance
  property_count: 20
  slug: logicmonitor-device-data-source-instance
- name: DeviceDataSource
  property_count: 31
  slug: logicmonitor-device-data-source
- name: DeviceDatasourceInstancePaginationResponse
  property_count: 3
  slug: logicmonitor-device-datasource-instance-pagination-response
- name: DeviceDeltaPaginationResponse
  property_count: 4
  slug: logicmonitor-device-delta-pagination-response
- name: DeviceGroupDataSourceAlertConfig
  property_count: 2
  slug: logicmonitor-device-group-data-source-alert-config
- name: DeviceGroupDataSource
  property_count: 8
  slug: logicmonitor-device-group-data-source
- name: DeviceGroup
  property_count: 34
  slug: logicmonitor-device-group
- name: DeviceInstanceDataPaginationResponse
  property_count: 3
  slug: logicmonitor-device-instance-data-pagination-response
- name: DeviceInstances
  property_count: 1
  slug: logicmonitor-device-instances
- name: Device
  property_count: 39
  slug: logicmonitor-device
- name: DiagnosticRemediationAssignedSource
  property_count: 6
  slug: logicmonitor-diagnostic-remediation-assigned-source
- name: DiagnosticsSourceExecution
  property_count: 9
  slug: logicmonitor-diagnostics-source-execution
- name: DiagnosticsSource
  property_count: 19
  slug: logicmonitor-diagnostics-source
- name: DiagnosticsourcePaginationResponse
  property_count: 1
  slug: logicmonitor-diagnosticsource-pagination-response
- name: DisableProcessorPayload
  property_count: 1
  slug: logicmonitor-disable-processor-payload
- name: EntityProperty
  property_count: 4
  slug: logicmonitor-entity-property
- name: EscalatingChain
  property_count: 9
  slug: logicmonitor-escalating-chain
- name: EscalationChainPaginationResponse
  property_count: 3
  slug: logicmonitor-escalation-chain-pagination-response
- name: EventSource_2
  property_count: 26
  slug: logicmonitor-event-source-2
- name: EventSourcePaginationResponse
  property_count: 3
  slug: logicmonitor-event-source-pagination-response
- name: GenerateReportRequest
  property_count: 3
  slug: logicmonitor-generate-report-request
- name: GenerateReportResult
  property_count: 3
  slug: logicmonitor-generate-report-result
- name: GraphPlot
  property_count: 29
  slug: logicmonitor-graph-plot
- name: IntegrationAuditLogPaginationResponse
  property_count: 1
  slug: logicmonitor-integration-audit-log-pagination-response
- name: LogPartition
  property_count: 14
  slug: logicmonitor-log-partition
- name: LogQueryGroupPaginationResponse
  property_count: 3
  slug: logicmonitor-log-query-group-pagination-response
- name: LogQueryGroup
  property_count: 8
  slug: logicmonitor-log-query-group
- name: LogSourcePaginationResponse
  property_count: 3
  slug: logicmonitor-log-source-pagination-response
- name: LogSource
  property_count: 22
  slug: logicmonitor-log-source
- name: NetscanPaginationResponse
  property_count: 3
  slug: logicmonitor-netscan-pagination-response
- name: Netscan
  property_count: 17
  slug: logicmonitor-netscan
- name: OidSourcePaginationResponse
  property_count: 3
  slug: logicmonitor-oid-source-pagination-response
- name: OpsNotePaginationResponse
  property_count: 3
  slug: logicmonitor-ops-note-pagination-response
- name: OpsNote
  property_count: 6
  slug: logicmonitor-ops-note
- name: Pagination
  property_count: 4
  slug: logicmonitor-pagination
- name: PipelinePaginationResponse
  property_count: 3
  slug: logicmonitor-pipeline-pagination-response
- name: PipelineProcessorPaginationResponse
  property_count: 3
  slug: logicmonitor-pipeline-processor-pagination-response
- name: PropertyPaginationResponse
  property_count: 3
  slug: logicmonitor-property-pagination-response
- name: PropertyRulePaginationResponse
  property_count: 3
  slug: logicmonitor-property-rule-pagination-response
- name: PropertyRule
  property_count: 26
  slug: logicmonitor-property-rule
- name: RecipientGroupPaginationResponse
  property_count: 3
  slug: logicmonitor-recipient-group-pagination-response
- name: RecipientGroup
  property_count: 4
  slug: logicmonitor-recipient-group
- name: RemediationSourceExecution
  property_count: 9
  slug: logicmonitor-remediation-source-execution
- name: RemediationSourcePaginationResponse
  property_count: 1
  slug: logicmonitor-remediation-source-pagination-response
- name: RemediationSource
  property_count: 19
  slug: logicmonitor-remediation-source
- name: ReportBase
  property_count: 21
  slug: logicmonitor-report-base
- name: ReportGroupPaginationResponse
  property_count: 3
  slug: logicmonitor-report-group-pagination-response
- name: ReportGroup
  property_count: 6
  slug: logicmonitor-report-group
- name: ReportPaginationResponse
  property_count: 3
  slug: logicmonitor-report-pagination-response
- name: Response
  property_count: 4
  slug: logicmonitor-response
- name: RestAppliesToFunctionPaginationResponse
  property_count: 3
  slug: logicmonitor-rest-applies-to-function-pagination-response
- name: RestCloudRecommendationCategoryV3
  property_count: 2
  slug: logicmonitor-rest-cloud-recommendation-category-v3
- name: RestCloudRecommendationV3
  property_count: 16
  slug: logicmonitor-rest-cloud-recommendation-v3
- name: RestCollectorEventV3
  property_count: 9
  slug: logicmonitor-rest-collector-event-v3
- name: RestCollectorLogFileV3
  property_count: 5
  slug: logicmonitor-rest-collector-log-file-v3
- name: RestCollectorSizingRequestV3
  property_count: 5
  slug: logicmonitor-rest-collector-sizing-request-v3
- name: RestCollectorSizingResponseV3
  property_count: 4
  slug: logicmonitor-rest-collector-sizing-response-v3
- name: RestCollectorStatusV3
  property_count: 8
  slug: logicmonitor-rest-collector-status-v3
- name: RestContractInfoBaseV3
  property_count: 11
  slug: logicmonitor-rest-contract-info-base-v3
- name: RestDashboardGroupAsyncCloneResponse
  property_count: 1
  slug: logicmonitor-rest-dashboard-group-async-clone-response
- name: RestDeviceInstanceGroupAlertConfigV3
  property_count: 14
  slug: logicmonitor-rest-device-instance-group-alert-config-v3
- name: RestDiagnosticSourceV4
  property_count: 54
  slug: logicmonitor-rest-diagnostic-source-v4
- name: RestDNSMappingV3
  property_count: 6
  slug: logicmonitor-rest-dnsmapping-v3
- name: RestLogPipelineProcessorV3
  property_count: 13
  slug: logicmonitor-rest-log-pipeline-processor-v3
- name: RestLogPipelineV3
  property_count: 5
  slug: logicmonitor-rest-log-pipeline-v3
- name: RestLogQueryGroupImportResult
  property_count: 5
  slug: logicmonitor-rest-log-query-group-import-result
- name: RestLogQueryGroupValidationRequestItemV4
  property_count: 3
  slug: logicmonitor-rest-log-query-group-validation-request-item-v4
- name: RestMapModuleV3
  property_count: 3
  slug: logicmonitor-rest-map-module-v3
- name: RestOidV3
  property_count: 10
  slug: logicmonitor-rest-oid-v3
- name: RestResponse
  property_count: 9
  slug: logicmonitor-rest-response
- name: RestUserCustomizedDataV3
  property_count: 2
  slug: logicmonitor-rest-user-customized-data-v3
- name: RolePaginationResponse
  property_count: 3
  slug: logicmonitor-role-pagination-response
- name: Role
  property_count: 11
  slug: logicmonitor-role
- name: SDT
  property_count: 19
  slug: logicmonitor-sdt
- name: SDTPaginationResponse
  property_count: 3
  slug: logicmonitor-sdtpagination-response
- name: SiteMonitorCheckPointPaginationResponse
  property_count: 3
  slug: logicmonitor-site-monitor-check-point-pagination-response
- name: TopologySourcePaginationResponse
  property_count: 3
  slug: logicmonitor-topology-source-pagination-response
- name: TopologySource
  property_count: 19
  slug: logicmonitor-topology-source
- name: TrackQueryGroupPaginationResponse
  property_count: 3
  slug: logicmonitor-track-query-group-pagination-response
- name: TrackedQueryGroup
  property_count: 6
  slug: logicmonitor-tracked-query-group
- name: Usage
  property_count: 18
  slug: logicmonitor-usage
- name: WebsiteCheckpointRawData
  property_count: 3
  slug: logicmonitor-website-checkpoint-raw-data
- name: WebsiteGroupPaginationResponse
  property_count: 3
  slug: logicmonitor-website-group-pagination-response
- name: WebsiteGroup
  property_count: 14
  slug: logicmonitor-website-group
- name: WebsiteGroupSDTHistoryPaginationResponse
  property_count: 3
  slug: logicmonitor-website-group-sdthistory-pagination-response
- name: WebsitePaginationResponse
  property_count: 3
  slug: logicmonitor-website-pagination-response
- name: Website
  property_count: 27
  slug: logicmonitor-website
- name: WebsiteSDTHistoryPaginationResponse
  property_count: 3
  slug: logicmonitor-website-sdthistory-pagination-response
- name: WidgetPaginationResponse
  property_count: 3
  slug: logicmonitor-widget-pagination-response
- name: Widget
  property_count: 11
  slug: logicmonitor-widget
jsonld:
- class_count: 120
  name: Logicmonitor Context
  property_count: 509
  slug: logicmonitor-context
layout: provider
mcp_servers:
- description: 'An MCP server over the LogicMonitor REST API v3, published to npm as logicmonitor-api-mcp and hosted in the logicmonitor GitHub organization. It is NOT a vendor-hosted remote endpoint: there is no URL'
  name: LogicMonitor MCP Server
  slug: logicmonitor-mcp-server
modified: '2026-08-29'
name: LogicMonitor
nav: Providers
network: true
overview: 'LogicMonitor publishes 59 API contracts indexed on the [APIs.io](https://apis.io/) network, including Access Group API, Action Chains API, Action Rules API, and 56 more. Tagged areas include AIOps, Monitoring, Observability, Infrastructure, and Log Management.


  The LogicMonitor catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 1 Spectral governance ruleset.


  LogicMonitor''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, pricing, signup flow, and 38 more developer resources.'
plans:
- name: Logicmonitor Plans Pricing
  plan_count: 3
  slug: logicmonitor-plans-pricing
random_paper: 6
rate_limits:
- limit_count: 20
  name: Logicmonitor Rate Limits
  slug: logicmonitor-rate-limits
rules:
- authorship: generated
  effective_rule_count: 54
  extends:
  - spectral:oas
  name: LogicMonitor API Rules
  rule_count: 13
  severity_counts:
    error: 10
    hint: 0
    info: 1
    warn: 2
  slug: logicmonitor-rules
scopes:
- name: Logicmonitor Scopes
  scope_count: 0
  slug: logicmonitor-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: exemplar
  composite: 79.1
  coverage:
    artifact_dirs: 35
    catalog_earned: 84.8
    catalog_earned_first_party: 24.0
    catalog_gap: 30.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -1.4
  facets:
    access_clarity: 100.0
    contract_governance: 35.6
    contract_quality: 69.0
    developer_ergonomics: 73.2
    discoverability: 65.0
    operational_transparency: 82.9
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - united-states
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
  previous_composite: 80.5
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 58
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 39.2
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 27.8
screenshot: https://apis.io/screenshots/logicmonitor/logicmonitor-2026-06-20T184653.png
security:
- kind: authentication
  name: Logicmonitor Authentication
  slug: logicmonitor-authentication
  summary_line: 3 schemes
- kind: domain-security
  name: Logicmonitor Domain Security
  slug: logicmonitor-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Logicmonitor Trust Center
  slug: logicmonitor-trust-center
  summary_line: SOC 2, ISO 27001, ISO 27017, ISO 27018, HIPAA, FedRAMP, GDPR
skill_count: 4
skills:
- name: logicmonitor-onboard-a-device
  slug: logicmonitor-onboard-a-device
- name: logicmonitor-pull-performance-data
  slug: logicmonitor-pull-performance-data
- name: logicmonitor-schedule-maintenance
  slug: logicmonitor-schedule-maintenance
- name: logicmonitor-triage-alerts
  slug: logicmonitor-triage-alerts
slug: logicmonitor
tags:
- AIOps
- Monitoring
- Observability
- Infrastructure
- Log Management
- Network Monitoring
- Cloud Monitoring
- Alerting
- Synthetic Monitoring
- OpenTelemetry
- ITOps
website: https://www.logicmonitor.com
---
