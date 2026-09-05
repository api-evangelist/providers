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
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 24.8
  scored_at: '2026-09-04'
agentic_access:
- acting_count: 3
  human_in_the_loop: 0
  name: Verisk Agentic Access
  operation_count: 6
  slug: verisk-agentic-access
  summary_line: 6 operations · 3 acting
api_count: 1
apis:
- description: Verisk UnderWriting API provides personal and commercial lines insurance underwriting data including homeowner data, motor vehicle reports, A-PLUS auto and property reports, LightSpeed prefill, geocod
  name: Verisk UnderWriting API
  slug: underwriting-api
- baseURL: https://api.verisk.com/insurance/v1
  baseurl_source: spec
  description: Catastrophe modeling and peril data
  name: Verisk Catastrophe API
  slug: verisk-catastrophe-api
- baseURL: https://api.verisk.com/insurance/v1
  baseurl_source: spec
  description: Claims analytics and benchmarking
  name: Verisk Claims API
  slug: verisk-claims-api
- baseURL: https://api.verisk.com/insurance/v1
  baseurl_source: spec
  description: Property risk data and analytics
  name: Verisk Property API
  slug: verisk-property-api
- baseURL: https://api.verisk.com/insurance/v1
  baseurl_source: spec
  description: Insurance risk scores and rating factors
  name: Verisk Risk Scoring API
  slug: verisk-risk-scoring-api
artifact_total: 81
collections:
- collection_type: postman
  name: Verisk Insurance Analytics Catastrophe API
  slug: postman-verisk-catastrophe-api
- collection_type: postman
  name: Verisk Insurance Analytics Catastrophe Claims API
  slug: postman-verisk-claims-api
- collection_type: postman
  name: Verisk Insurance Analytics Catastrophe Property API
  slug: postman-verisk-property-api
- collection_type: postman
  name: Verisk Insurance Analytics Catastrophe Risk Scoring API
  slug: postman-verisk-risk-scoring-api
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Verisk Insurance Analytics Catastrophe API
  slug: open-verisk-catastrophe-api
- collection_type: open
  name: Verisk Insurance Analytics Catastrophe Claims API
  slug: open-verisk-claims-api
- collection_type: open
  name: Verisk Insurance Analytics API
  slug: open-verisk-insurance-analytics
- collection_type: open
  name: Verisk Insurance Analytics Catastrophe Property API
  slug: open-verisk-property-api
- collection_type: open
  name: Verisk Insurance Analytics Catastrophe Risk Scoring API
  slug: open-verisk-risk-scoring-api
common:
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/verisk-capability-edges.yml
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/verisk/overview
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/verisk-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/verisk-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/verisk-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/verisk
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/verisk-analytics
- group: company
  title: ''
  type: Website
  url: https://www.verisk.com
- group: start
  title: ''
  type: Portal
  url: https://gateway-documentation.verisk.com/
- group: docs
  title: ''
  type: APIReference
  url: https://apicatalog.verisk.com/
- group: docs
  title: ''
  type: Documentation
  url: https://gateway.verisk.com/docs/MainPage.ashx
- group: start
  title: ''
  type: GettingStarted
  url: https://gateway.verisk.com/docs/Getting-Started.ashx
- group: auth
  title: ''
  type: Authentication
  url: https://gateway.verisk.com/docs/Authentication.ashx
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.verisk.com/terms-of-use/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.verisk.com/privacy-policy/
- group: operate
  title: ''
  type: Contact
  url: https://www.verisk.com/contact/
- group: design
  title: ''
  type: SpectralRules
  url: https://raw.githubusercontent.com/api-evangelist/verisk/refs/heads/main/rules/verisk-spectral-rules.yml
- group: design
  title: ''
  type: Vocabulary
  url: https://raw.githubusercontent.com/api-evangelist/verisk/refs/heads/main/vocabulary/verisk-vocabulary.yaml
created: '2026-05-03'
description: Verisk (formerly ISO) is a leading data analytics and technology company serving the insurance, energy, and financial services industries. Verisk provides risk scoring, actuarial data, property analytics, catastrophe modeling, claims benchmarking, and underwriting intelligence through RESTful APIs that power insurance pricing, reserving, and exposure management workflows.
examples:
- key_count: 5
  name: Insurance Analytics Address Example
  slug: insurance-analytics-address-example
- key_count: 6
  name: Insurance Analytics Address Lookup Request Example
  slug: insurance-analytics-address-lookup-request-example
- key_count: 6
  name: Insurance Analytics Claims Benchmarks Example
  slug: insurance-analytics-claims-benchmarks-example
- key_count: 7
  name: Insurance Analytics Construction Data Example
  slug: insurance-analytics-construction-data-example
