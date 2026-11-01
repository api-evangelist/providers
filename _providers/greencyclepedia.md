---
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
    mcp_server: documented
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 15.6
  scored_at: '2026-10-31'
api_count: 1
apis:
- description: 'GreenCycle Compound Atlas API as documented publicly: 3 operations. Contract generated from the documentation by API Evangelist (2026-10-24); not the provider''s own document.'
  name: GreenCycle Compound Atlas API
  slug: greencyclepedia-api
artifact_total: 4
common:
- group: design
  href: https://artifacts.apis.io/greencyclepedia/rules/greencyclepedia-rules.yml
  title: ''
  type: Spectral
  url: rules/greencyclepedia-rules.yml
- group: design
  href: https://artifacts.apis.io/greencyclepedia/vocabulary/greencyclepedia-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/greencyclepedia-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/greencyclepedia/conformance/greencyclepedia-conformance.yml
  title: ''
  type: Conformance
  url: conformance/greencyclepedia-conformance.yml
- group: agent
  href: https://artifacts.apis.io/greencyclepedia/llms/greencyclepedia-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/greencyclepedia-llms.txt
- group: agent
  href: https://artifacts.apis.io/greencyclepedia/mcp/greencyclepedia-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/greencyclepedia-mcp.yml
- group: agent
  href: https://artifacts.apis.io/greencyclepedia/well-known/greencyclepedia-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/greencyclepedia-well-known.yml
- group: other
  href: https://artifacts.apis.io/greencyclepedia/hosts/greencyclepedia-hosts.yml
  title: ''
  type: Hosts
  url: hosts/greencyclepedia-hosts.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://greencyclepedia.com/about/terms/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://greencyclepedia.com/about/privacy/
- group: company
  title: ''
  type: Newsroom
  url: https://greencyclepedia.com/news/
- group: operate
  title: ''
  type: ChangeLog
  url: https://greencyclepedia.com/release-notes/
- group: docs
  title: ''
  type: APIReference
  url: https://greencyclepedia.com/llms.txt
- group: auth
  href: https://artifacts.apis.io/greencyclepedia/security/greencyclepedia-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/greencyclepedia-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://greencyclepedia.com
created: '2026-10-24'
description: GreenCycle Compound Atlas offers an open, community‑curated atlas of cannabis compounds, their receptors, associated medical conditions, and related data. The platform aggregates verified scientific sources and provides JSON endpoints for compounds, targets, structures, conditions, and more, all licensed under CC BY 4.0. It supports researchers, developers, and the public by delivering reliable, machine‑readable cannabis information, complete with source citations and licensing details, enabling integration into applications and AI agents.
image: https://greencyclepedia.com/assets/og-storybook.png
layout: provider
mcp_servers:
- description: Remote MCP server at greencyclepedia.com.
  name: GreenCycle Compound Atlas MCP Server
  slug: greencyclepedia-mcp-yml
modified: '2026-10-24'
name: GreenCycle Compound Atlas
nav: Providers
network: true
overview: 'GreenCycle Compound Atlas is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Cannabis, Anatomy Atlas, and Educational Reference.


  The GreenCycle Compound Atlas catalog on APIs.io includes 1 Spectral governance ruleset.


  GreenCycle Compound Atlas'' developer surface includes changelog, API reference, and 12 more developer resources.'
random_paper: 12
rules:
- authorship: generated
  effective_rule_count: 49
  extends:
  - spectral:oas
  name: GreenCycle Compound Atlas API Rules
  rule_count: 8
  severity_counts:
    error: 6
    hint: 0
    info: 1
    warn: 1
  slug: greencyclepedia-rules
score:
  band: emerging
  composite: 18.2
  coverage:
    artifact_dirs: 11
    catalog_earned: 32.8
    catalog_earned_first_party: 0.0
    catalog_gap: 82.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 21.1
    contract_governance: 22.0
    contract_quality: 9.4
    developer_ergonomics: 7.1
    discoverability: 50.0
    operational_transparency: 15.8
  provenance:
    conformance: derived
    contracts:
      callable: 0.0
      derived: 4
      marker_coverage: 100.0
      total: 4
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 18.6
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Greencyclepedia Domain Security
  slug: greencyclepedia-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: greencyclepedia
tags:
- Cannabis
- Anatomy Atlas
- Educational Reference
website: https://greencyclepedia.com
---
