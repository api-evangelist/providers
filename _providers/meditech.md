---
access_model:
  confidence: high
  label: Unknown pricing · Registration request required
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - https://ehr.meditech.com/ehr-solutions/greenfield-workspace
  - https://greenfield.meditech.com/explorer/topic/welcome
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
    rate_limit_signal: documented
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 33.1
  scored_at: '2026-09-05'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Meditech Agentic Access
  operation_count: 10
  slug: meditech-agentic-access
  summary_line: 10 operations
api_count: 1
apis:
- description: 'MEDITECH''s FHIR API surface for Expanse, exposed to approved developers through the Greenfield Workspace. US Core FHIR R4 provides view-only access to patient-facing data after the patient authorizes '
  name: MEDITECH Expanse FHIR API
  slug: meditech-api
- baseURL: https://{facility}.meditech.com/fhir/r4
  baseurl_source: declared
  description: Allergy and intolerance records
  name: meditech Allergy API
  slug: meditech-allergy-api
- baseURL: https://{facility}.meditech.com/fhir/r4
  baseurl_source: declared
  description: FHIR server capability
  name: meditech Capability API
  slug: meditech-capability-api
- baseURL: https://{facility}.meditech.com/fhir/r4
  baseurl_source: declared
  description: Problem list and diagnoses
  name: meditech Condition API
  slug: meditech-condition-api
- baseURL: https://{facility}.meditech.com/fhir/r4
  baseurl_source: declared
  description: Diagnostic reports (lab, radiology, pathology)
  name: meditech Diagnostic API
  slug: meditech-diagnostic-api
- baseURL: https://{facility}.meditech.com/fhir/r4
  baseurl_source: declared
  description: Clinical encounters and visits
  name: meditech Encounter API
  slug: meditech-encounter-api
- baseURL: https://{facility}.meditech.com/fhir/r4
  baseurl_source: declared
  description: Medication requests and prescriptions
  name: meditech Medication API
  slug: meditech-medication-api
- baseURL: https://{facility}.meditech.com/fhir/r4
  baseurl_source: declared
  description: Vital signs and laboratory results
  name: meditech Observation API
  slug: meditech-observation-api
- baseURL: https://{facility}.meditech.com/fhir/r4
  baseurl_source: declared
  description: US Core Patient resources
  name: meditech Patient API
  slug: meditech-patient-api
artifact_total: 30
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Meditech Expanse FHIR R4 Allergy API
  slug: open-meditech-allergy-api
- collection_type: open
  name: Meditech Expanse FHIR R4 Allergy Capability API
  slug: open-meditech-capability-api
- collection_type: open
  name: Meditech Expanse FHIR R4 Allergy Condition API
  slug: open-meditech-condition-api
- collection_type: open
  name: Meditech Expanse FHIR R4 Allergy Diagnostic API
  slug: open-meditech-diagnostic-api
- collection_type: open
  name: Meditech Expanse FHIR R4 Allergy Encounter API
  slug: open-meditech-encounter-api
- collection_type: open
  name: Meditech Expanse FHIR R4 API
  slug: open-meditech-fhir
- collection_type: open
  name: Meditech Expanse FHIR R4 Allergy Medication API
  slug: open-meditech-medication-api
- collection_type: open
  name: Meditech Expanse FHIR R4 Allergy Observation API
  slug: open-meditech-observation-api
- collection_type: open
  name: Meditech Expanse FHIR R4 Allergy Patient API
  slug: open-meditech-patient-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/meditech-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/meditech-domain-security.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/meditech-greenfield-conformance.yml
- group: other
  title: ''
  type: CapabilityStatement
  url: conformance/meditech-greenfield-capabilitystatement.json
- group: agent
  title: ''
  type: WellKnown
  url: well-known/meditech-greenfield-smart-configuration.json
- group: auth
  title: ''
  type: Authentication
  url: authentication/meditech-greenfield-oauth.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/meditech-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/meditech-scopes.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/meditech
- group: start
  title: ''
  type: Portal
  url: https://greenfield.meditech.com/
- group: company
  title: ''
  type: Website
  url: https://www.meditech.com/
- group: docs
  title: ''
  type: Documentation
  url: https://greenfield.meditech.com/explorer/topic/welcome
- group: docs
  title: ''
  type: APIReference
  url: https://greenfield.meditech.com/explorer/api
- group: other
  title: ''
  type: Endpoints
  url: https://greenfield.meditech.com/explorer/endpoints
- group: auth
  title: ''
  type: Scopes
  url: https://greenfield.meditech.com/explorer/scope
- group: auth
  title: ''
  type: Authentication
  url: https://greenfield.meditech.com/explorer/authorization
- group: design
  title: ''
  type: Errors
  url: https://greenfield.meditech.com/explorer/status-codes
- group: start
  title: ''
  type: SignUp
  url: https://ehr.meditech.com/ehr-solutions/greenfield-workspace
- group: start
  title: ''
  type: GettingStarted
  url: https://ehr.meditech.com/ehr-solutions/how-to-work-in-the-greenfield-workspace
- group: other
  title: ''
  type: Resources
  url: https://ehr.meditech.com/ehr-solutions/greenfield-workspace-resources
- group: other
  title: ''
  type: HL7Interfaces
  url: https://ehr.meditech.com/hl7-outbound-list-for-greenfield
