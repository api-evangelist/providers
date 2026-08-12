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
    mcp_server: false
    openapi_examples: verified
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 44.1
  scored_at: '2026-08-11'
agentic_access:
- acting_count: 25
  human_in_the_loop: 1
  name: Cloudwatch Agentic Access
  operation_count: 25
  slug: cloudwatch-agentic-access
  summary_line: 25 operations · 25 acting · 1 human-in-the-loop
api_count: 8
apis:
- description: API for automatic instrumentation and monitoring of application services with service level objectives.
  name: Amazon CloudWatch Application Signals API
  slug: amazon-cloudwatch-application-signals-api
- description: API for active network monitoring to identify network issues within AWS or company networks using synthetic probes.
  name: Amazon CloudWatch Network Monitor API
  slug: amazon-cloudwatch-network-monitor-api
- description: Operations for creating, managing, and querying CloudWatch alarms
  name: AWS CloudWatch Alarms API
  slug: cloudwatch-alarms-api
- description: Operations for CloudWatch anomaly detection models
  name: AWS CloudWatch Anomaly Detection API
  slug: cloudwatch-anomaly-detection-api
- description: Operations for composite alarms that aggregate multiple alarm states
  name: AWS CloudWatch Composite Alarms API
  slug: cloudwatch-composite-alarms-api
- description: Operations for creating and managing CloudWatch dashboards
  name: AWS CloudWatch Dashboards API
  slug: cloudwatch-dashboards-api
- description: Operations for managing metric streams
  name: AWS CloudWatch Metric Streams API
  slug: cloudwatch-metric-streams-api
- description: Operations for working with CloudWatch metrics and metric data
  name: AWS CloudWatch Metrics API
  slug: cloudwatch-metrics-api
artifact_total: 341
collections:
- collection_type: postman
  name: AWS CloudWatch Amazon CloudWatch Alarms API
  slug: postman-cloudwatch-alarms-api
- collection_type: postman
  name: AWS CloudWatch Amazon CloudWatch Alarms Anomaly Detection API
  slug: postman-cloudwatch-anomaly-detection-api
- collection_type: postman
  name: AWS CloudWatch Amazon CloudWatch Alarms Composite Alarms API
  slug: postman-cloudwatch-composite-alarms-api
- collection_type: postman
  name: AWS CloudWatch Amazon CloudWatch Alarms Dashboards API
  slug: postman-cloudwatch-dashboards-api
- collection_type: postman
  name: AWS CloudWatch Amazon CloudWatch Alarms Metric Streams API
  slug: postman-cloudwatch-metric-streams-api
- collection_type: postman
  name: AWS CloudWatch Amazon CloudWatch Alarms Metrics API
  slug: postman-cloudwatch-metrics-api
- collection_type: open
  name: AWS CloudWatch Amazon CloudWatch API
  slug: open-cloudwatch
common:
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/aws-cloudwatch/overview
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/cloudwatch-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/cloudwatch-trust-center.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/cloudwatch-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/cloudwatch-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/cloudwatch-authentication.yml
- group: company
  title: ''
  type: Blog
  url: https://aws.amazon.com/blogs/aws/category/management-tools/amazon-cloudwatch/
- group: operate
  title: ''
  type: FAQ
  url: https://aws.amazon.com/cloudwatch/faqs/
- group: operate
  title: ''
  type: Support
  url: https://aws.amazon.com/premiumsupport/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.aws.amazon.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://aws.amazon.com/service-terms/
- group: operate
  title: ''
  type: ChangeLog
  url: https://aws.amazon.com/releasenotes/
- group: commercial
  title: ''
  type: Pricing
  url: https://aws.amazon.com/cloudwatch/pricing/
- group: start
  title: ''
  type: Console
  url: https://console.aws.amazon.com/cloudwatch/
- group: build
  title: ''
  type: SDKs
  url: https://aws.amazon.com/tools/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.aws.amazon.com/cloudwatch/
- group: docs
  title: ''
  type: OpenAPI
  url: openapi/_original/cloudwatch-openapi.yml
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/cloudwatch-alarm-schema.json
- group: design
  title: ''
  type: JSONLD
  url: json-ld/cloudwatch-context.jsonld
- group: design
  title: ''
  type: SpectralRules
  url: rules/cloudwatch-spectral-rules.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/cloudwatch-vocabulary.yaml
created: '2024-01-15'
description: Amazon CloudWatch is a monitoring and observability service that provides data and actionable insights for AWS, hybrid, and on-premises applications and infrastructure resources.
examples:
- key_count: 6
  name: Cloudwatch Alarm History Item Example
  slug: cloudwatch-alarm-history-item-example
- key_count: 2
  name: Cloudwatch Anomaly Detector Configuration Example
  slug: cloudwatch-anomaly-detector-configuration-example
- key_count: 5
  name: Cloudwatch Anomaly Detector Example
  slug: cloudwatch-anomaly-detector-example
- key_count: 0
  name: Cloudwatch Comparison Operator Example
  slug: cloudwatch-comparison-operator-example
- key_count: 18
  name: Cloudwatch Composite Alarm Example
  slug: cloudwatch-composite-alarm-example
- key_count: 1
  name: Cloudwatch Dashboard Body Example
  slug: cloudwatch-dashboard-body-example
- key_count: 4
  name: Cloudwatch Dashboard Entry Example
  slug: cloudwatch-dashboard-entry-example
