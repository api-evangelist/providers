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
  href: https://artifacts.apis.io/tencent-music-entertainment-group/hosts/tencent-music-entertainment-group-hosts.yml
  title: ''
  type: Hosts
  url: hosts/tencent-music-entertainment-group-hosts.yml
- group: other
  href: https://artifacts.apis.io/tencent-music-entertainment-group/vendors/tencent-music-entertainment-group-vendors.yml
  title: ''
  type: Vendors
  url: vendors/tencent-music-entertainment-group-vendors.yml
- group: build
  href: https://artifacts.apis.io/tencent-music-entertainment-group/packages/tencent-music-entertainment-group-packages.yml
  title: ''
  type: SDKs
  url: packages/tencent-music-entertainment-group-packages.yml
- group: build
  href: https://artifacts.apis.io/tencent-music-entertainment-group/packages/tencent-music-entertainment-group-packages.yml
  title: ''
  type: Packages
  url: packages/tencent-music-entertainment-group-packages.yml
- group: auth
  href: https://artifacts.apis.io/tencent-music-entertainment-group/security/tencent-music-entertainment-group-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/tencent-music-entertainment-group-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.tencentmusic.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://opencloud.tencentmusic.com/
- group: docs
  title: ''
  type: Documentation
  url: https://www.tencentmusic.com/zh-cn/about-us.html
- group: docs
  title: ''
  type: APIReference
  url: https://opencloud.tencentmusic.com/
- group: start
  title: ''
  type: GettingStarted
  url: https://www.tencentmusic.com/zh-cn/about-us.html
- group: operate
  title: ''
  type: Support
  url: https://www.tencentmusic.com/zh-cn/contact.html
- group: company
  title: ''
  type: Blog
  url: https://www.tencentmusic.com/zh-cn/news.html
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/tencentmusic
- group: operate
  title: ''
  type: Roadmap
  url: https://www.tencentmusic.com/zh-cn/business.html
- group: commercial
  title: ''
  type: Pricing
  url: https://www.tencentmusic.com/zh-cn/business.html
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.tencentmusic.com/zh-cn/protocol.html
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.tencentmusic.com/zh-cn/privacypolicy.html
- group: build
  title: ''
  type: Postman
  url: https://www.postman.com/tencentmusic
coverage:
  checked: '2026-10-22'
  detail: Developer portal at https://opencloud.tencentmusic.com/ returns a 403 HTML page, no machine‑readable spec.
  evidence:
  - status: 403
    url: https://opencloud.tencentmusic.com/
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-22'
description: Tencent Music Entertainment Group (TME) is a leading Chinese online music entertainment platform offering streaming services, digital music distribution, and live concert experiences across brands such as QQ Music, Kugou, Kuwo, and JOOX. It provides a comprehensive ecosystem for artists, listeners, and partners, integrating social features, AI-driven recommendations, and extensive licensing across domestic and international markets. TME is publicly listed and actively expands its audio content through acquisitions and strategic partnerships.
image: https://prodpublic-1253428821.cos.ap-guangzhou.myqcloud.com/public/tme_logo/TME_LOGO_CN.png
layout: provider
modified: '2026-10-22'
name: Tencent Music Entertainment Group
nav: Providers
network: true
overview: 'Tencent Music Entertainment Group is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Music, Streaming, Entertainment, and China.


  Tencent Music Entertainment Group''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, pricing, and 12 more developer resources.'
random_paper: 12
score:
  band: emerging
  composite: 14.3
  coverage:
    artifact_dirs: 11
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -9.4
  facets:
    access_clarity: 15.8
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 32.1
    discoverability: 48.2
    operational_transparency: 5.3
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - china
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - greater-china
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 23.7
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
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/tencent-music-entertainment-group/tencent-music-entertainment-group-2026-11-03T144439.png
security:
- kind: domain-security
  name: Tencent Music Entertainment Group Domain Security
  slug: tencent-music-entertainment-group-domain-security
  summary_line: TLSv1.3 · DMARC
slug: tencent-music-entertainment-group
tags:
- Company
- Music
- Streaming
- Entertainment
- China
website: https://www.tencentmusic.com/
---
