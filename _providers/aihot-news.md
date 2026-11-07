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
    agent_skills: false
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
    mcp_server: documented
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
  score: 31.2
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Aihot News Agentic Access
  operation_count: 25
  slug: aihot-news-agentic-access
  summary_line: 25 operations
api_count: 1
apis:
- baseURL_template: '{{siteUrl}}'
  baseurl_source: spec_template
  description: The Agent API from AIHOT — 11 operation(s) for agent.
  name: AIHOT Agent API
  slug: aihot-news-agent-api
- baseURL_template: '{{siteUrl}}'
  baseurl_source: spec_template
  description: The Dailies API from AIHOT — 3 operation(s) for dailies.
  name: AIHOT Dailies API
  slug: aihot-news-dailies-api
- baseURL_template: '{{siteUrl}}'
  baseurl_source: spec_template
  description: The Hot Topics API from AIHOT — 1 operation(s) for hot topics.
  name: AIHOT Hot Topics API
  slug: aihot-news-hot-topics-api
- baseURL_template: '{{siteUrl}}'
  baseurl_source: spec_template
  description: The Items API from AIHOT — 1 operation(s) for items.
  name: AIHOT Items API
  slug: aihot-news-items-api
- baseURL_template: '{{siteUrl}}'
  baseurl_source: spec_template
  description: The Monthlies API from AIHOT — 3 operation(s) for monthlies.
  name: AIHOT Monthlies API
  slug: aihot-news-monthlies-api
- baseURL_template: '{{siteUrl}}'
  baseurl_source: spec_template
  description: The Selected API from AIHOT — 2 operation(s) for selected.
  name: AIHOT Selected API
  slug: aihot-news-selected-api
- baseURL_template: '{{siteUrl}}'
  baseurl_source: spec_template
  description: The Stories API from AIHOT — 1 operation(s) for stories.
  name: AIHOT Stories API
  slug: aihot-news-stories-api
- baseURL_template: '{{siteUrl}}'
  baseurl_source: spec_template
  description: The Weeklies API from AIHOT — 3 operation(s) for weeklies.
  name: AIHOT Weeklies API
  slug: aihot-news-weeklies-api
artifact_total: 13
common:
- group: agent
  href: https://artifacts.apis.io/aihot-news/agentic-access/aihot-news-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/aihot-news-agentic-access.yml
- group: design
  href: https://artifacts.apis.io/aihot-news/rules/aihot-news-rules.yml
  title: ''
  type: Spectral
  url: rules/aihot-news-rules.yml
- group: design
  href: https://artifacts.apis.io/aihot-news/json-ld/aihot-news-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/aihot-news-context.jsonld
- group: design
  href: https://artifacts.apis.io/aihot-news/vocabulary/aihot-news-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/aihot-news-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/aihot-news/data-model/aihot-news-data-model.yml
  title: ''
  type: DataModel
  url: data-model/aihot-news-data-model.yml
- group: operate
  href: https://artifacts.apis.io/aihot-news/changelog/aihot-news-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/aihot-news-changelog.yml
- group: auth
  href: https://artifacts.apis.io/aihot-news/security/aihot-news-vulnerability-disclosure.yml
  title: ''
  type: Security
  url: security/aihot-news-vulnerability-disclosure.yml
- group: design
  href: https://artifacts.apis.io/aihot-news/errors/aihot-news-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/aihot-news-problem-types.yml
- group: design
  href: https://artifacts.apis.io/aihot-news/conformance/aihot-news-conformance.yml
  title: ''
  type: Conformance
  url: conformance/aihot-news-conformance.yml
- group: agent
  href: https://artifacts.apis.io/aihot-news/llms/aihot-news-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/aihot-news-llms.txt
- group: auth
  href: https://artifacts.apis.io/aihot-news/well-known/aihot-news-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/aihot-news-security.txt
- group: agent
  href: https://artifacts.apis.io/aihot-news/well-known/aihot-news-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/aihot-news-well-known.yml
- group: other
  href: https://artifacts.apis.io/aihot-news/hosts/aihot-news-hosts.yml
  title: ''
  type: Hosts
  url: hosts/aihot-news-hosts.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://aihot.news/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://aihot.news/privacy
- group: operate
  title: ''
  type: ChangeLog
  url: https://aihot.news/changelog
- group: docs
  title: ''
  type: APIReference
  url: https://aihot.news/llms.txt
- group: auth
  href: https://artifacts.apis.io/aihot-news/security/aihot-news-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/aihot-news-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/aihot-news/security/aihot-news-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/aihot-news-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://aihot.news/
created: '2026-11-01'
description: AIHOT aggregates AI industry news, providing daily curated newsletters and real-time updates from over 900 sources. The platform offers free, read‑only access to its API, RSS feeds, and MCP endpoints without requiring registration or API keys. It supports non‑commercial, nonprofit, and internal organizational use, while commercial usage requires prior authorization. Operated by Beijing Xushi Kongji Cultural Technology Co., Ltd., AIHOT aims to deliver timely AI insights while respecting source copyrights and user privacy.
image: https://aihot.news/og/site.png
jsonld:
- class_count: 28
  name: Aihot News Context
  property_count: 68
  slug: aihot-news-context
layout: provider
modified: '2026-11-01'
name: AIHOT
nav: Providers
network: true
overview: 'AIHOT publishes 8 API contracts indexed on the [APIs.io](https://apis.io/) network, including Agent API, Dailies API, Hot Topics API, and 5 more. Tagged areas include Company.


  The AIHOT catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  AIHOT''s developer surface includes changelog, API reference, and 18 more developer resources.'
random_paper: 15
rules:
- authorship: generated
  effective_rule_count: 56
  extends:
  - spectral:oas
  name: AIHOT API Rules
  rule_count: 15
  severity_counts:
    error: 13
    hint: 0
    info: 1
    warn: 1
  slug: aihot-news-rules
score:
  band: emerging
  composite: 26.1
  coverage:
    artifact_dirs: 16
    catalog_earned: 43.8
    catalog_earned_first_party: 0.0
    catalog_gap: 71.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -4.5
  facets:
    access_clarity: 10.5
    contract_governance: 22.0
    contract_quality: 50.5
    developer_ergonomics: 3.6
    discoverability: 48.2
    operational_transparency: 18.4
  previous_composite: 30.6
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 9
    mcp: first-party
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 20.6
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Aihot News Domain Security
  slug: aihot-news-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC
- kind: vulnerability-disclosure
  name: Aihot News Vulnerability Disclosure
  slug: aihot-news-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: aihot-news
tags:
- Company
website: https://aihot.news/
---
