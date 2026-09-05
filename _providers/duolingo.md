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
  band: agent-aware
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
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 12.9
  scored_at: '2026-09-04'
api_count: 0
artifact_total: 3
common:
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/duolingo-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/duolingo-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.duolingo.com
- group: other
  title: ''
  type: SuperDuolingo
  url: https://www.duolingo.com/super
- group: other
  title: ''
  type: DuolingoMax
  url: https://www.duolingo.com/max
- group: other
  title: ''
  type: DuolingoEnglishTest
  url: https://englishtest.duolingo.com
- group: other
  title: ''
  type: DuolingoEnglishTestForInstitutions
  url: https://englishtest.duolingo.com/institutions
- group: other
  title: ''
  type: DuolingoForSchools
  url: https://schools.duolingo.com
- group: other
  title: ''
  type: DuolingoABC
  url: https://www.duolingo.com/abc
- group: other
  title: ''
  type: DuolingoMath
  url: https://www.duolingo.com/math
- group: other
  title: ''
  type: DuolingoMusic
  url: https://www.duolingo.com/music
- group: other
  title: ''
  type: Company
  url: https://www.duolingo.com/info
- group: company
  title: ''
  type: Newsroom
  url: https://blog.duolingo.com
- group: other
  title: ''
  type: Research
  url: https://research.duolingo.com
- group: build
  title: ''
  type: GitHub
  url: https://github.com/duolingo
- group: company
  title: ''
  type: InvestorRelations
  url: https://investors.duolingo.com
- group: other
  title: ''
  type: SECFilings
  url: https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0001562088
- group: company
  title: ''
  type: Careers
  url: https://careers.duolingo.com
- group: operate
  title: ''
  type: Support
  url: https://support.duolingo.com
- group: company
  title: ''
  type: Twitter
  url: https://twitter.com/duolingo
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/duolingo
- group: learn
  title: ''
  type: YouTube
  url: https://www.youtube.com/@duolingo
- group: docs
  title: ''
  type: GraphQL
  url: graphql/duolingo-graphql.md
- group: company
  title: ''
  type: Blog
  url: https://blog.duolingo.com/rss/
created: '2026-05-25'
description: 'Duolingo (NASDAQ: DUOL) is a Pittsburgh, Pennsylvania based learning technology company best known for the Duolingo language-learning app, the world''s most-downloaded education app, offering courses in more than 40 languages including Spanish, English, French, German, Italian, Portuguese, Japanese, and Chinese. Founded in 2011 by Luis von Ahn and Severin Hacker, Duolingo has expanded its consumer learning footprint beyond languages with Duolingo Math, Duolingo Music, a newly rolled-out Chess course, and Duolingo ABC for early literacy, all delivered through the same gamified, streak- driven mobile experience. The Company also operates the Duolingo English Test, a digital English-proficiency exam accepted by thousands of higher- education institutions, certification programs, and government agencies worldwide as an alternative to TOEFL and IELTS. Duolingo monetizes through Super Duolingo and Duolingo Max subscriptions, in-app advertising, in-app purchases, and Duolingo English
  Test fees. The company surpassed 50 million daily active users in Q3 2025 and reported 41% revenue growth in Q2 2025. Duolingo does not publish an official public developer API, SDK, or developer portal; integrations with the Duolingo English Test (score-send to institutional CRMs such as Slate) are handled through a private API-key program negotiated directly with accepting institutions. Community- maintained reverse-engineered clients exist against the unofficial https://www.duolingo.com/api/1 surface but are not endorsed by Duolingo.'
graphqls:
- description: This directory contains a conceptual GraphQL schema for Duolingo, the world's most-downloaded language-learning app. Duolingo does not publish an official public GraphQL or REST API for third-party de
  name: Duolingo GraphQL Schema
  slug: duolingo-graphql
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/duolingo.png
layout: provider
modified: '2026-05-25'
name: Duolingo
nav: Providers
network: true
overview: 'Duolingo is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Language Learning, Education, EdTech, Mobile Learning, and Gamification.


  Duolingo''s developer surface includes GitHub presence, support, YouTube channel, engineering blog, and 20 more developer resources.'
random_paper: 4
score:
  band: emerging
  composite: 14.7
  coverage:
    artifact_dirs: 4
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 37.2
    developer_ergonomics: 2.4
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 5.3
  previous_composite: 14.7
  regulatory:
    applies: true
    matched_via: tags
    regime: Education & Research
    regime_id: education
    score: 22.2
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/duolingo/refs/heads/main/screenshots/duolingo-2026-07-25T212508.png
security:
- kind: domain-security
  name: Duolingo Domain Security
  slug: duolingo-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: vulnerability-disclosure
  name: Duolingo Vulnerability Disclosure
  slug: duolingo-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: duolingo
tags:
- Language Learning
- Education
- EdTech
- Mobile Learning
- Gamification
- Language Assessment
- English Proficiency
- Math Learning
- Music Learning
- Early Literacy
- Consumer Apps
- Subscription
website: https://www.duolingo.com
---
