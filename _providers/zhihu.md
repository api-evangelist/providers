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
  scored_at: '2026-09-01'
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
    artifact_dirs: 1
    catalog_gap: 88.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
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
  previous_composite: 9.2
  schema_version: 0.18.0
  scored_at: '2026-09-01'
  trend: flat
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
