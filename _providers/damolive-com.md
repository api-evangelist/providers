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
    agent_card: false
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: false
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
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 17.3
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Damolive Com Agentic Access
  operation_count: 6
  slug: damolive-com-agentic-access
  summary_line: 6 operations
api_count: 1
apis:
- baseURL: https://api.damolive.com
  baseurl_source: declared
  description: The Health API from DAMO — 1 operation(s) for health.
  name: DAMO Health API
  slug: damolive-com-health-api
- baseURL: https://api.damolive.com
  baseurl_source: declared
  description: The Market State API from DAMO — 2 operation(s) for market state.
  name: DAMO Market State API
  slug: damolive-com-market-state-api
- baseURL: https://api.damolive.com
  baseurl_source: declared
  description: The States API from DAMO — 1 operation(s) for states.
  name: DAMO States API
  slug: damolive-com-states-api
- baseURL: https://api.damolive.com
  baseurl_source: declared
  description: The Symbols API from DAMO — 1 operation(s) for symbols.
  name: DAMO Symbols API
  slug: damolive-com-symbols-api
- baseURL: https://api.damolive.com
  baseurl_source: declared
  description: The .well Known API from DAMO — 1 operation(s) for .well known.
  name: DAMO .well Known API
  slug: damolive-com-well-known-api
artifact_total: 8
common:
- group: agent
  href: https://artifacts.apis.io/damolive-com/agentic-access/damolive-com-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/damolive-com-agentic-access.yml
- group: design
  href: https://artifacts.apis.io/damolive-com/rules/damolive-com-rules.yml
  title: ''
  type: Spectral
  url: rules/damolive-com-rules.yml
- group: design
  href: https://artifacts.apis.io/damolive-com/errors/damolive-com-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/damolive-com-problem-types.yml
- group: design
  href: https://artifacts.apis.io/damolive-com/conformance/damolive-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/damolive-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/damolive-com/llms/damolive-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/damolive-com-llms.txt
- group: other
  href: https://artifacts.apis.io/damolive-com/hosts/damolive-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/damolive-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/damolive-com/vendors/damolive-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/damolive-com-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.damolive.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.damolive.com/privacy
- group: commercial
  title: ''
  type: Pricing
  url: https://www.damolive.com/pricing
- group: auth
  href: https://artifacts.apis.io/damolive-com/security/damolive-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/damolive-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://damolive.com/
created: '2026-11-04'
description: DAMO provides a multi‑timeframe market state intelligence layer designed for humans, AI agents, and trading systems. It aggregates and visualizes market data across various time horizons, offering insights, trend analysis, and predictive signals to support decision‑making in finance and investment contexts. The platform emphasizes real‑time updates, customizable dashboards, and API access for integration into automated trading workflows.
layout: provider
modified: '2026-11-04'
name: DAMO
nav: Providers
network: true
overview: 'DAMO publishes 5 API contracts indexed on the [APIs.io](https://apis.io/) network, including Health API, Market State API, States API, and 2 more. Tagged areas include Finance, Market Data, Artificial Intelligence, Analytics, and Trading.


  The DAMO catalog on APIs.io includes 1 Spectral governance ruleset.


  DAMO''s developer surface includes pricing and 11 more developer resources.'
random_paper: 13
rules:
- authorship: generated
  effective_rule_count: 85
  extends:
  - spectral:oas
  name: DAMO API Rules
  rule_count: 44
  severity_counts:
    error: 41
    hint: 0
    info: 2
    warn: 1
  slug: damolive-com-rules
score:
  band: emerging
  composite: 25.0
  coverage:
    artifact_dirs: 15
    catalog_earned: 39.5
    catalog_earned_first_party: 0.0
    catalog_gap: 75.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 31.6
    contract_governance: 18.2
    contract_quality: 43.5
    developer_ergonomics: 0.0
    discoverability: 62.5
    operational_transparency: 0.0
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 5
    mcp: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Securities & Market Data
    regime_id: securities_market_data
    score: 16.4
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Damolive Com Domain Security
  slug: damolive-com-domain-security
  summary_line: TLSv1.3 · HSTS
slug: damolive-com
tags:
- Finance
- Market Data
- Artificial Intelligence
- Analytics
- Trading
website: https://damolive.com/
---
