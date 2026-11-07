---
access_model:
  confidence: medium
  gated: none
  gated_source:
  - onboarding
  label: Open access
  onboarding: open
  pricing: unknown
  public: true
  source:
  - authentication
  - rate-limits
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
    well_known_catalog: true
  schema_version: '0.2'
  score: 12.4
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: Managed Content Publishing (MCP) service allowing agents to publish and manage apps.
  name: Reachpad MCP
  slug: reachpad-mcp
artifact_total: 7
common:
- group: operate
  href: https://artifacts.apis.io/reachpad-dev/rate-limits/reachpad-dev-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/reachpad-dev-rate-limits.yml
- group: build
  href: https://artifacts.apis.io/reachpad-dev/cli/reachpad-dev-cli.yml
  title: ''
  type: CLI
  url: cli/reachpad-dev-cli.yml
- group: design
  href: https://artifacts.apis.io/reachpad-dev/lifecycle/reachpad-dev-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/reachpad-dev-lifecycle.yml
- group: agent
  href: https://artifacts.apis.io/reachpad-dev/llms/reachpad-dev-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/reachpad-dev-llms.txt
- group: agent
  href: https://artifacts.apis.io/reachpad-dev/mcp/reachpad-dev-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/reachpad-dev-mcp.yml
- group: agent
  href: https://artifacts.apis.io/reachpad-dev/well-known/reachpad-dev-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/reachpad-dev-well-known.yml
- group: other
  href: https://artifacts.apis.io/reachpad-dev/hosts/reachpad-dev-hosts.yml
  title: ''
  type: Hosts
  url: hosts/reachpad-dev-hosts.yml
- group: other
  href: https://artifacts.apis.io/reachpad-dev/vendors/reachpad-dev-vendors.yml
  title: ''
  type: Vendors
  url: vendors/reachpad-dev-vendors.yml
- group: build
  href: https://artifacts.apis.io/reachpad-dev/packages/reachpad-dev-packages.yml
  title: ''
  type: SDKs
  url: packages/reachpad-dev-packages.yml
- group: build
  href: https://artifacts.apis.io/reachpad-dev/packages/reachpad-dev-packages.yml
  title: ''
  type: Packages
  url: packages/reachpad-dev-packages.yml
- group: auth
  href: https://artifacts.apis.io/reachpad-dev/security/reachpad-dev-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/reachpad-dev-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://reachpad.dev/
- group: company
  title: ''
  type: Blog
  url: https://reachpad.dev/blog
- group: docs
  title: ''
  type: Documentation
  url: https://reachpad.dev/docs
- group: start
  title: ''
  type: DeveloperPortal
  url: https://reachpad.dev/docs
- group: docs
  title: ''
  type: APIReference
  url: https://reachpad.dev/docs
- group: start
  title: ''
  type: Login
  url: https://reachpad.dev/sign-in?returnTo=/apps
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://reachpad.dev/privacy
- group: commercial
  title: ''
  type: Pricing
  url: https://reachpad.dev/pricing
- group: start
  title: ''
  type: SignUp
  url: https://reachpad.dev/sign-up
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Reachpad
created: '2026-10-31'
description: Reachpad is a platform that lets users turn ideas into AI‑powered apps, publish them as shareable links, collaborate, manage versions, and control access. It integrates a coding agent, offers a Managed Content Publishing (MCP) service, and provides a web interface for creating, sharing, and managing apps with public, organization, or restricted access and full version history.
image: https://reachpad.dev/opengraph-image?9a7fa9eccc925bc4
json_schemas:
- name: Reachpad Dev Mcp
  property_count: 0
  slug: reachpad-dev-mcp
layout: provider
mcp_servers:
- description: Remote MCP server at reachpad.dev.
  name: reachpad-dev MCP Server
  slug: reachpad-dev-mcp-yml
modified: '2026-10-31'
name: reachpad-dev
nav: Providers
network: true
overview: 'reachpad-dev is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Artificial Intelligence, Collaboration, AppHosting, Low-Code, and Productivity.


  reachpad-dev''s developer surface includes CLI, engineering blog, documentation, API reference, pricing, signup flow, and 15 more developer resources.'
plans:
- name: Reachpad Dev Plans Pricing
  plan_count: 0
  slug: reachpad-dev-plans-pricing
random_paper: 12
rate_limits:
- limit_count: 6
  name: Reachpad Dev Rate Limits
  slug: reachpad-dev-rate-limits
score:
  band: emerging
  composite: 18.9
  coverage:
    artifact_dirs: 21
    catalog_earned: 49.0
    catalog_earned_first_party: 12.0
    catalog_gap: 66.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -6.9
  facets:
    access_clarity: 17.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 28.6
    discoverability: 65.0
    operational_transparency: 34.2
  previous_composite: 25.8
  provenance:
    mcp: first-party
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 7.3
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/reachpad-dev/reachpad-dev-2026-11-03T142009.png
security:
- kind: authentication
  name: Reachpad Dev Authentication
  slug: reachpad-dev-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Reachpad Dev Domain Security
  slug: reachpad-dev-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: reachpad-dev
tags:
- Artificial Intelligence
- Collaboration
- AppHosting
- Low-Code
- Productivity
website: https://reachpad.dev/
---
