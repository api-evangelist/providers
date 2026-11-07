---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - authentication
  - scopes
  - rate-limits
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: false
    idempotency: documented
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: documented
    operation_distinctiveness: mostly
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: verified
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 34.9
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 63
  human_in_the_loop: 11
  name: Microsoft Azure Batch Agentic Access
  operation_count: 114
  slug: microsoft-azure-batch-agentic-access
  summary_line: 114 operations · 63 acting · 11 human-in-the-loop
api_count: 2
apis:
- baseURL: https://{account}.{region}.batch.azure.com
  baseurl_source: declared
  description: The Jobs API from microsoft-azure-batch — 1 operation(s) for jobs. Partial, API Evangelist-authored view; the complete provider contract is the Azure Batch Service API entry below.
  name: microsoft-azure-batch Jobs API
  slug: microsoft-azure-batch-jobs-api
- baseURL: https://{account}.{region}.batch.azure.com
  baseurl_source: declared
  description: The Pools API from microsoft-azure-batch — 2 operation(s) for pools. Partial, API Evangelist-authored view; the complete provider contract is the Azure Batch Service API entry below.
  name: microsoft-azure-batch Pools API
  slug: microsoft-azure-batch-pools-api
- baseURL: https://{account}.{region}.batch.azure.com
  baseurl_source: declared
  description: The Tasks API from microsoft-azure-batch — 1 operation(s) for tasks. Partial, API Evangelist-authored view; the complete provider contract is the Azure Batch Service API entry below.
  name: microsoft-azure-batch Tasks API
  slug: microsoft-azure-batch-tasks-api
- baseURL: https://{account}.{region}.batch.azure.com
  baseurl_source: declared
  description: The Application API from Microsoft Azure Batch — 2 operation(s) for application.
  name: Microsoft Azure Batch Application API
  slug: microsoft-azure-batch-application-api
- baseURL: https://{account}.{region}.batch.azure.com
  baseurl_source: declared
  description: The ApplicationPackage API from Microsoft Azure Batch — 3 operation(s) for applicationpackage.
  name: Microsoft Azure Batch Application Package API
  slug: microsoft-azure-batch-applicationpackage-api
- baseURL: https://{account}.{region}.batch.azure.com
  baseurl_source: declared
  description: The Applications API from Microsoft Azure Batch — 2 operation(s) for applications.
  name: Microsoft Azure Batch Applications API
  slug: microsoft-azure-batch-applications-api
- baseURL: https://{account}.{region}.batch.azure.com
  baseurl_source: declared
  description: The BatchAccount API from Microsoft Azure Batch — 7 operation(s) for batchaccount.
  name: Microsoft Azure Batch Batch Account API
  slug: microsoft-azure-batch-batchaccount-api
- baseURL: https://{account}.{region}.batch.azure.com
  baseurl_source: declared
  description: The DetectorResponses API from Microsoft Azure Batch — 2 operation(s) for detectorresponses.
  name: Microsoft Azure Batch Detector Responses API
  slug: microsoft-azure-batch-detectorresponses-api
- baseURL: https://{account}.{region}.batch.azure.com
  baseurl_source: declared
  description: The Job Schedules API from Microsoft Azure Batch — 5 operation(s) for job schedules.
  name: Microsoft Azure Batch Job Schedules API
  slug: microsoft-azure-batch-job-schedules-api
- baseURL: https://{account}.{region}.batch.azure.com
  baseurl_source: declared
  description: The Location API from Microsoft Azure Batch — 3 operation(s) for location.
  name: Microsoft Azure Batch Location API
  slug: microsoft-azure-batch-location-api
- baseURL: https://{account}.{region}.batch.azure.com
  baseurl_source: declared
  description: The NetworkSecurityPerimeter API from Microsoft Azure Batch — 3 operation(s) for networksecurityperimeter.
  name: Microsoft Azure Batch Network Security Perimeter API
  slug: microsoft-azure-batch-networksecurityperimeter-api
- baseURL: https://{account}.{region}.batch.azure.com
  baseurl_source: declared
  description: The Nodes API from Microsoft Azure Batch — 16 operation(s) for nodes.
  name: Microsoft Azure Batch Nodes API
  slug: microsoft-azure-batch-nodes-api
