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
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: na
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: false
    idempotency: na
    mcp_server: false
    openapi_examples: documented
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 28.7
  scored_at: '2026-08-26'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Independence Blue Cross Agentic Access
  operation_count: 60
  slug: independence-blue-cross-agentic-access
  summary_line: 60 operations
api_count: 4
apis:
- description: 'Monthly machine-readable JSON files published under 45 CFR Part Â§147.211 / the Transparency in Coverage rule for three carrier brands operated by Independence Blue Cross: Keystone Health Plan East, Q'
  name: Independence Blue Cross Transparency In Coverage Data
  slug: transparency-in-coverage
- description: Public Da Vinci USDF FHIR R4 drug formulary resources.
  name: Independence Blue Cross Formulary API
  slug: independence-blue-cross-formulary-api
- description: FHIR R4 Patient Access resources for member-authorized access.
  name: Independence Blue Cross Patient Access API
  slug: independence-blue-cross-patient-access-api
- description: Public Da Vinci Plan-Net FHIR R4 provider directory resources.
  name: Independence Blue Cross Provider Directory API
  slug: independence-blue-cross-provider-directory-api
artifact_total: 70
collections:
- collection_type: postman
  name: Independence Blue Cross Drug FHIR Formulary API
  slug: postman-independence-blue-cross-formulary-api
- collection_type: postman
  name: Independence Blue Cross Drug FHIR Formulary Patient Access API
  slug: postman-independence-blue-cross-patient-access-api
- collection_type: postman
  name: Independence Blue Cross Drug FHIR Formulary Provider Directory API
  slug: postman-independence-blue-cross-provider-directory-api
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Independence Blue Cross Drug FHIR Formulary API
  slug: open-independence-blue-cross-formulary-api
- collection_type: open
  name: Independence Blue Cross Drug Formulary FHIR API
  slug: open-independence-blue-cross-formulary
- collection_type: open
  name: Independence Blue Cross Drug FHIR Formulary Patient Access API
  slug: open-independence-blue-cross-patient-access-api
- collection_type: open
  name: Independence Blue Cross Patient Access FHIR API
  slug: open-independence-blue-cross-patient
- collection_type: open
  name: Independence Blue Cross Drug FHIR Formulary Provider Directory API
  slug: open-independence-blue-cross-provider-directory-api
- collection_type: open
  name: Independence Blue Cross Provider Directory FHIR API
  slug: open-independence-blue-cross-provider
common:
- group: docs
  title: ''
  type: Swagger
  url: openapi/_original/independence-blue-cross-cms-swagger.json
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/independence-blue-cross-llms.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/independence-blue-cross-well-known.yml
- group: build
  title: ''
  type: Packages
  url: packages/independence-blue-cross-packages.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/independence-blue-cross-mcp.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/independence-blue-cross-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: https://www.ibx.com/privacy-policy/hipaa-compliance.html
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/independence-blue-cross-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/independence-blue-cross-lifecycle.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/independence-blue-cross-conventions.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/independence-blue-cross-data-model.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/independence-blue-cross-sandbox.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: start
  title: ''
  type: GettingStarted
  url: https://www.ibx.com/developer-resources/index.html
- group: operate
  title: ''
  type: Support
  url: https://www.ibx.com/contact-us/index.html
- group: build
  title: ''
  type: Examples
  url: examples/independence-blue-cross-patient-read-example.json
- group: build
  title: ''
  type: Examples
  url: examples/independence-blue-cross-coverage-search-example.json
- group: build
  title: ''
  type: Examples
  url: examples/independence-blue-cross-explanation-of-benefit-search-example.json
- group: build
  title: ''
  type: Examples
  url: examples/independence-blue-cross-practitioner-search-example.json
- group: build
  title: ''
  type: Examples
  url: examples/independence-blue-cross-organization-search-example.json
- group: build
  title: ''
  type: Examples
  url: examples/independence-blue-cross-medication-knowledge-search-example.json
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/independence-blue-cross/overview
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/independence-blue-cross-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/independence-blue-cross-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/independence-blue-cross-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/independence-blue-cross-scopes.yml
- group: start
  title: ''
  type: Portal
  url: https://devportal.ibx.com/
- group: company
  title: ''
  type: Website
  url: https://www.ibx.com
