---
access_model:
  confidence: high
  label: Free · Self-serve signup
  onboarding: self-serve
  pricing: free
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
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 34.0
  scored_at: '2026-09-01'
agentic_access:
- acting_count: 13
  human_in_the_loop: 1
  name: Splunk Agentic Access
  operation_count: 26
  slug: splunk-agentic-access
  summary_line: 26 operations · 13 acting · 1 human-in-the-loop
api_count: 1
apis:
- description: API monitoring checks to see if API-connected resources are available, working properly and responding to calls.
  name: Splunk
  slug: splunk
- description: The Splunk Cloud Platform REST API provides a subset of the Splunk Enterprise REST API endpoints for managing and interacting with your Splunk Cloud Platform deployment. Access requires port 8089 to b
  name: Splunk Cloud Platform REST API
  slug: splunk-cloud-platform-rest-api
- description: The Admin Config Service (ACS) is a cloud-native API that provides programmatic self-service administration capabilities for Splunk Cloud Platform. Administrators can use the ACS API to manage indexes
  name: Splunk Cloud Admin Config Service (ACS) API
  slug: splunk-cloud-admin-config-service-api
- description: The Splunk Observability Cloud API provides REST endpoints for sending and managing metrics, traces, and events. It supports infrastructure monitoring, application performance monitoring (APM), real u
  name: Splunk Observability Cloud API
  slug: splunk-observability-cloud-api
- description: 'The Splunk SOAR REST API enables programmatic creation, updating, and management of security automation objects including containers, assets, playbooks, indicators, lists, and audit records. REST API '
  name: Splunk SOAR REST API
  slug: splunk-soar-rest-api
- description: The Splunk Enterprise Security API provides REST endpoints for accessing and modifying findings, investigations, risk scores, assets, and identities in Splunk Enterprise Security. It includes an OpenA
  name: Splunk Enterprise Security API
  slug: splunk-enterprise-security-api
- description: The Splunk IT Service Intelligence (ITSI) REST API allows bulk creation and updating of ITOA interface objects such as entities, services, and KPI base searches. ITSI is a monitoring and analytics sol
  name: Splunk IT Service Intelligence (ITSI) REST API
  slug: splunk-itsi-rest-api
- description: The Splunk HTTP Event Collector (HEC) is a high-performance REST API data input that accepts JSON or raw text data sent over HTTP or HTTPS. It uses token-based authentication and provides endpoints fo
  name: Splunk HTTP Event Collector (HEC) API
  slug: splunk-http-event-collector-api
- description: The Splunk Intelligence Management (formerly ThreatStream) API provides REST v2.0 endpoints for managing threat intelligence data including indicators, observables, and intelligence sources. It suppor
  name: Splunk Intelligence Management API
  slug: splunk-intelligence-management-api
- description: The Splunk SOAR Playbook Automation API provides Python APIs for developing playbooks and automation within Splunk SOAR. It includes container, playbook, data access, vault, network, and session autom
  name: Splunk SOAR Playbook Automation API
  slug: splunk-soar-playbook-automation-api
- description: The Splunk AppInspect API validates Splunk apps and add-ons against Splunk best practices and requirements for publishing to Splunkbase or installing on Splunk Cloud Platform. It provides automated ap
  name: Splunk AppInspect API
  slug: splunk-appinspect-api
- description: Endpoints for configuring and managing data inputs including monitors, TCP/UDP inputs, scripted inputs, and HTTP Event Collector (HEC) tokens. Data inputs define how Splunk ingests data.
  name: Splunk Data Inputs API
  slug: splunk-data-inputs-api
- description: Endpoints for managing Splunk indexes, which store and organize ingested data. Indexes can be created, modified, listed, and configured for retention and storage policies.
  name: Splunk Index API
  slug: splunk-index-api
- description: Endpoints for creating, managing, and retrieving search jobs and their results. Splunk search processing language (SPL) queries are submitted as search jobs that run asynchronously.
  name: Splunk Search API
  slug: splunk-search-api
arazzos:
- description: Dispatch a long search, finalize it early, read partial results, then delete the job.
  name: Splunk Finalize, Read, and Clean Up a Search Job
  slug: splunk-control-and-cleanup-search-workflow
- description: Provision a HEC token with acknowledgment, send a JSON event, and confirm it was indexed.
  name: Splunk HEC Ingest an Event and Confirm Indexing
  slug: splunk-hec-ingest-and-acknowledge-workflow
