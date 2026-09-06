---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source: []
  trial: false
  try_now: false
agent_readiness:
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: false
    consent_identity: false
    delegated_identity: false
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
  score: 0.0
  scored_at: '2026-09-05'
api_count: 0
artifact_total: 2
common:
- group: company
  title: ''
  type: Website
  url: https://www.doctolib.fr
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developers.doctolib.com/
- group: start
  title: ''
  type: SignUp
  url: https://pro.doctolib.fr
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/doctolib
- group: operate
  title: ''
  type: StatusPage
  url: https://status.doctolib.com/
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/doctolib-lifecycle.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/doctolib-well-known.yml
- group: auth
  title: ''
  type: SecurityTxt
  url: security/doctolib-security.txt
- group: auth
  title: ''
  type: Security
  url: https://yeswehack.com/programs/doctolib-public-bug-bounty-program
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/doctolib-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/doctolib-domain-security.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/doctolib-llms.txt
created: '2026-07-17'
description: Doctolib is a European e-health company founded in 2013 and headquartered in Levallois-Perret, France, operating across France, Germany, Italy and the Netherlands. It provides an online medical appointment-booking platform and practice-management software used by patients and by hundreds of thousands of healthcare professionals and facilities. Its product surface spans appointment booking, telehealth/video consultation, patient messaging, clinical software, patient billing, and the Doctolib Connect integration and single-sign-on layer. Doctolib exposes a partner/integration API via an authentication-gated developer portal (developers.doctolib.com); it publishes an RFC 9116 security.txt and runs a public YesWeHack bug-bounty program, an Atlassian Statuspage, and an open-source GitHub organization, but does not publish a public OpenAPI specification, first-party API SDK, or hosted MCP server.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/doctolib.png
layout: provider
modified: '2026-07-18'
name: Doctolib
nav: Providers
network: true
overview: 'Doctolib is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Healthcare, E-Health, Appointment Booking, and Telehealth.


  Doctolib''s developer surface includes signup flow and 11 more developer resources.'
random_paper: 8
score:
  band: minimal
  composite: 9.9
  coverage:
    artifact_dirs: 5
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 4.8
    discoverability: 57.4
    governance: 0.0
    operational_transparency: 28.9
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - france
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - europe
    - france-iberia
  previous_composite: 9.9
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 15.0
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/doctolib/refs/heads/main/screenshots/doctolib-2026-07-25T212221.png
security:
- kind: domain-security
  name: Doctolib Domain Security
  slug: doctolib-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Doctolib Vulnerability Disclosure
  slug: doctolib-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: doctolib
tags:
- Company
- Healthcare
- E-Health
- Appointment Booking
- Telehealth
- Practice Management
- Patient Engagement
- Software-as-a-Service
- France
website: https://www.doctolib.fr
---
