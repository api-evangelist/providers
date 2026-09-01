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
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 27.7
  scored_at: '2026-09-01'
agentic_access:
- acting_count: 16
  human_in_the_loop: 1
  name: Oracle Enterprise Manager Agentic Access
  operation_count: 36
  slug: oracle-enterprise-manager-agentic-access
  summary_line: 36 operations · 16 acting · 1 human-in-the-loop
api_count: 1
apis:
- description: 'Command-line interface providing scriptable access to Enterprise Manager functionality including target management, job operations, patching, provisioning, and administration tasks through verbs that '
  name: Enterprise Manager Command Line Interface (EM CLI)
  slug: enterprise-manager-command-line-interface-em-cli
- description: API for creating, managing, and monitoring Enterprise Manager jobs and tasks including scheduling, execution tracking, and deployment procedures.
  name: Enterprise Manager Job System API
  slug: enterprise-manager-job-system-api
- description: API for accessing performance metrics, monitoring data, and alerting information including numeric metric data points over time, latest metric values, and metric group metadata.
  name: Enterprise Manager Metric and Monitoring API
  slug: enterprise-manager-metric-and-monitoring-api
- description: API for managing monitored targets including discovery, configuration, lifecycle operations, bulk property updates, and target type metadata.
  name: Enterprise Manager Target Management API
  slug: enterprise-manager-target-management-api
- description: REST API for searching, viewing, and managing incidents and events in Enterprise Manager, including clearing, suppressing, unsuppressing incidents, viewing member events, and managing annotations.
  name: Enterprise Manager Incidents and Events API
  slug: enterprise-manager-incidents-and-events-api
- description: REST API for managing blackouts (maintenance windows) in Enterprise Manager, including creating, editing, deleting, listing, and stopping blackouts, managing blackout reasons, and retrieving targets i
  name: Enterprise Manager Blackout Management API
  slug: enterprise-manager-blackout-management-api
- description: REST API for managing named credentials, monitoring credentials, and preferred credentials in Enterprise Manager, including creating, listing, deleting, updating, testing, and searching credential typ
  name: Enterprise Manager Credentials Management API
  slug: enterprise-manager-credentials-management-api
- description: 'REST API for managing Enterprise Manager users and roles, including creating, modifying, and deleting users and roles, managing privilege grants and role assignments, and listing secure resources and '
  name: Enterprise Manager User Management API
  slug: enterprise-manager-user-management-api
- description: REST API for database maintenance operations including updates, upgrades, and patching, with support for creating and managing Gold Images, patch recommendations, compliance reporting, and Fleet Patch
  name: Enterprise Manager Database Patching and Maintenance API
  slug: enterprise-manager-database-patching-and-maintenance-api
- description: REST API for managing deployment procedures including creating, submitting, and deleting procedures, managing procedure instances with resume, suspend, stop, and retry operations, and tracking executi
  name: Enterprise Manager Deployment Procedure API
  slug: enterprise-manager-deployment-procedure-api
- description: REST API for configuring and managing database backup settings, fleet-level backup configuration, and scheduling backup operations in Enterprise Manager.
  name: Enterprise Manager Database Backup Management API
  slug: enterprise-manager-database-backup-management-api
- description: REST API for managing Oracle Zero Data Loss Recovery Appliance (ZDLRA) including adding and removing protected databases, creating and managing protection policies, creating archival backups, and retr
  name: Enterprise Manager ZDLRA Management API
  slug: enterprise-manager-zdlra-management-api
- description: REST API for executing SQL queries against database targets monitored by Enterprise Manager and against the Enterprise Manager repository, enabling custom data extraction for dashboards and KPI report
  name: Enterprise Manager SQL Execution REST API
  slug: enterprise-manager-sql-execution-rest-api
- description: REST API for managing Oracle Data Guard configurations in Enterprise Manager, enabling high availability operations including switchover, failover, and standby database management.
  name: Enterprise Manager Data Guard Administration REST API
  slug: enterprise-manager-data-guard-administration-rest-api
- description: REST APIs for Database as a Service (DBaaS) operations enabling self-service database provisioning, request management, and quota administration through Enterprise Manager Cloud Control.
  name: Enterprise Manager Cloud APIs (DBaaS)
  slug: enterprise-manager-cloud-apis-dbaas
- description: Extensibility Development Kit providing tools, utilities, and APIs for developing Enterprise Manager plug-ins to extend platform capabilities for custom target monitoring and management.
  name: Enterprise Manager Extensibility Development Kit (EDK) API
  slug: enterprise-manager-extensibility-development-kit-edk-api
- description: Manage blackout windows for maintenance activities. Blackouts suppress monitoring and alerting during scheduled maintenance periods, preventing false alerts.
  name: Oracle Enterprise Manager Blackouts API
  slug: oracle-enterprise-manager-blackouts-api
- description: Access individual event details. Events are the underlying occurrences that are correlated into incidents.
  name: Oracle Enterprise Manager Events API
  slug: oracle-enterprise-manager-events-api
- description: Manage global properties that can be applied across targets for classification, grouping, and reporting purposes.
  name: Oracle Enterprise Manager Global Target Properties API
  slug: oracle-enterprise-manager-global-target-properties-api
- description: Search, view, and manage incidents and events. Incidents represent actionable issues detected by Enterprise Manager monitoring, with operations for clearing, suppressing, and annotating.
  name: Oracle Enterprise Manager Incidents API
  slug: oracle-enterprise-manager-incidents-api
