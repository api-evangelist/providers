---
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
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 30.0
  scored_at: '2026-09-01'
agentic_access:
- acting_count: 8
  human_in_the_loop: 0
  name: Emis Health Agentic Access
  operation_count: 80
  slug: emis-health-agentic-access
  summary_line: 80 operations · 8 acting
api_count: 1
apis:
- description: EMIS-X App Launch lets partner applications be launched in-context from within the EMIS-X / EMIS Web clinical workflow, passing an authenticated user and patient context to the integrating application
  name: EMIS-X App Launch
  slug: emis-x-app-launch
- description: EMIS-X Analytics provides partner access to an EMIS-X data warehouse with modelled datasets across domains including Community Pharmacy, Incremental Primary Care Views (iPCVs), OpenSAFELY, Recruit, an
  name: EMIS-X Analytics
  slug: emis-x-analytics
- description: The appointments API from EMIS Health — 17 operation(s) for appointments.
  name: EMIS Health Appointments API
  slug: emis-health-appointments-api
- description: The CORS API from EMIS Health — 40 operation(s) for cors.
  name: EMIS Health CORS API
  slug: emis-health-cors-api
- description: The health API from EMIS Health — 1 operation(s) for health.
  name: EMIS Health Health API
  slug: emis-health-health-api
- description: The medicalRecord API from EMIS Health — 12 operation(s) for medicalrecord.
  name: EMIS Health Medical Record API
  slug: emis-health-medicalrecord-api
- description: The organisation API from EMIS Health — 2 operation(s) for organisation.
  name: EMIS Health Organisation API
  slug: emis-health-organisation-api
- description: The patient API from EMIS Health — 1 operation(s) for patient.
  name: EMIS Health Patient API
  slug: emis-health-patient-api
- description: The patientMatching API from EMIS Health — 4 operation(s) for patientmatching.
  name: EMIS Health Patient Matching API
  slug: emis-health-patientmatching-api
- description: The search API from EMIS Health — 1 operation(s) for search.
  name: EMIS Health Search API
  slug: emis-health-search-api
- description: The swagger API from EMIS Health — 1 operation(s) for swagger.
  name: EMIS Health Swagger API
  slug: emis-health-swagger-api
- description: The user API from EMIS Health — 1 operation(s) for user.
  name: EMIS Health User API
  slug: emis-health-user-api
artifact_total: 18
collections:
- collection_type: open
  name: Partner API
  slug: open-emis-health-partner-api
common:
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/emis-health-capability-edges.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/emis-health-partner-api-overlay.yaml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/emis-health-mcp.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/emis-health-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/emis-health-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/emis-health-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/emis-health-scopes.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/emis-health-well-known.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/emis-health-conventions.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/emis-health-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/emis-health-conformance.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/emis-health-sandbox.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/emis-health-llms.txt
- group: company
  title: ''
  type: Website
  url: https://www.emishealth.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.partner.emis-x.uk/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.partner.emis-x.uk/getting-started/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.partner.emis-x.uk/openapi/papi
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.partner.emis-x.uk/getting-started/
- group: start
  title: ''
  type: Onboarding
  url: https://docs.partner.emis-x.uk/onboarding-one/
- group: auth
  title: ''
  type: Authentication
  url: https://docs.partner.emis-x.uk/auth/
- group: other
  title: ''
  type: OpenIDConfiguration
  url: https://identity.stg.emis-x.uk/b205162c-c95a-4639-8076-bb1fcb152d2b/b2c_1a_clientcredentials/.well-known/openid-configuration
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.emishealth.com/privacy-policy
created: '2026-07-24'
description: EMIS Health is a United Kingdom health-technology company and one of the two dominant GP clinical-system providers in the NHS (alongside TPP SystmOne), supplying the EMIS Web electronic patient record used across primary care, community pharmacy, and other care settings. EMIS is migrating from EMIS Web to EMIS-X, a cloud-first platform, and exposes third-party integration through the EMIS Partner Developer Portal at docs.partner.emis-x.uk. The gated partner programme documents a RESTful JSON Partner API (PAPI) covering appointments, the clinical/medical record, patient demographics and matching, organisation lookup and clinical searches, plus EMIS-X App Launch and an EMIS-X Analytics data warehouse. Authentication is OAuth2 / OIDC (Microsoft Entra External ID / Azure AD B2C) using authorization-code, PKCE, and client-credentials flows with scoped JWT access tokens; native HL7 FHIR resource support is documented as upcoming rather than yet available.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/apis-json-logo.jpg
layout: provider
mcp_servers:
- description: ''
  name: EMIS Health MCP Server
  slug: emis-health-mcp-server
modified: '2026-07-24'
name: EMIS Health
nav: Providers
network: true
overview: 'EMIS Health publishes 10 APIs on the [APIs.io](https://apis.io/) network, including Appointments API, CORS API, Health API, and 7 more. Tagged areas include Healthcare, United Kingdom, EHR, EMR, and Interoperability.


  EMIS Health''s developer surface includes authentication, sandbox, documentation, API reference, getting-started guide, and 18 more developer resources.'
random_paper: 13
scopes:
- name: Emis Health Scopes
  scope_count: 7
  slug: emis-health-scopes
  summary_line: 7 scopes · authorizationCode
score:
  band: thin
  composite: 37.5
  coverage:
    artifact_dirs: 19
    catalog_gap: 83.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 10.5
    commercial_clarity: 10.5
    contract_governance: 4.5
    contract_quality: 43.9
    developer_ergonomics: 58.9
    discoverability: 66.7
    governance: 4.5
    operational_transparency: 0.0
  previous_composite: 37.5
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 10
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 55.0
  schema_version: 0.18.0
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/emis-health/refs/heads/main/screenshots/emis-health-2026-07-25T213240.png
security:
- kind: authentication
  name: Emis Health Authentication
  slug: emis-health-authentication
  summary_line: http/oauth2/openIdConnect · 2 schemes
- kind: domain-security
  name: Emis Health Domain Security
  slug: emis-health-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: emis-health
tags:
- Healthcare
- United Kingdom
- EHR
- EMR
- Interoperability
- HL7
- FHIR
- Primary Care
- NHS
- Clinical Data
- Electronic Patient Record
website: https://www.emishealth.com/
---
