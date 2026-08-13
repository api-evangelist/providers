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
    agent_skills: false
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: derived
    openapi_examples: verified
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 43.7
  scored_at: '2026-08-12'
agentic_access:
- acting_count: 13
  human_in_the_loop: 0
  name: Amazon Codeguru Profiler Agentic Access
  operation_count: 23
  slug: amazon-codeguru-profiler-agentic-access
  summary_line: 23 operations · 13 acting
api_count: 4
apis:
- description: The Internal API from Amazon CodeGuru Profiler — 4 operation(s) for internal.
  name: Amazon CodeGuru Profiler Internal API
  slug: amazon-codeguru-profiler-internal-api
- description: The ProfilingGroups API from Amazon CodeGuru Profiler — 12 operation(s) for profilinggroups.
  name: Amazon CodeGuru Profiler ProfilingGroups API
  slug: amazon-codeguru-profiler-profilinggroups-api
- description: The ProfilingGroups#clientToken API from Amazon CodeGuru Profiler — 1 operation(s) for profilinggroups#clienttoken.
  name: Amazon CodeGuru Profiler ProfilingGroups#clientToken API
  slug: amazon-codeguru-profiler-profilinggroups-clienttoken-api
- description: The Tags API from Amazon CodeGuru Profiler — 2 operation(s) for tags.
  name: Amazon CodeGuru Profiler Tags API
  slug: amazon-codeguru-profiler-tags-api
artifact_total: 325
common:
- group: agent
  title: ''
  type: MCPServer
  url: mcp/amazon-codeguru-profiler-mcp.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/amazon-codeguru-profiler-openapi-original-overlay.yaml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/amazon-codeguru-profiler-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/amazon-codeguru-profiler-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/amazon-codeguru-profiler-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/amazon-codeguru-profiler-authentication.yml
- group: company
  title: ''
  type: Blog
  url: https://aws.amazon.com/blogs/devops/tag/codeguru-profiler/feed/
created: '2026-03-16'
description: Amazon CodeGuru Profiler collects runtime performance data from your live applications, providing recommendations to help you reduce CPU utilization, cut costs, and improve application performance. The profiler analyzes your application's CPU and heap usage to identify the most expensive lines of code and offers actionable recommendations.
examples:
- key_count: 1
  name: Amazon Codeguru Profiler Add Notification Channels Request Example
  slug: amazon-codeguru-profiler-add-notification-channels-request-example
- key_count: 1
  name: Amazon Codeguru Profiler Add Notification Channels Response Example
  slug: amazon-codeguru-profiler-add-notification-channels-response-example
- key_count: 3
  name: Amazon Codeguru Profiler Agent Configuration Example
  slug: amazon-codeguru-profiler-agent-configuration-example
- key_count: 1
  name: Amazon Codeguru Profiler Agent Orchestration Config Example
  slug: amazon-codeguru-profiler-agent-orchestration-config-example
- key_count: 0
  name: Amazon Codeguru Profiler Agent Parameters Example
  slug: amazon-codeguru-profiler-agent-parameters-example
- key_count: 2
  name: Amazon Codeguru Profiler Aggregated Profile Time Example
  slug: amazon-codeguru-profiler-aggregated-profile-time-example
- key_count: 3
  name: Amazon Codeguru Profiler Anomaly Example
  slug: amazon-codeguru-profiler-anomaly-example
- key_count: 4
  name: Amazon Codeguru Profiler Anomaly Instance Example
  slug: amazon-codeguru-profiler-anomaly-instance-example
- key_count: 1
  name: Amazon Codeguru Profiler Batch Get Frame Metric Data Request Example
  slug: amazon-codeguru-profiler-batch-get-frame-metric-data-request-example
- key_count: 6
  name: Amazon Codeguru Profiler Batch Get Frame Metric Data Response Example
  slug: amazon-codeguru-profiler-batch-get-frame-metric-data-response-example
- key_count: 3
  name: Amazon Codeguru Profiler Channel Example
  slug: amazon-codeguru-profiler-channel-example
- key_count: 2
  name: Amazon Codeguru Profiler Configure Agent Request Example
  slug: amazon-codeguru-profiler-configure-agent-request-example
- key_count: 1
  name: Amazon Codeguru Profiler Configure Agent Response Example
  slug: amazon-codeguru-profiler-configure-agent-response-example
- key_count: 4
  name: Amazon Codeguru Profiler Create Profiling Group Request Example
  slug: amazon-codeguru-profiler-create-profiling-group-request-example
- key_count: 1
  name: Amazon Codeguru Profiler Create Profiling Group Response Example
  slug: amazon-codeguru-profiler-create-profiling-group-response-example
- key_count: 0
  name: Amazon Codeguru Profiler Delete Profiling Group Request Example
  slug: amazon-codeguru-profiler-delete-profiling-group-request-example
- key_count: 0
  name: Amazon Codeguru Profiler Delete Profiling Group Response Example
  slug: amazon-codeguru-profiler-delete-profiling-group-response-example
- key_count: 0
  name: Amazon Codeguru Profiler Describe Profiling Group Request Example
  slug: amazon-codeguru-profiler-describe-profiling-group-request-example
- key_count: 1
  name: Amazon Codeguru Profiler Describe Profiling Group Response Example
  slug: amazon-codeguru-profiler-describe-profiling-group-response-example
- key_count: 5
  name: Amazon Codeguru Profiler Findings Report Summary Example
  slug: amazon-codeguru-profiler-findings-report-summary-example
- key_count: 2
  name: Amazon Codeguru Profiler Frame Metric Datum Example
  slug: amazon-codeguru-profiler-frame-metric-datum-example
- key_count: 3
  name: Amazon Codeguru Profiler Frame Metric Example
  slug: amazon-codeguru-profiler-frame-metric-example
- key_count: 0
  name: Amazon Codeguru Profiler Get Findings Report Account Summary Request Example
  slug: amazon-codeguru-profiler-get-findings-report-account-summary-request-example