- description: Query metric data and metadata for monitored targets. Access time-series performance data, latest metric values, and metric group definitions.
  name: Oracle Enterprise Manager Metrics API
  slug: oracle-enterprise-manager-metrics-api
- description: Manage monitored targets in Enterprise Manager including discovery, configuration, lifecycle operations, and property management. Targets represent any managed entity such as databases, hosts, middlew
  name: Oracle Enterprise Manager Targets API
  slug: oracle-enterprise-manager-targets-api
arazzos:
- description: Confirm a target, read its current properties, then bulk-apply property updates.
  name: Oracle Enterprise Manager Bulk Configure Target Properties
  slug: oracle-enterprise-manager-bulk-configure-target-workflow
- description: Create a global target property, verify it, and read back its valid values.
  name: Oracle Enterprise Manager Define Global Target Property
  slug: oracle-enterprise-manager-define-global-property-workflow
- description: Find a started blackout for a target and stop it early to resume monitoring.
  name: Oracle Enterprise Manager End Active Blackout
  slug: oracle-enterprise-manager-end-active-blackout-workflow
- description: Find a monitored target by name and pull its full configuration profile.
  name: Oracle Enterprise Manager Inspect Target
  slug: oracle-enterprise-manager-inspect-target-workflow
- description: Review an incident's details and annotations, then suppress it.
  name: Oracle Enterprise Manager Investigate and Suppress Incident
  slug: oracle-enterprise-manager-investigate-suppress-incident-workflow
- description: Resolve a target's metric group and pull its latest collected data point.
  name: Oracle Enterprise Manager Read Metric Snapshot
  slug: oracle-enterprise-manager-read-metric-snapshot-workflow
- description: Ensure a blackout reason exists, then create and verify a maintenance window.
  name: Oracle Enterprise Manager Schedule Blackout
  slug: oracle-enterprise-manager-schedule-blackout-workflow
- description: Resolve a target by name, then pull a metric time series over a window.
  name: Oracle Enterprise Manager Target Metric Trend
  slug: oracle-enterprise-manager-target-metric-trend-workflow
- description: Drill from an incident into its events and one event's full detail.
  name: Oracle Enterprise Manager Trace Incident Event
  slug: oracle-enterprise-manager-trace-incident-event-workflow
- description: Find the most severe open incident, inspect its events, and clear it.
  name: Oracle Enterprise Manager Triage and Clear Incident
  slug: oracle-enterprise-manager-triage-clear-incident-workflow
artifact_total: 242
collections:
- collection_type: postman
  name: Oracle Enterprise Manager Cloud Control REST API
  slug: postman-oracle-enterprise-manager-cloud-control
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Oracle Enterprise Manager Cloud Control REST Blackouts API
  slug: open-oracle-enterprise-manager-blackouts-api
- collection_type: open
  name: Oracle Enterprise Manager Cloud Control REST API
  slug: open-oracle-enterprise-manager-cloud-control
- collection_type: open
  name: Oracle Enterprise Manager Cloud Control REST Blackouts Events API
  slug: open-oracle-enterprise-manager-events-api
- collection_type: open
  name: Oracle Enterprise Manager Cloud Control REST Blackouts Global Target Properties API
  slug: open-oracle-enterprise-manager-global-target-properties-api
- collection_type: open
  name: Oracle Enterprise Manager Cloud Control REST Blackouts Incidents API
  slug: open-oracle-enterprise-manager-incidents-api
- collection_type: open
  name: Oracle Enterprise Manager Cloud Control REST Blackouts Metrics API
  slug: open-oracle-enterprise-manager-metrics-api
- collection_type: open
  name: Oracle Enterprise Manager Cloud Control REST Blackouts Targets API
  slug: open-oracle-enterprise-manager-targets-api
common:
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/oracle-enterprise-manager-capability-edges.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/oracle-enterprise-manager-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/oracle-enterprise-manager-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/oracle-enterprise-manager-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/oracle-enterprise-manager-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/oracle-enterprise-manager-problem-types.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/oracle-enterprise-manager-conformance.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/oracle-enterprise-manager-data-model.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/oracle-enterprise-manager-lifecycle.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/oracle-enterprise-manager-changelog.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/oracle-enterprise-manager-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/oracle-enterprise-manager-llms.txt
- group: other
  title: ''
  type: Overlay
  url: overlays/oracle-enterprise-manager-cloud-control-overlay.yaml
- group: build
  title: ''
  type: CLI
  url: cli/oracle-enterprise-manager-cli.yml
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/oracle-enterprise-manager/overview
- group: design
  title: ''
  type: Arazzo
  url: arazzo/oracle-enterprise-manager-bulk-configure-target-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/oracle-enterprise-manager-define-global-property-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/oracle-enterprise-manager-end-active-blackout-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/oracle-enterprise-manager-inspect-target-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/oracle-enterprise-manager-investigate-suppress-incident-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/oracle-enterprise-manager-read-metric-snapshot-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/oracle-enterprise-manager-schedule-blackout-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/oracle-enterprise-manager-target-metric-trend-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/oracle-enterprise-manager-trace-incident-event-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/oracle-enterprise-manager-triage-clear-incident-workflow.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/oracle
- group: start
  title: ''
  type: Portal
  url: https://www.oracle.com/enterprise-manager/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.oracle.com/en/enterprise-manager/
