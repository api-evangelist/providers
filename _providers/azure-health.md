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
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 30.6
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 26
  human_in_the_loop: 0
  name: Azure Health Agentic Access
  operation_count: 53
  slug: azure-health-agentic-access
  summary_line: 53 operations · 26 acting
api_count: 13
apis:
- description: The Collection API from Microsoft Azure Health Data Services — 2 operation(s) for collection.
  name: Microsoft Azure Health Data Services Collection API
  slug: azure-health-collection-api
- description: The Deid API from Microsoft Azure Health Data Services — 1 operation(s) for deid.
  name: Microsoft Azure Health Data Services Deid API
  slug: azure-health-deid-api
- description: The DicomServices API from Microsoft Azure Health Data Services — 2 operation(s) for dicomservices.
  name: Microsoft Azure Health Data Services DicomServices API
  slug: azure-health-dicomservices-api
- description: The FhirServices API from Microsoft Azure Health Data Services — 2 operation(s) for fhirservices.
  name: Microsoft Azure Health Data Services FhirServices API
  slug: azure-health-fhirservices-api
- description: The IotConnectors API from Microsoft Azure Health Data Services — 4 operation(s) for iotconnectors.
  name: Microsoft Azure Health Data Services IotConnectors API
  slug: azure-health-iotconnectors-api
- description: The Jobs API from Microsoft Azure Health Data Services — 4 operation(s) for jobs.
  name: Microsoft Azure Health Data Services Jobs API
  slug: azure-health-jobs-api
- description: The PrivateEndpointConnections API from Microsoft Azure Health Data Services — 2 operation(s) for privateendpointconnections.
  name: Microsoft Azure Health Data Services PrivateEndpointConnections API
  slug: azure-health-privateendpointconnections-api
- description: The PrivateLinkResources API from Microsoft Azure Health Data Services — 2 operation(s) for privatelinkresources.
  name: Microsoft Azure Health Data Services PrivateLinkResources API
  slug: azure-health-privatelinkresources-api
- description: The Proxy API from Microsoft Azure Health Data Services — 3 operation(s) for proxy.
  name: Microsoft Azure Health Data Services Proxy API
  slug: azure-health-proxy-api
- description: The Resource API from Microsoft Azure Health Data Services — 1 operation(s) for resource.
  name: Microsoft Azure Health Data Services Resource API
  slug: azure-health-resource-api
- description: The WorkspacePrivateEndpointConnections API from Microsoft Azure Health Data Services — 2 operation(s) for workspaceprivateendpointconnections.
  name: Microsoft Azure Health Data Services WorkspacePrivateEndpointConnections API
  slug: azure-health-workspaceprivateendpointconnections-api
- description: The WorkspacePrivateLinkResources API from Microsoft Azure Health Data Services — 2 operation(s) for workspaceprivatelinkresources.
  name: Microsoft Azure Health Data Services WorkspacePrivateLinkResources API
  slug: azure-health-workspaceprivatelinkresources-api
- description: The Workspaces API from Microsoft Azure Health Data Services — 3 operation(s) for workspaces.
  name: Microsoft Azure Health Data Services Workspaces API
  slug: azure-health-workspaces-api
artifact_total: 49
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
common:
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/microsoft-azure-health-data-services/overview
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/azure-health-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/azure-health-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/azure-health-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/azure-health-authentication.yml
- group: auth
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
- name: Microsoft Azure Health Data Services Finops
  service_category: Healthcare / Health Data Services
  slug: microsoft-azure-health-data-services-finops
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
modified: '2026-06-13'
name: Microsoft Azure Health Data Services
nav: Providers
network: true
overview: 'Microsoft Azure Health Data Services publishes 13 APIs on the [APIs.io](https://apis.io/) network, including Collection API, Deid API, DicomServices API, and 10 more. Tagged areas include Healthcare, FHIR, DICOM, MedTech, and IoMT.


  The Microsoft Azure Health Data Services catalog on APIs.io includes 2 JSON-LD contexts and 1 Spectral governance ruleset.


  Microsoft Azure Health Data Services'' developer surface includes authentication, documentation, pricing, signup flow, changelog, status page, support, and 18 more developer resources.'
plans:
- name: Microsoft Azure Health Data Services Plans
  plan_count: 5
  slug: microsoft-azure-health-data-services-plans
random_paper: 78
rate_limits:
- limit_count: 9
  name: Microsoft Azure Health Data Services Rate Limits
  slug: microsoft-azure-health-data-services-rate-limits
rules:
- name: Microsoft Azure Health Data Services API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: azure-health-jsonschema-spectral-rules
scopes:
- name: Azure Health Scopes
  scope_count: 2
  slug: azure-health-scopes
  summary_line: 2 scopes · authorizationCode/implicit
score:
  band: developing
  composite: 51.8
  delta: -8.4
  facets:
    commercial_clarity: 57.9
    contract_quality: 45.2
    developer_ergonomics: 37.0
    discoverability: 68.5
    governance: 58.3
    operational_transparency: 52.6
  previous_composite: 60.2
  provenance:
    agentic_access: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 13
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 56.3
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: falling
screenshot: https://raw.githubusercontent.com/api-evangelist/azure-health/refs/heads/main/screenshots/azure-health-2026-06-20T172859.png
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
slug: azure-health
tags:
- Healthcare
- FHIR
- DICOM
- MedTech
- IoMT
- Health Data
- HIPAA
- HITRUST
- Cloud
- Azure
- Microsoft
website: https://azure.microsoft.com/en-us/products/health-data-services
---
