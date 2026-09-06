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
  scored_at: '2026-09-05'
api_count: 1
apis:
- description: The OpenID Connect and OAuth 2.0 provider behind SEED player accounts. Klang publishes no documentation for it; this entry is recorded from the public discovery documents at seed.game and login.seed.g
  name: SEED Identity (OpenID Connect)
  slug: seed-identity
artifact_total: 4
common:
- group: company
  title: ''
  type: Website
  url: https://www.klang-games.com/
- group: company
  title: ''
  type: About
  url: https://www.klang-games.com/about
- group: company
  title: ''
  type: Blog
  url: https://www.klang-games.com/news
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/klanggames
- group: operate
  title: ''
  type: Support
  url: https://klang-games.eu.theymes.com/hc/en/seed
- group: start
  title: ''
  type: SignUp
  url: https://seed.game/signup
- group: start
  title: ''
  type: Login
  url: https://seed.game/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://seed.game/legal/terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://seed.game/legal/privacy-policy
- group: operate
  title: ''
  type: StatusPage
  url: https://status.seed.game/
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/klang-lifecycle.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/klang-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/klang-scopes.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/klang-well-known.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/klang-conformance.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/klang-domain-security.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/klang-llms.txt
created: '2026-07-17'
description: 'Klang Games is an entertainment and game development studio headquartered in Berlin, founded in 2013 by three Icelandic co-founders — Mundi Vondi (CEO), Oddur Snær Magnússon (CTO) and Ívar Emilsson (CCO) — several of whom came out of CCP and EVE Online. Its flagship product is SEED, a persistent large-scale MMO society simulator built on Google Cloud, backed by investors including Animoca Brands, Supercell, LEGO Ventures, Anthos Capital, Kingway Capital and Northzone. Klang publishes no developer platform: there is no API documentation, no SDKs and no partner program. The only publicly discoverable machine interface is the OpenID Connect provider behind SEED player accounts, captured in this repo from its discovery documents.'
image: https://images.ctfassets.net/a9xx8dr17bmr/5223oQiDQ5KEJejerjCXXU/52485195787ac411bfc206caab898ea5/Huge-new-MMO-is-Sims-4-Stardew-Valley-and-Star-Citizen-all-in-one-1536x864.jpeg
layout: provider
modified: '2026-07-19'
name: Klang Games
nav: Providers
network: true
overview: 'Klang Games publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Consumer, Gaming, Game Development, and MMO.


  Klang Games'' developer surface includes engineering blog, support, signup flow, authentication, and 13 more developer resources.'
random_paper: 0
scopes:
- name: Klang Scopes
  scope_count: 5
  slug: klang-scopes
  summary_line: 5 scopes · authorizationCode/deviceCode
score:
  band: emerging
  composite: 21.2
  coverage:
    artifact_dirs: 9
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 34.2
    commercial_clarity: 34.2
    contract_governance: 4.5
    contract_quality: 0.0
    developer_ergonomics: 19.0
    discoverability: 75.9
    governance: 4.5
    operational_transparency: 18.4
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - dach
    - europe
  previous_composite: 21.2
  provenance:
    conformance: derived
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/klang/refs/heads/main/screenshots/klang-2026-07-25T223927.png
security:
- kind: authentication
  name: Klang Authentication
  slug: klang-authentication
  summary_line: oauth2/openIdConnect · 2 schemes
- kind: domain-security
  name: Klang Domain Security
  slug: klang-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: klang
tags:
- Company
- Consumer
- Gaming
- Game Development
- MMO
- Simulation
- Entertainment
- Identity
- OpenID Connect
- Berlin
website: https://www.klang-games.com/
---
