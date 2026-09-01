---
access_model:
  confidence: high
  label: Free · Open access
  onboarding: open
  pricing: free
  public: true
  source:
  - plans
  - authentication
  trial: false
  try_now: true
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: verified
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 39.7
  scored_at: '2026-09-01'
agentic_access:
- acting_count: 21
  human_in_the_loop: 1
  name: Cms Agentic Access
  operation_count: 94
  slug: cms-agentic-access
  summary_line: 94 operations · 21 acting · 1 human-in-the-loop
api_count: 4
apis:
- description: Provides Original Medicare claims data to fee-for-service Medicare providers in a structured, standardized FHIR format at the point of care. Helps providers gain complete views of patient medical hist
  name: CMS Data at the Point of Care (DPC) API
  slug: cms-data-at-the-point-of-care-dpc-api
- description: The API behind Finder.Healthcare.gov that helps users find private health plans available outside the Health Insurance Marketplace. Supports individual plan lookups, small group plan searches, and geo
  name: CMS Finder API
  slug: cms-finder-api
- description: Enables QPP participants to submit quality performance data and receive real-time performance scoring feedback. Supports Merit-based Incentive Payment System (MIPS) and Advanced Alternative Payment Mo
  name: CMS Quality Payment Program (QPP) Submissions API
  slug: cms-quality-payment-program-qpp-submissions-api
- description: Information about the state of Marketplace API.
  name: Centers for Medicare and Medicaid Services API Reference API
  slug: cms-api-reference-api
- description: Information about the bulk data json files maintained by Marketplace API.
  name: Centers for Medicare and Medicaid Services Bulk Data API
  slug: cms-bulk-data-api
- description: Search CPT/HCPCS codes by procedure codes or terms describing medical procedures. Get code details for a given procedure code.
  name: Centers for Medicare and Medicaid Services Code Search API
  slug: cms-code-search-api
- description: For a given procedure code or entire set of codes, get national averages for the amount Medicare pays hospitals or surgical centers, and the national average copay amounts.
  name: Centers for Medicare and Medicaid Services Cost Search API
  slug: cms-cost-search-api
- description: Enrollment grouping validation and information.
  name: Centers for Medicare and Medicaid Services Enrollments API
  slug: cms-enrollments-api
- description: Geographic data, including information on states, counties, and zipcodes.
  name: Centers for Medicare and Medicaid Services Geography API
  slug: cms-geography-api
- description: Household specific calculations, including eligibility information, out of pocket costs, poverty levels, and cost benchmarks.
  name: Centers for Medicare and Medicaid Services Households & Eligibility API
  slug: cms-households-eligibility-api
- description: Data related to health insurance issuers on the marketplace.
  name: Centers for Medicare and Medicaid Services Insurance Issuers API
  slug: cms-insurance-issuers-api
- description: Data on both health and dental insurance plans.
  name: Centers for Medicare and Medicaid Services Insurance Plans API
  slug: cms-insurance-plans-api
- description: The Plans API from Centers for Medicare and Medicaid Services — 1 operation(s) for plans.
  name: Centers for Medicare and Medicaid Services Plans API
  slug: cms-plans-api
- description: Lookup information on providers, drugs, and what is covered under what plans.
  name: Centers for Medicare and Medicaid Services Provider & Drug Coverage API
  slug: cms-provider-drug-coverage-api
- description: data.cms.gov hosts hundreds of CMS datasets including Medicare Fee-for-Service utilization and payment data, Provider of Services files, Medicare Part B/D Prescriber summaries, Marketplace open enroll
  name: CMS Socrata Open Data API (data.cms.gov)
  slug: cms-socrata-open-data
- description: The Provider Data Catalog API (formerly Hospital Compare) exposes the Medicare.gov Care Compare datasets including Hospital, Nursing Home, Home Health, Hospice, Physician, Long-Term Care Hospital, Inp
  name: CMS Provider Data Catalog API (Care Compare)
  slug: cms-provider-data-catalog
- description: The NPPES NPI Registry API provides free public access to look up active National Provider Identifier records for individual and organizational healthcare providers, supporting FHIR-compatible JSON re
  name: NPPES NPI Registry API
  slug: nppes-npi-registry