- group: docs
  title: ''
  type: Documentation
  url: https://devportal.ibx.com/documentation/
- group: docs
  title: ''
  type: Swagger
  url: https://www.ibx.com/scripts/custom/swagger/cmsSwagger.json
- group: auth
  title: ''
  type: Authentication
  url: https://eapics.ibx.com/patient/v1/fhir/.well-known/smart-configuration
- group: other
  title: ''
  type: Registration
  url: https://devportal.ibx.com/cmssignin/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.ibx.com/htdocs/custom/tnc/Developer%20Portal%20TandC.pdf
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.ibx.com/privacy-policy
- group: start
  title: ''
  type: Login
  url: https://www.ibx.com/login
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
- group: commercial
  title: ''
  type: DaVinciPlanNet
  url: http://hl7.org/fhir/us/davinci-pdex-plan-net/ImplementationGuide/hl7.fhir.us.davinci-pdex-plan-net
- group: other
  title: ''
  type: DaVinciUSDF
  url: http://hl7.org/fhir/us/davinci-drug-formulary/ImplementationGuide/hl7.fhir.us.davinci-drug-formulary
- group: other
  title: ''
  type: USCore
  url: https://hl7.org/fhir/us/core/STU3.1.1/
- group: other
  title: ''
  type: SMARTAppLaunch
  url: https://hl7.org/fhir/smart-app-launch/1.0.0/
- group: other
  title: ''
  type: Affiliates
  url: https://www.ibx.com/about-us/affiliates
- group: operate
  title: ''
  type: ContactUs
  url: mailto:AppOnboardingSupport@ibx.com
- group: operate
  title: ''
  type: ContactSupport
  url: https://www.ibx.com/contact-us
- group: company
  title: ''
  type: NewsBlog
  url: https://news.ibx.com/
- group: other
  title: ''
  type: TransparencyInCoverage
  url: https://www.ibx.com/resources/for-members/transparency-in-coverage.html
- group: company
  title: ''
  type: Facebook
  url: https://www.facebook.com/ibx
- group: company
  title: ''
  type: Twitter
  url: https://www.twitter.com/ibx
- group: learn
  title: ''
  type: YouTube
  url: https://www.youtube.com/ibxphilly
- group: company
  title: ''
  type: Instagram
  url: https://www.instagram.com/ibxfearless/
- group: other
  title: ''
  type: Pinterest
  url: https://pinterest.com/IBXBlueCross/
- group: other
  title: ''
  type: AntiFraud
  url: https://www.ibx.com/anti-fraud
- group: commercial
  title: ''
  type: Plans
  url: plans/independence-blue-cross-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/independence-blue-cross-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/independence-blue-cross-finops.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/independence-blue-cross-vocabulary.yml
- group: design
  title: ''
  type: JSONLDContext
  url: json-ld/independence-blue-cross-context.jsonld
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/independence-blue-cross-health-plan-structure.json
- group: company
  title: ''
  type: Blog
  url: https://news.ibx.com/feed/
created: '2024-01-01'
description: 'Independence Blue Cross (IBX) is the Blue Cross Blue Shield Association licensee for southeastern Pennsylvania (Bucks, Chester, Delaware, Montgomery, and Philadelphia counties) and a subsidiary of Independence Health Group, Inc., the parent holding company that consolidated IBX, AmeriHealth (commercial, including AmeriHealth New Jersey and the AmeriHealth Administrators TPA business), and the AmeriHealth Caritas family of Medicaid managed care plans in 2013. The company has called Philadelphia home for more than 85 years, serves nearly three million members directly, and — through Independence Health Group — supports roughly nine million covered lives across commercial, Medicare Advantage, Medicaid, CHIP, dental, vision, and behavioral health lines of business. Independence Health Group reported consolidated revenue of $36.3 billion for 2025. To satisfy the CMS Interoperability and Patient Access final rule (CMS-9115-F), IBX publishes three HL7 FHIR R4 (4.0.1) APIs from its
  `eapics.ibx.com` gateway and developer portal at `devportal.ibx.com`: a SMART-on-FHIR / OAuth 2.0 secured Patient Access API for Medicare Advantage and Keystone HMO CHIP members, a public Da Vinci PDex Plan-Net Provider Directory API, and a public Da Vinci US Drug Formulary (USDF) API. The provider also publishes monthly Transparency in Coverage machine-readable files (in-network rates, allowed amounts, prescription drugs) for three carrier brands — Keystone Health Plan East, QCC Insurance Company, and Independence Assurance Co, Inc.'
