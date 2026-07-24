---
access_model:
  confidence: high
  label: Enterprise · Self-serve signup
  onboarding: self-serve
  pricing: enterprise
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_skills: false
    agentic_access: true
    asyncapi_events: true
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
  score: 53.8
  scored_at: '2026-07-23'
agentic_access:
- acting_count: 24
  human_in_the_loop: 1
  name: Cisco Voice Portal Agentic Access
  operation_count: 68
  slug: cisco-voice-portal-agentic-access
  summary_line: 68 operations · 24 acting · 1 human-in-the-loop
api_count: 24
apis:
- description: Event-driven interface for consuming real-time CVP call lifecycle events, system alerts, device status changes, and operational notifications via JMS messaging and syslog.
  name: Cisco Voice Portal Call Events API
  slug: cisco-voice-portal-call-events-api
- description: Configure VXML application runtime settings
  name: Cisco Voice Portal Application Configuration API
  slug: cisco-voice-portal-application-configuration-api
- description: Deploy and manage VXML and Call Studio applications
  name: Cisco Voice Portal Application Management API
  slug: cisco-voice-portal-application-management-api
- description: Access and query call detail records
  name: Cisco Voice Portal Call Detail Records API
  slug: cisco-voice-portal-call-detail-records-api
- description: Manage and control active calls
  name: Cisco Voice Portal Call Management API
  slug: cisco-voice-portal-call-management-api
- description: Call routing lookup and testing
  name: Cisco Voice Portal Call Routing API
  slug: cisco-voice-portal-call-routing-api
- description: Configure and manage CVP Call Servers
  name: Cisco Voice Portal Call Server Management API
  slug: cisco-voice-portal-call-server-management-api
- description: Deploy configuration to managed devices
  name: Cisco Voice Portal Deployment API
  slug: cisco-voice-portal-deployment-api
- description: Manage CVP devices (Call Servers, VXML Servers, Reporting Servers)
  name: Cisco Voice Portal Device Management API
  slug: cisco-voice-portal-device-management-api
- description: Manage call routing dialed number patterns
  name: Cisco Voice Portal Dialed Number Patterns API
  slug: cisco-voice-portal-dialed-number-patterns-api
- description: Manage speech recognition grammar files
  name: Cisco Voice Portal Grammar Management API
  slug: cisco-voice-portal-grammar-management-api
- description: Call Server health and connectivity status
  name: Cisco Voice Portal Health API
  slug: cisco-voice-portal-health-api
- description: Aggregated historical reporting data
  name: Cisco Voice Portal Historical Reports API
  slug: cisco-voice-portal-historical-reports-api
- description: Manage audio media files and prompts
  name: Cisco Voice Portal Media Management API
  slug: cisco-voice-portal-media-management-api
- description: Manage built-in CVP micro-applications
  name: Cisco Voice Portal Micro-Applications API
  slug: cisco-voice-portal-micro-applications-api
- description: Current call processing statistics
  name: Cisco Voice Portal Real-Time Statistics API
  slug: cisco-voice-portal-real-time-statistics-api
- description: Execute pre-defined report templates
  name: Cisco Voice Portal Report Templates API
  slug: cisco-voice-portal-report-templates-api
- description: VXML Server status and monitoring
  name: Cisco Voice Portal Server Status API
  slug: cisco-voice-portal-server-status-api
- description: Monitor active VXML call sessions
  name: Cisco Voice Portal Session Monitoring API
  slug: cisco-voice-portal-session-monitoring-api
- description: Configure SIP server groups and settings
  name: Cisco Voice Portal SIP Configuration API
  slug: cisco-voice-portal-sip-configuration-api
- description: Monitor SIP session details
  name: Cisco Voice Portal SIP Sessions API
  slug: cisco-voice-portal-sip-sessions-api
- description: Global system settings and licensing
  name: Cisco Voice Portal System Configuration API
  slug: cisco-voice-portal-system-configuration-api
- description: Manage OAMP user accounts
  name: Cisco Voice Portal User Management API
  slug: cisco-voice-portal-user-management-api
- description: Configure and manage CVP VXML Servers
  name: Cisco Voice Portal VXML Server Management API
  slug: cisco-voice-portal-vxml-server-management-api
