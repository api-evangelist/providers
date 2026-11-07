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
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: conformant
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: derived
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    mcp_tool_quality: na
    openapi_examples: partial
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 31.2
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 7
  human_in_the_loop: 0
  name: Caper Network Agentic Access
  operation_count: 20
  slug: caper-network-agentic-access
  summary_line: 20 operations · 7 acting
api_count: 1
apis:
- baseURL: https://caper.network
  baseurl_source: declared
  description: The Agent API from Caper — 7 operation(s) for agent.
  name: Caper Agent API
  slug: caper-network-agent-api
- baseURL: https://caper.network
  baseurl_source: declared
  description: The Blog API from Caper — 1 operation(s) for blog.
  name: Caper Blog API
  slug: caper-network-blog-api
- baseURL: https://caper.network
  baseurl_source: declared
  description: The Blog.xml API from Caper — 1 operation(s) for blog.xml.
  name: Caper Blog.xml API
  slug: caper-network-blog-xml-api
- baseURL: https://caper.network
  baseurl_source: declared
  description: The Capers API from Caper — 3 operation(s) for capers.
  name: Caper Capers API
  slug: caper-network-capers-api
- baseURL: https://caper.network
  baseurl_source: declared
  description: The Llms.txt API from Caper — 1 operation(s) for llms.txt.
  name: Caper Llms.txt API
  slug: caper-network-llms-txt-api
- baseURL: https://caper.network
  baseurl_source: declared
  description: The Mcp API from Caper — 1 operation(s) for mcp.
  name: Caper MCP API
  slug: caper-network-mcp-api
- baseURL: https://caper.network
  baseurl_source: declared
  description: The Sitemap.xml API from Caper — 1 operation(s) for sitemap.xml.
  name: Caper Sitemap.xml API
  slug: caper-network-sitemap-xml-api
- baseURL: https://caper.network
  baseurl_source: declared
  description: The .well Known API from Caper — 2 operation(s) for .well known.
  name: Caper .well Known API
  slug: caper-network-well-known-api
- baseURL: https://caper.network
  baseurl_source: declared
  description: The Wiki API from Caper — 3 operation(s) for wiki.
  name: Caper Wiki API
  slug: caper-network-wiki-api
artifact_total: 14
common:
- group: agent
  href: https://artifacts.apis.io/caper-network/agentic-access/caper-network-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/caper-network-agentic-access.yml
- group: design
  href: https://artifacts.apis.io/caper-network/rules/caper-network-rules.yml
  title: ''
  type: Spectral
  url: rules/caper-network-rules.yml
- group: design
  href: https://artifacts.apis.io/caper-network/errors/caper-network-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/caper-network-problem-types.yml
- group: design
  href: https://artifacts.apis.io/caper-network/conformance/caper-network-conformance.yml
  title: ''
  type: Conformance
  url: conformance/caper-network-conformance.yml
- group: agent
  href: https://artifacts.apis.io/caper-network/llms/caper-network-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/caper-network-llms.txt
- group: other
  href: https://artifacts.apis.io/caper-network/a2a/caper-network-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/caper-network-a2a.yml
- group: agent
  href: https://artifacts.apis.io/caper-network/mcp/caper-network-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/caper-network-mcp.yml
- group: other
  href: https://artifacts.apis.io/caper-network/hosts/caper-network-hosts.yml
  title: ''
  type: Hosts
  url: hosts/caper-network-hosts.yml
- group: other
  href: https://artifacts.apis.io/caper-network/vendors/caper-network-vendors.yml
  title: ''
  type: Vendors
  url: vendors/caper-network-vendors.yml
- group: operate
  title: ''
  type: Support
  url: https://caper.network/wiki/help
- group: company
  title: ''
  type: Blog
  url: https://caper.network/blog
- group: docs
  title: ''
  type: APIReference
  url: https://caper.network/wiki/foundations/getting-started
- group: auth
  href: https://artifacts.apis.io/caper-network/authentication/caper-network-authentication.yml
  title: ''
  type: Authentication
  url: authentication/caper-network-authentication.yml
- group: auth
  href: https://artifacts.apis.io/caper-network/security/caper-network-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/caper-network-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://caper.network/
- group: docs
  title: ''
  type: Documentation
  url: https://caper.network/wiki
- group: commercial
  title: ''
  type: TermsOfService
  url: https://caper.network/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://caper.network/privacy
created: '2026-11-04'
description: Caper is a platform on Radix that enables perpetual fundraising for organizations by launching tokenized DAOs with continuous liquidity, governance, and market mechanisms. It provides tools to create, manage, and exit DAOs, offering 24/7 fundraising, transparent treasury management, and community-driven decision making. The system integrates on-chain execution, voting tokens, and market-driven proposals to ensure decentralized control and sustainable capital deployment.
image: https://caper.network/og?title=Perpetual+fundraising+for+organizations&eyebrow=caper&description=A+caper+is+a+DAO+anyone+can+launch+on+Radix+in+one+transaction%2C+with+its+own+token%2C+a+treasury%2C+and+a+market+that+raises+from+anyone+at+any+time.
layout: provider
mcp_servers:
- description: Remote MCP server at caper.network.
  name: Caper MCP Server
  slug: caper-network-mcp-yml
modified: '2026-11-04'
name: Caper
nav: Providers
network: true
overview: 'Caper publishes 9 API contracts indexed on the [APIs.io](https://apis.io/) network, including Agent API, Blog API, Blog.xml API, and 6 more. Tagged areas include DAO, Blockchain, Fundraising, Radix, and Decentralized.


  The Caper catalog on APIs.io includes 1 Spectral governance ruleset.


  Caper''s developer surface includes support, engineering blog, API reference, authentication, documentation, and 13 more developer resources.'
random_paper: 2
rules:
- authorship: generated
  effective_rule_count: 81
  extends:
  - spectral:oas
  name: Caper API Rules
  rule_count: 40
  severity_counts:
    error: 37
    hint: 0
    info: 1
    warn: 2
  slug: caper-network-rules
score:
  band: thin
  composite: 27.3
  coverage:
    artifact_dirs: 15
    catalog_earned: 41.5
    catalog_earned_first_party: 0.0
    catalog_gap: 73.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 10.5
    contract_governance: 18.2
    contract_quality: 43.9
    developer_ergonomics: 23.8
    discoverability: 65.0
    operational_transparency: 0.0
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 9
    mcp: first-party
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 20.6
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Caper Network Authentication
  slug: caper-network-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Caper Network Domain Security
  slug: caper-network-domain-security
  summary_line: TLSv1.3 · HSTS
slug: caper-network
tags:
- DAO
- Blockchain
- Fundraising
- Radix
- Decentralized
website: https://caper.network/
---
