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
    auth_clarity: served
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
    well_known_catalog: true
  schema_version: 0.2
  score: 9.4
  scored_at: '2026-09-05'
api_count: 0
artifact_total: 2
common:
- group: company
  title: ''
  type: Website
  url: https://www.kixeye.com/
- group: company
  title: ''
  type: About
  url: https://corp.kixeye.com/
- group: operate
  title: ''
  type: Support
  url: https://www.kixeye.com/support
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Kixeye
- group: commercial
  title: ''
  type: TermsOfService
  url: https://corp.kixeye.com/tos.html
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://corp.kixeye.com/pp.html
- group: other
  title: ''
  type: CookiePolicy
  url: https://corp.kixeye.com/cookie-policy.html
- group: commercial
  title: ''
  type: Legal
  url: https://corp.kixeye.com/legal.html
- group: company
  title: ''
  type: Careers
  url: https://corp.kixeye.com/#careers
- group: agent
  title: ''
  type: WellKnown
  url: well-known/kixeye-well-known.yml
- group: other
  title: ''
  type: OpenIDConnect
  url: well-known/kixeye-openid-configuration.json
- group: auth
  title: ''
  type: Authentication
  url: authentication/kixeye-authentication.yml
- group: build
  title: ''
  type: Packages
  url: packages/kixeye-packages.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/kixeye-domain-security.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/kixeye-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/kixeye-lifecycle.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/kixeye-llms.txt
created: '2026-07-17'
description: 'KIXEYE Inc. is a video game developer and publisher founded in 2009 and headquartered in Victoria, British Columbia, with staff across Canada and the United States. KIXEYE creates, develops, and publishes massively multiplayer online real-time strategy (MMORTS) games for browsers, tablets, and smartphones, including Battle Pirates, War Commander, War Commander: Rogue Assault, and Rise of Firstborn. An early innovator in the free-to-play genre, KIXEYE operates long-lived live-service game worlds with monthly events, alliances, and competitive leaderboards for millions of players worldwide. KIXEYE is part of the Stillfront Group. KIXEYE publishes no public developer program or partner API; its api.kixeye.com host is a private game-services backend that exposes an OpenID Connect discovery document and JWKS for token verification. The company does maintain a public GitHub organization of open-source infrastructure libraries (chassis, kixmpp, janus, scout) used to build its own
  cloud services.'
image: https://www.kixeye.com/modules/footer/images/logo.png
layout: provider
modified: '2026-07-19'
name: Kixeye
nav: Providers
network: true
overview: 'Kixeye is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Gaming, Video Games, Game Development, and Mobile Games.


  Kixeye''s developer surface includes support, legal docs, authentication, and 14 more developer resources.'
random_paper: 4
score:
  band: emerging
  composite: 14.2
  coverage:
    artifact_dirs: 8
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 21.1
    commercial_clarity: 21.1
    contract_governance: 4.5
    contract_quality: 0.0
    developer_ergonomics: 16.7
    discoverability: 57.4
    governance: 4.5
    operational_transparency: 2.6
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - north-america
  previous_composite: 14.2
  provenance:
    conformance: derived
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/kixeye/refs/heads/main/screenshots/kixeye-2026-07-25T223925.png
security:
- kind: authentication
  name: Kixeye Authentication
  slug: kixeye-authentication
  summary_line: openIdConnect · 1 scheme
- kind: domain-security
  name: Kixeye Domain Security
  slug: kixeye-domain-security
  summary_line: TLSv1.2 · DMARC
slug: kixeye
tags:
- Company
- Gaming
- Video Games
- Game Development
- Mobile Games
- Strategy Games
- Free-to-Play
- Live Service
website: https://www.kixeye.com/
---
