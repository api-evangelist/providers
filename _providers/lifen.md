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
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: true
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 39.4
  scored_at: '2026-09-21'
api_count: 2
apis:
- baseURL: https://api.lifen.fr/fhir/v3
  baseurl_source: declared
  description: The CommunicationRequest API from Lifen — 3 operation(s) for communicationrequest.
  name: Lifen CommunicationRequest API
  slug: lifen-communicationrequest-api
- baseURL: https://api.lifen.fr/fhir/v3
  baseurl_source: declared
  description: The Coverage API from Lifen — 1 operation(s) for coverage.
  name: Lifen Coverage API
  slug: lifen-coverage-api
- baseURL: https://api.lifen.fr/fhir/v3
  baseurl_source: declared
  description: The Encounter API from Lifen — 2 operation(s) for encounter.
  name: Lifen Encounter API
  slug: lifen-encounter-api
- baseURL: https://api.lifen.fr/fhir/v3
  baseurl_source: declared
  description: The Organization API from Lifen — 1 operation(s) for organization.
  name: Lifen Organization API
  slug: lifen-organization-api
- baseURL: https://api.lifen.fr/fhir/v3
  baseurl_source: declared
  description: The Patient API from Lifen — 2 operation(s) for patient.
  name: Lifen Patient API
  slug: lifen-patient-api
- baseURL: https://api.lifen.fr/fhir/v3
  baseurl_source: declared
  description: The Practitioner API from Lifen — 1 operation(s) for practitioner.
  name: Lifen Practitioner API
  slug: lifen-practitioner-api
- baseURL: https://api.lifen.fr/fhir/v3
  baseurl_source: declared
  description: The Token API from Lifen — 1 operation(s) for token.
  name: Lifen Token API
  slug: lifen-token-api
artifact_total: 27
asyncapis:
- description: ''
  name: Lifen Platform Webhooks
  slug: lifen-platform-webhooks
collections:
- collection_type: postman
  name: lifen-authentication-api CommunicationRequest API
  slug: postman-lifen-communicationrequest-api
- collection_type: postman
  name: lifen-authentication-api CommunicationRequest Coverage API
  slug: postman-lifen-coverage-api
- collection_type: postman
  name: lifen-authentication-api CommunicationRequest Encounter API
  slug: postman-lifen-encounter-api
- collection_type: postman
  name: lifen-authentication-api CommunicationRequest Organization API
  slug: postman-lifen-organization-api
- collection_type: postman
  name: lifen-authentication-api CommunicationRequest Patient API
  slug: postman-lifen-patient-api
- collection_type: postman
  name: lifen-authentication-api CommunicationRequest Practitioner API
  slug: postman-lifen-practitioner-api
- collection_type: postman
  name: lifen-authentication-api CommunicationRequest Token API
  slug: postman-lifen-token-api
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: lifen-authentication-api CommunicationRequest API
  slug: open-lifen-communicationrequest-api
- collection_type: open
  name: lifen-authentication-api CommunicationRequest Coverage API
  slug: open-lifen-coverage-api
- collection_type: open
  name: lifen-authentication-api CommunicationRequest Encounter API
  slug: open-lifen-encounter-api
- collection_type: open
  name: lifen-authentication-api CommunicationRequest Organization API
  slug: open-lifen-organization-api
- collection_type: open
  name: lifen-authentication-api CommunicationRequest Patient API
  slug: open-lifen-patient-api
- collection_type: open
  name: lifen-authentication-api CommunicationRequest Practitioner API
  slug: open-lifen-practitioner-api
- collection_type: open
  name: lifen-authentication-api CommunicationRequest Token API
  slug: open-lifen-token-api
common:
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/lifen/refs/heads/main/capabilities/lifen-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/lifen-capability-edges.yml
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/lifen/overview
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/lifen/refs/heads/main/security/lifen-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/lifen-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.lifen.fr/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.lifen.fr/
- group: docs
  title: ''
  type: Documentation
  url: https://developer.lifen.fr/docs/platform-services-documentation
- group: docs
  title: ''
  type: APIReference
  url: https://developer.lifen.fr/reference/patient
- group: start
  title: ''
  type: GettingStarted
  url: https://developer.lifen.fr/docs/quickstart
- group: operate
  title: ''
  type: Support
  url: https://www.lifen.fr/contact
- group: company
  title: ''
  type: Blog
  url: https://www.lifen.fr/ressources/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/honestica
- group: start
  title: ''
  type: SignUp
  url: https://www.lifen.fr/sign-up
- group: start
  title: ''
  type: Login
  url: https://www.lifen.fr/log-in
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.lifen.fr/cgu
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.lifen.fr/donnees-personnelles
- group: commercial
  title: ''
  type: LegalNotice
  url: https://www.lifen.fr/mentions-legales
- group: build
  title: ''
  type: Postman
  url: https://developer.lifen.fr/docs/quickstart
- group: operate
  title: ''
  type: StatusPage
  url: https://status.lifen.fr/793930656
