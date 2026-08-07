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
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 36.9
  scored_at: '2026-08-06'
agentic_access:
- acting_count: 32
  human_in_the_loop: 0
  name: Application Research Agentic Access
  operation_count: 103
  slug: application-research-agentic-access
  summary_line: 103 operations · 32 acting
api_count: 36
apis:
- description: API Resource operations
  name: Application Research API Resources API
  slug: application-research-api-resources-api
- description: Application resource operations
  name: Application Research Applications API
  slug: application-research-applications-api
- description: Operations for managing CNAB bundle descriptors
  name: Application Research Bundles API
  slug: application-research-bundles-api
- description: Capability operations
  name: Application Research Capabilities API
  slug: application-research-capabilities-api
- description: Operations for managing claim execution results
  name: Application Research Claim Results API
  slug: application-research-claim-results-api
- description: Operations for managing installation claims
  name: Application Research Claims API
  slug: application-research-claims-api
- description: Operations for managing component descriptors
  name: Application Research Components API
  slug: application-research-components-api
- description: Operations for managing component configurations
  name: Application Research Configurations API
  slug: application-research-configurations-api
- description: Consumption Bundle operations
  name: Application Research Consumption Bundles API
  slug: application-research-consumption-bundles-api
- description: Container resource operations
  name: Application Research Containers API
  slug: application-research-containers-api
- description: Credential management operations
  name: Application Research Credentials API
  slug: application-research-credentials-api
- description: Dapr component operations
  name: Application Research Dapr API
  slug: application-research-dapr-api
- description: Data Product operations
  name: Application Research Data Products API
  slug: application-research-data-products-api
- description: Datastore portable resource operations
  name: Application Research Datastores API
  slug: application-research-datastores-api
- description: Entity Type operations
  name: Application Research Entity Types API
  slug: application-research-entity-types-api
- description: Environment resource operations
  name: Application Research Environments API
  slug: application-research-environments-api
- description: Event Resource operations
  name: Application Research Event Resources API
  slug: application-research-event-resources-api
- description: Extender portable resource operations
  name: Application Research Extenders API
  slug: application-research-extenders-api
- description: Gateway resource operations
  name: Application Research Gateways API
  slug: application-research-gateways-api
- description: Group and Group Type operations
  name: Application Research Groups API
  slug: application-research-groups-api
- description: Integration Dependency operations
  name: Application Research Integration Dependencies API
  slug: application-research-integration-dependencies-api
- description: Messaging portable resource operations
  name: Application Research Messaging API
  slug: application-research-messaging-api
- description: Operations for ORD Document management
  name: Application Research ORD Documents API
  slug: application-research-ord-documents-api
- description: Package management operations
  name: Application Research Packages API
  slug: application-research-packages-api
- description: Plane management operations
  name: Application Research Planes API
  slug: application-research-planes-api
- description: Product operations
  name: Application Research Products API
  slug: application-research-products-api
- description: Resource group operations
  name: Application Research ResourceGroups API
  slug: application-research-resourcegroups-api
- description: Operations for managing component resources
  name: Application Research Resources API
  slug: application-research-resources-api
- description: Secret store operations
  name: Application Research SecretStores API
  slug: application-research-secretstores-api
- description: Operations for component signing and verification
  name: Application Research Signatures API
  slug: application-research-signatures-api
- description: Operations for managing component sources
  name: Application Research Sources API
  slug: application-research-sources-api
- description: Operations for querying installation status
  name: Application Research Status API
  slug: application-research-status-api
- description: Workload validation operations
  name: Application Research Validation API
  slug: application-research-validation-api
- description: Vendor operations
  name: Application Research Vendors API
  slug: application-research-vendors-api
- description: Volume resource operations
  name: Application Research Volumes API
  slug: application-research-volumes-api
- description: Score workload management operations
  name: Application Research Workloads API
  slug: application-research-workloads-api
artifact_total: 379
collections:
- collection_type: open
  name: Application Research CNAB Bundle API
  slug: open-cloud-native-application-bundle
- collection_type: open
  name: Application Research Open Component Model API
  slug: open-open-component-model
- collection_type: open
  name: Application Research Open Resource Discovery (ORD) API
  slug: open-open-resource-discovery
- collection_type: open
  name: Application Research Radius API
  slug: open-radius
- collection_type: open
  name: Application Research Score Workload Specification API
  slug: open-score
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/application-research-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/application-research-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/application-research-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/application-research-scopes.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/api-evangelist
- group: design
  title: ''
  type: JSONLD
  url: json-ld/application-research-context.jsonld
