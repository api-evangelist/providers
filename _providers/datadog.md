---
access_model:
  confidence: medium
  gated: none
  gated_source:
  - onboarding
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  - security
  trial: false
  try_now: true
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    mcp_tool_quality: na
    openapi_examples: partial
    operation_distinctiveness: distinct
    pagination_ratio: false
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 49.6
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 299
  human_in_the_loop: 4
  name: Datadog Agentic Access
  operation_count: 542
  slug: datadog-agentic-access
  summary_line: 542 operations · 299 acting · 4 human-in-the-loop
api_count: 6
apis:
- baseURL: https://api.datadoghq.com
  baseurl_source: declared
  description: The Dashboards API allows you to create, update, delete, and retrieve dashboards and dashboard lists. It also supports organizing, finding, and sharing dashboards with your team and organization.
  name: Datadog Dashboards API
  phrasing_intents:
  - id: DeleteDashboardListItems
    intent: Remove dashboards from a dashboard list
    question: Can I take dashboards out of a list without deleting them?
  - id: GetDashboardListItems
    intent: Get dashboards in a dashboard list
    question: Which dashboards are in a given dashboard list?
  - id: UpdateDashboardListItems
    intent: Replace the dashboards in a dashboard list
    question: Can I set exactly which dashboards a list contains?
  phrasing_ops: 3
  slug: datadog-dashboards-api
- description: The Synthetics API allows you to manage API tests and browser tests programmatically. Datadog Synthetics uses simulated user requests and browser rendering to help ensure uptime, identify regional iss
  name: Datadog Synthetics API
  slug: datadog-synthetics-api
- description: The Service Level Objectives API provides a framework for defining clear targets around application performance. SLOs help teams provide a consistent customer experience, balance feature development w
  name: Datadog Service Level Objectives API
  slug: datadog-service-level-objectives-api
- description: The Security Monitoring API allows you to create and manage security rules, signals, and filters. It provides programmatic access to Datadog Cloud SIEM capabilities for threat detection and security s
  name: Datadog Security Monitoring API
  slug: datadog-security-monitoring-api
- description: The Service Definition API allows you to create, update, retrieve, and delete service definitions in the Datadog Service Catalog. It supports the v2.2 schema and earlier; for v3.0 schema use the Softw
  name: Datadog Service Definition API
  slug: datadog-service-definition-api
- description: The Software Catalog API allows you to create, update, retrieve, and delete Software Catalog entities using the v3.0 schema. It provides a unified catalog for tracking ownership, reliability, and perf
  name: Datadog Software Catalog API
  slug: datadog-software-catalog-api
- description: The Users API allows you to create, edit, and disable users within your Datadog organization. It supports role assignment and user management for access control purposes.
  name: Datadog Users API
  slug: datadog-users-api
- description: The Roles API is used to create and manage Datadog roles, the global permissions they grant, and which users belong to them. Roles provide role-based access control for Datadog resources and features.
  name: Datadog Roles API
  slug: datadog-roles-api
- description: The Key Management API allows you to manage your Datadog API and application keys. It provides endpoints to create, list, update, and delete both API keys and application keys for your organization.
  name: Datadog Key Management API
  slug: datadog-key-management-api
- description: The Organizations API allows you to create, edit, and manage your Datadog organizations. It supports multi-org account configurations where a parent organization manages one or more child organization
  name: Datadog Organizations API
  slug: datadog-organizations-api
- description: 'The Downtimes API gives you greater control over monitor notifications by allowing you to globally exclude scopes from alerting. Downtime settings can be scheduled with start and end times to prevent '
  name: Datadog Downtimes API
  slug: datadog-downtimes-api
- description: The RUM API allows you to manage Real User Monitoring applications and search or aggregate RUM events over HTTP. It provides access to session data, user interactions, and frontend performance metrics
  name: Datadog RUM API
  slug: datadog-rum-api
- description: The APM Retention Filters API allows you to manage configuration of APM retention filters for your organization. Retention filters control which traces are indexed and retained for analysis and requir
  name: Datadog APM Retention Filters API
  slug: datadog-apm-retention-filters-api
- description: The Usage Metering API allows you to get hourly, daily, and monthly usage across multiple facets of Datadog. It is available to all Pro and Enterprise customers, with usage data delayed by up to 72 ho
  name: Datadog Usage Metering API
  slug: datadog-usage-metering-api
- description: The Spans API allows you to search and aggregate spans from your Datadog platform over HTTP. It supports querying distributed tracing data collected by Datadog APM.
  name: Datadog Spans API
  slug: datadog-spans-api
- description: The Processes API allows you to query processes data for your organization. It provides access to live process information collected from hosts running the Datadog Agent.
  name: Datadog Processes API
  slug: datadog-processes-api
- baseURL: https://api.datadoghq.com
  baseurl_source: declared
  description: The Teams API allows you to view and manage teams within Datadog. Teams can be associated with incidents, dashboards, and other resources to organize ownership and collaboration within your organizati
  name: Datadog Teams API
  phrasing_intents:
  - id: UpdateTeam
    intent: Update a team
    question: How do I rename a team or change its description?
  phrasing_ops: 1
  slug: datadog-teams-api
- description: The Workflow Automation API allows you to automate end-to-end processes by connecting Datadog with the rest of your tech stack. It supports over 1,000 out-of-the-box actions including integrations wit
  name: Datadog Workflow Automation API
  slug: datadog-workflow-automation-api
- description: The Case Management API allows you to view and manage cases and projects within Datadog Case Management. Cases can be created from monitors, security signals, and other alert sources to track investig
  name: Datadog Case Management API
  slug: datadog-case-management-api
- description: The Observability Pipelines API allows you to collect and process logs within your own infrastructure and route them to downstream integrations. It provides programmatic management of pipeline configu
  name: Datadog Observability Pipelines API
  slug: datadog-observability-pipelines-api
- description: The Sensitive Data Scanner API allows you to create, update, delete, and retrieve sensitive data scanner groups and rules. It enables automated detection and redaction of sensitive data within logs, A
  name: Datadog Sensitive Data Scanner API
  slug: datadog-sensitive-data-scanner-api
- description: The AWS Integration API allows you to configure your Datadog-AWS integration directly through the Datadog API. It supports managing AWS accounts, metrics collection, and log forwarding configuration.
  name: Datadog AWS Integration API
  slug: datadog-aws-integration-api
- description: The GCP Integration API allows you to configure your Datadog-Google Cloud Platform integration directly through the Datadog API. It supports managing GCP projects, service accounts, and metrics collec
  name: Datadog GCP Integration API
  slug: datadog-gcp-integration-api
- description: The CI Visibility Pipelines API allows you to search or aggregate CI Visibility pipeline events and send them to your Datadog site over HTTP. It provides insight into the performance and reliability o
  name: Datadog CI Visibility Pipelines API
  slug: datadog-ci-visibility-pipelines-api
- description: The Network Device Monitoring API allows you to fetch devices and interfaces and their attributes. It provides programmatic access to network topology and performance data collected from network devic
  name: Datadog Network Device Monitoring API
  slug: datadog-network-device-monitoring-api
- description: The On-Call API allows you to configure and manage Datadog On-Call schedules, escalation policies, and teams. It also supports triggering and managing on-call pages directly through the Datadog API.
  name: Datadog On-Call API
  slug: datadog-on-call-api
- description: The DORA Metrics API allows you to search and send events for DORA Metrics to measure and improve software delivery performance. It tracks deployment frequency, lead time for changes, change failure r
  name: Datadog DORA Metrics API
  slug: datadog-dora-metrics-api
- description: The Cloud Cost Management API allows you to set up, edit, and delete Cloud Cost Management accounts for AWS and Azure. Cost data can be queried using the Metrics endpoint with the cloud_cost data sour
  name: Datadog Cloud Cost Management API
  slug: datadog-cloud-cost-management-api
- description: The Hosts API allows you to search for hosts by name, alias, or tag and retrieve host totals. Hosts live within the past 3 hours are included by default, with a retention of 7 days.
  name: Datadog Hosts API
  slug: datadog-hosts-api
- description: The Tags API allows you to assign tags to hosts, returning a mapping of tags to hosts for your entire infrastructure. Tags can be used to filter and group resources across Datadog.
  name: Datadog Tags API
  slug: datadog-tags-api
- description: The Containers API allows you to get all containers for your organization. It provides programmatic access to container data collected from hosts running the Datadog Agent.
  name: Datadog Containers API
  slug: datadog-containers-api
- description: The Container Images API allows you to get all container images for your organization. It provides visibility into the container images running across your infrastructure.
  name: Datadog Container Images API
  slug: datadog-container-images-api
- description: The Notebooks API allows you to interact with Datadog Notebooks programmatically. Notebooks combine graphs and text in a linear, cell-based layout for exploring and sharing stories with your data.
  name: Datadog Notebooks API
  slug: datadog-notebooks-api
- description: The Dashboard Lists API allows you to interact with dashboard lists through the API to organize, find, and share all of your dashboards with your team and organization.
  name: Datadog Dashboard Lists API
  slug: datadog-dashboard-lists-api
- description: The Logs Pipelines API allows you to manage pipelines and processors that operate on incoming logs, parsing and transforming them into structured attributes for easier querying.
  name: Datadog Logs Pipelines API
  slug: datadog-logs-pipelines-api
- description: The Logs Indexes API allows you to manage configuration of log indexes for your organization. Log indexes define how logs are filtered, aggregated, and stored for retention and querying.
  name: Datadog Logs Indexes API
  slug: datadog-logs-indexes-api
- description: The Logs Metrics API allows you to manage configuration of log-based metrics for your organization. It provides the ability to generate metrics from log data for cost-effective long-term analysis.
  name: Datadog Logs Metrics API
  slug: datadog-logs-metrics-api
- description: The Logs Archives API allows you to manage logs archives that forward all ingested logs to cloud storage systems. It supports configuration of archive destinations and rehydration settings.
  name: Datadog Logs Archives API
  slug: datadog-logs-archives-api
- description: The Logs Custom Destinations API allows you to manage custom destinations that forward all ingested logs to external destinations such as Elasticsearch, Microsoft Sentinel, and HTTP endpoints.
  name: Datadog Logs Custom Destinations API
  slug: datadog-logs-custom-destinations-api
- description: The Logs Restriction Queries API allows you to manage restriction queries that control which logs the logs_read_data permission grants read access to, enabling fine-grained log access control by role.
  name: Datadog Logs Restriction Queries API
  slug: datadog-logs-restriction-queries-api
- description: The Spans Metrics API allows you to manage configuration of span-based metrics for your organization. It provides the ability to generate metrics from spans for cost-effective long-term analysis of AP
  name: Datadog Spans Metrics API
  slug: datadog-spans-metrics-api
- description: The Service Checks API allows you to submit a list of service checks to Datadog. Service checks can be submitted up to 10 minutes in the past and are used to monitor the status of services.
  name: Datadog Service Checks API
  slug: datadog-service-checks-api
- description: The Snapshots API allows you to take graph snapshots. Snapshots are PNG images generated by rendering a specified widget and capturing it once the data is available.
  name: Datadog Snapshots API
  slug: datadog-snapshots-api
- description: The IP Ranges API provides a list of IP prefixes belonging to Datadog. It returns available prefix information for Agent, API, and APM endpoints along with IPv4 and IPv6 prefixes.
  name: Datadog IP Ranges API
  slug: datadog-ip-ranges-api
- description: The IP Allowlist API is used to manage the IP addresses that can access the Datadog API and web UI. It allows you to configure IP address restrictions for your organization.
  name: Datadog IP Allowlist API
  slug: datadog-ip-allowlist-api
- baseURL: https://api.datadoghq.com
  baseurl_source: declared
  description: The Audit API allows you to search your Audit Logs events over HTTP. It returns Audit Logs events that match an audit search query, providing visibility into actions taken within your organization.
  name: Datadog Audit API
  phrasing_intents:
  - id: ListAuditLogs
    intent: List recent audit log events
    question: Who changed what in our Datadog org recently?
  - id: SearchAuditLogs
    intent: Search audit logs with a complex query
    question: Can I run an advanced filtered search over audit logs with a timezone?
  phrasing_ops: 2
  slug: datadog-audit-api
- description: The APM API provides endpoints for working with Application Performance Monitoring services and tracing data. It supports querying service-level metrics and trace data collected by Datadog APM.
  name: Datadog APM API
  slug: datadog-apm-api
- description: The Webhooks Integration API allows you to configure the Datadog-Webhooks integration directly through the Datadog API. It supports creating, updating, and deleting webhook endpoints and custom variab
  name: Datadog Webhooks Integration API
  slug: datadog-webhooks-integration-api
- description: The SLO Corrections API allows you to create, update, and delete corrections for Service Level Objectives. SLO corrections adjust SLO status calculations to account for planned maintenance or known is
  name: Datadog SLO Corrections API
  slug: datadog-slo-corrections-api
- description: The AWS Logs Integration API allows you to configure log collection from AWS services and manage your Datadog-AWS Logs integration. It supports listing and managing AWS log collection configurations.
  name: Datadog AWS Logs Integration API
  slug: datadog-aws-logs-integration-api
- description: The Azure Integration API allows you to configure your Datadog-Azure integration directly through the Datadog API. It supports managing Azure tenants, host filters, and metrics collection settings.
  name: Datadog Azure Integration API
  slug: datadog-azure-integration-api
- description: The Slack Integration API allows you to configure your Datadog-Slack integration directly through the Datadog API. It supports managing Slack channels for monitor notifications and alerts.
  name: Datadog Slack Integration API
  slug: datadog-slack-integration-api
- description: The PagerDuty Integration API allows you to configure your Datadog-PagerDuty integration directly through the Datadog API. It supports managing PagerDuty services and scheduling configurations.
  name: Datadog PagerDuty Integration API
  slug: datadog-pagerduty-integration-api
- description: The Opsgenie Integration API allows you to configure your Datadog-Opsgenie integration directly through the Datadog API. It supports managing Opsgenie services and alert routing.
  name: Datadog Opsgenie Integration API
  slug: datadog-opsgenie-integration-api
- description: The Cloudflare Integration API allows you to manage your Datadog-Cloudflare integration directly through the Datadog API. It supports listing and managing Cloudflare accounts and their associated reso
  name: Datadog Cloudflare Integration API
  slug: datadog-cloudflare-integration-api
- description: The Fastly Integration API allows you to manage your Datadog-Fastly integration accounts and services directly through the Datadog API. It supports listing and managing Fastly accounts.
  name: Datadog Fastly Integration API
  slug: datadog-fastly-integration-api
- description: The Confluent Cloud API allows you to manage your Datadog-Confluent Cloud integration accounts and account resources directly through the Datadog API. It supports monitoring Kafka clusters and related
  name: Datadog Confluent Cloud API
  slug: datadog-confluent-cloud-api
- description: The Okta Integration API allows you to configure your Datadog-Okta integration directly through the Datadog API. It supports listing and managing Okta accounts and their configurations.
  name: Datadog Okta Integration API
  slug: datadog-okta-integration-api
- description: The Microsoft Teams Integration API allows you to configure your Datadog-Microsoft Teams integration directly through the Datadog API. It supports managing Teams channels for notifications and alerts.
  name: Datadog Microsoft Teams Integration API
  slug: datadog-microsoft-teams-integration-api
- description: The Jira Integration API allows you to configure your Datadog-Jira integration directly through the Datadog API. It supports managing Jira issue templates and project configurations.
  name: Datadog Jira Integration API
  slug: datadog-jira-integration-api
- description: The Error Tracking API allows you to search issues within your organization programmatically. It returns a list of issues that match a given search query using event search syntax.
  name: Datadog Error Tracking API
  slug: datadog-error-tracking-api
- description: The Application Security API provides protection against application-level attacks that aim to exploit code-level vulnerabilities such as SSRF, SQL injection, Log4Shell, and XSS.
  name: Datadog Application Security API
  slug: datadog-application-security-api
- description: The CSM Threats API provides endpoints for managing Cloud Security Management Workload Protection agent rules. It monitors file, network, and process activity to detect real-time threats to your infra
  name: Datadog CSM Threats API
  slug: datadog-csm-threats-api
- description: The CSM Agents API allows you to get the list of all Cloud Security Management agents running on your hosts and containers. It provides visibility into agent coverage across your infrastructure.
  name: Datadog CSM Agents API
  slug: datadog-csm-agents-api
- description: The Service Scorecards API allows you to create and manage scorecard rules and outcomes. Scorecards help formalize your organization's best practices and track service compliance against defined crite
  name: Datadog Service Scorecards API
  slug: datadog-service-scorecards-api
- description: The Service Dependencies API allows you to get a list of services from APM and their dependencies. Services are filtered by environment and primary tag to map your service topology.
  name: Datadog Service Dependencies API
  slug: datadog-service-dependencies-api
- description: The Powerpack API allows you to create, update, delete, and retrieve Powerpacks. Powerpacks are templated groups of dashboard widgets that scale graphing expertise as reusable building blocks.
  name: Datadog Powerpack API
  slug: datadog-powerpack-api
- description: The Embeddable Graphs API allows you to create and manage embeddable graph snapshots that can be shared outside of Datadog. It supports creating, revoking, and listing embeddable graphs.
  name: Datadog Embeddable Graphs API
  slug: datadog-embeddable-graphs-api
- description: The RUM Metrics API allows you to manage configuration of RUM-based metrics for your organization. It provides the ability to generate metrics from Real User Monitoring data.
  name: Datadog RUM Metrics API
  slug: datadog-rum-metrics-api
- description: The Domain Allowlist API allows you to manage the email domain allowlist for your organization. It supports getting and updating the list of allowed email domains.
  name: Datadog Domain Allowlist API
  slug: datadog-domain-allowlist-api
- description: The Restriction Policies API allows you to manage restriction policies associated with Datadog resources including dashboards, notebooks, security rules, SLOs, workflows, and more.
  name: Datadog Restriction Policies API
  slug: datadog-restriction-policies-api
- description: The AuthN Mappings API is used to automatically map groups of users to roles in Datadog using attributes sent from Identity Providers. It enables federated authentication to role mapping.
  name: Datadog AuthN Mappings API
  slug: datadog-authn-mappings-api
- description: The Integrations API allows you to manage Datadog integrations programmatically. It provides endpoints for configuring and managing third-party service integrations within your organization.
  name: Datadog Integrations API
  slug: datadog-integrations-api
- description: The CI Visibility Tests API allows you to search or aggregate CI Visibility test events over HTTP. It provides insight into the performance and reliability of your test suites.
  name: Datadog CI Visibility Tests API
  slug: datadog-ci-visibility-tests-api
- description: The Agentless Scanning API provides visibility into risks and vulnerabilities within your hosts, running containers, and serverless functions without requiring teams to install Agents.
  name: Datadog Agentless Scanning API
  slug: datadog-agentless-scanning-api
- description: The Static Analysis API provides access to static analysis and dependency scanning results. It supports querying code analysis data for your organization.
  name: Datadog Static Analysis API
  slug: datadog-static-analysis-api
