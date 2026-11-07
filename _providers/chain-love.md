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
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 16.5
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Chain Love Agentic Access
  operation_count: 5
  slug: chain-love-agentic-access
  summary_line: 5 operations
api_count: 1
apis:
- baseURL: https://www.chain.love
  baseurl_source: declared
  description: Text files and manifests for AI crawlers and agents.
  name: Chain.Love AI Context API
  slug: chain-love-ai-context-api
- baseURL: https://www.chain.love
  baseurl_source: declared
  description: Public endpoints for discovering Chain.Love resources.
  name: Chain.Love Discovery API
  slug: chain-love-discovery-api
artifact_total: 5
common:
- group: agent
  href: https://artifacts.apis.io/chain-love/agentic-access/chain-love-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/chain-love-agentic-access.yml
- group: design
  href: https://artifacts.apis.io/chain-love/rules/chain-love-rules.yml
  title: ''
  type: Spectral
  url: rules/chain-love-rules.yml
- group: design
  href: https://artifacts.apis.io/chain-love/vocabulary/chain-love-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/chain-love-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/chain-love/conformance/chain-love-conformance.yml
  title: ''
  type: Conformance
  url: conformance/chain-love-conformance.yml
- group: agent
  href: https://artifacts.apis.io/chain-love/llms/chain-love-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/chain-love-llms.txt
- group: agent
  href: https://artifacts.apis.io/chain-love/well-known/chain-love-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/chain-love-well-known.yml
- group: other
  href: https://artifacts.apis.io/chain-love/hosts/chain-love-hosts.yml
  title: ''
  type: Hosts
  url: hosts/chain-love-hosts.yml
- group: other
  href: https://artifacts.apis.io/chain-love/vendors/chain-love-vendors.yml
  title: ''
  type: Vendors
  url: vendors/chain-love-vendors.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://status.chain.love/
- group: auth
  title: ''
  type: Security
  url: https://app.chain.love/toolbox/security
- group: build
  title: ''
  type: SDKs
  url: https://app.chain.love/toolbox/sdks
- group: auth
  href: https://artifacts.apis.io/chain-love/security/chain-love-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/chain-love-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.chain.love/
- group: docs
  title: ''
  type: APIReference
  url: https://www.chain.love/openapi.json
- group: start
  title: ''
  type: GettingStarted
  url: https://www.chain.love/about
- group: operate
  title: ''
  type: Support
  url: https://www.chain.love/contact-us
- group: company
  title: ''
  type: Blog
  url: https://chain-love.gitbook.io/chain-love-docs
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Chain-Love/chain-love
created: '2026-11-03'
description: Chain.Love helps developers and AI agents discover Web3 infrastructure across 15 categories, including MCP servers, APIs, wallets, bridges, and SDKs. Founded in 2018, it offers a discovery platform, MCP gateway, and AI context services for global users.
image: https://www.chain.love/chainlove.png
layout: provider
modified: '2026-11-03'
name: Chain.Love
nav: Providers
network: true
overview: 'Chain.Love publishes 2 API contracts indexed on the [APIs.io](https://apis.io/) network: AI Context API and Discovery API. Tagged areas include Web3 Infrastructure, RPC, Indexing, Oracle, and Bridge.


  The Chain.Love catalog on APIs.io includes 1 Spectral governance ruleset.


  Chain.Love''s developer surface includes API reference, getting-started guide, support, engineering blog, and 14 more developer resources.'
random_paper: 14
rules:
- authorship: generated
  effective_rule_count: 78
  extends:
  - spectral:oas
  name: Chain.Love API Rules
  rule_count: 37
  severity_counts:
    error: 35
    hint: 0
    info: 1
    warn: 1
  slug: chain-love-rules
score:
  band: emerging
  composite: 25.9
  coverage:
    artifact_dirs: 14
    catalog_earned: 42.8
    catalog_earned_first_party: 0.0
    catalog_gap: 72.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 0.0
    contract_governance: 22.0
    contract_quality: 44.7
    developer_ergonomics: 20.2
    discoverability: 66.1
    operational_transparency: 15.8
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 2
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 10.8
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Chain Love Domain Security
  slug: chain-love-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: chain-love
tags:
- Web3 Infrastructure
- RPC
- Indexing
- Oracle
- Bridge
- Developer Tools
- Marketplace
website: https://www.chain.love/
---