- description: The Healthcare.gov Marketplace API and accompanying Open Data Plan Finder exposes Qualified Health Plan (QHP) details, plan attributes, provider networks, and formularies for the Federally-Facilitated
  name: Healthcare.gov Marketplace API
  slug: healthcare-gov-marketplace
- description: The Quality Payment Program Measures Data repository and REST API publish machine-readable specifications of MIPS quality, promoting interoperability, improvement activities, and cost measures for eac
  name: CMS Quality Payment Program (QPP) Measures API
  slug: qpp-measures-api
- description: The Medicare Coverage Database publishes National Coverage Determinations (NCDs), Local Coverage Determinations (LCDs), articles, and coding guidance used to determine Medicare coverage and reimbursem
  name: Medicare Coverage Database (MCD) API
  slug: medicare-coverage-database
- description: FHIR server capability statements and metadata.
  name: Centers for Medicare and Medicaid Services Capability API
  slug: centers-for-medicare-and-medicaid-services-capability-api
- description: Beneficiary coverage records.
  name: Centers for Medicare and Medicaid Services Coverage API
  slug: centers-for-medicare-and-medicaid-services-coverage-api
- description: Medicare claims expressed as ExplanationOfBenefit resources.
  name: Centers for Medicare and Medicaid Services ExplanationOfBenefit API
  slug: centers-for-medicare-and-medicaid-services-explanationofbenefit-api
- description: Beneficiary (Patient) resources.
  name: Centers for Medicare and Medicaid Services Patient API
  slug: centers-for-medicare-and-medicaid-services-patient-api
- description: API through which an authenticated and authorized PDP sponsor may request a bulk-data export from a server.
  name: Centers for Medicare and Medicaid Services 1. Export API
  slug: cms-1-export-api
- description: API to determine the status of the job, the files to download once the job is complete and an endpoint to cancel a job
  name: Centers for Medicare and Medicaid Services 2. Status API
  slug: cms-2-status-api
- description: After creating a job, the API to download the generated bulk download files
  name: Centers for Medicare and Medicaid Services 3. Download API
  slug: cms-3-download-api
- description: Provide the standard required FHIR capability statement
  name: Centers for Medicare and Medicaid Services 4. Capabilities API
  slug: cms-4-capabilities-api
- description: The admin-api API from Centers for Medicare and Medicaid Services — 5 operation(s) for admin-api.
  name: Centers for Medicare and Medicaid Services Admin API
  slug: cms-admin-api-api
- description: The attribution API from Centers for Medicare and Medicaid Services — 2 operation(s) for attribution.
  name: Centers for Medicare and Medicaid Services Attribution API
  slug: cms-attribution-api
- description: The auth API from Centers for Medicare and Medicaid Services — 3 operation(s) for auth.
  name: Centers for Medicare and Medicaid Services Auth API
  slug: cms-auth-api
- description: Provide the standard required FHIR capability statement
  name: Centers for Medicare and Medicaid Services Capabilities API
  slug: cms-capabilities-api
- description: The data API from Centers for Medicare and Medicaid Services — 1 operation(s) for data.
  name: Centers for Medicare and Medicaid Services Data API
  slug: cms-data-api
- description: After creating a job, the API to download the generated bulk download files
  name: Centers for Medicare and Medicaid Services Download API
  slug: cms-download-api
- description: API through which an authenticated and authorized PDP sponsor may request a bulk-data export from a server.
  name: Centers for Medicare and Medicaid Services Export API
  slug: cms-export-api
- description: The group API from Centers for Medicare and Medicaid Services — 2 operation(s) for group.
  name: Centers for Medicare and Medicaid Services Group API
  slug: cms-group-api
- description: The health-api API from Centers for Medicare and Medicaid Services — 1 operation(s) for health-api.
  name: Centers for Medicare and Medicaid Services Health API
  slug: cms-health-api-api
- description: The job API from Centers for Medicare and Medicaid Services — 4 operation(s) for job.
  name: Centers for Medicare and Medicaid Services Job API
  slug: cms-job-api
