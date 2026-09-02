---
agent_readiness:
  band: agent-native
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
    error_semantics: verified
    event_surface_described: false
    idempotency: documented
    mcp_server: false
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 38.7
  scored_at: '2026-09-01'
agentic_access:
- acting_count: 19
  human_in_the_loop: 0
  name: Advancedmd Agentic Access
  operation_count: 81
  slug: advancedmd-agentic-access
  summary_line: 81 operations · 19 acting
api_count: 3
apis:
- description: Developer-portal helper API that mints JWT client assertions for testing the FHIR Bulk Data workflow. Documented as POST /v1/fhir-jwks/token with a grant_type=client_credentials&alg=rsa body, authoriz
  name: AdvancedMD FHIR Bulk JWKS API
  slug: advancedmd-fhir-bulk-jwks-api
- description: 'Public, unauthenticated service base URL publication required of ONC-certified API suppliers. GET https://providerapi.advancedmd.com/v1/r4/endpoints returns a FHIR Bundle of Endpoint and Organization '
  name: AdvancedMD FHIR Endpoint Directory
  slug: advancedmd-fhir-endpoint-directory
- description: AdvancedMD's proprietary partner API family, published in both XML-RPC and REST formats, which lets developers build companion applications that replicate functionality available in the AdvancedMD use
  name: AdvancedMD Connect APIs
  slug: advancedmd-connect-apis
- description: The AllergyIntolerance API from AdvancedMD — 3 operation(s) for allergyintolerance.
  name: AdvancedMD Allergy Intolerance API
  slug: advancedmd-allergyintolerance-api
- description: The Authentication API from AdvancedMD — 1 operation(s) for authentication.
  name: AdvancedMD Authentication API
  slug: advancedmd-authentication-api
- description: The C-CDA API from AdvancedMD — 1 operation(s) for c-cda.
  name: AdvancedMD C CDA API
  slug: advancedmd-c-cda-api
- description: The Cancel Bulk Data Export API from AdvancedMD — 1 operation(s) for cancel bulk data export.
  name: AdvancedMD Cancel Bulk Data Export API
  slug: advancedmd-cancel-bulk-data-export-api
- description: The CarePlan API from AdvancedMD — 3 operation(s) for careplan.
  name: AdvancedMD Care Plan API
  slug: advancedmd-careplan-api
- description: The CareTeam API from AdvancedMD — 3 operation(s) for careteam.
  name: AdvancedMD Care Team API
  slug: advancedmd-careteam-api
- description: The Check Data Export Status API from AdvancedMD — 1 operation(s) for check data export status.
  name: AdvancedMD Check Data Export Status API
  slug: advancedmd-check-data-export-status-api
- description: The Clinical API from AdvancedMD — 15 operation(s) for clinical.
  name: AdvancedMD Clinical API
  slug: advancedmd-clinical-api
- description: The Condition API from AdvancedMD — 3 operation(s) for condition.
  name: AdvancedMD Condition API
  slug: advancedmd-condition-api
- description: The Coverage API from AdvancedMD — 3 operation(s) for coverage.
  name: AdvancedMD Coverage API
  slug: advancedmd-coverage-api
- description: The Device API from AdvancedMD — 3 operation(s) for device.
  name: AdvancedMD Device API
  slug: advancedmd-device-api
- description: The DiagnosticReport API from AdvancedMD — 3 operation(s) for diagnosticreport.
  name: AdvancedMD Diagnostic Report API
  slug: advancedmd-diagnosticreport-api
- description: The DocumentReference API from AdvancedMD — 4 operation(s) for documentreference.
  name: AdvancedMD Document Reference API
  slug: advancedmd-documentreference-api
- description: The Encounter API from AdvancedMD — 2 operation(s) for encounter.
  name: AdvancedMD Encounter API
  slug: advancedmd-encounter-api
- description: The Get FHIR Entity API from AdvancedMD — 1 operation(s) for get fhir entity.
  name: AdvancedMD Get FHIR Entity API
  slug: advancedmd-get-fhir-entity-api
- description: The Goal API from AdvancedMD — 3 operation(s) for goal.
  name: AdvancedMD Goal API
  slug: advancedmd-goal-api
- description: The Immunization API from AdvancedMD — 3 operation(s) for immunization.
  name: AdvancedMD Immunization API
  slug: advancedmd-immunization-api
- description: The Location API from AdvancedMD — 2 operation(s) for location.
  name: AdvancedMD Location API
  slug: advancedmd-location-api
- description: The MedicationDispense API from AdvancedMD — 3 operation(s) for medicationdispense.
  name: AdvancedMD Medication Dispense API
  slug: advancedmd-medicationdispense-api