- key_count: 2
  name: Amazon Codeguru Profiler Get Findings Report Account Summary Response Example
  slug: amazon-codeguru-profiler-get-findings-report-account-summary-response-example
- key_count: 0
  name: Amazon Codeguru Profiler Get Notification Configuration Request Example
  slug: amazon-codeguru-profiler-get-notification-configuration-request-example
- key_count: 1
  name: Amazon Codeguru Profiler Get Notification Configuration Response Example
  slug: amazon-codeguru-profiler-get-notification-configuration-response-example
- key_count: 0
  name: Amazon Codeguru Profiler Get Policy Request Example
  slug: amazon-codeguru-profiler-get-policy-request-example
- key_count: 2
  name: Amazon Codeguru Profiler Get Policy Response Example
  slug: amazon-codeguru-profiler-get-policy-response-example
- key_count: 0
  name: Amazon Codeguru Profiler Get Profile Request Example
  slug: amazon-codeguru-profiler-get-profile-request-example
- key_count: 1
  name: Amazon Codeguru Profiler Get Profile Response Example
  slug: amazon-codeguru-profiler-get-profile-response-example
- key_count: 0
  name: Amazon Codeguru Profiler Get Recommendations Request Example
  slug: amazon-codeguru-profiler-get-recommendations-request-example
- key_count: 5
  name: Amazon Codeguru Profiler Get Recommendations Response Example
  slug: amazon-codeguru-profiler-get-recommendations-response-example
- key_count: 0
  name: Amazon Codeguru Profiler List Findings Reports Request Example
  slug: amazon-codeguru-profiler-list-findings-reports-request-example
- key_count: 2
  name: Amazon Codeguru Profiler List Findings Reports Response Example
  slug: amazon-codeguru-profiler-list-findings-reports-response-example
- key_count: 0
  name: Amazon Codeguru Profiler List Profile Times Request Example
  slug: amazon-codeguru-profiler-list-profile-times-request-example
- key_count: 2
  name: Amazon Codeguru Profiler List Profile Times Response Example
  slug: amazon-codeguru-profiler-list-profile-times-response-example
- key_count: 0
  name: Amazon Codeguru Profiler List Profiling Groups Request Example
  slug: amazon-codeguru-profiler-list-profiling-groups-request-example
- key_count: 3
  name: Amazon Codeguru Profiler List Profiling Groups Response Example
  slug: amazon-codeguru-profiler-list-profiling-groups-response-example
- key_count: 0
  name: Amazon Codeguru Profiler List Tags For Resource Request Example
  slug: amazon-codeguru-profiler-list-tags-for-resource-request-example
- key_count: 1
  name: Amazon Codeguru Profiler List Tags For Resource Response Example
  slug: amazon-codeguru-profiler-list-tags-for-resource-response-example
- key_count: 3
  name: Amazon Codeguru Profiler Match Example
  slug: amazon-codeguru-profiler-match-example
- key_count: 0
  name: Amazon Codeguru Profiler Metadata Example
  slug: amazon-codeguru-profiler-metadata-example
- key_count: 3
  name: Amazon Codeguru Profiler Metric Example
  slug: amazon-codeguru-profiler-metric-example
- key_count: 1
  name: Amazon Codeguru Profiler Notification Configuration Example
  slug: amazon-codeguru-profiler-notification-configuration-example
- key_count: 7
  name: Amazon Codeguru Profiler Pattern Example
  slug: amazon-codeguru-profiler-pattern-example
- key_count: 1
  name: Amazon Codeguru Profiler Post Agent Profile Request Example
  slug: amazon-codeguru-profiler-post-agent-profile-request-example
- key_count: 0
  name: Amazon Codeguru Profiler Post Agent Profile Response Example
  slug: amazon-codeguru-profiler-post-agent-profile-response-example
- key_count: 1
  name: Amazon Codeguru Profiler Profile Time Example
  slug: amazon-codeguru-profiler-profile-time-example
- key_count: 8
  name: Amazon Codeguru Profiler Profiling Group Description Example
  slug: amazon-codeguru-profiler-profiling-group-description-example
- key_count: 3
  name: Amazon Codeguru Profiler Profiling Status Example
  slug: amazon-codeguru-profiler-profiling-status-example
- key_count: 2
  name: Amazon Codeguru Profiler Put Permission Request Example
  slug: amazon-codeguru-profiler-put-permission-request-example
- key_count: 2
  name: Amazon Codeguru Profiler Put Permission Response Example
  slug: amazon-codeguru-profiler-put-permission-response-example
- key_count: 6
  name: Amazon Codeguru Profiler Recommendation Example
  slug: amazon-codeguru-profiler-recommendation-example
- key_count: 0
  name: Amazon Codeguru Profiler Remove Notification Channel Request Example
  slug: amazon-codeguru-profiler-remove-notification-channel-request-example
- key_count: 1
  name: Amazon Codeguru Profiler Remove Notification Channel Response Example
  slug: amazon-codeguru-profiler-remove-notification-channel-response-example
- key_count: 0
  name: Amazon Codeguru Profiler Remove Permission Request Example
  slug: amazon-codeguru-profiler-remove-permission-request-example
- key_count: 2
  name: Amazon Codeguru Profiler Remove Permission Response Example
  slug: amazon-codeguru-profiler-remove-permission-response-example
- key_count: 2
  name: Amazon Codeguru Profiler Submit Feedback Request Example
  slug: amazon-codeguru-profiler-submit-feedback-request-example
- key_count: 0
  name: Amazon Codeguru Profiler Submit Feedback Response Example
  slug: amazon-codeguru-profiler-submit-feedback-response-example
- key_count: 1
  name: Amazon Codeguru Profiler Tag Resource Request Example
  slug: amazon-codeguru-profiler-tag-resource-request-example
- key_count: 0
  name: Amazon Codeguru Profiler Tag Resource Response Example
  slug: amazon-codeguru-profiler-tag-resource-response-example
- key_count: 0
  name: Amazon Codeguru Profiler Tags Map Example
  slug: amazon-codeguru-profiler-tags-map-example
