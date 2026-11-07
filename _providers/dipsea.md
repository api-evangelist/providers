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
- group: agent
  href: https://artifacts.apis.io/dipsea/llms/dipsea-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/dipsea-llms.txt
- group: auth
  href: https://artifacts.apis.io/dipsea/well-known/dipsea-support-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/dipsea-support-security.txt
- group: agent
  href: https://artifacts.apis.io/dipsea/well-known/dipsea-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/dipsea-well-known.yml
- group: other
  href: https://artifacts.apis.io/dipsea/hosts/dipsea-hosts.yml
  title: ''
  type: Hosts
  url: hosts/dipsea-hosts.yml
- group: other
  href: https://artifacts.apis.io/dipsea/vendors/dipsea-vendors.yml
  title: ''
  type: Vendors
  url: vendors/dipsea-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.dipseastories.com/terms/
- group: operate
  title: ''
  type: Support
  url: https://support.dipseastories.com/en/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.dipseastories.com/privacypolicy/
- group: company
  title: ''
  type: Blog
  url: https://www.dipseastories.com/blog/
- group: auth
  href: https://artifacts.apis.io/dipsea/security/dipsea-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/dipsea-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.dipseastories.com
coverage:
  checked: '2026-10-23'
  detail: The provider's website hosts storytelling content with no API documentation or contracts discovered.
  evidence:
  - status: 200
    url: https://www.dipseastories.com
  reason: not-a-software-company
  state: none
created: '2026-10-23'
description: Dipsea is a San Francisco‑based media production company that offers a subscription‑based app delivering audio erotica and immersive storytelling from a female‑gaze perspective. The platform features a library of over 1,000 erotic audio stories across diverse tropes, created by professional writers and narrators, aiming to provide a safe, uncensored space for sexual wellness exploration.
image: https://www.dipseastories.com/images/share-image-dusk.jpg
layout: provider
modified: '2026-10-23'
name: Dipsea
nav: Providers
network: true
overview: 'Dipsea is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Audio, Erotica, Subscription, and Media.


  Dipsea''s developer surface includes support, engineering blog, and 9 more developer resources.'
random_paper: 6
score:
  band: minimal
  composite: 8.9
  coverage:
    artifact_dirs: 9
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -3.4
  facets:
    access_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 3.6
    discoverability: 55.4
    operational_transparency: 10.5
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - united-states
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - north-america
  previous_composite: 12.3
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
screenshot: https://apis.io/screenshots/dipsea/dipsea-2026-11-03T130740.png
security:
- kind: domain-security
  name: Dipsea Domain Security
  slug: dipsea-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: dipsea
tags:
- Company
- Audio
- Erotica
- Subscription
- Media
website: https://www.dipseastories.com
---