- group: design
  title: ''
  type: SpectralRules
  url: rules/application-research-spectral-rules.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/application-research-vocabulary.yaml
created: '2026-03-16'
description: 'Application Research is a topic collection focused on specifications for declaring application service integration dependencies. It covers five specification formats: Score (platform-agnostic workload specs), Cloud Native Application Bundle (CNAB), Open Component Model (OCM), Open Resource Discovery (ORD), and Radius — all aimed at enabling deployment teams to understand what services (APIs, databases, caches, message buses, blob stores) an application requires.'
features:
- description: Score enables defining workloads once and deploying across multiple platforms
  name: Platform-Agnostic Workload Specs
- description: CNAB provides standardized packaging and distribution of cloud-native applications
  name: Application Bundle Packaging
- description: OCM enables tracking and verifying software components through delivery pipelines
  name: Software Supply Chain Tracking
- description: ORD enables machines to discover what resources and APIs an application exposes
  name: Automatic API Discovery
- description: Radius enables portable application definitions with dependency declarations across clouds
  name: Cloud-Agnostic Dependency Declarations
finops:
- name: Application Research Finops
  service_category: Application Specifications / Cloud Native
  slug: application-research-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/application-research.png
integrations:
- description: Primary deployment target for Score, CNAB, OCM, and Radius specs
  name: Kubernetes
- description: Score and CNAB support Helm-based deployment and chart generation
  name: Helm
- description: Score workloads can be compiled to Docker Compose files
  name: Docker
- description: Radius integrates with Terraform for infrastructure provisioning
  name: Terraform
- description: GitOps-based deployment of Score and CNAB bundles via ArgoCD
  name: ArgoCD
- description: ORD integrations enable Backstage service catalog population
  name: Backstage
json_schemas:
- name: Access
  property_count: 1
  slug: application-research-access
- name: Access Strategy
  property_count: 3
  slug: application-research-accessstrategy
- name: ACIRuntimeProperties
  property_count: 1
  slug: application-research-aciruntimeproperties
- name: Action
  property_count: 4
  slug: application-research-action
- name: ActionExecutionRequest
  property_count: 2
  slug: application-research-actionexecutionrequest
- name: Annotations
  property_count: 0
  slug: application-research-annotations
- name: API/Event Resource Link
  property_count: 3
  slug: application-research-apieventresourcelink
- name: API Model Selector (JSON Pointer)
  property_count: 2
  slug: application-research-apimodelselectorjsonpointer
- name: API Model Selector (OData)
  property_count: 2
  slug: application-research-apimodelselectorodata
- name: ApiProtocol
  property_count: 0
  slug: application-research-apiprotocol
- name: API Resource
  property_count: 47
  slug: application-research-apiresource
- name: API Resource Definition
  property_count: 5
  slug: application-research-apiresourcedefinition
- name: API Resource Integration Aspect
  property_count: 2
  slug: application-research-apiresourceintegrationaspect
- name: ApiResourceList
  property_count: 4
  slug: application-research-apiresourcelist
- name: ApplicationProperties
  property_count: 4
  slug: application-research-applicationproperties
- name: ApplicationResource
  property_count: 7
  slug: application-research-applicationresource
- name: ApplicationResourceListResult
  property_count: 2
  slug: application-research-applicationresourcelistresult
- name: AuthConfig
  property_count: 1
  slug: application-research-authconfig
- name: AwsAccessKeyCredentialProperties
  property_count: 0
  slug: application-research-awsaccesskeycredentialproperties
- name: AwsCredentialProperties
  property_count: 2
  slug: application-research-awscredentialproperties
- name: AwsCredentialResource
  property_count: 7
  slug: application-research-awscredentialresource
- name: AwsCredentialResourceListResult
  property_count: 2
  slug: application-research-awscredentialresourcelistresult
- name: AwsIRSACredentialProperties
  property_count: 0
  slug: application-research-awsirsacredentialproperties
- name: AzureContainerInstanceCompute
  property_count: 0
  slug: application-research-azurecontainerinstancecompute
- name: AzureContainerInstanceExtension
  property_count: 0
  slug: application-research-azurecontainerinstanceextension
- name: AzureCredentialProperties
  property_count: 2
  slug: application-research-azurecredentialproperties
- name: AzureCredentialResource
  property_count: 7
  slug: application-research-azurecredentialresource
- name: AzureCredentialResourceListResult
  property_count: 2
  slug: application-research-azurecredentialresourcelistresult
- name: AzureKeyVaultVolumeProperties
  property_count: 0
  slug: application-research-azurekeyvaultvolumeproperties
