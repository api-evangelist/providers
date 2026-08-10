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
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: derived
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.2
  score: 38.5
  scored_at: '2026-08-10'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Clever Care Agentic Access
  operation_count: 26
  slug: clever-care-agentic-access
  summary_line: 26 operations
api_count: 13
apis:
- description: The Coverage API from Clever Care — 2 operation(s) for coverage.
  name: Clever Care Coverage API
  slug: clever-care-coverage-api
- description: The Endpoint API from Clever Care — 2 operation(s) for endpoint.
  name: Clever Care Endpoint API
  slug: clever-care-endpoint-api
- description: The ExplanationOfBenefit API from Clever Care — 2 operation(s) for explanationofbenefit.
  name: Clever Care ExplanationOfBenefit API
  slug: clever-care-explanationofbenefit-api
- description: The HealthcareService API from Clever Care — 2 operation(s) for healthcareservice.
  name: Clever Care HealthcareService API
  slug: clever-care-healthcareservice-api
- description: The InsurancePlan API from Clever Care — 2 operation(s) for insuranceplan.
  name: Clever Care InsurancePlan API
  slug: clever-care-insuranceplan-api
- description: The List API from Clever Care — 2 operation(s) for list.
  name: Clever Care List API
  slug: clever-care-list-api
- description: The Location API from Clever Care — 2 operation(s) for location.
  name: Clever Care Location API
  slug: clever-care-location-api
- description: The MedicationKnowledge API from Clever Care — 2 operation(s) for medicationknowledge.
  name: Clever Care MedicationKnowledge API
  slug: clever-care-medicationknowledge-api
- description: The Organization API from Clever Care — 2 operation(s) for organization.
  name: Clever Care Organization API
  slug: clever-care-organization-api
- description: The OrganizationAffiliation API from Clever Care — 2 operation(s) for organizationaffiliation.
  name: Clever Care OrganizationAffiliation API
  slug: clever-care-organizationaffiliation-api
- description: The Patient API from Clever Care — 2 operation(s) for patient.
  name: Clever Care Patient API
  slug: clever-care-patient-api
- description: The Practitioner API from Clever Care — 2 operation(s) for practitioner.
  name: Clever Care Practitioner API
  slug: clever-care-practitioner-api
- description: The PractitionerRole API from Clever Care — 2 operation(s) for practitionerrole.
  name: Clever Care PractitionerRole API
  slug: clever-care-practitionerrole-api
artifact_total: 18
common:
- group: company
  title: ''
  type: Website
  url: https://clevercarehealthplan.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://fhir-portal.clevercarehealthplan.com/devportal
- group: docs
  title: ''
  type: Documentation
  url: https://clevercarehealthplan.com/fhir-api-developer-resources/
- group: docs
  title: ''
  type: APIReference
  url: https://fhir-portal.clevercarehealthplan.com/api-docs/
- group: start
  title: ''
  type: GettingStarted
  url: https://clevercarehealthplan.com/fhir-api-developer-resources/
- group: start
  title: ''
  type: SignUp
  url: https://fhir-portal.clevercarehealthplan.com/devportal
- group: operate
  title: ''
  type: Roadmap
  url: https://clevercarehealthplan.com/interoperability-and-patient-access/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://clevercarehealthplan.com/terms-of-use/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://clevercarehealthplan.com/privacy-practices/
- group: auth
  title: ''
  type: Authentication
  url: authentication/clever-care-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/clever-care-scopes.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/clever-care-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/clever-care-domain-security.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/clever-care-lifecycle.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/clever-care-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/clever-care-problem-types.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/clever-care-data-model.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/clever-care-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/clever-care-llms.txt
- group: other
  title: ''
  type: Overlay
  url: overlays/clever-care-fhir-overlay.yaml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/clever-care-well-known.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/clever-care-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: https://clevercarehealthplan.com/interoperability-and-patient-access/
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-07-17'
description: 'Clever Care Health Plan is a California Medicare Advantage (HMO and HMO C-SNP) plan headquartered in Huntington Beach, CA, that blends the healing therapies of Eastern medicine with the innovative practices of Western medicine to serve Los Angeles, Orange, San Diego, Riverside, and San Bernardino counties. In compliance with the CMS Interoperability and Patient Access rule (CMS-9115-F), Clever Care operates a secure, standards-based HL7 FHIR R4 API surface (WSO2 gateway) spanning 13 published resource APIs across three domains: Patient Access (CARIN Blue Button), Provider Directory (Da Vinci PDex Plan-Net), and Drug Formulary (Da Vinci US Drug Formulary). Patient Access resources are secured with SMART on FHIR OAuth 2.0 / OpenID Connect; directory and formulary resources are public and rate-limited. Provider Access, Payer-to-Payer, and Prior Authorization APIs are planned for January 1, 2027.'
image: https://fhir-portal.clevercarehealthplan.com/api-docs/images/cc_logo_H.png
layout: provider
mcp_servers:
- description: ''
  name: clever-care-mcp.yml
  slug: clever-care-mcpyml
modified: '2026-07-18'
name: Clever Care
nav: Providers
network: true
overview: 'Clever Care publishes 13 APIs on the [APIs.io](https://apis.io/) network, including Coverage API, Endpoint API, ExplanationOfBenefit API, and 10 more. Tagged areas include Company, Life Sciences, Health Insurance, Medicare Advantage, and Healthcare.


  Clever Care''s developer surface includes documentation, API reference, getting-started guide, signup flow, authentication, and 19 more developer resources.'
random_paper: 53
scopes:
- name: Clever Care Scopes
  scope_count: 4
  slug: clever-care-scopes
  summary_line: 4 scopes
score:
  band: developing
  composite: 49.7
  delta: 0.0
  facets:
    commercial_clarity: 42.1
    contract_quality: 49.7
    developer_ergonomics: 49.5
    discoverability: 92.6
    governance: 20.8
    operational_transparency: 5.3
  previous_composite: 49.7
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 13
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 86.3
  schema_version: 0.9.1
  scored_at: '2026-08-10'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/clever-care/refs/heads/main/screenshots/clever-care-2026-07-25T205602.png
security:
- kind: authentication
  name: Clever Care Authentication
  slug: clever-care-authentication
  summary_line: oauth2/openIdConnect · 3 schemes
- kind: domain-security
  name: Clever Care Domain Security
  slug: clever-care-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: clever-care
tags:
- Company
- Life Sciences
- Health Insurance
- Medicare Advantage
- Healthcare
- FHIR
- Healthcare Interoperability
- Patient Access
- Provider Directory
- CMS-9115-F
website: https://clevercarehealthplan.com
---
