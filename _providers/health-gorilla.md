---
access_model:
  confidence: high
  gated: none
  gated_source:
  - onboarding
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  - scopes
  - rate-limits
  - security
  - sandbox
  trial: false
  try_now: true
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
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: true
    idempotency: documented
    mcp_server: verified
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 43.4
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 4
  human_in_the_loop: 0
  name: Health Gorilla Agentic Access
  operation_count: 22
  slug: health-gorilla-agentic-access
  summary_line: 22 operations · 4 acting
api_count: 1
apis:
- baseURL: https://api.healthgorilla.com/fhir/R4
  baseurl_source: declared
  description: Raw clinical document content.
  name: Health Gorilla Binary API
  slug: health-gorilla-binary-api
- baseURL: https://api.healthgorilla.com/fhir/R4
  baseurl_source: declared
  description: Patient insurance coverage / eligibility.
  name: Health Gorilla Coverage API
  slug: health-gorilla-coverage-api
- baseURL: https://api.healthgorilla.com/fhir/R4
  baseurl_source: declared
  description: Structured lab and radiology results.
  name: Health Gorilla DiagnosticReport API
  slug: health-gorilla-diagnosticreport-api
- baseURL: https://api.healthgorilla.com/fhir/R4
  baseurl_source: declared
  description: Individual result observations.
  name: Health Gorilla Observation API
  slug: health-gorilla-observation-api
- baseURL: https://api.healthgorilla.com/fhir/R4
  baseurl_source: declared
  description: Patient demographics and patient-scoped record retrieval.
  name: Health Gorilla Patient API
  slug: health-gorilla-patient-api
- baseURL: https://api.healthgorilla.com/fhir/R4
  baseurl_source: declared
  description: Ordering and rendering providers.
  name: Health Gorilla Practitioner API
  slug: health-gorilla-practitioner-api
- baseURL: https://api.healthgorilla.com/fhir/R4
  baseurl_source: declared
  description: Parent diagnostic orders nesting individual ServiceRequest tests.
  name: Health Gorilla RequestGroup API
  slug: health-gorilla-requestgroup-api
- baseURL: https://api.healthgorilla.com/fhir/R4
  baseurl_source: declared
  description: Diagnostic (lab and radiology) order requests.
  name: Health Gorilla ServiceRequest API
  slug: health-gorilla-servicerequest-api
- baseURL: https://api.healthgorilla.com/fhir/R4
  baseurl_source: declared
  description: FHIR server capability discovery.
  name: Health Gorilla Capability Statement API
  slug: health-gorilla-capability-statement-api
- baseURL: https://api.healthgorilla.com/fhir/R4
  baseurl_source: declared
  description: Clinical document metadata.
  name: Health Gorilla Document Reference API
  slug: health-gorilla-document-reference-api
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
artifact_total: 53
asyncapis:
- description: ''
  name: Health Gorilla Webhooks
  slug: health-gorilla-webhooks
collections:
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
- group: design
  href: https://artifacts.apis.io/health-gorilla/rules/health-gorilla-rules.yml
  title: ''
  type: Spectral
  url: rules/health-gorilla-rules.yml
- group: design
  href: https://artifacts.apis.io/health-gorilla/json-ld/health-gorilla-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/health-gorilla-context.jsonld
- group: design
  href: https://artifacts.apis.io/health-gorilla/vocabulary/health-gorilla-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/health-gorilla-vocabulary.yml
- group: operate
  href: https://artifacts.apis.io/health-gorilla/lifecycle/health-gorilla-lifecycle.yml
  title: ''
  type: Deprecation
  url: lifecycle/health-gorilla-lifecycle.yml
- group: other
  href: https://artifacts.apis.io/health-gorilla/hosts/health-gorilla-hosts.yml
  title: ''
  type: Hosts
  url: hosts/health-gorilla-hosts.yml
- group: other
  href: https://artifacts.apis.io/health-gorilla/vendors/health-gorilla-vendors.yml
  title: ''
  type: Vendors
  url: vendors/health-gorilla-vendors.yml
- group: build
  href: https://artifacts.apis.io/health-gorilla/packages/health-gorilla-packages.yml
  title: ''
  type: SDKs
  url: packages/health-gorilla-packages.yml
- group: company
  title: ''
  type: Newsroom
  url: https://www.healthgorilla.com/home/resources/news
