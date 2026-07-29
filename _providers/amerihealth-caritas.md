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
  band: agent-ready
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
    openapi_examples: verified
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 36.9
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 269
  human_in_the_loop: 0
  name: Amerihealth Caritas Agentic Access
  operation_count: 622
  slug: amerihealth-caritas-agentic-access
  summary_line: 622 operations · 269 acting
api_count: 25
apis:
- description: HL7 FHIR R4 Formulary API published to satisfy CMS-9115-F drug formulary publication requirements for Medicaid managed care and D-SNP populations. Covered drug lists, tier information, and prior autho
  name: AmeriHealth Caritas Formulary FHIR API
  slug: formulary-api
- description: Public corporate website for AmeriHealth Caritas, hosting the family-of-plans health plan finder, solutions overview, careers, member and provider portals for the federated state plans, and pointers t
  name: AmeriHealth Caritas Corporate Website
  slug: website
- description: The AllergyIntolerance FHIR resource type
  name: AmeriHealth Caritas AllergyIntolerance API
  slug: amerihealth-caritas-allergyintolerance-api
- description: The Claim FHIR resource type
  name: AmeriHealth Caritas Claim API
  slug: amerihealth-caritas-claim-api
- description: The Condition FHIR resource type
  name: AmeriHealth Caritas Condition API
  slug: amerihealth-caritas-condition-api
- description: The Coverage FHIR resource type
  name: AmeriHealth Caritas Coverage API
  slug: amerihealth-caritas-coverage-api
- description: The Encounter FHIR resource type
  name: AmeriHealth Caritas Encounter API
  slug: amerihealth-caritas-encounter-api
- description: The ExplanationOfBenefit FHIR resource type
  name: AmeriHealth Caritas ExplanationOfBenefit API
  slug: amerihealth-caritas-explanationofbenefit-api
- description: The HealthcareService FHIR resource type
  name: AmeriHealth Caritas HealthcareService API
  slug: amerihealth-caritas-healthcareservice-api
- description: The Immunization FHIR resource type
  name: AmeriHealth Caritas Immunization API
  slug: amerihealth-caritas-immunization-api
- description: The InsurancePlan FHIR resource type
  name: AmeriHealth Caritas InsurancePlan API
  slug: amerihealth-caritas-insuranceplan-api
- description: The List FHIR resource type
  name: AmeriHealth Caritas List API
  slug: amerihealth-caritas-list-api
- description: The Location FHIR resource type
  name: AmeriHealth Caritas Location API
  slug: amerihealth-caritas-location-api
- description: The Medication FHIR resource type
  name: AmeriHealth Caritas Medication API
  slug: amerihealth-caritas-medication-api
- description: The MedicationDispense FHIR resource type
  name: AmeriHealth Caritas MedicationDispense API
  slug: amerihealth-caritas-medicationdispense-api
- description: The MedicationKnowledge FHIR resource type
  name: AmeriHealth Caritas MedicationKnowledge API
  slug: amerihealth-caritas-medicationknowledge-api
- description: The MedicationRequest FHIR resource type
  name: AmeriHealth Caritas MedicationRequest API
  slug: amerihealth-caritas-medicationrequest-api
- description: The Observation FHIR resource type
  name: AmeriHealth Caritas Observation API
  slug: amerihealth-caritas-observation-api
- description: The Organization FHIR resource type
  name: AmeriHealth Caritas Organization API
  slug: amerihealth-caritas-organization-api
- description: The OrganizationAffiliation FHIR resource type
  name: AmeriHealth Caritas OrganizationAffiliation API
  slug: amerihealth-caritas-organizationaffiliation-api
- description: The Patient FHIR resource type
  name: AmeriHealth Caritas Patient API
  slug: amerihealth-caritas-patient-api
- description: The Practitioner FHIR resource type
  name: AmeriHealth Caritas Practitioner API
  slug: amerihealth-caritas-practitioner-api