- key_count: 2
  name: Cloudwatch Dashboard Validation Message Example
  slug: cloudwatch-dashboard-validation-message-example
- key_count: 6
  name: Cloudwatch Dashboard Widget Example
  slug: cloudwatch-dashboard-widget-example
- key_count: 7
  name: Cloudwatch Datapoint Example
  slug: cloudwatch-datapoint-example
- key_count: 1
  name: Cloudwatch Delete Alarms Input Example
  slug: cloudwatch-delete-alarms-input-example
- key_count: 4
  name: Cloudwatch Delete Anomaly Detector Input Example
  slug: cloudwatch-delete-anomaly-detector-input-example
- key_count: 1
  name: Cloudwatch Delete Dashboards Input Example
  slug: cloudwatch-delete-dashboards-input-example
- key_count: 6
  name: Cloudwatch Deletealarms Example
  slug: cloudwatch-deletealarms-example
- key_count: 6
  name: Cloudwatch Deleteanomalydetector Example
  slug: cloudwatch-deleteanomalydetector-example
- key_count: 6
  name: Cloudwatch Deletedashboards Example
  slug: cloudwatch-deletedashboards-example
- key_count: 8
  name: Cloudwatch Describe Alarm History Input Example
  slug: cloudwatch-describe-alarm-history-input-example
- key_count: 2
  name: Cloudwatch Describe Alarm History Output Example
  slug: cloudwatch-describe-alarm-history-output-example
- key_count: 5
  name: Cloudwatch Describe Alarms For Metric Input Example
  slug: cloudwatch-describe-alarms-for-metric-input-example
- key_count: 1
  name: Cloudwatch Describe Alarms For Metric Output Example
  slug: cloudwatch-describe-alarms-for-metric-output-example
- key_count: 8
  name: Cloudwatch Describe Alarms Input Example
  slug: cloudwatch-describe-alarms-input-example
- key_count: 3
  name: Cloudwatch Describe Alarms Output Example
  slug: cloudwatch-describe-alarms-output-example
- key_count: 6
  name: Cloudwatch Describe Anomaly Detectors Input Example
  slug: cloudwatch-describe-anomaly-detectors-input-example
- key_count: 2
  name: Cloudwatch Describe Anomaly Detectors Output Example
  slug: cloudwatch-describe-anomaly-detectors-output-example
- key_count: 6
  name: Cloudwatch Describealarmhistory Example
  slug: cloudwatch-describealarmhistory-example
- key_count: 6
  name: Cloudwatch Describealarms Example
  slug: cloudwatch-describealarms-example
- key_count: 6
  name: Cloudwatch Describealarmsformetric Example
  slug: cloudwatch-describealarmsformetric-example
- key_count: 6
  name: Cloudwatch Describeanomalydetectors Example
  slug: cloudwatch-describeanomalydetectors-example
- key_count: 2
  name: Cloudwatch Dimension Example
  slug: cloudwatch-dimension-example
- key_count: 2
  name: Cloudwatch Dimension Filter Example
  slug: cloudwatch-dimension-filter-example
- key_count: 1
  name: Cloudwatch Disable Alarm Actions Input Example
  slug: cloudwatch-disable-alarm-actions-input-example
- key_count: 6
  name: Cloudwatch Disablealarmactions Example
  slug: cloudwatch-disablealarmactions-example
- key_count: 1
  name: Cloudwatch Enable Alarm Actions Input Example
  slug: cloudwatch-enable-alarm-actions-input-example
- key_count: 6
  name: Cloudwatch Enablealarmactions Example
  slug: cloudwatch-enablealarmactions-example
- key_count: 2
  name: Cloudwatch Error Response Example
  slug: cloudwatch-error-response-example
- key_count: 1
  name: Cloudwatch Get Dashboard Input Example
  slug: cloudwatch-get-dashboard-input-example
- key_count: 3
  name: Cloudwatch Get Dashboard Output Example
  slug: cloudwatch-get-dashboard-output-example
- key_count: 7
  name: Cloudwatch Get Metric Data Input Example
  slug: cloudwatch-get-metric-data-input-example
- key_count: 3
  name: Cloudwatch Get Metric Data Output Example
  slug: cloudwatch-get-metric-data-output-example
- key_count: 8
  name: Cloudwatch Get Metric Statistics Input Example
  slug: cloudwatch-get-metric-statistics-input-example
- key_count: 2
  name: Cloudwatch Get Metric Statistics Output Example
  slug: cloudwatch-get-metric-statistics-output-example
- key_count: 6
  name: Cloudwatch Getdashboard Example
  slug: cloudwatch-getdashboard-example
- key_count: 6
  name: Cloudwatch Getmetricdata Example
  slug: cloudwatch-getmetricdata-example
- key_count: 6
  name: Cloudwatch Getmetricstatistics Example
  slug: cloudwatch-getmetricstatistics-example
- key_count: 2
  name: Cloudwatch List Dashboards Input Example
  slug: cloudwatch-list-dashboards-input-example
- key_count: 2
  name: Cloudwatch List Dashboards Output Example
  slug: cloudwatch-list-dashboards-output-example
- key_count: 2
  name: Cloudwatch List Metric Streams Input Example
  slug: cloudwatch-list-metric-streams-input-example
- key_count: 2
  name: Cloudwatch List Metric Streams Output Example
  slug: cloudwatch-list-metric-streams-output-example
