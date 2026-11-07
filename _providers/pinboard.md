---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - authentication
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
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
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 5.4
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: Pinboard provides a read‑only API (v1) for accessing bookmarks, notes, tags and user data. All methods are GET and return XML or JSON.
  name: Pinboard API
  slug: pinboard-api
artifact_total: 5
common:
- group: design
  href: https://artifacts.apis.io/pinboard/conventions/pinboard-conventions.yml
  title: ''
  type: Conventions
  url: conventions/pinboard-conventions.yml
- group: auth
  href: https://artifacts.apis.io/pinboard/authentication/pinboard-authentication.yml
  title: ''
  type: Authentication
  url: authentication/pinboard-authentication.yml
- group: design
  href: https://artifacts.apis.io/pinboard/lifecycle/pinboard-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/pinboard-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/pinboard/errors/pinboard-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/pinboard-problem-types.yml
- group: other
  href: https://artifacts.apis.io/pinboard/hosts/pinboard-hosts.yml
  title: ''
  type: Hosts
  url: hosts/pinboard-hosts.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://pinboard.in/tos/
- group: auth
  title: ''
  type: Security
  url: https://pinboard.in/security/
- group: auth
  href: https://artifacts.apis.io/pinboard/security/pinboard-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/pinboard-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/pinboard/security/pinboard-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/pinboard-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://pinboard.in/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://pinboard.in/api/
- group: docs
  title: ''
  type: Documentation
  url: https://pinboard.in/api/
- group: docs
  title: ''
  type: APIReference
  url: https://pinboard.in/api/
- group: start
  title: ''
  type: GettingStarted
  url: https://pinboard.in/api/
- group: company
  title: ''
  type: Blog
  url: https://blog.pinboard.in/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/pinboard
- group: start
  title: ''
  type: SignUp
  url: https://pinboard.in/signup
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://pinboard.in/privacy
coverage:
  checked: '2026-10-28'
  detail: The Pinboard API documentation is HTML only and provides no OpenAPI, AsyncAPI, GraphQL, gRPC, or WSDL spec.
  evidence:
  - status: 200
    url: https://pinboard.in/api/
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-28'
description: Pinboard is a social bookmarking service designed for introverts, allowing users to save, tag, and share web pages. It offers a simple, read‑only API for retrieving bookmarks, adding new ones, managing tags, and searching. The service emphasizes privacy, minimalism, and long‑term storage, and provides paid plans for unlimited bookmarks. Its API documentation is publicly available at https://pinboard.in/api/.
image: https://pinboard.in/blue-pin.png
layout: provider
modified: '2026-10-28'
name: Pinboard
nav: Providers
network: true
overview: 'Pinboard is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Bookmarking, Social, Productivity, and Web.


  Pinboard''s developer surface includes authentication, documentation, API reference, getting-started guide, engineering blog, signup flow, and 12 more developer resources.'
random_paper: 7
scopes:
- name: Pinboard Scopes
  scope_count: 0
  slug: pinboard-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: emerging
  composite: 19.9
  coverage:
    artifact_dirs: 18
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -9.1
  facets:
    access_clarity: 17.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 32.1
    discoverability: 66.1
    operational_transparency: 7.9
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 29.0
  provenance:
    conformance: unknown
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 31.4
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/pinboard/pinboard-2026-11-03T141220.png
security:
- kind: authentication
  name: Pinboard Authentication
  slug: pinboard-authentication
  summary_line: 2 schemes
- kind: domain-security
  name: Pinboard Domain Security
  slug: pinboard-domain-security
  summary_line: TLSv1.3 · HSTS
- kind: vulnerability-disclosure
  name: Pinboard Vulnerability Disclosure
  slug: pinboard-vulnerability-disclosure
  summary_line: no policy recorded
slug: pinboard
tags:
- Company
- Bookmarking
- Social
- Productivity
- Web
website: https://pinboard.in/
---