- name: AzureServicePrincipalProperties
  property_count: 0
  slug: application-research-azureserviceprincipalproperties
- name: AzureWorkloadIdentityProperties
  property_count: 0
  slug: application-research-azureworkloadidentityproperties
- name: BicepConfigProperties
  property_count: 1
  slug: application-research-bicepconfigproperties
- name: BicepRecipeProperties
  property_count: 0
  slug: application-research-biceprecipeproperties
- name: BinaryInput
  property_count: 4
  slug: application-research-binaryinput
- name: Bundle
  property_count: 16
  slug: application-research-bundle
- name: BundleListResponse
  property_count: 4
  slug: application-research-bundlelistresponse
- name: BundleOutput
  property_count: 4
  slug: application-research-bundleoutput
- name: Capability
  property_count: 23
  slug: application-research-capability
- name: Capability Definition
  property_count: 5
  slug: application-research-capabilitydefinition
- name: CapabilityList
  property_count: 4
  slug: application-research-capabilitylist
- name: CertificateObjectProperties
  property_count: 6
  slug: application-research-certificateobjectproperties
- name: Changelog Entry
  property_count: 5
  slug: application-research-changelogentry
- name: Claim
  property_count: 9
  slug: application-research-claim
- name: ClaimListResponse
  property_count: 2
  slug: application-research-claimlistresponse
- name: ClaimResult
  property_count: 7
  slug: application-research-claimresult
- name: ClaimResultListResponse
  property_count: 0
  slug: application-research-claimresultlistresponse
- name: ClaimResultOutput
  property_count: 1
  slug: application-research-claimresultoutput
- name: ClaimResultStatus
  property_count: 0
  slug: application-research-claimresultstatus
- name: Component
  property_count: 9
  slug: application-research-component
- name: ComponentConfiguration
  property_count: 1
  slug: application-research-componentconfiguration
- name: ComponentDescriptor
  property_count: 4
  slug: application-research-componentdescriptor
- name: ComponentDescriptorListResponse
  property_count: 4
  slug: application-research-componentdescriptorlistresponse
- name: ComponentName
  property_count: 0
  slug: application-research-componentname
- name: ComponentReference
  property_count: 6
  slug: application-research-componentreference
- name: ComponentReferenceListResponse
  property_count: 0
  slug: application-research-componentreferencelistresponse
- name: ConfigurationListResponse
  property_count: 2
  slug: application-research-configurationlistresponse
- name: ConnectionProperties
  property_count: 3
  slug: application-research-connectionproperties
- name: Consumption Bundle
  property_count: 14
  slug: application-research-consumptionbundle
- name: ConsumptionBundleList
  property_count: 4
  slug: application-research-consumptionbundlelist
- name: Consumption Bundle Reference
  property_count: 2
  slug: application-research-consumptionbundlereference
- name: Container
  property_count: 10
  slug: application-research-container
- name: ContainerFile
  property_count: 5
  slug: application-research-containerfile
- name: ContainerFileMap
  property_count: 0
  slug: application-research-containerfilemap
- name: ContainerMap
  property_count: 0
  slug: application-research-containermap
- name: ContainerPortProperties
  property_count: 4
  slug: application-research-containerportproperties
- name: ContainerProbe
  property_count: 2
  slug: application-research-containerprobe
- name: ContainerProperties
  property_count: 12
  slug: application-research-containerproperties
- name: ContainerResource
  property_count: 7
  slug: application-research-containerresource
- name: ContainerResourceListResult
  property_count: 2
  slug: application-research-containerresourcelistresult
- name: ContainerResources
  property_count: 2
  slug: application-research-containerresources
- name: ContainerVolume
  property_count: 3
  slug: application-research-containervolume
- name: ContainerVolumeMap
  property_count: 0
  slug: application-research-containervolumemap
- name: CorrelationId
  property_count: 0
  slug: application-research-correlationid
- name: Credential
  property_count: 5
  slug: application-research-credential
- name: Credential Exchange Strategy
  property_count: 4
  slug: application-research-credentialexchangestrategy
- name: CredentialStorageProperties
  property_count: 1
  slug: application-research-credentialstorageproperties
- name: CustomPolicyLevel
  property_count: 0
  slug: application-research-custompolicylevel
- name: DaprConfigurationStoreProperties
  property_count: 12
  slug: application-research-daprconfigurationstoreproperties
- name: DaprConfigurationStoreResource
  property_count: 7
  slug: application-research-daprconfigurationstoreresource
- name: DaprConfigurationStoreResourceListResult
  property_count: 2
  slug: application-research-daprconfigurationstoreresourcelistresult
