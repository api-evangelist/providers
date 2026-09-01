---
access_model:
  confidence: medium
  label: Enterprise · Partner onboarding (API onboarding form + app registration)
  onboarding: unknown
  pricing: enterprise
  public: false
  source:
  - authentication
  - documentation
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: documented
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
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
  score: 29.7
  scored_at: '2026-09-01'
agentic_access:
- acting_count: 4
  human_in_the_loop: 0
  name: Nextgen Healthcare Agentic Access
  operation_count: 54
  slug: nextgen-healthcare-agentic-access
  summary_line: 54 operations · 4 acting
api_count: 2
apis:
- description: HL7 FHIR API for the NextGen Enterprise EHR, certified under the 21st Century Cures Act Patient Access criteria, exposing USCDI data to patient-facing apps. Available in FHIR R4 (4.0.1) and legacy DST
  name: NextGen Enterprise Patient Access FHIR API
  slug: nextgen-enterprise-patient-access-fhir-api
- description: 'An extensive collection of JSON-based RESTful APIs (800+ routes) that power apps used by provider organizations on the NextGen Enterprise platform (v5.9.0+), covering clinical and practice-management '
  name: NextGen Enterprise API
  slug: nextgen-enterprise-api
- description: HL7 FHIR STU3 (R3) API for the NextGen Office EHR with C-CDA support, authenticated with SMART App Launch / OpenID Connect OAuth2 via Keycloak. Predecessor surface to the R4 Patient Access API.
  name: NextGen Office FHIR R3 API
  slug: nextgen-office-fhir-r3-api
- description: FHIR R4-based Patient Access API for NextGen Office (formerly MediTouch) ambulatory practices. Enables patients and authorized apps to access personal health information via the YourHealthFile patient
  name: NextGen Office Patient FHIR API
  slug: nextgen-office-patient-fhir-api
- description: SMART on FHIR App Launch API for NextGen Office enabling vendor applications to obtain USCDIv1 clinical data for a single patient. Compliant with 21st Century Cures Act requirements. Supports HL7 SMAR
  name: NextGen Office SMART App Launch FHIR API
  slug: nextgen-office-smart-app-launch-fhir-api
- description: Bulk FHIR API for NextGen Office enabling authorized vendors to obtain USCDIv1 data for multiple patients in a group using the HL7 FHIR Bulk Data Access specification. Compliant with 21st Century Cure
  name: NextGen Office Bulk FHIR API
  slug: nextgen-office-bulk-fhir-api
- description: 'API for NextGen Mirth Connect, an open-source healthcare integration engine supporting HL7 v2, FHIR, and other healthcare data standards for interoperability between clinical systems. Enables message '
  name: NextGen Mirth Connect Integration Engine API
  slug: nextgen-mirth-connect-integration-engine-api
- description: https://hl7.org/fhir/R4/allergyintolerance.html
  name: NextGen Healthcare Allergy Intolerance API
  slug: nextgen-healthcare-allergyintolerance-api
- description: https://hl7.org/fhir/R4/careplan.html
  name: NextGen Healthcare Care Plan API
  slug: nextgen-healthcare-careplan-api
- description: https://hl7.org/fhir/R4/careteam.html
  name: NextGen Healthcare Care Team API
  slug: nextgen-healthcare-careteam-api
- description: The CCDA API from NextGen Healthcare — 1 operation(s) for ccda.
  name: NextGen Healthcare CCDA API
  slug: nextgen-healthcare-ccda-api
- description: https://hl7.org/fhir/R4/condition.html
  name: NextGen Healthcare Condition API
  slug: nextgen-healthcare-condition-api
- description: https://hl7.org/fhir/R4/coverage.html
  name: NextGen Healthcare Coverage API
  slug: nextgen-healthcare-coverage-api
- description: https://hl7.org/fhir/R4/device.html
  name: NextGen Healthcare Device API
  slug: nextgen-healthcare-device-api
- description: https://hl7.org/fhir/R4/diagnosticreport.html
  name: NextGen Healthcare Diagnostic Report API
  slug: nextgen-healthcare-diagnosticreport-api
- description: https://hl7.org/fhir/R4/documentreference.html
  name: NextGen Healthcare Document Reference API
  slug: nextgen-healthcare-documentreference-api
- description: https://hl7.org/fhir/R4/encounter.html
  name: NextGen Healthcare Encounter API
  slug: nextgen-healthcare-encounter-api
- description: The Export APIs API from NextGen Healthcare — 2 operation(s) for export apis.
  name: NextGen Healthcare Export APIs API
  slug: nextgen-healthcare-export-apis-api
- description: https://hl7.org/fhir/R4/goal.html
  name: NextGen Healthcare Goal API
  slug: nextgen-healthcare-goal-api
- description: The Group APIs API from NextGen Healthcare — 2 operation(s) for group apis.
  name: NextGen Healthcare Group APIs API
  slug: nextgen-healthcare-group-apis-api
- description: https://hl7.org/fhir/R4/immunization.html
  name: NextGen Healthcare Immunization API
  slug: nextgen-healthcare-immunization-api
