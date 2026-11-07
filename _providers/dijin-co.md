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
  - scopes
  - rate-limits
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
    error_semantics: documented
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
  score: 27.6
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: 'Remote Model Context Protocol endpoint for Dijin''s permissioned memory layer. Agents recall approved summaries, entities, decisions, conflicts and evidence, and can propose memory through gated write '
  name: Dijin Memory MCP
  slug: dijin-memory-mcp
artifact_total: 9
common:
- group: build
  href: https://artifacts.apis.io/dijin-co/integrations/dijin-co-integration-edges.yml
  title: ''
  type: IntegrationEdges
  url: integrations/dijin-co-integration-edges.yml
- group: operate
  href: https://artifacts.apis.io/dijin-co/rate-limits/dijin-co-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/dijin-co-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/dijin-co/plans/dijin-co-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/dijin-co-plans-pricing.yml
- group: build
  href: https://artifacts.apis.io/dijin-co/cli/dijin-co-cli.yml
  title: ''
  type: CLI
  url: cli/dijin-co-cli.yml
- group: operate
  href: https://artifacts.apis.io/dijin-co/changelog/dijin-co-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/dijin-co-changelog.yml
- group: design
  href: https://artifacts.apis.io/dijin-co/conventions/dijin-co-conventions.yml
  title: ''
  type: Conventions
  url: conventions/dijin-co-conventions.yml
- group: auth
  title: ''
  type: Compliance
  url: https://dijin.co/en/security
- group: auth
  href: https://artifacts.apis.io/dijin-co/authentication/dijin-co-authentication.yml
  title: ''
  type: Authentication
  url: authentication/dijin-co-authentication.yml
- group: auth
  href: https://artifacts.apis.io/dijin-co/scopes/dijin-co-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/dijin-co-scopes.yml
- group: design
  href: https://artifacts.apis.io/dijin-co/lifecycle/dijin-co-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/dijin-co-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/dijin-co/errors/dijin-co-error-codes.yml
  title: ''
  type: ErrorCatalog
  url: errors/dijin-co-error-codes.yml
- group: design
  href: https://artifacts.apis.io/dijin-co/conformance/dijin-co-conformance.yml
  title: ''
  type: Conformance
  url: conformance/dijin-co-conformance.yml
- group: agent
  href: https://artifacts.apis.io/dijin-co/llms/dijin-co-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/dijin-co-llms.txt
- group: auth
  href: https://artifacts.apis.io/dijin-co/well-known/dijin-co-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/dijin-co-security.txt
- group: auth
  href: https://artifacts.apis.io/dijin-co/well-known/dijin-co-mcp-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/dijin-co-mcp-security.txt
- group: auth
  href: https://artifacts.apis.io/dijin-co/well-known/dijin-co-app-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/dijin-co-app-security.txt
- group: agent
  href: https://artifacts.apis.io/dijin-co/well-known/dijin-co-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/dijin-co-well-known.yml
- group: other
  href: https://artifacts.apis.io/dijin-co/hosts/dijin-co-hosts.yml
  title: ''
  type: Hosts
  url: hosts/dijin-co-hosts.yml
- group: other
  href: https://artifacts.apis.io/dijin-co/vendors/dijin-co-vendors.yml
  title: ''
  type: Vendors
  url: vendors/dijin-co-vendors.yml
- group: auth
  href: https://artifacts.apis.io/dijin-co/security/dijin-co-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/dijin-co-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/dijin-co/security/dijin-co-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/dijin-co-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/dijin-co/security/dijin-co-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/dijin-co-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://dijin.co/
- group: docs
  title: ''
  type: Documentation
  url: https://dijin.co/en/docs
- group: start
  title: ''
  type: DeveloperPortal
  url: https://dijin.co/en/developers
- group: start
  title: ''
  type: GettingStarted
  url: https://dijin.co/en/quickstart
- group: agent
  title: ''
  type: MCPServer
  url: https://dijin.co/en/mcp
- group: company
  title: ''
  type: Blog
  url: https://dijin.co/en/blog
- group: other
  title: ''
  type: RSSFeed
  url: https://dijin.co/feed.xml
- group: operate
  title: ''
  type: ChangeLog
  url: https://dijin.co/en/changelog
- group: operate
  title: ''
  type: StatusPage
  url: https://dijin.co/en/status
- group: commercial
  title: ''
  type: Pricing
  url: https://dijin.co/en/pricing
- group: operate
  title: ''
  type: Support
  url: https://dijin.co/en/support
- group: operate
  title: ''
  type: Contact
  url: https://dijin.co/en/contact
- group: auth
  title: ''
  type: Security
  url: https://dijin.co/en/security
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/dijin-company
- group: start
  title: ''
  type: SignUp
  url: https://dijin.co/en/download
- group: start
  title: ''
  type: Login
  url: https://dijin.co/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://dijin.co/en/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://dijin.co/en/privacy
created: '2026-11-05'
description: Dijin is a permissioned Memory Layer between AI agents, apps, and humans. Users save what matters and recall it across Claude, ChatGPT, Cursor, and future agents, with evidence on every answer, gated scopes for agent writes, audit logs, and portable export through the open DMF (Dijin Memory Format). Developers connect agents over a single MCP endpoint secured with OAuth 2.1. Dijin is operated by DİJİN TEKNOLOJİ LİMİTED ŞİRKETİ, registered in Ankara, Türkiye.
image: https://dijin.co/icon-512x512.png
layout: provider
mcp_servers:
- description: ''
  name: Dijin MCP Server
  slug: mcp
modified: '2026-11-05'
name: Dijin
nav: Providers
network: true
overview: 'Dijin is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, AI Agents, Memory, MCP, and Personal Data.


  Dijin''s developer surface includes CLI, changelog, authentication, documentation, getting-started guide, engineering blog, pricing, and 33 more developer resources.'
plans:
- name: Dijin Co Plans Pricing
  plan_count: 4
  slug: dijin-co-plans-pricing
random_paper: 13
rate_limits:
- limit_count: 1
  name: Dijin Co Rate Limits
  slug: dijin-co-rate-limits
scopes:
- name: Dijin Co Scopes
  scope_count: 13
  slug: dijin-co-scopes
  summary_line: 13 scopes
score:
  band: developing
  composite: 51.9
  coverage:
    artifact_dirs: 20
    catalog_earned: 57.0
    catalog_earned_first_party: 20.0
    catalog_gap: 58.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 92.1
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 57.1
    discoverability: 65.0
    operational_transparency: 68.4
  provenance:
    conformance: first-party
    mcp: first-party
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 45.1
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Dijin Co Authentication
  slug: dijin-co-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Dijin Co Domain Security
  slug: dijin-co-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Dijin Co Vulnerability Disclosure
  slug: dijin-co-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Dijin Co Trust Center
  slug: dijin-co-trust-center
  summary_line: GDPR
slug: dijin-co
tags:
- Company
- AI Agents
- Memory
- MCP
- Personal Data
- Privacy
- OAuth
website: https://dijin.co/
---
