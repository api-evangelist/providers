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
    agent_skills: false
    agentic_access: true
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: true
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.1
  score: 48.1
  scored_at: '2026-07-27'
agentic_access:
- acting_count: 20
  human_in_the_loop: 0
  name: Amazon Ground Station Agentic Access
  operation_count: 33
  slug: amazon-ground-station-agentic-access
  summary_line: 33 operations · 20 acting
api_count: 12
apis:
- description: The Agent API from Amazon Ground Station — 3 operation(s) for agent.
  name: Amazon Ground Station Agent API
  slug: amazon-ground-station-agent-api
- description: The Config API from Amazon Ground Station — 2 operation(s) for config.
  name: Amazon Ground Station Config API
  slug: amazon-ground-station-config-api
- description: The Contact API from Amazon Ground Station — 2 operation(s) for contact.
  name: Amazon Ground Station Contact API
  slug: amazon-ground-station-contact-api
- description: The Contacts API from Amazon Ground Station — 1 operation(s) for contacts.
  name: Amazon Ground Station Contacts API
  slug: amazon-ground-station-contacts-api
- description: The DataflowEndpointGroup API from Amazon Ground Station — 2 operation(s) for dataflowendpointgroup.
  name: Amazon Ground Station DataflowEndpointGroup API
  slug: amazon-ground-station-dataflowendpointgroup-api
- description: The Ephemerides API from Amazon Ground Station — 1 operation(s) for ephemerides.
  name: Amazon Ground Station Ephemerides API
  slug: amazon-ground-station-ephemerides-api
- description: The Ephemeris API from Amazon Ground Station — 2 operation(s) for ephemeris.
  name: Amazon Ground Station Ephemeris API
  slug: amazon-ground-station-ephemeris-api
- description: The Groundstation API from Amazon Ground Station — 1 operation(s) for groundstation.
  name: Amazon Ground Station Groundstation API
  slug: amazon-ground-station-groundstation-api
- description: The Minute Usage API from Amazon Ground Station — 1 operation(s) for minute usage.
  name: Amazon Ground Station Minute Usage API
  slug: amazon-ground-station-minute-usage-api
- description: The Missionprofile API from Amazon Ground Station — 2 operation(s) for missionprofile.
  name: Amazon Ground Station Missionprofile API
  slug: amazon-ground-station-missionprofile-api
- description: The Satellite API from Amazon Ground Station — 2 operation(s) for satellite.
  name: Amazon Ground Station Satellite API
  slug: amazon-ground-station-satellite-api
- description: The Tags API from Amazon Ground Station — 2 operation(s) for tags.
  name: Amazon Ground Station Tags API
  slug: amazon-ground-station-tags-api
artifact_total: 553
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/amazon-ground-station-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/amazon-ground-station-trust-center.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/amazon-ground-station-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/amazon-ground-station-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/amazon-ground-station-authentication.yml
- group: start
  title: ''
  type: Portal
  url: https://aws.amazon.com/ground-station/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.aws.amazon.com/ground-station/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://aws.amazon.com/service-terms/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://aws.amazon.com/privacy/
- group: operate
  title: ''
  type: Support
  url: https://aws.amazon.com/premiumsupport/
- group: company
  title: ''
  type: Blog
  url: https://aws.amazon.com/blogs/publicsector/tag/aws-ground-station/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/aws
- group: start
  title: ''
  type: Console
  url: https://console.aws.amazon.com/groundstation/
- group: start
  title: ''
  type: Signup
  url: https://portal.aws.amazon.com/billing/signup
- group: operate
  title: ''
  type: StatusPage
  url: https://health.aws.amazon.com/health/status
- group: operate
  title: ''
  type: Contact
  url: https://aws.amazon.com/contact-us/
- group: design
  title: ''
  type: SpectralRules
  url: rules/amazon-ground-station-spectral-rules.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/amazon-ground-station-vocabulary.yaml
created: '2026-03-16'
description: AWS Ground Station is a fully managed service that lets you control satellite communications, process satellite data, and scale your satellite operations without having to worry about building or managing your own ground station infrastructure.
examples:
- key_count: 6
  name: Ground Station Agent Details Example
  slug: ground-station-agent-details-example
- key_count: 2
  name: Ground Station Aggregate Status Example
  slug: ground-station-aggregate-status-example
- key_count: 1
  name: Ground Station Antenna Demod Decode Details Example
  slug: ground-station-antenna-demod-decode-details-example
- key_count: 1
  name: Ground Station Antenna Downlink Config Example
  slug: ground-station-antenna-downlink-config-example
- key_count: 3
  name: Ground Station Antenna Downlink Demod Decode Config Example
  slug: ground-station-antenna-downlink-demod-decode-config-example
- key_count: 3
  name: Ground Station Antenna Uplink Config Example
  slug: ground-station-antenna-uplink-config-example
- key_count: 5
  name: Ground Station Aws Ground Station Agent Endpoint Example
  slug: ground-station-aws-ground-station-agent-endpoint-example
- key_count: 0
  name: Ground Station Cancel Contact Request Example
  slug: ground-station-cancel-contact-request-example
- key_count: 6
  name: Ground Station Component Status Data Example
  slug: ground-station-component-status-data-example
- key_count: 2
  name: Ground Station Component Version Example
  slug: ground-station-component-version-example
- key_count: 3
  name: Ground Station Config Details Example
  slug: ground-station-config-details-example
- key_count: 3
  name: Ground Station Config Id Response Example
  slug: ground-station-config-id-response-example
- key_count: 4
  name: Ground Station Config List Item Example
  slug: ground-station-config-list-item-example
- key_count: 6
  name: Ground Station Config Type Data Example
  slug: ground-station-config-type-data-example
- key_count: 2
  name: Ground Station Connection Details Example
  slug: ground-station-connection-details-example
- key_count: 6
  name: Ground Station Contact Data Example
  slug: ground-station-contact-data-example
- key_count: 1
  name: Ground Station Contact Id Response Example
  slug: ground-station-contact-id-response-example
- key_count: 3
  name: Ground Station Create Config Request Example
  slug: ground-station-create-config-request-example
- key_count: 4
  name: Ground Station Create Dataflow Endpoint Group Request Example
  slug: ground-station-create-dataflow-endpoint-group-request-example
- key_count: 6
  name: Ground Station Create Ephemeris Request Example
  slug: ground-station-create-ephemeris-request-example
- key_count: 6
  name: Ground Station Create Mission Profile Request Example
  slug: ground-station-create-mission-profile-request-example
- key_count: 3
  name: Ground Station Dataflow Detail Example
  slug: ground-station-dataflow-detail-example
- key_count: 2
  name: Ground Station Dataflow Endpoint Config Example
  slug: ground-station-dataflow-endpoint-config-example
- key_count: 4
  name: Ground Station Dataflow Endpoint Example
  slug: ground-station-dataflow-endpoint-example
- key_count: 1
  name: Ground Station Dataflow Endpoint Group Id Response Example
  slug: ground-station-dataflow-endpoint-group-id-response-example
- key_count: 2
  name: Ground Station Dataflow Endpoint List Item Example
  slug: ground-station-dataflow-endpoint-list-item-example
- key_count: 1
  name: Ground Station Decode Config Example
  slug: ground-station-decode-config-example
- key_count: 0
  name: Ground Station Delete Config Request Example
  slug: ground-station-delete-config-request-example
- key_count: 0
  name: Ground Station Delete Dataflow Endpoint Group Request Example
  slug: ground-station-delete-dataflow-endpoint-group-request-example
- key_count: 0
  name: Ground Station Delete Ephemeris Request Example
  slug: ground-station-delete-ephemeris-request-example
- key_count: 0
  name: Ground Station Delete Mission Profile Request Example
  slug: ground-station-delete-mission-profile-request-example
- key_count: 1
  name: Ground Station Demodulation Config Example
  slug: ground-station-demodulation-config-example
- key_count: 0
  name: Ground Station Describe Contact Request Example
  slug: ground-station-describe-contact-request-example