- group: commercial
  title: ''
  type: Pricing
  url: https://www.healthgorilla.com/home/contact
- group: other
  href: https://artifacts.apis.io/health-gorilla/overlays/health-gorilla-capabilitystatement-api-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/health-gorilla-capabilitystatement-api-overlay.yaml
- group: other
  href: https://artifacts.apis.io/health-gorilla/overlays/health-gorilla-documentreference-api-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/health-gorilla-documentreference-api-overlay.yaml
- group: other
  href: https://artifacts.apis.io/health-gorilla/capabilities/health-gorilla-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/health-gorilla-capability-edges.yml
- group: agent
  href: https://artifacts.apis.io/health-gorilla/agentic-access/health-gorilla-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/health-gorilla-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/health-gorilla/security/health-gorilla-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/health-gorilla-domain-security.yml
- group: auth
  href: https://artifacts.apis.io/health-gorilla/authentication/health-gorilla-authentication.yml
  title: ''
  type: Authentication
  url: authentication/health-gorilla-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/healthgorilla
- group: company
  title: ''
  type: Website
  url: https://www.healthgorilla.com
- group: docs
  title: ''
  type: Documentation
  url: https://developer.healthgorilla.com
- group: commercial
  href: https://artifacts.apis.io/health-gorilla/plans/health-gorilla-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/health-gorilla-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/health-gorilla/rate-limits/health-gorilla-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/health-gorilla-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/health-gorilla/finops/health-gorilla-finops.yml
  title: ''
  type: FinOps
  url: finops/health-gorilla-finops.yml
- group: design
  title: ''
  type: ArazzoWorkflows
  url: ''
- group: agent
  href: https://artifacts.apis.io/health-gorilla/well-known/health-gorilla-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/health-gorilla-well-known.yml
- group: other
  href: https://artifacts.apis.io/health-gorilla/fhir/health-gorilla-fhir.yml
  title: ''
  type: CapabilityStatement
  url: fhir/health-gorilla-fhir.yml
- group: auth
  href: https://artifacts.apis.io/health-gorilla/scopes/health-gorilla-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/health-gorilla-scopes.yml
- group: design
  href: https://artifacts.apis.io/health-gorilla/conventions/health-gorilla-conventions.yml
  title: ''
  type: Conventions
  url: conventions/health-gorilla-conventions.yml
- group: design
  href: https://artifacts.apis.io/health-gorilla/conventions/health-gorilla-conventions.yml
  title: ''
  type: Idempotency
  url: conventions/health-gorilla-conventions.yml
- group: design
  href: https://artifacts.apis.io/health-gorilla/errors/health-gorilla-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/health-gorilla-problem-types.yml
- group: design
  href: https://artifacts.apis.io/health-gorilla/lifecycle/health-gorilla-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/health-gorilla-lifecycle.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://status.healthgorilla.com
- group: operate
  href: https://artifacts.apis.io/health-gorilla/changelog/health-gorilla-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/health-gorilla-changelog.yml
- group: operate
  title: ''
  type: ChangeLog
  url: https://developer.healthgorilla.com/changelog
- group: start
  href: https://artifacts.apis.io/health-gorilla/sandbox/health-gorilla-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/health-gorilla-sandbox.yml
- group: design
  href: https://artifacts.apis.io/health-gorilla/conformance/health-gorilla-conformance.yml
  title: ''
  type: Conformance
  url: conformance/health-gorilla-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: https://www.healthgorilla.com/home/company/health-data-security
- group: auth
  href: https://artifacts.apis.io/health-gorilla/security/health-gorilla-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/health-gorilla-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/health-gorilla/security/health-gorilla-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/health-gorilla-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: https://www.healthgorilla.com/home/security-txt
- group: design
  href: https://artifacts.apis.io/health-gorilla/asyncapi/health-gorilla-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/health-gorilla-webhooks.yml
- group: agent
  href: https://artifacts.apis.io/health-gorilla/llms/health-gorilla-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/health-gorilla-llms.txt
- group: agent
  href: https://artifacts.apis.io/health-gorilla/mcp/health-gorilla-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/health-gorilla-mcp.yml
- group: build
  href: https://artifacts.apis.io/health-gorilla/mcp/health-gorilla-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/health-gorilla-tool-crosswalk.yml
- group: build
  href: https://artifacts.apis.io/health-gorilla/packages/health-gorilla-packages.yml
  title: ''
  type: Packages
  url: packages/health-gorilla-packages.yml
