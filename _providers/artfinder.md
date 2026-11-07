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
    well_known_catalog: false
  schema_version: '0.2'
  score: 0.0
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: Artfinder provides a marketplace API (no public machine‑readable contract discovered).
  name: Artfinder API
  slug: artfinder-api
artifact_total: 2
common:
- group: other
  href: https://artifacts.apis.io/artfinder/hosts/artfinder-hosts.yml
  title: ''
  type: Hosts
  url: hosts/artfinder-hosts.yml
- group: other
  href: https://artifacts.apis.io/artfinder/vendors/artfinder-vendors.yml
  title: ''
  type: Vendors
  url: vendors/artfinder-vendors.yml
- group: build
  href: https://artifacts.apis.io/artfinder/packages/artfinder-packages.yml
  title: ''
  type: SDKs
  url: packages/artfinder-packages.yml
- group: build
  href: https://artifacts.apis.io/artfinder/packages/artfinder-packages.yml
  title: ''
  type: Packages
  url: packages/artfinder-packages.yml
- group: operate
  title: ''
  type: Support
  url: https://help.artfinder.com/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.artfinder.com/help/privacy-policy/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.artfinder.com/art/price_max-500/
- group: company
  title: ''
  type: Newsroom
  url: https://www.artfinder.com/press/
- group: company
  title: ''
  type: Blog
  url: https://www.artfinder.com/blog/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/artfinder
- group: auth
  href: https://artifacts.apis.io/artfinder/security/artfinder-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/artfinder-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.artfinder.com
- group: docs
  title: ''
  type: Documentation
  url: https://about.artfinder.com/
- group: company
  title: ''
  type: About
  url: https://about.artfinder.com/
- group: other
  title: ''
  type: Sustainability
  url: https://about.artfinder.com/sustainability
- group: other
  title: ''
  type: Team
  url: https://about.artfinder.com/team
- group: other
  title: ''
  type: BCorp
  url: https://about.artfinder.com/b-corp
- group: other
  title: ''
  type: SellOn
  url: https://about.artfinder.com/sell
- group: other
  title: ''
  type: Curators
  url: https://about.artfinder.com/curators
- group: other
  title: ''
  type: TradeProgram
  url: https://about.artfinder.com/trade
- group: other
  title: ''
  type: PersonalShopping
  url: https://about.artfinder.com/personal-shopping
coverage:
  checked: 2026-09-26
  detail: Documentation pages are rendered via JavaScript and no machine‑readable spec was found.
  evidence:
  - status: 200
    url: https://about.artfinder.com/
  reason: js-rendered-docs
  state: unreadable
created: '2026-09-26'
description: Artfinder is an online marketplace that connects independent artists with buyers worldwide, offering a curated selection of original artworks, prints, and sculptures. The platform enables artists to showcase and sell their creations directly to collectors, providing detailed artist profiles, secure transactions, and worldwide shipping. Artfinder emphasizes supporting creative communities and fostering a vibrant art‑selling ecosystem.
image: https://d2m7ibezl7l5lt.cloudfront.net/img/v2/default-share-image.bca336466cdd.jpg
layout: provider
modified: '2026-09-26'
name: Artfinder
nav: Providers
network: true
overview: 'Artfinder is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Marketplace, Art, E-Commerce, and Community.


  Artfinder''s developer surface includes support, pricing, engineering blog, documentation, and 17 more developer resources.'
random_paper: 23
score:
  band: minimal
  composite: 10.2
  coverage:
    artifact_dirs: 11
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -4.6
  facets:
    access_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 15.5
    discoverability: 58.0
    operational_transparency: 2.6
  previous_composite: 14.8
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 7.8
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/artfinder/artfinder-2026-10-11T100414.png
security:
- kind: domain-security
  name: Artfinder Domain Security
  slug: artfinder-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: artfinder
tags:
- Company
- Marketplace
- Art
- E-Commerce
- Community
website: https://www.artfinder.com
---
