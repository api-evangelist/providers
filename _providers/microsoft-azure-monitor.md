---
access_model:
  confidence: high
  label: Paid · Self-serve signup
  onboarding: self-serve
  pricing: paid
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: verified
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 37.8
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 33
  human_in_the_loop: 0
  name: Microsoft Azure Monitor Agentic Access
  operation_count: 72
  slug: microsoft-azure-monitor-agentic-access
  summary_line: 72 operations · 33 acting
api_count: 19
apis:
- description: Operations for managing action groups
  name: Azure Monitor Action Groups API
  slug: microsoft-azure-monitor-action-groups-api
- description: Operations for querying Azure Activity Log events
  name: Azure Monitor Activity Logs API
  slug: microsoft-azure-monitor-activity-logs-api
- description: Operations for managing classic metric alert rules
  name: Azure Monitor Alert Rules API
  slug: microsoft-azure-monitor-alert-rules-api
- description: Operations for managing autoscale settings
  name: Azure Monitor Autoscale Settings API
  slug: microsoft-azure-monitor-autoscale-settings-api
- description: Operations for managing data collection endpoints
  name: Azure Monitor Data Collection Endpoints API
  slug: microsoft-azure-monitor-data-collection-endpoints-api
- description: Operations for managing data collection rules
  name: Azure Monitor Data Collection Rules API
  slug: microsoft-azure-monitor-data-collection-rules-api
- description: Operations for managing diagnostic settings on Azure resources
  name: Azure Monitor Diagnostic Settings API
  slug: microsoft-azure-monitor-diagnostic-settings-api
- description: Operations for retrieving Application Insights events
  name: Azure Monitor Events API
  slug: microsoft-azure-monitor-events-api
- description: Operations for ingesting custom log data into Azure Monitor
  name: Azure Monitor Logs Ingestion API
  slug: microsoft-azure-monitor-logs-ingestion-api
- description: Operations for retrieving Application Insights metadata
  name: Azure Monitor Metadata API
  slug: microsoft-azure-monitor-metadata-api
- description: Operations for listing metric definitions
  name: Azure Monitor Metric Definitions API
  slug: microsoft-azure-monitor-metric-definitions-api
- description: Operations for retrieving Application Insights metrics
  name: Azure Monitor Metrics API
  slug: microsoft-azure-monitor-metrics-api
- description: Operations for batch querying Azure Monitor metrics across multiple resources
  name: Azure Monitor Metrics Batch API
  slug: microsoft-azure-monitor-metrics-batch-api
- description: Operations for getting predictive autoscale metrics
  name: Azure Monitor Predictive Metrics API
  slug: microsoft-azure-monitor-predictive-metrics-api
- description: Operations for managing Azure Monitor Private Link Scopes
  name: Azure Monitor Private Link Scopes API
  slug: microsoft-azure-monitor-private-link-scopes-api
- description: Operations for querying Application Insights telemetry data
  name: Azure Monitor Query API
  slug: microsoft-azure-monitor-query-api
- description: Operations for managing scheduled query-based alert rules
  name: Azure Monitor Scheduled Query Rules API
  slug: microsoft-azure-monitor-scheduled-query-rules-api
- description: Operations for managing scoped resources within a Private Link Scope
  name: Azure Monitor Scoped Resources API
  slug: microsoft-azure-monitor-scoped-resources-api
- description: Operations for sending and retrieving test notifications
  name: Azure Monitor Test Notifications API
  slug: microsoft-azure-monitor-test-notifications-api
arazzos:
- description: Create an action group, read it back, and send a test notification to validate its receivers.
  name: Azure Monitor Action Group Lifecycle
  slug: microsoft-azure-monitor-action-group-lifecycle-workflow
- description: Read an action group, then re-enable a receiver that had been unsubscribed.
  name: Azure Monitor Action Group Receiver Recovery
  slug: microsoft-azure-monitor-action-group-receiver-recovery-workflow
