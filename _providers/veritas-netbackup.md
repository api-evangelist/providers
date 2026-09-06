---
access_model:
  confidence: medium
  label: Enterprise
  onboarding: unknown
  pricing: enterprise
  public: false
  source:
  - plans
  - authentication
  - security
  trial: false
  try_now: false
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
    mcp_server: false
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 32.3
  scored_at: '2026-09-05'
agentic_access:
- acting_count: 13
  human_in_the_loop: 0
  name: Veritas Netbackup Agentic Access
  operation_count: 27
  slug: veritas-netbackup-agentic-access
  summary_line: 27 operations · 13 acting
api_count: 1
apis:
- description: API for managing NetBackup jobs including getting job details, listing jobs by filter, restarting, resuming, suspending, canceling, and deleting jobs, and retrieving job file lists and logs.
  name: NetBackup Administration API
  slug: netbackup-administration-api
- description: API for managing NetBackup assets including servers, clients, and storage devices.
  name: NetBackup Asset Management API
  slug: netbackup-asset-management-api
- description: API endpoints for managing authentication, authorization, certificates, credentials, tokens, and security audit logging configurations.
  name: NetBackup Security API
  slug: netbackup-security-api
- description: API for managing backup images, catalogs, and media retention.
  name: NetBackup Image Management API
  slug: netbackup-image-management-api
- description: API for configuring NetBackup hosts, policies, servers, VM server credentials, and storage settings.
  name: NetBackup Configuration API
  slug: netbackup-configuration-api
- description: API for managing storage consumption, capacity reporting, and backup storage on NetBackup primary servers.
  name: NetBackup Storage API
  slug: netbackup-storage-api
- description: API for VMware and cloud workload recovery operations including restore and instant access.
  name: NetBackup Recovery API
  slug: netbackup-recovery-api
- description: API for managing role-based access control, permissions, access rules, and access control lists.
  name: NetBackup RBAC Administration API
  slug: netbackup-rbac-administration-api
- description: API for managing entitlements and tracking Front-end Terabytes (FETBs) consumption for NetBackup licensing.
  name: NetBackup Licensing API
  slug: netbackup-licensing-api
- description: API for managing service-level objectives (SLOs), protection plans, and subscription handling for backup operations.
  name: NetBackup Service Catalog API
  slug: netbackup-service-catalog-api
- description: API for managing alerts and notification operations in NetBackup environments.
  name: NetBackup Manage API
  slug: netbackup-manage-api
- description: API for status code resolution and error reference to assist with troubleshooting NetBackup issues.
  name: NetBackup Troubleshooting API
  slug: netbackup-troubleshooting-api
- description: REST API for accessing NetBackup IT Analytics report data, exporting reports in JSON, XML, HTML, PDF, and CSV formats, and exporting custom dashboards.
  name: NetBackup IT Analytics REST API
  slug: netbackup-it-analytics-rest-api
- description: REST API for the NetBackup Self Service portal providing backup utilization data, protection status, tenant management, and self-service backup and restore operations.
  name: NetBackup Self Service REST API
  slug: netbackup-self-service-rest-api
- description: REST API for controlling all aspects of NetBackup Flex Scale configuration including infrastructure monitoring, user management, node management, patch upgrades, and storage licensing.
  name: NetBackup Flex Scale REST API
  slug: netbackup-flex-scale-rest-api
- baseURL: https://netbackup-primary-server:1556/netbackup
  baseurl_source: declared
  description: Manage NetBackup clients including listing registered clients, retrieving client configuration details, and managing client-server trust relationships.
  name: Veritas NetBackup Clients API
  slug: veritas-netbackup-clients-api
- baseURL: https://netbackup-primary-server:1556/netbackup
  baseurl_source: declared
  description: Query the NetBackup image catalog to retrieve backup image metadata, search for images by policy or client, and manage image lifecycle operations such as expiration and duplication.
  name: Veritas NetBackup Images API
  slug: veritas-netbackup-images-api