examples:
- key_count: 6
  name: Independence Blue Cross Coverage Search Example
  slug: independence-blue-cross-coverage-search-example
- key_count: 6
  name: Independence Blue Cross Explanation Of Benefit Search Example
  slug: independence-blue-cross-explanation-of-benefit-search-example
- key_count: 6
  name: Independence Blue Cross Medication Knowledge Search Example
  slug: independence-blue-cross-medication-knowledge-search-example
- key_count: 6
  name: Independence Blue Cross Organization Search Example
  slug: independence-blue-cross-organization-search-example
- key_count: 11
  name: Independence Blue Cross Patient Read Example
  slug: independence-blue-cross-patient-read-example
- key_count: 6
  name: Independence Blue Cross Practitioner Search Example
  slug: independence-blue-cross-practitioner-search-example
features:
- description: SMART on FHIR / OAuth 2.0 secured member access (Medicare Advantage and Keystone HMO CHIP populations) to AllergyIntolerance, CarePlan, Condition, Coverage, DiagnosticReport, Encounter, ExplanationOfBenefit, Goal, Immunization, Location, Medication, MedicationDispense, MedicationRequest, Observation, Organization, Patient, Practitioner, PractitionerRole, and Procedure FHIR R4 resources.
  name: HL7 FHIR R4 Patient Access API
- description: Public, unauthenticated Da Vinci PDex Plan-Net FHIR Provider Directory exposing Practitioner, PractitionerRole, Organization, OrganizationAffiliation, Location, HealthcareService, InsurancePlan, and Endpoint resources for the Independence Blue Cross network.
  name: HL7 FHIR R4 Provider Directory API
- description: Public Da Vinci USDF Drug Formulary surface exposing MedicationKnowledge and List resources for the Independence Blue Cross covered drug list.
  name: HL7 FHIR R4 Drug Formulary API
- description: SMART configuration advertises `client-public`, `sso-openid-connect`, `launch-standalone`, `client-confidential-symmetric`, `context-standalone-patient`, `permission-offline`, and `permission-patient` capabilities. Authorize at `member.ibx.com/patientaccesssvc/oauth2/v1/authorize`, exchange at `eapics.ibx.com/oauth2/v2/token`.
  name: SMART App Launch 1.0.0 OAuth 2.0 with PKCE
- description: Patient Access aligns with CARIN BB, CPCDS, US Core 3.1.1, and Da Vinci PDex. Provider Directory implements Da Vinci PDex Plan-Net. Drug Formulary implements Da Vinci USDF.
  name: CARIN Blue Button / Da Vinci / US Core Conformance
- description: devportal.ibx.com provides documentation, registration (`/cmssignin/`), sandbox services, and per-app credentials. App onboarding support is at AppOnboardingSupport@ibx.com.
  name: Developer Portal Self-Service
- description: Monthly published in-network rate, allowed amount, and prescription drug JSON files for Keystone Health Plan East, QCC Insurance Company, and Independence Assurance Co, Inc. at `www.ibx.com/cmstic/?brand={khpe|qcc|iac}`.
  name: Transparency In Coverage Machine-Readable Files
- description: Independence Blue Cross does not maintain a public api-evangelist-discoverable GitHub organization for its FHIR developer surface; SDKs, sample code, and documentation are distributed through the dev portal rather than open-source repositories.
  name: No Public GitHub Organization
finops:
- name: Independence Blue Cross Finops
  service_category: Healthcare Interoperability
  slug: independence-blue-cross-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/independence-blue-cross.png
integrations:
- description: Independence Blue Cross is a subsidiary of Independence Health Group, Inc., the 2013 holding company that also owns AmeriHealth (commercial) and majority-owns AmeriHealth Caritas (Medicaid managed care).
  name: Independence Health Group
- description: Majority-owned (61.3%) by Independence with Blue Cross Blue Shield of Michigan as a 38.7% co-owner; runs Medicaid managed care, CHIP, D-SNP, LTSS, and Marketplace plans across thirteen states plus DC.
  name: AmeriHealth Caritas