- key_count: 6
  name: Ground Station Describe Contact Response Example
  slug: ground-station-describe-contact-response-example
- key_count: 0
  name: Ground Station Describe Ephemeris Request Example
  slug: ground-station-describe-ephemeris-request-example
- key_count: 6
  name: Ground Station Describe Ephemeris Response Example
  slug: ground-station-describe-ephemeris-response-example
- key_count: 4
  name: Ground Station Destination Example
  slug: ground-station-destination-example
- key_count: 3
  name: Ground Station Discovery Data Example
  slug: ground-station-discovery-data-example
- key_count: 2
  name: Ground Station Eirp Example
  slug: ground-station-eirp-example
- key_count: 2
  name: Ground Station Elevation Example
  slug: ground-station-elevation-example
- key_count: 5
  name: Ground Station Endpoint Details Example
  slug: ground-station-endpoint-details-example
- key_count: 2
  name: Ground Station Ephemeris Data Example
  slug: ground-station-ephemeris-data-example
- key_count: 2
  name: Ground Station Ephemeris Description Example
  slug: ground-station-ephemeris-description-example
- key_count: 1
  name: Ground Station Ephemeris Id Response Example
  slug: ground-station-ephemeris-id-response-example
- key_count: 6
  name: Ground Station Ephemeris Item Example
  slug: ground-station-ephemeris-item-example
- key_count: 4
  name: Ground Station Ephemeris Meta Data Example
  slug: ground-station-ephemeris-meta-data-example
- key_count: 2
  name: Ground Station Ephemeris Type Description Example
  slug: ground-station-ephemeris-type-description-example
- key_count: 2
  name: Ground Station Frequency Bandwidth Example
  slug: ground-station-frequency-bandwidth-example
- key_count: 2
  name: Ground Station Frequency Example
  slug: ground-station-frequency-example
- key_count: 0
  name: Ground Station Get Agent Configuration Request Example
  slug: ground-station-get-agent-configuration-request-example
- key_count: 2
  name: Ground Station Get Agent Configuration Response Example
  slug: ground-station-get-agent-configuration-response-example
- key_count: 0
  name: Ground Station Get Config Request Example
  slug: ground-station-get-config-request-example
- key_count: 6
  name: Ground Station Get Config Response Example
  slug: ground-station-get-config-response-example
- key_count: 0
  name: Ground Station Get Dataflow Endpoint Group Request Example
  slug: ground-station-get-dataflow-endpoint-group-request-example
- key_count: 6
  name: Ground Station Get Dataflow Endpoint Group Response Example
  slug: ground-station-get-dataflow-endpoint-group-response-example
- key_count: 2
  name: Ground Station Get Minute Usage Request Example
  slug: ground-station-get-minute-usage-request-example
- key_count: 5
  name: Ground Station Get Minute Usage Response Example
  slug: ground-station-get-minute-usage-response-example
- key_count: 0
  name: Ground Station Get Mission Profile Request Example
  slug: ground-station-get-mission-profile-request-example
- key_count: 6
  name: Ground Station Get Mission Profile Response Example
  slug: ground-station-get-mission-profile-response-example
- key_count: 0
  name: Ground Station Get Satellite Request Example
  slug: ground-station-get-satellite-request-example
- key_count: 5
  name: Ground Station Get Satellite Response Example
  slug: ground-station-get-satellite-response-example
- key_count: 3
  name: Ground Station Ground Station Data Example
  slug: ground-station-ground-station-data-example
- key_count: 2
  name: Ground Station Integer Range Example
  slug: ground-station-integer-range-example
- key_count: 2
  name: Ground Station Kms Key Example
  slug: ground-station-kms-key-example
- key_count: 0
  name: Ground Station List Configs Request Example
  slug: ground-station-list-configs-request-example
- key_count: 2
  name: Ground Station List Configs Response Example
  slug: ground-station-list-configs-response-example
- key_count: 6
  name: Ground Station List Contacts Request Example
  slug: ground-station-list-contacts-request-example
- key_count: 2
  name: Ground Station List Contacts Response Example
  slug: ground-station-list-contacts-response-example
- key_count: 0
  name: Ground Station List Dataflow Endpoint Groups Request Example
  slug: ground-station-list-dataflow-endpoint-groups-request-example
- key_count: 2
  name: Ground Station List Dataflow Endpoint Groups Response Example
  slug: ground-station-list-dataflow-endpoint-groups-response-example
- key_count: 4
  name: Ground Station List Ephemerides Request Example
  slug: ground-station-list-ephemerides-request-example
- key_count: 2
  name: Ground Station List Ephemerides Response Example
  slug: ground-station-list-ephemerides-response-example
- key_count: 0
  name: Ground Station List Ground Stations Request Example
  slug: ground-station-list-ground-stations-request-example
- key_count: 2
  name: Ground Station List Ground Stations Response Example
  slug: ground-station-list-ground-stations-response-example
- key_count: 0
  name: Ground Station List Mission Profiles Request Example
  slug: ground-station-list-mission-profiles-request-example
- key_count: 2
  name: Ground Station List Mission Profiles Response Example
  slug: ground-station-list-mission-profiles-response-example
- key_count: 0
  name: Ground Station List Satellites Request Example
  slug: ground-station-list-satellites-request-example
- key_count: 2
  name: Ground Station List Satellites Response Example
  slug: ground-station-list-satellites-response-example
- key_count: 0
  name: Ground Station List Tags For Resource Request Example
  slug: ground-station-list-tags-for-resource-request-example
- key_count: 1
  name: Ground Station List Tags For Resource Response Example
  slug: ground-station-list-tags-for-resource-response-example
- key_count: 1
  name: Ground Station Mission Profile Id Response Example
  slug: ground-station-mission-profile-id-response-example
- key_count: 4
  name: Ground Station Mission Profile List Item Example
  slug: ground-station-mission-profile-list-item-example
- key_count: 2
  name: Ground Station Oem Ephemeris Example
  slug: ground-station-oem-ephemeris-example
- key_count: 2
  name: Ground Station Ranged Connection Details Example
  slug: ground-station-ranged-connection-details-example
- key_count: 2
  name: Ground Station Ranged Socket Address Example
  slug: ground-station-ranged-socket-address-example
- key_count: 2
  name: Ground Station Register Agent Request Example
  slug: ground-station-register-agent-request-example
- key_count: 1
  name: Ground Station Register Agent Response Example
  slug: ground-station-register-agent-response-example
- key_count: 6
  name: Ground Station Reserve Contact Request Example
  slug: ground-station-reserve-contact-request-example
- key_count: 3
  name: Ground Station S3 Object Example
  slug: ground-station-s3-object-example
- key_count: 3
  name: Ground Station S3 Recording Config Example
  slug: ground-station-s3-recording-config-example
- key_count: 2
  name: Ground Station S3 Recording Details Example
  slug: ground-station-s3-recording-details-example
- key_count: 5
  name: Ground Station Satellite List Item Example
  slug: ground-station-satellite-list-item-example
- key_count: 3
  name: Ground Station Security Details Example
  slug: ground-station-security-details-example
- key_count: 0
  name: Ground Station Signature Map Example
  slug: ground-station-signature-map-example
- key_count: 2
  name: Ground Station Socket Address Example
  slug: ground-station-socket-address-example
- key_count: 4
  name: Ground Station Source Example
  slug: ground-station-source-example
- key_count: 3
  name: Ground Station Spectrum Config Example
  slug: ground-station-spectrum-config-example
- key_count: 1
  name: Ground Station Tag Resource Request Example
  slug: ground-station-tag-resource-request-example
- key_count: 0
  name: Ground Station Tag Resource Response Example
  slug: ground-station-tag-resource-response-example
- key_count: 0
  name: Ground Station Tags Map Example
  slug: ground-station-tags-map-example
- key_count: 2
  name: Ground Station Time Range Example
  slug: ground-station-time-range-example
- key_count: 3
  name: Ground Station Tle Data Example
  slug: ground-station-tle-data-example
