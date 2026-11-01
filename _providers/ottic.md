---
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: conformant
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: paginated
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 51.9
  scored_at: '2026-10-31'
api_count: 1
apis:
- description: API for Ottic platform providing AI agent capabilities. Documentation at the API Reference page.
  name: Ottic API
  slug: ottic-api
artifact_total: 4
common:
- group: design
  href: https://artifacts.apis.io/ottic/rules/ottic-rules.yml
  title: ''
  type: Spectral
  url: rules/ottic-rules.yml
- group: design
  href: https://artifacts.apis.io/ottic/json-ld/ottic-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/ottic-context.jsonld
- group: design
  href: https://artifacts.apis.io/ottic/vocabulary/ottic-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/ottic-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/ottic/data-model/ottic-data-model.yml
  title: ''
  type: DataModel
  url: data-model/ottic-data-model.yml
- group: design
  href: https://artifacts.apis.io/ottic/errors/ottic-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/ottic-problem-types.yml
- group: design
  href: https://artifacts.apis.io/ottic/conformance/ottic-conformance.yml
  title: ''
  type: Conformance
  url: conformance/ottic-conformance.yml
- group: agent
  href: https://artifacts.apis.io/ottic/llms/ottic-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/ottic-llms.txt
- group: other
  href: https://artifacts.apis.io/ottic/a2a/ottic-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/ottic-a2a.yml
- group: agent
  href: https://artifacts.apis.io/ottic/well-known/ottic-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/ottic-well-known.yml
- group: other
  href: https://artifacts.apis.io/ottic/hosts/ottic-hosts.yml
  title: ''
  type: Hosts
  url: hosts/ottic-hosts.yml
- group: build
  href: https://artifacts.apis.io/ottic/packages/ottic-packages.yml
  title: ''
  type: SDKs
  url: packages/ottic-packages.yml
- group: build
  href: https://artifacts.apis.io/ottic/packages/ottic-packages.yml
  title: ''
  type: Packages
  url: packages/ottic-packages.yml
- group: auth
  href: https://artifacts.apis.io/ottic/security/ottic-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/ottic-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://ottic.ai/
- group: docs
  title: ''
  type: Documentation
  url: https://ottic.ai/docs/
- group: docs
  title: ''
  type: APIReference
  url: https://ottic.ai/docs/llms.txt
- group: start
  title: ''
  type: GettingStarted
  url: https://ottic.ai/docs/basics/giving-your-agent-context/
coverage:
  checked: '2026-10-21'
  detail: Documentation is served as a JavaScript shell, preventing machine‑readable contract extraction.
  evidence:
  - status: 200
    url: https://docs.ottic.ai/api-reference/openapi.json
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-21'
description: Ottic provides an AI agent platform that automates busywork by researching, coding, browsing the web, and delivering results. It offers a cloud sandbox with a real terminal and browser, enabling integrations, custom connectors, and reusable skills. Users can define goals in plain language, and the agent executes end‑to‑end workflows, handling data extraction, analysis, and deliverable generation. Ottic aims to turn AI from a chat assistant into a productive work partner, supporting teams with collaborative tools, automation routines, and secure artifact sharing.
image: https://ottic.ai/og-image.png
jsonld:
- class_count: 2
  name: Ottic Context
  property_count: 4
  slug: ottic-context
layout: provider
modified: '2026-10-21'
name: Ottic
nav: Providers
network: true
overview: 'Ottic publishes 1 API contract indexed on the [APIs.io](https://apis.io/) network. Tagged areas include Artificial Intelligence, Automation, Productivity, Agents, and Platform.


  The Ottic catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Ottic''s developer surface includes documentation, API reference, getting-started guide, and 14 more developer resources.'
random_paper: 19
rules:
- authorship: generated
  effective_rule_count: 53
  extends:
  - spectral:oas
  name: Ottic API Rules
  rule_count: 12
  severity_counts:
    error: 10
    hint: 0
    info: 1
    warn: 1
  slug: ottic-rules
score:
  band: thin
  composite: 29.2
  coverage:
    artifact_dirs: 16
    catalog_earned: 42.8
    catalog_earned_first_party: 0.0
    catalog_gap: 72.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 0.0
    contract_governance: 35.6
    contract_quality: 48.1
    developer_ergonomics: 35.7
    discoverability: 57.1
    operational_transparency: 0.0
  provenance:
    conformance: first-party
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 1
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 15.5
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Ottic Domain Security
  slug: ottic-domain-security
  summary_line: TLSv1.3 · DMARC
slug: ottic
tags:
- Artificial Intelligence
- Automation
- Productivity
- Agents
- Platform
website: https://ottic.ai/
---
