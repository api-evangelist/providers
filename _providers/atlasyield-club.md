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
  band_gated_from: agent-native
  dimensions:
    agent_card: conformant
    agent_skills: unknown
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: derived
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    mcp_tool_quality: na
    openapi_examples: verified
    operation_distinctiveness: distinct
    pagination_ratio: false
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 53.3
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 1
  human_in_the_loop: 0
  name: Atlasyield Club Agentic Access
  operation_count: 8
  slug: atlasyield-club-agentic-access
  summary_line: 8 operations · 1 acting
api_count: 1
apis:
- baseURL: https://api.atlasyield.club/v1
  baseurl_source: declared
  description: The Basket API from AtlasYield — 1 operation(s) for basket.
  name: AtlasYield Basket API
  slug: atlasyield-club-basket-api
- baseURL: https://api.atlasyield.club/v1
  baseurl_source: declared
  description: The Catalog API from AtlasYield — 1 operation(s) for catalog.
  name: AtlasYield Catalog API
  slug: atlasyield-club-catalog-api
- baseURL: https://api.atlasyield.club/v1
  baseurl_source: declared
  description: The Gas API from AtlasYield — 1 operation(s) for gas.
  name: AtlasYield Gas API
  slug: atlasyield-club-gas-api
- baseURL: https://api.atlasyield.club/v1
  baseurl_source: declared
  description: The Portfolio API from AtlasYield — 1 operation(s) for portfolio.
  name: AtlasYield Portfolio API
  slug: atlasyield-club-portfolio-api
- baseURL: https://api.atlasyield.club/v1
  baseurl_source: declared
  description: The Scores API from AtlasYield — 1 operation(s) for scores.
  name: AtlasYield Scores API
  slug: atlasyield-club-scores-api
- baseURL: https://api.atlasyield.club/v1
  baseurl_source: declared
  description: The Vaults API from AtlasYield — 3 operation(s) for vaults.
  name: AtlasYield Vaults API
  slug: atlasyield-club-vaults-api
artifact_total: 21
common:
- group: agent
  href: https://artifacts.apis.io/atlasyield-club/agentic-access/atlasyield-club-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/atlasyield-club-agentic-access.yml
- group: operate
  href: https://artifacts.apis.io/atlasyield-club/rate-limits/atlasyield-club-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/atlasyield-club-rate-limits.yml
- group: design
  href: https://artifacts.apis.io/atlasyield-club/rules/atlasyield-club-rules.yml
  title: ''
  type: Spectral
  url: rules/atlasyield-club-rules.yml
- group: design
  href: https://artifacts.apis.io/atlasyield-club/json-ld/atlasyield-club-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/atlasyield-club-context.jsonld
- group: design
  href: https://artifacts.apis.io/atlasyield-club/vocabulary/atlasyield-club-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/atlasyield-club-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/atlasyield-club/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/atlasyield-club/data-model/atlasyield-club-data-model.yml
  title: ''
  type: DataModel
  url: data-model/atlasyield-club-data-model.yml
- group: auth
  href: https://artifacts.apis.io/atlasyield-club/authentication/atlasyield-club-authentication.yml
  title: ''
  type: Authentication
  url: authentication/atlasyield-club-authentication.yml
- group: design
  href: https://artifacts.apis.io/atlasyield-club/errors/atlasyield-club-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/atlasyield-club-problem-types.yml
- group: design
  href: https://artifacts.apis.io/atlasyield-club/conformance/atlasyield-club-conformance.yml
  title: ''
  type: Conformance
  url: conformance/atlasyield-club-conformance.yml
- group: agent
  href: https://artifacts.apis.io/atlasyield-club/llms/atlasyield-club-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/atlasyield-club-llms.txt
- group: other
  href: https://artifacts.apis.io/atlasyield-club/a2a/atlasyield-club-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/atlasyield-club-a2a.yml
- group: build
  href: https://artifacts.apis.io/atlasyield-club/mcp/atlasyield-club-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/atlasyield-club-tool-crosswalk.yml
- group: agent
  href: https://artifacts.apis.io/atlasyield-club/mcp/atlasyield-club-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/atlasyield-club-mcp.yml
- group: agent
  href: https://artifacts.apis.io/atlasyield-club/well-known/atlasyield-club-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/atlasyield-club-well-known.yml
