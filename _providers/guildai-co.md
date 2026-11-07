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
  band: agent-native
  dimensions:
    agent_card: false
    agent_skills: unknown
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: na
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: false
    idempotency: na
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: verified
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 42.5
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Guildai Co Agentic Access
  operation_count: 2
  slug: guildai-co-agentic-access
  summary_line: 2 operations
api_count: 2
apis:
- baseURL: https://app.guildai.co
  baseurl_source: declared
  description: The Opportunity Feed API from Guild — 1 operation(s) for opportunity feed.
  name: Guild Opportunity Feed API
  slug: guildai-co-opportunity-feed-api
artifact_total: 10
common:
- group: agent
  href: https://artifacts.apis.io/guildai-co/agentic-access/guildai-co-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/guildai-co-agentic-access.yml
- group: design
  href: https://artifacts.apis.io/guildai-co/rules/guildai-co-rules.yml
  title: ''
  type: Spectral
  url: rules/guildai-co-rules.yml
- group: design
  href: https://artifacts.apis.io/guildai-co/json-ld/guildai-co-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/guildai-co-context.jsonld
- group: design
  href: https://artifacts.apis.io/guildai-co/vocabulary/guildai-co-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/guildai-co-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/guildai-co/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/guildai-co/data-model/guildai-co-data-model.yml
  title: ''
  type: DataModel
  url: data-model/guildai-co-data-model.yml
- group: auth
  href: https://artifacts.apis.io/guildai-co/authentication/guildai-co-authentication.yml
  title: ''
  type: Authentication
  url: authentication/guildai-co-authentication.yml
- group: design
  href: https://artifacts.apis.io/guildai-co/errors/guildai-co-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/guildai-co-problem-types.yml
- group: design
  href: https://artifacts.apis.io/guildai-co/conformance/guildai-co-conformance.yml
  title: ''
  type: Conformance
  url: conformance/guildai-co-conformance.yml
- group: other
  href: https://artifacts.apis.io/guildai-co/overlays/guildai-co-openapi-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/guildai-co-openapi-overlay.yaml
- group: other
  href: https://artifacts.apis.io/guildai-co/hosts/guildai-co-hosts.yml
  title: ''
  type: Hosts
  url: hosts/guildai-co-hosts.yml
- group: other
  href: https://artifacts.apis.io/guildai-co/vendors/guildai-co-vendors.yml
  title: ''
  type: Vendors
  url: vendors/guildai-co-vendors.yml
- group: auth
  href: https://artifacts.apis.io/guildai-co/security/guildai-co-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/guildai-co-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.guildai.co
- group: docs
  title: ''
  type: Documentation
  url: https://docs.guildai.co
- group: docs
  title: ''
  type: APIReference
  url: https://docs.guildai.co/openapi.yaml
- group: start
  title: ''
  type: GettingStarted
  url: https://www.guildai.co/platform/
- group: operate
  title: ''
  type: Support
  url: mailto:info@guildai.co
- group: start
  title: ''
  type: DeveloperPortal
  url: https://app.guildai.co/auth
- group: start
  title: ''
  type: SignUp
  url: https://app.guildai.co/auth
created: '2026-10-29'
description: Guild is an AI-native defense contractor that transforms government requirements into manufactured aerospace parts, handling everything from planning through delivery. The company leverages artificial intelligence to automate the conversion of technical specifications into production plans, coordinate qualified factories, manage compliance, and ensure timely delivery of critical defense hardware. Backed by Y Combinator, Guild aims to reduce waste, accelerate production cycles, and provide transparent, traceable manufacturing for defense contracts.
image: https://www.guildai.co/hero/guild-galaxy-spline-poster.jpg
json_schemas:
- name: OpportunityFeedResponse
  property_count: 3
  slug: guildai-co-opportunity-feed-response
jsonld:
- class_count: 3
  name: Guildai Co Context
  property_count: 17
  slug: guildai-co-context
layout: provider
modified: '2026-10-29'
name: Guild
nav: Providers
network: true
overview: 'Guild publishes 1 API contract indexed on the [APIs.io](https://apis.io/) network: Opportunity Feed API. Tagged areas include Company, Artificial Intelligence, Defense, Manufacturing, and Aerospace.


  The Guild catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Guild''s developer surface includes authentication, documentation, API reference, getting-started guide, support, signup flow, and 14 more developer resources.'
random_paper: 6
rate_limits:
- limit_count: 0
  name: Guildai Co Rate Limits
  slug: guildai-co-rate-limits
rules:
- authorship: generated
  effective_rule_count: 57
  extends:
  - spectral:oas
  name: Guild API Rules
  rule_count: 16
  severity_counts:
    error: 14
    hint: 0
    info: 1
    warn: 1
  slug: guildai-co-rules
scopes:
- name: Guildai Co Scopes
  scope_count: 0
  slug: guildai-co-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: thin
  composite: 35.2
  coverage:
    artifact_dirs: 27
    catalog_earned: 56.2
    catalog_earned_first_party: 0.0
    catalog_gap: 58.9
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -5.1
  facets:
    access_clarity: 6.6
    contract_governance: 22.0
    contract_quality: 59.0
    developer_ergonomics: 42.1
    discoverability: 66.1
    operational_transparency: 0.0
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 40.3
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 50.0
      derived: 0
      marker_coverage: 0.0
      total: 2
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
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: this provider''s published contracts declare no write operations, and a read-only API cannot create-or-update. Excluded from the denominator, not zeroed.'
    reason: read_only
screenshot: https://apis.io/screenshots/guildai-co/guildai-co-2026-11-03T133121.png
security:
- kind: authentication
  name: Guildai Co Authentication
  slug: guildai-co-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Guildai Co Domain Security
  slug: guildai-co-domain-security
  summary_line: TLSv1.3 · DMARC
skill_count: 1
skills:
- name: public-opportunity-feed
  slug: guildai-co-public-opportunity-feed
slug: guildai-co
tags:
- Company
- Artificial Intelligence
- Defense
- Manufacturing
- Aerospace
- Startups
website: https://www.guildai.co
---
