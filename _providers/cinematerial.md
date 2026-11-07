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
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: true
  schema_version: '0.2'
  score: 2.9
  scored_at: '2026-11-06'
api_count: 0
artifact_total: 1
common:
- group: other
  href: https://artifacts.apis.io/cinematerial/hosts/cinematerial-hosts.yml
  title: ''
  type: Hosts
  url: hosts/cinematerial-hosts.yml
- group: auth
  href: https://artifacts.apis.io/cinematerial/security/cinematerial-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/cinematerial-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://cinematerial.com/
- group: start
  title: ''
  type: SignUp
  url: https://www.cinematerial.com/register
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.cinematerial.com/terms-and-conditions
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.cinematerial.com/privacy-policy
- group: operate
  title: ''
  type: Support
  url: https://www.cinematerial.com/contact
created: '2026-10-28'
description: CineMaterial is a digital community that curates a comprehensive archive of movie posters, covers, logos, key art, and related visual media. It hosts over one million images spanning classic, vintage, and contemporary cinema, providing searchable collections for movies, TV shows, artists, and designers. Users can explore posters by title, era, or creator, and contribute to the growing database.
layout: provider
modified: '2026-10-28'
name: CineMaterial
nav: Providers
network: true
overview: 'CineMaterial is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Media, Archives, Movies, and Community.


  CineMaterial''s developer surface includes signup flow, support, and 5 more developer resources.'
random_paper: 14
score:
  band: minimal
  composite: 7.6
  coverage:
    artifact_dirs: 8
    catalog_earned: 25.0
    catalog_earned_first_party: 0.0
    catalog_gap: 90.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -4.5
  facets:
    access_clarity: 17.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 2.4
    discoverability: 44.6
    operational_transparency: 0.0
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 12.1
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 9.8
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/cinematerial/cinematerial-2026-11-03T124146.png
security:
- kind: domain-security
  name: Cinematerial Domain Security
  slug: cinematerial-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
slug: cinematerial
tags:
- Company
- Media
- Archives
- Movies
- Community
website: https://cinematerial.com/
---
