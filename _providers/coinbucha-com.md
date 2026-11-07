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
    mcp_server: documented
    mcp_tool_quality: na
    openapi_examples: verified
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 25.6
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Coinbucha Com Agentic Access
  operation_count: 3
  slug: coinbucha-com-agentic-access
  summary_line: 3 operations
api_count: 1
apis:
- baseURL: https://coinbucha.com
  baseurl_source: declared
  description: The bitcoin API from CoinBucha — 3 operation(s) for bitcoin.
  name: CoinBucha Bitcoin API
  slug: coinbucha-com-bitcoin-api
artifact_total: 6
common:
- group: agent
  href: https://artifacts.apis.io/coinbucha-com/agentic-access/coinbucha-com-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/coinbucha-com-agentic-access.yml
- group: design
  href: https://artifacts.apis.io/coinbucha-com/rules/coinbucha-com-rules.yml
  title: ''
  type: Spectral
  url: rules/coinbucha-com-rules.yml
- group: design
  href: https://artifacts.apis.io/coinbucha-com/vocabulary/coinbucha-com-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/coinbucha-com-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/coinbucha-com/errors/coinbucha-com-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/coinbucha-com-problem-types.yml
- group: design
  href: https://artifacts.apis.io/coinbucha-com/conformance/coinbucha-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/coinbucha-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/coinbucha-com/llms/coinbucha-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/coinbucha-com-llms.txt
- group: agent
  href: https://artifacts.apis.io/coinbucha-com/mcp/coinbucha-com-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/coinbucha-com-mcp.yml
- group: other
  href: https://artifacts.apis.io/coinbucha-com/hosts/coinbucha-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/coinbucha-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/coinbucha-com/vendors/coinbucha-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/coinbucha-com-vendors.yml
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://coinbucha.com/privacy
- group: commercial
  title: ''
  type: Pricing
  url: https://coinbucha.com/pricing
- group: auth
  href: https://artifacts.apis.io/coinbucha-com/security/coinbucha-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/coinbucha-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://coinbucha.com/
created: '2026-11-04'
description: CoinBucha provides a listed Bitcoin index aggregating publicly filed holdings of companies that own Bitcoin. It offers free data, CSV downloads, and a Machine-Readable API (MCP) for AI agents. The service includes pricing tiers, privacy policy, and detailed documentation of its Bitcoin signal intelligence platform.
image: https://coinbucha.com/og-card-2026-10.png
layout: provider
mcp_servers:
- description: Remote MCP server at coinbucha.com.
  name: CoinBucha MCP Server
  slug: coinbucha-com-mcp-yml
modified: '2026-11-04'
name: CoinBucha
nav: Providers
network: true
overview: 'CoinBucha publishes 1 API contract indexed on the [APIs.io](https://apis.io/) network: Bitcoin API. Tagged areas include Company, Bitcoin, Index, and Data.


  The CoinBucha catalog on APIs.io includes 1 Spectral governance ruleset.


  CoinBucha''s developer surface includes pricing and 12 more developer resources.'
plans:
- name: Coinbucha Com Plans Pricing
  plan_count: 0
  slug: coinbucha-com-plans-pricing
random_paper: 8
rules:
- authorship: generated
  effective_rule_count: 74
  extends:
  - spectral:oas
  name: CoinBucha API Rules
  rule_count: 33
  severity_counts:
    error: 31
    hint: 0
    info: 1
    warn: 1
  slug: coinbucha-com-rules
score:
  band: emerging
  composite: 24.9
  coverage:
    artifact_dirs: 15
    catalog_earned: 37.8
    catalog_earned_first_party: 0.0
    catalog_gap: 77.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 21.1
    contract_governance: 22.0
    contract_quality: 49.6
    developer_ergonomics: 0.0
    discoverability: 56.7
    operational_transparency: 0.0
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 1
    mcp: first-party
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 14.7
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Coinbucha Com Domain Security
  slug: coinbucha-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: coinbucha-com
tags:
- Company
- Bitcoin
- Index
- Data
website: https://coinbucha.com/
---
