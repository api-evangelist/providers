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
  url: security/eql-games-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.eqlgames.com
- group: company
  title: ''
  type: About
  url: https://www.eqlgames.com/about-us
- group: other
  title: ''
  type: Technology
  url: https://www.eqlgames.com/technology
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/eqlgames
created: '2026-07-17'
description: EQL Games is a Louisville, Kentucky based lottery-industry technology company that operates as an original game studio, third-party content aggregator, and boutique licensor for the global iLottery market. Its iLottery Marketplace aggregates a catalog of 300+ games from 24 partner studios behind a single integration point for lottery operators, while its EQL Labs innovation division builds original instant-win and eInstant titles that fold in licensed intellectual property and live sports. The company also represents brands across lottery verticals (instant scratch and eInstant) and reports serving 8 lottery clients. EQL Games was surfaced through Bullpen Capital's portfolio and added to the API Evangelist network; it publishes a marketing and corporate web presence but no public developer portal, API documentation, or machine-readable API specification at this time.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/eql-games.png
layout: provider
modified: '2026-07-19'
name: EQL Games
nav: Providers
network: true
overview: EQL Games is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Lottery, iLottery, iGaming, and Games.
random_paper: 10
score:
  band: minimal
  composite: 5.0
  coverage:
    artifact_dirs: 2
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
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 5.0
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/eql-games/refs/heads/main/screenshots/eql-games-2026-07-25T213533.png
security:
- kind: domain-security
  name: Eql Games Domain Security
  slug: eql-games-domain-security
  summary_line: TLSv1.3 · DMARC
slug: eql-games
tags:
- Company
- Lottery
- iLottery
- iGaming
- Games
- Game Studio
- Content Aggregator
- Licensing
- Entertainment
website: https://www.eqlgames.com
---
