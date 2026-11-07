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
artifact_total: 1
common:
- group: agent
  href: https://artifacts.apis.io/cbest-ir/llms/cbest-ir-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/cbest-ir-llms.txt
- group: other
  href: https://artifacts.apis.io/cbest-ir/hosts/cbest-ir-hosts.yml
  title: ''
  type: Hosts
  url: hosts/cbest-ir-hosts.yml
- group: other
  href: https://artifacts.apis.io/cbest-ir/vendors/cbest-ir-vendors.yml
  title: ''
  type: Vendors
  url: vendors/cbest-ir-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.cbest.ir/lighting/terms
- group: start
  title: ''
  type: Login
  url: https://www.cbest.ir/lighting/provider/login
- group: auth
  href: https://artifacts.apis.io/cbest-ir/security/cbest-ir-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/cbest-ir-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.cbest.ir/
coverage:
  checked: '2026-11-04'
  detail: The provider's documentation site returns only a JavaScript shell with no machine‑readable API spec.
  evidence:
  - status: 200
    url: https://www.cbest.ir/
  reason: js-rendered-docs
  state: unreadable
created: '2026-11-04'
description: سیبست یک شرکت ایرانی است که در زمینه فروش و نصب لامپ‌های LED و تجهیزات روشنایی فعالیت می‌کند. وب‌سایت این شرکت شامل اطلاعاتی درباره محصولات، خدمات نصب، تماس با ما، شرایط استفاده و لینک‌های مرتبط با تأمین‌کنندگان می‌باشد. این شرکت همچنین دارای بخش MCP برای مدیریت محتوا و ارتباط با مشتریان است.
image: https://www.cbest.ir/assets/og-cbest.png
layout: provider
modified: '2026-11-04'
name: سیبست
nav: Providers
network: true
overview: سیبست is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company.
random_paper: 1
score:
  band: minimal
  composite: 5.2
  coverage:
    artifact_dirs: 7
    catalog_earned: 22.0
    catalog_earned_first_party: 0.0
    catalog_gap: 93.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 11.8
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 39.3
    operational_transparency: 0.0
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - iran
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 7.8
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Cbest Ir Domain Security
  slug: cbest-ir-domain-security
  summary_line: TLSv1.3 · HSTS
slug: cbest-ir
tags:
- Company
website: https://www.cbest.ir/
---
