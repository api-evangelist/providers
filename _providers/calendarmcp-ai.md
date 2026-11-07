---
access_model:
  confidence: low
  gated: none
  gated_source:
  - onboarding
  label: Self-serve signup
  onboarding: self-serve
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
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
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
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 18.9
  scored_at: '2026-11-06'
api_count: 2
apis:
- description: API for Calendar MCP service, documented at https://calendarmcp.ai/api/docs
  name: Calendar MCP API
  slug: calendar-mcp-api
- description: 'CalendarMCP API as documented publicly: 1 operations. Contract generated from the documentation by API Evangelist (2026-11-03); not the provider''s own document.'
  name: CalendarMCP API
  slug: calendarmcp-ai-api
artifact_total: 6
common:
- group: design
  href: https://artifacts.apis.io/calendarmcp-ai/rules/calendarmcp-ai-rules.yml
  title: ''
  type: Spectral
  url: rules/calendarmcp-ai-rules.yml
- group: design
  href: https://artifacts.apis.io/calendarmcp-ai/vocabulary/calendarmcp-ai-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/calendarmcp-ai-vocabulary.yml
- group: operate
  href: https://artifacts.apis.io/calendarmcp-ai/changelog/calendarmcp-ai-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/calendarmcp-ai-changelog.yml
- group: design
  href: https://artifacts.apis.io/calendarmcp-ai/conventions/calendarmcp-ai-conventions.yml
  title: ''
  type: Conventions
  url: conventions/calendarmcp-ai-conventions.yml
- group: auth
  href: https://artifacts.apis.io/calendarmcp-ai/authentication/calendarmcp-ai-authentication.yml
  title: ''
  type: Authentication
  url: authentication/calendarmcp-ai-authentication.yml
- group: design
  href: https://artifacts.apis.io/calendarmcp-ai/conformance/calendarmcp-ai-conformance.yml
  title: ''
  type: Conformance
  url: conformance/calendarmcp-ai-conformance.yml
- group: agent
  href: https://artifacts.apis.io/calendarmcp-ai/mcp/calendarmcp-ai-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/calendarmcp-ai-mcp.yml
- group: agent
  href: https://artifacts.apis.io/calendarmcp-ai/well-known/calendarmcp-ai-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/calendarmcp-ai-well-known.yml
- group: other
  href: https://artifacts.apis.io/calendarmcp-ai/hosts/calendarmcp-ai-hosts.yml
  title: ''
  type: Hosts
  url: hosts/calendarmcp-ai-hosts.yml
- group: other
  href: https://artifacts.apis.io/calendarmcp-ai/vendors/calendarmcp-ai-vendors.yml
  title: ''
  type: Vendors
  url: vendors/calendarmcp-ai-vendors.yml
- group: operate
  title: ''
  type: ChangeLog
  url: https://calendarmcp.ai/changelog
- group: auth
  href: https://artifacts.apis.io/calendarmcp-ai/security/calendarmcp-ai-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/calendarmcp-ai-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://calendarmcp.ai/
- group: docs
  title: ''
  type: Documentation
  url: https://calendarmcp.ai/docs
- group: docs
  title: ''
  type: APIReference
  url: https://calendarmcp.ai/api/docs
- group: commercial
  title: ''
  type: Pricing
  url: https://calendarmcp.ai/pricing
- group: company
  title: ''
  type: Blog
  url: https://calendarmcp.ai/blog
- group: operate
  title: ''
  type: Support
  url: https://calendarmcp.ai/dashboard
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://calendarmcp.ai/privacy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://calendarmcp.ai/terms
coverage:
  checked: '2026-11-03'
  detail: API documentation is provided as a simple JSON description, not a machine‑readable OpenAPI/GraphQL/AsyncAPI spec.
  evidence:
  - status: 200
    url: https://calendarmcp.ai/api/docs
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-11-03'
description: CalendarMCP provides a hosted Google Calendar MCP (Machine-Callable Procedure) service designed for AI agents. It offers free start-up access, scoped API keys, and a set of calendar tools such as list, create, update, and delete events. The platform includes agent‑readable docs, human documentation, pricing, and integration guides, enabling agents to manage calendars without handling Google credentials directly.
layout: provider
mcp_servers:
- description: Remote MCP server at calendarmcp.ai requiring an API key.
  name: CalendarMCP MCP Server
  slug: calendarmcp-ai-mcp-yml
modified: '2026-11-03'
name: CalendarMCP
nav: Providers
network: true
overview: 'CalendarMCP is listed with 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Calendar, Artificial Intelligence, MCP, Google Calendar, and Integration.


  The CalendarMCP catalog on APIs.io includes 1 Spectral governance ruleset.


  CalendarMCP''s developer surface includes changelog, authentication, documentation, API reference, pricing, engineering blog, support, and 13 more developer resources.'
random_paper: 1
rules:
- authorship: generated
  effective_rule_count: 68
  extends:
  - spectral:oas
  name: CalendarMCP API Rules
  rule_count: 27
  severity_counts:
    error: 25
    hint: 0
    info: 1
    warn: 1
  slug: calendarmcp-ai-rules
score:
  band: emerging
  composite: 20.4
  coverage:
    artifact_dirs: 15
    catalog_earned: 35.8
    catalog_earned_first_party: 0.0
    catalog_gap: 79.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 15.8
    contract_governance: 22.0
    contract_quality: 11.6
    developer_ergonomics: 23.8
    discoverability: 53.3
    operational_transparency: 7.9
  provenance:
    conformance: derived
    contracts:
      callable: 0.0
      derived: 1
      marker_coverage: 100.0
      total: 1
    mcp: first-party
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 19.1
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Calendarmcp Ai Authentication
  slug: calendarmcp-ai-authentication
  summary_line: 2 schemes
- kind: domain-security
  name: Calendarmcp Ai Domain Security
  slug: calendarmcp-ai-domain-security
  summary_line: TLSv1.3 · HSTS
slug: calendarmcp-ai
tags:
- Calendar
- Artificial Intelligence
- MCP
- Google Calendar
- Integration
website: https://calendarmcp.ai/
---
