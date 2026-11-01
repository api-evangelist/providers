---
agent_readiness:
  band: agent-aware
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
    error_semantics: derived
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    operation_distinctiveness: false
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 21.1
  scored_at: '2026-10-31'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Lrcmux Agentic Access
  operation_count: 5
  slug: lrcmux-agentic-access
  summary_line: 5 operations
api_count: 1
apis:
- baseURL: https://api.lrcmux.dev
  baseurl_source: declared
  description: The Compatibility API from LRCMux — 3 operation(s) for compatibility.
  name: LRCMux Compatibility API
  slug: lrcmux-compatibility-api
- baseURL: https://api.lrcmux.dev
  baseurl_source: declared
  description: The Lyrics API from LRCMux — 1 operation(s) for lyrics.
  name: LRCMux Lyrics API
  slug: lrcmux-lyrics-api
- baseURL: https://api.lrcmux.dev
  baseurl_source: declared
  description: The Meta API from LRCMux — 1 operation(s) for meta.
  name: LRCMux Meta API
  slug: lrcmux-meta-api
artifact_total: 12
common:
- group: agent
  href: https://artifacts.apis.io/lrcmux/agentic-access/lrcmux-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/lrcmux-agentic-access.yml
- group: design
  href: https://artifacts.apis.io/lrcmux/rules/lrcmux-rules.yml
  title: ''
  type: Spectral
  url: rules/lrcmux-rules.yml
- group: design
  href: https://artifacts.apis.io/lrcmux/json-ld/lrcmux-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/lrcmux-context.jsonld
- group: design
  href: https://artifacts.apis.io/lrcmux/vocabulary/lrcmux-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/lrcmux-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/lrcmux/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/lrcmux/data-model/lrcmux-data-model.yml
  title: ''
  type: DataModel
  url: data-model/lrcmux-data-model.yml
- group: design
  href: https://artifacts.apis.io/lrcmux/errors/lrcmux-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/lrcmux-problem-types.yml
- group: design
  href: https://artifacts.apis.io/lrcmux/conformance/lrcmux-conformance.yml
  title: ''
  type: Conformance
  url: conformance/lrcmux-conformance.yml
- group: other
  href: https://artifacts.apis.io/lrcmux/hosts/lrcmux-hosts.yml
  title: ''
  type: Hosts
  url: hosts/lrcmux-hosts.yml
- group: other
  href: https://artifacts.apis.io/lrcmux/vendors/lrcmux-vendors.yml
  title: ''
  type: Vendors
  url: vendors/lrcmux-vendors.yml
- group: auth
  href: https://artifacts.apis.io/lrcmux/security/lrcmux-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/lrcmux-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://lrcmux.dev/
- group: docs
  title: ''
  type: Documentation
  url: https://lrcmux.dev/docs
- group: other
  title: ''
  type: Source
  url: https://github.com/f1nniboy/lrcmux
- group: operate
  title: ''
  type: Support
  url: https://matrix.to/#/#lrcmux:oss.zone
created: '2026-10-28'
description: LRCMux provides a free synchronized lyrics API that delivers LRC, word‑by‑word, and plain‑text lyrics for any song. Powered by multiple providers, the service requires no API key and offers easy integration for developers building music‑related applications.
image: https://lrcmux.dev/logo.png
json_schemas:
- name: JSONResponse
  property_count: 3
  slug: lrcmux-jsonresponse
- name: KpoeResponse
  property_count: 5
  slug: lrcmux-kpoe-response
- name: LrclibResponse
  property_count: 9
  slug: lrcmux-lrclib-response
- name: StatsOutputBody
  property_count: 3
  slug: lrcmux-stats-output-body
jsonld:
- class_count: 18
  name: Lrcmux Context
  property_count: 51
  slug: lrcmux-context
layout: provider
modified: '2026-10-28'
name: LRCMux
nav: Providers
network: true
overview: 'LRCMux publishes 3 API contracts indexed on the [APIs.io](https://apis.io/) network: Compatibility API, Lyrics API, and Meta API. Tagged areas include Lyrics, Music, API, Free, and NoAuth.


  The LRCMux catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  LRCMux''s developer surface includes documentation, support, and 13 more developer resources.'
random_paper: 19
rules:
- authorship: generated
  effective_rule_count: 52
  extends:
  - spectral:oas
  name: LRCMux API Rules
  rule_count: 11
  severity_counts:
    error: 10
    hint: 0
    info: 1
    warn: 0
  slug: lrcmux-rules
score:
  band: emerging
  composite: 25.0
  coverage:
    artifact_dirs: 16
    catalog_earned: 62.0
    catalog_earned_first_party: 0.0
    catalog_gap: 53.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 0.0
    contract_governance: 19.7
    contract_quality: 50.3
    developer_ergonomics: 20.7
    discoverability: 66.1
    operational_transparency: 0.0
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 3
    mcp: derived
    skills: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 10.8
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Lrcmux Domain Security
  slug: lrcmux-domain-security
  summary_line: TLSv1.3
skill_count: 1
skills:
- name: get-lyrics
  slug: lrcmux-get-lyrics
slug: lrcmux
tags:
- Lyrics
- Music
- API
- Free
- NoAuth
website: https://lrcmux.dev/
---