- description: The PractitionerRole FHIR resource type
  name: AmeriHealth Caritas PractitionerRole API
  slug: amerihealth-caritas-practitionerrole-api
- description: The Procedure FHIR resource type
  name: AmeriHealth Caritas Procedure API
  slug: amerihealth-caritas-procedure-api
- description: Server-level operations
  name: AmeriHealth Caritas System Level Operations API
  slug: amerihealth-caritas-system-level-operations-api
artifact_total: 78
collections:
- collection_type: open
  name: AmeriHealth Caritas
  slug: open-amerihealth-caritas-patient-access
- collection_type: open
  name: AmeriHealth Caritas
  slug: open-amerihealth-caritas-provider-directory
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/amerihealth-caritas-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/amerihealth-caritas-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/amerihealth-caritas-authentication.yml
- group: start
  title: ''
  type: Portal
  url: https://developer.amerihealthcaritas.com/
- group: company
  title: ''
  type: Website
  url: https://www.amerihealthcaritas.com
- group: docs
  title: ''
  type: Documentation
  url: https://developer.amerihealthcaritas.com/dvp/v1/apiadditionaldocsinfo/
- group: start
  title: ''
  type: GettingStarted
  url: https://developer.amerihealthcaritas.com/dvp/v1/apiadditionaldocsinfo/
- group: auth
  title: ''
  type: Authentication
  url: https://developer.amerihealthcaritas.com/dvp/v1/apiadditionaldocsinfo/
- group: other
  title: ''
  type: CMSFinalRule
  url: https://www.cms.gov/priorities/key-initiatives/burden-reduction/interoperability
- group: other
  title: ''
  type: CARINBlueButton
  url: https://hl7.org/fhir/us/carin-bb/history.html
- group: other
  title: ''
  type: DaVinciPDex
  url: https://hl7.org/fhir/us/davinci-pdex/history.html
- group: other
  title: ''
  type: USCDI
  url: https://www.healthit.gov/isp/united-states-core-data-interoperability-uscdi#uscdi-v1
- group: other
  title: ''
  type: SMARTAppLaunch
  url: https://hl7.org/fhir/smart-app-launch/1.0.0/
- group: commercial
  title: ''
  type: HealthPlanFinder
  url: https://www.amerihealthcaritas.com/find-a-health-plan
- group: operate
  title: ''
  type: ContactUs
  url: https://www.amerihealthcaritas.com/contact-us
- group: company
  title: ''
  type: Careers
  url: https://careers.amerihealthcaritas.com/us/en
- group: company
  title: ''
  type: NewsBlog
  url: https://www.amerihealthcaritas.com/newsroom
- group: other
  title: ''
  type: TransparencyInCoverage
  url: https://www.amerihealthcaritas.com/about-us/transparency-in-coverage.aspx
- group: build
  title: ''
  type: GitHub
  url: https://github.com/amerihealth
- group: commercial
  title: ''
  type: Plans
  url: plans/amerihealth-caritas-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/amerihealth-caritas-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/amerihealth-caritas-finops.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/amerihealth-caritas-vocabulary.yml
- group: design
  title: ''
  type: JSONLDContext
  url: json-ld/amerihealth-caritas-context.jsonld
- group: agent
  title: ''
  type: LlmsText
  url: https://developer.amerihealthcaritas.com/llms.txt
created: '2024-01-01'
description: AmeriHealth Caritas is one of the largest Medicaid managed care organizations in the United States, serving roughly five million members across Medicaid, Children's Health Insurance Program (CHIP), dual-eligible Medicare-Medicaid (D-SNP), Medicare-Medicaid LTSS, and Marketplace lines of business across thirteen states plus the District of Columbia. The company is owned jointly by Independence Blue Cross (majority) and Blue Cross Blue Shield of Michigan, operates state health plans under brands such as Keystone First, Select Health of South Carolina, Blue Cross Complete of Michigan, AmeriHealth Caritas Next, AmeriHealth Caritas VIP Care, and PerformCare, and exposes a set of HL7 FHIR R4 APIs through its developer portal at developer.amerihealthcaritas.com to satisfy the CMS Interoperability and Patient Access final rule (CMS-9115-F).
examples:
- key_count: 5
  name: Amerihealth Caritas Coverage Search Example
  slug: amerihealth-caritas-coverage-search-example
