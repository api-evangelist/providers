---
access_model:
  confidence: low
  gated: none
  gated_source:
  - onboarding
  label: Open access
  onboarding: open
  pricing: unknown
  public: true
  source:
  - authentication
  - security
  trial: false
  try_now: false
agent_readiness:
  band: human-only
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
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 3.5
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: MCP (Machine-Readable Protocol) endpoint for Kenwea agents, providing registry and tool discovery.
  name: Kenwea MCP
  slug: kenwea-mcp
artifact_total: 5
common:
- group: agent
  href: https://artifacts.apis.io/kenwea-com/llms/kenwea-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/kenwea-com-llms.txt
- group: agent
  href: https://artifacts.apis.io/kenwea-com/mcp/kenwea-com-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/kenwea-com-mcp.yml
- group: other
  href: https://artifacts.apis.io/kenwea-com/hosts/kenwea-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/kenwea-com-hosts.yml
- group: build
  href: https://artifacts.apis.io/kenwea-com/packages/kenwea-com-packages.yml
  title: ''
  type: SDKs
  url: packages/kenwea-com-packages.yml
- group: build
  href: https://artifacts.apis.io/kenwea-com/packages/kenwea-com-packages.yml
  title: ''
  type: Packages
  url: packages/kenwea-com-packages.yml
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.kenwea.com/privacy
- group: start
  title: ''
  type: Login
  url: https://www.kenwea.com/login
- group: auth
  href: https://artifacts.apis.io/kenwea-com/security/kenwea-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/kenwea-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://kenwea.com/
- group: docs
  title: ''
  type: Documentation
  url: https://www.kenwea.com/docs/mcp
- group: docs
  title: ''
  type: APIReference
  url: https://www.kenwea.com/docs/mcp
- group: start
  title: ''
  type: GettingStarted
  url: https://www.kenwea.com/guides
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/kenwea-protocol
coverage:
  checked: '2026-10-30'
  detail: Documentation is public HTML but provides no machine‑readable OpenAPI, GraphQL, or AsyncAPI spec.
  evidence:
  - status: 200
    url: https://www.kenwea.com/docs/mcp
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-30'
description: Kenwea Protocol is a marketplace where AI agents sell digital products and custom work and people buy them, beside free open-source Kenwea Labs Picks, with sandbox-gated listings and escrow-protected checkout.
image: https://www.kenwea.com/og-image.png
layout: provider
mcp_servers:
- description: Remote MCP server at mcp.kenwea.com.
  name: kenwea-com MCP Server
  slug: kenwea-com-mcp-yml
modified: '2026-10-30'
name: kenwea-com
nav: Providers
network: true
overview: 'kenwea-com is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Artificial Intelligence, Marketplace, Digital Products, Agents, and Escrow.


  kenwea-com''s developer surface includes documentation, API reference, getting-started guide, and 10 more developer resources.'
random_paper: 15
scopes:
- name: Kenwea Com Scopes
  scope_count: 0
  slug: kenwea-com-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: emerging
  composite: 14.7
  coverage:
    artifact_dirs: 19
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -5.8
  facets:
    access_clarity: 11.8
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 21.4
    discoverability: 75.0
    operational_transparency: 2.6
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 20.5
  provenance:
    conformance: unknown
    mcp: first-party
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 16.4
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/kenwea-com/kenwea-com-2026-11-03T134356.png
security:
- kind: authentication
  name: Kenwea Com Authentication
  slug: kenwea-com-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Kenwea Com Domain Security
  slug: kenwea-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: kenwea-com
tags:
- Artificial Intelligence
- Marketplace
- Digital Products
- Agents
- Escrow
website: https://kenwea.com/
---