- description: Create an event index, verify it, then create a file monitor input that feeds it.
  name: Splunk Provision an Index and Attach a Monitor Input
  slug: splunk-provision-index-and-monitor-workflow
- description: Send raw text to HEC, then run an SPL search and poll it to confirm the data landed.
  name: Splunk Ingest Raw Data then Search for It
  slug: splunk-raw-ingest-and-search-workflow
- description: Dispatch an SPL search, poll the job until it finishes, then read the results.
  name: Splunk Run a Search Job and Retrieve Results
  slug: splunk-run-search-job-workflow
- description: Run an SPL search, wait for it to finish, then pull the untransformed events.
  name: Splunk Search and Retrieve Raw Events
  slug: splunk-search-events-workflow
artifact_total: 180
collections:
- collection_type: postman
  name: Splunk Enterprise REST API
  slug: postman-splunk-enterprise-rest-api
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Splunk Enterprise REST Data Inputs API
  slug: open-splunk-data-inputs-api
- collection_type: open
  name: Splunk Enterprise REST API
  slug: open-splunk-enterprise-rest-api
- collection_type: open
  name: Splunk Enterprise REST Data Inputs Index API
  slug: open-splunk-index-api
- collection_type: open
  name: Splunk Enterprise REST Data Inputs Search API
  slug: open-splunk-search-api
common:
- group: operate
  title: ''
  type: IssueTracker
  url: https://github.com/signalfx/splunk-otel-collector/issues
- group: operate
  title: ''
  type: Releases
  url: https://github.com/signalfx/splunk-otel-collector/releases
- group: build
  title: ''
  type: CodeOfConduct
  url: https://github.com/signalfx/splunk-otel-collector/blob/main/CODE_OF_CONDUCT.md
- group: docs
  title: ''
  type: ContributionGuide
  url: https://github.com/signalfx/splunk-otel-collector/blob/main/CONTRIBUTING.md
- group: other
  title: ''
  type: ParentCompany
  url: https://apis.io/providers/cisco/
- group: commercial
  title: ''
  type: License
  url: https://github.com/signalfx/splunk-otel-collector/blob/main/LICENSE
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/splunk-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/splunk-trust-center.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/splunk-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/splunk-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/splunk-authentication.yml
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/splunk/overview
- group: design
  title: ''
  type: Arazzo
  url: arazzo/splunk-control-and-cleanup-search-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/splunk-hec-ingest-and-acknowledge-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/splunk-provision-index-and-monitor-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/splunk-raw-ingest-and-search-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/splunk-run-search-job-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/splunk-search-events-workflow.yml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://dev.splunk.com/
- group: company
  title: ''
  type: Blog
  url: https://www.splunk.com/en_us/blog
- group: operate
  title: ''
  type: Support
  url: https://www.splunk.com/en_us/support-and-services.html
- group: operate
  title: ''
  type: StatusPage
  url: https://www.splunk.com/en_us/customer-success/splunk-services-status.html
- group: docs
  title: Community
  type: Documentation
  url: https://community.splunk.com/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/splunk
- group: docs
  title: ''
  type: Documentation
  url: https://docs.splunk.com/Documentation
- group: docs
  title: Help Center
  type: Documentation
  url: https://help.splunk.com/en
- group: start
  title: ''
  type: GettingStarted
  url: https://dev.splunk.com/enterprise/docs
- group: docs
  title: Developer Tools
  type: Documentation
  url: https://dev.splunk.com/enterprise/docs/devtools/
- group: docs
  title: Downloads
  type: Documentation
  url: https://dev.splunk.com/enterprise/downloads
- group: other
  title: ''
  type: Marketplace
  url: https://splunkbase.splunk.com/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.splunk.com/en_us/products/pricing.html
- group: start
  title: ''
  type: Signup
  url: https://www.splunk.com/en_us/download/splunk-cloud.html
- group: start
  title: Developer License
  type: Signup
  url: https://dev.splunk.com/enterprise/dev_license/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.splunk.com/en_us/legal/terms/terms-of-use.html
- group: commercial
  title: General Terms
  type: TermsOfService
  url: https://www.splunk.com/en_us/legal/splunk-general-terms.html