- group: operate
  title: ''
  type: Support
  url: https://www.oracle.com/support/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.oracle.com/enterprise-manager/pricing.html
- group: company
  title: ''
  type: Blog
  url: https://blogs.oracle.com/oem/
- group: learn
  title: ''
  type: Training
  url: https://education.oracle.com/enterprise-manager
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.oracle.com/legal/terms.html
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.oracle.com/legal/privacy/
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.oracle.com/en/enterprise-manager/cloud-control/enterprise-manager-cloud-control/13.5/index.html
- group: operate
  title: ''
  type: ReleaseNotes
  url: https://docs.oracle.com/en/enterprise-manager/cloud-control/enterprise-manager-cloud-control/13.5/emrel/cloud-control-release-notes-emrel.html
- group: operate
  title: ''
  type: ChangeLog
  url: https://docs.oracle.com/en/enterprise-manager/cloud-control/enterprise-manager-cloud-control/13.5/emcon/new-features-release-update.html
- group: auth
  title: ''
  type: Security
  url: https://docs.oracle.com/en/enterprise-manager/cloud-control/enterprise-manager-cloud-control/13.5/emsec/index.html
- group: other
  title: ''
  type: Resources
  url: https://www.oracle.com/enterprise-manager/technologies/
created: '2024-01-01'
description: Oracle Enterprise Manager (OEM) provides a comprehensive management platform for managing Oracle IT infrastructure and applications. The APIs enable programmatic access to monitoring, administration, and automation capabilities.
examples:
- key_count: 6
  name: Oracle Enterprise Manager Bulkupdatetargetproperties Example
  slug: oracle-enterprise-manager-bulkupdatetargetproperties-example
- key_count: 6
  name: Oracle Enterprise Manager Clearincident Example
  slug: oracle-enterprise-manager-clearincident-example
- key_count: 1
  name: Oracle Enterprise Manager Cloud Control Annotation Collection Example
  slug: oracle-enterprise-manager-cloud-control-annotation-collection-example
- key_count: 5
  name: Oracle Enterprise Manager Cloud Control Annotation Example
  slug: oracle-enterprise-manager-cloud-control-annotation-example
- key_count: 5
  name: Oracle Enterprise Manager Cloud Control Blackout Collection Example
  slug: oracle-enterprise-manager-cloud-control-blackout-collection-example
- key_count: 4
  name: Oracle Enterprise Manager Cloud Control Blackout Create Request Example
  slug: oracle-enterprise-manager-cloud-control-blackout-create-request-example
- key_count: 5
  name: Oracle Enterprise Manager Cloud Control Blackout Dashboard Example
  slug: oracle-enterprise-manager-cloud-control-blackout-dashboard-example
- key_count: 10
  name: Oracle Enterprise Manager Cloud Control Blackout Example
  slug: oracle-enterprise-manager-cloud-control-blackout-example
- key_count: 1
  name: Oracle Enterprise Manager Cloud Control Blackout Reason Collection Example
  slug: oracle-enterprise-manager-cloud-control-blackout-reason-collection-example
- key_count: 1
  name: Oracle Enterprise Manager Cloud Control Blackout Reason Create Request Example
  slug: oracle-enterprise-manager-cloud-control-blackout-reason-create-request-example
- key_count: 2
  name: Oracle Enterprise Manager Cloud Control Blackout Reason Example
  slug: oracle-enterprise-manager-cloud-control-blackout-reason-example
- key_count: 7
  name: Oracle Enterprise Manager Cloud Control Blackout Schedule Example
  slug: oracle-enterprise-manager-cloud-control-blackout-schedule-example
- key_count: 1
  name: Oracle Enterprise Manager Cloud Control Blackout Target Collection Example
  slug: oracle-enterprise-manager-cloud-control-blackout-target-collection-example
- key_count: 3
  name: Oracle Enterprise Manager Cloud Control Blackout Target Example
  slug: oracle-enterprise-manager-cloud-control-blackout-target-example
- key_count: 3
  name: Oracle Enterprise Manager Cloud Control Blackout Update Request Example
  slug: oracle-enterprise-manager-cloud-control-blackout-update-request-example
- key_count: 1
  name: Oracle Enterprise Manager Cloud Control Bulk Property Update Request Example
  slug: oracle-enterprise-manager-cloud-control-bulk-property-update-request-example
- key_count: 4
  name: Oracle Enterprise Manager Cloud Control Error Example
  slug: oracle-enterprise-manager-cloud-control-error-example
- key_count: 1
  name: Oracle Enterprise Manager Cloud Control Event Collection Example
  slug: oracle-enterprise-manager-cloud-control-event-collection-example
- key_count: 12
  name: Oracle Enterprise Manager Cloud Control Event Example
  slug: oracle-enterprise-manager-cloud-control-event-example
- key_count: 1
  name: Oracle Enterprise Manager Cloud Control Global Target Property Collection Example
  slug: oracle-enterprise-manager-cloud-control-global-target-property-collection-example
- key_count: 5
  name: Oracle Enterprise Manager Cloud Control Global Target Property Create Request Example
  slug: oracle-enterprise-manager-cloud-control-global-target-property-create-request-example
- key_count: 6
  name: Oracle Enterprise Manager Cloud Control Global Target Property Example
  slug: oracle-enterprise-manager-cloud-control-global-target-property-example
- key_count: 3
  name: Oracle Enterprise Manager Cloud Control Global Target Property Update Request Example
  slug: oracle-enterprise-manager-cloud-control-global-target-property-update-request-example