- key_count: 7
  name: Cloudwatch List Metrics Input Example
  slug: cloudwatch-list-metrics-input-example
- key_count: 3
  name: Cloudwatch List Metrics Output Example
  slug: cloudwatch-list-metrics-output-example
- key_count: 1
  name: Cloudwatch List Tags For Resource Input Example
  slug: cloudwatch-list-tags-for-resource-input-example
- key_count: 1
  name: Cloudwatch List Tags For Resource Output Example
  slug: cloudwatch-list-tags-for-resource-output-example
- key_count: 6
  name: Cloudwatch Listdashboards Example
  slug: cloudwatch-listdashboards-example
- key_count: 6
  name: Cloudwatch Listmetrics Example
  slug: cloudwatch-listmetrics-example
- key_count: 6
  name: Cloudwatch Listmetricstreams Example
  slug: cloudwatch-listmetricstreams-example
- key_count: 6
  name: Cloudwatch Listtagsforresource Example
  slug: cloudwatch-listtagsforresource-example
- key_count: 2
  name: Cloudwatch Message Data Example
  slug: cloudwatch-message-data-example
- key_count: 24
  name: Cloudwatch Metric Alarm Example
  slug: cloudwatch-metric-alarm-example
- key_count: 1
  name: Cloudwatch Metric Characteristics Example
  slug: cloudwatch-metric-characteristics-example
- key_count: 6
  name: Cloudwatch Metric Data Query Example
  slug: cloudwatch-metric-data-query-example
- key_count: 6
  name: Cloudwatch Metric Data Result Example
  slug: cloudwatch-metric-data-result-example
- key_count: 7
  name: Cloudwatch Metric Datum Example
  slug: cloudwatch-metric-datum-example
- key_count: 3
  name: Cloudwatch Metric Example
  slug: cloudwatch-metric-example
- key_count: 1
  name: Cloudwatch Metric Math Anomaly Detector Example
  slug: cloudwatch-metric-math-anomaly-detector-example
- key_count: 2
  name: Cloudwatch Metric Stat Example
  slug: cloudwatch-metric-stat-example
- key_count: 7
  name: Cloudwatch Metric Stream Entry Example
  slug: cloudwatch-metric-stream-entry-example
- key_count: 2
  name: Cloudwatch Metric Stream Filter Example
  slug: cloudwatch-metric-stream-filter-example
- key_count: 4
  name: Cloudwatch Put Anomaly Detector Input Example
  slug: cloudwatch-put-anomaly-detector-input-example
- key_count: 11
  name: Cloudwatch Put Composite Alarm Input Example
  slug: cloudwatch-put-composite-alarm-input-example
- key_count: 2
  name: Cloudwatch Put Dashboard Input Example
  slug: cloudwatch-put-dashboard-input-example
- key_count: 1
  name: Cloudwatch Put Dashboard Output Example
  slug: cloudwatch-put-dashboard-output-example
- key_count: 19
  name: Cloudwatch Put Metric Alarm Input Example
  slug: cloudwatch-put-metric-alarm-input-example
- key_count: 2
  name: Cloudwatch Put Metric Data Input Example
  slug: cloudwatch-put-metric-data-input-example
- key_count: 8
  name: Cloudwatch Put Metric Stream Input Example
  slug: cloudwatch-put-metric-stream-input-example
- key_count: 1
  name: Cloudwatch Put Metric Stream Output Example
  slug: cloudwatch-put-metric-stream-output-example
- key_count: 6
  name: Cloudwatch Putanomalydetector Example
  slug: cloudwatch-putanomalydetector-example
- key_count: 6
  name: Cloudwatch Putcompositealarm Example
  slug: cloudwatch-putcompositealarm-example
- key_count: 6
  name: Cloudwatch Putdashboard Example
  slug: cloudwatch-putdashboard-example
- key_count: 6
  name: Cloudwatch Putmetricalarm Example
  slug: cloudwatch-putmetricalarm-example
- key_count: 6
  name: Cloudwatch Putmetricdata Example
  slug: cloudwatch-putmetricdata-example
- key_count: 6
  name: Cloudwatch Putmetricstream Example
  slug: cloudwatch-putmetricstream-example
- key_count: 2
  name: Cloudwatch Range Example
  slug: cloudwatch-range-example
- key_count: 3
  name: Cloudwatch Set Alarm State Input Example
  slug: cloudwatch-set-alarm-state-input-example
- key_count: 6
  name: Cloudwatch Setalarmstate Example
  slug: cloudwatch-setalarmstate-example
- key_count: 5
  name: Cloudwatch Single Metric Anomaly Detector Example
  slug: cloudwatch-single-metric-anomaly-detector-example
- key_count: 0
  name: Cloudwatch Standard Unit Example
  slug: cloudwatch-standard-unit-example
- key_count: 0
  name: Cloudwatch State Value Example
  slug: cloudwatch-state-value-example
- key_count: 0
  name: Cloudwatch Statistic Example
  slug: cloudwatch-statistic-example
- key_count: 4
  name: Cloudwatch Statistic Set Example
  slug: cloudwatch-statistic-set-example
- key_count: 2
  name: Cloudwatch Tag Example
  slug: cloudwatch-tag-example
- key_count: 2
  name: Cloudwatch Tag Resource Input Example
  slug: cloudwatch-tag-resource-input-example
- key_count: 6
  name: Cloudwatch Tagresource Example
  slug: cloudwatch-tagresource-example
