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
  band: agent-aware
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
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: true
  schema_version: '0.2'
  score: 17.1
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 2
  human_in_the_loop: 0
  name: Blogbat Com Agentic Access
  operation_count: 2
  slug: blogbat-com-agentic-access
  summary_line: 2 operations · 2 acting
api_count: 1
apis:
- description: Agent-facing endpoints for BlogBat.
  name: BlogBat Agent API
  slug: blogbat-agent-api
artifact_total: 6
common:
- group: agent
  href: https://artifacts.apis.io/blogbat-com/agentic-access/blogbat-com-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/blogbat-com-agentic-access.yml
- group: design
  href: https://artifacts.apis.io/blogbat-com/rules/blogbat-com-rules.yml
  title: ''
  type: Spectral
  url: rules/blogbat-com-rules.yml
- group: design
  href: https://artifacts.apis.io/blogbat-com/errors/blogbat-com-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/blogbat-com-problem-types.yml
- group: design
  href: https://artifacts.apis.io/blogbat-com/conformance/blogbat-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/blogbat-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/blogbat-com/llms/blogbat-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/blogbat-com-llms.txt
- group: other
  href: https://artifacts.apis.io/blogbat-com/a2a/blogbat-com-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/blogbat-com-a2a.yml
- group: agent
  href: https://artifacts.apis.io/blogbat-com/mcp/blogbat-com-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/blogbat-com-mcp.yml
- group: agent
  href: https://artifacts.apis.io/blogbat-com/well-known/blogbat-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/blogbat-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/blogbat-com/hosts/blogbat-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/blogbat-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/blogbat-com/vendors/blogbat-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/blogbat-com-vendors.yml
- group: operate
  title: ''
  type: Support
  url: https://blogbat.com/support
- group: start
  title: ''
  type: Login
  url: https://app.blogbat.com/login
- group: company
  title: ''
  type: Blog
  url: https://blogbat.com/blog
- group: start
  title: ''
  type: GettingStarted
  url: https://blogbat.com/docs#getting-started
- group: auth
  href: https://artifacts.apis.io/blogbat-com/authentication/blogbat-com-authentication.yml
  title: ''
  type: Authentication
  url: authentication/blogbat-com-authentication.yml
- group: auth
  href: https://artifacts.apis.io/blogbat-com/security/blogbat-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/blogbat-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://blogbat.com/
created: '2026-11-02'
description: BlogBat is a fast, multitenant blog platform on Cloudflare’s edge, offering AI‑assisted writing, SEO‑ready publishing, and custom‑domain support. Users can create blogs at yourname.blogbat.com or map their own domains, leveraging built‑in AI from Anthropic, OpenAI or Google, with no‑code editor and automatic sitemap and RSS generation.
image: https://blogbat.com/opengraph-image?ca4352566297ed70
layout: provider
mcp_servers:
- description: Remote MCP server at blogbat.com requiring an API key.
  name: BlogBat MCP Server
  slug: blogbat-com-mcp-yml
modified: '2026-11-02'
name: BlogBat
nav: Providers
network: true
overview: 'BlogBat is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Blogging, Artificial Intelligence, SEO, Multi-Tenant, and CustomDomain.


  The BlogBat catalog on APIs.io includes 1 Spectral governance ruleset.


  BlogBat''s developer surface includes support, engineering blog, getting-started guide, authentication, and 13 more developer resources.'
random_paper: 15
rules:
- authorship: generated
  effective_rule_count: 76
  extends:
  - spectral:oas
  name: BlogBat API Rules
  rule_count: 35
  severity_counts:
    error: 33
    hint: 0
    info: 1
    warn: 1
  slug: blogbat-com-rules
score:
  band: emerging
  composite: 14.3
  coverage:
    artifact_dirs: 14
    catalog_earned: 41.5
    catalog_earned_first_party: 0.0
    catalog_gap: 73.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 6.6
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 21.4
    discoverability: 65.0
    operational_transparency: 0.0
  provenance:
    agentic_access: derived
    conformance: derived
    mcp: first-party
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 15.5
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Blogbat Com Authentication
  slug: blogbat-com-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Blogbat Com Domain Security
  slug: blogbat-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: blogbat-com
tags:
- Blogging
- Artificial Intelligence
- SEO
- Multi-Tenant
- CustomDomain
website: https://blogbat.com/
---