- key_count: 2
  name: Ground Station Tle Ephemeris Example
  slug: ground-station-tle-ephemeris-example
- key_count: 1
  name: Ground Station Tracking Config Example
  slug: ground-station-tracking-config-example
- key_count: 0
  name: Ground Station Untag Resource Request Example
  slug: ground-station-untag-resource-request-example
- key_count: 0
  name: Ground Station Untag Resource Response Example
  slug: ground-station-untag-resource-response-example
- key_count: 3
  name: Ground Station Update Agent Status Request Example
  slug: ground-station-update-agent-status-request-example
- key_count: 1
  name: Ground Station Update Agent Status Response Example
  slug: ground-station-update-agent-status-response-example
- key_count: 2
  name: Ground Station Update Config Request Example
  slug: ground-station-update-config-request-example
- key_count: 3
  name: Ground Station Update Ephemeris Request Example
  slug: ground-station-update-ephemeris-request-example
- key_count: 6
  name: Ground Station Update Mission Profile Request Example
  slug: ground-station-update-mission-profile-request-example
- key_count: 2
  name: Ground Station Uplink Echo Config Example
  slug: ground-station-uplink-echo-config-example
- key_count: 2
  name: Ground Station Uplink Spectrum Config Example
  slug: ground-station-uplink-spectrum-config-example
features:
- description: AWS manages a global network of antennas so you do not need to build or operate your own ground station infrastructure.
  name: Managed Ground Station Infrastructure
- description: Schedule satellite contacts through a simple API, selecting the satellite, time window, and ground station location.
  name: Satellite Contact Scheduling
- description: Access AWS ground station antennas deployed at strategic worldwide locations for maximum satellite coverage.
  name: Global Antenna Network
- description: Receive satellite data directly into AWS cloud services for processing, storage, and analysis.
  name: Data Downlink and Processing
- description: Configure mission profiles specifying dataflow endpoints, antenna frequencies, and processing parameters.
  name: Mission Profile Configuration
- description: Stream satellite data directly into Amazon S3, Kinesis, EC2, and other AWS services for processing.
  name: Integration with AWS Services
finops:
- name: Amazon Ground Station Finops
  service_category: API
  slug: amazon-ground-station-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/amazon-ground-station.png
json_schemas:
- name: AgentCpuCoresList
  property_count: 0
  slug: ground-station-agent-cpu-cores-list
- name: AgentDetails
  property_count: 6
  slug: ground-station-agent-details
- name: AgentStatus
  property_count: 0
  slug: ground-station-agent-status
- name: AggregateStatus
  property_count: 2
  slug: ground-station-aggregate-status
- name: AngleUnits
  property_count: 0
  slug: ground-station-angle-units
- name: AntennaDemodDecodeDetails
  property_count: 1
  slug: ground-station-antenna-demod-decode-details
- name: AntennaDownlinkConfig
  property_count: 1
  slug: ground-station-antenna-downlink-config
- name: AntennaDownlinkDemodDecodeConfig
  property_count: 3
  slug: ground-station-antenna-downlink-demod-decode-config
- name: AntennaUplinkConfig
  property_count: 3
  slug: ground-station-antenna-uplink-config
- name: AnyArn
  property_count: 0
  slug: ground-station-any-arn
- name: AuditResults
  property_count: 0
  slug: ground-station-audit-results
- name: AwsGroundStationAgentEndpoint
  property_count: 5
  slug: ground-station-aws-ground-station-agent-endpoint
- name: AWSRegion
  property_count: 0
  slug: ground-station-aws-region
- name: BandwidthUnits
  property_count: 0
  slug: ground-station-bandwidth-units
- name: Boolean
  property_count: 0
  slug: ground-station-boolean
- name: BucketArn
  property_count: 0
  slug: ground-station-bucket-arn
- name: CancelContactRequest
  property_count: 0
  slug: ground-station-cancel-contact-request
- name: CapabilityArnList
  property_count: 0
  slug: ground-station-capability-arn-list
- name: CapabilityArn
  property_count: 0
  slug: ground-station-capability-arn
- name: CapabilityHealthReasonList
  property_count: 0
  slug: ground-station-capability-health-reason-list
- name: CapabilityHealthReason
  property_count: 0
  slug: ground-station-capability-health-reason
- name: CapabilityHealth
  property_count: 0
  slug: ground-station-capability-health
- name: ComponentStatusData
  property_count: 7
  slug: ground-station-component-status-data
- name: ComponentStatusList
  property_count: 0
  slug: ground-station-component-status-list
- name: ComponentTypeString
  property_count: 0
  slug: ground-station-component-type-string
- name: ComponentVersionList
  property_count: 0
  slug: ground-station-component-version-list
- name: ComponentVersion
  property_count: 2
  slug: ground-station-component-version
- name: ConfigArn
  property_count: 0
  slug: ground-station-config-arn
- name: ConfigCapabilityType
  property_count: 0
  slug: ground-station-config-capability-type
- name: ConfigDetails
  property_count: 3
  slug: ground-station-config-details
- name: ConfigIdResponse
  property_count: 3
  slug: ground-station-config-id-response
- name: ConfigListItem
  property_count: 4
  slug: ground-station-config-list-item
- name: ConfigList
  property_count: 0
  slug: ground-station-config-list
- name: ConfigTypeData
  property_count: 7
  slug: ground-station-config-type-data
- name: ConnectionDetails
  property_count: 2
  slug: ground-station-connection-details
- name: ContactData
  property_count: 13
  slug: ground-station-contact-data
- name: ContactIdResponse
  property_count: 1
  slug: ground-station-contact-id-response
- name: ContactList
  property_count: 0
  slug: ground-station-contact-list
- name: ContactStatus
  property_count: 0
  slug: ground-station-contact-status
- name: CreateConfigRequest
  property_count: 3
  slug: ground-station-create-config-request
- name: CreateDataflowEndpointGroupRequest
  property_count: 4
  slug: ground-station-create-dataflow-endpoint-group-request
- name: CreateEphemerisRequest
  property_count: 8
  slug: ground-station-create-ephemeris-request
- name: CreateMissionProfileRequest
  property_count: 9
  slug: ground-station-create-mission-profile-request
- name: Criticality
  property_count: 0
  slug: ground-station-criticality
- name: CustomerEphemerisPriority
  property_count: 0
  slug: ground-station-customer-ephemeris-priority
- name: DataflowDetail
  property_count: 3
  slug: ground-station-dataflow-detail
- name: DataflowEdgeList
  property_count: 0
  slug: ground-station-dataflow-edge-list
- name: DataflowEdge
  property_count: 0
  slug: ground-station-dataflow-edge
- name: DataflowEndpointConfig
  property_count: 2
  slug: ground-station-dataflow-endpoint-config
- name: DataflowEndpointGroupArn
  property_count: 0
  slug: ground-station-dataflow-endpoint-group-arn
- name: DataflowEndpointGroupDurationInSeconds
  property_count: 0
  slug: ground-station-dataflow-endpoint-group-duration-in-seconds
- name: DataflowEndpointGroupIdResponse
  property_count: 1
  slug: ground-station-dataflow-endpoint-group-id-response
- name: DataflowEndpointGroupList
  property_count: 0
  slug: ground-station-dataflow-endpoint-group-list
- name: DataflowEndpointListItem
  property_count: 2
  slug: ground-station-dataflow-endpoint-list-item
- name: DataflowEndpointMtuInteger
  property_count: 0
  slug: ground-station-dataflow-endpoint-mtu-integer
- name: DataflowEndpoint
  property_count: 4
  slug: ground-station-dataflow-endpoint
- name: DataflowList
  property_count: 0
  slug: ground-station-dataflow-list
- name: DecodeConfig
  property_count: 1
  slug: ground-station-decode-config
- name: DeleteConfigRequest
  property_count: 0
  slug: ground-station-delete-config-request
- name: DeleteDataflowEndpointGroupRequest
  property_count: 0
  slug: ground-station-delete-dataflow-endpoint-group-request