- name: DaprPubSubBrokerProperties
  property_count: 12
  slug: application-research-daprpubsubbrokerproperties
- name: DaprPubSubBrokerResource
  property_count: 7
  slug: application-research-daprpubsubbrokerresource
- name: DaprPubSubBrokerResourceListResult
  property_count: 2
  slug: application-research-daprpubsubbrokerresourcelistresult
- name: DaprResourceAuth
  property_count: 1
  slug: application-research-daprresourceauth
- name: DaprSecretStoreProperties
  property_count: 10
  slug: application-research-daprsecretstoreproperties
- name: DaprSecretStoreResource
  property_count: 7
  slug: application-research-daprsecretstoreresource
- name: DaprSecretStoreResourceListResult
  property_count: 2
  slug: application-research-daprsecretstoreresourcelistresult
- name: DaprSidecarExtension
  property_count: 0
  slug: application-research-daprsidecarextension
- name: DaprStateStoreProperties
  property_count: 12
  slug: application-research-daprstatestoreproperties
- name: DaprStateStoreResource
  property_count: 7
  slug: application-research-daprstatestoreresource
- name: DaprStateStoreResourceListResult
  property_count: 2
  slug: application-research-daprstatestoreresourcelistresult
- name: Data Product
  property_count: 38
  slug: application-research-dataproduct
- name: Data Product Input Port
  property_count: 1
  slug: application-research-dataproductinputport
- name: Data Product Link
  property_count: 3
  slug: application-research-dataproductlink
- name: DataProductList
  property_count: 4
  slug: application-research-dataproductlist
- name: Data Product Output Port
  property_count: 1
  slug: application-research-dataproductoutputport
- name: Definition
  property_count: 29
  slug: application-research-definition
- name: Dependencies
  property_count: 1
  slug: application-research-dependencies
- name: Dependency
  property_count: 2
  slug: application-research-dependency
- name: DependencyVersion
  property_count: 2
  slug: application-research-dependencyversion
- name: DigestSpec
  property_count: 3
  slug: application-research-digestspec
- name: DirInput
  property_count: 8
  slug: application-research-dirinput
- name: DockerInput
  property_count: 3
  slug: application-research-dockerinput
- name: DockerMultiInput
  property_count: 3
  slug: application-research-dockermultiinput
- name: Documentation Labels
  property_count: 0
  slug: application-research-documentationlabels
- name: ElementName
  property_count: 0
  slug: application-research-elementname
- name: Entity Type
  property_count: 28
  slug: application-research-entitytype
- name: Entity Type Target (Correlation ID)
  property_count: 1
  slug: application-research-entitytypecorrelationidtarget
- name: EntityTypeList
  property_count: 4
  slug: application-research-entitytypelist
- name: Entity Type Mapping
  property_count: 2
  slug: application-research-entitytypemapping
- name: Entity Type Target (ORD ID)
  property_count: 1
  slug: application-research-entitytypeordidtarget
- name: EnvironmentCompute
  property_count: 3
  slug: application-research-environmentcompute
- name: EnvironmentProperties
  property_count: 7
  slug: application-research-environmentproperties
- name: EnvironmentResource
  property_count: 7
  slug: application-research-environmentresource
- name: EnvironmentResourceListResult
  property_count: 2
  slug: application-research-environmentresourcelistresult
- name: EnvironmentVariable
  property_count: 2
  slug: application-research-environmentvariable
- name: EnvironmentVariableReference
  property_count: 1
  slug: application-research-environmentvariablereference
- name: EnvironmentVariables
  property_count: 0
  slug: application-research-environmentvariables
- name: EphemeralVolume
  property_count: 0
  slug: application-research-ephemeralvolume
- name: Error
  property_count: 3
  slug: application-research-error
- name: ErrorResponse
  property_count: 1
  slug: application-research-errorresponse
- name: Event Resource
  property_count: 42
  slug: application-research-eventresource
- name: Event Resource Definition
  property_count: 5
  slug: application-research-eventresourcedefinition
- name: Event Resource Integration Aspect
  property_count: 4
  slug: application-research-eventresourceintegrationaspect
- name: Event Resource Integration Aspect Subset
  property_count: 1
  slug: application-research-eventresourceintegrationaspectsubset
- name: EventResourceList
  property_count: 4
  slug: application-research-eventresourcelist
- name: ExecHealthProbeProperties
  property_count: 0
  slug: application-research-exechealthprobeproperties
- name: ExecProbe
  property_count: 1
  slug: application-research-execprobe
- name: Exposed Entity Type
  property_count: 1
  slug: application-research-exposedentitytype
