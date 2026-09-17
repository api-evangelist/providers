---
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 39.7
  scored_at: '2026-09-16'
api_count: 38
apis:
- description: HL7 FHIR R4 (4.0.1) server exposing Cambio COSMIC clinical data through 24 FHIR resource types — Patient, Practitioner, Organization, Encounter, Condition, Observation, MedicationRequest, MedicationDi
  name: Cambio Open Services FHIR R4 API
  slug: cambio-healthcare-systems-fhir-r4
- baseURL: https://api.openservices.cambio.se/api/open/attentionsignals
  baseurl_source: declared
  description: The Booked Appointments API from Cambio Healthcare Systems — 1 operation(s) for booked appointments.
  name: Cambio Healthcare Systems Booked Appointments API
  slug: cambio-healthcare-systems-booked-appointments-api
- baseURL: https://api.openservices.cambio.se/api/open/attentionsignals
  baseurl_source: declared
  description: The * API from Cambio Healthcare Systems — 1 operation(s) for *.
  name: Cambio Healthcare Systems * API
  slug: cambio-healthcare-systems-default-api
- baseURL: https://api.openservices.cambio.se/api/open/attentionsignals
  baseurl_source: declared
  description: The Payment Notice API from Cambio Healthcare Systems — 1 operation(s) for payment notice.
  name: Cambio Healthcare Systems Payment Notice API
  slug: cambio-healthcare-systems-payment-notice-api
- baseURL: https://api.openservices.cambio.se/api/open/attentionsignals
  baseurl_source: declared
  description: The Protocol API from Cambio Healthcare Systems — 2 operation(s) for protocol.
  name: Cambio Healthcare Systems Protocol API
  slug: cambio-healthcare-systems-protocol-api
- baseURL: https://api.openservices.cambio.se/api/open/attentionsignals
  baseurl_source: declared
  description: The .well Known API from Cambio Healthcare Systems — 1 operation(s) for .well known.
  name: Cambio Healthcare Systems .well Known API
  slug: cambio-healthcare-systems-well-known-api
artifact_total: 11
common:
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/cambio-healthcare-systems/refs/heads/main/overlays/cambio-healthcare-systems-attention-signal-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/cambio-healthcare-systems-attention-signal-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/cambio-healthcare-systems/refs/heads/main/overlays/cambio-healthcare-systems-authorizer-openid-connect-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/cambio-healthcare-systems-authorizer-openid-connect-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/cambio-healthcare-systems/refs/heads/main/overlays/cambio-healthcare-systems-booked-appointments-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/cambio-healthcare-systems-booked-appointments-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/cambio-healthcare-systems/refs/heads/main/overlays/cambio-healthcare-systems-care-contacts-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/cambio-healthcare-systems-care-contacts-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/cambio-healthcare-systems/refs/heads/main/overlays/cambio-healthcare-systems-care-contacts-v2-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/cambio-healthcare-systems-care-contacts-v2-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/cambio-healthcare-systems/refs/heads/main/overlays/cambio-healthcare-systems-chemistry-lab-results-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/cambio-healthcare-systems-chemistry-lab-results-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/cambio-healthcare-systems/refs/heads/main/overlays/cambio-healthcare-systems-chemistry-lab-results-v2-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/cambio-healthcare-systems-chemistry-lab-results-v2-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/cambio-healthcare-systems/refs/heads/main/overlays/cambio-healthcare-systems-diagnosis-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/cambio-healthcare-systems-diagnosis-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/cambio-healthcare-systems/refs/heads/main/overlays/cambio-healthcare-systems-diagnosis-v2-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/cambio-healthcare-systems-diagnosis-v2-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/cambio-healthcare-systems/refs/heads/main/overlays/cambio-healthcare-systems-fhir-r4-public-profiles-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/cambio-healthcare-systems-fhir-r4-public-profiles-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/cambio-healthcare-systems/refs/heads/main/overlays/cambio-healthcare-systems-journal-notes-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/cambio-healthcare-systems-journal-notes-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/cambio-healthcare-systems/refs/heads/main/overlays/cambio-healthcare-systems-journal-notes-v2-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/cambio-healthcare-systems-journal-notes-v2-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/cambio-healthcare-systems/refs/heads/main/overlays/cambio-healthcare-systems-medication-prescriptions-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/cambio-healthcare-systems-medication-prescriptions-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/cambio-healthcare-systems/refs/heads/main/overlays/cambio-healthcare-systems-medication-prescriptions-v2-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/cambio-healthcare-systems-medication-prescriptions-v2-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/cambio-healthcare-systems/refs/heads/main/overlays/cambio-healthcare-systems-patient-information-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/cambio-healthcare-systems-patient-information-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/cambio-healthcare-systems/refs/heads/main/overlays/cambio-healthcare-systems-patient-information-v2-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/cambio-healthcare-systems-patient-information-v2-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/cambio-healthcare-systems/refs/heads/main/overlays/cambio-healthcare-systems-payment-notice-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/cambio-healthcare-systems-payment-notice-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/cambio-healthcare-systems/refs/heads/main/overlays/cambio-healthcare-systems-referral-requests-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/cambio-healthcare-systems-referral-requests-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/cambio-healthcare-systems/refs/heads/main/overlays/cambio-healthcare-systems-video-meetings-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/cambio-healthcare-systems-video-meetings-overlay.yaml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/cambio-healthcare-systems/refs/heads/main/security/cambio-healthcare-systems-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/cambio-healthcare-systems-domain-security.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/cambio-healthcare-systems/refs/heads/main/authentication/cambio-healthcare-systems-authentication.yml
  title: ''
  type: Authentication
  url: authentication/cambio-healthcare-systems-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://www.cambiogroup.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.openservices.cambio.se/