- description: The maintenance-mode-api API from Centers for Medicare and Medicaid Services — 1 operation(s) for maintenance-mode-api.
  name: Centers for Medicare and Medicaid Services Maintenance Mode API
  slug: cms-maintenance-mode-api-api
- description: The metadata API from Centers for Medicare and Medicaid Services — 3 operation(s) for metadata.
  name: Centers for Medicare and Medicaid Services Metadata API
  slug: cms-metadata-api
- description: API to determine the status of the job, the files to download once the job is complete and an endpoint to cancel a job
  name: Centers for Medicare and Medicaid Services Status API
  slug: cms-status-api
artifact_total: 177
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Marketplace API Reference API
  slug: open-cms-api-reference-api
- collection_type: open
  name: Marketplace API Reference Bulk Data API
  slug: open-cms-bulk-data-api
- collection_type: open
  name: CMS Blue Button 2.0 Capability API
  slug: open-cms-capability-api
- collection_type: open
  name: CMS Blue Button 2.0 API
  slug: open-cms-cms-blue-button-2
- collection_type: open
  name: Marketplace API Reference Code Search API
  slug: open-cms-code-search-api
- collection_type: open
  name: Marketplace API Reference Cost Search API
  slug: open-cms-cost-search-api
- collection_type: open
  name: CMS Blue Button 2.0 Capability Coverage API
  slug: open-cms-coverage-api
- collection_type: open
  name: Marketplace API Reference Enrollments API
  slug: open-cms-enrollments-api
- collection_type: open
  name: CMS Blue Button 2.0 Capability ExplanationOfBenefit API
  slug: open-cms-explanationofbenefit-api
- collection_type: open
  name: Marketplace API Reference Geography API
  slug: open-cms-geography-api
- collection_type: open
  name: Marketplace API Reference Households & Eligibility API
  slug: open-cms-households-eligibility-api
- collection_type: open
  name: Marketplace API Reference Insurance Issuers API
  slug: open-cms-insurance-issuers-api
- collection_type: open
  name: Marketplace API Reference Insurance Plans API
  slug: open-cms-insurance-plans-api
- collection_type: open
  name: CMS Blue Button 2.0 Capability Patient API
  slug: open-cms-patient-api
- collection_type: open
  name: Marketplace API Reference Plans API
  slug: open-cms-plans-api
- collection_type: open
  name: Marketplace API Reference Provider & Drug Coverage API
  slug: open-cms-provider-drug-coverage-api
common:
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/cms-capability-edges.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/cms-export-aco-claims-bcda.md
- group: agent
  title: ''
  type: AgentSkill
  url: skills/cms-export-partd-claims-ab2d.md
- group: operate
  title: ''
  type: IssueTracker
  url: https://github.com/CMSgov/bcda-app/issues
- group: operate
  title: ''
  type: Releases
  url: https://github.com/CMSgov/bcda-app/releases
- group: auth
  title: ''
  type: SecurityPolicy
  url: https://github.com/CMSgov/bcda-app/blob/main/SECURITY.md
- group: build
  title: ''
  type: CodeOfConduct
  url: https://github.com/CMSgov/bcda-app/blob/main/CODE_OF_CONDUCT.md
- group: docs
  title: ''
  type: ContributionGuide
  url: https://github.com/CMSgov/bcda-app/blob/main/CONTRIBUTING.md
- group: commercial
  title: ''
  type: License
  url: https://github.com/CMSgov/bcda-app/blob/main/LICENSE
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/cms-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/cms-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/cms-authentication.yml
- group: start
  title: ''
  type: Portal
  url: https://developer.cms.gov/
- group: start
  title: ''
  type: DataPortal
  url: https://data.cms.gov/
- group: other
  title: ''
  type: ProviderDataCatalog
  url: https://data.cms.gov/provider-data/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/cmsgov
- group: other
  title: ''
  type: InteroperabilityGuidance
  url: https://www.cms.gov/priorities/burden-reduction/overview/interoperability/implementation-guides-standards/application-programming-interfaces-apis-relevant-standards-implementation-guides-igs
