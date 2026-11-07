---
access_model:
  confidence: high
  gated: none
  gated_source:
  - onboarding
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  - rate-limits
  - security
  trial: false
  try_now: true
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: negotiable
    consent_identity: false
    delegated_identity: documented
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: derived
    event_surface_described: true
    idempotency: documented
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 37.1
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 26
  human_in_the_loop: 0
  name: Azure Health Agentic Access
  operation_count: 53
  slug: azure-health-agentic-access
  summary_line: 53 operations · 26 acting
api_count: 2
apis:
- baseURL: https://management.azure.com
  baseurl_source: declared
  description: The Collection API from Microsoft Azure Health Data Services — 2 operation(s) for collection.
  name: Microsoft Azure Health Data Services Collection API
  slug: azure-health-collection-api
- baseURL: https://{endpoint}
  baseurl_source: declared
  description: The Deid API from Microsoft Azure Health Data Services — 1 operation(s) for deid.
  name: Microsoft Azure Health Data Services Deid API
  slug: azure-health-deid-api
- baseURL: https://management.azure.com
  baseurl_source: declared
  description: The DicomServices API from Microsoft Azure Health Data Services — 2 operation(s) for dicomservices.
  name: Microsoft Azure Health Data Services DicomServices API
  slug: azure-health-dicomservices-api
- baseURL: https://management.azure.com
  baseurl_source: declared
  description: The FhirServices API from Microsoft Azure Health Data Services — 2 operation(s) for fhirservices.
  name: Microsoft Azure Health Data Services FhirServices API
  slug: azure-health-fhirservices-api
- baseURL: https://management.azure.com
  baseurl_source: declared
  description: The IotConnectors API from Microsoft Azure Health Data Services — 4 operation(s) for iotconnectors.
  name: Microsoft Azure Health Data Services IotConnectors API
  slug: azure-health-iotconnectors-api
- baseURL: https://{endpoint}
  baseurl_source: declared
  description: The Jobs API from Microsoft Azure Health Data Services — 4 operation(s) for jobs.
  name: Microsoft Azure Health Data Services Jobs API
  slug: azure-health-jobs-api
- baseURL: https://management.azure.com
  baseurl_source: declared
  description: The PrivateLinkResources API from Microsoft Azure Health Data Services — 2 operation(s) for privatelinkresources.
  name: Microsoft Azure Health Data Services PrivateLinkResources API
  slug: azure-health-privatelinkresources-api
- baseURL: https://management.azure.com
  baseurl_source: declared
  description: The Proxy API from Microsoft Azure Health Data Services — 3 operation(s) for proxy.
  name: Microsoft Azure Health Data Services Proxy API
  slug: azure-health-proxy-api
- baseURL: https://management.azure.com
  baseurl_source: declared
  description: The Resource API from Microsoft Azure Health Data Services — 1 operation(s) for resource.
  name: Microsoft Azure Health Data Services Resource API
  slug: azure-health-resource-api
- baseURL: https://management.azure.com
  baseurl_source: declared
  description: The WorkspacePrivateEndpointConnections API from Microsoft Azure Health Data Services — 2 operation(s) for workspaceprivateendpointconnections.
  name: Microsoft Azure Health Data Services WorkspacePrivateEndpointConnections API
  slug: azure-health-workspaceprivateendpointconnections-api
- baseURL: https://management.azure.com
  baseurl_source: declared
  description: The WorkspacePrivateLinkResources API from Microsoft Azure Health Data Services — 2 operation(s) for workspaceprivatelinkresources.
  name: Microsoft Azure Health Data Services WorkspacePrivateLinkResources API
  slug: azure-health-workspaceprivatelinkresources-api
- baseURL: https://management.azure.com
  baseurl_source: declared
  description: The Workspaces API from Microsoft Azure Health Data Services — 3 operation(s) for workspaces.
  name: Microsoft Azure Health Data Services Workspaces API
  slug: azure-health-workspaces-api