- baseURL: https://{account}.{region}.batch.azure.com
  baseurl_source: declared
  description: The Operations API from Microsoft Azure Batch — 1 operation(s) for operations.
  name: Microsoft Azure Batch Operations API
  slug: microsoft-azure-batch-operations-api
- baseURL: https://{account}.{region}.batch.azure.com
  baseurl_source: declared
  description: The Pool API from Microsoft Azure Batch — 4 operation(s) for pool.
  name: Microsoft Azure Batch Pool API
  slug: microsoft-azure-batch-pool-api
- baseURL: https://{account}.{region}.batch.azure.com
  baseurl_source: declared
  description: The PrivateLinkResource API from Microsoft Azure Batch — 2 operation(s) for privatelinkresource.
  name: Microsoft Azure Batch Private Link Resource API
  slug: microsoft-azure-batch-privatelinkresource-api
- baseURL: https://management.azure.com
  baseurl_source: declared
  description: The Private Endpoint Connection API from Microsoft Azure Batch — 2 operation(s) for private endpoint connection.
  name: Microsoft Azure Batch Private Endpoint Connection API
  slug: microsoft-azure-batch-private-endpoint-connection-api
artifact_total: 88
collections:
- collection_type: open
  name: Azure Batch Service REST Jobs API
  slug: open-microsoft-azure-batch-jobs-api
- collection_type: open
  name: Azure Batch Service REST Jobs Pools API
  slug: open-microsoft-azure-batch-pools-api
- collection_type: open
  name: Azure Batch Service REST Jobs Tasks API
  slug: open-microsoft-azure-batch-tasks-api
- collection_type: open
  name: Azure Batch Service REST API
  slug: open-microsoft-azure-batch
common:
- group: design
  href: https://artifacts.apis.io/microsoft-azure-batch/rules/microsoft-azure-batch-rules.yml
  title: ''
  type: Spectral
  url: rules/microsoft-azure-batch-rules.yml
- group: design
  href: https://artifacts.apis.io/microsoft-azure-batch/json-ld/microsoft-azure-batch-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/microsoft-azure-batch-context.jsonld
- group: design
  href: https://artifacts.apis.io/microsoft-azure-batch/vocabulary/microsoft-azure-batch-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/microsoft-azure-batch-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/microsoft-azure-batch/errors/microsoft-azure-batch-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/microsoft-azure-batch-problem-types.yml
- group: other
  href: https://artifacts.apis.io/microsoft-azure-batch/hosts/microsoft-azure-batch-hosts.yml
  title: ''
  type: Hosts
  url: hosts/microsoft-azure-batch-hosts.yml
- group: build
  href: https://artifacts.apis.io/microsoft-azure-batch/integrations/microsoft-azure-batch-integration-edges.yml
  title: ''
  type: IntegrationEdges
  url: integrations/microsoft-azure-batch-integration-edges.yml
- group: other
  href: https://artifacts.apis.io/microsoft-azure-batch/vendors/microsoft-azure-batch-vendors.yml
  title: ''
  type: Vendors
  url: vendors/microsoft-azure-batch-vendors.yml
- group: other
  title: ''
  type: Leadership
  url: https://news.microsoft.com/leadership
- group: other
  href: https://artifacts.apis.io/microsoft-azure-batch/capabilities/microsoft-azure-batch-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/microsoft-azure-batch-capability-edges.yml
- group: other
  href: https://artifacts.apis.io/microsoft-azure-batch/overlays/microsoft-azure-batch-batch-service-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/microsoft-azure-batch-batch-service-overlay.yaml
- group: other
  href: https://artifacts.apis.io/microsoft-azure-batch/overlays/microsoft-azure-batch-management-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/microsoft-azure-batch-management-overlay.yaml
- group: auth
  href: https://artifacts.apis.io/microsoft-azure-batch/security/microsoft-azure-batch-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/microsoft-azure-batch-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/microsoft-azure-batch/security/microsoft-azure-batch-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/microsoft-azure-batch-vulnerability-disclosure.yml
- group: company
  title: ''
  type: Website
  url: https://www.microsoft.com/