artifact_total: 218
asyncapis:
- description: The Cisco Unified Customer Voice Portal (CVP) generates real-time events during call processing that can be consumed for monitoring, analytics, and integration purposes. CVP publishes call lifecycle e
  name: Cisco Voice Portal Call Events API
  slug: cisco-voice-portal-call-events-asyncapi
collections:
- collection_type: open
  name: Cisco Voice Portal Administration API
  slug: open-cisco-voice-portal-administration
- collection_type: open
  name: Cisco Voice Portal Call Control API
  slug: open-cisco-voice-portal-call-control
- collection_type: open
  name: Cisco Voice Portal Reporting API
  slug: open-cisco-voice-portal-reporting
- collection_type: open
  name: Cisco Voice Portal VXML Services API
  slug: open-cisco-voice-portal-vxml-services
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/cisco-voice-portal-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/cisco-voice-portal-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/cisco-voice-portal-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/cisco-voice-portal-authentication.yml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.cisco.com/
- group: auth
  title: ''
  type: Authentication
  url: https://developer.cisco.com/docs/voice-portal/#!authentication
- group: operate
  title: ''
  type: StatusPage
  url: https://status.cisco.com/
- group: operate
  title: ''
  type: Support
  url: https://www.cisco.com/c/en/us/support/customer-collaboration/voice-portal/tsd-products-support-series-home.html
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.cisco.com/c/en/us/about/legal/terms-conditions.html
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.cisco.com/c/en/us/about/legal/privacy-full.html
- group: docs
  title: ''
  type: Documentation
  url: https://www.cisco.com/c/en/us/support/customer-collaboration/voice-portal/tsd-products-support-series-home.html
- group: start
  title: ''
  type: GettingStarted
  url: https://developer.cisco.com/site/devnet/
- group: company
  title: ''
  type: Blog
  url: https://blogs.cisco.com/developer
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/CiscoDevNet
- group: start
  title: ''
  type: Signup
  url: https://developer.cisco.com/join/devnet
- group: operate
  title: ''
  type: ReleaseNotes
  url: https://www.cisco.com/c/en/us/support/customer-collaboration/voice-portal/products-release-notes-list.html
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/cisco-voice-portal-call-detail-record.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/cisco-voice-portal-device.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/cisco-voice-portal-application.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/cisco-voice-portal-dialed-number-pattern.json
created: '2024'
description: Cisco Voice Portal (CVP) is an enterprise-class Voice XML (VXML) browser and call control platform that enables self-service applications for voice, video, and multimodal interactions.
examples:
- key_count: 8
  name: Cisco Voice Portal Administration Application Example
  slug: cisco-voice-portal-administration-application-example
- key_count: 4
  name: Cisco Voice Portal Administration Call Server Config Example
  slug: cisco-voice-portal-administration-call-server-config-example
- key_count: 7
  name: Cisco Voice Portal Administration Call Server Example
  slug: cisco-voice-portal-administration-call-server-example
- key_count: 5
  name: Cisco Voice Portal Administration Device Create Request Example
  slug: cisco-voice-portal-administration-device-create-request-example
- key_count: 8
  name: Cisco Voice Portal Administration Device Example
  slug: cisco-voice-portal-administration-device-example
- key_count: 7
  name: Cisco Voice Portal Administration Device Status Example
  slug: cisco-voice-portal-administration-device-status-example
- key_count: 3
  name: Cisco Voice Portal Administration Device Update Request Example
  slug: cisco-voice-portal-administration-device-update-request-example
- key_count: 5
  name: Cisco Voice Portal Administration Dialed Number Pattern Create Example
  slug: cisco-voice-portal-administration-dialed-number-pattern-create-example
- key_count: 6
  name: Cisco Voice Portal Administration Dialed Number Pattern Example
  slug: cisco-voice-portal-administration-dialed-number-pattern-example
- key_count: 4
  name: Cisco Voice Portal Administration Error Example
  slug: cisco-voice-portal-administration-error-example
- key_count: 6
  name: Cisco Voice Portal Administration License Info Example
  slug: cisco-voice-portal-administration-license-info-example
- key_count: 6
  name: Cisco Voice Portal Administration Operation Status Example
  slug: cisco-voice-portal-administration-operation-status-example
