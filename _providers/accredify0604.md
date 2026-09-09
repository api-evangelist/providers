---
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.2
  score: 36.5
  scored_at: '2026-09-08'
api_count: 2
apis:
- baseURL: https://nexus.accredify.io
  baseurl_source: declared
  description: 'The Accredify Nexus platform API. OAuth 2.0 client-credentials REST API split across three published OpenAPI 3.1 modules: Auth (organisation users, groups, roles, user tokens, token issuance), Workflo'
  name: Accredify Nexus API
  slug: accredify0604-nexus
- baseURL: https://dashboard.accredify.io/api
  baseurl_source: declared
  description: The Accredify Dashboard API, published as two OpenAPI 3.1 documents. v1 covers OAuth 2.0 authorization-code grant and refresh, OpenBadges issuance, update and revocation, batch upload (JSON and Excel)
  name: Accredify Dashboard API
  slug: accredify0604-dashboard
artifact_total: 8
common:
- group: company
  title: ''
  type: Website
  url: https://www.accredify.io/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.nexus.accredify.io/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.dashboard.accredify.io/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Accredifysg
- group: company
  title: ''
  type: Blog
  url: https://www.accredify.io/blog
- group: operate
  title: ''
  type: Support
  url: https://www.accredify.io/contact-us
- group: operate
  title: ''
  type: HelpCenter
  url: https://www.accredify.io/faq
- group: start
  title: ''
  type: SignUp
  url: https://www.accredify.io/schedule-demo
- group: start
  title: ''
  type: Login
  url: https://dashboard.accredify.io/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.accredify.io/service-terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.accredify.io/data-protection-notice
- group: operate
  title: ''
  type: StatusPage
  url: https://status.accredify.io/
- group: auth
  title: ''
  type: Security
  url: https://www.accredify.io/security
- group: auth
  title: ''
  type: Compliance
  url: https://www.accredify.io/security
- group: auth
  title: ''
  type: TrustCenter
  url: security/accredify0604-trust-center.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/accredify0604-llms.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/accredify0604-well-known.yml
- group: build
  title: ''
  type: Packages
  url: packages/accredify0604-packages.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/accredify0604-conformance.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/accredify0604-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/accredify0604-lifecycle.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/accredify0604-scopes.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/accredify0604-authentication.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/accredify0604-domain-security.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/accredify0604-conventions.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/accredify0604-sandbox.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/accredify0604-data-model.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/accredify0604-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/accredify0604-rate-limits.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-09-06'
description: Accredify is a Singapore-headquartered verifiable-credentials and "TrustTech" platform that lets organisations create, issue, verify and manage tamper-proof digital documents. Its Nexus platform exposes an OAuth 2.0 client-credentials REST API covering organisation users, groups, roles and user tokens (Auth module), workflow definitions, workflow runs, documents, design/document templates and courses (Workflow module), and document verification plus verifiable-data key extraction (Verification module). A separate Accredify Dashboard API (v1 and v2) covers OAuth 2.0 grants, OpenBadges issuance and revocation, batch upload/issue, certificate revocation, courses, templates and email templates. Accredify also operates a live OpenID for Verifiable Credential Issuance (OID4VCI) credential issuer at nexus.accredify.io, publishing mso_mdoc credential configurations for ISO/IEC 18013-5 mobile driving licence and ISO/IEC 23220 photo ID. The company issues in W3C VC, EBSI, mDL, SMART Health
  Card, OpenCerts, OpenAttestation and OpenBadges standards, serves education, healthcare, associations, licensing and public-sector customers across nine markets, and built Singapore's HealthCerts COVID-19 verification system.
image: https://www.accredify.io/wp-content/uploads/2022/10/Accredify-Logo.png
layout: provider
modified: '2026-09-06'
name: Accredify
nav: Providers
network: true
overview: 'Accredify publishes 2 APIs on the [APIs.io](https://apis.io/) network: Nexus API and Dashboard API. Tagged areas include Company, Verifiable Credentials, Digital Credentials, Identity, and Document Verification.


  Accredify''s developer surface includes documentation, API reference, engineering blog, support, signup flow, authentication, sandbox, and 23 more developer resources.'
plans:
- name: Accredify0604 Plans Pricing
  plan_count: 0
  slug: accredify0604-plans-pricing
random_paper: 6
rate_limits:
- limit_count: 0
  name: Accredify0604 Rate Limits
  slug: accredify0604-rate-limits
scopes:
- name: Accredify0604 Scopes
  scope_count: 20
  slug: accredify0604-scopes
  summary_line: 20 scopes · clientCredentials
score:
  band: developing
  composite: 51.9
  coverage:
    artifact_dirs: 19
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 50.0
    commercial_clarity: 50.0
    contract_governance: 18.2
    contract_quality: 53.0
    developer_ergonomics: 44.6
    discoverability: 75.9
    governance: 18.2
    operational_transparency: 28.9
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - singapore
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - southeast-asia
  previous_composite: 51.9
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
    score: 65.0
  schema_version: 0.20.0
  scored_at: '2026-09-08'
  trend: flat
  upsert:
    applies: true
    score: 0.0
security:
- kind: authentication
  name: Accredify0604 Authentication
  slug: accredify0604-authentication
  summary_line: http/oauth2 · 2 schemes
- kind: domain-security
  name: Accredify0604 Domain Security
  slug: accredify0604-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Accredify0604 Trust Center
  slug: accredify0604-trust-center
  summary_line: ISO/IEC 27001:2022, ISO/IEC 27017:2015, ISO/IEC 27018:2019, CSA STAR CAIQ, ISO 22301, IMDA Data Protection Trustmark
slug: accredify0604
tags:
- Company
- Verifiable Credentials
- Digital Credentials
- Identity
- Document Verification
- Credentialing
- Education
- Healthcare
- Trust
- OpenBadges
- OID4VCI
- Singapore
website: https://www.accredify.io/
---