- key_count: 1
  name: Amazon Codeguru Profiler Timestamp Structure Example
  slug: amazon-codeguru-profiler-timestamp-structure-example
- key_count: 0
  name: Amazon Codeguru Profiler Unprocessed End Time Map Example
  slug: amazon-codeguru-profiler-unprocessed-end-time-map-example
- key_count: 0
  name: Amazon Codeguru Profiler Untag Resource Request Example
  slug: amazon-codeguru-profiler-untag-resource-request-example
- key_count: 0
  name: Amazon Codeguru Profiler Untag Resource Response Example
  slug: amazon-codeguru-profiler-untag-resource-response-example
- key_count: 1
  name: Amazon Codeguru Profiler Update Profiling Group Request Example
  slug: amazon-codeguru-profiler-update-profiling-group-request-example
- key_count: 1
  name: Amazon Codeguru Profiler Update Profiling Group Response Example
  slug: amazon-codeguru-profiler-update-profiling-group-response-example
- key_count: 1
  name: Amazon Codeguru Profiler User Feedback Example
  slug: amazon-codeguru-profiler-user-feedback-example
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/amazon-codeguru-profiler.png
json_schemas:
- name: ActionGroup
  property_count: 0
  slug: amazon-codeguru-profiler-action-group
- name: AddNotificationChannelsRequest
  property_count: 1
  slug: amazon-codeguru-profiler-add-notification-channels-request
- name: AddNotificationChannelsResponse
  property_count: 1
  slug: amazon-codeguru-profiler-add-notification-channels-response
- name: AgentConfiguration
  property_count: 3
  slug: amazon-codeguru-profiler-agent-configuration
- name: AgentOrchestrationConfig
  property_count: 1
  slug: amazon-codeguru-profiler-agent-orchestration-config
- name: AgentParameterField
  property_count: 0
  slug: amazon-codeguru-profiler-agent-parameter-field
- name: AgentParameters
  property_count: 0
  slug: amazon-codeguru-profiler-agent-parameters
- name: AgentProfile
  property_count: 0
  slug: amazon-codeguru-profiler-agent-profile
- name: AggregatedProfile
  property_count: 0
  slug: amazon-codeguru-profiler-aggregated-profile
- name: AggregatedProfileTime
  property_count: 2
  slug: amazon-codeguru-profiler-aggregated-profile-time
- name: AggregationPeriod
  property_count: 0
  slug: amazon-codeguru-profiler-aggregation-period
- name: Anomalies
  property_count: 0
  slug: amazon-codeguru-profiler-anomalies
- name: AnomalyInstanceId
  property_count: 0
  slug: amazon-codeguru-profiler-anomaly-instance-id
- name: AnomalyInstance
  property_count: 4
  slug: amazon-codeguru-profiler-anomaly-instance
- name: AnomalyInstances
  property_count: 0
  slug: amazon-codeguru-profiler-anomaly-instances
- name: Anomaly
  property_count: 3
  slug: amazon-codeguru-profiler-anomaly
- name: BatchGetFrameMetricDataRequest
  property_count: 1
  slug: amazon-codeguru-profiler-batch-get-frame-metric-data-request
- name: BatchGetFrameMetricDataResponse
  property_count: 6
  slug: amazon-codeguru-profiler-batch-get-frame-metric-data-response
- name: Boolean
  property_count: 0
  slug: amazon-codeguru-profiler-boolean
- name: ChannelId
  property_count: 0
  slug: amazon-codeguru-profiler-channel-id
- name: Channel
  property_count: 3
  slug: amazon-codeguru-profiler-channel
- name: ChannelUri
  property_count: 0
  slug: amazon-codeguru-profiler-channel-uri
- name: Channels
  property_count: 0
  slug: amazon-codeguru-profiler-channels
- name: ClientToken
  property_count: 0
  slug: amazon-codeguru-profiler-client-token
- name: ComputePlatform
  property_count: 0
  slug: amazon-codeguru-profiler-compute-platform
- name: ConfigureAgentRequest
  property_count: 2
  slug: amazon-codeguru-profiler-configure-agent-request
- name: ConfigureAgentResponse
  property_count: 1
  slug: amazon-codeguru-profiler-configure-agent-response
- name: CreateProfilingGroupRequest
  property_count: 4
  slug: amazon-codeguru-profiler-create-profiling-group-request
- name: CreateProfilingGroupResponse
  property_count: 1
  slug: amazon-codeguru-profiler-create-profiling-group-response
- name: DeleteProfilingGroupRequest
  property_count: 0
  slug: amazon-codeguru-profiler-delete-profiling-group-request
- name: DeleteProfilingGroupResponse
  property_count: 0
  slug: amazon-codeguru-profiler-delete-profiling-group-response
- name: DescribeProfilingGroupRequest
  property_count: 0
  slug: amazon-codeguru-profiler-describe-profiling-group-request
- name: DescribeProfilingGroupResponse
  property_count: 1
  slug: amazon-codeguru-profiler-describe-profiling-group-response
- name: Double
  property_count: 0
  slug: amazon-codeguru-profiler-double
- name: EventPublisher
  property_count: 0
  slug: amazon-codeguru-profiler-event-publisher
- name: EventPublishers
  property_count: 0
  slug: amazon-codeguru-profiler-event-publishers
- name: FeedbackType
  property_count: 0
  slug: amazon-codeguru-profiler-feedback-type
- name: FindingsReportId
  property_count: 0
  slug: amazon-codeguru-profiler-findings-report-id
- name: FindingsReportSummaries
  property_count: 0
  slug: amazon-codeguru-profiler-findings-report-summaries
- name: FindingsReportSummary
  property_count: 5
  slug: amazon-codeguru-profiler-findings-report-summary
- name: FleetInstanceId
  property_count: 0
  slug: amazon-codeguru-profiler-fleet-instance-id
- name: FrameMetricData
  property_count: 0
  slug: amazon-codeguru-profiler-frame-metric-data
- name: FrameMetricDatum
  property_count: 2
  slug: amazon-codeguru-profiler-frame-metric-datum
