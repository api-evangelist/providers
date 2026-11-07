---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - authentication
  - rate-limits
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: conformant
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: true
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 32.4
  scored_at: '2026-11-06'
api_count: 1
apis:
- baseURL: https://api.barker.money
  baseurl_source: declared
  description: 'Barker Money API as documented publicly: 9 operations. Contract generated from the documentation by API Evangelist (2026-11-02); not the provider''s own document.'
  name: Barker Money API
  slug: barker-money-api
artifact_total: 10
asyncapis:
- description: ''
  name: Barker Money Webhooks
  slug: barker-money-webhooks
common:
- group: operate
  href: https://artifacts.apis.io/barker-money/rate-limits/barker-money-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/barker-money-rate-limits.yml
- group: design
  href: https://artifacts.apis.io/barker-money/rules/barker-money-rules.yml
  title: ''
  type: Spectral
  url: rules/barker-money-rules.yml
- group: design
  href: https://artifacts.apis.io/barker-money/json-ld/barker-money-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/barker-money-context.jsonld
- group: design
  href: https://artifacts.apis.io/barker-money/vocabulary/barker-money-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/barker-money-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/barker-money/asyncapi/barker-money-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/barker-money-webhooks.yml
- group: design
  href: https://artifacts.apis.io/barker-money/data-model/barker-money-data-model.yml
  title: ''
  type: DataModel
  url: data-model/barker-money-data-model.yml
- group: operate
  href: https://artifacts.apis.io/barker-money/changelog/barker-money-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/barker-money-changelog.yml
- group: auth
  href: https://artifacts.apis.io/barker-money/authentication/barker-money-authentication.yml
  title: ''
  type: Authentication
  url: authentication/barker-money-authentication.yml
- group: design
  href: https://artifacts.apis.io/barker-money/errors/barker-money-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/barker-money-problem-types.yml
- group: design
  href: https://artifacts.apis.io/barker-money/conformance/barker-money-conformance.yml
  title: ''
  type: Conformance
  url: conformance/barker-money-conformance.yml
- group: agent
  href: https://artifacts.apis.io/barker-money/llms/barker-money-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/barker-money-llms.txt
- group: other
  href: https://artifacts.apis.io/barker-money/a2a/barker-money-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/barker-money-a2a.yml
- group: agent
  href: https://artifacts.apis.io/barker-money/well-known/barker-money-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/barker-money-well-known.yml
- group: other
  href: https://artifacts.apis.io/barker-money/hosts/barker-money-hosts.yml
  title: ''
  type: Hosts
  url: hosts/barker-money-hosts.yml
- group: other
  href: https://artifacts.apis.io/barker-money/vendors/barker-money-vendors.yml
  title: ''
  type: Vendors
  url: vendors/barker-money-vendors.yml
- group: build
  href: https://artifacts.apis.io/barker-money/packages/barker-money-packages.yml
  title: ''
  type: SDKs
  url: packages/barker-money-packages.yml
- group: build
  href: https://artifacts.apis.io/barker-money/packages/barker-money-packages.yml
  title: ''
  type: Packages
  url: packages/barker-money-packages.yml
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.barker.money/quickstart
- group: docs
  title: ''
  type: Documentation
  url: https://docs.barker.money/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.barker.money/llms.txt
- group: auth
  href: https://artifacts.apis.io/barker-money/security/barker-money-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/barker-money-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://barker.money/
coverage:
  checked: '2026-11-02'
  detail: The provider's website offers HTML documentation but no publicly accessible OpenAPI, GraphQL, AsyncAPI, gRPC, or WSDL specifications.
  evidence:
  - status: 200
    url: https://barker.money/
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-11-02'
description: Barker Money provides a non-custodial yield primitive for the agent economy, enabling agents to route idle stablecoins to the best on‑chain yield opportunities with a single call. The platform aggregates liquidity across multiple vaults and LP pools, offering risk‑checked, automated routing and settlement. With over $12M of stablecoins deployed, Barker serves more than 50,000 active users, delivering transparent fee structures and real‑time APY pricing. It supports multilingual access, community resources, and integrates with popular agents via MCP and x402 protocols.
image: https://app.barker.money/images/twitter/twitter-og-image.png?v=d63559c9
json_schemas:
- name: GetApiPartnerProductsResponse
  property_count: 1
  slug: barker-money-get-api-partner-products-response
- name: GetProductsSlugPositionResponse
  property_count: 3
  slug: barker-money-get-products-slug-position-response
- name: GetProductsSlugYieldCalcResponse
  property_count: 2
  slug: barker-money-get-products-slug-yield-calc-response
jsonld:
- class_count: 3
  name: Barker Money Context
  property_count: 6
  slug: barker-money-context
layout: provider
modified: '2026-11-02'
name: Barker Money
nav: Providers
network: true
overview: 'Barker Money is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Finance, Cryptocurrency, Yield, DeFi, and AgentEconomy.


  The Barker Money catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 1 Spectral governance ruleset.


  Barker Money''s developer surface includes changelog, authentication, getting-started guide, documentation, API reference, and 17 more developer resources.'
random_paper: 4
rate_limits:
- limit_count: 2
  name: Barker Money Rate Limits
  slug: barker-money-rate-limits
rules:
- authorship: generated
  effective_rule_count: 83
  extends:
  - spectral:oas
  name: Barker Money API Rules
  rule_count: 42
  severity_counts:
    error: 40
    hint: 0
    info: 1
    warn: 1
  slug: barker-money-rules
score:
  band: thin
  composite: 29.3
  coverage:
    artifact_dirs: 22
    catalog_earned: 64.8
    catalog_earned_first_party: 8.0
    catalog_gap: 50.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 0.0
    contract_governance: 22.0
    contract_quality: 29.2
    developer_ergonomics: 33.3
    discoverability: 66.1
    operational_transparency: 44.7
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 1
      marker_coverage: 100.0
      total: 1
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 16.7
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Barker Money Authentication
  slug: barker-money-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Barker Money Domain Security
  slug: barker-money-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: barker-money
tags:
- Finance
- Cryptocurrency
- Yield
- DeFi
- AgentEconomy
website: https://barker.money/
---