- description: https://hl7.org/fhir/R4/location.html
  name: NextGen Healthcare Location API
  slug: nextgen-healthcare-location-api
- description: https://hl7.org/fhir/R4/medicationadministration.html
  name: NextGen Healthcare Medication Administration API
  slug: nextgen-healthcare-medicationadministration-api
- description: The MedicationDispense API from NextGen Healthcare — 2 operation(s) for medicationdispense.
  name: NextGen Healthcare Medication Dispense API
  slug: nextgen-healthcare-medicationdispense-api
- description: https://hl7.org/fhir/R4/medicationrequest.html
  name: NextGen Healthcare Medication Request API
  slug: nextgen-healthcare-medicationrequest-api
- description: https://hl7.org/fhir/R4/observation.html
  name: NextGen Healthcare Observation API
  slug: nextgen-healthcare-observation-api
- description: https://hl7.org/fhir/R4/organization.html
  name: NextGen Healthcare Organization API
  slug: nextgen-healthcare-organization-api
- description: https://hl7.org/fhir/R4/patient.html
  name: NextGen Healthcare Patient API
  slug: nextgen-healthcare-patient-api
- description: The Patient Search API from NextGen Healthcare — 1 operation(s) for patient search.
  name: NextGen Healthcare Patient Search API
  slug: nextgen-healthcare-patient-search-api
- description: https://hl7.org/fhir/R4/practitioner.html
  name: NextGen Healthcare Practitioner API
  slug: nextgen-healthcare-practitioner-api
- description: https://hl7.org/fhir/R4/practitionerrole.html
  name: NextGen Healthcare Practitioner Role API
  slug: nextgen-healthcare-practitionerrole-api
- description: https://hl7.org/fhir/R4/procedure.html
  name: NextGen Healthcare Procedure API
  slug: nextgen-healthcare-procedure-api
- description: https://hl7.org/fhir/R4/provenance.html
  name: NextGen Healthcare Provenance API
  slug: nextgen-healthcare-provenance-api
- description: https://hl7.org/fhir/R4/relatedperson.html
  name: NextGen Healthcare Related Person API
  slug: nextgen-healthcare-relatedperson-api
- description: https://hl7.org/fhir/R4/specimen.html
  name: NextGen Healthcare Specimen API
  slug: nextgen-healthcare-specimen-api
artifact_total: 47
collections:
- collection_type: open
  name: API Collection
  slug: open-nextgen-healthcare-fhir-capability-statement
- collection_type: open
  name: NextGen Office BulK FHIR API
  slug: open-nextgen-office-bulk-fhir-r4
common:
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/nextgen-healthcare-capability-edges.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/nextgen-healthcare-domain-security.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/nextgen-healthcare-agentic-access.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/nextgen-healthcare-scopes.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/nextgen-healthcare-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://www.nextgen.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://www.nextgen.com/developer-program
- group: start
  title: ''
  type: Portal
  url: https://developer.nextgen.com/
- group: docs
  title: ''
  type: Documentation
  url: https://www.nextgen.com/api
- group: docs
  title: ''
  type: APIReference
  url: https://www.nextgen.com/api/regulatory-nge
- group: start
  title: ''
  type: GettingStarted
  url: https://www.nextgen.com/api-on-boarding
- group: other
  title: ''
  type: Marketplace
  url: https://www.nextgen.com/marketplace
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/NextGenHealthcare
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/nextgen-healthcare-information-systems
- group: company
  title: ''
  type: Blog
  url: https://www.nextgen.com/blog
- group: operate
  title: ''
  type: Support
  url: https://www.nextgen.com/contact-us
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.nextgen.com/legal/terms-and-conditions
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.nextgen.com/legal/privacy-policy
- group: auth
  title: ''
  type: TrustCenter
  url: https://www.nextgen.com/trust
- group: auth
  title: ''
  type: Compliance
  url: https://www.nextgen.com/trust
- group: design
  title: ''
  type: Conformance
  url: conformance/nextgen-healthcare-conformance.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/nextgen-healthcare-well-known.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/nextgen-healthcare-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/nextgen-healthcare-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/nextgen-healthcare-lifecycle.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/nextgen-healthcare-data-model.yml
- group: build
  title: ''
  type: Packages
  url: packages/nextgen-healthcare-packages.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/nextgen-healthcare-llms.txt
- group: agent
  title: ''
  type: MCPServer
  url: mcp/nextgen-healthcare-mcp.yml
- group: build
  title: ''
  type: ToolCrosswalk
  url: mcp/nextgen-healthcare-tool-crosswalk.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/nextgen-healthcare-office-fhir-r4-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/nextgen-healthcare-office-bulk-fhir-r4-overlay.yaml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://dev-cd.nextgen.com/api
- group: other
  title: ''
  type: DeveloperProgram
  url: https://www.nextgen.com/developer-program
- group: other
  title: ''
  type: Marketplace
  url: https://www.nextgen.com/solutions/marketplace