- name: FrameMetric
  property_count: 3
  slug: amazon-codeguru-profiler-frame-metric
- name: FrameMetricValue
  property_count: 0
  slug: amazon-codeguru-profiler-frame-metric-value
- name: FrameMetricValues
  property_count: 0
  slug: amazon-codeguru-profiler-frame-metric-values
- name: FrameMetrics
  property_count: 0
  slug: amazon-codeguru-profiler-frame-metrics
- name: GetFindingsReportAccountSummaryRequest
  property_count: 0
  slug: amazon-codeguru-profiler-get-findings-report-account-summary-request
- name: GetFindingsReportAccountSummaryResponse
  property_count: 2
  slug: amazon-codeguru-profiler-get-findings-report-account-summary-response
- name: GetNotificationConfigurationRequest
  property_count: 0
  slug: amazon-codeguru-profiler-get-notification-configuration-request
- name: GetNotificationConfigurationResponse
  property_count: 1
  slug: amazon-codeguru-profiler-get-notification-configuration-response
- name: GetPolicyRequest
  property_count: 0
  slug: amazon-codeguru-profiler-get-policy-request
- name: GetPolicyResponse
  property_count: 2
  slug: amazon-codeguru-profiler-get-policy-response
- name: GetProfileRequest
  property_count: 0
  slug: amazon-codeguru-profiler-get-profile-request
- name: GetProfileResponse
  property_count: 1
  slug: amazon-codeguru-profiler-get-profile-response
- name: GetRecommendationsRequest
  property_count: 0
  slug: amazon-codeguru-profiler-get-recommendations-request
- name: GetRecommendationsResponse
  property_count: 5
  slug: amazon-codeguru-profiler-get-recommendations-response
- name: Integer
  property_count: 0
  slug: amazon-codeguru-profiler-integer
- name: ListFindingsReportsRequest
  property_count: 0
  slug: amazon-codeguru-profiler-list-findings-reports-request
- name: ListFindingsReportsResponse
  property_count: 2
  slug: amazon-codeguru-profiler-list-findings-reports-response
- name: ListOfTimestamps
  property_count: 0
  slug: amazon-codeguru-profiler-list-of-timestamps
- name: ListProfileTimesRequest
  property_count: 0
  slug: amazon-codeguru-profiler-list-profile-times-request
- name: ListProfileTimesResponse
  property_count: 2
  slug: amazon-codeguru-profiler-list-profile-times-response
- name: ListProfilingGroupsRequest
  property_count: 0
  slug: amazon-codeguru-profiler-list-profiling-groups-request
- name: ListProfilingGroupsResponse
  property_count: 3
  slug: amazon-codeguru-profiler-list-profiling-groups-response
- name: ListTagsForResourceRequest
  property_count: 0
  slug: amazon-codeguru-profiler-list-tags-for-resource-request
- name: ListTagsForResourceResponse
  property_count: 1
  slug: amazon-codeguru-profiler-list-tags-for-resource-response
- name: Locale
  property_count: 0
  slug: amazon-codeguru-profiler-locale
- name: Match
  property_count: 3
  slug: amazon-codeguru-profiler-match
- name: Matches
  property_count: 0
  slug: amazon-codeguru-profiler-matches
- name: MaxDepth
  property_count: 0
  slug: amazon-codeguru-profiler-max-depth
- name: MaxResults
  property_count: 0
  slug: amazon-codeguru-profiler-max-results
- name: MetadataField
  property_count: 0
  slug: amazon-codeguru-profiler-metadata-field
- name: Metadata
  property_count: 0
  slug: amazon-codeguru-profiler-metadata
- name: Metric
  property_count: 3
  slug: amazon-codeguru-profiler-metric
- name: MetricType
  property_count: 0
  slug: amazon-codeguru-profiler-metric-type
- name: NotificationConfiguration
  property_count: 1
  slug: amazon-codeguru-profiler-notification-configuration
- name: OrderBy
  property_count: 0
  slug: amazon-codeguru-profiler-order-by
- name: PaginationToken
  property_count: 0
  slug: amazon-codeguru-profiler-pagination-token
- name: Pattern
  property_count: 7
  slug: amazon-codeguru-profiler-pattern
- name: Percentage
  property_count: 0
  slug: amazon-codeguru-profiler-percentage
- name: Period
  property_count: 0
  slug: amazon-codeguru-profiler-period
- name: PostAgentProfileRequest
  property_count: 1
  slug: amazon-codeguru-profiler-post-agent-profile-request
- name: PostAgentProfileResponse
  property_count: 0
  slug: amazon-codeguru-profiler-post-agent-profile-response
- name: Principal
  property_count: 0
  slug: amazon-codeguru-profiler-principal
- name: Principals
  property_count: 0
  slug: amazon-codeguru-profiler-principals
- name: ProfileTime
  property_count: 1
  slug: amazon-codeguru-profiler-profile-time
- name: ProfileTimes
  property_count: 0
  slug: amazon-codeguru-profiler-profile-times
- name: ProfilingGroupArn
  property_count: 0
  slug: amazon-codeguru-profiler-profiling-group-arn
- name: ProfilingGroupDescription
  property_count: 8
  slug: amazon-codeguru-profiler-profiling-group-description
- name: ProfilingGroupDescriptions
  property_count: 0
  slug: amazon-codeguru-profiler-profiling-group-descriptions
- name: ProfilingGroupName
  property_count: 0
  slug: amazon-codeguru-profiler-profiling-group-name
- name: ProfilingGroupNames
  property_count: 0
  slug: amazon-codeguru-profiler-profiling-group-names
- name: ProfilingStatus
  property_count: 3
  slug: amazon-codeguru-profiler-profiling-status
- name: PutPermissionRequest
  property_count: 2
  slug: amazon-codeguru-profiler-put-permission-request
- name: PutPermissionResponse
  property_count: 2
  slug: amazon-codeguru-profiler-put-permission-response
- name: Recommendation
  property_count: 6
  slug: amazon-codeguru-profiler-recommendation
- name: Recommendations
  property_count: 0
  slug: amazon-codeguru-profiler-recommendations
