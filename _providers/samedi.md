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
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 10.8
  scored_at: '2026-09-18'
api_count: 1
apis:
- description: OAuth2 / OpenID-Connect secured API to discover bookable resources and book and manage patient appointments for a clinic. Versioned in the URL path (booking v3, auth v2).
  name: samedi Booking API
  slug: samedi-booking-api
artifact_total: 4
common:
- group: company
  title: ''
  type: Website
  url: https://www.samedi.com/en
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/samedi
- group: operate
  title: ''
  type: StatusPage
  url: https://status.samedi.de
- group: start
  title: ''
  type: SignUp
  url: https://patient.samedi.de/api/signup
- group: start
  title: ''
  type: Login
  url: https://app.samedi.de/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://legal.samedi.de/en/for_customers/tos/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://legal.samedi.de/en/for_customers/privacy_policy_in_general/
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/samedi/refs/heads/main/authentication/samedi-authentication.yml
  title: ''
  type: Authentication
  url: authentication/samedi-authentication.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/samedi/refs/heads/main/scopes/samedi-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/samedi-scopes.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/samedi/refs/heads/main/well-known/samedi-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/samedi-well-known.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/samedi/refs/heads/main/packages/samedi-packages.yml
  title: ''
  type: Packages
  url: packages/samedi-packages.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/samedi/refs/heads/main/packages/samedi-packages.yml
  title: ''
  type: SDKs
  url: packages/samedi-packages.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/samedi/refs/heads/main/conventions/samedi-conventions.yml
  title: ''
  type: Conventions
  url: conventions/samedi-conventions.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/samedi/refs/heads/main/lifecycle/samedi-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/samedi-lifecycle.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/samedi/refs/heads/main/conformance/samedi-conformance.yml
  title: ''
  type: Conformance
  url: conformance/samedi-conformance.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/samedi/refs/heads/main/security/samedi-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/samedi-domain-security.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/samedi/refs/heads/main/llms/samedi-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/samedi-llms.txt
created: '2026-07-17'
description: samedi is a Berlin-based healthcare software provider delivering smart scheduling and coordination software for medical practices, clinics and hospitals across the DACH region. Its platform covers online appointment booking, patient portals, video consultations, digital intake forms, AI phone assistance, resource and staff planning, and automated patient communication, serving thousands of healthcare institutions. For developers, samedi exposes an OAuth2 / OpenID-Connect Booking API and a Portal API, publishes open-source FHIR, HL7 and CalDAV integration gateways plus Ruby and PHP reference clients, and offers more than 40 interfaces to practice-management (PMS) and hospital-information (HIS) systems.
image: https://www.samedi.com/en
layout: provider
modified: '2026-07-21'
name: samedi
nav: Providers
network: true
overview: 'samedi publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Healthcare, Scheduling, Appointments, and Booking.


  samedi''s developer surface includes signup flow, authentication, and 15 more developer resources.'
random_paper: 11
scopes:
- name: Samedi Scopes
  scope_count: 10
  slug: samedi-scopes
  summary_line: 10 scopes · authorizationCode/clientCredentials
score:
  band: thin
  composite: 29.4
  coverage:
    artifact_dirs: 11
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 34.2
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 19.0
    discoverability: 75.9
    operational_transparency: 18.4
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - germany
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - dach
    - europe
  previous_composite: 29.4
  provenance:
    conformance: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 62.5
  schema_version: 0.22.0
  scored_at: '2026-09-18'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://raw.githubusercontent.com/api-evangelist/samedi/refs/heads/main/screenshots/samedi-2026-09-02T154341.png
security:
- kind: authentication
  name: Samedi Authentication
  slug: samedi-authentication
  summary_line: oauth2/openIdConnect · 3 schemes
- kind: domain-security
  name: Samedi Domain Security
  slug: samedi-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: samedi
tags:
- Company
- Healthcare
- Scheduling
- Appointments
- Booking
- Patient Engagement
- Authentication
- FHIR
- Telehealth
- Germany
website: https://www.samedi.com/en
---