- key_count: 4
  name: Cisco Voice Portal Administration Sip Server Group Create Example
  slug: cisco-voice-portal-administration-sip-server-group-create-example
- key_count: 5
  name: Cisco Voice Portal Administration Sip Server Group Example
  slug: cisco-voice-portal-administration-sip-server-group-example
- key_count: 3
  name: Cisco Voice Portal Administration System Config Example
  slug: cisco-voice-portal-administration-system-config-example
- key_count: 4
  name: Cisco Voice Portal Administration User Create Example
  slug: cisco-voice-portal-administration-user-create-example
- key_count: 6
  name: Cisco Voice Portal Administration User Example
  slug: cisco-voice-portal-administration-user-example
- key_count: 5
  name: Cisco Voice Portal Administration Vxml Server Config Example
  slug: cisco-voice-portal-administration-vxml-server-config-example
- key_count: 7
  name: Cisco Voice Portal Administration Vxml Server Example
  slug: cisco-voice-portal-administration-vxml-server-example
- key_count: 14
  name: Cisco Voice Portal Call Control Active Call Detail Example
  slug: cisco-voice-portal-call-control-active-call-detail-example
- key_count: 7
  name: Cisco Voice Portal Call Control Active Call Example
  slug: cisco-voice-portal-call-control-active-call-example
- key_count: 5
  name: Cisco Voice Portal Call Control Call Operation Result Example
  slug: cisco-voice-portal-call-control-call-operation-result-example
- key_count: 4
  name: Cisco Voice Portal Call Control Call Variables Example
  slug: cisco-voice-portal-call-control-call-variables-example
- key_count: 3
  name: Cisco Voice Portal Call Control Call Variables Update Example
  slug: cisco-voice-portal-call-control-call-variables-update-example
- key_count: 2
  name: Cisco Voice Portal Call Control Connectivity Status Example
  slug: cisco-voice-portal-call-control-connectivity-status-example
- key_count: 4
  name: Cisco Voice Portal Call Control Error Example
  slug: cisco-voice-portal-call-control-error-example
- key_count: 10
  name: Cisco Voice Portal Call Control Health Status Example
  slug: cisco-voice-portal-call-control-health-status-example
- key_count: 6
  name: Cisco Voice Portal Call Control Routing Result Example
  slug: cisco-voice-portal-call-control-routing-result-example
- key_count: 14
  name: Cisco Voice Portal Call Control Sip Session Detail Example
  slug: cisco-voice-portal-call-control-sip-session-detail-example
- key_count: 8
  name: Cisco Voice Portal Call Control Sip Session Example
  slug: cisco-voice-portal-call-control-sip-session-example
- key_count: 4
  name: Cisco Voice Portal Call Control Transfer Request Example
  slug: cisco-voice-portal-call-control-transfer-request-example
- key_count: 3
  name: Cisco Voice Portal Reporting Application Statistics Example
  slug: cisco-voice-portal-reporting-application-statistics-example
- key_count: 17
  name: Cisco Voice Portal Reporting Call Detail Record Example
  slug: cisco-voice-portal-reporting-call-detail-record-example
- key_count: 10
  name: Cisco Voice Portal Reporting Call Leg Example
  slug: cisco-voice-portal-reporting-call-leg-example
- key_count: 4
  name: Cisco Voice Portal Reporting Call Summary Statistics Example
  slug: cisco-voice-portal-reporting-call-summary-statistics-example
- key_count: 4
  name: Cisco Voice Portal Reporting Cdr Query Result Example
  slug: cisco-voice-portal-reporting-cdr-query-result-example
- key_count: 4
  name: Cisco Voice Portal Reporting Error Example
  slug: cisco-voice-portal-reporting-error-example
- key_count: 6
  name: Cisco Voice Portal Reporting Realtime Statistics Example
  slug: cisco-voice-portal-reporting-realtime-statistics-example
- key_count: 3
  name: Cisco Voice Portal Reporting Report Execution Request Example
  slug: cisco-voice-portal-reporting-report-execution-request-example
- key_count: 9
  name: Cisco Voice Portal Reporting Report Result Example
  slug: cisco-voice-portal-reporting-report-result-example
- key_count: 5
  name: Cisco Voice Portal Reporting Report Template Example
  slug: cisco-voice-portal-reporting-report-template-example