- name: RemoveNotificationChannelRequest
  property_count: 0
  slug: amazon-codeguru-profiler-remove-notification-channel-request
- name: RemoveNotificationChannelResponse
  property_count: 1
  slug: amazon-codeguru-profiler-remove-notification-channel-response
- name: RemovePermissionRequest
  property_count: 0
  slug: amazon-codeguru-profiler-remove-permission-request
- name: RemovePermissionResponse
  property_count: 2
  slug: amazon-codeguru-profiler-remove-permission-response
- name: RevisionId
  property_count: 0
  slug: amazon-codeguru-profiler-revision-id
- name: String
  property_count: 0
  slug: amazon-codeguru-profiler-string
- name: Strings
  property_count: 0
  slug: amazon-codeguru-profiler-strings
- name: SubmitFeedbackRequest
  property_count: 2
  slug: amazon-codeguru-profiler-submit-feedback-request
- name: SubmitFeedbackResponse
  property_count: 0
  slug: amazon-codeguru-profiler-submit-feedback-response
- name: TagKeys
  property_count: 0
  slug: amazon-codeguru-profiler-tag-keys
- name: TagResourceRequest
  property_count: 1
  slug: amazon-codeguru-profiler-tag-resource-request
- name: TagResourceResponse
  property_count: 0
  slug: amazon-codeguru-profiler-tag-resource-response
- name: TagsMap
  property_count: 0
  slug: amazon-codeguru-profiler-tags-map
- name: TargetFrame
  property_count: 0
  slug: amazon-codeguru-profiler-target-frame
- name: TargetFrames
  property_count: 0
  slug: amazon-codeguru-profiler-target-frames
- name: ThreadStates
  property_count: 0
  slug: amazon-codeguru-profiler-thread-states
- name: Timestamp
  property_count: 0
  slug: amazon-codeguru-profiler-timestamp
- name: TimestampStructure
  property_count: 1
  slug: amazon-codeguru-profiler-timestamp-structure
- name: UnprocessedEndTimeMap
  property_count: 0
  slug: amazon-codeguru-profiler-unprocessed-end-time-map
- name: UntagResourceRequest
  property_count: 0
  slug: amazon-codeguru-profiler-untag-resource-request
- name: UntagResourceResponse
  property_count: 0
  slug: amazon-codeguru-profiler-untag-resource-response
- name: UpdateProfilingGroupRequest
  property_count: 1
  slug: amazon-codeguru-profiler-update-profiling-group-request
- name: UpdateProfilingGroupResponse
  property_count: 1
  slug: amazon-codeguru-profiler-update-profiling-group-response
- name: UserFeedback
  property_count: 1
  slug: amazon-codeguru-profiler-user-feedback
json_structures:
- name: Amazon Codeguru Profiler Action Group Structure
  property_count: 0
  slug: amazon-codeguru-profiler-action-group-structure
- name: Amazon Codeguru Profiler Add Notification Channels Request Structure
  property_count: 1
  slug: amazon-codeguru-profiler-add-notification-channels-request-structure
- name: Amazon Codeguru Profiler Add Notification Channels Response Structure
  property_count: 1
  slug: amazon-codeguru-profiler-add-notification-channels-response-structure
- name: Amazon Codeguru Profiler Agent Configuration Structure
  property_count: 3
  slug: amazon-codeguru-profiler-agent-configuration-structure
- name: Amazon Codeguru Profiler Agent Orchestration Config Structure
  property_count: 1
  slug: amazon-codeguru-profiler-agent-orchestration-config-structure
- name: Amazon Codeguru Profiler Agent Parameter Field Structure
  property_count: 0
  slug: amazon-codeguru-profiler-agent-parameter-field-structure
- name: Amazon Codeguru Profiler Agent Parameters Structure
  property_count: 0
  slug: amazon-codeguru-profiler-agent-parameters-structure
- name: Amazon Codeguru Profiler Agent Profile Structure
  property_count: 0
  slug: amazon-codeguru-profiler-agent-profile-structure
- name: Amazon Codeguru Profiler Aggregated Profile Structure
  property_count: 0
  slug: amazon-codeguru-profiler-aggregated-profile-structure
- name: Amazon Codeguru Profiler Aggregated Profile Time Structure
  property_count: 2
  slug: amazon-codeguru-profiler-aggregated-profile-time-structure
- name: Amazon Codeguru Profiler Aggregation Period Structure
  property_count: 0
  slug: amazon-codeguru-profiler-aggregation-period-structure
- name: Amazon Codeguru Profiler Anomalies Structure
  property_count: 0
  slug: amazon-codeguru-profiler-anomalies-structure
- name: Amazon Codeguru Profiler Anomaly Instance Id Structure
  property_count: 0
  slug: amazon-codeguru-profiler-anomaly-instance-id-structure
- name: Amazon Codeguru Profiler Anomaly Instance Structure
  property_count: 4
  slug: amazon-codeguru-profiler-anomaly-instance-structure
- name: Amazon Codeguru Profiler Anomaly Instances Structure
  property_count: 0
  slug: amazon-codeguru-profiler-anomaly-instances-structure
- name: Amazon Codeguru Profiler Anomaly Structure
  property_count: 3
  slug: amazon-codeguru-profiler-anomaly-structure
- name: Amazon Codeguru Profiler Batch Get Frame Metric Data Request Structure
  property_count: 1
  slug: amazon-codeguru-profiler-batch-get-frame-metric-data-request-structure
- name: Amazon Codeguru Profiler Batch Get Frame Metric Data Response Structure
  property_count: 6
  slug: amazon-codeguru-profiler-batch-get-frame-metric-data-response-structure
- name: Amazon Codeguru Profiler Boolean Structure
  property_count: 0
  slug: amazon-codeguru-profiler-boolean-structure
- name: Amazon Codeguru Profiler Channel Id Structure
  property_count: 0
  slug: amazon-codeguru-profiler-channel-id-structure
- name: Amazon Codeguru Profiler Channel Structure
  property_count: 3
  slug: amazon-codeguru-profiler-channel-structure
