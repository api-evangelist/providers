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
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: false
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: derived
    event_surface_described: false
    idempotency: false
    mcp_server: platform
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: true
  schema_version: '0.2'
  score: 10.8
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 4
  human_in_the_loop: 1
  name: Anglero Com Agentic Access
  operation_count: 5
  slug: anglero-com-agentic-access
  summary_line: 5 operations · 4 acting · 1 human-in-the-loop
api_count: 1
apis:
- description: 'Public read tools for AI agents and Custom GPT Actions. Write tools (cart, forms) are omitted: they need a same-session WordPress REST nonce from the site page, not a public token.'
  name: WebMCP Tools
  slug: webmcp-tools
artifact_total: 8
common:
- group: agent
  href: https://artifacts.apis.io/anglero-com/agentic-access/anglero-com-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/anglero-com-agentic-access.yml
- group: design
  href: https://artifacts.apis.io/anglero-com/rules/anglero-com-rules.yml
  title: ''
  type: Spectral
  url: rules/anglero-com-rules.yml
- group: agent
  href: https://artifacts.apis.io/anglero-com/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/anglero-com/errors/anglero-com-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/anglero-com-problem-types.yml
- group: design
  href: https://artifacts.apis.io/anglero-com/conformance/anglero-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/anglero-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/anglero-com/llms/anglero-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/anglero-com-llms.txt
- group: agent
  href: https://artifacts.apis.io/anglero-com/mcp/anglero-com-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/anglero-com-mcp.yml
- group: agent
  href: https://artifacts.apis.io/anglero-com/well-known/anglero-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/anglero-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/anglero-com/hosts/anglero-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/anglero-com-hosts.yml
- group: company
  title: ''
  type: Newsroom
  url: https://anglero.com/media/
- group: auth
  href: https://artifacts.apis.io/anglero-com/security/anglero-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/anglero-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://anglero.com/
- group: docs
  title: ''
  type: Documentation
  url: https://anglero.com/.well-known/api-catalog
- group: docs
  title: ''
  type: APIReference
  url: https://anglero.com/wp-json/webmcp-bridge/v1/openapi
- group: company
  title: ''
  type: Blog
  url: https://anglero.com/blog/
- group: operate
  title: ''
  type: Support
  url: https://anglero.com/speaking-inquiry/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://anglero.com/privacy-policy/
coverage:
  detail: the company serves an API surface but requires credentials before any description of it can be read
  evidence:
  - status: 401
    url: https://anglero.com/mcp
  - status: 200
    url: https://anglero.com/
  reason: partner-login
  state: gated
created: '2026-11-01'
description: MerkabaPhi AS is a strategic AI advisory firm led by Thomas Anglero, offering executive leadership and board advisory services on AI transformation. Based in Oslo, Norway, the firm provides AI strategy consulting, keynote speaking, and advisory engagements, with Thomas delivering over 450 keynotes across 30+ countries, helping leaders navigate AI adoption and digital transformation.
image: https://anglero.com/wp-content/uploads/2023/06/Cognizant-Thomas-Anglero-3458.jpg
layout: provider
mcp_servers:
- description: Remote MCP server at anglero.com.
  name: MerkabaPhi AS MCP Server
  slug: anglero-com-mcp-yml
modified: '2026-11-01'
name: MerkabaPhi AS
nav: Providers
network: true
overview: 'MerkabaPhi AS is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Artificial Intelligence, Advisory, Consulting, Norway, and Leadership.


  The MerkabaPhi AS catalog on APIs.io includes 1 Spectral governance ruleset.


  MerkabaPhi AS''s developer surface includes documentation, API reference, engineering blog, support, and 13 more developer resources.'
random_paper: 4
rules:
- authorship: generated
  effective_rule_count: 54
  extends:
  - spectral:oas
  name: MerkabaPhi AS API Rules
  rule_count: 13
  severity_counts:
    error: 9
    hint: 0
    info: 3
    warn: 1
  slug: anglero-com-rules
scopes:
- name: Anglero Com Scopes
  scope_count: 0
  slug: anglero-com-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: emerging
  composite: 14.4
  coverage:
    artifact_dirs: 22
    catalog_earned: 41.5
    catalog_earned_first_party: 0.0
    catalog_gap: 73.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -3.7
  facets:
    access_clarity: 5.3
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 18.3
    discoverability: 65.8
    operational_transparency: 0.0
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - norway
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - europe
    - nordics
  previous_composite: 18.1
  provenance:
    agentic_access: derived
    conformance: derived
    mcp: platform-generated
    skills: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 20.9
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Anglero Com Authentication
  slug: anglero-com-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Anglero Com Domain Security
  slug: anglero-com-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
skill_count: 1
skills:
- name: get-site-info
  slug: anglero-com-get-site-info
slug: anglero-com
tags:
- Artificial Intelligence
- Advisory
- Consulting
- Norway
- Leadership
- Company
website: https://anglero.com/
---