- description: Create an action group, attach it to a new classic metric alert rule, and confirm the rule.
  name: Azure Monitor Action Group With Metric Alert
  slug: microsoft-azure-monitor-action-group-with-metric-alert-workflow
- description: Pull recent Activity Log events for a subscription, then drill into a resource's metric definitions and values.
  name: Azure Monitor Activity Log To Metrics
  slug: microsoft-azure-monitor-activity-log-to-metrics-workflow
- description: List classic alert rules in a resource group, branch on whether any exist, then inspect and re-tag the first rule.
  name: Azure Monitor Alert Rule Audit
  slug: microsoft-azure-monitor-alert-rule-audit-workflow
- description: List autoscale settings in a resource group, branch on whether any exist, then inspect and disable a named setting.
  name: Azure Monitor Autoscale Inventory And Reconfigure
  slug: microsoft-azure-monitor-autoscale-inventory-reconfigure-workflow
- description: Create an autoscale setting with a CPU-driven scale rule, confirm it, and pull its predictive metrics.
  name: Azure Monitor Autoscale Setting Provision
  slug: microsoft-azure-monitor-autoscale-setting-provision-workflow
- description: Resolve a resource's metric definitions, then batch-query the same metric across many resources at once.
  name: Azure Monitor Batch Metrics Query
  slug: microsoft-azure-monitor-batch-metrics-query-workflow
- description: Inventory existing diagnostic settings on a resource, route its logs and metrics to a destination, and confirm.
  name: Azure Monitor Diagnostic Setting Provision
  slug: microsoft-azure-monitor-diagnostic-setting-provision-workflow
- description: Discover the metric definitions available for a resource and then pull the metric values for them.
  name: Azure Monitor Resource Metrics Explorer
  slug: microsoft-azure-monitor-resource-metrics-explorer-workflow
artifact_total: 179
collections:
- collection_type: postman
  name: Azure Monitor Action Groups API
  slug: postman-azure-monitor-action-groups
- collection_type: postman
  name: Azure Monitor Activity Log API
  slug: postman-azure-monitor-activity-log
- collection_type: postman
  name: Azure Monitor Alerts API
  slug: postman-azure-monitor-alerts
- collection_type: postman
  name: Azure Monitor Azure Application Insights API
  slug: postman-azure-monitor-application-insights
- collection_type: postman
  name: Azure Monitor Autoscale API
  slug: postman-azure-monitor-autoscale
- collection_type: postman
  name: Azure Monitor Data Collection Endpoints API
  slug: postman-azure-monitor-data-collection-endpoints
- collection_type: postman
  name: Azure Monitor Data Collection Rules API
  slug: postman-azure-monitor-data-collection-rules
- collection_type: postman
  name: Azure Monitor Diagnostic Settings API
  slug: postman-azure-monitor-diagnostic-settings
- collection_type: postman
  name: Azure Monitor Logs Ingestion API
  slug: postman-azure-monitor-logs-ingestion
- collection_type: postman
  name: Azure Monitor Logs API
  slug: postman-azure-monitor-logs
- collection_type: postman
  name: Azure Monitor Metric Definitions API
  slug: postman-azure-monitor-metric-definitions
- collection_type: postman
  name: Azure Monitor Metrics Batch API
  slug: postman-azure-monitor-metrics-batch
- collection_type: postman
  name: Azure Monitor Metrics API
  slug: postman-azure-monitor-metrics
- collection_type: postman
  name: Azure Monitor Private Link Scopes API
  slug: postman-azure-monitor-private-link-scopes
- collection_type: postman
  name: Azure Monitor Scheduled Query Rules API
  slug: postman-azure-monitor-scheduled-query-rules
- collection_type: open
  name: Azure Monitor Action Groups API
  slug: open-azure-monitor-action-groups
- collection_type: open
  name: Azure Monitor Activity Log API
  slug: open-azure-monitor-activity-log