- baseURL: https://netbackup-primary-server:1556/netbackup
  baseurl_source: declared
  description: Manage and monitor backup, restore, and administrative jobs. Retrieve job details, list jobs by filter criteria, cancel, restart, suspend, and resume jobs, and access job file lists and try logs.
  name: Veritas NetBackup Jobs API
  slug: veritas-netbackup-jobs-api
- baseURL: https://netbackup-primary-server:1556/netbackup
  baseurl_source: declared
  description: Authenticate to the NetBackup REST API and obtain a JSON Web Token for subsequent API requests.
  name: Veritas NetBackup Login API
  slug: veritas-netbackup-login-api
- baseURL: https://netbackup-primary-server:1556/netbackup
  baseurl_source: declared
  description: Create, retrieve, update, and delete backup policies. Manage policy schedules, client lists, and backup selections that define what data gets backed up, when, and how.
  name: Veritas NetBackup Policies API
  slug: veritas-netbackup-policies-api
artifact_total: 198
collections:
- collection_type: postman
  name: Veritas NetBackup REST Clients API
  slug: postman-veritas-netbackup-clients-api
- collection_type: postman
  name: Veritas NetBackup REST Clients Images API
  slug: postman-veritas-netbackup-images-api
- collection_type: postman
  name: Veritas NetBackup REST Clients Jobs API
  slug: postman-veritas-netbackup-jobs-api
- collection_type: postman
  name: Veritas NetBackup REST Clients Login API
  slug: postman-veritas-netbackup-login-api
- collection_type: postman
  name: Veritas NetBackup REST Clients Policies API
  slug: postman-veritas-netbackup-policies-api
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Veritas NetBackup REST Clients API
  slug: open-veritas-netbackup-clients-api
- collection_type: open
  name: Veritas NetBackup REST Clients Images API
  slug: open-veritas-netbackup-images-api
- collection_type: open
  name: Veritas NetBackup REST Clients Jobs API
  slug: open-veritas-netbackup-jobs-api
- collection_type: open
  name: Veritas NetBackup REST Clients Login API
  slug: open-veritas-netbackup-login-api
- collection_type: open
  name: Veritas NetBackup REST Clients Policies API
  slug: open-veritas-netbackup-policies-api
- collection_type: open
  name: Veritas NetBackup REST API
  slug: open-veritas-netbackup-rest-api
common:
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/veritas-netbackup-capability-edges.yml
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/veritas-netbackup/overview
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/veritas-netbackup-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/veritas-netbackup-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/veritas-netbackup-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/veritas-netbackup-authentication.yml
- group: operate
  title: ''
  type: Support
  url: https://www.veritas.com/support
- group: docs
  title: ''
  type: Documentation
  url: https://www.veritas.com/support/en_US/article.100040135
- group: docs
  title: ''
  type: APIReference
  url: https://www.veritas.com/support/en_US/doc/139300789-139300792-0/index
- group: start
  title: ''
  type: GettingStarted
  url: https://sort.veritas.com/public/documents/nbu/10.3/windowsandunix/productguides/html/getting-started/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.veritas.com/products/backup-and-recovery/netbackup/pricing
- group: operate
  title: ''
  type: Support
  url: https://www.veritas.com/support/en_US/netbackup
- group: operate
  title: ''
  type: Contact
  url: https://www.veritas.com/company/contact
- group: other
  title: ''
  type: KnowledgeCenter
  url: https://www.veritas.com/support/en_US/netbackup.PRODUCT_HOME
- group: docs
  title: ''
  type: Documentation
  url: https://www.veritas.com/support/en_US/netbackup.download
- group: docs
  title: ''
  type: Documentation
  url: https://vox.veritas.com/category/cohesity-discussions/discussions/netbackup
- group: auth
  title: ''
  type: Authentication
  url: https://sort.veritas.com/public/documents/nbu/10.0/windowsandunix/productguides/html/getting-started/
- group: operate
  title: ''
  type: RateLimits
  url: https://sort.veritas.com/documents/netbackup/10.1/productguides