- group: other
  title: ''
  type: Interoperability
  url: https://ehr.meditech.com/ehr-solutions/meditech-interoperability
- group: company
  title: ''
  type: Blog
  url: https://blog.meditech.com/
- group: operate
  title: ''
  type: Support
  url: https://ehr.meditech.com/contact
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://ehr.meditech.com/privacy-policy
- group: docs
  title: ''
  type: OpenAPI
  url: https://raw.githubusercontent.com/api-evangelist/meditech/refs/heads/main/openapi/_original/meditech-fhir-openapi.yml
- group: docs
  title: ''
  type: JSONSchema
  url: https://raw.githubusercontent.com/api-evangelist/meditech/refs/heads/main/json-schema/meditech-patient-schema.json
- group: design
  title: ''
  type: JSONLDContext
  url: https://raw.githubusercontent.com/api-evangelist/meditech/refs/heads/main/json-ld/meditech-context.jsonld
- group: build
  title: ''
  type: PostmanCollection
  url: collections/meditech-fhir.postman_collection.json
- group: build
  title: ''
  type: OpenCollection
  url: collections/meditech-fhir.opencollection.json
- group: agent
  title: ''
  type: WellKnown
  url: well-known/meditech-well-known.yml
- group: agent
  title: ''
  type: X-MCPServerCandidate
  url: mcp/meditech-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/meditech-llms.txt
- group: other
  title: ''
  type: Overlay
  url: overlays/meditech-allergy-api-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/meditech-capability-api-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/meditech-condition-api-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/meditech-diagnostic-api-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/meditech-encounter-api-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/meditech-medication-api-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/meditech-observation-api-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/meditech-patient-api-overlay.yaml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/meditech-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/meditech-lifecycle.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/meditech-changelog.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/meditech-trust-center.yml
- group: auth
  title: ''
  type: Compliance
  url: security/meditech-trust-center.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/meditech-sandbox.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/meditech-conventions.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/meditech-data-model.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/meditech-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/meditech-rate-limits.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: docs
  title: ''
  type: Documentation
  url: https://home.meditech.com/en/d/restapiresources/pages/apidoc.htm
- group: commercial
  title: ''
  type: TermsOfService
  url: https://home.meditech.com/en/d/restapiresources/pages/apiterms.htm
created: '2026-05-04'
description: MEDITECH (Medical Information Technology, Inc.) is an electronic health record vendor serving community hospitals and health systems, primarily through its MEDITECH Expanse platform. Its API program is delivered through the Greenfield Workspace — a registration-gated developer environment where approved app developers get interactive documentation and a sandbox to execute APIs against a real MEDITECH EHR. Published surfaces are US Core FHIR R4 (view-only patient-facing data, USCDI v1, DSTU2/R4 compatible) and FHIR Scheduling APIs. MEDITECH also operates Traverse Exchange, its national data exchange network and TEFCA on-ramp, connecting 700+ facilities across 41 US states plus Canadian deployments.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/meditech.png
json_schemas:
- name: Meditech FHIR R4 Patient
  property_count: 16
  slug: meditech-patient
jsonld:
- class_count: 16
  name: Meditech Context
  property_count: 6
  slug: meditech-context
layout: provider
modified: '2026-08-14'
name: MEDITECH
nav: Providers
network: true
overview: 'MEDITECH publishes 8 APIs on the [APIs.io](https://apis.io/) network, including Allergy API, Capability API, Condition API, and 5 more. Tagged areas include Company, EHR, Healthcare, FHIR, and HL7.


  The MEDITECH catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  MEDITECH''s developer surface includes authentication, developer portal, documentation, API reference, signup flow, getting-started guide, engineering blog, and 47 more developer resources.'
plans:
- name: Meditech Plans Pricing
  plan_count: 0
  slug: meditech-plans-pricing
random_paper: 16
rate_limits:
- limit_count: 0
  name: Meditech Rate Limits
  slug: meditech-rate-limits
rules:
- effective_rule_count: 6
  extends: []
  name: MEDITECH API Rules
  rule_count: 6
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 4
  slug: meditech-jsonschema-spectral-rules
scopes:
- name: Meditech Scopes
  scope_count: 0
  slug: meditech-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: developing
  composite: 47.3
  coverage:
    artifact_dirs: 27
    catalog_earned: 54.3
    catalog_earned_first_party: 0.0
    catalog_gap: 60.8
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 50.0
    commercial_clarity: 50.0
    contract_governance: 9.8
    contract_quality: 28.0
    developer_ergonomics: 57.7
    discoverability: 68.5
    governance: 9.8
    operational_transparency: 15.8
  previous_composite: 47.3
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 8
      marker_coverage: 100.0
      total: 8
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 76.3
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/meditech/refs/heads/main/screenshots/meditech-2026-06-20T185121.png
security:
- kind: authentication
  name: Meditech Authentication
  slug: meditech-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Meditech Domain Security
  slug: meditech-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Meditech Vulnerability Disclosure
  slug: meditech-vulnerability-disclosure
  summary_line: Hackerone
- kind: trust-center
  name: Meditech Trust Center
  slug: meditech-trust-center
  summary_line: ONC Health IT Certification (2015 Edition Cures Update)
slug: meditech
tags:
- Company
- EHR
- Healthcare
- FHIR
- HL7
- Interoperability
website: https://www.meditech.com/
---