- group: other
  href: https://artifacts.apis.io/atlasyield-club/hosts/atlasyield-club-hosts.yml
  title: ''
  type: Hosts
  url: hosts/atlasyield-club-hosts.yml
- group: other
  href: https://artifacts.apis.io/atlasyield-club/vendors/atlasyield-club-vendors.yml
  title: ''
  type: Vendors
  url: vendors/atlasyield-club-vendors.yml
- group: build
  href: https://artifacts.apis.io/atlasyield-club/packages/atlasyield-club-packages.yml
  title: ''
  type: SDKs
  url: packages/atlasyield-club-packages.yml
- group: build
  href: https://artifacts.apis.io/atlasyield-club/packages/atlasyield-club-packages.yml
  title: ''
  type: Packages
  url: packages/atlasyield-club-packages.yml
- group: auth
  title: ''
  type: TrustCenter
  url: https://atlasyield.club/trust
- group: start
  title: ''
  type: Login
  url: https://atlasyield.club/login
- group: auth
  href: https://artifacts.apis.io/atlasyield-club/security/atlasyield-club-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/atlasyield-club-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://atlasyield.club/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.atlasyield.club/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.atlasyield.club/api-reference/introduction
- group: operate
  title: ''
  type: Support
  url: https://docs.atlasyield.club/partner-access
created: '2026-11-01'
description: AtlasYield rates DeFi vaults on 16 factors, shows who controls each one, and tests every day whether money can actually come back out. Free and public for people, apps and AI agents, with every score published before the outcome is known. Execution for agents is next.
image: https://atlasyield.club/opengraph-image.png?opengraph-image=0dkmbx.sprjvg.png
json_schemas:
- name: CompactScore
  property_count: 14
  slug: atlasyield-club-compact-score
- name: PortfolioSlice
  property_count: 13
  slug: atlasyield-club-portfolio-slice
- name: Score
  property_count: 16
  slug: atlasyield-club-score
- name: VaultFactors
  property_count: 10
  slug: atlasyield-club-vault-factors
- name: VaultMetrics
  property_count: 7
  slug: atlasyield-club-vault-metrics
- name: VaultRoute
  property_count: 15
  slug: atlasyield-club-vault-route
jsonld:
- class_count: 10
  name: Atlasyield Club Context
  property_count: 61
  slug: atlasyield-club-context
layout: provider
mcp_servers:
- description: Remote MCP server at atlasyield.club.
  name: AtlasYield MCP Server
  slug: atlasyield-club-mcp-yml
modified: '2026-11-01'
name: AtlasYield
nav: Providers
network: true
overview: 'AtlasYield publishes 6 API contracts indexed on the [APIs.io](https://apis.io/) network, including Basket API, Catalog API, Gas API, and 3 more. Tagged areas include DeFi, Yield, Risk Management, Analytics, and Onchain.


  The AtlasYield catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  AtlasYield''s developer surface includes authentication, documentation, API reference, support, and 22 more developer resources.'
random_paper: 23
rate_limits:
- limit_count: 2
  name: Atlasyield Club Rate Limits
  slug: atlasyield-club-rate-limits
rules:
- authorship: generated
  effective_rule_count: 98
  extends:
  - spectral:oas
  name: AtlasYield API Rules
  rule_count: 57
  severity_counts:
    error: 54
    hint: 0
    info: 2
    warn: 1
  slug: atlasyield-club-rules
scopes:
- name: Atlasyield Club Scopes
  scope_count: 0
  slug: atlasyield-club-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: thin
  composite: 39.1
  coverage:
    artifact_dirs: 28
    catalog_earned: 70.8
    catalog_earned_first_party: 8.0
    catalog_gap: 44.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -4.6
  facets:
    access_clarity: 10.5
    contract_governance: 22.0
    contract_quality: 63.1
    developer_ergonomics: 36.2
    discoverability: 65.0
    operational_transparency: 21.1
  previous_composite: 43.7
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 6
    mcp: first-party
    skills: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 28.9
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Atlasyield Club Authentication
  slug: atlasyield-club-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Atlasyield Club Domain Security
  slug: atlasyield-club-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
skill_count: 1
skills:
- name: get-scores
  slug: atlasyield-club-get-scores
slug: atlasyield-club
tags:
- DeFi
- Yield
- Risk Management
- Analytics
- Onchain
website: https://atlasyield.club/
---