- group: agent
  href: https://artifacts.apis.io/microsoft-azure-batch/agentic-access/microsoft-azure-batch-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/microsoft-azure-batch-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/microsoft-azure-batch/security/microsoft-azure-batch-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/microsoft-azure-batch-domain-security.yml
- group: auth
  href: https://artifacts.apis.io/microsoft-azure-batch/authentication/microsoft-azure-batch-authentication.yml
  title: ''
  type: Authentication
  url: authentication/microsoft-azure-batch-authentication.yml
- group: auth
  href: https://artifacts.apis.io/microsoft-azure-batch/scopes/microsoft-azure-batch-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/microsoft-azure-batch-scopes.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Azure
- group: start
  title: ''
  type: Portal
  url: https://portal.azure.com/
- group: commercial
  title: ''
  type: Pricing
  url: https://azure.microsoft.com/en-us/pricing/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.microsoft.com/en-us/legal/terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://privacy.microsoft.com/en-us/privacystatement
- group: operate
  title: ''
  type: Support
  url: https://support.microsoft.com/
- group: company
  title: ''
  type: Blog
  url: https://azure.microsoft.com/en-us/blog/feed/
- group: docs
  title: ''
  type: Documentation
  url: https://learn.microsoft.com/en-us/azure/batch/
- group: docs
  title: ''
  type: APIReference
  url: https://learn.microsoft.com/en-us/rest/api/batchservice/
- group: start
  title: ''
  type: GettingStarted
  url: https://learn.microsoft.com/en-us/azure/batch/quick-create-portal
- group: start
  title: ''
  type: DeveloperPortal
  url: https://azure.microsoft.com/en-us/products/batch
- group: start
  title: ''
  type: SignUp
  url: https://azure.microsoft.com/en-us/free/
- group: build
  href: https://artifacts.apis.io/microsoft-azure-batch/packages/microsoft-azure-batch-packages.yml
  title: ''
  type: Packages
  url: packages/microsoft-azure-batch-packages.yml
- group: build
  href: https://artifacts.apis.io/microsoft-azure-batch/packages/microsoft-azure-batch-packages.yml
  title: ''
  type: SDKs
  url: packages/microsoft-azure-batch-packages.yml
- group: build
  href: https://artifacts.apis.io/microsoft-azure-batch/cli/microsoft-azure-batch-cli.yml
  title: ''
  type: CLI
  url: cli/microsoft-azure-batch-cli.yml
- group: agent
  href: https://artifacts.apis.io/microsoft-azure-batch/well-known/microsoft-azure-batch-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/microsoft-azure-batch-well-known.yml
- group: auth
  href: https://artifacts.apis.io/microsoft-azure-batch/well-known/microsoft-azure-batch-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/microsoft-azure-batch-security.txt
- group: auth
  href: https://artifacts.apis.io/microsoft-azure-batch/security/microsoft-azure-batch-vulnerability-disclosure.yml
  title: ''
  type: Security
  url: security/microsoft-azure-batch-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/microsoft-azure-batch/conformance/microsoft-azure-batch-conformance.yml
  title: ''
  type: Compliance
  url: conformance/microsoft-azure-batch-conformance.yml
- group: design
  href: https://artifacts.apis.io/microsoft-azure-batch/conformance/microsoft-azure-batch-conformance.yml
  title: ''
  type: Conformance
  url: conformance/microsoft-azure-batch-conformance.yml
- group: design
  href: https://artifacts.apis.io/microsoft-azure-batch/errors/microsoft-azure-batch-error-codes.yml
  title: ''
  type: ErrorCatalog
  url: errors/microsoft-azure-batch-error-codes.yml
- group: design
  href: https://artifacts.apis.io/microsoft-azure-batch/conventions/microsoft-azure-batch-conventions.yml
  title: ''
  type: Conventions
  url: conventions/microsoft-azure-batch-conventions.yml
- group: design
  href: https://artifacts.apis.io/microsoft-azure-batch/conventions/microsoft-azure-batch-conventions.yml
  title: ''
  type: Idempotency
  url: conventions/microsoft-azure-batch-conventions.yml
- group: design
  href: https://artifacts.apis.io/microsoft-azure-batch/lifecycle/microsoft-azure-batch-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/microsoft-azure-batch-lifecycle.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://azure.status.microsoft/en-us/status
