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
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 2.5
  scored_at: '2026-09-03'
api_count: 0
artifact_total: 3
common:
- group: company
  title: ''
  type: Website
  url: https://www.coohua.com/about.html
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.coohua.com/terms.html
- group: operate
  title: ''
  type: Support
  url: https://www.coohua.com/faq.html
- group: operate
  title: ''
  type: Contact
  url: https://www.coohua.com/contact.html
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/coohua-dev
- group: build
  title: ''
  type: Packages
  url: packages/coohua-packages.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/coohua-domain-security.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/coohua-llms.txt
- group: commercial
  title: ''
  type: Plans
  url: plans/coohua-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/coohua-rate-limits.yml
coverage:
  checked: '2026-08-12'
  detail: Coohua ships consumer reward apps and sells lock-screen ad inventory by email (sale@coohua.com on its 广告合作 page); its own coohua.cn domain is dead — the apex has no A record and www/api/open/developer/docs are a DNS wildcard to 39.106.94.60 that answers openresty HTTP 500 on every path, including "/" — while the surviving coohua.com pages carry no developer, API or SDK entry anywhere in their navigation.
  evidence:
  - status: 500
    url: http://developer.coohua.cn/
  - status: 500
    url: http://api.coohua.cn/
  - status: 200
    url: https://www.coohua.com/partner.html
  - status: 404
    url: https://www.coohua.com/.well-known/agent-card.json
  - status: 404
    url: https://www.coohua.com/openapi.json
  reason: no-developer-program
  state: none
created: '2026-07-17'
description: Coohua (酷划在线) is a Beijing-based Chinese mobile advertising company founded in 2014 and backed by Qiming Venture Partners. It pioneered the incentive- and lock-screen-advertising model in China, rewarding users with cash for unlocking their screens, reading content, and engaging with ads. Its flagship products include Coohua Lockscreen (酷划锁屏) and the Tao News (淘新闻) reading-rewards app, serving advertisers across internet, finance, automotive, and e-commerce verticals. At its peak Coohua captured a majority share of China's lock-screen advertising market and returned billions of yuan in cash rewards to users annually. No public API, developer portal, SDK, or machine-readable specification could be found during enrichment; advertising business is transacted through a sales contact (sale@coohua.com) on the 广告合作 page rather than through any self-serve or programmatic surface. The company does maintain a GitHub organization (github.com/coohua-dev) publishing CocoaPods spec repositories
  for the iOS modules behind its two apps, but every podspec resolves its source to an unreachable internal gitlab.coohua.com host, so none of it is consumable by a third party. This profile is retained as a company/provider record surfaced from the Qiming portfolio.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/coohua.png
layout: provider
modified: '2026-08-12'
name: coohua
nav: Providers
network: true
overview: 'coohua is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Advertising, Mobile, AdTech, and Incentive Advertising.


  coohua''s developer surface includes support and 9 more developer resources.'
plans:
- name: Coohua Plans Pricing
  plan_count: 0
  slug: coohua-plans-pricing
random_paper: 9
rate_limits:
- limit_count: 0
  name: Coohua Rate Limits
  slug: coohua-rate-limits
score:
  band: minimal
  composite: 8.4
  coverage:
    artifact_dirs: 6
    catalog_gap: 88.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 10.5
    commercial_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 4.8
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 2.6
  previous_composite: 8.4
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
security:
- kind: domain-security
  name: Coohua Domain Security
  slug: coohua-domain-security
  summary_line: TLSv1.2
slug: coohua
tags:
- Company
- Advertising
- Mobile
- AdTech
- Incentive Advertising
- China
- Consumer
website: https://www.coohua.com/about.html
---
