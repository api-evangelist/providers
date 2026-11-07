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
api_count: 0
artifact_total: 1
common:
- group: agent
  href: https://artifacts.apis.io/adarch-co-jp/llms/adarch-co-jp-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/adarch-co-jp-llms.txt
- group: other
  href: https://artifacts.apis.io/adarch-co-jp/hosts/adarch-co-jp-hosts.yml
  title: ''
  type: Hosts
  url: hosts/adarch-co-jp-hosts.yml
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://adarch.co.jp/privacy.html
- group: auth
  href: https://artifacts.apis.io/adarch-co-jp/security/adarch-co-jp-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/adarch-co-jp-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://adarch.co.jp/
coverage:
  detail: the company publishes no developer documentation host and no machine-readable contract on its own domain
  evidence:
  - status: 200
    url: https://adarch.co.jp/
  reason: no-developer-program
  state: none
created: '2026-10-31'
description: Ad Arch Co., Ltd. is an advertising and creative agency group headquartered in Tokyo that provides ad planning, media planning, and creative production services. It serves international organizations, government agencies, and national brands across Japan through its network of 24 offices.
image: https://adarch.co.jp/ogp.jpg
layout: provider
modified: '2026-10-31'
name: Ad Arch株式会社
nav: Providers
network: true
overview: Ad Arch株式会社 is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Advertising, Media, Video Production, Marketing, and Japan.
random_paper: 1
score:
  band: minimal
  composite: 4.8
  coverage:
    artifact_dirs: 7
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -1.3
  facets:
    access_clarity: 5.3
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 48.2
    operational_transparency: 0.0
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - japan
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - japan-korea
  previous_composite: 6.1
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
security:
- kind: domain-security
  name: Adarch Co Jp Domain Security
  slug: adarch-co-jp-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: adarch-co-jp
tags:
- Advertising
- Media
- Video Production
- Marketing
- Japan
website: https://adarch.co.jp/
---
