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
  scored_at: '2026-09-02'
api_count: 3
apis:
- description: Public OpenID Connect / OAuth 2.0 identity provider operated by Rockstar Games at signin.rockstargames.com. Backs authentication for the Rockstar Games website, Rockstar Games Launcher, Social Club, R
  name: Rockstar Games Sign-In (OpenID Connect)
  slug: signin-oidc
- description: Rockstar's online authentication and player-services backbone originally launched in 2008 to back GTA IV and later every major Rockstar title. Provides player accounts, friends, Crews, multiplayer mat
  name: Rockstar Games Social Club
  slug: social-club
- description: Rockstar's first-party PC storefront and game launcher, distributing Grand Theft Auto V, Red Dead Redemption 2, L.A. Noire, Bully, Max Payne 3, the GTA and Midnight Club catalog, and Rockstar-publishe
  name: Rockstar Games Launcher
  slug: launcher
artifact_total: 6
common:
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/rockstar-games-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/rockstar-games-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.rockstargames.com
- group: company
  title: ''
  type: Newswire
  url: https://www.rockstargames.com/newswire
- group: operate
  title: ''
  type: Support
  url: https://support.rockstargames.com/
- group: auth
  title: ''
  type: Authentication
  url: https://signin.rockstargames.com/
- group: other
  title: ''
  type: ParentCompany
  url: https://www.take2games.com/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/rockstar-games
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/rockstar-games
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.rockstargames.com/legal
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.rockstargames.com/privacy
- group: other
  title: ''
  type: ProductPage
  url: https://www.rockstargames.com/gta-online
- group: other
  title: ''
  type: ProductPage
  url: https://www.rockstargames.com/reddeadonline
- group: other
  title: ''
  type: ProductPage
  url: https://www.rockstargames.com/VI
created: '2026-05-23'
description: 'Rockstar Games is an American video game publisher headquartered in New York City and a wholly-owned subsidiary of Take-Two Interactive Software (NASDAQ: TTWO). Best known for the Grand Theft Auto and Red Dead Redemption franchises, Rockstar operates online services for GTA Online and Red Dead Online, the Rockstar Games Launcher PC client, and the legacy Rockstar Games Social Club identity / authentication platform. Rockstar does not publish a public developer portal; its HTTP API surface is internal and consumed only by first-party clients (game executables, the Rockstar Games Launcher, and Rockstar''s mobile companion apps). The most visible public-facing API is its OpenID Connect / OAuth 2.0 identity provider at signin.rockstargames.com, which exposes standard /connect/authorize, /connect/Token, /connect/introspect, and /.well-known/jwks endpoints. Grand Theft Auto VI is scheduled to launch on November 19, 2026 for PlayStation 5 and Xbox Series X/S and will include a "significant
  online mode" succeeding GTA Online.'
graphqls:
- description: ''
  name: Rockstar Games GraphQL API
  slug: rockstar-games-graphql
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/rockstar-games.png
layout: provider
modified: '2026-07-25'
name: Rockstar Games
nav: Providers
network: true
overview: 'Rockstar Games publishes 3 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Gaming, Entertainment, Video Games, Grand Theft Auto, and Red Dead Redemption.


  Rockstar Games'' developer surface includes support, authentication, and 12 more developer resources.'
random_paper: 15
score:
  band: emerging
  composite: 14.3
  coverage:
    artifact_dirs: 4
    catalog_gap: 75.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 21.1
    commercial_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 11.9
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 2.6
  previous_composite: 14.3
  schema_version: 0.18.0
  scored_at: '2026-09-02'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/rockstar-games/refs/heads/main/screenshots/rockstar-games-2026-06-20T193200.png
security:
- kind: domain-security
  name: Rockstar Games Domain Security
  slug: rockstar-games-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Rockstar Games Vulnerability Disclosure
  slug: rockstar-games-vulnerability-disclosure
  summary_line: Hackerone · security.txt · contact published
slug: rockstar-games
tags:
- Gaming
- Entertainment
- Video Games
- Grand Theft Auto
- Red Dead Redemption
- Identity
- Authentication
website: https://www.rockstargames.com
---