- baseURL: https://management.azure.com
  baseurl_source: declared
  description: The Private Endpoint Connections API from Microsoft Azure Health Data Services — 2 operation(s) for private endpoint connections.
  name: Microsoft Azure Health Data Services Private Endpoint Connections API
  slug: azure-health-private-endpoint-connections-api
artifact_total: 96
asyncapis:
- description: ''
  name: Azure Health Events
  slug: azure-health-events
collections:
- collection_type: postman
  name: Azure Health Data Services de-identification service Collection API
  slug: postman-azure-health-collection-api
- collection_type: postman
  name: Azure Health Data Services de-identification service Collection Deid API
  slug: postman-azure-health-deid-api
- collection_type: postman
  name: Azure Health Data Services de-identification service Collection DicomServices API
  slug: postman-azure-health-dicomservices-api
- collection_type: postman
  name: Azure Health Data Services de-identification service Collection FhirServices API
  slug: postman-azure-health-fhirservices-api
- collection_type: postman
  name: Azure Health Data Services de-identification service Collection IotConnectors API
  slug: postman-azure-health-iotconnectors-api
- collection_type: postman
  name: Azure Health Data Services de-identification service Collection Jobs API
  slug: postman-azure-health-jobs-api
- collection_type: postman
  name: Azure Health Data Services de-identification service Collection PrivateEndpointConnections API
  slug: postman-azure-health-privateendpointconnections-api
- collection_type: postman
  name: Azure Health Data Services de-identification service Collection PrivateLinkResources API
  slug: postman-azure-health-privatelinkresources-api
- collection_type: postman
  name: Azure Health Data Services de-identification service Collection Proxy API
  slug: postman-azure-health-proxy-api
- collection_type: postman
  name: Azure Health Data Services de-identification service Collection Resource API
  slug: postman-azure-health-resource-api
- collection_type: postman
  name: Azure Health Data Services de-identification service Collection WorkspacePrivateEndpointConnections API
  slug: postman-azure-health-workspaceprivateendpointconnections-api
- collection_type: postman
  name: Azure Health Data Services de-identification service Collection WorkspacePrivateLinkResources API
  slug: postman-azure-health-workspaceprivatelinkresources-api
- collection_type: postman
  name: Azure Health Data Services de-identification service Collection Workspaces API
  slug: postman-azure-health-workspaces-api
- collection_type: open
  name: Azure Health Data Services de-identification service Collection API
  slug: open-azure-health-collection-api
- collection_type: open
  name: Azure Health Data Services de-identification service Collection Deid API
  slug: open-azure-health-deid-api
- collection_type: open
  name: Azure Health Data Services de-identification service Collection DicomServices API
  slug: open-azure-health-dicomservices-api
- collection_type: open
  name: Azure Health Data Services de-identification service Collection FhirServices API
  slug: open-azure-health-fhirservices-api
- collection_type: open
  name: Azure Health Data Services de-identification service Collection IotConnectors API
  slug: open-azure-health-iotconnectors-api
- collection_type: open
  name: Azure Health Data Services de-identification service Collection Jobs API
  slug: open-azure-health-jobs-api
- collection_type: open
  name: Azure Health Data Services de-identification service Collection PrivateEndpointConnections API
  slug: open-azure-health-privateendpointconnections-api
- collection_type: open
  name: Azure Health Data Services de-identification service Collection PrivateLinkResources API
  slug: open-azure-health-privatelinkresources-api
- collection_type: open
  name: Azure Health Data Services de-identification service Collection Proxy API
  slug: open-azure-health-proxy-api
- collection_type: open
  name: Azure Health Data Services de-identification service Collection Resource API
  slug: open-azure-health-resource-api
- collection_type: open
  name: Azure Health Data Services de-identification service Collection WorkspacePrivateEndpointConnections API
  slug: open-azure-health-workspaceprivateendpointconnections-api
- collection_type: open
  name: Azure Health Data Services de-identification service Collection WorkspacePrivateLinkResources API
  slug: open-azure-health-workspaceprivatelinkresources-api