- group: build
  title: ''
  type: GitHub
  url: https://github.com/nextgenhealthcare
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/nextgenhealthcareinc
- group: other
  title: ''
  type: X
  url: https://twitter.com/nextgen
- group: company
  title: ''
  type: Newsroom
  url: https://www.nextgen.com/company/newsroom
- group: other
  title: ''
  type: Interoperability
  url: https://www.nextgen.com/solutions/interoperability/api-fhir
- group: commercial
  title: ''
  type: Plans
  url: plans/nextgen-healthcare-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/nextgen-healthcare-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/nextgen-healthcare-finops.yml
- group: build
  title: ''
  type: CLI
  url: cli/nextgen-healthcare-cli.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/nextgen-healthcare-changelog.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/nextgen-healthcare-sandbox.yml
- group: commercial
  title: ''
  type: Pricing
  url: https://www.nextgen.com/pricing
- group: start
  title: ''
  type: SignUp
  url: https://developer.nextgen.com/login?returnUrl=%2F
created: '2026-07-24'
description: 'NextGen Healthcare is a United States ambulatory electronic health record (EHR/EMR) and practice-management vendor headquartered in Remote-first / Atlanta, Georgia, serving outpatient specialties and community health with its NextGen Enterprise and NextGen Office platforms plus the Mirth Connect interoperability engine. Its developer surface is standards-driven: 21st Century Cures Act-certified HL7 FHIR APIs for patient access and provider apps, a SMART App Launch API, and a Bulk FHIR (Flat FHIR) API delivering USCDI data, alongside an 800+ route JSON RESTful Enterprise API family. NextGen Enterprise exposes live FHIR R4 and DSTU2 service base URLs with SMART-on-FHIR OAuth2, and NextGen Office exposes live FHIR R3/R4 and Bulk FHIR endpoints. FHIR resources are coded against the US Core / USCDIv1 implementation guides. Developer onboarding is gated behind an API onboarding form and app registration, which is standard for regulated health-data access in the US market.'
finops:
- name: Nextgen Healthcare Finops
  service_category: ''
  slug: nextgen-healthcare-finops
image: https://nextgen.widen.net/content/mcckjhwu0f/svg/NG_Logo_Final_RGB.svg
jsonld:
- class_count: 22
  name: Nextgen Healthcare Context
  property_count: 2
  slug: nextgen-healthcare-context
layout: provider
mcp_servers:
- description: Candidate MCP tool surface DERIVED from the NextGen Office FHIR OpenAPI/Swagger. NextGen publishes no official hosted/remote MCP server. Tools map one-to-one onto real Bulk FHIR operationIds and the r
  name: NextGen Healthcare MCP Server
  slug: nextgen-healthcare-mcp-server
modified: '2026-08-14'
name: NextGen Healthcare
nav: Providers
network: true
overview: 'NextGen Healthcare publishes 28 APIs on the [APIs.io](https://apis.io/) network, including Allergy Intolerance API, Care Plan API, Care Team API, and 25 more. Tagged areas include Healthcare, United States, EHR, EMR, and FHIR.


  The NextGen Healthcare catalog on APIs.io includes 1 JSON-LD context.


  NextGen Healthcare''s developer surface includes authentication, developer portal, documentation, API reference, getting-started guide, engineering blog, support, and 42 more developer resources.'
plans:
- name: Nextgen Healthcare Plans Pricing
  plan_count: 3
  slug: nextgen-healthcare-plans-pricing
random_paper: 20
rate_limits:
- limit_count: 5
  name: Nextgen Healthcare Rate Limits
  slug: nextgen-healthcare-rate-limits
scopes:
- name: Nextgen Healthcare Scopes
  scope_count: 12
  slug: nextgen-healthcare-scopes
  summary_line: 12 scopes · authorizationCode/clientCredentials
score:
  band: exemplar
  composite: 71.1
  coverage:
    artifact_dirs: 28
    catalog_gap: 46.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 86.8
    commercial_clarity: 86.8
    contract_governance: 18.2
    contract_quality: 62.8
    developer_ergonomics: 63.7
    discoverability: 70.4
    governance: 18.2
    operational_transparency: 50.0
  previous_composite: 71.1
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 2
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 82.5
  schema_version: 0.17.2
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/nextgen-healthcare/refs/heads/main/screenshots/nextgen-healthcare-2026-08-07T185204.png
security:
- kind: authentication
  name: Nextgen Healthcare Authentication
  slug: nextgen-healthcare-authentication
  summary_line: http/oauth2 · 2 schemes
- kind: domain-security
  name: Nextgen Healthcare Domain Security
  slug: nextgen-healthcare-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Nextgen Healthcare Trust Center
  slug: nextgen-healthcare-trust-center
  summary_line: SOC 2 Type II, HITRUST CSF, ISO 27001, HIPAA, PCI DSS, NIST
slug: nextgen-healthcare
tags:
- Healthcare
- United States
- EHR
- EMR
- FHIR
- HL7
- Interoperability
- SMART on FHIR
- USCDI
- Bulk FHIR
- Patient Access
- 21st Century Cures
website: https://www.nextgen.com/
---