- group: operate
  href: https://artifacts.apis.io/microsoft-azure-batch/lifecycle/microsoft-azure-batch-lifecycle.yml
  title: ''
  type: Deprecation
  url: lifecycle/microsoft-azure-batch-lifecycle.yml
- group: operate
  href: https://artifacts.apis.io/microsoft-azure-batch/changelog/microsoft-azure-batch-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/microsoft-azure-batch-changelog.yml
- group: operate
  href: https://artifacts.apis.io/microsoft-azure-batch/rate-limits/microsoft-azure-batch-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/microsoft-azure-batch-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/microsoft-azure-batch/plans/microsoft-azure-batch-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/microsoft-azure-batch-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/microsoft-azure-batch/data-model/microsoft-azure-batch-data-model.yml
  title: ''
  type: DataModel
  url: data-model/microsoft-azure-batch-data-model.yml
- group: agent
  href: https://artifacts.apis.io/microsoft-azure-batch/llms/microsoft-azure-batch-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/microsoft-azure-batch-llms.txt
- group: agent
  href: https://artifacts.apis.io/microsoft-azure-batch/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: build
  href: https://artifacts.apis.io/microsoft-azure-batch/examples/_index.yml
  title: ''
  type: Examples
  url: examples/_index.yml
- group: commercial
  href: https://artifacts.apis.io/microsoft-azure-batch/finops/microsoft-azure-batch-finops.yml
  title: ''
  type: FinOps
  url: finops/microsoft-azure-batch-finops.yml
- group: build
  title: ''
  type: SourceCode
  url: https://github.com/Azure/azure-rest-api-specs/tree/main/specification/batch
created: '2026-03-13'
description: 'Azure Batch is Microsoft’s managed job-scheduling and cluster-management service for large-scale parallel and high-performance computing workloads. You describe pools of virtual machines, jobs and tasks through a REST API; Batch allocates the compute, schedules the work across it, retries failures, and scales the pool up and down against a formula you supply. Microsoft publishes two machine-readable contracts for it in the open azure-rest-api-specs repository: a 72-operation data plane per Batch account, and a 42-operation Azure Resource Manager control plane for the accounts themselves. There is no charge for Batch; you pay for the virtual machines, storage and networking the pools consume, with Spot VMs as the discount lever. Authentication is Microsoft Entra ID OAuth 2.0 (or a legacy shared key), and effective permission comes from Azure RBAC rather than from OAuth scopes.'
finops:
- has_sources: true
  method: derived
  name: Microsoft Azure Batch Finops
  primary_unit: ''
  service_category: ''
  slug: microsoft-azure-batch-finops
  template: true
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/microsoft-azure-batch.png
json_schemas:
- name: ActivateApplicationPackageParameters
  property_count: 1
  slug: microsoft-azure-batch-activate-application-package-parameters
- name: ApplicationPackage
  property_count: 3
  slug: microsoft-azure-batch-application-package
- name: Application
  property_count: 3
  slug: microsoft-azure-batch-application
- name: BatchAccountCreateParameters
  property_count: 4
  slug: microsoft-azure-batch-batch-account-create-parameters
- name: BatchAccountKeys
  property_count: 3
  slug: microsoft-azure-batch-batch-account-keys
- name: BatchAccountListResult
  property_count: 2
  slug: microsoft-azure-batch-batch-account-list-result
- name: BatchAccount
  property_count: 2
  slug: microsoft-azure-batch-batch-account
- name: BatchAccountUpdateParameters
  property_count: 3
  slug: microsoft-azure-batch-batch-account-update-parameters
- name: BatchApplicationListResult
  property_count: 2
  slug: microsoft-azure-batch-batch-application-list-result
- name: BatchApplication
  property_count: 3
  slug: microsoft-azure-batch-batch-application
- name: BatchJobCreateOptions
  property_count: 16
  slug: microsoft-azure-batch-batch-job-create-options
- name: BatchJobListResult
  property_count: 2
  slug: microsoft-azure-batch-batch-job-list-result
- name: BatchJobPreparationAndReleaseTaskStatusListResult
  property_count: 2
  slug: microsoft-azure-batch-batch-job-preparation-and-release-task-status-list-result