- group: company
  title: ''
  type: Blog
  url: https://www.veritas.com/blogs
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/VeritasOS
- group: build
  title: ''
  type: SDKs
  url: https://github.com/VeritasOS/netbackup-api-code-samples
- group: build
  title: ''
  type: CodeExamples
  url: https://veritasos.github.io/netbackup-api-code-samples/
- group: operate
  title: ''
  type: ChangeLog
  url: https://www.veritas.com/protection/netbackup/whats-new
- group: operate
  title: ''
  type: ReleaseNotes
  url: https://www.veritas.com/support/en_US/doc/103228346-168289021-0/v168307842-168289021
- group: docs
  title: ''
  type: Documentation
  url: https://www.veritas.com/support/en_US/article.100032801
- group: other
  title: ''
  type: X
  url: https://twitter.com/veritastechllc
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/veritas-technologies-llc
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.veritas.com/company/legal/legal-terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.veritas.com/company/privacy
- group: docs
  title: ''
  type: Documentation
  url: https://www.veritas.com/company
- group: docs
  title: ''
  type: Documentation
  url: https://www.veritas.com/protection/netbackup/self-service
- group: docs
  title: ''
  type: Documentation
  url: https://www.veritas.com/support/en_US/article.100043102
- group: docs
  title: ''
  type: Documentation
  url: https://www.veritas.com/support/en_US/article.100052421
created: '2024'
description: Enterprise-grade data protection and backup solution with comprehensive REST APIs for backup, recovery, and data management operations.
examples:
- key_count: 6
  name: Veritas Netbackup Canceljob Example
  slug: veritas-netbackup-canceljob-example
- key_count: 6
  name: Veritas Netbackup Createpolicy Example
  slug: veritas-netbackup-createpolicy-example
- key_count: 6
  name: Veritas Netbackup Deletejob Example
  slug: veritas-netbackup-deletejob-example
- key_count: 6
  name: Veritas Netbackup Deletepolicy Example
  slug: veritas-netbackup-deletepolicy-example
- key_count: 6
  name: Veritas Netbackup Deletepolicyschedule Example
  slug: veritas-netbackup-deletepolicyschedule-example
- key_count: 6
  name: Veritas Netbackup Expireimage Example
  slug: veritas-netbackup-expireimage-example
- key_count: 6
  name: Veritas Netbackup Getclient Example
  slug: veritas-netbackup-getclient-example
- key_count: 6
  name: Veritas Netbackup Getimage Example
  slug: veritas-netbackup-getimage-example
- key_count: 6
  name: Veritas Netbackup Getimagecontents Example
  slug: veritas-netbackup-getimagecontents-example
- key_count: 6
  name: Veritas Netbackup Getjob Example
  slug: veritas-netbackup-getjob-example
- key_count: 6
  name: Veritas Netbackup Getjobfilelist Example
  slug: veritas-netbackup-getjobfilelist-example
- key_count: 6
  name: Veritas Netbackup Getjobtrylogs Example
  slug: veritas-netbackup-getjobtrylogs-example
- key_count: 6
  name: Veritas Netbackup Getpolicy Example
  slug: veritas-netbackup-getpolicy-example
- key_count: 6
  name: Veritas Netbackup Getpolicyschedule Example
  slug: veritas-netbackup-getpolicyschedule-example
- key_count: 6
  name: Veritas Netbackup Listclients Example
  slug: veritas-netbackup-listclients-example
- key_count: 6
  name: Veritas Netbackup Listimages Example
  slug: veritas-netbackup-listimages-example
- key_count: 6
  name: Veritas Netbackup Listjobs Example
  slug: veritas-netbackup-listjobs-example
- key_count: 6
  name: Veritas Netbackup Listpolicies Example
  slug: veritas-netbackup-listpolicies-example
- key_count: 6
  name: Veritas Netbackup Listpolicyclients Example
  slug: veritas-netbackup-listpolicyclients-example