- collection_type: open
  name: Azure Health Data Services de-identification service Collection Workspaces API
  slug: open-azure-health-workspaces-api
common:
- group: design
  href: https://artifacts.apis.io/azure-health/rules/azure-health-rules.yml
  title: ''
  type: Spectral
  url: rules/azure-health-rules.yml
- group: design
  href: https://artifacts.apis.io/azure-health/rules/azure-health-jsonschema-spectral-rules.yml
  title: ''
  type: Spectral
  url: rules/azure-health-jsonschema-spectral-rules.yml
- group: design
  href: https://artifacts.apis.io/azure-health/json-ld/azure-health-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/azure-health-context.jsonld
- group: design
  href: https://artifacts.apis.io/azure-health/vocabulary/azure-health-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/azure-health-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/azure-health/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/azure-health/data-model/azure-health-data-model.yml
  title: ''
  type: DataModel
  url: data-model/azure-health-data-model.yml
- group: build
  href: https://artifacts.apis.io/azure-health/cli/azure-health-cli.yml
  title: ''
  type: CLI
  url: cli/azure-health-cli.yml
- group: design
  href: https://artifacts.apis.io/azure-health/conventions/azure-health-conventions.yml
  title: ''
  type: Idempotency
  url: conventions/azure-health-conventions.yml
- group: design
  href: https://artifacts.apis.io/azure-health/conventions/azure-health-conventions.yml
  title: ''
  type: Conventions
  url: conventions/azure-health-conventions.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://azure.status.microsoft/en-us/status
- group: design
  href: https://artifacts.apis.io/azure-health/lifecycle/azure-health-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/azure-health-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/azure-health/errors/azure-health-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/azure-health-problem-types.yml
- group: design
  href: https://artifacts.apis.io/azure-health/conformance/azure-health-conformance.yml
  title: ''
  type: Conformance
  url: conformance/azure-health-conformance.yml
- group: agent
  href: https://artifacts.apis.io/azure-health/llms/azure-health-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/azure-health-llms.txt
- group: other
  href: https://artifacts.apis.io/azure-health/hosts/azure-health-hosts.yml
  title: ''
  type: Hosts
  url: hosts/azure-health-hosts.yml
- group: other
  href: https://artifacts.apis.io/azure-health/vendors/azure-health-vendors.yml
  title: ''
  type: Vendors
  url: vendors/azure-health-vendors.yml
- group: build
  href: https://artifacts.apis.io/azure-health/packages/azure-health-packages.yml
  title: ''
  type: Packages
  url: packages/azure-health-packages.yml
- group: other
  href: https://artifacts.apis.io/azure-health/capabilities/azure-health-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/azure-health-capability-edges.yml
- group: commercial
  href: https://artifacts.apis.io/azure-health/plans/microsoft-azure-health-data-services-plans.yml
  title: ''
  type: Plans
  url: plans/microsoft-azure-health-data-services-plans.yml
- group: operate
  href: https://artifacts.apis.io/azure-health/rate-limits/microsoft-azure-health-data-services-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/microsoft-azure-health-data-services-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/azure-health/finops/microsoft-azure-health-data-services-finops.yml
  title: ''
  type: FinOps
  url: finops/microsoft-azure-health-data-services-finops.yml
- group: operate
  title: ''
  type: IssueTracker
  url: https://github.com/Azure/azure-rest-api-specs/issues
- group: operate
  title: ''
  type: Releases
  url: https://github.com/Azure/azure-rest-api-specs/releases
- group: auth
  title: ''
  type: SecurityPolicy
  url: https://github.com/Azure/azure-rest-api-specs/blob/main/SECURITY.md
- group: build
  title: ''
  type: CodeOfConduct
  url: https://github.com/Azure/.github/blob/main/CODE_OF_CONDUCT.md
- group: docs
  title: ''
  type: ContributionGuide
  url: https://github.com/Azure/azure-rest-api-specs/blob/main/.github/CONTRIBUTING.md
