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
    agentic_commerce: false
    auth_clarity: negotiable
    consent_identity: false
    delegated_identity: documented
    dry_run_mode: na
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: false
    idempotency: na
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 30.2
  scored_at: '2026-09-01'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Clevercarehealthplan Agentic Access
  operation_count: 27
  slug: clevercarehealthplan-agentic-access
  summary_line: 27 operations
api_count: 1
apis:
- description: Public (rate limited) drug formulary resources
  name: Clever Care Health Plan Drug Formulary API
  slug: clevercarehealthplan-drug-formulary-api
- description: Secured (OpenID Connect / OAuth 2.0) member data resources
  name: Clever Care Health Plan Patient Access API
  slug: clevercarehealthplan-patient-access-api
- description: Public (rate limited) provider directory resources
  name: Clever Care Health Plan Provider Directory API
  slug: clevercarehealthplan-provider-directory-api
artifact_total: 12
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Clever Care Health Plan FHIR R4 Drug Formulary API
  slug: open-clevercarehealthplan-drug-formulary-api
- collection_type: open
  name: Clever Care Health Plan FHIR R4 Drug Formulary Patient Access API
  slug: open-clevercarehealthplan-patient-access-api
- collection_type: open
  name: Clever Care Health Plan FHIR R4 Drug Formulary Provider Directory API
  slug: open-clevercarehealthplan-provider-directory-api
common:
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/clevercarehealthplan-capability-edges.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/clevercarehealthplan-fhir-overlay.yaml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://fhir-portal.clevercarehealthplan.com/devportal
- group: start
  title: ''
  type: GettingStarted
  url: https://clevercarehealthplan.com/fhir-api-developer-resources/
- group: docs
  title: ''
  type: Documentation
  url: https://fhir-portal.clevercarehealthplan.com/api-docs/
- group: docs
  title: ''
  type: APIReference
  url: https://fhir-portal.clevercarehealthplan.com/api-docs/
- group: start
  title: ''
  type: SignUp
  url: https://fhir-portal.clevercarehealthplan.com/devportal
- group: auth
  title: ''
  type: Authentication
  url: authentication/clevercarehealthplan-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/clevercarehealthplan-scopes.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/clevercarehealthplan-agentic-access.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/clevercarehealthplan-mcp.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/clevercarehealthplan-well-known.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/clevercarehealthplan-llms.txt
- group: design
  title: ''
  type: Conformance
  url: conformance/clevercarehealthplan-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: https://clevercarehealthplan.com/medicare-compliance/
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/clevercarehealthplan-problem-types.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/clevercarehealthplan-conventions.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/clevercarehealthplan-lifecycle.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/clevercarehealthplan-data-model.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/clevercarehealthplan-domain-security.yml
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://clevercarehealthplan.com/privacy-practices/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://clevercarehealthplan.com/terms-of-use/
- group: company
  title: ''
  type: Website
  url: https://clevercarehealthplan.com
created: '2026-07-17'
description: 'Clever Care Health Plan is a California Medicare Advantage (HMO and HMO C-SNP) insurer that blends Eastern and Western medicine for seniors. For developers it publishes an HL7 FHIR R4 (4.0.1) API implementing the CMS Interoperability and Patient Access final rule (CMS-9115-F): a secured Patient Access API (Patient, Coverage, and CARIN Blue Button ExplanationOfBenefit) protected with SMART-on-FHIR OAuth 2.0 / OpenID Connect, plus public, rate-limited Provider Directory and Drug Formulary APIs. The FHIR server runs on WSO2 Open Healthcare with a developer portal for app registration and API subscription.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/clevercarehealthplan.png
layout: provider
mcp_servers:
- description: ''
  name: Clever Care Health Plan MCP Server
  slug: clever-care-health-plan-mcp-server
modified: '2026-07-18'
name: Clever Care Health Plan
nav: Providers
network: true
overview: 'Clever Care Health Plan publishes 3 APIs on the [APIs.io](https://apis.io/) network: Drug Formulary API, Patient Access API, and Provider Directory API. Tagged areas include Company, Healthcare, Health Insurance, Medicare Advantage, and FHIR.


  Clever Care Health Plan''s developer surface includes getting-started guide, documentation, API reference, signup flow, authentication, and 19 more developer resources.'
random_paper: 9
scopes:
- name: Clevercarehealthplan Scopes
  scope_count: 4
  slug: clevercarehealthplan-scopes
  summary_line: 4 scopes · authorizationCode/clientCredentials
score:
  band: developing
  composite: 40.4
  coverage:
    artifact_dirs: 18
    catalog_gap: 78.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 13.2
    commercial_clarity: 13.2
    contract_governance: 18.2
    contract_quality: 49.4
    developer_ergonomics: 39.9
    discoverability: 75.9
    governance: 18.2
    operational_transparency: 0.0
  previous_composite: 40.4
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
    jurisdictions:
    - jurisdiction: US
      standard: hipaa
    - jurisdiction: US
      standard: us-core
    jurisdictions_satisfied: 1
    matched_via: tags
    regime: Health
    regime_id: health
    score: 70.0
  schema_version: 0.17.2
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/clevercarehealthplan/refs/heads/main/screenshots/clevercarehealthplan-2026-07-25T205602.png
security:
- kind: authentication
  name: Clevercarehealthplan Authentication
  slug: clevercarehealthplan-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Clevercarehealthplan Domain Security
  slug: clevercarehealthplan-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: clevercarehealthplan
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
website: https://clevercarehealthplan.com
---