- key_count: 6
  name: Veritas Netbackup Listpolicyschedules Example
  slug: veritas-netbackup-listpolicyschedules-example
- key_count: 6
  name: Veritas Netbackup Login Example
  slug: veritas-netbackup-login-example
- key_count: 9
  name: Veritas Netbackup Rest Client Attributes Example
  slug: veritas-netbackup-rest-client-attributes-example
- key_count: 1
  name: Veritas Netbackup Rest Client List Response Example
  slug: veritas-netbackup-rest-client-list-response-example
- key_count: 1
  name: Veritas Netbackup Rest Client Resource Example
  slug: veritas-netbackup-rest-client-resource-example
- key_count: 3
  name: Veritas Netbackup Rest Error Response Example
  slug: veritas-netbackup-rest-error-response-example
- key_count: 19
  name: Veritas Netbackup Rest Image Attributes Example
  slug: veritas-netbackup-rest-image-attributes-example
- key_count: 1
  name: Veritas Netbackup Rest Image Contents Response Example
  slug: veritas-netbackup-rest-image-contents-response-example
- key_count: 1
  name: Veritas Netbackup Rest Image List Response Example
  slug: veritas-netbackup-rest-image-list-response-example
- key_count: 1
  name: Veritas Netbackup Rest Image Resource Example
  slug: veritas-netbackup-rest-image-resource-example
- key_count: 24
  name: Veritas Netbackup Rest Job Attributes Example
  slug: veritas-netbackup-rest-job-attributes-example
- key_count: 1
  name: Veritas Netbackup Rest Job File List Response Example
  slug: veritas-netbackup-rest-job-file-list-response-example
- key_count: 1
  name: Veritas Netbackup Rest Job List Response Example
  slug: veritas-netbackup-rest-job-list-response-example
- key_count: 1
  name: Veritas Netbackup Rest Job Resource Example
  slug: veritas-netbackup-rest-job-resource-example
- key_count: 1
  name: Veritas Netbackup Rest Job Try Log Response Example
  slug: veritas-netbackup-rest-job-try-log-response-example
- key_count: 4
  name: Veritas Netbackup Rest Login Request Example
  slug: veritas-netbackup-rest-login-request-example
- key_count: 3
  name: Veritas Netbackup Rest Login Response Example
  slug: veritas-netbackup-rest-login-response-example
- key_count: 1
  name: Veritas Netbackup Rest Pagination Meta Example
  slug: veritas-netbackup-rest-pagination-meta-example
- key_count: 9
  name: Veritas Netbackup Rest Policy Attributes Example
  slug: veritas-netbackup-rest-policy-attributes-example
- key_count: 4
  name: Veritas Netbackup Rest Policy Client Example
  slug: veritas-netbackup-rest-policy-client-example
- key_count: 1
  name: Veritas Netbackup Rest Policy Client List Request Example
  slug: veritas-netbackup-rest-policy-client-list-request-example
- key_count: 1
  name: Veritas Netbackup Rest Policy Client List Response Example
  slug: veritas-netbackup-rest-policy-client-list-response-example
- key_count: 1
  name: Veritas Netbackup Rest Policy Create Request Example
  slug: veritas-netbackup-rest-policy-create-request-example
- key_count: 1
  name: Veritas Netbackup Rest Policy List Response Example
  slug: veritas-netbackup-rest-policy-list-response-example
- key_count: 1
  name: Veritas Netbackup Rest Policy Resource Example
  slug: veritas-netbackup-rest-policy-resource-example
- key_count: 8
  name: Veritas Netbackup Rest Policy Schedule Example
  slug: veritas-netbackup-rest-policy-schedule-example
- key_count: 1
  name: Veritas Netbackup Rest Policy Schedule List Response Example
  slug: veritas-netbackup-rest-policy-schedule-list-response-example
- key_count: 1
  name: Veritas Netbackup Rest Policy Schedule Request Example
  slug: veritas-netbackup-rest-policy-schedule-request-example
