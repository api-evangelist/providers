---
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
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: true
  schema_version: '0.2'
  score: 6.3
  scored_at: '2026-10-31'
api_count: 1
apis:
- description: Full public API for TokenOS platform, curated agent surface.
  name: TokenOS API
  slug: tokenos-api
artifact_total: 4
common:
- group: commercial
  href: https://artifacts.apis.io/tokenos-ai/plans/tokenos-ai-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/tokenos-ai-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/tokenos-ai/changelog/tokenos-ai-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/tokenos-ai-changelog.yml
- group: design
  href: https://artifacts.apis.io/tokenos-ai/conformance/tokenos-ai-conformance.yml
  title: ''
  type: Conformance
  url: conformance/tokenos-ai-conformance.yml
- group: agent
  href: https://artifacts.apis.io/tokenos-ai/llms/tokenos-ai-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/tokenos-ai-llms.txt
- group: agent
  href: https://artifacts.apis.io/tokenos-ai/mcp/tokenos-ai-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/tokenos-ai-mcp.yml
- group: other
  href: https://artifacts.apis.io/tokenos-ai/hosts/tokenos-ai-hosts.yml
  title: ''
  type: Hosts
  url: hosts/tokenos-ai-hosts.yml
- group: other
  href: https://artifacts.apis.io/tokenos-ai/vendors/tokenos-ai-vendors.yml
  title: ''
  type: Vendors
  url: vendors/tokenos-ai-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://tokenos.ai/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://tokenos.ai/privacy
- group: operate
  title: ''
  type: ChangeLog
  url: https://tokenos.ai/docs/whats-new
- group: start
  title: ''
  type: GettingStarted
  url: https://tokenos.ai/docs/quickstart
- group: docs
  title: ''
  type: APIReference
  url: https://tokenos.ai/llms.txt
- group: auth
  href: https://artifacts.apis.io/tokenos-ai/security/tokenos-ai-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/tokenos-ai-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://tokenos.ai/
- group: docs
  title: ''
  type: Documentation
  url: https://tokenos.ai/docs
- group: start
  title: ''
  type: DeveloperPortal
  url: https://tokenos.ai/mcp
- group: commercial
  title: ''
  type: Pricing
  url: https://tokenos.ai/pricing
- group: company
  title: ''
  type: Blog
  url: https://tokenos.ai/blog
created: '2026-10-29'
description: TokenOS is an AI‑powered operating system for building, deploying and launching Web3 applications. It lets developers describe an app in plain language and generates full‑stack Solana and EVM dApps, handling smart‑contract compilation, wallet integration, and deployment to multiple chains. The platform includes a marketplace for AI agents, a P2P AI inference market, and tools for token launches, NFTs, DAOs, and more, all without custodial control of private keys.
image: https://tokenos.ai/og_tokenos.png
layout: provider
mcp_servers:
- description: Remote MCP server at tokenos.ai.
  name: tokenos-ai MCP Server
  slug: tokenos-ai-mcp-yml
modified: '2026-10-29'
name: tokenos-ai
nav: Providers
network: true
overview: 'tokenos-ai is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include AI, Web3, Platform, Tokenization, and Decentralized.


  tokenos-ai''s developer surface includes changelog, getting-started guide, API reference, documentation, pricing, engineering blog, and 12 more developer resources.'
plans:
- name: Tokenos Ai Plans Pricing
  plan_count: 4
  slug: tokenos-ai-plans-pricing
random_paper: 10
score:
  band: thin
  composite: 30.2
  coverage:
    artifact_dirs: 11
    catalog_earned: 49.0
    catalog_earned_first_party: 12.0
    catalog_gap: 66.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 63.2
    contract_governance: 4.5
    contract_quality: 0.0
    developer_ergonomics: 40.5
    discoverability: 65.0
    operational_transparency: 15.8
  provenance:
    conformance: derived
    mcp: first-party
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 17.3
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Tokenos Ai Domain Security
  slug: tokenos-ai-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: tokenos-ai
tags:
- AI
- Web3
- Platform
- Tokenization
- Decentralized
website: https://tokenos.ai/
---
