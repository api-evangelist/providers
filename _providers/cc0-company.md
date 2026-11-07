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
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 18.2
  scored_at: '2026-11-06'
api_count: 2
apis:
- description: API for CC0 Company providing access to digital art marketplace features.
  name: CC0 Company API
  slug: cc0-company-api-2
- baseURL: https://cc0.company
  baseurl_source: declared
  description: 'CC0 Company API as documented publicly: 27 operations. Contract generated from the documentation by API Evangelist (2026-11-04); not the provider''s own document.'
  name: CC0 Company API
  slug: cc0-company-api
artifact_total: 5
common:
- group: design
  href: https://artifacts.apis.io/cc0-company/rules/cc0-company-rules.yml
  title: ''
  type: Spectral
  url: rules/cc0-company-rules.yml
- group: design
  href: https://artifacts.apis.io/cc0-company/vocabulary/cc0-company-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/cc0-company-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/cc0-company/conformance/cc0-company-conformance.yml
  title: ''
  type: Conformance
  url: conformance/cc0-company-conformance.yml
- group: agent
  href: https://artifacts.apis.io/cc0-company/llms/cc0-company-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/cc0-company-llms.txt
- group: agent
  href: https://artifacts.apis.io/cc0-company/mcp/cc0-company-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/cc0-company-mcp.yml
- group: other
  href: https://artifacts.apis.io/cc0-company/hosts/cc0-company-hosts.yml
  title: ''
  type: Hosts
  url: hosts/cc0-company-hosts.yml
- group: other
  href: https://artifacts.apis.io/cc0-company/vendors/cc0-company-vendors.yml
  title: ''
  type: Vendors
  url: vendors/cc0-company-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://app.cc0.company/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://app.cc0.company/privacy
- group: docs
  title: ''
  type: Documentation
  url: https://app.cc0.company/docs
- group: docs
  title: ''
  type: APIReference
  url: https://app.cc0.company/docs/api-reference
- group: start
  title: ''
  type: GettingStarted
  url: https://app.cc0.company/docs/getting-started
- group: auth
  href: https://artifacts.apis.io/cc0-company/security/cc0-company-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/cc0-company-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://cc0.company/
coverage:
  checked: '2026-11-04'
  detail: Documentation is public but no machine‑readable OpenAPI, AsyncAPI, GraphQL, gRPC or WSDL contracts were found.
  evidence:
  - status: 200
    url: https://app.cc0.company/docs/api-reference
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-11-04'
description: CC0 Company operates a social network for digital art, enabling creators to showcase, sell, and trade NFTs and artworks. The platform aggregates feeds from major NFT marketplaces like SuperRare, Foundation, Transient Labs, networked.art, and BasePaint, offering a unified browsing experience for art enthusiasts and collectors. Users can mint new artworks, launch tokens, and participate in live auctions, while also accessing token staking and marketplace features. The service emphasizes community-driven discovery and supports a wide range of digital assets across multiple blockchain networks.
image: https://cc0.company/og-cc0company.jpg
layout: provider
mcp_servers:
- description: Remote MCP server at cc0.company.
  name: CC0 Company MCP Server
  slug: cc0-company-mcp-yml
modified: '2026-11-04'
name: CC0 Company
nav: Providers
network: true
overview: 'CC0 Company is listed with 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Digital Art, Social Network, NFT, live auctions, and Token Launch.


  The CC0 Company catalog on APIs.io includes 1 Spectral governance ruleset.


  CC0 Company''s developer surface includes documentation, API reference, getting-started guide, and 11 more developer resources.'
random_paper: 18
rules:
- authorship: generated
  effective_rule_count: 73
  extends:
  - spectral:oas
  name: CC0 Company API Rules
  rule_count: 32
  severity_counts:
    error: 30
    hint: 0
    info: 1
    warn: 1
  slug: cc0-company-rules
score:
  band: emerging
  composite: 15.9
  coverage:
    artifact_dirs: 16
    catalog_earned: 37.8
    catalog_earned_first_party: 0.0
    catalog_gap: 77.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 10.5
    contract_governance: 22.0
    contract_quality: 10.7
    developer_ergonomics: 14.3
    discoverability: 56.7
    operational_transparency: 0.0
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 1
      marker_coverage: 100.0
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
  name: Cc0 Company Domain Security
  slug: cc0-company-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: cc0-company
tags:
- Digital Art
- Social Network
- NFT
- live auctions
- Token Launch
- AI Agents
website: https://cc0.company/
---
