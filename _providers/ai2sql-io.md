---
access_model:
  confidence: high
  gated: none
  gated_source:
  - onboarding
  label: Freemium (free trial) · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  - rate-limits
  - security
  trial: true
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
    mcp_server: false
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
  score: 24.1
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: AI2SQL provides an API for generating SQL queries from natural language prompts.
  name: AI2SQL API
  slug: ai2sql-api
artifact_total: 6
common:
- group: operate
  href: https://artifacts.apis.io/ai2sql-io/rate-limits/ai2sql-io-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/ai2sql-io-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/ai2sql-io/plans/ai2sql-io-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/ai2sql-io-plans-pricing.yml
- group: auth
  href: https://artifacts.apis.io/ai2sql-io/authentication/ai2sql-io-authentication.yml
  title: ''
  type: Authentication
  url: authentication/ai2sql-io-authentication.yml
- group: design
  href: https://artifacts.apis.io/ai2sql-io/errors/ai2sql-io-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/ai2sql-io-problem-types.yml
- group: agent
  href: https://artifacts.apis.io/ai2sql-io/llms/ai2sql-io-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/ai2sql-io-llms.txt
- group: agent
  href: https://artifacts.apis.io/ai2sql-io/well-known/ai2sql-io-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/ai2sql-io-well-known.yml
- group: other
  href: https://artifacts.apis.io/ai2sql-io/hosts/ai2sql-io-hosts.yml
  title: ''
  type: Hosts
  url: hosts/ai2sql-io-hosts.yml
- group: other
  href: https://artifacts.apis.io/ai2sql-io/vendors/ai2sql-io-vendors.yml
  title: ''
  type: Vendors
  url: vendors/ai2sql-io-vendors.yml
- group: auth
  href: https://artifacts.apis.io/ai2sql-io/security/ai2sql-io-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/ai2sql-io-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://ai2sql.io/
- group: operate
  title: ''
  type: Support
  url: https://ai2sql.io/
- group: company
  title: ''
  type: Blog
  url: https://ai2sql.io/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://ai2sql.io/pricing
- group: start
  title: ''
  type: SignUp
  url: https://builder.ai2sql.io/login
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://ai2sql.io/privacy-policy
coverage:
  checked: '2026-11-01'
  detail: The provider's documentation pages are HTML with examples but do not publish any machine‑readable OpenAPI, AsyncAPI, GraphQL, or other contract.
  evidence:
  - status: 200
    url: https://builder.ai2sql.io/api-docs.html
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-11-01'
description: AI2SQL is an AI‑powered SQL query builder and generator that connects to your live database schema to generate, explain, fix, and optimize SQL queries from plain‑English prompts. It offers read‑only execution, supports PostgreSQL, MySQL, SQL Server, Oracle, Snowflake, BigQuery, Redshift, MongoDB, SQLite and Firebird, and provides both a web interface and MCP endpoint for AI agents. Free plans include limited queries, with paid tiers offering more usage and a desktop app.
image: https://ai2sql.io/og.jpg
layout: provider
modified: '2026-11-01'
name: AI2SQL
nav: Providers
network: true
overview: 'AI2SQL is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Artificial Intelligence, SQL, Database, Automation, and No-Code.


  AI2SQL''s developer surface includes authentication, support, engineering blog, pricing, signup flow, and 10 more developer resources.'
plans:
- name: Ai2Sql Io Plans Pricing
  plan_count: 5
  slug: ai2sql-io-plans-pricing
random_paper: 9
rate_limits:
- limit_count: 4
  name: Ai2Sql Io Rate Limits
  slug: ai2sql-io-rate-limits
scopes:
- name: Ai2Sql Io Scopes
  scope_count: 0
  slug: ai2sql-io-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: emerging
  composite: 23.7
  coverage:
    artifact_dirs: 20
    catalog_earned: 56.0
    catalog_earned_first_party: 24.0
    catalog_gap: 59.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -4.4
  facets:
    access_clarity: 48.7
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 15.5
    discoverability: 57.1
    operational_transparency: 31.6
  previous_composite: 28.1
  provenance:
    conformance: unknown
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 21.8
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Ai2Sql Io Authentication
  slug: ai2sql-io-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Ai2Sql Io Domain Security
  slug: ai2sql-io-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: ai2sql-io
tags:
- Artificial Intelligence
- SQL
- Database
- Automation
- No-Code
- Developer Tools
website: https://ai2sql.io/
---
