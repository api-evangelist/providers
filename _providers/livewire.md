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
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
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
  score: 18.0
  scored_at: '2026-11-06'
api_count: 0
artifact_total: 1
common:
- group: agent
  href: https://artifacts.apis.io/livewire/llms/livewire-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/livewire-llms.txt
- group: agent
  href: https://artifacts.apis.io/livewire/well-known/livewire-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/livewire-well-known.yml
- group: other
  href: https://artifacts.apis.io/livewire/hosts/livewire-hosts.yml
  title: ''
  type: Hosts
  url: hosts/livewire-hosts.yml
- group: auth
  href: https://artifacts.apis.io/livewire/security/livewire-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/livewire-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.livewire.com/
- group: docs
  title: ''
  type: Documentation
  url: https://www.livewire.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.livewire.com/documents/terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.livewire.com/documents/privacy-policy
- group: operate
  title: ''
  type: Support
  url: https://www.livewire.com/contact
- group: company
  title: ''
  type: Blog
  url: https://www.livewire.com/the-pulse/latest-news
coverage:
  checked: '2026-10-28'
  detail: LiveWire's website provides no developer documentation or API reference pages.
  evidence:
  - status: 200
    url: https://www.livewire.com/
  reason: no-developer-program
  state: none
created: '2026-10-27'
description: LiveWire designs and manufactures high-performance electric motorcycles, offering models such as the LiveWire ONE, S4 Honcho, and S2 series. The company focuses on innovative electric vehicle technology, sustainability, and a premium riding experience, with a US presence and a growing global market. It provides product information, financing options, and a dealer network through its website.
image: https://livewire.widen.net/content/0qscmotdlo/web/media-accordion-homepage-trail-loop.jpg
layout: provider
modified: '2026-10-27'
name: LiveWire
nav: Providers
network: true
overview: 'LiveWire is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Electric Motorcycles, Electric Vehicles, Transportation, and Sustainability.


  LiveWire''s developer surface includes documentation, support, engineering blog, and 7 more developer resources.'
random_paper: 7
score:
  band: minimal
  composite: 9.4
  coverage:
    artifact_dirs: 9
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -4.4
  facets:
    access_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 8.3
    discoverability: 55.4
    operational_transparency: 0.0
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - north-america
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 13.8
  provenance:
    mcp: unknown
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
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/livewire/livewire-2026-11-03T134947.png
security:
- kind: domain-security
  name: Livewire Domain Security
  slug: livewire-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: livewire
tags:
- Company
- Electric Motorcycles
- Electric Vehicles
- Transportation
- Sustainability
- US
website: https://www.livewire.com/
---
