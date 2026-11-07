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
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    mcp_tool_quality: na
    openapi_examples: partial
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 43.7
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Altcoinchasershq App Agentic Access
  operation_count: 30
  slug: altcoinchasershq-app-agentic-access
  summary_line: 30 operations
api_count: 1
apis:
- baseURL: https://altcoinchasershq.app
  baseurl_source: declared
  description: The Agent API from Altcoin Chasers HQ — 9 operation(s) for agent.
  name: Altcoin Chasers HQ Agent API
  slug: altcoinchasershq-app-agent-api
- baseURL: https://altcoinchasershq.app
  baseurl_source: declared
  description: The Member API from Altcoin Chasers HQ — 12 operation(s) for member.
  name: Altcoin Chasers HQ Member API
  slug: altcoinchasershq-app-member-api
- baseURL: https://altcoinchasershq.app
  baseurl_source: declared
  description: The X402 API from Altcoin Chasers HQ — 9 operation(s) for x402.
  name: Altcoin Chasers HQ X402 API
  slug: altcoinchasershq-app-x402-api
artifact_total: 11
common:
- group: agent
  href: https://artifacts.apis.io/altcoinchasershq-app/agentic-access/altcoinchasershq-app-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/altcoinchasershq-app-agentic-access.yml
- group: design
  href: https://artifacts.apis.io/altcoinchasershq-app/rules/altcoinchasershq-app-rules.yml
  title: ''
  type: Spectral
  url: rules/altcoinchasershq-app-rules.yml
- group: design
  href: https://artifacts.apis.io/altcoinchasershq-app/json-ld/altcoinchasershq-app-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/altcoinchasershq-app-context.jsonld
- group: design
  href: https://artifacts.apis.io/altcoinchasershq-app/vocabulary/altcoinchasershq-app-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/altcoinchasershq-app-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/altcoinchasershq-app/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/altcoinchasershq-app/data-model/altcoinchasershq-app-data-model.yml
  title: ''
  type: DataModel
  url: data-model/altcoinchasershq-app-data-model.yml
- group: design
  href: https://artifacts.apis.io/altcoinchasershq-app/errors/altcoinchasershq-app-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/altcoinchasershq-app-problem-types.yml
- group: design
  href: https://artifacts.apis.io/altcoinchasershq-app/conformance/altcoinchasershq-app-conformance.yml
  title: ''
  type: Conformance
  url: conformance/altcoinchasershq-app-conformance.yml
- group: agent
  href: https://artifacts.apis.io/altcoinchasershq-app/llms/altcoinchasershq-app-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/altcoinchasershq-app-llms.txt
- group: agent
  href: https://artifacts.apis.io/altcoinchasershq-app/mcp/altcoinchasershq-app-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/altcoinchasershq-app-mcp.yml
- group: agent
  href: https://artifacts.apis.io/altcoinchasershq-app/well-known/altcoinchasershq-app-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/altcoinchasershq-app-well-known.yml
- group: other
  href: https://artifacts.apis.io/altcoinchasershq-app/hosts/altcoinchasershq-app-hosts.yml
  title: ''
  type: Hosts
  url: hosts/altcoinchasershq-app-hosts.yml
- group: auth
  href: https://artifacts.apis.io/altcoinchasershq-app/authentication/altcoinchasershq-app-authentication.yml
  title: ''
  type: Authentication
  url: authentication/altcoinchasershq-app-authentication.yml
- group: auth
  href: https://artifacts.apis.io/altcoinchasershq-app/security/altcoinchasershq-app-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/altcoinchasershq-app-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://altcoinchasershq.app/
- group: docs
  title: ''
  type: APIReference
  url: https://altcoinchasershq.app/openapi.json
- group: operate
  title: ''
  type: Support
  url: https://altcoinchasershq.app/support
- group: commercial
  title: ''
  type: TermsOfService
  url: https://altcoinchasershq.app/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://altcoinchasershq.app/privacy
created: '2026-11-01'
description: Altcoin Chasers HQ is an AI‑assisted crypto research terminal offering rug and honeypot checks, bundle/sniper detection, smart‑money and KOL wallet tracking. It provides cross‑source causal synthesis, exact‑contract identity, launch and surge discovery, forensics, and prediction‑market context for altcoin traders and researchers. Research only, not financial advice.
image: https://altcoinchasershq.app/og-image.jpg
json_schemas:
- name: AgentResponse
  property_count: 3
  slug: altcoinchasershq-app-agent-response
jsonld:
- class_count: 2
  name: Altcoinchasershq App Context
  property_count: 5
  slug: altcoinchasershq-app-context
layout: provider
mcp_servers:
- description: Remote MCP server at altcoinchasershq.app.
  name: Altcoin Chasers HQ MCP Server
  slug: altcoinchasershq-app-mcp-yml
modified: '2026-11-01'
name: Altcoin Chasers HQ
nav: Providers
network: true
overview: 'Altcoin Chasers HQ publishes 3 API contracts indexed on the [APIs.io](https://apis.io/) network: Agent API, Member API, and X402 API. Tagged areas include Cryptocurrency, Research, Artificial Intelligence, Finance, and Altcoins.


  The Altcoin Chasers HQ catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Altcoin Chasers HQ''s developer surface includes authentication, API reference, support, and 16 more developer resources.'
random_paper: 10
rules:
- authorship: generated
  effective_rule_count: 56
  extends:
  - spectral:oas
  name: Altcoin Chasers HQ API Rules
  rule_count: 15
  severity_counts:
    error: 13
    hint: 0
    info: 1
    warn: 1
  slug: altcoinchasershq-app-rules
score:
  band: thin
  composite: 29.2
  coverage:
    artifact_dirs: 20
    catalog_earned: 53.2
    catalog_earned_first_party: 0.0
    catalog_gap: 61.9
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -3.9
  facets:
    access_clarity: 10.5
    contract_governance: 22.0
    contract_quality: 53.9
    developer_ergonomics: 19.6
    discoverability: 65.0
    operational_transparency: 0.0
  previous_composite: 33.1
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 3
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 19.1
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Altcoinchasershq App Authentication
  slug: altcoinchasershq-app-authentication
  summary_line: http · 2 schemes
- kind: domain-security
  name: Altcoinchasershq App Domain Security
  slug: altcoinchasershq-app-domain-security
  summary_line: TLSv1.3 · HSTS
skill_count: 1
skills:
- name: market-history
  slug: altcoinchasershq-app-market-history
slug: altcoinchasershq-app
tags:
- Cryptocurrency
- Research
- Artificial Intelligence
- Finance
- Altcoins
website: https://altcoinchasershq.app/
---
