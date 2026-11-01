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
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: false
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
  scored_at: '2026-10-31'
api_count: 1
apis:
- description: Bearer-token / OAuth 2.0 authenticated JSON REST API for browsing and managing Thingiverse things (3D models), their files and images, users, collections, categories, tags, and search. Operated by Mak
  name: Thingiverse REST API
  slug: thingiverse-rest-api
artifact_total: 3
common:
- group: company
  title: ''
  type: BlogRSS
  url: https://www.makerbot.com/feed/
- group: company
  title: ''
  type: Website
  url: https://makerbot.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://www.thingiverse.com/developers
- group: docs
  title: ''
  type: Documentation
  url: https://www.thingiverse.com/developers
- group: docs
  title: ''
  type: APIReference
  url: https://www.thingiverse.com/developers
- group: auth
  href: https://artifacts.apis.io/makerbot/authentication/makerbot-authentication.yml
  title: ''
  type: Authentication
  url: authentication/makerbot-authentication.yml
- group: design
  href: https://artifacts.apis.io/makerbot/errors/makerbot-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/makerbot-problem-types.yml
- group: design
  href: https://artifacts.apis.io/makerbot/conventions/makerbot-conventions.yml
  title: ''
  type: Conventions
  url: conventions/makerbot-conventions.yml
- group: design
  href: https://artifacts.apis.io/makerbot/conformance/makerbot-conformance.yml
  title: ''
  type: Conformance
  url: conformance/makerbot-conformance.yml
- group: agent
  href: https://artifacts.apis.io/makerbot/mcp/makerbot-mcp.yml
  title: ''
  type: X-MCPServerCandidate
  url: mcp/makerbot-mcp.yml
- group: auth
  href: https://artifacts.apis.io/makerbot/security/makerbot-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/makerbot-domain-security.yml
- group: agent
  href: https://artifacts.apis.io/makerbot/llms/makerbot-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/makerbot-llms.txt
- group: build
  href: https://artifacts.apis.io/makerbot/packages/makerbot-packages.yml
  title: ''
  type: Packages
  url: packages/makerbot-packages.yml
- group: build
  href: https://artifacts.apis.io/makerbot/packages/makerbot-packages.yml
  title: ''
  type: SDKs
  url: packages/makerbot-packages.yml
- group: design
  href: https://artifacts.apis.io/makerbot/lifecycle/makerbot-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/makerbot-lifecycle.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://status.ultimaker.com
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/makerbot
- group: start
  title: ''
  type: SignUp
  url: https://www.thingiverse.com/join
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.thingiverse.com/legal/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.thingiverse.com/legal/privacy
- group: operate
  title: ''
  type: Support
  url: https://support.makerbot.com
created: '2026-07-17'
description: MakerBot is a desktop 3D printer manufacturer, now part of UltiMaker, and the operator of Thingiverse, the largest online community for discovering, sharing, and downloading 3D-printable designs. MakerBot's public developer surface is the Thingiverse REST API (https://api.thingiverse.com), a Bearer-token / OAuth 2.0 authenticated JSON API that exposes things (models), their files and images, users, collections, categories, tags, and full-text search. Developers register an application on the Thingiverse developers site to receive an App Token or run the OAuth 2.0 authorization flow to act on behalf of a Thingiverse user. This profile was surfaced as a venture-backed company and enriched from its live API.
image: https://www.makerbot.com/favicon.ico
layout: provider
modified: '2026-10-06'
name: Makerbot
nav: Providers
network: true
overview: 'Makerbot is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, 3D Printing, Manufacturing, Thingiverse, and Maker.


  Makerbot''s developer surface includes documentation, API reference, authentication, signup flow, support, and 16 more developer resources.'
random_paper: 13
score:
  band: thin
  composite: 29.8
  coverage:
    artifact_dirs: 14
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
    developer_ergonomics: 50.0
    discoverability: 66.1
    operational_transparency: 21.1
  previous_composite: 29.8
  provenance:
    conformance: first-party
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 24.5
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/makerbot/makerbot-2026-07-25T225942.png
security:
- kind: authentication
  name: Makerbot Authentication
  slug: makerbot-authentication
  summary_line: oauth2/http · 2 schemes
- kind: domain-security
  name: Makerbot Domain Security
  slug: makerbot-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: makerbot
tags:
- Company
- 3D Printing
- Manufacturing
- Thingiverse
- Maker
- Hardware
- Design
- Community
website: https://makerbot.com
---
