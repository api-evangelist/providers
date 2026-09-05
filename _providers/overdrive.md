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
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
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
  score: 2.5
  scored_at: '2026-09-04'
api_count: 3
apis:
- description: Discovery APIs to search and find information about titles in a library's OverDrive collection — Library Account, Search, Metadata, and Library Availability.
  name: OverDrive Discovery API
  slug: overdrive-discovery-api
- description: Circulation APIs to authenticate patrons and manage checkouts and holds against a library's OverDrive collection.
  name: OverDrive Circulation API
  slug: overdrive-circulation-api
- description: Reporting API to see the titles that were borrowed from a specific collection during a specific time period (public libraries only).
  name: OverDrive Reporting API
  slug: overdrive-reporting-api
artifact_total: 6
common:
- group: company
  title: ''
  type: Website
  url: http://www.overdrive.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.overdrive.com/
- group: docs
  title: ''
  type: Documentation
  url: https://developer.overdrive.com/api-docs/authentication
- group: docs
  title: ''
  type: APIReference
  url: https://developer.overdrive.com/api-docs/discovery-apis
- group: start
  title: ''
  type: GettingStarted
  url: https://developer.overdrive.com/getting-started/api-overview
- group: auth
  title: ''
  type: Authentication
  url: authentication/overdrive-authentication.yml
- group: operate
  title: ''
  type: Support
  url: https://developer.overdrive.com/support/contact-us
- group: start
  title: ''
  type: SignUp
  url: https://developer.overdrive.com/request-access
- group: operate
  title: ''
  type: StatusPage
  url: https://status.overdrive.com/
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/overdrive-lifecycle.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/overdrive-conventions.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/overdrive-conformance.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/overdrive-well-known.yml
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/overdrive-security.txt
- group: auth
  title: ''
  type: DomainSecurity
  url: security/overdrive-domain-security.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/overdrive-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: https://developer.overdrive.com/.well-known/security.txt
- group: agent
  title: ''
  type: X-MCPServerCandidate
  url: mcp/overdrive-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/overdrive-llms.txt
created: '2026-07-17'
description: 'OverDrive is a digital reading platform that distributes ebooks, audiobooks, and magazines to public libraries and schools worldwide, best known for its Libby and Sora reading apps. OverDrive publishes a set of REST APIs that let library systems, integrators, and partners work against a library''s OverDrive collection: Discovery APIs (Library Account, Search, Metadata, and Library Availability), Circulation APIs (patron information, checkouts, and holds), Reporting APIs (checkouts report), and a Title Link API. Access is authorized with OAuth 2.0 client-credentials (client authentication) for discovery and patron authentication (including QR-code sign-in) for borrowing and holds, with a dedicated integration environment for testing against real titles before going live.'
image: https://developer.overdrive.com/img/overdrive-logo.png
layout: provider
modified: '2026-07-20'
name: OverDrive
nav: Providers
network: true
overview: 'OverDrive publishes 3 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Books, Libraries, Ebooks, and Audiobooks.


  OverDrive''s developer surface includes documentation, API reference, getting-started guide, authentication, support, signup flow, and 13 more developer resources.'
random_paper: 16
score:
  band: thin
  composite: 27.3
  coverage:
    artifact_dirs: 9
    catalog_earned: 40.0
    catalog_earned_first_party: 0.0
    catalog_gap: 75.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 13.2
    commercial_clarity: 13.2
    contract_governance: 4.5
    contract_quality: 0.0
    developer_ergonomics: 54.8
    discoverability: 81.5
    governance: 4.5
    operational_transparency: 21.1
  previous_composite: 27.3
  provenance:
    conformance: derived
    mcp: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Education & Research
    regime_id: education
    score: 42.6
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/overdrive/refs/heads/main/screenshots/overdrive-2026-08-07T191124.png
security:
- kind: authentication
  name: Overdrive Authentication
  slug: overdrive-authentication
  summary_line: oauth2 · 3 schemes
- kind: domain-security
  name: Overdrive Domain Security
  slug: overdrive-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: vulnerability-disclosure
  name: Overdrive Vulnerability Disclosure
  slug: overdrive-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: overdrive
tags:
- Company
- Books
- Libraries
- Ebooks
- Audiobooks
- Digital Media
- Publishing
- Education
- Reading
- Circulation
website: http://www.overdrive.com/
---