- name: DeleteEphemerisRequest
  property_count: 0
  slug: ground-station-delete-ephemeris-request
- name: DeleteMissionProfileRequest
  property_count: 0
  slug: ground-station-delete-mission-profile-request
- name: DemodulationConfig
  property_count: 1
  slug: ground-station-demodulation-config
- name: DependencyException
  property_count: 0
  slug: ground-station-dependency-exception
- name: DescribeContactRequest
  property_count: 0
  slug: ground-station-describe-contact-request
- name: DescribeContactResponse
  property_count: 14
  slug: ground-station-describe-contact-response
- name: DescribeEphemerisRequest
  property_count: 0
  slug: ground-station-describe-ephemeris-request
- name: DescribeEphemerisResponse
  property_count: 10
  slug: ground-station-describe-ephemeris-response
- name: Destination
  property_count: 4
  slug: ground-station-destination
- name: DiscoveryData
  property_count: 3
  slug: ground-station-discovery-data
- name: Double
  property_count: 0
  slug: ground-station-double
- name: DurationInSeconds
  property_count: 0
  slug: ground-station-duration-in-seconds
- name: Eirp
  property_count: 2
  slug: ground-station-eirp
- name: EirpUnits
  property_count: 0
  slug: ground-station-eirp-units
- name: Elevation
  property_count: 2
  slug: ground-station-elevation
- name: EndpointDetailsList
  property_count: 0
  slug: ground-station-endpoint-details-list
- name: EndpointDetails
  property_count: 5
  slug: ground-station-endpoint-details
- name: EndpointStatus
  property_count: 0
  slug: ground-station-endpoint-status
- name: EphemeridesList
  property_count: 0
  slug: ground-station-ephemerides-list
- name: EphemerisData
  property_count: 2
  slug: ground-station-ephemeris-data
- name: EphemerisDescription
  property_count: 2
  slug: ground-station-ephemeris-description
- name: EphemerisIdResponse
  property_count: 1
  slug: ground-station-ephemeris-id-response
- name: EphemerisInvalidReason
  property_count: 0
  slug: ground-station-ephemeris-invalid-reason
- name: EphemerisItem
  property_count: 7
  slug: ground-station-ephemeris-item
- name: EphemerisMetaData
  property_count: 4
  slug: ground-station-ephemeris-meta-data
- name: EphemerisPriority
  property_count: 0
  slug: ground-station-ephemeris-priority
- name: EphemerisSource
  property_count: 0
  slug: ground-station-ephemeris-source
- name: EphemerisStatusList
  property_count: 0
  slug: ground-station-ephemeris-status-list
- name: EphemerisStatus
  property_count: 0
  slug: ground-station-ephemeris-status
- name: EphemerisTypeDescription
  property_count: 2
  slug: ground-station-ephemeris-type-description
- name: FrequencyBandwidth
  property_count: 2
  slug: ground-station-frequency-bandwidth
- name: Frequency
  property_count: 2
  slug: ground-station-frequency
- name: FrequencyUnits
  property_count: 0
  slug: ground-station-frequency-units
- name: GetAgentConfigurationRequest
  property_count: 0
  slug: ground-station-get-agent-configuration-request
- name: GetAgentConfigurationResponse
  property_count: 2
  slug: ground-station-get-agent-configuration-response
- name: GetConfigRequest
  property_count: 0
  slug: ground-station-get-config-request
- name: GetConfigResponse
  property_count: 6
  slug: ground-station-get-config-response
- name: GetDataflowEndpointGroupRequest
  property_count: 0
  slug: ground-station-get-dataflow-endpoint-group-request
- name: GetDataflowEndpointGroupResponse
  property_count: 6
  slug: ground-station-get-dataflow-endpoint-group-response
- name: GetMinuteUsageRequest
  property_count: 2
  slug: ground-station-get-minute-usage-request
- name: GetMinuteUsageResponse
  property_count: 5
  slug: ground-station-get-minute-usage-response
- name: GetMissionProfileRequest
  property_count: 0
  slug: ground-station-get-mission-profile-request
- name: GetMissionProfileResponse
  property_count: 12
  slug: ground-station-get-mission-profile-response
- name: GetSatelliteRequest
  property_count: 0
  slug: ground-station-get-satellite-request
- name: GetSatelliteResponse
  property_count: 5
  slug: ground-station-get-satellite-response
- name: GroundStationData
  property_count: 3
  slug: ground-station-ground-station-data
- name: GroundStationIdList
  property_count: 0
  slug: ground-station-ground-station-id-list
- name: GroundStationList
  property_count: 0
  slug: ground-station-ground-station-list
- name: GroundStationName
  property_count: 0
  slug: ground-station-ground-station-name
- name: InstanceId
  property_count: 0
  slug: ground-station-instance-id
- name: InstanceType
  property_count: 0
  slug: ground-station-instance-type
- name: IntegerRange
  property_count: 2
  slug: ground-station-integer-range
- name: Integer
  property_count: 0
  slug: ground-station-integer
- name: InvalidParameterException
  property_count: 0
  slug: ground-station-invalid-parameter-exception
- name: IpAddressList
  property_count: 0
  slug: ground-station-ip-address-list
- name: IpV4Address
  property_count: 0
  slug: ground-station-ip-v4-address
- name: JsonString
  property_count: 0
  slug: ground-station-json-string
- name: KeyAliasArn
  property_count: 0
  slug: ground-station-key-alias-arn
- name: KeyArn
  property_count: 0
  slug: ground-station-key-arn
- name: KmsKey
  property_count: 2
  slug: ground-station-kms-key
- name: ListConfigsRequest
  property_count: 0
  slug: ground-station-list-configs-request
- name: ListConfigsResponse
  property_count: 2
  slug: ground-station-list-configs-response
- name: ListContactsRequest
  property_count: 8
  slug: ground-station-list-contacts-request
- name: ListContactsResponse
  property_count: 2
  slug: ground-station-list-contacts-response
- name: ListDataflowEndpointGroupsRequest
  property_count: 0
  slug: ground-station-list-dataflow-endpoint-groups-request
- name: ListDataflowEndpointGroupsResponse
  property_count: 2
  slug: ground-station-list-dataflow-endpoint-groups-response
- name: ListEphemeridesRequest
  property_count: 4
  slug: ground-station-list-ephemerides-request
- name: ListEphemeridesResponse
  property_count: 2
  slug: ground-station-list-ephemerides-response
- name: ListGroundStationsRequest
  property_count: 0
  slug: ground-station-list-ground-stations-request
- name: ListGroundStationsResponse
  property_count: 2
  slug: ground-station-list-ground-stations-response
- name: ListMissionProfilesRequest
  property_count: 0
  slug: ground-station-list-mission-profiles-request
- name: ListMissionProfilesResponse
  property_count: 2
  slug: ground-station-list-mission-profiles-response
- name: ListSatellitesRequest
  property_count: 0
  slug: ground-station-list-satellites-request
- name: ListSatellitesResponse
  property_count: 2
  slug: ground-station-list-satellites-response
- name: ListTagsForResourceRequest
  property_count: 0
  slug: ground-station-list-tags-for-resource-request
- name: ListTagsForResourceResponse
  property_count: 1
  slug: ground-station-list-tags-for-resource-response
- name: Long
  property_count: 0
  slug: ground-station-long
- name: MissionProfileArn
  property_count: 0
  slug: ground-station-mission-profile-arn
- name: MissionProfileIdResponse
  property_count: 1
  slug: ground-station-mission-profile-id-response
- name: MissionProfileListItem
  property_count: 4
  slug: ground-station-mission-profile-list-item
- name: MissionProfileList
  property_count: 0
  slug: ground-station-mission-profile-list
- name: Month
  property_count: 0
  slug: ground-station-month
- name: noradSatelliteID
  property_count: 0
  slug: ground-station-norad-satellite-id
- name: OEMEphemeris
  property_count: 2
  slug: ground-station-oem-ephemeris
- name: PaginationMaxResults
  property_count: 0
  slug: ground-station-pagination-max-results
