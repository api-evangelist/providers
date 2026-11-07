---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - authentication
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: unknown
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: na
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: false
    idempotency: na
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: verified
    operation_distinctiveness: na
    pagination_ratio: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 38.0
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Hasfiyat Agentic Access
  operation_count: 1
  slug: hasfiyat-agentic-access
  summary_line: 1 operation
api_count: 1
apis:
- baseURL: https://api.hasfiyat.com
  baseurl_source: spec
  description: Canlı altın, gümüş ve döviz fiyatları
  name: Hasfiyat Fiyatlar API
  slug: hasfiyat-fiyatlar-api
artifact_total: 7
common:
- group: agent
  href: https://artifacts.apis.io/hasfiyat/agentic-access/hasfiyat-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/hasfiyat-agentic-access.yml
- group: design
  href: https://artifacts.apis.io/hasfiyat/rules/hasfiyat-rules.yml
  title: ''
  type: Spectral
  url: rules/hasfiyat-rules.yml
- group: design
  href: https://artifacts.apis.io/hasfiyat/json-ld/hasfiyat-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/hasfiyat-context.jsonld
- group: design
  href: https://artifacts.apis.io/hasfiyat/vocabulary/hasfiyat-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/hasfiyat-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/hasfiyat/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/hasfiyat/data-model/hasfiyat-data-model.yml
  title: ''
  type: DataModel
  url: data-model/hasfiyat-data-model.yml
- group: design
  href: https://artifacts.apis.io/hasfiyat/errors/hasfiyat-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/hasfiyat-problem-types.yml
- group: design
  href: https://artifacts.apis.io/hasfiyat/conformance/hasfiyat-conformance.yml
  title: ''
  type: Conformance
  url: conformance/hasfiyat-conformance.yml
- group: agent
  href: https://artifacts.apis.io/hasfiyat/llms/hasfiyat-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/hasfiyat-llms.txt
- group: agent
  href: https://artifacts.apis.io/hasfiyat/well-known/hasfiyat-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/hasfiyat-well-known.yml
- group: other
  href: https://artifacts.apis.io/hasfiyat/hosts/hasfiyat-hosts.yml
  title: ''
  type: Hosts
  url: hosts/hasfiyat-hosts.yml
- group: company
  title: ''
  type: Blog
  url: https://hasfiyat.com/blog
- group: auth
  href: https://artifacts.apis.io/hasfiyat/authentication/hasfiyat-authentication.yml
  title: ''
  type: Authentication
  url: authentication/hasfiyat-authentication.yml
- group: auth
  href: https://artifacts.apis.io/hasfiyat/security/hasfiyat-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/hasfiyat-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://hasfiyat.com/
- group: docs
  title: ''
  type: APIReference
  url: https://altinapi.hasfiyat.com/
- group: start
  title: ''
  type: GettingStarted
  url: https://hasfiyat.com/premium
- group: operate
  title: ''
  type: Support
  url: https://hasfiyat.com/iletisim
- group: commercial
  title: ''
  type: Pricing
  url: https://hasfiyat.com/premium
created: '2026-10-17'
description: Hasfiyat provides a comprehensive software platform for jewelry businesses, offering real‑time gold and foreign‑exchange pricing, digital price boards, cash and ledger management, e‑invoice integration, KYC compliance, and customer portals across web, Windows and mobile. The solution streamlines operations, enhances pricing transparency, and supports regulatory requirements for Turkish jewelers.
image: https://hasfiyat.com/hasfiyat-og-v4.png
jsonld:
- class_count: 3
  name: Hasfiyat Context
  property_count: 13
  slug: hasfiyat-context
layout: provider
modified: '2026-10-17'
name: Hasfiyat
nav: Providers
network: true
overview: 'Hasfiyat publishes 1 API contract indexed on the [APIs.io](https://apis.io/) network: Fiyatlar API. Tagged areas include Company, Jewelry, Software, Pricing, and Management.


  The Hasfiyat catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Hasfiyat''s developer surface includes engineering blog, authentication, API reference, getting-started guide, support, pricing, and 13 more developer resources.'
random_paper: 17
rules:
- authorship: generated
  effective_rule_count: 59
  extends:
  - spectral:oas
  name: Hasfiyat API Rules
  rule_count: 18
  severity_counts:
    error: 16
    hint: 0
    info: 1
    warn: 1
  slug: hasfiyat-rules
score:
  band: thin
  composite: 30.6
  coverage:
    artifact_dirs: 21
    catalog_earned: 40.8
    catalog_earned_first_party: 0.0
    catalog_gap: 74.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -3.6
  facets:
    access_clarity: 5.3
    contract_governance: 22.0
    contract_quality: 59.3
    developer_ergonomics: 31.4
    discoverability: 55.4
    operational_transparency: 0.0
  previous_composite: 34.2
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 1
    mcp: derived
    skills: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 16.7
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: this provider''s published contracts declare no write operations, and a read-only API cannot create-or-update. Excluded from the denominator, not zeroed.'
    reason: read_only
screenshot: https://apis.io/screenshots/hasfiyat/hasfiyat-2026-11-03T133232.png
security:
- kind: authentication
  name: Hasfiyat Authentication
  slug: hasfiyat-authentication
  summary_line: apiKey/http · 2 schemes
- kind: domain-security
  name: Hasfiyat Domain Security
  slug: hasfiyat-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
skill_count: 1
skills:
- name: get-prices
  slug: hasfiyat-get-prices-skill
slug: hasfiyat
tags:
- Company
- Jewelry
- Software
- Pricing
- Management
website: https://hasfiyat.com/
---
