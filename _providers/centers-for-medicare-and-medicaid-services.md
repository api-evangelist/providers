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
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 30.6
  scored_at: '2026-08-03'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Centers For Medicare And Medicaid Services Agentic Access
  operation_count: 7
  slug: centers-for-medicare-and-medicaid-services-agentic-access
  summary_line: 7 operations
api_count: 12
apis:
- description: The Beneficiary Claims Data API (BCDA) is a Bulk FHIR API that delivers Medicare Part A, B, and D claims data to Medicare Shared Savings Program ACOs, ACO REACH participants, and other Alternative Pay
  name: CMS Beneficiary Claims Data API (BCDA)
  slug: cms-bcda
- description: Data at the Point of Care is a FHIR Bulk Data API that delivers Original Medicare claims data to fee-for-service providers for the patients currently under their care, enabling clinicians to see a pat
  name: CMS Data at the Point of Care (DPC) API
  slug: cms-dpc
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
artifact_total: 20
collections:
- collection_type: open
  name: CMS Blue Button 2.0 API
  slug: open-centers-for-medicare-and-medicaid-services-cms-blue-button-2
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/centers-for-medicare-and-medicaid-services-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/centers-for-medicare-and-medicaid-services-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/centers-for-medicare-and-medicaid-services-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/centers-for-medicare-and-medicaid-services-scopes.yml
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
created: '2024-12-03'
description: The Centers for Medicare and Medicaid Services (CMS) is the federal agency that provides health coverage to more than 160 million Americans through Medicare, Medicaid, the Children's Health Insurance Program (CHIP), and the Health Insurance Marketplace. CMS operates one of the largest public API programs in the U.S. government, including the FHIR-based Blue Button 2.0, Beneficiary Claims Data API (BCDA), and Data at the Point of Care (DPC); the data.cms.gov Socrata Open Data API covering Medicare claims, provider, and enrollment datasets; the Medicare Provider Data Catalog (Hospital Compare, Nursing Home Compare); the Healthcare.gov Marketplace API; NPPES and NPI Registry APIs; the QPP Measures API; and Medicaid Transformed Medicaid Statistical Information System (T-MSIS) resources.
finops:
- name: Centers For Medicare And Medicaid Services Finops
  service_category: API
  slug: centers-for-medicare-and-medicaid-services-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/centers-for-medicare-and-medicaid-services.png
layout: provider
modified: '2026-05-19'
name: Centers for Medicare and Medicaid Services
nav: Providers
network: true
overview: 'Centers for Medicare and Medicaid Services publishes 4 APIs on the [APIs.io](https://apis.io/) network, including Capability API, Coverage API, ExplanationOfBenefit API, and 1 more. Tagged areas include BCDA, Blue Button, CMS, Claims, and DPC.


  Centers for Medicare and Medicaid Services'' developer surface includes authentication and 15 more developer resources.'
plans:
- name: Centers For Medicare And Medicaid Services Plans Pricing
  plan_count: 3
  slug: centers-for-medicare-and-medicaid-services-plans-pricing
random_paper: 40
rate_limits:
- limit_count: 5
  name: Centers For Medicare And Medicaid Services Rate Limits
  slug: centers-for-medicare-and-medicaid-services-rate-limits
scopes:
- name: Centers For Medicare And Medicaid Services Scopes
  scope_count: 3
  slug: centers-for-medicare-and-medicaid-services-scopes
  summary_line: 3 scopes · authorizationCode
score:
  band: thin
  composite: 39.8
  delta: 0.0
  facets:
    commercial_clarity: 50.0
    contract_quality: 64.3
    developer_ergonomics: 10.9
    discoverability: 64.8
    governance: 0.0
    operational_transparency: 36.8
  previous_composite: 39.8
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
    regime: Health
    regime_id: health
    score: 41.3
  schema_version: 0.9
  scored_at: '2026-08-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/centers-for-medicare-and-medicaid-services/refs/heads/main/screenshots/centers-for-medicare-and-medicaid-services-2026-06-20T174129.png
security:
- kind: authentication
  name: Centers For Medicare And Medicaid Services Authentication
  slug: centers-for-medicare-and-medicaid-services-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Centers For Medicare And Medicaid Services Domain Security
  slug: centers-for-medicare-and-medicaid-services-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: centers-for-medicare-and-medicaid-services
tags:
- BCDA
- Blue Button
- CMS
- Claims
- DPC
- FHIR
- Federal Government
- Healthcare
- Interoperability
- Marketplace
- Medicaid
- Medicare
- Open Data
- Provider Data
- Socrata
website: https://www.cms.gov/
---