- key_count: 1
  name: Veritas Netbackup Rest Policy Schedule Resource Example
  slug: veritas-netbackup-rest-policy-schedule-resource-example
- key_count: 6
  name: Veritas Netbackup Restartjob Example
  slug: veritas-netbackup-restartjob-example
- key_count: 6
  name: Veritas Netbackup Resumejob Example
  slug: veritas-netbackup-resumejob-example
- key_count: 6
  name: Veritas Netbackup Suspendjob Example
  slug: veritas-netbackup-suspendjob-example
- key_count: 6
  name: Veritas Netbackup Updatepolicy Example
  slug: veritas-netbackup-updatepolicy-example
- key_count: 6
  name: Veritas Netbackup Updatepolicyclients Example
  slug: veritas-netbackup-updatepolicyclients-example
- key_count: 6
  name: Veritas Netbackup Updatepolicyschedule Example
  slug: veritas-netbackup-updatepolicyschedule-example
features:
- description: Comprehensive backup and recovery for physical, virtual, and cloud workloads across heterogeneous environments.
  name: Enterprise Backup and Recovery
- description: Create and manage backup policies with configurable schedules, retention rules, and client selections.
  name: Policy-Based Protection
- description: Monitor, control, and troubleshoot backup and restore jobs with full lifecycle management via REST API.
  name: Job Management
- description: Query and manage backup image catalogs for tracking, searching, and lifecycle management of backup data.
  name: Catalog Management
- description: Fine-grained RBAC for managing user permissions across NetBackup operations and resources.
  name: Role-Based Access Control
- description: Enable tenant-level self-service backup and restore operations through the Self Service portal API.
  name: Self-Service Portal
- description: Access and export analytics reports and dashboards for backup environment monitoring and capacity planning.
  name: IT Analytics and Reporting
- description: Manage NetBackup Flex Scale appliance infrastructure including nodes, storage, users, and patch upgrades.
  name: Flex Scale Infrastructure
finops:
- name: Veritas Netbackup Finops
  service_category: Backup / Data Protection
  slug: veritas-netbackup-finops
integrations:
- description: Native integration for backup and instant recovery of VMware virtual machines and vSphere environments.
  name: VMware vSphere
- description: Support for backup and recovery of workloads running on AWS, Azure, and Google Cloud Platform.
  name: Cloud Platforms
- description: Container workload protection with backup and recovery support for Kubernetes clusters.
  name: Kubernetes
- description: Application-consistent backup and granular recovery for Oracle and Microsoft SQL Server databases.
  name: Oracle and SQL Server
- description: Comprehensive REST API coverage for programmatic integration with ITSM, orchestration, and monitoring tools.
  name: RESTful API Ecosystem
json_schemas:
- name: ClientAttributes
  property_count: 9
  slug: veritas-netbackup-clientattributes
- name: ClientListResponse
  property_count: 2
  slug: veritas-netbackup-clientlistresponse
- name: ClientResource
  property_count: 1
  slug: veritas-netbackup-clientresource
- name: ErrorResponse
  property_count: 3
  slug: veritas-netbackup-errorresponse
- name: ImageAttributes
  property_count: 19
  slug: veritas-netbackup-imageattributes
- name: ImageContentsResponse
  property_count: 2
  slug: veritas-netbackup-imagecontentsresponse
- name: ImageListResponse
  property_count: 2
  slug: veritas-netbackup-imagelistresponse
- name: ImageResource
  property_count: 1
  slug: veritas-netbackup-imageresource
- name: Veritas NetBackup Job
  property_count: 1
  slug: veritas-netbackup-job
- name: JobAttributes
  property_count: 24
  slug: veritas-netbackup-jobattributes
- name: JobFileListResponse
  property_count: 2
  slug: veritas-netbackup-jobfilelistresponse
- name: JobListResponse
  property_count: 2
  slug: veritas-netbackup-joblistresponse
- name: JobResource
  property_count: 1
  slug: veritas-netbackup-jobresource
