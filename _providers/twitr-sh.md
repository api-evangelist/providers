---
agent_readiness:
  band: agent-native
  dimensions:
    agent_card: false
    agent_skills: unknown
    agentic_access: unknown
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: false
    idempotency: verified
    mcp_server: documented
    openapi_examples: verified
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 52.0
  scored_at: '2026-10-31'
agentic_access:
- acting_count: 23
  human_in_the_loop: 0
  name: Twitr Sh Agentic Access
  operation_count: 32
  slug: twitr-sh-agentic-access
  summary_line: 32 operations · 23 acting
api_count: 1
apis:
- baseURL: https://twitr.sh
  baseurl_source: declared
  description: The Accounts API from twitr-sh — 5 operation(s) for accounts.
  name: twitr-sh Accounts API
  slug: twitr-sh-accounts-api
- baseURL: https://twitr.sh
  baseurl_source: declared
  description: The Creator API from twitr-sh — 1 operation(s) for creator.
  name: twitr-sh Creator API
  slug: twitr-sh-creator-api
- baseURL: https://twitr.sh
  baseurl_source: declared
  description: The Intelligence API from twitr-sh — 3 operation(s) for intelligence.
  name: twitr-sh Intelligence API
  slug: twitr-sh-intelligence-api
- baseURL: https://twitr.sh
  baseurl_source: declared
  description: The Monitors API from twitr-sh — 3 operation(s) for monitors.
  name: twitr-sh Monitors API
  slug: twitr-sh-monitors-api
- baseURL: https://twitr.sh
  baseurl_source: declared
  description: The Search API from twitr-sh — 1 operation(s) for search.
  name: twitr-sh Search API
  slug: twitr-sh-search-api
- baseURL: https://twitr.sh
  baseurl_source: declared
  description: The Snapshots API from twitr-sh — 2 operation(s) for snapshots.
  name: twitr-sh Snapshots API
  slug: twitr-sh-snapshots-api
- baseURL: https://twitr.sh
  baseurl_source: declared
  description: The Social API from twitr-sh — 9 operation(s) for social.
  name: twitr-sh Social API
  slug: twitr-sh-social-api
- baseURL: https://twitr.sh
  baseurl_source: declared
  description: The Webhooks API from twitr-sh — 5 operation(s) for webhooks.
  name: twitr-sh Webhooks API
  slug: twitr-sh-webhooks-api
artifact_total: 19
common:
- group: agent
  href: https://artifacts.apis.io/twitr-sh/agentic-access/twitr-sh-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/twitr-sh-agentic-access.yml
- group: operate
  href: https://artifacts.apis.io/twitr-sh/rate-limits/twitr-sh-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/twitr-sh-rate-limits.yml
- group: design
  href: https://artifacts.apis.io/twitr-sh/rules/twitr-sh-rules.yml
  title: ''
  type: Spectral
  url: rules/twitr-sh-rules.yml
- group: design
  href: https://artifacts.apis.io/twitr-sh/json-ld/twitr-sh-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/twitr-sh-context.jsonld
- group: design
  href: https://artifacts.apis.io/twitr-sh/vocabulary/twitr-sh-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/twitr-sh-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/twitr-sh/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/twitr-sh/data-model/twitr-sh-data-model.yml
  title: ''
  type: DataModel
  url: data-model/twitr-sh-data-model.yml
- group: design
  href: https://artifacts.apis.io/twitr-sh/conventions/twitr-sh-conventions.yml
  title: ''
  type: Idempotency
  url: conventions/twitr-sh-conventions.yml
- group: design
  href: https://artifacts.apis.io/twitr-sh/conventions/twitr-sh-conventions.yml
  title: ''
  type: Conventions
  url: conventions/twitr-sh-conventions.yml
- group: auth
  href: https://artifacts.apis.io/twitr-sh/authentication/twitr-sh-authentication.yml
  title: ''
  type: Authentication
  url: authentication/twitr-sh-authentication.yml
- group: design
  href: https://artifacts.apis.io/twitr-sh/errors/twitr-sh-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/twitr-sh-problem-types.yml
- group: design
  href: https://artifacts.apis.io/twitr-sh/conformance/twitr-sh-conformance.yml
  title: ''
  type: Conformance
  url: conformance/twitr-sh-conformance.yml
