---
access_model:
  confidence: high
  gated: none
  gated_source:
  - onboarding
  label: Freemium · Open access
  onboarding: open
  pricing: freemium
  public: true
  source:
  - plans
  - authentication
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
  score: 24.3
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: API for Better Design UI component service
  name: Better Design API
  slug: better-design-api
artifact_total: 8
common:
- group: commercial
  href: https://artifacts.apis.io/better-design-com/plans/better-design-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/better-design-com-plans-pricing.yml
- group: build
  href: https://artifacts.apis.io/better-design-com/cli/better-design-com-cli.yml
  title: ''
  type: CLI
  url: cli/better-design-com-cli.yml
- group: auth
  title: ''
  type: Compliance
  url: https://better-design.com/security
- group: agent
  href: https://artifacts.apis.io/better-design-com/llms/better-design-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/better-design-com-llms.txt
- group: auth
  href: https://artifacts.apis.io/better-design-com/well-known/better-design-com-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/better-design-com-security.txt
- group: agent
  href: https://artifacts.apis.io/better-design-com/well-known/better-design-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/better-design-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/better-design-com/hosts/better-design-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/better-design-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/better-design-com/vendors/better-design-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/better-design-com-vendors.yml
- group: auth
  title: ''
  type: Security
  url: https://better-design.com/security
- group: start
  title: ''
  type: Login
  url: https://better-design.com/sign-in
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/marvkr
- group: operate
  title: ''
  type: ChangeLog
  url: https://better-design.com/changelog
- group: start
  title: ''
  type: GettingStarted
  url: https://better-design.com/blog/connect-linear-mcp-to-codex
- group: auth
  href: https://artifacts.apis.io/better-design-com/security/better-design-com-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/better-design-com-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/better-design-com/security/better-design-com-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/better-design-com-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/better-design-com/security/better-design-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/better-design-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://better-design.com/
- group: docs
  title: ''
  type: Documentation
  url: https://better-design.com/llms.txt
- group: commercial
  title: ''
  type: Pricing
  url: https://better-design.com/pricing
- group: company
  title: ''
  type: Blog
  url: https://better-design.com/blog
- group: commercial
  title: ''
  type: TermsOfService
  url: https://better-design.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://better-design.com/privacy
- group: operate
  title: ''
  type: Support
  url: https://better-design.com/support
- group: operate
  title: ''
  type: Contact
  url: https://better-design.com/contact
coverage:
  checked: '2026-11-02'
  detail: Documentation is available but no machine‑readable OpenAPI/GraphQL/AsyncAPI spec is published.
  evidence:
  - status: 200
    url: https://better-design.com/docs/icons.md
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-11-02'
description: Better Design provides AI coding agents with real design systems, offering 87 components each through a single MCP server. It aims to replace generic-looking apps with brand‑consistent UI, enabling faster, higher‑quality development.
image: https://better-design.com/api/og/page?path=%2F&v=51c840621038
layout: provider
modified: '2026-11-02'
name: Better Design
nav: Providers
network: true
overview: 'Better Design is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Design, Artificial Intelligence, Components, MCP, and UI.


  Better Design''s developer surface includes CLI, changelog, getting-started guide, documentation, pricing, engineering blog, support, and 17 more developer resources.'
plans:
- name: Better Design Com Plans Pricing
  plan_count: 3
  slug: better-design-com-plans-pricing
random_paper: 9
rate_limits:
- limit_count: 2
  name: Better Design Com Rate Limits
  slug: better-design-com-rate-limits
scopes:
- name: Better Design Com Scopes
  scope_count: 0
  slug: better-design-com-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: thin
  composite: 30.4
  coverage:
    artifact_dirs: 20
    catalog_earned: 52.0
    catalog_earned_first_party: 20.0
    catalog_gap: 63.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 65.8
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 21.4
    discoverability: 57.1
    operational_transparency: 36.8
  provenance:
    conformance: unknown
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 31.4
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Better Design Com Authentication
  slug: better-design-com-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Better Design Com Domain Security
  slug: better-design-com-domain-security
  summary_line: TLSv1.3 · HSTS
- kind: vulnerability-disclosure
  name: Better Design Com Vulnerability Disclosure
  slug: better-design-com-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Better Design Com Trust Center
  slug: better-design-com-trust-center
  summary_line: SOC 2, ISO 27001
slug: better-design-com
tags:
- Design
- Artificial Intelligence
- Components
- MCP
- UI
website: https://better-design.com/
---
