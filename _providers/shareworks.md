---
access_model:
  confidence: high
  label: Enterprise · Self-serve signup
  onboarding: self-serve
  pricing: enterprise
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
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 25.5
  scored_at: '2026-09-01'
agentic_access:
- acting_count: 24
  human_in_the_loop: 1
  name: Shareworks Agentic Access
  operation_count: 48
  slug: shareworks-agentic-access
  summary_line: 48 operations · 24 acting · 1 human-in-the-loop
api_count: 1
apis:
- description: 'The Shareworks Public API is a REST-based system for managing equity compensation plans including stock options, RSU grants, ESPP, and participant data. The API supports both read-only and read-write '
  name: Shareworks Public API
  slug: shareworks-public-api
- description: The Authentication Token API from Shareworks — 3 operation(s) for authentication token.
  name: Shareworks Authentication Token API
  slug: shareworks-authentication-token-api
- description: The Authorized Capital API from Shareworks — 5 operation(s) for authorized capital.
  name: Shareworks Authorized Capital API
  slug: shareworks-authorized-capital-api
- description: The Award Type API from Shareworks — 1 operation(s) for award type.
  name: Shareworks Award Type API
  slug: shareworks-award-type-api
- description: The Company API from Shareworks — 2 operation(s) for company.
  name: Shareworks Company API
  slug: shareworks-company-api
- description: The Company Board API from Shareworks — 3 operation(s) for company board.
  name: Shareworks Company Board API
  slug: shareworks-company-board-api
- description: The Company Integration API from Shareworks — 1 operation(s) for company integration.
  name: Shareworks Company Integration API
  slug: shareworks-company-integration-api
- description: The Entity Stakeholder API from Shareworks — 3 operation(s) for entity stakeholder.
  name: Shareworks Entity Stakeholder API
  slug: shareworks-entity-stakeholder-api
- description: The Grant API from Shareworks — 2 operation(s) for grant.
  name: Shareworks Grant API
  slug: shareworks-grant-api
- description: The Holdings API from Shareworks — 2 operation(s) for holdings.
  name: Shareworks Holdings API
  slug: shareworks-holdings-api
- description: The Individual Stakeholder API from Shareworks — 3 operation(s) for individual stakeholder.
  name: Shareworks Individual Stakeholder API
  slug: shareworks-individual-stakeholder-api
- description: The Plan API from Shareworks — 1 operation(s) for plan.
  name: Shareworks Plan API
  slug: shareworks-plan-api
- description: The Stock Certificate API from Shareworks — 2 operation(s) for stock certificate.
  name: Shareworks Stock Certificate API
  slug: shareworks-stock-certificate-api
- description: The Stock Filing API from Shareworks — 2 operation(s) for stock filing.
  name: Shareworks Stock Filing API
  slug: shareworks-stock-filing-api
- description: The Vesting Schedule API from Shareworks — 3 operation(s) for vesting schedule.
  name: Shareworks Vesting Schedule API
  slug: shareworks-vesting-schedule-api
artifact_total: 119
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Shareworks Admin REST Authentication Token API
  slug: open-shareworks-authentication-token-api
- collection_type: open
  name: Shareworks Admin REST Authentication Token Authorized Capital API
  slug: open-shareworks-authorized-capital-api
- collection_type: open
  name: Shareworks Admin REST Authentication Token Award Type API
  slug: open-shareworks-award-type-api
- collection_type: open
  name: Shareworks Admin REST Authentication Token Company API
  slug: open-shareworks-company-api
- collection_type: open
  name: Shareworks Admin REST Authentication Token Company Board API
  slug: open-shareworks-company-board-api
- collection_type: open
  name: Shareworks Admin REST Authentication Token Company Integration API
  slug: open-shareworks-company-integration-api
- collection_type: open
  name: Shareworks Admin REST Authentication Token Entity Stakeholder API
  slug: open-shareworks-entity-stakeholder-api
- collection_type: open
  name: Shareworks Admin REST Authentication Token Grant API
  slug: open-shareworks-grant-api
- collection_type: open
  name: Shareworks Admin REST Authentication Token Holdings API
  slug: open-shareworks-holdings-api