- name: Amazon Codeguru Profiler Channel Uri Structure
  property_count: 0
  slug: amazon-codeguru-profiler-channel-uri-structure
- name: Amazon Codeguru Profiler Channels Structure
  property_count: 0
  slug: amazon-codeguru-profiler-channels-structure
- name: Amazon Codeguru Profiler Client Token Structure
  property_count: 0
  slug: amazon-codeguru-profiler-client-token-structure
- name: Amazon Codeguru Profiler Compute Platform Structure
  property_count: 0
  slug: amazon-codeguru-profiler-compute-platform-structure
- name: Amazon Codeguru Profiler Configure Agent Request Structure
  property_count: 2
  slug: amazon-codeguru-profiler-configure-agent-request-structure
- name: Amazon Codeguru Profiler Configure Agent Response Structure
  property_count: 1
  slug: amazon-codeguru-profiler-configure-agent-response-structure
- name: Amazon Codeguru Profiler Create Profiling Group Request Structure
  property_count: 4
  slug: amazon-codeguru-profiler-create-profiling-group-request-structure
- name: Amazon Codeguru Profiler Create Profiling Group Response Structure
  property_count: 1
  slug: amazon-codeguru-profiler-create-profiling-group-response-structure
- name: Amazon Codeguru Profiler Delete Profiling Group Request Structure
  property_count: 0
  slug: amazon-codeguru-profiler-delete-profiling-group-request-structure
- name: Amazon Codeguru Profiler Delete Profiling Group Response Structure
  property_count: 0
  slug: amazon-codeguru-profiler-delete-profiling-group-response-structure
- name: Amazon Codeguru Profiler Describe Profiling Group Request Structure
  property_count: 0
  slug: amazon-codeguru-profiler-describe-profiling-group-request-structure
- name: Amazon Codeguru Profiler Describe Profiling Group Response Structure
  property_count: 1
  slug: amazon-codeguru-profiler-describe-profiling-group-response-structure
- name: Amazon Codeguru Profiler Double Structure
  property_count: 0
  slug: amazon-codeguru-profiler-double-structure
- name: Amazon Codeguru Profiler Event Publisher Structure
  property_count: 0
  slug: amazon-codeguru-profiler-event-publisher-structure
- name: Amazon Codeguru Profiler Event Publishers Structure
  property_count: 0
  slug: amazon-codeguru-profiler-event-publishers-structure
- name: Amazon Codeguru Profiler Feedback Type Structure
  property_count: 0
  slug: amazon-codeguru-profiler-feedback-type-structure
- name: Amazon Codeguru Profiler Findings Report Id Structure
  property_count: 0
  slug: amazon-codeguru-profiler-findings-report-id-structure
- name: Amazon Codeguru Profiler Findings Report Summaries Structure
  property_count: 0
  slug: amazon-codeguru-profiler-findings-report-summaries-structure
- name: Amazon Codeguru Profiler Findings Report Summary Structure
  property_count: 5
  slug: amazon-codeguru-profiler-findings-report-summary-structure
- name: Amazon Codeguru Profiler Fleet Instance Id Structure
  property_count: 0
  slug: amazon-codeguru-profiler-fleet-instance-id-structure
- name: Amazon Codeguru Profiler Frame Metric Data Structure
  property_count: 0
  slug: amazon-codeguru-profiler-frame-metric-data-structure
- name: Amazon Codeguru Profiler Frame Metric Datum Structure
  property_count: 2
  slug: amazon-codeguru-profiler-frame-metric-datum-structure
- name: Amazon Codeguru Profiler Frame Metric Structure
  property_count: 3
  slug: amazon-codeguru-profiler-frame-metric-structure
- name: Amazon Codeguru Profiler Frame Metric Value Structure
  property_count: 0
  slug: amazon-codeguru-profiler-frame-metric-value-structure
- name: Amazon Codeguru Profiler Frame Metric Values Structure
  property_count: 0
  slug: amazon-codeguru-profiler-frame-metric-values-structure
- name: Amazon Codeguru Profiler Frame Metrics Structure
  property_count: 0
  slug: amazon-codeguru-profiler-frame-metrics-structure
- name: Amazon Codeguru Profiler Get Findings Report Account Summary Request Structure
  property_count: 0
  slug: amazon-codeguru-profiler-get-findings-report-account-summary-request-structure
- name: Amazon Codeguru Profiler Get Findings Report Account Summary Response Structure
  property_count: 2
  slug: amazon-codeguru-profiler-get-findings-report-account-summary-response-structure
- name: Amazon Codeguru Profiler Get Notification Configuration Request Structure
  property_count: 0
  slug: amazon-codeguru-profiler-get-notification-configuration-request-structure
- name: Amazon Codeguru Profiler Get Notification Configuration Response Structure
  property_count: 1
  slug: amazon-codeguru-profiler-get-notification-configuration-response-structure
- name: Amazon Codeguru Profiler Get Policy Request Structure
  property_count: 0
  slug: amazon-codeguru-profiler-get-policy-request-structure
- name: Amazon Codeguru Profiler Get Policy Response Structure
  property_count: 2
  slug: amazon-codeguru-profiler-get-policy-response-structure
- name: Amazon Codeguru Profiler Get Profile Request Structure
  property_count: 0
  slug: amazon-codeguru-profiler-get-profile-request-structure
- name: Amazon Codeguru Profiler Get Profile Response Structure
  property_count: 1
  slug: amazon-codeguru-profiler-get-profile-response-structure
- name: Amazon Codeguru Profiler Get Recommendations Request Structure
  property_count: 0
  slug: amazon-codeguru-profiler-get-recommendations-request-structure
- name: Amazon Codeguru Profiler Get Recommendations Response Structure
  property_count: 5
  slug: amazon-codeguru-profiler-get-recommendations-response-structure
- name: Amazon Codeguru Profiler Integer Structure
  property_count: 0
  slug: amazon-codeguru-profiler-integer-structure
