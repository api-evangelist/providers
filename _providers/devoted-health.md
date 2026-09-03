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
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 38.7
  scored_at: '2026-09-03'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Devoted Health Agentic Access
  operation_count: 6
  slug: devoted-health-agentic-access
  summary_line: 6 operations
api_count: 3
apis:
- baseURL: https://api.prod.devoted.com/fhir
  baseurl_source: declared
  description: The CodeSystem FHIR resource type
  name: Devoted Health CodeSystem API
  slug: devoted-health-codesystem-api
- baseURL: https://api.prod.devoted.com/fhir
  baseurl_source: declared
  description: The Condition API from Devoted Health — 1 operation(s) for condition.
  name: Devoted Health Condition API
  slug: devoted-health-condition-api
- baseURL: https://api.prod.devoted.com/fhir
  baseurl_source: declared
  description: The Encounter API from Devoted Health — 1 operation(s) for encounter.
  name: Devoted Health Encounter API
  slug: devoted-health-encounter-api
- baseURL: https://api.prod.devoted.com/fhir
  baseurl_source: declared
  description: The ExplanationOfBenefit API from Devoted Health — 1 operation(s) for explanationofbenefit.
  name: Devoted Health ExplanationOfBenefit API
  slug: devoted-health-explanationofbenefit-api
- baseURL: https://api.prod.devoted.com/fhir
  baseurl_source: declared
  description: The HealthcareService FHIR resource type
  name: Devoted Health HealthcareService API
  slug: devoted-health-healthcareservice-api
- baseURL: https://api.prod.devoted.com/fhir
  baseurl_source: declared
  description: The InsurancePlan FHIR resource type
  name: Devoted Health InsurancePlan API
  slug: devoted-health-insuranceplan-api
- baseURL: https://api.prod.devoted.com/fhir
  baseurl_source: declared
  description: The List FHIR resource type
  name: Devoted Health List API
  slug: devoted-health-list-api
- baseURL: https://api.prod.devoted.com/fhir
  baseurl_source: declared
  description: The Location FHIR resource type
  name: Devoted Health Location API
  slug: devoted-health-location-api
- baseURL: https://api.prod.devoted.com/fhir
  baseurl_source: declared
  description: The Medication API from Devoted Health — 1 operation(s) for medication.
  name: Devoted Health Medication API
  slug: devoted-health-medication-api
- baseURL: https://api.prod.devoted.com/fhir
  baseurl_source: declared
  description: The MedicationKnowledge FHIR resource type
  name: Devoted Health MedicationKnowledge API
  slug: devoted-health-medicationknowledge-api
- baseURL: https://api.prod.devoted.com/fhir
  baseurl_source: declared
  description: The OperationDefinition FHIR resource type
  name: Devoted Health OperationDefinition API
  slug: devoted-health-operationdefinition-api
- baseURL: https://api.prod.devoted.com/fhir
  baseurl_source: declared
  description: The Organization FHIR resource type
  name: Devoted Health Organization API
  slug: devoted-health-organization-api
- baseURL: https://api.prod.devoted.com/fhir
  baseurl_source: declared
  description: The OrganizationAffiliation FHIR resource type
  name: Devoted Health OrganizationAffiliation API
  slug: devoted-health-organizationaffiliation-api
- baseURL: https://api.prod.devoted.com/fhir
  baseurl_source: declared
  description: The Patient API from Devoted Health — 2 operation(s) for patient.
  name: Devoted Health Patient API
  slug: devoted-health-patient-api
- baseURL: https://api.prod.devoted.com/fhir
  baseurl_source: declared
  description: The Practitioner FHIR resource type
  name: Devoted Health Practitioner API
  slug: devoted-health-practitioner-api
- baseURL: https://api.prod.devoted.com/fhir
  baseurl_source: declared
  description: The PractitionerRole FHIR resource type
  name: Devoted Health PractitionerRole API
  slug: devoted-health-practitionerrole-api
- baseURL: https://api.prod.devoted.com/fhir
  baseurl_source: declared
  description: The SearchParameter FHIR resource type
  name: Devoted Health SearchParameter API
  slug: devoted-health-searchparameter-api
- baseURL: https://api.prod.devoted.com/fhir
  baseurl_source: declared
  description: The StructureDefinition FHIR resource type
  name: Devoted Health StructureDefinition API
  slug: devoted-health-structuredefinition-api
- baseURL: https://api.prod.devoted.com/fhir
  baseurl_source: declared
  description: The Subscription FHIR resource type
  name: Devoted Health Subscription API
  slug: devoted-health-subscription-api
- baseURL: https://api.prod.devoted.com/fhir
  baseurl_source: declared
  description: Server-level operations
  name: Devoted Health System Level Operations API
  slug: devoted-health-system-level-operations-api
- baseURL: https://api.prod.devoted.com/fhir
  baseurl_source: declared
  description: The ValueSet FHIR resource type
  name: Devoted Health ValueSet API
  slug: devoted-health-valueset-api
- description: Public FHIR R4 API for in-network providers, facilities, and pharmacies, based on the Da Vinci PDEX Plan-Net reference implementation.
  name: Provider & Pharmacy Directory API
  slug: provider-pharmacy-directory-api
- description: Public FHIR R4 API for drug formulary information, based on the Da Vinci PDEX US Drug Formulary implementation guide.
  name: Plan Coverage & Formularies API
  slug: plan-coverage-formularies-api
artifact_total: 49
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Untitled CodeSystem API
  slug: open-devoted-health-codesystem-api
- collection_type: open
  name: Untitled Condition API
  slug: open-devoted-health-condition-api