- group: commercial
  title: ''
  type: License
  url: https://github.com/Azure/azure-rest-api-specs/blob/main/LICENSE
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/microsoft-azure-health-data-services/overview
- group: agent
  href: https://artifacts.apis.io/azure-health/agentic-access/azure-health-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/azure-health-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/azure-health/security/azure-health-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/azure-health-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/azure-health/security/azure-health-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/azure-health-domain-security.yml
- group: auth
  href: https://artifacts.apis.io/azure-health/authentication/azure-health-authentication.yml
  title: ''
  type: Authentication
  url: authentication/azure-health-authentication.yml
- group: auth
  href: https://artifacts.apis.io/azure-health/scopes/azure-health-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/azure-health-scopes.yml
- group: company
  title: ''
  type: Website
  url: https://azure.microsoft.com/en-us/products/health-data-services
- group: docs
  title: ''
  type: Documentation
  url: https://learn.microsoft.com/en-us/azure/healthcare-apis/
- group: docs
  title: ''
  type: REST API Reference
  url: https://learn.microsoft.com/en-us/rest/api/healthcareapis/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Azure
- group: build
  title: ''
  type: GitHubRepository
  url: https://github.com/Azure/azure-rest-api-specs
- group: build
  title: ''
  type: GitHubRepository
  url: https://github.com/microsoft/fhir-server
- group: build
  title: ''
  type: GitHubRepository
  url: https://learn.microsoft.com/en-us/azure/healthcare-apis/github-projects
- group: commercial
  title: ''
  type: Pricing
  url: https://azure.microsoft.com/en-us/pricing/details/health-data-services/
- group: commercial
  title: ''
  type: PricingCalculator
  url: https://azure.microsoft.com/en-us/pricing/calculator/
- group: start
  title: ''
  type: Signup
  url: https://azure.microsoft.com/en-us/free/
- group: operate
  title: ''
  type: ChangeLog
  url: https://learn.microsoft.com/en-us/azure/healthcare-apis/release-notes-2024
- group: operate
  title: ''
  type: Status
  url: https://azure.status.microsoft/en-us/status
- group: other
  title: ''
  type: ServiceHealth
  url: https://azure.microsoft.com/en-us/get-started/azure-portal/service-health
- group: operate
  title: ''
  type: Support
  url: https://learn.microsoft.com/en-us/answers/tags/389/azure-health-data-services/
- group: auth
  title: ''
  type: Compliance
  url: https://learn.microsoft.com/en-us/azure/healthcare-apis/healthcare-apis-overview#services-in-azure-health-data-services
- group: auth
  title: ''
  type: Authentication
  url: https://learn.microsoft.com/en-us/azure/healthcare-apis/authentication-authorization
- group: other
  title: ''
  type: PrivateLink
  url: https://learn.microsoft.com/en-us/azure/healthcare-apis/healthcare-apis-overview
- group: build
  title: ''
  type: SDKs
  url: https://learn.microsoft.com/en-us/azure/healthcare-apis/github-projects
- group: company
  title: ''
  type: Blog
  url: https://techcommunity.microsoft.com/t5/s/gxcuf89792/rss/board?board.id=HealthcareAndLifeSciencesBlog
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.microsoft.com/en-us
- group: start
  title: ''
  type: GettingStarted
  url: https://learn.microsoft.com/en-us/azure/healthcare-apis/healthcare-apis-quickstart
- group: operate
  title: ''
  type: ChangeLog
  url: https://learn.microsoft.com/en-us/azure/healthcare-apis/release-notes-2025
- group: commercial
  title: ''
  type: TermsOfService
  url: https://azure.microsoft.com/en-us/support/legal/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://privacy.microsoft.com/en-us/privacystatement
created: '2026-06-13'
description: Microsoft Azure Health Data Services is a cloud-based suite of managed API services built on open healthcare standards (FHIR R4, DICOM, HL7) that enables healthcare organizations to collect, store, analyze, and exchange protected health information (PHI) at scale. The platform includes a FHIR service for structured clinical data exchange, a DICOM service for medical imaging workflows, a MedTech service for IoMT device data ingestion, and a de-identification service for HIPAA-compliant PHI removal from unstructured text. All services run within a HIPAA/HITRUST compliance boundary in an Azure workspace and authenticate via Microsoft Entra ID OAuth 2.0 bearer tokens.
examples:
- key_count: 5
  name: Deidentification Batch Job
  slug: deidentification-batch-job