- key_count: 3
  name: Cisco Voice Portal Reporting Server Statistics Example
  slug: cisco-voice-portal-reporting-server-statistics-example
- key_count: 7
  name: Cisco Voice Portal Vxml Services Application Config Example
  slug: cisco-voice-portal-vxml-services-application-config-example
- key_count: 6
  name: Cisco Voice Portal Vxml Services Application Config Update Example
  slug: cisco-voice-portal-vxml-services-application-config-update-example
- key_count: 6
  name: Cisco Voice Portal Vxml Services Call Flow Element Example
  slug: cisco-voice-portal-vxml-services-call-flow-element-example
- key_count: 4
  name: Cisco Voice Portal Vxml Services Error Example
  slug: cisco-voice-portal-vxml-services-error-example
- key_count: 6
  name: Cisco Voice Portal Vxml Services Grammar File Example
  slug: cisco-voice-portal-vxml-services-grammar-file-example
- key_count: 6
  name: Cisco Voice Portal Vxml Services Log Entry Example
  slug: cisco-voice-portal-vxml-services-log-entry-example
- key_count: 6
  name: Cisco Voice Portal Vxml Services Media File Example
  slug: cisco-voice-portal-vxml-services-media-file-example
- key_count: 3
  name: Cisco Voice Portal Vxml Services Micro App Config Example
  slug: cisco-voice-portal-vxml-services-micro-app-config-example
- key_count: 4
  name: Cisco Voice Portal Vxml Services Micro Application Example
  slug: cisco-voice-portal-vxml-services-micro-application-example
- key_count: 3
  name: Cisco Voice Portal Vxml Services Operation Result Example
  slug: cisco-voice-portal-vxml-services-operation-result-example
- key_count: 12
  name: Cisco Voice Portal Vxml Services Vxml Application Detail Example
  slug: cisco-voice-portal-vxml-services-vxml-application-detail-example
- key_count: 6
  name: Cisco Voice Portal Vxml Services Vxml Application Example
  slug: cisco-voice-portal-vxml-services-vxml-application-example
- key_count: 11
  name: Cisco Voice Portal Vxml Services Vxml Server Status Example
  slug: cisco-voice-portal-vxml-services-vxml-server-status-example
- key_count: 11
  name: Cisco Voice Portal Vxml Services Vxml Session Detail Example
  slug: cisco-voice-portal-vxml-services-vxml-session-detail-example
- key_count: 8
  name: Cisco Voice Portal Vxml Services Vxml Session Example
  slug: cisco-voice-portal-vxml-services-vxml-session-example
finops:
- name: Cisco Voice Portal Finops
  service_category: Contact Center
  slug: cisco-voice-portal-finops
image: https://www.cisco.com/c/en/us/products/customer-collaboration/unified-contact-center-enterprise/index.html
json_schemas:
- name: Application
  property_count: 8
  slug: cisco-voice-portal-administration-application
- name: CallServerConfig
  property_count: 4
  slug: cisco-voice-portal-administration-call-server-config
- name: CallServer
  property_count: 7
  slug: cisco-voice-portal-administration-call-server
- name: DeviceCreateRequest
  property_count: 5
  slug: cisco-voice-portal-administration-device-create-request
- name: Device
  property_count: 8
  slug: cisco-voice-portal-administration-device
- name: DeviceStatus
  property_count: 7
  slug: cisco-voice-portal-administration-device-status
- name: DeviceUpdateRequest
  property_count: 3
  slug: cisco-voice-portal-administration-device-update-request
- name: DialedNumberPatternCreate
  property_count: 5
  slug: cisco-voice-portal-administration-dialed-number-pattern-create
- name: DialedNumberPattern
  property_count: 6
  slug: cisco-voice-portal-administration-dialed-number-pattern
- name: Error
  property_count: 4
  slug: cisco-voice-portal-administration-error
- name: LicenseInfo
  property_count: 6
  slug: cisco-voice-portal-administration-license-info
- name: OperationStatus
  property_count: 6
  slug: cisco-voice-portal-administration-operation-status
- name: SipServerGroupCreate
  property_count: 4
  slug: cisco-voice-portal-administration-sip-server-group-create
- name: SipServerGroup
  property_count: 5
  slug: cisco-voice-portal-administration-sip-server-group