- collection_type: open
  name: Azure Monitor Alerts API
  slug: open-azure-monitor-alerts
- collection_type: open
  name: Azure Monitor Azure Application Insights API
  slug: open-azure-monitor-application-insights
- collection_type: open
  name: Azure Monitor Autoscale API
  slug: open-azure-monitor-autoscale
- collection_type: open
  name: Azure Monitor Data Collection Endpoints API
  slug: open-azure-monitor-data-collection-endpoints
- collection_type: open
  name: Azure Monitor Data Collection Rules API
  slug: open-azure-monitor-data-collection-rules
- collection_type: open
  name: Azure Monitor Diagnostic Settings API
  slug: open-azure-monitor-diagnostic-settings
- collection_type: open
  name: Azure Monitor Logs Ingestion API
  slug: open-azure-monitor-logs-ingestion
- collection_type: open
  name: Azure Monitor Logs API
  slug: open-azure-monitor-logs
- collection_type: open
  name: Azure Monitor Metric Definitions API
  slug: open-azure-monitor-metric-definitions
- collection_type: open
  name: Azure Monitor Metrics Batch API
  slug: open-azure-monitor-metrics-batch
- collection_type: open
  name: Azure Monitor Metrics API
  slug: open-azure-monitor-metrics
- collection_type: open
  name: Azure Monitor Private Link Scopes API
  slug: open-azure-monitor-private-link-scopes
- collection_type: open
  name: Azure Monitor Scheduled Query Rules API
  slug: open-azure-monitor-scheduled-query-rules
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/microsoft-azure-monitor-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/microsoft-azure-monitor-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/microsoft-azure-monitor-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/microsoft-azure-monitor-scopes.yml
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/azure-monitor/overview
- group: design
  title: ''
  type: Arazzo
  url: arazzo/microsoft-azure-monitor-action-group-lifecycle-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/microsoft-azure-monitor-action-group-receiver-recovery-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/microsoft-azure-monitor-action-group-with-metric-alert-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/microsoft-azure-monitor-activity-log-to-metrics-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/microsoft-azure-monitor-alert-rule-audit-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/microsoft-azure-monitor-autoscale-inventory-reconfigure-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/microsoft-azure-monitor-autoscale-setting-provision-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/microsoft-azure-monitor-batch-metrics-query-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/microsoft-azure-monitor-diagnostic-setting-provision-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/microsoft-azure-monitor-resource-metrics-explorer-workflow.yml
- group: start
  title: ''
  type: Portal
  url: https://portal.azure.com
- group: docs
  title: ''
  type: Documentation
  url: https://learn.microsoft.com/en-us/azure/azure-monitor/
- group: start
  title: ''
  type: GettingStarted
  url: https://learn.microsoft.com/en-us/azure/azure-monitor/overview
- group: auth
  title: ''
  type: Authentication
  url: https://learn.microsoft.com/en-us/azure/azure-monitor/logs/api/access-api
- group: company
  title: ''
  type: Blog
  url: https://azure.microsoft.com/en-us/blog/topics/monitor/
- group: operate
  title: ''
  type: ChangeLog
  url: https://learn.microsoft.com/en-us/azure/azure-monitor/fundamentals/whats-new
- group: build
  title: ''
  type: SDKs
  url: https://learn.microsoft.com/en-us/azure/azure-monitor/app/platforms
- group: commercial
  title: ''
  type: Pricing
  url: https://azure.microsoft.com/en-us/pricing/details/monitor/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.azure.com/
- group: operate
  title: ''
  type: Support
  url: https://azure.microsoft.com/en-us/support/options/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://azure.microsoft.com/en-us/support/legal/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://azure.microsoft.com/en-us/explore/trusted-cloud/privacy
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Azure
- group: operate
  title: ''
  type: Community
  url: https://techcommunity.microsoft.com/t5/azure-monitor/bd-p/AzureMonitor
