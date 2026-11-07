---
access_model:
  confidence: low
  gated: none
  gated_source:
  - onboarding
  label: Open access
  onboarding: open
  pricing: unknown
  public: true
  source:
  - authentication
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
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: true
  schema_version: '0.2'
  score: 6.8
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: Actions, parameters, response shapes, authentication, and payment headers for the LONG Events REST API.
  name: LONG Events API
  slug: long-events-api
artifact_total: 7
common:
- group: design
  href: https://artifacts.apis.io/belong-events/rules/belong-events-rules.yml
  title: ''
  type: Spectral
  url: rules/belong-events-rules.yml
- group: design
  href: https://artifacts.apis.io/belong-events/json-ld/belong-events-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/belong-events-context.jsonld
- group: design
  href: https://artifacts.apis.io/belong-events/vocabulary/belong-events-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/belong-events-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/belong-events/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/belong-events/data-model/belong-events-data-model.yml
  title: ''
  type: DataModel
  url: data-model/belong-events-data-model.yml
- group: design
  href: https://artifacts.apis.io/belong-events/errors/belong-events-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/belong-events-problem-types.yml
- group: design
  href: https://artifacts.apis.io/belong-events/conformance/belong-events-conformance.yml
  title: ''
  type: Conformance
  url: conformance/belong-events-conformance.yml
- group: agent
  href: https://artifacts.apis.io/belong-events/llms/belong-events-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/belong-events-llms.txt
- group: agent
  href: https://artifacts.apis.io/belong-events/well-known/belong-events-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/belong-events-well-known.yml
- group: other
  href: https://artifacts.apis.io/belong-events/hosts/belong-events-hosts.yml
  title: ''
  type: Hosts
  url: hosts/belong-events-hosts.yml
- group: auth
  href: https://artifacts.apis.io/belong-events/security/belong-events-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/belong-events-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://belong.events/
- group: docs
  title: ''
  type: Documentation
  url: https://belong.events/docs
- group: docs
  title: ''
  type: APIReference
  url: https://belong.events/docs/api
- group: start
  title: ''
  type: GettingStarted
  url: https://belong.events/docs
- group: operate
  title: ''
  type: Support
  url: https://belong.events/support
- group: company
  title: ''
  type: Blog
  url: https://belong.events/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/belong-events
- group: operate
  title: ''
  type: Roadmap
  url: https://belong.events/roadmap
- group: commercial
  title: ''
  type: Pricing
  url: https://belong.events/pricing
- group: start
  title: ''
  type: SignUp
  url: https://belong.events/signup
- group: commercial
  title: ''
  type: TermsOfService
  url: https://belong.events/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://belong.events/privacy
coverage:
  checked: '2026-11-02'
  detail: API documentation is served as a JavaScript-rendered site on belong.events, and the OpenAPI spec points to long.events, a separate domain, so no contract belongs to Belong Events.
  evidence:
  - status: 200
    url: https://belong.events/docs/api
  reason: js-rendered-docs
  state: unreadable
created: '2026-11-02'
description: Belong Events aggregates upcoming music, crypto/web3, tech, and nomad community events worldwide, pulling data from dozens of sources to provide a searchable platform for event discovery. The service offers curated listings, event details, and tools for users to explore and attend events across multiple categories and locations.
image: https://belong.events/belong-og-conference-host.png
jsonld:
- class_count: 9
  name: Belong Events Context
  property_count: 59
  slug: belong-events-context
layout: provider
modified: '2026-11-02'
name: Belong Events
nav: Providers
network: true
overview: 'Belong Events publishes 1 API contract indexed on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Event, Music, Cryptocurrency, and Tech.


  The Belong Events catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Belong Events'' developer surface includes documentation, API reference, getting-started guide, support, engineering blog, pricing, signup flow, and 16 more developer resources.'
random_paper: 17
rules:
- authorship: generated
  effective_rule_count: 99
  extends:
  - spectral:oas
  name: Belong Events API Rules
  rule_count: 58
  severity_counts:
    error: 56
    hint: 0
    info: 1
    warn: 1
  slug: belong-events-rules
scopes:
- name: Belong Events Scopes
  scope_count: 0
  slug: belong-events-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: emerging
  composite: 23.5
  coverage:
    artifact_dirs: 25
    catalog_earned: 48.8
    catalog_earned_first_party: 0.0
    catalog_gap: 66.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 22.4
    contract_governance: 22.0
    contract_quality: 14.7
    developer_ergonomics: 24.3
    discoverability: 57.1
    operational_transparency: 5.3
  provenance:
    conformance: derived
    mcp: derived
    skills: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 24.5
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Belong Events Authentication
  slug: belong-events-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Belong Events Domain Security
  slug: belong-events-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC
skill_count: 1
skills:
- name: belong-events-basic
  slug: belong-events-basic
slug: belong-events
tags:
- Company
- Event
- Music
- Cryptocurrency
- Tech
- Community
website: https://belong.events/
---