- name: SystemConfig
  property_count: 3
  slug: cisco-voice-portal-administration-system-config
- name: UserCreate
  property_count: 4
  slug: cisco-voice-portal-administration-user-create
- name: User
  property_count: 6
  slug: cisco-voice-portal-administration-user
- name: VxmlServerConfig
  property_count: 5
  slug: cisco-voice-portal-administration-vxml-server-config
- name: VxmlServer
  property_count: 7
  slug: cisco-voice-portal-administration-vxml-server
- name: Cisco Voice Portal Application
  property_count: 16
  slug: cisco-voice-portal-application
- name: ActiveCallDetail
  property_count: 14
  slug: cisco-voice-portal-call-control-active-call-detail
- name: ActiveCall
  property_count: 7
  slug: cisco-voice-portal-call-control-active-call
- name: CallOperationResult
  property_count: 5
  slug: cisco-voice-portal-call-control-call-operation-result
- name: CallVariables
  property_count: 4
  slug: cisco-voice-portal-call-control-call-variables
- name: CallVariablesUpdate
  property_count: 3
  slug: cisco-voice-portal-call-control-call-variables-update
- name: ConnectivityStatus
  property_count: 2
  slug: cisco-voice-portal-call-control-connectivity-status
- name: Error
  property_count: 4
  slug: cisco-voice-portal-call-control-error
- name: HealthStatus
  property_count: 10
  slug: cisco-voice-portal-call-control-health-status
- name: RoutingResult
  property_count: 6
  slug: cisco-voice-portal-call-control-routing-result
- name: SipSessionDetail
  property_count: 14
  slug: cisco-voice-portal-call-control-sip-session-detail
- name: SipSession
  property_count: 8
  slug: cisco-voice-portal-call-control-sip-session
- name: TransferRequest
  property_count: 4
  slug: cisco-voice-portal-call-control-transfer-request
- name: Cisco Voice Portal Call Detail Record
  property_count: 20
  slug: cisco-voice-portal-call-detail-record
- name: Cisco Voice Portal Device
  property_count: 10
  slug: cisco-voice-portal-device
- name: Cisco Voice Portal Dialed Number Pattern
  property_count: 11
  slug: cisco-voice-portal-dialed-number-pattern
- name: ApplicationStatistics
  property_count: 3
  slug: cisco-voice-portal-reporting-application-statistics
- name: CallDetailRecord
  property_count: 17
  slug: cisco-voice-portal-reporting-call-detail-record
- name: CallLeg
  property_count: 10
  slug: cisco-voice-portal-reporting-call-leg
- name: CallSummaryStatistics
  property_count: 4
  slug: cisco-voice-portal-reporting-call-summary-statistics
- name: CdrQueryResult
  property_count: 4
  slug: cisco-voice-portal-reporting-cdr-query-result
- name: Error
  property_count: 4
  slug: cisco-voice-portal-reporting-error
- name: RealtimeStatistics
  property_count: 6
  slug: cisco-voice-portal-reporting-realtime-statistics
- name: ReportExecutionRequest
  property_count: 3
  slug: cisco-voice-portal-reporting-report-execution-request
- name: ReportResult
  property_count: 9
  slug: cisco-voice-portal-reporting-report-result
- name: ReportTemplate
  property_count: 5
  slug: cisco-voice-portal-reporting-report-template
- name: ServerStatistics
  property_count: 3
  slug: cisco-voice-portal-reporting-server-statistics
- name: ApplicationConfig
  property_count: 7
  slug: cisco-voice-portal-vxml-services-application-config
- name: ApplicationConfigUpdate
  property_count: 6
  slug: cisco-voice-portal-vxml-services-application-config-update
- name: CallFlowElement
  property_count: 6
  slug: cisco-voice-portal-vxml-services-call-flow-element
- name: Error
  property_count: 4
  slug: cisco-voice-portal-vxml-services-error
- name: GrammarFile
  property_count: 6
  slug: cisco-voice-portal-vxml-services-grammar-file
- name: LogEntry
  property_count: 6
  slug: cisco-voice-portal-vxml-services-log-entry
- name: MediaFile
  property_count: 6
  slug: cisco-voice-portal-vxml-services-media-file
- name: MicroAppConfig
  property_count: 3
  slug: cisco-voice-portal-vxml-services-micro-app-config