- collection_type: open
  name: Shareworks Admin REST Authentication Token Individual Stakeholder API
  slug: open-shareworks-individual-stakeholder-api
- collection_type: open
  name: Shareworks Admin REST Authentication Token Plan API
  slug: open-shareworks-plan-api
- collection_type: open
  name: Shareworks Admin REST Authentication Token Read Access API
  slug: open-shareworks-read-access-api
- collection_type: open
  name: Shareworks Admin REST Authentication Token Stock Certificate API
  slug: open-shareworks-stock-certificate-api
- collection_type: open
  name: Shareworks Admin REST Authentication Token Stock Filing API
  slug: open-shareworks-stock-filing-api
- collection_type: open
  name: Shareworks Admin REST Authentication Token Vesting Schedule API
  slug: open-shareworks-vesting-schedule-api
- collection_type: open
  name: Shareworks Admin REST Authentication Token Write Access API
  slug: open-shareworks-write-access-api
common:
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/shareworks-capability-edges.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/shareworks-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/shareworks-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/shareworks-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/shareworks-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://www.morganstanley.com/atwork/shareworks
- group: docs
  title: ''
  type: Documentation
  url: https://downloads.shareworks.com/api/index.html
- group: build
  title: ''
  type: GitHubOrg
  url: https://github.com/shareworks
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/morgan-stanley-at-work
- group: company
  title: ''
  type: Blog
  url: https://www.morganstanley.com/press-releases/morgan-stanley-at-work-and-pave-announce-api-integration
- group: commercial
  title: ''
  type: Pricing
  url: https://www.vendr.com/marketplace/shareworks
- group: operate
  title: ''
  type: Support
  url: https://support.solium.com/hc/en-us
- group: commercial
  title: ''
  type: Plans
  url: plans/shareworks-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/shareworks-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/shareworks-finops.yml
created: '2026-06-13'
description: Shareworks by Morgan Stanley is an equity compensation management platform offering REST APIs for managing stock option plans, RSU grants, ESPP, and employee equity administration for both public and private companies. The platform provides predictable resource-oriented URLs, JSON-encoded responses, and JWT-based bearer token authentication. Access requires IP whitelisting and initial setup through Morgan Stanley at Work.
examples:
- key_count: 1
  name: Shareworks Examples
  slug: shareworks-examples
finops:
- name: Shareworks Finops
  service_category: ''
  slug: shareworks-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/shareworks.png
json_schemas:
- name: Access Token Body
  property_count: 1
  slug: AccessToken
- name: Access Token Body
  property_count: 1
  slug: AccessTokenRequest
- name: Token Response
  property_count: 7
  slug: AccessTokenResponse
- name: Token Wrapper
  property_count: 1
  slug: AccessTokenWrapper
- name: Authorized Capital Response
  property_count: 11
  slug: AuthorizedCapitalDetails
- name: Award Type Response
  property_count: 2
  slug: AwardTypeDetails
- name: Authorized Capital Class Detailed Response
  property_count: 7
  slug: ClassOfSecuritiesDetails
- name: Class Summary Response
  property_count: 5
  slug: ClassOfSecuritiesSummaryDetails
- name: Company Address Body
  property_count: 8
  slug: CompanyAddressCrudRequest
- name: Company Address Response
  property_count: 9
  slug: CompanyAddressDetails
- name: Company Board Appointment Body
  property_count: 9
  slug: CompanyBoardAppointmentCreateCrudRequest
- name: Company Board Appointment Response
  property_count: 13
  slug: CompanyBoardAppointmentDetails
- name: Company Board Appointment Body
  property_count: 8
  slug: CompanyBoardAppointmentUpdateCrudRequest
- name: Company Board Body
  property_count: 4
  slug: CompanyBoardCrudRequest
- name: Company Board Response
  property_count: 5
  slug: CompanyBoardDetails
- name: Company Board Detailed Response
  property_count: 6
  slug: CompanyBoardDetailsWithAppointments
- name: Company Contact Body
  property_count: 5
  slug: CompanyContactCrudRequest
- name: Company Contact Response
  property_count: 6
  slug: CompanyContactDetails
- name: Company Body
  property_count: 12
  slug: CompanyCrudRequest