- group: company
  title: ''
  type: Website
  url: https://azure.microsoft.com/en-us/products/monitor
- group: start
  title: ''
  type: Login
  url: https://portal.azure.com
- group: start
  title: ''
  type: Signup
  url: https://azure.microsoft.com/en-us/free
- group: design
  title: ''
  type: JSONLD
  url: json-ld/azure-monitor-context.jsonld
created: '2024'
description: Azure Monitor helps you maximize the availability and performance of your applications and services. It delivers a comprehensive solution for collecting, analyzing, and acting on telemetry from your cloud and on-premises environments.
finops:
- name: Microsoft Azure Monitor Finops
  service_category: Observability / Monitoring
  slug: microsoft-azure-monitor-finops
image: https://azure.microsoft.com/svghandler/monitor/
json_schemas:
- name: Azure Monitor Action Group
  property_count: 6
  slug: azure-monitor-action-group
- name: Azure Monitor Activity Log Event
  property_count: 24
  slug: azure-monitor-activity-log-event
- name: Azure Monitor Alert Rule
  property_count: 6
  slug: azure-monitor-alert-rule
- name: Azure Monitor Autoscale Setting
  property_count: 6
  slug: azure-monitor-autoscale-setting
- name: Azure Monitor Data Collection Rule
  property_count: 7
  slug: azure-monitor-data-collection-rule
- name: Azure Monitor Diagnostic Setting
  property_count: 4
  slug: azure-monitor-diagnostic-setting
- name: Azure Monitor Log Query
  property_count: 2
  slug: azure-monitor-log-query
- name: Azure Monitor Metric Definition
  property_count: 13
  slug: azure-monitor-metric-definition
- name: Azure Monitor Metric
  property_count: 8
  slug: azure-monitor-metric
- name: ActionGroup
  property_count: 13
  slug: microsoft-azure-monitor-actiongroup
- name: ActionGroupList
  property_count: 2
  slug: microsoft-azure-monitor-actiongrouplist
- name: ActionGroupPatchBody
  property_count: 2
  slug: microsoft-azure-monitor-actiongrouppatchbody
- name: ActionGroupResource
  property_count: 6
  slug: microsoft-azure-monitor-actiongroupresource
- name: Actions
  property_count: 2
  slug: microsoft-azure-monitor-actions
- name: AlertRule
  property_count: 7
  slug: microsoft-azure-monitor-alertrule
- name: AlertRuleResource
  property_count: 6
  slug: microsoft-azure-monitor-alertruleresource
- name: AlertRuleResourceCollection
  property_count: 1
  slug: microsoft-azure-monitor-alertruleresourcecollection
- name: AlertRuleResourcePatch
  property_count: 2
  slug: microsoft-azure-monitor-alertruleresourcepatch
- name: ArmRoleReceiver
  property_count: 3
  slug: microsoft-azure-monitor-armrolereceiver
- name: AutomationRunbookReceiver
  property_count: 7
  slug: microsoft-azure-monitor-automationrunbookreceiver
- name: AutoscaleNotification
  property_count: 3
  slug: microsoft-azure-monitor-autoscalenotification
- name: AutoscaleProfile
  property_count: 5
  slug: microsoft-azure-monitor-autoscaleprofile
- name: AutoscaleSetting
  property_count: 7
  slug: microsoft-azure-monitor-autoscalesetting
- name: AutoscaleSettingResource
  property_count: 6
  slug: microsoft-azure-monitor-autoscalesettingresource
- name: AutoscaleSettingResourceCollection
  property_count: 2
  slug: microsoft-azure-monitor-autoscalesettingresourcecollection
- name: AutoscaleSettingResourcePatch
  property_count: 2
  slug: microsoft-azure-monitor-autoscalesettingresourcepatch
- name: AzureAppPushReceiver
  property_count: 2
  slug: microsoft-azure-monitor-azureapppushreceiver
- name: AzureFunctionReceiver
  property_count: 5
  slug: microsoft-azure-monitor-azurefunctionreceiver
