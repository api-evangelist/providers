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
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: true
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: documented
    mcp_server: documented
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 15.3
  scored_at: '2026-10-31'
api_count: 1
apis:
- description: 'The v1 REST API behind Cloutdesk''s Agent Platform — the programmatic surface agencies, brands, and talent representatives use to run influencer marketing through AI agents. Cursor-paginated, URI-path '
  name: Cloutdesk Agent Platform API
  slug: agent-platform
artifact_total: 23
common:
- group: commercial
  title: ''
  type: License
  url: https://github.com/cloutdesk/agents/blob/main/LICENSE
- group: agent
  href: https://artifacts.apis.io/cloutjam/mcp/cloutjam-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/cloutjam-mcp.yml
- group: company
  title: ''
  type: Website
  url: https://cloutdesk.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://www.cloutdesk.com/agent-platform
- group: docs
  title: ''
  type: Documentation
  url: https://www.cloutdesk.com/agent-platform
- group: start
  title: ''
  type: Login
  url: https://dashboard.cloutdesk.com
- group: operate
  title: ''
  type: Support
  url: mailto:hello@cloutdesk.com
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.cloutdesk.com/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.iubenda.com/privacy-policy/65621163/cookie-policy
- group: auth
  href: https://artifacts.apis.io/cloutjam/authentication/cloutjam-authentication.yml
  title: ''
  type: Authentication
  url: authentication/cloutjam-authentication.yml
- group: auth
  href: https://artifacts.apis.io/cloutjam/scopes/cloutjam-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/cloutjam-scopes.yml
- group: design
  href: https://artifacts.apis.io/cloutjam/conventions/cloutjam-conventions.yml
  title: ''
  type: Conventions
  url: conventions/cloutjam-conventions.yml
- group: design
  href: https://artifacts.apis.io/cloutjam/conventions/cloutjam-conventions.yml
  title: ''
  type: Idempotency
  url: conventions/cloutjam-conventions.yml
- group: design
  href: https://artifacts.apis.io/cloutjam/conformance/cloutjam-conformance.yml
  title: ''
  type: Conformance
  url: conformance/cloutjam-conformance.yml
- group: agent
  href: https://artifacts.apis.io/cloutjam/llms/cloutjam-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/cloutjam-llms.txt
- group: auth
  href: https://artifacts.apis.io/cloutjam/security/cloutjam-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/cloutjam-domain-security.yml
- group: agent
  href: https://artifacts.apis.io/cloutjam/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: build
  href: https://artifacts.apis.io/cloutjam/packages/cloutjam-packages.yml
  title: ''
  type: Packages
  url: packages/cloutjam-packages.yml
- group: design
  href: https://artifacts.apis.io/cloutjam/data-model/cloutjam-data-model.yml
  title: ''
  type: DataModel
  url: data-model/cloutjam-data-model.yml
- group: design
  href: https://artifacts.apis.io/cloutjam/lifecycle/cloutjam-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/cloutjam-lifecycle.yml
- group: commercial
  href: https://artifacts.apis.io/cloutjam/plans/cloutjam-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/cloutjam-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/cloutjam/rate-limits/cloutjam-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/cloutjam-rate-limits.yml
- group: build
  href: https://artifacts.apis.io/cloutjam/cli/cloutjam-cli.yml
  title: ''
  type: CLI
  url: cli/cloutjam-cli.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/cloutdesk
- group: build
  title: ''
  type: SourceCode
  url: https://github.com/cloutdesk/agents
- group: start
  title: ''
  type: GettingStarted
  url: https://github.com/cloutdesk/agents#quick-start
created: '2026-07-17'
description: CloutDesk (formerly CloutJam) is a 500 Global-backed, New York-based platform for modern influencer marketing and creator management, building open infrastructure that lets agencies, brands, and talent representatives run creator partnerships end-to-end - outreach, relationship management, content approval, contract negotiation, invoicing, reporting, and payments. Its agent-first Agent Platform (closed beta) exposes every workflow to AI agents through an MCP server with six published tools, a cursor-paginated v1 REST API with RFC 7807 errors and idempotent writes, and a CLI. CloutDesk also publishes 16 MIT-licensed Agent Skills and four agent templates for Claude Code, OpenAI Codex, and Microsoft Agent Framework in its own public GitHub org.
image: https://cdn.prod.website-files.com/684989b6fb9b11bb4d485104/68cd29a469d19b89648e1d17_open-graph.avif
layout: provider
mcp_servers:
- description: MCP server requiring OAuth; 6 tools listed.
  name: CloutJam MCP Server
  slug: cloutdesk
modified: '2026-08-13'
name: CloutJam
nav: Providers
network: true
overview: 'CloutJam is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Influencer Marketing, Creator Management, Creator Economy, and Marketing.


  CloutJam''s developer surface includes documentation, support, authentication, CLI, getting-started guide, and 21 more developer resources.'
plans:
- name: Cloutjam Plans Pricing
  plan_count: 0
  slug: cloutjam-plans-pricing
random_paper: 23
rate_limits:
- limit_count: 0
  name: Cloutjam Rate Limits
  slug: cloutjam-rate-limits
scopes:
- name: Cloutjam Scopes
  scope_count: 4
  slug: cloutjam-scopes
  summary_line: 4 scopes · authorizationCode
score:
  band: thin
  composite: 31.5
  coverage:
    artifact_dirs: 18
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 34.2
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 61.9
    discoverability: 65.0
    operational_transparency: 5.3
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - united-states
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - north-america
  previous_composite: 31.5
  provenance:
    conformance: first-party
    mcp: first-party
    skills: first-party
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 34.3
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/cloutjam/cloutjam-2026-07-25T205717.png
security:
- kind: authentication
  name: Cloutjam Authentication
  slug: cloutjam-authentication
  summary_line: http/oauth2 · 2 schemes
- kind: domain-security
  name: Cloutjam Domain Security
  slug: cloutjam-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
skill_count: 16
skills:
- name: campaign-brief-drafting
  slug: cloutjam-campaign-brief-drafting
- name: campaign-recap-reporting
  slug: cloutjam-campaign-recap-reporting
- name: client-reporting
  slug: cloutjam-client-reporting
- name: compliance-check
  slug: cloutjam-compliance-check
- name: content-performance-analysis
  slug: cloutjam-content-performance-analysis
- name: content-strategy
  slug: cloutjam-content-strategy
- name: deliverable-tracking
  slug: cloutjam-deliverable-tracking
- name: influencer-contract-drafting
  slug: cloutjam-influencer-contract-drafting
- name: influencer-contract-negotiation
  slug: cloutjam-influencer-contract-negotiation
- name: influencer-contract-review
  slug: cloutjam-influencer-contract-review
- name: invoice-management
  slug: cloutjam-invoice-management
- name: media-kit-creation
  slug: cloutjam-media-kit-creation
- name: payout-orchestration
  slug: cloutjam-payout-orchestration
- name: proposal-drafting
  slug: cloutjam-proposal-drafting
- name: talent-communications
  slug: cloutjam-talent-communications
- name: talent-discovery
  slug: cloutjam-talent-discovery
slug: cloutjam
tags:
- Company
- Influencer Marketing
- Creator Management
- Creator Economy
- Marketing
- AI Agents
- Agents
- MCP
- Agent Skills
- Talent Management
- Influencer Marketing Platform
website: https://cloutdesk.com
---