- name: JobTryLogResponse
  property_count: 1
  slug: veritas-netbackup-jobtrylogresponse
- name: LoginRequest
  property_count: 4
  slug: veritas-netbackup-loginrequest
- name: LoginResponse
  property_count: 3
  slug: veritas-netbackup-loginresponse
- name: PaginationMeta
  property_count: 1
  slug: veritas-netbackup-paginationmeta
- name: PolicyAttributes
  property_count: 9
  slug: veritas-netbackup-policyattributes
- name: PolicyClient
  property_count: 4
  slug: veritas-netbackup-policyclient
- name: PolicyClientListRequest
  property_count: 1
  slug: veritas-netbackup-policyclientlistrequest
- name: PolicyClientListResponse
  property_count: 1
  slug: veritas-netbackup-policyclientlistresponse
- name: PolicyCreateRequest
  property_count: 1
  slug: veritas-netbackup-policycreaterequest
- name: PolicyListResponse
  property_count: 2
  slug: veritas-netbackup-policylistresponse
- name: PolicyResource
  property_count: 1
  slug: veritas-netbackup-policyresource
- name: PolicySchedule
  property_count: 8
  slug: veritas-netbackup-policyschedule
- name: PolicyScheduleListResponse
  property_count: 1
  slug: veritas-netbackup-policyschedulelistresponse
- name: PolicyScheduleRequest
  property_count: 1
  slug: veritas-netbackup-policyschedulerequest
- name: PolicyScheduleResource
  property_count: 1
  slug: veritas-netbackup-policyscheduleresource
- name: ClientAttributes
  property_count: 9
  slug: veritas-netbackup-rest-client-attributes
- name: ClientListResponse
  property_count: 1
  slug: veritas-netbackup-rest-client-list-response
- name: ClientResource
  property_count: 1
  slug: veritas-netbackup-rest-client-resource
- name: ErrorResponse
  property_count: 3
  slug: veritas-netbackup-rest-error-response
- name: ImageAttributes
  property_count: 19
  slug: veritas-netbackup-rest-image-attributes
- name: ImageContentsResponse
  property_count: 1
  slug: veritas-netbackup-rest-image-contents-response
- name: ImageListResponse
  property_count: 1
  slug: veritas-netbackup-rest-image-list-response
- name: ImageResource
  property_count: 1
  slug: veritas-netbackup-rest-image-resource
- name: JobAttributes
  property_count: 24
  slug: veritas-netbackup-rest-job-attributes
- name: JobFileListResponse
  property_count: 1
  slug: veritas-netbackup-rest-job-file-list-response
- name: JobListResponse
  property_count: 1
  slug: veritas-netbackup-rest-job-list-response
- name: JobResource
  property_count: 1
  slug: veritas-netbackup-rest-job-resource
- name: JobTryLogResponse
  property_count: 1
  slug: veritas-netbackup-rest-job-try-log-response
- name: LoginRequest
  property_count: 4
  slug: veritas-netbackup-rest-login-request
- name: LoginResponse
  property_count: 3
  slug: veritas-netbackup-rest-login-response
- name: PaginationMeta
  property_count: 1
  slug: veritas-netbackup-rest-pagination-meta
- name: PolicyAttributes
  property_count: 9
  slug: veritas-netbackup-rest-policy-attributes
- name: PolicyClientListRequest
  property_count: 1
  slug: veritas-netbackup-rest-policy-client-list-request
- name: PolicyClientListResponse
  property_count: 1
  slug: veritas-netbackup-rest-policy-client-list-response
- name: PolicyClient
  property_count: 4
  slug: veritas-netbackup-rest-policy-client
- name: PolicyCreateRequest
  property_count: 1
  slug: veritas-netbackup-rest-policy-create-request
- name: PolicyListResponse
  property_count: 1
  slug: veritas-netbackup-rest-policy-list-response
- name: PolicyResource
  property_count: 1
  slug: veritas-netbackup-rest-policy-resource
