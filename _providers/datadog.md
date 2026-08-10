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
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: true
    openapi_examples: partial
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 51.8
  scored_at: '2026-08-10'
agentic_access:
- acting_count: 324
  human_in_the_loop: 4
  name: Datadog Agentic Access
  operation_count: 558
  slug: datadog-agentic-access
  summary_line: 558 operations · 324 acting · 4 human-in-the-loop
api_count: 290
apis:
- description: The Dashboards API allows you to create, update, delete, and retrieve dashboards and dashboard lists. It also supports organizing, finding, and sharing dashboards with your team and organization.
  name: Datadog Dashboards API
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
- description: The Teams API allows you to view and manage teams within Datadog. Teams can be associated with incidents, dashboards, and other resources to organize ownership and collaboration within your organizati
  name: Datadog Teams API
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
- description: The Audit API allows you to search your Audit Logs events over HTTP. It returns Audit Logs events that match an audit search query, providing visibility into actions taken within your organization.
  name: Datadog Audit API
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
- description: The Account API from Datadog — 20 operation(s) for account.
  name: Datadog Account API
  slug: datadog-account-api
- description: The Accounts API from Datadog — 6 operation(s) for accounts.
  name: Datadog Accounts API
  slug: datadog-accounts-api
- description: The Acknowledge API from Datadog — 1 operation(s) for acknowledge.
  name: Datadog Acknowledge API
  slug: datadog-acknowledge-api
- description: The Across API from Datadog — 6 operation(s) for across.
  name: Datadog Across API
  slug: datadog-across-api
- description: The Action API from Datadog — 2 operation(s) for action.
  name: Datadog Action API
  slug: datadog-action-api
- description: The Active API from Datadog — 3 operation(s) for active.
  name: Datadog Active API
  slug: datadog-active-api
- description: The Add API from Datadog — 9 operation(s) for add.
  name: Datadog Add API
  slug: datadog-add-api
- description: The Agent API from Datadog — 4 operation(s) for agent.
  name: Datadog Agent API
  slug: datadog-agent-api
- description: The Agents API from Datadog — 2 operation(s) for agents.
  name: Datadog Agents API
  slug: datadog-agents-api
- description: The Aggregate API from Datadog — 5 operation(s) for aggregate.
  name: Datadog Aggregate API
  slug: datadog-aggregate-api
- description: The Aggregated API from Datadog — 1 operation(s) for aggregated.
  name: Datadog Aggregated API
  slug: datadog-aggregated-api
- description: The Aggregations API from Datadog — 1 operation(s) for aggregations.
  name: Datadog Aggregations API
  slug: datadog-aggregations-api
- description: The All API from Datadog — 44 operation(s) for all.
  name: Datadog All API
  slug: datadog-all-api
- description: The Analysis API from Datadog — 3 operation(s) for analysis.
  name: Datadog Analysis API
  slug: datadog-analysis-api
- description: The Applications API from Datadog — 12 operation(s) for applications.
  name: Datadog Applications API
  slug: datadog-applications-api
- description: The Archive API from Datadog — 5 operation(s) for archive.
  name: Datadog Archive API
  slug: datadog-archive-api
- description: The Archives API from Datadog — 1 operation(s) for archives.
  name: Datadog Archives API
  slug: datadog-archives-api
- description: The Assets API from Datadog — 2 operation(s) for assets.
  name: Datadog Assets API
  slug: datadog-assets-api
- description: The Assign API from Datadog — 1 operation(s) for assign.
  name: Datadog Assign API
  slug: datadog-assign-api
- description: The Assignee API from Datadog — 1 operation(s) for assignee.
  name: Datadog Assignee API
  slug: datadog-assignee-api
- description: The Attachments API from Datadog — 1 operation(s) for attachments.
  name: Datadog Attachments API
  slug: datadog-attachments-api
- description: The Attributes API from Datadog — 1 operation(s) for attributes.
  name: Datadog Attributes API
  slug: datadog-attributes-api
- description: Search your Audit Logs events over HTTP.
  name: Datadog Audit API
  slug: datadog-audit-api
