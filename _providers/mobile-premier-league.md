---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - security
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
artifact_total: 1
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/mobile-premier-league-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.mplgames.com/
- group: operate
  title: ''
  type: Support
  url: https://www.mplgames.com/help
- group: company
  title: ''
  type: Blog
  url: https://www.mplgames.com/blog
- group: company
  title: ''
  type: BlogRSS
  url: https://www.mplgames.com/blog/feed
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.mplgames.com/about-us/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.mplgames.com/about-us/privacy-policy
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/mobile-premier-league-lifecycle.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/mobile-premier-league-llms.txt
coverage:
  checked: '2026-08-25'
  detail: MPL's game-developer program is gone at the DNS layer — docs.developer.mpl.live returns NXDOMAIN and developer.mpl.live is a dangling CNAME to a deleted AWS load balancer (dualstack.prod-developer-dashboard-2060818981.ap-south-1.elb.amazonaws.com, itself NXDOMAIN) — and the surviving hosts publish nothing machine-readable, with api.mpl.live returning a JSON 404 to every spec, GraphQL and /.well-known/ path probed.
  evidence:
  - status: 0
    url: https://docs.developer.mpl.live/docs
  - status: 0
    url: https://developer.mpl.live/
  - status: 404
    url: https://api.mpl.live/openapi.json
  - status: 404
    url: https://www.mplgames.com/.well-known/api-catalog
  - status: 200
    url: https://www.mplgames.com/about-us
  reason: no-developer-program
  state: none
created: '2026-08-25'
description: Mobile Premier League (MPL) is a mobile skill-gaming and esports platform founded in 2018 and headquartered in Bengaluru, India, operated by Galactus Funware Technology. It distributes a catalog of casual, card, board and fantasy-sports titles inside a single app and runs tournaments and contests around them, reporting more than 100 million registered users across Asia, Europe and North America. MPL historically ran a game-developer program — a Developer Dashboard and a publish-and-monetize SDK at developer.mpl.live, documented at docs.developer.mpl.live — that let third-party studios ship a single build to the MPL app under a revenue-share agreement. That program's hosts no longer resolve, and MPL publishes no public REST, GraphQL, MCP or event API today. Following India's Promotion and Regulation of Online Gaming Act, 2025, MPL discontinued real-money gaming in India; www.mplgames.com is the live consumer surface, principally serving the United States.
image: https://cms-origin.mpl.live/cms-latest-env/images/MPL_logo_13457e45ff_c5f37df2e8.webp
layout: provider
modified: '2026-08-25'
name: Mobile Premier League
nav: Providers
network: true
overview: 'Mobile Premier League is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Gaming, Mobile Gaming, Esports, and Skill Gaming.


  Mobile Premier League''s developer surface includes support, engineering blog, and 7 more developer resources.'
random_paper: 5
score:
  band: minimal
  composite: 10.6
  coverage:
    artifact_dirs: 6
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 21.1
    commercial_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 7.1
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 0.0
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - india
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - india-south-asia
  previous_composite: 10.6
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/mobile-premier-league/refs/heads/main/screenshots/mobile-premier-league-2026-09-02T150557.png
security:
- kind: domain-security
  name: Mobile Premier League Domain Security
  slug: mobile-premier-league-domain-security
  summary_line: TLSv1.3
slug: mobile-premier-league
tags:
- Company
- Gaming
- Mobile Gaming
- Esports
- Skill Gaming
- Games
- Consumer
- Entertainment
- Tournaments
- India
website: https://www.mplgames.com/
---
