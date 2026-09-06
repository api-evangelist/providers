---
access_model:
  confidence: medium
  label: Freemium
  onboarding: unknown
  pricing: freemium
  public: false
  source:
  - plans
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
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 2.5
  scored_at: '2026-09-05'
api_count: 1
apis:
- description: An API for developers to get information on over 4 million podcasts, 180 million episodes, and 1.5 million transcripts. Powered by Taddy's GraphQL API and supports search across podcast series, episod
  name: Podcast API (Taddy)
  slug: podcast-api
artifact_total: 6
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/podcast-api-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/listen-notes
- group: company
  title: ''
  type: Website
  url: https://taddy.org
- group: docs
  title: ''
  type: Documentation
  url: https://taddy.org/developers/podcast-api
created: '2025-05-02'
description: An API for developers to get information on over 4 million podcasts, 180 million episodes, and 1.5 million transcripts. Powered by Taddy's GraphQL API, the Podcast API supports search across podcast series, episode details, transcripts, top charts, popularity data, and webhook subscriptions.
finops:
- name: Podcast Api Finops
  service_category: API
  slug: podcast-api-finops
graphqls:
- description: An API for developers to get information on over 4 million podcasts, 180 million episodes, and 1.5 million transcripts. Powered by Taddy's GraphQL API and supports search across podcast series, episod
  name: Podcast API GraphQL API
  slug: podcast-api-graphql
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/podcast-api.png
layout: provider
modified: '2026-04-28'
name: Podcast API
nav: Providers
network: true
overview: 'Podcast API publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Podcasts, Podcasting, Episodes, Transcripts, and Search.


  Podcast API''s developer surface includes documentation and 3 more developer resources.'
plans:
- name: Podcast Api Plans Pricing
  plan_count: 3
  slug: podcast-api-plans-pricing
random_paper: 17
rate_limits:
- limit_count: 5
  name: Podcast Api Rate Limits
  slug: podcast-api-rate-limits
score:
  band: emerging
  composite: 12.9
  coverage:
    artifact_dirs: 6
    catalog_earned: 46.0
    catalog_earned_first_party: 0.0
    catalog_gap: 69.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 15.8
    commercial_clarity: 15.8
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 9.5
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 7.9
  previous_composite: 12.9
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/podcast-api/refs/heads/main/screenshots/podcast-api-2026-06-20T191829.png
security:
- kind: domain-security
  name: Podcast Api Domain Security
  slug: podcast-api-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
slug: podcast-api
tags:
- Podcasts
- Podcasting
- Episodes
- Transcripts
- Search
- GraphQL
- Webhook
website: https://taddy.org
---