- name: ExtenderProperties
  property_count: 7
  slug: application-research-extenderproperties
- name: ExtenderResource
  property_count: 7
  slug: application-research-extenderresource
- name: ExtenderResourceListResult
  property_count: 2
  slug: application-research-extenderresourcelistresult
- name: Extensible
  property_count: 2
  slug: application-research-extensible
- name: Extension
  property_count: 1
  slug: application-research-extension
- name: FileInput
  property_count: 4
  slug: application-research-fileinput
- name: GatewayHostname
  property_count: 2
  slug: application-research-gatewayhostname
- name: GatewayProperties
  property_count: 9
  slug: application-research-gatewayproperties
- name: GatewayResource
  property_count: 7
  slug: application-research-gatewayresource
- name: GatewayResourceListResult
  property_count: 2
  slug: application-research-gatewayresourcelistresult
- name: GatewayRoute
  property_count: 5
  slug: application-research-gatewayroute
- name: GatewayRouteTimeoutPolicy
  property_count: 2
  slug: application-research-gatewayroutetimeoutpolicy
- name: GatewayTls
  property_count: 3
  slug: application-research-gatewaytls
- name: GitAuthConfig
  property_count: 1
  slug: application-research-gitauthconfig
- name: GitHubAccess
  property_count: 4
  slug: application-research-githubaccess
- name: Group
  property_count: 4
  slug: application-research-group
- name: GroupId
  property_count: 0
  slug: application-research-groupid
- name: GroupList
  property_count: 4
  slug: application-research-grouplist
- name: Group Type
  property_count: 3
  slug: application-research-grouptype
- name: GroupTypeList
  property_count: 4
  slug: application-research-grouptypelist
- name: HealthProbeProperties
  property_count: 5
  slug: application-research-healthprobeproperties
- name: HelmAccess
  property_count: 5
  slug: application-research-helmaccess
- name: HelmInput
  property_count: 7
  slug: application-research-helminput
- name: HttpAccess
  property_count: 2
  slug: application-research-httpaccess
- name: HttpGetHealthProbeProperties
  property_count: 0
  slug: application-research-httpgethealthprobeproperties
- name: HttpHeader
  property_count: 2
  slug: application-research-httpheader
- name: HttpProbe
  property_count: 5
  slug: application-research-httpprobe
- name: IamProperties
  property_count: 2
  slug: application-research-iamproperties
- name: IdentityAttribute
  property_count: 0
  slug: application-research-identityattribute
- name: IdentitySettingKind
  property_count: 0
  slug: application-research-identitysettingkind
- name: IdentitySettings
  property_count: 4
  slug: application-research-identitysettings
- name: Image
  property_count: 7
  slug: application-research-image
- name: Industry
  property_count: 0
  slug: application-research-industry
- name: Input
  property_count: 1
  slug: application-research-input
- name: Integration Aspect
  property_count: 6
  slug: application-research-integrationaspect
- name: Integration Dependency
  property_count: 21
  slug: application-research-integrationdependency
- name: IntegrationDependencyList
  property_count: 4
  slug: application-research-integrationdependencylist
- name: InternalCredentialStorageProperties
  property_count: 0
  slug: application-research-internalcredentialstorageproperties
- name: InvocationImage
  property_count: 6
  slug: application-research-invocationimage
- name: KeyObjectProperties
  property_count: 3
  slug: application-research-keyobjectproperties
- name: KubernetesCompute
  property_count: 0
  slug: application-research-kubernetescompute
- name: KubernetesMetadataExtension
  property_count: 0
  slug: application-research-kubernetesmetadataextension
- name: KubernetesNamespaceExtension
  property_count: 0
  slug: application-research-kubernetesnamespaceextension
- name: KubernetesRuntimeProperties
  property_count: 2
  slug: application-research-kubernetesruntimeproperties
- name: Label
  property_count: 5
  slug: application-research-label
- name: Labels
  property_count: 0
  slug: application-research-labels
- name: LineOfBusiness
  property_count: 0
  slug: application-research-lineofbusiness
- name: Link
  property_count: 3
  slug: application-research-link
- name: LocalBlobAccess
  property_count: 5
  slug: application-research-localblobaccess
- name: Maintainer
  property_count: 3
  slug: application-research-maintainer
- name: ManualScalingExtension
  property_count: 0
  slug: application-research-manualscalingextension
- name: Merge
  property_count: 2
  slug: application-research-merge
- name: Meta
  property_count: 1
  slug: application-research-meta
- name: MetadataValue
  property_count: 2
  slug: application-research-metadatavalue
- name: MetadataValueFromSecret
  property_count: 2
  slug: application-research-metadatavaluefromsecret