- key_count: 2
  name: Cloudwatch Untag Resource Input Example
  slug: cloudwatch-untag-resource-input-example
- key_count: 6
  name: Cloudwatch Untagresource Example
  slug: cloudwatch-untagresource-example
features:
- Unified monitoring across AWS resources with automatic dashboards
- Metric collection and custom metrics publishing
- CloudWatch Alarms with composite alarm support and anomaly detection
- CloudWatch Logs Insights for interactive log analytics
- Synthetics canaries for endpoint and API monitoring
- Real User Monitoring (RUM) for client-side performance
- Internet Monitor for availability and latency tracking
- Application Signals for automatic service instrumentation and SLOs
- Cross-account observability with Observability Access Manager
- Network Monitor for hybrid connectivity health
finops:
- name: Cloudwatch Finops
  service_category: Observability
  slug: cloudwatch-finops
image: https://a0.awsstatic.com/libra-css/images/logos/aws_logo_smile_1200x630.png
json_schemas:
- name: AlarmHistoryItem
  property_count: 6
  slug: cloudwatch-alarm-history-item
- name: Amazon CloudWatch Alarm
  property_count: 29
  slug: cloudwatch-alarm
- name: AlarmHistoryItem
  property_count: 6
  slug: cloudwatch-alarmhistoryitem
- name: AnomalyDetectorConfiguration
  property_count: 2
  slug: cloudwatch-anomaly-detector-configuration
- name: AnomalyDetector
  property_count: 5
  slug: cloudwatch-anomaly-detector
- name: AnomalyDetector
  property_count: 9
  slug: cloudwatch-anomalydetector
- name: AnomalyDetectorConfiguration
  property_count: 2
  slug: cloudwatch-anomalydetectorconfiguration
- name: ComparisonOperator
  property_count: 0
  slug: cloudwatch-comparison-operator
- name: ComparisonOperator
  property_count: 0
  slug: cloudwatch-comparisonoperator
- name: CompositeAlarm
  property_count: 18
  slug: cloudwatch-composite-alarm
- name: CompositeAlarm
  property_count: 19
  slug: cloudwatch-compositealarm
- name: DashboardBody
  property_count: 1
  slug: cloudwatch-dashboard-body
- name: DashboardEntry
  property_count: 4
  slug: cloudwatch-dashboard-entry
- name: DashboardValidationMessage
  property_count: 2
  slug: cloudwatch-dashboard-validation-message
- name: DashboardWidget
  property_count: 6
  slug: cloudwatch-dashboard-widget
- name: DashboardBody
  property_count: 1
  slug: cloudwatch-dashboardbody
- name: DashboardEntry
  property_count: 4
  slug: cloudwatch-dashboardentry
- name: DashboardValidationMessage
  property_count: 2
  slug: cloudwatch-dashboardvalidationmessage
- name: DashboardWidget
  property_count: 6
  slug: cloudwatch-dashboardwidget
- name: Datapoint
  property_count: 7
  slug: cloudwatch-datapoint
- name: DeleteAlarmsInput
  property_count: 1
  slug: cloudwatch-delete-alarms-input
- name: DeleteAnomalyDetectorInput
  property_count: 4
  slug: cloudwatch-delete-anomaly-detector-input
- name: DeleteDashboardsInput
  property_count: 1
  slug: cloudwatch-delete-dashboards-input
- name: DeleteAlarmsInput
  property_count: 1
  slug: cloudwatch-deletealarmsinput
- name: DeleteAnomalyDetectorInput
  property_count: 6
  slug: cloudwatch-deleteanomalydetectorinput
- name: DeleteDashboardsInput
  property_count: 1
  slug: cloudwatch-deletedashboardsinput
- name: DescribeAlarmHistoryInput
  property_count: 8
  slug: cloudwatch-describe-alarm-history-input
- name: DescribeAlarmHistoryOutput
  property_count: 2
  slug: cloudwatch-describe-alarm-history-output
- name: DescribeAlarmsForMetricInput
  property_count: 5
  slug: cloudwatch-describe-alarms-for-metric-input
- name: DescribeAlarmsForMetricOutput
  property_count: 1
  slug: cloudwatch-describe-alarms-for-metric-output
- name: DescribeAlarmsInput
  property_count: 8
  slug: cloudwatch-describe-alarms-input
- name: DescribeAlarmsOutput
  property_count: 3
  slug: cloudwatch-describe-alarms-output
- name: DescribeAnomalyDetectorsInput
  property_count: 6
  slug: cloudwatch-describe-anomaly-detectors-input
- name: DescribeAnomalyDetectorsOutput
  property_count: 2
  slug: cloudwatch-describe-anomaly-detectors-output
- name: DescribeAlarmHistoryInput
  property_count: 8
  slug: cloudwatch-describealarmhistoryinput
- name: DescribeAlarmHistoryOutput
  property_count: 2
  slug: cloudwatch-describealarmhistoryoutput
- name: DescribeAlarmsForMetricInput
  property_count: 7
  slug: cloudwatch-describealarmsformetricinput
- name: DescribeAlarmsForMetricOutput
  property_count: 1
  slug: cloudwatch-describealarmsformetricoutput
- name: DescribeAlarmsInput
  property_count: 9
  slug: cloudwatch-describealarmsinput
- name: DescribeAlarmsOutput
  property_count: 3
  slug: cloudwatch-describealarmsoutput