- name: Amazon Codeguru Profiler List Findings Reports Request Structure
  property_count: 0
  slug: amazon-codeguru-profiler-list-findings-reports-request-structure
- name: Amazon Codeguru Profiler List Findings Reports Response Structure
  property_count: 2
  slug: amazon-codeguru-profiler-list-findings-reports-response-structure
- name: Amazon Codeguru Profiler List Of Timestamps Structure
  property_count: 0
  slug: amazon-codeguru-profiler-list-of-timestamps-structure
- name: Amazon Codeguru Profiler List Profile Times Request Structure
  property_count: 0
  slug: amazon-codeguru-profiler-list-profile-times-request-structure
- name: Amazon Codeguru Profiler List Profile Times Response Structure
  property_count: 2
  slug: amazon-codeguru-profiler-list-profile-times-response-structure
- name: Amazon Codeguru Profiler List Profiling Groups Request Structure
  property_count: 0
  slug: amazon-codeguru-profiler-list-profiling-groups-request-structure
- name: Amazon Codeguru Profiler List Profiling Groups Response Structure
  property_count: 3
  slug: amazon-codeguru-profiler-list-profiling-groups-response-structure
- name: Amazon Codeguru Profiler List Tags For Resource Request Structure
  property_count: 0
  slug: amazon-codeguru-profiler-list-tags-for-resource-request-structure
- name: Amazon Codeguru Profiler List Tags For Resource Response Structure
  property_count: 1
  slug: amazon-codeguru-profiler-list-tags-for-resource-response-structure
- name: Amazon Codeguru Profiler Locale Structure
  property_count: 0
  slug: amazon-codeguru-profiler-locale-structure
- name: Amazon Codeguru Profiler Match Structure
  property_count: 3
  slug: amazon-codeguru-profiler-match-structure
- name: Amazon Codeguru Profiler Matches Structure
  property_count: 0
  slug: amazon-codeguru-profiler-matches-structure
- name: Amazon Codeguru Profiler Max Depth Structure
  property_count: 0
  slug: amazon-codeguru-profiler-max-depth-structure
- name: Amazon Codeguru Profiler Max Results Structure
  property_count: 0
  slug: amazon-codeguru-profiler-max-results-structure
- name: Amazon Codeguru Profiler Metadata Field Structure
  property_count: 0
  slug: amazon-codeguru-profiler-metadata-field-structure
- name: Amazon Codeguru Profiler Metadata Structure
  property_count: 0
  slug: amazon-codeguru-profiler-metadata-structure
- name: Amazon Codeguru Profiler Metric Structure
  property_count: 3
  slug: amazon-codeguru-profiler-metric-structure
- name: Amazon Codeguru Profiler Metric Type Structure
  property_count: 0
  slug: amazon-codeguru-profiler-metric-type-structure
- name: Amazon Codeguru Profiler Notification Configuration Structure
  property_count: 1
  slug: amazon-codeguru-profiler-notification-configuration-structure
- name: Amazon Codeguru Profiler Order By Structure
  property_count: 0
  slug: amazon-codeguru-profiler-order-by-structure
- name: Amazon Codeguru Profiler Pagination Token Structure
  property_count: 0
  slug: amazon-codeguru-profiler-pagination-token-structure
- name: Amazon Codeguru Profiler Pattern Structure
  property_count: 7
  slug: amazon-codeguru-profiler-pattern-structure
- name: Amazon Codeguru Profiler Percentage Structure
  property_count: 0
  slug: amazon-codeguru-profiler-percentage-structure
- name: Amazon Codeguru Profiler Period Structure
  property_count: 0
  slug: amazon-codeguru-profiler-period-structure
- name: Amazon Codeguru Profiler Post Agent Profile Request Structure
  property_count: 1
  slug: amazon-codeguru-profiler-post-agent-profile-request-structure
- name: Amazon Codeguru Profiler Post Agent Profile Response Structure
  property_count: 0
  slug: amazon-codeguru-profiler-post-agent-profile-response-structure
- name: Amazon Codeguru Profiler Principal Structure
  property_count: 0
  slug: amazon-codeguru-profiler-principal-structure
- name: Amazon Codeguru Profiler Principals Structure
  property_count: 0
  slug: amazon-codeguru-profiler-principals-structure
- name: Amazon Codeguru Profiler Profile Time Structure
  property_count: 1
  slug: amazon-codeguru-profiler-profile-time-structure
- name: Amazon Codeguru Profiler Profile Times Structure
  property_count: 0
  slug: amazon-codeguru-profiler-profile-times-structure
- name: Amazon Codeguru Profiler Profiling Group Arn Structure
  property_count: 0
  slug: amazon-codeguru-profiler-profiling-group-arn-structure
- name: Amazon Codeguru Profiler Profiling Group Description Structure
  property_count: 8
  slug: amazon-codeguru-profiler-profiling-group-description-structure
- name: Amazon Codeguru Profiler Profiling Group Descriptions Structure
  property_count: 0
  slug: amazon-codeguru-profiler-profiling-group-descriptions-structure
- name: Amazon Codeguru Profiler Profiling Group Name Structure
  property_count: 0
  slug: amazon-codeguru-profiler-profiling-group-name-structure
- name: Amazon Codeguru Profiler Profiling Group Names Structure
  property_count: 0
  slug: amazon-codeguru-profiler-profiling-group-names-structure
- name: Amazon Codeguru Profiler Profiling Status Structure
  property_count: 3
  slug: amazon-codeguru-profiler-profiling-status-structure
- name: Amazon Codeguru Profiler Put Permission Request Structure
  property_count: 2
  slug: amazon-codeguru-profiler-put-permission-request-structure
- name: Amazon Codeguru Profiler Put Permission Response Structure
  property_count: 2
  slug: amazon-codeguru-profiler-put-permission-response-structure
- name: Amazon Codeguru Profiler Recommendation Structure
  property_count: 6
  slug: amazon-codeguru-profiler-recommendation-structure
- name: Amazon Codeguru Profiler Recommendations Structure
  property_count: 0
  slug: amazon-codeguru-profiler-recommendations-structure
