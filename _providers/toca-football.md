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
  scored_at: '2026-09-04'
api_count: 0
artifact_total: 1
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/toca-football-domain-security.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/toca-football-llms.txt
- group: company
  title: ''
  type: Website
  url: https://www.tocafootball.com/
- group: company
  title: ''
  type: About
  url: https://www.tocafootball.com/about
- group: operate
  title: ''
  type: Support
  url: https://support.tocafootball.com/support/home
- group: company
  title: ''
  type: Blog
  url: https://www.tocafootball.com/articles
- group: company
  title: ''
  type: Press
  url: https://www.tocafootball.com/news
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/TOCA-LLC
- group: start
  title: ''
  type: SignUp
  url: https://my.tocafootball.com/auth/signup
- group: start
  title: ''
  type: Login
  url: https://my.tocafootball.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.tocafootball.com/policies/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.tocafootball.com/policies/privacy-policy
- group: operate
  title: ''
  type: Contact
  url: https://www.tocafootball.com/contact-us
- group: company
  title: ''
  type: Careers
  url: https://www.tocafootball.com/careers
- group: company
  title: ''
  type: Partners
  url: https://www.tocafootball.com/partnerships
- group: other
  title: ''
  type: Licensing
  url: https://www.tocafootball.com/licensing
- group: other
  title: ''
  type: Patents
  url: https://www.tocafootball.com/patents
- group: other
  title: ''
  type: Shop
  url: https://shop.tocafootball.com/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/toca-football
- group: learn
  title: ''
  type: YouTube
  url: https://www.youtube.com/user/tocafootball
- group: company
  title: ''
  type: Instagram
  url: https://www.instagram.com/tocafootball
- group: company
  title: ''
  type: Facebook
  url: https://www.facebook.com/TOCAsoccer/
- group: other
  title: ''
  type: SecondaryMarket
  url: https://forgeglobal.com/toca-football_stock/
coverage:
  checked: '2026-08-05'
  detail: TOCA ships software only as consumer end-user products (the MyTOCA booking/performance app and the TOCA Remote ball-machine controller); api., docs. and developer.tocafootball.com do not resolve in DNS, and the only public code the company publishes is a two-repo GitHub org holding a Snowflake/dbt CI image and a Java player-pathway tool.
  evidence:
  - status: 404
    url: https://www.tocafootball.com/openapi.json
  - status: 404
    url: https://www.tocafootball.com/llms.txt
  - status: 404
    url: https://www.tocafootball.com/.well-known/security.txt
  - status: 404
    url: https://www.tocafootball.com/.well-known/agent-card.json
  - status: 0
    url: https://api.tocafootball.com/
  - status: 0
    url: https://developer.tocafootball.com/
  - status: 0
    url: https://docs.tocafootball.com/
  - status: 200
    url: https://api.github.com/orgs/TOCA-LLC/repos
  reason: no-developer-program
  state: none
created: '2026-08-05'
description: 'TOCA Football, Inc. is a technology-enabled soccer experience and entertainment company headquartered in Costa Mesa, California, founded on the training methodology of former US international and Premier League player Eddie Lewis. It operates two businesses: TOCA Soccer, a network of indoor soccer training centers across the United States, Canada and Mexico offering private training, classes, clinics, camps, youth and adult leagues, tournaments and pickup play; and TOCA Social, a soccer-themed dining and entertainment venue brand. Its training centers pair a proprietary ball-delivery machine and digitalized smart targets with the MyTOCA player app, which tracks session performance, player cards, leaderboards and progress. TOCA is the official soccer training partner of Major League Soccer. TOCA publishes no public API, SDK, webhook or developer program: its software ships only as end-user consumer apps and in-venue systems.'
image: https://cdn.prod.website-files.com/60c7be61132e3a9edf0a3315/69656c31b8bcac0228627149_indoor-soccer-practice-training-programs-toca.jpg
layout: provider
modified: '2026-08-05'
name: TOCA Football
nav: Providers
network: true
overview: 'TOCA Football is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Sports, Soccer, Sports Technology, and Youth Sports.


  TOCA Football''s developer surface includes support, engineering blog, signup flow, YouTube channel, and 19 more developer resources.'
random_paper: 17
score:
  band: emerging
  composite: 13.0
  coverage:
    artifact_dirs: 4
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 27.6
    commercial_clarity: 27.6
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 7.1
    discoverability: 57.4
    governance: 0.0
    operational_transparency: 2.6
  previous_composite: 13.0
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/toca-football/refs/heads/main/screenshots/toca-football-2026-09-02T163837.png
security:
- kind: domain-security
  name: Toca Football Domain Security
  slug: toca-football-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: toca-football
tags:
- Company
- Sports
- Soccer
- Sports Technology
- Youth Sports
- Training
- Fitness
- Entertainment
- Location-Based Entertainment
- Consumer Mobile Apps
- United States
website: https://www.tocafootball.com/
---