- name: PaginationToken
  property_count: 0
  slug: ground-station-pagination-token
- name: Polarization
  property_count: 0
  slug: ground-station-polarization
- name: PositiveDurationInSeconds
  property_count: 0
  slug: ground-station-positive-duration-in-seconds
- name: RangedConnectionDetailsMtuInteger
  property_count: 0
  slug: ground-station-ranged-connection-details-mtu-integer
- name: RangedConnectionDetails
  property_count: 2
  slug: ground-station-ranged-connection-details
- name: RangedSocketAddress
  property_count: 2
  slug: ground-station-ranged-socket-address
- name: RegisterAgentRequest
  property_count: 2
  slug: ground-station-register-agent-request
- name: RegisterAgentResponse
  property_count: 1
  slug: ground-station-register-agent-response
- name: ReserveContactRequest
  property_count: 6
  slug: ground-station-reserve-contact-request
- name: ResourceLimitExceededException
  property_count: 0
  slug: ground-station-resource-limit-exceeded-exception
- name: ResourceNotFoundException
  property_count: 0
  slug: ground-station-resource-not-found-exception
- name: RoleArn
  property_count: 0
  slug: ground-station-role-arn
- name: S3BucketName
  property_count: 0
  slug: ground-station-s3-bucket-name
- name: S3KeyPrefix
  property_count: 0
  slug: ground-station-s3-key-prefix
- name: S3ObjectKey
  property_count: 0
  slug: ground-station-s3-object-key
- name: S3Object
  property_count: 3
  slug: ground-station-s3-object
- name: S3RecordingConfig
  property_count: 3
  slug: ground-station-s3-recording-config
- name: S3RecordingDetails
  property_count: 2
  slug: ground-station-s3-recording-details
- name: S3VersionId
  property_count: 0
  slug: ground-station-s3-version-id
- name: SafeName
  property_count: 0
  slug: ground-station-safe-name
- name: satelliteArn
  property_count: 0
  slug: ground-station-satellite-arn
- name: SatelliteListItem
  property_count: 5
  slug: ground-station-satellite-list-item
- name: SatelliteList
  property_count: 0
  slug: ground-station-satellite-list
- name: SecurityDetails
  property_count: 3
  slug: ground-station-security-details
- name: SecurityGroupIdList
  property_count: 0
  slug: ground-station-security-group-id-list
- name: SignatureMap
  property_count: 0
  slug: ground-station-signature-map
- name: SocketAddress
  property_count: 2
  slug: ground-station-socket-address
- name: Source
  property_count: 4
  slug: ground-station-source
- name: SpectrumConfig
  property_count: 3
  slug: ground-station-spectrum-config
- name: StatusList
  property_count: 0
  slug: ground-station-status-list
- name: String
  property_count: 0
  slug: ground-station-string
- name: SubnetList
  property_count: 0
  slug: ground-station-subnet-list
- name: TagKeys
  property_count: 0
  slug: ground-station-tag-keys
- name: TagResourceRequest
  property_count: 1
  slug: ground-station-tag-resource-request
- name: TagResourceResponse
  property_count: 0
  slug: ground-station-tag-resource-response
- name: TagsMap
  property_count: 0
  slug: ground-station-tags-map
- name: TimeRange
  property_count: 2
  slug: ground-station-time-range
- name: Timestamp
  property_count: 0
  slug: ground-station-timestamp
- name: TLEDataList
  property_count: 0
  slug: ground-station-tle-data-list
- name: TLEData
  property_count: 3
  slug: ground-station-tle-data
- name: TLEEphemeris
  property_count: 2
  slug: ground-station-tle-ephemeris
- name: TleLineOne
  property_count: 0
  slug: ground-station-tle-line-one
- name: TleLineTwo
  property_count: 0
  slug: ground-station-tle-line-two
- name: TrackingConfig
  property_count: 1
  slug: ground-station-tracking-config
- name: UnboundedString
  property_count: 0
  slug: ground-station-unbounded-string
- name: UntagResourceRequest
  property_count: 0
  slug: ground-station-untag-resource-request
- name: UntagResourceResponse
  property_count: 0
  slug: ground-station-untag-resource-response
- name: UpdateAgentStatusRequest
  property_count: 3
  slug: ground-station-update-agent-status-request
- name: UpdateAgentStatusResponse
  property_count: 1
  slug: ground-station-update-agent-status-response
- name: UpdateConfigRequest
  property_count: 2
  slug: ground-station-update-config-request
- name: UpdateEphemerisRequest
  property_count: 3
  slug: ground-station-update-ephemeris-request
- name: UpdateMissionProfileRequest
  property_count: 8
  slug: ground-station-update-mission-profile-request
- name: UplinkEchoConfig
  property_count: 2
  slug: ground-station-uplink-echo-config
- name: UplinkSpectrumConfig
  property_count: 2
  slug: ground-station-uplink-spectrum-config
- name: Uuid
  property_count: 0
  slug: ground-station-uuid
- name: VersionStringList
  property_count: 0
  slug: ground-station-version-string-list
- name: VersionString
  property_count: 0
  slug: ground-station-version-string
- name: Year
  property_count: 0
  slug: ground-station-year
json_structures:
- name: Ground Station Agent Cpu Cores List Structure
  property_count: 0
  slug: ground-station-agent-cpu-cores-list-structure
- name: Ground Station Agent Details Structure
  property_count: 6
  slug: ground-station-agent-details-structure
- name: Ground Station Agent Status Structure
  property_count: 0
  slug: ground-station-agent-status-structure
- name: Ground Station Aggregate Status Structure
  property_count: 2
  slug: ground-station-aggregate-status-structure
- name: Ground Station Angle Units Structure
  property_count: 0
  slug: ground-station-angle-units-structure
- name: Ground Station Antenna Demod Decode Details Structure
  property_count: 1
  slug: ground-station-antenna-demod-decode-details-structure
- name: Ground Station Antenna Downlink Config Structure
  property_count: 1
  slug: ground-station-antenna-downlink-config-structure
- name: Ground Station Antenna Downlink Demod Decode Config Structure
  property_count: 3
  slug: ground-station-antenna-downlink-demod-decode-config-structure
- name: Ground Station Antenna Uplink Config Structure
  property_count: 3
  slug: ground-station-antenna-uplink-config-structure
- name: Ground Station Any Arn Structure
  property_count: 0
  slug: ground-station-any-arn-structure
- name: Ground Station Audit Results Structure
  property_count: 0
  slug: ground-station-audit-results-structure
- name: Ground Station Aws Ground Station Agent Endpoint Structure
  property_count: 5
  slug: ground-station-aws-ground-station-agent-endpoint-structure
- name: Ground Station Aws Region Structure
  property_count: 0
  slug: ground-station-aws-region-structure
- name: Ground Station Bandwidth Units Structure
  property_count: 0
  slug: ground-station-bandwidth-units-structure
- name: Ground Station Boolean Structure
  property_count: 0
  slug: ground-station-boolean-structure
- name: Ground Station Bucket Arn Structure
  property_count: 0
  slug: ground-station-bucket-arn-structure
- name: Ground Station Cancel Contact Request Structure
  property_count: 0
  slug: ground-station-cancel-contact-request-structure
- name: Ground Station Capability Arn List Structure
  property_count: 0
  slug: ground-station-capability-arn-list-structure
- name: Ground Station Capability Arn Structure
  property_count: 0
  slug: ground-station-capability-arn-structure
- name: Ground Station Capability Health Reason List Structure
  property_count: 0
  slug: ground-station-capability-health-reason-list-structure
- name: Ground Station Capability Health Reason Structure
  property_count: 0
  slug: ground-station-capability-health-reason-structure
- name: Ground Station Capability Health Structure
  property_count: 0
  slug: ground-station-capability-health-structure
- name: Ground Station Component Status Data Structure
  property_count: 7
  slug: ground-station-component-status-data-structure
- name: Ground Station Component Status List Structure
  property_count: 0
  slug: ground-station-component-status-list-structure
- name: Ground Station Component Type String Structure
  property_count: 0
  slug: ground-station-component-type-string-structure
