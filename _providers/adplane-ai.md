---
access_model:
  confidence: low
  gated: none
  gated_source:
  - onboarding
  label: Self-serve signup
  onboarding: self-serve
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
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: documented
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
  score: 25.0
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: Adplane provides an API for managing Google, Meta, Microsoft, and TikTok advertising campaigns via a conversational interface.
  name: Adplane API
  slug: adplane-api
artifact_total: 5
common:
- group: auth
  href: https://artifacts.apis.io/adplane-ai/authentication/adplane-ai-authentication.yml
  title: ''
  type: Authentication
  url: authentication/adplane-ai-authentication.yml
- group: design
  href: https://artifacts.apis.io/adplane-ai/errors/adplane-ai-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/adplane-ai-problem-types.yml
- group: agent
  href: https://artifacts.apis.io/adplane-ai/llms/adplane-ai-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/adplane-ai-llms.txt
- group: agent
  href: https://artifacts.apis.io/adplane-ai/mcp/adplane-ai-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/adplane-ai-mcp.yml
- group: auth
  href: https://artifacts.apis.io/adplane-ai/well-known/adplane-ai-chatgpt-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/adplane-ai-chatgpt-security.txt
- group: agent
  href: https://artifacts.apis.io/adplane-ai/well-known/adplane-ai-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/adplane-ai-well-known.yml
- group: other
  href: https://artifacts.apis.io/adplane-ai/hosts/adplane-ai-hosts.yml
  title: ''
  type: Hosts
  url: hosts/adplane-ai-hosts.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://adplane.ai/terms
- group: operate
  title: ''
  type: Support
  url: https://adplane.ai/help
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://adplane.ai/privacy
- group: start
  title: ''
  type: Login
  url: https://adplane.ai/auth/google/login
- group: auth
  href: https://artifacts.apis.io/adplane-ai/security/adplane-ai-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/adplane-ai-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://adplane.ai/
- group: docs
  title: ''
  type: Documentation
  url: https://adplane.ai/docs
- group: start
  title: ''
  type: GettingStarted
  url: https://adplane.ai/guides
- group: other
  title: ''
  type: Installation
  url: https://adplane.ai/install
- group: commercial
  title: ''
  type: Pricing
  url: https://adplane.ai/#pricing
coverage:
  checked: '2026-10-31'
  detail: API documentation pages (e.g., /google-ads-api) return a 200 page indicating the product does not exist without authentication, showing the API is behind a login wall.
  evidence:
  - status: 200
    url: https://adplane.ai/google-ads-api
  reason: auth-required
  state: gated
created: '2026-10-31'
description: Adplane enables users to run all their Google, Meta, Microsoft, and TikTok advertising campaigns through a conversational interface powered by Claude or ChatGPT. By connecting multiple ad accounts to a single chat, users can ask questions, retrieve reports, adjust budgets, and make campaign changes in real time, all after a one‑click sign‑in. The platform offers a free trial and a $9.95 per month plan.
image: https://adplane.ai/opengraph-image.png?284751221cb5c74a
layout: provider
mcp_servers:
- description: Remote MCP server at mcp.adplane.ai requiring OAuth.
  name: Adplane MCP Server
  slug: adplane-ai-mcp-yml
modified: '2026-10-31'
name: Adplane
nav: Providers
network: true
overview: 'Adplane is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Ads, Artificial Intelligence, ChatGPT, Claude, and Marketing Automation.


  Adplane''s developer surface includes authentication, support, documentation, getting-started guide, pricing, and 12 more developer resources.'
random_paper: 12
scopes:
- name: Adplane Ai Scopes
  scope_count: 0
  slug: adplane-ai-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: emerging
  composite: 17.8
  coverage:
    artifact_dirs: 17
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -7.6
  facets:
    access_clarity: 22.4
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 25.0
    discoverability: 56.7
    operational_transparency: 10.5
  previous_composite: 25.4
  provenance:
    conformance: unknown
    mcp: first-party
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
  name: Adplane Ai Authentication
  slug: adplane-ai-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Adplane Ai Domain Security
  slug: adplane-ai-domain-security
  summary_line: TLSv1.3 · DMARC
slug: adplane-ai
tags:
- Ads
- Artificial Intelligence
- ChatGPT
- Claude
- Marketing Automation
- Ad Management
website: https://adplane.ai/
---
