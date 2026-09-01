---
access_model:
  confidence: high
  label: Enterprise · Self-serve signup
  onboarding: self-serve
  pricing: enterprise
  public: false
  source:
  - plans
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
    auth_clarity: served
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: true
    idempotency: documented
    mcp_server: documented
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 38.5
  scored_at: '2026-09-01'
agentic_access:
- acting_count: 4
  human_in_the_loop: 0
  name: Health Gorilla Agentic Access
  operation_count: 22
  slug: health-gorilla-agentic-access
  summary_line: 22 operations · 4 acting
api_count: 1
apis:
- description: Raw clinical document content.
  name: Health Gorilla Binary API
  slug: health-gorilla-binary-api
- description: FHIR server capability discovery.
  name: Health Gorilla CapabilityStatement API
  slug: health-gorilla-capabilitystatement-api
- description: Patient insurance coverage / eligibility.
  name: Health Gorilla Coverage API
  slug: health-gorilla-coverage-api
- description: Structured lab and radiology results.
  name: Health Gorilla DiagnosticReport API
  slug: health-gorilla-diagnosticreport-api
- description: Clinical document metadata.
  name: Health Gorilla DocumentReference API
  slug: health-gorilla-documentreference-api
- description: Individual result observations.
  name: Health Gorilla Observation API
  slug: health-gorilla-observation-api
- description: Patient demographics and patient-scoped record retrieval.
  name: Health Gorilla Patient API
  slug: health-gorilla-patient-api
- description: Ordering and rendering providers.
  name: Health Gorilla Practitioner API
  slug: health-gorilla-practitioner-api
- description: Parent diagnostic orders nesting individual ServiceRequest tests.
  name: Health Gorilla RequestGroup API
  slug: health-gorilla-requestgroup-api
- description: Diagnostic (lab and radiology) order requests.
  name: Health Gorilla ServiceRequest API
  slug: health-gorilla-servicerequest-api
arazzos:
- description: Locate a patient, search their insurance Coverage resources, then read a single Coverage for full plan detail.
  name: Health Gorilla Coverage Retrieval
  slug: health-gorilla-coverage-workflow
- description: Confirm server capabilities, locate a patient, then place a laboratory order as a ServiceRequest grouped inside a RequestGroup.
  name: Health Gorilla FHIR Lab Order
  slug: health-gorilla-lab-order-workflow
- description: Locate a patient, read the Patient resource, then pull the complete US Core record with the Patient $everything operation.
  name: Health Gorilla Patient Everything
  slug: health-gorilla-patient-everything-workflow
- description: Locate a patient, then pull their US Core laboratory DiagnosticReports, read one report, and retrieve the discrete result Observations.
  name: Health Gorilla Lab Results Retrieval
  slug: health-gorilla-results-retrieval-workflow
artifact_total: 37
asyncapis:
- description: ''
  name: Health Gorilla Webhooks
  slug: health-gorilla-webhooks
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Health Gorilla FHIR R4 Binary API
  slug: open-health-gorilla-binary-api
- collection_type: open
  name: Health Gorilla FHIR R4 Binary CapabilityStatement API
  slug: open-health-gorilla-capabilitystatement-api
- collection_type: open
  name: Health Gorilla FHIR R4 Binary Coverage API
  slug: open-health-gorilla-coverage-api
- collection_type: open
  name: Health Gorilla FHIR R4 Binary DiagnosticReport API
  slug: open-health-gorilla-diagnosticreport-api
- collection_type: open
  name: Health Gorilla FHIR R4 Binary DocumentReference API
  slug: open-health-gorilla-documentreference-api
- collection_type: open
  name: Health Gorilla FHIR R4 Binary Observation API
  slug: open-health-gorilla-observation-api
- collection_type: open
  name: Health Gorilla FHIR R4 Binary Patient API
  slug: open-health-gorilla-patient-api
- collection_type: open
  name: Health Gorilla FHIR R4 Binary Practitioner API
  slug: open-health-gorilla-practitioner-api
- collection_type: open
  name: Health Gorilla FHIR R4 Binary RequestGroup API
  slug: open-health-gorilla-requestgroup-api
- collection_type: open
  name: Health Gorilla FHIR R4 Binary ServiceRequest API
  slug: open-health-gorilla-servicerequest-api
- collection_type: open
  name: Health Gorilla FHIR R4 API
  slug: open-health-gorilla
common:
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/health-gorilla-capability-edges.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/health-gorilla-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/health-gorilla-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/health-gorilla-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/healthgorilla
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/health-gorilla
- group: company
  title: ''
  type: Website
  url: https://www.healthgorilla.com
- group: docs
  title: ''
  type: Documentation
  url: https://developer.healthgorilla.com
- group: commercial
  title: ''
  type: Plans
  url: plans/health-gorilla-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/health-gorilla-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/health-gorilla-finops.yml
- group: design
  title: ''
  type: ArazzoWorkflows
  url: ''
- group: agent
  title: ''
  type: WellKnown
  url: well-known/health-gorilla-well-known.yml
- group: other
  title: ''
  type: CapabilityStatement
  url: fhir/health-gorilla-fhir.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/health-gorilla-scopes.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/health-gorilla-conventions.yml