- key_count: 5
  name: Oracle Enterprise Manager Cloud Control Incident Collection Example
  slug: oracle-enterprise-manager-cloud-control-incident-collection-example
- key_count: 18
  name: Oracle Enterprise Manager Cloud Control Incident Example
  slug: oracle-enterprise-manager-cloud-control-incident-example
- key_count: 5
  name: Oracle Enterprise Manager Cloud Control Metric Column Example
  slug: oracle-enterprise-manager-cloud-control-metric-column-example
- key_count: 1
  name: Oracle Enterprise Manager Cloud Control Metric Data Collection Example
  slug: oracle-enterprise-manager-cloud-control-metric-data-collection-example
- key_count: 4
  name: Oracle Enterprise Manager Cloud Control Metric Data Point Example
  slug: oracle-enterprise-manager-cloud-control-metric-data-point-example
- key_count: 1
  name: Oracle Enterprise Manager Cloud Control Metric Group Collection Example
  slug: oracle-enterprise-manager-cloud-control-metric-group-collection-example
- key_count: 5
  name: Oracle Enterprise Manager Cloud Control Metric Group Example
  slug: oracle-enterprise-manager-cloud-control-metric-group-example
- key_count: 1
  name: Oracle Enterprise Manager Cloud Control Metric Time Series Collection Example
  slug: oracle-enterprise-manager-cloud-control-metric-time-series-collection-example
- key_count: 6
  name: Oracle Enterprise Manager Cloud Control Metric Time Series Example
  slug: oracle-enterprise-manager-cloud-control-metric-time-series-example
- key_count: 5
  name: Oracle Enterprise Manager Cloud Control Target Collection Example
  slug: oracle-enterprise-manager-cloud-control-target-collection-example
- key_count: 5
  name: Oracle Enterprise Manager Cloud Control Target Create Request Example
  slug: oracle-enterprise-manager-cloud-control-target-create-request-example
- key_count: 17
  name: Oracle Enterprise Manager Cloud Control Target Example
  slug: oracle-enterprise-manager-cloud-control-target-example
- key_count: 1
  name: Oracle Enterprise Manager Cloud Control Target Property Collection Example
  slug: oracle-enterprise-manager-cloud-control-target-property-collection-example
- key_count: 3
  name: Oracle Enterprise Manager Cloud Control Target Property Example
  slug: oracle-enterprise-manager-cloud-control-target-property-example
- key_count: 1
  name: Oracle Enterprise Manager Cloud Control Target Update Request Example
  slug: oracle-enterprise-manager-cloud-control-target-update-request-example
- key_count: 6
  name: Oracle Enterprise Manager Createblackout Example
  slug: oracle-enterprise-manager-createblackout-example
- key_count: 6
  name: Oracle Enterprise Manager Createblackoutreason Example
  slug: oracle-enterprise-manager-createblackoutreason-example
- key_count: 6
  name: Oracle Enterprise Manager Createglobaltargetproperty Example
  slug: oracle-enterprise-manager-createglobaltargetproperty-example
- key_count: 6
  name: Oracle Enterprise Manager Createtarget Example
  slug: oracle-enterprise-manager-createtarget-example
- key_count: 6
  name: Oracle Enterprise Manager Editblackout Example
  slug: oracle-enterprise-manager-editblackout-example
- key_count: 6
  name: Oracle Enterprise Manager Getblackout Example
  slug: oracle-enterprise-manager-getblackout-example
- key_count: 6
  name: Oracle Enterprise Manager Getblackoutdashboard Example
  slug: oracle-enterprise-manager-getblackoutdashboard-example
- key_count: 6
  name: Oracle Enterprise Manager Getblackouttargets Example
  slug: oracle-enterprise-manager-getblackouttargets-example
- key_count: 6
  name: Oracle Enterprise Manager Getevent Example
  slug: oracle-enterprise-manager-getevent-example
- key_count: 6
  name: Oracle Enterprise Manager Getglobaltargetproperty Example
  slug: oracle-enterprise-manager-getglobaltargetproperty-example
- key_count: 6
  name: Oracle Enterprise Manager Getglobaltargetpropertyvalidvalues Example
  slug: oracle-enterprise-manager-getglobaltargetpropertyvalidvalues-example
- key_count: 6
  name: Oracle Enterprise Manager Getincident Example
  slug: oracle-enterprise-manager-getincident-example
- key_count: 6
  name: Oracle Enterprise Manager Getincidentannotations Example
  slug: oracle-enterprise-manager-getincidentannotations-example
- key_count: 6
  name: Oracle Enterprise Manager Getincidentevents Example
  slug: oracle-enterprise-manager-getincidentevents-example
- key_count: 6
  name: Oracle Enterprise Manager Getlatestmetricdata Example
  slug: oracle-enterprise-manager-getlatestmetricdata-example
- key_count: 6
  name: Oracle Enterprise Manager Getmetricgroup Example
  slug: oracle-enterprise-manager-getmetricgroup-example
- key_count: 6
  name: Oracle Enterprise Manager Getmetrictimeseries Example
  slug: oracle-enterprise-manager-getmetrictimeseries-example
- key_count: 6
  name: Oracle Enterprise Manager Gettarget Example
  slug: oracle-enterprise-manager-gettarget-example
- key_count: 6
  name: Oracle Enterprise Manager Gettargetproperties Example
  slug: oracle-enterprise-manager-gettargetproperties-example