- name: Company Response
  property_count: 10
  slug: CompanyDetails
- name: Company Integration Response
  property_count: 2
  slug: CompanyIntegrationDetails
- name: Company Integration Body
  property_count: 1
  slug: CompanyIntegrationRequest
- name: Class Designated Share Summary Response
  property_count: 3
  slug: DesignatedSharesSummaryDetails
- name: Entity Stakeholder Body
  property_count: 2
  slug: EntityStakeholderCrudRequest
- name: Entity Stakeholder Response
  property_count: 3
  slug: EntityStakeholderDetails
- name: Entity Stakeholder Search Body
  property_count: 2
  slug: EntityStakeholderSearchRequest
- name: Validation Error
  property_count: 2
  slug: ErrorWithCode
- name: Fund Details Response
  property_count: 4
  slug: FundDetails
- name: Individual Stakeholder Body
  property_count: 4
  slug: IndividualStakeholderCrudRequest
- name: Individual Stakeholder Response
  property_count: 5
  slug: IndividualStakeholderDetails
- name: Individual Stakeholder Search Body
  property_count: 3
  slug: IndividualStakeholderSearchRequest
- name: Manual Vesting Row Body
  property_count: 2
  slug: ManualVestingRowCrudRequest
- name: Manual Vesting Row Response
  property_count: 2
  slug: ManualVestingRowDetails
- name: Manual Vesting Schedule Response
  property_count: 3
  slug: ManualVestingScheduleDetails
- name: Plan Summary Response
  property_count: 13
  slug: PlanSummaryDetails
- name: Plan Summary Detailed Response
  property_count: 14
  slug: PlanSummaryDetailsWithGrants
- name: Error Response
  property_count: 4
  slug: RestApiErrorResponse
- name: Designation Summary Response
  property_count: 20
  slug: SecuritiesDesignationDetails
- name: Plan Body
  property_count: 4
  slug: SharePoolPlanCreationRequest
- name: Plan Response
  property_count: 5
  slug: SharePoolPlanDetails
- name: Vesting Acceleration Body
  property_count: 3
  slug: StakeholderGrantAcceleratedVestingCrudRequest
- name: Accelerated Vesting Response
  property_count: 3
  slug: StakeholderGrantAcceleratedVestingDetails
- name: Grant Body
  property_count: 15
  slug: StakeholderGrantCrudRequest
- name: Grant Response
  property_count: 20
  slug: StakeholderGrantDetails
- name: Grant Summary Response
  property_count: 23
  slug: StakeholderGrantSummaryDetails
- name: Holdings Summary Response
  property_count: 2
  slug: StakeholderHoldingsDetails
- name: Stakeholder Holdings Response
  property_count: 8
  slug: StakeholderHoldingsSummaryDetails
- name: Stock Certificate Body
  property_count: 9
  slug: StockCertificateCrudRequest
- name: Stock Certificate Response
  property_count: 14
  slug: StockCertificateDetails
- name: Stock Certificate Summary Response
  property_count: 16
  slug: StockCertificateSummaryDetails
- name: Stock Filing Class Response
  property_count: 3
  slug: StockFilingClassDetails
- name: Stock Filing Designation Response
  property_count: 11
  slug: StockFilingDesignationDetails
- name: Stock Filing Response
  property_count: 4
  slug: StockFilingDetails
- name: Stock Filing Designation Body
  property_count: 12
  slug: StockFilingWithNewDesignationCreationRequest
- name: Vesting Schedule Body
  property_count: 7
  slug: VestingScheduleCrudRequest
- name: Vesting Schedule Response
  property_count: 8
  slug: VestingScheduleDetails
- name: Vesting Schedule Row Response
  property_count: 5
  slug: VestingScheduleRowDetails
- name: Vesting Schedule Row Body
  property_count: 4
  slug: VestingScheduleRowRequest
- name: Warrant Details Response
  property_count: 3
  slug: WarrantsSummaryDetails
- name: WrappedCollectionAwardTypeDetails
  property_count: 2
  slug: WrappedCollectionAwardTypeDetails
- name: WrappedCollectionFundDetails
  property_count: 2
  slug: WrappedCollectionFundDetails