- name: DescribeAnomalyDetectorsInput
  property_count: 6
  slug: cloudwatch-describeanomalydetectorsinput
- name: DescribeAnomalyDetectorsOutput
  property_count: 2
  slug: cloudwatch-describeanomalydetectorsoutput
- name: DimensionFilter
  property_count: 2
  slug: cloudwatch-dimension-filter
- name: Dimension
  property_count: 2
  slug: cloudwatch-dimension
- name: DimensionFilter
  property_count: 2
  slug: cloudwatch-dimensionfilter
- name: DisableAlarmActionsInput
  property_count: 1
  slug: cloudwatch-disable-alarm-actions-input
- name: DisableAlarmActionsInput
  property_count: 1
  slug: cloudwatch-disablealarmactionsinput
- name: EnableAlarmActionsInput
  property_count: 1
  slug: cloudwatch-enable-alarm-actions-input
- name: EnableAlarmActionsInput
  property_count: 1
  slug: cloudwatch-enablealarmactionsinput
- name: ErrorResponse
  property_count: 2
  slug: cloudwatch-error-response
- name: ErrorResponse
  property_count: 2
  slug: cloudwatch-errorresponse
- name: GetDashboardInput
  property_count: 1
  slug: cloudwatch-get-dashboard-input
- name: GetDashboardOutput
  property_count: 3
  slug: cloudwatch-get-dashboard-output
- name: GetMetricDataInput
  property_count: 7
  slug: cloudwatch-get-metric-data-input
- name: GetMetricDataOutput
  property_count: 3
  slug: cloudwatch-get-metric-data-output
- name: GetMetricStatisticsInput
  property_count: 8
  slug: cloudwatch-get-metric-statistics-input
- name: GetMetricStatisticsOutput
  property_count: 2
  slug: cloudwatch-get-metric-statistics-output
- name: GetDashboardInput
  property_count: 1
  slug: cloudwatch-getdashboardinput
- name: GetDashboardOutput
  property_count: 3
  slug: cloudwatch-getdashboardoutput
- name: GetMetricDataInput
  property_count: 7
  slug: cloudwatch-getmetricdatainput
- name: GetMetricDataOutput
  property_count: 3
  slug: cloudwatch-getmetricdataoutput
- name: GetMetricStatisticsInput
  property_count: 9
  slug: cloudwatch-getmetricstatisticsinput
- name: GetMetricStatisticsOutput
  property_count: 2
  slug: cloudwatch-getmetricstatisticsoutput
- name: ListDashboardsInput
  property_count: 2
  slug: cloudwatch-list-dashboards-input
- name: ListDashboardsOutput
  property_count: 2
  slug: cloudwatch-list-dashboards-output
- name: ListMetricStreamsInput
  property_count: 2
  slug: cloudwatch-list-metric-streams-input
- name: ListMetricStreamsOutput
  property_count: 2
  slug: cloudwatch-list-metric-streams-output
- name: ListMetricsInput
  property_count: 7
  slug: cloudwatch-list-metrics-input
- name: ListMetricsOutput
  property_count: 3
  slug: cloudwatch-list-metrics-output
- name: ListTagsForResourceInput
  property_count: 1
  slug: cloudwatch-list-tags-for-resource-input
- name: ListTagsForResourceOutput
  property_count: 1
  slug: cloudwatch-list-tags-for-resource-output
- name: ListDashboardsInput
  property_count: 2
  slug: cloudwatch-listdashboardsinput
- name: ListDashboardsOutput
  property_count: 2
  slug: cloudwatch-listdashboardsoutput
- name: ListMetricsInput
  property_count: 7
  slug: cloudwatch-listmetricsinput
- name: ListMetricsOutput
  property_count: 3
  slug: cloudwatch-listmetricsoutput
- name: ListMetricStreamsInput
  property_count: 2
  slug: cloudwatch-listmetricstreamsinput
- name: ListMetricStreamsOutput
  property_count: 2
  slug: cloudwatch-listmetricstreamsoutput
- name: ListTagsForResourceInput
  property_count: 1
  slug: cloudwatch-listtagsforresourceinput
- name: ListTagsForResourceOutput
  property_count: 1
  slug: cloudwatch-listtagsforresourceoutput
- name: MessageData
  property_count: 2
  slug: cloudwatch-message-data
- name: MessageData
  property_count: 2
  slug: cloudwatch-messagedata
- name: MetricAlarm
  property_count: 24
  slug: cloudwatch-metric-alarm
- name: MetricCharacteristics
  property_count: 1
  slug: cloudwatch-metric-characteristics
- name: MetricDataQuery
  property_count: 6
  slug: cloudwatch-metric-data-query
- name: MetricDataResult
  property_count: 6
  slug: cloudwatch-metric-data-result
- name: MetricDatum
  property_count: 7
  slug: cloudwatch-metric-datum
- name: MetricMathAnomalyDetector
  property_count: 1
  slug: cloudwatch-metric-math-anomaly-detector
- name: Metric
  property_count: 3
  slug: cloudwatch-metric
- name: MetricStat
  property_count: 2
  slug: cloudwatch-metric-stat
- name: MetricStreamEntry
  property_count: 7
  slug: cloudwatch-metric-stream-entry
- name: MetricStreamFilter
  property_count: 2
  slug: cloudwatch-metric-stream-filter
- name: MetricAlarm
  property_count: 28
  slug: cloudwatch-metricalarm