- key_count: 2
  name: Insurance Analytics Coordinates Example
  slug: insurance-analytics-coordinates-example
- key_count: 8
  name: Insurance Analytics Fire Protection Class Example
  slug: insurance-analytics-fire-protection-class-example
- key_count: 2
  name: Insurance Analytics Peril Score Request Example
  slug: insurance-analytics-peril-score-request-example
- key_count: 1
  name: Insurance Analytics Peril Score Response Example
  slug: insurance-analytics-peril-score-response-example
- key_count: 5
  name: Insurance Analytics Property Lookup Response Example
  slug: insurance-analytics-property-lookup-response-example
- key_count: 7
  name: Insurance Analytics Property Risk Example
  slug: insurance-analytics-property-risk-example
- key_count: 2
  name: Insurance Analytics Risk Score Request Example
  slug: insurance-analytics-risk-score-request-example
- key_count: 1
  name: Insurance Analytics Risk Score Response Example
  slug: insurance-analytics-risk-score-response-example
- key_count: 7
  name: Verisk Property Risk Example
  slug: verisk-property-risk-example
features:
- description: Comprehensive property risk scoring including construction, fire protection class, and hazard exposure for fire, wind, hail, flood, and earthquake perils.
  name: Property Risk Assessment
- description: ISO Public Protection Classification (PPC) grading measuring community fire suppression capability on a 1-10 scale.
  name: ISO Fire Protection Classification
- description: Natural hazard exposure scores for hurricane, tornado, hail, wildfire, earthquake, and flood risk used for catastrophe risk management.
  name: Catastrophe Peril Scoring
- description: Risk scores for properties, policies, and portfolios including fire protection class, building code effectiveness grading, flood zone, and earthquake zone scores.
  name: Insurance Risk Scoring
- description: Industry claims benchmarking data for loss frequency, severity, combined ratio, and loss ratio metrics across lines of business and states.
  name: Claims Benchmarking
- description: Address-to-property resolution with geocoding to USGS coordinates and ISO property identification for prefill and underwriting workflows.
  name: Address Geocoding and Lookup
- description: LightSpeed and homeowner data APIs provide instant underwriting intelligence from a business name and address for small commercial and personal lines.
  name: Prefill and Accelerated Underwriting
- description: Benchmark API provides hail, wind, lightning, and hurricane wind analytics for property and auto claims and underwriting decisions.
  name: Weather Analytics Integration
finops:
- name: Verisk Finops
  service_category: Insurance Risk Analytics
  slug: verisk-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/verisk.png
integrations:
- description: Integrate risk scores and underwriting data directly into existing policy administration and underwriting workflow systems.
  name: Policy Administration Systems
- description: Embed weather analytics and property data into claims management platforms for faster adjudication.
  name: Claims Management Systems
- description: Feed peril scores and property data into catastrophe modeling platforms like AIR Worldwide and RMS for exposure analysis.
  name: Catastrophe Modeling Platforms
- description: API-enabled GenAI commercial underwriting assistant that integrates into existing policy administration systems.
  name: Generative AI Underwriting Assistant
json_schemas:
- name: AddressLookupRequest
  property_count: 6
  slug: insurance-analytics-address-lookup-request
- name: Address
  property_count: 5
  slug: insurance-analytics-address
- name: ClaimsBenchmarks
  property_count: 6
  slug: insurance-analytics-claims-benchmarks
- name: ConstructionData
  property_count: 7
  slug: insurance-analytics-construction-data
- name: Coordinates
  property_count: 2
  slug: insurance-analytics-coordinates
- name: FireProtectionClass
  property_count: 8
  slug: insurance-analytics-fire-protection-class
- name: PerilScoreRequest
  property_count: 2
  slug: insurance-analytics-peril-score-request
- name: PerilScoreResponse
  property_count: 1
  slug: insurance-analytics-peril-score-response
- name: PropertyLookupResponse
  property_count: 5
  slug: insurance-analytics-property-lookup-response
- name: PropertyRisk
  property_count: 7
  slug: insurance-analytics-property-risk
- name: RiskScoreRequest
  property_count: 2
  slug: insurance-analytics-risk-score-request
- name: RiskScoreResponse
  property_count: 1
  slug: insurance-analytics-risk-score-response
- name: Verisk Property Risk Assessment
  property_count: 7
  slug: verisk-property-risk
json_structures:
- name: Insurance Analytics Address Lookup Request Structure
  property_count: 6
  slug: insurance-analytics-address-lookup-request-structure
- name: Insurance Analytics Address Structure
  property_count: 5
  slug: insurance-analytics-address-structure
