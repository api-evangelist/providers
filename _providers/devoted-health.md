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
    agentic_access: false
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: documented
    idempotency: false
    mcp_server: derived
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.2
  score: 36.3
  scored_at: '2026-07-28'
api_count: 21
apis:
- description: The CodeSystem FHIR resource type
  name: Devoted Health CodeSystem API
  slug: devoted-health-codesystem-api
- description: The Condition API from Devoted Health — 1 operation(s) for condition.
  name: Devoted Health Condition API
  slug: devoted-health-condition-api
- description: The Encounter API from Devoted Health — 1 operation(s) for encounter.
  name: Devoted Health Encounter API
  slug: devoted-health-encounter-api
- description: The ExplanationOfBenefit API from Devoted Health — 1 operation(s) for explanationofbenefit.
  name: Devoted Health ExplanationOfBenefit API
  slug: devoted-health-explanationofbenefit-api
- description: The HealthcareService FHIR resource type
  name: Devoted Health HealthcareService API
  slug: devoted-health-healthcareservice-api
- description: The InsurancePlan FHIR resource type
  name: Devoted Health InsurancePlan API
  slug: devoted-health-insuranceplan-api
- description: The List FHIR resource type
  name: Devoted Health List API
  slug: devoted-health-list-api
- description: The Location FHIR resource type
  name: Devoted Health Location API
  slug: devoted-health-location-api
- description: The Medication API from Devoted Health — 1 operation(s) for medication.
  name: Devoted Health Medication API
  slug: devoted-health-medication-api
- description: The MedicationKnowledge FHIR resource type
  name: Devoted Health MedicationKnowledge API
  slug: devoted-health-medicationknowledge-api
- description: The OperationDefinition FHIR resource type
  name: Devoted Health OperationDefinition API
  slug: devoted-health-operationdefinition-api
- description: The Organization FHIR resource type
  name: Devoted Health Organization API
  slug: devoted-health-organization-api
- description: The OrganizationAffiliation FHIR resource type
  name: Devoted Health OrganizationAffiliation API
  slug: devoted-health-organizationaffiliation-api
- description: The Patient API from Devoted Health — 2 operation(s) for patient.
  name: Devoted Health Patient API
  slug: devoted-health-patient-api
- description: The Practitioner FHIR resource type
  name: Devoted Health Practitioner API
  slug: devoted-health-practitioner-api
- description: The PractitionerRole FHIR resource type
  name: Devoted Health PractitionerRole API
  slug: devoted-health-practitionerrole-api
- description: The SearchParameter FHIR resource type
  name: Devoted Health SearchParameter API
  slug: devoted-health-searchparameter-api
- description: The StructureDefinition FHIR resource type
  name: Devoted Health StructureDefinition API
  slug: devoted-health-structuredefinition-api
- description: The Subscription FHIR resource type
  name: Devoted Health Subscription API
  slug: devoted-health-subscription-api
- description: Server-level operations
  name: Devoted Health System Level Operations API
  slug: devoted-health-system-level-operations-api
- description: The ValueSet FHIR resource type
  name: Devoted Health ValueSet API
  slug: devoted-health-valueset-api
artifact_total: 25
common:
- group: company
  title: ''
  type: Website
  url: https://devoted.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://www.devoted.com/developers/
- group: docs
  title: ''
  type: Documentation
  url: https://www.devoted.com/developers/
- group: docs
  title: ''
  type: APIReference
  url: https://devoted.com/developers/fhir/swagger/
- group: start
  title: ''
  type: SignUp
  url: https://forms.gle/UFYvckiAeEjWP49K9
- group: operate
  title: ''
  type: Support
  url: mailto:interop@devoted.com
- group: company
  title: ''
  type: Blog
  url: https://www.devoted.com/newsroom/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.devoted.com/privacy-policy/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.devoted.com/terms-of-use/
- group: auth
  title: ''
  type: Authentication
  url: authentication/devoted-health-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/devoted-health-scopes.yml
- group: other
  title: ''
  type: OpenIDConnect
  url: well-known/devoted-health-openid-configuration.json
- group: agent
  title: ''
  type: WellKnown
  url: well-known/devoted-health-well-known.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/devoted-health-conformance.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/devoted-health-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/devoted-health-lifecycle.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/devoted-health-conventions.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/devoted-health-data-model.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/devoted-health-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/devoted-health-llms.txt
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/devoted-health-patient-access-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/devoted-health-provider-directory-overlay.yaml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/devoted-health-domain-security.yml
created: '2026-07-17'
description: 'Devoted Health is a Medicare Advantage health insurance company that operates its own health plans, clinical care, and pharmacy for older Americans. For developers, Devoted publishes CMS Interoperability (21st Century Cures Act) FHIR R4 (4.0.1) APIs: a member-authorized Patient Access API exposing claims, clinical, and coverage data (Patient, Condition, Encounter, Medication, ExplanationOfBenefit), and public Provider Directory, Pharmacy Directory, and Drug Formulary APIs (Practitioner, Organization, Location, HealthcareService, InsurancePlan, MedicationKnowledge, List). Access uses OAuth 2.0 / OpenID Connect with SMART-on-FHIR authorization; third-party member-facing apps register for a Client ID and Secret through Devoted''s interoperability team.'
image: https://www.devoted.com/wp-content/uploads/2021/03/devoted-health-logo.png
layout: provider
mcp_servers:
- description: ''
  name: devoted-health-mcp.yml
  slug: devoted-health-mcpyml
modified: '2026-07-18'
name: Devoted Health
nav: Providers
network: true
overview: 'Devoted Health publishes 21 APIs on the [APIs.io](https://apis.io/) network, including CodeSystem API, Condition API, Encounter API, and 18 more. Tagged areas include Company, Healthcare, Health Insurance, Medicare Advantage, and FHIR.


  Devoted Health''s developer surface includes documentation, API reference, signup flow, support, engineering blog, authentication, and 18 more developer resources.'
random_paper: 0
scopes:
- name: Devoted Health Scopes
  scope_count: 14
  slug: devoted-health-scopes
  summary_line: 14 scopes
score:
  band: developing
  composite: 44.1
  delta: 0.8
  facets:
    commercial_clarity: 34.2
    contract_quality: 47.5
    developer_ergonomics: 45.1
    discoverability: 92.6
    governance: 20.8
    operational_transparency: 0.0
  previous_composite: 43.3
  provenance:
    conformance: first-party
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 21
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 70.0
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/devoted-health/refs/heads/main/screenshots/devoted-health-2026-07-25T211822.png
security:
- kind: authentication
  name: Devoted Health Authentication
  slug: devoted-health-authentication
  summary_line: oauth2/openIdConnect · 2 schemes
- kind: domain-security
  name: Devoted Health Domain Security
  slug: devoted-health-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: devoted-health
tags:
- Company
- Healthcare
- Health Insurance
- Medicare Advantage
- FHIR
- Interoperability
- Patient Access
- Provider Directory
- Drug Formulary
- CMS
- HL7
- SMART on FHIR
website: https://devoted.com
---
