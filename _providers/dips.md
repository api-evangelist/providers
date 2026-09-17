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
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
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
  score: 32.6
  scored_at: '2026-09-16'
api_count: 3
apis:
- description: The DIPS HL7 FHIR R4 API exposes core clinical and administrative data from the DIPS Arena EHR — Patient, Person, RelatedPerson, Practitioner, PractitionerRole, Organization, Location, HealthcareServi
  name: DIPS FHIR R4 API
  slug: dips-fhir-r4-api
- baseURL: https://api.dips.no/dips.oauth
  baseurl_source: declared
  description: The Account API from DIPS — 2 operation(s) for account.
  name: DIPS Account API
  slug: dips-account-api
- baseURL: https://api.dips.no/dips.oauth
  baseurl_source: declared
  description: The Connect API from DIPS — 7 operation(s) for connect.
  name: DIPS Connect API
  slug: dips-connect-api
- baseURL: https://api.dips.no/dips.oauth
  baseurl_source: declared
  description: The Consent API from DIPS — 1 operation(s) for consent.
  name: DIPS Consent API
  slug: dips-consent-api
- baseURL: https://api.dips.no/dips.oauth
  baseurl_source: declared
  description: The * API from DIPS — 1 operation(s) for *.
  name: DIPS * API
  slug: dips-default-api
- baseURL: https://api.dips.no/dips.oauth
  baseurl_source: declared
  description: The Home API from DIPS — 1 operation(s) for home.
  name: DIPS Home API
  slug: dips-home-api
- baseURL: https://api.dips.no/dips.oauth
  baseurl_source: declared
  description: The Login API from DIPS — 1 operation(s) for login.
  name: DIPS Login API
  slug: dips-login-api
- baseURL: https://api.dips.no/dips.oauth
  baseurl_source: declared
  description: The Status API from DIPS — 2 operation(s) for status.
  name: DIPS Status API
  slug: dips-status-api
- baseURL: https://api.dips.no/dips.oauth
  baseurl_source: declared
  description: The .well Known API from DIPS — 2 operation(s) for .well known.
  name: DIPS .well Known API
  slug: dips-well-known-api
- baseURL: https://api.dips.no/fhir
  baseurl_source: declared
  description: The User Role API from DIPS — 2 operation(s) for user role.
  name: DIPS User Role API
  slug: dips-user-role-api
artifact_total: 15
common:
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/dips/refs/heads/main/overlays/dips-federation-service-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/dips-federation-service-overlay.yaml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/dips/refs/heads/main/security/dips-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/dips-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.dips.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://dips.developer.azure-api.net/
- group: docs
  title: ''
  type: Documentation
  url: https://dips.developer.azure-api.net/getting-started
- group: docs
  title: ''
  type: APIReference
  url: https://dips.developer.azure-api.net/apis
- group: start
  title: ''
  type: GettingStarted
  url: https://dips.developer.azure-api.net/getting-started
- group: start
  title: ''
  type: SignUp
  url: https://dips.developer.azure-api.net/signup
- group: start
  title: ''
  type: Login
  url: https://dips.developer.azure-api.net/signin
- group: commercial
  title: ''
  type: TermsOfService
  url: https://dips.developer.azure-api.net/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.dips.com/personvern
- group: operate
  title: ''
  type: Support
  url: https://www.dips.com/kontakt
- group: company
  title: ''
  type: Blog
  url: https://www.dips.com/innsikt
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/DIPSAS
- group: company
  title: ''
  type: Partners
  url: https://dips.developer.azure-api.net/partner
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/dips/refs/heads/main/llms/dips-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/dips-llms.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/dips/refs/heads/main/well-known/dips-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/dips-well-known.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/dips/refs/heads/main/packages/dips-packages.yml
  title: ''
  type: Packages
  url: packages/dips-packages.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/dips/refs/heads/main/packages/dips-packages.yml
  title: ''
  type: SDKs
  url: packages/dips-packages.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/dips/refs/heads/main/conventions/dips-conventions.yml
  title: ''
  type: Conventions
  url: conventions/dips-conventions.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/dips/refs/heads/main/lifecycle/dips-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/dips-lifecycle.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/dips/refs/heads/main/plans/dips-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/dips-plans-pricing.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/dips/refs/heads/main/rate-limits/dips-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/dips-rate-limits.yml
- group: start
  href: https://raw.githubusercontent.com/api-evangelist/dips/refs/heads/main/sandbox/dips-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/dips-sandbox.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/dips/refs/heads/main/conformance/dips-conformance.yml
  title: ''
  type: Conformance
  url: conformance/dips-conformance.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/dips/refs/heads/main/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/dips/refs/heads/main/data-model/dips-data-model.yml
  title: ''
  type: DataModel
  url: data-model/dips-data-model.yml
created: '2026-09-02'
description: DIPS AS is Norway's largest supplier of electronic health record (EHR) systems to hospitals, in operation since 1987 and headquartered in Bodø. Its DIPS Arena EHR is built on the openEHR reference model and exposes standardised HL7 FHIR R4 and openEHR REST interfaces. Through Open DIPS — a public developer portal and synthetic-data sandbox at dips.developer.azure-api.net — DIPS publishes an OpenID Connect provider (DIPS Federation Service), a FHIR Patient API and a SMART on FHIR launch surface, backed by a public FHIR R4 Implementation Guide and an openEHR archetype repository on GitHub.
image: https://dips.developer.azure-api.net/content/Dips_symbol.png
layout: provider
modified: '2026-09-02'
name: DIPS
nav: Providers
network: true
overview: 'DIPS publishes 9 APIs on the [APIs.io](https://apis.io/) network, including Account API, Connect API, Consent API, and 6 more. Tagged areas include Company, Healthcare, Electronic Health Records, Health IT, and FHIR.


  DIPS''s developer surface includes documentation, API reference, getting-started guide, signup flow, support, engineering blog, sandbox, and 20 more developer resources.'
plans:
- name: Dips Plans Pricing
  plan_count: 1
  slug: dips-plans-pricing
random_paper: 14
rate_limits:
- limit_count: 0
  name: Dips Rate Limits
  slug: dips-rate-limits
scopes:
- name: Dips Scopes
  scope_count: 0
  slug: dips-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: developing
  composite: 53.7
  coverage:
    artifact_dirs: 19
    catalog_earned: 48.0
    catalog_earned_first_party: 8.0
    catalog_gap: 67.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.7
  facets:
    access_clarity: 55.3
    contract_governance: 18.2
    contract_quality: 46.7
    developer_ergonomics: 73.2
    discoverability: 74.1
    operational_transparency: 2.6
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - norway
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - europe
    - nordics
  previous_composite: 53.0
  provenance:
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 9
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 66.3
  schema_version: 0.22.0
  scored_at: '2026-09-16'
  trend: flat
  upsert:
    applies: true
    score: 0.0
security:
- kind: authentication
  name: Dips Authentication
  slug: dips-authentication
  summary_line: apiKey/openIdConnect · 3 schemes
- kind: domain-security
  name: Dips Domain Security
  slug: dips-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: dips
tags:
- Company
- Healthcare
- Electronic Health Records
- Health IT
- FHIR
- openEHR
- Interoperability
- Identity
- OpenID Connect
- Norway
- Hospitals
- SMART on FHIR
website: https://www.dips.com/
---
