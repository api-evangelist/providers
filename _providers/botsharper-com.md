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
  band: agent-aware
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
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 12.9
  scored_at: '2026-11-06'
api_count: 2
apis:
- description: API for BotSharper providing analytics and bot testing endpoints.
  name: BotSharper API
  slug: botsharper-api
- description: 'BotSharper API as documented publicly: 1 operations. Contract generated from the documentation by API Evangelist (2026-11-03); not the provider''s own document.'
  name: BotSharper API
  slug: botsharper-com-api
artifact_total: 6
common:
- group: design
  href: https://artifacts.apis.io/botsharper-com/rules/botsharper-com-rules.yml
  title: ''
  type: Spectral
  url: rules/botsharper-com-rules.yml
- group: design
  href: https://artifacts.apis.io/botsharper-com/json-ld/botsharper-com-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/botsharper-com-context.jsonld
- group: design
  href: https://artifacts.apis.io/botsharper-com/vocabulary/botsharper-com-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/botsharper-com-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/botsharper-com/data-model/botsharper-com-data-model.yml
  title: ''
  type: DataModel
  url: data-model/botsharper-com-data-model.yml
- group: design
  href: https://artifacts.apis.io/botsharper-com/conformance/botsharper-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/botsharper-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/botsharper-com/llms/botsharper-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/botsharper-com-llms.txt
- group: other
  href: https://artifacts.apis.io/botsharper-com/hosts/botsharper-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/botsharper-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/botsharper-com/vendors/botsharper-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/botsharper-com-vendors.yml
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://botsharper.com/privacy
- group: other
  title: ''
  type: Leadership
  url: https://botsharper.com/team/bwamJzztZsepfkteWRChggmXuiiCQvpLqPietdNfSXa
- group: auth
  href: https://artifacts.apis.io/botsharper-com/security/botsharper-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/botsharper-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://botsharper.com/
- group: other
  title: ''
  type: Image
  url: https://botsharper.com/og.png
- group: docs
  title: ''
  type: Documentation
  url: https://botsharper.com/pro
- group: operate
  title: ''
  type: Support
  url: https://t.me/BotSharperBot
coverage:
  checked: '2026-11-03'
  detail: Documentation page provides HTML only, no OpenAPI or other machine-readable contract.
  evidence:
  - status: 200
    url: https://botsharper.com/pro
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-11-02'
description: BotSharper provides a free web tool to test and tune Solana trading bots on real pump.fun data. Users can replay bot settings, check profitability, view token launch rankings, and access a Pro API for private connector integration. The service operates without requiring wallet connections, offering analytics, token checks, and multilingual support.
image: https://botsharper.com/og.png
json_schemas:
- name: PostMcpRequest
  property_count: 4
  slug: botsharper-com-post-mcp-request
jsonld:
- class_count: 1
  name: Botsharper Com Context
  property_count: 4
  slug: botsharper-com-context
layout: provider
modified: '2026-11-02'
name: BotSharper
nav: Providers
network: true
overview: 'BotSharper is listed with 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Finance, Solana, TradingBots, and Analytics.


  The BotSharper catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  BotSharper''s developer surface includes documentation, support, and 13 more developer resources.'
random_paper: 6
rules:
- authorship: generated
  effective_rule_count: 71
  extends:
  - spectral:oas
  name: BotSharper API Rules
  rule_count: 30
  severity_counts:
    error: 28
    hint: 0
    info: 1
    warn: 1
  slug: botsharper-com-rules
score:
  band: emerging
  composite: 14.0
  coverage:
    artifact_dirs: 15
    catalog_earned: 43.2
    catalog_earned_first_party: 0.0
    catalog_gap: 71.9
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 5.3
    contract_governance: 22.0
    contract_quality: 17.4
    developer_ergonomics: 7.1
    discoverability: 49.1
    operational_transparency: 0.0
  provenance:
    conformance: derived
    contracts:
      callable: 0.0
      derived: 1
      marker_coverage: 100.0
      total: 1
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 12.7
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Botsharper Com Domain Security
  slug: botsharper-com-domain-security
  summary_line: TLSv1.3 · HSTS
slug: botsharper-com
tags:
- Finance
- Solana
- TradingBots
- Analytics
website: https://botsharper.com/
---