- name: AzureMonitorPrivateLinkScope
  property_count: 7
  slug: microsoft-azure-monitor-azuremonitorprivatelinkscope
- name: AzureMonitorPrivateLinkScopeListResult
  property_count: 2
  slug: microsoft-azure-monitor-azuremonitorprivatelinkscopelistresult
- name: AzureMonitorPrivateLinkScopeProperties
  property_count: 3
  slug: microsoft-azure-monitor-azuremonitorprivatelinkscopeproperties
- name: Column
  property_count: 2
  slug: microsoft-azure-monitor-column
- name: Condition
  property_count: 9
  slug: microsoft-azure-monitor-condition
- name: DataCollectionEndpoint
  property_count: 10
  slug: microsoft-azure-monitor-datacollectionendpoint
- name: DataCollectionEndpointResource
  property_count: 9
  slug: microsoft-azure-monitor-datacollectionendpointresource
- name: DataCollectionEndpointResourceListResult
  property_count: 2
  slug: microsoft-azure-monitor-datacollectionendpointresourcelistresult
- name: DataCollectionRule
  property_count: 8
  slug: microsoft-azure-monitor-datacollectionrule
- name: DataCollectionRuleResource
  property_count: 9
  slug: microsoft-azure-monitor-datacollectionruleresource
- name: DataCollectionRuleResourceListResult
  property_count: 2
  slug: microsoft-azure-monitor-datacollectionruleresourcelistresult
- name: DataFlow
  property_count: 5
  slug: microsoft-azure-monitor-dataflow
- name: DataSources
  property_count: 5
  slug: microsoft-azure-monitor-datasources
- name: Destinations
  property_count: 7
  slug: microsoft-azure-monitor-destinations
- name: DiagnosticSettings
  property_count: 9
  slug: microsoft-azure-monitor-diagnosticsettings
- name: DiagnosticSettingsResource
  property_count: 5
  slug: microsoft-azure-monitor-diagnosticsettingsresource
- name: DiagnosticSettingsResourceCollection
  property_count: 1
  slug: microsoft-azure-monitor-diagnosticsettingsresourcecollection
- name: Dimension
  property_count: 3
  slug: microsoft-azure-monitor-dimension
- name: EmailReceiver
  property_count: 4
  slug: microsoft-azure-monitor-emailreceiver
- name: EnableRequest
  property_count: 1
  slug: microsoft-azure-monitor-enablerequest
- name: ErrorResponse
  property_count: 2
  slug: microsoft-azure-monitor-errorresponse
- name: EventData
  property_count: 24
  slug: microsoft-azure-monitor-eventdata
- name: EventDataCollection
  property_count: 2
  slug: microsoft-azure-monitor-eventdatacollection
- name: EventHubReceiver
  property_count: 6
  slug: microsoft-azure-monitor-eventhubreceiver
- name: EventsResultData
  property_count: 10
  slug: microsoft-azure-monitor-eventsresultdata
- name: EventsResults
  property_count: 4
  slug: microsoft-azure-monitor-eventsresults
- name: ItsmReceiver
  property_count: 5
  slug: microsoft-azure-monitor-itsmreceiver
- name: LocalizableString
  property_count: 2
  slug: microsoft-azure-monitor-localizablestring
- name: LogicAppReceiver
  property_count: 4
  slug: microsoft-azure-monitor-logicappreceiver
- name: LogSettings
  property_count: 4
  slug: microsoft-azure-monitor-logsettings
- name: ManagedServiceIdentity
  property_count: 4
  slug: microsoft-azure-monitor-managedserviceidentity
- name: MetadataFunction
  property_count: 4
  slug: microsoft-azure-monitor-metadatafunction
- name: MetadataResults
  property_count: 2
  slug: microsoft-azure-monitor-metadataresults
- name: MetadataTable
  property_count: 4
  slug: microsoft-azure-monitor-metadatatable
