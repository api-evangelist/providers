---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - authentication
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
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
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 26.8
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 6
  human_in_the_loop: 0
  name: Lawdiver Com Agentic Access
  operation_count: 12
  slug: lawdiver-com-agentic-access
  summary_line: 12 operations · 6 acting
api_count: 1
apis:
- description: LawDiver API v1 provides case search, citation resolution, and other legal research endpoints.
  name: LawDiver API
  slug: lawdiver-api
artifact_total: 7
common:
- group: agent
  href: https://artifacts.apis.io/lawdiver-com/agentic-access/lawdiver-com-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/lawdiver-com-agentic-access.yml
- group: design
  href: https://artifacts.apis.io/lawdiver-com/rules/lawdiver-com-rules.yml
  title: ''
  type: Spectral
  url: rules/lawdiver-com-rules.yml
- group: auth
  href: https://artifacts.apis.io/lawdiver-com/authentication/lawdiver-com-authentication.yml
  title: ''
  type: Authentication
  url: authentication/lawdiver-com-authentication.yml
- group: design
  href: https://artifacts.apis.io/lawdiver-com/errors/lawdiver-com-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/lawdiver-com-problem-types.yml
- group: design
  href: https://artifacts.apis.io/lawdiver-com/conformance/lawdiver-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/lawdiver-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/lawdiver-com/llms/lawdiver-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/lawdiver-com-llms.txt
- group: agent
  href: https://artifacts.apis.io/lawdiver-com/mcp/lawdiver-com-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/lawdiver-com-mcp.yml
- group: agent
  href: https://artifacts.apis.io/lawdiver-com/well-known/lawdiver-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/lawdiver-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/lawdiver-com/hosts/lawdiver-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/lawdiver-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/lawdiver-com/vendors/lawdiver-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/lawdiver-com-vendors.yml
- group: auth
  title: ''
  type: Security
  url: https://lawdiver.com/security
- group: start
  title: ''
  type: Login
  url: https://lawdiver.com/login
- group: auth
  href: https://artifacts.apis.io/lawdiver-com/security/lawdiver-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/lawdiver-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://lawdiver.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://lawdiver.com/docs/api
- group: docs
  title: ''
  type: Documentation
  url: https://lawdiver.com/docs/api
- group: docs
  title: ''
  type: APIReference
  url: https://lawdiver.com/docs/api
- group: start
  title: ''
  type: GettingStarted
  url: https://lawdiver.com/docs/api#getting-started
- group: operate
  title: ''
  type: Support
  url: https://lawdiver.com/support
- group: company
  title: ''
  type: Blog
  url: https://lawdiver.com/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://lawdiver.com/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://lawdiver.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://lawdiver.com/privacy
coverage:
  detail: the company serves an API surface but requires credentials before any description of it can be read
  evidence:
  - status: null
    url: https://lawdiver.com/v1/openapi.json
  - status: null
    url: https://bazaar.lawdiver.com/v1/openapi.json
  - status: null
    url: https://enterprise.lawdiver.com/v1/openapi.json
  - status: 401
    url: https://lawdiver.com/mcp
  - status: 401
    url: https://bazaar.lawdiver.com/mcp
  - status: 401
    url: https://enterprise.lawdiver.com/mcp
  reason: partner-login
  state: gated
created: '2026-10-29'
description: LawDiver is a free legal research platform offering a Westlaw and Lexis alternative. It provides access to over 10 million U.S. court opinions, more than 1,300 United States treaties, and over 8,000 pattern jury instructions. Users can search cases, check citations, and retrieve full-text PDFs without login. The service includes a public API (v1) for programmatic access to case search and citation resolution, licensed for any commercial purpose.
image: https://lawdiver.com/logo.png
layout: provider
mcp_servers:
- description: Remote MCP server at lawdiver.com requiring an API key.
  name: LawDiver MCP Server
  slug: lawdiver-com-mcp-yml
modified: '2026-10-29'
name: LawDiver
nav: Providers
network: true
overview: 'LawDiver is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Legal Tech, Legal Research, and Free.


  The LawDiver catalog on APIs.io includes 1 Spectral governance ruleset.


  LawDiver''s developer surface includes authentication, documentation, API reference, getting-started guide, support, engineering blog, pricing, and 16 more developer resources.'
random_paper: 2
rules:
- authorship: generated
  effective_rule_count: 49
  extends:
  - spectral:oas
  name: LawDiver API Rules
  rule_count: 8
  severity_counts:
    error: 7
    hint: 0
    info: 1
    warn: 0
  slug: lawdiver-com-rules
scopes:
- name: Lawdiver Com Scopes
  scope_count: 0
  slug: lawdiver-com-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: emerging
  composite: 22.9
  coverage:
    artifact_dirs: 23
    catalog_earned: 35.8
    catalog_earned_first_party: 0.0
    catalog_gap: 79.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -11.1
  facets:
    access_clarity: 22.4
    contract_governance: 15.9
    contract_quality: 0.0
    developer_ergonomics: 34.5
    discoverability: 66.7
    operational_transparency: 5.3
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 34.0
  provenance:
    agentic_access: derived
    conformance: derived
    mcp: first-party
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 30.4
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/lawdiver-com/lawdiver-com-2026-11-03T134717.png
security:
- kind: authentication
  name: Lawdiver Com Authentication
  slug: lawdiver-com-authentication
  summary_line: 4 schemes
- kind: domain-security
  name: Lawdiver Com Domain Security
  slug: lawdiver-com-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: lawdiver-com
tags:
- Company
- Legal Tech
- Legal Research
- Free
website: https://lawdiver.com
---