- key_count: 5
  name: Amerihealth Caritas Explanation Of Benefit Search Example
  slug: amerihealth-caritas-explanation-of-benefit-search-example
- key_count: 5
  name: Amerihealth Caritas Medication Knowledge Search Example
  slug: amerihealth-caritas-medication-knowledge-search-example
- key_count: 5
  name: Amerihealth Caritas Organization Search Example
  slug: amerihealth-caritas-organization-search-example
- key_count: 11
  name: Amerihealth Caritas Patient Read Example
  slug: amerihealth-caritas-patient-read-example
- key_count: 5
  name: Amerihealth Caritas Practitioner Search Example
  slug: amerihealth-caritas-practitioner-search-example
features:
- description: SMART on FHIR / OAuth 2.0 secured member access to AllergyIntolerance, Claim, Condition, Coverage, Encounter, ExplanationOfBenefit, HealthcareService, Immunization, InsurancePlan, List, Location, Medication, MedicationDispense, MedicationKnowledge, MedicationRequest, Observation, Organization, OrganizationAffiliation, Patient, Practitioner, PractitionerRole, and Procedure FHIR R4 resources across the AmeriHealth Caritas family of plans.
  name: HL7 FHIR R4 Patient Access API
- description: Public, unauthenticated FHIR Provider Directory exposing Practitioner, PractitionerRole, Organization, OrganizationAffiliation, Location, and InsurancePlan resources for member, broker, and care-management consumers.
  name: HL7 FHIR R4 Provider Directory API
- description: CMS-mandated public Drug Formulary surface for AmeriHealth Caritas managed Medicaid and dual-eligible plans, exposed via FHIR MedicationKnowledge and List resources.
  name: HL7 FHIR R4 Drug Formulary API
- description: FHIR base URLs are routed per state plan using a four-digit plan code (for example 0100, 0500, 0900, 1200, 2100, 2400, 2600) on api-ext.amerihealthcaritas.com so each Medicaid / D-SNP / Marketplace plan is reachable independently while sharing one developer registration.
  name: Per-Plan FHIR Endpoint Routing
- description: Standard authorization code and PKCE authorization code flows backed by token, authorize, introspect, revoke, and session management endpoints under fhir.amerihealthcaritas.com.
  name: SMART App Launch 1.0.0 OAuth 2.0
- description: Implementation aligns with the CARIN Blue Button Implementation Guide and the Da Vinci Payer Data Exchange (PDex) IG referenced from the developer portal best-practices section.
  name: CARIN Blue Button & Da Vinci PDex Conformance
- description: Data elements published map to the United States Core Data for Interoperability (USCDI v1) to support clinical data exchange to consumer apps.
  name: USCDI Data Coverage
- description: Developers register, attest, and receive Client ID and Client Secret credentials from developer.amerihealthcaritas.com; once approved, sandbox patient credentials are issued for testing.
  name: Developer Portal Self-Service
finops:
- name: Amerihealth Caritas Finops
  service_category: Healthcare Interoperability
  slug: amerihealth-caritas-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/amerihealth-caritas.png
integrations:
- description: AmeriHealth Caritas is majority-owned by Independence Blue Cross (Philadelphia) and shares brand and operational relationships with the Independence family.
  name: Independence Blue Cross
- description: Blue Cross Blue Shield of Michigan is a co-owner of AmeriHealth Caritas and the joint sponsor of Blue Cross Complete of Michigan, the Michigan Medicaid managed care plan operated by AmeriHealth Caritas.
  name: Blue Cross Blue Shield of Michigan