- description: The Available API from Datadog — 1 operation(s) for available.
  name: Datadog Available API
  slug: datadog-available-api
- description: The Batch API from Datadog — 2 operation(s) for batch.
  name: Datadog Batch API
  slug: datadog-batch-api
- description: The Billing API from Datadog — 2 operation(s) for billing.
  name: Datadog Billing API
  slug: datadog-billing-api
- description: The Budget API from Datadog — 2 operation(s) for budget.
  name: Datadog Budget API
  slug: datadog-budget-api
- description: The Budgets API from Datadog — 1 operation(s) for budgets.
  name: Datadog Budgets API
  slug: datadog-budgets-api
- description: The Cancel API from Datadog — 3 operation(s) for cancel.
  name: Datadog Cancel API
  slug: datadog-cancel-api
- description: The Cap API from Datadog — 1 operation(s) for cap.
  name: Datadog Cap API
  slug: datadog-cap-api
- description: The Cardinality API from Datadog — 1 operation(s) for cardinality.
  name: Datadog Cardinality API
  slug: datadog-cardinality-api
- description: The Case API from Datadog — 8 operation(s) for case.
  name: Datadog Case API
  slug: datadog-case-api
- description: The Cases API from Datadog — 1 operation(s) for cases.
  name: Datadog Cases API
  slug: datadog-cases-api
- description: The Change API from Datadog — 2 operation(s) for change.
  name: Datadog Change API
  slug: datadog-change-api
- description: The Channel API from Datadog — 1 operation(s) for channel.
  name: Datadog Channel API
  slug: datadog-channel-api
- description: The Cloud API from Datadog — 5 operation(s) for cloud.
  name: Datadog Cloud API
  slug: datadog-cloud-api
- description: The Cloudflare API from Datadog — 2 operation(s) for cloudflare.
  name: Datadog Cloudflare API
  slug: datadog-cloudflare-api
- description: The Configuration API from Datadog — 4 operation(s) for configuration.
  name: Datadog Configuration API
  slug: datadog-configuration-api
- description: The Configure API from Datadog — 1 operation(s) for configure.
  name: Datadog Configure API
  slug: datadog-configure-api
- description: The Connection API from Datadog — 2 operation(s) for connection.
  name: Datadog Connection API
  slug: datadog-connection-api
- description: The Connections API from Datadog — 1 operation(s) for connections.
  name: Datadog Connections API
  slug: datadog-connections-api