- name: MetadataValue
  property_count: 2
  slug: microsoft-azure-monitor-metadatavalue
- name: Metric
  property_count: 6
  slug: microsoft-azure-monitor-metric
- name: MetricAvailability
  property_count: 2
  slug: microsoft-azure-monitor-metricavailability
- name: MetricDefinition
  property_count: 13
  slug: microsoft-azure-monitor-metricdefinition
- name: MetricDefinitionCollection
  property_count: 1
  slug: microsoft-azure-monitor-metricdefinitioncollection
- name: MetricResultsResponse
  property_count: 7
  slug: microsoft-azure-monitor-metricresultsresponse
- name: MetricsBatchRequest
  property_count: 1
  slug: microsoft-azure-monitor-metricsbatchrequest
- name: MetricsBatchResponse
  property_count: 1
  slug: microsoft-azure-monitor-metricsbatchresponse
- name: MetricSettings
  property_count: 4
  slug: microsoft-azure-monitor-metricsettings
- name: MetricsPostBody
  property_count: 2
  slug: microsoft-azure-monitor-metricspostbody
- name: MetricsResponse
  property_count: 6
  slug: microsoft-azure-monitor-metricsresponse
- name: MetricsResult
  property_count: 1
  slug: microsoft-azure-monitor-metricsresult
- name: MetricTrigger
  property_count: 12
  slug: microsoft-azure-monitor-metrictrigger
- name: MetricUnit
  property_count: 0
  slug: microsoft-azure-monitor-metricunit
- name: MetricValue
  property_count: 6
  slug: microsoft-azure-monitor-metricvalue
- name: NotificationRequestBody
  property_count: 6
  slug: microsoft-azure-monitor-notificationrequestbody
- name: PredictiveAutoscalePolicy
  property_count: 2
  slug: microsoft-azure-monitor-predictiveautoscalepolicy
- name: PredictiveResponse
  property_count: 5
  slug: microsoft-azure-monitor-predictiveresponse
- name: QueryBody
  property_count: 3
  slug: microsoft-azure-monitor-querybody
- name: QueryResults
  property_count: 1
  slug: microsoft-azure-monitor-queryresults
- name: Recurrence
  property_count: 2
  slug: microsoft-azure-monitor-recurrence
- name: RecurrentSchedule
  property_count: 4
  slug: microsoft-azure-monitor-recurrentschedule
- name: ResourceForUpdate
  property_count: 2
  slug: microsoft-azure-monitor-resourceforupdate
- name: RetentionPolicy
  property_count: 2
  slug: microsoft-azure-monitor-retentionpolicy
- name: RuleAction
  property_count: 1
  slug: microsoft-azure-monitor-ruleaction
- name: RuleCondition
  property_count: 2
  slug: microsoft-azure-monitor-rulecondition
- name: RuleDataSource
  property_count: 5
  slug: microsoft-azure-monitor-ruledatasource
- name: ScaleAction
  property_count: 4
  slug: microsoft-azure-monitor-scaleaction
- name: ScaleCapacity
  property_count: 3
  slug: microsoft-azure-monitor-scalecapacity
- name: ScaleRule
  property_count: 2
  slug: microsoft-azure-monitor-scalerule
- name: ScaleRuleMetricDimension
  property_count: 3
  slug: microsoft-azure-monitor-scalerulemetricdimension
- name: ScheduledQueryRuleCriteria
  property_count: 1
  slug: microsoft-azure-monitor-scheduledqueryrulecriteria
- name: ScheduledQueryRuleProperties
  property_count: 18
  slug: microsoft-azure-monitor-scheduledqueryruleproperties
- name: ScheduledQueryRuleResource
  property_count: 9
  slug: microsoft-azure-monitor-scheduledqueryruleresource
- name: ScheduledQueryRuleResourceCollection
  property_count: 2
  slug: microsoft-azure-monitor-scheduledqueryruleresourcecollection