- name: BatchJobScheduleCreateOptions
  property_count: 5
  slug: microsoft-azure-batch-batch-job-schedule-create-options
- name: BatchJobScheduleListResult
  property_count: 2
  slug: microsoft-azure-batch-batch-job-schedule-list-result
- name: BatchJobSchedule
  property_count: 15
  slug: microsoft-azure-batch-batch-job-schedule
- name: BatchJobScheduleUpdateOptions
  property_count: 3
  slug: microsoft-azure-batch-batch-job-schedule-update-options
- name: BatchJob
  property_count: 26
  slug: microsoft-azure-batch-batch-job
- name: BatchJobUpdateOptions
  property_count: 8
  slug: microsoft-azure-batch-batch-job-update-options
- name: BatchLocationQuota
  property_count: 1
  slug: microsoft-azure-batch-batch-location-quota
- name: BatchNodeFileListResult
  property_count: 2
  slug: microsoft-azure-batch-batch-node-file-list-result
- name: BatchNodeRemoteLoginSettings
  property_count: 4
  slug: microsoft-azure-batch-batch-node-remote-login-settings
- name: BatchNode
  property_count: 23
  slug: microsoft-azure-batch-batch-node
- name: BatchNodeUserCreateOptions
  property_count: 5
  slug: microsoft-azure-batch-batch-node-user-create-options
- name: BatchNodeUserUpdateOptions
  property_count: 3
  slug: microsoft-azure-batch-batch-node-user-update-options
- name: BatchPoolCreateOptions
  property_count: 20
  slug: microsoft-azure-batch-batch-pool-create-options
- name: BatchPoolEnableAutoScaleOptions
  property_count: 2
  slug: microsoft-azure-batch-batch-pool-enable-auto-scale-options
- name: BatchPoolReplaceOptions
  property_count: 3
  slug: microsoft-azure-batch-batch-pool-replace-options
- name: BatchPoolResizeOptions
  property_count: 4
  slug: microsoft-azure-batch-batch-pool-resize-options
- name: BatchPool
  property_count: 34
  slug: microsoft-azure-batch-batch-pool
- name: BatchPoolUpdateOptions
  property_count: 13
  slug: microsoft-azure-batch-batch-pool-update-options
- name: BatchTaskCountsResult
  property_count: 2
  slug: microsoft-azure-batch-batch-task-counts-result
- name: BatchTaskCreateOptions
  property_count: 15
  slug: microsoft-azure-batch-batch-task-create-options
- name: BatchTaskGroup
  property_count: 1
  slug: microsoft-azure-batch-batch-task-group
- name: BatchTaskListResult
  property_count: 2
  slug: microsoft-azure-batch-batch-task-list-result
- name: BatchTaskListSubtasksResult
  property_count: 2
  slug: microsoft-azure-batch-batch-task-list-subtasks-result
- name: BatchTask
  property_count: 26
  slug: microsoft-azure-batch-batch-task
- name: CheckNameAvailabilityParameters
  property_count: 2
  slug: microsoft-azure-batch-check-name-availability-parameters
- name: CheckNameAvailabilityResult
  property_count: 3
  slug: microsoft-azure-batch-check-name-availability-result
- name: DetectorListResult
  property_count: 2
  slug: microsoft-azure-batch-detector-list-result
- name: DetectorResponse
  property_count: 3
  slug: microsoft-azure-batch-detector-response
- name: ListApplicationPackagesResult
  property_count: 2
  slug: microsoft-azure-batch-list-application-packages-result
- name: ListApplicationsResult
  property_count: 2
  slug: microsoft-azure-batch-list-applications-result
- name: ListPoolsResult
  property_count: 2
  slug: microsoft-azure-batch-list-pools-result
- name: ListPrivateEndpointConnectionsResult
  property_count: 2
  slug: microsoft-azure-batch-list-private-endpoint-connections-result
- name: ListPrivateLinkResourcesResult
  property_count: 2
  slug: microsoft-azure-batch-list-private-link-resources-result
- name: NetworkSecurityPerimeterConfigurationListResult
  property_count: 2
  slug: microsoft-azure-batch-network-security-perimeter-configuration-list-result
- name: Result of the request to list REST API operations. It contains a list of operations and a URL nextLink to get the next set of results.
  property_count: 2
  slug: microsoft-azure-batch-operation-list-result
