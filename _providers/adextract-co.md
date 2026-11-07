---
access_model:
  confidence: medium
  gated: none
  gated_source:
  - onboarding
  label: Free · Self-serve signup
  onboarding: self-serve
  pricing: free
  public: false
  source:
  - plans
  - authentication
  - security
  trial: false
  try_now: true
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
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 19.6
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: Hosted MCP server providing ad intelligence for AI agents across Meta, Google, TikTok, and LinkedIn. Connect via the MCP endpoint to search competitor ads.
  name: adextract MCP Server
  slug: adextract-mcp-server
artifact_total: 6
common:
- group: commercial
  href: https://artifacts.apis.io/adextract-co/plans/adextract-co-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/adextract-co-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/adextract-co/conventions/adextract-co-conventions.yml
  title: ''
  type: Conventions
  url: conventions/adextract-co-conventions.yml
- group: auth
  href: https://artifacts.apis.io/adextract-co/authentication/adextract-co-authentication.yml
  title: ''
  type: Authentication
  url: authentication/adextract-co-authentication.yml
- group: agent
  href: https://artifacts.apis.io/adextract-co/llms/adextract-co-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/adextract-co-llms.txt
- group: agent
  href: https://artifacts.apis.io/adextract-co/mcp/adextract-co-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/adextract-co-mcp.yml
- group: agent
  href: https://artifacts.apis.io/adextract-co/well-known/adextract-co-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/adextract-co-well-known.yml
- group: other
  href: https://artifacts.apis.io/adextract-co/hosts/adextract-co-hosts.yml
  title: ''
  type: Hosts
  url: hosts/adextract-co-hosts.yml
- group: other
  href: https://artifacts.apis.io/adextract-co/vendors/adextract-co-vendors.yml
  title: ''
  type: Vendors
  url: vendors/adextract-co-vendors.yml
- group: docs
  title: ''
  type: Documentation
  url: https://adextract.co/documentation
- group: start
  title: ''
  type: GettingStarted
  url: https://adextract.co/blog/conversion-tracking-setup-solo-founder
- group: auth
  href: https://artifacts.apis.io/adextract-co/security/adextract-co-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/adextract-co-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://adextract.co/
- group: company
  title: ''
  type: Blog
  url: https://adextract.co/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://adextract.co/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://adextract.co/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://adextract.co/privacy
coverage:
  checked: '2026-10-31'
  detail: Documentation provides an MCP endpoint but no OpenAPI, AsyncAPI, GraphQL, gRPC, or WSDL contract.
  evidence:
  - status: 200
    url: https://adextract.co/documentation
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-31'
description: adextract provides ad intelligence for AI agents, allowing searches across Meta, Google, TikTok, and LinkedIn ad libraries. The hosted MCP server lets Claude, Hermes, OpenClaw, Codex, Cursor, and other agents retrieve competitor ads in plain language. It normalizes results with advertiser, headline, body, media URLs, dates, and adds structured marketing insights such as creative description, marketing goal, target audience, emotion scores, and industry fields. Users can compare creatives across platforms, with quick setup via a single MCP URL and API key or OAuth, and start with 50 free searches.
image: https://adextract.co/favicon-32.png
layout: provider
mcp_servers:
- description: Remote MCP server at mcp.adextract.co requiring an API key.
  name: adextract MCP Server
  slug: adextract-co-mcp-yml
modified: '2026-10-31'
name: adextract
nav: Providers
network: true
overview: 'adextract is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Advertising, Artificial Intelligence, MCP, Marketing, and Competitor Analysis.


  adextract''s developer surface includes authentication, documentation, getting-started guide, engineering blog, pricing, and 11 more developer resources.'
plans:
- name: Adextract Co Plans Pricing
  plan_count: 2
  slug: adextract-co-plans-pricing
random_paper: 15
scopes:
- name: Adextract Co Scopes
  scope_count: 0
  slug: adextract-co-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: emerging
  composite: 19.9
  coverage:
    artifact_dirs: 16
    catalog_earned: 45.0
    catalog_earned_first_party: 8.0
    catalog_gap: 70.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -6.1
  facets:
    access_clarity: 36.8
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 23.8
    discoverability: 65.0
    operational_transparency: 0.0
  previous_composite: 26.0
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 23.6
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Adextract Co Authentication
  slug: adextract-co-authentication
  summary_line: 2 schemes
- kind: domain-security
  name: Adextract Co Domain Security
  slug: adextract-co-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: adextract-co
tags:
- Advertising
- Artificial Intelligence
- MCP
- Marketing
- Competitor Analysis
website: https://adextract.co/
---