- key_count: 6
  name: Oracle Enterprise Manager Listblackoutreasons Example
  slug: oracle-enterprise-manager-listblackoutreasons-example
- key_count: 6
  name: Oracle Enterprise Manager Listblackouts Example
  slug: oracle-enterprise-manager-listblackouts-example
- key_count: 6
  name: Oracle Enterprise Manager Listglobaltargetproperties Example
  slug: oracle-enterprise-manager-listglobaltargetproperties-example
- key_count: 6
  name: Oracle Enterprise Manager Listincidents Example
  slug: oracle-enterprise-manager-listincidents-example
- key_count: 6
  name: Oracle Enterprise Manager Listmetricgroups Example
  slug: oracle-enterprise-manager-listmetricgroups-example
- key_count: 6
  name: Oracle Enterprise Manager Listtargets Example
  slug: oracle-enterprise-manager-listtargets-example
- key_count: 6
  name: Oracle Enterprise Manager Modifyglobaltargetproperty Example
  slug: oracle-enterprise-manager-modifyglobaltargetproperty-example
- key_count: 6
  name: Oracle Enterprise Manager Stopblackout Example
  slug: oracle-enterprise-manager-stopblackout-example
- key_count: 6
  name: Oracle Enterprise Manager Suppressincident Example
  slug: oracle-enterprise-manager-suppressincident-example
- key_count: 6
  name: Oracle Enterprise Manager Unsuppressincident Example
  slug: oracle-enterprise-manager-unsuppressincident-example
- key_count: 6
  name: Oracle Enterprise Manager Updatetarget Example
  slug: oracle-enterprise-manager-updatetarget-example
features:
- description: Monitor Oracle databases, hosts, middleware, and custom applications with configurable metrics, thresholds, and alerting.
  name: Target Monitoring
- description: Correlate events into actionable incidents with severity, priority, escalation, and automated notification workflows.
  name: Incident Management
- description: Schedule maintenance windows to suppress monitoring alerts during planned downtime without losing data collection.
  name: Blackout Management
- description: Automate database patching, upgrades, and fleet maintenance with Gold Images and compliance reporting.
  name: Database Lifecycle Management
- description: Create and manage multi-step deployment workflows for provisioning, patching, and configuration changes.
  name: Deployment Procedures
- description: Enable Database as a Service with self-service provisioning, quota management, and request workflows.
  name: Cloud Self-Service
finops:
- name: Oracle Enterprise Manager Finops
  service_category: IT Operations Management
  slug: oracle-enterprise-manager-finops
image: /assets/icons/oracle-enterprise-manager.png
integrations:
- description: Visualize Enterprise Manager metrics in Grafana dashboards using the OEM data source plugin.
  name: Grafana
- description: Extend monitoring to OCI resources and hybrid cloud environments through unified management.
  name: Oracle Cloud Infrastructure
- description: Forward incidents to ServiceNow for ITSM integration and automated ticket creation.
  name: ServiceNow
json_schemas:
- name: Annotation
  property_count: 5
  slug: oracle-enterprise-manager-annotation
- name: AnnotationCollection
  property_count: 1
  slug: oracle-enterprise-manager-annotationcollection
- name: Blackout
  property_count: 11
  slug: oracle-enterprise-manager-blackout
- name: BlackoutCollection
  property_count: 5
  slug: oracle-enterprise-manager-blackoutcollection
- name: BlackoutCreateRequest
  property_count: 5
  slug: oracle-enterprise-manager-blackoutcreaterequest
- name: BlackoutDashboard
  property_count: 5
  slug: oracle-enterprise-manager-blackoutdashboard
- name: BlackoutReason
  property_count: 2
  slug: oracle-enterprise-manager-blackoutreason
- name: BlackoutReasonCollection
  property_count: 1
  slug: oracle-enterprise-manager-blackoutreasoncollection
- name: BlackoutReasonCreateRequest
  property_count: 1
  slug: oracle-enterprise-manager-blackoutreasoncreaterequest
- name: BlackoutSchedule
  property_count: 7
  slug: oracle-enterprise-manager-blackoutschedule
- name: BlackoutTarget
  property_count: 3
  slug: oracle-enterprise-manager-blackouttarget
- name: BlackoutTargetCollection
  property_count: 1
  slug: oracle-enterprise-manager-blackouttargetcollection
- name: BlackoutUpdateRequest
  property_count: 4
  slug: oracle-enterprise-manager-blackoutupdaterequest
- name: BulkPropertyUpdateRequest
  property_count: 1
  slug: oracle-enterprise-manager-bulkpropertyupdaterequest
- name: AnnotationCollection
  property_count: 1
  slug: oracle-enterprise-manager-cloud-control-annotation-collection
- name: Annotation
  property_count: 5
  slug: oracle-enterprise-manager-cloud-control-annotation
- name: BlackoutCollection
  property_count: 5
  slug: oracle-enterprise-manager-cloud-control-blackout-collection
- name: BlackoutCreateRequest
  property_count: 4
  slug: oracle-enterprise-manager-cloud-control-blackout-create-request
- name: BlackoutDashboard
  property_count: 5
  slug: oracle-enterprise-manager-cloud-control-blackout-dashboard
- name: BlackoutReasonCollection
  property_count: 1
  slug: oracle-enterprise-manager-cloud-control-blackout-reason-collection
