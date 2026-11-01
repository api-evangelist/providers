---
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: true
  schema_version: '0.2'
  score: 25.0
  scored_at: '2026-10-31'
api_count: 0
artifact_total: 3
common:
- group: commercial
  href: https://artifacts.apis.io/stalkchain-com/plans/stalkchain-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/stalkchain-com-plans-pricing.yml
- group: build
  href: https://artifacts.apis.io/stalkchain-com/cli/stalkchain-com-cli.yml
  title: ''
  type: CLI
  url: cli/stalkchain-com-cli.yml
- group: agent
  href: https://artifacts.apis.io/stalkchain-com/llms/stalkchain-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/stalkchain-com-llms.txt
- group: agent
  href: https://artifacts.apis.io/stalkchain-com/mcp/stalkchain-com-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/stalkchain-com-mcp.yml
- group: agent
  href: https://artifacts.apis.io/stalkchain-com/well-known/stalkchain-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/stalkchain-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/stalkchain-com/hosts/stalkchain-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/stalkchain-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/stalkchain-com/vendors/stalkchain-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/stalkchain-com-vendors.yml
- group: build
  href: https://artifacts.apis.io/stalkchain-com/packages/stalkchain-com-packages.yml
  title: ''
  type: SDKs
  url: packages/stalkchain-com-packages.yml
- group: build
  href: https://artifacts.apis.io/stalkchain-com/packages/stalkchain-com-packages.yml
  title: ''
  type: Packages
  url: packages/stalkchain-com-packages.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://stalkchain.com/terms-conditions
- group: start
  title: ''
  type: GettingStarted
  url: https://stalkchain.com/docs/guides/getting-started
- group: docs
  title: ''
  type: APIReference
  url: https://stalkchain.com/llms.txt
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/StalkChain
- group: auth
  href: https://artifacts.apis.io/stalkchain-com/security/stalkchain-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/stalkchain-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://stalkchain.com/
- group: docs
  title: ''
  type: Documentation
  url: https://stalkchain.com/api
- group: commercial
  title: ''
  type: Pricing
  url: https://stalkchain.com/pricing
- group: company
  title: ''
  type: Blog
  url: https://stalkchain.com/blog
- group: operate
  title: ''
  type: Support
  url: https://stalkchain.com/contact
created: '2026-10-21'
description: StalkChain provides a Crypto MCP Server and API that aggregates on‑chain and social data across multiple blockchains. It offers real‑time feeds of influencer trades, token trends, whale movements, and transaction analytics for AI agents like Claude, ChatGPT, and others. Users can connect their AI tools to retrieve live market data, track token holdings, and get actionable insights without needing separate data pipelines.
image: https://stalkchain.com/og/home.jpg
layout: provider
mcp_servers:
- description: Remote MCP server at data.stalkchain.com requiring OAuth.
  name: stalkchain-com MCP Server
  slug: stalkchain-com-mcp-yml
modified: '2026-10-21'
name: stalkchain-com
nav: Providers
network: true
overview: 'stalkchain-com is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Crypto, Data, AI, and Blockchain.


  stalkchain-com''s developer surface includes CLI, getting-started guide, API reference, documentation, pricing, engineering blog, support, and 12 more developer resources.'
plans:
- name: Stalkchain Com Plans Pricing
  plan_count: 3
  slug: stalkchain-com-plans-pricing
random_paper: 6
score:
  band: emerging
  composite: 25.9
  coverage:
    artifact_dirs: 11
    catalog_earned: 39.0
    catalog_earned_first_party: 12.0
    catalog_gap: 76.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 52.6
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 50.0
    discoverability: 48.3
    operational_transparency: 5.3
  provenance:
    conformance: unknown
    mcp: first-party
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 14.5
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Stalkchain Com Domain Security
  slug: stalkchain-com-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
slug: stalkchain-com
tags:
- Company
- Crypto
- Data
- AI
- Blockchain
- Analytics
website: https://stalkchain.com/
---