- group: other
  title: ''
  type: PublicDatasets
  url: https://www.cms.gov/data-research/cms-data/data-available-everyone
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/cms-scopes.yml
- group: company
  title: ''
  type: Website
  url: https://www.cms.gov/
- group: other
  title: ''
  type: Developer
  url: https://developer.cms.gov/
- group: other
  title: ''
  type: OpenData
  url: https://data.cms.gov/
- group: other
  title: ''
  type: ProviderData
  url: https://data.cms.gov/provider-data/
- group: other
  title: ''
  type: BlueButton
  url: https://bluebutton.cms.gov/
- group: other
  title: ''
  type: BCDA
  url: https://bcda.cms.gov/
- group: other
  title: ''
  type: DPC
  url: https://dpc.cms.gov/
- group: other
  title: ''
  type: NPPES
  url: https://npiregistry.cms.hhs.gov/
- group: other
  title: ''
  type: Marketplace
  url: https://www.healthcare.gov/developers/
- group: other
  title: ''
  type: QPP
  url: https://qpp.cms.gov/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/CMSgov
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.cms.gov/privacy
- group: agent
  title: ''
  type: WellKnown
  url: well-known/cms-well-known.yml
- group: other
  title: ''
  type: OpenIDConnect
  url: https://api.bluebutton.cms.gov/.well-known/openid-configuration
- group: build
  title: ''
  type: Packages
  url: packages/cms-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/cms-packages.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/cms-mcp.yml
- group: build
  title: ''
  type: ToolCrosswalk
  url: mcp/cms-tool-crosswalk.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/cms-llms.txt
- group: design
  title: ''
  type: Conformance
  url: conformance/cms-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: https://security.cms.gov/
- group: auth
  title: ''
  type: TrustCenter
  url: https://security.cms.gov/
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/cms-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/cms-lifecycle.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://ab2d.cms.gov/status
- group: operate
  title: ''
  type: Deprecation
  url: https://bcda.cms.gov/v3/welcome-v3
- group: design
  title: ''
  type: Versioning
  url: https://bcda.cms.gov/bcda-data/difference-between-v1-v2.html
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/cms-changelog.yml
- group: auth
  title: ''
  type: Security
  url: https://www.cms.gov/vulnerability-disclosure-policy
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/cms-vulnerability-disclosure.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/cms-conventions.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/cms-sandbox.yml
- group: build
  title: ''
  type: CLI
  url: cli/cms-cli.yml
- group: design
  title: ''
  type: Components
  url: components/cms-components.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/cms-data-model.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/cms-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/cms-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/cms-finops.yml
- group: design
  title: ''
  type: SpectralRules
  url: rules/cms-jsonschema-spectral-rules.yml
- group: design
  title: ''
  type: JSONLDContext
  url: json-ld/cms-context.jsonld
- group: build
  title: ''
  type: Examples
  url: examples/marketplace-plan-example.json
- group: build
  title: ''
  type: Examples
  url: examples/marketplace-household-example.json
- group: build
  title: ''
  type: Examples
  url: examples/marketplace-provider-example.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/marketplace-plan.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/marketplace-household.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/marketplace-eligibility.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/marketplace-provider.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/marketplace-drug.json
- group: build
  title: ''
  type: PostmanCollection
  url: collections/cms-cms-blue-button-2.postman_collection.json
- group: other
  title: ''
  type: Overlay
  url: overlays/cms-bcda-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/cms-ab2d-overlay.yaml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.cms.gov/
- group: docs
  title: ''
  type: Documentation
  url: https://bcda.cms.gov/api-documentation.html
- group: docs
  title: ''
  type: APIReference
  url: https://bluebutton.cms.gov/api-documentation/
- group: start
  title: ''
  type: GettingStarted
  url: https://bcda.cms.gov/api-documentation/get-a-bearer-token.html
- group: operate
  title: ''
  type: Support
  url: https://bcda.cms.gov/support.html