- name: BlackoutReasonCreateRequest
  property_count: 1
  slug: oracle-enterprise-manager-cloud-control-blackout-reason-create-request
- name: BlackoutReason
  property_count: 2
  slug: oracle-enterprise-manager-cloud-control-blackout-reason
- name: BlackoutSchedule
  property_count: 7
  slug: oracle-enterprise-manager-cloud-control-blackout-schedule
- name: Blackout
  property_count: 10
  slug: oracle-enterprise-manager-cloud-control-blackout
- name: BlackoutTargetCollection
  property_count: 1
  slug: oracle-enterprise-manager-cloud-control-blackout-target-collection
- name: BlackoutTarget
  property_count: 3
  slug: oracle-enterprise-manager-cloud-control-blackout-target
- name: BlackoutUpdateRequest
  property_count: 3
  slug: oracle-enterprise-manager-cloud-control-blackout-update-request
- name: BulkPropertyUpdateRequest
  property_count: 1
  slug: oracle-enterprise-manager-cloud-control-bulk-property-update-request
- name: Error
  property_count: 4
  slug: oracle-enterprise-manager-cloud-control-error
- name: EventCollection
  property_count: 1
  slug: oracle-enterprise-manager-cloud-control-event-collection
- name: Event
  property_count: 12
  slug: oracle-enterprise-manager-cloud-control-event
- name: GlobalTargetPropertyCollection
  property_count: 1
  slug: oracle-enterprise-manager-cloud-control-global-target-property-collection
- name: GlobalTargetPropertyCreateRequest
  property_count: 5
  slug: oracle-enterprise-manager-cloud-control-global-target-property-create-request
- name: GlobalTargetProperty
  property_count: 6
  slug: oracle-enterprise-manager-cloud-control-global-target-property
- name: GlobalTargetPropertyUpdateRequest
  property_count: 3
  slug: oracle-enterprise-manager-cloud-control-global-target-property-update-request
- name: IncidentCollection
  property_count: 5
  slug: oracle-enterprise-manager-cloud-control-incident-collection
- name: Incident
  property_count: 18
  slug: oracle-enterprise-manager-cloud-control-incident
- name: MetricColumn
  property_count: 5
  slug: oracle-enterprise-manager-cloud-control-metric-column
- name: MetricDataCollection
  property_count: 1
  slug: oracle-enterprise-manager-cloud-control-metric-data-collection
- name: MetricDataPoint
  property_count: 4
  slug: oracle-enterprise-manager-cloud-control-metric-data-point
- name: MetricGroupCollection
  property_count: 1
  slug: oracle-enterprise-manager-cloud-control-metric-group-collection
- name: MetricGroup
  property_count: 5
  slug: oracle-enterprise-manager-cloud-control-metric-group
- name: MetricTimeSeriesCollection
  property_count: 1
  slug: oracle-enterprise-manager-cloud-control-metric-time-series-collection
- name: MetricTimeSeries
  property_count: 6
  slug: oracle-enterprise-manager-cloud-control-metric-time-series
- name: TargetCollection
  property_count: 5
  slug: oracle-enterprise-manager-cloud-control-target-collection
- name: TargetCreateRequest
  property_count: 5
  slug: oracle-enterprise-manager-cloud-control-target-create-request
- name: TargetPropertyCollection
  property_count: 1
  slug: oracle-enterprise-manager-cloud-control-target-property-collection
- name: TargetProperty
  property_count: 3
  slug: oracle-enterprise-manager-cloud-control-target-property
- name: Target
  property_count: 17
  slug: oracle-enterprise-manager-cloud-control-target
- name: TargetUpdateRequest
  property_count: 1
  slug: oracle-enterprise-manager-cloud-control-target-update-request
- name: Error
  property_count: 4
  slug: oracle-enterprise-manager-error
- name: Event
  property_count: 12
  slug: oracle-enterprise-manager-event
- name: EventCollection
  property_count: 1
  slug: oracle-enterprise-manager-eventcollection
- name: GlobalTargetProperty
  property_count: 6
  slug: oracle-enterprise-manager-globaltargetproperty
- name: GlobalTargetPropertyCollection
  property_count: 1
  slug: oracle-enterprise-manager-globaltargetpropertycollection
- name: GlobalTargetPropertyCreateRequest
  property_count: 5
  slug: oracle-enterprise-manager-globaltargetpropertycreaterequest
- name: GlobalTargetPropertyUpdateRequest
  property_count: 3
  slug: oracle-enterprise-manager-globaltargetpropertyupdaterequest
- name: Incident
  property_count: 18
  slug: oracle-enterprise-manager-incident
- name: IncidentCollection
  property_count: 5
  slug: oracle-enterprise-manager-incidentcollection
- name: MetricColumn
  property_count: 5
  slug: oracle-enterprise-manager-metriccolumn
- name: MetricDataCollection
  property_count: 1
  slug: oracle-enterprise-manager-metricdatacollection
- name: MetricDataPoint
  property_count: 4
  slug: oracle-enterprise-manager-metricdatapoint
- name: MetricGroup
  property_count: 5
  slug: oracle-enterprise-manager-metricgroup
- name: MetricGroupCollection
  property_count: 1
  slug: oracle-enterprise-manager-metricgroupcollection
- name: MetricTimeSeries
  property_count: 6
  slug: oracle-enterprise-manager-metrictimeseries