- name: Ground Station Component Version List Structure
  property_count: 0
  slug: ground-station-component-version-list-structure
- name: Ground Station Component Version Structure
  property_count: 2
  slug: ground-station-component-version-structure
- name: Ground Station Config Arn Structure
  property_count: 0
  slug: ground-station-config-arn-structure
- name: Ground Station Config Capability Type Structure
  property_count: 0
  slug: ground-station-config-capability-type-structure
- name: Ground Station Config Details Structure
  property_count: 3
  slug: ground-station-config-details-structure
- name: Ground Station Config Id Response Structure
  property_count: 3
  slug: ground-station-config-id-response-structure
- name: Ground Station Config List Item Structure
  property_count: 4
  slug: ground-station-config-list-item-structure
- name: Ground Station Config List Structure
  property_count: 0
  slug: ground-station-config-list-structure
- name: Ground Station Config Type Data Structure
  property_count: 7
  slug: ground-station-config-type-data-structure
- name: Ground Station Connection Details Structure
  property_count: 2
  slug: ground-station-connection-details-structure
- name: Ground Station Contact Data Structure
  property_count: 13
  slug: ground-station-contact-data-structure
- name: Ground Station Contact Id Response Structure
  property_count: 1
  slug: ground-station-contact-id-response-structure
- name: Ground Station Contact List Structure
  property_count: 0
  slug: ground-station-contact-list-structure
- name: Ground Station Contact Status Structure
  property_count: 0
  slug: ground-station-contact-status-structure
- name: Ground Station Create Config Request Structure
  property_count: 3
  slug: ground-station-create-config-request-structure
- name: Ground Station Create Dataflow Endpoint Group Request Structure
  property_count: 4
  slug: ground-station-create-dataflow-endpoint-group-request-structure
- name: Ground Station Create Ephemeris Request Structure
  property_count: 8
  slug: ground-station-create-ephemeris-request-structure
- name: Ground Station Create Mission Profile Request Structure
  property_count: 9
  slug: ground-station-create-mission-profile-request-structure
- name: Ground Station Criticality Structure
  property_count: 0
  slug: ground-station-criticality-structure
- name: Ground Station Customer Ephemeris Priority Structure
  property_count: 0
  slug: ground-station-customer-ephemeris-priority-structure
- name: Ground Station Dataflow Detail Structure
  property_count: 3
  slug: ground-station-dataflow-detail-structure
- name: Ground Station Dataflow Edge List Structure
  property_count: 0
  slug: ground-station-dataflow-edge-list-structure
- name: Ground Station Dataflow Edge Structure
  property_count: 0
  slug: ground-station-dataflow-edge-structure
- name: Ground Station Dataflow Endpoint Config Structure
  property_count: 2
  slug: ground-station-dataflow-endpoint-config-structure
- name: Ground Station Dataflow Endpoint Group Arn Structure
  property_count: 0
  slug: ground-station-dataflow-endpoint-group-arn-structure
- name: Ground Station Dataflow Endpoint Group Duration In Seconds Structure
  property_count: 0
  slug: ground-station-dataflow-endpoint-group-duration-in-seconds-structure
- name: Ground Station Dataflow Endpoint Group Id Response Structure
  property_count: 1
  slug: ground-station-dataflow-endpoint-group-id-response-structure
- name: Ground Station Dataflow Endpoint Group List Structure
  property_count: 0
  slug: ground-station-dataflow-endpoint-group-list-structure
- name: Ground Station Dataflow Endpoint List Item Structure
  property_count: 2
  slug: ground-station-dataflow-endpoint-list-item-structure
- name: Ground Station Dataflow Endpoint Mtu Integer Structure
  property_count: 0
  slug: ground-station-dataflow-endpoint-mtu-integer-structure
- name: Ground Station Dataflow Endpoint Structure
  property_count: 4
  slug: ground-station-dataflow-endpoint-structure
- name: Ground Station Dataflow List Structure
  property_count: 0
  slug: ground-station-dataflow-list-structure
- name: Ground Station Decode Config Structure
  property_count: 1
  slug: ground-station-decode-config-structure
- name: Ground Station Delete Config Request Structure
  property_count: 0
  slug: ground-station-delete-config-request-structure
- name: Ground Station Delete Dataflow Endpoint Group Request Structure
  property_count: 0
  slug: ground-station-delete-dataflow-endpoint-group-request-structure
- name: Ground Station Delete Ephemeris Request Structure
  property_count: 0
  slug: ground-station-delete-ephemeris-request-structure
- name: Ground Station Delete Mission Profile Request Structure
  property_count: 0
  slug: ground-station-delete-mission-profile-request-structure
- name: Ground Station Demodulation Config Structure
  property_count: 1
  slug: ground-station-demodulation-config-structure
- name: Ground Station Dependency Exception Structure
  property_count: 0
  slug: ground-station-dependency-exception-structure
- name: Ground Station Describe Contact Request Structure
  property_count: 0
  slug: ground-station-describe-contact-request-structure
- name: Ground Station Describe Contact Response Structure
  property_count: 14
  slug: ground-station-describe-contact-response-structure
- name: Ground Station Describe Ephemeris Request Structure
  property_count: 0
  slug: ground-station-describe-ephemeris-request-structure
- name: Ground Station Describe Ephemeris Response Structure
  property_count: 10
  slug: ground-station-describe-ephemeris-response-structure
- name: Ground Station Destination Structure
  property_count: 4
  slug: ground-station-destination-structure
- name: Ground Station Discovery Data Structure
  property_count: 3
  slug: ground-station-discovery-data-structure
- name: Ground Station Double Structure
  property_count: 0
  slug: ground-station-double-structure
- name: Ground Station Duration In Seconds Structure
  property_count: 0
  slug: ground-station-duration-in-seconds-structure
- name: Ground Station Eirp Structure
  property_count: 2
  slug: ground-station-eirp-structure
- name: Ground Station Eirp Units Structure
  property_count: 0
  slug: ground-station-eirp-units-structure
- name: Ground Station Elevation Structure
  property_count: 2
  slug: ground-station-elevation-structure
- name: Ground Station Endpoint Details List Structure
  property_count: 0
  slug: ground-station-endpoint-details-list-structure
- name: Ground Station Endpoint Details Structure
  property_count: 5
  slug: ground-station-endpoint-details-structure
- name: Ground Station Endpoint Status Structure
  property_count: 0
  slug: ground-station-endpoint-status-structure
- name: Ground Station Ephemerides List Structure
  property_count: 0
  slug: ground-station-ephemerides-list-structure
- name: Ground Station Ephemeris Data Structure
  property_count: 2
  slug: ground-station-ephemeris-data-structure
- name: Ground Station Ephemeris Description Structure
  property_count: 2
  slug: ground-station-ephemeris-description-structure
- name: Ground Station Ephemeris Id Response Structure
  property_count: 1
  slug: ground-station-ephemeris-id-response-structure
- name: Ground Station Ephemeris Invalid Reason Structure
  property_count: 0
  slug: ground-station-ephemeris-invalid-reason-structure
- name: Ground Station Ephemeris Item Structure
  property_count: 7
  slug: ground-station-ephemeris-item-structure
- name: Ground Station Ephemeris Meta Data Structure
  property_count: 4
  slug: ground-station-ephemeris-meta-data-structure
- name: Ground Station Ephemeris Priority Structure
  property_count: 0
  slug: ground-station-ephemeris-priority-structure
- name: Ground Station Ephemeris Source Structure
  property_count: 0
  slug: ground-station-ephemeris-source-structure
- name: Ground Station Ephemeris Status List Structure
  property_count: 0
  slug: ground-station-ephemeris-status-list-structure
- name: Ground Station Ephemeris Status Structure
  property_count: 0
  slug: ground-station-ephemeris-status-structure
- name: Ground Station Ephemeris Type Description Structure
  property_count: 2
  slug: ground-station-ephemeris-type-description-structure