- group: design
  href: https://artifacts.apis.io/health-gorilla/components/health-gorilla-components.yml
  title: ''
  type: Components
  url: components/health-gorilla-components.yml
- group: design
  href: https://artifacts.apis.io/health-gorilla/data-model/health-gorilla-data-model.yml
  title: ''
  type: DataModel
  url: data-model/health-gorilla-data-model.yml
- group: agent
  href: https://artifacts.apis.io/health-gorilla/skills/_index.yml
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
- has_sources: true
  method: derived
  name: Health Gorilla Finops
  primary_unit: ''
  service_category: ''
  slug: health-gorilla-finops
  template: true
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/health-gorilla.png
json_schemas:
- name: Binary
  property_count: 4
  slug: health-gorilla-binary
- name: Bundle
  property_count: 5
  slug: health-gorilla-bundle
- name: CapabilityStatement
  property_count: 4
  slug: health-gorilla-capability-statement
- name: Coverage
  property_count: 6
  slug: health-gorilla-coverage
- name: DiagnosticReport
  property_count: 9
  slug: health-gorilla-diagnostic-report
- name: DocumentReference
  property_count: 6
  slug: health-gorilla-document-reference
- name: Patient
  property_count: 8
  slug: health-gorilla-patient
- name: Practitioner
  property_count: 4
  slug: health-gorilla-practitioner
- name: RequestGroup
  property_count: 7
  slug: health-gorilla-request-group
- name: ServiceRequest
  property_count: 8
  slug: health-gorilla-service-request
jsonld:
- class_count: 11
  name: Health Gorilla Context
  property_count: 33
  slug: health-gorilla-context
layout: provider
mcp_servers:
- description: Health Gorilla serves a live remote MCP endpoint from its own developer-portal host. An agent can reach it today at https://developer.healthgorilla.com/mcp — no install step, no local process. What it
  name: Health Gorilla MCP Server
  slug: health-gorilla-docs
modified: '2026-08-14'
name: Health Gorilla
nav: Providers
network: true
overview: 'Health Gorilla publishes 10 API contracts indexed on the [APIs.io](https://apis.io/) network, including Binary API, Coverage API, DiagnosticReport API, and 7 more. Tagged areas include Health, Interoperability, FHIR, Clinical Data, and Lab Ordering.


  The Health Gorilla catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 1 Spectral governance ruleset.


  Health Gorilla''s developer surface includes pricing, authentication, documentation, changelog, sandbox, API reference, getting-started guide, and 47 more developer resources.'
plans:
- name: Health Gorilla Plans Pricing
  plan_count: 3
  slug: health-gorilla-plans-pricing
random_paper: 5
rate_limits:
- limit_count: 7
  name: Health Gorilla Rate Limits
  slug: health-gorilla-rate-limits
rules:
- authorship: generated
  effective_rule_count: 55
  extends:
  - spectral:oas
  name: Health Gorilla API Rules
  rule_count: 14
  severity_counts:
    error: 12
    hint: 0
    info: 1
    warn: 1
  slug: health-gorilla-rules
scopes:
- name: Health Gorilla Scopes
  scope_count: 11
  slug: health-gorilla-scopes
  summary_line: 11 scopes · authorizationCode/implicit/clientCredentials/jwtBearer
score:
  band: exemplar
  composite: 74.5
  coverage:
    artifact_dirs: 39
    catalog_earned: 86.8
    catalog_earned_first_party: 24.0
    catalog_gap: 28.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 2.9
  facets:
    access_clarity: 80.3
    contract_governance: 35.6
    contract_quality: 65.5
    developer_ergonomics: 69.6
    discoverability: 75.8
    operational_transparency: 84.2
  previous_composite: 71.6
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
    score: 52.3
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/health-gorilla/health-gorilla-2026-07-25T220828.png
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
skill_count: 5
skills:
- name: health-gorilla-check-coverage
  slug: health-gorilla-check-coverage
- name: health-gorilla-place-lab-order
  slug: health-gorilla-place-lab-order
- name: health-gorilla-pull-patient-record
  slug: health-gorilla-pull-patient-record
- name: health-gorilla-retrieve-lab-results
  slug: health-gorilla-retrieve-lab-results
- name: health-gorilla-subscribe-to-events
  slug: health-gorilla-subscribe-to-events
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
