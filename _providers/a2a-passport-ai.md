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
    agent_card: flavored
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
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: true
  schema_version: '0.2'
  score: 13.9
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: 'One document, three questions. A passport is a signed document for a product or a retail banner: where its record lives, where it is on the record, who lists it, where the money door is. Issued live f'
  name: MCP
  slug: mcp
artifact_total: 7
common:
- group: agent
  href: https://artifacts.apis.io/a2a-passport-ai/llms/a2a-passport-ai-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/a2a-passport-ai-llms.txt
- group: agent
  href: https://artifacts.apis.io/a2a-passport-ai/mcp/a2a-passport-ai-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/a2a-passport-ai-mcp.yml
- group: auth
  href: https://artifacts.apis.io/a2a-passport-ai/well-known/a2a-passport-ai-mcp-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/a2a-passport-ai-mcp-security.txt
- group: agent
  href: https://artifacts.apis.io/a2a-passport-ai/well-known/a2a-passport-ai-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/a2a-passport-ai-well-known.yml
- group: other
  href: https://artifacts.apis.io/a2a-passport-ai/hosts/a2a-passport-ai-hosts.yml
  title: ''
  type: Hosts
  url: hosts/a2a-passport-ai-hosts.yml
- group: other
  href: https://artifacts.apis.io/a2a-passport-ai/vendors/a2a-passport-ai-vendors.yml
  title: ''
  type: Vendors
  url: vendors/a2a-passport-ai-vendors.yml
- group: auth
  href: https://artifacts.apis.io/a2a-passport-ai/security/a2a-passport-ai-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/a2a-passport-ai-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://a2a-passport.ai/
- group: docs
  title: ''
  type: Documentation
  url: https://a2a-passport.ai/.well-known/api-catalog
- group: other
  title: ''
  type: AgentCard
  url: https://a2a-passport.ai/.well-known/agent-card.json
- group: docs
  title: ''
  type: APIReference
  url: https://a2a-passport.ai/.well-known/api-catalog
- group: start
  title: ''
  type: GettingStarted
  url: https://a2a-passport.ai/index.md
created: '2026-10-31'
description: 'A passport is a signed document for a product or a retail banner: where its record lives, where it is on the record, who lists it, where the money door is. Issued live from the GSC hubs, stamped every week.'
image: https://a2a-passport.ai/favicon.svg
layout: provider
mcp_servers:
- description: Remote MCP server at mcp.gtinfetch.ai.
  name: A2A Passport MCP Server
  slug: a2a-passport-ai-mcp-yml
modified: '2026-10-31'
name: A2A Passport
nav: Providers
network: true
overview: 'A2A Passport is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include GTIN, Retail, Product Data, and Passport.


  A2A Passport''s developer surface includes documentation, API reference, getting-started guide, and 9 more developer resources.'
plans:
- name: A2A Passport Ai Plans Pricing
  plan_count: 0
  slug: a2a-passport-ai-plans-pricing
random_paper: 12
rate_limits:
- limit_count: 0
  name: A2A Passport Ai Rate Limits
  slug: a2a-passport-ai-rate-limits
scopes:
- name: A2A Passport Ai Scopes
  scope_count: 0
  slug: a2a-passport-ai-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: minimal
  composite: 10.0
  coverage:
    artifact_dirs: 20
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -3.7
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 14.3
    discoverability: 56.7
    operational_transparency: 10.5
  previous_composite: 13.7
  provenance:
    conformance: unknown
    mcp: first-party
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 15.7
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: A2A Passport Ai Authentication
  slug: a2a-passport-ai-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: A2A Passport Ai Domain Security
  slug: a2a-passport-ai-domain-security
  summary_line: TLSv1.3
slug: a2a-passport-ai
tags:
- GTIN
- Retail
- Product Data
- Passport
website: https://a2a-passport.ai/
---