- description: The Containers API allows you to query container data for your organization. See the [Container Monitoring page](https://docs.datadoghq.com/containers/) for more information.
  name: Datadog Containers API
  slug: datadog-containers-api
- description: The Convert API from Datadog — 3 operation(s) for convert.
  name: Datadog Convert API
  slug: datadog-convert-api
- description: The Cost API from Datadog — 10 operation(s) for cost.
  name: Datadog Cost API
  slug: datadog-cost-api
- description: The Coverage API from Datadog — 3 operation(s) for coverage.
  name: Datadog Coverage API
  slug: datadog-coverage-api
- description: The Create API from Datadog — 69 operation(s) for create.
  name: Datadog Create API
  slug: datadog-create-api
- description: The Current API from Datadog — 2 operation(s) for current.
  name: Datadog Current API
  slug: datadog-current-api
- description: The Custom API from Datadog — 8 operation(s) for custom.
  name: Datadog Custom API
  slug: datadog-custom-api
- description: The Dashboards API from Datadog — 1 operation(s) for dashboards.
  name: Datadog Dashboards API
  slug: datadog-dashboards-api
- description: The Data API from Datadog — 2 operation(s) for data.
  name: Datadog Data API
  slug: datadog-data-api
- description: The Definition API from Datadog — 2 operation(s) for definition.
  name: Datadog Definition API
  slug: datadog-definition-api
- description: The Definitions API from Datadog — 1 operation(s) for definitions.
  name: Datadog Definitions API
  slug: datadog-definitions-api
- description: The Delegate API from Datadog — 1 operation(s) for delegate.
  name: Datadog Delegate API
  slug: datadog-delegate-api
- description: The Delete API from Datadog — 72 operation(s) for delete.
  name: Datadog Delete API
  slug: datadog-delete-api
- description: The Demand API from Datadog — 2 operation(s) for demand.
  name: Datadog Demand API
  slug: datadog-demand-api
- description: The Deployments API from Datadog — 3 operation(s) for deployments.
  name: Datadog Deployments API
  slug: datadog-deployments-api
- description: The Destination API from Datadog — 2 operation(s) for destination.
  name: Datadog Destination API
  slug: datadog-destination-api
- description: The Destinations API from Datadog — 1 operation(s) for destinations.
  name: Datadog Destinations API
  slug: datadog-destinations-api
- description: The Detection API from Datadog — 2 operation(s) for detection.
  name: Datadog Detection API
  slug: datadog-detection-api
- description: The Devices API from Datadog — 4 operation(s) for devices.
  name: Datadog Devices API
  slug: datadog-devices-api
- description: The Dimension API from Datadog — 1 operation(s) for dimension.
  name: Datadog Dimension API
  slug: datadog-dimension-api
- description: The Dimensions API from Datadog — 1 operation(s) for dimensions.
  name: Datadog Dimensions API
  slug: datadog-dimensions-api
- description: The Disables API from Datadog — 1 operation(s) for disables.
  name: Datadog Disables API
  slug: datadog-disables-api
- description: The Domain API from Datadog — 1 operation(s) for domain.
  name: Datadog Domain API
  slug: datadog-domain-api
- description: The Download API from Datadog — 2 operation(s) for download.
  name: Datadog Download API
  slug: datadog-download-api
- description: The Edit API from Datadog — 6 operation(s) for edit.
  name: Datadog Edit API
  slug: datadog-edit-api
- description: The Emails API from Datadog — 1 operation(s) for emails.
  name: Datadog Emails API
  slug: datadog-emails-api
- description: The Enabled API from Datadog — 1 operation(s) for enabled.
  name: Datadog Enabled API
  slug: datadog-enabled-api
- description: The Entities API from Datadog — 1 operation(s) for entities.
  name: Datadog Entities API
  slug: datadog-entities-api
- description: The Entity API from Datadog — 2 operation(s) for entity.
  name: Datadog Entity API
  slug: datadog-entity-api
- description: The Entry API from Datadog — 1 operation(s) for entry.
  name: Datadog Entry API
  slug: datadog-entry-api
- description: The Escalate API from Datadog — 1 operation(s) for escalate.
  name: Datadog Escalate API
  slug: datadog-escalate-api
- description: The Event Management API allows you to programmatically post events to the Events Explorer and fetch events from the Events Explorer. See the [Event Management page](https://docs.datadoghq.com/service
  name: Datadog Events API
  slug: datadog-events-api
- description: The Execute API from Datadog — 1 operation(s) for execute.
  name: Datadog Execute API
  slug: datadog-execute-api
- description: The Existing API from Datadog — 12 operation(s) for existing.
  name: Datadog Existing API
  slug: datadog-existing-api
- description: The External API from Datadog — 1 operation(s) for external.
  name: Datadog External API
  slug: datadog-external-api
- description: The Failure API from Datadog — 2 operation(s) for failure.
  name: Datadog Failure API
  slug: datadog-failure-api
- description: The Family API from Datadog — 1 operation(s) for family.
  name: Datadog Family API
  slug: datadog-family-api
- description: The Files API from Datadog — 2 operation(s) for files.
  name: Datadog Files API
  slug: datadog-files-api
- description: The Filter API from Datadog — 8 operation(s) for filter.
  name: Datadog Filter API
  slug: datadog-filter-api
- description: The Finding API from Datadog — 1 operation(s) for finding.
  name: Datadog Finding API
  slug: datadog-finding-api
- description: The Findings API from Datadog — 1 operation(s) for findings.
  name: Datadog Findings API
  slug: datadog-findings-api
- description: The Framework API from Datadog — 2 operation(s) for framework.
  name: Datadog Framework API
  slug: datadog-framework-api
- description: The Generate API from Datadog — 1 operation(s) for generate.
  name: Datadog Generate API
  slug: datadog-generate-api
- description: The Get API from Datadog — 170 operation(s) for get.
  name: Datadog Get API
  slug: datadog-get-api
- description: The Given API from Datadog — 3 operation(s) for given.
  name: Datadog Given API
  slug: datadog-given-api
- description: The Grants API from Datadog — 3 operation(s) for grants.
  name: Datadog Grants API
  slug: datadog-grants-api
- description: The Groups API from Datadog — 5 operation(s) for groups.
  name: Datadog Groups API
  slug: datadog-groups-api
- description: The Handle API from Datadog — 4 operation(s) for handle.
  name: Datadog Handle API
  slug: datadog-handle-api
- description: The Historical API from Datadog — 3 operation(s) for historical.
  name: Datadog Historical API
  slug: datadog-historical-api
- description: The History API from Datadog — 1 operation(s) for history.
  name: Datadog History API
  slug: datadog-history-api
- description: The Hosts API from Datadog — 1 operation(s) for hosts.
  name: Datadog Hosts API
  slug: datadog-hosts-api
- description: The Hourly API from Datadog — 4 operation(s) for hourly.
  name: Datadog Hourly API
  slug: datadog-hourly-api
- description: The Identifiers API from Datadog — 3 operation(s) for identifiers.
  name: Datadog Identifiers API
  slug: datadog-identifiers-api
- description: The Images API from Datadog — 1 operation(s) for images.
  name: Datadog Images API
  slug: datadog-images-api
- description: The Incident API from Datadog — 14 operation(s) for incident.
  name: Datadog Incident API
  slug: datadog-incident-api
- description: Manage teams associated with incidents
  name: Datadog Incident Teams API
  slug: datadog-incident-teams-api
- description: Create and manage incident records
  name: Datadog Incidents API
  slug: datadog-incidents-api
- description: The Information API from Datadog — 3 operation(s) for information.
  name: Datadog Information API
  slug: datadog-information-api
- description: The Instance API from Datadog — 2 operation(s) for instance.
  name: Datadog Instance API
  slug: datadog-instance-api
- description: The Instances API from Datadog — 1 operation(s) for instances.
  name: Datadog Instances API
  slug: datadog-instances-api
- description: The Integration API from Datadog — 4 operation(s) for integration.
  name: Datadog Integration API
  slug: datadog-integration-api
- description: The Integrations API from Datadog — 1 operation(s) for integrations.
  name: Datadog Integrations API
  slug: datadog-integrations-api
- description: The Interfaces API from Datadog — 1 operation(s) for interfaces.
  name: Datadog Interfaces API
  slug: datadog-interfaces-api
- description: The Invitation API from Datadog — 2 operation(s) for invitation.
  name: Datadog Invitation API
  slug: datadog-invitation-api
- description: The Invocations API from Datadog — 1 operation(s) for invocations.
  name: Datadog Invocations API
  slug: datadog-invocations-api
- description: The Ip API from Datadog — 1 operation(s) for ip.
  name: Datadog Ip API
  slug: datadog-ip-api
- description: The Items API from Datadog — 1 operation(s) for items.
  name: Datadog Items API
  slug: datadog-items-api
- description: The Jobs API from Datadog — 4 operation(s) for jobs.
  name: Datadog Jobs API
  slug: datadog-jobs-api
- description: The Keys API from Datadog — 8 operation(s) for keys.
  name: Datadog Keys API
  slug: datadog-keys-api
- description: The Lambda API from Datadog — 1 operation(s) for lambda.
  name: Datadog Lambda API
  slug: datadog-lambda-api
- description: The Link API from Datadog — 2 operation(s) for link.
  name: Datadog Link API
  slug: datadog-link-api
- description: The Links API from Datadog — 1 operation(s) for links.
  name: Datadog Links API
  slug: datadog-links-api
- description: The Lists API from Datadog — 75 operation(s) for lists.
  name: Datadog Lists API
  slug: datadog-lists-api
- description: Aggregate and analyze log data
  name: Datadog Log Aggregation API
  slug: datadog-log-aggregation-api
- description: Manage log indexes and retention policies
  name: Datadog Log Indexes API
  slug: datadog-log-indexes-api
- description: Search your logs and send them to your Datadog platform over HTTP. See the [Log Management page](https://docs.datadoghq.com/logs/) for more information.
  name: Datadog Logs API
  slug: datadog-logs-api
- description: The Management API from Datadog — 4 operation(s) for management.
  name: Datadog Management API
  slug: datadog-management-api
- description: The Mapping API from Datadog — 3 operation(s) for mapping.
  name: Datadog Mapping API
  slug: datadog-mapping-api
- description: The Memberships API from Datadog — 3 operation(s) for memberships.
  name: Datadog Memberships API
  slug: datadog-memberships-api
- description: View and manage metric metadata and active metrics
  name: Datadog Metric Metadata API
  slug: datadog-metric-metadata-api
- description: Manage metric tag configurations
  name: Datadog Metric Tags API
  slug: datadog-metric-tags-api
- description: 'The metrics endpoint allows you to: - Post metrics data so it can be graphed on Datadog’s dashboards - Query metrics from any time period (timeseries and scalar) - Modify tag configurations for metric'
  name: Datadog Metrics API
  slug: datadog-metrics-api
- description: The Modify API from Datadog — 1 operation(s) for modify.
  name: Datadog Modify API
  slug: datadog-modify-api
- description: The Monitor API from Datadog — 5 operation(s) for monitor.
  name: Datadog Monitor API
  slug: datadog-monitor-api
- description: Mute and unmute monitors to suppress notifications
  name: Datadog Monitor Muting API
  slug: datadog-monitor-muting-api
- description: Validate monitor configurations before creation
  name: Datadog Monitor Validation API
  slug: datadog-monitor-validation-api
- description: Create, read, update, and delete monitors
  name: Datadog Monitors API
  slug: datadog-monitors-api
- description: The Monthly API from Datadog — 1 operation(s) for monthly.
  name: Datadog Monthly API
  slug: datadog-monthly-api
- description: The Multiple API from Datadog — 4 operation(s) for multiple.
  name: Datadog Multiple API
  slug: datadog-multiple-api
- description: The Mute API from Datadog — 1 operation(s) for mute.
  name: Datadog Mute API
  slug: datadog-mute-api
- description: The Names API from Datadog — 4 operation(s) for names.
  name: Datadog Names API
  slug: datadog-names-api
- description: The Namespaces API from Datadog — 1 operation(s) for namespaces.
  name: Datadog Namespaces API
  slug: datadog-namespaces-api
- description: The Objects API from Datadog — 2 operation(s) for objects.
  name: Datadog Objects API
  slug: datadog-objects-api
- description: The Observability API from Datadog — 2 operation(s) for observability.
  name: Datadog Observability API
  slug: datadog-observability-api
- description: The Options API from Datadog — 2 operation(s) for options.
  name: Datadog Options API
  slug: datadog-options-api
- description: The Order API from Datadog — 2 operation(s) for order.
  name: Datadog Order API
  slug: datadog-order-api
- description: Create, edit, and manage your organizations. Read more about [multi-org accounts](https://docs.datadoghq.com/account_management/multi_organization).
  name: Datadog Organizations API
  slug: datadog-organizations-api
- description: The Owned API from Datadog — 2 operation(s) for owned.
  name: Datadog Owned API
  slug: datadog-owned-api
- description: The Pages API from Datadog — 4 operation(s) for pages.
  name: Datadog Pages API
  slug: datadog-pages-api
- description: The Patch API from Datadog — 5 operation(s) for patch.
  name: Datadog Patch API
  slug: datadog-patch-api
- description: The Patterns API from Datadog — 1 operation(s) for patterns.
  name: Datadog Patterns API
  slug: datadog-patterns-api
- description: The Permissions API from Datadog — 5 operation(s) for permissions.
  name: Datadog Permissions API
  slug: datadog-permissions-api
- description: The Pipelines API from Datadog — 8 operation(s) for pipelines.
  name: Datadog Pipelines API
  slug: datadog-pipelines-api
- description: The Policies API from Datadog — 9 operation(s) for policies.
  name: Datadog Policies API
  slug: datadog-policies-api
- description: The Post API from Datadog — 4 operation(s) for post.
  name: Datadog Post API
  slug: datadog-post-api
- description: The Principal API from Datadog — 1 operation(s) for principal.
  name: Datadog Principal API
  slug: datadog-principal-api
- description: The Priority API from Datadog — 1 operation(s) for priority.
  name: Datadog Priority API
  slug: datadog-priority-api
- description: The Product API from Datadog — 1 operation(s) for product.
  name: Datadog Product API
  slug: datadog-product-api
- description: The Products API from Datadog — 2 operation(s) for products.
  name: Datadog Products API
  slug: datadog-products-api
- description: The Projects API from Datadog — 2 operation(s) for projects.
  name: Datadog Projects API
  slug: datadog-projects-api
- description: The Protections API from Datadog — 8 operation(s) for protections.
  name: Datadog Protections API
  slug: datadog-protections-api
- description: The Publish API from Datadog — 1 operation(s) for publish.
  name: Datadog Publish API
  slug: datadog-publish-api
- description: The Queries API from Datadog — 7 operation(s) for queries.
  name: Datadog Queries API
  slug: datadog-queries-api
- description: The Read API from Datadog — 1 operation(s) for read.
  name: Datadog Read API
  slug: datadog-read-api
- description: The Ready API from Datadog — 1 operation(s) for ready.
  name: Datadog Ready API
  slug: datadog-ready-api
- description: The Related API from Datadog — 2 operation(s) for related.
  name: Datadog Related API
  slug: datadog-related-api
- description: The Remove API from Datadog — 5 operation(s) for remove.
  name: Datadog Remove API
  slug: datadog-remove-api
- description: The Reorder API from Datadog — 1 operation(s) for reorder.
  name: Datadog Reorder API
  slug: datadog-reorder-api
- description: The Reports API from Datadog — 3 operation(s) for reports.
  name: Datadog Reports API
  slug: datadog-reports-api
- description: The Resolve API from Datadog — 1 operation(s) for resolve.
  name: Datadog Resolve API
  slug: datadog-resolve-api
- description: The Resource API from Datadog — 3 operation(s) for resource.
  name: Datadog Resource API
  slug: datadog-resource-api
- description: The Resources API from Datadog — 1 operation(s) for resources.
  name: Datadog Resources API
  slug: datadog-resources-api
- description: The Restrictions API from Datadog — 6 operation(s) for restrictions.
  name: Datadog Restrictions API
  slug: datadog-restrictions-api
- description: The Result API from Datadog — 1 operation(s) for result.
  name: Datadog Result API
  slug: datadog-result-api
- description: The Retention API from Datadog — 6 operation(s) for retention.
  name: Datadog Retention API
  slug: datadog-retention-api
- description: The Revoke API from Datadog — 3 operation(s) for revoke.
  name: Datadog Revoke API
  slug: datadog-revoke-api
- description: The Role API from Datadog — 8 operation(s) for role.
  name: Datadog Role API
  slug: datadog-role-api
- description: The Roles API is used to create and manage Datadog roles, what [global permissions](https://docs.datadoghq.com/account_management/rbac/) they grant, and which users belong to them. Permissions related
  name: Datadog Roles API
  slug: datadog-roles-api
- description: The Routing API from Datadog — 1 operation(s) for routing.
  name: Datadog Routing API
  slug: datadog-routing-api
- description: The Rules API from Datadog — 27 operation(s) for rules.
  name: Datadog Rules API
  slug: datadog-rules-api
- description: Manage your Real User Monitoring (RUM) applications, and search or aggregate your RUM events over HTTP. See the [RUM & Session Replay page](https://docs.datadoghq.com/real_user_monitoring/) for more i
  name: Datadog Rum API
  slug: datadog-rum-api
- description: The Runs API from Datadog — 1 operation(s) for runs.
  name: Datadog Runs API
  slug: datadog-runs-api
- description: The Save API from Datadog — 1 operation(s) for save.
  name: Datadog Save API
  slug: datadog-save-api
- description: The Scan API from Datadog — 2 operation(s) for scan.
  name: Datadog Scan API
  slug: datadog-scan-api
- description: The Scanning API from Datadog — 5 operation(s) for scanning.
  name: Datadog Scanning API
  slug: datadog-scanning-api
- description: The Schedules API from Datadog — 4 operation(s) for schedules.
  name: Datadog Schedules API
  slug: datadog-schedules-api
- description: The Search API from Datadog — 10 operation(s) for search.
  name: Datadog Search API
  slug: datadog-search-api
- description: The Security API from Datadog — 8 operation(s) for security.
  name: Datadog Security API
  slug: datadog-security-api
- description: The Send API from Datadog — 5 operation(s) for send.
  name: Datadog Send API
  slug: datadog-send-api
- description: The Serverless API from Datadog — 2 operation(s) for serverless.
  name: Datadog Serverless API
  slug: datadog-serverless-api
- description: The Sets API from Datadog — 2 operation(s) for sets.
  name: Datadog Sets API
  slug: datadog-sets-api
- description: The Setting API from Datadog — 1 operation(s) for setting.
  name: Datadog Setting API
  slug: datadog-setting-api
- description: The Settings API from Datadog — 1 operation(s) for settings.
  name: Datadog Settings API
  slug: datadog-settings-api
- description: The Signal API from Datadog — 4 operation(s) for signal.
  name: Datadog Signal API
  slug: datadog-signal-api
- description: The Single API from Datadog — 3 operation(s) for single.
  name: Datadog Single API
  slug: datadog-single-api
- description: The Specific API from Datadog — 2 operation(s) for specific.
  name: Datadog Specific API
  slug: datadog-specific-api
- description: The Standard API from Datadog — 1 operation(s) for standard.
  name: Datadog Standard API
  slug: datadog-standard-api
- description: The State API from Datadog — 1 operation(s) for state.
  name: Datadog State API
  slug: datadog-state-api
- description: The Status API from Datadog — 2 operation(s) for status.
  name: Datadog Status API
  slug: datadog-status-api
- description: The Submit API from Datadog — 1 operation(s) for submit.
  name: Datadog Submit API
  slug: datadog-submit-api
- description: The Suppression API from Datadog — 2 operation(s) for suppression.
  name: Datadog Suppression API
  slug: datadog-suppression-api
- description: The Tasks API from Datadog — 2 operation(s) for tasks.
  name: Datadog Tasks API
  slug: datadog-tasks-api
- description: View and manage teams within Datadog. See the [Teams page](https://docs.datadoghq.com/account_management/teams/) for more information.
  name: Datadog Teams API
  slug: datadog-teams-api
- description: The Terraform API from Datadog — 2 operation(s) for terraform.
  name: Datadog Terraform API
  slug: datadog-terraform-api
- description: The Tests API from Datadog — 5 operation(s) for tests.
  name: Datadog Tests API
  slug: datadog-tests-api
- description: The Type API from Datadog — 2 operation(s) for type.
  name: Datadog Type API
  slug: datadog-type-api
- description: The Types API from Datadog — 1 operation(s) for types.
  name: Datadog Types API
  slug: datadog-types-api
- description: The Unarchive API from Datadog — 1 operation(s) for unarchive.
  name: Datadog Unarchive API
  slug: datadog-unarchive-api
- description: The Unassign API from Datadog — 1 operation(s) for unassign.
  name: Datadog Unassign API
  slug: datadog-unassign-api
- description: The Update API from Datadog — 72 operation(s) for update.
  name: Datadog Update API
  slug: datadog-update-api
- description: The Upload API from Datadog — 2 operation(s) for upload.
  name: Datadog Upload API
  slug: datadog-upload-api
- description: The Usage API from Datadog — 5 operation(s) for usage.
  name: Datadog Usage API
  slug: datadog-usage-api
- description: Create, edit, and disable users.
  name: Datadog Users API
  slug: datadog-users-api
- description: The Validate API from Datadog — 2 operation(s) for validate.
  name: Datadog Validate API
  slug: datadog-validate-api
- description: The Value API from Datadog — 2 operation(s) for value.
  name: Datadog Value API
  slug: datadog-value-api
- description: The Versions API from Datadog — 1 operation(s) for versions.
  name: Datadog Versions API
  slug: datadog-versions-api
- description: The Volumes API from Datadog — 1 operation(s) for volumes.
  name: Datadog Volumes API
  slug: datadog-volumes-api
- description: The Vulnerabilities API from Datadog — 3 operation(s) for vulnerabilities.
  name: Datadog Vulnerabilities API
  slug: datadog-vulnerabilities-api
- description: The Webhooks API from Datadog — 2 operation(s) for webhooks.
  name: Datadog Webhooks API
  slug: datadog-webhooks-api
- description: The Workflows API from Datadog — 7 operation(s) for workflows.
  name: Datadog Workflows API
  slug: datadog-workflows-api
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
artifact_total: 558
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
  name: Datadog API
  slug: open-datadog-api
- collection_type: open
  name: Datadog Events API
  slug: open-datadog-events
- collection_type: open
  name: Datadog Incidents API
  slug: open-datadog-incidents
- collection_type: open
  name: Datadog Logs API
  slug: open-datadog-logs
- collection_type: open
  name: Datadog Metrics API
  slug: open-datadog-metrics
- collection_type: open
  name: Datadog Monitors API
  slug: open-datadog-monitors
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/datadog-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/datadog-trust-center.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/datadog-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/datadog-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/datadog-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/datadog-scopes.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/datadog-bulk-mute-monitors-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/datadog-cleanup-stale-monitors-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/datadog-create-incident-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/datadog-create-log-archive-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/datadog-create-log-metric-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/datadog-create-log-pipeline-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/datadog-create-monitor-config-policy-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/datadog-create-monitor-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/datadog-create-role-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/datadog-create-service-account-key-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/datadog-create-team-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/datadog-declare-incident-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/datadog-ingest-and-search-logs-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/datadog-invite-user-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/datadog-manage-api-keys-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/datadog-manage-incident-attachments-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/datadog-manage-metric-metadata-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/datadog-mute-monitor-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/datadog-post-and-search-events-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/datadog-resolve-incident-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/datadog-schedule-downtime-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/datadog-search-incidents-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/datadog-submit-and-query-metrics-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/datadog-tune-monitor-thresholds-workflow.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/datadog
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
  title: ''
  type: JSONLD
  url: json-ld/datadog-context.jsonld
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/datadog-metric-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/datadog-monitor-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/datadog-log-event-schema.json
- group: docs
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
- name: Datadog Finops
  service_category: Observability
  slug: datadog-finops
graphqls:
- description: 'This conceptual GraphQL schema models the Datadog observability and monitoring platform. Datadog does not currently expose a public GraphQL API; this schema is a structured representation of the core '
  name: Datadog GraphQL Schema
  slug: datadog-graphql
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
modified: '2026-05-19'
name: Datadog
nav: Providers
network: true
overview: 'Datadog publishes 221 APIs on the [APIs.io](https://apis.io/) network, including Dashboards API, Users API, Roles API, and 218 more. Tagged areas include Analytics, Dashboards, Monitoring, Platform, and T1.


  The Datadog catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Datadog''s developer surface includes authentication, developer portal, documentation, engineering blog, support, pricing, signup flow, and 77 more developer resources.'
plans:
- name: Datadog Plans Pricing
  plan_count: 7
  slug: datadog-plans-pricing
random_paper: 28
rate_limits:
- limit_count: 6
  name: Datadog Rate Limits
  slug: datadog-rate-limits
rules:
- name: Datadog API Rules
  rule_count: 6
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 5
  slug: datadog-jsonschema-spectral-rules
- name: Datadog API Rules
  rule_count: 25
  severity_counts:
    error: 14
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
  composite: 69.9
  delta: 0.0
  facets:
    commercial_clarity: 92.1
    contract_quality: 73.1
    developer_ergonomics: 65.2
    discoverability: 50.0
    governance: 58.3
    operational_transparency: 63.2
  previous_composite: 69.9
  provenance:
    agentic_access: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 211
  schema_version: 0.9.1
  scored_at: '2026-08-10'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/datadog/refs/heads/main/screenshots/datadog-2026-06-20T175637.png
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
- Analytics
- Dashboards
- Monitoring
- Platform
- T1
- Visualizations
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
