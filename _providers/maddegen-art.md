---
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: conformant
    agent_skills: unknown
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
    openapi_examples: verified
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 33.5
  scored_at: '2026-10-31'
agentic_access:
- acting_count: 4
  human_in_the_loop: 0
  name: Maddegen Art Agentic Access
  operation_count: 4
  slug: maddegen-art-agentic-access
  summary_line: 4 operations · 4 acting
api_count: 2
apis:
- baseURL: https://augur-trade.com
  baseurl_source: declared
  description: The Pump Cortex API from maddegen-art — 4 operation(s) for pump cortex.
  name: maddegen-art Pump Cortex API
  slug: maddegen-art-pump-cortex-api
artifact_total: 10
common:
- group: agent
  href: https://artifacts.apis.io/maddegen-art/agentic-access/maddegen-art-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/maddegen-art-agentic-access.yml
- group: design
  href: https://artifacts.apis.io/maddegen-art/rules/maddegen-art-rules.yml
  title: ''
  type: Spectral
  url: rules/maddegen-art-rules.yml
- group: design
  href: https://artifacts.apis.io/maddegen-art/vocabulary/maddegen-art-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/maddegen-art-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/maddegen-art/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: auth
  href: https://artifacts.apis.io/maddegen-art/authentication/maddegen-art-authentication.yml
  title: ''
  type: Authentication
  url: authentication/maddegen-art-authentication.yml
- group: design
  href: https://artifacts.apis.io/maddegen-art/errors/maddegen-art-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/maddegen-art-problem-types.yml
- group: design
  href: https://artifacts.apis.io/maddegen-art/conformance/maddegen-art-conformance.yml
  title: ''
  type: Conformance
  url: conformance/maddegen-art-conformance.yml
- group: agent
  href: https://artifacts.apis.io/maddegen-art/llms/maddegen-art-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/maddegen-art-llms.txt
- group: other
  href: https://artifacts.apis.io/maddegen-art/a2a/maddegen-art-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/maddegen-art-a2a.yml
- group: agent
  href: https://artifacts.apis.io/maddegen-art/well-known/maddegen-art-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/maddegen-art-well-known.yml
- group: other
  href: https://artifacts.apis.io/maddegen-art/hosts/maddegen-art-hosts.yml
  title: ''
  type: Hosts
  url: hosts/maddegen-art-hosts.yml
- group: docs
  title: ''
  type: Documentation
  url: https://maddegen.art/guides/
- group: auth
  href: https://artifacts.apis.io/maddegen-art/security/maddegen-art-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/maddegen-art-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://maddegen.art/
created: '2026-10-29'
description: 'maddegen-art is a company surfaced via the API Evangelist harvest backlog (source: mcp-registry) and added to the network as a stub for full-pipeline profiling.'
image: https://augur-trade.com/og/home.jpg?v=445606f9d5
layout: provider
modified: '2026-10-29'
name: maddegen-art
nav: Providers
network: true
overview: 'maddegen-art publishes 1 API contract indexed on the [APIs.io](https://apis.io/) network: Pump Cortex API. Tagged areas include Company.


  The maddegen-art catalog on APIs.io includes 1 Spectral governance ruleset.


  maddegen-art''s developer surface includes authentication, documentation, and 12 more developer resources.'
random_paper: 17
rules:
- authorship: generated
  effective_rule_count: 53
  extends:
  - spectral:oas
  name: maddegen-art API Rules
  rule_count: 12
  severity_counts:
    error: 10
    hint: 0
    info: 1
    warn: 1
  slug: maddegen-art-rules
scopes:
- name: Maddegen Art Scopes
  scope_count: 0
  slug: maddegen-art-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: thin
  composite: 27.0
  coverage:
    artifact_dirs: 24
    catalog_earned: 32.8
    catalog_earned_first_party: 0.0
    catalog_gap: 82.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 0.0
    contract_governance: 22.0
    contract_quality: 49.0
    developer_ergonomics: 27.9
    discoverability: 48.2
    operational_transparency: 0.0
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 11
    mcp: derived
    skills: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 26.5
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Maddegen Art Authentication
  slug: maddegen-art-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Maddegen Art Domain Security
  slug: maddegen-art-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
skill_count: 4
skills:
- name: pump-history
  slug: pump-history
- name: pump-launches
  slug: pump-launches
- name: pump-pulse
  slug: pump-pulse
- name: pump-token
  slug: pump-token
slug: maddegen-art
tags:
- Company
website: https://maddegen.art/
---
