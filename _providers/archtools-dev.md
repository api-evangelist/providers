---
access_model:
  confidence: high
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
  - rate-limits
  - security
  trial: false
  try_now: true
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: flavored
    agent_skills: unknown
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: documented
    event_surface_described: unknown
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
  score: 36.1
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: Production-ready API tools for developers and AI agents. Use one API key across the platform or pay with x402 USDC micropayments.
  name: Arch Tools API
  slug: arch-tools-api
artifact_total: 9
common:
- group: operate
  href: https://artifacts.apis.io/archtools-dev/rate-limits/archtools-dev-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/archtools-dev-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/archtools-dev/plans/archtools-dev-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/archtools-dev-plans-pricing.yml
- group: agent
  href: https://artifacts.apis.io/archtools-dev/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: operate
  href: https://artifacts.apis.io/archtools-dev/changelog/archtools-dev-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/archtools-dev-changelog.yml
- group: auth
  href: https://artifacts.apis.io/archtools-dev/authentication/archtools-dev-authentication.yml
  title: ''
  type: Authentication
  url: authentication/archtools-dev-authentication.yml
- group: design
  href: https://artifacts.apis.io/archtools-dev/errors/archtools-dev-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/archtools-dev-problem-types.yml
- group: design
  href: https://artifacts.apis.io/archtools-dev/conformance/archtools-dev-conformance.yml
  title: ''
  type: Conformance
  url: conformance/archtools-dev-conformance.yml
- group: agent
  href: https://artifacts.apis.io/archtools-dev/llms/archtools-dev-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/archtools-dev-llms.txt
- group: other
  href: https://artifacts.apis.io/archtools-dev/a2a/archtools-dev-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/archtools-dev-a2a.yml
- group: build
  href: https://artifacts.apis.io/archtools-dev/mcp/archtools-dev-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/archtools-dev-tool-crosswalk.yml
- group: agent
  href: https://artifacts.apis.io/archtools-dev/mcp/archtools-dev-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/archtools-dev-mcp.yml
- group: agent
  href: https://artifacts.apis.io/archtools-dev/well-known/archtools-dev-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/archtools-dev-well-known.yml
- group: other
  href: https://artifacts.apis.io/archtools-dev/hosts/archtools-dev-hosts.yml
  title: ''
  type: Hosts
  url: hosts/archtools-dev-hosts.yml
- group: other
  href: https://artifacts.apis.io/archtools-dev/vendors/archtools-dev-vendors.yml
  title: ''
  type: Vendors
  url: vendors/archtools-dev-vendors.yml
- group: build
  href: https://artifacts.apis.io/archtools-dev/packages/archtools-dev-packages.yml
  title: ''
  type: Packages
  url: packages/archtools-dev-packages.yml
- group: design
  title: ''
  type: Webhooks
  url: https://archtools.dev/webhooks
- group: operate
  title: ''
  type: StatusPage
  url: https://archtools.dev/status
- group: auth
  title: ''
  type: Security
  url: https://archtools.dev/security
- group: start
  title: ''
  type: Sandbox
  url: https://archtools.dev/playground
- group: build
  title: ''
  type: SDKs
  url: https://archtools.dev/sdk
- group: start
  title: ''
  type: Login
  url: https://archtools.dev/login
- group: start
  title: ''
  type: DeveloperPortal
  url: https://archtools.dev/developers
- group: operate
  title: ''
  type: ChangeLog
  url: https://archtools.dev/changelog
- group: auth
  href: https://artifacts.apis.io/archtools-dev/security/archtools-dev-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/archtools-dev-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/archtools-dev/security/archtools-dev-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/archtools-dev-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://archtools.dev/
- group: docs
  title: ''
  type: Documentation
  url: https://archtools.dev/docs
- group: docs
  title: ''
  type: APIReference
  url: https://archtools.dev/docs
- group: start
  title: ''
  type: GettingStarted
  url: https://archtools.dev/getting-started
- group: commercial
  title: ''
  type: Pricing
  url: https://archtools.dev/pricing
- group: company
  title: ''
  type: Blog
  url: https://archtools.dev/blog
- group: commercial
  title: ''
  type: TermsOfService
  url: https://archtools.dev/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://archtools.dev/privacy
- group: operate
  title: ''
  type: Support
  url: https://archtools.dev/docs/support
created: '2026-10-30'
description: Arch Tools provides a unified API platform offering 63 AI-powered tools for developers and autonomous agents. The service includes web search, web scraping, image generation, OCR, crypto price data, fact-checking, research reports, domain analysis, and more, all accessible via a single API key. It supports the x402 payment protocol with USDC and offers pay-per-call pricing, enabling flexible integration into applications. The platform is built for MCP compatibility and integrates with LangChain, making it suitable for a wide range of AI and automation use cases.
image: https://archtools.dev/og-image.png
layout: provider
mcp_servers:
- description: Remote MCP server at archtools.dev.
  name: archtools-dev MCP Server
  slug: archtools-dev-mcp-yml
modified: '2026-10-30'
name: archtools-dev
nav: Providers
network: true
overview: 'archtools-dev is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Artificial Intelligence, Tools, Automation, and MCP.


  archtools-dev''s developer surface includes changelog, authentication, sandbox, documentation, API reference, getting-started guide, pricing, and 27 more developer resources.'
plans:
- name: Archtools Dev Plans Pricing
  plan_count: 5
  slug: archtools-dev-plans-pricing
random_paper: 19
rate_limits:
- limit_count: 5
  name: Archtools Dev Rate Limits
  slug: archtools-dev-rate-limits
scopes:
- name: Archtools Dev Scopes
  scope_count: 0
  slug: archtools-dev-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: thin
  composite: 38.3
  coverage:
    artifact_dirs: 25
    catalog_earned: 61.0
    catalog_earned_first_party: 24.0
    catalog_gap: 54.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -13.5
  facets:
    access_clarity: 53.9
    contract_governance: 4.5
    contract_quality: 0.0
    developer_ergonomics: 51.7
    discoverability: 65.0
    operational_transparency: 56.6
  previous_composite: 51.8
  provenance:
    conformance: derived
    mcp: first-party
    skills: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 33.6
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/archtools-dev/archtools-dev-2026-11-03T121104.png
security:
- kind: authentication
  name: Archtools Dev Authentication
  slug: archtools-dev-authentication
  summary_line: 2 schemes
- kind: domain-security
  name: Archtools Dev Domain Security
  slug: archtools-dev-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Archtools Dev Vulnerability Disclosure
  slug: archtools-dev-vulnerability-disclosure
  summary_line: no policy recorded
skill_count: 1
skills:
- name: ai-generate
  slug: archtools-dev-ai-generate
slug: archtools-dev
tags:
- Company
- Artificial Intelligence
- Tools
- Automation
- MCP
website: https://archtools.dev/
---