- description: APIs exist to satisfy the CMS-9115-F Interoperability and Patient Access final rule for Medicaid managed care, CHIP, and D-SNP populations.
  name: CMS Interoperability Framework
- description: All three APIs implement HL7 FHIR 4.0.1 with SMART App Launch 1.0.0 security, CARIN Blue Button, and Da Vinci PDex guidance.
  name: HL7 FHIR R4
- description: Patient Access data set is profiled against USCDI v1 elements for clinical, encounter, medication, and care team data.
  name: USCDI v1
- description: Standard SMART App Launch authorization code flow and PKCE flow back the Patient Access security model.
  name: SMART on FHIR / OAuth 2.0 / OIDC / PKCE
- description: Each AmeriHealth Caritas state plan operates under contract with a state Medicaid agency (PA DHS, LA LDH, NC DHHS, OH ODM, FL AHCA, NH DHHS, MI MDHHS, DE DHSS, SC DHHS, NJ DHS).
  name: State Medicaid Agencies
json_schemas:
- name: AmeriHealthCaritasCoverage
  property_count: 20
  slug: amerihealth-caritas-coverage
- name: AmeriHealthCaritasExplanationOfBenefit
  property_count: 19
  slug: amerihealth-caritas-explanation-of-benefit
- name: AmeriHealthCaritasLocation
  property_count: 20
  slug: amerihealth-caritas-location
- name: AmeriHealthCaritasOrganization
  property_count: 13
  slug: amerihealth-caritas-organization
- name: AmeriHealthCaritasPatient
  property_count: 12
  slug: amerihealth-caritas-patient
- name: AmeriHealthCaritasPractitioner
  property_count: 12
  slug: amerihealth-caritas-practitioner
json_structures:
- name: Amerihealth Caritas Health Plan Structure
  property_count: 10
  slug: amerihealth-caritas-health-plan-structure
jsonld:
- class_count: 60
  name: Amerihealth Caritas Context
  property_count: 0
  slug: amerihealth-caritas-context
layout: provider
modified: '2026-05-23'
name: AmeriHealth Caritas
nav: Providers
network: true
overview: 'AmeriHealth Caritas publishes 23 APIs on the [APIs.io](https://apis.io/) network, including AllergyIntolerance API, Claim API, Condition API, and 20 more. Tagged areas include Healthcare, Health Insurance, Managed Care, Medicaid, and Medicare.


  The AmeriHealth Caritas catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  AmeriHealth Caritas'' developer surface includes authentication, developer portal, documentation, getting-started guide, GitHub presence, and 20 more developer resources.'
plans:
- name: Amerihealth Caritas Plans Pricing
  plan_count: 4
  slug: amerihealth-caritas-plans-pricing
random_paper: 19
rate_limits:
- limit_count: 6
  name: Amerihealth Caritas Rate Limits
  slug: amerihealth-caritas-rate-limits
rules:
- name: AmeriHealth Caritas API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: amerihealth-caritas-jsonschema-spectral-rules
- name: AmeriHealth Caritas API Rules
  rule_count: 0
  severity_counts:
    error: 0
    hint: 0
    info: 0
    warn: 0
  slug: amerihealth-caritas-rules
score:
  band: developing
  composite: 45.7
  delta: -6.0
  facets:
    commercial_clarity: 39.5
    contract_quality: 57.8
    developer_ergonomics: 39.1
    discoverability: 68.5
    governance: 68.8
    operational_transparency: 36.8
  previous_composite: 51.7
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 23
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 21.3
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: falling
screenshot: https://raw.githubusercontent.com/api-evangelist/amerihealth-caritas/refs/heads/main/screenshots/amerihealth-caritas-2026-06-20T171925.png
security:
- kind: authentication
  name: Amerihealth Caritas Authentication
  slug: amerihealth-caritas-authentication
  summary_line: openIdConnect · 1 scheme