- collection_type: open
  name: Untitled Condition Encounter API
  slug: open-devoted-health-encounter-api
- collection_type: open
  name: Untitled Condition ExplanationOfBenefit API
  slug: open-devoted-health-explanationofbenefit-api
- collection_type: open
  name: Untitled CodeSystem HealthcareService API
  slug: open-devoted-health-healthcareservice-api
- collection_type: open
  name: Untitled CodeSystem InsurancePlan API
  slug: open-devoted-health-insuranceplan-api
- collection_type: open
  name: Untitled CodeSystem List API
  slug: open-devoted-health-list-api
- collection_type: open
  name: Untitled CodeSystem Location API
  slug: open-devoted-health-location-api
- collection_type: open
  name: Untitled Condition Medication API
  slug: open-devoted-health-medication-api
- collection_type: open
  name: Untitled CodeSystem MedicationKnowledge API
  slug: open-devoted-health-medicationknowledge-api
- collection_type: open
  name: Untitled CodeSystem OperationDefinition API
  slug: open-devoted-health-operationdefinition-api
- collection_type: open
  name: Untitled CodeSystem Organization API
  slug: open-devoted-health-organization-api
- collection_type: open
  name: Untitled CodeSystem OrganizationAffiliation API
  slug: open-devoted-health-organizationaffiliation-api
- collection_type: open
  name: Untitled Condition Patient API
  slug: open-devoted-health-patient-api
- collection_type: open
  name: Untitled CodeSystem Practitioner API
  slug: open-devoted-health-practitioner-api
- collection_type: open
  name: Untitled CodeSystem PractitionerRole API
  slug: open-devoted-health-practitionerrole-api
- collection_type: open
  name: Untitled CodeSystem SearchParameter API
  slug: open-devoted-health-searchparameter-api
- collection_type: open
  name: Untitled CodeSystem StructureDefinition API
  slug: open-devoted-health-structuredefinition-api
- collection_type: open
  name: Untitled CodeSystem Subscription API
  slug: open-devoted-health-subscription-api
- collection_type: open
  name: Untitled CodeSystem System Level Operations API
  slug: open-devoted-health-system-level-operations-api
- collection_type: open
  name: Untitled CodeSystem ValueSet API
  slug: open-devoted-health-valueset-api
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
  type: X-MCPServerCandidate
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
- group: start
  title: ''
  type: GettingStarted
  url: https://www.devoted.com/developers/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/DevotedHealth
- group: auth
  title: ''
  type: Authentication
  url: authentication/devoted-health-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/devoted-health-scopes.yml
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
  type: Conventions
  url: conventions/devoted-health-conventions.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/devoted-health-data-model.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/devoted-health-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/devoted-health-lifecycle.yml
- group: agent
  title: ''
  type: X-MCPServerCandidate
  url: mcp/devoted-health-mcp.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/devoted-health-patient-access-overlay.yaml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/devoted-health-llms.txt
- group: auth
  title: ''
  type: DomainSecurity
  url: security/devoted-health-domain-security.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/devoted-health-agentic-access.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/devoted-health-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/devoted-health-scopes.yml
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
  type: Conventions
  url: conventions/devoted-health-conventions.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/devoted-health-data-model.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/devoted-health-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/devoted-health-lifecycle.yml
- group: agent
  title: ''
  type: X-MCPServerCandidate
  url: mcp/devoted-health-mcp.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/devoted-health-patient-access-overlay.yaml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/devoted-health-llms.txt
- group: auth
  title: ''
  type: DomainSecurity
  url: security/devoted-health-domain-security.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/devoted-health-agentic-access.yml
created: '2026-07-17'
description: 'Devoted Health is a Medicare Advantage health insurance company that operates its own health plans, clinical care, and pharmacy for older Americans. For developers, Devoted publishes CMS Interoperability (21st Century Cures Act) FHIR R4 (4.0.1) APIs: a member-authorized Patient Access API exposing claims, clinical, and coverage data (Patient, Condition, Encounter, Medication, ExplanationOfBenefit), and public Provider Directory, Pharmacy Directory, and Drug Formulary APIs (Practitioner, Organization, Location, HealthcareService, InsurancePlan, MedicationKnowledge, List). Access uses OAuth 2.0 / OpenID Connect with SMART-on-FHIR authorization; third-party member-facing apps register for a Client ID and Secret through Devoted''s interoperability team.'
image: https://www.devoted.com/wp-content/uploads/2021/03/devoted-health-logo.png
layout: provider
modified: '2026-07-18'
name: Devoted Health
nav: Providers
network: true
overview: 'Devoted Health publishes 21 APIs on the [APIs.io](https://apis.io/) network, including CodeSystem API, Condition API, Encounter API, and 18 more. Tagged areas include Company, Healthcare, Health Insurance, Medicare Advantage, and FHIR.


  Devoted Health''s developer surface includes documentation, API reference, signup flow, support, engineering blog, authentication, getting-started guide, and 45 more developer resources.'
random_paper: 15
scopes:
- name: Devoted Health Scopes
  scope_count: 14
  slug: devoted-health-scopes
  summary_line: 14 scopes
score:
  band: developing
  composite: 48.3
  coverage:
    artifact_dirs: 17
    catalog_gap: 75.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 34.2
    commercial_clarity: 34.2
    contract_governance: 18.2
    contract_quality: 45.4
    developer_ergonomics: 58.9
    discoverability: 81.5
    governance: 18.2
    operational_transparency: 2.6
  previous_composite: 48.3
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
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
  schema_version: 0.18.2
  scored_at: '2026-09-03'
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
