---
access_model:
  confidence: medium
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    openapi_examples: partial
    operation_distinctiveness: distinct
    pagination_ratio: partial
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 43.9
  scored_at: '2026-10-31'
agentic_access:
- acting_count: 1
  human_in_the_loop: 0
  name: Sourcebot Agentic Access
  operation_count: 17
  slug: sourcebot-agentic-access
  summary_line: 17 operations · 1 acting
api_count: 1
apis:
- baseURL: https://app.sourcebot.dev
  baseurl_source: declared
  description: Enterprise endpoints for user management and audit logging.
  name: Sourcebot Enterprise (EE) API
  slug: sourcebot-enterprise-ee-api
- baseURL: https://app.sourcebot.dev
  baseurl_source: declared
  description: Git history, diff, and file content endpoints.
  name: Sourcebot Git API
  slug: sourcebot-git-api
- baseURL: https://app.sourcebot.dev
  baseurl_source: declared
  description: Repository listing and metadata endpoints.
  name: Sourcebot Repositories API
  slug: sourcebot-repositories-api
- baseURL: https://app.sourcebot.dev
  baseurl_source: declared
  description: Code search and symbol navigation endpoints.
  name: Sourcebot Search & Navigation API
  slug: sourcebot-search-navigation-api
- baseURL: https://app.sourcebot.dev
  baseurl_source: declared
  description: System health and version endpoints.
  name: Sourcebot System API
  slug: sourcebot-system-api
artifact_total: 20
collections:
- collection_type: open
  name: Sourcebot Public Enterprise (EE) Enterprise (EE) Enterprise (EE) API
  slug: open-sourcebot-enterprise-ee-api
- collection_type: open
  name: Sourcebot Public Enterprise (EE) Enterprise (EE) Git API
  slug: open-sourcebot-git-api
- collection_type: open
  name: Sourcebot Public Enterprise (EE) Enterprise (EE) Repositories API
  slug: open-sourcebot-repositories-api
- collection_type: open
  name: Sourcebot Public Enterprise (EE) Enterprise (EE) Search & Navigation API
  slug: open-sourcebot-search-navigation-api
- collection_type: open
  name: Sourcebot Public Enterprise (EE) Enterprise (EE) System API
  slug: open-sourcebot-system-api
common:
- group: commercial
  href: https://artifacts.apis.io/sourcebot/plans/sourcebot-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/sourcebot-plans-pricing.yml
- group: other
  href: https://artifacts.apis.io/sourcebot/capabilities/sourcebot-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/sourcebot-capability-edges.yml
- group: other
  href: https://artifacts.apis.io/sourcebot/overlays/sourcebot-public-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/sourcebot-public-overlay.yaml
- group: agent
  href: https://artifacts.apis.io/sourcebot/agentic-access/sourcebot-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/sourcebot-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/sourcebot/security/sourcebot-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/sourcebot-domain-security.yml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.sourcebot.dev/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.sourcebot.dev/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.sourcebot.dev/api-reference/search-&-navigation/search-code
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.sourcebot.dev/docs/deployment/deploy-sourcebot
- group: start
  title: ''
  type: Quickstart
  url: https://docs.sourcebot.dev/docs/deployment/deploy-sourcebot
- group: company
  title: ''
  type: Website
  url: https://www.sourcebot.dev
- group: company
  title: ''
  type: Blog
  url: https://www.sourcebot.dev/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://www.sourcebot.dev/pricing
- group: start
  title: ''
  type: SignUp
  url: https://app.sourcebot.dev
- group: operate
  title: ''
  type: Support
  url: https://github.com/sourcebot-dev/sourcebot/issues
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/sourcebot-dev
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.sourcebot.dev/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.sourcebot.dev/privacy
- group: operate
  title: ''
  type: StatusPage
  url: https://status.sourcebot.dev
- group: operate
  title: ''
  type: Deprecation
  url: https://docs.sourcebot.dev/docs/upgrade/v4-to-v5-guide
- group: operate
  title: ''
  type: ChangeLog
  url: https://www.sourcebot.dev/changelog
- group: operate
  href: https://artifacts.apis.io/sourcebot/changelog/sourcebot-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/sourcebot-changelog.yml
- group: design
  href: https://artifacts.apis.io/sourcebot/lifecycle/sourcebot-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/sourcebot-lifecycle.yml
- group: agent
  href: https://artifacts.apis.io/sourcebot/mcp/sourcebot-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/sourcebot-mcp.yml