- group: agent
  href: https://artifacts.apis.io/twitr-sh/llms/twitr-sh-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/twitr-sh-llms.txt
- group: agent
  href: https://artifacts.apis.io/twitr-sh/mcp/twitr-sh-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/twitr-sh-mcp.yml
- group: agent
  href: https://artifacts.apis.io/twitr-sh/well-known/twitr-sh-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/twitr-sh-well-known.yml
- group: other
  href: https://artifacts.apis.io/twitr-sh/hosts/twitr-sh-hosts.yml
  title: ''
  type: Hosts
  url: hosts/twitr-sh-hosts.yml
- group: other
  href: https://artifacts.apis.io/twitr-sh/vendors/twitr-sh-vendors.yml
  title: ''
  type: Vendors
  url: vendors/twitr-sh-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://twitr.sh/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://twitr.sh/privacy
- group: auth
  href: https://artifacts.apis.io/twitr-sh/security/twitr-sh-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/twitr-sh-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://twitr.sh/
- group: docs
  title: ''
  type: Documentation
  url: https://twitr.sh/docs
- group: docs
  title: ''
  type: APIReference
  url: https://twitr.sh/openapi.json
- group: start
  title: ''
  type: GettingStarted
  url: https://twitr.sh/docs
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/lnvestor
created: '2026-10-31'
description: twitr.sh provides a pay‑per‑call X/Twitter API designed for AI agents. It offers read, search, timeline, bulk extraction, real‑time monitoring, signed webhooks and posting capabilities, all billed per request in USDC via x402 or MPP. No signup, API keys, or developer accounts are required; the wallet acts as the account. The service emphasizes seamless integration with Claude Code, Cursor, and OpenClaw agents.
image: https://twitr.sh/opengraph-image?4ae42b07156dcdc7
jsonld:
- class_count: 1
  name: Twitr Sh Context
  property_count: 9
  slug: twitr-sh-context
layout: provider
mcp_servers:
- description: Remote MCP server at twitr.sh.
  name: twitr-sh MCP Server
  slug: twitr-sh-mcp-yml
modified: '2026-10-31'
name: twitr-sh
nav: Providers
network: true
overview: 'twitr-sh publishes 8 API contracts indexed on the [APIs.io](https://apis.io/) network, including Accounts API, Creator API, Intelligence API, and 5 more. Tagged areas include Company, API, X, Twitter, and Pay-per-call.


  The twitr-sh catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  twitr-sh''s developer surface includes authentication, documentation, API reference, getting-started guide, and 21 more developer resources.'
plans:
- name: Twitr Sh Plans Pricing
  plan_count: 0
  slug: twitr-sh-plans-pricing
random_paper: 18
rate_limits:
- limit_count: 2
  name: Twitr Sh Rate Limits
  slug: twitr-sh-rate-limits
rules:
- authorship: generated
  effective_rule_count: 55
  extends:
  - spectral:oas
  name: twitr-sh API Rules
  rule_count: 14
  severity_counts:
    error: 12
    hint: 0
    info: 1
    warn: 1
  slug: twitr-sh-rules
scopes:
- name: Twitr Sh Scopes
  scope_count: 0
  slug: twitr-sh-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: developing
  composite: 47.5
  coverage:
    artifact_dirs: 27
    catalog_earned: 69.9
    catalog_earned_first_party: 0.0
    catalog_gap: 45.1
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 21.1
    contract_governance: 79.1
    contract_quality: 49.0
    developer_ergonomics: 46.9
    discoverability: 65.0
    operational_transparency: 24.2
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 31.8
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Twitr Sh Authentication
  slug: twitr-sh-authentication
  summary_line: 3 schemes
- kind: domain-security
  name: Twitr Sh Domain Security
  slug: twitr-sh-domain-security
  summary_line: TLSv1.3 · HSTS
skill_count: 2
skills:
- name: get-snapshot
  slug: twitr-sh-get-snapshot
- name: list-snapshots
  slug: twitr-sh-list-snapshots
slug: twitr-sh
tags:
- Company
- API
- X
- Twitter
- Pay-per-call
- AI
website: https://twitr.sh/
---
