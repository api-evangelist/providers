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
  scored_at: '2026-09-04'
api_count: 0
artifact_total: 3
common:
- group: company
  title: ''
  type: Website
  url: https://www.tungee.com
- group: company
  title: ''
  type: Blog
  url: https://www.tungee.com/about/media-report/1/
- group: operate
  title: ''
  type: Support
  url: https://www.tungee.com/about/intro/#contact
- group: start
  title: ''
  type: SignUp
  url: https://www.tungee.com/register/
- group: start
  title: ''
  type: Login
  url: https://user.tungee.com
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.tungee.com/services-agreement/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.tungee.com/privacy-policy/
- group: auth
  title: ''
  type: DomainSecurity
  url: security/tungee-domain-security.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/tungee-llms.txt
- group: commercial
  title: ''
  type: Plans
  url: plans/tungee-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/tungee-rate-limits.yml
coverage:
  checked: '2026-08-14'
  detail: 'Tungee markets an open API on its CRM integration page ("API接口灵活调用 -- 提供灵活开放的数据和功能调用接口，0代码对接") but publishes no reference for it anywhere: no developer host resolves in DNS (api./open./openapi./docs./developer. tungee.com are all NXDOMAIN) and the only route to it is an authenticated tenant at user.tungee.com.'
  evidence:
  - status: 200
    url: https://www.tungee.com/solution/integrate/
  - status: 200
    url: https://www.tungee.com/sitemap-0.xml
  - status: 404
    url: https://www.tungee.com/.well-known/api-catalog
  - status: 404
    url: https://futern.com/openapi.json
  reason: customer-only-docs
  state: gated
created: '2026-07-17'
description: Tungee (Guangzhou Tungee Technology Co., Ltd., 探迹科技) is a Chinese AI sales-intelligence company backed by Qiming Venture Partners. Its Tungee AI Sales Cloud covers the full B2B sales cycle -- AI prospecting over a 300M+ company knowledge graph, inbound capture, outreach via call center, SMS, and email, and an AI CRM -- plus a Sales GPT agent line, a mobile app, and a DingTalk edition. The group also operates Futern, an international B2B leads product, and reports 50,000+ customers. Tungee publishes no public developer portal or API documentation.
image: https://cdn.tungee.com/warehouse/logo/T.png
layout: provider
modified: '2026-08-14'
name: Tungee
nav: Providers
network: true
overview: 'Tungee is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Sales Intelligence, CRM, Lead Generation, and AI Agents.


  Tungee''s developer surface includes engineering blog, support, signup flow, and 8 more developer resources.'
plans:
- name: Tungee Plans Pricing
  plan_count: 0
  slug: tungee-plans-pricing
random_paper: 18
rate_limits:
- limit_count: 0
  name: Tungee Rate Limits
  slug: tungee-rate-limits
score:
  band: emerging
  composite: 14.0
  coverage:
    artifact_dirs: 7
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 34.2
    commercial_clarity: 34.2
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 7.1
    discoverability: 57.4
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 14.0
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/tungee/refs/heads/main/screenshots/tungee-2026-09-02T164527.png
security:
- kind: domain-security
  name: Tungee Domain Security
  slug: tungee-domain-security
  summary_line: TLSv1.2
slug: tungee
tags:
- Company
- Sales Intelligence
- CRM
- Lead Generation
- AI Agents
- B2B Data
- China
website: https://www.tungee.com
---
