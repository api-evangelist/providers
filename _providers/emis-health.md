---
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.2
  score: 39.4
  scored_at: '2026-08-06'
agentic_access:
- acting_count: 8
  human_in_the_loop: 0
  name: Emis Health Agentic Access
  operation_count: 80
  slug: emis-health-agentic-access
  summary_line: 80 operations · 8 acting
api_count: 3
apis:
- description: The EMIS Partner API (PAPI) is a RESTful JSON API for EMIS-X / EMIS Web integration, exposing appointments, the clinical/medical record, patient demographics, patient matching, organisation lookup, an
  name: EMIS Partner API (PAPI)
  slug: emis-partner-api
- description: EMIS-X App Launch lets partner applications be launched in-context from within the EMIS-X / EMIS Web clinical workflow, passing an authenticated user and patient context to the integrating application
  name: EMIS-X App Launch
  slug: emis-x-app-launch
- description: EMIS-X Analytics provides partner access to an EMIS-X data warehouse with modelled datasets across domains including Community Pharmacy, Incremental Primary Care Views (iPCVs), OpenSAFELY, Recruit, an
  name: EMIS-X Analytics
  slug: emis-x-analytics
artifact_total: 7
common:
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
modified: '2026-07-24'
name: EMIS Health
nav: Providers
network: true
overview: 'EMIS Health publishes 1 API on the [APIs.io](https://apis.io/) network: EMIS Partner API (PAPI). Tagged areas include Healthcare, United Kingdom, EHR, EMR, and Interoperability.


  EMIS Health''s developer surface includes authentication, sandbox, documentation, API reference, getting-started guide, and 15 more developer resources.'
random_paper: 88
scopes:
- name: Emis Health Scopes
  scope_count: 7
  slug: emis-health-scopes
  summary_line: 7 scopes · authorizationCode
score:
  band: thin
  composite: 36.7
  delta: 0.0
  facets:
    commercial_clarity: 10.5
    contract_quality: 43.4
    developer_ergonomics: 53.8
    discoverability: 83.3
    governance: 11.5
    operational_transparency: 0.0
  previous_composite: 36.7
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 1
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 55.0
  schema_version: 0.9.1
  scored_at: '2026-08-06'
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
