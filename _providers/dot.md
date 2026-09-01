---
access_model:
  confidence: medium
  label: Free · Open access
  onboarding: open
  pricing: free
  public: true
  source:
  - plans
  trial: false
  try_now: true
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
    dry_run_mode: na
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: na
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 22.9
  scored_at: '2026-09-01'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Dot Agentic Access
  operation_count: 44
  slug: dot-agentic-access
  summary_line: 44 operations
api_count: 1
apis:
- description: The FMCSA QCMobile API provides safety performance data for U.S. Department of Transportation registered motor carriers. Developers can query carrier registration information, licensing, insurance, op
  name: FMCSA QCMobile API
  slug: fmcsa-qcmobile-api
- description: 'The FMCSA SaferBus API is a RESTful service making available safety performance data for U.S. DOT-registered bus companies. It enables developers to build consumer-facing products that help travelers '
  name: FMCSA SaferBus API
  slug: fmcsa-saferbus-api
- description: The NHTSA Vehicle Product Information Catalog (vPIC) API provides programmatic access to vehicle make, model, manufacturer, and type data compiled by NHTSA. Key capabilities include VIN decoding (sing
  name: NHTSA vPIC Vehicle API
  slug: nhtsa-vpic-api
- description: NHTSA provides public datasets and APIs covering vehicle safety complaints, recalls, safety ratings (NCAP), and defect investigations. Complaint data entered into NHTSA's Office of Defects Investigati
  name: NHTSA Datasets and APIs
  slug: nhtsa-datasets-api
- description: 'The U.S. Department of Transportation Open Data Portal provides access to transportation datasets published by DOT agencies including FMCSA, NHTSA, FTA, BTS, FAA, PHMSA, and more. The portal supports '
  name: DOT Open Data Portal
  slug: dot-data-portal
- description: Child Seat search and list endpoints
  name: US Department of Transportation childSeats API
  slug: dot-childseats-api
- description: Equipment search and list endpoints
  name: US Department of Transportation equipment API
  slug: dot-equipment-api
- description: Early Warning Report endpoints
  name: US Department of Transportation ewr API
  slug: dot-ewr-api
- description: Foreign Campaign search and list endpoints
  name: US Department of Transportation foreignCampaigns API
  slug: dot-foreigncampaigns-api
- description: Recalls, Investigations, Complaints, and Manufacturer Communications
  name: US Department of Transportation safetyIssues API
  slug: dot-safetyissues-api
- description: Tire search and list endpoints
  name: US Department of Transportation tires API
  slug: dot-tires-api
- description: Vehicle search and list endpoints
  name: US Department of Transportation vehicles API
  slug: dot-vehicles-api
artifact_total: 97
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: NHTSA childSeats API
  slug: open-dot-childseats-api
- collection_type: open
  name: NHTSA childSeats equipment API
  slug: open-dot-equipment-api
- collection_type: open
  name: NHTSA childSeats ewr API
  slug: open-dot-ewr-api
- collection_type: open
  name: NHTSA childSeats foreignCampaigns API
  slug: open-dot-foreigncampaigns-api
- collection_type: open
  name: NHTSA childSeats safetyIssues API
  slug: open-dot-safetyissues-api
- collection_type: open
  name: NHTSA childSeats tires API
  slug: open-dot-tires-api
- collection_type: open
  name: NHTSA childSeats vehicles API
  slug: open-dot-vehicles-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/dot-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/dot-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.transportation.gov/
- group: docs
  title: ''
  type: Documentation
  url: https://www.transportation.gov/developer
- group: build
  title: ''
  type: GitHubOrg
  url: https://github.com/usdot-jpo-ode
- group: company
  title: ''
  type: Blog
  url: https://www.transportation.gov/newsroom
- group: operate
  title: ''
  type: StatusPage
  url: https://www.transportation.gov/status
- group: other
  title: ''
  type: X
  url: https://twitter.com/USDOT
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/us-department-of-transportation
- group: commercial
  title: ''
  type: Plans
  url: plans/dot-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/dot-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/dot-finops.yml
created: '2026-06-13'
description: The U.S. Department of Transportation (DOT) oversees federal transportation policy and operates multiple agencies that publish public REST APIs covering trucking and motor carrier safety (FMCSA), vehicle product information and safety recalls (NHTSA), aviation safety and airspace data (FAA), transit statistics, and transportation data portals. DOT APIs are free public government services requiring API key registration via Login.gov or the relevant agency developer portal.
examples:
- key_count: 44
  name: Nhtsa Datasets Api Examples
  slug: nhtsa-datasets-api-examples
finops:
- name: Dot Finops
  service_category: Government / Public Safety Data
  slug: dot-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/dot.png
json_schemas:
- name: AssociatedProduct
  property_count: 9
  slug: associatedproduct
- name: Attributes
  property_count: 2
  slug: attributes
- name: Childseat
  property_count: 8
  slug: childseat
- name: ChildSeatMode
  property_count: 15
  slug: childseatmode
- name: ChildSeatModeRating
  property_count: 4
  slug: childseatmoderating
- name: Complaint
  property_count: 22
  slug: complaint
- name: ComplaintAggregate
  property_count: 12
  slug: complaintaggregate
- name: ComplaintComponent
  property_count: 4
  slug: complaintcomponent
- name: Component
  property_count: 4
  slug: component
- name: Components
  property_count: 1
  slug: components
- name: CrashTestRating
  property_count: 10
  slug: crashtestrating
- name: Document
  property_count: 6
  slug: document
- name: Documents
  property_count: 5
  slug: documents
- name: Equipment
  property_count: 3
  slug: equipment
- name: EWRInjury
  property_count: 15
  slug: ewrinjury
- name: EWRManufacturer
  property_count: 3
  slug: ewrmanufacturer
- name: EWRManufacturerDetail
  property_count: 5
  slug: ewrmanufacturerdetail
- name: EWRProduction
  property_count: 9
  slug: ewrproduction
- name: EWRPropertyDamage
  property_count: 45
  slug: ewrpropertydamage
- name: EWRReportPeriod
  property_count: 3
  slug: ewrreportperiod
- name: EWRReportPeriodCategory
  property_count: 5
  slug: ewrreportperiodcategory
- name: Feature
  property_count: 3
  slug: feature
- name: ForeignCampaign
  property_count: 6
  slug: foreigncampaign
- name: InspectionStationDetails
  property_count: 14
  slug: inspectionstationdetails
- name: Investigation
  property_count: 14
  slug: investigation
- name: InvestigationAggregate
  property_count: 8
  slug: investigationaggregate
- name: InvestigationComponent
  property_count: 4
  slug: investigationcomponent
- name: Investigations
  property_count: 2
  slug: investigations
- name: Makes
  property_count: 2
  slug: makes
- name: Manufacturer
  property_count: 6
  slug: manufacturer
- name: ManufacturerCommunication
  property_count: 11
  slug: manufacturercommunication
- name: ManufacturerCommunicationComponent
  property_count: 3
  slug: manufacturercommunicationcomponent
- name: Media
  property_count: 2
  slug: media
- name: Message
  property_count: 4
  slug: message
- name: Meta
  property_count: 3
  slug: meta
- name: MFRCommunicationAggregate
  property_count: 6
  slug: mfrcommunicationaggregate
- name: Models
  property_count: 3
  slug: models
- name: ModelYears
  property_count: 1
  slug: modelyears
- name: NCAPRating
  property_count: 72
  slug: ncaprating
- name: Note
  property_count: 3
  slug: note
- name: Pagination
  property_count: 9
  slug: pagination
- name: PartialChildSeat
  property_count: 4
  slug: partialchildseat
- name: PartialVehicle
  property_count: 7
  slug: partialvehicle
- name: Product
  property_count: 12
  slug: product
- name: ProductComplaint
  property_count: 4
  slug: productcomplaint
- name: ProductManfacturerCommunication
  property_count: 3
  slug: productmanfacturercommunication
- name: Products
  property_count: 5
  slug: products
- name: Rating
  property_count: 8
  slug: rating
- name: Recall
  property_count: 26
  slug: recall
- name: RecallAggregate
  property_count: 11
  slug: recallaggregate
- name: RecallInvestigation
  property_count: 3
  slug: recallinvestigation
- name: Recalls
  property_count: 2
  slug: recalls
- name: RecommendedFeature
  property_count: 8
  slug: recommendedfeature
- name: SafetyConcern
  property_count: 2
  slug: safetyconcern
- name: SafetyFeature
  property_count: 3
  slug: safetyfeature
- name: SafetyIssue
  property_count: 7
  slug: safetyissue
- name: SafetyIssueAggregate
  property_count: 4
  slug: safetyissueaggregate
- name: SafetyRatingAggregate
  property_count: 3
  slug: safetyratingaggregate
- name: SafetyRatingFullAggregate
  property_count: 1
  slug: safetyratingfullaggregate
- name: test
  property_count: 0
  slug: test
- name: Tire
  property_count: 9
  slug: tire
- name: TireBrand
  property_count: 1
  slug: tirebrand
- name: Trims
  property_count: 5
  slug: trims
- name: Vehicle
  property_count: 19
  slug: vehicle
- name: VehicleBasic
  property_count: 15
  slug: vehiclebasic
- name: VehicleDetails
  property_count: 17
  slug: vehicledetails
- name: VehicleFull
  property_count: 16
  slug: vehiclefull
- name: VehicleMinimal
  property_count: 9
  slug: vehicleminimal
jsonld:
- class_count: 32
  name: Dot Context
  property_count: 0
  slug: dot-context
- class_count: 0
  name: Dot Provider Context
  property_count: 0
  slug: dot-provider
layout: provider
modified: '2026-06-13'
name: US Department of Transportation
nav: Providers
network: true
overview: 'US Department of Transportation publishes 7 APIs on the [APIs.io](https://apis.io/) network, including childSeats API, equipment API, ewr API, and 4 more. Tagged areas include Government, Transportation, Trucking, Aviation, and Vehicle Safety.


  The US Department of Transportation catalog on APIs.io includes 2 JSON-LD contexts and 1 Spectral governance ruleset.


  US Department of Transportation''s developer surface includes documentation, engineering blog, and 10 more developer resources.'
plans:
- name: Dot Plans Pricing
  plan_count: 1
  slug: dot-plans-pricing
random_paper: 12
rate_limits:
- limit_count: 5
  name: Dot Rate Limits
  slug: dot-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: US Department of Transportation API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: dot-jsonschema-spectral-rules
score:
  band: thin
  composite: 38.4
  coverage:
    artifact_dirs: 14
    catalog_gap: 43.8
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 28.9
    commercial_clarity: 28.9
    contract_governance: 9.8
    contract_quality: 46.3
    developer_ergonomics: 23.8
    discoverability: 68.5
    governance: 9.8
    operational_transparency: 52.6
  previous_composite: 38.4
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 7
  regulatory:
    applies: true
    matched_via: tags
    regime: Government & Public Sector
    regime_id: government
    score: 31.5
  schema_version: 0.17.2
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/dot/refs/heads/main/screenshots/dot-2026-06-20T180157.png
security:
- kind: domain-security
  name: Dot Domain Security
  slug: dot-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: dot
tags:
- Government
- Transportation
- Trucking
- Aviation
- Vehicle Safety
- Transit
- Open Data
website: https://www.transportation.gov/
---