- name: PolicyScheduleListResponse
  property_count: 1
  slug: veritas-netbackup-rest-policy-schedule-list-response
- name: PolicyScheduleRequest
  property_count: 1
  slug: veritas-netbackup-rest-policy-schedule-request
- name: PolicyScheduleResource
  property_count: 1
  slug: veritas-netbackup-rest-policy-schedule-resource
- name: PolicySchedule
  property_count: 8
  slug: veritas-netbackup-rest-policy-schedule
json_structures:
- name: Veritas Netbackup Rest Client Attributes Structure
  property_count: 9
  slug: veritas-netbackup-rest-client-attributes-structure
- name: Veritas Netbackup Rest Client List Response Structure
  property_count: 1
  slug: veritas-netbackup-rest-client-list-response-structure
- name: Veritas Netbackup Rest Client Resource Structure
  property_count: 1
  slug: veritas-netbackup-rest-client-resource-structure
- name: Veritas Netbackup Rest Error Response Structure
  property_count: 3
  slug: veritas-netbackup-rest-error-response-structure
- name: Veritas Netbackup Rest Image Attributes Structure
  property_count: 19
  slug: veritas-netbackup-rest-image-attributes-structure
- name: Veritas Netbackup Rest Image Contents Response Structure
  property_count: 1
  slug: veritas-netbackup-rest-image-contents-response-structure
- name: Veritas Netbackup Rest Image List Response Structure
  property_count: 1
  slug: veritas-netbackup-rest-image-list-response-structure
- name: Veritas Netbackup Rest Image Resource Structure
  property_count: 1
  slug: veritas-netbackup-rest-image-resource-structure
- name: Veritas Netbackup Rest Job Attributes Structure
  property_count: 24
  slug: veritas-netbackup-rest-job-attributes-structure
- name: Veritas Netbackup Rest Job File List Response Structure
  property_count: 1
  slug: veritas-netbackup-rest-job-file-list-response-structure
- name: Veritas Netbackup Rest Job List Response Structure
  property_count: 1
  slug: veritas-netbackup-rest-job-list-response-structure
- name: Veritas Netbackup Rest Job Resource Structure
  property_count: 1
  slug: veritas-netbackup-rest-job-resource-structure
- name: Veritas Netbackup Rest Job Try Log Response Structure
  property_count: 1
  slug: veritas-netbackup-rest-job-try-log-response-structure
- name: Veritas Netbackup Rest Login Request Structure
  property_count: 4
  slug: veritas-netbackup-rest-login-request-structure
- name: Veritas Netbackup Rest Login Response Structure
  property_count: 3
  slug: veritas-netbackup-rest-login-response-structure
- name: Veritas Netbackup Rest Pagination Meta Structure
  property_count: 1
  slug: veritas-netbackup-rest-pagination-meta-structure
- name: Veritas Netbackup Rest Policy Attributes Structure
  property_count: 9
  slug: veritas-netbackup-rest-policy-attributes-structure
- name: Veritas Netbackup Rest Policy Client List Request Structure
  property_count: 1
  slug: veritas-netbackup-rest-policy-client-list-request-structure
- name: Veritas Netbackup Rest Policy Client List Response Structure
  property_count: 1
  slug: veritas-netbackup-rest-policy-client-list-response-structure
- name: Veritas Netbackup Rest Policy Client Structure
  property_count: 4
  slug: veritas-netbackup-rest-policy-client-structure
- name: Veritas Netbackup Rest Policy Create Request Structure
  property_count: 1
  slug: veritas-netbackup-rest-policy-create-request-structure
- name: Veritas Netbackup Rest Policy List Response Structure
  property_count: 1
  slug: veritas-netbackup-rest-policy-list-response-structure
- name: Veritas Netbackup Rest Policy Resource Structure
  property_count: 1
  slug: veritas-netbackup-rest-policy-resource-structure
- name: Veritas Netbackup Rest Policy Schedule List Response Structure
  property_count: 1
  slug: veritas-netbackup-rest-policy-schedule-list-response-structure
