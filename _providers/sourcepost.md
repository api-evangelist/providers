---
access_model:
  confidence: medium
  gated: none
  gated_source:
  - onboarding
  label: Open access
  onboarding: open
  pricing: unknown
  public: true
  source:
  - authentication
  - rate-limits
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: unknown
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: false
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: verified
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: verified
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 35.2
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 1
  human_in_the_loop: 0
  name: Sourcepost Agentic Access
  operation_count: 3
  slug: sourcepost-agentic-access
  summary_line: 3 operations · 1 acting
api_count: 1
apis:
- description: SourcePost is a directory where AI agents find suppliers, services and data sources for their task.
  name: SourcePost API
  slug: sourcepost-api
- baseURL: https://sourcepost.dev
  baseurl_source: declared
  description: The interest API from SourcePost — 1 operation(s) for interest.
  name: SourcePost Interest API
  slug: sourcepost-interest-api
- baseURL: https://sourcepost.dev
  baseurl_source: declared
  description: The listings API from SourcePost — 2 operation(s) for listings.
  name: SourcePost Listings API
  slug: sourcepost-listings-api
artifact_total: 10
common:
- group: design
  href: https://artifacts.apis.io/sourcepost/data-model/sourcepost-data-model.yml
  title: ''
  type: DataModel
  url: data-model/sourcepost-data-model.yml
- group: agent
  href: https://artifacts.apis.io/sourcepost/agentic-access/sourcepost-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/sourcepost-agentic-access.yml
- group: operate
  href: https://artifacts.apis.io/sourcepost/rate-limits/sourcepost-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/sourcepost-rate-limits.yml
- group: design
  href: https://artifacts.apis.io/sourcepost/rules/sourcepost-rules.yml
  title: ''
  type: Spectral
  url: rules/sourcepost-rules.yml
- group: design
  href: https://artifacts.apis.io/sourcepost/vocabulary/sourcepost-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/sourcepost-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/sourcepost/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/sourcepost/errors/sourcepost-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/sourcepost-problem-types.yml
- group: design
  href: https://artifacts.apis.io/sourcepost/conformance/sourcepost-conformance.yml
  title: ''
  type: Conformance
  url: conformance/sourcepost-conformance.yml
- group: agent
  href: https://artifacts.apis.io/sourcepost/llms/sourcepost-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/sourcepost-llms.txt
- group: other
  href: https://artifacts.apis.io/sourcepost/hosts/sourcepost-hosts.yml
  title: ''
  type: Hosts
  url: hosts/sourcepost-hosts.yml
- group: auth
  href: https://artifacts.apis.io/sourcepost/security/sourcepost-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/sourcepost-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://sourcepost.dev
- group: docs
  title: ''
  type: Documentation
  url: https://sourcepost.dev/docs
- group: docs
  title: ''
  type: APIReference
  url: https://sourcepost.dev/openapi.json
- group: start
  title: ''
  type: GettingStarted
  url: https://sourcepost.dev/docs
- group: commercial
  title: ''
  type: TermsOfService
  url: https://sourcepost.dev/legal?lang=en
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://sourcepost.dev/privacy?lang=en
created: '2026-11-02'
description: SourcePost is a directory for AI agents, providing a searchable catalog of suppliers, services, APIs and data sources that agents need to accomplish tasks. The platform offers an open API allowing agents to query listings without authentication, supporting up to 60 requests per minute. Listings are curated and reviewed, with sponsored entries clearly marked. The service does not require user accounts, cookies, or trackers.
layout: provider
modified: '2026-11-02'
name: SourcePost
nav: Providers
network: true
overview: 'SourcePost publishes 3 API contracts indexed on the [APIs.io](https://apis.io/) network, including Interest API, Listings API, and 1 more. Tagged areas include Artificial Intelligence, Directory, Suppliers, Data, and Agents.


  The SourcePost catalog on APIs.io includes 1 Spectral governance ruleset.


  SourcePost''s developer surface includes documentation, API reference, getting-started guide, and 14 more developer resources.'
random_paper: 7
rate_limits:
- limit_count: 2
  name: Sourcepost Rate Limits
  slug: sourcepost-rate-limits
rules:
- authorship: generated
  effective_rule_count: 90
  extends:
  - spectral:oas
  name: SourcePost API Rules
  rule_count: 49
  severity_counts:
    error: 47
    hint: 0
    info: 1
    warn: 1
  slug: sourcepost-rules
scopes:
- name: Sourcepost Scopes
  scope_count: 0
  slug: sourcepost-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: thin
  composite: 30.7
  coverage:
    artifact_dirs: 25
    catalog_earned: 48.8
    catalog_earned_first_party: 8.0
    catalog_gap: 66.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 10.5
    contract_governance: 22.0
    contract_quality: 46.8
    developer_ergonomics: 20.7
    discoverability: 62.5
    operational_transparency: 21.1
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
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
    score: 22.7
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Sourcepost Authentication
  slug: sourcepost-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Sourcepost Domain Security
  slug: sourcepost-domain-security
  summary_line: TLSv1.3 · DMARC
skill_count: 1
skills:
- name: sourcepost
  slug: sourcepost-skill
slug: sourcepost
tags:
- Artificial Intelligence
- Directory
- Suppliers
- Data
- Agents
website: https://sourcepost.dev
---