- name: MicroApplication
  property_count: 4
  slug: cisco-voice-portal-vxml-services-micro-application
- name: OperationResult
  property_count: 3
  slug: cisco-voice-portal-vxml-services-operation-result
- name: VxmlApplicationDetail
  property_count: 12
  slug: cisco-voice-portal-vxml-services-vxml-application-detail
- name: VxmlApplication
  property_count: 6
  slug: cisco-voice-portal-vxml-services-vxml-application
- name: VxmlServerStatus
  property_count: 11
  slug: cisco-voice-portal-vxml-services-vxml-server-status
- name: VxmlSessionDetail
  property_count: 11
  slug: cisco-voice-portal-vxml-services-vxml-session-detail
- name: VxmlSession
  property_count: 8
  slug: cisco-voice-portal-vxml-services-vxml-session
json_structures:
- name: Cisco Voice Portal Administration Application Structure
  property_count: 8
  slug: cisco-voice-portal-administration-application-structure
- name: Cisco Voice Portal Administration Call Server Config Structure
  property_count: 4
  slug: cisco-voice-portal-administration-call-server-config-structure
- name: Cisco Voice Portal Administration Call Server Structure
  property_count: 7
  slug: cisco-voice-portal-administration-call-server-structure
- name: Cisco Voice Portal Administration Device Create Request Structure
  property_count: 5
  slug: cisco-voice-portal-administration-device-create-request-structure
- name: Cisco Voice Portal Administration Device Status Structure
  property_count: 7
  slug: cisco-voice-portal-administration-device-status-structure
- name: Cisco Voice Portal Administration Device Structure
  property_count: 8
  slug: cisco-voice-portal-administration-device-structure
- name: Cisco Voice Portal Administration Device Update Request Structure
  property_count: 3
  slug: cisco-voice-portal-administration-device-update-request-structure
- name: Cisco Voice Portal Administration Dialed Number Pattern Create Structure
  property_count: 5
  slug: cisco-voice-portal-administration-dialed-number-pattern-create-structure
- name: Cisco Voice Portal Administration Dialed Number Pattern Structure
  property_count: 6
  slug: cisco-voice-portal-administration-dialed-number-pattern-structure
- name: Cisco Voice Portal Administration Error Structure
  property_count: 4
  slug: cisco-voice-portal-administration-error-structure
- name: Cisco Voice Portal Administration License Info Structure
  property_count: 6
  slug: cisco-voice-portal-administration-license-info-structure
- name: Cisco Voice Portal Administration Operation Status Structure
  property_count: 6
  slug: cisco-voice-portal-administration-operation-status-structure
- name: Cisco Voice Portal Administration Sip Server Group Create Structure
  property_count: 4
  slug: cisco-voice-portal-administration-sip-server-group-create-structure
- name: Cisco Voice Portal Administration Sip Server Group Structure
  property_count: 5
  slug: cisco-voice-portal-administration-sip-server-group-structure
- name: Cisco Voice Portal Administration System Config Structure
  property_count: 3
  slug: cisco-voice-portal-administration-system-config-structure
- name: Cisco Voice Portal Administration User Create Structure
  property_count: 4
  slug: cisco-voice-portal-administration-user-create-structure
- name: Cisco Voice Portal Administration User Structure
  property_count: 6
  slug: cisco-voice-portal-administration-user-structure
- name: Cisco Voice Portal Administration Vxml Server Config Structure
  property_count: 5
  slug: cisco-voice-portal-administration-vxml-server-config-structure
- name: Cisco Voice Portal Administration Vxml Server Structure
  property_count: 7
  slug: cisco-voice-portal-administration-vxml-server-structure
- name: Cisco Voice Portal Call Control Active Call Detail Structure
  property_count: 14
  slug: cisco-voice-portal-call-control-active-call-detail-structure
- name: Cisco Voice Portal Call Control Active Call Structure
  property_count: 7
  slug: cisco-voice-portal-call-control-active-call-structure
- name: Cisco Voice Portal Call Control Call Operation Result Structure
  property_count: 5
  slug: cisco-voice-portal-call-control-call-operation-result-structure
- name: Cisco Voice Portal Call Control Call Variables Structure
  property_count: 4
  slug: cisco-voice-portal-call-control-call-variables-structure