- group: operate
  title: ''
  type: ChangeLog
  url: https://help.splunk.com/en/splunk-enterprise/release-notes-and-updates
- group: auth
  title: ''
  type: Authentication
  url: https://docs.splunk.com/Documentation/Splunk/latest/RESTUM/RESTusing
- group: build
  title: Python SDK
  type: SDKs
  url: https://github.com/splunk/splunk-sdk-python
- group: build
  title: Java SDK
  type: SDKs
  url: https://github.com/splunk/splunk-sdk-java
- group: build
  title: JavaScript SDK
  type: SDKs
  url: https://github.com/splunk/splunk-sdk-javascript
- group: build
  title: C# SDK
  type: SDKs
  url: https://github.com/splunk/splunk-sdk-csharp-pcl
- group: build
  title: C# SDK Documentation
  type: SDKs
  url: https://dev.splunk.com/enterprise/docs/devtools/csharp
- group: operate
  title: What's New
  type: ChangeLog
  url: https://dev.splunk.com/enterprise/docs/whatsnew/
- group: operate
  title: Release Notes
  type: ChangeLog
  url: https://dev.splunk.com/enterprise/docs/relnotes
- group: docs
  title: Custom REST Endpoints
  type: Documentation
  url: https://dev.splunk.com/enterprise/docs/devtools/customrestendpoints
- group: auth
  title: Auth Tokens
  type: Authentication
  url: https://docs.splunk.com/Documentation/Splunk/latest/Security/UseAuthTokens
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.splunk.com/en_us/legal/privacy-policy.html
- group: auth
  title: ''
  type: Security
  url: https://www.splunk.com/en_us/about-splunk/splunk-data-security-and-privacy.html
- group: build
  title: OpenTelemetry Collector
  type: GitHubRepository
  url: https://github.com/signalfx/splunk-otel-collector
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/splunk
- group: other
  title: ''
  type: X
  url: https://twitter.com/splunk
- group: design
  title: ''
  type: SpectralRules
  url: rules/splunk-spectral-rules.yml
- group: agent
  title: ''
  type: MCPServer
  url: https://github.com/splunk/splunk-mcp-server2
- group: other
  title: ''
  type: Subsidiary
  url: https://apis.io/providers/signalfx/
- group: other
  title: ''
  type: Subsidiary
  url: https://apis.io/providers/splunk-observability/
- group: other
  title: ''
  type: Subsidiary
  url: https://apis.io/providers/splunk-soar/
- group: other
  title: ''
  type: Subsidiary
  url: https://apis.io/providers/victorops/
created: '2025-01-08'
description: Splunk is a platform for searching, monitoring, and analyzing machine-generated big data via a web-style interface.
examples:
- key_count: 6
  name: Splunk Checkackstatus Example
  slug: splunk-checkackstatus-example
- key_count: 6
  name: Splunk Controlsearchjob Example
  slug: splunk-controlsearchjob-example
- key_count: 6
  name: Splunk Createhttpinputtoken Example
  slug: splunk-createhttpinputtoken-example
- key_count: 6
  name: Splunk Createindex Example
  slug: splunk-createindex-example
- key_count: 6
  name: Splunk Createmonitorinput Example
  slug: splunk-createmonitorinput-example
- key_count: 6
  name: Splunk Createsearchjob Example
  slug: splunk-createsearchjob-example
- key_count: 1
  name: Splunk Enterprise Rest Error Response Example
  slug: splunk-enterprise-rest-error-response-example
- key_count: 7
  name: Splunk Enterprise Rest Hec Event Example
  slug: splunk-enterprise-rest-hec-event-example
- key_count: 4
  name: Splunk Enterprise Rest Hec Response Example
  slug: splunk-enterprise-rest-hec-response-example
- key_count: 8
  name: Splunk Enterprise Rest Hec Token Create Request Example
  slug: splunk-enterprise-rest-hec-token-create-request-example
- key_count: 2
  name: Splunk Enterprise Rest Hec Token Example
  slug: splunk-enterprise-rest-hec-token-example
- key_count: 3
  name: Splunk Enterprise Rest Hec Token List Example
  slug: splunk-enterprise-rest-hec-token-list-example
- key_count: 10
  name: Splunk Enterprise Rest Index Create Request Example
  slug: splunk-enterprise-rest-index-create-request-example
- key_count: 2
  name: Splunk Enterprise Rest Index Example
  slug: splunk-enterprise-rest-index-example
