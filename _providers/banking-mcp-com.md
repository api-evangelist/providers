---
access_model:
  confidence: medium
  gated: none
  gated_source:
  - onboarding
  label: Paid · Self-serve signup
  onboarding: self-serve
  pricing: paid
  public: false
  source:
  - plans
  - authentication
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
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 22.1
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: BankingMCP is the banking MCP server for your bank accounts. Connect your bank once and ask Claude, ChatGPT, Mistral or Cursor about transactions and balances.
  name: BankingMCP API
  slug: bankingmcp-api
artifact_total: 7
common:
- group: commercial
  href: https://artifacts.apis.io/banking-mcp-com/plans/banking-mcp-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/banking-mcp-com-plans-pricing.yml
- group: build
  href: https://artifacts.apis.io/banking-mcp-com/cli/banking-mcp-com-cli.yml
  title: ''
  type: CLI
  url: cli/banking-mcp-com-cli.yml
- group: auth
  href: https://artifacts.apis.io/banking-mcp-com/authentication/banking-mcp-com-authentication.yml
  title: ''
  type: Authentication
  url: authentication/banking-mcp-com-authentication.yml
- group: design
  href: https://artifacts.apis.io/banking-mcp-com/conformance/banking-mcp-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/banking-mcp-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/banking-mcp-com/llms/banking-mcp-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/banking-mcp-com-llms.txt
- group: agent
  href: https://artifacts.apis.io/banking-mcp-com/mcp/banking-mcp-com-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/banking-mcp-com-mcp.yml
- group: agent
  href: https://artifacts.apis.io/banking-mcp-com/well-known/banking-mcp-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/banking-mcp-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/banking-mcp-com/hosts/banking-mcp-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/banking-mcp-com-hosts.yml
- group: start
  title: ''
  type: Login
  url: https://banking-mcp.com/en/login
- group: auth
  href: https://artifacts.apis.io/banking-mcp-com/security/banking-mcp-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/banking-mcp-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://banking-mcp.com/
- group: docs
  title: ''
  type: Documentation
  url: https://banking-mcp.com/en
- group: commercial
  title: ''
  type: Pricing
  url: https://banking-mcp.com/en/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://banking-mcp.com/en/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://banking-mcp.com/en/privacy
- group: company
  title: ''
  type: Blog
  url: https://banking-mcp.com/en/blog
- group: start
  title: ''
  type: GettingStarted
  url: https://banking-mcp.com/en/setup
- group: other
  title: ''
  type: Image
  url: https://banking-mcp.com/en/opengraph-image?c2e4a0ea31761e41
coverage:
  checked: '2026-11-02'
  detail: No OpenAPI, AsyncAPI, GraphQL, gRPC, or WSDL contract could be found despite probing documented hosts.
  evidence:
  - status: 404
    url: https://banking-mcp.com/openapi.json
  - status: 0
    url: https://api.banking-mcp.com/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-11-02'
description: Escher Consulting GmbH develops BankingMCP, a banking MCP server that lets users connect their bank accounts to AI assistants such as Claude, ChatGPT, Mistral, and Cursor. It supports a wide range of German banks and expanding across Europe, offering read‑only access to transaction and balance data. Users can try a free 7‑day trial before a €5 per month subscription. The service emphasizes security, never storing passwords, and plans future payment capabilities with explicit user approval.
image: https://banking-mcp.com/en/opengraph-image?c2e4a0ea31761e41
layout: provider
mcp_servers:
- description: Remote MCP server at banking-mcp.com.
  name: Escher Consulting GmbH MCP Server
  slug: banking-mcp-com-mcp-yml
modified: '2026-11-02'
name: Escher Consulting GmbH
nav: Providers
network: true
overview: 'Escher Consulting GmbH is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Banking, Artificial Intelligence, Finance, Open Banking, and MCP.


  Escher Consulting GmbH''s developer surface includes CLI, authentication, documentation, pricing, engineering blog, getting-started guide, and 12 more developer resources.'
plans:
- name: Banking Mcp Com Plans Pricing
  plan_count: 1
  slug: banking-mcp-com-plans-pricing
random_paper: 19
rate_limits:
- limit_count: 0
  name: Banking Mcp Com Rate Limits
  slug: banking-mcp-com-rate-limits
scopes:
- name: Banking Mcp Com Scopes
  scope_count: 0
  slug: banking-mcp-com-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: emerging
  composite: 23.9
  coverage:
    artifact_dirs: 22
    catalog_earned: 40.0
    catalog_earned_first_party: 8.0
    catalog_gap: 75.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -7.3
  facets:
    access_clarity: 43.4
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 31.0
    discoverability: 56.7
    operational_transparency: 0.0
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - europe
  previous_composite: 31.2
  provenance:
    conformance: first-party
    mcp: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Banking & Open Finance
    regime_id: banking_open_finance
    score: 28.1
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Banking Mcp Com Authentication
  slug: banking-mcp-com-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Banking Mcp Com Domain Security
  slug: banking-mcp-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: banking-mcp-com
tags:
- Banking
- Artificial Intelligence
- Finance
- Open Banking
- MCP
- Europe
website: https://banking-mcp.com/
---