- name: ScheduledQueryRuleResourcePatch
  property_count: 2
  slug: microsoft-azure-monitor-scheduledqueryruleresourcepatch
- name: ScopedResource
  property_count: 5
  slug: microsoft-azure-monitor-scopedresource
- name: ScopedResourceListResult
  property_count: 2
  slug: microsoft-azure-monitor-scopedresourcelistresult
- name: SmsReceiver
  property_count: 4
  slug: microsoft-azure-monitor-smsreceiver
- name: SubscriptionScopeMetricsRequestBody
  property_count: 12
  slug: microsoft-azure-monitor-subscriptionscopemetricsrequestbody
- name: SystemData
  property_count: 6
  slug: microsoft-azure-monitor-systemdata
- name: Table
  property_count: 3
  slug: microsoft-azure-monitor-table
- name: TagsResource
  property_count: 1
  slug: microsoft-azure-monitor-tagsresource
- name: TestNotificationDetailsResponse
  property_count: 4
  slug: microsoft-azure-monitor-testnotificationdetailsresponse
- name: TimeSeriesElement
  property_count: 2
  slug: microsoft-azure-monitor-timeserieselement
- name: TimeWindow
  property_count: 3
  slug: microsoft-azure-monitor-timewindow
- name: VoiceReceiver
  property_count: 3
  slug: microsoft-azure-monitor-voicereceiver
- name: WebhookReceiver
  property_count: 7
  slug: microsoft-azure-monitor-webhookreceiver
json_structures:
- name: Microsoft Azure Monitor Structure
  property_count: 0
  slug: microsoft-azure-monitor-structure
jsonld:
- class_count: 0
  name: Azure Monitor Context
  property_count: 13
  slug: azure-monitor-context
layout: provider
modified: '2026-05-19'
name: Azure Monitor
nav: Providers
network: true
overview: 'Azure Monitor publishes 19 APIs on the [APIs.io](https://apis.io/) network, including Action Groups API, Activity Logs API, Alert Rules API, and 16 more. Tagged areas include Application Insights, Cloud, Logs, Metrics, and Monitoring.


  The Azure Monitor catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Azure Monitor''s developer surface includes authentication, developer portal, documentation, getting-started guide, engineering blog, changelog, pricing, and 26 more developer resources.'
plans:
- name: Microsoft Azure Monitor Plans Pricing
  plan_count: 7
  slug: microsoft-azure-monitor-plans-pricing
random_paper: 21
rate_limits:
- limit_count: 8
  name: Microsoft Azure Monitor Rate Limits
  slug: microsoft-azure-monitor-rate-limits
rules:
- name: Azure Monitor API Rules
  rule_count: 6
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 4
  slug: microsoft-azure-monitor-jsonschema-spectral-rules
scopes:
- name: Microsoft Azure Monitor Scopes
  scope_count: 4
  slug: microsoft-azure-monitor-scopes
  summary_line: 4 scopes · clientCredentials
score:
  band: exemplar
  composite: 70.0
  delta: -3.3
  facets:
    commercial_clarity: 84.2
    contract_quality: 73.7
    developer_ergonomics: 56.5
    discoverability: 75.9
    governance: 58.3
    operational_transparency: 68.4
  previous_composite: 73.3
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 19
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/microsoft-azure-monitor/refs/heads/main/screenshots/microsoft-azure-monitor-2026-06-20T185425.png
security:
- kind: authentication
  name: Microsoft Azure Monitor Authentication
  slug: microsoft-azure-monitor-authentication
  summary_line: apiKey/oauth2 · 2 schemes
- kind: domain-security
  name: Microsoft Azure Monitor Domain Security
  slug: microsoft-azure-monitor-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: microsoft-azure-monitor
tags:
- Application Insights
- Cloud
- Logs
- Metrics
- Monitoring
- Observability
website: https://azure.microsoft.com/en-us/products/monitor
---
