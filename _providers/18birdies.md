---
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
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 2.5
  scored_at: '2026-09-05'
api_count: 0
artifact_total: 3
common:
- group: company
  title: ''
  type: Website
  url: https://18birdies.com/
- group: operate
  title: ''
  type: Support
  url: https://help.18birdies.com/
- group: company
  title: ''
  type: Blog
  url: https://18birdies.com/clubhouse/
- group: commercial
  title: ''
  type: Pricing
  url: https://18birdies.com/premium/
- group: start
  title: ''
  type: SignUp
  url: https://18birdies.com/install/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://18birdies.com/legal/terms/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://18birdies.com/legal/privacy-policy/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/18Birdies
- group: commercial
  title: ''
  type: Plans
  url: plans/18birdies-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/18birdies-rate-limits.yml
- group: build
  title: ''
  type: Packages
  url: packages/18birdies-packages.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/18birdies-domain-security.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/18birdies-llms.txt
coverage:
  checked: '2026-09-05'
  detail: 18Birdies ships only an end-user golf app — its site has no /developers, /developer, /api or /docs page (all 404), its Help Scout knowledge base has no API or integration category, and the mobile backend at api.18birdies.com answers 403 at the root and 404 on every OpenAPI, Swagger, GraphQL and .well-known discovery path.
  evidence:
  - status: 404
    url: https://18birdies.com/developers
  - status: 404
    url: https://18birdies.com/llms.txt
  - status: 404
    url: https://api.18birdies.com/openapi.json
  - status: 404
    url: https://api.18birdies.com/graphql
  - status: 403
    url: https://api.18birdies.com/
  - status: 404
    url: https://18birdies.com/.well-known/api-catalog
  reason: no-developer-program
  state: none
created: '2026-09-05'
description: 18Birdies is a golf technology company behind the 18Birdies mobile app — a golf GPS rangefinder, digital scorecard, shot- and stat-tracking platform and social network for golfers, founded in 2014. The app combines Google Maps-derived course imagery and elevation with hole-by-hole GPS distances, 3D green maps, wind and slope adjustment, club recommendations, strokes-gained analytics, an AI Swing Analyzer, handicap tracking, side games and tournament/league management across a worldwide golf course database. It operates a freemium consumer subscription (a free tier plus Premium) with companion Apple Watch and Wear OS experiences. 18Birdies runs a production backend at api.18birdies.com that serves its own mobile clients, but as of this profiling pass it publishes no public developer program, no API reference, and no machine-readable contract.
image: https://18birdies.com/public-images/apple-touch-icon.png
layout: provider
modified: '2026-09-05'
name: 18Birdies
nav: Providers
network: true
overview: '18Birdies is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Golf, Sports, Mobile Applications, Location, and Geolocation.


  18Birdies'' developer surface includes support, engineering blog, pricing, signup flow, and 9 more developer resources.'
plans:
- name: 18Birdies Plans Pricing
  plan_count: 4
  slug: 18birdies-plans-pricing
random_paper: 3
rate_limits:
- limit_count: 0
  name: 18Birdies Rate Limits
  slug: 18birdies-rate-limits
score:
  band: emerging
  composite: 22.4
  coverage:
    artifact_dirs: 6
    catalog_earned: 39.0
    catalog_earned_first_party: 12.0
    catalog_gap: 76.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 76.3
    commercial_clarity: 76.3
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 7.1
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 5.3
  schema_version: 0.18.3
  scored_at: '2026-09-05'
security:
- kind: domain-security
  name: 18Birdies Domain Security
  slug: 18birdies-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: 18birdies
tags:
- Golf
- Sports
- Mobile Applications
- Location
- Geolocation
- Mapping
- Consumer
- Fitness
- Social
- Analytics
- Tournaments
- Subscriptions
website: https://18birdies.com/
---