- name: Veritas Netbackup Rest Policy Schedule Request Structure
  property_count: 1
  slug: veritas-netbackup-rest-policy-schedule-request-structure
- name: Veritas Netbackup Rest Policy Schedule Resource Structure
  property_count: 1
  slug: veritas-netbackup-rest-policy-schedule-resource-structure
- name: Veritas Netbackup Rest Policy Schedule Structure
  property_count: 8
  slug: veritas-netbackup-rest-policy-schedule-structure
- name: Veritas Netbackup Structure
  property_count: 0
  slug: veritas-netbackup-structure
jsonld:
- class_count: 0
  name: Veritas Netbackup Context
  property_count: 8
  slug: veritas-netbackup-context
- class_count: 0
  name: Veritas Netbackup Rest Context
  property_count: 0
  slug: veritas-netbackup-rest-context
layout: provider
modified: '2026-05-19'
name: Veritas NetBackup
nav: Providers
network: true
overview: 'Veritas NetBackup publishes 5 APIs on the [APIs.io](https://apis.io/) network, including Clients API, Images API, Jobs API, and 2 more. Tagged areas include Backup, Data Protection, Disaster Recovery, Enterprise, and Recovery.


  The Veritas NetBackup catalog on APIs.io includes 2 JSON-LD contexts and 2 Spectral governance rulesets.


  Veritas NetBackup''s developer surface includes authentication, support, documentation, API reference, getting-started guide, pricing, engineering blog, and 26 more developer resources.'
plans:
- name: Veritas Netbackup Plans Pricing
  plan_count: 1
  slug: veritas-netbackup-plans-pricing
random_paper: 4
rate_limits:
- limit_count: 1
  name: Veritas Netbackup Rate Limits
  slug: veritas-netbackup-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: Veritas NetBackup API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: veritas-netbackup-jsonschema-spectral-rules
- effective_rule_count: 56
  extends:
  - spectral:oas
  name: Veritas NetBackup API Rules
  rule_count: 15
  severity_counts:
    error: 8
    hint: 0
    info: 1
    warn: 6
  slug: veritas-netbackup-spectral-rules
score:
  band: developing
  composite: 49.8
  coverage:
    artifact_dirs: 18
    catalog_earned: 52.5
    catalog_earned_first_party: 0.0
    catalog_gap: 62.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 44.7
    commercial_clarity: 44.7
    contract_governance: 13.6
    contract_quality: 71.7
    developer_ergonomics: 59.5
    discoverability: 63.0
    governance: 13.6
    operational_transparency: 23.7
  previous_composite: 49.8
  provenance:
    agentic_access: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 5
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/veritas-netbackup/refs/heads/main/screenshots/veritas-netbackup-2026-06-20T200933.png
security:
- kind: authentication
  name: Veritas Netbackup Authentication
  slug: veritas-netbackup-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Veritas Netbackup Domain Security
  slug: veritas-netbackup-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Veritas Netbackup Vulnerability Disclosure
  slug: veritas-netbackup-vulnerability-disclosure
  summary_line: disclosure policy published
slug: veritas-netbackup
tags:
- Backup
- Data Protection
- Disaster Recovery
- Enterprise
- Recovery
- Storage
use_cases:
- description: Automate backup policy creation, job scheduling, and monitoring through REST API integration with CI/CD pipelines.
  name: Automated Backup Operations
- description: Programmatically manage recovery operations for VMware and cloud workloads with instant access capabilities.
  name: Disaster Recovery Orchestration
- description: Track and report on backup coverage, retention compliance, and security audit events across the enterprise.
  name: Compliance and Audit
- description: Provide self-service backup and restore capabilities to multiple tenants through the Self Service portal API.
  name: Multi-Tenant Backup Management
- description: Use IT Analytics APIs to export reports on storage consumption, backup trends, and capacity forecasting.
  name: Capacity Planning
website: https://www.veritas.com/products/backup-and-recovery/netbackup
---