- name: Amazon Codeguru Profiler Remove Notification Channel Request Structure
  property_count: 0
  slug: amazon-codeguru-profiler-remove-notification-channel-request-structure
- name: Amazon Codeguru Profiler Remove Notification Channel Response Structure
  property_count: 1
  slug: amazon-codeguru-profiler-remove-notification-channel-response-structure
- name: Amazon Codeguru Profiler Remove Permission Request Structure
  property_count: 0
  slug: amazon-codeguru-profiler-remove-permission-request-structure
- name: Amazon Codeguru Profiler Remove Permission Response Structure
  property_count: 2
  slug: amazon-codeguru-profiler-remove-permission-response-structure
- name: Amazon Codeguru Profiler Revision Id Structure
  property_count: 0
  slug: amazon-codeguru-profiler-revision-id-structure
- name: Amazon Codeguru Profiler String Structure
  property_count: 0
  slug: amazon-codeguru-profiler-string-structure
- name: Amazon Codeguru Profiler Strings Structure
  property_count: 0
  slug: amazon-codeguru-profiler-strings-structure
- name: Amazon Codeguru Profiler Submit Feedback Request Structure
  property_count: 2
  slug: amazon-codeguru-profiler-submit-feedback-request-structure
- name: Amazon Codeguru Profiler Submit Feedback Response Structure
  property_count: 0
  slug: amazon-codeguru-profiler-submit-feedback-response-structure
- name: Amazon Codeguru Profiler Tag Keys Structure
  property_count: 0
  slug: amazon-codeguru-profiler-tag-keys-structure
- name: Amazon Codeguru Profiler Tag Resource Request Structure
  property_count: 1
  slug: amazon-codeguru-profiler-tag-resource-request-structure
- name: Amazon Codeguru Profiler Tag Resource Response Structure
  property_count: 0
  slug: amazon-codeguru-profiler-tag-resource-response-structure
- name: Amazon Codeguru Profiler Tags Map Structure
  property_count: 0
  slug: amazon-codeguru-profiler-tags-map-structure
- name: Amazon Codeguru Profiler Target Frame Structure
  property_count: 0
  slug: amazon-codeguru-profiler-target-frame-structure
- name: Amazon Codeguru Profiler Target Frames Structure
  property_count: 0
  slug: amazon-codeguru-profiler-target-frames-structure
- name: Amazon Codeguru Profiler Thread States Structure
  property_count: 0
  slug: amazon-codeguru-profiler-thread-states-structure
- name: Amazon Codeguru Profiler Timestamp Structure Structure
  property_count: 1
  slug: amazon-codeguru-profiler-timestamp-structure-structure
- name: Amazon Codeguru Profiler Timestamp Structure
  property_count: 0
  slug: amazon-codeguru-profiler-timestamp-structure
- name: Amazon Codeguru Profiler Unprocessed End Time Map Structure
  property_count: 0
  slug: amazon-codeguru-profiler-unprocessed-end-time-map-structure
- name: Amazon Codeguru Profiler Untag Resource Request Structure
  property_count: 0
  slug: amazon-codeguru-profiler-untag-resource-request-structure
- name: Amazon Codeguru Profiler Untag Resource Response Structure
  property_count: 0
  slug: amazon-codeguru-profiler-untag-resource-response-structure
- name: Amazon Codeguru Profiler Update Profiling Group Request Structure
  property_count: 1
  slug: amazon-codeguru-profiler-update-profiling-group-request-structure
- name: Amazon Codeguru Profiler Update Profiling Group Response Structure
  property_count: 1
  slug: amazon-codeguru-profiler-update-profiling-group-response-structure
- name: Amazon Codeguru Profiler User Feedback Structure
  property_count: 1
  slug: amazon-codeguru-profiler-user-feedback-structure
jsonld:
- class_count: 71
  name: Amazon Codeguru Profiler Context
  property_count: 71
  slug: amazon-codeguru-profiler-context
layout: provider
mcp_servers:
- description: ''
  name: amazon-codeguru-profiler-mcp.yml
  slug: amazon-codeguru-profiler-mcpyml
modified: '2026-04-19'
name: Amazon CodeGuru Profiler
nav: Providers
network: true
overview: 'Amazon CodeGuru Profiler publishes 4 APIs on the [APIs.io](https://apis.io/) network, including Internal API, ProfilingGroups API, ProfilingGroups#clientToken API, and 1 more. Tagged areas include Amazon, Application Performance, Profiling, DevOps, and Machine Learning.


  The Amazon CodeGuru Profiler catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Amazon CodeGuru Profiler''s developer surface includes authentication, engineering blog, and 5 more developer resources.'
random_paper: 65
rules:
- name: Amazon CodeGuru Profiler API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: amazon-codeguru-profiler-jsonschema-spectral-rules
- name: Amazon CodeGuru Profiler API Rules
  rule_count: 16
  severity_counts:
    error: 5
    hint: 0
    info: 2
    warn: 9
  slug: amazon-codeguru-profiler-spectral-rules
score:
  band: thin
  composite: 37.7
  delta: 0.0
  facets:
    commercial_clarity: 0.0
    contract_quality: 72.4
    developer_ergonomics: 15.2
    discoverability: 81.5
    governance: 69.8
    operational_transparency: 0.0
  previous_composite: 37.7
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 4
    mcp: derived
  schema_version: 0.11.0
  scored_at: '2026-08-12'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/amazon-codeguru-profiler/refs/heads/main/screenshots/amazon-codeguru-profiler-2026-07-25T195956.png
security:
- kind: authentication
  name: Amazon Codeguru Profiler Authentication
  slug: amazon-codeguru-profiler-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Amazon Codeguru Profiler Domain Security
  slug: amazon-codeguru-profiler-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Amazon Codeguru Profiler Vulnerability Disclosure
  slug: amazon-codeguru-profiler-vulnerability-disclosure
  summary_line: Hackerone · security.txt · contact published
slug: amazon-codeguru-profiler
tags:
- Amazon
- Application Performance
- Profiling
- DevOps
- Machine Learning
---