- kind: domain-security
  name: Amerihealth Caritas Domain Security
  slug: amerihealth-caritas-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: amerihealth-caritas
solutions:
- description: Full-risk Medicaid managed care plans operated for state Medicaid agencies in PA, DE, DC, NC, NH, OH, LA, FL, MI, and SC under brands including AmeriHealth Caritas Pennsylvania, Keystone First, AmeriHealth Caritas DC, AmeriHealth Caritas Delaware, AmeriHealth Caritas Louisiana, AmeriHealth Caritas North Carolina, AmeriHealth Caritas New Hampshire, AmeriHealth Caritas Ohio, AmeriHealth Caritas Florida, First Choice by Select Health of South Carolina, and Blue Cross Complete of Michigan.
  name: Medicaid Managed Care
- description: AmeriHealth Caritas VIP Care, Keystone First VIP Choice, and First Choice VIP Care D-SNP plans serve members eligible for both Medicare and Medicaid across multiple states.
  name: Dual-Eligible Special Needs Plans (D-SNP)
- description: Community HealthChoices plans (AmeriHealth Caritas Pennsylvania Community HealthChoices, Keystone First Community HealthChoices) deliver LTSS-managed care to dual eligibles and individuals with long-term care needs.
  name: Long-Term Services and Supports (LTSS)
- description: Keystone First CHIP and other CHIP plans provide state-administered coverage for children in eligible families.
  name: Children's Health Insurance Program (CHIP)
- description: AmeriHealth Caritas Next and First Choice Next plans on state-based and federal Marketplaces in DE, FL, LA, NC, and SC.
  name: Individual & Family Marketplace
- description: PerformCare (Pennsylvania) and PerformCare New Jersey deliver behavioral health managed care and contracted services for state and county programs.
  name: Behavioral Health
- description: PerformRx, a wholly-owned pharmacy benefits manager, administers pharmacy benefits for AmeriHealth Caritas plans and external clients.
  name: Pharmacy Benefits Management
- description: AmeriHealth Administrators provides third-party administration services for self-funded employer health plans.
  name: Third-Party Administration
tags:
- Healthcare
- Health Insurance
- Managed Care
- Medicaid
- Medicare
- Dual Eligible
- CHIP
- LTSS
- Behavioral Health
- Pharmacy Benefits
- Interoperability
- FHIR
- CMS
- SMART On FHIR
- Patient Access
- Provider Directory
use_cases:
- description: Third-party consumer apps allow Medicaid, D-SNP, and Marketplace members to download and aggregate claims, encounters, medications, immunizations, and care plan data from AmeriHealth Caritas plans into one personal health record.
  name: Member Health Record Aggregation
- description: Care navigation apps, broker tools, and benefits portals query the public Provider Directory FHIR API to find AmeriHealth-Caritas-contracted Practitioners, PractitionerRoles, Organizations, and Locations by specialty, location, or network.
  name: Provider Directory Lookups
- description: Members and prescribers query the public Drug Formulary FHIR API to confirm whether a medication is covered, the tier, and any prior authorization requirements before filling.
  name: Drug Formulary Browsing
- description: D-SNP / dual-eligible care managers reconcile Medicare and Medicaid coverage, ExplanationOfBenefit, and Encounter data to coordinate Long-Term Services and Supports (LTSS) and behavioral health services.
  name: Care Coordination Across Dual-Eligible Plans
- description: When a member switches plans, the Patient Access surface can inform payer-to-payer exchange workflows aligned with Da Vinci PDex to migrate clinical history.
  name: Payer-To-Payer Data Sharing
- description: State Medicaid agencies and quality reporting partners consume aggregated, member-authorized FHIR data to support HEDIS, quality measure, and SDOH reporting.
  name: Population Health Reporting
website: https://www.amerihealthcaritas.com
---
