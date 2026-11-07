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
    agent_card: flavored
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
  score: 20.0
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 1
  human_in_the_loop: 0
  name: Aiplumber Online Agentic Access
  operation_count: 2
  slug: aiplumber-online-agentic-access
  summary_line: 2 operations · 1 acting
api_count: 1
apis:
- baseURL: https://aiplumber.online
  baseurl_source: declared
  description: The Gta API from GTA AI Plumber — 1 operation(s) for gta.
  name: GTA AI Plumber Gta API
  slug: aiplumber-online-gta-api
- baseURL: https://aiplumber.online
  baseurl_source: declared
  description: The Health API from GTA AI Plumber — 1 operation(s) for health.
  name: GTA AI Plumber Health API
  slug: aiplumber-online-health-api
artifact_total: 5
common:
- group: agent
  href: https://artifacts.apis.io/aiplumber-online/agentic-access/aiplumber-online-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/aiplumber-online-agentic-access.yml
- group: design
  href: https://artifacts.apis.io/aiplumber-online/rules/aiplumber-online-rules.yml
  title: ''
  type: Spectral
  url: rules/aiplumber-online-rules.yml
- group: design
  href: https://artifacts.apis.io/aiplumber-online/errors/aiplumber-online-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/aiplumber-online-problem-types.yml
- group: design
  href: https://artifacts.apis.io/aiplumber-online/conformance/aiplumber-online-conformance.yml
  title: ''
  type: Conformance
  url: conformance/aiplumber-online-conformance.yml
- group: agent
  href: https://artifacts.apis.io/aiplumber-online/llms/aiplumber-online-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/aiplumber-online-llms.txt
- group: other
  href: https://artifacts.apis.io/aiplumber-online/a2a/aiplumber-online-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/aiplumber-online-a2a.yml
- group: other
  href: https://artifacts.apis.io/aiplumber-online/hosts/aiplumber-online-hosts.yml
  title: ''
  type: Hosts
  url: hosts/aiplumber-online-hosts.yml
- group: other
  href: https://artifacts.apis.io/aiplumber-online/vendors/aiplumber-online-vendors.yml
  title: ''
  type: Vendors
  url: vendors/aiplumber-online-vendors.yml
- group: auth
  href: https://artifacts.apis.io/aiplumber-online/security/aiplumber-online-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/aiplumber-online-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://aiplumber.online/
- group: operate
  title: ''
  type: Support
  url: https://aiplumber.online/support
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://aiplumber.online/privacy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://aiplumber.online/terms
- group: docs
  title: ''
  type: APIReference
  url: https://aiplumber.online/gta/openapi.json
created: '2026-11-01'
description: GTA AI Plumber is an online platform that connects users in the Greater Toronto Area with local plumbing professionals. The service allows customers to request plumbing jobs, receive quotes, and book appointments through an AI‑driven interface. It aims to provide rapid response times, transparent pricing, and coordination with multiple vetted plumbers to ensure the best fit for each job. The platform also offers coverage across 25 municipalities, handling both routine repairs and emergency situations, while emphasizing user safety and convenience.
layout: provider
modified: '2026-11-01'
name: GTA AI Plumber
nav: Providers
network: true
overview: 'GTA AI Plumber publishes 2 API contracts indexed on the [APIs.io](https://apis.io/) network: Gta API and Health API. Tagged areas include Plumbing, Artificial Intelligence, Marketplace, GTA, and Services.


  The GTA AI Plumber catalog on APIs.io includes 1 Spectral governance ruleset.


  GTA AI Plumber''s developer surface includes support, API reference, and 12 more developer resources.'
random_paper: 19
rules:
- authorship: generated
  effective_rule_count: 50
  extends:
  - spectral:oas
  name: GTA AI Plumber API Rules
  rule_count: 9
  severity_counts:
    error: 7
    hint: 0
    info: 1
    warn: 1
  slug: aiplumber-online-rules
score:
  band: emerging
  composite: 21.9
  coverage:
    artifact_dirs: 14
    catalog_earned: 39.5
    catalog_earned_first_party: 0.0
    catalog_gap: 75.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -3.9
  facets:
    access_clarity: 10.5
    contract_governance: 18.2
    contract_quality: 41.6
    developer_ergonomics: 6.0
    discoverability: 62.5
    operational_transparency: 0.0
  previous_composite: 25.8
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 2
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 13.6
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Aiplumber Online Domain Security
  slug: aiplumber-online-domain-security
  summary_line: TLSv1.3
slug: aiplumber-online
tags:
- Plumbing
- Artificial Intelligence
- Marketplace
- GTA
- Services
website: https://aiplumber.online/
---