- group: design
  title: ''
  type: Idempotency
  url: conventions/health-gorilla-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/health-gorilla-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/health-gorilla-lifecycle.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://status.healthgorilla.com
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/health-gorilla-changelog.yml
- group: operate
  title: ''
  type: ChangeLog
  url: https://developer.healthgorilla.com/changelog
- group: start
  title: ''
  type: Sandbox
  url: sandbox/health-gorilla-sandbox.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/health-gorilla-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: https://www.healthgorilla.com/home/company/health-data-security
- group: auth
  title: ''
  type: TrustCenter
  url: security/health-gorilla-trust-center.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/health-gorilla-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: https://www.healthgorilla.com/home/security-txt
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/health-gorilla-webhooks.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/health-gorilla-llms.txt
- group: agent
  title: ''
  type: MCPServer
  url: mcp/health-gorilla-mcp.yml
- group: build
  title: ''
  type: ToolCrosswalk
  url: mcp/health-gorilla-tool-crosswalk.yml
- group: build
  title: ''
  type: Packages
  url: packages/health-gorilla-packages.yml
- group: design
  title: ''
  type: Components
  url: components/health-gorilla-components.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/health-gorilla-data-model.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.healthgorilla.com
- group: docs
  title: ''
  type: APIReference
  url: https://developer.healthgorilla.com/reference/api-reference
- group: start
  title: ''
  type: GettingStarted
  url: https://developer.healthgorilla.com/docs/developer-quickstart
- group: operate
  title: ''
  type: Support
  url: https://support.healthgorilla.com
- group: company
  title: ''
  type: Blog
  url: https://www.healthgorilla.com/home/resources/blogs
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.healthgorilla.com/home/terms-of-use
- group: commercial
  title: ''
  type: TermsOfService
  url: https://developer.healthgorilla.com/docs/terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.healthgorilla.com/home/privacy-policy
- group: start
  title: ''
  type: Login
  url: https://www.healthgorilla.com/login
created: '2026-06-21'
description: Health Gorilla operates a national health-data interoperability network and a FHIR-first API suite for healthcare developers. Its HL7 FHIR R4 REST API provides access to patient records, person-authorized record retrieval across national exchange networks (QHIN / TEFCA), diagnostic (lab and radiology) ordering and results, clinical documents, and coverage/eligibility data under OAuth 2.0.
finops:
- name: Health Gorilla Finops
  service_category: Healthcare Interoperability
  slug: health-gorilla-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/health-gorilla.png
layout: provider
mcp_servers:
- description: Health Gorilla serves a live remote MCP endpoint from its own developer-portal host. An agent can reach it today at https://developer.healthgorilla.com/mcp — no install step, no local process. What it
  name: Health Gorilla MCP Server
  slug: health-gorilla-mcp-server
modified: '2026-08-14'
name: Health Gorilla
nav: Providers
network: true
overview: 'Health Gorilla publishes 10 APIs on the [APIs.io](https://apis.io/) network, including Binary API, CapabilityStatement API, Coverage API, and 7 more. Tagged areas include Health, Interoperability, FHIR, Clinical Data, and Lab Ordering.


  The Health Gorilla catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Health Gorilla''s developer surface includes authentication, documentation, changelog, sandbox, API reference, getting-started guide, support, and 37 more developer resources.'
plans:
- name: Health Gorilla Plans Pricing
  plan_count: 3
  slug: health-gorilla-plans-pricing
random_paper: 14
rate_limits:
- limit_count: 7
  name: Health Gorilla Rate Limits
  slug: health-gorilla-rate-limits
scopes:
- name: Health Gorilla Scopes
  scope_count: 11
  slug: health-gorilla-scopes
  summary_line: 11 scopes · authorizationCode/implicit/clientCredentials/jwtBearer
score:
  band: exemplar
  composite: 69.8
  coverage:
    artifact_dirs: 29
    catalog_gap: 51.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 82.9
    commercial_clarity: 82.9
    contract_governance: 18.2
    contract_quality: 58.5
    developer_ergonomics: 45.8
    discoverability: 75.9
    governance: 18.2
    operational_transparency: 76.3
  previous_composite: 69.8
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 10
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 83.8
  schema_version: 0.17.2
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/health-gorilla/refs/heads/main/screenshots/health-gorilla-2026-07-25T220828.png
security:
- kind: authentication
  name: Health Gorilla Authentication
  slug: health-gorilla-authentication
  summary_line: oauth2/openIdConnect/http · 3 schemes
- kind: domain-security
  name: Health Gorilla Domain Security
  slug: health-gorilla-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Health Gorilla Vulnerability Disclosure
  slug: health-gorilla-vulnerability-disclosure
  summary_line: Hackerone · security.txt · contact published
- kind: trust-center
  name: Health Gorilla Trust Center
  slug: health-gorilla-trust-center
  summary_line: HITRUST r2, SOC 2 Type 2, HIPAA
slug: health-gorilla
tags:
- Health
- Interoperability
- FHIR
- Clinical Data
- Lab Ordering
- TEFCA
- QHIN
- Health Information Exchange
- Lab Results
- Clinical Documents
- SMART on FHIR
- Patient Records
- HL7
website: https://www.healthgorilla.com
---