- description: The Entity Risk Scores API provides security risk assessments for entities like cloud resources, identities, or services based on detected signals, misconfigurations, and identity risks.
  name: Datadog Entity Risk Scores API
  slug: datadog-entity-risk-scores-api
- description: The API Management API allows you to create and manage APIs from OpenAPI specifications. It supports the Datadog API Catalog for tracking API performance, security, and ownership.
  name: Datadog API Management API
  slug: datadog-api-management-api
- description: The Cloud Workload Security API provides endpoints for managing workload protection rules and agent configurations. It monitors file, network, and process activity to detect real-time threats.
  name: Datadog Cloud Workload Security API
  slug: datadog-cloud-workload-security-api
- baseURL: https://api.datadoghq.com
  baseurl_source: declared
  description: The Account API from Datadog — 20 operation(s) for account.
  name: Datadog Account API
  phrasing_intents:
  - id: CreateGCPSTSAccount
    intent: Add a GCP STS service account
    question: How do I connect a GCP service account to Datadog using STS?
  - id: DeleteGCPSTSAccount
    intent: Remove a GCP STS service account
    question: Can I disconnect a GCP STS service account from Datadog?
  - id: UpdateGCPSTSAccount
    intent: Update a GCP STS service account
    question: Can I change settings on a GCP service account already connected via STS?
  - id: GetGCPSTSDelegate
    intent: Get the GCP STS delegate account
    question: Which Datadog service account do I grant access to in GCP?
  - id: CreateCloudflareAccount
    intent: Connect a Cloudflare account
    question: How do I add my Cloudflare account to Datadog?
  - id: DeleteCloudflareAccount
    intent: Remove a Cloudflare account integration
    question: Can I disconnect a Cloudflare account from Datadog?
  - id: GetCloudflareAccount
    intent: Get a Cloudflare account integration
    question: What are the settings of a connected Cloudflare account?
  - id: UpdateCloudflareAccount
    intent: Update a Cloudflare account integration
    question: Can I rotate the API key on a connected Cloudflare account?
  phrasing_ops: 35
  slug: datadog-account-api
- baseURL: https://api.datadoghq.com
  baseurl_source: declared
  description: The Accounts API from Datadog — 6 operation(s) for accounts.
  name: Datadog Accounts API
  phrasing_intents:
  - id: GetCSMCloudAccountsCoverageAnalysis
    intent: Get CSM coverage of my cloud accounts
    question: What share of my cloud accounts is scanned by Cloud Security Management?
  - id: ListGCPSTSAccounts
    intent: List GCP STS-enabled service accounts
    question: Which GCP service accounts are connected with STS?
  - id: ListCloudflareAccounts
    intent: List Cloudflare integration accounts
    question: Which Cloudflare accounts are connected to my integration?
  - id: ListConfluentAccount
    intent: List Confluent Cloud integration accounts
    question: Which Confluent Cloud accounts are configured in my integration?
  - id: ListFastlyAccounts
    intent: List Fastly integration accounts
    question: Which Fastly accounts are connected to my integration?
  - id: ListOktaAccounts
    intent: List Okta integration accounts
    question: Which Okta accounts are connected to my integration?
  phrasing_ops: 6
  slug: datadog-accounts-api
- baseURL: https://api.datadoghq.com
  baseurl_source: declared
  description: The Acknowledge API from Datadog — 1 operation(s) for acknowledge.
  name: Datadog Acknowledge API
  phrasing_intents:
  - id: AcknowledgeOnCallPage
    intent: Acknowledge an On-Call page
    question: Can I acknowledge an on-call page so escalation stops?
  phrasing_ops: 1
  slug: datadog-acknowledge-api
- baseURL: https://api.datadoghq.com
  baseurl_source: declared
  description: The Across API from Datadog — 6 operation(s) for across.
  name: Datadog Across API
  phrasing_intents:
  - id: QueryScalarData
    intent: Query scalar values across data sources
    question: How do I get a single aggregated number like a Query Value widget shows?
  - id: QueryTimeseriesData
    intent: Query timeseries data across data sources
    question: How do I pull a timeseries graph's data points through the API?
  phrasing_ops: 2
  slug: datadog-across-api
- baseURL: https://api.datadoghq.com
  baseurl_source: declared
  description: The Action API from Datadog — 2 operation(s) for action.
  name: Datadog Action API
  phrasing_intents:
  - id: CreateActionConnection
    intent: Create an Action Connection
    question: Can I create a connection that workflows and apps use to call external services?
  - id: DeleteActionConnection
    intent: Delete an Action Connection
    question: Can I remove an Action Connection that's no longer used?
  - id: GetActionConnection
    intent: Get an Action Connection
    question: Can I look up how an existing Action Connection is configured?
  - id: UpdateActionConnection
    intent: Update an Action Connection
    question: Can I rotate the credentials on an existing Action Connection?
  phrasing_ops: 4
  slug: datadog-action-api
- baseURL: https://api.datadoghq.com
  baseurl_source: declared
  description: The Active API from Datadog — 3 operation(s) for active.
  name: Datadog Active API
  phrasing_intents:
  - id: GetActiveBillingDimensions
    intent: Get active billing dimensions for cost attribution
    question: Which billing dimensions are active for cost attribution?
  - id: ListActiveMetricConfigurations
    intent: List actively queried tags for a metric
    question: Which tags of a metric are actually being queried on dashboards and monitors?
  - id: ListMonitorDowntimes
    intent: List active downtimes for a monitor
    question: Is a specific monitor currently silenced by a downtime?
  phrasing_ops: 3
  slug: datadog-active-api
- baseURL: https://api.datadoghq.com
  baseurl_source: declared
  description: The Add API from Datadog — 9 operation(s) for add.
  name: Datadog Add API
  phrasing_intents:
  - id: CreateDashboardListItems
    intent: Add dashboards to a dashboard list
    question: How do I add dashboards to an existing dashboard list?
  - id: CreateFastlyService
    intent: Add a Fastly service to an account
    question: How do I start monitoring a new Fastly service?
  - id: AddUserToRole
    intent: Add a user to a role
    question: How do I give a user a role in Datadog?
  - id: CreateTeamMembership
    intent: Add a user to a team
    question: How do I add someone to a team?
  phrasing_ops: 4
  slug: datadog-add-api
- baseURL: https://api.datadoghq.com
  baseurl_source: declared
  description: The Agent API from Datadog — 4 operation(s) for agent.
  name: Datadog Agent API
  phrasing_intents:
  - id: ListCSMThreatsAgentRules
    intent: List Workload Protection agent rules
    question: Which Workload Protection agent rules are defined on my commercial Datadog site?
  - id: CreateCSMThreatsAgentRule
    intent: Create a Workload Protection agent rule
    question: How do I add a new Workload Protection agent rule outside the government site?
  - id: DeleteCSMThreatsAgentRule
    intent: Delete a Workload Protection agent rule
    question: How do I remove a Workload Protection agent rule on a non-government site?
  - id: GetCSMThreatsAgentRule
    intent: Get a Workload Protection agent rule
    question: What expression does one Workload Protection agent rule use?
  - id: UpdateCSMThreatsAgentRule
    intent: Update a Workload Protection agent rule
    question: How do I change the expression or enabled state of a Workload Protection agent rule?
  - id: ListCloudWorkloadSecurityAgentRules
    intent: List agent rules on the US1-FED site
    question: Which Workload Protection agent rules exist on the US1-FED government site?
  - id: CreateCloudWorkloadSecurityAgentRule
    intent: Create an agent rule on the US1-FED site
    question: How do I create a Workload Protection agent rule on the US1-FED government site?
  - id: DeleteCloudWorkloadSecurityAgentRule
    intent: Delete an agent rule on the US1-FED site
    question: How do I delete a Workload Protection agent rule on the US1-FED site?
  phrasing_ops: 10
  slug: datadog-agent-api
- baseURL: https://api.datadoghq.com
  baseurl_source: declared
  description: The Agents API from Datadog — 2 operation(s) for agents.
  name: Datadog Agents API
  phrasing_intents:
  - id: ListAllCSMAgents
    intent: List Cloud Security agents on hosts
    question: Which hosts and containers are running Cloud Security Management agents?
  - id: ListAllCSMServerlessAgents
    intent: List Cloud Security serverless agents
    question: Which serverless workloads have CSM serverless agents?
  phrasing_ops: 2
  slug: datadog-agents-api
- baseURL: https://api.datadoghq.com
  baseurl_source: declared
  description: The Aggregate API from Datadog — 5 operation(s) for aggregate.
  name: Datadog Aggregate API
  phrasing_intents:
  - id: AggregateCIAppPipelineEvents
    intent: Aggregate CI pipeline events
    question: Can I compute average CI pipeline duration grouped by branch?
  - id: AggregateCIAppTestEvents
    intent: Aggregate CI test events
    question: Can I count failing CI tests grouped by test suite?
  - id: AggregateLogs
    intent: Aggregate log events into buckets
    question: Can I count log events grouped by service or status?
  - id: AggregateRUMEvents
    intent: Aggregate RUM events
    question: Can I count Real User Monitoring sessions grouped by browser?
  - id: AggregateSpans
    intent: Aggregate APM spans
    question: Can I compute latency percentiles across APM spans?
  phrasing_ops: 5
  slug: datadog-aggregate-api
- baseURL: https://api.datadoghq.com
  baseurl_source: declared
  description: The Aggregated API from Datadog — 1 operation(s) for aggregated.
  name: Datadog Aggregated API
  phrasing_intents:
  - id: GetAggregatedConnections
    intent: Get aggregated network connections
    question: Which services talk to each other most over the network?
  phrasing_ops: 1
  slug: datadog-aggregated-api
- baseURL: https://api.datadoghq.com
  baseurl_source: declared
  description: The All API from Datadog — 44 operation(s) for all.
  name: Datadog All API
  phrasing_intents:
  - id: ListAPIKeys
    intent: List the organization's API keys
    question: Which Datadog API keys exist in my organization?
  - id: ListSpansMetrics
    intent: List span-based metrics
    question: What span-based metrics have we configured from APM traces?
  - id: ListApmRetentionFilters
    intent: List APM retention filters
    question: Which APM retention filters decide what traces we keep?
  - id: ListApplicationKeys
    intent: List all application keys in the org
    question: What application keys exist across my whole organization?
  - id: ListAuthNMappings
    intent: List AuthN mappings
    question: Which SAML attribute mappings assign roles in my org?
  - id: GetProjects
    intent: List all Case Management projects
    question: What case management projects exist in our Datadog org?
  - id: ListContainerImages
    intent: List container images
    question: Which container images are running across my infrastructure?
  - id: ListContainers
    intent: List running containers
    question: What containers are running in my organization right now?
  phrasing_ops: 38
  slug: datadog-all-api
- baseURL: https://api.datadoghq.com
  baseurl_source: declared
  description: The Analysis API from Datadog — 3 operation(s) for analysis.
  name: Datadog Analysis API
  phrasing_intents:
  - id: GetCSMHostsAndContainersCoverageAnalysis
    intent: Get CSM coverage for hosts and containers
    question: What share of my hosts and containers have Cloud Security Management enabled?
  - id: GetCSMServerlessCoverageAnalysis
    intent: Get CSM coverage for serverless resources
    question: How much of my serverless footprint is covered by Cloud Security Management?
  phrasing_ops: 2
  slug: datadog-analysis-api
- baseURL: https://api.datadoghq.com
  baseurl_source: declared
  description: The Applications API from Datadog — 12 operation(s) for applications.
  name: Datadog Applications API
  phrasing_intents:
  - id: DeleteApps
    intent: Delete several App Builder apps at once
    question: Can I delete multiple App Builder apps in a single request?
  - id: ListApps
    intent: List App Builder apps
    question: Which App Builder apps exist in my org and who created them?
  - id: CreateApp
    intent: Create an App Builder app
    question: How do I create a new internal app in App Builder through the API?
  - id: DeleteApp
    intent: Delete a single App Builder app
    question: How do I delete one App Builder app by its ID?
  - id: GetApp
    intent: Get an App Builder app's full definition
    question: How can I see the full definition of an App Builder app?
  - id: UpdateApp
    intent: Update an App Builder app
    question: Does updating an App Builder app create a new version?
  - id: UnpublishApp
    intent: Unpublish an App Builder app
    question: Can I take an app offline without deleting it?
  - id: PublishApp
    intent: Publish an App Builder app
    question: How do I make an App Builder app available to other users?
  phrasing_ops: 20
  slug: datadog-applications-api
- baseURL: https://api.datadoghq.com
  baseurl_source: declared
  description: The Archive API from Datadog — 5 operation(s) for archive.
  name: Datadog Archive API
  phrasing_intents:
  - id: ArchiveCase
    intent: Archive a case
    question: How do I archive a case that's no longer active?
  - id: GetLogsArchiveOrder
    intent: Get the logs archive order
    question: In what order are my logs archives processed?
  - id: UpdateLogsArchiveOrder
    intent: Reorder logs archives
    question: Can I change which logs archive processes logs first?
  - id: CreateLogsArchive
    intent: Create a logs archive
    question: How do I start archiving logs to cloud storage?
  - id: DeleteLogsArchive
    intent: Delete a logs archive
    question: Can I remove a logs archive I no longer need?
  - id: GetLogsArchive
    intent: Get a logs archive
    question: What's the configuration of a specific logs archive?
  - id: UpdateLogsArchive
    intent: Replace a logs archive's configuration
    question: Can I change the destination bucket of an existing logs archive?
  - id: RemoveRoleFromArchive
    intent: Revoke a role's read access to an archive
    question: Can I take away a role's access to a logs archive?
  phrasing_ops: 10
  slug: datadog-archive-api
- baseURL: https://api.datadoghq.com
  baseurl_source: declared
  description: The Assets API from Datadog — 2 operation(s) for assets.
  name: Datadog Assets API
  phrasing_intents:
  - id: ListMetricAssets
    intent: Find dashboards and monitors that use a metric
    question: Which dashboards, monitors, notebooks and SLOs use this metric?
  - id: ListVulnerableAssets
    intent: List vulnerable assets
    question: Which of my assets have known vulnerabilities?
  phrasing_ops: 2
  slug: datadog-assets-api
- baseURL: https://api.datadoghq.com
  baseurl_source: declared
  description: The Assign API from Datadog — 1 operation(s) for assign.
  name: Datadog Assign API
  phrasing_intents:
  - id: AssignCase
    intent: Assign a case to a user
    question: How do I assign a Case Management case to a teammate?
  phrasing_ops: 1
  slug: datadog-assign-api
- baseURL: https://api.datadoghq.com
  baseurl_source: declared
  description: The Assignee API from Datadog — 1 operation(s) for assignee.
  name: Datadog Assignee API
  phrasing_intents:
  - id: EditSecurityMonitoringSignalAssignee
    intent: Assign a security signal for triage
    question: Can I assign a security signal to a teammate to investigate?
  phrasing_ops: 1
  slug: datadog-assignee-api
- baseURL: https://api.datadoghq.com
  baseurl_source: declared
  description: The Attachments API from Datadog — 1 operation(s) for attachments.
  name: Datadog Attachments API
  phrasing_intents:
  - id: ListIncidentAttachments
    intent: List an incident's attachments
    question: Which postmortems and links are attached to an incident?
  - id: UpdateIncidentAttachments
    intent: Add, change or remove incident attachments
    question: How do I attach a postmortem link to an incident?
  phrasing_ops: 2
  slug: datadog-attachments-api
- baseURL: https://api.datadoghq.com
  baseurl_source: declared
  description: The Attributes API from Datadog — 1 operation(s) for attributes.
  name: Datadog Attributes API
  phrasing_intents:
  - id: UpdateTeamMembership
    intent: Update a user's team membership
    question: How do I make a team member an admin of the team?
  phrasing_ops: 1
  slug: datadog-attributes-api
- baseURL: https://api.datadoghq.com
  baseurl_source: declared
  description: Search your Audit Logs events over HTTP.
  name: Datadog Audit API
  phrasing_intents:
  - id: ListAuditLogs
    intent: List recent audit log events
    question: Who changed what in our Datadog org recently?
  - id: SearchAuditLogs
    intent: Search audit logs with a complex query
    question: Can I run an advanced filtered search over audit logs with a timezone?
  phrasing_ops: 2
  slug: datadog-audit-api
- baseURL: https://api.datadoghq.com
  baseurl_source: declared
  description: The Available API from Datadog — 1 operation(s) for available.
  name: Datadog Available API
  phrasing_intents:
  - id: ListAWSNamespaces
    intent: List available AWS CloudWatch namespaces
    question: Which AWS CloudWatch namespaces can send metrics to Datadog?
  phrasing_ops: 1
  slug: datadog-available-api
- baseURL: https://api.datadoghq.com
  baseurl_source: declared
  description: The Batch API from Datadog — 2 operation(s) for batch.
  name: Datadog Batch API
  phrasing_intents:
  - id: MuteFindings
    intent: Mute or unmute a batch of findings
    question: Can I mute many posture management findings at once?
  - id: CreateScorecardOutcomesBatch
    intent: Set scorecard outcomes in bulk
    question: Can I report pass or fail for many service-rule pairs in one request?
  phrasing_ops: 2
  slug: datadog-batch-api
- baseURL: https://api.datadoghq.com
  baseurl_source: declared
  description: The Billing API from Datadog — 2 operation(s) for billing.
  name: Datadog Billing API
  phrasing_intents:
  - id: GetBillingDimensionMapping
    intent: Map billing dimensions to usage API keys
    question: Which usage API field corresponds to each billing dimension on my invoice?
  phrasing_ops: 1
  slug: datadog-billing-api
- baseURL: https://api.datadoghq.com
  baseurl_source: declared
  description: The Budget API from Datadog — 2 operation(s) for budget.
  name: Datadog Budget API
  phrasing_intents:
  - id: UpsertBudget
    intent: Create or update a cost budget
    question: Can I set a cloud cost budget with monthly entries?
  - id: DeleteBudget
    intent: Delete a cost budget
    question: Can I remove a cost budget I no longer track?
  - id: GetBudget
    intent: Get a cost budget
    question: Can I look up one cost budget and its entries?
  phrasing_ops: 3
  slug: datadog-budget-api
- baseURL: https://api.datadoghq.com
  baseurl_source: declared
  description: The Budgets API from Datadog — 1 operation(s) for budgets.
  name: Datadog Budgets API
  phrasing_intents:
  - id: ListBudgets
    intent: List cost budgets
    question: Which cloud cost budgets are set up in my organization?
  phrasing_ops: 1
  slug: datadog-budgets-api