- description: Independence operates AmeriHealth Insurance Company of New Jersey, a commercial payer serving roughly 209,000 New Jersey members.
  name: AmeriHealth New Jersey
- description: National third-party administrator (TPA) serving self-funded health plans, carriers, and administrators with business process outsourcing.
  name: AmeriHealth Administrators
- description: Independence-affiliated value-based primary care enablement company supporting coordinated, proactive care for primary care physicians.
  name: Tandigm Health
- description: Independence Blue Cross is an independent licensee of the Blue Cross Blue Shield Association serving Bucks, Chester, Delaware, Montgomery, and Philadelphia counties in PA.
  name: Blue Cross Blue Shield Association
- description: APIs exist to satisfy the CMS-9115-F Interoperability and Patient Access final rule for Medicare Advantage and Children's Health Insurance Program (CHIP) populations.
  name: CMS Interoperability Framework
- description: All three APIs implement HL7 FHIR 4.0.1 with SMART App Launch 1.0.0 security, CARIN BB, Da Vinci PDex / Plan-Net, and Da Vinci USDF guidance.
  name: HL7 FHIR R4
- description: Standard SMART App Launch authorization code flow and PKCE flow back the Patient Access security model. SMART configuration is published at the well-known endpoint on eapics.ibx.com.
  name: SMART on FHIR / OAuth 2.0 / OIDC / PKCE
- description: Underwriting carriers include Keystone Health Plan East, QCC Insurance Company, Independence Assurance Co, Inc., and Keystone Health Plan East HMO products. Each publishes its own Transparency in Coverage machine-readable files.
  name: Carrier Brands
json_schemas:
- name: IBX Coverage (CARIN BB subset)
  property_count: 13
  slug: independence-blue-cross-coverage
- name: IBX ExplanationOfBenefit (CARIN BB subset)
  property_count: 16
  slug: independence-blue-cross-explanation-of-benefit
- name: IBX Location (Da Vinci Plan-Net subset)
  property_count: 13
  slug: independence-blue-cross-location
- name: IBX Organization (Da Vinci Plan-Net subset)
  property_count: 12
  slug: independence-blue-cross-organization
- name: IBX Patient (US Core 3.1.1 subset)
  property_count: 10
  slug: independence-blue-cross-patient
- name: IBX Practitioner (Da Vinci Plan-Net subset)
  property_count: 9
  slug: independence-blue-cross-practitioner
json_structures:
- name: Independence Blue Cross Health Plan Structure
  property_count: 7
  slug: independence-blue-cross-health-plan-structure
jsonld:
- class_count: 23
  name: Independence Blue Cross Context
  property_count: 12
  slug: independence-blue-cross-context
layout: provider
mcp_servers:
- description: ''
  name: Independence Blue Cross MCP Server
  slug: independence-blue-cross-mcp-server
modified: '2026-08-15'
name: Independence Blue Cross
nav: Providers
network: true
overview: 'Independence Blue Cross publishes 3 APIs on the [APIs.io](https://apis.io/) network: Formulary API, Patient Access API, and Provider Directory API. Tagged areas include Healthcare, Health Insurance, Blue Cross Blue Shield, Managed Care, and Medicare.


  The Independence Blue Cross catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Independence Blue Cross'' developer surface includes sandbox, getting-started guide, support, code examples, authentication, developer portal, documentation, and 53 more developer resources.'
plans:
- name: Independence Blue Cross Plans Pricing
  plan_count: 5
  slug: independence-blue-cross-plans-pricing
random_paper: 8
rate_limits:
- limit_count: 5
  name: Independence Blue Cross Rate Limits
  slug: independence-blue-cross-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: Independence Blue Cross API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: independence-blue-cross-jsonschema-spectral-rules
- effective_rule_count: 0
  extends: []
  name: Independence Blue Cross API Rules
  rule_count: 0
  severity_counts:
    error: 0
    hint: 0
    info: 0
    warn: 0
  slug: independence-blue-cross-rules
scopes:
- name: Independence Blue Cross Scopes
  scope_count: 4
  slug: independence-blue-cross-scopes
  summary_line: 4 scopes · authorizationCode