- name: MongoDatabaseProperties
  property_count: 12
  slug: application-research-mongodatabaseproperties
- name: MongoDatabaseResource
  property_count: 7
  slug: application-research-mongodatabaseresource
- name: MongoDatabaseResourceListResult
  property_count: 2
  slug: application-research-mongodatabaseresourcelistresult
- name: MongoDatabaseSecrets
  property_count: 2
  slug: application-research-mongodatabasesecrets
- name: NestedComponentDigests
  property_count: 4
  slug: application-research-nestedcomponentdigests
- name: NestedDigestSpec
  property_count: 4
  slug: application-research-nesteddigestspec
- name: NpmAccess
  property_count: 4
  slug: application-research-npmaccess
- name: OciArtifactAccess
  property_count: 2
  slug: application-research-ociartifactaccess
- name: OciBlobAccess
  property_count: 6
  slug: application-research-ociblobaccess
- name: ORD Document
  property_count: 23
  slug: application-research-orddocument
- name: OrdDocumentList
  property_count: 4
  slug: application-research-orddocumentlist
- name: OutputResource
  property_count: 3
  slug: application-research-outputresource
- name: Package
  property_count: 22
  slug: application-research-package
- name: Package Link
  property_count: 3
  slug: application-research-packagelink
- name: PackageList
  property_count: 4
  slug: application-research-packagelist
- name: Parameter
  property_count: 5
  slug: application-research-parameter
- name: ParameterDestination
  property_count: 2
  slug: application-research-parameterdestination
- name: ParameterSource
  property_count: 2
  slug: application-research-parametersource
- name: ParameterSourceOutput
  property_count: 1
  slug: application-research-parametersourceoutput
- name: ParameterSources
  property_count: 0
  slug: application-research-parametersources
- name: PersistentVolume
  property_count: 0
  slug: application-research-persistentvolume
- name: PolicyLevel
  property_count: 0
  slug: application-research-policylevel
- name: PolicyLevelId
  property_count: 0
  slug: application-research-policylevelid
- name: Product
  property_count: 10
  slug: application-research-product
- name: ProductList
  property_count: 4
  slug: application-research-productlist
- name: Provider
  property_count: 2
  slug: application-research-provider
- name: ProviderConfigProperties
  property_count: 1
  slug: application-research-providerconfigproperties
- name: Providers
  property_count: 2
  slug: application-research-providers
- name: ProvidersAws
  property_count: 1
  slug: application-research-providersaws
- name: ProvidersAzure
  property_count: 1
  slug: application-research-providersazure
- name: ProvisioningState
  property_count: 0
  slug: application-research-provisioningstate
- name: RabbitMQQueueProperties
  property_count: 14
  slug: application-research-rabbitmqqueueproperties
- name: RabbitMQQueueResource
  property_count: 7
  slug: application-research-rabbitmqqueueresource
- name: RabbitMQQueueResourceListResult
  property_count: 2
  slug: application-research-rabbitmqqueueresourcelistresult
- name: RabbitMQSecrets
  property_count: 2
  slug: application-research-rabbitmqsecrets
- name: RadiusPlaneResource
  property_count: 7
  slug: application-research-radiusplaneresource
- name: RadiusPlaneResourceListResult
  property_count: 2
  slug: application-research-radiusplaneresourcelistresult
- name: RadiusPlaneResourceProperties
  property_count: 2
  slug: application-research-radiusplaneresourceproperties
- name: Recipe
  property_count: 2
  slug: application-research-recipe
- name: RecipeConfigProperties
  property_count: 4
  slug: application-research-recipeconfigproperties
- name: RecipeProperties
  property_count: 3
  slug: application-research-recipeproperties
- name: RecipeStatus
  property_count: 3
  slug: application-research-recipestatus
- name: RedisCacheProperties
  property_count: 12
  slug: application-research-rediscacheproperties
- name: RedisCacheResource
  property_count: 7
  slug: application-research-rediscacheresource
- name: RedisCacheResourceListResult
  property_count: 2
  slug: application-research-rediscacheresourcelistresult
- name: RedisCacheSecrets
  property_count: 3
  slug: application-research-rediscachesecrets
- name: RegistrySecretConfig
  property_count: 1
  slug: application-research-registrysecretconfig
- name: Related Entity Type
  property_count: 2
  slug: application-research-relatedentitytype
- name: ReleaseStatus
  property_count: 0
  slug: application-research-releasestatus
- name: RelocationMapping
  property_count: 0
  slug: application-research-relocationmapping
- name: RepositoryContext
  property_count: 3
  slug: application-research-repositorycontext