- name: Cisco Voice Portal Call Control Call Variables Update Structure
  property_count: 3
  slug: cisco-voice-portal-call-control-call-variables-update-structure
- name: Cisco Voice Portal Call Control Connectivity Status Structure
  property_count: 2
  slug: cisco-voice-portal-call-control-connectivity-status-structure
- name: Cisco Voice Portal Call Control Error Structure
  property_count: 4
  slug: cisco-voice-portal-call-control-error-structure
- name: Cisco Voice Portal Call Control Health Status Structure
  property_count: 10
  slug: cisco-voice-portal-call-control-health-status-structure
- name: Cisco Voice Portal Call Control Routing Result Structure
  property_count: 6
  slug: cisco-voice-portal-call-control-routing-result-structure
- name: Cisco Voice Portal Call Control Sip Session Detail Structure
  property_count: 14
  slug: cisco-voice-portal-call-control-sip-session-detail-structure
- name: Cisco Voice Portal Call Control Sip Session Structure
  property_count: 8
  slug: cisco-voice-portal-call-control-sip-session-structure
- name: Cisco Voice Portal Call Control Transfer Request Structure
  property_count: 4
  slug: cisco-voice-portal-call-control-transfer-request-structure
- name: Cisco Voice Portal Reporting Application Statistics Structure
  property_count: 3
  slug: cisco-voice-portal-reporting-application-statistics-structure
- name: Cisco Voice Portal Reporting Call Detail Record Structure
  property_count: 17
  slug: cisco-voice-portal-reporting-call-detail-record-structure
- name: Cisco Voice Portal Reporting Call Leg Structure
  property_count: 10
  slug: cisco-voice-portal-reporting-call-leg-structure
- name: Cisco Voice Portal Reporting Call Summary Statistics Structure
  property_count: 4
  slug: cisco-voice-portal-reporting-call-summary-statistics-structure
- name: Cisco Voice Portal Reporting Cdr Query Result Structure
  property_count: 4
  slug: cisco-voice-portal-reporting-cdr-query-result-structure
- name: Cisco Voice Portal Reporting Error Structure
  property_count: 4
  slug: cisco-voice-portal-reporting-error-structure
- name: Cisco Voice Portal Reporting Realtime Statistics Structure
  property_count: 6
  slug: cisco-voice-portal-reporting-realtime-statistics-structure
- name: Cisco Voice Portal Reporting Report Execution Request Structure
  property_count: 3
  slug: cisco-voice-portal-reporting-report-execution-request-structure
- name: Cisco Voice Portal Reporting Report Result Structure
  property_count: 9
  slug: cisco-voice-portal-reporting-report-result-structure
- name: Cisco Voice Portal Reporting Report Template Structure
  property_count: 5
  slug: cisco-voice-portal-reporting-report-template-structure
- name: Cisco Voice Portal Reporting Server Statistics Structure
  property_count: 3
  slug: cisco-voice-portal-reporting-server-statistics-structure
- name: Cisco Voice Portal Vxml Services Application Config Structure
  property_count: 7
  slug: cisco-voice-portal-vxml-services-application-config-structure
- name: Cisco Voice Portal Vxml Services Application Config Update Structure
  property_count: 6
  slug: cisco-voice-portal-vxml-services-application-config-update-structure
- name: Cisco Voice Portal Vxml Services Call Flow Element Structure
  property_count: 6
  slug: cisco-voice-portal-vxml-services-call-flow-element-structure
- name: Cisco Voice Portal Vxml Services Error Structure
  property_count: 4
  slug: cisco-voice-portal-vxml-services-error-structure
- name: Cisco Voice Portal Vxml Services Grammar File Structure
  property_count: 6
  slug: cisco-voice-portal-vxml-services-grammar-file-structure
- name: Cisco Voice Portal Vxml Services Log Entry Structure
  property_count: 6
  slug: cisco-voice-portal-vxml-services-log-entry-structure
- name: Cisco Voice Portal Vxml Services Media File Structure
  property_count: 6
  slug: cisco-voice-portal-vxml-services-media-file-structure
- name: Cisco Voice Portal Vxml Services Micro App Config Structure
  property_count: 3
  slug: cisco-voice-portal-vxml-services-micro-app-config-structure
