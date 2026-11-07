---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: conformant
    agent_skills: false
    agentic_access: derived
    agentic_commerce: self
    auth_clarity: false
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
    spec_presence: false
    well_known_catalog: true
  schema_version: '0.2'
  score: 17.5
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Blinkcodes Com Agentic Access
  operation_count: 2
  slug: blinkcodes-com-agentic-access
  summary_line: 2 operations
api_count: 1
apis:
- description: Public unauthenticated API for browsing catalog and creating orders.
  name: BlinkCodes API
  slug: blinkcodes-api
artifact_total: 5
common:
- group: agent
  href: https://artifacts.apis.io/blinkcodes-com/agentic-access/blinkcodes-com-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/blinkcodes-com-agentic-access.yml
- group: design
  href: https://artifacts.apis.io/blinkcodes-com/rules/blinkcodes-com-rules.yml
  title: ''
  type: Spectral
  url: rules/blinkcodes-com-rules.yml
- group: design
  href: https://artifacts.apis.io/blinkcodes-com/conformance/blinkcodes-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/blinkcodes-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/blinkcodes-com/llms/blinkcodes-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/blinkcodes-com-llms.txt
- group: other
  href: https://artifacts.apis.io/blinkcodes-com/a2a/blinkcodes-com-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/blinkcodes-com-a2a.yml
- group: build
  href: https://artifacts.apis.io/blinkcodes-com/mcp/blinkcodes-com-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/blinkcodes-com-tool-crosswalk.yml
- group: agent
  href: https://artifacts.apis.io/blinkcodes-com/mcp/blinkcodes-com-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/blinkcodes-com-mcp.yml
- group: agent
  href: https://artifacts.apis.io/blinkcodes-com/well-known/blinkcodes-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/blinkcodes-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/blinkcodes-com/hosts/blinkcodes-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/blinkcodes-com-hosts.yml
- group: auth
  href: https://artifacts.apis.io/blinkcodes-com/security/blinkcodes-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/blinkcodes-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://blinkcodes.com/
- group: docs
  title: ''
  type: Documentation
  url: https://blinkcodes.com/en/
- group: docs
  title: ''
  type: APIReference
  url: https://blinkcodes.com/openapi.json
- group: company
  title: ''
  type: Blog
  url: https://blinkcodes.com/en/blog/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://blinkcodes.com/en/privacy/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://blinkcodes.com/en/terms/
created: '2026-11-02'
description: BlinkCodes offers a catalog of digital gift cards, eSIMs, and virtual phone numbers across 80+ countries. Customers can instantly purchase Apple, Steam, Google Play, PlayStation gift cards, as well as eSIM data plans and temporary phone numbers for verification. The platform provides 24/7 support, fast delivery via email, and a searchable catalog with filters for quick selection. It serves both individual consumers and developers needing virtual numbers for AI agents or testing.
image: https://blinkcodes.com/og-image.webp
layout: provider
mcp_servers:
- description: Remote MCP server at blinkcodes.com.
  name: BlinkCodes MCP Server
  slug: blinkcodes-com-mcp-yml
modified: '2026-11-02'
name: BlinkCodes
nav: Providers
network: true
overview: 'BlinkCodes is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Gift Cards, eSIM, and Virtual Numbers.


  The BlinkCodes catalog on APIs.io includes 1 Spectral governance ruleset.


  BlinkCodes'' developer surface includes documentation, API reference, engineering blog, and 13 more developer resources.'
random_paper: 2
rules:
- authorship: generated
  effective_rule_count: 73
  extends:
  - spectral:oas
  name: BlinkCodes API Rules
  rule_count: 32
  severity_counts:
    error: 30
    hint: 0
    info: 1
    warn: 1
  slug: blinkcodes-com-rules
score:
  band: minimal
  composite: 10.9
  coverage:
    artifact_dirs: 13
    catalog_earned: 36.5
    catalog_earned_first_party: 0.0
    catalog_gap: 78.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 10.5
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 9.5
    discoverability: 56.7
    operational_transparency: 0.0
  provenance:
    agentic_access: derived
    conformance: derived
    mcp: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 13.4
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Blinkcodes Com Domain Security
  slug: blinkcodes-com-domain-security
  summary_line: TLSv1.3 · DMARC
slug: blinkcodes-com
tags:
- Company
- Gift Cards
- eSIM
- Virtual Numbers
website: https://blinkcodes.com/
---
