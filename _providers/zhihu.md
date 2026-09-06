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
  schema_version: 0.2
  score: 0.0
  scored_at: '2026-09-05'
api_count: 0
artifact_total: 1
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/zhihu-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://zhihu.com
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.zhihu.com/term/zhihu-terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.zhihu.com/term/privacy
- group: company
  title: ''
  type: InvestorRelations
  url: https://ir.zhihu.com/
created: '2026-07-17'
description: 'Zhihu (知乎) is a Chinese online question-and-answer and knowledge-sharing community, often described as China''s answer to Quora, where users post questions and answers, follow topics and creators, and consume long-form content, columns, live sessions, e-books and short video. Founded in 2011 and headquartered in Beijing, Zhihu operates one of China''s largest online content communities and is dual-listed (NYSE: ZH; HKEX: 2390). It was surfaced in the API Evangelist network as a portfolio company of Qiming Venture Partners. As of this enrichment pass Zhihu publishes no public developer platform, open API, SDKs, or machine-readable API artifacts on its primary domain; this profile therefore captures company identity plus a probed domain-security posture rather than an API surface.'
image: https://static.zhihu.com/static/img/favicon.ico
layout: provider
modified: '2026-07-21'
name: Zhihu
nav: Providers
network: true
overview: Zhihu is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Media Entertainment, Q&A, Knowledge Sharing, and Community.
random_paper: 6
score:
  band: minimal
  composite: 9.2
  coverage:
    artifact_dirs: 2
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 21.1
    commercial_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 0.0
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - china
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - greater-china
  previous_composite: 9.2
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/zhihu/refs/heads/main/screenshots/zhihu-2026-09-02T171718.png
security:
- kind: domain-security
  name: Zhihu Domain Security
  slug: zhihu-domain-security
  summary_line: TLSv1.2 · DMARC
slug: zhihu
tags:
- Company
- Media Entertainment
- Q&A
- Knowledge Sharing
- Community
- Content Platform
- Social
- China
website: https://zhihu.com
---