- key_count: 3
  name: Splunk Enterprise Rest Index List Example
  slug: splunk-enterprise-rest-index-list-example
- key_count: 7
  name: Splunk Enterprise Rest Index Update Request Example
  slug: splunk-enterprise-rest-index-update-request-example
- key_count: 10
  name: Splunk Enterprise Rest Monitor Input Create Request Example
  slug: splunk-enterprise-rest-monitor-input-create-request-example
- key_count: 2
  name: Splunk Enterprise Rest Monitor Input Example
  slug: splunk-enterprise-rest-monitor-input-example
- key_count: 3
  name: Splunk Enterprise Rest Monitor Input List Example
  slug: splunk-enterprise-rest-monitor-input-list-example
- key_count: 5
  name: Splunk Enterprise Rest Monitor Input Update Request Example
  slug: splunk-enterprise-rest-monitor-input-update-request-example
- key_count: 3
  name: Splunk Enterprise Rest Paging Example
  slug: splunk-enterprise-rest-paging-example
- key_count: 19
  name: Splunk Enterprise Rest Search Job Create Request Example
  slug: splunk-enterprise-rest-search-job-create-request-example
- key_count: 2
  name: Splunk Enterprise Rest Search Job Example
  slug: splunk-enterprise-rest-search-job-example
- key_count: 4
  name: Splunk Enterprise Rest Search Job List Example
  slug: splunk-enterprise-rest-search-job-list-example
- key_count: 6
  name: Splunk Enterprise Rest Search Results Example
  slug: splunk-enterprise-rest-search-results-example
- key_count: 2
  name: Splunk Enterprise Rest Tcp Input Example
  slug: splunk-enterprise-rest-tcp-input-example
- key_count: 3
  name: Splunk Enterprise Rest Tcp Input List Example
  slug: splunk-enterprise-rest-tcp-input-list-example
- key_count: 2
  name: Splunk Enterprise Rest Udp Input Example
  slug: splunk-enterprise-rest-udp-input-example
- key_count: 3
  name: Splunk Enterprise Rest Udp Input List Example
  slug: splunk-enterprise-rest-udp-input-list-example
- key_count: 6
  name: Splunk Exportsearchresults Example
  slug: splunk-exportsearchresults-example
- key_count: 6
  name: Splunk Getindex Example
  slug: splunk-getindex-example
- key_count: 6
  name: Splunk Getmonitorinput Example
  slug: splunk-getmonitorinput-example
- key_count: 6
  name: Splunk Getsearchevents Example
  slug: splunk-getsearchevents-example
- key_count: 6
  name: Splunk Getsearchjob Example
  slug: splunk-getsearchjob-example
- key_count: 6
  name: Splunk Getsearchresults Example
  slug: splunk-getsearchresults-example
- key_count: 6
  name: Splunk Listhttpinputtokens Example
  slug: splunk-listhttpinputtokens-example
- key_count: 6
  name: Splunk Listindexes Example
  slug: splunk-listindexes-example
- key_count: 6
  name: Splunk Listmonitorinputs Example
  slug: splunk-listmonitorinputs-example
- key_count: 6
  name: Splunk Listsearchjobs Example
  slug: splunk-listsearchjobs-example
- key_count: 6
  name: Splunk Listtcpcookedinputs Example
  slug: splunk-listtcpcookedinputs-example
- key_count: 6
  name: Splunk Listtcprawinputs Example
  slug: splunk-listtcprawinputs-example
- key_count: 6
  name: Splunk Listudpinputs Example
  slug: splunk-listudpinputs-example
- key_count: 6
  name: Splunk Sendevent Example
  slug: splunk-sendevent-example
- key_count: 6
  name: Splunk Sendrawevent Example
  slug: splunk-sendrawevent-example
- key_count: 6
  name: Splunk Updateindex Example
  slug: splunk-updateindex-example
- key_count: 6
  name: Splunk Updatemonitorinput Example
  slug: splunk-updatemonitorinput-example
features:
- 'Splunk (now Cisco): hundreds of services across Observability + SIEM'
- 'Detailed pricing: see https://www.splunk.com/en_us/products/pricing.html'
- 'Service: Splunk Enterprise / Cloud (data ingest)'
- 'Service: Splunk Observability Cloud (APM, Logs, RUM, Synthetics)'
- 'Service: Splunk SOAR'
- 'Service: Splunk Enterprise Security (SIEM)'
- 'Service: Splunk ITSI'
- 'Service: Splunk SOC Platform'
finops:
- name: Splunk Finops
  service_category: Observability + SIEM
  slug: splunk-finops