- key_count: 4
  name: Deidentification Text Request
  slug: deidentification-text-request
- key_count: 4
  name: Dicom Service Create
  slug: dicom-service-create
- key_count: 5
  name: Fhir Service Create
  slug: fhir-service-create
- key_count: 4
  name: Medtech Connector Create
  slug: medtech-connector-create
- key_count: 3
  name: Workspace Create
  slug: workspace-create
finops:
- has_sources: true
  method: derived
  name: Microsoft Azure Health Data Services Finops
  primary_unit: ''
  service_category: ''
  slug: microsoft-azure-health-data-services-finops
  template: true
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/azure-health.png
json_schemas:
- name: De-identification Request Content
  property_count: 3
  slug: DeidentificationContent
- name: De-identification Batch Job
  property_count: 11
  slug: DeidentificationJob
- name: Azure Health Data Services DICOM Service
  property_count: 2
  slug: DicomService
- name: Azure Health Data Services FHIR Service
  property_count: 3
  slug: FhirService
- name: Azure Health Data Services MedTech (IoT Connector)
  property_count: 2
  slug: IotConnector
- name: Azure Health Data Services Workspace
  property_count: 2
  slug: Workspace
- name: CheckNameAvailabilityParameters
  property_count: 2
  slug: azure-health-check-name-availability-parameters
- name: DeidentificationContent
  property_count: 3
  slug: azure-health-deidentification-content
- name: DeidentificationJob
  property_count: 11
  slug: azure-health-deidentification-job
- name: DeidentificationResult
  property_count: 2
  slug: azure-health-deidentification-result
- name: DicomServiceCollection
  property_count: 2
  slug: azure-health-dicom-service-collection
- name: DicomServicePatchResource
  property_count: 2
  slug: azure-health-dicom-service-patch-resource
- name: DicomService
  property_count: 9
  slug: azure-health-dicom-service
- name: FhirServiceCollection
  property_count: 2
  slug: azure-health-fhir-service-collection
- name: FhirServicePatchResource
  property_count: 2
  slug: azure-health-fhir-service-patch-resource
- name: FhirService
  property_count: 10
  slug: azure-health-fhir-service
- name: IotConnectorCollection
  property_count: 2
  slug: azure-health-iot-connector-collection
- name: IotConnectorPatchResource
  property_count: 2
  slug: azure-health-iot-connector-patch-resource
- name: IotConnector
  property_count: 9
  slug: azure-health-iot-connector
- name: IotFhirDestinationCollection
  property_count: 2
  slug: azure-health-iot-fhir-destination-collection
- name: IotFhirDestination
  property_count: 7
  slug: azure-health-iot-fhir-destination
- name: ListOperations
  property_count: 2
  slug: azure-health-list-operations
- name: OperationResultsDescription
  property_count: 6
  slug: azure-health-operation-results-description
- name: PagedDeidentificationDocumentDetails
  property_count: 2
  slug: azure-health-paged-deidentification-document-details
- name: PagedDeidentificationJob
  property_count: 2
  slug: azure-health-paged-deidentification-job
- name: PrivateEndpointConnectionDescription
  property_count: 1
  slug: azure-health-private-endpoint-connection-description
- name: PrivateEndpointConnectionListResultDescription
  property_count: 1
  slug: azure-health-private-endpoint-connection-list-result-description
- name: PrivateLinkResourceDescription
  property_count: 1
  slug: azure-health-private-link-resource-description
- name: PrivateLinkResourceListResultDescription
  property_count: 1
  slug: azure-health-private-link-resource-list-result-description
- name: ServicesDescriptionListResult
  property_count: 2
  slug: azure-health-services-description-list-result