- description: The MedicationRequest API from AdvancedMD — 3 operation(s) for medicationrequest.
  name: AdvancedMD Medication Request API
  slug: advancedmd-medicationrequest-api
- description: The Observation API from AdvancedMD — 3 operation(s) for observation.
  name: AdvancedMD Observation API
  slug: advancedmd-observation-api
- description: The Obtain Access Token API from AdvancedMD — 1 operation(s) for obtain access token.
  name: AdvancedMD Obtain Access Token API
  slug: advancedmd-obtain-access-token-api
- description: The Organization API from AdvancedMD — 2 operation(s) for organization.
  name: AdvancedMD Organization API
  slug: advancedmd-organization-api
- description: The Patient API from AdvancedMD — 3 operation(s) for patient.
  name: AdvancedMD Patient API
  slug: advancedmd-patient-api
- description: The Patient Demographics API from AdvancedMD — 1 operation(s) for patient demographics.
  name: AdvancedMD Patient Demographics API
  slug: advancedmd-patient-demographics-api
- description: The Practitioner API from AdvancedMD — 2 operation(s) for practitioner.
  name: AdvancedMD Practitioner API
  slug: advancedmd-practitioner-api
- description: The Procedure API from AdvancedMD — 3 operation(s) for procedure.
  name: AdvancedMD Procedure API
  slug: advancedmd-procedure-api
- description: The Provenance API from AdvancedMD — 1 operation(s) for provenance.
  name: AdvancedMD Provenance API
  slug: advancedmd-provenance-api
- description: The RelatedPerson API from AdvancedMD — 3 operation(s) for relatedperson.
  name: AdvancedMD Related Person API
  slug: advancedmd-relatedperson-api
- description: The Start Bulk Data Export API from AdvancedMD — 1 operation(s) for start bulk data export.
  name: AdvancedMD Start Bulk Data Export API
  slug: advancedmd-start-bulk-data-export-api
artifact_total: 43
collections:
- collection_type: open
  name: AdvancedMD Application Access APIs
  slug: open-advancedmd-application-access-apis-swagger
- collection_type: open
  name: FHIR Bulk API
  slug: open-advancedmd-fhir-bulk-api
- collection_type: open
  name: FHIR Single API - US Core 6.1.0
  slug: open-advancedmd-fhir-single-api
common:
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/advancedmd-capability-edges.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/advancedmd-fhir-single-api-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/advancedmd-fhir-bulk-api-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/advancedmd-application-access-apis-overlay.yaml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/advancedmd-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/advancedmd-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/advancedmd-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://www.advancedmd.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://fhir.advancedmd.com/
- group: start
  title: ''
  type: Portal
  url: https://developer.advancedmd.com/
- group: docs
  title: ''
  type: Documentation
  url: https://www.advancedmd.com/group-practice/developer-solutions/
- group: docs
  title: ''
  type: APIReference
  url: https://fhir.advancedmd.com/fhir/apis
- group: start
  title: ''
  type: GettingStarted
  url: https://fhir.advancedmd.com/getting-started
- group: auth
  title: ''
  type: Authentication
  url: https://fhir.advancedmd.com/fhir/launch-and-authorization
- group: other
  title: ''
  type: CapabilityStatement
  url: fhir/advancedmd-fhir-r4-capabilitystatement.json
- group: other
  title: ''
  type: SMARTConfiguration
  url: fhir/advancedmd-smart-configuration.json
- group: other
  title: ''
  type: OpenIDConfiguration
  url: fhir/advancedmd-openid-configuration.json
- group: operate
  title: ''
  type: FAQ
  url: https://fhir.advancedmd.com/faq-s
- group: start
  title: ''
  type: SignUp
  url: https://www.advancedmd.com/api-connection-request/
- group: start
  title: ''
  type: Login
  url: https://login.advancedmd.com/
- group: operate
  title: ''
  type: Support
  url: https://www.advancedmd.com/support/interoperability/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.advancedmd.com/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.advancedmd.com/software-pricing/
- group: company
  title: ''
  type: Blog
  url: https://www.advancedmd.com/blog/
- group: company
  title: ''
  type: BlogRSS
  url: https://www.advancedmd.com/blog/feed/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/AdvancedMD
- group: commercial
  title: ''
  type: TermsOfService
  url: https://fhir.advancedmd.com/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.advancedmd.com/privacy-notice/
- group: auth
  title: ''
  type: Security
  url: https://www.advancedmd.com/medical-office-software/security/
- group: operate
  title: ''
  type: HelpCenter
  url: https://www.advancedmd.com/support/