graphqls:
- description: Conceptual GraphQL schema for the Splunk platform, covering search, indexing, data inputs, access control, dashboards, saved searches, metrics, clustering, licensing, and diagnostics.
  name: Splunk GraphQL Schema
  slug: splunk-graphql
image: https://www.splunk.com/content/dam/splunk2/images/icons/favicons/favicon.ico
integrations:
- description: Ingest and analyze AWS CloudTrail, CloudWatch, VPC Flow Logs, and other AWS service data.
  name: AWS
- description: Collect and analyze Azure activity logs, metrics, and diagnostic data.
  name: Azure
- description: Ingest Google Cloud audit logs, metrics, and Pub/Sub messages for cloud monitoring.
  name: Google Cloud
- description: Monitor Kubernetes clusters with metrics, logs, and events from containers and orchestration.
  name: Kubernetes
- description: Integrate Splunk alerts and incidents with ServiceNow ITSM for ticketing and workflow automation.
  name: ServiceNow
- description: Trigger PagerDuty incidents from Splunk alerts for on-call notification and escalation.
  name: PagerDuty
- description: Collect and analyze Cisco network device logs, firewall events, and security telemetry.
  name: Cisco
- description: Ingest CrowdStrike Falcon endpoint detection data for correlated threat analysis.
  name: CrowdStrike
json_schemas:
- name: ErrorResponse
  property_count: 1
  slug: splunk-enterprise-rest-error-response
- name: HecEvent
  property_count: 7
  slug: splunk-enterprise-rest-hec-event
- name: HecResponse
  property_count: 4
  slug: splunk-enterprise-rest-hec-response
- name: HecTokenCreateRequest
  property_count: 8
  slug: splunk-enterprise-rest-hec-token-create-request
- name: HecTokenList
  property_count: 3
  slug: splunk-enterprise-rest-hec-token-list
- name: HecToken
  property_count: 2
  slug: splunk-enterprise-rest-hec-token
- name: IndexCreateRequest
  property_count: 10
  slug: splunk-enterprise-rest-index-create-request
- name: IndexList
  property_count: 3
  slug: splunk-enterprise-rest-index-list
- name: Index
  property_count: 2
  slug: splunk-enterprise-rest-index
- name: IndexUpdateRequest
  property_count: 7
  slug: splunk-enterprise-rest-index-update-request
- name: MonitorInputCreateRequest
  property_count: 10
  slug: splunk-enterprise-rest-monitor-input-create-request
- name: MonitorInputList
  property_count: 3
  slug: splunk-enterprise-rest-monitor-input-list
- name: MonitorInput
  property_count: 2
  slug: splunk-enterprise-rest-monitor-input
- name: MonitorInputUpdateRequest
  property_count: 5
  slug: splunk-enterprise-rest-monitor-input-update-request
- name: Paging
  property_count: 3
  slug: splunk-enterprise-rest-paging
- name: SearchJobCreateRequest
  property_count: 19
  slug: splunk-enterprise-rest-search-job-create-request
- name: SearchJobList
  property_count: 4
  slug: splunk-enterprise-rest-search-job-list
- name: SearchJob
  property_count: 2
  slug: splunk-enterprise-rest-search-job
- name: SearchResults
  property_count: 6
  slug: splunk-enterprise-rest-search-results
- name: TcpInputList
  property_count: 3
  slug: splunk-enterprise-rest-tcp-input-list
- name: TcpInput
  property_count: 2
  slug: splunk-enterprise-rest-tcp-input
- name: UdpInputList
  property_count: 3
  slug: splunk-enterprise-rest-udp-input-list
- name: UdpInput
  property_count: 2
  slug: splunk-enterprise-rest-udp-input
- name: ErrorResponse
  property_count: 1
  slug: splunk-errorresponse
- name: Splunk Event
  property_count: 19
  slug: splunk-event
- name: HecEvent
  property_count: 7
  slug: splunk-hecevent
- name: HecResponse
  property_count: 4
  slug: splunk-hecresponse
- name: HecToken
  property_count: 2
  slug: splunk-hectoken