- group: start
  title: ''
  type: SignUp
  url: https://sandbox.bluebutton.cms.gov/v1/accounts/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://bluebutton.cms.gov/terms/
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/cms-vocabulary.json
created: '2026-06-13'
description: The Centers for Medicare and Medicaid Services (CMS) provides a suite of public REST APIs enabling developers to access Medicare provider data, quality measures, drug spending, health plan finder, beneficiary claims, and public health insurance datasets. CMS APIs support interoperability standards including HL7 FHIR and OAuth 2.0 to power healthcare applications across the US health system.
examples:
- key_count: 3
  name: Marketplace Address Example
  slug: marketplace-address-example
- key_count: 3
  name: Marketplace Drug Example
  slug: marketplace-drug-example
- key_count: 3
  name: Marketplace Eligibility Example
  slug: marketplace-eligibility-example
- key_count: 3
  name: Marketplace Household Example
  slug: marketplace-household-example
- key_count: 3
  name: Marketplace Issuer Example
  slug: marketplace-issuer-example
- key_count: 3
  name: Marketplace Person Example
  slug: marketplace-person-example
- key_count: 3
  name: Marketplace Plan Example
  slug: marketplace-plan-example
- key_count: 3
  name: Marketplace Provider Example
  slug: marketplace-provider-example
- key_count: 3
  name: Ppl Code Example
  slug: ppl-code-example
- key_count: 3
  name: Ppl Cost Example
  slug: ppl-cost-example
finops:
- name: Cms Finops
  service_category: API
  slug: cms-finops
- name: Finops
  service_category: ''
  slug: finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/cms.png
json_schemas:
- name: Address
  property_count: 6
  slug: marketplace-address
- name: ApplicationError400
  property_count: 4
  slug: marketplace-applicationerror400
- name: ApplicationError404
  property_count: 4
  slug: marketplace-applicationerror404
- name: APT
  property_count: 2
  slug: marketplace-apt
- name: APTC
  property_count: 3
  slug: marketplace-aptc
- name: APTCAllocationResult
  property_count: 2
  slug: marketplace-aptcallocationresult
- name: APTCEnrollee
  property_count: 2
  slug: marketplace-aptcenrollee
- name: APTCEnrollmentGroup
  property_count: 4
  slug: marketplace-aptcenrollmentgroup
- name: APTTier
  property_count: 2
  slug: marketplace-apttier
- name: Benefit
  property_count: 8
  slug: marketplace-benefit
- name: CertificationStatus
  property_count: 0
  slug: marketplace-certificationstatus
- name: CostSharing
  property_count: 7
  slug: marketplace-costsharing
- name: CostSharingReductionEnum
  property_count: 0
  slug: marketplace-costsharingreductionenum
- name: County
  property_count: 3
  slug: marketplace-county
- name: CountyZips
  property_count: 3
  slug: marketplace-countyzips
- name: Coverage
  property_count: 0
  slug: marketplace-coverage
- name: Crosswalk
  property_count: 3
  slug: marketplace-crosswalk
- name: CrosswalkCode
  property_count: 2
  slug: marketplace-crosswalkcode
- name: CrosswalkData
  property_count: 7
  slug: marketplace-crosswalkdata
- name: CSREligibilityEnum
  property_count: 0
  slug: marketplace-csreligibilityenum
- name: CSRRequestEnum
  property_count: 0
  slug: marketplace-csrrequestenum
- name: CurrentEnrollment
  property_count: 3
  slug: marketplace-currentenrollment
- name: DataVersion
  property_count: 2
  slug: marketplace-dataversion
- name: DecileEnum
  property_count: 0
  slug: marketplace-decileenum
- name: DecileMapping
  property_count: 3
  slug: marketplace-decilemapping
- name: DecileUtilizationAgeMap
  property_count: 7
  slug: marketplace-decileutilizationagemap
- name: DecileUtilizationMapping
  property_count: 2
  slug: marketplace-decileutilizationmapping
- name: Deductible
  property_count: 8
  slug: marketplace-deductible
- name: DesignTypeEnum
  property_count: 0
  slug: marketplace-designtypeenum
- name: DiseaseMgmtProgramsEnum
  property_count: 0
  slug: marketplace-diseasemgmtprogramsenum
- name: Drug
  property_count: 8
  slug: marketplace-drug
- name: DrugCoverage
  property_count: 4
  slug: marketplace-drugcoverage