- group: agent
  href: https://artifacts.apis.io/sourcebot/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: build
  href: https://artifacts.apis.io/sourcebot/packages/sourcebot-packages.yml
  title: ''
  type: Packages
  url: packages/sourcebot-packages.yml
- group: build
  href: https://artifacts.apis.io/sourcebot/cli/sourcebot-cli.yml
  title: ''
  type: CLI
  url: cli/sourcebot-cli.yml
- group: start
  href: https://artifacts.apis.io/sourcebot/sandbox/sourcebot-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/sourcebot-sandbox.yml
- group: agent
  href: https://artifacts.apis.io/sourcebot/well-known/sourcebot-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/sourcebot-well-known.yml
- group: design
  href: https://artifacts.apis.io/sourcebot/conformance/sourcebot-conformance.yml
  title: ''
  type: Conformance
  url: conformance/sourcebot-conformance.yml
- group: agent
  href: https://artifacts.apis.io/sourcebot/llms/sourcebot-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/sourcebot-llms.txt
created: '2026-07-17'
description: Sourcebot is a self-hosted code understanding platform built by Taqla Inc. that helps developers and AI agents search, navigate, and understand large enterprise codebases. It indexes every repository across GitHub, GitLab, Bitbucket, Azure DevOps, Gerrit, and Gitea and runs entirely inside your own infrastructure, so source code never leaves your deployment. Alongside a fast regex- and symbol-aware code search UI with file explorer and git history/blame, Sourcebot ships "Ask Sourcebot" natural-language codebase Q&A and an agent code context layer (an MCP server) that gives coding agents like Cursor and Claude Code grounded context across every repo. Its public REST API exposes search, symbol navigation, repository listing, git history/blame/diff, and enterprise user/audit endpoints, secured with API keys (and EE OAuth for agent clients). Free self-hosted Basic tier, paid Pro tier for AI and enterprise security.
finops:
- has_sources: true
  method: derived
  name: Sourcebot Finops
  primary_unit: user / month
  service_category: ''
  slug: sourcebot-finops
  template: false
image: https://github.com/sourcebot-dev.png
layout: provider
mcp_servers:
- description: Sourcebot's "agent code context layer" — an MCP server that gives coding agents (Cursor, Claude Code, VS Code, and any MCP-compatible client) grounded search and navigation context across every repo i
  name: Sourcebot MCP Server
  slug: sourcebot
modified: '2026-07-21'
name: Sourcebot
nav: Providers
network: true
overview: 'Sourcebot publishes 5 API contracts indexed on the [APIs.io](https://apis.io/) network, including Enterprise (EE) API, Git API, Repositories API, and 2 more. Tagged areas include Company, Code Search, Code Intelligence, Developer Tools, and Source Code.


  Sourcebot''s developer surface includes documentation, API reference, getting-started guide, quickstart, engineering blog, pricing, signup flow, and 24 more developer resources.'
plans:
- name: Sourcebot Plans Pricing
  plan_count: 3
  slug: sourcebot-plans-pricing
- name: Sourcebot Price Estimates
  plan_count: 0
  slug: sourcebot-price-estimates
random_paper: 22
score:
  band: strong
  composite: 56.5
  coverage:
    artifact_dirs: 26
    catalog_earned: 52.0
    catalog_earned_first_party: 12.0
    catalog_gap: 63.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 7.9
  facets:
    access_clarity: 84.2
    contract_governance: 4.5
    contract_quality: 43.2
    developer_ergonomics: 73.2
    discoverability: 65.0
    operational_transparency: 44.7
  previous_composite: 48.6
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 5
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 24.5
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  trend: rising
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/sourcebot/sourcebot-2026-08-17T082010.png
security:
- kind: authentication
  name: Sourcebot Authentication
  slug: sourcebot-authentication
  summary_line: http/apiKey/oauth2 · 3 schemes
- kind: domain-security
  name: Sourcebot Domain Security
  slug: sourcebot-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
skill_count: 3
skills:
- name: Inspect git history, blame, and diffs
  slug: sourcebot-inspect-git-history
- name: Navigate symbol definitions and references
  slug: sourcebot-navigate-symbols
- name: Search code and read a matching file
  slug: sourcebot-search-and-read
slug: sourcebot
tags:
- Company
- Code Search
- Code Intelligence
- Developer Tools
- Source Code
- Version Control
- MCP
- AI Coding Agents
- Enterprise Search
- Self-Hosted
website: https://www.sourcebot.dev
---
