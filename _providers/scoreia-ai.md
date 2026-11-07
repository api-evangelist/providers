---
access_model:
  confidence: medium
  gated: none
  gated_source:
  - onboarding
  label: Paid · Open access
  onboarding: open
  pricing: paid
  public: true
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
    well_known_catalog: false
  schema_version: '0.2'
  score: 9.6
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: ScoreIA Multi‑Agent Competition Protocol (MCP) API exposing tools for AI agent benchmarking.
  name: ScoreIA MCP
  slug: scoreia-mcp
artifact_total: 8
common:
- group: commercial
  href: https://artifacts.apis.io/scoreia-ai/plans/scoreia-ai-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/scoreia-ai-plans-pricing.yml
- group: build
  href: https://artifacts.apis.io/scoreia-ai/cli/scoreia-ai-cli.yml
  title: ''
  type: CLI
  url: cli/scoreia-ai-cli.yml
- group: auth
  href: https://artifacts.apis.io/scoreia-ai/security/scoreia-ai-vulnerability-disclosure.yml
  title: ''
  type: Security
  url: security/scoreia-ai-vulnerability-disclosure.yml
- group: agent
  href: https://artifacts.apis.io/scoreia-ai/llms/scoreia-ai-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/scoreia-ai-llms.txt
- group: agent
  href: https://artifacts.apis.io/scoreia-ai/mcp/scoreia-ai-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/scoreia-ai-mcp.yml
- group: auth
  href: https://artifacts.apis.io/scoreia-ai/well-known/scoreia-ai-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/scoreia-ai-security.txt
- group: agent
  href: https://artifacts.apis.io/scoreia-ai/well-known/scoreia-ai-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/scoreia-ai-well-known.yml
- group: other
  href: https://artifacts.apis.io/scoreia-ai/hosts/scoreia-ai-hosts.yml
  title: ''
  type: Hosts
  url: hosts/scoreia-ai-hosts.yml
- group: other
  href: https://artifacts.apis.io/scoreia-ai/vendors/scoreia-ai-vendors.yml
  title: ''
  type: Vendors
  url: vendors/scoreia-ai-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://scoreia.ai/en/terms
- group: auth
  href: https://artifacts.apis.io/scoreia-ai/security/scoreia-ai-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/scoreia-ai-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/scoreia-ai/security/scoreia-ai-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/scoreia-ai-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://scoreia.ai/
- group: docs
  title: ''
  type: Documentation
  url: https://scoreia.ai/protocole/mcp/
- group: docs
  title: ''
  type: APIReference
  url: https://scoreia.ai/protocole/mcp/
- group: start
  title: ''
  type: GettingStarted
  url: https://scoreia.ai/protocole/mcp/
- group: operate
  title: ''
  type: Support
  url: https://scoreia.ai/contact
- group: commercial
  title: ''
  type: Pricing
  url: https://scoreia.ai/pricing
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://scoreia.ai/privacy
- group: operate
  title: ''
  type: Roadmap
  url: https://scoreia.ai/roadmap
created: '2026-10-29'
description: ScoreIA is a French platform that lets users test, benchmark, and compare AI agents such as Claude, GPT, Grok, and DeepSeek using the Multi‑Agent Competition Protocol (MCP). Users can pit agents against a dragon in 3‑D duels, run private head‑to‑head matches, and view detailed, verifiable results. The service provides public leaderboards, customizable challenges, and an open protocol for reproducible AI evaluation, aiming to foster transparent AI performance assessment.
image: https://scoreia.ai/rencontres/return-poster.jpg
layout: provider
mcp_servers:
- description: Remote MCP server at scoreia.ai.
  name: scoreia-ai MCP Server
  slug: scoreia-ai-mcp-yml
modified: '2026-10-29'
name: scoreia-ai
nav: Providers
network: true
overview: 'scoreia-ai is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Artificial Intelligence, Benchmarks, MCP, and Gaming.


  scoreia-ai''s developer surface includes CLI, documentation, API reference, getting-started guide, support, pricing, and 14 more developer resources.'
plans:
- name: Scoreia Ai Plans Pricing
  plan_count: 1
  slug: scoreia-ai-plans-pricing
random_paper: 5
rate_limits:
- limit_count: 0
  name: Scoreia Ai Rate Limits
  slug: scoreia-ai-rate-limits
scopes:
- name: Scoreia Ai Scopes
  scope_count: 0
  slug: scoreia-ai-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: emerging
  composite: 22.6
  coverage:
    artifact_dirs: 21
    catalog_earned: 45.0
    catalog_earned_first_party: 8.0
    catalog_gap: 70.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -7.4
  facets:
    access_clarity: 36.8
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 23.8
    discoverability: 75.0
    operational_transparency: 13.2
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - france
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 30.0
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
screenshot: https://apis.io/screenshots/scoreia-ai/scoreia-ai-2026-11-03T142822.png
security:
- kind: authentication
  name: Scoreia Ai Authentication
  slug: scoreia-ai-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Scoreia Ai Domain Security
  slug: scoreia-ai-domain-security
  summary_line: TLSv1.3 · HSTS
- kind: vulnerability-disclosure
  name: Scoreia Ai Vulnerability Disclosure
  slug: scoreia-ai-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: scoreia-ai
tags:
- Company
- Artificial Intelligence
- Benchmarks
- MCP
- Gaming
website: https://scoreia.ai/
---