- group: docs
  title: ''
  type: Documentation
  url: https://developer.openservices.cambio.se/getting-started
- group: docs
  title: ''
  type: APIReference
  url: https://developer.openservices.cambio.se/apis
- group: start
  title: ''
  type: GettingStarted
  url: https://developer.openservices.cambio.se/getting-started
- group: start
  title: ''
  type: SignUp
  url: https://developer.openservices.cambio.se/signup
- group: start
  title: ''
  type: Login
  url: https://developer.openservices.cambio.se/signin
- group: operate
  title: ''
  type: Support
  url: https://developer.openservices.cambio.se/help
- group: company
  title: ''
  type: Blog
  url: https://www.cambiogroup.com/news/
- group: company
  title: ''
  type: BlogRSS
  url: https://www.cambiogroup.com/feed/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.cambiogroup.com/about-us/privacy-policy/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/CambioHealthcare
- group: auth
  title: ''
  type: Compliance
  url: https://www.cambiogroup.com/compliance-eng/
- group: operate
  title: ''
  type: ChangeLog
  url: https://developer.openservices.cambio.se/api-changelog
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/cambio-healthcare-systems/refs/heads/main/scopes/cambio-healthcare-systems-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/cambio-healthcare-systems-scopes.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/cambio-healthcare-systems/refs/heads/main/well-known/cambio-healthcare-systems-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/cambio-healthcare-systems-well-known.yml
- group: other
  title: ''
  type: OpenIDConnect
  url: https://api.openservices.cambio.se/auth/realms/COS/.well-known/openid-configuration
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/cambio-healthcare-systems/refs/heads/main/errors/cambio-healthcare-systems-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/cambio-healthcare-systems-problem-types.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/cambio-healthcare-systems/refs/heads/main/lifecycle/cambio-healthcare-systems-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/cambio-healthcare-systems-lifecycle.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/cambio-healthcare-systems/refs/heads/main/lifecycle/cambio-healthcare-systems-lifecycle.yml
  title: ''
  type: Deprecation
  url: lifecycle/cambio-healthcare-systems-lifecycle.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/cambio-healthcare-systems/refs/heads/main/conventions/cambio-healthcare-systems-conventions.yml
  title: ''
  type: Conventions
  url: conventions/cambio-healthcare-systems-conventions.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/cambio-healthcare-systems/refs/heads/main/conformance/cambio-healthcare-systems-conformance.yml
  title: ''
  type: Conformance
  url: conformance/cambio-healthcare-systems-conformance.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/cambio-healthcare-systems/refs/heads/main/packages/cambio-healthcare-systems-packages.yml
  title: ''
  type: Packages
  url: packages/cambio-healthcare-systems-packages.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/cambio-healthcare-systems/refs/heads/main/mcp/cambio-healthcare-systems-mcp.yml
  title: ''
  type: X-MCPServerCandidate
  url: mcp/cambio-healthcare-systems-mcp.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/cambio-healthcare-systems/refs/heads/main/llms/cambio-healthcare-systems-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/cambio-healthcare-systems-llms.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/cambio-healthcare-systems/refs/heads/main/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/cambio-healthcare-systems/refs/heads/main/data-model/cambio-healthcare-systems-data-model.yml
  title: ''
  type: DataModel
  url: data-model/cambio-healthcare-systems-data-model.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/cambio-healthcare-systems/refs/heads/main/examples/cambio-healthcare-systems-examples.yml
  title: ''
  type: Examples
  url: examples/cambio-healthcare-systems-examples.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/cambio-healthcare-systems/refs/heads/main/plans/cambio-healthcare-systems-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/cambio-healthcare-systems-plans-pricing.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/cambio-healthcare-systems/refs/heads/main/rate-limits/cambio-healthcare-systems-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/cambio-healthcare-systems-rate-limits.yml
