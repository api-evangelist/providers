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
- acting_count: 10
  human_in_the_loop: 0
  name: Cms Agentic Access
  operation_count: 43
  slug: cms-agentic-access
  summary_line: 43 operations · 10 acting
api_count: 16
apis:
- description: Enables Medicare Accountable Care Organizations (ACOs) and alternative payment model participants to retrieve Medicare Part A, B, and D claims data for their attributed enrollees. Implements the HL7 B
  name: CMS Beneficiary Claims Data API (BCDA)
  slug: cms-beneficiary-claims-data-api-bcda
- description: Enables stand-alone Medicare Part D Prescription Drug Plan sponsors to retrieve bulk Medicare Part A and B claims data for their active beneficiaries using the FHIR standard in NDJSON format. Authenti
  name: CMS AB2D API (Claims Data to Part D Sponsors)
  slug: cms-ab2d-api-claims-data-to-part-d-sponsors
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
artifact_total: 128
common:
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
modified: '2026-06-13'
name: Centers for Medicare and Medicaid Services
nav: Providers
network: true
overview: 'Centers for Medicare and Medicaid Services publishes 11 APIs on the [APIs.io](https://apis.io/) network, including API Reference API, Bulk Data API, Code Search API, and 8 more. Tagged areas include Medicare, Medicaid, Healthcare, Health Insurance, and FHIR.


  The Centers for Medicare and Medicaid Services catalog on APIs.io includes 2 JSON-LD contexts and 1 Spectral governance ruleset.


  Centers for Medicare and Medicaid Services'' developer surface includes authentication, developer portal, and 7 more developer resources.'
plans:
- name: Plans
  plan_count: 4
  slug: plans
random_paper: 77
rate_limits:
- limit_count: 0
  name: Rate Limits
  slug: rate-limits
rules:
- name: Centers for Medicare and Medicaid Services API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: cms-jsonschema-spectral-rules
score:
  band: thin
  composite: 36.7
  delta: -7.9
  facets:
    commercial_clarity: 39.5
    contract_quality: 50.0
    developer_ergonomics: 19.6
    discoverability: 74.1
    governance: 58.3
    operational_transparency: 5.3
  previous_composite: 44.6
  provenance:
    agentic_access: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 11
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 21.3
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: falling
screenshot: https://raw.githubusercontent.com/api-evangelist/cms/refs/heads/main/screenshots/cms-2026-06-20T174629.png
security:
- kind: authentication
  name: Cms Authentication
  slug: cms-authentication
  summary_line: apiKey · 3 schemes
- kind: domain-security
  name: Cms Domain Security
  slug: cms-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: cms
tags:
- Medicare
- Medicaid
- Healthcare
- Health Insurance
- FHIR
- Federal Government
- Drug Spending
- Provider Data
- Quality Measures
- Claims Data
website: https://developer.cms.gov/
---
