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
    mcp_server: false
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 8.3
  scored_at: '2026-10-31'
api_count: 1
apis:
- description: PowMCP provides a suite of web-based developer utilities accessible via its web interface.
  name: PowMCP Developer Tools
  slug: powmcp-developer-tools
artifact_total: 6
common:
- group: operate
  href: https://artifacts.apis.io/powmcp-com/rate-limits/powmcp-com-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/powmcp-com-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/powmcp-com/plans/powmcp-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/powmcp-com-plans-pricing.yml
- group: agent
  href: https://artifacts.apis.io/powmcp-com/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: auth
  href: https://artifacts.apis.io/powmcp-com/authentication/powmcp-com-authentication.yml
  title: ''
  type: Authentication
  url: authentication/powmcp-com-authentication.yml
- group: auth
  href: https://artifacts.apis.io/powmcp-com/scopes/powmcp-com-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/powmcp-com-scopes.yml
- group: agent
  href: https://artifacts.apis.io/powmcp-com/llms/powmcp-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/powmcp-com-llms.txt
- group: other
  href: https://artifacts.apis.io/powmcp-com/hosts/powmcp-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/powmcp-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/powmcp-com/vendors/powmcp-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/powmcp-com-vendors.yml
- group: auth
  title: ''
  type: Security
  url: https://powmcp.com/apps/categories/security/
- group: company
  title: ''
  type: Newsroom
  url: https://powmcp.com/apps/categories/media/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://powmcp.com/apps/categories/developer/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/powmcp
- group: auth
  href: https://artifacts.apis.io/powmcp-com/security/powmcp-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/powmcp-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://powmcp.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://powmcp.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://powmcp.com/privacy
coverage:
  checked: '2026-10-29'
  detail: Developer portal provides web tools but no machine‑readable API specification.
  evidence:
  - status: 200
    url: https://powmcp.com/apps/categories/developer/
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-29'
description: PowMCP offers a suite of single‑job utility applications designed to work with AI assistants such as ChatGPT, Claude, and MCP agents. These tools enable users to perform tasks like website checking, file validation, and other lightweight operations directly in the browser or through AI integrations. All apps are provided free of charge and aim to extend the capabilities of conversational AI platforms.
image: https://powmcp.com/images/logo/favicon/favicon-256.png
layout: provider
modified: '2026-10-29'
name: powmcp-com
nav: Providers
network: true
overview: 'powmcp-com is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include AI, Utilities, ChatGPT, Claude, and MCP.


  powmcp-com''s developer surface includes authentication and 15 more developer resources.'
plans:
- name: Powmcp Com Plans Pricing
  plan_count: 3
  slug: powmcp-com-plans-pricing
random_paper: 18
rate_limits:
- limit_count: 2
  name: Powmcp Com Rate Limits
  slug: powmcp-com-rate-limits
scopes:
- name: Powmcp Com Scopes
  scope_count: 0
  slug: powmcp-com-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: thin
  composite: 29.1
  coverage:
    artifact_dirs: 23
    catalog_earned: 52.0
    catalog_earned_first_party: 20.0
    catalog_gap: 63.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 52.6
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 27.9
    discoverability: 58.9
    operational_transparency: 36.8
  provenance:
    conformance: unknown
    mcp: derived
    skills: unknown
  regulatory:
    applies: true
    matched_via: tags
    regime: Energy & Utilities
    regime_id: energy_utilities
    score: 28.5
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Powmcp Com Authentication
  slug: powmcp-com-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Powmcp Com Domain Security
  slug: powmcp-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: powmcp-com
tags:
- AI
- Utilities
- ChatGPT
- Claude
- MCP
website: https://powmcp.com/
---