- baseURL: https://api.datadoghq.com
  baseurl_source: declared
  description: The Cancel API from Datadog — 3 operation(s) for cancel.
  name: Datadog Cancel API
  phrasing_intents:
  - id: CancelDowntime
    intent: Cancel a downtime
    question: How do I end a downtime early so monitors alert again?
  - id: CancelHistoricalJob
    intent: Cancel a historical detection job
    question: Can I stop a SIEM historical job that's still running?
  - id: CancelWorkflowInstance
    intent: Cancel a running workflow execution
    question: How do I cancel a workflow execution that's in progress?
  phrasing_ops: 3
  slug: datadog-cancel-api
- baseURL: https://api.datadoghq.com
  baseurl_source: declared
  description: The Cap API from Datadog — 1 operation(s) for cap.
  name: Datadog Cap API
  phrasing_intents:
  - id: GetOnDemandConcurrencyCap
    intent: Get the Synthetics on-demand concurrency cap
    question: What is my current on-demand concurrency cap for Synthetic tests?
  - id: SetOnDemandConcurrencyCap
    intent: Set the Synthetics on-demand concurrency cap
    question: Can I raise the number of Synthetic tests that run in parallel on demand?
  phrasing_ops: 2
  slug: datadog-cap-api
- baseURL: https://api.datadoghq.com
  baseurl_source: declared
  description: The Cardinality API from Datadog — 1 operation(s) for cardinality.
  name: Datadog Cardinality API
  phrasing_intents:
  - id: EstimateMetricsOutputSeries
    intent: Estimate a metric's cardinality for a tag config
    question: How many custom metric series would I get if I limit a metric to certain tags?
  phrasing_ops: 1
  slug: datadog-cardinality-api
- baseURL: https://api.datadoghq.com
  baseurl_source: declared
  description: The Case API from Datadog — 8 operation(s) for case.
  name: Datadog Case API
  phrasing_intents:
  - id: CreateCase
    intent: Create a case
    question: Can I open a case in Case Management from an automation?
  - id: GetCase
    intent: Get a case's details
    question: Can I look up a case by its key instead of its UUID?
  - id: UpdatePriority
    intent: Change a case's priority
    question: Can I raise the priority of an existing case?
  - id: UpdateStatus
    intent: Change a case's status
    question: Can I move a case to in progress or closed?
  - id: UnarchiveCase
    intent: Unarchive a case
    question: Can I bring an archived case back?
  - id: UnassignCase
    intent: Remove the assignee from a case
    question: Can I unassign a case so nobody owns it?
  phrasing_ops: 6
  slug: datadog-case-api
- baseURL: https://api.datadoghq.com
  baseurl_source: declared
  description: The Cases API from Datadog — 1 operation(s) for cases.
  name: Datadog Cases API
  phrasing_intents:
  - id: SearchCases
    intent: Search cases
    question: Can I search Case Management cases by keyword?
  phrasing_ops: 1
  slug: datadog-cases-api
- baseURL: https://api.datadoghq.com
  baseurl_source: declared
  description: The Change API from Datadog — 2 operation(s) for change.
  name: Datadog Change API
  phrasing_intents:
  - id: EditSecurityMonitoringSignalIncidents
    intent: Change a security signal's related incidents
    question: How do I link a security signal to an incident?
  - id: EditSecurityMonitoringSignalState
    intent: Change a security signal's triage state
    question: How do I mark a security signal as reviewed or archived?
  phrasing_ops: 2
  slug: datadog-change-api
- baseURL: https://api.datadoghq.com
  baseurl_source: declared
  description: The Channel API from Datadog — 1 operation(s) for channel.
  name: Datadog Channel API
  phrasing_intents:
  - id: GetChannelByName
    intent: Look up a Microsoft Teams channel by name
    question: How do I find the IDs for a Microsoft Teams channel by its name?
  phrasing_ops: 1
  slug: datadog-channel-api
- baseURL: https://api.datadoghq.com
  baseurl_source: declared
  description: The Cloud API from Datadog — 5 operation(s) for cloud.
  name: Datadog Cloud API
  phrasing_intents:
  - id: ListCostAWSCURConfigs
    intent: List AWS CUR cost configs
    question: Which AWS Cost and Usage Report configs are set up for Cloud Cost Management?
  - id: CreateCostAWSCURConfig
    intent: Add an AWS CUR config for cost management
    question: How do I connect an AWS Cost and Usage Report to Cloud Cost Management?
  - id: DeleteCostAWSCURConfig
    intent: Archive an AWS CUR cost account
    question: Can I archive an AWS cost account I no longer want tracked?
  - id: UpdateCostAWSCURConfig
    intent: Update an AWS CUR cost config
    question: Can I change which AWS accounts an existing CUR config includes?
  - id: ListCostAzureUCConfigs
    intent: List Azure cost configs
    question: Which Azure usage cost configs are set up in Cloud Cost Management?
  - id: CreateCostAzureUCConfigs
    intent: Add an Azure cost config
    question: Can I connect Azure billing exports to Cloud Cost Management?
  - id: DeleteCostAzureUCConfig
    intent: Archive an Azure cost account
    question: Can I archive an Azure cost account so it stops being tracked?
  - id: UpdateCostAzureUCConfigs
    intent: Update an Azure cost config status
    question: Can I switch an Azure cost config between active and archived?
  phrasing_ops: 8
  slug: datadog-cloud-api
- baseURL: https://api.datadoghq.com
  baseurl_source: declared
  description: The Configuration API from Datadog — 4 operation(s) for configuration.
  name: Datadog Configuration API
  phrasing_intents:
  - id: DeleteTagConfiguration
    intent: Delete a metric's tag configuration
    question: How do I remove the tag configuration from a metric?
  - id: ListTagConfigurationByName
    intent: Get a metric's tag configuration
    question: Which tag keys are queryable for a given metric?
  - id: UpdateTagConfiguration
    intent: Update a metric's tag configuration
    question: Can I switch a metric's tag configuration to exclude tags instead of including them?
  - id: CreateTagConfiguration
    intent: Create a tag configuration for a metric
    question: How do I limit which tags are queryable on a metric to cut custom metric costs?
  - id: CreateMonitorConfigPolicy
    intent: Create a monitor configuration policy
    question: How do I require specific tags on every new monitor?
  - id: DeleteMonitorConfigPolicy
    intent: Delete a monitor configuration policy
    question: How do I stop enforcing a monitor tag policy?
  - id: GetMonitorConfigPolicy
    intent: Get a monitor configuration policy
    question: Which tag keys and values does a monitor configuration policy require?
  - id: UpdateMonitorConfigPolicy
    intent: Edit a monitor configuration policy
    question: How do I change the allowed tag values in an existing monitor policy?
  phrasing_ops: 8
  slug: datadog-configuration-api
- baseURL: https://api.datadoghq.com
  baseurl_source: declared
  description: The Configure API from Datadog — 1 operation(s) for configure.
  name: Datadog Configure API
  phrasing_intents:
  - id: CreateBulkTagsMetricsConfiguration
    intent: Configure queryable tags for many metrics
    question: Can I set queryable tag keys for every metric sharing a name prefix?
  phrasing_ops: 1
  slug: datadog-configure-api
- baseURL: https://api.datadoghq.com
  baseurl_source: declared
  description: The Convert API from Datadog — 3 operation(s) for convert.
  name: Datadog Convert API
  phrasing_intents:
  - id: ConvertSecurityMonitoringRuleFromJSONToTerraform
    intent: Convert a draft rule's JSON to Terraform
    question: Can I turn a detection rule I haven't created yet into Terraform config?
  - id: ConvertExistingSecurityMonitoringRule
    intent: Export an existing rule as Terraform
    question: How do I export an existing detection rule as Terraform?
  - id: ConvertJobResultToSignal
    intent: Convert a historical job result to a signal
    question: Can I turn a historical detection job result into a security signal?
  phrasing_ops: 3
  slug: datadog-convert-api
- baseURL: https://api.datadoghq.com
  baseurl_source: declared
  description: The Cost API from Datadog — 10 operation(s) for cost.
  name: Datadog Cost API
  phrasing_intents:
  - id: GetMonthlyCostAttribution
    intent: Get monthly cost attribution by tag
    question: How much did each team spend on Datadog last month, broken down by tag?
  phrasing_ops: 1
  slug: datadog-cost-api
- baseURL: https://api.datadoghq.com
  baseurl_source: declared
  description: The Create API from Datadog — 69 operation(s) for create.
  name: Datadog Create API
  phrasing_intents:
  - id: CreateAPIKey
    intent: Create a new API key
    question: Can I generate a fresh Datadog API key for a new agent or service?
  - id: CreateOpenAPI
    intent: Register an API in the API Catalog from OpenAPI
    question: Can I add an API to the API Catalog by uploading its OpenAPI file?
  - id: CreateSpansMetric
    intent: Create a metric from ingested spans
    question: Can I turn my APM spans into a custom metric?
  - id: CreateApmRetentionFilter
    intent: Create an APM span retention filter
    question: Can I choose which spans get indexed and retained in APM?
  - id: CreateAuthNMapping
    intent: Map an identity provider attribute to a role
    question: Can I map a SAML attribute from my identity provider to a Datadog role?
  - id: CreateProject
    intent: Create a Case Management project
    question: Can I set up a new project to organize cases in Case Management?
  - id: UpsertCatalogEntity
    intent: Create or update Software Catalog entities
    question: Can I register services and other entities in the Software Catalog programmatically?
  - id: CreateCustomFramework
    intent: Create a custom compliance framework
    question: Can I define my own compliance framework in Cloud Security Management?
  phrasing_ops: 51
  slug: datadog-create-api
- baseURL: https://api.datadoghq.com
  baseurl_source: declared
  description: The Custom API from Datadog — 8 operation(s) for custom.
  name: Datadog Custom API
  phrasing_intents:
  - id: DeleteCustomFramework
    intent: Delete a custom compliance framework
    question: Can I remove a custom framework I no longer use?
  - id: GetCustomFramework
    intent: Get a custom compliance framework
    question: Can I fetch one version of a custom compliance framework?
  - id: UpdateCustomFramework
    intent: Update a custom compliance framework
    question: Can I change the requirements in an existing custom framework?
  - id: ListCustomCostsFiles
    intent: List Custom Costs files
    question: Which Custom Costs files have been uploaded to Cloud Cost Management?
  - id: UploadCustomCostsFile
    intent: Upload a Custom Costs file
    question: Can I bring costs from a vendor without a native integration into Cloud Cost Management?
  - id: DeleteCustomCostsFile
    intent: Delete a Custom Costs file
    question: Can I remove a custom costs file that was uploaded by mistake?
  - id: GetCustomCostsFile
    intent: Get a Custom Costs file
    question: Can I fetch one Custom Costs file to check what was uploaded?
  - id: DeleteLogsCustomDestination
    intent: Delete a custom log destination
    question: Can I stop forwarding logs to a custom destination by deleting it?
  phrasing_ops: 13
  slug: datadog-custom-api
- baseURL: https://api.datadoghq.com
  baseurl_source: declared
  description: The Dashboards API from Datadog — 1 operation(s) for dashboards.
  name: Datadog Dashboards API
  phrasing_intents:
  - id: DeleteDashboardListItems
    intent: Remove dashboards from a dashboard list
    question: Can I take dashboards out of a list without deleting them?
  - id: GetDashboardListItems
    intent: Get dashboards in a dashboard list
    question: Which dashboards are in a given dashboard list?
  - id: UpdateDashboardListItems
    intent: Replace the dashboards in a dashboard list
    question: Can I set exactly which dashboards a list contains?
  phrasing_ops: 3
  slug: datadog-dashboards-api
- baseURL: https://api.datadoghq.com
  baseurl_source: declared
  description: The Definition API from Datadog — 2 operation(s) for definition.
  name: Datadog Definition API
  phrasing_intents:
  - id: DeleteServiceDefinition
    intent: Delete a service definition
    question: Can I remove a service from the Service Catalog?
  - id: GetServiceDefinition
    intent: Get a service definition
    question: What owner and links are recorded for a service in the Service Catalog?
  phrasing_ops: 2
  slug: datadog-definition-api
- baseURL: https://api.datadoghq.com
  baseurl_source: declared
  description: The Delete API from Datadog — 72 operation(s) for delete.
  name: Datadog Delete API
  phrasing_intents:
  - id: DeleteAwsScanOptions
    intent: Remove Agentless scan options for an AWS account
    question: How do I stop Agentless scanning settings from applying to one AWS account?
  - id: DeleteAPIKey
    intent: Delete an API key
    question: How do I permanently delete a Datadog API key that leaked?
  - id: DeleteOpenAPI
    intent: Delete an API from the API catalog
    question: What's the way to remove an API definition from the API catalog?
  - id: DeleteSpansMetric
    intent: Delete a span-based metric
    question: How can I get rid of a metric I generated from APM spans?
  - id: DeleteApmRetentionFilter
    intent: Delete an APM span retention filter
    question: Can I delete an APM retention filter that keeps spans I no longer need?
  - id: DeleteAuthNMapping
    intent: Delete an AuthN mapping
    question: How do I remove a SAML attribute-to-role AuthN mapping?
  - id: DeleteCatalogEntity
    intent: Delete an entity from Software Catalog
    question: How can I remove a service or entity from the Software Catalog?
  - id: DeleteIncidentType
    intent: Delete an incident type
    question: Can I delete an incident type I configured but never use?
  phrasing_ops: 44
  slug: datadog-delete-api
- baseURL: https://api.datadoghq.com
  baseurl_source: declared
  description: The Demand API from Datadog — 2 operation(s) for demand.
  name: Datadog Demand API
  phrasing_intents:
  - id: ListAwsOnDemandTasks
    intent: List AWS on-demand scan tasks
    question: Which on-demand agentless scans have run against my AWS resources?
  - id: CreateAwsOnDemandTask
    intent: Trigger an AWS on-demand agentless scan
    question: Can I scan one AWS resource right now with high priority?
  - id: GetAwsOnDemandTask
    intent: Get an AWS on-demand scan task
    question: Can I check the status of one on-demand scan task?
  phrasing_ops: 3
  slug: datadog-demand-api
- baseURL: https://api.datadoghq.com
  baseurl_source: declared
  description: The Deployments API from Datadog — 3 operation(s) for deployments.
  name: Datadog Deployments API
  phrasing_intents:
  - id: CreateDORADeployment
    intent: Send a deployment event for DORA metrics
    question: How do I report deployments so DORA deployment frequency and lead time are tracked?
  - id: ListDORADeployments
    intent: List DORA deployment events
    question: Which deployments have been recorded for DORA metrics?
  - id: GetDORADeployment
    intent: Get a DORA deployment event
    question: How can I look up a single deployment event by ID?
  phrasing_ops: 3
  slug: datadog-deployments-api
- baseURL: https://api.datadoghq.com
  baseurl_source: declared
  description: The Detection API from Datadog — 2 operation(s) for detection.
  name: Datadog Detection API
  phrasing_intents:
  - id: ValidateSecurityMonitoringRule
    intent: Validate a detection rule
    question: Can I check a detection rule for errors before creating it?
  phrasing_ops: 1
  slug: datadog-detection-api
- baseURL: https://api.datadoghq.com
  baseurl_source: declared
  description: The Devices API from Datadog — 4 operation(s) for devices.
  name: Datadog Devices API
  phrasing_intents:
  - id: ListDevices
    intent: List network devices
    question: Which network devices is Network Device Monitoring tracking?
  - id: GetDevice
    intent: Get a network device's details
    question: What vendor, model and IP address does a monitored device have?
  - id: GetInterfaces
    intent: List a device's network interfaces
    question: Which interfaces does a network device have and are they up?
  - id: ListDeviceUserTags
    intent: List the tags on a network device
    question: What user tags are applied to a network device?
  - id: UpdateDeviceUserTags
    intent: Update the tags on a network device
    question: How do I change the tags on a network device?
  phrasing_ops: 5
  slug: datadog-devices-api
- baseURL: https://api.datadoghq.com
  baseurl_source: declared
  description: The Disables API from Datadog — 1 operation(s) for disables.
  name: Datadog Disables API
  phrasing_intents:
  - id: DisableUser
    intent: Disable a user
    question: How do I disable a user who has left the company?
  phrasing_ops: 1
  slug: datadog-disables-api
- baseURL: https://api.datadoghq.com
  baseurl_source: declared
  description: The Domain API from Datadog — 1 operation(s) for domain.
  name: Datadog Domain API
  phrasing_intents:
  - id: GetDomainAllowlist
    intent: Get the email domain allowlist
    question: Which email domains are allowed to receive notifications from my org?
  - id: PatchDomainAllowlist
    intent: Update the email domain allowlist
    question: Can I restrict notification emails to my company's domains?
  phrasing_ops: 2
  slug: datadog-domain-api
- baseURL: https://api.datadoghq.com
  baseurl_source: declared
  description: The Download API from Datadog — 2 operation(s) for download.
  name: Datadog Download API
  phrasing_intents:
  - id: DownloadCSMThreatsPolicy
    intent: Download the Workload Protection policy file
    question: How do I export my active Workload Protection agent rules as a .policy file?
  - id: DownloadCloudWorkloadPolicyFile
    intent: Download the Workload Protection policy (US1-FED)
    question: Which endpoint downloads the Workload Protection policy on the US1-FED government site?
  phrasing_ops: 2
  slug: datadog-download-api
- baseURL: https://api.datadoghq.com
  baseurl_source: declared
  description: The Edit API from Datadog — 6 operation(s) for edit.
  name: Datadog Edit API
  phrasing_intents:
  - id: UpdateAPIKey
    intent: Edit an API key
    question: How do I rename an existing API key?
  - id: UpdateAuthNMapping
    intent: Edit an AuthN mapping
    question: How do I change which role a SAML attribute maps to?
  phrasing_ops: 2
  slug: datadog-edit-api
- baseURL: https://api.datadoghq.com
  baseurl_source: declared
  description: The Emails API from Datadog — 1 operation(s) for emails.
  name: Datadog Emails API
  phrasing_intents:
  - id: SendInvitations
    intent: Send invitation emails to users
    question: Can I invite several people to my organization at once by email?
  phrasing_ops: 1
  slug: datadog-emails-api
- baseURL: https://api.datadoghq.com
  baseurl_source: declared
  description: The Entities API from Datadog — 1 operation(s) for entities.
  name: Datadog Entities API
  phrasing_intents:
  - id: ListCatalogEntity
    intent: List Software Catalog entities
    question: Which services are registered in the Software Catalog?
  phrasing_ops: 1
  slug: datadog-entities-api
- baseURL: https://api.datadoghq.com
  baseurl_source: declared
  description: The Entity API from Datadog — 2 operation(s) for entity.
  name: Datadog Entity API
  phrasing_intents:
  - id: ListCatalogRelation
    intent: List Software Catalog entity relations
    question: What depends on a given service in the Software Catalog?
  phrasing_ops: 1
  slug: datadog-entity-api
- baseURL: https://api.datadoghq.com
  baseurl_source: declared
  description: The Escalate API from Datadog — 1 operation(s) for escalate.
  name: Datadog Escalate API
  phrasing_intents:
  - id: EscalateOnCallPage
    intent: Escalate an On-Call page
    question: How do I escalate a page to the next level right away?
  phrasing_ops: 1
  slug: datadog-escalate-api