- name: OutboundEnvironmentEndpointCollection
  property_count: 2
  slug: microsoft-azure-batch-outbound-environment-endpoint-collection
- name: Pool
  property_count: 4
  slug: microsoft-azure-batch-pool
- name: PrivateEndpointConnection
  property_count: 3
  slug: microsoft-azure-batch-private-endpoint-connection
- name: PrivateLinkResource
  property_count: 3
  slug: microsoft-azure-batch-private-link-resource
- name: SupportedSkusResult
  property_count: 2
  slug: microsoft-azure-batch-supported-skus-result
- name: UploadBatchServiceLogsOptions
  property_count: 4
  slug: microsoft-azure-batch-upload-batch-service-logs-options
- name: UploadBatchServiceLogsResult
  property_count: 2
  slug: microsoft-azure-batch-upload-batch-service-logs-result
jsonld:
- class_count: 120
  name: Microsoft Azure Batch Context
  property_count: 215
  slug: microsoft-azure-batch-context
layout: provider
modified: '2026-09-17'
name: Microsoft Azure Batch
nav: Providers
network: true
overview: 'Microsoft Azure Batch publishes 16 API contracts indexed on the [APIs.io](https://apis.io/) network, including microsoft-azure-batch Jobs API, microsoft-azure-batch Pools API, microsoft-azure-batch Tasks API, and 13 more. Tagged areas include Batch, Compute, Job Scheduling, High Performance Computing, and Cloud.


  The Microsoft Azure Batch catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Microsoft Azure Batch''s developer surface includes authentication, developer portal, pricing, support, engineering blog, documentation, API reference, and 46 more developer resources.'
plans:
- name: Microsoft Azure Batch Plans Pricing
  plan_count: 0
  slug: microsoft-azure-batch-plans-pricing
random_paper: 1
rate_limits:
- limit_count: 11
  name: Microsoft Azure Batch Rate Limits
  slug: microsoft-azure-batch-rate-limits
rules:
- authorship: generated
  effective_rule_count: 94
  extends:
  - spectral:oas
  name: Microsoft Azure Batch API Rules
  rule_count: 53
  severity_counts:
    error: 44
    hint: 0
    info: 3
    warn: 6
  slug: microsoft-azure-batch-rules
scopes:
- name: Microsoft Azure Batch Scopes
  scope_count: 2
  slug: microsoft-azure-batch-scopes
  summary_line: 2 scopes · implicit
score:
  band: exemplar
  composite: 67.9
  coverage:
    artifact_dirs: 35
    catalog_earned: 74.8
    catalog_earned_first_party: 12.0
    catalog_gap: 40.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 4.1
  facets:
    access_clarity: 60.5
    contract_governance: 35.6
    contract_quality: 61.3
    developer_ergonomics: 73.2
    discoverability: 67.9
    operational_transparency: 84.2
  previous_composite: 63.8
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 64.7
      derived: 0
      marker_coverage: 0.0
      total: 17
    mcp: derived
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
    score: 0.0
screenshot: https://apis.io/screenshots/microsoft-azure-batch/microsoft-azure-batch-2026-06-20T185401.png
security:
- kind: authentication
  name: Microsoft Azure Batch Authentication
  slug: microsoft-azure-batch-authentication
  summary_line: oauth2/shared-key · 3 schemes
- kind: domain-security
  name: Microsoft Azure Batch Domain Security
  slug: microsoft-azure-batch-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Microsoft Azure Batch Vulnerability Disclosure
  slug: microsoft-azure-batch-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Microsoft Azure Batch Trust Center
  slug: microsoft-azure-batch-trust-center
  summary_line: GDPR
skill_count: 2
skills:
- name: microsoft-azure-batch-run-a-batch-workload
  slug: microsoft-azure-batch-run-a-batch-workload
- name: microsoft-azure-batch-scale-and-schedule
  slug: microsoft-azure-batch-scale-and-schedule
slug: microsoft-azure-batch
tags:
- Batch
- Compute
- Job Scheduling
- High Performance Computing
- Cloud
- Microsoft
- Microsoft Azure
- Parallel Processing
- Scheduling
- Infrastructure
website: https://www.microsoft.com/
---
