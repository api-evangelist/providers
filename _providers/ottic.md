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
  band: human-only
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
    well_known_catalog: false
  schema_version: '0.2'
  score: 0.7
  scored_at: '2026-11-06'
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
  effective_rule_count: 77
  extends:
  - spectral:oas
  name: Ottic API Rules
  rule_count: 36
  severity_counts:
    error: 34
    hint: 0
    info: 1
    warn: 1
  slug: ottic-rules
score:
  band: emerging
  composite: 15.2
  coverage:
    artifact_dirs: 18
    catalog_earned: 42.8
    catalog_earned_first_party: 0.0
    catalog_gap: 72.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -5.9
  facets:
    access_clarity: 0.0
    contract_governance: 35.6
    contract_quality: 6.7
    developer_ergonomics: 21.4
    discoverability: 64.3
    operational_transparency: 0.0
  previous_composite: 21.1
  provenance:
    conformance: first-party
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 10.0
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/ottic/ottic-2026-11-03T140818.png
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