- baseURL: https://api.datadoghq.com
  baseurl_source: declared
  description: The Event Management API allows you to programmatically post events to the Events Explorer and fetch events from the Events Explorer. See the [Event Management page](https://docs.datadoghq.com/service
  name: Datadog Events API
  phrasing_intents:
  - id: CreateCIAppPipelineEvent
    intent: Send a CI pipeline event
    question: How do I report a pipeline run from an unsupported CI provider to CI Visibility?
  - id: ListCIAppPipelineEvents
    intent: List CI pipeline events
    question: Which CI pipelines ran in the last hour?
  - id: SearchCIAppPipelineEvents
    intent: Search CI pipeline events with complex filters
    question: How do I run a complex search across CI pipeline events?
  - id: ListCIAppTestEvents
    intent: List CI test events
    question: Which tests ran in my CI recently?
  - id: SearchCIAppTestEvents
    intent: Search CI test events with complex filters
    question: How can I search CI test events, for example to find flaky failures?
  - id: ListDORAFailures
    intent: List DORA failure events
    question: Which DORA failure events have been recorded for my services?
  - id: GetDORAFailure
    intent: Get a DORA failure event
    question: How can I look up one DORA failure event by ID?
  - id: CreateDORAIncident
    intent: Send an incident event for DORA metrics
    question: How do I feed incident data into DORA change failure rate and time to restore?
  phrasing_ops: 14
  slug: datadog-events-api
- baseURL: https://api.datadoghq.com
  baseurl_source: declared
  description: The Execute API from Datadog — 1 operation(s) for execute.
  name: Datadog Execute API
  phrasing_intents:
  - id: CreateWorkflowInstance
    intent: Run a workflow
    question: Can I trigger a Workflow Automation run from code?
  phrasing_ops: 1
  slug: datadog-execute-api
- baseURL: https://api.datadoghq.com
  baseurl_source: declared
  description: The Existing API from Datadog — 12 operation(s) for existing.
  name: Datadog Existing API
  phrasing_intents:
  - id: UpdateIncident
    intent: Update an incident
    question: How do I change an incident's severity or status?
  - id: UpdateIncidentIntegration
    intent: Update an incident's integration metadata
    question: Can I edit the integration metadata linked to an incident?
  - id: UpdateScorecardRule
    intent: Update a Scorecard rule
    question: How do I edit a Scorecard rule that grades my services?
  - id: UpdateSecurityMonitoringRule
    intent: Update a security detection rule
    question: Must I resend every query when I modify a security detection rule?
  - id: TestExistingSecurityMonitoringRule
    intent: Test an existing security detection rule
    question: Can I test a detection rule I already saved against sample payloads?
  - id: UpdateIncidentService
    intent: Update an incident service
    question: How do I rename an incident service?
  - id: UpdateIncidentTeam
    intent: Update an incident team
    question: Can I rename an incident team?
  - id: GetWorkflow
    intent: Get a workflow
    question: How can I view a Workflow Automation workflow's definition?
  phrasing_ops: 9
  slug: datadog-existing-api
- baseURL: https://api.datadoghq.com
  baseurl_source: declared
  description: The External API from Datadog — 1 operation(s) for external.
  name: Datadog External API
  phrasing_intents:
  - id: CreateNewAWSExternalID
    intent: Generate a new AWS external ID
    question: How do I get a new external ID for the AWS role trust policy?
  phrasing_ops: 1
  slug: datadog-external-api
- baseURL: https://api.datadoghq.com
  baseurl_source: declared
  description: The Family API from Datadog — 1 operation(s) for family.
  name: Datadog Family API
  phrasing_intents:
  - id: GetHourlyUsage
    intent: Get hourly usage by product family
    question: How much infrastructure and log usage did we consume each hour?
  phrasing_ops: 1
  slug: datadog-family-api
- baseURL: https://api.datadoghq.com
  baseurl_source: declared
  description: The Filter API from Datadog — 8 operation(s) for filter.
  name: Datadog Filter API
  phrasing_intents:
  - id: GetApmRetentionFilter
    intent: Get an APM retention filter
    question: What does a specific APM retention filter keep?
  - id: UpdateApmRetentionFilter
    intent: Update an APM retention filter
    question: Can I change the sampling rate of an APM retention filter?
  - id: GetApplicationSecurityWafExclusionFilter
    intent: Get a WAF exclusion filter
    question: What traffic does a particular WAF exclusion filter skip?
  - id: UpdateApplicationSecurityWafExclusionFilter
    intent: Update a WAF exclusion filter
    question: Can I edit the paths a WAF exclusion filter applies to?
  - id: GetRetentionFilter
    intent: Get a RUM retention filter
    question: What does one RUM retention filter keep for an app?
  - id: UpdateRetentionFilter
    intent: Update a RUM retention filter
    question: Can I change how many RUM sessions a retention filter keeps?
  - id: GetSecurityFilter
    intent: Get a security filter
    question: Which logs does a given security filter exclude from analysis?
  - id: UpdateSecurityFilter
    intent: Update a security filter
    question: Can I add exclusions to an existing security filter?
  phrasing_ops: 8
  slug: datadog-filter-api
- baseURL: https://api.datadoghq.com
  baseurl_source: declared
  description: The Finding API from Datadog — 1 operation(s) for finding.
  name: Datadog Finding API
  phrasing_intents:
  - id: GetFinding
    intent: Get a posture management finding
    question: What misconfiguration does a security posture finding describe?
  phrasing_ops: 1
  slug: datadog-finding-api
- baseURL: https://api.datadoghq.com
  baseurl_source: declared
  description: The Findings API from Datadog — 1 operation(s) for findings.
  name: Datadog Findings API
  phrasing_intents:
  - id: ListFindings
    intent: List security posture findings
    question: Which misconfigurations are currently failing in my cloud accounts?
  phrasing_ops: 1
  slug: datadog-findings-api
- baseURL: https://api.datadoghq.com
  baseurl_source: declared
  description: The Get API from Datadog — 170 operation(s) for get.
  name: Datadog Get API
  phrasing_intents:
  - id: ListAwsScanOptions
    intent: List agentless scan options for AWS accounts
    question: Which AWS accounts have agentless scanning options configured?
  - id: GetAPIKey
    intent: Look up a single API key
    question: How do I look up the details of one Datadog API key?
  - id: GetOpenAPI
    intent: Download an API catalog entry as OpenAPI
    question: Can I export an API from the API catalog as an OpenAPI file?
  - id: GetSpansMetric
    intent: Get a span-based metric
    question: What filter and aggregation does one of my span-based metrics use?
  - id: GetAuthNMapping
    intent: Get an AuthN mapping
    question: Which role does a particular SAML attribute AuthN mapping assign?
  - id: GetProject
    intent: Get a Case Management project
    question: How do I see the details of a Case Management project?
  - id: GetDowntime
    intent: Get a scheduled downtime
    question: When does a particular downtime start and end, and what does it silence?
  - id: ListIncidents
    intent: List incidents in the organization
    question: What incidents does my organization have open or recorded in Datadog?
  phrasing_ops: 72
  slug: datadog-get-api
- baseURL: https://api.datadoghq.com
  baseurl_source: declared
  description: The Grants API from Datadog — 3 operation(s) for grants.
  name: Datadog Grants API
  phrasing_intents:
  - id: AddRoleToRestrictionQuery
    intent: Grant a role to a logs restriction query
    question: How do I apply a logs restriction query to a role?
  - id: AddPermissionToRole
    intent: Grant a permission to a role
    question: How do I give a role an extra permission?
  phrasing_ops: 2
  slug: datadog-grants-api
- baseURL: https://api.datadoghq.com
  baseurl_source: declared
  description: The Groups API from Datadog — 5 operation(s) for groups.
  name: Datadog Groups API
  phrasing_intents:
  - id: ListSCIMGroups
    intent: List SCIM groups
    question: Which groups have been provisioned into my organization over SCIM?
  - id: PatchSCIMGroup
    intent: Patch a SCIM group
    question: How do I add or remove a single member from a SCIM group without replacing it?
  - id: UpdateSCIMGroup
    intent: Replace a SCIM group
    question: How do I replace a SCIM group's name and full member list in one call?
  - id: ListScanningGroups
    intent: List Sensitive Data Scanner groups
    question: Which Sensitive Data Scanner groups are configured in my org?
  - id: ReorderScanningGroups
    intent: Reorder Sensitive Data Scanner groups
    question: How do I change the order in which scanning groups are evaluated?
  - id: UpdateScanningGroup
    intent: Update a scanning group and its rule order
    question: How do I change the filter or settings of one Sensitive Data Scanner group?
  phrasing_ops: 6
  slug: datadog-groups-api
- baseURL: https://api.datadoghq.com
  baseurl_source: declared
  description: The Handle API from Datadog — 4 operation(s) for handle.
  name: Datadog Handle API
  phrasing_intents:
  - id: UpdateTenantBasedHandle
    intent: Update a Microsoft Teams tenant-based handle
    question: Can I repoint a tenant-based Teams handle to a different channel?
  - id: UpdateWorkflowsWebhookHandle
    intent: Update a Teams Workflows webhook handle
    question: Can I change the webhook URL behind a Workflows handle?
  phrasing_ops: 2
  slug: datadog-handle-api
- baseURL: https://api.datadoghq.com
  baseurl_source: declared
  description: The Historical API from Datadog — 3 operation(s) for historical.
  name: Datadog Historical API
  phrasing_intents:
  - id: ListHistoricalJobs
    intent: List historical detection jobs
    question: Which SIEM historical detection jobs have I run?
  - id: RunHistoricalJob
    intent: Run a historical detection job
    question: How do I run a detection rule against past logs?
  phrasing_ops: 2
  slug: datadog-historical-api
- baseURL: https://api.datadoghq.com
  baseurl_source: declared
  description: The Incident API from Datadog — 14 operation(s) for incident.
  name: Datadog Incident API
  phrasing_intents:
  - id: UpdateIncidentType
    intent: Update an incident type
    question: How do I rename or redescribe an incident type?
  - id: UpdateIncidentTodo
    intent: Update an incident todo
    question: How do I mark an incident todo as completed?
  phrasing_ops: 2
  slug: datadog-incident-api
- baseURL: https://api.datadoghq.com
  baseurl_source: declared
  description: The Instances API from Datadog — 1 operation(s) for instances.
  name: Datadog Instances API
  phrasing_intents:
  - id: ListWorkflowInstances
    intent: List a workflow's executions
    question: What runs has this workflow had recently?
  phrasing_ops: 1
  slug: datadog-instances-api
- baseURL: https://api.datadoghq.com
  baseurl_source: declared
  description: The Integration API from Datadog — 4 operation(s) for integration.
  name: Datadog Integration API
  phrasing_intents:
  - id: UpdateAWSAccount
    intent: Update an AWS account integration
    question: Can I change the regions or namespaces collected for an AWS account?
  phrasing_ops: 1
  slug: datadog-integration-api
- baseURL: https://api.datadoghq.com
  baseurl_source: declared
  description: The Ip API from Datadog — 1 operation(s) for ip.
  name: Datadog Ip API
  phrasing_intents:
  - id: UpdateIPAllowlist
    intent: Edit the IP allowlist
    question: How do I add an office IP range to the allowlist?
  phrasing_ops: 1
  slug: datadog-ip-api
- baseURL: https://api.datadoghq.com
  baseurl_source: declared
  description: The Link API from Datadog — 2 operation(s) for link.
  name: Datadog Link API
  phrasing_intents:
  - id: DeleteTeamLink
    intent: Remove a link from a team
    question: Can I remove an outdated link from a team's page?
  - id: UpdateTeamLink
    intent: Update a team link
    question: Can I change the URL or label of a team link?
  phrasing_ops: 2
  slug: datadog-link-api
- baseURL: https://api.datadoghq.com
  baseurl_source: declared
  description: The Lists API from Datadog — 75 operation(s) for lists.
  name: Datadog Lists API
  phrasing_intents:
  - id: ListAPIs
    intent: List APIs in the API Catalog
    question: Which APIs are registered in our API Catalog, and what are their IDs?
  - id: GetResourceEvaluationFilters
    intent: List cloud resource evaluation filters
    question: Which resource filters are excluding cloud resources from security evaluation?
  - id: ListFastlyServices
    intent: List Fastly services for an account
    question: Which Fastly services are attached to my connected Fastly account?
  - id: ListRestrictionQueries
    intent: List log restriction queries
    question: Which log restriction queries exist in my organization?
  - id: ListRestrictionQueryRoles
    intent: List roles that have a restriction query
    question: Which roles are bound to a given log restriction query?
  - id: ListTagsByMetricName
    intent: List indexed tags for a metric
    question: What tag key-value pairs are indexed on a metric?
  - id: ListVolumesByMetricName
    intent: Get distinct volumes for a metric
    question: How many distinct custom metric volumes is one metric producing?
  - id: ListOrgConfigs
    intent: List organization configs
    question: What org-level configuration settings are set for my organization?
  phrasing_ops: 16
  slug: datadog-lists-api
- baseURL: https://api.datadoghq.com
  baseurl_source: declared
  description: Aggregate and analyze log data
  name: Datadog Log Aggregation API
  phrasing_intents:
  - id: aggregateLogs
    intent: Compute aggregations over logs
    question: Can I get the 95th percentile of a log attribute grouped by facet?
  phrasing_ops: 1
  slug: datadog-log-aggregation-api
- baseURL: https://api.datadoghq.com
  baseurl_source: declared
  description: Manage log indexes and retention policies
  name: Datadog Log Indexes API
  phrasing_intents:
  - id: listLogIndexes
    intent: List log indexes
    question: Which log indexes are configured and in what order are they evaluated?
  - id: getLogIndex
    intent: Get one log index's configuration
    question: Can I see the exclusion filters and retention of one log index?
  phrasing_ops: 2
  slug: datadog-log-indexes-api
- baseURL: https://api.datadoghq.com
  baseurl_source: declared
  description: Search your logs and send them to your Datadog platform over HTTP. See the [Log Management page](https://docs.datadoghq.com/logs/) for more information.
  name: Datadog Logs API
  phrasing_intents:
  - id: SubmitLog
    intent: Send logs over HTTP
    question: How do I ship logs to Datadog over HTTP without an agent?
  - id: ListLogs
    intent: Search logs
    question: How can I search my logs for errors from a service?
  phrasing_ops: 2
  slug: datadog-logs-api
- baseURL: https://api.datadoghq.com
  baseurl_source: declared
  description: Manage metric tag configurations
  name: Datadog Metric Tags API
  phrasing_intents:
  - id: getMetricTagConfiguration
    intent: Get a custom metric's tag configuration
    question: Which tag keys and aggregations are configured on a custom metric?
  - id: createMetricTagConfiguration
    intent: Create a custom metric's tag configuration
    question: How do I choose which tag keys to keep on a custom metric?
  - id: updateMetricTagConfiguration
    intent: Update a custom metric's tag configuration
    question: Can I partially update the tag keys on a custom metric with a merge patch?
  - id: deleteMetricTagConfiguration
    intent: Delete a custom metric's tag configuration
    question: What happens to my custom metric usage if I delete a tag configuration?
  phrasing_ops: 4
  slug: datadog-metric-tags-api
- baseURL: https://api.datadoghq.com
  baseurl_source: declared
  description: 'The metrics endpoint allows you to: - Post metrics data so it can be graphed on Datadog’s dashboards - Query metrics from any time period (timeseries and scalar) - Modify tag configurations for metric'
  name: Datadog Metrics API
  phrasing_intents:
  - id: UpdateSpansMetric
    intent: Update a span-based metric
    question: Can I change the group-by tags on a span-based metric?
  - id: UpdateLogsMetric
    intent: Update a log-based metric
    question: Can I change the grouping on a metric generated from logs?
  - id: UpdateRumMetric
    intent: Update a RUM-based metric
    question: Can I edit a metric generated from RUM events?
  - id: SubmitMetrics
    intent: Submit custom metric data points
    question: How do I send my own time-series metrics to Datadog?
  - id: queryMetricsTimeseries
    intent: Query metric timeseries data
    question: Can I pull metric values over time for a chart outside Datadog?
  - id: queryMetricsScalar
    intent: Query a scalar metric value
    question: What was the average latency over the last day as a single number?
  phrasing_ops: 6
  slug: datadog-metrics-api
- baseURL: https://api.datadoghq.com
  baseurl_source: declared
  description: The Monitor API from Datadog — 5 operation(s) for monitor.
  name: Datadog Monitor API
  phrasing_intents:
  - id: UpdateMonitorNotificationRule
    intent: Update a monitor notification rule
    question: Can I change the recipients of a monitor notification rule?
  phrasing_ops: 1
  slug: datadog-monitor-api
- baseURL: https://api.datadoghq.com
  baseurl_source: declared
  description: Mute and unmute monitors to suppress notifications
  name: Datadog Monitor Muting API
  phrasing_intents:
  - id: muteMonitor
    intent: Mute a monitor
    question: How do I silence alerts from a monitor during maintenance?
  - id: unmuteMonitor
    intent: Unmute a monitor
    question: How do I turn alert notifications back on for a muted monitor?
  phrasing_ops: 2
  slug: datadog-monitor-muting-api
- baseURL: https://api.datadoghq.com
  baseurl_source: declared
  description: Validate monitor configurations before creation
  name: Datadog Monitor Validation API
  phrasing_intents:
  - id: validateMonitor
    intent: Validate a monitor without creating it
    question: Can I check whether a monitor query is valid before I create it?
  phrasing_ops: 1
  slug: datadog-monitor-validation-api
- baseURL: https://api.datadoghq.com
  baseurl_source: declared
  description: Create, read, update, and delete monitors
  name: Datadog Monitors API
  phrasing_intents:
  - id: createMonitor
    intent: Create a monitor
    question: How do I set up an alert when a metric crosses a threshold?
  - id: listMonitors
    intent: List monitors
    question: Which monitors are currently alerting?
  - id: getMonitor
    intent: Get a monitor
    question: What's the current status and query of a given monitor?
  - id: updateMonitor
    intent: Edit a monitor
    question: Can I change the threshold or query of an existing monitor?
  - id: deleteMonitor
    intent: Delete a monitor
    question: Can I delete a monitor that an SLO still references?
  phrasing_ops: 5
  slug: datadog-monitors-api
- baseURL: https://api.datadoghq.com
  baseurl_source: declared
  description: The Objects API from Datadog — 2 operation(s) for objects.
  name: Datadog Objects API
  phrasing_intents:
  - id: UpdateOpsgenieService
    intent: Update an Opsgenie service object
    question: Can I change the region or key of an Opsgenie service?
  phrasing_ops: 1
  slug: datadog-objects-api
- baseURL: https://api.datadoghq.com
  baseurl_source: declared
  description: The Observability API from Datadog — 2 operation(s) for observability.
  name: Datadog Observability API
  phrasing_intents:
  - id: ValidatePipeline
    intent: Validate an Observability Pipeline config
    question: Can I check an Observability Pipelines configuration for errors before saving?
  phrasing_ops: 1
  slug: datadog-observability-api
- baseURL: https://api.datadoghq.com
  baseurl_source: declared
  description: The Options API from Datadog — 2 operation(s) for options.
  name: Datadog Options API
  phrasing_intents:
  - id: CreateAwsScanOptions
    intent: Activate Agentless scanning for an AWS account
    question: How do I turn on Agentless scanning for an AWS account?
  - id: UpdateAwsScanOptions
    intent: Update Agentless scan options for an AWS account
    question: Can I change which Agentless scans run on an already activated AWS account?
  phrasing_ops: 2
  slug: datadog-options-api
- baseURL: https://api.datadoghq.com
  baseurl_source: declared
  description: The Order API from Datadog — 2 operation(s) for order.
  name: Datadog Order API
  phrasing_intents:
  - id: OrderRetentionFilters
    intent: Reorder RUM retention filters
    question: Can I change the order RUM retention filters are evaluated in?
  phrasing_ops: 1
  slug: datadog-order-api
- baseURL: https://api.datadoghq.com
  baseurl_source: declared
  description: The Pages API from Datadog — 4 operation(s) for pages.
  name: Datadog Pages API
  phrasing_intents:
  - id: ResolveOnCallPage
    intent: Resolve an On-Call page
    question: How do I close out an On-Call page once the issue is fixed?
  phrasing_ops: 1
  slug: datadog-pages-api
- baseURL: https://api.datadoghq.com
  baseurl_source: declared
  description: The Patch API from Datadog — 5 operation(s) for patch.
  name: Datadog Patch API
  phrasing_intents:
  - id: PatchSCIMUser
    intent: Patch a SCIM user
    question: How do I deactivate or rename a user through SCIM?
  - id: PatchSignalNotificationRule
    intent: Patch a security signal notification rule
    question: How do I change only the recipients of a security signal notification rule?
  - id: PatchVulnerabilityNotificationRule
    intent: Patch a vulnerability notification rule
    question: How do I change the targets of a vulnerability notification rule?
  phrasing_ops: 3
  slug: datadog-patch-api
- baseURL: https://api.datadoghq.com
  baseurl_source: declared
  description: The Permissions API from Datadog — 5 operation(s) for permissions.
  name: Datadog Permissions API
  phrasing_intents:
  - id: RemovePermissionFromRole
    intent: Revoke a permission from a role
    question: Can I take a single permission away from a role?
  - id: UpdateTeamPermissionSetting
    intent: Update a team's permission setting
    question: Can I control who is allowed to edit a team or manage its members?
  phrasing_ops: 2
  slug: datadog-permissions-api
- baseURL: https://api.datadoghq.com
  baseurl_source: declared
  description: The Pipelines API from Datadog — 8 operation(s) for pipelines.
  name: Datadog Pipelines API
  phrasing_intents:
  - id: UpdatePipeline
    intent: Update an Observability Pipeline
    question: Can I change the sources or destinations of an existing pipeline?
  phrasing_ops: 1
  slug: datadog-pipelines-api
- baseURL: https://api.datadoghq.com
  baseurl_source: declared
  description: The Policies API from Datadog — 9 operation(s) for policies.
  name: Datadog Policies API
  phrasing_intents:
  - id: UpdateOnCallEscalationPolicy
    intent: Update an On-Call escalation policy
    question: Can I change the steps or targets of an On-Call escalation policy?
  - id: UpdateCSMThreatsAgentPolicy
    intent: Update a Workload Protection policy
    question: Can I enable or rename a Workload Protection agent policy?
  - id: UpdateRestrictionPolicy
    intent: Set who can access a resource
    question: How do I restrict who can edit a specific dashboard?
  phrasing_ops: 3
  slug: datadog-policies-api
- baseURL: https://api.datadoghq.com
  baseurl_source: declared
  description: The Projects API from Datadog — 2 operation(s) for projects.
  name: Datadog Projects API
  phrasing_intents:
  - id: DeleteProject
    intent: Remove a Case Management project
    question: How do I delete a Case Management project?
  phrasing_ops: 1
  slug: datadog-projects-api
- baseURL: https://api.datadoghq.com
  baseurl_source: declared
  description: The Queries API from Datadog — 7 operation(s) for queries.
  name: Datadog Queries API
  phrasing_intents:
  - id: UpdateRestrictionQuery
    intent: Edit a logs restriction query
    question: How do I change the query on a logs restriction query?
  - id: RemoveRoleFromRestrictionQuery
    intent: Remove a role from a logs restriction query
    question: Can I unassign a role from a logs restriction query?
  phrasing_ops: 2
  slug: datadog-queries-api
- baseURL: https://api.datadoghq.com
  baseurl_source: declared
  description: The Remove API from Datadog — 5 operation(s) for remove.
  name: Datadog Remove API
  phrasing_intents:
  - id: RemoveUserFromRole
    intent: Remove a user from a role
    question: Can I take a role away from a user without deleting the user?
  - id: DeleteTeam
    intent: Delete a team
    question: Can I delete a team that's been disbanded?
  - id: DeleteTeamMembership
    intent: Remove a user from a team
    question: Can I take one person off a team?
  phrasing_ops: 3
  slug: datadog-remove-api
- baseURL: https://api.datadoghq.com
  baseurl_source: declared
  description: The Resource API from Datadog — 3 operation(s) for resource.
  name: Datadog Resource API
  phrasing_intents:
  - id: UpdateResourceEvaluationFilters
    intent: Update cloud security resource filters
    question: Can I exclude certain cloud resources from security evaluation?
  phrasing_ops: 1
  slug: datadog-resource-api
- baseURL: https://api.datadoghq.com
  baseurl_source: declared
  description: The Retention API from Datadog — 6 operation(s) for retention.
  name: Datadog Retention API
  phrasing_intents:
  - id: ReorderApmRetentionFilters
    intent: Reorder APM retention filters
    question: How do I change the order my APM retention filters are evaluated in?
  phrasing_ops: 1
  slug: datadog-retention-api
- baseURL: https://api.datadoghq.com
  baseurl_source: declared
  description: The Role API from Datadog — 8 operation(s) for role.
  name: Datadog Role API
  phrasing_intents:
  - id: UpdateRole
    intent: Edit a role
    question: Can I rename a role or change its settings?
  phrasing_ops: 1
  slug: datadog-role-api
- baseURL: https://api.datadoghq.com
  baseurl_source: declared
  description: The Routing API from Datadog — 1 operation(s) for routing.
  name: Datadog Routing API
  phrasing_intents:
  - id: SetOnCallTeamRoutingRules
    intent: Set a team's On-Call routing rules
    question: How do I configure where pages for a team get routed in On-Call?
  phrasing_ops: 1
  slug: datadog-routing-api
- baseURL: https://api.datadoghq.com
  baseurl_source: declared
  description: The Rules API from Datadog — 27 operation(s) for rules.
  name: Datadog Rules API
  phrasing_intents:
  - id: UpdateSecurityMonitoringSuppression
    intent: Update a security suppression rule
    question: Can I change the query of an existing suppression rule?
  - id: TestSecurityMonitoringRule
    intent: Test a new detection rule before saving
    question: Can I test a detection rule definition before I create it?
  - id: UpdateScanningRule
    intent: Update a Sensitive Data Scanner rule
    question: Can I change the regex of a Sensitive Data Scanner rule?
  phrasing_ops: 3
  slug: datadog-rules-api
- baseURL: https://api.datadoghq.com
  baseurl_source: declared
  description: The Schedules API from Datadog — 4 operation(s) for schedules.
  name: Datadog Schedules API
  phrasing_intents:
  - id: CreateDowntime
    intent: Schedule a downtime
    question: How do I schedule a downtime to silence monitors during a deploy?
  - id: UpdateOnCallSchedule
    intent: Update an On-Call schedule
    question: How do I change the rotation layers of an On-Call schedule?
  phrasing_ops: 2
  slug: datadog-schedules-api
- baseURL: https://api.datadoghq.com
  baseurl_source: declared
  description: The Search API from Datadog — 10 operation(s) for search.
  name: Datadog Search API
  phrasing_intents:
  - id: SearchIncidents
    intent: Search incidents
    question: Which incidents are still active?
  - id: ListSpans
    intent: Search APM spans
    question: Can I search individual trace spans with a complex query?
  phrasing_ops: 2
  slug: datadog-search-api
- baseURL: https://api.datadoghq.com
  baseurl_source: declared
  description: The Specific API from Datadog — 2 operation(s) for specific.
  name: Datadog Specific API
  phrasing_intents:
  - id: UpdateOrgConfig
    intent: Update an org config setting
    question: Can I change an organization-level config value through the API?
  phrasing_ops: 1
  slug: datadog-specific-api
- baseURL: https://api.datadoghq.com
  baseurl_source: declared
  description: View and manage teams within Datadog. See the [Teams page](https://docs.datadoghq.com/account_management/teams/) for more information.
  name: Datadog Teams API
  phrasing_intents:
  - id: UpdateTeam
    intent: Update a team
    question: How do I rename a team or change its description?
  phrasing_ops: 1
  slug: datadog-teams-api
- baseURL: https://api.datadoghq.com
  baseurl_source: declared
  description: The Update API from Datadog — 72 operation(s) for update.
  name: Datadog Update API
  phrasing_intents:
  - id: UpdateOpenAPI
    intent: Replace an API's OpenAPI definition in the catalog
    question: How do I upload a new OpenAPI file for an API already in the catalog?
  - id: UpdateDowntime
    intent: Update a downtime
    question: Can I extend or reschedule a downtime that's already set?
  - id: UpdateFastlyService
    intent: Update a Fastly service
    question: How do I change tags on a Fastly service I'm monitoring?
  - id: UpdatePowerpack
    intent: Update a powerpack
    question: Can I change the widgets in an existing powerpack?
  - id: UpdateSCIMUser
    intent: Replace a SCIM user's attributes
    question: How does my identity provider deactivate a user over SCIM?
  - id: UpdateUser
    intent: Edit a user
    question: How do I change a user's name or disable them as an admin?
  phrasing_ops: 6
  slug: datadog-update-api
- baseURL: https://api.datadoghq.com
  baseurl_source: declared
  description: The Upload API from Datadog — 2 operation(s) for upload.
  name: Datadog Upload API
  phrasing_intents:
  - id: UploadIdPMetadata
    intent: Upload SAML IdP metadata
    question: Can I upload my identity provider's metadata to set up SAML login?
  phrasing_ops: 1
  slug: datadog-upload-api
- baseURL: https://api.datadoghq.com
  baseurl_source: declared
  description: View and manage metric metadata and active metrics
  name: Datadog Metric Meta Data API
  phrasing_intents:
  - id: listActiveMetrics
    intent: List actively reporting metrics
    question: Which metrics are actively reporting right now?
  phrasing_ops: 1
  slug: datadog-metric-meta-data-api
arazzos:
- description: Search monitors by tag, then mute a matched monitor to silence alerts.
  name: Datadog Bulk Mute Monitors
  slug: datadog-bulk-mute-monitors-workflow
- description: List monitors by tag, then delete a matched stale monitor.
  name: Datadog Cleanup Stale Monitors
  slug: datadog-cleanup-stale-monitors-workflow
- description: Declare an incident, read it back, then list incidents.
  name: Datadog Create an Incident
  slug: datadog-create-incident-workflow
- description: Create a logs archive backed by an S3 destination then read it back.
  name: Datadog Create a Logs Archive
  slug: datadog-create-log-archive-workflow
- description: Create a log-based metric from a query then read it back.
  name: Datadog Create a Log-based Metric
  slug: datadog-create-log-metric-workflow
- description: Create an observability pipeline, retrieve it, then list pipelines to confirm placement.
  name: Datadog Create an Observability Pipeline
  slug: datadog-create-log-pipeline-workflow
- description: Create a tag monitor configuration policy, read it back, then list policies.
  name: Datadog Create a Monitor Configuration Policy
  slug: datadog-create-monitor-config-policy-workflow
- description: Create a Datadog monitor, read it back, and validate the configuration.
  name: Datadog Create a Monitor
  slug: datadog-create-monitor-workflow
- description: Create a role, read it back, then list roles.
  name: Datadog Create a Role
  slug: datadog-create-role-workflow
- description: Create a service account, mint an application key for it, then read the key back.
  name: Datadog Create a Service Account and Application Key
  slug: datadog-create-service-account-key-workflow
- description: Create a team, read it back, then list teams.
  name: Datadog Create a Team
  slug: datadog-create-team-workflow
- description: Create an incident, update its details, then add a follow-up todo entry.
  name: Datadog Declare an Incident
  slug: datadog-declare-incident-workflow
- description: Submit log entries to Datadog then search the platform for those logs.
  name: Datadog Ingest and Search Logs
  slug: datadog-ingest-and-search-logs-workflow
- description: Create (invite) a user for the organization, read it back, then list users.
  name: Datadog Invite a User
  slug: datadog-invite-user-workflow
- description: Create an API key, read it back, then list all API keys for the org.
  name: Datadog Manage API Keys
  slug: datadog-manage-api-keys-workflow
- description: List an incident's attachments then add a link attachment via bulk update.
  name: Datadog Manage Incident Attachments
  slug: datadog-manage-incident-attachments-workflow
- description: Read a metric's tag configuration, then update its tags and metadata.
  name: Datadog Manage Metric Metadata
  slug: datadog-manage-metric-metadata-workflow
- description: Fetch a Datadog monitor, then mute it to suppress alert notifications.
  name: Datadog Mute a Monitor
  slug: datadog-mute-monitor-workflow
- description: Post an event to the Events Explorer, then search events to find it.
  name: Datadog Post and Search Events
  slug: datadog-post-and-search-events-workflow
- description: Retrieve an incident then update its state to resolved.
  name: Datadog Resolve an Incident
  slug: datadog-resolve-incident-workflow
- description: Schedule a downtime for monitors matching a scope, confirm it, then cancel it.
  name: Datadog Schedule a Downtime
  slug: datadog-schedule-downtime-workflow
- description: Search incidents by a facet query then fetch the first match by id.
  name: Datadog Search Incidents
  slug: datadog-search-incidents-workflow
- description: Submit a metric series, then query it back as timeseries data.
  name: Datadog Submit and Query Metrics
  slug: datadog-submit-and-query-metrics-workflow
- description: Fetch a Datadog monitor, then update its options and alert thresholds.
  name: Datadog Tune Monitor Thresholds
  slug: datadog-tune-monitor-thresholds-workflow
artifact_total: 678
collections:
- collection_type: postman
  name: Datadog API
  slug: postman-datadog-api
- collection_type: postman
  name: Datadog Events API
  slug: postman-datadog-events
- collection_type: postman
  name: Datadog Incidents API
  slug: postman-datadog-incidents
- collection_type: postman
  name: Datadog Logs API
  slug: postman-datadog-logs
- collection_type: postman
  name: Datadog Metrics API
  slug: postman-datadog-metrics
- collection_type: postman
  name: Datadog Monitors API
  slug: postman-datadog-monitors
- collection_type: open
  name: Datadog Account API
  slug: open-datadog-account-api
- collection_type: open
  name: Datadog Account Accounts API
  slug: open-datadog-accounts-api
- collection_type: open
  name: Datadog Account Acknowledge API
  slug: open-datadog-acknowledge-api
- collection_type: open
  name: Datadog Account Across API
  slug: open-datadog-across-api
- collection_type: open
  name: Datadog Account Action API
  slug: open-datadog-action-api
- collection_type: open
  name: Datadog Account Active API
  slug: open-datadog-active-api
- collection_type: open
  name: Datadog Account Add API
  slug: open-datadog-add-api
- collection_type: open
  name: Datadog Account Agent API
  slug: open-datadog-agent-api
- collection_type: open
  name: Datadog Account Agents API
  slug: open-datadog-agents-api
- collection_type: open
  name: Datadog Account Aggregate API
  slug: open-datadog-aggregate-api
- collection_type: open
  name: Datadog Account Aggregated API
  slug: open-datadog-aggregated-api
- collection_type: open
  name: Datadog Account Aggregations API
  slug: open-datadog-aggregations-api
- collection_type: open
  name: Datadog Account All API
  slug: open-datadog-all-api
- collection_type: open
  name: Datadog Account Analysis API
  slug: open-datadog-analysis-api
- collection_type: open
  name: Datadog API
  slug: open-datadog-api
- collection_type: open
  name: Datadog Account Applications API
  slug: open-datadog-applications-api
- collection_type: open
  name: Datadog Account Archive API
  slug: open-datadog-archive-api
- collection_type: open
  name: Datadog Account Archives API
  slug: open-datadog-archives-api
- collection_type: open
  name: Datadog Account Assets API
  slug: open-datadog-assets-api
- collection_type: open
  name: Datadog Account Assign API
  slug: open-datadog-assign-api
- collection_type: open
  name: Datadog Account Assignee API
  slug: open-datadog-assignee-api
- collection_type: open
  name: Datadog Account Attachments API
  slug: open-datadog-attachments-api
- collection_type: open
  name: Datadog Account Attributes API
  slug: open-datadog-attributes-api
- collection_type: open
  name: Datadog Account Audit API
  slug: open-datadog-audit-api
- collection_type: open
  name: Datadog Account Available API
  slug: open-datadog-available-api
- collection_type: open
  name: Datadog Account Batch API
  slug: open-datadog-batch-api
- collection_type: open
  name: Datadog Account Billing API
  slug: open-datadog-billing-api
- collection_type: open
  name: Datadog Account Budget API
  slug: open-datadog-budget-api
- collection_type: open
  name: Datadog Account Budgets API
  slug: open-datadog-budgets-api
- collection_type: open
  name: Datadog Account Cancel API
  slug: open-datadog-cancel-api
- collection_type: open
  name: Datadog Account Cap API
  slug: open-datadog-cap-api
- collection_type: open
  name: Datadog Account Cardinality API
  slug: open-datadog-cardinality-api
- collection_type: open
  name: Datadog Account Case API
  slug: open-datadog-case-api
- collection_type: open
  name: Datadog Account Cases API
  slug: open-datadog-cases-api
- collection_type: open
  name: Datadog Account Change API
  slug: open-datadog-change-api
- collection_type: open
  name: Datadog Account Channel API
  slug: open-datadog-channel-api
- collection_type: open
  name: Datadog Account Cloud API
  slug: open-datadog-cloud-api
- collection_type: open
  name: Datadog Account Cloudflare API
  slug: open-datadog-cloudflare-api
- collection_type: open
  name: Datadog Account Configuration API
  slug: open-datadog-configuration-api
- collection_type: open
  name: Datadog Account Configure API
  slug: open-datadog-configure-api
- collection_type: open
  name: Datadog Account Connection API
  slug: open-datadog-connection-api
- collection_type: open
  name: Datadog Account Connections API
  slug: open-datadog-connections-api
- collection_type: open
  name: Datadog Account Containers API
  slug: open-datadog-containers-api
- collection_type: open
  name: Datadog Account Convert API
  slug: open-datadog-convert-api
- collection_type: open
  name: Datadog Account Cost API
  slug: open-datadog-cost-api
- collection_type: open
  name: Datadog Account Coverage API
  slug: open-datadog-coverage-api
- collection_type: open
  name: Datadog Account Create API
  slug: open-datadog-create-api
- collection_type: open
  name: Datadog Account Current API
  slug: open-datadog-current-api
- collection_type: open
  name: Datadog Account Custom API
  slug: open-datadog-custom-api
- collection_type: open
  name: Datadog Account Dashboards API
  slug: open-datadog-dashboards-api
- collection_type: open
  name: Datadog Account Data API
  slug: open-datadog-data-api
- collection_type: open
  name: Datadog Account Definition API
  slug: open-datadog-definition-api
- collection_type: open
  name: Datadog Account Definitions API
  slug: open-datadog-definitions-api
- collection_type: open
  name: Datadog Account Delegate API
  slug: open-datadog-delegate-api
- collection_type: open
  name: Datadog Account Delete API
  slug: open-datadog-delete-api
- collection_type: open
  name: Datadog Account Demand API
  slug: open-datadog-demand-api
- collection_type: open
  name: Datadog Account Deployments API
  slug: open-datadog-deployments-api
- collection_type: open
  name: Datadog Account Destination API
  slug: open-datadog-destination-api
- collection_type: open
  name: Datadog Account Destinations API
  slug: open-datadog-destinations-api
- collection_type: open
  name: Datadog Account Detection API
  slug: open-datadog-detection-api
- collection_type: open
  name: Datadog Account Devices API
  slug: open-datadog-devices-api
- collection_type: open
  name: Datadog Account Dimension API
  slug: open-datadog-dimension-api
- collection_type: open
  name: Datadog Account Dimensions API
  slug: open-datadog-dimensions-api
- collection_type: open
  name: Datadog Account Disables API
  slug: open-datadog-disables-api
- collection_type: open
  name: Datadog Account Domain API
  slug: open-datadog-domain-api
- collection_type: open
  name: Datadog Account Download API
  slug: open-datadog-download-api
- collection_type: open
  name: Datadog Account Edit API
  slug: open-datadog-edit-api
- collection_type: open
  name: Datadog Account Emails API
  slug: open-datadog-emails-api
- collection_type: open
  name: Datadog Account Enabled API
  slug: open-datadog-enabled-api
- collection_type: open
  name: Datadog Account Entities API
  slug: open-datadog-entities-api
- collection_type: open
  name: Datadog Account Entity API
  slug: open-datadog-entity-api
- collection_type: open
  name: Datadog Account Entry API
  slug: open-datadog-entry-api
- collection_type: open
  name: Datadog Account Escalate API
  slug: open-datadog-escalate-api
- collection_type: open
  name: Datadog Account Events API
  slug: open-datadog-events-api
- collection_type: open
  name: Datadog Events API
  slug: open-datadog-events
- collection_type: open
  name: Datadog Account Execute API
  slug: open-datadog-execute-api
- collection_type: open
  name: Datadog Account Existing API
  slug: open-datadog-existing-api
- collection_type: open
  name: Datadog Account External API
  slug: open-datadog-external-api
- collection_type: open
  name: Datadog Account Failure API
  slug: open-datadog-failure-api
- collection_type: open
  name: Datadog Account Family API
  slug: open-datadog-family-api
- collection_type: open
  name: Datadog Account Files API
  slug: open-datadog-files-api
- collection_type: open
  name: Datadog Account Filter API
  slug: open-datadog-filter-api
- collection_type: open
  name: Datadog Account Finding API
  slug: open-datadog-finding-api
- collection_type: open
  name: Datadog Account Findings API
  slug: open-datadog-findings-api
- collection_type: open
  name: Datadog Account Framework API
  slug: open-datadog-framework-api
- collection_type: open
  name: Datadog Account Generate API
  slug: open-datadog-generate-api
- collection_type: open
  name: Datadog Account Get API
  slug: open-datadog-get-api
- collection_type: open
  name: Datadog Account Given API
  slug: open-datadog-given-api
- collection_type: open
  name: Datadog Account Grants API
  slug: open-datadog-grants-api
- collection_type: open
  name: Datadog Account Groups API
  slug: open-datadog-groups-api
- collection_type: open
  name: Datadog Account Handle API
  slug: open-datadog-handle-api
- collection_type: open
  name: Datadog Account Historical API
  slug: open-datadog-historical-api
- collection_type: open
  name: Datadog Account History API
  slug: open-datadog-history-api
- collection_type: open
  name: Datadog Account Hosts API
  slug: open-datadog-hosts-api
- collection_type: open
  name: Datadog Account Hourly API
  slug: open-datadog-hourly-api
- collection_type: open
  name: Datadog Account Identifiers API
  slug: open-datadog-identifiers-api
- collection_type: open
  name: Datadog Account Images API
  slug: open-datadog-images-api
- collection_type: open
  name: Datadog Account Incident API
  slug: open-datadog-incident-api
- collection_type: open
  name: Datadog Account Incident Teams API
  slug: open-datadog-incident-teams-api
- collection_type: open
  name: Datadog Account Incidents API
  slug: open-datadog-incidents-api
- collection_type: open
  name: Datadog Incidents API
  slug: open-datadog-incidents
- collection_type: open
  name: Datadog Account Information API
  slug: open-datadog-information-api
- collection_type: open
  name: Datadog Account Instance API
  slug: open-datadog-instance-api
- collection_type: open
  name: Datadog Account Instances API
  slug: open-datadog-instances-api
- collection_type: open
  name: Datadog Account Integration API
  slug: open-datadog-integration-api
- collection_type: open
  name: Datadog Account Integrations API
  slug: open-datadog-integrations-api
- collection_type: open
  name: Datadog Account Interfaces API
  slug: open-datadog-interfaces-api
- collection_type: open
  name: Datadog Account Invitation API
  slug: open-datadog-invitation-api
- collection_type: open
  name: Datadog Account Invocations API
  slug: open-datadog-invocations-api
- collection_type: open
  name: Datadog Account Ip API
  slug: open-datadog-ip-api
- collection_type: open
  name: Datadog Account Items API
  slug: open-datadog-items-api
- collection_type: open
  name: Datadog Account Jobs API
  slug: open-datadog-jobs-api
- collection_type: open
  name: Datadog Account Keys API
  slug: open-datadog-keys-api
- collection_type: open
  name: Datadog Account Lambda API
  slug: open-datadog-lambda-api
- collection_type: open
  name: Datadog Account Link API
  slug: open-datadog-link-api
- collection_type: open
  name: Datadog Account Links API
  slug: open-datadog-links-api
- collection_type: open
  name: Datadog Account Lists API
  slug: open-datadog-lists-api
- collection_type: open
  name: Datadog Account Log Aggregation API
  slug: open-datadog-log-aggregation-api
- collection_type: open
  name: Datadog Account Log Indexes API
  slug: open-datadog-log-indexes-api
- collection_type: open
  name: Datadog Account Logs API
  slug: open-datadog-logs-api
- collection_type: open
  name: Datadog Logs API
  slug: open-datadog-logs
- collection_type: open
  name: Datadog Account Management API
  slug: open-datadog-management-api
- collection_type: open
  name: Datadog Account Mapping API
  slug: open-datadog-mapping-api
- collection_type: open
  name: Datadog Account Memberships API
  slug: open-datadog-memberships-api
- collection_type: open
  name: Datadog Account Metric Metadata API
  slug: open-datadog-metric-metadata-api
- collection_type: open
  name: Datadog Account Metric Tags API
  slug: open-datadog-metric-tags-api
- collection_type: open
  name: Datadog Account Metrics API
  slug: open-datadog-metrics-api
- collection_type: open
  name: Datadog Metrics API
  slug: open-datadog-metrics
- collection_type: open
  name: Datadog Account Modify API
  slug: open-datadog-modify-api
- collection_type: open
  name: Datadog Account Monitor API
  slug: open-datadog-monitor-api
- collection_type: open
  name: Datadog Account Monitor Muting API
  slug: open-datadog-monitor-muting-api
- collection_type: open
  name: Datadog Account Monitor Validation API
  slug: open-datadog-monitor-validation-api
- collection_type: open
  name: Datadog Account Monitors API
  slug: open-datadog-monitors-api
- collection_type: open
  name: Datadog Monitors API
  slug: open-datadog-monitors
- collection_type: open
  name: Datadog Account Monthly API
  slug: open-datadog-monthly-api
- collection_type: open
  name: Datadog Account Multiple API
  slug: open-datadog-multiple-api
- collection_type: open
  name: Datadog Account Mute API
  slug: open-datadog-mute-api
- collection_type: open
  name: Datadog Account Names API
  slug: open-datadog-names-api
- collection_type: open
  name: Datadog Account Namespaces API
  slug: open-datadog-namespaces-api
- collection_type: open
  name: Datadog Account Objects API
  slug: open-datadog-objects-api
- collection_type: open
  name: Datadog Account Observability API
  slug: open-datadog-observability-api
- collection_type: open
  name: Datadog Account Options API
  slug: open-datadog-options-api
- collection_type: open
  name: Datadog Account Order API
  slug: open-datadog-order-api
- collection_type: open
  name: Datadog Account Organizations API
  slug: open-datadog-organizations-api
- collection_type: open
  name: Datadog Account Owned API
  slug: open-datadog-owned-api
- collection_type: open
  name: Datadog Account Pages API
  slug: open-datadog-pages-api
- collection_type: open
  name: Datadog Account Patch API
  slug: open-datadog-patch-api
- collection_type: open
  name: Datadog Account Patterns API
  slug: open-datadog-patterns-api
- collection_type: open
  name: Datadog Account Permissions API
  slug: open-datadog-permissions-api
- collection_type: open
  name: Datadog Account Pipelines API
  slug: open-datadog-pipelines-api
- collection_type: open
  name: Datadog Account Policies API
  slug: open-datadog-policies-api
- collection_type: open
  name: Datadog Account Post API
  slug: open-datadog-post-api
- collection_type: open
  name: Datadog Account Principal API
  slug: open-datadog-principal-api
- collection_type: open
  name: Datadog Account Priority API
  slug: open-datadog-priority-api
- collection_type: open
  name: Datadog Account Product API
  slug: open-datadog-product-api
- collection_type: open
  name: Datadog Account Products API
  slug: open-datadog-products-api
- collection_type: open
  name: Datadog Account Projects API
  slug: open-datadog-projects-api
- collection_type: open
  name: Datadog Account Protections API
  slug: open-datadog-protections-api
- collection_type: open
  name: Datadog Account Publish API
  slug: open-datadog-publish-api
- collection_type: open
  name: Datadog Account Queries API
  slug: open-datadog-queries-api
- collection_type: open
  name: Datadog Account Read API
  slug: open-datadog-read-api
- collection_type: open
  name: Datadog Account Ready API
  slug: open-datadog-ready-api
- collection_type: open
  name: Datadog Account Related API
  slug: open-datadog-related-api
- collection_type: open
  name: Datadog Account Remove API
  slug: open-datadog-remove-api
- collection_type: open
  name: Datadog Account Reorder API
  slug: open-datadog-reorder-api
- collection_type: open
  name: Datadog Account Reports API
  slug: open-datadog-reports-api
- collection_type: open
  name: Datadog Account Resolve API
  slug: open-datadog-resolve-api
- collection_type: open
  name: Datadog Account Resource API
  slug: open-datadog-resource-api
- collection_type: open
  name: Datadog Account Resources API
  slug: open-datadog-resources-api
- collection_type: open
  name: Datadog Account Restrictions API
  slug: open-datadog-restrictions-api
- collection_type: open
  name: Datadog Account Result API
  slug: open-datadog-result-api
- collection_type: open
  name: Datadog Account Retention API
  slug: open-datadog-retention-api
- collection_type: open
  name: Datadog Account Revoke API
  slug: open-datadog-revoke-api
- collection_type: open
  name: Datadog Account Role API
  slug: open-datadog-role-api
- collection_type: open
  name: Datadog Account Roles API
  slug: open-datadog-roles-api
- collection_type: open
  name: Datadog Account Routing API
  slug: open-datadog-routing-api
- collection_type: open
  name: Datadog Account Rules API
  slug: open-datadog-rules-api
- collection_type: open
  name: Datadog Account Rum API
  slug: open-datadog-rum-api
- collection_type: open
  name: Datadog Account Runs API
  slug: open-datadog-runs-api
- collection_type: open
  name: Datadog Account Save API
  slug: open-datadog-save-api
- collection_type: open
  name: Datadog Account Scan API
  slug: open-datadog-scan-api
- collection_type: open
  name: Datadog Account Scanning API
  slug: open-datadog-scanning-api
- collection_type: open
  name: Datadog Account Schedules API
  slug: open-datadog-schedules-api
- collection_type: open
  name: Datadog Account Search API
  slug: open-datadog-search-api
- collection_type: open
  name: Datadog Account Security API
  slug: open-datadog-security-api
- collection_type: open
  name: Datadog Account Send API
  slug: open-datadog-send-api
- collection_type: open
  name: Datadog Account Serverless API
  slug: open-datadog-serverless-api
- collection_type: open
  name: Datadog Account Sets API
  slug: open-datadog-sets-api
- collection_type: open
  name: Datadog Account Setting API
  slug: open-datadog-setting-api
- collection_type: open
  name: Datadog Account Settings API
  slug: open-datadog-settings-api
- collection_type: open
  name: Datadog Account Signal API
  slug: open-datadog-signal-api
- collection_type: open
  name: Datadog Account Single API
  slug: open-datadog-single-api
- collection_type: open
  name: Datadog Account Specific API
  slug: open-datadog-specific-api
- collection_type: open
  name: Datadog Account Standard API
  slug: open-datadog-standard-api
- collection_type: open
  name: Datadog Account State API
  slug: open-datadog-state-api
- collection_type: open
  name: Datadog Account Status API
  slug: open-datadog-status-api
- collection_type: open
  name: Datadog Account Submit API
  slug: open-datadog-submit-api
- collection_type: open
  name: Datadog Account Suppression API
  slug: open-datadog-suppression-api
- collection_type: open
  name: Datadog Account Tasks API
  slug: open-datadog-tasks-api
- collection_type: open
  name: Datadog Account Teams API
  slug: open-datadog-teams-api
- collection_type: open
  name: Datadog Account Terraform API
  slug: open-datadog-terraform-api
- collection_type: open
  name: Datadog Account Tests API
  slug: open-datadog-tests-api
- collection_type: open
  name: Datadog Account Type API
  slug: open-datadog-type-api
- collection_type: open
  name: Datadog Account Types API
  slug: open-datadog-types-api
- collection_type: open
  name: Datadog Account Unarchive API
  slug: open-datadog-unarchive-api
- collection_type: open
  name: Datadog Account Unassign API
  slug: open-datadog-unassign-api
- collection_type: open
  name: Datadog Account Update API
  slug: open-datadog-update-api
- collection_type: open
  name: Datadog Account Upload API
  slug: open-datadog-upload-api
- collection_type: open
  name: Datadog Account Usage API
  slug: open-datadog-usage-api
- collection_type: open
  name: Datadog Account Users API
  slug: open-datadog-users-api
- collection_type: open
  name: Datadog Account Validate API
  slug: open-datadog-validate-api
- collection_type: open
  name: Datadog Account Value API
  slug: open-datadog-value-api
- collection_type: open
  name: Datadog Account Versions API
  slug: open-datadog-versions-api
- collection_type: open
  name: Datadog Account Volumes API
  slug: open-datadog-volumes-api
- collection_type: open
  name: Datadog Account Vulnerabilities API
  slug: open-datadog-vulnerabilities-api
- collection_type: open
  name: Datadog Account Webhooks API
  slug: open-datadog-webhooks-api
- collection_type: open
  name: Datadog Account Workflows API
  slug: open-datadog-workflows-api
common:
- group: design
  href: https://artifacts.apis.io/datadog/errors/datadog-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/datadog-problem-types.yml
- group: commercial
  href: https://artifacts.apis.io/datadog/finops/datadog-finops.yml
  title: ''
  type: FinOps
  url: finops/datadog-finops.yml
- group: operate
  href: https://artifacts.apis.io/datadog/rate-limits/datadog-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/datadog-rate-limits.yml
- group: design
  href: https://artifacts.apis.io/datadog/rules/datadog-spectral-rules.yml
  title: ''
  type: Spectral
  url: rules/datadog-spectral-rules.yml
- group: design
  href: https://artifacts.apis.io/datadog/rules/datadog-rules.yml
  title: ''
  type: Spectral
  url: rules/datadog-rules.yml
- group: design
  href: https://artifacts.apis.io/datadog/rules/datadog-jsonschema-spectral-rules.yml
  title: ''
  type: Spectral
  url: rules/datadog-jsonschema-spectral-rules.yml
- group: design
  href: https://artifacts.apis.io/datadog/vocabulary/datadog-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/datadog-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/datadog/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/datadog/data-model/datadog-data-model.yml
  title: ''
  type: DataModel
  url: data-model/datadog-data-model.yml
- group: build
  href: https://artifacts.apis.io/datadog/cli/datadog-cli.yml
  title: ''
  type: CLI
  url: cli/datadog-cli.yml
- group: design
  href: https://artifacts.apis.io/datadog/conventions/datadog-conventions.yml
  title: ''
  type: Conventions
  url: conventions/datadog-conventions.yml
- group: auth
  title: ''
  type: Compliance
  url: https://trust.datadoghq.com/
- group: operate
  href: https://artifacts.apis.io/datadog/lifecycle/datadog-lifecycle.yml
  title: ''
  type: Deprecation
  url: lifecycle/datadog-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/datadog/lifecycle/datadog-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/datadog-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/datadog/conformance/datadog-conformance.yml
  title: ''
  type: Conformance
  url: conformance/datadog-conformance.yml
- group: other
  href: https://artifacts.apis.io/datadog/overlays/datadog-api-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/datadog-api-overlay.yaml
- group: agent
  href: https://artifacts.apis.io/datadog/llms/datadog-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/datadog-llms.txt
- group: build
  href: https://artifacts.apis.io/datadog/mcp/datadog-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/datadog-tool-crosswalk.yml
- group: auth
  href: https://artifacts.apis.io/datadog/well-known/datadog-status-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/datadog-status-security.txt
- group: auth
  href: https://artifacts.apis.io/datadog/well-known/datadog-mcp-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/datadog-mcp-security.txt
- group: agent
  href: https://artifacts.apis.io/datadog/well-known/datadog-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/datadog-well-known.yml
- group: other
  href: https://artifacts.apis.io/datadog/hosts/datadog-hosts.yml
  title: ''
  type: Hosts
  url: hosts/datadog-hosts.yml
- group: other
  href: https://artifacts.apis.io/datadog/vendors/datadog-vendors.yml
  title: ''
  type: Vendors
  url: vendors/datadog-vendors.yml
- group: build
  href: https://artifacts.apis.io/datadog/packages/datadog-packages.yml
  title: ''
  type: Packages
  url: packages/datadog-packages.yml
- group: commercial
  href: https://artifacts.apis.io/datadog/plans/datadog-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/datadog-plans-pricing.yml
- group: other
  href: https://artifacts.apis.io/datadog/capabilities/datadog-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/datadog-capability-edges.yml
- group: agent
  href: https://artifacts.apis.io/datadog/agentic-access/datadog-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/datadog-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/datadog/security/datadog-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/datadog-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/datadog/security/datadog-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/datadog-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/datadog/security/datadog-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/datadog-domain-security.yml
- group: auth
  href: https://artifacts.apis.io/datadog/authentication/datadog-authentication.yml
  title: ''
  type: Authentication
  url: authentication/datadog-authentication.yml
- group: auth
  href: https://artifacts.apis.io/datadog/scopes/datadog-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/datadog-scopes.yml
- group: design
  href: https://artifacts.apis.io/datadog/arazzo/datadog-bulk-mute-monitors-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/datadog-bulk-mute-monitors-workflow.yml
- group: design
  href: https://artifacts.apis.io/datadog/arazzo/datadog-cleanup-stale-monitors-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/datadog-cleanup-stale-monitors-workflow.yml
- group: design
  href: https://artifacts.apis.io/datadog/arazzo/datadog-create-incident-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/datadog-create-incident-workflow.yml
- group: design
  href: https://artifacts.apis.io/datadog/arazzo/datadog-create-log-archive-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/datadog-create-log-archive-workflow.yml
- group: design
  href: https://artifacts.apis.io/datadog/arazzo/datadog-create-log-metric-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/datadog-create-log-metric-workflow.yml
- group: design
  href: https://artifacts.apis.io/datadog/arazzo/datadog-create-log-pipeline-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/datadog-create-log-pipeline-workflow.yml
- group: design
  href: https://artifacts.apis.io/datadog/arazzo/datadog-create-monitor-config-policy-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/datadog-create-monitor-config-policy-workflow.yml
- group: design
  href: https://artifacts.apis.io/datadog/arazzo/datadog-create-monitor-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/datadog-create-monitor-workflow.yml
- group: design
  href: https://artifacts.apis.io/datadog/arazzo/datadog-create-role-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/datadog-create-role-workflow.yml
- group: design
  href: https://artifacts.apis.io/datadog/arazzo/datadog-create-service-account-key-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/datadog-create-service-account-key-workflow.yml
- group: design
  href: https://artifacts.apis.io/datadog/arazzo/datadog-create-team-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/datadog-create-team-workflow.yml
- group: design
  href: https://artifacts.apis.io/datadog/arazzo/datadog-declare-incident-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/datadog-declare-incident-workflow.yml
- group: design
  href: https://artifacts.apis.io/datadog/arazzo/datadog-ingest-and-search-logs-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/datadog-ingest-and-search-logs-workflow.yml
- group: design
  href: https://artifacts.apis.io/datadog/arazzo/datadog-invite-user-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/datadog-invite-user-workflow.yml
- group: design
  href: https://artifacts.apis.io/datadog/arazzo/datadog-manage-api-keys-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/datadog-manage-api-keys-workflow.yml
- group: design
  href: https://artifacts.apis.io/datadog/arazzo/datadog-manage-incident-attachments-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/datadog-manage-incident-attachments-workflow.yml
- group: design
  href: https://artifacts.apis.io/datadog/arazzo/datadog-manage-metric-metadata-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/datadog-manage-metric-metadata-workflow.yml
- group: design
  href: https://artifacts.apis.io/datadog/arazzo/datadog-mute-monitor-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/datadog-mute-monitor-workflow.yml
- group: design
  href: https://artifacts.apis.io/datadog/arazzo/datadog-post-and-search-events-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/datadog-post-and-search-events-workflow.yml
- group: design
  href: https://artifacts.apis.io/datadog/arazzo/datadog-resolve-incident-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/datadog-resolve-incident-workflow.yml
- group: design
  href: https://artifacts.apis.io/datadog/arazzo/datadog-schedule-downtime-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/datadog-schedule-downtime-workflow.yml
- group: design
  href: https://artifacts.apis.io/datadog/arazzo/datadog-search-incidents-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/datadog-search-incidents-workflow.yml
- group: design
  href: https://artifacts.apis.io/datadog/arazzo/datadog-submit-and-query-metrics-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/datadog-submit-and-query-metrics-workflow.yml
- group: design
  href: https://artifacts.apis.io/datadog/arazzo/datadog-tune-monitor-thresholds-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/datadog-tune-monitor-thresholds-workflow.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/datadog
- group: company
  title: ''
  type: Twitter
  url: https://x.com/datadoghq
- group: learn
  title: ''
  type: YouTube
  url: https://www.youtube.com/@datadoghq
- group: company
  title: ''
  type: Facebook
  url: https://www.facebook.com/datadoghq
- group: company
  title: ''
  type: Careers
  url: https://www.datadoghq.com/careers/
- group: company
  title: ''
  type: Website
  url: https://www.datadoghq.com/
- group: start
  title: ''
  type: Portal
  url: https://docs.datadoghq.com/api/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.datadoghq.com/
- group: auth
  title: ''
  type: Authentication
  url: https://docs.datadoghq.com/api/latest/authentication/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/DataDog
- group: company
  title: ''
  type: Blog
  url: https://www.datadoghq.com/blog/
- group: operate
  title: ''
  type: Support
  url: https://www.datadoghq.com/support/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.datadoghq.com/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.datadoghq.com/pricing/
- group: start
  title: ''
  type: Login
  url: https://app.datadoghq.com/
- group: start
  title: ''
  type: Signup
  url: https://www.datadoghq.com/free-datadog-trial/
- group: design
  href: https://artifacts.apis.io/datadog/json-ld/datadog-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/datadog-context.jsonld
- group: docs
  href: https://artifacts.apis.io/datadog/json-schema/datadog-metric-schema.json
  title: ''
  type: JSONSchema
  url: json-schema/datadog-metric-schema.json
- group: docs
  href: https://artifacts.apis.io/datadog/json-schema/datadog-monitor-schema.json
  title: ''
  type: JSONSchema
  url: json-schema/datadog-monitor-schema.json
- group: docs
  href: https://artifacts.apis.io/datadog/json-schema/datadog-log-event-schema.json
  title: ''
  type: JSONSchema
  url: json-schema/datadog-log-event-schema.json
- group: docs
  href: https://artifacts.apis.io/datadog/json-schema/datadog-event-schema.json
  title: ''
  type: JSONSchema
  url: json-schema/datadog-event-schema.json
- group: other
  title: ''
  type: Products
  url: https://www.datadoghq.com/product/
- group: other
  title: ''
  type: Customers
  url: https://www.datadoghq.com/customers/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.datadoghq.com/pricing/
- group: company
  title: ''
  type: About
  url: https://www.datadoghq.com/about/leadership/
- group: company
  title: ''
  type: Blog
  url: https://www.datadoghq.com/blog/
- group: start
  title: ''
  type: Login
  url: https://app.datadoghq.com/account/login
- group: start
  title: ''
  type: Login
  url: https://app.datadoghq.com/account/login
- group: start
  title: ''
  type: Login
  url: https://app.datadoghq.com/account/login
- group: start
  title: ''
  type: Signup
  url: https://us5.datadoghq.com/signup
- group: operate
  title: ''
  type: Support
  url: https://www.datadoghq.com/support/
- group: auth
  title: ''
  type: Certifications
  url: https://www.datadoghq.com/certification/overview/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.datadoghq.com/privacy/
- group: auth
  title: ''
  type: Security
  url: https://www.datadoghq.com/security/
- group: auth
  title: ''
  type: Trust
  url: https://trust.datadoghq.com/
- group: company
  title: ''
  type: Partners
  url: https://www.datadoghq.com/partner/network/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.datadoghq.com/
- group: start
  title: ''
  type: Portal
  url: https://docs.datadoghq.com/api/latest/
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.datadoghq.com/getting_started/
- group: auth
  title: ''
  type: Authentication
  url: https://docs.datadoghq.com/api/latest/authentication/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.datadoghq.com/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/DataDog
- group: operate
  title: ''
  type: RateLimits
  url: https://docs.datadoghq.com/api/latest/rate-limits/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.datadoghq.com/developers/
- group: build
  title: ''
  type: SDKs
  url: https://docs.datadoghq.com/developers/libraries/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.datadoghq.com/legal/terms/
- group: other
  title: ''
  type: Agent
  url: https://docs.datadoghq.com/agent/
- group: operate
  title: ''
  type: Community
  url: https://community.datadoghq.com/
- group: auth
  title: ''
  type: Authorization Scopes
  url: https://docs.datadoghq.com/api/latest/scopes/
- group: other
  title: ''
  type: Using the API
  url: https://docs.datadoghq.com/api/latest/using-the-api/
- group: learn
  title: ''
  type: Learning Center
  url: https://learn.datadoghq.com/
- group: other
  title: ''
  type: Events
  url: https://www.datadoghq.com/events-webinars/
- group: other
  title: ''
  type: Marketplace
  url: https://www.datadoghq.com/marketplacepartners/
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/datadog/datadog-s-public-workspace/overview
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.datadoghq.com/getting_started/api/
- group: learn
  title: ''
  type: Learning Resources
  url: https://www.datadoghq.com/learn/
- group: agent
  title: ''
  type: MCPServer
  url: https://www.datadoghq.com/blog/introducing-datadog-code-security-mcp/
- group: agent
  title: ''
  type: LlmsText
  url: https://docs.datadoghq.com/llms.txt
- group: other
  href: https://artifacts.apis.io/datadog/vendor-facets/datadog-vendor-facets.yml
  title: ''
  type: VendorFacets
  url: vendor-facets/datadog-vendor-facets.yml
coverage:
  checked: '2026-10-04'
  detail: Datadog provides extensive HTML API documentation but no publicly accessible OpenAPI or other machine‑readable contract.
  evidence:
  - status: 404
    url: https://api.datadoghq.com/openapi.json
  - status: 200
    url: https://docs.datadoghq.com/api/
  reason: no-machine-readable-spec
  state: unreadable
created: 2024/04/14
description: Datadog is a monitoring and analytics platform that helps organizations gain insight into their infrastructure, applications, and services. It allows users to collect, visualize, and analyze real-time data from a variety of sources, including servers, databases, and cloud services. Datadog's platform enables companies to track performance metrics, troubleshoot issues, and optimize their systems for peak efficiency.
examples:
- key_count: 1
  name: Datadog Api Api Error Response Example
  slug: datadog-api-api-error-response-example
- key_count: 3
  name: Datadog Api Api Key Create Attributes Example
  slug: datadog-api-api-key-create-attributes-example
- key_count: 2
  name: Datadog Api Api Key Create Data Example
  slug: datadog-api-api-key-create-data-example
- key_count: 1
  name: Datadog Api Api Key Create Request Example
  slug: datadog-api-api-key-create-request-example
- key_count: 2
  name: Datadog Api Api Key Relationships Example
  slug: datadog-api-api-key-relationships-example
- key_count: 2
  name: Datadog Api Api Key Response Example
  slug: datadog-api-api-key-response-example
- key_count: 3
  name: Datadog Api Api Key Update Attributes Example
  slug: datadog-api-api-key-update-attributes-example
- key_count: 3
  name: Datadog Api Api Key Update Data Example
  slug: datadog-api-api-key-update-data-example
- key_count: 1
  name: Datadog Api Api Key Update Request Example
  slug: datadog-api-api-key-update-request-example
- key_count: 3
  name: Datadog Event Example
  slug: datadog-event-example
- key_count: 1
  name: Datadog Events Api Error Response Example
  slug: datadog-events-api-error-response-example
- key_count: 10
  name: Datadog Events Event Attributes Example
  slug: datadog-events-event-attributes-example
- key_count: 9
  name: Datadog Events Event Create Attributes Example
  slug: datadog-events-event-create-attributes-example
- key_count: 1
  name: Datadog Events Event Create Request Example
  slug: datadog-events-event-create-request-example
- key_count: 2
  name: Datadog Events Event Create Response Example
  slug: datadog-events-event-create-response-example
- key_count: 3
  name: Datadog Events Event Example
  slug: datadog-events-event-example
- key_count: 1
  name: Datadog Events Event Response Example
  slug: datadog-events-event-response-example
- key_count: 3
  name: Datadog Events Events List Response Example
  slug: datadog-events-events-list-response-example
- key_count: 3
  name: Datadog Events Events Search Request Example
  slug: datadog-events-events-search-request-example
- key_count: 10
  name: Datadog Incidents Incident Attributes Example
  slug: datadog-incidents-incident-attributes-example
- key_count: 8
  name: Datadog Incidents Incident Create Attributes Example
  slug: datadog-incidents-incident-create-attributes-example
- key_count: 1
  name: Datadog Incidents Incident Create Request Example
  slug: datadog-incidents-incident-create-request-example
- key_count: 4
  name: Datadog Incidents Incident Example
  slug: datadog-incidents-incident-example
- key_count: 2
  name: Datadog Incidents Incident Response Example
  slug: datadog-incidents-incident-response-example
- key_count: 1
  name: Datadog Incidents Incident Team Create Request Example
  slug: datadog-incidents-incident-team-create-request-example
- key_count: 1
  name: Datadog Incidents Incident Team Update Request Example
  slug: datadog-incidents-incident-team-update-request-example
- key_count: 8
  name: Datadog Incidents Incident Update Attributes Example
  slug: datadog-incidents-incident-update-attributes-example
- key_count: 1
  name: Datadog Incidents Incident Update Request Example
  slug: datadog-incidents-incident-update-request-example
- key_count: 3
  name: Datadog Incidents Incidents Response Example
  slug: datadog-incidents-incidents-response-example
- key_count: 4
  name: Datadog Log Event Example
  slug: datadog-log-event-example
- key_count: 6
  name: Datadog Logs Http Log Item Example
  slug: datadog-logs-http-log-item-example
- key_count: 8
  name: Datadog Logs Log Attributes Example
  slug: datadog-logs-log-attributes-example
- key_count: 3
  name: Datadog Logs Log Example
  slug: datadog-logs-log-example
- key_count: 4
  name: Datadog Logs Logs Aggregate Request Example
  slug: datadog-logs-logs-aggregate-request-example
- key_count: 4
  name: Datadog Logs Logs Compute Example
  slug: datadog-logs-logs-compute-example
- key_count: 3
  name: Datadog Logs Logs Group By Example
  slug: datadog-logs-logs-group-by-example
- key_count: 3
  name: Datadog Logs Logs List Request Example
  slug: datadog-logs-logs-list-request-example
- key_count: 2
  name: Datadog Logs Logs List Response Example
  slug: datadog-logs-logs-list-response-example
- key_count: 4
  name: Datadog Logs Logs Query Filter Example
  slug: datadog-logs-logs-query-filter-example
- key_count: 9
  name: Datadog Metric Example
  slug: datadog-metric-example
- key_count: 1
  name: Datadog Metrics Intake Payload Accepted Example
  slug: datadog-metrics-intake-payload-accepted-example
- key_count: 1
  name: Datadog Metrics Metric Payload Example
  slug: datadog-metrics-metric-payload-example
- key_count: 2
  name: Datadog Metrics Metric Point Example
  slug: datadog-metrics-metric-point-example
- key_count: 3
  name: Datadog Metrics Metric Query Definition Example
  slug: datadog-metrics-metric-query-definition-example
- key_count: 2
  name: Datadog Metrics Metric Resource Example
  slug: datadog-metrics-metric-resource-example
- key_count: 8
  name: Datadog Metrics Metric Series Example
  slug: datadog-metrics-metric-series-example
- key_count: 1
  name: Datadog Metrics Metric Timeseries Query Example
  slug: datadog-metrics-metric-timeseries-query-example
- key_count: 1
  name: Datadog Metrics Metric Timeseries Response Example
  slug: datadog-metrics-metric-timeseries-response-example
- key_count: 3
  name: Datadog Metrics Query Formula Example
  slug: datadog-metrics-query-formula-example
- key_count: 4
  name: Datadog Metrics Timeseries Result Example
  slug: datadog-metrics-timeseries-result-example
- key_count: 10
  name: Datadog Monitor Example
  slug: datadog-monitor-example
- key_count: 4
  name: Datadog Monitors Creator Example
  slug: datadog-monitors-creator-example
- key_count: 1
  name: Datadog Monitors Deleted Monitor Example
  slug: datadog-monitors-deleted-monitor-example
- key_count: 10
  name: Datadog Monitors Monitor Example
  slug: datadog-monitors-monitor-example
- key_count: 5
  name: Datadog Monitors Monitor Group State Example
  slug: datadog-monitors-monitor-group-state-example
- key_count: 2
  name: Datadog Monitors Monitor Mute Settings Example
  slug: datadog-monitors-monitor-mute-settings-example
- key_count: 10
  name: Datadog Monitors Monitor Options Example
  slug: datadog-monitors-monitor-options-example
- key_count: 1
  name: Datadog Monitors Monitor State Example
  slug: datadog-monitors-monitor-state-example
- key_count: 6
  name: Datadog Monitors Monitor Thresholds Example
  slug: datadog-monitors-monitor-thresholds-example
- key_count: 2
  name: Datadog Monitors Monitor Unmute Settings Example
  slug: datadog-monitors-monitor-unmute-settings-example
- key_count: 7
  name: Datadog Monitors Monitor Update Request Example
  slug: datadog-monitors-monitor-update-request-example
features:
- Infrastructure Monitoring with 1,000+ integrations and 15-month metric retention
- APM (Application Performance Monitoring) with end-to-end distributed traces
- APM Pro with Data Streams Monitoring for queue/pipeline observability
- APM Enterprise with Continuous Profiler
- Log Management with $0.10/GB ingest and tiered indexing/Flex storage
- Real User Monitoring (RUM) for browser and mobile
- Synthetic Monitoring with API and browser tests
- Network Performance Monitoring
- Database Monitoring
- Cloud Security Posture Management (CSPM)
- Cloud Workload Security
- Cloud SIEM
- Sensitive Data Scanner
- Watchdog ML-based anomaly detection (Enterprise)
- Governance Console for org-wide policy
- Per-endpoint REST API rate limits with X-RateLimit-* headers
- Cost Management and Usage Metering for FinOps
finops:
- has_sources: true
  method: derived
  name: Datadog Finops
  primary_unit: host
  service_category: ''
  slug: datadog-finops
  template: false
image: https://imgix.datadoghq.com/img/dd_logo_n_70x75.png
integrations:
- description: Native integration with 80+ AWS services for metrics, logs, and traces.
  name: AWS
- description: Container orchestration monitoring with cluster, pod, and node visibility.
  name: Kubernetes
- description: Infrastructure-as-code management of Datadog monitors, dashboards, and alerts.
  name: Terraform
- description: Alert notifications and incident management within Slack channels.
  name: Slack
- description: Incident escalation and on-call management integration.
  name: PagerDuty
- description: Create Jira tickets from Datadog alerts and incidents.
  name: Jira
json_schemas:
- name: APIErrorResponse
  property_count: 1
  slug: datadog-api-api-error-response
- name: APIKeyCreateAttributes
  property_count: 3
  slug: datadog-api-api-key-create-attributes
- name: APIKeyCreateData
  property_count: 2
  slug: datadog-api-api-key-create-data
- name: APIKeyCreateRequest
  property_count: 1
  slug: datadog-api-api-key-create-request
- name: APIKeyRelationships
  property_count: 2
  slug: datadog-api-api-key-relationships
- name: APIKeyResponse
  property_count: 2
  slug: datadog-api-api-key-response
- name: APIKeyUpdateAttributes
  property_count: 3
  slug: datadog-api-api-key-update-attributes
- name: APIKeyUpdateData
  property_count: 3
  slug: datadog-api-api-key-update-data
- name: APIKeyUpdateRequest
  property_count: 1
  slug: datadog-api-api-key-update-request
- name: Datadog Event
  property_count: 3
  slug: datadog-event
- name: APIErrorResponse
  property_count: 1
  slug: datadog-events-api-error-response
- name: EventAttributes
  property_count: 11
  slug: datadog-events-event-attributes
- name: EventCreateAttributes
  property_count: 9
  slug: datadog-events-event-create-attributes
- name: EventCreateRequest
  property_count: 1
  slug: datadog-events-event-create-request
- name: EventCreateResponse
  property_count: 2
  slug: datadog-events-event-create-response
- name: EventResponse
  property_count: 1
  slug: datadog-events-event-response
- name: Event
  property_count: 3
  slug: datadog-events-event
- name: EventsListResponse
  property_count: 3
  slug: datadog-events-events-list-response
- name: EventsSearchRequest
  property_count: 3
  slug: datadog-events-events-search-request
- name: IncidentAttributes
  property_count: 18
  slug: datadog-incidents-incident-attributes
- name: IncidentCreateAttributes
  property_count: 8
  slug: datadog-incidents-incident-create-attributes
- name: IncidentCreateRequest
  property_count: 1
  slug: datadog-incidents-incident-create-request
- name: IncidentResponse
  property_count: 2
  slug: datadog-incidents-incident-response
- name: Incident
  property_count: 4
  slug: datadog-incidents-incident
- name: IncidentTeamCreateRequest
  property_count: 1
  slug: datadog-incidents-incident-team-create-request
- name: IncidentTeamUpdateRequest
  property_count: 1
  slug: datadog-incidents-incident-team-update-request
- name: IncidentUpdateAttributes
  property_count: 8
  slug: datadog-incidents-incident-update-attributes
- name: IncidentUpdateRequest
  property_count: 1
  slug: datadog-incidents-incident-update-request
- name: IncidentsResponse
  property_count: 3
  slug: datadog-incidents-incidents-response
- name: Datadog Log Event
  property_count: 4
  slug: datadog-log-event
- name: HTTPLogItem
  property_count: 6
  slug: datadog-logs-http-log-item
- name: LogAttributes
  property_count: 8
  slug: datadog-logs-log-attributes
- name: Log
  property_count: 3
  slug: datadog-logs-log
- name: LogsAggregateRequest
  property_count: 4
  slug: datadog-logs-logs-aggregate-request
- name: LogsCompute
  property_count: 4
  slug: datadog-logs-logs-compute
- name: LogsGroupBy
  property_count: 3
  slug: datadog-logs-logs-group-by
- name: LogsListRequest
  property_count: 3
  slug: datadog-logs-logs-list-request
- name: LogsListResponse
  property_count: 2
  slug: datadog-logs-logs-list-response
- name: LogsQueryFilter
  property_count: 4
  slug: datadog-logs-logs-query-filter
- name: Datadog Metric Series
  property_count: 9
  slug: datadog-metric
- name: IntakePayloadAccepted
  property_count: 1
  slug: datadog-metrics-intake-payload-accepted
- name: MetricPayload
  property_count: 1
  slug: datadog-metrics-metric-payload
- name: MetricPoint
  property_count: 2
  slug: datadog-metrics-metric-point
- name: MetricQueryDefinition
  property_count: 3
  slug: datadog-metrics-metric-query-definition
- name: MetricResource
  property_count: 2
  slug: datadog-metrics-metric-resource
- name: MetricSeries
  property_count: 8
  slug: datadog-metrics-metric-series
- name: MetricTimeseriesQuery
  property_count: 1
  slug: datadog-metrics-metric-timeseries-query
- name: MetricTimeseriesResponse
  property_count: 1
  slug: datadog-metrics-metric-timeseries-response
- name: QueryFormula
  property_count: 3
  slug: datadog-metrics-query-formula
- name: TimeseriesResult
  property_count: 4
  slug: datadog-metrics-timeseries-result
- name: Datadog Monitor
  property_count: 14
  slug: datadog-monitor
- name: Creator
  property_count: 4
  slug: datadog-monitors-creator
- name: DeletedMonitor
  property_count: 1
  slug: datadog-monitors-deleted-monitor
- name: MonitorGroupState
  property_count: 5
  slug: datadog-monitors-monitor-group-state
- name: MonitorMuteSettings
  property_count: 2
  slug: datadog-monitors-monitor-mute-settings
- name: MonitorOptions
  property_count: 14
  slug: datadog-monitors-monitor-options
- name: Monitor
  property_count: 14
  slug: datadog-monitors-monitor
- name: MonitorState
  property_count: 1
  slug: datadog-monitors-monitor-state
- name: MonitorThresholds
  property_count: 6
  slug: datadog-monitors-monitor-thresholds
- name: MonitorUnmuteSettings
  property_count: 2
  slug: datadog-monitors-monitor-unmute-settings
- name: MonitorUpdateRequest
  property_count: 7
  slug: datadog-monitors-monitor-update-request
json_structures:
- name: Datadog Api Api Error Response Structure
  property_count: 1
  slug: datadog-api-api-error-response-structure
- name: Datadog Api Api Key Create Attributes Structure
  property_count: 3
  slug: datadog-api-api-key-create-attributes-structure
- name: Datadog Api Api Key Create Data Structure
  property_count: 2
  slug: datadog-api-api-key-create-data-structure
- name: Datadog Api Api Key Create Request Structure
  property_count: 1
  slug: datadog-api-api-key-create-request-structure
- name: Datadog Api Api Key Relationships Structure
  property_count: 2
  slug: datadog-api-api-key-relationships-structure
- name: Datadog Api Api Key Response Structure
  property_count: 2
  slug: datadog-api-api-key-response-structure
- name: Datadog Api Api Key Update Attributes Structure
  property_count: 3
  slug: datadog-api-api-key-update-attributes-structure
- name: Datadog Api Api Key Update Data Structure
  property_count: 3
  slug: datadog-api-api-key-update-data-structure
- name: Datadog Api Api Key Update Request Structure
  property_count: 1
  slug: datadog-api-api-key-update-request-structure
- name: Datadog Event Structure
  property_count: 3
  slug: datadog-event-structure
- name: Datadog Events Api Error Response Structure
  property_count: 1
  slug: datadog-events-api-error-response-structure
- name: Datadog Events Event Attributes Structure
  property_count: 11
  slug: datadog-events-event-attributes-structure
- name: Datadog Events Event Create Attributes Structure
  property_count: 9
  slug: datadog-events-event-create-attributes-structure
- name: Datadog Events Event Create Request Structure
  property_count: 1
  slug: datadog-events-event-create-request-structure
- name: Datadog Events Event Create Response Structure
  property_count: 2
  slug: datadog-events-event-create-response-structure
- name: Datadog Events Event Response Structure
  property_count: 1
  slug: datadog-events-event-response-structure
- name: Datadog Events Event Structure
  property_count: 3
  slug: datadog-events-event-structure
- name: Datadog Events Events List Response Structure
  property_count: 3
  slug: datadog-events-events-list-response-structure
- name: Datadog Events Events Search Request Structure
  property_count: 3
  slug: datadog-events-events-search-request-structure
- name: Datadog Incidents Incident Attributes Structure
  property_count: 18
  slug: datadog-incidents-incident-attributes-structure
- name: Datadog Incidents Incident Create Attributes Structure
  property_count: 8
  slug: datadog-incidents-incident-create-attributes-structure
- name: Datadog Incidents Incident Create Request Structure
  property_count: 1
  slug: datadog-incidents-incident-create-request-structure
- name: Datadog Incidents Incident Response Structure
  property_count: 2
  slug: datadog-incidents-incident-response-structure
- name: Datadog Incidents Incident Structure
  property_count: 4
  slug: datadog-incidents-incident-structure
- name: Datadog Incidents Incident Team Create Request Structure
  property_count: 1
  slug: datadog-incidents-incident-team-create-request-structure
- name: Datadog Incidents Incident Team Update Request Structure
  property_count: 1
  slug: datadog-incidents-incident-team-update-request-structure
- name: Datadog Incidents Incident Update Attributes Structure
  property_count: 8
  slug: datadog-incidents-incident-update-attributes-structure
- name: Datadog Incidents Incident Update Request Structure
  property_count: 1
  slug: datadog-incidents-incident-update-request-structure
- name: Datadog Incidents Incidents Response Structure
  property_count: 3
  slug: datadog-incidents-incidents-response-structure
- name: Datadog Log Event Structure
  property_count: 4
  slug: datadog-log-event-structure
- name: Datadog Logs Http Log Item Structure
  property_count: 6
  slug: datadog-logs-http-log-item-structure
- name: Datadog Logs Log Attributes Structure
  property_count: 8
  slug: datadog-logs-log-attributes-structure
- name: Datadog Logs Log Structure
  property_count: 3
  slug: datadog-logs-log-structure
- name: Datadog Logs Logs Aggregate Request Structure
  property_count: 4
  slug: datadog-logs-logs-aggregate-request-structure
- name: Datadog Logs Logs Compute Structure
  property_count: 4
  slug: datadog-logs-logs-compute-structure
- name: Datadog Logs Logs Group By Structure
  property_count: 3
  slug: datadog-logs-logs-group-by-structure
- name: Datadog Logs Logs List Request Structure
  property_count: 3
  slug: datadog-logs-logs-list-request-structure
- name: Datadog Logs Logs List Response Structure
  property_count: 2
  slug: datadog-logs-logs-list-response-structure
- name: Datadog Logs Logs Query Filter Structure
  property_count: 4
  slug: datadog-logs-logs-query-filter-structure
- name: Datadog Metric Structure
  property_count: 9
  slug: datadog-metric-structure
- name: Datadog Metrics Intake Payload Accepted Structure
  property_count: 1
  slug: datadog-metrics-intake-payload-accepted-structure
- name: Datadog Metrics Metric Payload Structure
  property_count: 1
  slug: datadog-metrics-metric-payload-structure
- name: Datadog Metrics Metric Point Structure
  property_count: 2
  slug: datadog-metrics-metric-point-structure
- name: Datadog Metrics Metric Query Definition Structure
  property_count: 3
  slug: datadog-metrics-metric-query-definition-structure
- name: Datadog Metrics Metric Resource Structure
  property_count: 2
  slug: datadog-metrics-metric-resource-structure
- name: Datadog Metrics Metric Series Structure
  property_count: 8
  slug: datadog-metrics-metric-series-structure
- name: Datadog Metrics Metric Timeseries Query Structure
  property_count: 1
  slug: datadog-metrics-metric-timeseries-query-structure
- name: Datadog Metrics Metric Timeseries Response Structure
  property_count: 1
  slug: datadog-metrics-metric-timeseries-response-structure
- name: Datadog Metrics Query Formula Structure
  property_count: 3
  slug: datadog-metrics-query-formula-structure
- name: Datadog Metrics Timeseries Result Structure
  property_count: 4
  slug: datadog-metrics-timeseries-result-structure
- name: Datadog Monitor Structure
  property_count: 14
  slug: datadog-monitor-structure
- name: Datadog Monitors Creator Structure
  property_count: 4
  slug: datadog-monitors-creator-structure
- name: Datadog Monitors Deleted Monitor Structure
  property_count: 1
  slug: datadog-monitors-deleted-monitor-structure
- name: Datadog Monitors Monitor Group State Structure
  property_count: 5
  slug: datadog-monitors-monitor-group-state-structure
- name: Datadog Monitors Monitor Mute Settings Structure
  property_count: 2
  slug: datadog-monitors-monitor-mute-settings-structure
- name: Datadog Monitors Monitor Options Structure
  property_count: 14
  slug: datadog-monitors-monitor-options-structure
- name: Datadog Monitors Monitor State Structure
  property_count: 1
  slug: datadog-monitors-monitor-state-structure
- name: Datadog Monitors Monitor Structure
  property_count: 14
  slug: datadog-monitors-monitor-structure
- name: Datadog Monitors Monitor Thresholds Structure
  property_count: 6
  slug: datadog-monitors-monitor-thresholds-structure
- name: Datadog Monitors Monitor Unmute Settings Structure
  property_count: 2
  slug: datadog-monitors-monitor-unmute-settings-structure
- name: Datadog Monitors Monitor Update Request Structure
  property_count: 7
  slug: datadog-monitors-monitor-update-request-structure
jsonld:
- class_count: 60
  name: Datadog Context
  property_count: 106
  slug: datadog-context
layout: provider
mcp_servers:
- description: ''
  name: MCP Server
  slug: mcp-server
- description: Official Datadog MCP Server bridging Datadog observability data (APM, logs, metrics, monitors, dashboards, incidents, security signals, RUM, synthetics, CI Visibility, cloud cost, and more) to any MCP
  name: Datadog MCP Server
  slug: datadog
modified: '2026-09-23'
name: Datadog
nav: Providers
network: true
overview: 'Datadog publishes 186 API contracts indexed on the [APIs.io](https://apis.io/) network, including Dashboards API, Teams API, Audit API, and 183 more. Tagged areas include Visualization, Datadog, Analytics, Dashboards, and Monitoring.


  The Datadog catalog on APIs.io includes 1 JSON-LD context and 3 Spectral governance rulesets.


  Datadog''s developer surface includes CLI, authentication, YouTube channel, developer portal, documentation, engineering blog, support, and 108 more developer resources.'
plans:
- name: Datadog Plans Pricing
  plan_count: 17
  slug: datadog-plans-pricing
- name: Datadog Price Estimates
  plan_count: 0
  slug: datadog-price-estimates
random_paper: 4
rate_limits:
- limit_count: 6
  name: Datadog Rate Limits
  slug: datadog-rate-limits
rules:
- authorship: generated
  effective_rule_count: 6
  extends: []
  name: Datadog — jsonschema rules
  rule_count: 6
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 5
  slug: datadog-jsonschema-spectral-rules
- authorship: generated
  effective_rule_count: 61
  extends:
  - spectral:oas
  name: Datadog API Rules
  rule_count: 20
  severity_counts:
    error: 13
    hint: 0
    info: 3
    warn: 4
  slug: datadog-rules
- authorship: generated
  effective_rule_count: 65
  extends:
  - spectral:oas
  name: Datadog API Rules
  rule_count: 24
  severity_counts:
    error: 13
    hint: 0
    info: 2
    warn: 9
  slug: datadog-spectral-rules
scopes:
- name: Datadog Scopes
  scope_count: 68
  slug: datadog-scopes
  summary_line: 68 scopes · authorizationCode
score:
  band: exemplar
  composite: 79.2
  coverage:
    artifact_dirs: 40
    catalog_earned: 78.0
    catalog_earned_first_party: 12.0
    catalog_gap: 37.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 93.4
    contract_governance: 45.5
    contract_quality: 67.4
    developer_ergonomics: 78.0
    discoverability: 80.0
    operational_transparency: 44.7
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - united-states
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
  previous_composite: 79.2
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 107
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 45.1
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 50.0
screenshot: https://apis.io/screenshots/datadog/datadog-2026-06-20T175637.png
security:
- kind: authentication
  name: Datadog Authentication
  slug: datadog-authentication
  summary_line: apiKey/http/oauth2 · 4 schemes
- kind: domain-security
  name: Datadog Domain Security
  slug: datadog-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Datadog Vulnerability Disclosure
  slug: datadog-vulnerability-disclosure
  summary_line: Hackerone
- kind: trust-center
  name: Datadog Trust Center
  slug: datadog-trust-center
  summary_line: SOC 2, ISO 27001, ISO 27017, ISO 27018, PCI DSS, HIPAA, FedRAMP, GDPR, CSA STAR
skill_count: 11
skills:
- name: datadog-create-and-retrieve-event
  slug: datadog-create-and-retrieve-event
- name: datadog-create-incident-workflow
  slug: datadog-create-incident-workflow
- name: datadog-create-incident
  slug: datadog-create-incident
- name: datadog-create-monitor
  slug: datadog-create-monitor
- name: datadog-get-incident-details
  slug: datadog-get-incident-details
- name: datadog-ingest-and-search-logs
  slug: datadog-ingest-and-search-logs
- name: datadog-manage-api-keys
  slug: datadog-manage-api-keys
- name: datadog-post-and-search-events
  slug: datadog-post-and-search-events
- name: datadog-schedule-downtime
  slug: datadog-schedule-downtime
- name: datadog-submit-and-query-metrics
  slug: datadog-submit-and-query-metrics
- name: datadog-update-existing-incident
  slug: datadog-update-existing-incident
slug: datadog
solutions:
- description: Infrastructure monitoring with 800+ integrations for servers, containers, and cloud.
  name: Datadog Infrastructure
- description: Application performance monitoring with distributed tracing and profiling.
  name: Datadog APM
- description: Log management with indexing, archiving, and analytics.
  name: Datadog Logs
- description: Cloud security posture management and threat detection.
  name: Datadog Security
tags:
- Visualization
- Datadog
- Analytics
- Dashboards
- Monitoring
- Platform
- T1
use_cases:
- description: Correlate metrics, traces, and logs across the entire application stack.
  name: Full-Stack Observability
- description: Monitor Kubernetes, Docker, and container orchestration platforms.
  name: Container Monitoring
- description: Monitor AWS, Azure, GCP, and hybrid cloud environments.
  name: Cloud Infrastructure Monitoring
- description: Identify and resolve application bottlenecks with distributed tracing.
  name: Application Performance Management
- description: Centralize and analyze logs for troubleshooting and compliance.
  name: Log Analytics
- description: Automate incident detection, response, and resolution workflows.
  name: Incident Management
- description: Integrate monitoring into CI/CD pipelines with API-driven workflows.
  name: DevOps Automation
- description: Monitor cloud security misconfigurations and compliance violations.
  name: Security Posture Management
website: https://www.datadoghq.com/
---
