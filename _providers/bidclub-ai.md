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
    idempotency: verified
    mcp_server: documented
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: false
    pagination_ratio: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 31.5
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 4
  human_in_the_loop: 0
  name: Bidclub Ai Agentic Access
  operation_count: 22
  slug: bidclub-ai-agentic-access
  summary_line: 22 operations · 4 acting
api_count: 1
apis:
- baseURL: https://bidclub.ai
  baseurl_source: declared
  description: The Dl API from BidClub — 2 operation(s) for dl.
  name: BidClub Dl API
  slug: bidclub-ai-dl-api
- baseURL: https://bidclub.ai
  baseurl_source: declared
  description: The Episodes API from BidClub — 2 operation(s) for episodes.
  name: BidClub Episodes API
  slug: bidclub-ai-episodes-api
- baseURL: https://bidclub.ai
  baseurl_source: declared
  description: The Feed Index API from BidClub — 3 operation(s) for feed index.
  name: BidClub Feed Index API
  slug: bidclub-ai-feed-index-api
- baseURL: https://bidclub.ai
  baseurl_source: declared
  description: The Pitch API from BidClub — 5 operation(s) for pitch.
  name: BidClub Pitch API
  slug: bidclub-ai-pitch-api
- baseURL: https://bidclub.ai
  baseurl_source: declared
  description: The Search API from BidClub — 1 operation(s) for search.
  name: BidClub Search API
  slug: bidclub-ai-search-api
- baseURL: https://bidclub.ai
  baseurl_source: declared
  description: The Shows API from BidClub — 1 operation(s) for shows.
  name: BidClub Shows API
  slug: bidclub-ai-shows-api
artifact_total: 17
common:
- group: agent
  href: https://artifacts.apis.io/bidclub-ai/agentic-access/bidclub-ai-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/bidclub-ai-agentic-access.yml
- group: design
  href: https://artifacts.apis.io/bidclub-ai/rules/bidclub-ai-rules.yml
  title: ''
  type: Spectral
  url: rules/bidclub-ai-rules.yml
- group: design
  href: https://artifacts.apis.io/bidclub-ai/json-ld/bidclub-ai-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/bidclub-ai-context.jsonld
- group: design
  href: https://artifacts.apis.io/bidclub-ai/vocabulary/bidclub-ai-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/bidclub-ai-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/bidclub-ai/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/bidclub-ai/data-model/bidclub-ai-data-model.yml
  title: ''
  type: DataModel
  url: data-model/bidclub-ai-data-model.yml
- group: design
  href: https://artifacts.apis.io/bidclub-ai/conventions/bidclub-ai-conventions.yml
  title: ''
  type: Idempotency
  url: conventions/bidclub-ai-conventions.yml
- group: design
  href: https://artifacts.apis.io/bidclub-ai/conventions/bidclub-ai-conventions.yml
  title: ''
  type: Conventions
  url: conventions/bidclub-ai-conventions.yml
- group: design
  href: https://artifacts.apis.io/bidclub-ai/errors/bidclub-ai-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/bidclub-ai-problem-types.yml
- group: design
  href: https://artifacts.apis.io/bidclub-ai/conformance/bidclub-ai-conformance.yml
  title: ''
  type: Conformance
  url: conformance/bidclub-ai-conformance.yml
- group: agent
  href: https://artifacts.apis.io/bidclub-ai/llms/bidclub-ai-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/bidclub-ai-llms.txt
- group: other
  href: https://artifacts.apis.io/bidclub-ai/hosts/bidclub-ai-hosts.yml
  title: ''
  type: Hosts
  url: hosts/bidclub-ai-hosts.yml
- group: other
  href: https://artifacts.apis.io/bidclub-ai/vendors/bidclub-ai-vendors.yml
  title: ''
  type: Vendors
  url: vendors/bidclub-ai-vendors.yml
- group: auth
  href: https://artifacts.apis.io/bidclub-ai/security/bidclub-ai-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/bidclub-ai-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://bidclub.ai/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://bidclub.ai/api-docs
- group: docs
  title: ''
  type: Documentation
  url: https://bidclub.ai/api-docs
- group: start
  title: ''
  type: GettingStarted
  url: https://bidclub.ai/readme
- group: other
  title: ''
  type: ReadMe
  url: https://bidclub.ai/readme
created: '2026-11-02'
description: BidClub provides free, bilingual investment‑podcast transcripts and research across frontier technology, finance, and companies. Its keyless API lets developers search and download spoken‑intelligence data without authentication, supporting both English and Chinese content. The platform aims to democratize access to investment research through open, searchable datasets and easy integration.
image: https://bidclub.ai/icon-192.png
json_schemas:
- name: EpisodeListResponse
  property_count: 3
  slug: bidclub-ai-episode-list-response
- name: Episode
  property_count: 33
  slug: bidclub-ai-episode
- name: FeedIndexResponse
  property_count: 2
  slug: bidclub-ai-feed-index-response
- name: PitchPage
  property_count: 3
  slug: bidclub-ai-pitch-page
- name: SearchResponse
  property_count: 5
  slug: bidclub-ai-search-response
- name: ShowList
  property_count: 1
  slug: bidclub-ai-show-list
jsonld:
- class_count: 13
  name: Bidclub Ai Context
  property_count: 63
  slug: bidclub-ai-context
layout: provider
modified: '2026-11-02'
name: BidClub
nav: Providers
network: true
overview: 'BidClub publishes 6 API contracts indexed on the [APIs.io](https://apis.io/) network, including Dl API, Episodes API, Feed Index API, and 3 more. Tagged areas include Company, Investment, Podcasts, and Research.


  The BidClub catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  BidClub''s developer surface includes documentation, getting-started guide, and 17 more developer resources.'
random_paper: 12
rules:
- authorship: generated
  effective_rule_count: 83
  extends:
  - spectral:oas
  name: BidClub API Rules
  rule_count: 42
  severity_counts:
    error: 32
    hint: 0
    info: 3
    warn: 7
  slug: bidclub-ai-rules
score:
  band: thin
  composite: 26.5
  coverage:
    artifact_dirs: 19
    catalog_earned: 57.8
    catalog_earned_first_party: 0.0
    catalog_gap: 57.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 0.0
    contract_governance: 22.0
    contract_quality: 57.8
    developer_ergonomics: 21.9
    discoverability: 57.1
    operational_transparency: 0.0
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 6
    mcp: unknown
    skills: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 10.8
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Bidclub Ai Domain Security
  slug: bidclub-ai-domain-security
  summary_line: TLSv1.3 · HSTS
skill_count: 1
skills:
- name: get-feed-index
  slug: bidclub-ai-get-feed-index
slug: bidclub-ai
tags:
- Company
- Investment
- Podcasts
- Research
website: https://bidclub.ai/
---
