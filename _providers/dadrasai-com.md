---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - plans
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
    mcp_server: documented
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
  score: 3.1
  scored_at: '2026-11-06'
api_count: 0
artifact_total: 2
common:
- group: commercial
  href: https://artifacts.apis.io/dadrasai-com/plans/dadrasai-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/dadrasai-com-plans-pricing.yml
- group: agent
  href: https://artifacts.apis.io/dadrasai-com/llms/dadrasai-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/dadrasai-com-llms.txt
- group: other
  href: https://artifacts.apis.io/dadrasai-com/hosts/dadrasai-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/dadrasai-com-hosts.yml
- group: auth
  title: ''
  type: TrustCenter
  url: https://dadrasai.com/trust
- group: commercial
  title: ''
  type: TermsOfService
  url: https://dadrasai.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://dadrasai.com/privacy
- group: commercial
  title: ''
  type: Pricing
  url: https://dadrasai.com/pricing
- group: start
  title: ''
  type: Login
  url: https://dadrasai.com/login
- group: company
  title: ''
  type: Blog
  url: https://dadrasai.com/blog
- group: auth
  href: https://artifacts.apis.io/dadrasai-com/security/dadrasai-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/dadrasai-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://dadrasai.com/
coverage:
  checked: '2026-11-05'
  detail: The provider's website offers a legal AI platform but provides no public API documentation or machine‑readable contracts.
  evidence:
  - status: 200
    url: https://dadrasai.com/
  reason: no-developer-program
  state: none
created: '2026-11-04'
description: دادرس یک پلتفرم هوشمند حقوقی به زبان فارسی است که از هوش مصنوعی برای ارائه مشاوره حقوقی، جستجوی قوانین و آرای ایران، و مدیریت پرونده‌های حقوقی استفاده می‌کند. کاربران می‌توانند با پرسیدن سوالات حقوقی به فارسی، پاسخ‌های واضح همراه با ارجاع به متن قانون دریافت کنند. این سرویس شامل ابزارهای محاسبه‌گرهای حقوقی، تنظیم آنلاین دادخواست، لایحه و قرارداد، و امکان جستجوی پیشرفته در متون قانونی می‌باشد. هدف ارائه دستیار حقوقی هوشمند برای تسهیل دسترسی به اطلاعات حقوقی در ایران است.
image: https://dadrasai.com/og/site.png?v=9jqm5j
layout: provider
modified: '2026-11-04'
name: دادرس
nav: Providers
network: true
overview: 'دادرس is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Legal Tech, Artificial Intelligence, Persian, Platform, and Documentation.


  دادرس''s developer surface includes pricing, engineering blog, and 9 more developer resources.'
plans:
- name: Dadrasai Com Plans Pricing
  plan_count: 1
  slug: dadrasai-com-plans-pricing
random_paper: 13
score:
  band: emerging
  composite: 20.4
  coverage:
    artifact_dirs: 10
    catalog_earned: 35.0
    catalog_earned_first_party: 8.0
    catalog_gap: 80.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 73.7
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 2.4
    discoverability: 48.2
    operational_transparency: 0.0
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 17.3
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Dadrasai Com Domain Security
  slug: dadrasai-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: dadrasai-com
tags:
- Legal Tech
- Artificial Intelligence
- Persian
- Platform
- Documentation
- Company
website: https://dadrasai.com/
---
