---
access_model:
  confidence: high
  gated: none
  gated_source:
  - onboarding
  label: Freemium · Open access
  onboarding: open
  pricing: freemium
  public: true
  source:
  - plans
  - authentication
  - rate-limits
  - security
  trial: false
  try_now: true
agent_readiness:
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: false
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: derived
    event_surface_described: false
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 5.0
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 1
  human_in_the_loop: 0
  name: Adson Jp Agentic Access
  operation_count: 1
  slug: adson-jp-agentic-access
  summary_line: 1 operation · 1 acting
api_count: 1
apis:
- description: Extract a public website into JSON with company/site intelligence.
  name: Japan Data API
  slug: japan-data-api
artifact_total: 8
common:
- group: agent
  href: https://artifacts.apis.io/adson-jp/agentic-access/adson-jp-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/adson-jp-agentic-access.yml
- group: design
  href: https://artifacts.apis.io/adson-jp/rules/adson-jp-rules.yml
  title: ''
  type: Spectral
  url: rules/adson-jp-rules.yml
- group: design
  href: https://artifacts.apis.io/adson-jp/errors/adson-jp-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/adson-jp-problem-types.yml
- group: design
  href: https://artifacts.apis.io/adson-jp/conformance/adson-jp-conformance.yml
  title: ''
  type: Conformance
  url: conformance/adson-jp-conformance.yml
- group: agent
  href: https://artifacts.apis.io/adson-jp/llms/adson-jp-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/adson-jp-llms.txt
- group: other
  href: https://artifacts.apis.io/adson-jp/hosts/adson-jp-hosts.yml
  title: ''
  type: Hosts
  url: hosts/adson-jp-hosts.yml
- group: other
  href: https://artifacts.apis.io/adson-jp/vendors/adson-jp-vendors.yml
  title: ''
  type: Vendors
  url: vendors/adson-jp-vendors.yml
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://app.adson.jp/privacy
- group: commercial
  title: ''
  type: Pricing
  url: https://app.adson.jp/pricing
- group: auth
  href: https://artifacts.apis.io/adson-jp/security/adson-jp-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/adson-jp-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://adson.jp/
created: '2026-11-01'
description: ADSON株式会社は、2020年に東京で設立されたデザイン・開発・事業運営の会社です。アプリ開発、ブランド、メディア、データ提供など多岐にわたるサービスを展開し、AI・WebアプリやデータAPIを提供しています。無料相談や問い合わせ窓口も設け、顧客のアイデアを形にすることをミッションとしています。
image: https://adson.jp/images/ADSON%E3%83%96%E3%83%A9%E3%83%B3%E3%83%89%E3%83%AD%E3%82%B4%E5%8E%9F%E6%9C%AC.png
layout: provider
modified: '2026-11-01'
name: ADSON
nav: Providers
network: true
overview: 'ADSON is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Design, Development, Media, and Data.


  The ADSON catalog on APIs.io includes 1 Spectral governance ruleset.


  ADSON''s developer surface includes pricing and 10 more developer resources.'
plans:
- name: Adson Jp Plans Pricing
  plan_count: 2
  slug: adson-jp-plans-pricing
random_paper: 4
rate_limits:
- limit_count: 3
  name: Adson Jp Rate Limits
  slug: adson-jp-rate-limits
rules:
- authorship: generated
  effective_rule_count: 50
  extends:
  - spectral:oas
  name: ADSON API Rules
  rule_count: 9
  severity_counts:
    error: 7
    hint: 0
    info: 1
    warn: 1
  slug: adson-jp-rules
scopes:
- name: Adson Jp Scopes
  scope_count: 0
  slug: adson-jp-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: emerging
  composite: 19.2
  coverage:
    artifact_dirs: 20
    catalog_earned: 56.5
    catalog_earned_first_party: 20.0
    catalog_gap: 58.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -2.4
  facets:
    access_clarity: 31.6
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 57.1
    operational_transparency: 31.6
  previous_composite: 21.6
  provenance:
    agentic_access: derived
    conformance: derived
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 20.9
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Adson Jp Authentication
  slug: adson-jp-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Adson Jp Domain Security
  slug: adson-jp-domain-security
  summary_line: TLSv1.3
slug: adson-jp
tags:
- Company
- Design
- Development
- Media
- Data
- Artificial Intelligence
website: https://adson.jp/
---
