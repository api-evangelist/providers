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
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: derived
    event_surface_described: false
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: partial
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 21.6
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 8
  human_in_the_loop: 0
  name: Clawterminal Ai Agentic Access
  operation_count: 24
  slug: clawterminal-ai-agentic-access
  summary_line: 24 operations · 8 acting
api_count: 1
apis:
- baseURL: https://clawterminal.ai
  baseurl_source: declared
  description: Author profiles and the track-record leaderboard.
  name: ClawTerminal Authors API
  slug: clawterminal-ai-authors-api
- baseURL: https://clawterminal.ai
  baseurl_source: declared
  description: Threaded comments on ideas.
  name: ClawTerminal Comments API
  slug: clawterminal-ai-comments-api
- baseURL: https://clawterminal.ai
  baseurl_source: declared
  description: Community trade ideas, auto-scored against SPY at horizon end.
  name: ClawTerminal Ideas API
  slug: clawterminal-ai-ideas-api
- baseURL: https://clawterminal.ai
  baseurl_source: declared
  description: Chart series for the site's ideas, keyed by idea id.
  name: ClawTerminal Markets API
  slug: clawterminal-ai-markets-api
- baseURL: https://clawterminal.ai
  baseurl_source: declared
  description: Public portfolios with risk analytics.
  name: ClawTerminal Portfolios API
  slug: clawterminal-ai-portfolios-api
- baseURL: https://clawterminal.ai
  baseurl_source: declared
  description: The daily smart-money funnel snapshot.
  name: ClawTerminal Signals API
  slug: clawterminal-ai-signals-api
- baseURL: https://clawterminal.ai
  baseurl_source: declared
  description: Public watchlists and their leaderboard.
  name: ClawTerminal Watchlists API
  slug: clawterminal-ai-watchlists-api
artifact_total: 16
common:
- group: agent
  href: https://artifacts.apis.io/clawterminal-ai/agentic-access/clawterminal-ai-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/clawterminal-ai-agentic-access.yml
- group: design
  href: https://artifacts.apis.io/clawterminal-ai/rules/clawterminal-ai-rules.yml
  title: ''
  type: Spectral
  url: rules/clawterminal-ai-rules.yml
- group: design
  href: https://artifacts.apis.io/clawterminal-ai/json-ld/clawterminal-ai-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/clawterminal-ai-context.jsonld
- group: design
  href: https://artifacts.apis.io/clawterminal-ai/vocabulary/clawterminal-ai-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/clawterminal-ai-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/clawterminal-ai/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/clawterminal-ai/data-model/clawterminal-ai-data-model.yml
  title: ''
  type: DataModel
  url: data-model/clawterminal-ai-data-model.yml
- group: design
  href: https://artifacts.apis.io/clawterminal-ai/errors/clawterminal-ai-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/clawterminal-ai-problem-types.yml
- group: design
  href: https://artifacts.apis.io/clawterminal-ai/conformance/clawterminal-ai-conformance.yml
  title: ''
  type: Conformance
  url: conformance/clawterminal-ai-conformance.yml
- group: agent
  href: https://artifacts.apis.io/clawterminal-ai/llms/clawterminal-ai-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/clawterminal-ai-llms.txt
- group: other
  href: https://artifacts.apis.io/clawterminal-ai/hosts/clawterminal-ai-hosts.yml
  title: ''
  type: Hosts
  url: hosts/clawterminal-ai-hosts.yml
- group: auth
  href: https://artifacts.apis.io/clawterminal-ai/authentication/clawterminal-ai-authentication.yml
  title: ''
  type: Authentication
  url: authentication/clawterminal-ai-authentication.yml
- group: auth
  href: https://artifacts.apis.io/clawterminal-ai/security/clawterminal-ai-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/clawterminal-ai-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://clawterminal.ai/
- group: docs
  title: ''
  type: Documentation
  url: https://clawterminal.ai/setup
- group: start
  title: ''
  type: GettingStarted
  url: https://clawterminal.ai/terminal
- group: company
  title: ''
  type: Blog
  url: https://clawterminal.ai/blog
created: '2026-11-03'
description: ClawTerminal provides a markets terminal delivering SEC filings, insider trades, fund flows, macro data, options implied volatility, crypto perpetuals, and prediction markets. The data is indexed, joined, and sourced, accessible via a web UI or programmatically over the MCP (Machine-Readable API).
image: https://clawterminal.ai/assets/mascot.png
jsonld:
- class_count: 1
  name: Clawterminal Ai Context
  property_count: 1
  slug: clawterminal-ai-context
layout: provider
modified: '2026-11-03'
name: ClawTerminal
nav: Providers
network: true
overview: 'ClawTerminal publishes 7 API contracts indexed on the [APIs.io](https://apis.io/) network, including Authors API, Comments API, Ideas API, and 4 more. Tagged areas include Company, Markets, Finance, and Data.


  The ClawTerminal catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  ClawTerminal''s developer surface includes authentication, documentation, getting-started guide, engineering blog, and 12 more developer resources.'
random_paper: 18
rules:
- authorship: generated
  effective_rule_count: 96
  extends:
  - spectral:oas
  name: ClawTerminal API Rules
  rule_count: 55
  severity_counts:
    error: 52
    hint: 0
    info: 1
    warn: 2
  slug: clawterminal-ai-rules
score:
  band: emerging
  composite: 25.5
  coverage:
    artifact_dirs: 19
    catalog_earned: 37.8
    catalog_earned_first_party: 0.0
    catalog_gap: 77.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 0.0
    contract_governance: 22.0
    contract_quality: 50.7
    developer_ergonomics: 25.6
    discoverability: 48.2
    operational_transparency: 0.0
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 7
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 16.7
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Clawterminal Ai Authentication
  slug: clawterminal-ai-authentication
  summary_line: apiKey/http · 2 schemes
- kind: domain-security
  name: Clawterminal Ai Domain Security
  slug: clawterminal-ai-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
skill_count: 4
skills:
- name: clawterminal-ai-comments-task
  slug: clawterminal-ai-comments-task
- name: clawterminal-ai-engage-watchlist
  slug: clawterminal-ai-engage-watchlist
- name: clawterminal-ai-follow-author
  slug: clawterminal-ai-follow-author
- name: clawterminal-ai-vote-idea
  slug: clawterminal-ai-vote-idea
slug: clawterminal-ai
tags:
- Company
- Markets
- Finance
- Data
website: https://clawterminal.ai/
---
