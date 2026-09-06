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
  scored_at: '2026-09-05'
api_count: 0
artifact_total: 1
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/planet-fitness-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/planet-fitness
- group: company
  title: ''
  type: Website
  url: https://www.planetfitness.com/
created: '2026-05-05'
description: The largest fitness franchise in the United States by number of members and locations, operating over 2,500 clubs in the US, Canada, Panama, Mexico, and Australia. Planet Fitness is known for its affordable membership model (Classic and Black Card tiers), the non-intimidating Judgement Free Zone philosophy targeting casual and first-time gym-goers, and the PF App for workout content, club check-in, and member benefits. Planet Fitness does not publish a public developer API, integration portal, or third-party platform program; integrations with workout content providers and biometric/check-in vendors are handled via private commercial partnerships, not public APIs.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/planet-fitness.png
layout: provider
modified: '2026-05-09'
name: Planet Fitness
nav: Providers
network: true
overview: Planet Fitness is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Fitness, Wellness, Health, Franchise, and Consumer.
random_paper: 4
score:
  band: minimal
  composite: 3.3
  coverage:
    artifact_dirs: 3
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
  previous_composite: 3.3
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 7.5
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/planet-fitness/refs/heads/main/screenshots/planet-fitness-2026-06-20T191757.png
security:
- kind: domain-security
  name: Planet Fitness Domain Security
  slug: planet-fitness-domain-security
  summary_line: TLSv1.3 · DMARC
slug: planet-fitness
tags:
- Fitness
- Wellness
- Health
- Franchise
- Consumer
- Subscription
- Mobile App
website: https://www.planetfitness.com/
---
