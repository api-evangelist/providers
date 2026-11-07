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
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
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
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: partial
    protected_resource_metadata: false
    rate_limit_signal: verified
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 28.7
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Bithot News Agentic Access
  operation_count: 25
  slug: bithot-news-agentic-access
  summary_line: 25 operations
api_count: 1
apis:
- baseURL: https://bithot.news
  baseurl_source: declared
  description: The Agent API from BITHOT — 11 operation(s) for agent.
  name: BITHOT Agent API
  slug: bithot-news-agent-api
- baseURL: https://bithot.news
  baseurl_source: declared
  description: The Dailies API from BITHOT — 3 operation(s) for dailies.
  name: BITHOT Dailies API
  slug: bithot-news-dailies-api
- baseURL: https://bithot.news
  baseurl_source: declared
  description: The Hot Topics API from BITHOT — 1 operation(s) for hot topics.
  name: BITHOT Hot Topics API
  slug: bithot-news-hot-topics-api
- baseURL: https://bithot.news
  baseurl_source: declared
  description: The Items API from BITHOT — 1 operation(s) for items.
  name: BITHOT Items API
  slug: bithot-news-items-api
- baseURL: https://bithot.news
  baseurl_source: declared
  description: The Monthlies API from BITHOT — 3 operation(s) for monthlies.
  name: BITHOT Monthlies API
  slug: bithot-news-monthlies-api
- baseURL: https://bithot.news
  baseurl_source: declared
  description: The Selected API from BITHOT — 2 operation(s) for selected.
  name: BITHOT Selected API
  slug: bithot-news-selected-api
- baseURL: https://bithot.news
  baseurl_source: declared
  description: The Stories API from BITHOT — 1 operation(s) for stories.
  name: BITHOT Stories API
  slug: bithot-news-stories-api
- baseURL: https://bithot.news
  baseurl_source: declared
  description: The Weeklies API from BITHOT — 3 operation(s) for weeklies.
  name: BITHOT Weeklies API
  slug: bithot-news-weeklies-api
artifact_total: 19
common:
- group: agent
  href: https://artifacts.apis.io/bithot-news/agentic-access/bithot-news-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/bithot-news-agentic-access.yml
- group: design
  href: https://artifacts.apis.io/bithot-news/rules/bithot-news-rules.yml
  title: ''
  type: Spectral
  url: rules/bithot-news-rules.yml
- group: design
  href: https://artifacts.apis.io/bithot-news/json-ld/bithot-news-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/bithot-news-context.jsonld
- group: design
  href: https://artifacts.apis.io/bithot-news/vocabulary/bithot-news-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/bithot-news-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/bithot-news/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/bithot-news/data-model/bithot-news-data-model.yml
  title: ''
  type: DataModel
  url: data-model/bithot-news-data-model.yml
- group: operate
  href: https://artifacts.apis.io/bithot-news/changelog/bithot-news-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/bithot-news-changelog.yml
- group: design
  href: https://artifacts.apis.io/bithot-news/errors/bithot-news-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/bithot-news-problem-types.yml
- group: design
  href: https://artifacts.apis.io/bithot-news/conformance/bithot-news-conformance.yml
  title: ''
  type: Conformance
  url: conformance/bithot-news-conformance.yml
- group: agent
  href: https://artifacts.apis.io/bithot-news/llms/bithot-news-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/bithot-news-llms.txt
- group: other
  href: https://artifacts.apis.io/bithot-news/hosts/bithot-news-hosts.yml
  title: ''
  type: Hosts
  url: hosts/bithot-news-hosts.yml
- group: other
  href: https://artifacts.apis.io/bithot-news/vendors/bithot-news-vendors.yml
  title: ''
  type: Vendors
  url: vendors/bithot-news-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://bithot.news/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://bithot.news/privacy
- group: operate
  title: ''
  type: ChangeLog
  url: https://bithot.news/changelog
- group: auth
  href: https://artifacts.apis.io/bithot-news/security/bithot-news-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/bithot-news-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://bithot.news/
- group: docs
  title: ''
  type: APIReference
  url: https://bithot.news/openapi-v1.json
- group: other
  title: ''
  type: RSS
  url: https://bithot.news/feed.xml
- group: other
  title: ''
  type: PublicAPI
  url: https://bithot.news/api/v1/items
created: '2026-11-02'
description: BITHOT provides curated daily news, leaks, funding announcements and launches across blockchain, cryptocurrency, Web3 and memecoin sectors. The platform aggregates content from multiple sources, offering RSS feeds and a public JSON API for developers to access items, with updates at 07:00 Beijing time each day.
image: https://bithot.news/og/site.png
json_schemas:
- name: DailiesResponse
  property_count: 3
  slug: bithot-news-dailies-response
- name: ItemsResponse
  property_count: 4
  slug: bithot-news-items-response
- name: MonthliesResponse
  property_count: 3
  slug: bithot-news-monthlies-response
- name: SelectedChanges
  property_count: 6
  slug: bithot-news-selected-changes
- name: SelectedSnapshot
  property_count: 8
  slug: bithot-news-selected-snapshot
- name: WeekliesResponse
  property_count: 3
  slug: bithot-news-weeklies-response
jsonld:
- class_count: 28
  name: Bithot News Context
  property_count: 68
  slug: bithot-news-context
layout: provider
modified: '2026-11-02'
name: BITHOT
nav: Providers
network: true
overview: 'BITHOT publishes 8 API contracts indexed on the [APIs.io](https://apis.io/) network, including Agent API, Dailies API, Hot Topics API, and 5 more. Tagged areas include Company, Blockchain, Cryptocurrency, Web3, and Memecoin.


  The BITHOT catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  BITHOT''s developer surface includes changelog, API reference, and 18 more developer resources.'
random_paper: 12
rules:
- authorship: generated
  effective_rule_count: 87
  extends:
  - spectral:oas
  name: BITHOT API Rules
  rule_count: 46
  severity_counts:
    error: 36
    hint: 0
    info: 5
    warn: 5
  slug: bithot-news-rules
score:
  band: thin
  composite: 28.3
  coverage:
    artifact_dirs: 21
    catalog_earned: 62.8
    catalog_earned_first_party: 0.0
    catalog_gap: 52.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 10.5
    contract_governance: 22.0
    contract_quality: 59.7
    developer_ergonomics: 5.4
    discoverability: 66.1
    operational_transparency: 7.9
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 8
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 14.7
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Bithot News Domain Security
  slug: bithot-news-domain-security
  summary_line: TLSv1.3
skill_count: 1
skills:
- name: bithot-news-agent
  slug: bithot-news-agent
slug: bithot-news
tags:
- Company
- Blockchain
- Cryptocurrency
- Web3
- Memecoin
- News
website: https://bithot.news/
---