- group: operate
  title: ''
  type: ChangeLog
  url: https://developer.lifen.fr/changelog
- group: auth
  title: ''
  type: Compliance
  url: https://www.lifen.fr/nos-expertises/securite-des-donnees-de-sante
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/lifen/refs/heads/main/llms/lifen-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/lifen-llms.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/lifen/refs/heads/main/well-known/lifen-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/lifen-well-known.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/lifen/refs/heads/main/authentication/lifen-authentication.yml
  title: ''
  type: Authentication
  url: authentication/lifen-authentication.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/lifen/refs/heads/main/scopes/lifen-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/lifen-scopes.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/lifen/refs/heads/main/conventions/lifen-conventions.yml
  title: ''
  type: Conventions
  url: conventions/lifen-conventions.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/lifen/refs/heads/main/errors/lifen-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/lifen-problem-types.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/lifen/refs/heads/main/lifecycle/lifen-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/lifen-lifecycle.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/lifen/refs/heads/main/changelog/lifen-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/lifen-changelog.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/lifen/refs/heads/main/conformance/lifen-conformance.yml
  title: ''
  type: Conformance
  url: conformance/lifen-conformance.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/lifen/refs/heads/main/asyncapi/lifen-platform-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/lifen-platform-webhooks.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/lifen/refs/heads/main/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/lifen/refs/heads/main/mcp/lifen-mcp.yml
  title: ''
  type: X-MCPServerCandidate
  url: mcp/lifen-mcp.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/lifen/refs/heads/main/overlays/lifen-fhir-api-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/lifen-fhir-api-overlay.yaml
- group: start
  href: https://raw.githubusercontent.com/api-evangelist/lifen/refs/heads/main/sandbox/lifen-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/lifen-sandbox.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/lifen/refs/heads/main/data-model/lifen-data-model.yml
  title: ''
  type: DataModel
  url: data-model/lifen-data-model.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/lifen/refs/heads/main/rate-limits/lifen-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/lifen-rate-limits.yml
created: '2026-07-17'
description: 'Lifen (Honestica SAS, Paris) is a French digital-health company whose Lifen Platform exposes FHIR R4 APIs that let e-health applications exchange health data with French hospital information systems and with healthcare professionals over the national MSSanté secure-messaging network. The platform is organised as API Services: Hospital API Services (an Identity & Encounter service giving secure access to patient administrative, coverage, encounter and appointment data inside a given hospital, and a Send-documents-to-EHR service that pushes medical documents into hospital Electronic Health Records), and National API Services (the MSS service for sending medical documents to healthcare professionals via MSSanté). Access is machine-to-machine over OAuth 2.0 client credentials, scoped by functional scopes and bound to a healthcare organisation through a database_reference. Lifen also ships an SSO/OIDC API and a signed webhook surface for patient and encounter events. The company
  is ISO 27001 certified and an HDS (Hebergeur de Donnees de Sante) certified health-data host.'
image: https://files.readme.io/ea56e58-small-Logo_couleur.png
layout: provider
modified: '2026-07-19'
name: Lifen
nav: Providers
network: true
overview: 'Lifen publishes 7 APIs on the [APIs.io](https://apis.io/) network, including CommunicationRequest API, Coverage API, Encounter API, and 4 more. Tagged areas include Company, Healthcare, FHIR, Interoperability, and Health Data.


  The Lifen catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Lifen''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, signup flow, changelog, and 29 more developer resources.'
random_paper: 20
rate_limits:
- limit_count: 6
  name: Lifen Rate Limits
  slug: lifen-rate-limits
scopes:
- name: Lifen Scopes
  scope_count: 0
  slug: lifen-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: strong
  composite: 57.0
  coverage:
    artifact_dirs: 24
    catalog_earned: 49.0
    catalog_earned_first_party: 12.0
    catalog_gap: 66.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 42.1
    contract_governance: 18.2
    contract_quality: 60.6
    developer_ergonomics: 49.4
    discoverability: 75.9
    operational_transparency: 57.9
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - france
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - europe
    - france-iberia
  previous_composite: 57.0
  provenance:
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 7
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    jurisdictions:
    - jurisdiction: EU
      standard: gdpr
    jurisdictions_satisfied: 1
    matched_via: tags
    regime: Health
    regime_id: health
    score: 65.0
  schema_version: 0.22.0
  scored_at: '2026-09-21'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://raw.githubusercontent.com/api-evangelist/lifen/refs/heads/main/screenshots/lifen-2026-07-25T225040.png
security:
- kind: authentication
  name: Lifen Authentication
  slug: lifen-authentication
  summary_line: oauth2/openIdConnect/apiKey · 3 schemes
- kind: domain-security
  name: Lifen Domain Security
  slug: lifen-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: lifen
tags:
- Company
- Healthcare
- FHIR
- Interoperability
- Health Data
- Electronic Health Records
- Medical Documents
- Secure Messaging
- France
- HL7
website: https://www.lifen.fr/
---