- name: Insurance Analytics Claims Benchmarks Structure
  property_count: 6
  slug: insurance-analytics-claims-benchmarks-structure
- name: Insurance Analytics Construction Data Structure
  property_count: 7
  slug: insurance-analytics-construction-data-structure
- name: Insurance Analytics Coordinates Structure
  property_count: 2
  slug: insurance-analytics-coordinates-structure
- name: Insurance Analytics Fire Protection Class Structure
  property_count: 8
  slug: insurance-analytics-fire-protection-class-structure
- name: Insurance Analytics Peril Score Request Structure
  property_count: 2
  slug: insurance-analytics-peril-score-request-structure
- name: Insurance Analytics Peril Score Response Structure
  property_count: 1
  slug: insurance-analytics-peril-score-response-structure
- name: Insurance Analytics Property Lookup Response Structure
  property_count: 5
  slug: insurance-analytics-property-lookup-response-structure
- name: Insurance Analytics Property Risk Structure
  property_count: 7
  slug: insurance-analytics-property-risk-structure
- name: Insurance Analytics Risk Score Request Structure
  property_count: 2
  slug: insurance-analytics-risk-score-request-structure
- name: Insurance Analytics Risk Score Response Structure
  property_count: 1
  slug: insurance-analytics-risk-score-response-structure
- name: Verisk Property Risk Structure
  property_count: 7
  slug: verisk-property-risk-structure
jsonld:
- class_count: 27
  name: Verisk Context
  property_count: 5
  slug: verisk-context
- class_count: 13
  name: Verisk Insurance Analytics Context
  property_count: 42
  slug: verisk-insurance-analytics-context
layout: provider
modified: '2026-05-19'
name: Verisk
nav: Providers
network: true
overview: 'Verisk publishes 4 APIs on the [APIs.io](https://apis.io/) network, including Catastrophe API, Claims API, Property API, and 1 more. Tagged areas include Insurance, Analytics, Risk Management, Property Data, and Catastrophe Modeling.


  The Verisk catalog on APIs.io includes 2 JSON-LD contexts and 2 Spectral governance rulesets.


  Verisk''s developer surface includes authentication, developer portal, API reference, documentation, getting-started guide, and 13 more developer resources.'
plans:
- name: Verisk Plans Pricing
  plan_count: 1
  slug: verisk-plans-pricing
random_paper: 9
rate_limits:
- limit_count: 1
  name: Verisk Rate Limits
  slug: verisk-rate-limits
rules:
- effective_rule_count: 6
  extends: []
  name: Verisk API Rules
  rule_count: 6
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 4
  slug: verisk-jsonschema-spectral-rules
- effective_rule_count: 81
  extends:
  - spectral:oas
  name: Verisk API Rules
  rule_count: 40
  severity_counts:
    error: 18
    hint: 0
    info: 3
    warn: 19
  slug: verisk-spectral-rules
score:
  band: developing
  composite: 41.4
  coverage:
    artifact_dirs: 17
    catalog_earned: 69.5
    catalog_earned_first_party: 0.0
    catalog_gap: 45.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -0.7
  facets:
    access_clarity: 13.2
    commercial_clarity: 13.2
    contract_governance: 28.8
    contract_quality: 73.1
    developer_ergonomics: 51.2
    discoverability: 59.3
    governance: 28.8
    operational_transparency: 7.9
  previous_composite: 42.1
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 4
  regulatory:
    applies: true
    matched_via: tags
    regime: Insurance
    regime_id: insurance
    score: 25.8
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/verisk/refs/heads/main/screenshots/verisk-2026-08-17T082751.png
security:
- kind: authentication
  name: Verisk Authentication
  slug: verisk-authentication
  summary_line: apiKey/http · 2 schemes
- kind: domain-security
  name: Verisk Domain Security
  slug: verisk-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: verisk
tags:
- Insurance
- Analytics
- Risk Management
- Property Data
- Catastrophe Modeling
- Underwriting
- Claims
use_cases:
- description: Use risk scores and property data to accurately price insurance policies for homeowners, auto, and commercial lines of business.
  name: Insurance Pricing and Rating
- description: Assess portfolio exposure to natural hazard perils and estimate probable maximum loss (PML) for catastrophe reinsurance programs.
  name: Catastrophe Risk Management
- description: Integrate weather analytics and property data to streamline field adjustments, reduce inspection costs, and accelerate claim cycle times.
  name: Claims Adjudication
- description: Automate underwriting decisions by integrating prefill data, motor vehicle reports, and coverage verification into policy administration systems.
  name: Underwriting Automation
- description: Monitor geographic concentration and peril exposure across insurance portfolios for risk management and regulatory reporting.
  name: Portfolio Risk Monitoring
website: https://www.verisk.com
---
