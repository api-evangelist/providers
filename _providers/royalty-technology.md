---
access_model:
  confidence: medium
  gated: none
  gated_source:
  - onboarding
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
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
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: true
  schema_version: '0.2'
  score: 21.6
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: MCP (Machine Control Protocol) API for RoyalTea platform, providing tools for revenue split calculation, platform cuts, and studio setup.
  name: RoyalTea MCP
  slug: royaltea-mcp
artifact_total: 6
common:
- group: commercial
  href: https://artifacts.apis.io/royalty-technology/plans/royalty-technology-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/royalty-technology-plans-pricing.yml
- group: auth
  href: https://artifacts.apis.io/royalty-technology/authentication/royalty-technology-authentication.yml
  title: ''
  type: Authentication
  url: authentication/royalty-technology-authentication.yml
- group: design
  href: https://artifacts.apis.io/royalty-technology/lifecycle/royalty-technology-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/royalty-technology-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/royalty-technology/conformance/royalty-technology-conformance.yml
  title: ''
  type: Conformance
  url: conformance/royalty-technology-conformance.yml
- group: agent
  href: https://artifacts.apis.io/royalty-technology/llms/royalty-technology-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/royalty-technology-llms.txt
- group: agent
  href: https://artifacts.apis.io/royalty-technology/mcp/royalty-technology-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/royalty-technology-mcp.yml
- group: agent
  href: https://artifacts.apis.io/royalty-technology/well-known/royalty-technology-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/royalty-technology-well-known.yml
- group: other
  href: https://artifacts.apis.io/royalty-technology/hosts/royalty-technology-hosts.yml
  title: ''
  type: Hosts
  url: hosts/royalty-technology-hosts.yml
- group: other
  href: https://artifacts.apis.io/royalty-technology/vendors/royalty-technology-vendors.yml
  title: ''
  type: Vendors
  url: vendors/royalty-technology-vendors.yml
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://royalty.technology/privacy
- group: commercial
  title: ''
  type: Pricing
  url: https://royalty.technology/pricing
- group: docs
  title: ''
  type: Documentation
  url: https://royalty.technology/docs/mcp
- group: auth
  href: https://artifacts.apis.io/royalty-technology/security/royalty-technology-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/royalty-technology-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://royalty.technology/
coverage:
  checked: '2026-10-30'
  detail: Documentation is publicly available but no OpenAPI, AsyncAPI, GraphQL, or other machine‑readable spec is published.
  evidence:
  - status: 200
    url: https://royalty.technology/docs/mcp
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-30'
description: Royaltea (royalty.technology) is a SaaS platform that provides integrated game design tools—including tech and skill tree editors, lore bibles, level blockout planners, and pacing charts—within a single collaborative workspace. It combines project management features such as boards, sprints, roadmaps, and file storage with automated revenue‑sharing and contribution tracking, enabling indie studios and student teams to manage development and split future earnings transparently. The platform offers free core tools and a paid Pro tier, supports AI‑driven workflows via a 77‑tool MCP server, and integrates with popular services like Jira, GitHub, and Trello.
image: https://royalty.technology/images/social-card.jpg
layout: provider
mcp_servers:
- description: Remote MCP server at api.royalty.technology.
  name: royalty-technology MCP Server
  slug: royalty-technology-mcp-yml
modified: '2026-10-30'
name: royalty-technology
nav: Providers
network: true
overview: 'royalty-technology is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Game Development, Collaboration, Revenue Sharing, and Software-as-a-Service.


  royalty-technology''s developer surface includes authentication, pricing, documentation, and 11 more developer resources.'
plans:
- name: Royalty Technology Plans Pricing
  plan_count: 4
  slug: royalty-technology-plans-pricing
random_paper: 21
scopes:
- name: Royalty Technology Scopes
  scope_count: 0
  slug: royalty-technology-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: emerging
  composite: 23.3
  coverage:
    artifact_dirs: 19
    catalog_earned: 49.0
    catalog_earned_first_party: 12.0
    catalog_gap: 66.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -3.3
  facets:
    access_clarity: 42.1
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 16.7
    discoverability: 73.2
    operational_transparency: 0.0
  previous_composite: 26.6
  provenance:
    conformance: first-party
    mcp: first-party
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 28.4
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/royalty-technology/royalty-technology-2026-11-03T142446.png
security:
- kind: authentication
  name: Royalty Technology Authentication
  slug: royalty-technology-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Royalty Technology Domain Security
  slug: royalty-technology-domain-security
  summary_line: TLSv1.3 · HSTS
slug: royalty-technology
tags:
- Company
- Game Development
- Collaboration
- Revenue Sharing
- Software-as-a-Service
website: https://royalty.technology/
---
