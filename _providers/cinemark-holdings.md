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
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 5.0
  scored_at: '2026-09-05'
api_count: 0
artifact_total: 4
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/cinemark-holdings-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/cinemark
- group: company
  title: ''
  type: Website
  url: https://www.cinemark.com
- group: company
  title: ''
  type: Website
  url: https://investors.cinemark.com
- group: other
  title: ''
  type: Mobile App (iOS)
  url: https://apps.apple.com/us/app/cinemark-theatres/id435965836
- group: other
  title: ''
  type: Mobile App (Android)
  url: https://play.google.com/store/apps/details?id=com.cinemark.mobile
- group: other
  title: ''
  type: Loyalty Program
  url: https://www.cinemark.com/movie-club
- group: other
  title: ''
  type: Gift Cards
  url: https://www.cinemark.com/gift-cards
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.cinemark.com/privacy-policy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.cinemark.com/terms-conditions
- group: operate
  title: ''
  type: Support
  url: https://www.cinemark.com/contact-us
- group: company
  title: ''
  type: Careers
  url: https://careers.cinemark.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developers.cinemark.com.br/api-portal/
- group: start
  title: ''
  type: SignUp
  url: https://developers.cinemark.com.br/api-portal/user/register
- group: operate
  title: ''
  type: HelpCenter
  url: https://www.cinemark.com/faq
- group: build
  title: ''
  type: Packages
  url: packages/cinemark-holdings-packages.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/cinemark-holdings-llms.txt
- group: auth
  title: ''
  type: Authentication
  url: authentication/cinemark-holdings-authentication.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/cinemark-holdings-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/cinemark-holdings-rate-limits.yml
coverage:
  checked: '2026-09-05'
  detail: Cinemark's only developer surface is its Brazilian subsidiary's Sensedia portal at developers.cinemark.com.br, whose API list and interactive API Browser are served only to registered accounts — an anonymous GET of /api-portal/apis returns HTTP 403 "Acesso negado" — while the pages it does serve publicly are unmodified vendor template (Lorem ipsum terms and FAQ, Tumblr's OAuth endpoints on the auth page, Evernote's SDK copy), and the api.cinemark.com host returns HTTP 502 on every path.
  evidence:
  - status: 403
    url: https://developers.cinemark.com.br/api-portal/apis
  - status: 502
    url: https://api.cinemark.com/openapi.json
  - status: 404
    url: https://www.cinemark.com/openapi.json
  - status: 404
    url: https://www.cinemark.com.br/programacao.xml
  reason: partner-login
  state: gated
created: '2026-03-23'
description: 'Cinemark Holdings, Inc. (NYSE: CNK) is one of the largest motion picture exhibitors in the world, operating theatres across the United States and fifteen Latin American countries under the Cinemark, Century, Tinseltown, Rave and CineArts brands. Cinemark publishes no general-purpose public API and no machine-readable contract of any kind: as of September 2026 there is no OpenAPI, GraphQL SDL, AsyncAPI, agent card, MCP server or .well-known document on any Cinemark-controlled host. Its Brazilian subsidiary does operate a branded Sensedia developer portal at developers.cinemark.com.br, but the API list and interactive API Browser are gated behind developer registration and most of the portal''s public pages remain unmodified vendor template content. Showtime, ticketing and loyalty integrations are delivered through partner agreements and third-party aggregators such as Fandango, Atom Tickets and Movio.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/cinemark-holdings.png
layout: provider
modified: '2026-09-05'
name: Cinemark Holdings
nav: Providers
network: true
overview: 'Cinemark Holdings is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Cinema, Entertainment, Loyalty, Movie Theaters, and Ticketing.


  Cinemark Holdings'' developer surface includes support, signup flow, authentication, and 17 more developer resources.'
plans:
- name: Cinemark Holdings Plans Pricing
  plan_count: 0
  slug: cinemark-holdings-plans-pricing
press:
- date: '2026-05-25'
  title: Cinemark Q4 Earnings Call Highlights
  url: https://finance.yahoo.com/news/cinemark-q4-earnings-call-highlights-165524091.html
- date: '2026-05-25'
  title: Rokt to Unlock New Consumer Engagement Opportunities ...
  url: https://www.prnewswire.com/news-releases/rokt-to-unlock-new-consumer-engagement-opportunities-for-cinemark-302561560.html
- date: '2026-05-25'
  title: 10-K
  url: https://ir.cinemark.com/sec-filings/all-sec-filings/content/0000950170-25-022756/cnk-20241231.htm
- date: '2026-05-25'
  title: Cinemark Holdings, Inc. (CNK) Q1 2026 Earnings Call ...
  url: https://seekingalpha.com/article/4897445-cinemark-holdings-inc-cnk-q1-2026-earnings-call-transcript
- date: '2026-05-25'
  title: Cinemark Announces Greater Movie Theater Accessibility
  url: https://afb.org/blog/entry/cinemark-announces-greater-movie-theater-accessibility
random_paper: 0
rate_limits:
- limit_count: 0
  name: Cinemark Holdings Rate Limits
  slug: cinemark-holdings-rate-limits
score:
  band: emerging
  composite: 17.8
  coverage:
    artifact_dirs: 12
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 9.7
  facets:
    access_clarity: 34.2
    commercial_clarity: 34.2
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 26.2
    discoverability: 57.4
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 8.1
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: rising
security:
- kind: authentication
  name: Cinemark Holdings Authentication
  slug: cinemark-holdings-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Cinemark Holdings Domain Security
  slug: cinemark-holdings-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: cinemark-holdings
tags:
- Cinema
- Entertainment
- Loyalty
- Movie Theaters
- Ticketing
- Fortune 1000
website: https://www.cinemark.com
---