- name: MetricCharacteristics
  property_count: 1
  slug: cloudwatch-metriccharacteristics
- name: MetricDataQuery
  property_count: 7
  slug: cloudwatch-metricdataquery
- name: MetricDataResult
  property_count: 6
  slug: cloudwatch-metricdataresult
- name: MetricDatum
  property_count: 9
  slug: cloudwatch-metricdatum
- name: MetricMathAnomalyDetector
  property_count: 1
  slug: cloudwatch-metricmathanomalydetector
- name: MetricStat
  property_count: 4
  slug: cloudwatch-metricstat
- name: MetricStreamEntry
  property_count: 7
  slug: cloudwatch-metricstreamentry
- name: MetricStreamFilter
  property_count: 2
  slug: cloudwatch-metricstreamfilter
- name: PutAnomalyDetectorInput
  property_count: 4
  slug: cloudwatch-put-anomaly-detector-input
- name: PutCompositeAlarmInput
  property_count: 11
  slug: cloudwatch-put-composite-alarm-input
- name: PutDashboardInput
  property_count: 2
  slug: cloudwatch-put-dashboard-input
- name: PutDashboardOutput
  property_count: 1
  slug: cloudwatch-put-dashboard-output
- name: PutMetricAlarmInput
  property_count: 19
  slug: cloudwatch-put-metric-alarm-input
- name: PutMetricDataInput
  property_count: 2
  slug: cloudwatch-put-metric-data-input
- name: PutMetricStreamInput
  property_count: 8
  slug: cloudwatch-put-metric-stream-input
- name: PutMetricStreamOutput
  property_count: 1
  slug: cloudwatch-put-metric-stream-output
- name: PutAnomalyDetectorInput
  property_count: 8
  slug: cloudwatch-putanomalydetectorinput
- name: PutCompositeAlarmInput
  property_count: 11
  slug: cloudwatch-putcompositealarminput
- name: PutDashboardInput
  property_count: 2
  slug: cloudwatch-putdashboardinput
- name: PutDashboardOutput
  property_count: 1
  slug: cloudwatch-putdashboardoutput
- name: PutMetricAlarmInput
  property_count: 22
  slug: cloudwatch-putmetricalarminput
- name: PutMetricDataInput
  property_count: 2
  slug: cloudwatch-putmetricdatainput
- name: PutMetricStreamInput
  property_count: 8
  slug: cloudwatch-putmetricstreaminput
- name: PutMetricStreamOutput
  property_count: 1
  slug: cloudwatch-putmetricstreamoutput
- name: Range
  property_count: 2
  slug: cloudwatch-range
- name: SetAlarmStateInput
  property_count: 3
  slug: cloudwatch-set-alarm-state-input
- name: SetAlarmStateInput
  property_count: 4
  slug: cloudwatch-setalarmstateinput
- name: SingleMetricAnomalyDetector
  property_count: 5
  slug: cloudwatch-single-metric-anomaly-detector
- name: SingleMetricAnomalyDetector
  property_count: 5
  slug: cloudwatch-singlemetricanomalydetector
- name: StandardUnit
  property_count: 0
  slug: cloudwatch-standard-unit
- name: StandardUnit
  property_count: 0
  slug: cloudwatch-standardunit
- name: StateValue
  property_count: 0
  slug: cloudwatch-state-value
- name: StateValue
  property_count: 0
  slug: cloudwatch-statevalue
- name: Statistic
  property_count: 0
  slug: cloudwatch-statistic
- name: StatisticSet
  property_count: 4
  slug: cloudwatch-statistic-set
- name: StatisticSet
  property_count: 4
  slug: cloudwatch-statisticset
- name: TagResourceInput
  property_count: 2
  slug: cloudwatch-tag-resource-input
- name: Tag
  property_count: 2
  slug: cloudwatch-tag
- name: TagResourceInput
  property_count: 2
  slug: cloudwatch-tagresourceinput
- name: UntagResourceInput
  property_count: 2
  slug: cloudwatch-untag-resource-input
- name: UntagResourceInput
  property_count: 2
  slug: cloudwatch-untagresourceinput
json_structures:
- name: Cloudwatch Alarm History Item Structure
  property_count: 6
  slug: cloudwatch-alarm-history-item-structure
- name: Cloudwatch Anomaly Detector Configuration Structure
  property_count: 2
  slug: cloudwatch-anomaly-detector-configuration-structure
- name: Cloudwatch Anomaly Detector Structure
  property_count: 5
  slug: cloudwatch-anomaly-detector-structure
- name: Cloudwatch Comparison Operator Structure
  property_count: 0
  slug: cloudwatch-comparison-operator-structure
- name: Cloudwatch Composite Alarm Structure
  property_count: 18
  slug: cloudwatch-composite-alarm-structure
- name: Cloudwatch Dashboard Body Structure
  property_count: 1
  slug: cloudwatch-dashboard-body-structure
- name: Cloudwatch Dashboard Entry Structure
  property_count: 4
  slug: cloudwatch-dashboard-entry-structure
- name: Cloudwatch Dashboard Validation Message Structure
  property_count: 2
  slug: cloudwatch-dashboard-validation-message-structure
- name: Cloudwatch Dashboard Widget Structure
  property_count: 6
  slug: cloudwatch-dashboard-widget-structure
- name: Cloudwatch Datapoint Structure
  property_count: 7
  slug: cloudwatch-datapoint-structure
