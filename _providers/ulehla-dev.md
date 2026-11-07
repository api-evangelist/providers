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
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: unknown
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
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: true
  schema_version: '0.2'
  score: 12.1
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: MCP endpoint providing tool listings for Ulehla-dev.
  name: Ulehla MCP
  slug: ulehla-mcp
artifact_total: 9
common:
- group: agent
  href: https://artifacts.apis.io/ulehla-dev/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: build
  href: https://artifacts.apis.io/ulehla-dev/cli/ulehla-dev-cli.yml
  title: ''
  type: CLI
  url: cli/ulehla-dev-cli.yml
- group: auth
  href: https://artifacts.apis.io/ulehla-dev/security/ulehla-dev-vulnerability-disclosure.yml
  title: ''
  type: Security
  url: security/ulehla-dev-vulnerability-disclosure.yml
- group: agent
  href: https://artifacts.apis.io/ulehla-dev/llms/ulehla-dev-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/ulehla-dev-llms.txt
- group: agent
  href: https://artifacts.apis.io/ulehla-dev/mcp/ulehla-dev-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/ulehla-dev-mcp.yml
- group: auth
  href: https://artifacts.apis.io/ulehla-dev/well-known/ulehla-dev-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/ulehla-dev-security.txt
- group: agent
  href: https://artifacts.apis.io/ulehla-dev/well-known/ulehla-dev-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/ulehla-dev-well-known.yml
- group: other
  href: https://artifacts.apis.io/ulehla-dev/hosts/ulehla-dev-hosts.yml
  title: ''
  type: Hosts
  url: hosts/ulehla-dev-hosts.yml
- group: other
  href: https://artifacts.apis.io/ulehla-dev/vendors/ulehla-dev-vendors.yml
  title: ''
  type: Vendors
  url: vendors/ulehla-dev-vendors.yml
- group: start
  title: ''
  type: Sandbox
  url: https://ulehla.dev/playground/
- group: auth
  href: https://artifacts.apis.io/ulehla-dev/security/ulehla-dev-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/ulehla-dev-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/ulehla-dev/security/ulehla-dev-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/ulehla-dev-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://ulehla.dev/
- group: docs
  title: ''
  type: Documentation
  url: https://ulehla.dev/index.md
- group: docs
  title: ''
  type: APIReference
  url: https://ulehla.dev/.well-known/api-catalog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/ondraulehla
coverage:
  checked: '2026-10-31'
  detail: No OpenAPI, AsyncAPI, GraphQL, gRPC, or WSDL contract is published; only an MCP endpoint is available.
  evidence:
  - status: 200
    url: https://mcpcost.ulehla.dev/mcp
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-31'
description: Ulehla-dev is the personal brand and professional portfolio of Ondřej Úlehla, a full‑stack developer and AI engineer based in Prague. He builds fast, well‑crafted software products, ranging from client‑side applications to cloud‑native back‑ends, and shares his work, projects, and insights through open‑source repositories, blog‑style markdown profiles, and a public API catalog. The site showcases his technical expertise, open‑source contributions, and offers machine‑readable documentation for developers and AI agents.
image: https://ulehla.dev/og/default-en.png
layout: provider
mcp_servers:
- description: Remote MCP server at mcpcost.ulehla.dev.
  name: ulehla-dev MCP Server
  slug: ulehla-dev-mcp-yml
modified: '2026-10-31'
name: ulehla-dev
nav: Providers
network: true
overview: 'ulehla-dev is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Full-Stack, AI Engineer, Developers, Personal Site, and Open Source.


  ulehla-dev''s developer surface includes CLI, sandbox, documentation, API reference, and 12 more developer resources.'
plans:
- name: Ulehla Dev Plans Pricing
  plan_count: 0
  slug: ulehla-dev-plans-pricing
random_paper: 15
rate_limits:
- limit_count: 0
  name: Ulehla Dev Rate Limits
  slug: ulehla-dev-rate-limits
scopes:
- name: Ulehla Dev Scopes
  scope_count: 0
  slug: ulehla-dev-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: emerging
  composite: 13.5
  coverage:
    artifact_dirs: 23
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -2.7
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 25.5
    discoverability: 56.7
    operational_transparency: 13.2
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - czech-republic
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
  previous_composite: 16.2
  provenance:
    conformance: unknown
    mcp: first-party
    skills: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 21.6
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/ulehla-dev/ulehla-dev-2026-11-03T145356.png
security:
- kind: authentication
  name: Ulehla Dev Authentication
  slug: ulehla-dev-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Ulehla Dev Domain Security
  slug: ulehla-dev-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Ulehla Dev Vulnerability Disclosure
  slug: ulehla-dev-vulnerability-disclosure
  summary_line: security.txt · contact published
skill_count: 1
skills:
- name: mcp-tools
  slug: ulehla-dev-mcp-tools
slug: ulehla-dev
tags:
- Full-Stack
- AI Engineer
- Developers
- Personal Site
- Open Source
website: https://ulehla.dev/
---