- name: MetricTimeSeriesCollection
  property_count: 1
  slug: oracle-enterprise-manager-metrictimeseriescollection
- name: Oracle Enterprise Manager Target
  property_count: 19
  slug: oracle-enterprise-manager-target
- name: TargetCollection
  property_count: 5
  slug: oracle-enterprise-manager-targetcollection
- name: TargetCreateRequest
  property_count: 5
  slug: oracle-enterprise-manager-targetcreaterequest
- name: TargetProperty
  property_count: 3
  slug: oracle-enterprise-manager-targetproperty
- name: TargetPropertyCollection
  property_count: 1
  slug: oracle-enterprise-manager-targetpropertycollection
- name: TargetUpdateRequest
  property_count: 1
  slug: oracle-enterprise-manager-targetupdaterequest
json_structures:
- name: Oracle Enterprise Manager Cloud Control Annotation Collection Structure
  property_count: 1
  slug: oracle-enterprise-manager-cloud-control-annotation-collection-structure
- name: Oracle Enterprise Manager Cloud Control Annotation Structure
  property_count: 5
  slug: oracle-enterprise-manager-cloud-control-annotation-structure
- name: Oracle Enterprise Manager Cloud Control Blackout Collection Structure
  property_count: 5
  slug: oracle-enterprise-manager-cloud-control-blackout-collection-structure
- name: Oracle Enterprise Manager Cloud Control Blackout Create Request Structure
  property_count: 4
  slug: oracle-enterprise-manager-cloud-control-blackout-create-request-structure
- name: Oracle Enterprise Manager Cloud Control Blackout Dashboard Structure
  property_count: 5
  slug: oracle-enterprise-manager-cloud-control-blackout-dashboard-structure
- name: Oracle Enterprise Manager Cloud Control Blackout Reason Collection Structure
  property_count: 1
  slug: oracle-enterprise-manager-cloud-control-blackout-reason-collection-structure
- name: Oracle Enterprise Manager Cloud Control Blackout Reason Create Request Structure
  property_count: 1
  slug: oracle-enterprise-manager-cloud-control-blackout-reason-create-request-structure
- name: Oracle Enterprise Manager Cloud Control Blackout Reason Structure
  property_count: 2
  slug: oracle-enterprise-manager-cloud-control-blackout-reason-structure
- name: Oracle Enterprise Manager Cloud Control Blackout Schedule Structure
  property_count: 7
  slug: oracle-enterprise-manager-cloud-control-blackout-schedule-structure
- name: Oracle Enterprise Manager Cloud Control Blackout Structure
  property_count: 10
  slug: oracle-enterprise-manager-cloud-control-blackout-structure
- name: Oracle Enterprise Manager Cloud Control Blackout Target Collection Structure
  property_count: 1
  slug: oracle-enterprise-manager-cloud-control-blackout-target-collection-structure
- name: Oracle Enterprise Manager Cloud Control Blackout Target Structure
  property_count: 3
  slug: oracle-enterprise-manager-cloud-control-blackout-target-structure
- name: Oracle Enterprise Manager Cloud Control Blackout Update Request Structure
  property_count: 3
  slug: oracle-enterprise-manager-cloud-control-blackout-update-request-structure
- name: Oracle Enterprise Manager Cloud Control Bulk Property Update Request Structure
  property_count: 1
  slug: oracle-enterprise-manager-cloud-control-bulk-property-update-request-structure
- name: Oracle Enterprise Manager Cloud Control Error Structure
  property_count: 4
  slug: oracle-enterprise-manager-cloud-control-error-structure
- name: Oracle Enterprise Manager Cloud Control Event Collection Structure
  property_count: 1
  slug: oracle-enterprise-manager-cloud-control-event-collection-structure
- name: Oracle Enterprise Manager Cloud Control Event Structure
  property_count: 12
  slug: oracle-enterprise-manager-cloud-control-event-structure
- name: Oracle Enterprise Manager Cloud Control Global Target Property Collection Structure
  property_count: 1
  slug: oracle-enterprise-manager-cloud-control-global-target-property-collection-structure
- name: Oracle Enterprise Manager Cloud Control Global Target Property Create Request Structure
  property_count: 5
  slug: oracle-enterprise-manager-cloud-control-global-target-property-create-request-structure
- name: Oracle Enterprise Manager Cloud Control Global Target Property Structure
  property_count: 6
  slug: oracle-enterprise-manager-cloud-control-global-target-property-structure
- name: Oracle Enterprise Manager Cloud Control Global Target Property Update Request Structure
  property_count: 3
  slug: oracle-enterprise-manager-cloud-control-global-target-property-update-request-structure
- name: Oracle Enterprise Manager Cloud Control Incident Collection Structure
  property_count: 5
  slug: oracle-enterprise-manager-cloud-control-incident-collection-structure
- name: Oracle Enterprise Manager Cloud Control Incident Structure
  property_count: 18
  slug: oracle-enterprise-manager-cloud-control-incident-structure
- name: Oracle Enterprise Manager Cloud Control Metric Column Structure
  property_count: 5
  slug: oracle-enterprise-manager-cloud-control-metric-column-structure
- name: Oracle Enterprise Manager Cloud Control Metric Data Collection Structure
  property_count: 1
  slug: oracle-enterprise-manager-cloud-control-metric-data-collection-structure
- name: Oracle Enterprise Manager Cloud Control Metric Data Point Structure
  property_count: 4
  slug: oracle-enterprise-manager-cloud-control-metric-data-point-structure