- name: Cloudwatch Delete Alarms Input Structure
  property_count: 1
  slug: cloudwatch-delete-alarms-input-structure
- name: Cloudwatch Delete Anomaly Detector Input Structure
  property_count: 4
  slug: cloudwatch-delete-anomaly-detector-input-structure
- name: Cloudwatch Delete Dashboards Input Structure
  property_count: 1
  slug: cloudwatch-delete-dashboards-input-structure
- name: Cloudwatch Describe Alarm History Input Structure
  property_count: 8
  slug: cloudwatch-describe-alarm-history-input-structure
- name: Cloudwatch Describe Alarm History Output Structure
  property_count: 2
  slug: cloudwatch-describe-alarm-history-output-structure
- name: Cloudwatch Describe Alarms For Metric Input Structure
  property_count: 5
  slug: cloudwatch-describe-alarms-for-metric-input-structure
- name: Cloudwatch Describe Alarms For Metric Output Structure
  property_count: 1
  slug: cloudwatch-describe-alarms-for-metric-output-structure
- name: Cloudwatch Describe Alarms Input Structure
  property_count: 8
  slug: cloudwatch-describe-alarms-input-structure
- name: Cloudwatch Describe Alarms Output Structure
  property_count: 3
  slug: cloudwatch-describe-alarms-output-structure
- name: Cloudwatch Describe Anomaly Detectors Input Structure
  property_count: 6
  slug: cloudwatch-describe-anomaly-detectors-input-structure
- name: Cloudwatch Describe Anomaly Detectors Output Structure
  property_count: 2
  slug: cloudwatch-describe-anomaly-detectors-output-structure
- name: Cloudwatch Dimension Filter Structure
  property_count: 2
  slug: cloudwatch-dimension-filter-structure
- name: Cloudwatch Dimension Structure
  property_count: 2
  slug: cloudwatch-dimension-structure
- name: Cloudwatch Disable Alarm Actions Input Structure
  property_count: 1
  slug: cloudwatch-disable-alarm-actions-input-structure
- name: Cloudwatch Enable Alarm Actions Input Structure
  property_count: 1
  slug: cloudwatch-enable-alarm-actions-input-structure
- name: Cloudwatch Error Response Structure
  property_count: 2
  slug: cloudwatch-error-response-structure
- name: Cloudwatch Get Dashboard Input Structure
  property_count: 1
  slug: cloudwatch-get-dashboard-input-structure
- name: Cloudwatch Get Dashboard Output Structure
  property_count: 3
  slug: cloudwatch-get-dashboard-output-structure
- name: Cloudwatch Get Metric Data Input Structure
  property_count: 7
  slug: cloudwatch-get-metric-data-input-structure
- name: Cloudwatch Get Metric Data Output Structure
  property_count: 3
  slug: cloudwatch-get-metric-data-output-structure
- name: Cloudwatch Get Metric Statistics Input Structure
  property_count: 8
  slug: cloudwatch-get-metric-statistics-input-structure
- name: Cloudwatch Get Metric Statistics Output Structure
  property_count: 2
  slug: cloudwatch-get-metric-statistics-output-structure
- name: Cloudwatch List Dashboards Input Structure
  property_count: 2
  slug: cloudwatch-list-dashboards-input-structure
- name: Cloudwatch List Dashboards Output Structure
  property_count: 2
  slug: cloudwatch-list-dashboards-output-structure
- name: Cloudwatch List Metric Streams Input Structure
  property_count: 2
  slug: cloudwatch-list-metric-streams-input-structure
- name: Cloudwatch List Metric Streams Output Structure
  property_count: 2
  slug: cloudwatch-list-metric-streams-output-structure
- name: Cloudwatch List Metrics Input Structure
  property_count: 7
  slug: cloudwatch-list-metrics-input-structure
- name: Cloudwatch List Metrics Output Structure
  property_count: 3
  slug: cloudwatch-list-metrics-output-structure
- name: Cloudwatch List Tags For Resource Input Structure
  property_count: 1
  slug: cloudwatch-list-tags-for-resource-input-structure
- name: Cloudwatch List Tags For Resource Output Structure
  property_count: 1
  slug: cloudwatch-list-tags-for-resource-output-structure
- name: Cloudwatch Message Data Structure
  property_count: 2
  slug: cloudwatch-message-data-structure
- name: Cloudwatch Metric Alarm Structure
  property_count: 24
  slug: cloudwatch-metric-alarm-structure
- name: Cloudwatch Metric Characteristics Structure
  property_count: 1
  slug: cloudwatch-metric-characteristics-structure
- name: Cloudwatch Metric Data Query Structure
  property_count: 6
  slug: cloudwatch-metric-data-query-structure
- name: Cloudwatch Metric Data Result Structure
  property_count: 6
  slug: cloudwatch-metric-data-result-structure
- name: Cloudwatch Metric Datum Structure
  property_count: 7
  slug: cloudwatch-metric-datum-structure
- name: Cloudwatch Metric Math Anomaly Detector Structure
  property_count: 1
  slug: cloudwatch-metric-math-anomaly-detector-structure
- name: Cloudwatch Metric Stat Structure
  property_count: 2
  slug: cloudwatch-metric-stat-structure
- name: Cloudwatch Metric Stream Entry Structure
  property_count: 7
  slug: cloudwatch-metric-stream-entry-structure
- name: Cloudwatch Metric Stream Filter Structure
  property_count: 2
  slug: cloudwatch-metric-stream-filter-structure