- name: Ground Station Frequency Bandwidth Structure
  property_count: 2
  slug: ground-station-frequency-bandwidth-structure
- name: Ground Station Frequency Structure
  property_count: 2
  slug: ground-station-frequency-structure
- name: Ground Station Frequency Units Structure
  property_count: 0
  slug: ground-station-frequency-units-structure
- name: Ground Station Get Agent Configuration Request Structure
  property_count: 0
  slug: ground-station-get-agent-configuration-request-structure
- name: Ground Station Get Agent Configuration Response Structure
  property_count: 2
  slug: ground-station-get-agent-configuration-response-structure
- name: Ground Station Get Config Request Structure
  property_count: 0
  slug: ground-station-get-config-request-structure
- name: Ground Station Get Config Response Structure
  property_count: 6
  slug: ground-station-get-config-response-structure
- name: Ground Station Get Dataflow Endpoint Group Request Structure
  property_count: 0
  slug: ground-station-get-dataflow-endpoint-group-request-structure
- name: Ground Station Get Dataflow Endpoint Group Response Structure
  property_count: 6
  slug: ground-station-get-dataflow-endpoint-group-response-structure
- name: Ground Station Get Minute Usage Request Structure
  property_count: 2
  slug: ground-station-get-minute-usage-request-structure
- name: Ground Station Get Minute Usage Response Structure
  property_count: 5
  slug: ground-station-get-minute-usage-response-structure
- name: Ground Station Get Mission Profile Request Structure
  property_count: 0
  slug: ground-station-get-mission-profile-request-structure
- name: Ground Station Get Mission Profile Response Structure
  property_count: 12
  slug: ground-station-get-mission-profile-response-structure
- name: Ground Station Get Satellite Request Structure
  property_count: 0
  slug: ground-station-get-satellite-request-structure
- name: Ground Station Get Satellite Response Structure
  property_count: 5
  slug: ground-station-get-satellite-response-structure
- name: Ground Station Ground Station Data Structure
  property_count: 3
  slug: ground-station-ground-station-data-structure
- name: Ground Station Ground Station Id List Structure
  property_count: 0
  slug: ground-station-ground-station-id-list-structure
- name: Ground Station Ground Station List Structure
  property_count: 0
  slug: ground-station-ground-station-list-structure
- name: Ground Station Ground Station Name Structure
  property_count: 0
  slug: ground-station-ground-station-name-structure
- name: Ground Station Instance Id Structure
  property_count: 0
  slug: ground-station-instance-id-structure
- name: Ground Station Instance Type Structure
  property_count: 0
  slug: ground-station-instance-type-structure
- name: Ground Station Integer Range Structure
  property_count: 2
  slug: ground-station-integer-range-structure
- name: Ground Station Integer Structure
  property_count: 0
  slug: ground-station-integer-structure
- name: Ground Station Invalid Parameter Exception Structure
  property_count: 0
  slug: ground-station-invalid-parameter-exception-structure
- name: Ground Station Ip Address List Structure
  property_count: 0
  slug: ground-station-ip-address-list-structure
- name: Ground Station Ip V4 Address Structure
  property_count: 0
  slug: ground-station-ip-v4-address-structure
- name: Ground Station Json String Structure
  property_count: 0
  slug: ground-station-json-string-structure
- name: Ground Station Key Alias Arn Structure
  property_count: 0
  slug: ground-station-key-alias-arn-structure
- name: Ground Station Key Arn Structure
  property_count: 0
  slug: ground-station-key-arn-structure
- name: Ground Station Kms Key Structure
  property_count: 2
  slug: ground-station-kms-key-structure
- name: Ground Station List Configs Request Structure
  property_count: 0
  slug: ground-station-list-configs-request-structure
- name: Ground Station List Configs Response Structure
  property_count: 2
  slug: ground-station-list-configs-response-structure
- name: Ground Station List Contacts Request Structure
  property_count: 8
  slug: ground-station-list-contacts-request-structure
- name: Ground Station List Contacts Response Structure
  property_count: 2
  slug: ground-station-list-contacts-response-structure
- name: Ground Station List Dataflow Endpoint Groups Request Structure
  property_count: 0
  slug: ground-station-list-dataflow-endpoint-groups-request-structure
- name: Ground Station List Dataflow Endpoint Groups Response Structure
  property_count: 2
  slug: ground-station-list-dataflow-endpoint-groups-response-structure
- name: Ground Station List Ephemerides Request Structure
  property_count: 4
  slug: ground-station-list-ephemerides-request-structure
- name: Ground Station List Ephemerides Response Structure
  property_count: 2
  slug: ground-station-list-ephemerides-response-structure
- name: Ground Station List Ground Stations Request Structure
  property_count: 0
  slug: ground-station-list-ground-stations-request-structure
- name: Ground Station List Ground Stations Response Structure
  property_count: 2
  slug: ground-station-list-ground-stations-response-structure
- name: Ground Station List Mission Profiles Request Structure
  property_count: 0
  slug: ground-station-list-mission-profiles-request-structure
- name: Ground Station List Mission Profiles Response Structure
  property_count: 2
  slug: ground-station-list-mission-profiles-response-structure
- name: Ground Station List Satellites Request Structure
  property_count: 0
  slug: ground-station-list-satellites-request-structure
- name: Ground Station List Satellites Response Structure
  property_count: 2
  slug: ground-station-list-satellites-response-structure
- name: Ground Station List Tags For Resource Request Structure
  property_count: 0
  slug: ground-station-list-tags-for-resource-request-structure
- name: Ground Station List Tags For Resource Response Structure
  property_count: 1
  slug: ground-station-list-tags-for-resource-response-structure
- name: Ground Station Long Structure
  property_count: 0
  slug: ground-station-long-structure
- name: Ground Station Mission Profile Arn Structure
  property_count: 0
  slug: ground-station-mission-profile-arn-structure
- name: Ground Station Mission Profile Id Response Structure
  property_count: 1
  slug: ground-station-mission-profile-id-response-structure
- name: Ground Station Mission Profile List Item Structure
  property_count: 4
  slug: ground-station-mission-profile-list-item-structure
- name: Ground Station Mission Profile List Structure
  property_count: 0
  slug: ground-station-mission-profile-list-structure
- name: Ground Station Month Structure
  property_count: 0
  slug: ground-station-month-structure
- name: Ground Station Norad Satellite Id Structure
  property_count: 0
  slug: ground-station-norad-satellite-id-structure
- name: Ground Station Oem Ephemeris Structure
  property_count: 2
  slug: ground-station-oem-ephemeris-structure
- name: Ground Station Pagination Max Results Structure
  property_count: 0
  slug: ground-station-pagination-max-results-structure
- name: Ground Station Pagination Token Structure
  property_count: 0
  slug: ground-station-pagination-token-structure
- name: Ground Station Polarization Structure
  property_count: 0
  slug: ground-station-polarization-structure
- name: Ground Station Positive Duration In Seconds Structure
  property_count: 0
  slug: ground-station-positive-duration-in-seconds-structure
- name: Ground Station Ranged Connection Details Mtu Integer Structure
  property_count: 0
  slug: ground-station-ranged-connection-details-mtu-integer-structure
- name: Ground Station Ranged Connection Details Structure
  property_count: 2
  slug: ground-station-ranged-connection-details-structure
- name: Ground Station Ranged Socket Address Structure
  property_count: 2
  slug: ground-station-ranged-socket-address-structure
- name: Ground Station Register Agent Request Structure
  property_count: 2
  slug: ground-station-register-agent-request-structure
- name: Ground Station Register Agent Response Structure
  property_count: 1
  slug: ground-station-register-agent-response-structure
- name: Ground Station Reserve Contact Request Structure
  property_count: 6
  slug: ground-station-reserve-contact-request-structure
- name: Ground Station Resource Limit Exceeded Exception Structure
  property_count: 0
  slug: ground-station-resource-limit-exceeded-exception-structure
- name: Ground Station Resource Not Found Exception Structure
  property_count: 0
  slug: ground-station-resource-not-found-exception-structure
