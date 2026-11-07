---
access_model:
  confidence: low
  label: Freemium
  onboarding: unknown
  pricing: freemium
  public: false
  source:
  - plans
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
- description: Ship your first App Intent in 5 minutes — TypeScript, compiled to Swift, validated in a sandbox.
  name: Axint API
  slug: axint-api
artifact_total: 4
common:
- group: commercial
  href: https://artifacts.apis.io/axint-ai/plans/axint-ai-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/axint-ai-plans-pricing.yml
- group: agent
  href: https://artifacts.apis.io/axint-ai/llms/axint-ai-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/axint-ai-llms.txt
- group: agent
  href: https://artifacts.apis.io/axint-ai/mcp/axint-ai-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/axint-ai-mcp.yml
- group: agent
  href: https://artifacts.apis.io/axint-ai/well-known/axint-ai-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/axint-ai-well-known.yml
- group: other
  href: https://artifacts.apis.io/axint-ai/hosts/axint-ai-hosts.yml
  title: ''
  type: Hosts
  url: hosts/axint-ai-hosts.yml
- group: other
  href: https://artifacts.apis.io/axint-ai/vendors/axint-ai-vendors.yml
  title: ''
  type: Vendors
  url: vendors/axint-ai-vendors.yml
- group: build
  href: https://artifacts.apis.io/axint-ai/packages/axint-ai-packages.yml
  title: ''
  type: SDKs
  url: packages/axint-ai-packages.yml
- group: build
  href: https://artifacts.apis.io/axint-ai/packages/axint-ai-packages.yml
  title: ''
  type: Packages
  url: packages/axint-ai-packages.yml
- group: auth
  title: ''
  type: TrustCenter
  url: https://axint.ai/trust
- group: commercial
  title: ''
  type: Pricing
  url: https://axint.ai/cloud/plans
- group: auth
  href: https://artifacts.apis.io/axint-ai/security/axint-ai-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/axint-ai-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://axint.ai/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.axint.ai/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.axint.ai/
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.axint.ai/guides/quickstart/
- group: company
  title: ''
  type: Blog
  url: https://axint.ai/blog
- group: commercial
  title: ''
  type: TermsOfService
  url: https://axint.ai/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://axint.ai/privacy
- group: build
  title: ''
  type: GitHubOrganization
  url: https://axint.ai/
coverage:
  checked: '2026-11-02'
  detail: Documentation is publicly available but no OpenAPI, AsyncAPI, GraphQL, or other machine-readable spec is published.
  evidence:
  - status: 404
    url: https://docs.axint.ai/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-11-02'
description: Axint provides an open-source compiler that transforms TypeScript, Python, and .axint definitions into Swift code for Apple platforms, emitting App Intents, SwiftUI views, WidgetKit widgets, and full apps. It includes evidence‑aware validation, Xcode build receipts, fix packets, and an MCP server for Claude, Cursor, and Windsurf, enabling automated repair and cloud‑based checks. The platform aims to streamline Apple software development with AI‑assisted tooling and comprehensive compatibility analysis across Xcode, Swift, and Apple Intelligence.
image: https://axint.ai/opengraph-image?c6899992a1c19e2e
layout: provider
mcp_servers:
- description: Remote MCP server at mcp.axint.ai.
  name: Axint MCP Server
  slug: axint-ai-mcp-yml
modified: '2026-11-02'
name: Axint
nav: Providers
network: true
overview: 'Axint is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Artificial Intelligence, Apple, Swift, Compilers, and Developer Tools.


  Axint''s developer surface includes pricing, documentation, getting-started guide, engineering blog, and 15 more developer resources.'
plans:
- name: Axint Ai Plans Pricing
  plan_count: 3
  slug: axint-ai-plans-pricing
random_paper: 3
score:
  band: emerging
  composite: 20.5
  coverage:
    artifact_dirs: 11
    catalog_earned: 44.0
    catalog_earned_first_party: 12.0
    catalog_gap: 71.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -8.5
  facets:
    access_clarity: 51.3
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 23.8
    discoverability: 56.7
    operational_transparency: 2.6
  previous_composite: 29.0
  provenance:
    mcp: first-party
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 11.4
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Axint Ai Domain Security
  slug: axint-ai-domain-security
  summary_line: TLSv1.3 · HSTS
slug: axint-ai
tags:
- Artificial Intelligence
- Apple
- Swift
- Compilers
- Developer Tools
website: https://axint.ai/
---