- name: Eligibility
  property_count: 4
  slug: marketplace-eligibility
- name: Enrollee
  property_count: 2
  slug: marketplace-enrollee
- name: Enrollment
  property_count: 2
  slug: marketplace-enrollment
- name: EnrollmentGroup
  property_count: 3
  slug: marketplace-enrollmentgroup
- name: ExtendedEnrollee
  property_count: 13
  slug: marketplace-extendedenrollee
- name: ExtendedEnrollment
  property_count: 6
  slug: marketplace-extendedenrollment
- name: FamilyCostEnum
  property_count: 0
  slug: marketplace-familycostenum
- name: FlattenedEnrollmentGroup
  property_count: 8
  slug: marketplace-flattenedenrollmentgroup
- name: GenderEnum
  property_count: 0
  slug: marketplace-genderenum
- name: Guideline
  property_count: 2
  slug: marketplace-guideline
- name: Household
  property_count: 5
  slug: marketplace-household
- name: HRA
  property_count: 0
  slug: marketplace-hra
- name: ICHRAResponse
  property_count: 2
  slug: marketplace-ichraresponse
- name: InsuranceMarketEnum
  property_count: 0
  slug: marketplace-insurancemarketenum
- name: Issuer
  property_count: 8
  slug: marketplace-issuer
- name: LowestCostPlanHousehold
  property_count: 2
  slug: marketplace-lowestcostplanhousehold
- name: LowestCostPlanPerson
  property_count: 2
  slug: marketplace-lowestcostplanperson
- name: LowestCostPlanResponse
  property_count: 4
  slug: marketplace-lowestcostplanresponse
- name: LowIncomeChild
  property_count: 3
  slug: marketplace-lowincomechild
- name: MarketEnum
  property_count: 0
  slug: marketplace-marketenum
- name: MarketplaceModelEnum
  property_count: 0
  slug: marketplace-marketplacemodelenum
- name: MarketYear
  property_count: 0
  slug: marketplace-marketyear
- name: MarketYears
  property_count: 2
  slug: marketplace-marketyears
- name: MetalDesignType
  property_count: 2
  slug: marketplace-metaldesigntype
- name: MetalLevelEnum
  property_count: 0
  slug: marketplace-metallevelenum
- name: MOOP
  property_count: 8
  slug: marketplace-moop
- name: NearbyProvider
  property_count: 3
  slug: marketplace-nearbyprovider
- name: NetworkTierEnum
  property_count: 0
  slug: marketplace-networktierenum
- name: NPI
  property_count: 0
  slug: marketplace-npi
- name: Person
  property_count: 14
  slug: marketplace-person
- name: Place
  property_count: 3
  slug: marketplace-place
- name: Plan
  property_count: 39
  slug: marketplace-plan
- name: PlanID
  property_count: 0
  slug: marketplace-planid
- name: PlanIDList
  property_count: 0
  slug: marketplace-planidlist
- name: PlanSearchFilter
  property_count: 22
  slug: marketplace-plansearchfilter
- name: PlanSearchRequest
  property_count: 12
  slug: marketplace-plansearchrequest
- name: PlanTypeEnum
  property_count: 0
  slug: marketplace-plantypeenum
- name: PovertyGuideline
  property_count: 2
  slug: marketplace-povertyguideline
- name: ProductDivisionEnum
  property_count: 0
  slug: marketplace-productdivisionenum
- name: Provider
  property_count: 9
  slug: marketplace-provider
- name: ProviderCoverage
  property_count: 5
  slug: marketplace-providercoverage
- name: ProviderGenderEnum
  property_count: 0
  slug: marketplace-providergenderenum
- name: ProviderTypeEnum
  property_count: 0
  slug: marketplace-providertypeenum
- name: QualityRating
  property_count: 10
  slug: marketplace-qualityrating
- name: Range
  property_count: 2
  slug: marketplace-range
- name: RateArea
  property_count: 2
  slug: marketplace-ratearea
- name: RateAreaCounty
  property_count: 2
  slug: marketplace-rateareacounty
- name: Relationship
  property_count: 0
  slug: marketplace-relationship
