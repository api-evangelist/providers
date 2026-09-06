---
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    agentic_commerce: false
    auth_clarity: negotiable
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: true
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: verified
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 41.1
  scored_at: '2026-09-05'
api_count: 1
apis:
- baseURL: https://www.znanylekarz.pl/api/v3/integration
  baseurl_source: declared
  description: OAuth 2.0 REST API (v1.14.0) for medical-software vendors integrating a practice-management system with the ZnanyLekarz marketplace. 44 operations across facilities, doctors, addresses, services, insu
  name: Docplanner Integrations API
  slug: docplanner-integrations-api
artifact_total: 9
asyncapis:
- description: ''
  name: Znanylekarz Notifications
  slug: znanylekarz-notifications
collections:
- collection_type: postman
  name: Docplanner Integrations API
  slug: postman-znanylekarz-integrations-api
common:
- group: company
  title: ''
  type: Website
  url: https://www.znanylekarz.pl/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://integrations.docplanner.com/
- group: docs
  title: ''
  type: Documentation
  url: https://integrations.docplanner.com/guide/
- group: docs
  title: ''
  type: APIReference
  url: https://integrations.docplanner.com/docs/
- group: start
  title: ''
  type: GettingStarted
  url: https://integrations.docplanner.com/guide/integration-process.html
- group: build
  title: ''
  type: Postman
  url: https://www.postman.com/run-collection/7fd8db9bb1fd14e0f0f7
- group: operate
  title: ''
  type: Support
  url: https://help.docplanner.com/
- group: company
  title: ''
  type: Blog
  url: https://www.znanylekarz.pl/blog/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/DocPlanner
- group: commercial
  title: ''
  type: Pricing
  url: https://pro.znanylekarz.pl/cennik/znanylekarz-dla-lekarzy
- group: start
  title: ''
  type: SignUp
  url: https://www.znanylekarz.pl/rejestracja-wybor
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.znanylekarz.pl/regulamin
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.znanylekarz.pl/prywatnosc
- group: operate
  title: ''
  type: StatusPage
  url: https://status.docplanner.com/
- group: build
  title: ''
  type: Packages
  url: packages/znanylekarz-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/znanylekarz-packages.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/znanylekarz-well-known.yml
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/znanylekarz-security.txt
- group: auth
  title: ''
  type: Security
  url: security/znanylekarz-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/znanylekarz-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/znanylekarz-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/znanylekarz-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/znanylekarz-scopes.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/znanylekarz-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/znanylekarz-problem-types.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/znanylekarz-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/znanylekarz-lifecycle.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/znanylekarz-changelog.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/znanylekarz-data-model.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/znanylekarz-sandbox.yml
- group: build
  title: ''
  type: Examples
  url: examples/znanylekarz-examples.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/znanylekarz-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/znanylekarz-rate-limits.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/znanylekarz-llms.txt
created: '2026-09-05'
description: ZnanyLekarz is the Polish healthcare marketplace and practice-management platform operated by Docplanner Group, connecting patients with over 146,000 listed doctors and equipping medical practices with online booking, calendar management, appointment reminders, patient reviews, e-prescriptions, video consultations and online payments. ZnanyLekarz.pl is the founding brand of the Docplanner Group and the Polish locale of the group's marketplace, which also trades as Doctoralia, MioDottore, Jameda, Doktor Takvimi and Znamylekar. Its public developer surface is the Docplanner Integrations API — an OAuth 2.0 REST API served on the www.znanylekarz.pl host that lets medical-software vendors synchronise facilities, doctors, addresses, services, insurance providers, calendars, breaks, slots and bookings, and receive push or pull event notifications when patients book, move, confirm or cancel visits.
image: https://platform.docplanner.com/img/pl/open-graph/og-v0.png
layout: provider
modified: '2026-09-05'
name: ZnanyLekarz
nav: Providers
network: true
overview: 'ZnanyLekarz publishes 1 API on the [APIs.io](https://apis.io/) network: Docplanner Integrations API. Tagged areas include Company, Healthcare, Health Tech, Appointments, and Booking.


  The ZnanyLekarz catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  ZnanyLekarz''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, pricing, signup flow, and 28 more developer resources.'
plans:
- name: Znanylekarz Plans Pricing
  plan_count: 4
  slug: znanylekarz-plans-pricing
random_paper: 12
rate_limits:
- limit_count: 2
  name: Znanylekarz Rate Limits
  slug: znanylekarz-rate-limits
scopes:
- name: Znanylekarz Scopes
  scope_count: 1
  slug: znanylekarz-scopes
  summary_line: 1 scope · clientCredentials
score:
  band: exemplar
  composite: 69.7
  coverage:
    artifact_dirs: 23
    catalog_earned: 57.0
    catalog_earned_first_party: 20.0
    catalog_gap: 58.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 76.3
    commercial_clarity: 76.3
    contract_governance: 4.5
    contract_quality: 61.7
    developer_ergonomics: 75.6
    discoverability: 75.9
    governance: 4.5
    operational_transparency: 73.7
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - poland
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - cee
    - europe
  provenance:
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
    score: 60.0
  schema_version: 0.18.3
  scored_at: '2026-09-05'
security:
- kind: authentication
  name: Znanylekarz Authentication
  slug: znanylekarz-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Znanylekarz Domain Security
  slug: znanylekarz-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: vulnerability-disclosure
  name: Znanylekarz Vulnerability Disclosure
  slug: znanylekarz-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: znanylekarz
tags:
- Company
- Healthcare
- Health Tech
- Appointments
- Booking
- Medical
- Marketplace
- Doctors
- Scheduling
- Poland
- Practice Management
- Telemedicine
website: https://www.znanylekarz.pl/
---