- name: Resource
  property_count: 10
  slug: application-research-resource
- name: ResourceGroupProperties
  property_count: 1
  slug: application-research-resourcegroupproperties
- name: ResourceGroupResource
  property_count: 7
  slug: application-research-resourcegroupresource
- name: ResourceGroupResourceListResult
  property_count: 2
  slug: application-research-resourcegroupresourcelistresult
- name: ResourceListResponse
  property_count: 0
  slug: application-research-resourcelistresponse
- name: ResourceMap
  property_count: 0
  slug: application-research-resourcemap
- name: ResourceMetadata
  property_count: 1
  slug: application-research-resourcemetadata
- name: ResourceProvisioning
  property_count: 0
  slug: application-research-resourceprovisioning
- name: ResourceReference
  property_count: 1
  slug: application-research-resourcereference
- name: ResourcesLimits
  property_count: 2
  slug: application-research-resourceslimits
- name: ResourceStatus
  property_count: 3
  slug: application-research-resourcestatus
- name: RuntimesProperties
  property_count: 2
  slug: application-research-runtimesproperties
- name: S3Access
  property_count: 5
  slug: application-research-s3access
- name: ScoreWorkload
  property_count: 5
  slug: application-research-scoreworkload
- name: SecretConfig
  property_count: 1
  slug: application-research-secretconfig
- name: SecretObjectProperties
  property_count: 4
  slug: application-research-secretobjectproperties
- name: SecretReference
  property_count: 2
  slug: application-research-secretreference
- name: SecretStoreProperties
  property_count: 7
  slug: application-research-secretstoreproperties
- name: SecretStoreResource
  property_count: 7
  slug: application-research-secretstoreresource
- name: SecretStoreResourceListResult
  property_count: 2
  slug: application-research-secretstoreresourcelistresult
- name: SecretValueProperties
  property_count: 3
  slug: application-research-secretvalueproperties
- name: SemVer
  property_count: 0
  slug: application-research-semver
- name: Service
  property_count: 1
  slug: application-research-service
- name: ServicePort
  property_count: 3
  slug: application-research-serviceport
- name: ServicePortMap
  property_count: 0
  slug: application-research-serviceportmap
- name: Signature
  property_count: 3
  slug: application-research-signature
- name: SignatureListResponse
  property_count: 0
  slug: application-research-signaturelistresponse
- name: SignatureRequest
  property_count: 4
  slug: application-research-signaturerequest
- name: SignatureSpec
  property_count: 3
  slug: application-research-signaturespec
- name: SimpleType
  property_count: 0
  slug: application-research-simpletype
- name: Source
  property_count: 7
  slug: application-research-source
- name: SourceListResponse
  property_count: 0
  slug: application-research-sourcelistresponse
- name: SpecificationId
  property_count: 0
  slug: application-research-specificationid
- name: SpiffInput
  property_count: 6
  slug: application-research-spiffinput
- name: SqlDatabaseProperties
  property_count: 12
  slug: application-research-sqldatabaseproperties
- name: SqlDatabaseResource
  property_count: 7
  slug: application-research-sqldatabaseresource
- name: SqlDatabaseResourceListResult
  property_count: 2
  slug: application-research-sqldatabaseresourcelistresult
- name: SqlDatabaseSecrets
  property_count: 2
  slug: application-research-sqldatabasesecrets
- name: SrcRef
  property_count: 2
  slug: application-research-srcref
- name: Status
  property_count: 3
  slug: application-research-status
- name: StatusComponent
  property_count: 3
  slug: application-research-statuscomponent
- name: StatusListResponse
  property_count: 0
  slug: application-research-statuslistresponse
- name: System Instance
  property_count: 6
  slug: application-research-systeminstance
- name: System Type
  property_count: 5
  slug: application-research-systemtype
- name: System Version
  property_count: 6
  slug: application-research-systemversion
- name: Tag
  property_count: 0
  slug: application-research-tag
- name: TcpHealthProbeProperties
  property_count: 0
  slug: application-research-tcphealthprobeproperties
- name: TerraformConfigProperties
  property_count: 2
  slug: application-research-terraformconfigproperties
- name: TerraformRecipeProperties
  property_count: 0
  slug: application-research-terraformrecipeproperties
- name: Tombstone
  property_count: 5
  slug: application-research-tombstone
- name: TransferRequest
  property_count: 4
  slug: application-research-transferrequest
- name: TransferResult
  property_count: 4
  slug: application-research-transferresult
- name: Utf8Input
  property_count: 7
  slug: application-research-utf8input
- name: ValidationError
  property_count: 3
  slug: application-research-validationerror