- group: start
  href: https://raw.githubusercontent.com/api-evangelist/cambio-healthcare-systems/refs/heads/main/sandbox/cambio-healthcare-systems-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/cambio-healthcare-systems-sandbox.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/cambio-healthcare-systems/refs/heads/main/changelog/cambio-healthcare-systems-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/cambio-healthcare-systems-changelog.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/cambio-healthcare-systems/refs/heads/main/fhir/cambio-healthcare-systems-fhir.yml
  title: ''
  type: CapabilityStatement
  url: fhir/cambio-healthcare-systems-fhir.yml
- group: build
  title: ''
  type: SourceCode
  url: https://github.com/CambioHealthcare/cp-nordic-hackathon-2025
created: '2026-09-02'
description: Cambio Healthcare Systems is a Swedish health-IT company founded in 1993 in Linkoping and headquartered in Stockholm, best known for Cambio COSMIC, an electronic health record and clinical decision support platform used across Swedish regions, Denmark and the United Kingdom by well over 100,000 clinical users. Cambio runs a public developer programme, Cambio Open Services (COS), which publishes 19 REST APIs and an HL7 FHIR R4 server on Azure API Management at api.openservices.cambio.se, together with a published FHIR Implementation Guide of COSMIC-specific profiles, a Keycloak OpenID Connect authorization server with SMART-on-FHIR style scopes, and a synthetic-data sandbox. COSMIC and its clinical decision support are CE-marked and MDR-certified (notified body BSI-2797), and the company holds ISO 9001, 13485, 14001, 20000 and 27001 certifications.
image: https://www.cambiogroup.com/wp-content/uploads/2021/03/cropped-Cambio-C-560x560px-270x270.png
layout: provider
modified: '2026-09-02'
name: Cambio Healthcare Systems
nav: Providers
network: true
overview: 'Cambio Healthcare Systems publishes 5 APIs on the [APIs.io](https://apis.io/) network, including Booked Appointments API, * API, Payment Notice API, and 2 more. Tagged areas include Healthcare, Electronic Health Records, EHR, Clinical Decision Support, and FHIR.


  Cambio Healthcare Systems'' developer surface includes authentication, documentation, API reference, getting-started guide, signup flow, support, engineering blog, and 48 more developer resources.'
plans:
- name: Cambio Healthcare Systems Plans Pricing
  plan_count: 0
  slug: cambio-healthcare-systems-plans-pricing
random_paper: 12
rate_limits:
- limit_count: 0
  name: Cambio Healthcare Systems Rate Limits
  slug: cambio-healthcare-systems-rate-limits
scopes:
- name: Cambio Healthcare Systems Scopes
  scope_count: 0
  slug: cambio-healthcare-systems-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: developing
  composite: 54.2
  coverage:
    artifact_dirs: 22
    catalog_earned: 40.0
    catalog_earned_first_party: 0.0
    catalog_gap: 75.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -0.5
  facets:
    access_clarity: 31.6
    contract_governance: 18.2
    contract_quality: 57.2
    developer_ergonomics: 66.1
    discoverability: 81.5
    operational_transparency: 26.3
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - sweden
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - europe
    - nordics
  previous_composite: 54.7
  provenance:
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 5
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 67.5
  schema_version: 0.22.0
  scored_at: '2026-09-16'
  trend: flat
  upsert:
    applies: true
    score: 0.0
security:
- kind: authentication
  name: Cambio Healthcare Systems Authentication
  slug: cambio-healthcare-systems-authentication
  summary_line: apiKey/oauth2/openIdConnect · 4 schemes
- kind: domain-security
  name: Cambio Healthcare Systems Domain Security
  slug: cambio-healthcare-systems-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: cambio-healthcare-systems
tags:
- Healthcare
- Electronic Health Records
- EHR
- Clinical Decision Support
- FHIR
- HL7
- Interoperability
- Health IT
- Sweden
- Nordic
- Patient Data
- Medical Records
- openEHR
- SMART on FHIR
- Company
website: https://www.cambiogroup.com/
---