- name: HecTokenCreateRequest
  property_count: 8
  slug: splunk-hectokencreaterequest
- name: HecTokenList
  property_count: 4
  slug: splunk-hectokenlist
- name: Index
  property_count: 2
  slug: splunk-index
- name: IndexCreateRequest
  property_count: 10
  slug: splunk-indexcreaterequest
- name: IndexList
  property_count: 4
  slug: splunk-indexlist
- name: IndexUpdateRequest
  property_count: 7
  slug: splunk-indexupdaterequest
- name: MonitorInput
  property_count: 2
  slug: splunk-monitorinput
- name: MonitorInputCreateRequest
  property_count: 10
  slug: splunk-monitorinputcreaterequest
- name: MonitorInputList
  property_count: 4
  slug: splunk-monitorinputlist
- name: MonitorInputUpdateRequest
  property_count: 5
  slug: splunk-monitorinputupdaterequest
- name: Paging
  property_count: 3
  slug: splunk-paging
- name: Splunk Search Job
  property_count: 9
  slug: splunk-search-job
- name: SearchJob
  property_count: 2
  slug: splunk-searchjob
- name: SearchJobCreateRequest
  property_count: 19
  slug: splunk-searchjobcreaterequest
- name: SearchJobList
  property_count: 5
  slug: splunk-searchjoblist
- name: SearchResults
  property_count: 6
  slug: splunk-searchresults
- name: TcpInput
  property_count: 2
  slug: splunk-tcpinput
- name: TcpInputList
  property_count: 4
  slug: splunk-tcpinputlist
- name: UdpInput
  property_count: 2
  slug: splunk-udpinput
- name: UdpInputList
  property_count: 4
  slug: splunk-udpinputlist
json_structures:
- name: Splunk Enterprise Rest Error Response Structure
  property_count: 1
  slug: splunk-enterprise-rest-error-response-structure
- name: Splunk Enterprise Rest Hec Event Structure
  property_count: 7
  slug: splunk-enterprise-rest-hec-event-structure
- name: Splunk Enterprise Rest Hec Response Structure
  property_count: 4
  slug: splunk-enterprise-rest-hec-response-structure
- name: Splunk Enterprise Rest Hec Token Create Request Structure
  property_count: 8
  slug: splunk-enterprise-rest-hec-token-create-request-structure
- name: Splunk Enterprise Rest Hec Token List Structure
  property_count: 3
  slug: splunk-enterprise-rest-hec-token-list-structure
- name: Splunk Enterprise Rest Hec Token Structure
  property_count: 2
  slug: splunk-enterprise-rest-hec-token-structure
- name: Splunk Enterprise Rest Index Create Request Structure
  property_count: 10
  slug: splunk-enterprise-rest-index-create-request-structure
- name: Splunk Enterprise Rest Index List Structure
  property_count: 3
  slug: splunk-enterprise-rest-index-list-structure
- name: Splunk Enterprise Rest Index Structure
  property_count: 2
  slug: splunk-enterprise-rest-index-structure
- name: Splunk Enterprise Rest Index Update Request Structure
  property_count: 7
  slug: splunk-enterprise-rest-index-update-request-structure
- name: Splunk Enterprise Rest Monitor Input Create Request Structure
  property_count: 10
  slug: splunk-enterprise-rest-monitor-input-create-request-structure
- name: Splunk Enterprise Rest Monitor Input List Structure
  property_count: 3
  slug: splunk-enterprise-rest-monitor-input-list-structure
- name: Splunk Enterprise Rest Monitor Input Structure
  property_count: 2
  slug: splunk-enterprise-rest-monitor-input-structure
- name: Splunk Enterprise Rest Monitor Input Update Request Structure
  property_count: 5
  slug: splunk-enterprise-rest-monitor-input-update-request-structure
- name: Splunk Enterprise Rest Paging Structure
  property_count: 3
  slug: splunk-enterprise-rest-paging-structure
- name: Splunk Enterprise Rest Search Job Create Request Structure
  property_count: 19
  slug: splunk-enterprise-rest-search-job-create-request-structure
- name: Splunk Enterprise Rest Search Job List Structure
  property_count: 4
  slug: splunk-enterprise-rest-search-job-list-structure
- name: Splunk Enterprise Rest Search Job Structure
  property_count: 2
  slug: splunk-enterprise-rest-search-job-structure
