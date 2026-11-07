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
    agent_card: conformant
    agent_skills: false
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
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 14.4
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 1
  human_in_the_loop: 0
  name: Agent Z App Agentic Access
  operation_count: 5
  slug: agent-z-app-agentic-access
  summary_line: 5 operations · 1 acting
api_count: 1
apis:
- description: Daily call basket API providing market calls with optional payment and member key authentication.
  name: EDGE DAILY 8 API
  slug: edge-daily-8-api
artifact_total: 6
common:
- group: agent
  href: https://artifacts.apis.io/agent-z-app/agentic-access/agent-z-app-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/agent-z-app-agentic-access.yml
- group: design
  href: https://artifacts.apis.io/agent-z-app/rules/agent-z-app-rules.yml
  title: ''
  type: Spectral
  url: rules/agent-z-app-rules.yml
- group: design
  href: https://artifacts.apis.io/agent-z-app/json-ld/agent-z-app-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/agent-z-app-context.jsonld
- group: design
  href: https://artifacts.apis.io/agent-z-app/vocabulary/agent-z-app-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/agent-z-app-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/agent-z-app/data-model/agent-z-app-data-model.yml
  title: ''
  type: DataModel
  url: data-model/agent-z-app-data-model.yml
- group: design
  href: https://artifacts.apis.io/agent-z-app/errors/agent-z-app-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/agent-z-app-problem-types.yml
- group: design
  href: https://artifacts.apis.io/agent-z-app/conformance/agent-z-app-conformance.yml
  title: ''
  type: Conformance
  url: conformance/agent-z-app-conformance.yml
- group: agent
  href: https://artifacts.apis.io/agent-z-app/llms/agent-z-app-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/agent-z-app-llms.txt
- group: other
  href: https://artifacts.apis.io/agent-z-app/a2a/agent-z-app-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/agent-z-app-a2a.yml
- group: agent
  href: https://artifacts.apis.io/agent-z-app/well-known/agent-z-app-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/agent-z-app-well-known.yml
- group: other
  href: https://artifacts.apis.io/agent-z-app/hosts/agent-z-app-hosts.yml
  title: ''
  type: Hosts
  url: hosts/agent-z-app-hosts.yml
- group: other
  href: https://artifacts.apis.io/agent-z-app/vendors/agent-z-app-vendors.yml
  title: ''
  type: Vendors
  url: vendors/agent-z-app-vendors.yml
- group: auth
  href: https://artifacts.apis.io/agent-z-app/authentication/agent-z-app-authentication.yml
  title: ''
  type: Authentication
  url: authentication/agent-z-app-authentication.yml
- group: auth
  href: https://artifacts.apis.io/agent-z-app/security/agent-z-app-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/agent-z-app-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://agent-z.app/
- group: docs
  title: ''
  type: Documentation
  url: https://agent-z.app/methodology
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://agent-z.app/privacy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://agent-z.app/disclaimer
- group: start
  title: ''
  type: GettingStarted
  url: https://agent-z.app/wallet-guide
coverage:
  detail: the company serves an API surface but requires credentials before any description of it can be read
  evidence:
  - status: null
    url: https://agent-z.app/openapi.json
  - status: 401
    url: https://agent-z.app/mcp
  - status: 200
    url: https://agent-z.app/
  reason: partner-login
  state: gated
created: '2026-10-31'
description: EDGE provides tokenized intelligence and automated trading strategies for users. The platform offers a trading edge through diversified investment models, allowing users to select risk levels and connect crypto wallets. It includes a free trial, portfolio rebalancing, and detailed performance tracking via a web dashboard.
image: https://pub-bb2e103a32db4e198524a2e9ed8f35b4.r2.dev/lovp_0w5vkw1drc8yjvwmes10x69rnt/23ec6eade74a70b898eaf661376b9774_1793482824471.png
jsonld:
- class_count: 1
  name: Agent Z App Context
  property_count: 11
  slug: agent-z-app-context
layout: provider
modified: '2026-10-31'
name: EDGE
nav: Providers
network: true
overview: 'EDGE is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Finance, Cryptocurrency, Trading, Automation, and Tokenization.


  The EDGE catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  EDGE''s developer surface includes authentication, documentation, getting-started guide, and 16 more developer resources.'
random_paper: 4
rules:
- authorship: generated
  effective_rule_count: 51
  extends:
  - spectral:oas
  name: EDGE API Rules
  rule_count: 10
  severity_counts:
    error: 7
    hint: 0
    info: 2
    warn: 1
  slug: agent-z-app-rules
score:
  band: emerging
  composite: 18.4
  coverage:
    artifact_dirs: 17
    catalog_earned: 50.8
    catalog_earned_first_party: 0.0
    catalog_gap: 64.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -4.8
  facets:
    access_clarity: 10.5
    contract_governance: 22.0
    contract_quality: 10.7
    developer_ergonomics: 22.6
    discoverability: 66.1
    operational_transparency: 0.0
  previous_composite: 23.2
  provenance:
    agentic_access: derived
    conformance: derived
    mcp: derived
  regulatory:
    applies: true
    matched_via: weak_tags
    regime: Securities & Market Data
    regime_id: securities_market_data
    score: 19.4
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Agent Z App Authentication
  slug: agent-z-app-authentication
  summary_line: apiKey/http · 2 schemes
- kind: domain-security
  name: Agent Z App Domain Security
  slug: agent-z-app-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: agent-z-app
tags:
- Finance
- Cryptocurrency
- Trading
- Automation
- Tokenization
website: https://agent-z.app/
---
