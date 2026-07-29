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
- acting_count: 91
  human_in_the_loop: 2
  name: Google Cloud Healthcare Agentic Access
  operation_count: 149
  slug: google-cloud-healthcare-agentic-access
  summary_line: 149 operations · 91 acting · 2 human-in-the-loop
api_count: 6
apis:
- description: The Cloud Healthcare FHIR API provides a fully managed implementation of the HL7 FHIR standard (supporting DSTU2, STU3, and R4 versions) for storing and querying clinical and administrative healthcare
  name: Cloud Healthcare FHIR API
  slug: healthcare-fhir
- description: The Cloud Healthcare HL7v2 API provides managed ingestion, storage, and retrieval of HL7 version 2.x messages, which are the most widely used standard for exchanging clinical data between hospital inf
  name: Cloud Healthcare HL7v2 API
  slug: healthcare-hl7v2
- description: The Cloud Healthcare DICOM API implements the DICOMweb standard for storing, querying, and retrieving medical imaging data including X-rays, CT scans, MRIs, and ultrasounds. It supports the WADO-RS (r
  name: Cloud Healthcare DICOM API
  slug: healthcare-dicom
- description: 'The Cloud Healthcare De-identification API provides automated redaction and transformation of protected health information (PHI) and personally identifiable information (PII) in FHIR resources, DICOM '
  name: Cloud Healthcare De-identification API
  slug: healthcare-deidentify
- description: The Cloud Healthcare Consent Management API provides fine-grained, patient-centric consent management for healthcare data access. It enables organizations to define consent policies, record patient co
  name: Cloud Healthcare Consent Management API
  slug: healthcare-consent
- description: The projects API from Google Cloud Healthcare — 111 operation(s) for projects.
  name: Google Cloud Healthcare projects API
  slug: google-cloud-healthcare-projects-api
artifact_total: 169
collections:
- collection_type: postman
  name: Cloud Healthcare projects API
  slug: postman-google-cloud-healthcare-projects-api
common:
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/google-cloud-healthcare/overview
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/google-cloud-healthcare-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/google-cloud-healthcare-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/google-cloud-healthcare-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/google-cloud-healthcare-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/google-cloud-healthcare-scopes.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/googleapis
- group: start
  title: ''
  type: GettingStarted
  url: https://cloud.google.com/healthcare-api/docs/quickstart
- group: commercial
  title: ''
  type: Pricing
  url: https://cloud.google.com/healthcare-api/pricing
- group: auth
  title: ''
  type: Authentication
  url: https://cloud.google.com/healthcare-api/docs/how-tos/authentication
- group: start
  title: ''
  type: Console
  url: https://console.cloud.google.com/healthcare
- group: build
  title: ''
  type: CLI
  url: https://cloud.google.com/sdk/gcloud/reference/healthcare
- group: build
  title: ''
  type: SDKs
  url: https://cloud.google.com/healthcare-api/docs/reference/libraries
- group: operate
  title: ''
  type: Support
  url: https://cloud.google.com/healthcare-api/docs/support
- group: operate
  title: ''
  type: StatusPage
  url: https://status.cloud.google.com
- group: auth
  title: ''
  type: Compliance
  url: https://cloud.google.com/healthcare-api/docs/concepts/hipaa
- group: operate
  title: ''
  type: RateLimits
  url: https://cloud.google.com/healthcare-api/quotas
- group: operate
  title: ''
  type: ReleaseNotes
  url: https://cloud.google.com/healthcare-api/docs/release-notes
created: '2026-06-13'
description: Google Cloud Healthcare API is a fully managed, HIPAA-eligible service for ingesting, storing, analyzing, and integrating healthcare data in the cloud. It provides native support for FHIR R4 (Fast Healthcare Interoperability Resources), HL7v2 clinical event messaging, and DICOM medical imaging standards, along with automated de-identification of protected health information (PHI). The API enables healthcare organizations to build interoperable data pipelines, connect clinical systems, and power machine learning applications on Google Cloud infrastructure.
examples:
- key_count: 4
  name: Consentstore Example
  slug: ConsentStore-example
- key_count: 2
  name: Dataset Example
  slug: Dataset-example
- key_count: 4
  name: Dicomstore Example
  slug: DicomStore-example
- key_count: 5
  name: Fhirstore Example
  slug: FhirStore-example
- key_count: 5
  name: Hl7V2Store Example
  slug: Hl7V2Store-example
- key_count: 5
  name: Message Example
  slug: Message-example
finops:
- name: Google Cloud Healthcare Finops
  service_category: Healthcare Data Platform
  slug: google-cloud-healthcare-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/google-cloud-healthcare.png
json_schemas:
- name: ActivateConsentRequest
  property_count: 3
  slug: ActivateConsentRequest
- name: AnalyzeEntitiesRequest
  property_count: 3
  slug: AnalyzeEntitiesRequest
- name: AnalyzeEntitiesResponse
  property_count: 4
  slug: AnalyzeEntitiesResponse
- name: ArchiveUserDataMappingRequest
  property_count: 0
  slug: ArchiveUserDataMappingRequest
- name: ArchiveUserDataMappingResponse
  property_count: 0
  slug: ArchiveUserDataMappingResponse
- name: Attribute
  property_count: 2
  slug: Attribute
- name: AttributeDefinition
  property_count: 6
  slug: AttributeDefinition
- name: AuditConfig
  property_count: 2
  slug: AuditConfig
- name: AuditLogConfig
  property_count: 2
  slug: AuditLogConfig
- name: Binding
  property_count: 3
  slug: Binding
- name: CancelOperationRequest
  property_count: 0
  slug: CancelOperationRequest
- name: CharacterMaskConfig
  property_count: 1
  slug: CharacterMaskConfig
- name: CheckDataAccessRequest
  property_count: 4
  slug: CheckDataAccessRequest
- name: CheckDataAccessResponse
  property_count: 2
  slug: CheckDataAccessResponse
- name: Consent
  property_count: 10
  slug: Consent
- name: ConsentArtifact
  property_count: 8
  slug: ConsentArtifact
- name: ConsentEvaluation
  property_count: 1
  slug: ConsentEvaluation
- name: ConsentList
  property_count: 1
  slug: ConsentList
- name: ConsentStore
  property_count: 4
  slug: ConsentStore
- name: CreateMessageRequest
  property_count: 1
  slug: CreateMessageRequest
- name: CryptoHashConfig
  property_count: 2
  slug: CryptoHashConfig
- name: Dataset
  property_count: 2
  slug: Dataset
- name: DateShiftConfig
  property_count: 2
  slug: DateShiftConfig
- name: DeidentifiedStoreDestination
  property_count: 2
  slug: DeidentifiedStoreDestination
- name: DeidentifyConfig
  property_count: 5
  slug: DeidentifyConfig
- name: DeidentifyDatasetRequest
  property_count: 3
  slug: DeidentifyDatasetRequest
- name: DeidentifyDicomStoreRequest
  property_count: 4
  slug: DeidentifyDicomStoreRequest
- name: DeidentifyFhirStoreRequest
  property_count: 5
  slug: DeidentifyFhirStoreRequest
- name: DeidentifySummary
  property_count: 0
  slug: DeidentifySummary
- name: DicomConfig
  property_count: 4
  slug: DicomConfig
- name: DicomFilterConfig
  property_count: 1
  slug: DicomFilterConfig
- name: DicomStore
  property_count: 4
  slug: DicomStore
- name: DicomStoreMetrics
  property_count: 6
  slug: DicomStoreMetrics
- name: Empty
  property_count: 0
  slug: Empty
- name: Entity
  property_count: 3
  slug: Entity
- name: EntityMention
  property_count: 8
  slug: EntityMention
- name: EntityMentionRelationship
  property_count: 3
  slug: EntityMentionRelationship
- name: EvaluateUserConsentsRequest
  property_count: 7
  slug: EvaluateUserConsentsRequest
- name: EvaluateUserConsentsResponse
  property_count: 2
  slug: EvaluateUserConsentsResponse
- name: ExportDicomDataRequest
  property_count: 2
  slug: ExportDicomDataRequest
- name: ExportDicomDataResponse
  property_count: 0
  slug: ExportDicomDataResponse
- name: ExportMessagesRequest
  property_count: 5
  slug: ExportMessagesRequest
- name: ExportMessagesResponse
  property_count: 0
  slug: ExportMessagesResponse
- name: ExportResourcesRequest
  property_count: 4
  slug: ExportResourcesRequest
- name: ExportResourcesResponse
  property_count: 0
  slug: ExportResourcesResponse
- name: Expr
  property_count: 4
  slug: Expr
- name: Feature
  property_count: 2
  slug: Feature
- name: FhirConfig
  property_count: 2
  slug: FhirConfig
- name: FhirFilter
  property_count: 1
  slug: FhirFilter
- name: FhirNotificationConfig
  property_count: 3
  slug: FhirNotificationConfig
- name: FhirStore
  property_count: 12
  slug: FhirStore
- name: FhirStoreMetric
  property_count: 3
  slug: FhirStoreMetric
- name: FhirStoreMetrics
  property_count: 2
  slug: FhirStoreMetrics
- name: Field
  property_count: 5
  slug: Field
- name: FieldMetadata
  property_count: 2
  slug: FieldMetadata
- name: GcsDestination
  property_count: 3
  slug: GcsDestination
- name: GcsSource
  property_count: 1
  slug: GcsSource
- name: GoogleCloudHealthcareV1ConsentGcsDestination
  property_count: 1
  slug: GoogleCloudHealthcareV1ConsentGcsDestination
- name: GoogleCloudHealthcareV1ConsentPolicy
  property_count: 2
  slug: GoogleCloudHealthcareV1ConsentPolicy
- name: GoogleCloudHealthcareV1DeidentifyDeidentifyDicomStoreSummary
  property_count: 0
  slug: GoogleCloudHealthcareV1DeidentifyDeidentifyDicomStoreSummary
- name: GoogleCloudHealthcareV1DeidentifyDeidentifyFhirStoreSummary
  property_count: 0
  slug: GoogleCloudHealthcareV1DeidentifyDeidentifyFhirStoreSummary
- name: GoogleCloudHealthcareV1DicomBigQueryDestination
  property_count: 3
  slug: GoogleCloudHealthcareV1DicomBigQueryDestination
- name: GoogleCloudHealthcareV1DicomGcsDestination
  property_count: 2
  slug: GoogleCloudHealthcareV1DicomGcsDestination
- name: GoogleCloudHealthcareV1DicomGcsSource
  property_count: 1
  slug: GoogleCloudHealthcareV1DicomGcsSource
- name: GoogleCloudHealthcareV1DicomStreamConfig
  property_count: 1
  slug: GoogleCloudHealthcareV1DicomStreamConfig
- name: GoogleCloudHealthcareV1FhirBigQueryDestination
  property_count: 4
  slug: GoogleCloudHealthcareV1FhirBigQueryDestination
- name: GoogleCloudHealthcareV1FhirGcsDestination
  property_count: 1
  slug: GoogleCloudHealthcareV1FhirGcsDestination
- name: GoogleCloudHealthcareV1FhirGcsSource
  property_count: 1
  slug: GoogleCloudHealthcareV1FhirGcsSource
- name: GroupOrSegment
  property_count: 2
  slug: GroupOrSegment
- name: Hl7SchemaConfig
  property_count: 2
  slug: Hl7SchemaConfig
- name: Hl7TypesConfig
  property_count: 2
  slug: Hl7TypesConfig
- name: Hl7V2NotificationConfig
  property_count: 2
  slug: Hl7V2NotificationConfig
- name: Hl7V2Store
  property_count: 5
  slug: Hl7V2Store
- name: Hl7V2StoreMetric
  property_count: 3
  slug: Hl7V2StoreMetric
- name: Hl7V2StoreMetrics
  property_count: 2
  slug: Hl7V2StoreMetrics
- name: HttpBody
  property_count: 3
  slug: HttpBody
- name: Image
  property_count: 2
  slug: Image
- name: ImageConfig
  property_count: 1
  slug: ImageConfig
- name: ImportDicomDataRequest
  property_count: 1
  slug: ImportDicomDataRequest
- name: ImportDicomDataResponse
  property_count: 0
  slug: ImportDicomDataResponse
- name: ImportMessagesRequest
  property_count: 1
  slug: ImportMessagesRequest
- name: ImportMessagesResponse
  property_count: 0
  slug: ImportMessagesResponse
- name: ImportResourcesRequest
  property_count: 2
  slug: ImportResourcesRequest
- name: ImportResourcesResponse
  property_count: 0
  slug: ImportResourcesResponse
- name: InfoTypeTransformation
  property_count: 6
  slug: InfoTypeTransformation
- name: IngestMessageRequest
  property_count: 1
  slug: IngestMessageRequest
- name: IngestMessageResponse
  property_count: 2
  slug: IngestMessageResponse
- name: KmsWrappedCryptoKey
  property_count: 2
  slug: KmsWrappedCryptoKey
- name: LinkedEntity
  property_count: 1
  slug: LinkedEntity
- name: ListAttributeDefinitionsResponse
  property_count: 2
  slug: ListAttributeDefinitionsResponse
- name: ListConsentArtifactsResponse
  property_count: 2
  slug: ListConsentArtifactsResponse
- name: ListConsentRevisionsResponse
  property_count: 2
  slug: ListConsentRevisionsResponse
- name: ListConsentStoresResponse
  property_count: 2
  slug: ListConsentStoresResponse
- name: ListConsentsResponse
  property_count: 2
  slug: ListConsentsResponse
- name: ListDatasetsResponse
  property_count: 2
  slug: ListDatasetsResponse
- name: ListDicomStoresResponse
  property_count: 2
  slug: ListDicomStoresResponse
- name: ListFhirStoresResponse
  property_count: 2
  slug: ListFhirStoresResponse
- name: ListHl7V2StoresResponse
  property_count: 2
  slug: ListHl7V2StoresResponse
- name: ListLocationsResponse
  property_count: 2
  slug: ListLocationsResponse
- name: ListMessagesResponse
  property_count: 2
  slug: ListMessagesResponse
- name: ListOperationsResponse
  property_count: 2
  slug: ListOperationsResponse
- name: ListUserDataMappingsResponse
  property_count: 2
  slug: ListUserDataMappingsResponse
- name: Location
  property_count: 5
  slug: Location
- name: Message
  property_count: 10
  slug: Message
- name: NotificationConfig
  property_count: 2
  slug: NotificationConfig
- name: Operation
  property_count: 5
  slug: Operation
- name: OperationMetadata
  property_count: 6
  slug: OperationMetadata
- name: ParsedData
  property_count: 1
  slug: ParsedData
- name: ParserConfig
  property_count: 4
  slug: ParserConfig
- name: PatientId
  property_count: 2
  slug: PatientId
- name: Policy
  property_count: 4
  slug: Policy
- name: ProgressCounter
  property_count: 3
  slug: ProgressCounter
- name: PubsubDestination
  property_count: 1
  slug: PubsubDestination
- name: QueryAccessibleDataRequest
  property_count: 3
  slug: QueryAccessibleDataRequest
- name: QueryAccessibleDataResponse
  property_count: 1
  slug: QueryAccessibleDataResponse
- name: RedactConfig
  property_count: 0
  slug: RedactConfig
- name: RejectConsentRequest
  property_count: 1
  slug: RejectConsentRequest
- name: ReplaceWithInfoTypeConfig
  property_count: 0
  slug: ReplaceWithInfoTypeConfig
- name: Resources
  property_count: 1
  slug: Resources
- name: Result
  property_count: 3
  slug: Result
- name: RevokeConsentRequest
  property_count: 1
  slug: RevokeConsentRequest
- name: RollbackFhirResourceFilteringFields
  property_count: 2
  slug: RollbackFhirResourceFilteringFields
- name: RollbackFhirResourcesRequest
  property_count: 8
  slug: RollbackFhirResourcesRequest
- name: RollbackFhirResourcesResponse
  property_count: 1
  slug: RollbackFhirResourcesResponse
- name: SchemaConfig
  property_count: 3
  slug: SchemaConfig
- name: SchemaGroup
  property_count: 5
  slug: SchemaGroup
- name: SchemaPackage
  property_count: 5
  slug: SchemaPackage
- name: SchemaSegment
  property_count: 3
  slug: SchemaSegment
- name: SchematizedData
  property_count: 2
  slug: SchematizedData
- name: SearchResourcesRequest
  property_count: 1
  slug: SearchResourcesRequest
- name: Segment
  property_count: 3
  slug: Segment
- name: SeriesMetrics
  property_count: 4
  slug: SeriesMetrics
- name: SetIamPolicyRequest
  property_count: 2
  slug: SetIamPolicyRequest
- name: Signature
  property_count: 4
  slug: Signature
- name: Status
  property_count: 3
  slug: Status
- name: StreamConfig
  property_count: 3
  slug: StreamConfig
- name: StudyMetrics
  property_count: 5
  slug: StudyMetrics
- name: TagFilterList
  property_count: 1
  slug: TagFilterList
- name: TestIamPermissionsRequest
  property_count: 1
  slug: TestIamPermissionsRequest
- name: TestIamPermissionsResponse
  property_count: 1
  slug: TestIamPermissionsResponse
- name: TextConfig
  property_count: 3
  slug: TextConfig
- name: TextSpan
  property_count: 2
  slug: TextSpan
- name: TimePartitioning
  property_count: 2
  slug: TimePartitioning
- name: Type
  property_count: 3
  slug: Type
- name: UserDataMapping
  property_count: 6
  slug: UserDataMapping
- name: ValidationConfig
  property_count: 5
  slug: ValidationConfig
- name: VersionSource
  property_count: 2
  slug: VersionSource
layout: provider
modified: '2026-06-13'
name: Google Cloud Healthcare
nav: Providers
network: true
overview: 'Google Cloud Healthcare publishes 1 API on the [APIs.io](https://apis.io/) network: projects API. Tagged areas include Healthcare, FHIR, HL7v2, DICOM, and Medical Imaging.


  The Google Cloud Healthcare catalog on APIs.io includes 1 Spectral governance ruleset.


  Google Cloud Healthcare''s developer surface includes authentication, getting-started guide, pricing, developer console, CLI, support, release notes, and 11 more developer resources.'
plans:
- name: Google Cloud Healthcare Plans Pricing
  plan_count: 6
  slug: google-cloud-healthcare-plans-pricing
random_paper: 35
rate_limits:
- limit_count: 13
  name: Google Cloud Healthcare Rate Limits
  slug: google-cloud-healthcare-rate-limits
rules:
- name: Google Cloud Healthcare API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: google-cloud-healthcare-jsonschema-spectral-rules
scopes:
- name: Google Cloud Healthcare Scopes
  scope_count: 2
  slug: google-cloud-healthcare-scopes
  summary_line: 2 scopes · implicit/authorizationCode
score:
  band: developing
  composite: 55.9
  delta: -5.8
  facets:
    commercial_clarity: 57.9
    contract_quality: 48.3
    developer_ergonomics: 50.0
    discoverability: 74.1
    governance: 58.3
    operational_transparency: 68.4
  previous_composite: 61.7
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 1
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 50.0
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: falling
screenshot: https://raw.githubusercontent.com/api-evangelist/google-cloud-healthcare/refs/heads/main/screenshots/google-cloud-healthcare-2026-06-20T182114.png
security:
- kind: authentication
  name: Google Cloud Healthcare Authentication
  slug: google-cloud-healthcare-authentication
  summary_line: oauth2 · 2 schemes
- kind: domain-security
  name: Google Cloud Healthcare Domain Security
  slug: google-cloud-healthcare-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Google Cloud Healthcare Vulnerability Disclosure
  slug: google-cloud-healthcare-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: google-cloud-healthcare
tags:
- Healthcare
- FHIR
- HL7v2
- DICOM
- Medical Imaging
- De-identification
- Interoperability
- Cloud
---