- name: RelationshipEdge
  property_count: 3
  slug: marketplace-relationshipedge
- name: RxCUI
  property_count: 0
  slug: marketplace-rxcui
- name: SBCScenario
  property_count: 4
  slug: marketplace-sbcscenario
- name: State
  property_count: 12
  slug: marketplace-state
- name: StateCounty
  property_count: 2
  slug: marketplace-statecounty
- name: StateMedicaid
  property_count: 12
  slug: marketplace-statemedicaid
- name: StateMedicaidList
  property_count: 3
  slug: marketplace-statemedicaidlist
- name: StateRateArea
  property_count: 2
  slug: marketplace-stateratearea
- name: SuppressionStatus
  property_count: 0
  slug: marketplace-suppressionstatus
- name: UtilizationEnum
  property_count: 0
  slug: marketplace-utilizationenum
- name: ZIPCounty
  property_count: 4
  slug: marketplace-zipcounty
- name: Code
  property_count: 3
  slug: ppl-code
- name: Cost
  property_count: 4
  slug: ppl-cost
jsonld:
- class_count: 0
  name: Cms Apis Context
  property_count: 0
  slug: cms-apis
- class_count: 150
  name: Cms Context
  property_count: 88
  slug: cms-context
layout: provider
mcp_servers:
- description: ''
  name: Centers for Medicare and Medicaid Services MCP Server
  slug: centers-for-medicare-and-medicaid-services-mcp-server
modified: '2026-08-15'
name: Centers for Medicare and Medicaid Services
nav: Providers
network: true
overview: 'Centers for Medicare and Medicaid Services publishes 32 APIs on the [APIs.io](https://apis.io/) network, including API Reference API, Bulk Data API, Code Search API, and 29 more. Tagged areas include Medicare, Medicaid, Healthcare, Health Insurance, and FHIR.


  The Centers for Medicare and Medicaid Services catalog on APIs.io includes 2 JSON-LD contexts and 1 Spectral governance ruleset.


  Centers for Medicare and Medicaid Services'' developer surface includes authentication, developer portal, changelog, sandbox, CLI, code examples, documentation, and 72 more developer resources.'
plans:
- name: Cms Plans Pricing
  plan_count: 3
  slug: cms-plans-pricing
- name: Plans
  plan_count: 4
  slug: plans
random_paper: 8
rate_limits:
- limit_count: 4
  name: Cms Rate Limits
  slug: cms-rate-limits
- limit_count: 0
  name: Rate Limits
  slug: rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: Centers for Medicare and Medicaid Services API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: cms-jsonschema-spectral-rules
scopes:
- name: Cms Scopes
  scope_count: 6
  slug: cms-scopes
  summary_line: 6 scopes · authorizationCode
score:
  band: exemplar
  composite: 85.5
  coverage:
    artifact_dirs: 31
    catalog_gap: 36.8
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 89.5
    commercial_clarity: 89.5
    contract_governance: 43.2
    contract_quality: 63.2
    developer_ergonomics: 82.7
    discoverability: 66.7
    governance: 43.2
    operational_transparency: 84.2
  open_source:
    applies: true
    score: 100.0
  previous_composite: 85.5
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 94.1
      derived: 0
      marker_coverage: 11.8
      total: 17
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 83.8
  schema_version: 0.17.2
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/cms/refs/heads/main/screenshots/cms-2026-06-20T174629.png
security:
- kind: authentication
  name: Cms Authentication
  slug: cms-authentication
  summary_line: apiKey/http (bearer)/http (basic)/oauth2 · 9 schemes
- kind: domain-security
  name: Cms Domain Security
  slug: cms-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Cms Vulnerability Disclosure
  slug: cms-vulnerability-disclosure
  summary_line: disclosure policy published
- kind: trust-center
  name: Cms Trust Center
  slug: cms-trust-center
  summary_line: trust center published
slug: cms
tags:
- Medicare
- Medicaid
- Healthcare
- Health Insurance
- FHIR
- Federal-Government
- Drug Spending
- Provider Data
- Quality Measures
- Claims Data
website: https://www.cms.gov/
---