- group: auth
  title: ''
  type: Compliance
  url: https://www.advancedmd.com/ai-information
- group: design
  title: ''
  type: Conformance
  url: conformance/advancedmd-conformance.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/advancedmd-scopes.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/advancedmd-conventions.yml
- group: design
  title: ''
  type: Idempotency
  url: conventions/advancedmd-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/advancedmd-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/advancedmd-lifecycle.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/advancedmd-rate-limits.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/advancedmd-plans-pricing.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/advancedmd-sandbox.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/advancedmd-data-model.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/advancedmd-well-known.yml
- group: other
  title: ''
  type: JSONWebKeySet
  url: well-known/advancedmd-jwks.json
- group: build
  title: ''
  type: Packages
  url: packages/advancedmd-packages.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/advancedmd-llms.txt
- group: agent
  title: ''
  type: MCPServer
  url: mcp/advancedmd-mcp.yml
- group: build
  title: ''
  type: ToolCrosswalk
  url: mcp/advancedmd-tool-crosswalk.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-07-27'
description: AdvancedMD is a cloud practice-management, medical-billing and electronic health record (EHR) software company founded in 1999 and headquartered in South Jordan, Utah, serving independent ambulatory practices, mental-health and physical-medicine clinics, med spas and medical-billing services across the United States. A standalone company again since Francisco Partners acquired it from Global Payments in December 2024, AdvancedMD operates two clearly separated developer surfaces. The first is a public, no-cost HL7 FHIR R4 (4.0.1) read-only API estate published for ONC (g)(10) Cures Act certification at fhir.advancedmd.com, aligned to the US Core 6.1.0 Implementation Guide, authorized with SMART-on-FHIR OAuth 2.0 and covering both single-patient access and FHIR Bulk Data Access group export. The second is a gated proprietary Connect API estate (REST and XML-RPC) plus an ODBC data-access driver, which require a signed Certified API Developer Agreement with licensing and support
  fees before sandbox or production credentials are issued.
image: https://www.advancedmd.com/wp-content/uploads/2025/06/cropped-bird_solid_5121-300x300.png
layout: provider
mcp_servers:
- description: Candidate MCP tool surface for AdvancedMD, one tool per published REST operation across the FHIR Single API, the FHIR Bulk Data API and the legacy Application Access APIs. AdvancedMD publishes no host
  name: AdvancedMD MCP Server
  slug: advancedmd-mcp-server
modified: '2026-08-15'
name: AdvancedMD
nav: Providers
network: true
overview: 'AdvancedMD publishes 30 APIs on the [APIs.io](https://apis.io/) network, including Allergy Intolerance API, Authentication API, C CDA API, and 27 more. Tagged areas include Healthcare, United States, EHR, EMR, and Practice Management.


  AdvancedMD''s developer surface includes authentication, developer portal, documentation, API reference, getting-started guide, FAQ, signup flow, and 41 more developer resources.'
plans:
- name: Advancedmd Plans Pricing
  plan_count: 6
  slug: advancedmd-plans-pricing
random_paper: 2
rate_limits:
- limit_count: 0
  name: Advancedmd Rate Limits
  slug: advancedmd-rate-limits
scopes:
- name: Advancedmd Scopes
  scope_count: 128
  slug: advancedmd-scopes
  summary_line: 128 scopes · authorizationCode/clientCredentials
score:
  band: strong
  composite: 54.3
  coverage:
    artifact_dirs: 24
    catalog_gap: 76.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 73.7
    commercial_clarity: 73.7
    contract_governance: 18.2
    contract_quality: 50.0
    developer_ergonomics: 32.7
    discoverability: 57.4
    governance: 18.2
    operational_transparency: 28.9
  previous_composite: 54.3
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 30
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    jurisdictions:
    - jurisdiction: US
      standard: hipaa
    jurisdictions_satisfied: 1
    matched_via: tags
    regime: Health
    regime_id: health
    score: 77.5
  schema_version: 0.18.0
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/advancedmd/refs/heads/main/screenshots/advancedmd-2026-08-07T160939.png
security:
- kind: authentication
  name: Advancedmd Authentication
  slug: advancedmd-authentication
  summary_line: oauth2/openIdConnect/apiKey/http · 7 schemes
- kind: domain-security
  name: Advancedmd Domain Security
  slug: advancedmd-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: advancedmd
tags:
- Healthcare
- United States
- EHR
- EMR
- Practice Management
- Medical Billing
- FHIR
- HL7
- SMART on FHIR
- US Core
- Interoperability
- Revenue Cycle Management
- Scheduling
website: https://www.advancedmd.com/
---
