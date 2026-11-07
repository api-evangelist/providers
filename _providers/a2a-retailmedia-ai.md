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
    protected_resource_metadata: documented
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: true
  schema_version: '0.2'
  score: 9.6
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: API for connecting agents, retrieving banner cards, and managing media placements as described in the Docs.
  name: A2A Retailmedia API
  slug: a2a-retailmedia-api
artifact_total: 5
common:
- group: agent
  href: https://artifacts.apis.io/a2a-retailmedia-ai/llms/a2a-retailmedia-ai-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/a2a-retailmedia-ai-llms.txt
- group: other
  href: https://artifacts.apis.io/a2a-retailmedia-ai/a2a/a2a-retailmedia-ai-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/a2a-retailmedia-ai-a2a.yml
- group: agent
  href: https://artifacts.apis.io/a2a-retailmedia-ai/mcp/a2a-retailmedia-ai-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/a2a-retailmedia-ai-mcp.yml
- group: agent
  href: https://artifacts.apis.io/a2a-retailmedia-ai/well-known/a2a-retailmedia-ai-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/a2a-retailmedia-ai-well-known.yml
- group: other
  href: https://artifacts.apis.io/a2a-retailmedia-ai/hosts/a2a-retailmedia-ai-hosts.yml
  title: ''
  type: Hosts
  url: hosts/a2a-retailmedia-ai-hosts.yml
- group: other
  href: https://artifacts.apis.io/a2a-retailmedia-ai/vendors/a2a-retailmedia-ai-vendors.yml
  title: ''
  type: Vendors
  url: vendors/a2a-retailmedia-ai-vendors.yml
- group: auth
  href: https://artifacts.apis.io/a2a-retailmedia-ai/security/a2a-retailmedia-ai-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/a2a-retailmedia-ai-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://a2a-retailmedia.ai/
- group: docs
  title: ''
  type: Documentation
  url: https://a2a-retailmedia.ai/docs
- group: start
  title: ''
  type: GettingStarted
  url: https://a2a-retailmedia.ai/setup
- group: operate
  title: ''
  type: Support
  url: https://a2a-retailmedia.ai/#contact
- group: commercial
  title: ''
  type: TermsOfService
  url: https://gsc-em.com/legal
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://gsc-em.com/privacy
coverage:
  checked: '2026-10-31'
  detail: Documentation is available but no OpenAPI/GraphQL/AsyncAPI spec was found.
  evidence:
  - status: 200
    url: https://a2a-retailmedia.ai/docs
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-31'
description: A2A Retailmedia is an agentic commerce hub that connects grocery retailers with makers through a Model Context Protocol (MCP) door. It enables retailers to claim media cards for each grocery banner and allows makers’ agents to discover and purchase media placements. The platform supports over 8,600 grocery banners across 20 markets, handling hundreds of thousands of makers. It offers self‑service setup, card claiming, and enrollment flows, and provides documentation and API access via a developer portal. Powered by gtinfetch.ai, A2A Retailmedia aims to streamline media buying on the shelf.
image: https://a2a-retailmedia.ai/og-image-1200x630.png
layout: provider
mcp_servers:
- description: Remote MCP server at a2a-retailmedia.ai.
  name: A2A Retailmedia MCP Server
  slug: a2a-retailmedia-ai-mcp-yml
modified: '2026-10-31'
name: A2A Retailmedia
nav: Providers
network: true
overview: 'A2A Retailmedia is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Retail, Media, AI Agents, and Grocery.


  A2A Retailmedia''s developer surface includes documentation, getting-started guide, support, and 10 more developer resources.'
random_paper: 9
scopes:
- name: A2A Retailmedia Ai Scopes
  scope_count: 0
  slug: a2a-retailmedia-ai-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: emerging
  composite: 11.1
  coverage:
    artifact_dirs: 19
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -6.1
  facets:
    access_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 13.1
    discoverability: 56.7
    operational_transparency: 0.0
  previous_composite: 17.2
  provenance:
    conformance: unknown
    mcp: first-party
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 19.6
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: A2A Retailmedia Ai Authentication
  slug: a2a-retailmedia-ai-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: A2A Retailmedia Ai Domain Security
  slug: a2a-retailmedia-ai-domain-security
  summary_line: TLSv1.3 · HSTS
slug: a2a-retailmedia-ai
tags:
- Retail
- Media
- AI Agents
- Grocery
website: https://a2a-retailmedia.ai/
---
