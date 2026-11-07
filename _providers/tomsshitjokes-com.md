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
    agentic_access: false
    agentic_commerce: false
    auth_clarity: false
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
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
  score: 12.9
  scored_at: '2026-11-06'
api_count: 2
apis:
- description: Free JSON jokes API without a key.
  name: Tom's Shit Jokes API
  slug: tom-s-shit-jokes-api
- description: 'Tom''s Shit Jokes API as documented publicly: 1 operations. Contract generated from the documentation by API Evangelist (2026-11-05); not the provider''s own document.'
  name: Tom's Shit Jokes API
  slug: tomsshitjokes-com-api
artifact_total: 4
common:
- group: design
  href: https://artifacts.apis.io/tomsshitjokes-com/rules/tomsshitjokes-com-rules.yml
  title: ''
  type: Spectral
  url: rules/tomsshitjokes-com-rules.yml
- group: design
  href: https://artifacts.apis.io/tomsshitjokes-com/vocabulary/tomsshitjokes-com-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/tomsshitjokes-com-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/tomsshitjokes-com/conformance/tomsshitjokes-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/tomsshitjokes-com-conformance.yml
- group: other
  href: https://artifacts.apis.io/tomsshitjokes-com/hosts/tomsshitjokes-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/tomsshitjokes-com-hosts.yml
- group: company
  title: ''
  type: Newsroom
  url: https://www.tomsshitjokes.com/jokes/news/
- group: auth
  href: https://artifacts.apis.io/tomsshitjokes-com/security/tomsshitjokes-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/tomsshitjokes-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.tomsshitjokes.com
- group: docs
  title: ''
  type: Documentation
  url: https://www.tomsshitjokes.com/joke-api/
- group: docs
  title: ''
  type: APIReference
  url: https://www.tomsshitjokes.com/wp-json/tsj/v1
- group: start
  title: ''
  type: GettingStarted
  url: https://www.tomsshitjokes.com/joke-api/
coverage:
  checked: '2026-11-05'
  detail: The provider only offers a JSON endpoint without an OpenAPI or other machine‑readable contract.
  evidence:
  - status: 200
    url: https://www.tomsshitjokes.com/wp-json/tsj/v1
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-11-05'
description: Tom's Shit Jokes is the No. 1 Shit Jokes website with 350+ really bad jokes across many categories. All profits from advertising and shop sales are donated to Macmillan. The API provides free JSON jokes without a key, accessible via the WP-JSON endpoint.
layout: provider
modified: '2026-11-05'
name: Tom's Shit Jokes
nav: Providers
network: true
overview: 'Tom''s Shit Jokes is listed with 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Jokes and Christmas Cards.


  The Tom''s Shit Jokes catalog on APIs.io includes 1 Spectral governance ruleset.


  Tom''s Shit Jokes'' developer surface includes documentation, API reference, getting-started guide, and 7 more developer resources.'
random_paper: 19
rules:
- authorship: generated
  effective_rule_count: 61
  extends:
  - spectral:oas
  name: Tom's Shit Jokes API Rules
  rule_count: 20
  severity_counts:
    error: 18
    hint: 0
    info: 1
    warn: 1
  slug: tomsshitjokes-com-rules
score:
  band: emerging
  composite: 13.9
  coverage:
    artifact_dirs: 12
    catalog_earned: 30.8
    catalog_earned_first_party: 0.0
    catalog_gap: 84.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 0.0
    contract_governance: 22.0
    contract_quality: 9.4
    developer_ergonomics: 28.6
    discoverability: 46.4
    operational_transparency: 0.0
  provenance:
    conformance: derived
    contracts:
      callable: 0.0
      derived: 1
      marker_coverage: 100.0
      total: 1
    mcp: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 9.8
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Tomsshitjokes Com Domain Security
  slug: tomsshitjokes-com-domain-security
  summary_line: TLSv1.3
slug: tomsshitjokes-com
tags:
- Jokes
- Christmas Cards
website: https://www.tomsshitjokes.com
---
