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
  - sandbox
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: conformant
    agent_skills: false
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
    openapi_examples: partial
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 47.0
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Adgentek Ai Agentic Access
  operation_count: 6
  slug: adgentek-ai-agentic-access
  summary_line: 6 operations
api_count: 1
apis:
- baseURL: https://api.adgentek.ai
  baseurl_source: declared
  description: Advertiser-facing endpoints (advertiser API keys).
  name: Adgentek Advertiser API
  slug: adgentek-ai-advertiser-api
- baseURL: https://api.adgentek.ai
  baseurl_source: declared
  description: Service metadata, health, metrics scrape, and this contract.
  name: Adgentek Meta API
  slug: adgentek-ai-meta-api
- baseURL: https://api.adgentek.ai
  baseurl_source: declared
  description: Publisher-facing endpoints (publisher API keys).
  name: Adgentek Publisher API
  slug: adgentek-ai-publisher-api
artifact_total: 12
common:
- group: design
  href: https://artifacts.apis.io/adgentek-ai/data-model/adgentek-ai-data-model.yml
  title: ''
  type: DataModel
  url: data-model/adgentek-ai-data-model.yml
- group: agent
  href: https://artifacts.apis.io/adgentek-ai/agentic-access/adgentek-ai-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/adgentek-ai-agentic-access.yml
- group: design
  href: https://artifacts.apis.io/adgentek-ai/rules/adgentek-ai-rules.yml
  title: ''
  type: Spectral
  url: rules/adgentek-ai-rules.yml
- group: design
  href: https://artifacts.apis.io/adgentek-ai/vocabulary/adgentek-ai-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/adgentek-ai-vocabulary.yml
- group: auth
  href: https://artifacts.apis.io/adgentek-ai/authentication/adgentek-ai-authentication.yml
  title: ''
  type: Authentication
  url: authentication/adgentek-ai-authentication.yml
- group: design
  href: https://artifacts.apis.io/adgentek-ai/errors/adgentek-ai-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/adgentek-ai-problem-types.yml
- group: design
  href: https://artifacts.apis.io/adgentek-ai/conformance/adgentek-ai-conformance.yml
  title: ''
  type: Conformance
  url: conformance/adgentek-ai-conformance.yml
- group: agent
  href: https://artifacts.apis.io/adgentek-ai/llms/adgentek-ai-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/adgentek-ai-llms.txt
- group: other
  href: https://artifacts.apis.io/adgentek-ai/a2a/adgentek-ai-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/adgentek-ai-a2a.yml
- group: agent
  href: https://artifacts.apis.io/adgentek-ai/mcp/adgentek-ai-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/adgentek-ai-mcp.yml
- group: agent
  href: https://artifacts.apis.io/adgentek-ai/well-known/adgentek-ai-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/adgentek-ai-well-known.yml
- group: other
  href: https://artifacts.apis.io/adgentek-ai/hosts/adgentek-ai-hosts.yml
  title: ''
  type: Hosts
  url: hosts/adgentek-ai-hosts.yml
- group: other
  href: https://artifacts.apis.io/adgentek-ai/vendors/adgentek-ai-vendors.yml
  title: ''
  type: Vendors
  url: vendors/adgentek-ai-vendors.yml
- group: build
  href: https://artifacts.apis.io/adgentek-ai/packages/adgentek-ai-packages.yml
  title: ''
  type: SDKs
  url: packages/adgentek-ai-packages.yml
- group: build
  href: https://artifacts.apis.io/adgentek-ai/packages/adgentek-ai-packages.yml
  title: ''
  type: Packages
  url: packages/adgentek-ai-packages.yml
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://app.adgentek.ai/privacy
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.adgentek.ai/publishers/quickstart
- group: start
  title: ''
  type: DeveloperPortal
  url: https://api.adgentek.ai`
- group: auth
  href: https://artifacts.apis.io/adgentek-ai/security/adgentek-ai-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/adgentek-ai-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://adgentek.ai/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.adgentek.ai/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.adgentek.ai/
- group: company
  title: ''
  type: Blog
  url: https://adgentek.ai/blog/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Adgentek
created: '2026-10-31'
description: 'Adgentek powers the agentic era of advertising: the Adgentek Ad Server monetizes AI surfaces and agents, delivering context‑aware ads within chatbots, AI‑powered apps, and autonomous agents. Publishers integrate via a lightweight JavaScript SDK, retain full control over formats and placements, and benefit from privacy‑safe derived signals. Brands reach high‑intent AI audiences at the moment of decision, while users experience seamless, conversational ad experiences across AI interfaces.'
image: https://adgentek.ai/assets/logo-on-dark.svg
json_schemas:
- name: AdvertiserReportingResponse
  property_count: 0
  slug: adgentek-ai-advertiser-reporting-response
- name: Health
  property_count: 0
  slug: adgentek-ai-health
- name: PublisherReportingResponse
  property_count: 0
  slug: adgentek-ai-publisher-reporting-response
- name: VersionInfo
  property_count: 0
  slug: adgentek-ai-version-info
layout: provider
mcp_servers:
- description: Remote MCP server at mcp.adgentek.ai requiring an API key.
  name: Adgentek MCP Server
  slug: adgentek-ai-mcp-yml
modified: '2026-10-31'
name: Adgentek
nav: Providers
network: true
overview: 'Adgentek publishes 3 API contracts indexed on the [APIs.io](https://apis.io/) network: Advertiser API, Meta API, and Publisher API. Tagged areas include Advertising, Artificial Intelligence, AdTech, AI Agents, and Monetization.


  The Adgentek catalog on APIs.io includes 1 Spectral governance ruleset.


  Adgentek''s developer surface includes authentication, getting-started guide, documentation, API reference, engineering blog, and 19 more developer resources.'
random_paper: 2
rules:
- authorship: generated
  effective_rule_count: 48
  extends:
  - spectral:oas
  name: Adgentek API Rules
  rule_count: 7
  severity_counts:
    error: 6
    hint: 0
    info: 1
    warn: 0
  slug: adgentek-ai-rules
score:
  band: thin
  composite: 30.7
  coverage:
    artifact_dirs: 24
    catalog_earned: 51.0
    catalog_earned_first_party: 0.0
    catalog_gap: 64.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -5.7
  facets:
    access_clarity: 5.3
    contract_governance: 19.7
    contract_quality: 49.0
    developer_ergonomics: 39.3
    discoverability: 65.0
    operational_transparency: 2.6
  previous_composite: 36.4
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 3
    mcp: first-party
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 17.3
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Adgentek Ai Authentication
  slug: adgentek-ai-authentication
  summary_line: 3 schemes
- kind: domain-security
  name: Adgentek Ai Domain Security
  slug: adgentek-ai-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
slug: adgentek-ai
tags:
- Advertising
- Artificial Intelligence
- AdTech
- AI Agents
- Monetization
- Servers
website: https://adgentek.ai/
---
