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
api_count: 1
apis:
- description: Developer API for CashbackPro partners, documented at the How Cashback Works guide.
  name: CashbackPro API
  slug: cashbackpro-api
artifact_total: 2
common:
- group: operate
  href: https://artifacts.apis.io/cashbackpro-org/changelog/cashbackpro-org-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/cashbackpro-org-changelog.yml
- group: agent
  href: https://artifacts.apis.io/cashbackpro-org/llms/cashbackpro-org-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/cashbackpro-org-llms.txt
- group: other
  href: https://artifacts.apis.io/cashbackpro-org/hosts/cashbackpro-org-hosts.yml
  title: ''
  type: Hosts
  url: hosts/cashbackpro-org-hosts.yml
- group: other
  href: https://artifacts.apis.io/cashbackpro-org/vendors/cashbackpro-org-vendors.yml
  title: ''
  type: Vendors
  url: vendors/cashbackpro-org-vendors.yml
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://cashbackpro.org/privacypolicy
- group: docs
  title: ''
  type: Documentation
  url: https://cashbackpro.org/guides/how-cashback-works
- group: operate
  title: ''
  type: ChangeLog
  url: https://cashbackpro.org/whats-new
- group: company
  title: ''
  type: Blog
  url: https://cashbackpro.org/blog
- group: auth
  href: https://artifacts.apis.io/cashbackpro-org/security/cashbackpro-org-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/cashbackpro-org-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://cashbackpro.org/
coverage:
  checked: '2026-11-04'
  detail: OpenAPI spec not found at https://api.cashbackpro.org/openapi.json (404).
  evidence:
  - status: 404
    url: https://api.cashbackpro.org/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-11-04'
description: CashbackPro is a free affiliate cashback platform for AliExpress, offering users up to 15% back on purchases. It features multiple loyalty levels, automatic order tracking, and a referral bonus. The service operates globally, supporting English, Russian, and Hebrew languages, and provides detailed analytics and a developer-friendly API for partners.
image: https://cashbackpro.org/og-image.png
layout: provider
modified: '2026-11-04'
name: CashbackPro
nav: Providers
network: true
overview: 'CashbackPro is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Cashback, Affiliates, AliExpress, Rewards, and E-Commerce.


  CashbackPro''s developer surface includes changelog, documentation, engineering blog, and 7 more developer resources.'
random_paper: 14
score:
  band: minimal
  composite: 7.9
  coverage:
    artifact_dirs: 8
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 5.3
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 6.0
    discoverability: 57.1
    operational_transparency: 7.9
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
  name: Cashbackpro Org Domain Security
  slug: cashbackpro-org-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: cashbackpro-org
tags:
- Cashback
- Affiliates
- AliExpress
- Rewards
- E-Commerce
website: https://cashbackpro.org/
---
