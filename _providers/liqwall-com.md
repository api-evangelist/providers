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
    mcp_server: documented
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
  score: 16.1
  scored_at: '2026-11-06'
api_count: 2
apis:
- description: Market data and MCP API providing real‑time crypto market data and analytics.
  name: Liqwall MCP
  slug: liqwall-mcp
- description: 'Liqwall API as documented publicly: 1 operations. Contract generated from the documentation by API Evangelist (2026-11-02); not the provider''s own document.'
  name: Liqwall API
  slug: liqwall-com-api
artifact_total: 7
common:
- group: design
  href: https://artifacts.apis.io/liqwall-com/rules/liqwall-com-rules.yml
  title: ''
  type: Spectral
  url: rules/liqwall-com-rules.yml
- group: design
  href: https://artifacts.apis.io/liqwall-com/json-ld/liqwall-com-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/liqwall-com-context.jsonld
- group: design
  href: https://artifacts.apis.io/liqwall-com/vocabulary/liqwall-com-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/liqwall-com-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/liqwall-com/data-model/liqwall-com-data-model.yml
  title: ''
  type: DataModel
  url: data-model/liqwall-com-data-model.yml
- group: design
  href: https://artifacts.apis.io/liqwall-com/conformance/liqwall-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/liqwall-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/liqwall-com/llms/liqwall-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/liqwall-com-llms.txt
- group: other
  href: https://artifacts.apis.io/liqwall-com/hosts/liqwall-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/liqwall-com-hosts.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://liqwall.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://liqwall.com/privacy
- group: company
  title: ''
  type: Newsroom
  url: https://liqwall.com/news
- group: auth
  href: https://artifacts.apis.io/liqwall-com/security/liqwall-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/liqwall-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://liqwall.com/
- group: docs
  title: ''
  type: Documentation
  url: https://liqwall.com/docs/mcp
coverage:
  checked: '2026-11-02'
  detail: Documentation at https://liqwall.com/docs/mcp is HTML without a machine‑readable OpenAPI or other contract.
  evidence:
  - status: 200
    url: https://liqwall.com/docs/mcp
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-11-02'
description: 'Liqwall provides crypto market data: liquidations, liquidation levels by exchange, order books of 14 exchanges, funding, open interest and Hyperliquid positions. Open endpoints need no key (/api/v1/free/fng, /api/v1/free/liqs, /api/v1/free/xmap), and its MCP server at https://liqwall.com/mcp is included in every plan, the free one too. Data download through the API with a key is on the Advanced plan ($499 a month).'
image: https://liqwall.com/brand/og.png
json_schemas:
- name: PostMcpRequest
  property_count: 4
  slug: liqwall-com-post-mcp-request
- name: PostMcpResponse
  property_count: 4
  slug: liqwall-com-post-mcp-response
jsonld:
- class_count: 2
  name: Liqwall Com Context
  property_count: 6
  slug: liqwall-com-context
layout: provider
modified: '2026-11-02'
name: Liqwall
nav: Providers
network: true
overview: 'Liqwall is listed with 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Cryptocurrency, Data, Visualization, Market Data, and Real-Time.


  The Liqwall catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Liqwall''s developer surface includes documentation and 12 more developer resources.'
random_paper: 18
rules:
- authorship: generated
  effective_rule_count: 73
  extends:
  - spectral:oas
  name: Liqwall API Rules
  rule_count: 32
  severity_counts:
    error: 30
    hint: 0
    info: 1
    warn: 1
  slug: liqwall-com-rules
score:
  band: emerging
  composite: 15.5
  coverage:
    artifact_dirs: 15
    catalog_earned: 51.8
    catalog_earned_first_party: 0.0
    catalog_gap: 63.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 10.5
    contract_governance: 22.0
    contract_quality: 19.9
    developer_ergonomics: 4.8
    discoverability: 58.0
    operational_transparency: 0.0
  provenance:
    conformance: derived
    contracts:
      callable: 0.0
      derived: 1
      marker_coverage: 100.0
      total: 1
    mcp: unknown
  regulatory:
    applies: true
    matched_via: tags
    regime: Securities & Market Data
    regime_id: securities_market_data
    score: 13.9
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Liqwall Com Domain Security
  slug: liqwall-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: liqwall-com
tags:
- Cryptocurrency
- Data
- Visualization
- Market Data
- Real-Time
- Company
website: https://liqwall.com/
---