score:
  band: exemplar
  composite: 70.9
  delta: 0.0
  facets:
    access_clarity: 75.0
    commercial_clarity: 75.0
    contract_governance: 55.3
    contract_quality: 64.6
    developer_ergonomics: 61.3
    discoverability: 81.5
    governance: 55.3
    operational_transparency: 31.6
  previous_composite: 70.9
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 3
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 76.3
  schema_version: 0.15.0
  scored_at: '2026-08-26'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/independence-blue-cross/refs/heads/main/screenshots/independence-blue-cross-2026-06-20T183313.png
security:
- kind: authentication
  name: Independence Blue Cross Authentication
  slug: independence-blue-cross-authentication
  summary_line: oauth2 · 2 schemes
- kind: domain-security
  name: Independence Blue Cross Domain Security
  slug: independence-blue-cross-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: independence-blue-cross
solutions:
- description: Group commercial coverage for individuals, families, small and mid-sized businesses, large employers, municipalities, unions, and education boards in southeastern Pennsylvania.
  name: Commercial Health Plans
- description: Keystone 65 HMO, Personal Choice 65 PPO, and related Medicare Advantage products including PA and re-entered NJ MA markets in 2024. Patient Access FHIR API is required for this population under CMS-9115-F.
  name: Medicare Advantage
- description: Keystone HMO CHIP covers eligible children in southeastern Pennsylvania under the Pennsylvania CHIP program; CHIP members are in scope for the Patient Access API.
  name: Children's Health Insurance Program (CHIP)
- description: Medicaid managed care delivered through the AmeriHealth Caritas subsidiary family (Keystone First, AmeriHealth Caritas Pennsylvania, AmeriHealth Caritas DC, AmeriHealth Caritas Delaware, AmeriHealth Caritas Louisiana, AmeriHealth Caritas North Carolina, AmeriHealth Caritas New Hampshire, AmeriHealth Caritas Ohio, AmeriHealth Caritas Florida, First Choice by Select Health of South Carolina, and Blue Cross Complete of Michigan).
  name: Medicaid (Through AmeriHealth Caritas)
- description: IBX Dental coverage offered through Keystone and United Concordia networks for commercial, Medicare, and individual buyers.
  name: Dental
- description: Vision coverage and provider network delivered through partner vision networks for commercial and Medicare buyers.
  name: Vision
- description: Behavioral health benefits embedded in commercial, Medicare Advantage, and Medicaid lines; PerformCare (operated by AmeriHealth Caritas) supports PA behavioral health.
  name: Behavioral Health
- description: Pharmacy benefits administration including the covered drug list (formulary) surfaced via the Drug Formulary FHIR API.
  name: Pharmacy Benefits
tags:
- Healthcare
- Health Insurance
- Blue Cross Blue Shield
- Managed Care
- Medicare
- Medicare Advantage
- Medicaid
- CHIP
- Commercial
- Dental
- Vision
- Behavioral Health
- Pharmacy Benefits
- Interoperability
- FHIR
- SMART on FHIR
- CMS
- Patient Access
- Provider Directory
- Drug Formulary
- Transparency In Coverage
use_cases:
- description: Consumer health apps allow Independence Medicare Advantage and Keystone HMO CHIP members to consent to share their clinical, claims, encounter, medication, and immunization history with third-party personal health record (PHR) apps.
  name: Member Health Record Aggregation
- description: Member-facing tools, broker apps, and care navigation tools query the public Da Vinci Plan-Net Provider Directory FHIR API to find in-network Practitioners, PractitionerRoles, Organizations, and Locations across southeastern PA.
  name: Provider Directory Lookups
- description: Members, prescribers, and pharmacy apps query the public USDF Drug Formulary FHIR API to confirm whether a medication is covered, the tier, and any prior authorization requirements before filling.
  name: Drug Formulary Browsing
- description: When a member switches plans, the Patient Access surface can inform payer-to-payer exchange workflows aligned with Da Vinci PDex to migrate clinical history.
  name: Payer-To-Payer Data Sharing
- description: Researchers, employers, and consumer cost-transparency tools ingest the monthly Transparency in Coverage machine-readable files for Keystone Health Plan East, QCC, and IAC to compare in-network rates and allowed amounts.
  name: Price Comparison & Cost Transparency
- description: Population health partners ingest member-authorized FHIR data to support HEDIS measure capture, risk adjustment, care-gap closure, and SDOH reporting.
  name: Clinical & Quality Reporting
website: https://www.ibx.com
---
