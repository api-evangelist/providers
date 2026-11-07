---
access_model:
  confidence: medium
  gated: none
  gated_source:
  - onboarding
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  - security
  trial: false
  try_now: true
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: na
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: na
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: derived
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 22.7
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Musixmatch Agentic Access
  operation_count: 16
  slug: musixmatch-agentic-access
  summary_line: 16 operations
api_count: 1
apis:
- baseURL: https://api.musixmatch.com/ws/1.1/
  baseurl_source: declared
  description: The Album API from Musixmatch — 2 operation(s) for album.
  name: Musixmatch Album API
  slug: musixmatch-album-api
- baseURL: https://api.musixmatch.com/ws/1.1/
  baseurl_source: declared
  description: The Artist API from Musixmatch — 4 operation(s) for artist.
  name: Musixmatch Artist API
  slug: musixmatch-artist-api
- baseURL: https://api.musixmatch.com/ws/1.1/
  baseurl_source: declared
  description: The Lyrics API from Musixmatch — 2 operation(s) for lyrics.
  name: Musixmatch Lyrics API
  slug: musixmatch-lyrics-api
- baseURL: https://api.musixmatch.com/ws/1.1/
  baseurl_source: declared
  description: The Snippets API from Musixmatch — 1 operation(s) for snippets.
  name: Musixmatch Snippets API
  slug: musixmatch-snippets-api
- baseURL: https://api.musixmatch.com/ws/1.1/
  baseurl_source: declared
  description: The Subtitle API from Musixmatch — 2 operation(s) for subtitle.
  name: Musixmatch Subtitle API
  slug: musixmatch-subtitle-api
- baseURL: https://api.musixmatch.com/ws/1.1/
  baseurl_source: declared
  description: The Track API from Musixmatch — 5 operation(s) for track.
  name: Musixmatch Track API
  slug: musixmatch-track-api
artifact_total: 19
collections:
- collection_type: open
  name: Musixmatch Album API
  slug: open-musixmatch-album-api
- collection_type: open
  name: Musixmatch Album Artist API
  slug: open-musixmatch-artist-api
- collection_type: open
  name: Musixmatch Album Lyrics API
  slug: open-musixmatch-lyrics-api
- collection_type: open
  name: Musixmatch Album Snippets API
  slug: open-musixmatch-snippets-api
- collection_type: open
  name: Musixmatch Album Subtitle API
  slug: open-musixmatch-subtitle-api
- collection_type: open
  name: Musixmatch Album Track API
  slug: open-musixmatch-track-api
common:
- group: commercial
  href: https://artifacts.apis.io/musixmatch/plans/musixmatch-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/musixmatch-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/musixmatch/rate-limits/musixmatch-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/musixmatch-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/musixmatch/finops/musixmatch-finops.yml
  title: ''
  type: FinOps
  url: finops/musixmatch-finops.yml
- group: company
  title: ''
  type: Website
  url: https://www.musixmatch.com/
- group: agent
  href: https://artifacts.apis.io/musixmatch/agentic-access/musixmatch-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/musixmatch-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/musixmatch/security/musixmatch-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/musixmatch-domain-security.yml
- group: auth
  href: https://artifacts.apis.io/musixmatch/authentication/musixmatch-authentication.yml
  title: ''
  type: Authentication
  url: authentication/musixmatch-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/musixmatch
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/musixmatch
- group: start
  title: ''
  type: Portal
  url: https://developer.musixmatch.com/
- group: start
  title: ''
  type: Login
  url: https://developer.musixmatch.com/login
- group: company
  title: ''
  type: Blog
  url: https://blog.musixmatch.com/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://about.musixmatch.com/privacy-policy
created: '2024-06-07'
description: Musixmatch is an Italian music data company and platform for users to search and share song lyrics with translations. Musixmatch has 80 million users, 8 million songs with their respective lyrics, and 115+ employees.
finops:
- has_sources: false
  method: generated
  name: Musixmatch Finops
  primary_unit: request
  service_category: API
  slug: musixmatch-finops
  template: true
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/musixmatch.png
layout: provider
modified: '2026-05-19'
name: Musixmatch
nav: Providers
network: true
overview: 'Musixmatch publishes 6 API contracts indexed on the [APIs.io](https://apis.io/) network, including Album API, Artist API, Lyrics API, and 3 more. Tagged areas include Lyrics, Music, and Translation.


  The Musixmatch catalog on APIs.io includes 1 Spectral governance ruleset.


  Musixmatch''s developer surface includes authentication, developer portal, engineering blog, and 10 more developer resources.'
plans:
- name: Musixmatch Plans Pricing
  plan_count: 3
  slug: musixmatch-plans-pricing
random_paper: 11
rate_limits:
- limit_count: 5
  name: Musixmatch Rate Limits
  slug: musixmatch-rate-limits
rules:
- authorship: generated
  effective_rule_count: 106
  extends:
  - spectral:oas
  name: Musixmatch API Rules
  rule_count: 65
  severity_counts:
    error: 63
    hint: 0
    info: 1
    warn: 1
  slug: musixmatch-rules
score:
  band: thin
  composite: 34.2
  coverage:
    artifact_dirs: 16
    catalog_earned: 42.5
    catalog_earned_first_party: 0.0
    catalog_gap: 72.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 1.2
  facets:
    access_clarity: 31.6
    contract_governance: 13.6
    contract_quality: 46.9
    developer_ergonomics: 33.3
    discoverability: 64.3
    operational_transparency: 10.5
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - italy
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
  previous_composite: 33.0
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 100.0
      total: 6
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 15.7
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: this provider''s published contracts declare no write operations, and a read-only API cannot create-or-update. Excluded from the denominator, not zeroed.'
    reason: read_only
screenshot: https://apis.io/screenshots/musixmatch/musixmatch-2026-06-20T185906.png
security:
- kind: authentication
  name: Musixmatch Authentication
  slug: musixmatch-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Musixmatch Domain Security
  slug: musixmatch-domain-security
  summary_line: TLSv1.2 · HSTS · DMARC
slug: musixmatch
tags:
- Lyrics
- Music
- Translation
website: https://www.musixmatch.com/
---