- name: Cisco Voice Portal Vxml Services Micro Application Structure
  property_count: 4
  slug: cisco-voice-portal-vxml-services-micro-application-structure
- name: Cisco Voice Portal Vxml Services Operation Result Structure
  property_count: 3
  slug: cisco-voice-portal-vxml-services-operation-result-structure
- name: Cisco Voice Portal Vxml Services Vxml Application Detail Structure
  property_count: 12
  slug: cisco-voice-portal-vxml-services-vxml-application-detail-structure
- name: Cisco Voice Portal Vxml Services Vxml Application Structure
  property_count: 6
  slug: cisco-voice-portal-vxml-services-vxml-application-structure
- name: Cisco Voice Portal Vxml Services Vxml Server Status Structure
  property_count: 11
  slug: cisco-voice-portal-vxml-services-vxml-server-status-structure
- name: Cisco Voice Portal Vxml Services Vxml Session Detail Structure
  property_count: 11
  slug: cisco-voice-portal-vxml-services-vxml-session-detail-structure
- name: Cisco Voice Portal Vxml Services Vxml Session Structure
  property_count: 8
  slug: cisco-voice-portal-vxml-services-vxml-session-structure
jsonld:
- class_count: 0
  name: Cisco Voice Portal Administration Context
  property_count: 0
  slug: cisco-voice-portal-administration-context
- class_count: 0
  name: Cisco Voice Portal Call Control Context
  property_count: 0
  slug: cisco-voice-portal-call-control-context
- class_count: 0
  name: Cisco Voice Portal Reporting Context
  property_count: 0
  slug: cisco-voice-portal-reporting-context
- class_count: 0
  name: Cisco Voice Portal Vxml Services Context
  property_count: 0
  slug: cisco-voice-portal-vxml-services-context
layout: provider
modified: '2026-05-19'
name: Cisco Voice Portal
nav: Providers
network: true
overview: 'Cisco Voice Portal publishes 24 APIs on the [APIs.io](https://apis.io/) network, including Call Events API, Application Configuration API, Application Management API, and 21 more. Tagged areas include Contact Center, IVR, Telephony, Voice, and VXML.


  The Cisco Voice Portal catalog on APIs.io includes 1 event-driven AsyncAPI specification, 4 JSON-LD contexts, and 3 Spectral governance rulesets.


  Cisco Voice Portal''s developer surface includes authentication, support, documentation, getting-started guide, engineering blog, signup flow, release notes, and 13 more developer resources.'
plans:
- name: Cisco Voice Portal Plans Pricing
  plan_count: 1
  slug: cisco-voice-portal-plans-pricing
random_paper: 26
rate_limits:
- limit_count: 2
  name: Cisco Voice Portal Rate Limits
  slug: cisco-voice-portal-rate-limits
rules:
- name: Cisco Voice Portal API Rules
  rule_count: 6
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 5
  slug: cisco-voice-portal-asyncapi-spectral-rules
- name: Cisco Voice Portal API Rules
  rule_count: 6
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 4
  slug: cisco-voice-portal-jsonschema-spectral-rules
- name: Cisco Voice Portal API Rules
  rule_count: 17
  severity_counts:
    error: 8
    hint: 0
    info: 2
    warn: 7
  slug: cisco-voice-portal-spectral-rules
score:
  band: developing
  composite: 59.4
  delta: 0.0
  facets:
    commercial_clarity: 50.0
    contract_quality: 73.5
    developer_ergonomics: 45.7
    discoverability: 55.0
    governance: 73.7
    operational_transparency: 57.9
  previous_composite: 59.4
  schema_version: 0.5
  scored_at: '2026-07-23'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/cisco-voice-portal/refs/heads/main/screenshots/cisco-voice-portal-2026-06-20T174408.png
security:
- kind: authentication
  name: Cisco Voice Portal Authentication
  slug: cisco-voice-portal-authentication
  summary_line: apiKey/http · 2 schemes
- kind: domain-security
  name: Cisco Voice Portal Domain Security
  slug: cisco-voice-portal-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Cisco Voice Portal Vulnerability Disclosure
  slug: cisco-voice-portal-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: cisco-voice-portal
tags:
- Contact Center
- IVR
- Telephony
- Voice
- VXML
website: https://developer.cisco.com/
---