- name: WrappedCollectionManualVestingScheduleDetails
  property_count: 2
  slug: WrappedCollectionManualVestingScheduleDetails
- name: WrappedCollectionSecuritiesDesignationDetails
  property_count: 2
  slug: WrappedCollectionSecuritiesDesignationDetails
- name: WrappedCollectionStakeholderHoldingsSummaryDetails
  property_count: 2
  slug: WrappedCollectionStakeholderHoldingsSummaryDetails
- name: WrappedDataAuthorizedCapitalDetails
  property_count: 2
  slug: WrappedDataAuthorizedCapitalDetails
- name: WrappedDataClassOfSecuritiesDetails
  property_count: 2
  slug: WrappedDataClassOfSecuritiesDetails
- name: WrappedDataCompanyBoardAppointmentDetails
  property_count: 2
  slug: WrappedDataCompanyBoardAppointmentDetails
- name: WrappedDataCompanyBoardDetailsWithAppointments
  property_count: 2
  slug: WrappedDataCompanyBoardDetailsWithAppointments
- name: WrappedDataCompanyDetails
  property_count: 2
  slug: WrappedDataCompanyDetails
- name: WrappedDataEntityStakeholderDetails
  property_count: 2
  slug: WrappedDataEntityStakeholderDetails
- name: WrappedDataIndividualStakeholderDetails
  property_count: 2
  slug: WrappedDataIndividualStakeholderDetails
- name: WrappedDataPlanSummaryDetailsWithGrants
  property_count: 2
  slug: WrappedDataPlanSummaryDetailsWithGrants
- name: WrappedDataStakeholderGrantDetails
  property_count: 2
  slug: WrappedDataStakeholderGrantDetails
- name: WrappedDataStakeholderHoldingsSummaryDetails
  property_count: 2
  slug: WrappedDataStakeholderHoldingsSummaryDetails
- name: WrappedDataStockCertificateDetails
  property_count: 2
  slug: WrappedDataStockCertificateDetails
- name: WrappedDataStockFilingDetails
  property_count: 2
  slug: WrappedDataStockFilingDetails
- name: WrappedDataVestingScheduleDetails
  property_count: 2
  slug: WrappedDataVestingScheduleDetails
jsonld:
- class_count: 20
  name: Shareworks Context
  property_count: 13
  slug: shareworks-context
layout: provider
modified: '2026-06-13'
name: Shareworks
nav: Providers
network: true
overview: 'Shareworks publishes 15 APIs on the [APIs.io](https://apis.io/) network, including Public API, Authentication Token API, Authorized Capital API, and 12 more. Tagged areas include Equity Compensation, Stock Options, RSU, ESPP, and Employee Equity.


  The Shareworks catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Shareworks'' developer surface includes authentication, documentation, engineering blog, pricing, support, and 10 more developer resources.'
plans:
- name: Shareworks Plans Pricing
  plan_count: 2
  slug: shareworks-plans-pricing
random_paper: 5
rate_limits:
- limit_count: 4
  name: Shareworks Rate Limits
  slug: shareworks-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: Shareworks API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: shareworks-jsonschema-spectral-rules
score:
  band: developing
  composite: 42.9
  coverage:
    artifact_dirs: 16
    catalog_gap: 40.8
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 39.5
    commercial_clarity: 39.5
    contract_governance: 9.8
    contract_quality: 62.1
    developer_ergonomics: 33.3
    discoverability: 68.5
    governance: 9.8
    operational_transparency: 36.8
  previous_composite: 42.9
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 14
  schema_version: 0.18.0
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/shareworks/refs/heads/main/screenshots/shareworks-2026-06-20T193746.png
security:
- kind: authentication
  name: Shareworks Authentication
  slug: shareworks-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Shareworks Domain Security
  slug: shareworks-domain-security
  summary_line: TLSv1.2 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Shareworks Vulnerability Disclosure
  slug: shareworks-vulnerability-disclosure
  summary_line: disclosure policy published
slug: shareworks
tags:
- Equity Compensation
- Stock Options
- RSU
- ESPP
- Employee Equity
- Financial-Services
- Morgan Stanley
- Equity Administration
- Private Companies
- Public Companies
website: https://www.morganstanley.com/atwork/shareworks
---