- name: Cloudwatch Metric Structure
  property_count: 3
  slug: cloudwatch-metric-structure
- name: Cloudwatch Put Anomaly Detector Input Structure
  property_count: 4
  slug: cloudwatch-put-anomaly-detector-input-structure
- name: Cloudwatch Put Composite Alarm Input Structure
  property_count: 11
  slug: cloudwatch-put-composite-alarm-input-structure
- name: Cloudwatch Put Dashboard Input Structure
  property_count: 2
  slug: cloudwatch-put-dashboard-input-structure
- name: Cloudwatch Put Dashboard Output Structure
  property_count: 1
  slug: cloudwatch-put-dashboard-output-structure
- name: Cloudwatch Put Metric Alarm Input Structure
  property_count: 19
  slug: cloudwatch-put-metric-alarm-input-structure
- name: Cloudwatch Put Metric Data Input Structure
  property_count: 2
  slug: cloudwatch-put-metric-data-input-structure
- name: Cloudwatch Put Metric Stream Input Structure
  property_count: 8
  slug: cloudwatch-put-metric-stream-input-structure
- name: Cloudwatch Put Metric Stream Output Structure
  property_count: 1
  slug: cloudwatch-put-metric-stream-output-structure
- name: Cloudwatch Range Structure
  property_count: 2
  slug: cloudwatch-range-structure
- name: Cloudwatch Set Alarm State Input Structure
  property_count: 3
  slug: cloudwatch-set-alarm-state-input-structure
- name: Cloudwatch Single Metric Anomaly Detector Structure
  property_count: 5
  slug: cloudwatch-single-metric-anomaly-detector-structure
- name: Cloudwatch Standard Unit Structure
  property_count: 0
  slug: cloudwatch-standard-unit-structure
- name: Cloudwatch State Value Structure
  property_count: 0
  slug: cloudwatch-state-value-structure
- name: Cloudwatch Statistic Set Structure
  property_count: 4
  slug: cloudwatch-statistic-set-structure
- name: Cloudwatch Statistic Structure
  property_count: 0
  slug: cloudwatch-statistic-structure
- name: Cloudwatch Structure
  property_count: 0
  slug: cloudwatch-structure
- name: Cloudwatch Tag Resource Input Structure
  property_count: 2
  slug: cloudwatch-tag-resource-input-structure
- name: Cloudwatch Tag Structure
  property_count: 2
  slug: cloudwatch-tag-structure
- name: Cloudwatch Untag Resource Input Structure
  property_count: 2
  slug: cloudwatch-untag-resource-input-structure
jsonld:
- class_count: 0
  name: Cloudwatch Context
  property_count: 0
  slug: cloudwatch-context
layout: provider
modified: '2026-05-19'
name: AWS CloudWatch
nav: Providers
network: true
overview: 'AWS CloudWatch publishes 6 APIs on the [APIs.io](https://apis.io/) network, including Alarms API, Anomaly Detection API, Composite Alarms API, and 3 more. Tagged areas include Alarms, Aws, Dashboards, Logs, and Metrics.


  The AWS CloudWatch catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  AWS CloudWatch''s developer surface includes authentication, engineering blog, FAQ, support, changelog, pricing, developer console, and 14 more developer resources.'
plans:
- name: Cloudwatch Plans Pricing
  plan_count: 7
  slug: cloudwatch-plans-pricing
random_paper: 26
rate_limits:
- limit_count: 10
  name: Cloudwatch Rate Limits
  slug: cloudwatch-rate-limits
rules:
- name: AWS CloudWatch API Rules
  rule_count: 6
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 5
  slug: cloudwatch-jsonschema-spectral-rules
- name: AWS CloudWatch API Rules
  rule_count: 15
  severity_counts:
    error: 8
    hint: 0
    info: 0
    warn: 7
  slug: cloudwatch-spectral-rules
score:
  band: strong
  composite: 56.7
  delta: -8.6
  facets:
    commercial_clarity: 44.7
    contract_quality: 76.9
    developer_ergonomics: 43.5
    discoverability: 64.8
    governance: 68.8
    operational_transparency: 39.5
  previous_composite: 65.3
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 6
  schema_version: 0.11.0
  scored_at: '2026-08-11'
  trend: falling
screenshot: https://raw.githubusercontent.com/api-evangelist/cloudwatch/refs/heads/main/screenshots/cloudwatch-2026-06-20T174619.png
security:
- kind: authentication
  name: Cloudwatch Authentication
  slug: cloudwatch-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Cloudwatch Domain Security
  slug: cloudwatch-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Cloudwatch Vulnerability Disclosure
  slug: cloudwatch-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Cloudwatch Trust Center
  slug: cloudwatch-trust-center
  summary_line: PCI DSS, HIPAA, FedRAMP, GDPR, FIPS 140
slug: cloudwatch
tags:
- Alarms
- Aws
- Dashboards
- Logs
- Metrics
- Monitoring
- Observability
use_cases:
- Monitoring application health and setting automated alarms
- Centralized log aggregation and analysis across AWS services
- Tracking end-user experience with real user monitoring
- Proactively detecting API and endpoint issues with synthetic monitoring
- Managing SLOs across microservices architectures
- Monitoring network performance for Direct Connect and VPN
- Cross-account observability for multi-account AWS organizations
- Anomaly detection on metrics to identify unexpected behavior
---
