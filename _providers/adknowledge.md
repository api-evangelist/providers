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
  schema_version: '0.2'
  score: 0.0
  scored_at: '2026-09-25'
api_count: 0
artifact_total: 0
created: '2026-07-17'
description: 'Adknowledge, Inc. was a performance-based digital advertising and marketing technology holding company founded in 2004 by Scott Lynn and headquartered in Kansas City, Missouri. It ran a response-based targeting marketplace that connected advertisers to consumers across email, search, domains, social and app inventory, and it exposed a publisher-facing AdStation platform with an automated offer engine and creative library. Ben Legg served as Group CEO from 2011 to 2016, during which the company consolidated a long acquisition run (Super Rewards, Miva, Cubics, Lookery, Hydra Group, AdParlor, Giant Media, TriVu Media and others) into video and social units that were then sold off; AdParlor was subsequently acquired by Fluent in 2019. Third-party company registries now list Adknowledge as out of business. It entered the API Evangelist network as a portfolio-lead stub via kleiner-perkins. Contemporary integration write-ups confirm a historical RESTful AdStation / Publisher Platform
  API, but as of this enrichment pass no live surface survives: the adknowledge.com zone is still registered (AWS Route 53 nameservers, Microsoft 365 mail with an SPF record) yet publishes no A record for the apex or for www, api, developer, developers, docs or publisher, so there is no reachable website, developer portal, API documentation or machine-readable specification from which to harvest provider artifacts.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/adknowledge.png
layout: provider
modified: '2026-07-20'
name: AdKnowledge
nav: Providers
network: true
overview: AdKnowledge is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Consumer, Advertising, Marketing, and AdTech.
random_paper: 13
score:
  band: minimal
  composite: 0.0
  coverage:
    artifact_dirs: 0
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 0.0
    operational_transparency: 0.0
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - north-america
  lifecycle: defunct
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: no_resolvable_host
    - owner: catalog
      reason: never_enriched
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 0.0
  schema_version: 0.23.0
  scored_at: '2026-09-25'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
slug: adknowledge
tags:
- Company
- Consumer
- Advertising
- Marketing
- AdTech
- Email
- Publishers
- Defunct
---
