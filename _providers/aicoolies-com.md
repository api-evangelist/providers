---
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: unknown
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: documented
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 13.5
  scored_at: '2026-10-31'
api_count: 1
apis:
- description: Catalog, dataset, health, discovery, and MCP endpoints for aicoolies.com. Public reads require no credential; MCP community writes accept a scoped GitHub-bound personal access token.
  name: aicoolies Public API
  slug: aicoolies-public-api
artifact_total: 7
common:
- group: operate
  href: https://artifacts.apis.io/aicoolies-com/rate-limits/aicoolies-com-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/aicoolies-com-rate-limits.yml
- group: agent
  href: https://artifacts.apis.io/aicoolies-com/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: build
  href: https://artifacts.apis.io/aicoolies-com/cli/aicoolies-com-cli.yml
  title: ''
  type: CLI
  url: cli/aicoolies-com-cli.yml
- group: design
  href: https://artifacts.apis.io/aicoolies-com/conventions/aicoolies-com-conventions.yml
  title: ''
  type: Conventions
  url: conventions/aicoolies-com-conventions.yml
- group: auth
  href: https://artifacts.apis.io/aicoolies-com/security/aicoolies-com-vulnerability-disclosure.yml
  title: ''
  type: Security
  url: security/aicoolies-com-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/aicoolies-com/authentication/aicoolies-com-authentication.yml
  title: ''
  type: Authentication
  url: authentication/aicoolies-com-authentication.yml
- group: auth
  href: https://artifacts.apis.io/aicoolies-com/scopes/aicoolies-com-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/aicoolies-com-scopes.yml
- group: operate
  href: https://artifacts.apis.io/aicoolies-com/lifecycle/aicoolies-com-lifecycle.yml
  title: ''
  type: Deprecation
  url: lifecycle/aicoolies-com-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/aicoolies-com/lifecycle/aicoolies-com-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/aicoolies-com-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/aicoolies-com/conformance/aicoolies-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/aicoolies-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/aicoolies-com/llms/aicoolies-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/aicoolies-com-llms.txt
- group: agent
  href: https://artifacts.apis.io/aicoolies-com/mcp/aicoolies-com-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/aicoolies-com-mcp.yml
- group: auth
  href: https://artifacts.apis.io/aicoolies-com/well-known/aicoolies-com-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/aicoolies-com-security.txt
- group: agent
  href: https://artifacts.apis.io/aicoolies-com/well-known/aicoolies-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/aicoolies-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/aicoolies-com/hosts/aicoolies-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/aicoolies-com-hosts.yml
- group: build
  href: https://artifacts.apis.io/aicoolies-com/packages/aicoolies-com-packages.yml
  title: ''
  type: SDKs
  url: packages/aicoolies-com-packages.yml
- group: build
  href: https://artifacts.apis.io/aicoolies-com/packages/aicoolies-com-packages.yml
  title: ''
  type: Packages
  url: packages/aicoolies-com-packages.yml
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://aicoolies.com/privacy
- group: commercial
  title: ''
  type: Pricing
  url: https://aicoolies.com/pricing
- group: start
  title: ''
  type: DeveloperPortal
  url: https://aicoolies.com/developers
- group: docs
  title: ''
  type: APIReference
  url: https://aicoolies.com/tools/redoc
- group: auth
  href: https://artifacts.apis.io/aicoolies-com/security/aicoolies-com-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/aicoolies-com-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/aicoolies-com/security/aicoolies-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/aicoolies-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://aicoolies.com
created: '2026-10-28'
description: aicoolies is an open directory of AI developer tools that aggregates reviews, pricing information, side‑by‑side comparisons, and recommendations to help developers discover, evaluate, and choose the best AI‑powered solutions for their projects. The platform curates tool listings, provides detailed insights, and aims to simplify the decision‑making process for engineers, product teams, and technology enthusiasts.
image: https://aicoolies.com/og.png
layout: provider
mcp_servers:
- description: Remote MCP server at aicoolies.com.
  name: aicoolies MCP Server
  slug: aicoolies-com-mcp-yml
modified: '2026-10-28'
name: aicoolies
nav: Providers
network: true
overview: 'aicoolies is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, AI, Developer Tools, Directory, and Reviews.


  aicoolies'' developer surface includes CLI, authentication, pricing, API reference, and 20 more developer resources.'
random_paper: 20
rate_limits:
- limit_count: 1
  name: Aicoolies Com Rate Limits
  slug: aicoolies-com-rate-limits
scopes:
- name: Aicoolies Com Scopes
  scope_count: 7
  slug: aicoolies-com-scopes
  summary_line: 7 scopes
score:
  band: thin
  composite: 30.7
  coverage:
    artifact_dirs: 19
    catalog_earned: 45.0
    catalog_earned_first_party: 8.0
    catalog_gap: 70.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 21.1
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 49.3
    discoverability: 65.0
    operational_transparency: 39.5
  provenance:
    conformance: first-party
    mcp: first-party
    skills: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 33.6
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Aicoolies Com Authentication
  slug: aicoolies-com-authentication
  summary_line: 2 schemes
- kind: domain-security
  name: Aicoolies Com Domain Security
  slug: aicoolies-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Aicoolies Com Vulnerability Disclosure
  slug: aicoolies-com-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: aicoolies-com
tags:
- Company
- AI
- Developer Tools
- Directory
- Reviews
- Comparisons
website: https://aicoolies.com
---
