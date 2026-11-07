---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
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
    agent_skills: unknown
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: false
    idempotency: documented
    mcp_server: documented
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 17.8
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: SanctionScreen provides a sanctions screening API for humans and AI agents.
  name: SanctionScreen API
  slug: sanctionscreen-api
artifact_total: 7
common:
- group: agent
  href: https://artifacts.apis.io/sanctionsscreen-io/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/sanctionsscreen-io/conventions/sanctionsscreen-io-conventions.yml
  title: ''
  type: Idempotency
  url: conventions/sanctionsscreen-io-conventions.yml
- group: design
  href: https://artifacts.apis.io/sanctionsscreen-io/conventions/sanctionsscreen-io-conventions.yml
  title: ''
  type: Conventions
  url: conventions/sanctionsscreen-io-conventions.yml
- group: auth
  href: https://artifacts.apis.io/sanctionsscreen-io/authentication/sanctionsscreen-io-authentication.yml
  title: ''
  type: Authentication
  url: authentication/sanctionsscreen-io-authentication.yml
- group: design
  href: https://artifacts.apis.io/sanctionsscreen-io/errors/sanctionsscreen-io-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/sanctionsscreen-io-problem-types.yml
- group: agent
  href: https://artifacts.apis.io/sanctionsscreen-io/llms/sanctionsscreen-io-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/sanctionsscreen-io-llms.txt
- group: agent
  href: https://artifacts.apis.io/sanctionsscreen-io/mcp/sanctionsscreen-io-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/sanctionsscreen-io-mcp.yml
- group: agent
  href: https://artifacts.apis.io/sanctionsscreen-io/well-known/sanctionsscreen-io-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/sanctionsscreen-io-well-known.yml
- group: other
  href: https://artifacts.apis.io/sanctionsscreen-io/hosts/sanctionsscreen-io-hosts.yml
  title: ''
  type: Hosts
  url: hosts/sanctionsscreen-io-hosts.yml
- group: other
  href: https://artifacts.apis.io/sanctionsscreen-io/vendors/sanctionsscreen-io-vendors.yml
  title: ''
  type: Vendors
  url: vendors/sanctionsscreen-io-vendors.yml
- group: auth
  href: https://artifacts.apis.io/sanctionsscreen-io/security/sanctionsscreen-io-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/sanctionsscreen-io-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://sanctionsscreen.io/
- group: docs
  title: ''
  type: Documentation
  url: https://sanctionsscreen.io/llms.txt
- group: docs
  title: ''
  type: APIReference
  url: https://sanctionsscreen.io/llms.txt
- group: start
  title: ''
  type: GettingStarted
  url: https://sanctionsscreen.io/#beta
- group: commercial
  title: ''
  type: Pricing
  url: https://sanctionsscreen.io/#pricing
- group: start
  title: ''
  type: SignUp
  url: https://sanctionsscreen.io/#beta
coverage:
  checked: '2026-10-31'
  detail: Only an MCP endpoint is documented; no OpenAPI/AsyncAPI/GraphQL spec is published.
  evidence:
  - status: 200
    url: https://sanctionsscreen.io/llms.txt
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-31'
description: SanctionScreen provides a per‑call sanctions screening API designed for both human users and AI agents. It enables rapid checks of names against OFAC, UK, EU (when available) and other sanctions lists, delivering enriched results with citations within approximately 110 ms per request. The service offers a free tier of 50 calls per month without requiring a credit card, and includes comprehensive documentation in llms.txt for easy integration.
layout: provider
mcp_servers:
- description: Remote MCP server at api.sanctionsscreen.io.
  name: sanctionsscreen-io MCP Server
  slug: sanctionsscreen-io-mcp-yml
modified: '2026-10-31'
name: sanctionsscreen-io
nav: Providers
network: true
overview: 'sanctionsscreen-io is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Sanctions, Compliance, and Fintech.


  sanctionsscreen-io''s developer surface includes authentication, documentation, API reference, getting-started guide, pricing, signup flow, and 11 more developer resources.'
plans:
- name: Sanctionsscreen Io Plans Pricing
  plan_count: 0
  slug: sanctionsscreen-io-plans-pricing
random_paper: 7
rate_limits:
- limit_count: 0
  name: Sanctionsscreen Io Rate Limits
  slug: sanctionsscreen-io-rate-limits
scopes:
- name: Sanctionsscreen Io Scopes
  scope_count: 0
  slug: sanctionsscreen-io-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: emerging
  composite: 15.2
  coverage:
    artifact_dirs: 22
    catalog_earned: 30.0
    catalog_earned_first_party: 0.0
    catalog_gap: 85.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -6.1
  facets:
    access_clarity: 11.8
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 32.6
    discoverability: 53.3
    operational_transparency: 0.0
  previous_composite: 21.3
  provenance:
    conformance: unknown
    mcp: first-party
    skills: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 21.6
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/sanctionsscreen-io/sanctionsscreen-io-2026-11-03T142701.png
security:
- kind: authentication
  name: Sanctionsscreen Io Authentication
  slug: sanctionsscreen-io-authentication
  summary_line: 2 schemes
- kind: domain-security
  name: Sanctionsscreen Io Domain Security
  slug: sanctionsscreen-io-domain-security
  summary_line: TLSv1.3
slug: sanctionsscreen-io
tags:
- Company
- Sanctions
- Compliance
- Fintech
website: https://sanctionsscreen.io/
---