- name: Oracle Enterprise Manager Cloud Control Metric Group Collection Structure
  property_count: 1
  slug: oracle-enterprise-manager-cloud-control-metric-group-collection-structure
- name: Oracle Enterprise Manager Cloud Control Metric Group Structure
  property_count: 5
  slug: oracle-enterprise-manager-cloud-control-metric-group-structure
- name: Oracle Enterprise Manager Cloud Control Metric Time Series Collection Structure
  property_count: 1
  slug: oracle-enterprise-manager-cloud-control-metric-time-series-collection-structure
- name: Oracle Enterprise Manager Cloud Control Metric Time Series Structure
  property_count: 6
  slug: oracle-enterprise-manager-cloud-control-metric-time-series-structure
- name: Oracle Enterprise Manager Cloud Control Target Collection Structure
  property_count: 5
  slug: oracle-enterprise-manager-cloud-control-target-collection-structure
- name: Oracle Enterprise Manager Cloud Control Target Create Request Structure
  property_count: 5
  slug: oracle-enterprise-manager-cloud-control-target-create-request-structure
- name: Oracle Enterprise Manager Cloud Control Target Property Collection Structure
  property_count: 1
  slug: oracle-enterprise-manager-cloud-control-target-property-collection-structure
- name: Oracle Enterprise Manager Cloud Control Target Property Structure
  property_count: 3
  slug: oracle-enterprise-manager-cloud-control-target-property-structure
- name: Oracle Enterprise Manager Cloud Control Target Structure
  property_count: 17
  slug: oracle-enterprise-manager-cloud-control-target-structure
- name: Oracle Enterprise Manager Cloud Control Target Update Request Structure
  property_count: 1
  slug: oracle-enterprise-manager-cloud-control-target-update-request-structure
- name: Oracle Enterprise Manager Structure
  property_count: 0
  slug: oracle-enterprise-manager-structure
jsonld:
- class_count: 0
  name: Oracle Enterprise Manager Cloud Control Context
  property_count: 0
  slug: oracle-enterprise-manager-cloud-control-context
- class_count: 9
  name: Oracle Enterprise Manager Context
  property_count: 13
  slug: oracle-enterprise-manager-context
layout: provider
mcp_servers:
- description: Candidate MCP server tool list derived one-to-one from the Oracle Enterprise Manager Cloud Control REST API OpenAPI operations. Oracle publishes MCP servers for several products (Oracle Database, MySQ
  name: Oracle Enterprise Manager MCP Server
  slug: oracle-enterprise-manager-mcp-server
modified: '2026-06-20'
name: Oracle Enterprise Manager
nav: Providers
network: true
overview: 'Oracle Enterprise Manager publishes 6 APIs on the [APIs.io](https://apis.io/) network, including Blackouts API, Events API, Global Target Properties API, and 3 more. Tagged areas include Cloud Management, Database Management, Enterprise Management, Infrastructure Management, and Monitoring.


  The Oracle Enterprise Manager catalog on APIs.io includes 2 JSON-LD contexts and 2 Spectral governance rulesets.


  Oracle Enterprise Manager''s developer surface includes authentication, changelog, CLI, developer portal, documentation, support, pricing, and 32 more developer resources.'
plans:
- name: Oracle Enterprise Manager Plans Pricing
  plan_count: 6
  slug: oracle-enterprise-manager-plans-pricing
random_paper: 20
rate_limits:
- limit_count: 3
  name: Oracle Enterprise Manager Rate Limits
  slug: oracle-enterprise-manager-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: Oracle Enterprise Manager API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: oracle-enterprise-manager-jsonschema-spectral-rules
- effective_rule_count: 58
  extends:
  - spectral:oas
  name: Oracle Enterprise Manager API Rules
  rule_count: 17
  severity_counts:
    error: 8
    hint: 0
    info: 2
    warn: 7
  slug: oracle-enterprise-manager-spectral-rules
score:
  band: developing
  composite: 54.0
  coverage:
    artifact_dirs: 29
    catalog_gap: 47.5
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 36.8
    commercial_clarity: 36.8
    contract_governance: 18.2
    contract_quality: 73.0
    developer_ergonomics: 69.0
    discoverability: 75.9
    governance: 18.2
    operational_transparency: 36.8
  previous_composite: 54.0
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 6
    mcp: derived
  schema_version: 0.17.2
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/oracle-enterprise-manager/refs/heads/main/screenshots/oracle-enterprise-manager-2026-06-20T191128.png
security:
- kind: authentication
  name: Oracle Enterprise Manager Authentication
  slug: oracle-enterprise-manager-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Oracle Enterprise Manager Domain Security
  slug: oracle-enterprise-manager-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: oracle-enterprise-manager
tags:
- Cloud Management
- Database Management
- Enterprise Management
- Infrastructure Management
- Monitoring
- Oracle
use_cases:
- description: Centralized monitoring of Oracle databases, hosts, middleware, and applications with real-time metrics and alerting.
  name: Infrastructure Monitoring
- description: Fleet-level database patching using Gold Images with compliance validation and rollback capabilities.
  name: Automated Patching
- description: Detect, triage, and resolve infrastructure issues using correlated incidents with annotations and escalation.
  name: Incident Response
- description: Analyze metric trends over time to forecast resource needs and optimize infrastructure utilization.
  name: Capacity Planning
website: https://www.oracle.com/enterprise-manager/
---
