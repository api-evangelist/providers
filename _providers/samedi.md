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
  schema_version: 0.2
  score: 10.8
  scored_at: '2026-09-01'
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
  title: ''
  type: Authentication
  url: authentication/samedi-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/samedi-scopes.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/samedi-well-known.yml
- group: build
  title: ''
  type: Packages
  url: packages/samedi-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/samedi-packages.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/samedi-conventions.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/samedi-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/samedi-conformance.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/samedi-domain-security.yml
- group: agent
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
random_paper: 18
scopes:
- name: Samedi Scopes
  scope_count: 10
  slug: samedi-scopes
  summary_line: 10 scopes · authorizationCode/clientCredentials
score:
  band: thin
  composite: 29.4
  coverage:
    artifact_dirs: 9
    catalog_gap: 78.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 34.2
    commercial_clarity: 34.2
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 19.0
    discoverability: 75.9
    governance: 18.2
    operational_transparency: 18.4
  previous_composite: 29.4
  provenance:
    conformance: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 62.5
  schema_version: 0.18.0
  scored_at: '2026-09-01'
  trend: flat
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
- Telemedicine
- Germany
website: https://www.samedi.com/en
---
