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
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 21.4
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 1
  human_in_the_loop: 0
  name: Accsly Io Agentic Access
  operation_count: 14
  slug: accsly-io-agentic-access
  summary_line: 14 operations · 1 acting
api_count: 1
apis:
- description: 'Read-only price data of accsly.io: VPS/VDS, shared hosting and dedicated plans.'
  name: Accsly Agent API
  slug: accsly-agent-api
- baseURL: https://accsly.io
  baseurl_source: spec
  description: The Accounts API from Accsly — 1 operation(s) for accounts.
  name: Accsly Accounts API
  slug: accsly-io-accounts-api
- baseURL: https://accsly.io
  baseurl_source: spec
  description: The Markdown pages API from Accsly — 10 operation(s) for markdown pages.
  name: Accsly Markdown pages API
  slug: accsly-io-markdown-pages-api
- baseURL: https://accsly.io
  baseurl_source: spec
  description: The MCP API from Accsly — 1 operation(s) for mcp.
  name: Accsly MCP API
  slug: accsly-io-mcp-api
- baseURL: https://accsly.io
  baseurl_source: spec
  description: The VPS API from Accsly — 2 operation(s) for vps.
  name: Accsly VPS API
  slug: accsly-io-vps-api
artifact_total: 9
common:
- group: agent
  href: https://artifacts.apis.io/accsly-io/agentic-access/accsly-io-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/accsly-io-agentic-access.yml
- group: design
  href: https://artifacts.apis.io/accsly-io/rules/accsly-io-rules.yml
  title: ''
  type: Spectral
  url: rules/accsly-io-rules.yml
- group: design
  href: https://artifacts.apis.io/accsly-io/json-ld/accsly-io-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/accsly-io-context.jsonld
- group: design
  href: https://artifacts.apis.io/accsly-io/vocabulary/accsly-io-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/accsly-io-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/accsly-io/data-model/accsly-io-data-model.yml
  title: ''
  type: DataModel
  url: data-model/accsly-io-data-model.yml
- group: design
  href: https://artifacts.apis.io/accsly-io/errors/accsly-io-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/accsly-io-problem-types.yml
- group: design
  href: https://artifacts.apis.io/accsly-io/conformance/accsly-io-conformance.yml
  title: ''
  type: Conformance
  url: conformance/accsly-io-conformance.yml
- group: agent
  href: https://artifacts.apis.io/accsly-io/llms/accsly-io-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/accsly-io-llms.txt
- group: other
  href: https://artifacts.apis.io/accsly-io/hosts/accsly-io-hosts.yml
  title: ''
  type: Hosts
  url: hosts/accsly-io-hosts.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://accsly.io/ru/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://accsly.io/ru/privacy
- group: company
  title: ''
  type: Blog
  url: https://accsly.io/ru/blog
- group: auth
  href: https://artifacts.apis.io/accsly-io/security/accsly-io-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/accsly-io-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://accsly.io
created: '2026-10-28'
description: Accsly offers a marketplace for buying cheap accounts for services such as Telegram, Steam, Google/Gmail, TikTok, Discord, email, games, and AI tools. The site aggregates verified shop offers into a catalog, allowing users to compare prices and purchase directly from sellers.
image: https://accsly.io/og/card?title=%D0%90%D0%B3%D1%80%D0%B5%D0%B3%D0%B0%D1%82%D0%BE%D1%80%20%D1%86%D0%B8%D1%84%D1%80%D0%BE%D0%B2%D1%8B%D1%85%20%D1%82%D0%BE%D0%B2%D0%B0%D1%80%D0%BE%D0%B2%20%D0%B8%20%D1%83%D1%81%D0%BB%D1%83%D0%B3&sub=%D1%81%D1%80%D0%B0%D0%B2%D0%BD%D0%B8%20%D1%86%D0%B5%D0%BD%D1%8B%20%D0%B8%20%D0%BA%D1%83%D0%BF%D0%B8%20%D0%B2%D1%8B%D0%B3%D0%BE%D0%B4%D0%BD%D0%BE
jsonld:
- class_count: 5
  name: Accsly Io Context
  property_count: 42
  slug: accsly-io-context
layout: provider
modified: '2026-10-28'
name: Accsly
nav: Providers
network: true
overview: 'Accsly publishes 5 API contracts indexed on the [APIs.io](https://apis.io/) network, including Accounts API, Markdown pages API, MCP API, and 2 more. Tagged areas include Marketplace, Account, Gaming, AI Tools, and E-Commerce.


  The Accsly catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Accsly''s developer surface includes engineering blog and 13 more developer resources.'
random_paper: 12
rules:
- authorship: generated
  effective_rule_count: 54
  extends:
  - spectral:oas
  name: Accsly API Rules
  rule_count: 13
  severity_counts:
    error: 11
    hint: 0
    info: 1
    warn: 1
  slug: accsly-io-rules
score:
  band: emerging
  composite: 24.0
  coverage:
    artifact_dirs: 17
    catalog_earned: 48.8
    catalog_earned_first_party: 0.0
    catalog_gap: 66.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -2.9
  facets:
    access_clarity: 10.5
    contract_governance: 22.0
    contract_quality: 53.4
    developer_ergonomics: 1.2
    discoverability: 64.3
    operational_transparency: 0.0
  previous_composite: 26.9
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 4
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 14.7
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/accsly-io/accsly-io-2026-11-03T120203.png
security:
- kind: domain-security
  name: Accsly Io Domain Security
  slug: accsly-io-domain-security
  summary_line: TLSv1.3 · DMARC
slug: accsly-io
tags:
- Marketplace
- Account
- Gaming
- AI Tools
- E-Commerce
website: https://accsly.io
---