- name: Ground Station Role Arn Structure
  property_count: 0
  slug: ground-station-role-arn-structure
- name: Ground Station S3 Bucket Name Structure
  property_count: 0
  slug: ground-station-s3-bucket-name-structure
- name: Ground Station S3 Key Prefix Structure
  property_count: 0
  slug: ground-station-s3-key-prefix-structure
- name: Ground Station S3 Object Key Structure
  property_count: 0
  slug: ground-station-s3-object-key-structure
- name: Ground Station S3 Object Structure
  property_count: 3
  slug: ground-station-s3-object-structure
- name: Ground Station S3 Recording Config Structure
  property_count: 3
  slug: ground-station-s3-recording-config-structure
- name: Ground Station S3 Recording Details Structure
  property_count: 2
  slug: ground-station-s3-recording-details-structure
- name: Ground Station S3 Version Id Structure
  property_count: 0
  slug: ground-station-s3-version-id-structure
- name: Ground Station Safe Name Structure
  property_count: 0
  slug: ground-station-safe-name-structure
- name: Ground Station Satellite Arn Structure
  property_count: 0
  slug: ground-station-satellite-arn-structure
- name: Ground Station Satellite List Item Structure
  property_count: 5
  slug: ground-station-satellite-list-item-structure
- name: Ground Station Satellite List Structure
  property_count: 0
  slug: ground-station-satellite-list-structure
- name: Ground Station Security Details Structure
  property_count: 3
  slug: ground-station-security-details-structure
- name: Ground Station Security Group Id List Structure
  property_count: 0
  slug: ground-station-security-group-id-list-structure
- name: Ground Station Signature Map Structure
  property_count: 0
  slug: ground-station-signature-map-structure
- name: Ground Station Socket Address Structure
  property_count: 2
  slug: ground-station-socket-address-structure
- name: Ground Station Source Structure
  property_count: 4
  slug: ground-station-source-structure
- name: Ground Station Spectrum Config Structure
  property_count: 3
  slug: ground-station-spectrum-config-structure
- name: Ground Station Status List Structure
  property_count: 0
  slug: ground-station-status-list-structure
- name: Ground Station String Structure
  property_count: 0
  slug: ground-station-string-structure
- name: Ground Station Subnet List Structure
  property_count: 0
  slug: ground-station-subnet-list-structure
- name: Ground Station Tag Keys Structure
  property_count: 0
  slug: ground-station-tag-keys-structure
- name: Ground Station Tag Resource Request Structure
  property_count: 1
  slug: ground-station-tag-resource-request-structure
- name: Ground Station Tag Resource Response Structure
  property_count: 0
  slug: ground-station-tag-resource-response-structure
- name: Ground Station Tags Map Structure
  property_count: 0
  slug: ground-station-tags-map-structure
- name: Ground Station Time Range Structure
  property_count: 2
  slug: ground-station-time-range-structure
- name: Ground Station Timestamp Structure
  property_count: 0
  slug: ground-station-timestamp-structure
- name: Ground Station Tle Data List Structure
  property_count: 0
  slug: ground-station-tle-data-list-structure
- name: Ground Station Tle Data Structure
  property_count: 3
  slug: ground-station-tle-data-structure
- name: Ground Station Tle Ephemeris Structure
  property_count: 2
  slug: ground-station-tle-ephemeris-structure
- name: Ground Station Tle Line One Structure
  property_count: 0
  slug: ground-station-tle-line-one-structure
- name: Ground Station Tle Line Two Structure
  property_count: 0
  slug: ground-station-tle-line-two-structure
- name: Ground Station Tracking Config Structure
  property_count: 1
  slug: ground-station-tracking-config-structure
- name: Ground Station Unbounded String Structure
  property_count: 0
  slug: ground-station-unbounded-string-structure
- name: Ground Station Untag Resource Request Structure
  property_count: 0
  slug: ground-station-untag-resource-request-structure
- name: Ground Station Untag Resource Response Structure
  property_count: 0
  slug: ground-station-untag-resource-response-structure
- name: Ground Station Update Agent Status Request Structure
  property_count: 3
  slug: ground-station-update-agent-status-request-structure
- name: Ground Station Update Agent Status Response Structure
  property_count: 1
  slug: ground-station-update-agent-status-response-structure
- name: Ground Station Update Config Request Structure
  property_count: 2
  slug: ground-station-update-config-request-structure
- name: Ground Station Update Ephemeris Request Structure
  property_count: 3
  slug: ground-station-update-ephemeris-request-structure
- name: Ground Station Update Mission Profile Request Structure
  property_count: 8
  slug: ground-station-update-mission-profile-request-structure
- name: Ground Station Uplink Echo Config Structure
  property_count: 2
  slug: ground-station-uplink-echo-config-structure
- name: Ground Station Uplink Spectrum Config Structure
  property_count: 2
  slug: ground-station-uplink-spectrum-config-structure
- name: Ground Station Uuid Structure
  property_count: 0
  slug: ground-station-uuid-structure
- name: Ground Station Version String List Structure
  property_count: 0
  slug: ground-station-version-string-list-structure
- name: Ground Station Version String Structure
  property_count: 0
  slug: ground-station-version-string-structure
- name: Ground Station Year Structure
  property_count: 0
  slug: ground-station-year-structure
jsonld:
- class_count: 114
  name: Amazon Ground Station Context
  property_count: 155
  slug: amazon-ground-station-context
layout: provider
modified: '2026-05-19'
name: Amazon Ground Station
nav: Providers
network: true
overview: 'Amazon Ground Station publishes 12 APIs on the [APIs.io](https://apis.io/) network, including Agent API, Config API, Contact API, and 9 more. Tagged areas include Data Processing, IoT, Satellite Communications, and Space Technology.


  The Amazon Ground Station catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Amazon Ground Station''s developer surface includes authentication, developer portal, documentation, support, engineering blog, developer console, signup flow, and 11 more developer resources.'
plans:
- name: Amazon Ground Station Plans Pricing
  plan_count: 3
  slug: amazon-ground-station-plans-pricing
random_paper: 53
rate_limits:
- limit_count: 5
  name: Amazon Ground Station Rate Limits
  slug: amazon-ground-station-rate-limits
rules:
- name: Amazon Ground Station API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: amazon-ground-station-jsonschema-spectral-rules
- name: Amazon Ground Station API Rules
  rule_count: 15
  severity_counts:
    error: 5
    hint: 0
    info: 2
    warn: 8
  slug: amazon-ground-station-spectral-rules
score:
  band: strong
  composite: 67.2
  delta: 0.0
  facets:
    commercial_clarity: 68.4
    contract_quality: 77.0
    developer_ergonomics: 41.3
    discoverability: 87.5
    governance: 86.8
    operational_transparency: 52.6
  previous_composite: 67.2
  schema_version: 0.5
  scored_at: '2026-07-27'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/amazon-ground-station/refs/heads/main/screenshots/amazon-ground-station-2026-06-20T171659.png
security:
- kind: authentication
  name: Amazon Ground Station Authentication
  slug: amazon-ground-station-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Amazon Ground Station Domain Security
  slug: amazon-ground-station-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Amazon Ground Station Vulnerability Disclosure
  slug: amazon-ground-station-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Amazon Ground Station Trust Center
  slug: amazon-ground-station-trust-center
  summary_line: PCI DSS, HIPAA, FedRAMP, GDPR, FIPS 140
slug: amazon-ground-station
tags:
- Data Processing
- IoT
- Satellite Communications
- Space Technology
use_cases:
- description: Collect and process satellite imagery for environmental monitoring, agriculture, and urban planning.
  name: Earth Observation
- description: Receive data from weather satellites for meteorological analysis and forecasting.
  name: Weather Forecasting
- description: Track ship positions and maritime assets using satellite AIS data.
  name: Maritime Tracking
- description: Use geostationary satellites for communications relay applications.
  name: Communications Relay
- description: Support space-based scientific missions with managed data collection and downlink.
  name: Scientific Research
website: https://aws.amazon.com/ground-station/
---
