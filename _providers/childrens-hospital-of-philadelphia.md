---
access_model:
  confidence: medium
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - authentication
  trial: false
  try_now: false
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
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 27.5
  scored_at: '2026-08-10'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Childrens Hospital Of Philadelphia Agentic Access
  operation_count: 22
  slug: childrens-hospital-of-philadelphia-agentic-access
  summary_line: 22 operations
api_count: 8
apis:
- description: MyChart-based patient portal that gives patients, parents and guardians access to virtual medical records, lab results, secure messaging, telehealth visits, medication refills, and appointment schedul
  name: MyCHOP Patient Portal
  slug: mychop-patient-portal
- description: Internet-based portal for referring physician offices that provides real-time, read-only access to the CHOP Epic EMR. Surfaces discharge notes, operative reports, progress notes, consult reports, labs
  name: Link2CHOP Referring Physician Portal
  slug: link2chop-referring-physician-portal
- description: The Center for Data Driven Discovery in Biomedicine (D3b) at CHOP operates the open research data infrastructure for pediatric cancer and rare disease. Programs include RADIANT (Real-time Analysis and
  name: D3b Data Sharing Platforms
  slug: d3b-data-sharing-platforms
- description: CHOP's Department of Biomedical and Health Informatics (DBHi) maintains 168 public repositories covering health data infrastructure, EHR integration, and SMART on FHIR tools. Notable open-source proje
  name: DBHi Biomedical and Health Informatics
  slug: dbhi-biomedical-and-health-informatics
- description: HL7 FHIR Bulk Data Access (Flat FHIR) Group-level export.
  name: Children's Hospital of Philadelphia Bulk Data API
  slug: childrens-hospital-of-philadelphia-bulk-data-api
- description: Patient-mediated clinical and claims data resources required under CMS-9115-F.
  name: Children's Hospital of Philadelphia Patient Access API
  slug: childrens-hospital-of-philadelphia-patient-access-api
- description: Public provider, organization, location, and endpoint resources required under CMS-9115-F.
  name: Children's Hospital of Philadelphia Provider Directory API
  slug: childrens-hospital-of-philadelphia-provider-directory-api
- description: SMART on FHIR launch and discovery endpoints.
  name: Children's Hospital of Philadelphia SMART API
  slug: childrens-hospital-of-philadelphia-smart-api
artifact_total: 47
collections:
- collection_type: open
  name: Children's Hospital of Philadelphia FHIR R4 API
  slug: open-chop-fhir-r4
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/childrens-hospital-of-philadelphia-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/childrens-hospital-of-philadelphia-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/childrens-hospital-of-philadelphia-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/childrens-hospital-of-philadelphia-scopes.yml
- group: start
  title: ''
  type: Portal
  url: https://www.chop.edu
- group: start
  title: ''
  type: DeveloperPortal
  url: https://fhir.epic.com
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/chop-dbhi
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/d3b-center
- group: company
  title: ''
  type: Blog
  url: https://www.chop.edu/news
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.chop.edu/pages/privacy-policy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.chop.edu/pages/terms-and-conditions
- group: auth
  title: ''
  type: Compliance
  url: https://www.chop.edu/health-resources/cms-interoperability-and-patient-access
- group: operate
  title: ''
  type: Support
  url: https://www.chop.edu/contact-us
- group: design
  title: ''
  type: SpectralRules
  url: rules/chop-fhir-rules.yml
- group: design
  title: ''
  type: JSONLD
  url: json-ld/childrens-hospital-of-philadelphia-context.jsonld
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/childrens-hospital-of-philadelphia-vocabulary.yml
created: '2026-05-23'
description: Founded in 1855 as the first hospital in the United States dedicated to the healthcare of children, Children's Hospital of Philadelphia (CHOP) is a 692-bed flagship pediatric academic medical center affiliated with the University of Pennsylvania Perelman School of Medicine. CHOP records roughly 1.63 million outpatient visits and 34,829 admissions per year and operates one of the largest pediatric research enterprises in the world through its Research Institute and the Center for Data Driven Discovery in Biomedicine (D3b). From an API perspective, CHOP runs a production Epic-backed HL7 FHIR R4 endpoint at `https://epicnsproxy.chop.edu/fhir/api/FHIR/R4` exposing CMS-9115-F Patient Access and Provider Directory resources, US Core 6.1.0, SMART on FHIR, and HL7 Bulk Data. CHOP additionally publishes 320+ public repositories across the `chop-dbhi` (Department of Biomedical and Health Informatics) and `d3b-center` GitHub organizations, plus shared research data platforms including
  RADIANT, CAVATICA, PedcBioPortal, the Children's Brain Tumor Network, and the Kids First Data Resource Center.
examples:
- key_count: 5
  name: Chop Fhir Bulk Export Example
  slug: chop-fhir-bulk-export-example
- key_count: 9
  name: Chop Fhir Observation Example
  slug: chop-fhir-observation-example
- key_count: 10
  name: Chop Fhir Organization Example
  slug: chop-fhir-organization-example
- key_count: 11
  name: Chop Fhir Patient Example
  slug: chop-fhir-patient-example
- key_count: 8
  name: Chop Fhir Practitioner Example
  slug: chop-fhir-practitioner-example
features:
- description: HL7 FHIR R4 server with US Core 6.1.0 conformance and SMART on FHIR authorization, fulfilling CMS-9115-F Patient Access requirements.
  name: CMS-Compliant Patient Access FHIR API
- description: Unauthenticated FHIR resources for Practitioner, PractitionerRole, Organization, Location, and Endpoint.
  name: Public Provider Directory
- description: Group-level $export per the HL7 Bulk Data IG; supports backend services (client_credentials) authentication.
  name: HL7 Bulk Data Access
- description: Capability statement advertises 59 resource types covering clinical, administrative, and financial data, including AllergyIntolerance, Condition, Observation, MedicationRequest, Immunization, Procedure, Encounter, DiagnosticReport, DocumentReference, Coverage, ExplanationOfBenefit, and Claim.
  name: 59 FHIR Resource Types
- description: 168 public DBHi repositories and 153 public D3b repositories spanning ETL, anonymization, biorepository analytics, and SMART apps.
  name: Open-Source Health Informatics Tools
image: https://www.chop.edu/themes/custom/chop/logo.svg
integrations:
- description: CHOP's underlying EHR; the FHIR endpoint is served by Epic November 2025.
  name: Epic EHR
- description: Third-party app developers register apps at fhir.epic.com and target CHOP (Organization ID 332).
  name: Epic on FHIR
- description: SMART on FHIR launch protocols for EHR-integrated and standalone apps.
  name: SMART App Launch
- description: Backend-services authentication and Group-level export.
  name: HL7 FHIR Bulk Data IG
- description: CapabilityStatement instantiates us-core-server profile.
  name: HL7 US Core 6.1.0
- description: Funding partner for the RADIANT pediatric data-sharing platform.
  name: ARPA-H
- description: Funds the Gabriella Miller Kids First Data Resource Center, coordinated by D3b.
  name: NIH Common Fund
- description: Academic affiliate (Perelman School of Medicine).
  name: University of Pennsylvania
json_schemas:
- name: CHOP FHIR Observation
  property_count: 9
  slug: chop-fhir-observation
- name: CHOP FHIR Organization
  property_count: 9
  slug: chop-fhir-organization
- name: CHOP FHIR Patient
  property_count: 10
  slug: chop-fhir-patient
- name: CHOP FHIR Practitioner
  property_count: 7
  slug: chop-fhir-practitioner
jsonld:
- class_count: 22
  name: Childrens Hospital Of Philadelphia Context
  property_count: 0
  slug: childrens-hospital-of-philadelphia-context
layout: provider
modified: '2026-05-23'
name: Children's Hospital of Philadelphia
nav: Providers
network: true
overview: 'Children''s Hospital of Philadelphia publishes 4 APIs on the [APIs.io](https://apis.io/) network, including Bulk Data API, Patient Access API, Provider Directory API, and 1 more. Tagged areas include Healthcare, Pediatrics, FHIR, SMART On FHIR, and Patient Access.


  The Children''s Hospital of Philadelphia catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Children''s Hospital of Philadelphia''s developer surface includes authentication, developer portal, engineering blog, support, and 12 more developer resources.'
random_paper: 61
rules:
- name: Children's Hospital of Philadelphia API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: childrens-hospital-of-philadelphia-jsonschema-spectral-rules
- name: Children's Hospital of Philadelphia API Rules
  rule_count: 4
  severity_counts:
    error: 2
    hint: 0
    info: 0
    warn: 2
  slug: chop-fhir-rules
scopes:
- name: Childrens Hospital Of Philadelphia Scopes
  scope_count: 6
  slug: childrens-hospital-of-philadelphia-scopes
  summary_line: 6 scopes · authorizationCode/clientCredentials
score:
  band: developing
  composite: 46.9
  delta: 0.0
  facets:
    commercial_clarity: 28.9
    contract_quality: 73.6
    developer_ergonomics: 26.1
    discoverability: 64.8
    governance: 68.8
    operational_transparency: 5.3
  previous_composite: 46.9
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
    score: 58.8
  schema_version: 0.9.1
  scored_at: '2026-08-10'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/childrens-hospital-of-philadelphia/refs/heads/main/screenshots/childrens-hospital-of-philadelphia-2026-06-20T174310.png
security:
- kind: authentication
  name: Childrens Hospital Of Philadelphia Authentication
  slug: childrens-hospital-of-philadelphia-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Childrens Hospital Of Philadelphia Domain Security
  slug: childrens-hospital-of-philadelphia-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: childrens-hospital-of-philadelphia
solutions:
- description: CMS-mandated patient-mediated data access surface.
  name: Patient Access
- description: CMS-mandated public provider directory surface.
  name: Provider Directory
- description: Population-scale data extraction for approved partners.
  name: Bulk Data Analytics
- description: D3b platforms for pediatric cancer and rare-disease research collaboration.
  name: Open Research Data
tags:
- Healthcare
- Pediatrics
- FHIR
- SMART On FHIR
- Patient Access
- Provider Directory
- CMS Interoperability
- US Core
- Bulk Data
- Research Data
- Open Data
use_cases:
- description: Parents and guardians download their child's full clinical and claims history into third-party PHR apps via SMART on FHIR.
  name: Patient-Mediated Data Download
- description: Approved EHR-launched and standalone SMART apps surface CHOP data inside referring-provider and care-coordination tools.
  name: Care-Coordination Apps
- description: Approved system-level clients run Group-level $export to extract de-identified cohorts for research and quality measurement.
  name: Population Analytics
- description: D3b platforms (RADIANT, CAVATICA, PedcBioPortal, CBTN) enable multi-site sharing of pediatric oncology and rare-disease data.
  name: Pediatric Cancer Research Collaboration
- description: Link2CHOP gives credentialed referring physicians live access to discharge notes, labs, imaging, medications, and diagnoses for shared patients.
  name: Referring Provider Read-Only EMR Access
website: https://fhir.epic.com
---