- name: ValidationResult
  property_count: 3
  slug: application-research-validationresult
- name: ValidationWarning
  property_count: 3
  slug: application-research-validationwarning
- name: ValueFromProperties
  property_count: 2
  slug: application-research-valuefromproperties
- name: Vendor
  property_count: 6
  slug: application-research-vendor
- name: VendorList
  property_count: 4
  slug: application-research-vendorlist
- name: VerificationRequest
  property_count: 2
  slug: application-research-verificationrequest
- name: VerificationResult
  property_count: 5
  slug: application-research-verificationresult
- name: Version
  property_count: 0
  slug: application-research-version
- name: VersionListResponse
  property_count: 2
  slug: application-research-versionlistresponse
- name: Visibility
  property_count: 0
  slug: application-research-visibility
- name: Volume
  property_count: 2
  slug: application-research-volume
- name: VolumeProperties
  property_count: 5
  slug: application-research-volumeproperties
- name: VolumeResource
  property_count: 7
  slug: application-research-volumeresource
- name: VolumeResourceListResult
  property_count: 2
  slug: application-research-volumeresourcelistresult
- name: WgetAccess
  property_count: 7
  slug: application-research-wgetaccess
- name: WorkloadList
  property_count: 4
  slug: application-research-workloadlist
- name: WorkloadMetadata
  property_count: 2
  slug: application-research-workloadmetadata
json_structures:
- name: Application Research Structure
  property_count: 0
  slug: application-research-structure
- name: Cloud Native Application Bundle Schema Structure
  property_count: 0
  slug: cloud-native-application-bundle-schema-structure
- name: Open Component Model Structure
  property_count: 0
  slug: open-component-model-structure
- name: Open Resource Discovery Structure
  property_count: 23
  slug: open-resource-discovery-structure
- name: Radius Structure
  property_count: 0
  slug: radius-structure
- name: Score Structure
  property_count: 5
  slug: score-structure
jsonld:
- class_count: 9
  name: Application Research Context
  property_count: 16
  slug: application-research-context
layout: provider
modified: '2026-05-19'
name: Application Research
nav: Providers
network: true
overview: 'Application Research publishes 36 APIs on the [APIs.io](https://apis.io/) network, including API Resources API, Applications API, Bundles API, and 33 more. Tagged areas include Application Dependencies, Cloud Native, Integration, Research, and Specifications.


  The Application Research catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Application Research''s developer surface includes authentication and 7 more developer resources.'
plans:
- name: Application Research Plans Pricing
  plan_count: 1
  slug: application-research-plans-pricing
random_paper: 28
rate_limits:
- limit_count: 1
  name: Application Research Rate Limits
  slug: application-research-rate-limits
rules:
- name: Application Research API Rules
  rule_count: 6
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 4
  slug: application-research-jsonschema-spectral-rules
- name: Application Research API Rules
  rule_count: 26
  severity_counts:
    error: 9
    hint: 0
    info: 1
    warn: 16
  slug: application-research-spectral-rules
scopes:
- name: Application Research Scopes
  scope_count: 3
  slug: application-research-scopes
  summary_line: 3 scopes · clientCredentials
score:
  band: developing
  composite: 45.6
  delta: 0.0
  facets:
    commercial_clarity: 28.9
    contract_quality: 76.5
    developer_ergonomics: 10.9
    discoverability: 68.5
    governance: 68.8
    operational_transparency: 26.3
  previous_composite: 45.6
  provenance:
    agentic_access: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 36
  schema_version: 0.9.1
  scored_at: '2026-08-06'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/application-research/refs/heads/main/screenshots/application-research-2026-06-20T172330.png
security:
- kind: authentication
  name: Application Research Authentication
  slug: application-research-authentication
  summary_line: apiKey/http/oauth2/openIdConnect · 4 schemes
- kind: domain-security
  name: Application Research Domain Security
  slug: application-research-domain-security
  summary_line: TLSv1.3 · HSTS
slug: application-research
tags:
- Application Dependencies
- Cloud Native
- Integration
- Research
- Specifications
- Workload Specifications
use_cases:
- description: Define an application once and deploy it across Kubernetes, Docker, or cloud platforms
  name: Multi-Platform Deployment
- description: Explicitly declare all required services (databases, caches, queues) for an application
  name: Dependency Documentation
- description: Track and verify software component provenance and integrity
  name: Software Supply Chain Security
- description: Enable API management platforms to automatically discover application capabilities
  name: API Landscape Discovery
- description: Move applications between cloud providers without rewriting configuration
  name: Cloud Migration
---