- name: ServicesDescription
  property_count: 10
  slug: azure-health-services-description
- name: ServicesNameAvailabilityInfo
  property_count: 3
  slug: azure-health-services-name-availability-info
- name: ServicesPatchDescription
  property_count: 2
  slug: azure-health-services-patch-description
- name: WorkspaceList
  property_count: 2
  slug: azure-health-workspace-list
- name: WorkspacePatchResource
  property_count: 1
  slug: azure-health-workspace-patch-resource
- name: Workspace
  property_count: 8
  slug: azure-health-workspace
jsonld:
- class_count: 0
  name: Azure Health Context
  property_count: 33
  slug: azure-health-context
- class_count: 0
  name: Azure Health Graph Context
  property_count: 0
  slug: azure-health-graph
layout: provider
modified: '2026-11-05'
name: Microsoft Azure Health Data Services
nav: Providers
network: true
overview: 'Microsoft Azure Health Data Services publishes 13 API contracts indexed on the [APIs.io](https://apis.io/) network, including Collection API, Deid API, DicomServices API, and 10 more. Tagged areas include Healthcare, FHIR, DICOM, IoMT, and Health Data.


  The Microsoft Azure Health Data Services catalog on APIs.io includes 1 event-driven AsyncAPI specification, 2 JSON-LD contexts, and 2 Spectral governance rulesets.


  Microsoft Azure Health Data Services'' developer surface includes CLI, authentication, documentation, pricing, signup flow, changelog, status page, and 50 more developer resources.'
plans:
- name: Microsoft Azure Health Data Services Plans
  plan_count: 15
  slug: microsoft-azure-health-data-services-plans
random_paper: 2
rate_limits:
- limit_count: 4
  name: Microsoft Azure Health Data Services Rate Limits
  slug: microsoft-azure-health-data-services-rate-limits
rules:
- authorship: generated
  effective_rule_count: 5
  extends: []
  name: Microsoft Azure Health Data Services — jsonschema rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: azure-health-jsonschema-spectral-rules
- authorship: generated
  effective_rule_count: 96
  extends:
  - spectral:oas
  name: Microsoft Azure Health Data Services API Rules
  rule_count: 55
  severity_counts:
    error: 42
    hint: 0
    info: 4
    warn: 9
  slug: azure-health-rules
scopes:
- name: Azure Health Scopes
  scope_count: 2
  slug: azure-health-scopes
  summary_line: 2 scopes · implicit/authorizationCode
score:
  band: exemplar
  composite: 75.2
  coverage:
    artifact_dirs: 37
    catalog_earned: 83.8
    catalog_earned_first_party: 24.0
    catalog_gap: 31.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 22.7
  facets:
    access_clarity: 84.2
    contract_governance: 22.0
    contract_quality: 60.8
    developer_ergonomics: 67.3
    discoverability: 66.1
    operational_transparency: 76.3
  open_source:
    applies: true
    score: 100.0
  previous_composite: 52.5
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 84.6
      derived: 0
      marker_coverage: 0.0
      total: 13
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 41.4
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: rising
  upsert:
    applies: true
    score: 33.3
screenshot: https://apis.io/screenshots/azure-health/azure-health-2026-06-20T172859.png
security:
- kind: authentication
  name: Azure Health Authentication
  slug: azure-health-authentication
  summary_line: oauth2 · 2 schemes
- kind: domain-security
  name: Azure Health Domain Security
  slug: azure-health-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Azure Health Vulnerability Disclosure
  slug: azure-health-vulnerability-disclosure
  summary_line: security.txt · contact published
skill_count: 2
skills:
- name: azure-health-deidentify-documents
  slug: azure-health-deidentify-documents
- name: azure-health-provision-fhir-service
  slug: azure-health-provision-fhir-service
slug: azure-health
tags:
- Healthcare
- FHIR
- DICOM
- IoMT
- Health Data
- HIPAA
- HITRUST
- Cloud
- Microsoft Azure
- Microsoft
website: https://azure.microsoft.com/en-us/products/health-data-services
---