- name: Splunk Enterprise Rest Search Results Structure
  property_count: 6
  slug: splunk-enterprise-rest-search-results-structure
- name: Splunk Enterprise Rest Tcp Input List Structure
  property_count: 3
  slug: splunk-enterprise-rest-tcp-input-list-structure
- name: Splunk Enterprise Rest Tcp Input Structure
  property_count: 2
  slug: splunk-enterprise-rest-tcp-input-structure
- name: Splunk Enterprise Rest Udp Input List Structure
  property_count: 3
  slug: splunk-enterprise-rest-udp-input-list-structure
- name: Splunk Enterprise Rest Udp Input Structure
  property_count: 2
  slug: splunk-enterprise-rest-udp-input-structure
- name: Splunk Structure
  property_count: 0
  slug: splunk-structure
jsonld:
- class_count: 0
  name: Splunk Context
  property_count: 15
  slug: splunk-context
- class_count: 0
  name: Splunk Enterprise Rest Context
  property_count: 0
  slug: splunk-enterprise-rest-context
layout: provider
mcp_servers:
- description: ''
  name: MCP Server
  slug: mcp-server
modified: '2026-08-19'
name: Splunk
nav: Providers
network: true
overview: 'Splunk publishes 3 APIs on the [APIs.io](https://apis.io/) network: Data Inputs API, Index API, and Search API. Tagged areas include Analytics, Data Analysis, Logging, Machine Data, and Monitoring.


  The Splunk catalog on APIs.io includes 2 JSON-LD contexts and 2 Spectral governance rulesets.


  Splunk''s developer surface includes authentication, engineering blog, support, documentation, getting-started guide, pricing, signup flow, and 50 more developer resources.'
plans:
- name: Splunk Plans Pricing
  plan_count: 3
  slug: splunk-plans-pricing
random_paper: 18
rate_limits:
- limit_count: 2
  name: Splunk Rate Limits
  slug: splunk-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: Splunk API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: splunk-jsonschema-spectral-rules
- effective_rule_count: 57
  extends:
  - spectral:oas
  name: Splunk API Rules
  rule_count: 16
  severity_counts:
    error: 8
    hint: 0
    info: 1
    warn: 7
  slug: splunk-spectral-rules
score:
  band: developing
  composite: 46.7
  coverage:
    artifact_dirs: 20
    catalog_gap: 57.5
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 68.4
    commercial_clarity: 68.4
    contract_governance: 13.6
    contract_quality: 35.4
    developer_ergonomics: 69.0
    discoverability: 50.0
    governance: 13.6
    operational_transparency: 34.2
  open_source:
    applies: true
    score: 40.0
  previous_composite: 46.7
  provenance:
    agentic_access: derived
    contracts:
      callable: 0.0
      derived: 3
      marker_coverage: 100.0
      total: 3
  schema_version: 0.18.0
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/splunk/refs/heads/main/screenshots/splunk-2026-06-20T194332.png
security:
- kind: authentication
  name: Splunk Authentication
  slug: splunk-authentication
  summary_line: apiKey/http · 3 schemes
- kind: domain-security
  name: Splunk Domain Security
  slug: splunk-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Splunk Vulnerability Disclosure
  slug: splunk-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Splunk Trust Center
  slug: splunk-trust-center
  summary_line: SOC 2, ISO 27001, ISO 27017, ISO 27018, PCI DSS, HIPAA, FedRAMP, GDPR, CSA STAR
slug: splunk
tags:
- Analytics
- Data Analysis
- Logging
- Machine Data
- Monitoring
- Observability
- Platform
- Security
- SIEM
use_cases:
- description: Centralize security event data for real-time threat detection, investigation, and compliance reporting.
  name: Security Information and Event Management
- description: Monitor infrastructure health, application performance, and service availability across hybrid environments.
  name: IT Operations Monitoring
- description: Collect, index, and analyze log data from servers, applications, and network devices for troubleshooting.
  name: Log Management
- description: Automate security incident triage, enrichment, and response using SOAR playbooks and integrations.
  name: Incident Response Automation
- description: Trace application requests end-to-end to identify bottlenecks and optimize performance.
  name: Application Performance Monitoring
- description: Generate compliance reports and audit trails from indexed data to meet regulatory requirements.
  name: Compliance and Audit
website: https://dev.splunk.com/
---
